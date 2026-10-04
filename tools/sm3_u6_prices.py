#!/usr/bin/env python3
"""Ценники к заданию Unit 6 Homework 1: шесть гаджетов с ценами.

В выгрузке ребёнок смотрел на разворот магазина из учебника и складывал цены.
Наша картинка магазина (`scene_gadget_shop`) ценники держит пустыми — генератор
текст на них не рисует, а дорисовать их на место нельзя: ценник у зубной щётки
стоит ближе к радио, и ребёнок прочитал бы чужую цену. Поэтому отдельный лист:
карточка гаджета и под ней цена.

Суммы подобраны под ответы задания: laptop 325, games console 200,
torch + electric toothbrush = 20, tablet + walkie-talkie = 115.

    python3 tools/sm3_u6_prices.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U6 = os.path.join(ROOT, "media", "sm3", "u6")

ITEMS = [
    ("gad_laptop", "a laptop", 325),
    ("gad_console", "a games console", 200),
    ("gad_tablet", "a tablet", 95),
    ("gad_walkie_talkies", "a walkie-talkie", 20),
    ("gad_torch", "a torch", 5),
    ("gad_toothbrush", "an electric toothbrush", 15),
]

COLS, ROWS = 3, 2
CELL_W, CELL_H = 300, 330
PIC = 210
GAP = 12
PAD = 16
BG = (247, 244, 238)
CARD = (255, 255, 255)
EDGE = (226, 221, 212)
INK = (45, 42, 38)
PRICE = (214, 92, 32)


def font(size, bold=True):
    names = ["DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf",
             "LiberationSans-Bold.ttf" if bold else "LiberationSans-Regular.ttf"]
    for d in ("/usr/share/fonts/truetype/dejavu/", "/usr/share/fonts/truetype/liberation/"):
        for n in names:
            if os.path.exists(d + n):
                return ImageFont.truetype(d + n, size)
    return ImageFont.load_default()


def main():
    W = PAD * 2 + CELL_W * COLS + GAP * (COLS - 1)
    H = PAD * 2 + CELL_H * ROWS + GAP * (ROWS - 1)
    sheet = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(sheet)
    f_name = font(22, bold=False)
    f_price = font(34)

    for i, (pic, label, price) in enumerate(ITEMS):
        x = PAD + (i % COLS) * (CELL_W + GAP)
        y = PAD + (i // COLS) * (CELL_H + GAP)
        draw.rounded_rectangle([x, y, x + CELL_W, y + CELL_H], radius=16,
                               fill=CARD, outline=EDGE, width=2)
        im = Image.open(os.path.join(U6, pic + ".webp")).convert("RGB")
        im.thumbnail((PIC, PIC), Image.LANCZOS)
        sheet.paste(im, (x + (CELL_W - im.width) // 2, y + 14 + (PIC - im.height) // 2))

        tw = draw.textlength(label, font=f_name)
        draw.text((x + (CELL_W - tw) / 2, y + PIC + 26), label, fill=INK, font=f_name)
        text = f"£{price}"
        tw = draw.textlength(text, font=f_price)
        draw.text((x + (CELL_W - tw) / 2, y + PIC + 58), text, fill=PRICE, font=f_price)

    out = os.path.join(U6, "shop_prices.webp")
    sheet.save(out, "WEBP", quality=88, method=6)
    print(out, sheet.width, "x", sheet.height)


if __name__ == "__main__":
    main()
