#!/usr/bin/env python3
"""Циферблаты для Unit 6 «Telling the time» → media/gg1/u6/clock_HHMM.svg.

Часы рисует скрипт, а не генератор: генератор ставит стрелки «примерно», а в
задании «It's twenty to nine» часовая стрелка обязана стоять между 8 и 9,
ближе к 9. Здесь угол считается точно: минутная — 6° на минуту, часовая —
30° на час плюс 0.5° на минуту.

  python3 tools/gg1_clocks.py
"""
import math, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "media", "gg1", "u6")

# hw4 «Найди пару» — 8 штук; test 2.4, 2.5, 3.3; hw7 «доп. задание» — 12:30
TIMES = ["04:45", "06:00", "09:10", "01:15", "08:40", "02:30", "05:05", "12:55",
         "02:15", "08:00", "07:30", "12:30"]

C = 200          # центр, viewBox 400×400
R = 170          # радиус обода


def hand(angle_deg, length, width, colour, tail=18):
    a = math.radians(angle_deg)
    x2, y2 = C + length * math.sin(a), C - length * math.cos(a)
    x1, y1 = C - tail * math.sin(a), C + tail * math.cos(a)
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{colour}" stroke-width="{width}" stroke-linecap="round"/>')


def svg(h, m):
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">',
        f'<circle cx="{C}" cy="{C}" r="{R + 14}" fill="#2E86DE"/>',
        f'<circle cx="{C}" cy="{C}" r="{R}" fill="#FFFFFF" stroke="#1B5FA8" stroke-width="4"/>',
    ]
    for i in range(60):
        a = math.radians(i * 6)
        big = i % 5 == 0
        r1 = R - (22 if big else 10)
        parts.append(
            f'<line x1="{C + r1 * math.sin(a):.1f}" y1="{C - r1 * math.cos(a):.1f}" '
            f'x2="{C + (R - 4) * math.sin(a):.1f}" y2="{C - (R - 4) * math.cos(a):.1f}" '
            f'stroke="#333" stroke-width="{5 if big else 2}" stroke-linecap="round"/>')
    for n in range(1, 13):
        a = math.radians(n * 30)
        rr = R - 48
        parts.append(
            f'<text x="{C + rr * math.sin(a):.1f}" y="{C - rr * math.cos(a) + 13:.1f}" '
            f'font-family="Arial, Helvetica, sans-serif" font-size="38" font-weight="bold" '
            f'fill="#222" text-anchor="middle">{n}</text>')
    parts.append(hand((h % 12) * 30 + m * 0.5, 72, 14, "#E53935"))   # часовая — короткая, красная
    parts.append(hand(m * 6, 108, 8, "#222222"))                    # минутная — длинная, чёрная
    parts.append(f'<circle cx="{C}" cy="{C}" r="11" fill="#222"/>')
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main():
    os.makedirs(OUT, exist_ok=True)
    for t in TIMES:
        h, m = map(int, t.split(":"))
        path = os.path.join(OUT, f"clock_{h:02d}{m:02d}.svg")
        with open(path, "w") as f:
            f.write(svg(h, m))
        print(os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
