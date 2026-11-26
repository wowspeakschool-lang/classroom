# -*- coding: utf-8 -*-
"""Перегенерация шести карточек GG3 ДЗ 1: убрать надписи на технике и книгах,
бокал вина заменить стаканом, сделать понятнее «разгружать посудомойку»."""
import base64, json, os, sys, urllib.request
ACCOUNT="de106aecd4f629fa2e8c12e6184b5f4f"; MODEL="@cf/black-forest-labs/flux-1-schnell"
OUT=sys.argv[1]; os.makedirs(OUT, exist_ok=True)
NOTEXT=("absolutely no text anywhere, no logos, no brand names, no writing on appliances, "
        "no posters with letters, no book titles, no numbers, ")
STYLE=("semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, "
       "restrained natural colours, realistic teenage proportions, natural small eyes, not a cartoon, "
       "no exaggerated features, plain flat pure white background, the whole scene complete and not "
       "touching the edge, " + NOTEXT)
P={
 "empty_the_dishwasher":"An animated film character: a teenage boy standing beside an open dishwasher in a bright kitchen, taking a clean white plate out of the lower rack with one hand, more clean plates still in the rack. ",
 "set_the_table":"An animated film character: a teenage boy laying a dining table: a plate, a fork, a knife and a simple drinking glass of water, the table clean and half set. No wine glass. ",
 "clear_the_table":"An animated film character: a teenage girl carrying two used dirty plates with cutlery away from a messy dining table towards the kitchen, dirty glasses still on the table. ",
 "vacuum_the_living_room":"An animated film character: a teenage boy vacuuming a grey carpet in a living room with a plain upright vacuum cleaner, a sofa behind him. ",
 "load_the_washing_machine":"An animated film character: a teenage boy kneeling and putting colourful laundry into an open front-loading washing machine with a plain blank control panel, a laundry basket beside him. ",
 "tidy_my_room":"An animated film character: a teenage girl tidying her bedroom, putting a plain book onto a shelf, clothes already folded in a basket, plain walls without posters. ",
}
url=f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/{MODEL}"
for name,prompt in P.items():
    body=json.dumps({"prompt":prompt+STYLE,"steps":8}).encode()
    req=urllib.request.Request(url,data=body,headers={"Authorization":"Bearer dummy","Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=180) as r: res=json.load(r)
    img=res.get("result",{}).get("image")
    if not img: print(name,"пусто"); continue
    open(os.path.join(OUT,name+".png"),"wb").write(base64.b64decode(img)); print(name,"ок")
