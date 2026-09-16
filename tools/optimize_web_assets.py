#!/usr/bin/env python3
"""Облегчённые версии картинок карты для веба.

Оригиналы в assets/map/ — мастера, их не трогаем. Здесь из них делаются WebP
того размера, в котором картинка реально показывается на странице (с запасом
x2 под retina). Карту открывают с телефона, поэтому вес важнее пикселей.
"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets", "map")
OUT = os.path.join(SRC, "web")

# файл: (ширина в пикселях, качество WebP)
PLAN = {
    "island-1-fair": (820, 82), "island-2-mirrors": (820, 82),
    "island-3-friends": (820, 82), "island-4-castle-closed": (820, 82),
    "island-4-castle-festive": (820, 82),
    # Фон занимает весь экран, поэтому сжимаем его бережнее остальных и не
    # уменьшаем: вертикальное небо — 1024 px, горизонтальное — 1536 px в ширину.
    # Раньше стояло 1000 px и качество 78, и на ноутбуке фон заметно мылился.
    "map-background": (1024, 84),
    "map-background-wide": (1536, 84),
    # Обрывки пергамента и собранная карта на странице больше не нужны:
    # по решению Анны наградой стал ключик от следующего острова, а не часть карты.
    # Мастера PNG и tools/cut_parchment.py остаются на случай возврата к этой идее.
    "dragon": (270, 88), "crown": (250, 88),
}


def main():
    os.makedirs(OUT, exist_ok=True)
    before = after = 0
    for name, (width, q) in PLAN.items():
        src = os.path.join(SRC, name + ".png")
        im = Image.open(src)
        before += os.path.getsize(src)
        if im.width > width:
            im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
        dst = os.path.join(OUT, name + ".webp")
        im.save(dst, "WEBP", quality=q, method=6)
        after += os.path.getsize(dst)
        # прозрачность должна пережить конвертацию, иначе остров поедет белым прямоугольником
        alpha = "без альфы" if Image.open(dst).mode != "RGBA" else "альфа на месте"
        print("%-26s %5d КБ -> %4d КБ  (%s)" % (
            name, os.path.getsize(src) / 1024, os.path.getsize(dst) / 1024, alpha))
    print("\nвсего: %.1f МБ -> %.1f МБ" % (before / 1e6, after / 1e6))


if __name__ == "__main__":
    main()
