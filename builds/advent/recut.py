from PIL import Image;import numpy as np;from collections import deque
im=Image.open('/tmp/claude-0/-home-user/4f1aec8c-7236-5d0b-8cab-c22529efe1d2/images/7.webp').convert('RGBA')
a=np.array(im);m=a[...,3]>24;H,W=m.shape
def comp(seed):
  seen=np.zeros_like(m);q=deque([seed]);seen[seed]=1
  while q:
    y,x=q.popleft()
    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
      ny,nx=y+dy,x+dx
      if 0<=ny<H and 0<=nx<W and m[ny,nx] and not seen[ny,nx]:seen[ny,nx]=1;q.append((ny,nx))
  return seen
# крупнейшая компонента в клетке 0 (верх-лево)
sub=m[:512,:512];ys,xs=np.nonzero(sub)
best=None
tried=np.zeros_like(m)
for y,x in zip(ys[::97],xs[::97]):
  if tried[y,x]:continue
  c=comp((y,x));tried|=c
  if best is None or c.sum()>best.sum():best=c
ys,xs=np.nonzero(best);print(best.sum(),ys.min(),ys.max(),xs.min(),xs.max())
out=a.copy();out[...,3]=np.where(best,a[...,3],0)
# мягкий край: оставляем полупрозрачные пиксели рядом с компонентой
from PIL import ImageFilter
dil=Image.fromarray((best*255).astype('uint8')).filter(ImageFilter.MaxFilter(5))
out[...,3]=np.where(np.array(dil)>0,a[...,3],0)
img=Image.fromarray(out).crop((xs.min()-3,ys.min()-3,xs.max()+4,ys.max()+4))
img.thumbnail((320,320));img.save('img/heart.webp',quality=88);print(img.size)
