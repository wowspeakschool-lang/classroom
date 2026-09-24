"""Перекраска в целевой цвет — только основной цвет предмета.

Простой сдвиг всех цветных пикселей делает машинку одноцветной: синие окна,
жёлтые фары и зелёный стебель цветка красятся вместе с кузовом. Поэтому
сначала ищем господствующий тон (самая большая цветная область), и красим
только его — остальное остаётся как было.
"""
from PIL import Image, ImageChops

S_MIN, V_MIN, SPREAD = 38, 30, 30   # spread — полуширина тона в шкале 0..255


def dominant_hue(im):
    h, s, v = im.convert("HSV").split()
    hist = [0] * 256
    hp, sp, vp = h.load(), s.load(), v.load()
    w, ht = im.size
    for y in range(0, ht, 3):
        for x in range(0, w, 3):
            if sp[x, y] >= S_MIN and vp[x, y] >= V_MIN:
                hist[hp[x, y]] += 1
    # берём не одиночный пик, а лучшее окно шириной 2*SPREAD
    best, best_sum = 0, -1
    for c in range(256):
        total = sum(hist[(c + d) % 256] for d in range(-SPREAD, SPREAD + 1))
        if total > best_sum:
            best, best_sum = c, total
    return best


def recolor(im, target_hue_deg, src_hue=None):
    im = im.convert("RGBA")
    alpha = im.getchannel("A")
    hsv = im.convert("RGB").convert("HSV")
    h, s, v = hsv.split()
    src = dominant_hue(im) if src_hue is None else src_hue

    # маска: тон рядом с господствующим, достаточно цветной и не чёрный
    shifted = h.point(lambda p: (p - src + 128) % 256)          # пик в центр
    near = shifted.point(lambda p: 255 if abs(p - 128) <= SPREAD else 0)
    mask = ImageChops.multiply(near, s.point(lambda p: 255 if p >= S_MIN else 0))
    mask = ImageChops.multiply(mask, v.point(lambda p: 255 if p >= V_MIN else 0))

    tgt = int(round(target_hue_deg / 360 * 256)) % 256
    new_h = Image.composite(Image.new("L", im.size, tgt), h, mask)
    out = Image.merge("HSV", (new_h, s, v)).convert("RGB").convert("RGBA")
    out.putalpha(alpha)
    return out
