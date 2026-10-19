from PIL import Image, ImageDraw, ImageFont
OUT='/home/user/classroom/media/sm1/old/'
PRE='/tmp/claude-0/-home-user-classroom/1a6ce660-add2-54a8-875f-7eac683dcc65/scratchpad/c2/'
FB='/usr/share/fonts/opentype/inter/Inter-Bold.otf'
FR='/usr/share/fonts/opentype/inter/Inter-Medium.otf'
FX='/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'
def f(p,s): return ImageFont.truetype(p,s)
INK=(23,49,92); MUTE=(80,90,110); A=(229,57,53); AN=(30,136,229)

# ---- number cards 1..10 (same look as media/sm3/u0/num_*.webp)
for n in range(1,11):
    im=Image.new('RGB',(420,300),'white'); d=ImageDraw.Draw(im)
    d.rounded_rectangle((18,18,402,282),34,fill=(243,247,253),outline=(200,214,232),width=4)
    ft=f('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',150)
    d.text((210,152),str(n),font=ft,fill=INK,anchor='mm')
    im.save(OUT+f'num_{n}.webp','WEBP',quality=88)

# ---- colour cards
cols={'yellow':(255,210,31),'red':(229,57,53),'orange':(251,140,0),'purple':(142,68,173),'blue':(30,136,229),'green':(67,160,71)}
for k,c in cols.items():
    S=4; im=Image.new('RGB',(300*S,300*S),'white'); d=ImageDraw.Draw(im)
    dark=tuple(int(v*0.8) for v in c)
    d.ellipse((40*S,40*S,260*S,260*S),fill=c,outline=dark,width=6*S)
    d.ellipse((85*S,75*S,135*S,115*S),fill=tuple(min(255,int(v+(255-v)*0.55)) for v in c))
    im.resize((300,300),Image.LANCZOS).save(OUT+f'color_{k}.webp','WEBP',quality=88)

# ---- rule cards
def wrap(d,text,font,maxw):
    words=text.split(' '); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if d.textlength(t,font=font)<=maxw: cur=t
        else: lines.append(cur); cur=w
    lines.append(cur); return lines
def rich(d,x,y,parts,font):
    for txt,col in parts:
        d.text((x,y),txt,font=font,fill=col); x+=d.textlength(txt,font=font)
def card(name,title,band,body):
    W=900; im=Image.new('RGB',(W,1400),(250,251,255)); d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,120),fill=band)
    d.text((W//2-10,66),title,font=f(FX,52),fill='white',anchor='mm')
    y=160
    for kind,val in body:
        if kind=='p':
            for ln in wrap(d,val,f(FR,34),W-120):
                d.text((60,y),ln,font=f(FR,34),fill=MUTE); y+=48
            y+=14
        elif kind=='ex':   # list of (parts) big examples
            for parts in val:
                d.rounded_rectangle((60,y,W-60,y+78),22,fill='white',outline=(214,222,236),width=2)
                rich(d,90,y+16,parts,f(FB,40)); y+=94
            y+=10
        elif kind=='h':
            rich(d,60,y,val,f(FB,38)); y+=60
    im=im.crop((0,0,W-20,y+20))
    out=Image.new('RGB',(W,y+40),'white')
    m=Image.new('L',im.size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,im.width-1,im.height-1),36,fill=255)
    out.paste(im.crop((0,0,im.width,im.height)),(10,10),m)
    ImageDraw.Draw(out).rounded_rectangle((10,10,W-11,y+29),36,outline=(214,222,236),width=3)
    im=out
    im.save(OUT+name+'.webp','WEBP',quality=88); im.save(PRE+name+'.png')

G=(46,125,50)
card('u2_hw3_rule_adjectives','Какой? Слова-признаки',(251,140,0),[
  ('p','Слово-признак говорит, какой предмет: большой, маленький, новый.'),
  ('h',[('По-английски оно стоит ',INK),('перед',(229,57,53)),(' словом:',INK)]),
  ('ex',[[('a ',INK),('big',(229,57,53)),(' ball',INK),(' — большой мяч',MUTE)],
         [('a ',INK),('small',(229,57,53)),(' doll',INK),(' — маленькая кукла',MUTE)],
         [('a ',INK),('new',(229,57,53)),(' bike',INK),(' — новый велосипед',MUTE)]]),
  ('h',[('Слова-противоположности:',INK)]),
  ('ex',[[('big ',G),('↔',MUTE),(' small     ',G),('new ',G),('↔',MUTE),(' old',G)],
         [('long ',G),('↔',MUTE),(' short     ',G),('ugly ',G),('↔',MUTE),(' beautiful',G)]]),
])
card('u2_hw3_rule_a_an','a или an?',(30,136,229),[
  ('h',[('an',AN),(' — если слово начинается',INK)]),
  ('p','с гласного звука: a, e, i, o, u'),
  ('ex',[[('an',AN),(' apple',INK),('   ',INK),('an',AN),(' egg',INK),('   ',INK),('an',AN),(' elephant',INK)]]),
  ('h',[('a',A),(' — если слово начинается с согласного',INK)]),
  ('ex',[[('a',A),(' cat',INK),('   ',INK),('a',A),(' dog',INK),('   ',INK),('a',A),(' ball',INK)]]),
  ('p','Смотри на слово сразу после a / an:'),
  ('ex',[[('an',AN),(' old car',INK),(',  но  ',MUTE),('a',A),(' new car',INK)]]),
])

# ---- friends: four heroes together
L='/home/user/classroom/media/sm1/legacy/'
hs=[Image.open(L+x+'.webp').convert('RGBA') for x in ['eb68810585d6','32dd089617ca','af307dbdc2ee','746c511616d8']]
H=300; hs=[h.resize((round(h.width*H/h.height),H),Image.LANCZOS) for h in hs]
W=sum(h.width for h in hs)+20*5
im=Image.new('RGB',(W,H+40),'white'); x=20
for h in hs: im.paste(h,(x,20),h); x+=h.width+20
im.save(OUT+'u0_friends.webp','WEBP',quality=85)
