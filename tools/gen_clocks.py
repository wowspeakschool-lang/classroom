#!/usr/bin/env python3
"""Циферблаты для Unit 3 — SVG, без цифр, точные стрелки.

Генератор картинок стрелки не держит: из 12 сгенерированных циферблатов
правильными оказались 5. Здесь угол считается, а не рисуется на глаз.

    python3 tools/gen_clocks.py            # в media/sm3/u3/
    python3 tools/gen_clocks.py --out DIR
"""
import argparse, math, pathlib

# (часы, минуты, как читается) — порядок как в листах Л3.4 и Л3.5
TIMES = [
    (8, 15, "quarter_past_eight"),
    (8, 30, "half_past_eight"),
    (5, 15, "quarter_past_five"),
    (6, 45, "quarter_to_seven"),
    (6, 30, "half_past_six"),
    (12, 0, "twelve_oclock"),
    (3, 40, "twenty_to_four"),
    (3, 15, "quarter_past_three"),
    (4, 45, "quarter_to_five"),
    (6, 0, "six_oclock"),
    (10, 30, "half_past_ten"),
    (7, 45, "quarter_to_eight"),
]

# пастельные фоны по кругу, чтобы карточки различались в ряду
BACKS = ["#cfe4f7", "#d6efd8", "#fbd9df", "#fdeec6", "#e2d9f5", "#cdeceb"]

S = 512          # сторона картинки
CX = CY = S / 2
R_FACE = S * 0.40        # радиус циферблата
R_RIM = S * 0.43         # внешний радиус ободка
HOUR_LEN = R_FACE * 0.52 # часовая заметно короче
MIN_LEN = R_FACE * 0.80


def hand(angle_deg: float, length: float, width: float) -> str:
    """Стрелка от центра: 0° — вверх на 12, дальше по часовой."""
    a = math.radians(angle_deg - 90)
    x2 = CX + length * math.cos(a)
    y2 = CY + length * math.sin(a)
    # хвостик за центр, как у настоящих часов
    xb = CX - length * 0.13 * math.cos(a)
    yb = CY - length * 0.13 * math.sin(a)
    return (f'<line x1="{xb:.1f}" y1="{yb:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="#23272e" stroke-width="{width:.1f}" stroke-linecap="round"/>')


def ticks() -> str:
    out = []
    for i in range(12):
        a = math.radians(i * 30 - 90)
        r1 = R_FACE * 0.82
        r2 = R_FACE * 0.94
        w = 7 if i % 3 == 0 else 5          # четверти чуть жирнее
        out.append(
            f'<line x1="{CX + r1 * math.cos(a):.1f}" y1="{CY + r1 * math.sin(a):.1f}" '
            f'x2="{CX + r2 * math.cos(a):.1f}" y2="{CY + r2 * math.sin(a):.1f}" '
            f'stroke="#23272e" stroke-width="{w}" stroke-linecap="round"/>')
    return "\n  ".join(out)


def clock_svg(h: int, m: int, back: str) -> str:
    hour_a = (h % 12) * 30 + m * 0.5        # часовая ползёт вместе с минутной
    min_a = m * 6
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">
  <rect width="{S}" height="{S}" fill="{back}"/>
  <circle cx="{CX}" cy="{CY}" r="{R_RIM:.1f}" fill="#3c4250"/>
  <circle cx="{CX}" cy="{CY}" r="{R_FACE:.1f}" fill="#ffffff"/>
  {ticks()}
  {hand(hour_a, HOUR_LEN, 15)}
  {hand(min_a, MIN_LEN, 10)}
  <circle cx="{CX}" cy="{CY}" r="13" fill="#23272e"/>
</svg>
'''


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="media/sm3/u3")
    args = ap.parse_args()
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for i, (h, m, name) in enumerate(TIMES):
        path = out / f"clock_{name}.svg"
        path.write_text(clock_svg(h, m, BACKS[i % len(BACKS)]), encoding="utf-8")
        print(f"{path}  {h:02d}:{m:02d}")


if __name__ == "__main__":
    main()
