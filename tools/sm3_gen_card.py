#!/usr/bin/env python3
"""Догенерировать отдельную карточку SM3, когда в листах её не оказалось.

Листы промптов (docs/SM3_листы_промптов.md) покрывают почти всё, но в заданиях
иногда всплывает предмет, которого в них нет. Такие карточки добираются по
одной — тем же стилем и теми же правилами, что и листы.

  python3 tools/sm3_gen_card.py --unit u2 --name food_flies \
      --what "a small white plate with four or five chunky cartoon flies on it"

Готовую картинку перед заливкой показываем Анне.
"""
import argparse, base64, io, json, os, sys, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARD = 400          # сторона карточки в media/, как у нарезанных листов
QUALITY = "medium"  # «low» только на черновик: несоответствия промпту видны и в нём

STYLE = (
    "Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid "
    "saturated colours, soft even light from the top-left. One single object group "
    "centred in the frame with clear empty margins on all four sides - nothing may touch "
    "or cross the edge of the picture. Plain flat pure white background, no shadow on the "
    "background. No people at all - no humans, no hands, no faces. Absolutely no text, no "
    "letters, no numbers, no labels, no brand marks anywhere."
)


def generate(what):
    body = {"model": "gpt-image-1-mini", "prompt": what.rstrip(". ") + ". " + STYLE,
            "size": "1024x1024", "quality": QUALITY, "output_format": "png", "n": 1}
    req = urllib.request.Request(
        "https://api.openai.com/v1/images/generations",
        data=json.dumps(body).encode(),
        headers={"Authorization": "Bearer " + os.environ["OPENAI_API_KEY"],
                 "Content-Type": "application/json"})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=900))
    except urllib.error.HTTPError as e:
        sys.exit("ОШИБКА %s: %s" % (e.code, e.read().decode()[:400]))
    return base64.b64decode(r["data"][0]["b64_json"])


def edge_ink(im, thresh=244):
    """Доля не-белых пикселей вдоль каждой стороны.

    Генератор любит упирать предмет в край и обрезать его — после генерации
    это надо проверять, а не смотреть на глаз.
    """
    px = im.convert("L").load()
    w, h = im.size
    band = max(2, min(w, h) // 100)
    sides = {}
    sides["верх"] = sum(px[x, y] < thresh for y in range(band) for x in range(w)) / (band * w)
    sides["низ"] = sum(px[x, h - 1 - y] < thresh for y in range(band) for x in range(w)) / (band * w)
    sides["лево"] = sum(px[x, y] < thresh for x in range(band) for y in range(h)) / (band * h)
    sides["право"] = sum(px[w - 1 - x, y] < thresh for x in range(band) for y in range(h)) / (band * h)
    return sides


def main():
    from PIL import Image
    ap = argparse.ArgumentParser()
    ap.add_argument("--unit", required=True, help="папка media/sm3/<unit>/")
    ap.add_argument("--name", required=True, help="имя файла без расширения")
    ap.add_argument("--what", required=True, help="что нарисовать, по-английски")
    ap.add_argument("--side", type=int, default=CARD)
    args = ap.parse_args()

    im = Image.open(io.BytesIO(generate(args.what))).convert("RGB")
    im.thumbnail((args.side, args.side), Image.LANCZOS)
    out = os.path.join(ROOT, "media", "sm3", args.unit, args.name + ".webp")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    im.save(out, "WEBP", quality=82, method=6)

    print(os.path.relpath(out, ROOT), "%d×%d" % im.size, os.path.getsize(out) // 1024, "КБ")
    for side, share in edge_ink(im).items():
        mark = "  ← предмет упёрся в край" if share > 0.02 else ""
        print("  %-5s %.1f%%%s" % (side, share * 100, mark))


if __name__ == "__main__":
    main()
