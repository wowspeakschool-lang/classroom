"""Контактный лист: фоны и предметы (на сером, чтобы видно прозрачность) + проба комнаты."""
import sys, os
from PIL import Image, ImageDraw, ImageFont
M = 'media/mvu_13plus'
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 22)
def sheet(names, out, cell=300, cols=3, bg=(70, 70, 78)):
    rows = (len(names) + cols - 1) // cols
    W = Image.new('RGB', (cols * cell, rows * (cell + 34)), (245, 245, 245))
    d = ImageDraw.Draw(W)
    for i, n in enumerate(names):
        im = Image.open(f'{M}/{n}.webp').convert('RGBA')
        im.thumbnail((cell - 20, cell - 20))
        x, y = (i % cols) * cell, (i // cols) * (cell + 34)
        tile = Image.new('RGBA', (cell - 8, cell - 8), bg + (255,))
        tile.alpha_composite(im, ((cell - 8 - im.width) // 2, (cell - 8 - im.height) // 2))
        W.paste(tile.convert('RGB'), (x + 4, y + 4))
        d.text((x + 8, y + cell), f'{n}  {Image.open(f"{M}/{n}.webp").size[0]}×{Image.open(f"{M}/{n}.webp").size[1]}', fill=(20, 20, 20), font=F)
    W.save(out)
def room(bg, items, out):
    R = Image.open(f'{M}/{bg}.webp').convert('RGBA')
    for n, x, y, h in items:
        im = Image.open(f'{M}/{n}.webp').convert('RGBA')
        im = im.resize((round(im.width * h / im.height), h), Image.LANCZOS)
        glow = Image.new('RGBA', im.size, (255, 220, 120, 0))
        R.alpha_composite(im, (x - im.width // 2, y - im.height))
    R.convert('RGB').save(out, quality=85)
if __name__ == '__main__':
    o = sys.argv[1]
    sheet(['room1_living', 'room2_study', 'room3_lab', 'door_open'], f'{o}/kl_fony.png', cell=420, cols=2)
    sheet(['family_photo', 'schoolbag', 'passport', 'fruit_bowl', 'football', 'bus', 'cinema_tickets', 'umbrella', 'cat'], f'{o}/kl_p1.png')
    room('room1_living', [('family_photo', 1290, 520, 120), ('bus', 1430, 520, 62),
          ('fruit_bowl', 760, 700, 95), ('cinema_tickets', 900, 705, 55), ('passport', 620, 708, 52),
          ('umbrella', 1180, 860, 150), ('schoolbag', 470, 905, 190), ('football', 330, 1000, 105),
          ('cat', 1080, 1000, 175)], f'{o}/proba_room1.jpg')
