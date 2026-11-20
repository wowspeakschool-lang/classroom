from PIL import Image, ImageDraw, ImageFont
F='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
f_h=ImageFont.truetype(FB,36); f_o=ImageFont.truetype(F,26)
f_n=ImageFont.truetype(FB,26); f_s=ImageFont.truetype(F,22); f_sb=ImageFont.truetype(FB,22)

COL=500; GAP=30; PAD=30
W=PAD*2+COL*3+GAP*2
img=Image.new('RGB',(W,1400),'white'); d=ImageDraw.Draw(img)

def wrap(text,font,width):
    out=[]
    for para in text.split('\n'):
        line=''
        for w in para.split(' '):
            t=(line+' '+w).strip()
            if d.textlength(t,font=font)<=width: line=t
            else: out.append(line); line=w
        out.append(line)
    return out

d.text((PAD,24),'SM1 · юнит 2 · ДЗ 2 · блок 11 — вопрос 1 (на картинке мальчик)',font=f_h,fill='#1a1a1a')
d.text((PAD,72),'Задание учит his / her. Так ребёнок видит вопрос сейчас и так увидит в каждом варианте.',font=f_s,fill='#555')

pic=Image.open('/home/user/classroom/media/sm1/legacy/df0ea8b0d65c.webp')
ph=280; pw=int(pic.width*ph/pic.height); pic=pic.resize((pw,ph),Image.LANCZOS)

cols=[
 ('СЕЙЧАС','#b00020',False,
  [("His name's Daniel.",1),("Her name's Daniel.",0),("His name's Lisa.",1)],
  'Подходят две строки. На картинке мальчик — значит и «His name’s Daniel», '
  'и «His name’s Lisa» грамматически верны. Имени Daniel ребёнок нигде в курсе '
  'не встречал, узнать его по картинке неоткуда: выбрать можно только угадав. '
  'То же в вопросах 2 и 3 — там имена Lisa и Fiona.'),
 ('ВАРИАНТ А','#0b6b3a',True,
  [("His name's Daniel.",1),("Her name's Daniel.",0),("His name's Lisa.",0)],
  'Добавляем запись: ребёнок слышит «Daniel» и смотрит на картинку. Теперь «His name’s Lisa» '
  'отпадает — имя другое. Заголовок становится «Послушай имя, посмотри на картинку и выбери '
  'правильный вариант». Варианты остаются как есть, все три.\n'
  'От вас: нажать «Озвучить пачкой» — 6 новых мест. Пока не нажали, вопросы 1–3 остаются '
  'такими же, как сейчас; урок опубликован.'),
 ('ВАРИАНТ Б','#0b6b3a',False,
  [("His name's Daniel.",1),("Her name's Daniel.",0)],
  'Убираем строку с чужим именем. Имя в обеих строках одно, различаются только His и Her: '
  'ребёнок смотрит на картинку, видит мальчика и выбирает первую. Имя знать не нужно. '
  'Вопросы 4–6 (Flash, Thunder, Misty) не трогаем — там три варианта и всё работает.\n'
  'От вас: ничего. Звук не нужен, правка действует сразу.'),
]

TOP=118; BODY_Y=None
boxes=[]
for i,(name,color,audio,opts,note) in enumerate(cols):
    x=PAD+i*(COL+GAP); y=TOP
    yy=y+74
    img.paste(pic,(x+(COL-pw)//2,yy)); yy+=ph+20
    if audio:
        d.rounded_rectangle([x+26,yy,x+COL-26,yy+56],12,fill='#e8f3ee',outline='#0b6b3a',width=2)
        d.text((x+46,yy+15),'▶  запись: «Daniel.»',font=f_sb,fill='#0b6b3a')
        yy+=74
    for txt,ok in opts:
        d.rounded_rectangle([x+26,yy,x+COL-26,yy+58],12,fill='white',outline='#c7c7c7',width=2)
        d.text((x+44,yy+15),txt,font=f_o,fill='#1a1a1a')
        if ok: d.ellipse([x+COL-64,yy+18,x+COL-42,yy+40],fill='#0b6b3a')
        yy+=70
    boxes.append((x,y,color,name,yy,note))

note_top=max(b[4] for b in boxes)+16
bottom=note_top
for x,y,color,name,_,note in boxes:
    lines=wrap(note,f_s,COL-52)
    bottom=max(bottom, note_top+len(lines)*30+20)
H=int(bottom+30)
img2=Image.new('RGB',(W,H),'white'); img2.paste(img.crop((0,0,W,min(H,img.height))),(0,0))
d=ImageDraw.Draw(img2)
for x,y,color,name,_,note in boxes:
    d.rounded_rectangle([x,y,x+COL,H-50],14,outline='#d8d8d8',width=2)
    d.rounded_rectangle([x,y,x+COL,y+54],14,fill=color)
    d.text((x+20,y+12),name,font=f_n,fill='white')
    yy=note_top
    for ln in wrap(note,f_s,COL-52):
        d.text((x+26,yy),ln,font=f_s,fill='#333'); yy+=30
d.ellipse([PAD+6,H-36,PAD+24,H-18],fill='#0b6b3a')
d.text((PAD+34,H-38),'— строка, которую ребёнок может выбрать и быть правым',font=f_s,fill='#555')
img2.save('/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/sravnenie137/sm1_blok11_varianty.png')
print(img2.size)
