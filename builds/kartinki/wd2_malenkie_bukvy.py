# Маленькие b и d в стиле курса: берём готовую маленькую p (bubble-буква),
# переворачиваем и перекрашиваем заливку, контур остаётся прежним.
from PIL import Image
import numpy as np

SRC = 'media/wow-dragon-2/legacy/a1d9a00ffd77.webp'   # маленькая p
KONTUR = np.array([70, 25, 135], float)
ZALIVKA_P = np.array([180, 116, 245], float)
SINIY = np.array([110, 205, 245], float)      # как у большой B
ZHELTYY = np.array([247, 196, 53], float)     # как у большой D


def perekrasit(im, novaya):
    a = np.array(im).astype(float)
    rgb, al = a[..., :3], a[..., 3:]
    os_ = ZALIVKA_P - KONTUR
    t = ((rgb - KONTUR) @ os_) / (os_ @ os_)
    t = np.clip(t, 0, 1)[..., None]
    new = KONTUR + t * (novaya - KONTUR)
    return Image.fromarray(np.concatenate([new, al], axis=2).astype(np.uint8), 'RGBA')


p = Image.open(SRC).convert('RGBA')
b = perekrasit(p.transpose(Image.FLIP_TOP_BOTTOM), SINIY)
d = perekrasit(p.transpose(Image.ROTATE_180), ZHELTYY)
b.save('media/wow-dragon-2/new/letter_b_small.webp', 'WEBP', quality=92, method=6)
d.save('media/wow-dragon-2/new/letter_d_small.webp', 'WEBP', quality=92, method=6)
print('готово')
