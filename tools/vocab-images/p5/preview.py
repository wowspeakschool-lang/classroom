"""Превью нарезанных листов Prepare 4 в порядке промпта: python3 preview.py 1 2 3"""
import os, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, '..')
from lib import fname
from sheets import S
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
os.makedirs('preview', exist_ok=True)
for n in map(int, sys.argv[1:]):
    fs = [fname(t) for _, t, _ in S[n - 1][2]]
    rows = (len(fs) + 4) // 5
    sh = Image.new('RGB', (1520, rows * 330 + 20), 'white'); dr = ImageDraw.Draw(sh)
    for k, f in enumerate(fs):
        x = 10 + k % 5 * 300; y = 10 + k // 5 * 330
        bg = Image.new('RGB', (290, 290), (214, 230, 245)); bd = ImageDraw.Draw(bg)
        for i in range(0, 290, 20):
            for j in range(0, 290, 20):
                if (i // 20 + j // 20) % 2: bd.rectangle((i, j, i + 19, j + 19), fill=(236, 242, 250))
        im = Image.open(f'out/{n}/{f}').resize((290, 290)); bg.paste(im, (0, 0), im); sh.paste(bg, (x, y))
        dr.text((x + 4, y + 294), f[:-4].replace('_', ' '), fill='black', font=font)
    sh.save(f'preview/{n}.png')
