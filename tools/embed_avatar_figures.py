#!/usr/bin/env python3
"""Вставляет объёмные фигурки в одевалку Урока 4 и переводит её на целые картинки.

Раньше фигурка собиралась из семи плоских слоёв. Объёмные слои не сводятся —
генератор не повторяет позу пиксель в пиксель, — поэтому рисуем восемь готовых
сочетаний на каждый пол (tools/gen_avatar_figures.py) и показываем одну картинку.

Скрипт:
  * чистит картинку от мусорных пятен (оставляет самую большую связную область),
  * режет все восемь картинок пола одним общим окном, чтобы фигурка не прыгала
    при переключении стрелками,
  * кладёт их в урок ключами fig_<пол>_<кепка><куртка><шорты>,
  * переписывает makeZoneFigure на одну картинку, кнопки выбора пола и фигурку
    на экране проекта (там теперь виден собранный аватар, а не общая картинка),
  * правит размер рамки под новое соотношение сторон.

Переприменяемый: и картинки, и куски кода заменяются целиком по месту.
Запуск: python3 tools/embed_avatar_figures.py
"""
import base64, io, os, re, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets", "lesson-4")
LESSON = os.path.join(ROOT, "lessons", "wowspeak-mini", "lesson-4.html")
CODES = ["000", "001", "010", "011", "100", "101", "110", "111"]
HEIGHT = 700          # показывается ~360 px, берём с запасом под retina
MARGIN = 0.02


def clean(path):
    """Убирает мусорные пятна: оставляем самую большую связную область альфы."""
    im = Image.open(path).convert("RGBA")
    w, h = im.size
    step = 4
    sw, sh = w // step, h // step
    small = im.getchannel("A").resize((sw, sh), Image.BILINEAR).point(lambda v: 1 if v > 40 else 0)
    px = small.load()
    best, seen = set(), set()
    for sy in range(sh):
        for sx in range(sw):
            if not px[sx, sy] or (sx, sy) in seen:
                continue
            comp, stack = set(), [(sx, sy)]
            while stack:
                x, y = stack.pop()
                if (x, y) in seen or not (0 <= x < sw and 0 <= y < sh) or not px[x, y]:
                    continue
                seen.add((x, y)); comp.add((x, y))
                stack += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            if len(comp) > len(best):
                best = comp
    mask = Image.new("L", (sw, sh), 0)
    mp = mask.load()
    for x, y in best:
        mp[x, y] = 255
    big = mask.resize((w, h), Image.BILINEAR).point(lambda v: 255 if v > 24 else 0)
    alpha = im.getchannel("A")
    im.putalpha(Image.composite(alpha, Image.new("L", (w, h), 0), big))
    return im


def tight_box(im, need=5):
    a = im.getchannel("A").point(lambda v: 255 if v > 40 else 0)
    w, h = a.size
    p = a.load()
    cols = [x for x in range(w) if sum(1 for y in range(0, h, 2) if p[x, y]) >= need]
    rows = [y for y in range(h) if sum(1 for x in range(0, w, 2) if p[x, y]) >= need]
    return (cols[0], rows[0], cols[-1] + 1, rows[-1] + 1)


def build(gender):
    cleaned, boxes = {}, []
    for code in CODES:
        im = clean(os.path.join(SRC, "fig_%s_%s.webp" % (gender, code)))
        cleaned[code] = im
        boxes.append(tight_box(im))
    x0 = min(b[0] for b in boxes); y0 = min(b[1] for b in boxes)
    x1 = max(b[2] for b in boxes); y1 = max(b[3] for b in boxes)
    mx = int((x1 - x0) * MARGIN); my = int((y1 - y0) * MARGIN)
    W, H = cleaned[CODES[0]].size
    box = (max(0, x0 - mx), max(0, y0 - my), min(W, x1 + mx), min(H, y1 + my))
    out = {}
    for code, im in cleaned.items():
        part = im.crop(box)
        part = part.resize((max(1, round(part.width * HEIGHT / part.height)), HEIGHT), Image.LANCZOS)
        buf = io.BytesIO()
        part.save(buf, "WEBP", quality=86, method=6)
        out[code] = ("data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode(),
                     part.size, len(buf.getvalue()))
    return out


# ── куски кода урока ──────────────────────────────────────────────────────────
FIGURE_FN = '''function avatarCode(){
  const z = zoneState();
  return "" + (z.head|0) + (z.torso|0) + (z.legs|0);
}
function avatarFigureSrc(){
  const g = (state.avatarGender === "girl") ? "girl" : "boy";
  return IMG["fig_" + g + "_" + avatarCode()];
}
function makeZoneFigure(){
  const box = el("div", { class:"zfig-box" });
  const fig = el("img", { class:"zlayer", src:avatarFigureSrc(), draggable:"false", alt:"аватар" });
  box.appendChild(fig);
  function update(){ fig.src = avatarFigureSrc(); }
  update();
  return { box:box, update:update };
}'''


ZONE_DEF = '''const ZONE = {
  head:  { label:"HEAD",    variants:[ {name:"No cap"}, {name:"Cap"} ] },
  torso: { label:"CLOTHES", variants:[ {name:"T-shirt"}, {name:"T-shirt + jacket"} ] },
  legs:  { label:"LEGS",    variants:[ {name:"Jeans"}, {name:"Shorts + socks"} ] }
};'''


MODEL_LINES = '''    const EN_NAME = { cap:"a cap", tshirt:"a T-shirt", jacket:"a jacket",
                      jeans:"jeans", shoes:"shoes", socks:"socks", skirt:"a skirt" };
    const worn = zoneItems();
    const missing = ["a cap","a jacket","jeans","a skirt"].filter(function(n){
      return worn.map(function(k){ return EN_NAME[k]; }).indexOf(n) < 0; })[0] || "a skirt";
    const modelLines = [P + " has got a T-shirt.", P + " hasn't got " + missing + "."];'''


def patch_code(s, ratio):
    # образец на экране проекта больше не может говорить «hasn't got a cap»,
    # когда на фигурке кепка: теперь там виден собранный аватар
    s = re.sub(r'    const modelLines = \(g === "girl"\)\n.*?\n.*?\n', MODEL_LINES + "\n",
               s, count=1)
    # в вариантах остались имена слоёв — они больше не нужны, а пока они в файле,
    # prune_dead_images считает слои живыми и не выкидывает их
    s = re.sub(r'const ZONE = \{.*?\n\};', ZONE_DEF, s, count=1, flags=re.S)
    # сама фигурка
    s = re.sub(r'function makeZoneFigure\(\)\{.*?\n\}', FIGURE_FN, s, count=1, flags=re.S)
    # кнопки выбора пола
    s = s.replace('src:IMG[gp[0]==="boy"?"ava_boy":"ava_girl"]', 'src:IMG["fig_" + gp[0] + "_000"]')
    # фигурка на экране проекта — показываем собранного аватара
    s = s.replace('src:IMG[g === "girl" ? "ava_girl" : "ava_boy"]', 'src:avatarFigureSrc()')
    # рамка под новое соотношение сторон
    s = re.sub(r'\.zfig-box \{[^}]*\}',
               '.zfig-box { position:relative; width:%dpx; height:362px; margin:0 auto; }'
               % round(362 * ratio), s, count=1)
    return s


def main():
    s = open(LESSON, encoding="utf-8").read()
    total = 0
    for gender in ("boy", "girl"):
        made = build(gender)
        for code, (data, size, weight) in made.items():
            key = "fig_%s_%s" % (gender, code)
            pat = re.compile(r'(\b%s\s*:\s*)"data:image/[a-z]+;base64,[^"]+"' % key)
            if pat.search(s):
                s = pat.sub(lambda m: m.group(1) + '"' + data + '"', s, count=1)
            else:   # первый раз — дописываем в объект картинок рядом с аватарами
                s = re.sub(r'(\n(\s*)ava_boy\s*:\s*")',
                           lambda m: '\n%s%s: "%s",%s' % (m.group(2), key, data, m.group(1)),
                           s, count=1)
            total += weight
        print("%s: %d картинок, %dx%d, %.0f КБ"
              % (gender, len(made), made["000"][1][0], made["000"][1][1],
                 sum(w for _, _, w in made.values()) / 1024))
    # рамку берём по самой широкой фигурке — у девочки шире из-за волос,
    # иначе она вписалась бы в узкую рамку и стала мельче мальчика
    ratio = 0
    for key in ("fig_boy_000", "fig_girl_000"):
        m = re.search(r'\b%s\s*:\s*"data:image/[a-z]+;base64,([^"]+)"' % key, s)
        im = Image.open(io.BytesIO(base64.b64decode(m.group(1))))
        ratio = max(ratio, im.width / im.height)
    s = patch_code(s, ratio)
    open(LESSON, "w", encoding="utf-8").write(s)
    print("всего картинок фигурок: %.1f МБ, урок %.1f МБ, рамка %dx362"
          % (total / 1048576, os.path.getsize(LESSON) / 1048576, round(362 * ratio)))


if __name__ == "__main__":
    main()
