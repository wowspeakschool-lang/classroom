#!/usr/bin/env python3
"""Волшебные предметы для рюкзака (§1 ТЗ, решение Анны от 16.09.2026).

Цепочка: звёздочка выдаётся при знакомстве и работает в Уроке 1, бутылочка —
в конце У1 для дороги в У2, сапоги — в конце У2, колокольчик — в конце У3
(им будят Дракона в У4), корона — подарок Дракона в финале (ассет уже есть).

Каждый предмет — ещё и карточка английского слова с озвучкой, поэтому названия
простые: a star, a bottle, boots, a bell.
"""
import base64, json, os, sys, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "items")
QUALITY = "medium"

STYLE = ("A single object centred in the frame with empty space around it, nothing else. "
         "Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid "
         "saturated colors - violet, pink, gold, turquoise. Lighting from the top-left, soft "
         "shadow under the object. No text, no letters, no numbers. Transparent background.")

ITEMS = {
    "star": "A magic star charm: a plump five-pointed golden star with a warm glow, rounded "
            "edges and tiny sparkles floating around it. " + STYLE,
    "bottle": "A magic water bottle: a small rounded glass flask with a wooden cork, filled "
              "with sparkling turquoise water, a few bubbles and sparkles inside. " + STYLE,
    "boots": "A pair of magic travelling boots standing side by side: short chunky boots of "
             "violet leather with golden buckles and small golden wings at the ankles. " + STYLE,
    "bell": "A magic hand bell: a golden bell with a smooth wooden handle and a small star on "
            "top, a few sparkles around its rim. " + STYLE,
}


def generate(key):
    body = {"model": "gpt-image-1", "prompt": ITEMS[key], "size": "1024x1024",
            "quality": QUALITY, "background": "transparent", "output_format": "png", "n": 1}
    req = urllib.request.Request("https://api.openai.com/v1/images/generations",
        data=json.dumps(body).encode(),
        headers={"Authorization": "Bearer " + os.environ["OPENAI_API_KEY"],
                 "Content-Type": "application/json"})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=900))
    except urllib.error.HTTPError as e:
        return key, "ОШИБКА %s: %s" % (e.code, e.read().decode()[:200])
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, key + ".png")
    open(path, "wb").write(base64.b64decode(r["data"][0]["b64_json"]))
    return key, "готово (~$%.3f)" % (r["usage"]["output_tokens"] * 40 / 1e6)


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--final" in args:
        QUALITY = "high"; args.remove("--final")
    with ThreadPoolExecutor(max_workers=4) as pool:
        for k, msg in pool.map(generate, args or list(ITEMS)):
            print(k, "->", msg)
