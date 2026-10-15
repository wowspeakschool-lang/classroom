"""Сетки 4×3 в натуральную величину на белом — для просмотра глазами."""
import sys, os, glob
from PIL import Image, ImageDraw, ImageFont
src, tag, sheets = sys.argv[1], sys.argv[2], sys.argv[3:]
OUT = os.environ.get('QC_OUT', 'qc')
os.makedirs(OUT, exist_ok=True)
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 16)
fs = [f for n in sheets for f in sorted(glob.glob(f'{src}/{n}/*.png'))]
for g in range(0, len(fs), 12):
    sh = Image.new('RGB', (4 * 310, 3 * 330), (225, 222, 235)); d = ImageDraw.Draw(sh)
    for k, f in enumerate(fs[g:g + 12]):
        im = Image.open(f).convert('RGBA'); bg = Image.new('RGB', im.size, 'white'); bg.paste(im, (0, 0), im)
        bg.thumbnail((300, 300)); x, y = k % 4 * 310 + 5, k // 4 * 330 + 5
        sh.paste(bg, (x, y)); d.text((x, y + 302), f.split('/')[-2] + ':' + os.path.basename(f)[:-4], fill='black', font=font)
    sh.save(f'{OUT}/{tag}_{g // 12:02d}.png')
print(len(fs))
