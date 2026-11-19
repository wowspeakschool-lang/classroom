"""Карточки-цифры в стиле Wow Dragon: жирный чёрный контур, плоский цвет."""
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
CVETA = {1: (124, 77, 255), 2: (255, 152, 0), 3: (0, 176, 118)}
RAZMER = 420

for n, cvet in CVETA.items():
    im = Image.new("RGBA", (RAZMER, RAZMER), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(FONT, 330)
    t = str(n)
    l, t_, r, b = d.textbbox((0, 0), t, font=f)
    x = (RAZMER - (r - l)) // 2 - l
    y = (RAZMER - (b - t_)) // 2 - t_
    d.text((x, y), t, font=f, fill=cvet + (255,),
           stroke_width=18, stroke_fill=(26, 26, 46, 255))
    im.save(f"media/shared/numbers/digit_{n}.webp", "WEBP", quality=92)
    print("digit_%d.webp" % n, im.size)

# превью
lst = Image.new("RGB", (RAZMER * 3 + 80, RAZMER + 40), "white")
for i, n in enumerate(sorted(CVETA)):
    c = Image.open(f"media/shared/numbers/digit_{n}.webp").convert("RGBA")
    lst.paste(c, (20 + i * (RAZMER + 20), 20), c)
lst.save("/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/qc/cifry.png")
