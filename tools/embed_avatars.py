#!/usr/bin/env python3
"""Вставляет восемь детей-аватаров (av1-av8) в Уроки 2, 3 и 4.

Картинки генерирует Анна по docs/WowSpeak_промпты_аватары.md и кладёт
в assets/avatars/ под именами av1.png … av8.png (webp и jpg тоже подойдут).

Скрипт:
  * срезает белый фон заливкой от краёв,
  * ругается, если фигура упирается в край картинки — значит макушку или ступни
    обрезало и картинку надо перегенерировать,
  * приводит всех к одному росту (в заданиях они стоят рядом),
  * кладёт в три урока одним и тем же ключом.

Запуск: python3 tools/embed_avatars.py [--check]
"""
import base64, io, os, re, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets", "avatars")
LESSONS = os.path.join(ROOT, "lessons", "wowspeak-mini")
KEYS = ["av%d" % i for i in range(1, 9)]
HEIGHT = 520          # показывается 240 px, берём с запасом под retina
WHITE_CUT = 238


def find(key):
    for ext in (".png", ".webp", ".jpg", ".jpeg"):
        p = os.path.join(SRC, key + ext)
        if os.path.exists(p):
            return p
    return None


def cut_white(im):
    """Белый фон заливкой от краёв — белое внутри картинки не трогаем."""
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


def prepare(key):
    path = find(key)
    if not path:
        return None, "файла нет"
    im = cut_white(Image.open(path))
    box = im.getbbox()
    if not box:
        return None, "картинка пустая"
    w, h = im.size
    touch = [n for n, hit in (("слева", box[0] == 0), ("сверху", box[1] == 0),
                              ("справа", box[2] == w), ("снизу", box[3] == h)) if hit]
    part = im.crop(box)
    part = part.resize((max(1, round(part.width * HEIGHT / part.height)), HEIGHT), Image.LANCZOS)
    note = "фигура упирается в край (%s) — перегенерировать" % ", ".join(touch) if touch else ""
    return part, note


def main(check_only=False):
    made, bad = {}, []
    for key in KEYS:
        part, note = prepare(key)
        if part is None:
            bad.append("%s: %s" % (key, note))
            continue
        if note:
            bad.append("%s: %s" % (key, note))
        buf = io.BytesIO()
        part.save(buf, "WEBP", quality=88, method=6)
        made[key] = ("data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode(),
                     part.size, len(buf.getvalue()))
        print("%s: %dx%d, %.0f КБ%s" % (key, part.width, part.height,
                                        len(buf.getvalue()) / 1024, "  ⚠ " + note if note else ""))
    if bad:
        print("\nпроблемы:\n  " + "\n  ".join(bad))
    if check_only or len(made) < len(KEYS):
        if not check_only:
            print("\nвставку не делаю: готовы не все восемь картинок")
        return
    for n in (2, 3, 4):
        path = os.path.join(LESSONS, "lesson-%d.html" % n)
        s = open(path, encoding="utf-8").read()
        done = 0
        for key, (data, _, _) in made.items():
            pat = re.compile(r'(\b%s\s*:\s*)"data:image/[a-z]+;base64,[^"]+"' % key)
            if pat.search(s):
                s = pat.sub(lambda m: m.group(1) + '"' + data + '"', s, count=1)
                done += 1
        open(path, "w", encoding="utf-8").write(s)
        print("Урок %d: заменено %d, файл %.1f МБ" % (n, done, os.path.getsize(path) / 1048576))


if __name__ == "__main__":
    main("--check" in sys.argv)
