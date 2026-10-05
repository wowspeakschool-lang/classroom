#!/usr/bin/env python3
"""Кляксы краски для слов-цветов Go Getter 1 → media/gg1/u0/colour_<цвет>.svg.

Цвета рисует скрипт, а не генератор: red на карточке, в паре и в тесте должен
быть одним и тем же red. Форма у всех клякс одна, меняется только заливка.
Белая и жёлтая получают обводку темнее, иначе на белой карточке их не видно.

  python3 tools/gg1_colours.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "media", "gg1", "u0")

COLOURS = {
    "red":    "#E53935",
    "blue":   "#1E6FE0",
    "green":  "#2EAA4A",
    "yellow": "#FFD21F",
    "orange": "#FF8A1F",
    "pink":   "#FF6FB5",
    "purple": "#8E44D9",
    "black":  "#222222",
    "white":  "#FFFFFF",
    "grey":   "#9A9A9A",
    "brown":  "#8B5A2B",
}

# обводка: у светлых — заметнее, у остальных — чуть темнее заливки
OUTLINE = {"white": "#B8B8B8", "yellow": "#D9A800"}

BLOB = ("M100 18 C128 14 150 30 160 52 C178 58 190 80 182 102 "
        "C194 124 180 152 154 158 C142 182 112 190 92 176 "
        "C68 188 38 176 34 150 C12 140 6 112 22 94 "
        "C12 70 26 42 52 40 C64 22 84 16 100 18 Z")
DROPS = [(176, 40, 9), (24, 172, 7), (186, 170, 6)]


def darker(hex_colour, k=0.78):
    r, g, b = (int(hex_colour[i:i + 2], 16) for i in (1, 3, 5))
    return "#%02X%02X%02X" % (int(r * k), int(g * k), int(b * k))


def svg(name, fill):
    stroke = OUTLINE.get(name, darker(fill))
    drops = "".join(
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'
        for x, y, r in DROPS)
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="400" height="400">'
        f'<path d="{BLOB}" fill="{fill}" stroke="{stroke}" stroke-width="4" stroke-linejoin="round"/>'
        '<ellipse cx="78" cy="62" rx="22" ry="11" fill="#FFFFFF" opacity="0.35" '
        'transform="rotate(-25 78 62)"/>'
        f"{drops}</svg>\n")


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, fill in COLOURS.items():
        path = os.path.join(OUT, f"colour_{name}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg(name, fill))
        print(os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
