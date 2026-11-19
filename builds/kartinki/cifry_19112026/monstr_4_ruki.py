"""SM0 ДЗ 3 блок 7: монстр с четырьмя руками — вторая пара рук из его же рук."""
from PIL import Image

src = Image.open('media/sm0/new/mon_purple.webp').convert('RGBA')
W, H = src.size
holst = Image.new('RGBA', (W, H), (0, 0, 0, 0))
holst.paste(src, (0, 0))

# левая рука и правая рука — кропы
levaya  = src.crop((28, 330, 178, 505))
pravaya = src.crop((425, 350, 568, 560))

# вторая пара — выше, ближе к плечам
holst.alpha_composite(levaya,  (58, 205))
holst.alpha_composite(pravaya, (398, 215))
# исходные руки поверх, чтобы стык был чистым
holst.alpha_composite(src.crop((0, 300, W, H)), (0, 300))

holst.save('media/sm0/new/mon_purple_4arms.webp', 'WEBP', quality=92)

bg = Image.new('RGB', (W, H), 'white'); bg.paste(holst, (0, 0), holst)
bg.save('/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/qc/purple4.png')
print('ok', holst.size)
