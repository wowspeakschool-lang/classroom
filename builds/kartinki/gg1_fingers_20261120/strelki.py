"""Стрелки к пальцам на карточке fingers (GG1 юнит 4): просьба Анны 20.11.2026.
Без стрелок карточка не отличается от hand — ребёнок видит ту же ладонь."""
from PIL import Image, ImageDraw
import math, sys

SRC = 'media/gg1/u4/body_fingers.webp'
DST = sys.argv[1] if len(sys.argv) > 1 else SRC
KRASNYJ = (226, 48, 48)
POLE = 70

im = Image.open(SRC).convert('RGB')
holst = Image.new('RGB', (im.width + 2 * POLE, im.height + POLE), 'white')
holst.paste(im, (POLE, POLE))
d = ImageDraw.Draw(holst)

# концы стрелок — кончики пальцев в координатах исходника + поле
TIPS = [((110, 25), (152, 100)), ((235, 18), (235, 62)), ((382, 25), (338, 100)),
        ((452, 118), (394, 176)), ((18, 252), (74, 228))]

def strelka(nachalo, konec, cvet, shirina, golova):
    dx, dy = konec[0] - nachalo[0], konec[1] - nachalo[1]
    dl = math.hypot(dx, dy); ux, uy = dx / dl, dy / dl
    hvost = (konec[0] - ux * golova * 1.6, konec[1] - uy * golova * 1.6)
    d.line([nachalo, hvost], fill=cvet, width=shirina)
    px, py = -uy, ux
    d.polygon([(hvost[0] + px * golova, hvost[1] + py * golova),
               (hvost[0] - px * golova, hvost[1] - py * golova),
               konec], fill=cvet)

for a, b in TIPS:
    strelka(a, b, (255, 255, 255), 16, 15)   # белая обводка
for a, b in TIPS:
    strelka(a, b, KRASNYJ, 8, 10)

holst.save(DST, 'WEBP', quality=90)
print(DST, holst.size)
