"""Картинка для «подпиши части тела» (GG1 юнит 4 ДЗ 3): лицо крупно слева,
фигура целиком справа. Одной фигуры мало — кружки платформы налезают на нос и рот."""
from PIL import Image, ImageChops, ImageDraw
import json, sys

SRC = sys.argv[1]
DST = sys.argv[2]
im = Image.open(SRC).convert('RGB')

# фигура целиком: обрезаем белые поля
bg = Image.new('RGB', im.size, (255, 255, 255))
d = ImageChops.difference(im, bg).convert('L').point(lambda x: 255 if x > 12 else 0)
figura = im.crop(d.getbbox())

golova = im.crop((380, 5, 650, 335))          # лицо и шея

H = 900                                        # высота панелей
f = figura.resize((int(figura.width * H / figura.height), H), Image.LANCZOS)
g = golova.resize((int(golova.width * H / golova.height), H), Image.LANCZOS)

ZAZOR = 60
holst = Image.new('RGB', (g.width + ZAZOR + f.width + 80, H + 80), 'white')
holst.paste(g, (40, 40))
holst.paste(f, (40 + g.width + ZAZOR, 40))
holst.save(DST, 'WEBP', quality=90)
print(DST, holst.size, 'лицо', g.size, 'фигура', f.size)
print(json.dumps({'golova_x': 40, 'golova_w': g.width, 'figura_x': 40 + g.width + ZAZOR,
                  'figura_w': f.width, 'y0': 40, 'h': H,
                  'holst': holst.size, 'golova_box': [380, 5, 650, 335],
                  'figura_box': list(d.getbbox())}))
