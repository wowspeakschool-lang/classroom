#!/usr/bin/env python3
"""Флаги стран Unit 1 Go Getter 1 → media/gg1/u1/flag_<страна>.svg.

Флаг — точный рисунок, генератор его путает (звёзды, кресты Юнион Джека),
поэтому флаги рисует скрипт. Все флаги одной пропорции 3:2, с тонкой рамкой:
белая полоса польского флага иначе сливается с белой карточкой. Герб Испании
опущен — на карточке размером с ладонь он всё равно неразличим.

  python3 tools/gg1_flags.py
"""
import math, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "media", "gg1", "u1")
W, H = 300, 200


def star(cx, cy, r, rot=0.0, fill="#FFDE00"):
    pts = []
    for i in range(10):
        rr = r if i % 2 == 0 else r * 0.382
        a = math.radians(-90 + rot + i * 36)
        pts.append(f"{cx + rr * math.cos(a):.2f},{cy + rr * math.sin(a):.2f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"/>'


def stripes_h(colours):
    h = H / len(colours)
    return "".join(f'<rect x="0" y="{i * h:.3f}" width="{W}" height="{h + 0.5:.3f}" fill="{c}"/>'
                   for i, c in enumerate(colours))


def stripes_v(colours):
    w = W / len(colours)
    return "".join(f'<rect x="{i * w:.3f}" y="0" width="{w + 0.5:.3f}" height="{H}" fill="{c}"/>'
                   for i, c in enumerate(colours))


def uk():
    # Юнион Джек на поле 60×30, растянут на 3:2 — так его рисуют на карточках
    return (
        '<svg x="0" y="0" width="300" height="200" viewBox="0 0 60 30" preserveAspectRatio="none">'
        '<clipPath id="s"><path d="M0,0 v30 h60 v-30 z"/></clipPath>'
        '<clipPath id="t"><path d="M30,15 h30 v15 z v15 h-30 z h-30 v-15 z v-15 h30 z"/></clipPath>'
        '<g clip-path="url(#s)">'
        '<path d="M0,0 v30 h60 v-30 z" fill="#012169"/>'
        '<path d="M0,0 L60,30 M60,0 L0,30" stroke="#fff" stroke-width="6"/>'
        '<path d="M0,0 L60,30 M60,0 L0,30" clip-path="url(#t)" stroke="#C8102E" stroke-width="4"/>'
        '<path d="M30,0 v30 M0,15 h60" stroke="#fff" stroke-width="10"/>'
        '<path d="M30,0 v30 M0,15 h60" stroke="#C8102E" stroke-width="6"/>'
        '</g></svg>')


def usa():
    out = stripes_h(["#B22234", "#FFFFFF"] * 6 + ["#B22234"])
    cw, ch = W * 0.4, H * 7 / 13
    out += f'<rect x="0" y="0" width="{cw:.2f}" height="{ch:.2f}" fill="#3C3B6E"/>'
    # 50 звёзд: 9 рядов по 6 и 5 вперемежку
    for row in range(9):
        n = 6 if row % 2 == 0 else 5
        for k in range(n):
            x = cw / 12 * (2 * k + 1 + (row % 2))
            y = ch / 10 * (row + 1)
            out += star(x, y, 4.4, fill="#FFFFFF")
    return out


def china():
    u = W / 30          # флаг 30×20 клеток
    out = f'<rect width="{W}" height="{H}" fill="#EE1C25"/>'
    out += star(5 * u, 5 * u, 3 * u)
    for x, y in [(10, 2), (12, 4), (12, 7), (10, 9)]:
        rot = math.degrees(math.atan2(5 - y, 5 - x)) + 90
        out += star(x * u, y * u, u, rot)
    return out


FLAGS = {
    "uk": uk,
    "usa": usa,
    "china": china,
    "poland": lambda: stripes_h(["#FFFFFF", "#DC143C"]),
    "france": lambda: stripes_v(["#0055A4", "#FFFFFF", "#EF4135"]),
    "italy": lambda: stripes_v(["#009246", "#FFFFFF", "#CE2B37"]),
    "spain": lambda: (f'<rect width="{W}" height="{H}" fill="#AA151B"/>'
                      f'<rect y="{H / 4}" width="{W}" height="{H / 2}" fill="#F1BF00"/>'),
}


def svg(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-6 -6 {W + 12} {H + 12}" '
            f'width="{(W + 12) * 2}" height="{(H + 12) * 2}">'
            f'<clipPath id="r"><rect width="{W}" height="{H}" rx="10"/></clipPath>'
            f'<g clip-path="url(#r)">{body}</g>'
            f'<rect width="{W}" height="{H}" rx="10" fill="none" stroke="#9A9A9A" stroke-width="3"/>'
            '</svg>\n')


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, draw in FLAGS.items():
        path = os.path.join(OUT, f"flag_{name}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg(draw()))
        print(os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
