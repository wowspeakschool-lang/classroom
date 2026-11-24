from PIL import Image;import numpy as np
T={'red':355,'blue':212,'green':128,'gold':42,'purple':275,'pink':328,'silver':None}
def rec(src,band,target,out,keep=0):
  im=Image.open('img/'+src+'.webp').convert('RGBA');al=im.getchannel('A')
  hsv=np.array(im.convert('RGB').convert('HSV')).astype(float)
  h=hsv[...,0]*360/255;s=hsv[...,1];v=hsv[...,2]
  lo,hi=band;c=(lo+((hi-lo)%360)/2)%360
  d=((h-c+180)%360)-180;half=((hi-lo)%360)/2
  w=np.clip((half+12-np.abs(d))/12,0,1)*np.clip((s-40)/30,0,1)
  if keep:
    H0=w.shape[0];w[:int(H0*keep)]=0
  if target=='silver':
    s2=s*(1-w*0.92);v2=np.clip(v*(1-w)+w*(v*0.75+60),0,255);h2=h
  else:
    t=T[target];h2=(h+w*(((t-c+180)%360)-180))%360;s2=s;v2=v
    if target=='pink':s2=s*(1-w*0.2);v2=np.clip(v*(1+w*0.12),0,255)
    if target=='gold':s2=s*(1-w*0.08);v2=v*(1-w*0.15)
  o=np.stack([h2*255/360,s2,v2],-1).round().clip(0,255).astype('uint8')
  img=Image.fromarray(o,'HSV').convert('RGB').convert('RGBA');img.putalpha(al)
  img.save('img/v/'+out+'.webp',quality=88)
def tint(src,target,out):  # для белых/неярких предметов: окрашиваем по яркости
  im=Image.open('img/'+src+'.webp').convert('RGBA');al=im.getchannel('A')
  a=np.array(im.convert('RGB')).astype(float);L=a.mean(-1,keepdims=True)
  col=np.array({'blue':(90,160,255),'gold':(255,196,70),'pink':(255,130,190)}[target],float)
  o=np.clip(L/255*col*1.05+ (L/255)**3*60,0,255).astype('uint8')
  img=Image.fromarray(o).convert('RGBA');img.putalpha(al);img.save('img/v/'+out+'.webp',quality=88)
GOLD=(10,55);RED=(325,15)
J=[('bell',GOLD,['silver','red']),('star',GOLD,['silver','red','blue']),('top_star',GOLD,['silver']),
   ('tinsel',GOLD,['silver','red','green','blue']),('bow',RED,['blue','green','purple']),
   ('candy_cane',RED,['green','blue']),('stocking',RED,['green','blue']),('heart',(295,335),['red','purple']),
   ('mitten',(165,225),['red','green','pink']),('sweet',(300,350),['blue','green','purple'])]
for src,band,cols in J:
  for c in cols:rec(src,band,c,src+'_'+c,{'star':.16,'heart':.15,'sweet':.25,'mitten':.1,'stocking':.1,'candy_cane':.1,'bow':.12,'top_star':0}.get(src,0))
for c in ['blue','gold','pink']:tint('snowflake',c,'snowflake_'+c)
print('ok')
