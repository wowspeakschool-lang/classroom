# Прописи Reading Club 10+: большая и маленькая буква на линейках, цифры у начала черт и стрелки.
# Рисуем кодом (генератор кривит буквы). Пары букв — в одной картинке: media/reading10/write/<буква>.svg
import os, sys, math
OUT = sys.argv[1]
TOP, MID, BASE, DESC = 20, 60, 110, 132   # линейки в координатах ячейки 100 × 140
# черты: список путей SVG (по порядку написания); в каждой черте первая точка — старт
LOW = {
 'c': ['M75 70 C68 59 49 56 38 65 C27 75 27 95 38 104 C49 113 68 110 76 100'],
 'k': ['M34 20 L34 110', 'M74 60 L36 90', 'M50 79 L76 110'],
 'e': ['M30 86 L74 86 C74 66 62 58 52 58 C38 58 30 71 30 85 C30 100 40 111 54 111 C64 111 70 107 75 101'],
 'u': ['M32 60 L32 92 C32 106 42 111 52 111 C63 111 72 104 72 92 L72 60', 'M72 60 L72 110'],
 'r': ['M36 60 L36 110', 'M36 80 C40 65 53 58 70 61'],
}
UP = {
 'c': ['M84 36 C74 20 52 17 39 26 C23 37 21 73 30 90 C41 113 71 115 85 96'],
 'k': ['M30 20 L30 110', 'M80 20 L31 70', 'M49 52 L82 110'],
 'e': ['M32 20 L32 110', 'M32 20 L78 20', 'M32 65 L70 65', 'M32 110 L78 110'],
 'u': ['M28 20 L28 80 C28 104 43 112 54 112 C66 112 80 104 80 80 L80 20'],
 'r': ['M30 20 L30 110', 'M30 20 L58 20 C81 20 81 64 58 64 L30 64', 'M52 64 L82 110'],
}
COL = ['#6A4DF4', '#F7628C', '#E8862A', '#2FB57C']
def start_point(d):
    p = d[1:].replace('C', ' ').replace('L', ' ').split()
    return float(p[0]), float(p[1])
def cell(paths, ox):
    g = [f'<g transform="translate({ox},0)">']
    for d in paths:  # сама буква — толстая светлая линия
        g.append(f'<path d="{d}" fill="none" stroke="#E4DCFF" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>')
    for k, d in enumerate(paths):  # направление — тонкая цветная линия со стрелкой
        c = COL[k % len(COL)]
        g.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#ar{k % len(COL)})"/>')
    for k, d in enumerate(paths):  # номера поверх линий
        x, y = start_point(d); c = COL[k % len(COL)]
        g.append(f'<circle cx="{x}" cy="{y}" r="6.2" fill="{c}"/><text x="{x}" y="{y + 3.3}" font-family="Montserrat,Arial,sans-serif" font-weight="900" font-size="8.5" text-anchor="middle" fill="#fff">{k + 1}</text>')
    g.append('</g>'); return ''.join(g)
def svg(l):
    W = 230
    lines = (f'<line x1="4" y1="{TOP}" x2="{W - 4}" y2="{TOP}" stroke="#D9D3EA" stroke-width="1.2"/>'
             f'<line x1="4" y1="{MID}" x2="{W - 4}" y2="{MID}" stroke="#D9D3EA" stroke-width="1.2" stroke-dasharray="5 5"/>'
             f'<line x1="4" y1="{BASE}" x2="{W - 4}" y2="{BASE}" stroke="#B9B0D6" stroke-width="2"/>'
             f'<line x1="4" y1="{DESC}" x2="{W - 4}" y2="{DESC}" stroke="#EEEAF3" stroke-width="1.2"/>')
    marks = ''.join(f'<marker id="ar{k}" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>' for k, c in enumerate(COL))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 140" width="{W * 3}" height="420"><defs>{marks}</defs>'
            f'<rect width="{W}" height="140" fill="#fff"/>{lines}{cell(UP[l], 8)}{cell(LOW[l], 118)}</svg>')
for l in LOW:
    open(os.path.join(OUT, l + '.svg'), 'w').write(svg(l)); print(l, end=' ')
