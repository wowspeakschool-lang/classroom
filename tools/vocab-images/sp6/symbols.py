"""Знаки и числа, которые рисуем сами, а не генератор: out/<лист>/<слово>.png и out/digits/.
Знак кладётся поверх нарезки с листа (minus — генератор нарисовал непонятную сценку)."""
import os, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, '..')
from lib import fname
from sheets import S, DIGITS
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
COL = [(240, 120, 60), (70, 150, 220), (90, 180, 90), (230, 80, 120), (250, 180, 40), (150, 100, 210), (40, 170, 170)]
def draw(txt, col, path, px=300):
    k = px / 300
    im = Image.new('RGBA', (px, px), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    size = int((200 if len(txt) == 1 else 170 if len(txt) <= 2 else 120) * k)
    fnt = ImageFont.truetype(FONT, size)
    sw = round(10 * k)
    while d.textbbox((0, 0), txt, font=fnt, stroke_width=sw)[2] > 280 * k:
        size -= 6; fnt = ImageFont.truetype(FONT, size)
    b = d.textbbox((0, 0), txt, font=fnt, stroke_width=sw)
    d.text(((px - b[2] - b[0]) // 2, (px - b[3] - b[1]) // 2), txt, font=fnt, fill=col + (255,),
           stroke_width=sw, stroke_fill=(70, 40, 20, 255))
    im.save(path)
SYM = {'minus': '5 − 2'}
for n, (_, _, ws) in enumerate(S, 1):
    for i, (t, cap, _) in enumerate(ws):
        if t in SYM:
            draw(SYM[t], COL[i % len(COL)], f'out/{n}/{fname(cap)}')
            if os.path.isdir(f'out512/{n}'): draw(SYM[t], COL[i % len(COL)], f'out512/{n}/{fname(cap)}', 512)
NUM = {'eleven': '11', 'twelve': '12', 'thirteen': '13', 'fourteen': '14', 'fifteen': '15', 'sixteen': '16',
       'seventeen': '17', 'eighteen': '18', 'nineteen': '19', 'twenty': '20'}
os.makedirs('out/digits', exist_ok=True); os.makedirs('out512/digits', exist_ok=True)
for i, (t, cap, _) in enumerate(DIGITS):
    draw(NUM[t], COL[i % len(COL)], f'out/digits/{fname(cap)}')
    draw(NUM[t], COL[i % len(COL)], f'out512/digits/{fname(cap)}', 512)
print('ok', len(DIGITS))
