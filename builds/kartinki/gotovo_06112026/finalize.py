from PIL import Image
import numpy as np, os
src={}
for d in ['gen_noch','gen_r2','gen_r3','gen_r5','gen_r6']:
    for f in os.listdir(d):
        if f.startswith('park__'): continue
        src[f[:-4].replace('__','/')]=d+'/'+f   # later rounds override
src['gg2/u3/camera']='camera_fix.png'; src['gg2/u1/ruler']='ruler_fix.png'
scenes={'gg1/u2/far_cap','gg1/u2/far_hoodie','gg1/u2/near_tracksuit','gg1/u1/place_london','gg1/u3/room_garden'}
rep=[]
for k,p in sorted(src.items()):
    im=Image.open(p).convert('RGB'); dst='final/'+k+'.webp'; os.makedirs(os.path.dirname(dst),exist_ok=True)
    if k in scenes:
        im.save(dst,'WEBP',quality=85); rep.append((k,im.size,'сцена')); continue
    a=np.asarray(im).astype(int); m=a.min(-1)<238
    ys,xs=np.where(m); x0,x1,y0,y1=xs.min(),xs.max(),ys.min(),ys.max()
    mg=round(max(x1-x0,y1-y0)*0.07)
    box=(max(0,x0-mg),max(0,y0-mg),min(1024,x1+mg),min(1024,y1+mg))
    c=im.crop(box); c=Image.new('RGB',(box[2]-box[0],box[3]-box[1]),'white'); c.paste(im.crop(box))
    s=700/max(c.size)
    if s<1: c=c.resize((round(c.width*s),round(c.height*s)),Image.LANCZOS)
    # edge check
    b=np.asarray(c).astype(int); e=max((b[:3].min(-1)<235).mean(),(b[-3:].min(-1)<235).mean(),(b[:,:3].min(-1)<235).mean(),(b[:,-3:].min(-1)<235).mean())
    c.save(dst,'WEBP',quality=88); rep.append((k,c.size,'край %.3f'%e))
Image.open('park_full.png').save('final/sm2/u7/hw5_city_empty.webp','WEBP',quality=85); rep.append(('sm2/u7/hw5_city_empty',(1536,864),'сцена'))
for r in rep: print(*r)
print(len(rep))
