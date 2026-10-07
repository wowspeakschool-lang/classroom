#!/usr/bin/env python3
"""Контактный лист превью: карточки с подписями, для показа методисту.

  python3 tools/sm1_contact.py out.png u5/act_go_swimming u1/school_book ...
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CELL, COLS, LABEL = 220, 6, 26


def main():
    out, names = sys.argv[1], sys.argv[2:]
    rows = (len(names) + COLS - 1) // COLS
    sheet = Image.new("RGB", (COLS * CELL, rows * (CELL + LABEL)), "white")
    d = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 13)
    except OSError:
        font = ImageFont.load_default()
    for i, n in enumerate(names):
        im = Image.open(os.path.join(ROOT, "media", "sm1", n + ".webp")).convert("RGB")
        im.thumbnail((CELL - 12, CELL - 12))
        x, y = (i % COLS) * CELL, (i // COLS) * (CELL + LABEL)
        sheet.paste(im, (x + (CELL - im.width) // 2, y + (CELL - im.height) // 2))
        d.rectangle((x + 2, y + 2, x + CELL - 3, y + CELL - 3), outline=(220, 220, 220))
        d.text((x + 6, y + CELL + 4), n.split("/")[-1], fill=(40, 40, 40), font=font)
    sheet.save(out)


if __name__ == "__main__":
    main()
