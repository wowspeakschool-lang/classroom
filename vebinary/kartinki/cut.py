# Нарезка листа-сетки: компоненты по не-белым пикселям, раскладка по клеткам rows×cols.
import sys
from PIL import Image
import numpy as np
from scipy import ndimage

def cut(src, names, rows, cols, outdir, pad=0.08):
    im = Image.open(src).convert('RGB'); a = np.asarray(im).astype(int); H, W = a.shape[:2]
    mask = ndimage.binary_dilation(a.min(axis=2) < 232, iterations=6)
    lab, n = ndimage.label(mask); objs = ndimage.find_objects(lab); sizes = ndimage.sum(mask, lab, range(1, n + 1))
    cells = {}
    for i, sl in enumerate(objs):
        if sizes[i] < 400: continue
        cy = (sl[0].start + sl[0].stop) / 2; cx = (sl[1].start + sl[1].stop) / 2
        c = (min(rows - 1, int(cy / (H / rows))), min(cols - 1, int(cx / (W / cols))))
        b = (sl[0].start, sl[0].stop, sl[1].start, sl[1].stop)
        cells[c] = b if c not in cells else (min(cells[c][0], b[0]), max(cells[c][1], b[1]), min(cells[c][2], b[2]), max(cells[c][3], b[3]))
    out = []
    for idx, nm in enumerate(names):
        y0, y1, x0, x1 = cells[divmod(idx, cols)]
        y0 = max(0, y0 + 5); x0 = max(0, x0 + 5); y1 = min(H, y1 - 5); x1 = min(W, x1 - 5)
        crop = im.crop((x0, y0, x1, y1)); w, h = crop.size; p = int(max(w, h) * pad)
        o = Image.new('RGB', (w + 2 * p, h + 2 * p), 'white'); o.paste(crop, (p, p))
        arr = np.asarray(o).astype(int); arr[arr.min(axis=2) >= 238] = 255
        Image.fromarray(arr.astype('uint8')).save(f'{outdir}/{nm}.png', optimize=True)
        out.append((nm, o.size))
    return out
