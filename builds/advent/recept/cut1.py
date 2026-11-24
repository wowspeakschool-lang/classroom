"""Лист продуктов для рецепта (Анна, 24.11.2026): 2 ряда по 4. Фон белый или прозрачный —
фон = то, что связано с краем и почти белое/прозрачное; предмет = крупные компоненты."""
import sys, numpy as np
from PIL import Image, ImageDraw, ImageFilter
SRC=sys.argv[1]; OUT=sys.argv[2]; NAMES=sys.argv[3].split(',')
im=Image.open(SRC).convert('RGBA'); a=np.array(im).astype(int); H,W=a.shape[:2]
bgish=(a[...,3]<40)|((a[...,0]>238)&(a[...,1]>238)&(a[...,2]>238))
m=Image.fromarray(np.where(bgish,255,0).astype('uint8'),'L').copy()
for x in range(0,W,4):
    for y in (0,H-1):
        if m.getpixel((x,y))==255: ImageDraw.floodfill(m,(x,y),128)
for y in range(0,H,4):
    for x in (0,W-1):
        if m.getpixel((x,y))==255: ImageDraw.floodfill(m,(x,y),128)
bg=np.array(m)==128
fg=~bg
# мягкий край: альфа по «белизне» на границе
white=np.clip((765-(a[...,0]+a[...,1]+a[...,2]))/45.0,0,1)
alpha=np.where(fg,255,0).astype(float)
edge=np.array(Image.fromarray((fg*255).astype('uint8')).filter(ImageFilter.MaxFilter(3)))>0
ring=edge&~fg
alpha=np.where(ring,white*255,alpha)
if (a[...,3]<250).mean()>0.2: alpha=np.minimum(alpha,a[...,3])
# компоненты по уменьшенной маске
S=4; small=Image.fromarray((fg*255).astype('uint8')).resize((W//S,H//S),Image.BILINEAR)
sm=(np.array(small)>40).astype('uint8')*2+1; work=Image.fromarray(sm,'L').copy(); h,w=sm.shape; comps=[]
while True:
    arr=np.array(work); idx=np.flatnonzero(arr==3)
    if idx.size==0: break
    y,x=divmod(int(idx[0]),w); ImageDraw.floodfill(work,(x,y),9); arr=np.array(work); c=arr==9; ys,xs=np.nonzero(c)
    comps.append([int(c.sum()),ys.min()*S,ys.max()*S+S,xs.min()*S,xs.max()*S+S]); arr[c]=1; work=Image.fromarray(arr,'L').copy()
big=max(c[0] for c in comps); keep=[c for c in comps if c[0]>big*0.03]
# склеиваем куски одного предмета: по ячейке сетки центра
rows=2 if len(NAMES)<=8 else 3; cols=(len(NAMES)+rows-1)//rows
cells={}
for c in keep:
    cy=(c[1]+c[2])/2; cx=(c[3]+c[4])/2; key=(int(cy/H*rows),int(cx/W*cols))
    if key in cells:
        o=cells[key]; cells[key]=[o[0]+c[0],min(o[1],c[1]),max(o[2],c[2]),min(o[3],c[3]),max(o[4],c[4])]
    else: cells[key]=c
rgba=np.dstack([a[...,:3],alpha]).astype('uint8'); full=Image.fromarray(rgba,'RGBA')
for k,n in enumerate(NAMES):
    key=(k//cols,k%cols)
    if key not in cells: print('нет',n); continue
    _,y0,y1,x0,x1=cells[key]; p=int(max(y1-y0,x1-x0)*0.06)
    crop=full.crop((max(0,x0-p),max(0,y0-p),min(W,x1+p),min(H,y1+p)))
    side=max(crop.size); sq=Image.new('RGBA',(side,side),(0,0,0,0)); sq.paste(crop,((side-crop.size[0])//2,(side-crop.size[1])//2))
    sq.save(OUT+n+'.webp',quality=88); print(n,sq.size)
