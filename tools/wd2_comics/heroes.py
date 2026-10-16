import sys
from PIL import Image
S=sys.argv[1]
# (name, source, box in VIEW coords, view width)
H=[('dragon','34.png',(915,75,1064,370),1400),('unicorn','34.png',(1090,80,1216,340),1400),
   ('princess','34.png',(1220,100,1380,365),1400),('granny','18.jpg',(918,158,1150,446),1400),
   ('bunny','18.jpg',(762,110,895,395),1400),('martian','75.png',(664,445,748,535),1199)]
ims=[]
for n,src,box,vw in H:
    im=Image.open(f'{S}/comics/img/{src}').convert('RGB'); k=im.size[0]/vw
    c=im.crop(tuple(int(v*k) for v in box)); c.save(f'{S}/comics/heroes/{n}.png'); ims.append(c)
W=sum(i.size[0] for i in ims)+20*len(ims); Hh=max(i.size[1] for i in ims)
sheet=Image.new('RGB',(W,Hh),'white'); x=0
for i in ims: sheet.paste(i,(x,0)); x+=i.size[0]+20
sheet.save(f'{S}/comics/heroes/sheet.jpg',quality=85)
