"""Кадры одного героя — в одну рамку и один масштаб, чтобы смена картинки не «прыгала».
python3 builds/mvu_46/tools/norm.py   (повторный запуск безопасен: исходники берутся из media/mvu_46/hero/_src/)
Каждый кадр: обрезка по альфе, масштаб группы, вставка в общий холст по низу и центру, поле 6 %."""
import os, glob, shutil
from PIL import Image
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'media', 'mvu_46')
H, SRC = os.path.join(R, 'hero'), os.path.join(R, 'hero', '_src')
os.makedirs(SRC, exist_ok=True)
for f in glob.glob(H + '/*.webp'):
    d = os.path.join(SRC, os.path.basename(f))
    if not os.path.exists(d): shutil.copy(f, d)
def crop(p):
    im = Image.open(p).convert('RGBA'); a = im.split()[3].point(lambda v: 255 if v > 24 else 0); return im.crop(a.getbbox())
# масштаб: листы «бабушка ест» нарисованы крупнее листа с позами бабушки — приводим к одному росту
SCALE = {f'granny_eat_{x}': 545 / 685 for x in 'pizza broccoli icecream fish cake apple banana carrot'.split()}
GROUPS = {'dragon': [os.path.basename(f)[:-5] for f in glob.glob(SRC + '/dragon_*.webp')],
          'granny': [os.path.basename(f)[:-5] for f in glob.glob(SRC + '/granny_*.webp')]}
for g, names in GROUPS.items():
    ims = {}
    for n in names:
        im = crop(os.path.join(SRC, n + '.webp')); k = SCALE.get(n, 1)
        if k != 1: im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
        ims[n] = im
    W = max(i.width for i in ims.values()); Hh = max(i.height for i in ims.values()); m = int(max(W, Hh) * .06)
    for n, im in ims.items():
        c = Image.new('RGBA', (W + 2 * m, Hh + 2 * m), (0, 0, 0, 0)); c.paste(im, (m + (W - im.width) // 2, m + Hh - im.height))
        c.save(os.path.join(H, n + '.webp'), quality=88, method=6)
    print(g, len(ims), 'кадров, холст', (W + 2 * m, Hh + 2 * m))
