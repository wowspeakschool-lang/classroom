"""Нарезка листов новых игрушек (Анна, 24.11.2026). Листы с прозрачным фоном,
у эпических и легендарных вокруг игрушек полупрозрачная дымка и искры.
Игрушка = крупная плотная компонента (alpha>200), дымка и мелкие искры отбрасываются."""
import os, numpy as np
from PIL import Image, ImageDraw, ImageFilter
IM='/tmp/claude-0/-home-user/4f1aec8c-7236-5d0b-8cab-c22529efe1d2/images/'
OUT='/tmp/claude-0/-home-user/4f1aec8c-7236-5d0b-8cab-c22529efe1d2/scratchpad/advent/img/n/'
os.makedirs(OUT,exist_ok=True)
SHEETS={'24':['teddy_bear','penguin','owl','fox','toy_train'],
        '25':['drum','ice_skates','gingerbread_house','carousel','hot_chocolate']}
S=4
for sh,names in SHEETS.items():
    src=Image.open(IM+sh+'.webp').convert('RGBA'); a=np.array(src); H,W=a.shape[:2]
    r,g,b=[a[...,i].astype(int) for i in range(3)]
    haze=((b-g)>12)&((r-g)>4)&(g>110) if sh in ('21','22') else np.zeros(r.shape,bool)
    # дымку снимаем только снаружи: та, что связана с прозрачным фоном (белое внутри игрушки остаётся)
    mm=Image.fromarray(np.where(haze|(a[...,3]<120),255,5).astype('uint8'),'L').copy()
    for xx in range(0,W,5):
        for yy in (0,H-1):
            if mm.getpixel((xx,yy))==255: ImageDraw.floodfill(mm,(xx,yy),100)
    for yy in range(0,H,5):
        for xx in (0,W-1):
            if mm.getpixel((xx,yy))==255: ImageDraw.floodfill(mm,(xx,yy),100)
    haze=haze&((np.array(mm)==100)|((b-g)>28))
    solid=(a[...,3]>200)&~haze
    small=Image.fromarray((solid*255).astype('uint8')).resize((W//S,H//S),Image.BILINEAR)
    sm=(np.array(small)>60).astype('uint8')*2+1
    work=Image.fromarray(sm,'L').copy(); h,w=sm.shape; comps=[]; k=0
    lab=np.zeros((h,w),int)
    while True:
        arr=np.array(work); idx=np.flatnonzero(arr==3)
        if idx.size==0: break
        y,x=divmod(int(idx[0]),w); ImageDraw.floodfill(work,(x,y),9); arr=np.array(work)
        c=arr==9; k+=1; ys,xs=np.nonzero(c); lab[c]=k
        comps.append([int(c.sum()),ys.min(),ys.max(),xs.min(),xs.max(),[k]])
        arr[c]=1; work=Image.fromarray(arr,'L').copy()
    big=max(c[0] for c in comps)
    keep=sorted([c for c in comps if c[0]>big*0.02],key=lambda c:-c[0])
    groups=[]
    bigs=[c for c in keep if c[0]>big*0.15]; groups=[c[:] for c in bigs]
    for c in keep:
        if c in bigs: continue
        for g in sorted(groups,key=lambda g:abs((g[3]+g[4])/2-(c[3]+c[4])/2)+abs(g[1]-c[2])):
            if not(c[3]>g[4]+1 or c[4]<g[3]-1 or c[1]>g[2]+1 or c[2]<g[1]-1):
                g[1]=min(g[1],c[1]);g[2]=max(g[2],c[2]);g[3]=min(g[3],c[3]);g[4]=max(g[4],c[4]);g[5]+=c[5];break
        else: groups.append(c[:])
    rows=2 if len(names)>3 else 1
    groups.sort(key=lambda g:(int(((g[1]+g[2])/2)//(h/rows)),(g[3]+g[4])/2))
    print(sh,len(groups),'ожидалось',len(names))
    for g,nm in zip(groups,names):
        m=np.isin(lab,g[5]).astype('uint8')*255
        mk=Image.fromarray(m).resize((W,H),Image.BILINEAR).filter(ImageFilter.MaxFilter(5))
        mk=np.array(mk)>40
        al=np.where(mk&(a[...,3]>120)&~haze,a[...,3],0).astype('uint8')
        out=a.copy(); out[...,3]=al
        y0,y1,x0,x1=g[1]*S,g[2]*S+S,g[3]*S,g[4]*S+S
        im=Image.fromarray(out).crop((max(0,x0-6),max(0,y0-6),min(W,x1+6),min(H,y1+6)))
        bb=im.getbbox(); im=im.crop(bb)
        im.thumbnail((360,360)); im.save(OUT+nm+'.webp',quality=88)
