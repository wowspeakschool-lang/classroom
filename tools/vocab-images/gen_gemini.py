"""Картинки к словам тренажёра через Gemini — по одной на слово, без листов и нарезки.

Описания берутся из файлов промптов docs/Тренажёр_*_промпты_*.md: каждый пункт
«N. term — описание» внутри блока «ИЗОБРАЖЕНИЕ K» с общей строкой про персонажа.

  python3 gen_gemini.py --list                 что будет нарисовано
  python3 gen_gemini.py --only camp_under_the_stars climb_a_tree
  python3 gen_gemini.py --sheet 1.1            один лист партии 1
  python3 gen_gemini.py                        всё, чего ещё нет
  python3 gen_gemini.py --force --only toe     перерисовать

Ключ — GEMINI_API_KEY. Модель — GEMINI_IMAGE_MODEL, по умолчанию gemini-2.5-flash-image.
Выход: out/<партия>.<лист>/<term>.png (300×300 RGBA, как у нарезки) и raw/ с исходником.
В листах со сквозным персонажем первая готовая картинка листа уходит образцом
во все следующие — иначе персонаж меняется от картинки к картинке.
"""
import argparse, base64, glob, io, json, os, re, sys, time, urllib.parse, urllib.request, urllib.error
import numpy as np
from PIL import Image
from lib import fname, make_soft_transparent, to_square

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(HERE, '..', '..', 'docs')
MODEL = os.environ.get('GEMINI_IMAGE_MODEL', 'gemini-2.5-flash-image')
URL = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent'

STYLE = """Hand-drawn children's storybook illustration style. Every object has a bold dark brown or black outline
of even thickness. Colours are rich and saturated, filled with soft internal shading and highlights that
give the object volume. Textures are drawn by hand: fur strokes, leaf veins, wood grain, fabric folds.
Friendly rounded cartoon shapes, warm palette.
NOT flat vector icons. NOT minimalist icon style. NOT clip-art. NOT sharp geometric shapes.
NOT plain single-colour fills without shading. Keep the level of hand-drawn detail of a printed picture dictionary."""

# Листы, где сквозной персонаж есть не во всех клетках: номера клеток с ним.
CHARACTER_CELLS = {'1.4': range(4, 11), '4.2': (1, 2, 3, 4, 5, 6, 9, 10), '5.2': (1, 3, 4, 5, 6, 7)}

RULES = """ONE single illustration, centred, for a children's picture dictionary card.
Pure white background (#FFFFFF), uniform, no textures, no gradients, no ground shadow patch.
Leave a clean white margin of at least 8% on every side: nothing touches or is cut by the edge of the image.
No caption, no word under the picture, no frame, no border, no speech bubbles, no watermark, no emoji,
no readable text or logos inside the drawing — except letters or symbols explicitly named in the description."""


def parse_prompts():
    """[(batch, sheet, term, desc, note)] из всех файлов промптов по порядку партий."""
    items = []
    for path in sorted(glob.glob(os.path.join(DOCS, 'Тренажёр_*_промпты_*.md'))):
        text = open(path, encoding='utf-8').read()
        for bm in re.finditer(r'^## Партия (\d+).*?\n```\n(.*?)\n```', text, re.S | re.M):
            batch, body = int(bm.group(1)), bm.group(2)
            for sm in re.finditer(r'^ИЗОБРАЖЕНИЕ (\d+) — .*?\n(.*?)(?=^--ar)', body, re.S | re.M):
                sheet, block = int(sm.group(1)), sm.group(2)
                lines = block.split('\n')
                first = next(i for i, l in enumerate(lines) if re.match(r'^1\. ', l))
                note = ' '.join(l.strip() for l in lines[1:first] if l.strip())  # [0] — сетка
                for l in lines[first:]:
                    m = re.match(r'^(\d+)\. (.+?) — (.+)$', l)
                    if m:
                        items.append(dict(batch=batch, sheet=sheet, n=int(m.group(1)),
                                          term=m.group(2), desc=m.group(3), note=note))
    return items


def prompt_for(it, has_ref):
    ref = ('\nThe attached image is the reference: draw EXACTLY the same character — same face, hair, '
           'clothes and colours — only the action changes.' if has_ref else '')
    return (f"{STYLE}\n\n{RULES}\n\nWord: \"{it['term']}\".\n"
            f"Что нарисовать: {it['desc']}.\n"
            f"Общее для этой серии картинок: {it['note']}{ref}")


# Pollinations (Flux) плохо понимает русский — для него описания по-английски.
# Пока переведён только пробный лист 1.1; для остальных листов добавить сюда.
EN_NOTE = {'1.1': 'The same girl in every picture: 12 years old, red hair in a ponytail, yellow windbreaker, '
                  'dark blue trousers, green hiking boots. Only a small piece of nature around her, not a full landscape.'}
EN = {
 'camp under the stars': 'she lies in a sleeping bag on the grass next to a small tent, looking up; above her a small oval patch of night sky with stars and a moon, only around the scene',
 'climb a tree': 'she climbs along a thick branch of a big leafy tree, holding on with hands and legs',
 'explore a cave': 'wearing a head torch she looks into the dark entrance of a cave in a rock, a beam of light goes inside',
 'kayak down a river': 'she sits in a red kayak with a double-bladed paddle, riding a river with white foamy rapids',
 'look for fossils': 'she crouches by a flat stone holding a magnifying glass and a brush; an ammonite shell fossil imprint in the stone',
 'pick wild fruit': 'she picks blackberries from a thorny bush into a wicker basket',
 'play in the snow': 'in a hat and scarf she builds a snowman, snowdrifts around, snow under her feet',
 'record birdsong': 'she holds a small voice recorder with a microphone towards a little bird singing on a branch; musical notes come from its beak',
 'track wild animals': 'she kneels with a magnifying glass over a line of paw prints in mud; the prints lead to a fox peeking out from behind a bush',
 'try rock climbing': 'in a helmet and climbing harness she climbs a steep rock wall with colourful holds, a rope hangs from above',
}


def call_pollinations(it, seed, tries=4):
    key = f"{it['batch']}.{it['sheet']}"
    if it['term'] not in EN:
        raise RuntimeError('нет английского описания в EN — добавить')
    prompt = (f"Children's picture dictionary illustration of \"{it['term']}\": {EN[it['term']]}. "
              f"{EN_NOTE.get(key, '')} Hand-drawn storybook style, bold dark brown outlines of even thickness, "
              "rich saturated colours with soft shading and volume, hand-drawn textures, friendly rounded cartoon shapes. "
              "Single centred illustration on a pure white background, wide white margin on every side, "
              "nothing cut by the edge. No text, no letters, no caption, no frame, no border.")
    q = urllib.parse.urlencode({'width': 1024, 'height': 1024, 'model': 'flux', 'nologo': 'true',
                                'seed': seed, 'enhance': 'false'})
    url = 'https://image.pollinations.ai/prompt/' + urllib.parse.quote(prompt) + '?' + q
    for a in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=240) as r:
                data = r.read()
            im = Image.open(io.BytesIO(data)); b = io.BytesIO(); im.convert('RGB').save(b, 'PNG')
            return b.getvalue()
        except Exception as e:
            if a == tries - 1:
                raise
            print(f'    {e}, повтор'); time.sleep(15 * (a + 1))


def call(prompt, ref_png=None, tries=4):
    key = os.environ.get('GEMINI_API_KEY')
    if not key:
        sys.exit('нет GEMINI_API_KEY')
    parts = [{'text': prompt}]
    if ref_png:
        parts.append({'inline_data': {'mime_type': 'image/png',
                                      'data': base64.b64encode(ref_png).decode()}})
    body = json.dumps({'contents': [{'parts': parts}],
                       'generationConfig': {'responseModalities': ['IMAGE'],
                                            'imageConfig': {'aspectRatio': '1:1'}}}).encode()
    for a in range(tries):
        req = urllib.request.Request(URL, body, {'Content-Type': 'application/json',
                                                 'x-goog-api-key': key})
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                data = json.load(r)
            for p in data['candidates'][0]['content']['parts']:
                blob = p.get('inlineData') or p.get('inline_data')
                if blob:
                    return base64.b64decode(blob['data'])
            raise RuntimeError('в ответе нет картинки: ' + json.dumps(data)[:400])
        except urllib.error.HTTPError as e:
            msg = e.read().decode()[:600]
            if e.code in (429, 500, 503) and a < tries - 1:
                wait = 20 * (a + 1)
                print(f'    {e.code}, жду {wait} с'); time.sleep(wait); continue
            raise RuntimeError(f'HTTP {e.code}: {msg}')


def finish(png_bytes):
    """Исходник → вырезанный фон, обрезка по предмету, 300×300 как у нарезки листов."""
    im = Image.open(io.BytesIO(png_bytes)).convert('RGB')
    rgba = make_soft_transparent(im)
    a = np.array(rgba)[..., 3]
    ys, xs = np.where(a > 8)
    if len(xs):
        rgba = rgba.crop((max(0, xs.min() - 6), max(0, ys.min() - 6),
                          min(a.shape[1], xs.max() + 7), min(a.shape[0], ys.max() + 7)))
    return to_square(rgba)


def edge_ink(png_bytes):
    """Доля не-белых пикселей по краям: >0 значит, рисунок упёрся в край."""
    m = np.array(Image.open(io.BytesIO(png_bytes)).convert('L')) < 235
    return max(m[:4].mean(), m[-4:].mean(), m[:, :4].mean(), m[:, -4:].mean())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--only', nargs='*', help='имена файлов без .png, как в fname()')
    ap.add_argument('--sheet', nargs='*', help='партия.лист, например 1.1')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--out', default=os.path.join(HERE, 'out'))
    ap.add_argument('--engine', choices=['gemini', 'pollinations'], default='gemini')
    ap.add_argument('--seed', type=int, default=42, help='pollinations: один seed на лист держит стиль ровнее')
    args = ap.parse_args()

    items = items_all = parse_prompts()
    if args.sheet:
        items = [i for i in items if f"{i['batch']}.{i['sheet']}" in args.sheet]
    if args.only:
        items = [i for i in items if fname(i['term'])[:-4] in args.only]
    if args.list:
        for i in items:
            print(f"{i['batch']}.{i['sheet']}.{i['n']:<3} {i['term']}")
        print(len(items), 'картинок')
        return

    for it in items:
        sd = os.path.join(args.out, f"{it['batch']}.{it['sheet']}")
        rd = os.path.join(sd, 'raw')
        os.makedirs(rd, exist_ok=True)
        dst = os.path.join(sd, fname(it['term']))
        if os.path.exists(dst) and not args.force:
            continue
        key = f"{it['batch']}.{it['sheet']}"
        cells = CHARACTER_CELLS.get(key)
        same = 'один и тот же' in it['note'] and (cells is None or it['n'] in cells)
        ref = None
        if same:
            mates = {fname(i['term']) for i in items_all
                     if f"{i['batch']}.{i['sheet']}" == key and i['term'] != it['term']
                     and (cells is None or i['n'] in cells)}
            raws = sorted(glob.glob(os.path.join(rd, '*.png')), key=os.path.getmtime)
            raws = [r for r in raws if os.path.basename(r) in mates]
            if raws:
                ref = open(raws[0], 'rb').read()
        print(f"{it['batch']}.{it['sheet']}.{it['n']} {it['term']}" + (' (по образцу)' if ref else ''))
        try:
            raw = (call_pollinations(it, args.seed) if args.engine == 'pollinations'
                   else call(prompt_for(it, bool(ref)), ref))
        except Exception as e:
            print('   ОШИБКА', e); continue
        open(os.path.join(rd, fname(it['term'])), 'wb').write(raw)
        finish(raw).save(dst)
        e = edge_ink(raw)
        if e > 0.01:
            print(f'   ! рисунок у края ({e:.1%}) — проверить обрезку')


if __name__ == '__main__':
    main()
