"""Перекраска в целевой цвет — только основной цвет предмета.

Простой сдвиг всех цветных пикселей делает машинку одноцветной: синие окна,
жёлтые фары и зелёный стебель цветка красятся вместе с кузовом. Поэтому
сначала ищем господствующий тон (самая большая цветная область), и красим
только его — остальное остаётся как было.
"""
from PIL import Image, ImageChops

S_MIN, V_MIN, SPREAD = 38, 30, 30   # spread — полуширина тона в шкале 0..255

# Господствующий тон ищем по уверенно цветным пикселям (S_MIN), а красим и
# бледные тоже (S_PALE). Блик на лепестке — тот же розовый, но выцветший:
# при пороге 38 он оставался розовым, и на зелёном цветке по лепесткам шли
# розовые полосы. Совсем бесцветное (S < S_PALE) не трогаем: у ботинок от
# этого позеленела бы белая подошва.
S_PALE = 12


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


def recolor(im, target_hue_deg, src_hue=None, whole=False, sat=1.0, val=1.0):
    """whole=True — красить весь предмет, не только господствующий тон.

    Нужно там, где предмет одноцветный по замыслу, а генератор развёл в нём
    два-три тона: у цветка стебель попадал в полосу лишь частично, и на синем
    цветке он выходил в полоску — где синий, где зелёный.

    val — множитель яркости; вместе с sat=0 даёт «бесцветную» вещь для
    задания «раскрась». Одной обесцветки мало: вещь выходит почти белой и
    на светлом фоне теряется.

    sat — множитель насыщенности для перекрашенного. Цветок в исходнике
    пастельный (медиана 122 против 200 у шарика и кружки), и рядом с ними
    его зелёный читался другим цветом. На уроке цветов это путает.
    """
    im = im.convert("RGBA")
    alpha = im.getchannel("A")
    hsv = im.convert("RGB").convert("HSV")
    h, s, v = hsv.split()
    src = dominant_hue(im) if src_hue is None else src_hue

    # маска: тон рядом с господствующим, достаточно цветной и не чёрный
    shifted = h.point(lambda p: (p - src + 128) % 256)          # пик в центр
    near = shifted.point(lambda p: 255 if abs(p - 128) <= SPREAD else 0)
    if whole:
        near = Image.new("L", im.size, 255)
    mask = ImageChops.multiply(near, s.point(lambda p: 255 if p >= S_PALE else 0))
    mask = ImageChops.multiply(mask, v.point(lambda p: 255 if p >= V_MIN else 0))

    tgt = int(round(target_hue_deg / 360 * 256)) % 256
    new_h = Image.composite(Image.new("L", im.size, tgt), h, mask)
    new_s = s
    if sat != 1.0:
        up = s.point(lambda p: min(255, int(p * sat)))
        new_s = Image.composite(up, s, mask)
    new_v = v
    if val != 1.0:
        down = v.point(lambda p: max(0, min(255, int(p * val))))
        new_v = Image.composite(down, v, mask)
    out = Image.merge("HSV", (new_h, new_s, new_v)).convert("RGB").convert("RGBA")
    out.putalpha(alpha)
    return out
