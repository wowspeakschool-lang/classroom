"""Коробки-сюрпризы для Мастерской эльфов из готовых подарков календаря (тот же 3D-стиль).
обычная — крафт-бумага с белой лентой; редкая — синяя с серебряной; эпическая — фиолетовая с розовой;
легендарная — золотая с красной. Сзади свечение цвета редкости, на коробке бирка «?»."""
import colorsys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

D = os.path.dirname(os.path.abspath(__file__))
def load(n): return np.array(Image.open(f'{D}/img/{n}.webp').convert('RGBA')).astype(float)/255

def hsv(a):
    r,g,b = a[...,0],a[...,1],a[...,2]
    mx=a[...,:3].max(-1); mn=a[...,:3].min(-1); d=mx-mn+1e-6
    h=np.where(mx==r,((g-b)/d)%6,np.where(mx==g,(b-r)/d+2,(r-g)/d+4))/6
    s=np.where(mx>0,(mx-mn)/(mx+1e-6),0); return h,s,mx
def rgb(h,s,v):
    i=np.floor(h*6)%6; f=h*6-np.floor(h*6); p=v*(1-s); q=v*(1-f*s); t=v*(1-(1-f)*s)
    out=np.zeros(h.shape+(3,))
    for k,(x,y,z) in enumerate([(v,t,p),(q,v,p),(p,v,t),(p,q,v),(t,p,v),(v,p,q)]):
        m=i==k; out[m,0]=x[m]; out[m,1]=y[m]; out[m,2]=z[m]
    return out

def recolor(a, rules):
    h,s,v=hsv(a); out=a.copy(); rgbv=out[...,:3]
    for (h0,h1,smin),(nh,ns_k,nv_k) in rules:
        m=(s>smin)&(((h>=h0)&(h<h1)) if h0<h1 else ((h>=h0)|(h<h1)))&(a[...,3]>0.05)
        hh=np.full(h.shape,nh) if nh is not None else h
        res=rgb(hh, np.clip(s*ns_k,0,1), np.clip(v*nv_k,0,1))
        rgbv[m]=res[m]
    out[...,:3]=rgbv; return out

def finish(a, glow, name, tagcol):
    im=Image.fromarray((a*255).astype('uint8'),'RGBA')
    W,H=im.size; pad=40; can=Image.new('RGBA',(W+2*pad,H+2*pad),(0,0,0,0))
    if glow:
        al=im.split()[3].resize((W,H)); g=Image.new('RGBA',(W,H),glow+(0,)); g.putalpha(al)
        big=Image.new('RGBA',can.size,(0,0,0,0)); big.alpha_composite(g,(pad,pad))
        big=big.filter(ImageFilter.GaussianBlur(18))
        for _ in range(2): can.alpha_composite(big)
    can.alpha_composite(im,(pad,pad))
    # бирка «?» на передней стенке
    d=ImageDraw.Draw(can); cx,cy,r=pad+W*0.5,pad+H*0.66,30
    d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=(255,255,255,240),outline=tagcol+(255,),width=5)
    try: f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',40)
    except Exception: f=ImageFont.load_default()
    d.text((cx,cy+1),'?',fill=tagcol+(255,),font=f,anchor='mm')
    bb=can.getbbox(); can=can.crop(bb)
    can.save(f'{D}/img/box_{name}.webp',quality=88); return can

# обычная: красная коробка с белой лентой → крафт
a=load('gift6'); h,s,v=hsv(a)
red=(s>0.35)&((h<0.06)|(h>0.93))
kraft=rgb(np.full(h.shape,0.08),np.full(h.shape,0.42),np.clip(v*0.95,0,1))
a[red,:3]=kraft[red]; finish(a,None,'common',(150,100,60))
# редкая: синяя коробка, красная лента → серебро
a=load('gift4'); a=recolor(a,[((0.93,0.06,0.3),(None,0.08,1.15))]); finish(a,None,'rare',(46,111,214))
# эпическая: фиолетовая коробка, розовая лента — как есть
a=load('gift2'); finish(a,None,'epic',(122,47,208))
# легендарная: жёлтая коробка → золото, синяя лента → красная
a=load('gift3'); a=recolor(a,[((0.5,0.75,0.3),(0.99,1.0,0.95)),((0.1,0.2,0.3),(0.11,1.05,0.97))]); finish(a,None,'legend',(214,140,10))
print('ok')
