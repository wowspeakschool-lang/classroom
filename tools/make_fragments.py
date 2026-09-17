#!/usr/bin/env python3
"""Нарезает «кусочки одежды» для угадайки из наших же картинок.

В уроках 2-4 есть задание «что это за вещь по кусочку»: увеличенный фрагмент
предмета. Генерировать их отдельно не нужно и вредно — цвета разъезжались бы
с основными картинками (в старой версии кепка на кусочке была красной, а в уроке
фиолетовой). Режем из assets/lesson-1/.

Координаты — доли холста исходной картинки (предмет в нём отцентрован).
Белый фон срезается до нарезки и по всей картинке: из обрезка заливка от краёв
до белых «карманов» между предметом и краем не доходит, и они остаются белыми
пятнами на сиреневой плашке задания. Доли при этом считаются от холста, а не от
рамки предмета, — иначе после срезания фона они разъехались бы.
"""
import base64, io, os, re, sys
from PIL import Image

WHITE_CUT = 238   # всё светлее этого по краям кусочка считаем фоном

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets", "lesson-1")
LESSONS = os.path.join(ROOT, "lessons", "wowspeak-mini")

# ключ: (файл, доля по X слева, доля сверху, доля по X справа, доля снизу, ширина итога, высота итога)
CROPS = {
    "frag_cap":    ("cap",    0.05, 0.45, 0.95, 0.85,  520, 172),   # козырёк
    "frag_tshirt": ("tshirt", 0.02, 0.05, 0.42, 0.52,  520, 424),   # плечо и рукав
    "frag_jeans":  ("jeans",  0.05, 0.60, 0.95, 1.00,  520, 370),   # низ штанин с отворотами
    "frag_skirt":  ("skirt",  0.05, 0.60, 0.95, 0.95,  520, 200),   # подол
    "frag_jacket": ("jacket", 0.25, 0.02, 0.78, 0.40,  520, 204),   # воротник и молния
    "frag_shoes":  ("shoes",  0.02, 0.35, 0.70, 0.95,  520, 324),   # носы ботинок
    "frag_socks":  ("socks",  0.08, 0.02, 0.92, 0.38,  520, 242),   # резинка сверху
}


def cut_white(im):
    """Убирает белый фон заливкой от краёв — внутри предмета белое не трогается."""
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    stack = [(x, y) for x in range(w) for y in (0, h - 1)]
    stack += [(x, y) for y in range(h) for x in (0, w - 1)]
    seen = set()
    while stack:
        x, y = stack.pop()
        if (x, y) in seen or not (0 <= x < w and 0 <= y < h):
            continue
        r, g, b, a = px[x, y]
        if not (r > WHITE_CUT and g > WHITE_CUT and b > WHITE_CUT and a > 0):
            continue
        seen.add((x, y))
        px[x, y] = (r, g, b, 0)
        stack += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return im


def crop(key):
    name, x0, y0, x1, y1, w, h = CROPS[key]
    im = Image.open(os.path.join(SRC, name + ".webp")).convert("RGBA")
    bw, bh = im.size
    box = (bw * x0, bh * y0, bw * x1, bh * y1)
    part = cut_white(im).crop(tuple(int(v) for v in box))
    part = part.crop(part.getbbox() or (0, 0, part.width, part.height))
    # вписываем в нужные пропорции, добираем прозрачностью, если не сходится
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    part.thumbnail((w, h), Image.LANCZOS)
    out.alpha_composite(part, ((w - part.width) // 2, (h - part.height) // 2))
    return out


def uri(im):
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=88, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode(), len(buf.getvalue())


def main(preview=False):
    made = {}
    for key in CROPS:
        im = crop(key)
        if preview:
            os.makedirs("/tmp/frag", exist_ok=True)
            im.save("/tmp/frag/%s.png" % key)
        made[key] = uri(im)
    if preview:
        print("превью в /tmp/frag/")
        return
    for n in (2, 3, 4):
        path = os.path.join(LESSONS, "lesson-%d.html" % n)
        s = open(path, encoding="utf-8").read()
        done = 0
        for key, (data, size) in made.items():
            pat = re.compile(r'(\b%s\s*:\s*)"data:image/[a-z]+;base64,[^"]+"' % key)
            if pat.search(s):
                s = pat.sub(lambda m: m.group(1) + '"' + data + '"', s, count=1)
                done += 1
        open(path, "w", encoding="utf-8").write(s)
        print("Урок %d: кусочков заменено %d, файл %.1f МБ"
              % (n, done, os.path.getsize(path) / 1048576))


if __name__ == "__main__":
    main("--preview" in sys.argv)
