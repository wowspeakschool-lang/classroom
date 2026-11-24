"""SM1 юнит 2 ДЗ 3: «It's a long blue train.» - вагоны длинного поезда перекрашены в синий
(были зелёный, жёлтый, оранжевый, фиолетовый). Заявка преподавателя 24.11.2026."""
import colorsys, sys
from PIL import Image
SRC = 'media/sm1/legacy/8a41095ac3a3.webp'
OUT = 'media/sm1/u2/long_blue_train.webp'
BLUE_H = colorsys.rgb_to_hsv(41/255, 99/255, 161/255)[0]   # тон синего вагона
BASES = [(42,166,4), (251,202,16), (252,80,20), (149,50,198)]  # зелёный, жёлтый, оранжевый, фиолетовый
im = Image.open(SRC).convert('RGB'); px = im.load()
W, H = im.size
def hsv(c): return colorsys.rgb_to_hsv(*[v/255 for v in c])
bh = [hsv(b)[0] for b in BASES]
BV = hsv((41, 99, 161))
bv = [hsv(b)[2] for b in BASES]
for x in range(255, W):
    for y in range(186, 247):
        r, g, b = px[x, y]; h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        if s < 0.45 or v < 0.25: continue
        d = [min(abs(h-t), 1-abs(h-t)) for t in bh]
        i = d.index(min(d))
        if d[i] > 0.05 and not (y < 238 and (h < 0.03 or h > 0.97)): continue
        if d[i] > 0.05: i = 2  # красные края оранжевого вагона
        if y >= 238 and (h < 0.03 or h > 0.97): continue  # красные ступицы колёс не трогаем
        nr, ng, nb = colorsys.hsv_to_rgb(BLUE_H, BV[1], min(1, v * BV[2] / bv[i]))
        px[x, y] = (int(nr*255), int(ng*255), int(nb*255))
# паровоз: красный корпус (без колёс) тоже в синий
RV = hsv((255, 54, 46))[2]
for x in range(30, 168):
    for y in range(150, 247):
        r, g, b = px[x, y]; h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        if s < 0.5 or v < 0.3 or not (h < 0.03 or h > 0.97): continue
        nr, ng, nb = colorsys.hsv_to_rgb(BLUE_H, BV[1], min(1, v * BV[2] / RV))
        px[x, y] = (int(nr*255), int(ng*255), int(nb*255))
im.save(OUT, 'WEBP', quality=88)
