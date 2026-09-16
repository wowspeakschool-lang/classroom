#!/usr/bin/env python3
"""Облегчённые версии картинок карты для веба.

Оригиналы в assets/map/ — мастера, их не трогаем. Здесь из них делаются WebP
того размера, в котором картинка реально показывается на странице (с запасом
x2 под retina). Карту открывают с телефона, поэтому вес важнее пикселей.
"""
import os
from PIL import Image, ImageFilter

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
    "map-background": (1024, 84),        # телефон: родное разрешение, тянуть нечего
    "map-background-wide": (2304, 86),   # ноутбук с retina: 1536 -> 2304
    # Обрывки пергамента и собранная карта на странице больше не нужны:
    # по решению Анны наградой стал ключик от следующего острова, а не часть карты.
    # Мастера PNG и tools/cut_parchment.py остаются на случай возврата к этой идее.
    "dragon": (270, 88), "crown": (250, 88),
}


def lesson_skies():
    """Фон уроков — только небо, без моря.

    В полном небе у горизонта есть светлая полоса. За содержимым урока она
    попадала ровно под кнопку и читалась как белая линия во всю ширину экрана.
    Море уместно на карте, а под текстом нужен ровный фон.
    """
    for src_name, dst_name, keep in (("map-background-wide", "sky-lesson-wide", 0.62),
                                     ("map-background", "sky-lesson-tall", 0.58)):
        im = Image.open(os.path.join(SRC, src_name + ".png")).convert("RGB")
        im = im.crop((0, 0, im.width, int(im.height * keep)))
        width = 2304 if "wide" in dst_name else 1024
        if im.width != width:
            im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
            im = im.filter(ImageFilter.UnsharpMask(radius=1.6, percent=55, threshold=2))
        dst = os.path.join(OUT, dst_name + ".webp")
        im.save(dst, "WEBP", quality=84, method=6)
        print("%-26s %s -> %4.0f КБ" % (dst_name, im.size, os.path.getsize(dst) / 1024))


def main():
    os.makedirs(OUT, exist_ok=True)
    lesson_skies()
    before = after = 0
    for name, (width, q) in PLAN.items():
        src = os.path.join(SRC, name + ".png")
        im = Image.open(src)
        before += os.path.getsize(src)
        if im.width != width:
            im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
            if width > Image.open(src).width:
                # увеличиваем сами и слегка поднимаем резкость: иначе на retina
                # растягивать будет браузер, и края облаков расплываются
                im = im.filter(ImageFilter.UnsharpMask(radius=1.6, percent=55, threshold=2))
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
