# -*- coding: utf-8 -*-
"""Режет присланный методистом лист на отдельные картинки.

Лист — сетка предметов на белом. Делим по пустым полосам: сначала на строки,
потом каждую строку на ячейки. Строки задаются списком: сколько предметов в
каждой. Узкие щели внутри одного предмета (ложка и ключ, ребёнок и мяч)
склеиваются обратно порогом min_gap.
"""
from PIL import Image
import numpy as np
import os


def _bands(mask, min_run=10):
    out, st = [], None
    for i, v in enumerate(mask):
        if v and st is None:
            st = i
        elif not v and st is not None:
            if i - st >= min_run:
                out.append((st, i))
            st = None
    if st is not None and len(mask) - st >= min_run:
        out.append((st, len(mask)))
    return out


def _merge(bs, min_gap):
    out = [list(bs[0])]
    for a, b in bs[1:]:
        if a - out[-1][1] < min_gap:
            out[-1][1] = b
        else:
            out.append([a, b])
    return [tuple(x) for x in out]


def sheet(src, rows, names, dst='.', pad=14, row_gap=20, col_gap=40, thr=245):
    """rows — список: сколько предметов в каждой строке листа."""
    im = Image.open(src).convert('RGB')
    m = np.array(im.convert('L')) < thr
    rb = _merge(_bands(m.any(axis=1)), row_gap)
    assert len(rb) == len(rows), f'{src}: строк {len(rb)}, ждали {len(rows)}'
    boxes = []
    for (r0, r1), n in zip(rb, rows):
        sub = m[r0:r1]
        cb = _merge(_bands(sub.any(axis=0)), col_gap)
        assert len(cb) == n, f'{src}: в строке ячеек {len(cb)}, ждали {n}'
        for c0, c1 in cb:
            ys, xs = np.where(m[r0:r1, c0:c1])
            boxes.append((c0 + xs.min() - pad, r0 + ys.min() - pad,
                          c0 + xs.max() + pad + 1, r0 + ys.max() + pad + 1))
    assert len(boxes) == len(names), f'{src}: кусков {len(boxes)}, имён {len(names)}'
    os.makedirs(dst, exist_ok=True)
    for name, b in zip(names, boxes):
        b = (max(0, b[0]), max(0, b[1]), min(im.width, b[2]), min(im.height, b[3]))
        im.crop(b).save(f'{dst}/{name}.png')
        print(f'  {name:14} {b[2]-b[0]}×{b[3]-b[1]}')


def whole(src, name, dst='.'):
    os.makedirs(dst, exist_ok=True)
    im = Image.open(src).convert('RGB')
    im.save(f'{dst}/{name}.png')
    print(f'  {name:14} {im.width}×{im.height} — целиком')


def preview(names, out, src='.', cols=5, cell=230, label=26):
    from PIL import ImageDraw
    rows = (len(names) + cols - 1) // cols
    s = Image.new('RGB', (cols * cell, rows * (cell + label)), 'white')
    d = ImageDraw.Draw(s)
    for i, n in enumerate(names):
        im = Image.open(f'{src}/{n}.png').convert('RGB')
        im.thumbnail((cell - 16, cell - 16))
        x = (i % cols) * cell + (cell - im.width) // 2
        y = (i // cols) * (cell + label) + (cell - im.height) // 2
        s.paste(im, (x, y))
        d.text(((i % cols) * cell + 8, (i // cols) * (cell + label) + cell + 4), n, fill='black')
    for c in range(1, cols):
        d.line([(c * cell, 0), (c * cell, s.height)], fill=(221, 221, 221))
    for r in range(1, rows):
        d.line([(0, r * (cell + label)), (s.width, r * (cell + label))], fill=(221, 221, 221))
    s.save(out)
    print(out, s.size)
