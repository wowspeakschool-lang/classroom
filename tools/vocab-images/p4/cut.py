"""Нарезка листов Prepare 4: python3 cut.py <лист> <картинка> [<лист> <картинка> ...]
Ряды — по профилю строк (полоса рисунков, за ней полоса подписей). Внутри ряда —
кластеры по зазору (12 → 6 → 3); не сошлось — границы по самым пустым колонкам
около равных долей ряда. Выход: out/<лист>/<term>.png."""
import sys, os
import numpy as np
from PIL import Image
sys.path.insert(0, '..')
from lib import row, row_x, clusters_of, min_rgb_of
from sheets import S

LAYOUT = {7: [4, 3], 8: [4, 4], 9: [5, 4], 10: [5, 5], 11: [4, 4, 3], 12: [4, 4, 4], 13: [5, 4, 4]}

def bands(path):
    a = min_rgb_of(Image.open(path))
    ink = (a < 200).sum(1) > 3
    out, s = [], None
    for y, v in enumerate(ink):
        if v and s is None: s = y
        if not v and s is not None:
            if y - s > 4: out.append((s, y))
            s = None
    if s is not None: out.append((s, len(ink)))
    return out

def split_rows(path, bs, n_rows):
    """Полосы рисунков — выше 60 px. Если полоса началась вплотную к предыдущей,
    в её верх влипла подпись прошлого ряда: срезаем по самой пустой строке под ней."""
    c = (min_rgb_of(Image.open(path)) < 200).sum(1)
    rows, prev, prev_pic = [], -100, False
    for i, (y0, y1) in enumerate(bs):
        pic = y1 - y0 > 60
        if pic:
            if prev_pic and y0 - prev < 8:
                y0 = y0 + 20 + int(np.argmin(c[y0 + 20:y0 + 90]))
            else:
                # светлые пряди и тени не дотягивают до порога 200 — берём весь белый
                # промежуток до предыдущей полосы (подписи), он гарантированно пустой
                y0 = max(0, prev + 2)
            nxt = bs[i + 1][0] if i + 1 < len(bs) else len(c)
            rows.append((y0, max(y1, nxt - 2)))
        prev, prev_pic = y1, pic
    if len(rows) != n_rows:
        raise SystemExit(f'рядов {len(rows)} вместо {n_rows}: {bs}')
    return rows

def column_cuts(path, y0, y1, n):
    a = min_rgb_of(Image.open(path))[y0:y1] < 235
    c = a.sum(0); xs = np.where(c > 0)[0]; L, R = xs.min(), xs.max()
    cuts = []
    for k in range(1, n):
        mid = L + (R - L) * k / n; w = (R - L) / n * 0.25
        lo, hi = int(mid - w), int(mid + w)
        cuts.append(lo + int(np.argmin(c[lo:hi])))
    return cuts, [int(c[x]) for x in cuts]

def cut(sheet, path, out='out'):
    title, note, items = S[sheet - 1]
    lay = LAYOUT[len(items)]
    rows = split_rows(path, bands(path), len(lay))
    k = 0; report = []
    for (y0, y1), n in zip(rows, lay):
        words = [t for _, t, _ in items[k:k + n]]; k += n
        d = f'{out}/{sheet}'
        ok = False
        for g in (12, 6, 3):
            if len(clusters_of(path, y0, y1, 150, 235, g)[4]) == n:
                row(path, y0, y1, words, d, gap=g, min_area=150); ok = True
                report.append(f'  ряд {y0}-{y1}: {n} шт, зазор {g}'); break
        if not ok:
            cuts, ink = column_cuts(path, y0, y1, n)
            row_x(path, y0, y1, words, d, cuts)
            report.append(f'  ряд {y0}-{y1}: {n} шт, ПО КОЛОНКАМ {cuts} чернил {ink}')
    print(f'лист {sheet} {title}:'); print('\n'.join(report))

if __name__ == '__main__':
    a = sys.argv[1:]
    for i in range(0, len(a), 2):
        cut(int(a[i]), a[i + 1])
