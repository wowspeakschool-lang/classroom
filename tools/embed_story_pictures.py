#!/usr/bin/env python3
"""Ставит картинки на сюжетные экраны вместо эмодзи.

Экран входа на остров показывал 🎪 / 🪞 / 👫 / 🏰, экран награды — 🔑, хотя
острова уже нарисованы для карты, а ключик рисуется на ней же в замке. Ребёнок
должен узнавать тот самый остров, на который он пришёл с карты.

Вставляются два ключа картинок: `island` (свой остров у каждого урока) и `key`.
Рисовалка сюжетного экрана переводится с текста на picNode — она сама берёт
картинку по таблице EMOJI_KEY и падает обратно на эмодзи, если картинки нет.

Запуск: python3 tools/embed_story_pictures.py
"""
import base64, io, os, re
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(ROOT, "lessons", "wowspeak-mini")
MAP = os.path.join(ROOT, "assets", "map", "web")

ISLAND = {
    1: "island-1-fair.webp",
    2: "island-2-mirrors.webp",
    3: "island-3-friends.webp",
    4: "island-4-castle-festive.webp",   # ворота уже открыты — как в тексте экрана
}
KEY_SRC = os.path.join(ROOT, "assets", "items", "key.png")
ISLAND_W = 880      # показывается максимум 440 px, берём вдвое под retina
KEY_W = 700

# эмодзи сюжетных экранов → ключ картинки
EMOJI_ADD = {"🎪": "island", "🪞": "island", "👫": "island", "🏰": "island", "🔑": "key"}


def data_uri(im, quality=84):
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=quality, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode(), len(buf.getvalue())


def scaled(path, width):
    im = Image.open(path).convert("RGBA")
    if im.width != width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    return im


def put_key(s, key, uri):
    """Заменяет картинку по ключу или дописывает её рядом с портретами учителя."""
    pat = re.compile(r'(\b%s\s*:\s*)"data:image/[a-z]+;base64,[^"]*"' % key)
    if pat.search(s):
        return pat.sub(lambda m: m.group(1) + '"' + uri + '"', s, count=1)
    return re.sub(r'(\n(\s*)backpack\s*:\s*")',
                  lambda m: '\n%s%s: "%s",%s' % (m.group(2), key, uri, m.group(1)), s, count=1)


def patch_render(s):
    # 1. сюжетный экран рисует картинку, а не текст эмодзи
    s = s.replace('placeholder-emoji" }, s.icon));',
                  'placeholder-emoji" }, picNode(null, s.icon)));')
    # 2. таблица эмодзи → ключ
    m = re.search(r'const EMOJI_KEY = \{(.*?)\};', s, re.S)
    body = m.group(1)
    for emoji, key in EMOJI_ADD.items():
        if '"%s"' % emoji not in body:
            body = body.rstrip().rstrip(",") + ', "%s": "%s"' % (emoji, key)
    return s[:m.start()] + "const EMOJI_KEY = {%s };" % body + s[m.end():]


def main():
    key_uri, key_weight = data_uri(scaled(KEY_SRC, KEY_W), 86)
    for n in (1, 2, 3, 4):
        path = os.path.join(LESSONS, "lesson-%d.html" % n)
        s = open(path, encoding="utf-8").read()
        isl_uri, isl_weight = data_uri(scaled(os.path.join(MAP, ISLAND[n]), ISLAND_W))
        s = put_key(s, "island", isl_uri)
        s = put_key(s, "key", key_uri)
        s = patch_render(s)
        open(path, "w", encoding="utf-8").write(s)
        print("Урок %d: остров %s (%.0f КБ) + ключик (%.0f КБ), файл %.1f МБ"
              % (n, ISLAND[n], isl_weight / 1024, key_weight / 1024,
                 os.path.getsize(path) / 1048576))


if __name__ == "__main__":
    main()
