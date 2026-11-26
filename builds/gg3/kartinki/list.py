# -*- coding: utf-8 -*-
"""Контактный лист карточек GG3 ДЗ 1: по три в ряд, клетка 520 px, подпись снизу."""
import sys, os
from PIL import Image, ImageDraw, ImageFont
SLOVA=[("chore_make_the_bed","make the bed · застилать кровать",0),
 ("chore_load_the_dishwasher","load the dishwasher · загружать посудомойку",0),
 ("chore_empty_the_dishwasher","empty the dishwasher · разгружать посудомойку",0),
 ("chore_wash_the_dishes","wash the dishes · мыть посуду",0),
 ("chore_vacuum_the_living_room","vacuum the living room · пылесосить",0),
 ("chore_set_the_table","set the table · накрывать на стол",0),
 ("chore_clear_the_table","clear the table · убирать со стола",0),
 ("chore_iron_my_tshirt","iron my T-shirt · гладить футболку",0),
 ("chore_put_away_my_clothes","put away my clothes · убирать одежду",0),
 ("chore_tidy_my_room","tidy my room · убираться в комнате",0),
 ("chore_cook_lunch","cook lunch · готовить обед",0),
 ("chore_load_the_washing_machine","load the washing machine · загрузить стирку",0),
 ("chore_take_out_the_rubbish","take out the rubbish · выносить мусор",1),
 ("chore_water_the_plants","water the plants · поливать цветы",1),
 ("chore_feed_my_pet","feed my pet · кормить питомца",1)]
KL=520; POLE=16; PODPIS=56
try:
    F=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",19)
    FB=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",19)
except Exception:
    F=FB=ImageFont.load_default()
def lист(punkty, put):
    ryady=(len(punkty)+2)//3
    W=3*(KL+POLE)+POLE; H=ryady*(KL+PODPIS+POLE)+POLE
    holst=Image.new("RGB",(W,H),"white"); d=ImageDraw.Draw(holst)
    for i,(imya,podpis,staraya) in enumerate(punkty):
        r,c=divmod(i,3)
        x=POLE+c*(KL+POLE); y=POLE+r*(KL+PODPIS+POLE)
        p=f"media/gg3/u1/{imya}.webp"
        if os.path.exists(p):
            im=Image.open(p).convert("RGB"); im.thumbnail((KL,KL), Image.LANCZOS)
            holst.paste(im,(x+(KL-im.width)//2, y+(KL-im.height)//2))
        d.rectangle([x,y,x+KL,y+KL], outline=(220,80,80) if staraya else (210,210,210), width=3 if staraya else 1)
        d.text((x+4,y+KL+6), podpis, font=FB if not staraya else F, fill=(0,0,0) if not staraya else (200,0,0))
        if staraya:
            d.text((x+4,y+KL+30), "СТАРАЯ — жду замену", font=F, fill=(200,0,0))
    holst.save(put,"PNG")
    print(put, holst.size)
out=sys.argv[1] if len(sys.argv)>1 else "/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad"
lист(SLOVA[:9], f"{out}/gg3_hw1_list1.png")
lист(SLOVA[9:], f"{out}/gg3_hw1_list2.png")
