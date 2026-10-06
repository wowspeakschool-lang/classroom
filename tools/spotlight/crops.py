"""Страницы Word List -> куски: колонка (лев/прав) x половина (верх/низ), режем по пустым полосам."""
import pymupdf, numpy as np, os, json
from PIL import Image
BOOKS = {  # класс: [(файл, первая, последняя страница)]
 2: [('2 (1).pdf',0,1),('2 (2).pdf',0,2)],
 3: [('3 (1).pdf',4,7),('3 (2).pdf',3,6)],
 4: [('4 (1).pdf',4,7),('4 (2).pdf',5,7)],
 5: [('Spotlight_5_SB.pdf',17,33)],
 6: [('Spotlight 6 SB-страницы.pdf',9,16)],
 7: [('Spotlight_7_SB.pdf',11,26)],
 8: [('Spotlight_8_SB.pdf',23,46)],
 9: [('Spotlight_9_SB-страницы.pdf',28,50)],
}
def gap(prof, lo, hi):
    seg = prof[lo:hi]; return lo + int(np.argmin(np.convolve(seg, np.ones(9), 'same')))
idx = {}
for g, parts in BOOKS.items():
    out = f'crops/{g}'; os.makedirs(out, exist_ok=True); n = 0; lst = []
    for f, a, b in parts:
        d = pymupdf.open('pdf/' + f)
        for p in range(a, b + 1):
            pm = d[p].get_pixmap(dpi=200)
            im = Image.frombytes('RGB', (pm.width, pm.height), pm.samples)
            ink = np.array(im.convert('L')) < 150
            W, H = im.size
            x = gap(ink.sum(0), int(W * .4), int(W * .6))
            for side, (x0, x1) in (('L', (0, x)), ('R', (x, W))):
                col = ink[:, x0:x1]
                y = gap(col.sum(1), int(H * .4), int(H * .6))
                for half, (y0, y1) in (('a', (0, y)), ('b', (y, H))):
                    n += 1
                    name = f'{out}/{n:03d}_p{p}{side}{half}.png'
                    im.crop((x0, y0, x1, y1)).save(name); lst.append(name)
    idx[g] = lst; print(g, len(lst))
json.dump(idx, open('crops/index.json', 'w'), indent=0)
