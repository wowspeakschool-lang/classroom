#!/usr/bin/env python3
"""Нарезка листа картинок по белым промежуткам: сначала строки, потом колонки.

    python3 tools/cut_sheet.py лист.webp папка имя1,имя2,… [--max 420] [--q 82]

Сетка, где строки перекрываются хвостами, — флаг --cols-first; ровная сетка — --grid 3x3.\nИмена — построчно, слева направо, как в промпте. Пустая клетка — «-».
Каждый кусок обрезается по содержимому с полем 4 %, белый фон остаётся.
"""
import sys, numpy as np
from PIL import Image
from pathlib import Path

def bands(mask, axis, min_gap):
    proj = mask.any(axis=axis)
    out, start, gap = [], None, 0
    for i, v in enumerate(proj):
        if v:
            if start is None: start = i
            gap = 0; end = i
        elif start is not None:
            gap += 1
            if gap >= min_gap: out.append((start, end)); start = None
    if start is not None: out.append((start, end))
    return out

def clean(p):
    """Стереть мелкие обрывки соседних картинок, касающиеся края куска."""
    a = np.asarray(p).copy(); m = a.min(axis=2) < 235
    h, w = m.shape; lab = np.zeros((h, w), int); sizes = {}; edge = {}; k = 0
    for y in range(h):
        for x in range(w):
            if m[y, x] and not lab[y, x]:
                k += 1; st = [(y, x)]; lab[y, x] = k; n = 0; e = False
                while st:
                    cy, cx = st.pop(); n += 1
                    if cy in (0, h-1) or cx in (0, w-1): e = True
                    for dy in (-1, 0, 1):
                        for dx in (-1, 0, 1):
                            ny, nx = cy+dy, cx+dx
                            if 0 <= ny < h and 0 <= nx < w and m[ny, nx] and not lab[ny, nx]:
                                lab[ny, nx] = k; st.append((ny, nx))
                sizes[k] = n; edge[k] = e
    big = max(sizes.values()) if sizes else 0
    for k, n in sizes.items():
        if edge[k] and n < big * 0.15: a[lab == k] = 255
    return Image.fromarray(a)

def main():
    src, outdir, names = sys.argv[1], Path(sys.argv[2]), sys.argv[3].split(',')
    mx = int(sys.argv[sys.argv.index('--max')+1]) if '--max' in sys.argv else 420
    q = int(sys.argv[sys.argv.index('--q')+1]) if '--q' in sys.argv else 82
    im = Image.open(src).convert('RGB'); a = np.asarray(im).astype(int)
    mask = (a.min(axis=2) < 235)
    gap = int(sys.argv[sys.argv.index('--gap')+1]) if '--gap' in sys.argv else max(8, im.width // 60)
    pieces = []
    if '--grid' in sys.argv:   # ровная сетка R×C, в клетке — обрезка по содержимому
        R, C = map(int, sys.argv[sys.argv.index('--grid')+1].split('x'))
        for ri in range(R):
            for ci in range(C):
                y0, y1 = ri*im.height//R, (ri+1)*im.height//R
                x0, x1 = ci*im.width//C, (ci+1)*im.width//C
                ys, xs = np.nonzero(mask[y0:y1, x0:x1])
                if len(ys) >= 400: pieces.append((y0+ys.min(), y0+ys.max(), x0+xs.min(), x0+xs.max()))
    elif '--cols-first' in sys.argv:   # сетка: колонки, внутри — строки; порядок — построчно
        cells = []
        for ci, (c0, c1) in enumerate(bands(mask, 0, gap)):
            for ri, (r0, r1) in enumerate(bands(mask[:, c0:c1+1], 1, gap)):
                if mask[r0:r1+1, c0:c1+1].sum() >= 400: cells.append((ri, ci, (r0, r1, c0, c1)))
        pieces = [c[2] for c in sorted(cells)]
    else:
        for r0, r1 in bands(mask, 1, gap):
            for c0, c1 in bands(mask[r0:r1+1], 0, gap):
                if mask[r0:r1+1, c0:c1+1].sum() >= 400: pieces.append((r0, r1, c0, c1))
    names = [n for n in names if n != '-']
    if len(pieces) != len(names):
        sys.exit(f'кусков {len(pieces)}, имён {len(names)}: {pieces}')
    outdir.mkdir(parents=True, exist_ok=True)
    for (r0, r1, c0, c1), n in zip(pieces, names):
        h, w = r1-r0+1, c1-c0+1; pad = int(max(h, w)*0.04)
        box = (max(0, c0-pad), max(0, r0-pad), min(im.width, c1+pad+1), min(im.height, r1+pad+1))
        p = clean(im.crop(box)); p.thumbnail((mx, mx), Image.LANCZOS)
        p.save(outdir/f'{n}.webp', 'WEBP', quality=q)
        print(n, p.size)

if __name__ == '__main__': main()
