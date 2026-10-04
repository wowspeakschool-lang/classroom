#!/usr/bin/env python3
"""Картинки к заданиям Unit 5 Homework 7: лист из шести и пляж «тогда и сейчас».

В выгрузке на этом месте стоял разворот учебника с шестью фотографиями
(нефть на птице, черепаха в чистом море, свалка на пляже, дельфин, черепаха
в пластике, белые медведи). Фотографии не берём — собираем свой лист из наших
карточек. Номера нужны: в задании ребёнок пишет «Pictures 1, 3 and 5 make me
feel happy because…».

Второй лист — две наши картинки пляжа рядом, с подписями «In 1990» и «Today»:
в блоке пропусков картинка одна, а задание сравнивает два времени.

    python3 tools/sm3_u5_eco_sheet.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U5 = os.path.join(ROOT, "media", "sm3", "u5")

# порядок намеренно вперемешку: подряд «хорошая — плохая» задание не решало бы
PICS = [
    "good_turtle_free",
    "bad_rubbish_beach",
    "good_dolphins",
    "bad_turtle_bag",
    "good_planting",
    "bad_cut_forest",
]

COLS, ROWS = 3, 2
CELL = 300
GAP = 12
PAD = 14
BG = (247, 244, 238)
BADGE = (242, 140, 40)


def font(size):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def main():
    W = PAD * 2 + CELL * COLS + GAP * (COLS - 1)
    H = PAD * 2 + CELL * ROWS + GAP * (ROWS - 1)
    sheet = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(sheet)
    f = font(34)

    for i, name in enumerate(PICS):
        im = Image.open(os.path.join(U5, name + ".webp")).convert("RGB")
        im = im.resize((CELL, CELL), Image.LANCZOS)
        x = PAD + (i % COLS) * (CELL + GAP)
        y = PAD + (i // COLS) * (CELL + GAP)
        sheet.paste(im, (x, y))
        draw.rounded_rectangle([x, y, x + CELL, y + CELL], radius=14,
                               outline=(226, 221, 212), width=2)
        draw.ellipse([x + 10, y + 10, x + 56, y + 56], fill=BADGE)
        n = str(i + 1)
        tw = draw.textlength(n, font=f)
        draw.text((x + 33 - tw / 2, y + 16), n, fill=(255, 255, 255), font=f)

    out = os.path.join(U5, "eco_six_pictures.webp")
    sheet.save(out, "WEBP", quality=88, method=6)
    print(out, sheet.width, "x", sheet.height)

    then_now()


def then_now():
    """Пляж «тогда и сейчас» — одной картинкой, с подписями."""
    cap = 54
    side = 420
    W = PAD * 2 + side * 2 + GAP
    H = PAD * 2 + side + cap
    sheet = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(sheet)
    f = font(32)
    for i, (name, label) in enumerate((("beach_clean_then", "In 1990"),
                                       ("beach_polluted_now", "Today"))):
        im = Image.open(os.path.join(U5, name + ".webp")).convert("RGB")
        im = im.resize((side, side), Image.LANCZOS)
        x = PAD + i * (side + GAP)
        draw.text((x + 4, PAD + 4), label, fill=(60, 55, 50), font=f)
        sheet.paste(im, (x, PAD + cap))
        draw.rounded_rectangle([x, PAD + cap, x + side, PAD + cap + side],
                               radius=14, outline=(226, 221, 212), width=2)
    out = os.path.join(U5, "beach_then_now.webp")
    sheet.save(out, "WEBP", quality=88, method=6)
    print(out, sheet.width, "x", sheet.height)


if __name__ == "__main__":
    main()
