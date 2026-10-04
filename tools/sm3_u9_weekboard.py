#!/usr/bin/env python3
"""Дни недели на прогноз погоды — к заданию Unit 9 Homework 2.

Задание спрашивает «On Monday it's going to be sunny?», а на нашей картинке
(`scene_weather_board`) семь экранов без подписей. Скрипт подписывает их
Mon…Sun, чтобы ребёнок понимал, где какой день.

    python3 tools/sm3_u9_weekboard.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U9 = os.path.join(ROOT, "media", "sm3", "u9")

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# центры экранов на картинке 880x587, замерено по разделителям
CENTERS = [92, 210, 330, 450, 570, 688, 802]
LABEL_Y = 300


def font(size):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def main():
    src = os.path.join(U9, "scene_weather_board.webp")
    im = Image.open(src).convert("RGB")
    draw = ImageDraw.Draw(im)
    f = font(30)
    for day, cx in zip(DAYS, CENTERS):
        w = draw.textlength(day, font=f)
        box = [cx - w / 2 - 10, LABEL_Y - 6, cx + w / 2 + 10, LABEL_Y + 40]
        draw.rounded_rectangle(box, radius=10, fill=(255, 255, 255))
        draw.text((cx - w / 2, LABEL_Y), day, fill=(30, 60, 120), font=f)

    out = os.path.join(U9, "weather_week_board.webp")
    im.save(out, "WEBP", quality=90, method=6)
    print(out, im.width, "x", im.height)


if __name__ == "__main__":
    main()
