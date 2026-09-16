#!/usr/bin/env python3
"""Ставит нового учителя (Хранительницу Слов) во все четыре урока.

Три состояния — neutral / smile / excited — это один и тот же персонаж:
базовый портрет и две его правки (см. tools/gen_teacher.py).

Портрет кладётся на мягкую светлую подложку: учитель показывается в круглой
рамке поверх неба, и на прозрачном фоне волосы и плащ терялись бы на облаках.
"""
import base64, io, os, re
from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets", "teacher")
LESSONS = os.path.join(ROOT, "lessons", "wowspeak-mini")
SIZE = 440          # в уроке кружок максимум 200 px, берём с запасом под retina
FILES = {"neutral": "teacher-neutral.png", "smile": "teacher-smile.png",
         "excited": "teacher-excited.png"}


ZOOM = 0.85   # доля ширины персонажа в кадре: лицо крупное, обруч и плащ ещё видны


def crop_portrait(im):
    """Квадрат по голове и плечам. Исходник поясной, и в круглой рамке урока
    лицо получалось мелким — кадрируем от верха видимой части персонажа."""
    b = im.getbbox()
    side = int((b[2] - b[0]) * ZOOM)
    cx = (b[0] + b[2]) // 2
    left = max(0, min(im.width - side, cx - side // 2))
    top = max(0, b[1] - int(side * 0.04))
    return im.crop((left, top, left + side, min(im.height, top + side)))


def medallion(path):
    im = crop_portrait(Image.open(path).convert("RGBA")).resize((SIZE, SIZE), Image.LANCZOS)
    # подложка: тёплый центр к сиреневому краю, чтобы силуэт читался на любом фоне
    bg = Image.new("RGB", (SIZE, SIZE), (233, 226, 246))
    glow = Image.new("RGB", (SIZE, SIZE), (255, 249, 235))
    mask = Image.new("L", (SIZE, SIZE), 0)
    ImageDraw.Draw(mask).ellipse((-SIZE * 0.15, -SIZE * 0.1, SIZE * 1.15, SIZE * 1.05), fill=255)
    bg.paste(glow, (0, 0), mask.filter(ImageFilter.GaussianBlur(SIZE * 0.22)))
    out = bg.convert("RGBA")
    out.alpha_composite(im)
    buf = io.BytesIO()
    out.convert("RGB").save(buf, "WEBP", quality=86, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode(), len(buf.getvalue())


def main():
    uris = {}
    for key, f in FILES.items():
        uris[key], size = medallion(os.path.join(SRC, f))
        print("%-8s -> %.0f КБ" % (key, size / 1024))

    for n in (1, 2, 3, 4):
        path = os.path.join(LESSONS, "lesson-%d.html" % n)
        s = open(path, encoding="utf-8").read()
        i = s.index("TEACHER_IMG = {")
        end = s.index("};", i)
        block, before, after = s[i:end], s[:i], s[end:]
        changed = 0
        for key, uri in uris.items():
            new_block, cnt = re.subn(r'(\b%s:\s*)"data:image/[a-z]+;base64,[^"]+"' % key,
                                     lambda m: m.group(1) + '"' + uri + '"', block, count=1)
            assert cnt == 1, "в уроке %d не найдено состояние %s" % (n, key)
            block = new_block
            changed += cnt
        open(path, "w", encoding="utf-8").write(before + block + after)
        print("Урок %d: заменено состояний — %d, файл %.1f МБ"
              % (n, changed, os.path.getsize(path) / 1048576))


if __name__ == "__main__":
    main()
