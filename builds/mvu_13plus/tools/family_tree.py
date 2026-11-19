"""Семейное дерево для задания у семейной фотографии (замечание 17): портреты + связи линиями, под портретом только имя."""
from PIL import Image, ImageDraw, ImageFont
import os
M = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'media', 'mvu_13plus')
W, H, P = 1500, 1180, 210           # холст, размер портрета
BG, LINE, TXT = (247, 239, 224), (122, 74, 30), (42, 26, 16)
im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 40)
# центр портрета
pos = {'George': (560, 150), 'Rose': (940, 150),
       'Mark': (270, 560), 'Kate': (600, 560), 'Bob': (900, 560), 'Lily': (1230, 560),
       'Tom': (270, 960), 'Emma': (600, 960)}
files = {'George': 'fam_grandfather', 'Rose': 'fam_grandmother', 'Mark': 'fam_father', 'Kate': 'fam_mother',
         'Bob': 'fam_uncle', 'Lily': 'fam_aunt', 'Tom': 'fam_boy', 'Emma': 'fam_girl'}
lw = 7
def bottom(n): x, y = pos[n]; return x, y + P // 2 + 58
def top(n): x, y = pos[n]; return x, y - P // 2 - 6
def couple(a, b):
    (xa, ya), (xb, yb) = pos[a], pos[b]
    for dy in (-8, 8): d.line([(xa + P // 2 + 4, ya + dy), (xb - P // 2 - 4, yb + dy)], fill=LINE, width=lw - 2)
    return (xa + xb) // 2, ya
def down(frm, kids):
    x0, y0 = frm; ymid = top(kids[0])[1] - 70
    d.line([(x0, y0 + 8), (x0, ymid)], fill=LINE, width=lw)
    xs = [pos[k][0] for k in kids]
    d.line([(min(xs + [x0]), ymid), (max(xs + [x0]), ymid)], fill=LINE, width=lw)
    for k in kids: d.line([(pos[k][0], ymid), top(k)], fill=LINE, width=lw)
gr = couple('George', 'Rose'); mk = couple('Mark', 'Kate'); couple('Bob', 'Lily')
down(gr, ['Mark', 'Bob'])
down(mk, ['Tom', 'Emma'])
for n, f in files.items():
    p = Image.open(os.path.join(M, f + '.webp')).convert('RGBA'); p.thumbnail((P, P))
    x, y = pos[n]
    card = Image.new('RGBA', (P + 16, P + 16), (255, 255, 255, 255))
    im.paste(card, (x - P // 2 - 8, y - P // 2 - 8), card)
    im.paste(p, (x - p.width // 2, y - p.height // 2), p)
    d.rectangle([x - P // 2 - 8, y - P // 2 - 8, x + P // 2 + 8, y + P // 2 + 8], outline=LINE, width=4)
    tw = d.textlength(n, font=font); d.text((x - tw / 2, y + P // 2 + 14), n, font=font, fill=TXT)
im.save(os.path.join(M, 'family_tree.webp'), quality=88)
print('ok', im.size)
