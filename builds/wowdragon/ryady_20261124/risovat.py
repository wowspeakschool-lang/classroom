"""Ряды для «Продолжи ряд» WD1 ДЗ 46 и 47 (вопросы 2 и 3) - в стиле row_*_q.webp.
24.11.2026: у этих вопросов не было картинки, ряд давала запись, её сняли 11.11."""
from PIL import Image, ImageDraw
SRC = 'media/wow-dragon-1/new/'
OUT = 'media/wow-dragon-1/new/'
LINE = (55, 8, 99); W = 5; S = 4  # supersample
COL = {'orange': (254, 141, 40), 'pink': (254, 84, 150), 'white': (255, 255, 255),
       'blue': (103, 192, 250), 'yellow': (253, 200, 30), 'green': (69, 204, 74)}
cloud = Image.open(SRC + 'row_orange_pink_q.webp').convert('RGB').crop((410, 0, 600, 166))

def row(items, name):
    n = len(items); pitch = 135; c0 = 78
    width = c0 + (n - 1) * pitch + 55 + 6 + cloud.width
    big = Image.new('RGB', (width * S, 166 * S), 'white'); d = ImageDraw.Draw(big)
    for i, (shape, col) in enumerate(items):
        cx, cy = (c0 + i * pitch) * S, 83 * S
        if shape == 'circle':
            r = 54 * S; d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=COL[col], outline=LINE, width=W * S)
        elif shape == 'square':
            r = 50 * S; d.rectangle((cx - r, cy - r, cx + r, cy + r), fill=COL[col], outline=LINE, width=W * S)
        else:
            h = 52 * S; pts = [(cx, cy - h), (cx + 56 * S, cy + 44 * S), (cx - 56 * S, cy + 44 * S)]
            d.polygon(pts, fill=COL[col]); d.line(pts + [pts[0]], fill=LINE, width=W * S, joint='curve')
    im = big.resize((width, 166), Image.LANCZOS)
    im.paste(cloud, (width - cloud.width, 0))
    im.save(OUT + name, 'WEBP', quality=90)
    return im

row([('circle','white'),('circle','pink'),('circle','white'),('circle','pink'),('circle','white')], 'row_white_pink_q.webp')
row([('circle','orange'),('circle','orange'),('circle','pink'),('circle','orange'),('circle','orange')], 'row_orange_orange_pink_q.webp')
row([('square','blue'),('triangle','yellow'),('square','blue'),('triangle','yellow'),('square','blue')], 'row_square_triangle_q.webp')
row([('triangle','orange'),('circle','yellow'),('circle','yellow'),('triangle','orange'),('circle','yellow')], 'row_triangle_circle_circle_q.webp')
