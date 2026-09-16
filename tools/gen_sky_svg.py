#!/usr/bin/env python3
"""Небо и море вектором.

Картинка-фон упирается в предел генератора: 1536 px по длинной стороне. На
retina-ноутбуке экран шире вдвое, поэтому фон всегда растягивается и мылится.
Вектор масштабируется без потерь и весит единицы килобайт вместо сотен.

Делает два файла: горизонтальное небо для ноутбука и вертикальное для телефона.
Seed фиксирован — повторный запуск даёт тот же результат.
"""
import os, random

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "assets", "map", "web")


def cloud(cx, cy, s, op):
    """Облако из перекрывающихся эллипсов с мягкой заливкой."""
    parts = [(0, 0, 1.0, 0.62), (-0.75, 0.16, 0.72, 0.5), (0.78, 0.2, 0.66, 0.46),
             (-0.34, -0.3, 0.62, 0.46), (0.36, -0.26, 0.58, 0.42)]
    body = "".join(
        '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f"/>'
        % (cx + dx * s, cy + dy * s, rx * s, ry * s) for dx, dy, rx, ry in parts)
    base = ('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f"/>'
            % (cx, cy + 0.3 * s, 1.5 * s, 0.34 * s))
    # светлая шапка по верхним клубам — объём вместо плоского силуэта
    top = "".join(
        '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f"/>'
        % (cx + dx * s, cy + (dy - 0.1) * s, rx * s * 0.78, ry * s * 0.6)
        for dx, dy, rx, ry in parts[:3])
    return ('<g opacity="%.2f"><g fill="url(#cl)">%s%s</g>'
            '<g fill="url(#clTop)">%s</g></g>') % (op, base, body, top)


def sparkle(x, y, r, color, op):
    d = ("M %.1f %.1f C %.1f %.1f, %.1f %.1f, %.1f %.1f C %.1f %.1f, %.1f %.1f, %.1f %.1f "
         "C %.1f %.1f, %.1f %.1f, %.1f %.1f C %.1f %.1f, %.1f %.1f, %.1f %.1f Z") % (
        x, y - r, x + r * .18, y - r * .18, x + r * .18, y - r * .18, x + r, y,
        x + r * .18, y + r * .18, x + r * .18, y + r * .18, x, y + r,
        x - r * .18, y + r * .18, x - r * .18, y + r * .18, x - r, y,
        x - r * .18, y - r * .18, x - r * .18, y - r * .18, x, y - r)
    return '<path d="%s" fill="%s" opacity="%.2f"/>' % (d, color, op)


def build(w, h, sea_at, seed):
    rnd = random.Random(seed)
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
           'preserveAspectRatio="xMidYMid slice">' % (w, h)]
    out.append(("""<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#2f97dd"/><stop offset="0.38" stop-color="#46c6e6"/>
  <stop offset="0.72" stop-color="#84e2d7"/><stop offset="1" stop-color="#ffeaa6"/>
</linearGradient>
<linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#2ecdcd"/><stop offset="1" stop-color="#0f9fb0"/>
</linearGradient>
<linearGradient id="cl" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="%(sea)d">
  <stop offset="0" stop-color="#fff0f7"/><stop offset="0.45" stop-color="#ffd2ee"/>
  <stop offset="0.75" stop-color="#e3b6f2"/><stop offset="1" stop-color="#bda8f0"/>
</linearGradient>
<linearGradient id="clTop" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="%(sea)d">
  <stop offset="0" stop-color="#fffdf6" stop-opacity="0.85"/>
  <stop offset="1" stop-color="#ffe7f6" stop-opacity="0.4"/>
</linearGradient>
<radialGradient id="sun" cx="0.5" cy="0" r="0.7">
  <stop offset="0" stop-color="#fff3bd" stop-opacity="0.95"/>
  <stop offset="1" stop-color="#fff3bd" stop-opacity="0"/>
</radialGradient>
</defs>""") % {"sea": sea_at})
    out.append('<rect width="%d" height="%d" fill="url(#sky)"/>' % (w, h))
    out.append('<ellipse cx="%d" cy="0" rx="%d" ry="%d" fill="url(#sun)"/>'
               % (w * 0.5, w * 0.45, h * 0.5))

    # облака: крупные ближе к верху, мелкие и бледные к горизонту
    for i in range(16):
        cy = rnd.uniform(h * 0.05, sea_at - h * 0.06)
        depth = (cy - h * 0.05) / max(1.0, sea_at - h * 0.11)
        s = w * rnd.uniform(0.055, 0.1) * (1.0 - depth * 0.45)
        out.append(cloud(rnd.uniform(-w * 0.05, w * 1.05), cy, s, 0.95 - depth * 0.35))

    for i in range(26):
        y = rnd.uniform(h * 0.04, sea_at - h * 0.02)
        col = rnd.choice(["#ffe89a", "#ffe89a", "#ffd3ef"])
        out.append(sparkle(rnd.uniform(0, w), y, w * rnd.uniform(0.004, 0.011), col,
                           rnd.uniform(0.5, 0.95)))

    # море и завитки волн
    out.append('<rect x="0" y="%.0f" width="%d" height="%.0f" fill="url(#sea)"/>'
               % (sea_at, w, h - sea_at))
    for i in range(9):
        y = rnd.uniform(sea_at + (h - sea_at) * 0.12, h * 0.99)
        x = rnd.uniform(-w * 0.1, w)
        ln = w * rnd.uniform(0.16, 0.34)
        amp = (h - sea_at) * rnd.uniform(0.03, 0.07)
        out.append('<path d="M %.0f %.0f q %.0f %.0f, %.0f 0 q %.0f %.0f, %.0f 0" '
                   'fill="none" stroke="#d6fbf6" stroke-width="%.1f" stroke-linecap="round" '
                   'opacity="%.2f"/>' % (x, y, ln / 4, -amp, ln / 2, ln / 4, amp, ln / 2,
                                         (h - sea_at) * 0.014, rnd.uniform(0.35, 0.7)))
    out.append("</svg>")
    return "".join(out)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, (w, h, sea, seed) in {
            "sky-wide": (1600, 1000, 700, 20260916),
            "sky-tall": (900, 1500, 900, 20260917)}.items():
        path = os.path.join(OUT, name + ".svg")
        open(path, "w", encoding="utf-8").write(build(w, h, sea, seed))
        print("%s -> %.1f КБ" % (path, os.path.getsize(path) / 1024))
