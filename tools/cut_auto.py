# -*- coding: utf-8 -*-
"""Нарезка листа на отдельные картинки по кускам изображения, а не по сетке.

    python3.13 tools/cut_auto.py лист.png папка имя1,имя2,… [--max 800] [--q 90]

Ровная сетка (`cut_sheet.py --grid`) срубает фигуре макушку, если та заходит
за середину листа, а деление по белым полосам не работает, когда картинки
стоят «лесенкой». Здесь ищутся связные пятна краски, близкие пятна
объединяются в один предмет (мальчик и мяч рядом — это одна картинка), затем
берутся N самых крупных групп по числу имён. Поле вокруг — 4 %, но не больше
половины промежутка до соседа, чтобы в кусок не залез сосед.
"""
import sys
import numpy as np
from PIL import Image
from pathlib import Path


def components(mask):
    """Связные пятна без scipy: обход в ширину по сетке с шагом 1."""
    h, w = mask.shape
    seen = np.zeros_like(mask, bool)
    boxes = []
    from collections import deque
    for y in range(h):
        row = mask[y]
        for x in range(w):
            if row[x] and not seen[y, x]:
                q = deque([(y, x)]); seen[y, x] = True
                x0 = x1 = x; y0 = y1 = y; size = 0
                while q:
                    cy, cx = q.popleft(); size += 1
                    if cx < x0: x0 = cx
                    if cx > x1: x1 = cx
                    if cy < y0: y0 = cy
                    if cy > y1: y1 = cy
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not seen[ny, nx]:
                            seen[ny, nx] = True; q.append((ny, nx))
                boxes.append([x0, x1, y0, y1, size])
    return boxes


def merge(boxes, dist):
    """Склеивает пятна, чьи рамки ближе dist: мальчик, мяч и нотки — один предмет."""
    changed = True
    while changed:
        changed = False
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                a, b = boxes[i], boxes[j]
                if (a[0] - dist <= b[1] and b[0] - dist <= a[1]
                        and a[2] - dist <= b[3] and b[2] - dist <= a[3]):
                    boxes[i] = [min(a[0], b[0]), max(a[1], b[1]),
                                min(a[2], b[2]), max(a[3], b[3]), a[4] + b[4]]
                    boxes.pop(j); changed = True; break
            if changed:
                break
    return boxes


def main():
    src, outdir, names = sys.argv[1], sys.argv[2], sys.argv[3].split(',')
    mx = int(sys.argv[sys.argv.index('--max') + 1]) if '--max' in sys.argv else 800
    q = int(sys.argv[sys.argv.index('--q') + 1]) if '--q' in sys.argv else 90
    im = Image.open(src).convert('RGB')
    K = 3                                   # считаем по уменьшенной копии — быстрее
    small = np.asarray(im.reduce(K))
    mask = small.sum(2) < 730
    H, W = mask.shape
    want = len([n for n in names if n != '-'])

    groups = None
    for frac in (0.0, 0.003, 0.006, 0.01, 0.015, 0.02, 0.03, 0.045, 0.06, 0.08):
        boxes = merge([b for b in components(mask) if b[4] > mask.size * 0.0004],
                      int(max(H, W) * frac))
        boxes = [b for b in boxes if b[4] > mask.size * 0.001]
        if len(boxes) == want:
            groups = boxes
            break
    if groups is None:
        print(f'не вышло разделить на {want}: получилось {len(boxes)}')
        sys.exit(1)

    rowh = max(b[3] - b[2] for b in groups)
    groups.sort(key=lambda b: (round((b[2] + b[3]) / 2 / (rowh * 0.8)), b[0]))
    print(f'кусков {len(groups)}, имён {want}')

    Path(outdir).mkdir(parents=True, exist_ok=True)
    for b, name in zip(groups, [n for n in names if n != '-']):
        x0, x1, y0, y1 = [v * K for v in b[:4]]
        pad = int(max(x1 - x0, y1 - y0) * 0.04) + 2
        # поле не должно дотянуться до соседа
        for o in groups:
            if o is b:
                continue
            ox0, ox1, oy0, oy1 = [v * K for v in o[:4]]
            if not (oy1 < y0 or oy0 > y1):
                if ox0 > x1: pad = min(pad, (ox0 - x1) // 2)
                if ox1 < x0: pad = min(pad, (x0 - ox1) // 2)
            if not (ox1 < x0 or ox0 > x1):
                if oy0 > y1: pad = min(pad, (oy0 - y1) // 2)
                if oy1 < y0: pad = min(pad, (y0 - oy1) // 2)
        pad = max(pad, 0)
        cut = im.crop((max(0, x0 - pad), max(0, y0 - pad),
                       min(im.size[0], x1 + K + pad), min(im.size[1], y1 + K + pad)))
        if max(cut.size) > mx:
            cut.thumbnail((mx, mx))
        cut.save(f'{outdir}/{name}.webp', 'WEBP', quality=q)
        print(f'  {name} {cut.size}')


if __name__ == '__main__':
    main()
