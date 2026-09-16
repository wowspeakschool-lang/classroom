#!/usr/bin/env python3
"""Нарезка пергамента на 4 обрывка с рваными краями (ТЗ §3).

Куски режутся двумя рваными линиями — вертикальной и горизонтальной. Каждый кусок
сохраняется на полном холсте 1024x1024, прозрачном вокруг обрывка: если положить
все четыре друг на друга в одной позиции, карта сходится пиксель в пиксель.
Seed фиксирован, повторный запуск даёт тот же результат.
"""
import os, random
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets", "map", "parchment-map.png")
NAMES = ["piece-1-tl", "piece-2-tr", "piece-3-bl", "piece-4-br"]


def jagged(length, centre, rnd, step=14, amp=26, spike=9):
    """Рваная линия: крупные зубцы плюс мелкие волокна бумаги."""
    pts, pos, val = [], 0, centre
    while pos < length:
        val = max(centre - amp * 2, min(centre + amp * 2, val + rnd.uniform(-amp, amp)))
        pts.append((pos, val + rnd.uniform(-spike, spike)))
        pos += rnd.randint(step // 2, step)
    pts.append((length, centre + rnd.uniform(-spike, spike)))
    return pts


def half_mask(size, vertical, rnd):
    """Маска половины холста, отрезанной рваной линией (левая или верхняя)."""
    w, h = size
    m = Image.new("L", size, 0)
    d = ImageDraw.Draw(m)
    if vertical:
        line = jagged(h, w / 2, rnd)
        poly = [(0, 0)] + [(x, y) for y, x in line] + [(0, h)]
    else:
        line = jagged(w, h / 2, rnd)
        poly = [(0, 0)] + list(line) + [(w, 0)]
    d.polygon(poly, fill=255)
    return m


def main():
    src = Image.open(SRC).convert("RGBA")
    rnd = random.Random(20260916)
    left = half_mask(src.size, True, rnd)
    top = half_mask(src.size, False, rnd)
    from PIL import ImageChops
    right, bottom = ImageChops.invert(left), ImageChops.invert(top)
    quadrants = [ImageChops.multiply(left, top), ImageChops.multiply(right, top),
                 ImageChops.multiply(left, bottom), ImageChops.multiply(right, bottom)]
    out_dir = os.path.join(ROOT, "assets", "map")
    for name, mask in zip(NAMES, quadrants):
        # края намеренно без размытия: маски соседних кусков строго дополняют друг друга,
        # иначе на стыке собранной карты светится полупрозрачный шов
        alpha = ImageChops.multiply(src.getchannel("A"), mask)
        # цвет под прозрачной частью обнуляем: PNG хранит его и без этого кусок весит
        # столько же, сколько целая карта
        piece = Image.new("RGBA", src.size, (0, 0, 0, 0))
        piece.paste(src, (0, 0), alpha)
        piece.putalpha(alpha)
        path = os.path.join(out_dir, "map-%s.png" % name)
        piece.save(path, optimize=True)
        bbox = piece.getbbox()
        print("%s -> %s, занятая область %s" % (name, path, bbox))

    # контрольная сборка: четыре куска обратно в целую карту
    check = Image.new("RGBA", src.size, (0, 0, 0, 0))
    for name in NAMES:
        check.alpha_composite(Image.open(os.path.join(out_dir, "map-%s.png" % name)))
    holes = sum(check.getchannel("A").histogram()[:250])
    print("дырок после сборки (пикселей с alpha<250): %d" % holes)
    check.convert("RGB").save(os.path.join(ROOT, "assets", "map", "parchment-reassembled.png"))


if __name__ == "__main__":
    main()
