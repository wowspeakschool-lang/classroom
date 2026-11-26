# Значки шифра (листы Анны, 26.11.2026) → media/reading10/cipher/<буква>.webp с прозрачным фоном
import sys, numpy as np
from PIL import Image, ImageDraw, ImageFilter
SRC, OUT = sys.argv[1], sys.argv[2]
SHEETS = {'12.webp': 'abcdefg', '10.webp': 'hijklmn', '11.webp': 'opqrst', '13.webp': 'uvwxyz'}
def bands(mask, axis, gap):
    p = mask.any(axis=axis); res = []; on = False; st = 0; blank = 0
    for k, v in enumerate(p):
        if v:
            if not on: on, st = True, k
            blank = 0
        elif on:
            blank += 1
            if blank > gap: res.append((st, k - blank + 1)); on = False
    if on: res.append((st, len(p)))
    return [b for b in res if b[1] - b[0] > 30]
def clean(t):
    # убрать мелкие оторванные кусочки (осколки соседнего предмета), оставить крупные части
    a = np.asarray(t.getchannel('A')) > 70; h, w = a.shape; lab = np.zeros((h, w), int); sizes = {}; n = 0
    for y0 in range(h):
        for x0 in range(w):
            if a[y0, x0] and not lab[y0, x0]:
                n += 1; st = [(y0, x0)]; lab[y0, x0] = n; c = 0
                while st:
                    y, x = st.pop(); c += 1
                    for yy, xx in ((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
                        if 0 <= yy < h and 0 <= xx < w and a[yy, xx] and not lab[yy, xx]: lab[yy, xx] = n; st.append((yy, xx))
                sizes[n] = c
    big = max(sizes.values()); keep = {k for k, v in sizes.items() if v >= big * 0.02}
    al = np.asarray(t.getchannel('A')).copy(); grow = np.isin(lab, list(keep))
    from PIL import ImageFilter
    km = Image.fromarray((grow * 255).astype('uint8')).filter(ImageFilter.MaxFilter(5))
    al[np.asarray(km) == 0] = 0; t.putalpha(Image.fromarray(al)); return t.crop(t.getchannel('A').getbbox())
def cut(im):
    mask = np.asarray(im.getchannel('A')) > 70
    out = []
    for r0, r1 in bands(mask, 1, 8):
        for c0, c1 in bands(mask[r0:r1], 0, 6):
            rr = np.where(mask[r0:r1, c0:c1].any(axis=1))[0]
            out.append((c0, r0 + rr[0], c1, r0 + rr[-1] + 1))
    return out
def transparent(c):
    a = np.asarray(c).astype(int); h, w = a.shape[:2]
    cand = ((a.min(axis=2) >= 232) & (a.max(axis=2) - a.min(axis=2) < 16)).astype('uint8') * 255
    m = Image.fromarray(cand, 'L')
    for x, y in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)] + [(x, 0) for x in range(0, w, 25)] + [(x, h - 1) for x in range(0, w, 25)] + [(0, y) for y in range(0, h, 25)] + [(w - 1, y) for y in range(0, h, 25)]:
        if m.getpixel((x, y)) == 255: ImageDraw.floodfill(m, (x, y), 128)
    bg = np.asarray(m) == 128
    alpha = Image.fromarray(np.where(bg, 0, 255).astype('uint8'), 'L').filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    rgba = c.convert('RGBA'); rgba.putalpha(alpha); return rgba
for f, letters in SHEETS.items():
    im = Image.open(f'{SRC}/{f}').convert('RGBA'); bx = cut(im)
    if len(bx) == len(letters) - 1:  # два предмета слиплись краями — делим самый широкий по самому пустому столбцу
        k = max(range(len(bx)), key=lambda j: bx[j][2] - bx[j][0]); x0, y0, x1, y1 = bx[k]
        col = (np.asarray(im.getchannel('A'))[y0:y1, x0:x1] > 70).sum(axis=0); w = x1 - x0
        sx = x0 + int(w * .3) + int(np.argmin(col[int(w * .3):int(w * .7)]))
        bx[k:k + 1] = [(x0, y0, sx, y1), (sx, y0, x1, y1)]
    if len(bx) != len(letters): print('!!', f, len(bx), bx); continue
    for b, l in zip(bx, letters):
        pad = 14; x0, y0, x1, y1 = max(0, b[0] - pad), max(0, b[1] - pad), min(im.width, b[2] + pad), min(im.height, b[3] + pad)
        t = im.crop((x0, y0, x1, y1)); a = t.getchannel('A').point(lambda v: 0 if v < 24 else v); t.putalpha(a); t = clean(t.crop(a.getbbox()))
        s = max(t.size); sq = Image.new('RGBA', (int(s * 1.08), int(s * 1.08)), (0, 0, 0, 0)); sq.paste(t, ((sq.width - t.width) // 2, (sq.height - t.height) // 2))
        sq.thumbnail((360, 360), Image.LANCZOS); sq.save(f'{OUT}/{l}.webp', quality=90); print(l, t.size, end='  ')
    print()
