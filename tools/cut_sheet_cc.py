# Нарезка листа по связным областям (scipy): python3 tools/cut_sheet_cc.py лист папка имя1,имя2,- R C [качество]
# Каждая область уходит в клетку сетки RxC по своему центру — соседние картинки не попадают в кусок.
import sys, numpy as np
from PIL import Image
from scipy import ndimage
src,out,names,R,C=sys.argv[1],sys.argv[2],sys.argv[3].split(','),int(sys.argv[4]),int(sys.argv[5])
q=int(sys.argv[6]) if len(sys.argv)>6 else 82
im=Image.open(src).convert('RGB'); a=np.asarray(im).astype(int)
mask=(a.min(axis=2)<235)
lab,n=ndimage.label(ndimage.binary_dilation(mask,iterations=6))
H,W=mask.shape
cells={}
for i,sl in enumerate(ndimage.find_objects(lab),1):
    if sl is None: continue
    ys,xs=sl; area=(lab[sl]==i).sum()
    if area<150: continue
    cy=(ys.start+ys.stop)/2; cx=(xs.start+xs.stop)/2
    r=min(int(cy/H*R),R-1); c=min(int(cx/W*C),C-1)
    cells.setdefault((r,c),[]).append((ys.start,ys.stop,xs.start,xs.stop,i))
for k,nm in enumerate(names):
    if nm=='-': continue
    r,c=divmod(k,C); comps=cells.get((r,c),[])
    if not comps: print('empty',nm); continue
    y0=min(t[0] for t in comps);y1=max(t[1] for t in comps);x0=min(t[2] for t in comps);x1=max(t[3] for t in comps)
    keep=np.isin(lab[y0:y1,x0:x1],[t[4] for t in comps])
    crop=np.asarray(im)[y0:y1,x0:x1].copy(); crop[~keep]=255
    p=Image.fromarray(crop); pad=int(max(p.size)*0.04)
    bg=Image.new('RGB',(p.width+2*pad,p.height+2*pad),'white'); bg.paste(p,(pad,pad)); bg.thumbnail((420,420))
    bg.save(f'{out}/{nm}.webp',quality=q); print(nm,bg.size,len(comps))
