#!/usr/bin/env python3
"""Часы для Unit 3 — SVG: стрелочные циферблаты и электронное табло.

Генератор картинок стрелки не держит: из 12 сгенерированных циферблатов
правильными оказались 5. Здесь угол считается, а не рисуется на глаз.

Электронное табло нужно домашке 2: там шесть вопросов «сколько времени на
картинке?» по фотографиям электронных часов из интернета (одна с водяным
знаком стока, одна вообще футболка с принтом). Цифры рисуются семью
сегментами-многоугольниками, а не текстом: шрифта в SVG может не оказаться,
и тогда время расползётся или пропадёт.

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
    # добавлены для картинки к тесту: ровно то время, что в заданиях теста
    (7, 15, "quarter_past_seven"),
    (11, 0, "eleven_oclock"),
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


# ---------- электронное табло ----------

# (часы, минуты, имя файла) — ровно те времена, что в выгрузке домашки 2
DIGITAL = [
    (2, 15, "digital_two_fifteen"),
    (11, 0, "digital_eleven_oclock"),
    (12, 45, "digital_twelve_forty_five"),
    (9, 30, "digital_nine_thirty"),
    (5, 45, "digital_five_forty_five"),
    (8, 0, "digital_eight_oclock"),
]

# какие сегменты горят у каждой цифры; a — верх, g — середина
SEGS = {
    "0": "abcdef", "1": "bc",     "2": "abdeg",  "3": "abcdg", "4": "bcfg",
    "5": "acdfg",  "6": "acdefg", "7": "abc",    "8": "abcdefg", "9": "abcdfg",
}

DW, DH, DT = 58, 104, 13          # ширина, высота и толщина цифры
GAP = 18                          # просвет между цифрами
COLON_W = 26


def seg_poly(seg: str, x: float, y: float) -> str:
    """Один сегмент как шестиугольник: скошенные концы, как у настоящего табло."""
    t, w, h = DT, DW, DH
    k = t / 2
    if seg in "ad g"[:3] or seg == "g":                 # горизонтальные a, d, g
        cy = {"a": y, "d": y + h, "g": y + h / 2}[seg]
        return (f'{x+k},{cy-k} {x+w-k},{cy-k} {x+w-k+k/2},{cy} '
                f'{x+w-k},{cy+k} {x+k},{cy+k} {x+k-k/2},{cy}')
    cx = x + (w if seg in "bc" else 0)                  # вертикальные b, c, e, f
    top = y + (h / 2 if seg in "ce" else 0)
    bot = top + h / 2
    return (f'{cx-k},{top+k} {cx},{top+k-k/2} {cx+k},{top+k} '
            f'{cx+k},{bot-k} {cx},{bot-k+k/2} {cx-k},{bot-k}')


def digital_svg(h: int, m: int) -> str:
    text = f"{h}:{m:02d}"
    # ширина табло: цифры + двоеточия + поля
    body = 0.0
    for ch in text:
        body += COLON_W if ch == ":" else DW
        body += GAP
    body -= GAP
    pad_x, pad_y = 70, 56
    W = int(body + pad_x * 2)
    H = int(DH + pad_y * 2)
    on, off = "#ff8a1f", "#3a2a18"
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
           f'  <rect width="{W}" height="{H}" rx="28" fill="#141414"/>',
           f'  <rect x="14" y="14" width="{W-28}" height="{H-28}" rx="18" '
           f'fill="none" stroke="#2c2c2c" stroke-width="4"/>']
    x = float(pad_x)
    for ch in text:
        if ch == ":":
            for cy in (pad_y + DH * 0.30, pad_y + DH * 0.70):
                out.append(f'  <circle cx="{x + COLON_W/2:.1f}" cy="{cy:.1f}" r="{DT*0.55:.1f}" fill="{on}"/>')
            x += COLON_W + GAP
            continue
        lit = SEGS[ch]
        for seg in "abcdefg":
            colour = on if seg in lit else off
            out.append(f'  <polygon points="{seg_poly(seg, x, pad_y)}" fill="{colour}"/>')
        x += DW + GAP
    out.append("</svg>")
    return "\n".join(out) + "\n"


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
    for h, m, name in DIGITAL:
        path = out / f"{name}.svg"
        path.write_text(digital_svg(h, m), encoding="utf-8")
        print(f"{path}  {h}:{m:02d}")


if __name__ == "__main__":
    main()
