"""Чёрный велосипед для SM3 ДЗ 6 юнита 6 (аудирование: у Дженни велосипед)."""
from PIL import Image
import numpy as np, statistics

src = '/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/gen/out_bike/bike_black_1.png'
im = Image.open(src).convert('RGB')

# закрасить мелкую надпись на седле цветом седла
box = (548, 212, 600, 243)
okolo = im.crop((box[0]-14, box[1]-14, box[2]+14, box[3]+14))
a = np.array(okolo).reshape(-1, 3)
temn = a[a.sum(axis=1) < 260]                       # только тёмные пиксели седла
cvet = tuple(int(x) for x in np.median(temn, axis=0)) if len(temn) else (45, 45, 48)
im.paste(Image.new('RGB', (box[2]-box[0], box[3]-box[1]), cvet), box[:2])

# обрезка по содержимому и поле 6 %
a = np.array(im.convert('L'))
maska = a < 245
ys, xs = np.where(maska)
im = im.crop((xs.min(), ys.min(), xs.max()+1, ys.max()+1))
pole = int(max(im.size) * 0.06)
holst = Image.new('RGB', (im.width + 2*pole, im.height + 2*pole), 'white')
holst.paste(im, (pole, pole))
holst.thumbnail((760, 760), Image.LANCZOS)
holst.save('media/sm3/u6/gad_bike.webp', 'WEBP', quality=90)
holst.save('/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/qc/gad_bike.png')
print('gad_bike.webp', holst.size, 'цвет заплатки', cvet)
