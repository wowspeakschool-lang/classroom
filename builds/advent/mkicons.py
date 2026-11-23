# значки гирлянд для кружка календаря: кусок с крючком и 3–5 бусинами/лампочками, квадрат 320 px
from PIL import Image
import numpy as np
jobs=[('garland','garland',240),('fairy_lights','fairy_lights',232),('tinsel','tinsel',240)]
for c in ['blue','green','red','silver']: jobs.append(('v/tinsel_'+c,'tinsel_'+c,240))
for src,name,x1 in jobs:
  im=Image.open('img/'+src+'.webp').convert('RGBA').crop((0,0,x1,10**4))
  if name!='garland':
    ar=np.array(im).astype(float);k=28
    ar[:,-k:,3]*=np.linspace(1,0,k)[None,:]
    im=Image.fromarray(ar.astype('uint8'),'RGBA')
  a=np.array(im)[:,:,3]; ys,xs=np.where(a>24)
  im=im.crop((xs.min(),ys.min(),xs.max()+1,ys.max()+1))
  w,h=im.size; s=int(max(w,h)*1.08)
  sq=Image.new('RGBA',(s,s),(0,0,0,0)); sq.alpha_composite(im,((s-w)//2,(s-h)//2))
  sq.resize((320,320),Image.LANCZOS).save('img/ic_'+name+'.webp',quality=88)
  print(name,w,h)
