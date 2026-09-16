#!/usr/bin/env python3
"""Вставляет присланные картинки в урок вместо старых.

Картинки Анна генерирует по docs/WowSpeak_промпты_урок1.md и кладёт в
assets/lesson-N/ под именами из таблицы (cap.png, tshirt.png и так далее).

Скрипт сам:
  * вырезает белый фон, если картинка пришла не с прозрачным,
  * обрезает пустые поля и центрирует предмет в квадрате,
  * ужимает в WebP нужного размера,
  * заменяет запись в объекте картинок урока.

Запуск: python3 tools/embed_lesson_images.py 1
"""
import base64, io, os, re, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIZE = 420        # в задании картинка показывается максимум ~200 px, берём с запасом
WHITE_CUT = 238   # всё светлее этого по краям считаем фоном


def cut_white(im):
    """Убирает белый фон, если он есть: заливка от краёв, чтобы не выесть белое внутри."""
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    corners = [px[0, 0], px[w - 1, 0], px[0, h - 1], px[w - 1, h - 1]]
    if not all(c[0] > WHITE_CUT and c[1] > WHITE_CUT and c[2] > WHITE_CUT for c in corners):
        return im          # фон уже прозрачный или цветной — не трогаем
    seen = set()
    stack = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]
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


def to_square(im):
    box = im.getbbox()
    if box:
        im = im.crop(box)
    side = int(max(im.size) * 1.08)          # небольшие поля вокруг предмета
    sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    sq.paste(im, ((side - im.width) // 2, (side - im.height) // 2))
    return sq.resize((SIZE, SIZE), Image.LANCZOS)


def uri(path):
    im = to_square(cut_white(Image.open(path)))
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=88, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode(), len(buf.getvalue())


def main(n):
    src_dir = os.path.join(ROOT, "assets", "lesson-%d" % n)
    path = os.path.join(ROOT, "lessons", "wowspeak-mini", "lesson-%d.html" % n)
    if not os.path.isdir(src_dir):
        sys.exit("нет папки %s — положите туда картинки" % src_dir)
    s = open(path, encoding="utf-8").read()
    done, skipped = [], []
    for f in sorted(os.listdir(src_dir)):
        key, ext = os.path.splitext(f)
        if ext.lower() not in (".png", ".jpg", ".jpeg", ".webp"):
            continue
        data, size = uri(os.path.join(src_dir, f))
        pat = re.compile(r'(\b%s\s*:\s*)"data:image/[a-z]+;base64,[^"]+"' % re.escape(key))
        if not pat.search(s):
            skipped.append(key)
            continue
        s = pat.sub(lambda m: m.group(1) + '"' + data + '"', s, count=1)
        done.append("%s (%.0f КБ)" % (key, size / 1024))
    open(path, "w", encoding="utf-8").write(s)
    print("вставлено:", ", ".join(done) if done else "ничего")
    if skipped:
        print("НЕ НАЙДЕНЫ в уроке (проверьте имя файла):", ", ".join(skipped))
    print("урок %d: %.1f МБ" % (n, os.path.getsize(path) / 1048576))


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
