from PIL import Image, ImageDraw, ImageFont
exec(open('contact.py').read().split("T=250")[0])  # groups, fonts
f=ImageFont.truetype(F,26); fb=ImageFont.truetype(FB,34)
T=520;G=24;C=3;W=C*(T+G)+G
def sheet(gs,park,out):
    H=20+sum(60+((len(it)+C-1)//C)*(T+50) for _,it in gs)+(80+round((W-2*G)*864/1536)+60 if park else 0)
    s=Image.new('RGB',(W,H),(236,236,236));d=ImageDraw.Draw(s);y=10
    for title,it in gs:
        d.text((G,y+12),title,fill=(20,20,20),font=fb); y+=60
        for i,k in enumerate(it):
            x=G+(i%C)*(T+G); yy=y+(i//C)*(T+50)
            d.rectangle((x,yy,x+T,yy+T),fill='white')
            im=Image.open('final/'+k+'.webp').convert('RGB'); im.thumbnail((T-16,T-16),Image.LANCZOS)
            s.paste(im,(x+(T-im.width)//2,yy+(T-im.height)//2))
            d.text((x,yy+T+8),k.split('/',1)[1],fill=(0,0,0),font=f)
        y+=((len(it)+C-1)//C)*(T+50)
    if park:
        d.text((G,y+12),'SM2 Unit 7 ДЗ 5, блок 6 — парк (собран из 6 предметов)',fill=(20,20,20),font=fb); y+=70
        pk=Image.open('final/sm2/u7/hw5_city_empty.webp').convert('RGB'); pw=W-2*G; pk=pk.resize((pw,round(pw*864/1536)),Image.LANCZOS)
        dp=ImageDraw.Draw(pk)
        for px,py,t in [(10.5,63,'boat'),(24.5,41.5,'bird'),(36.8,61.5,'boy'),(60.5,63.5,'girl'),(70.3,59,'lizard'),(85.5,68,'flowers')]:
            X,Y=px*pk.width/100,py*pk.height/100; dp.ellipse((X-20,Y-20,X+20,Y+20),outline=(220,0,0),width=5); dp.text((X+24,Y-14),t,fill=(220,0,0),font=f)
        s.paste(pk,(G,y)); y+=pk.height+10
        d.text((G,y),'Красные кружки — точки из блока, в самой картинке их нет.',fill=(60,60,60),font=f)
    s.save(out); print(out,s.size)
sheet(groups[:2],False,'kontakt_06112026_1.png')
sheet(groups[2:],True,'kontakt_06112026_2.png')
