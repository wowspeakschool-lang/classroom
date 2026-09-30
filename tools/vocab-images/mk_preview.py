"""Превью нарезки: по файлу на лист, картинки на шахматке — видно прозрачность."""
import os, sys
from PIL import Image, ImageDraw, ImageFont
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
font = ImageFont.truetype(F, 15) if os.path.exists(F) else ImageFont.load_default()
os.makedirs('preview', exist_ok=True)
for d in sys.argv[1:] or sorted(os.listdir('out')):
    fs = sorted(f for f in os.listdir('out/' + d) if f.endswith('.png'))
    cols = 5; rows = (len(fs) + cols - 1) // cols; W, H = 300, 330
    sh = Image.new('RGB', (cols * W + 20, rows * H + 20), (255, 255, 255)); dr = ImageDraw.Draw(sh)
    for k, f in enumerate(fs):
        x = 10 + k % cols * W; y = 10 + k // cols * H
        bg = Image.new('RGB', (290, 290), (214, 230, 245)); bd = ImageDraw.Draw(bg)
        for i in range(0, 290, 20):
            for j in range(0, 290, 20):
                if (i // 20 + j // 20) % 2: bd.rectangle((i, j, i + 19, j + 19), fill=(236, 242, 250))
        im = Image.open('out/' + d + '/' + f).resize((290, 290))
        bg.paste(im, (0, 0), im); sh.paste(bg, (x, y))
        dr.text((x + 4, y + 294), f[:-4].replace('_', ' '), fill=(0, 0, 0), font=font)
    sh.save(f'preview/{d}.png'); print(d, len(fs))
