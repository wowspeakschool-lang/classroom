"""Превью партии: python3 preview.py batch1.json → preview/batch1_<n>.jpg (по 12 на лист, с переводом)."""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, '..')
from lib import fname
here = os.path.dirname(os.path.abspath(__file__))
f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
src = sys.argv[1]; name = os.path.splitext(os.path.basename(src))[0]
jobs = json.load(open(src))
ts = [t for t in jobs if os.path.exists(f'{here}/real/out512/{fname(t)}')]
os.makedirs(f'{here}/preview', exist_ok=True)
for p in range(0, len(ts), 12):
    part = ts[p:p + 12]; rows = (len(part) + 3) // 4
    sh = Image.new('RGB', (4 * 380 + 10, rows * 430 + 10), (225, 222, 235)); d = ImageDraw.Draw(sh)
    for k, t in enumerate(part):
        x = 10 + k % 4 * 380; y = 10 + k // 4 * 430
        sh.paste(Image.open(f'{here}/real/out512/{fname(t)}').convert('RGB').resize((370, 370)), (x, y))
        ru = jobs[t]['ru'] if isinstance(jobs[t], dict) else ''
        d.text((x + 4, y + 374), f'{p + k + 1}. {t}', fill='black', font=f); d.text((x + 4, y + 394), ru[:44], fill=(90, 90, 90), font=f)
    sh.save(f'{here}/preview/{name}_{p // 12 + 1}.jpg', quality=86)
print(len(ts))
