"""Превью всех картинок ВУ 4–6 листами по 3 в ряд → builds/mvu_46/prevyu/list_N.png"""
from PIL import Image, ImageDraw, ImageFont
M='media/mvu_46/'
G=[('Фоны',[('bg/'+n,n) for n in 'map room forest park launch space jungle'.split()]),
 ('Планеты крупно — иллюминаторы',[('obj/porthole_'+n,n) for n in 'red ice moon earth'.split()]),
 ('Дракоша',[('hero/dragon_'+n,n) for n in 'wave1 wave2 walk1 walk2 crouch jumpkey sad think point book astro_wave astro_float jump swim fly run dance clap'.split()]),
 ('Бабушка',[('hero/granny_'+n,n) for n in 'sad cry eat yuck key'.split()]),
 ('Ключи, сундук, книга',[('obj/'+n,n) for n in 'key_red key_blue key_green key_yellow chest_closed chest_open book'.split()]),
 ('Комната: игрушки, школа, одежда',[('obj/'+n,n) for n in 'car ball doll robot plane pencil schoolbook ruler tshirt socks hat sneakers teddy backpack toybox rug'.split()]),
 ('Лес',[('obj/'+n,n) for n in 'tree bush1 bush2 bush3 fox rabbit owl hedgehog bear squirrel butterfly bird pair_kittens pair_ducks pair_frogs pair_rabbits'.split()]),
 ('Парк: дети и еда',[('obj/'+n,n) for n in 'kid_run kid_skip kid_bike kid_swing kid_football kid_icecream pizza broccoli icecream fish cake apple banana carrot plate'.split()]),
 ('Космос',[('obj/'+n,n) for n in 'planet_red planet_blue planet_earth planet_moon planet_ring rocket postcard star'.split()]),
]
try: F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',30); f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',22)
except: F=f=ImageFont.load_default()
C=520; rows=[]
for title,items in G:
    rows.append(('h',title))
    for i in range(0,len(items),3): rows.append(('r',items[i:i+3]))
H={'h':60,'r':C}
sheets=[];cur=[];hh=0
for r in rows:
    if hh+H[r[0]]>2700 or (r[0]=='h' and hh+60+C>2700):
        sheets.append(cur);cur=[];hh=0
    cur.append(r);hh+=H[r[0]]
sheets.append(cur)
for k,sh in enumerate(sheets,1):
    im=Image.new('RGB',(C*3,sum(H[r[0]] for r in sh)),'white');d=ImageDraw.Draw(im);y=0
    for t,v in sh:
        if t=='h': d.rectangle([0,y,C*3,y+60],fill=(90,50,160));d.text((16,y+12),v,font=F,fill='white');y+=60;continue
        for i,(p,name) in enumerate(v):
            x=i*C; d.rectangle([x+6,y+6,x+C-6,y+C-6],fill=(244,244,248))
            pic=Image.open(M+p+'.webp').convert('RGBA');pic.thumbnail((C-40,C-70))
            im.paste(pic,(x+(C-pic.width)//2,y+14+(C-70-pic.height)//2),pic)
            d.text((x+18,y+C-46),name,font=f,fill=(60,60,60))
        y+=C
    im.save(f'builds/mvu_46/prevyu/list_{k}.png');print(k,im.size)
