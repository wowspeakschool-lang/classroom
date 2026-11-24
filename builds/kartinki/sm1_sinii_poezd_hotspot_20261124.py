"""Подменяет длинный поезд в общей картинке SM1 юнит 2 ДЗ 3 блок 8 (hotspot) на синий."""
from PIL import Image
HS = 'media/sm1/legacy/2b7d0d001037.webp'
NEW = 'media/sm1/u2/long_blue_train.webp'
OUT = 'media/sm1/u2/toys_hotspot_blue_train.webp'
def bbox_nonwhite(im, box):
    x0, y0, x1, y1 = box; px = im.load(); xs = []; ys = []
    for x in range(x0, x1):
        for y in range(y0, y1):
            r, g, b = px[x, y]
            if min(r, g, b) < 200: xs.append(x); ys.append(y)
    return min(xs), min(ys), max(xs) + 1, max(ys) + 1
hs = Image.open(HS).convert('RGB'); new = Image.open(NEW).convert('RGB')
tb = bbox_nonwhite(hs, (505, 560, 1010, 780))          # поезд внутри панели 5
nb = bbox_nonwhite(new, (25, 120, 595, 330))           # поезд внутри новой картинки
train = new.crop(nb).resize((tb[2] - tb[0], tb[3] - tb[1]), Image.LANCZOS)
pad = 4
hs.paste((255, 255, 255), (tb[0] - pad, tb[1] - pad, tb[2] + pad, tb[3] + pad))
hs.paste(train, tb[:2])
hs.save(OUT, 'WEBP', quality=88)
print(tb, nb)
