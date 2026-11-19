# Сцена «рядом — далеко» для WD2 ДЗ 39: пол уходит вдаль (линии перспективы),
# близкий предмет крупный внизу, дальние — маленькие у горизонта. Текста нет.
from PIL import Image, ImageDraw
import numpy as np

W, H = 1200, 700
GORIZONT = 200
STENA = (236, 243, 255)
POL1 = (245, 228, 200)
POL2 = (237, 216, 182)
KONTUR = (70, 25, 135)


def bez_fona(put, vysota):
    im = Image.open(put).convert('RGBA')
    a = np.array(im)
    a[(a[..., :3] > 236).all(axis=2), 3] = 0
    im = Image.fromarray(a, 'RGBA').crop(Image.fromarray(a, 'RGBA').getbbox())
    k = vysota / im.height
    return im.resize((max(1, int(im.width * k)), vysota), Image.LANCZOS)


h = Image.new('RGBA', (W, H), STENA + (255,))
d = ImageDraw.Draw(h)
d.rectangle((0, GORIZONT, W, H), fill=POL1 + (255,))

# полосы пола, сходящиеся к точке схода
tochka = (W // 2, GORIZONT)
kraya = [-900 + i * 300 for i in range(10)]
for i in range(len(kraya) - 1):
    if i % 2:
        continue
    d.polygon([(kraya[i], H), (kraya[i + 1], H), tochka], fill=POL2 + (255,))
d.line((0, GORIZONT, W, GORIZONT), fill=KONTUR + (255,), width=4)

# дальние предметы — маленькие, у горизонта
koshelek = bez_fona('media/wow-dragon-2/new/obj_wallet.webp', 70)
mints = bez_fona('media/wow-dragon-2/new/obj_mints.webp', 74)
d.ellipse((465, GORIZONT + 82, 555, GORIZONT + 98), fill=(226, 203, 168, 255))
d.ellipse((655, GORIZONT + 82, 745, GORIZONT + 98), fill=(226, 203, 168, 255))
h.alpha_composite(koshelek, (470, GORIZONT + 20))
h.alpha_composite(mints, (660, GORIZONT + 16))

# близкий предмет — крупный, внизу
telefon = bez_fona('media/wow-dragon-2/new/obj_smartphone.webp', 430)
d.ellipse((150, H - 70, 450, H - 20), fill=(226, 203, 168, 255))
h.alpha_composite(telefon, (170, H - telefon.height - 40))

h.convert('RGB').save('media/wow-dragon-2/new/scene_hw39_blizko_daleko.webp', 'WEBP', quality=90, method=6)
print('готово')
