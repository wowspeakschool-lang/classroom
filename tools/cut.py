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


def blobs(src, n, names, dst='.', pad=14, thr=245, join=34, min_area=1500):
    """Режет лист по связным пятнам, а не по щелям между рядами.

    Генератор часто ставит предметы вплотную: между двумя рядами остаётся
    пиксель, и проекция их уже не разделяет. Пятна разделяют, потому что
    предметы всё равно не соприкасаются. Куски одного предмета (лимон, половинка
    и листик) собираются обратно: прямоугольники ближе join пикселей — один
    предмет. Порядок — построчно сверху вниз, внутри строки слева направо,
    как в промпте.
    """
    from scipy import ndimage
    im = Image.open(src).convert('RGB')
    m = np.array(im.convert('L')) < thr
    lab, k = ndimage.label(m)
    boxes = []
    for sy, sx in ndimage.find_objects(lab):
        if (sy.stop - sy.start) * (sx.stop - sx.start) >= min_area:
            boxes.append([sx.start, sy.start, sx.stop, sy.stop])

    # склеиваем куски одного предмета: пока есть близкие прямоугольники
    merged = True
    while merged:
        merged = False
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                a, b = boxes[i], boxes[j]
                dx = max(0, max(a[0], b[0]) - min(a[2], b[2]))
                dy = max(0, max(a[1], b[1]) - min(a[3], b[3]))
                if dx < join and dy < join:
                    boxes[i] = [min(a[0], b[0]), min(a[1], b[1]),
                                max(a[2], b[2]), max(a[3], b[3])]
                    boxes.pop(j); merged = True; break
            if merged:
                break
    assert len(boxes) == n, f'{src}: пятен {len(boxes)}, ждали {n}'

    # раскладываем построчно: новая строка, когда предмет начинается ниже
    # середины предыдущего
    boxes.sort(key=lambda b: b[1])
    rows, cur = [], [boxes[0]]
    for b in boxes[1:]:
        if b[1] > (cur[-1][1] + cur[-1][3]) / 2:
            rows.append(cur); cur = [b]
        else:
            cur.append(b)
    rows.append(cur)
    order = [b for r in rows for b in sorted(r, key=lambda b: b[0])]
    assert len(order) == len(names), f'{src}: кусков {len(order)}, имён {len(names)}'

    os.makedirs(dst, exist_ok=True)
    for name, b in zip(names, order):
        box = (max(0, b[0] - pad), max(0, b[1] - pad),
               min(im.width, b[2] + pad), min(im.height, b[3] + pad))
        im.crop(box).save(f'{dst}/{name}.png')
        print(f'  {name:22} {box[2]-box[0]}×{box[3]-box[1]}')


def _seams(profile, k, span=0.35):
    """k-1 позиций разреза: там, где краски меньше всего, рядом с ожидаемой границей."""
    n = len(profile)
    cuts = []
    for i in range(1, k):
        c = i * n / k
        w = int(span * n / k)
        lo, hi = max(1, int(c - w)), min(n - 1, int(c + w))
        seg = profile[lo:hi]
        cuts.append(lo + int(np.argmin(seg)))
    return cuts


def seams(src, rows, names, dst='.', pad=10, thr=245):
    """Режет лист, даже если предметы соприкасаются.

    Пятна и щели не помогают, когда генератор поставил предметы вплотную.
    Тогда режем по шву: берём профиль краски и ищем в нём самое светлое место
    рядом с ожидаемой границей ячейки. Каждую ячейку потом обжимаем по её
    собственным краям, так что небольшой промах шва ничего не портит.
    """
    im = Image.open(src).convert('RGB')
    m = np.array(im.convert('L')) < thr
    ys, xs = np.where(m)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    sub = m[y0:y1, x0:x1]

    hcuts = [0] + _seams(sub.sum(axis=1), len(rows)) + [sub.shape[0]]
    os.makedirs(dst, exist_ok=True)
    out = []
    for r, k in enumerate(rows):
        band = sub[hcuts[r]:hcuts[r + 1]]
        vcuts = [0] + _seams(band.sum(axis=0), k) + [band.shape[1]]
        for c in range(k):
            cell = band[:, vcuts[c]:vcuts[c + 1]]
            cys, cxs = np.where(cell)
            out.append((x0 + vcuts[c] + cxs.min(), y0 + hcuts[r] + cys.min(),
                        x0 + vcuts[c] + cxs.max() + 1, y0 + hcuts[r] + cys.max() + 1))
    assert len(out) == len(names), f'{src}: ячеек {len(out)}, имён {len(names)}'
    for name, b in zip(names, out):
        box = (max(0, b[0] - pad), max(0, b[1] - pad),
               min(im.width, b[2] + pad), min(im.height, b[3] + pad))
        im.crop(box).save(f'{dst}/{name}.png')
        print(f'  {name:22} {box[2]-box[0]}×{box[3]-box[1]}')


def clean(path, thr=245, pad=10, share=0.15):
    """Убирает с куска обрезки соседей.

    После резки тесного листа в углу остаётся край чужого предмета. Признак
    именно обрезка: пятно упирается в край кадра и заметно меньше главного.
    Половинка лимона или листик внутрь кадра помещаются целиком, их это
    правило не трогает.
    """
    from scipy import ndimage
    im = Image.open(path).convert('RGB')
    a = np.array(im)
    m = np.array(im.convert('L')) < thr
    lab, k = ndimage.label(m)
    if k < 2:
        return 0
    sizes = ndimage.sum(m, lab, range(1, k + 1))
    big = sizes.max()
    h, w = m.shape
    drop_ids = []
    for i, (sy, sx) in enumerate(ndimage.find_objects(lab), start=1):
        touches = (sy.start == 0 or sx.start == 0 or sy.stop == h or sx.stop == w)
        if touches and sizes[i - 1] < share * big:
            drop_ids.append(i)
    if not drop_ids:
        return 0
    a[np.isin(lab, drop_ids)] = 255
    im2 = Image.fromarray(a)
    m2 = np.array(im2.convert('L')) < thr
    ys, xs = np.where(m2)
    im2.crop((max(0, xs.min() - pad), max(0, ys.min() - pad),
              min(im2.width, xs.max() + 1 + pad),
              min(im2.height, ys.max() + 1 + pad))).save(path)
    return len(drop_ids)


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
