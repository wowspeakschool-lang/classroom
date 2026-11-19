from PIL import Image, ImageDraw, ImageFilter
import numpy as np

src = '/home/user/classroom/media/wow-dragon-2/legacy/68aa77cdcd12.webp'
im = Image.open(src).convert('RGBA')
arr = np.array(im)
H, W = arr.shape[:2]
yy, xx = np.mgrid[0:H, 0:W]

eyes = [(132, 124, 17), (205, 137, 18)]

for cx, cy, r in eyes:
    dist2 = (xx-cx)**2 + (yy-cy)**2
    ring = (dist2 > (r+2)**2) & (dist2 <= (r+7)**2)
    px = arr[ring][:, :3].astype(int)
    goden = (px[:,2] > px[:,0] + 20) & (px.sum(axis=1) > 320)   # голубое, не контур и не тень
    cvet = np.median(px[goden], axis=0).astype(np.uint8)
    hole = dist2 <= r*r
    arr[hole, 0], arr[hole, 1], arr[hole, 2] = cvet
    arr[hole, 3] = 255

im2 = Image.fromarray(arr, 'RGBA')
# лёгкое размытие только по заплатке, чтобы край не был резким
blur = im2.filter(ImageFilter.GaussianBlur(1.6))
mask = Image.new('L', (W, H), 0)
md = ImageDraw.Draw(mask)
for cx, cy, r in eyes:
    md.ellipse((cx-r-2, cy-r-2, cx+r+2, cy+r+2), fill=255)
im2 = Image.composite(blur, im2, mask)

d = ImageDraw.Draw(im2)
TEMNO = (45, 40, 92, 255)
for cx, cy, r in eyes:
    rx, ry = 12, 13
    d.ellipse((cx-rx, cy-ry, cx+rx, cy+ry), fill=TEMNO)
    d.ellipse((cx-rx+3, cy-ry+2, cx-rx+9, cy-ry+9), fill=(255,255,255,255))
    d.ellipse((cx+2, cy+4, cx+6, cy+8), fill=(255,255,255,170))

im2.save('teddy_new2.png')
im2.convert('RGB').crop((80,90,250,200)).resize((680,440), Image.LANCZOS).save('face_new2.png')
old = Image.open(src).convert('RGBA')
sheet = Image.new('RGB', (old.width*2+60, old.height+40), 'white')
for i, p in enumerate((old, im2)):
    bg = Image.new('RGBA', p.size, (255,255,255,255)); bg.alpha_composite(p)
    sheet.paste(bg.convert('RGB'), (20 + i*(old.width+20), 20))
sheet.save('sravnenie2.png')
print('ok')
