from PIL import Image, ImageDraw, ImageFilter
import numpy as np
W,H=1536,864
bg=Image.open('gen_r3/park__bg.png').convert('RGB').crop((0,230,1024,806)).resize((W,H),Image.LANCZOS)
def fill(arr):
    w=Image.fromarray(arr.astype('uint8'))
    for xy in [(0,0),(1023,0),(0,1023),(1023,1023),(512,0),(512,1023),(0,512),(1023,512)]:
        ImageDraw.floodfill(w,xy,(255,0,255),thresh=12)
    a=np.asarray(w); return (a[...,0]==255)&(a[...,1]==0)&(a[...,2]==255)
def cut(p,band):
    im=Image.open(p).convert('RGB'); o=np.asarray(im).astype(int)
    soft=fill(o)
    o2=o.copy(); light=(o.min(-1)>170)&((o.max(-1)-o.min(-1))<30); o2[light]=255
    hard=fill(o2)
    ys=np.where(~soft)[0]; top,bot=ys.min(),ys.max()
    cut_from=round(bot-(bot-top)*band)
    bgm=soft.copy(); bgm[cut_from:]|=hard[cut_from:]
    al=Image.fromarray(((~bgm)*255).astype('uint8')).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1))
    im.putalpha(al); return im.crop(al.getbbox())
items=[('lake','gen_r4/park__lake.png',130,(0.5,0.5),(10.5,63),1),
 ('tree','gen_r4/park__tree.png',430,(0.5,0.25),(24.5,41.5),1),
 ('bench','gen_r3/park__bench.png',120,(0.5,0.3),(36.8,61.5),1),
 ('fountain','gen_r3/park__fountain.png',215,(0.5,0.62),(60.5,63.5),1),
 ('wall','gen_r3/park__wall.png',46,(0.5,0.12),(70.3,59),0.25),
 ('cafe','gen_r3/park__cafe.png',280,(0.5,0.78),(85.5,68),0.06)]
out=bg.copy().convert('RGBA')
for n,f,h,(fx,fy),(px,py),band in items:
    o=cut(f,band); o=o.resize((round(o.width*h/o.height),h),Image.LANCZOS)
    x=round(px*W/100-fx*o.width); y=round(py*H/100-fy*o.height)
    print(n,'bbox',x,y,x+o.width,y+o.height); out.alpha_composite(o,(x,y))
out=out.convert('RGB'); out.save('park_full.png')
d=out.copy(); dr=ImageDraw.Draw(d)
for *_,(px,py),b in items:
    X,Y=px*W/100,py*H/100; dr.ellipse((X-22,Y-22,X+22,Y+22),outline='red',width=5)
d.save('park_dbg.png')
