"""Нарезка листа на отдельные картинки с прозрачным фоном.

python3 splat/tools/cut.py лист.png папка имя1,имя2,… [--max 520]
Имена — построчно, слева направо, как в промпте. Фон — белый (у генератора почти чистый 255),
он становится прозрачным: заливкой от края по «почти белым» пикселям, так что белые
детали внутри предмета (живот пингвинёнка, снежок) не трогаются.
"""
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi


def cut(src, out_dir, names, max_side=520, grow=18, thr=10):
    im = Image.open(src).convert('RGB')
    a = np.asarray(im).astype(int)
    dist = 255 - a.min(axis=2)                       # насколько пиксель темнее белого
    fg = dist > thr
    fg = ndi.binary_opening(fg, iterations=2)
    grown = ndi.binary_dilation(fg, iterations=grow)
    lab, n = ndi.label(grown)
    sizes = ndi.sum(np.ones_like(lab), lab, range(1, n + 1))
    keep = [i + 1 for i, s in enumerate(sizes) if s > lab.size * 0.004]
    boxes = [(i, ndi.find_objects((lab == i).astype(int))[0]) for i in keep]
    # построчно: группируем по центру по вертикали
    boxes.sort(key=lambda b: (b[1][0].start + b[1][0].stop) / 2)
    rows, cur = [], []
    for b in boxes:
        cy = (b[1][0].start + b[1][0].stop) / 2
        if cur and cy - (cur[-1][1][0].start + cur[-1][1][0].stop) / 2 > a.shape[0] * 0.12:
            rows.append(cur); cur = []
        cur.append(b)
    rows.append(cur)
    ordered = [b for r in rows for b in sorted(r, key=lambda b: b[1][1].start)]
    if len(ordered) != len(names):
        raise SystemExit(f'{src}: найдено {len(ordered)} кусков, имён {len(names)}')
    for name, (i, (sy, sx)) in zip(names, ordered):
        pad = 6
        y0, y1 = max(sy.start - pad, 0), min(sy.stop + pad, a.shape[0])
        x0, x1 = max(sx.start - pad, 0), min(sx.stop + pad, a.shape[1])
        crop = a[y0:y1, x0:x1]
        own = lab[y0:y1, x0:x1] == i
        d = 255 - crop.min(axis=2)
        nearwhite = d <= 6
        bl, _ = ndi.label(nearwhite)
        border = set(np.unique(np.concatenate([bl[0], bl[-1], bl[:, 0], bl[:, -1]]))) - {0}
        bg = np.isin(bl, list(border)) | ~own
        bg = ~ndi.binary_fill_holes(~bg)          # замкнутые белые пятна внутри (глаза, блики) — часть предмета
        alpha = np.where(bg, 0, 255).astype(np.uint8)
        # мягкий край: переход 6..18 «темнее белого» у границы с фоном
        edge = ndi.binary_dilation(bg, iterations=2) & ~bg
        soft = np.clip((d - 6) / 12 * 255, 0, 255).astype(np.uint8)
        alpha = np.where(edge, np.minimum(alpha, soft), alpha)
        rgba = np.dstack([crop.astype(np.uint8), alpha])
        pim = Image.fromarray(rgba, 'RGBA')
        pim.putalpha(pim.getchannel('A').filter(ImageFilter.GaussianBlur(0.6)))
        bb = pim.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox()
        pim = pim.crop(bb)
        pim.thumbnail((max_side, max_side), Image.LANCZOS)
        pim.save(f'{out_dir}/{name}.webp', 'WEBP', quality=88, method=6)
        print(name, pim.size)


if __name__ == '__main__':
    args = sys.argv[1:]
    opt = {'--max': 520, '--grow': 18, '--thr': 10}
    for key in list(opt):
        if key in args:
            k = args.index(key); opt[key] = int(args[k + 1]); del args[k:k + 2]
    cut(args[0], args[1], args[2].split(','), opt['--max'], opt['--grow'], opt['--thr'])
