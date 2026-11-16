from PIL import Image, ImageDraw, ImageFilter
import numpy as np
bg0=Image.open('/home/user/classroom/builds/kartinki/park_v2/park_v2_bg.png').convert('RGB'); W,H=bg0.size
an=Image.open('anna_park.webp').convert('RGB')
bg0.paste(an.crop((770,405,1050,497)),(770,405))
band=an.crop((968,405,1098,497)); mk=Image.new('L',band.size,255); dk=ImageDraw.Draw(mk)
for i in range(16): dk.line((i,0,i,band.size[1]),fill=int(255*i/16)); dk.line((band.size[0]-1-i,0,band.size[0]-1-i,band.size[1]),fill=int(255*i/16))
bg0.paste(band,(842,405),mk)
bl=bg0.filter(ImageFilter.GaussianBlur(5)); m=Image.new('L',bg0.size,0); dm=ImageDraw.Draw(m)
for x in (512,742,780,1040): dm.rectangle((x-9,505,x+9,668),fill=255)
for y in (512,660): dm.rectangle((505,y-7,1047,y+7),fill=255)
m=m.filter(ImageFilter.GaussianBlur(4)); bg=Image.composite(bl,bg0,m).convert('RGBA')
def fill(arr):
    w=Image.fromarray(arr.astype('uint8'))
    for xy in [(0,0),(1023,0),(0,1023),(1023,1023),(512,0),(512,1023),(0,512),(1023,512)]:
        ImageDraw.floodfill(w,xy,(255,0,255),thresh=12)
    a=np.asarray(w); return (a[...,0]==255)&(a[...,1]==0)&(a[...,2]==255)
def cut(p,band,glass=False):
    im=Image.open(p).convert('RGB'); o=np.asarray(im).astype(int)
    soft=fill(o); o2=o.copy(); light=(o.min(-1)>170)&((o.max(-1)-o.min(-1))<30); o2[light]=255; hard=fill(o2)
    ys=np.where(~soft)[0]; top,bot=ys.min(),ys.max(); cf=round(bot-(bot-top)*band)
    m=soft.copy(); m[cf:]|=hard[cf:]
    al=Image.fromarray(((~m)*255).astype('uint8')).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1))
    if glass:
        A=np.asarray(al).astype(int); lt=(o.min(-1)>195)&((o.max(-1)-o.min(-1))<25)&(A>0); lt[:top+int((bot-top)*0.36)]=False
        A[lt]=np.minimum(A[lt],70); al=Image.fromarray(A.astype('uint8'))
    im.putalpha(al); return im.crop(al.getbbox())
bs=cut('gen_dobor/sm2__u7__park_bus_stop_a.png',0.08,True); car=cut('gen_dobor/sm2__u7__park_car_a.png',0.16)
def place(o,h,left,bottom):
    o=o.resize((round(o.width*h/o.height),h),Image.LANCZOS); bg.alpha_composite(o,(left,bottom-h)); return (left,bottom-h,left+o.width,bottom)
print('bus',place(bs,250,632,650)); print('car',place(car,130,782,655))
out=bg.convert('RGB'); out.save('park_v2.png')
d=out.copy(); dr=ImageDraw.Draw(d)
for x,y in [(10.5,63),(24.5,41.5),(36.8,61.5),(60.5,63.5),(70.3,59),(85.5,68)]:
    X,Y=x*W/100,y*H/100; dr.ellipse((X-14,Y-14,X+14,Y+14),outline='red',width=4)
d.save('park_v2_dbg.png')
