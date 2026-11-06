from PIL import Image, ImageDraw, ImageFont
import os
F='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; FB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
f=ImageFont.truetype(F,17); fb=ImageFont.truetype(FB,24); fs=ImageFont.truetype(F,15)
groups=[('Go Getter 1 — сцены (полуреалистичный 3D)',['gg1/u2/far_cap','gg1/u2/far_hoodie','gg1/u2/near_tracksuit','gg1/u1/place_london','gg1/u3/room_garden']),
('Go Getter 3 — стыки, Unit 6 и 7',['gg3/u6/oven','gg3/u6/fork','gg3/u6/bowl','gg3/u6/cake_tin','gg3/u6/pot','gg3/u6/spoon','gg3/u7/lift','gg3/u7/mirror','gg3/u7/tap','gg3/u7/stairs']),
('Go Getter 2 — стыки, Unit 0, 1, 3',['gg2/u3/camera','gg2/u3/keyboard','gg2/u3/printer','gg2/u3/headphones','gg2/u3/tablet','gg2/u0/armchair','gg2/u0/wardrobe','gg2/u1/ruler','gg2/u1/pencil_case','gg2/u1/scissors','gg2/u1/dictionary']),
('SM0 — части лица · SM3 — автобус',['sm0/new/mouth','sm0/new/nose','sm0/new/ears','sm0/new/eyes','sm3/ft/opt_school_bus'])]
T=250;G=16;C=6;W=C*(T+G)+G
H=0
for _,it in groups: H+=50+((len(it)+C-1)//C)*(T+40)
H+=60+round((W-2*G)*864/1536)+60
s=Image.new('RGB',(W,H),(236,236,236));d=ImageDraw.Draw(s);y=10
for title,it in groups:
    d.text((G,y+10),title,fill=(20,20,20),font=fb); y+=50
    for i,k in enumerate(it):
        x=G+(i%C)*(T+G); yy=y+(i//C)*(T+40)
        d.rectangle((x,yy,x+T,yy+T),fill='white')
        im=Image.open('final/'+k+'.webp').convert('RGB'); im.thumbnail((T-10,T-10),Image.LANCZOS)
        s.paste(im,(x+(T-im.width)//2,yy+(T-im.height)//2))
        d.text((x,yy+T+6),k.split('/',1)[1],fill=(0,0,0),font=f)
    y+=((len(it)+C-1)//C)*(T+40)
d.text((G,y+10),'SM2 Unit 7 ДЗ 5, блок 6 — парк для «расставь по местам» (собран скриптом из 6 предметов)',fill=(20,20,20),font=fb); y+=50
pk=Image.open('final/sm2/u7/hw5_city_empty.webp').convert('RGB'); pw=W-2*G; pk=pk.resize((pw,round(pw*864/1536)),Image.LANCZOS)
dp=ImageDraw.Draw(pk)
pts=[(10.5,63,'boat'),(24.5,41.5,'bird'),(36.8,61.5,'boy'),(60.5,63.5,'girl'),(70.3,59,'lizard'),(85.5,68,'flowers')]
for px,py,t in pts:
    X,Y=px*pk.width/100,py*pk.height/100; dp.ellipse((X-16,Y-16,X+16,Y+16),outline=(220,0,0),width=4)
    dp.text((X+20,Y-10),t,fill=(220,0,0),font=f)
s.paste(pk,(G,y)); y+=pk.height+8
d.text((G,y),'Красные кружки — точки из блока (на контактном листе для проверки, в картинке их нет).',fill=(60,60,60),font=fs)
s.save('kontakt_06112026.png'); print(s.size)
