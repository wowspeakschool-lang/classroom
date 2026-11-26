# -*- coding: utf-8 -*-
"""GG3 юнит 1 ДЗ 1 — 15 карточек «дела по дому», второй круг: рамка задана прямо и цвет ярче
(26.11.2026, «227 плохо обрезаны» — модель резала фигуру краем кадра). Стиль Go Getter: полуреалистичный 3D,
подросток, никаких малышей. Ключ к Cloudflare подставляет прокси (сетевой секрет),
поэтому в заголовке — заглушка."""
import base64, json, os, sys, urllib.request

ACCOUNT = "de106aecd4f629fa2e8c12e6184b5f4f"
MODEL = "@cf/black-forest-labs/flux-1-schnell"
OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/gg3_u1"
os.makedirs(OUT, exist_ok=True)

STYLE = ("semi-realistic 3D render, natural proportions, detailed fabric and hair, "
         "bright cheerful colours, colourful clothes and interior, warm sunny lighting, "
         "realistic teenage proportions, natural small eyes, not a cartoon, no exaggerated features, "
         "plain flat pure white background, full figure from head to feet completely inside the frame, "
         "nothing cropped, wide empty white margin on all four sides, the character small in the "
         "middle of a large white square image, "
         "no text, no letters, no labels, no numbers")

P = {
 "make_the_bed": "An animated film character: a teenage girl smoothing a light grey duvet and placing a pillow on a neatly made single bed in a bright bedroom. ",
 "load_the_dishwasher": "An animated film character: a teenage boy crouching in front of an open dishwasher and putting a dirty plate into the lower rack, a few dirty plates still on the worktop. ",
 "empty_the_dishwasher": "An animated film character: a teenage boy holding a tall stack of clean white plates taken out of an open empty dishwasher and putting them on a cupboard shelf. ",
 "wash_the_dishes": "An animated film character: a teenage girl standing at a kitchen sink, washing a plate with a yellow sponge, white soap foam and running water. ",
 "vacuum_the_living_room": "An animated film character: a teenage boy vacuuming a grey carpet in a living room with an upright vacuum cleaner, a sofa behind him. ",
 "take_out_the_rubbish": "An animated film character: a teenage girl carrying a tied black rubbish bag with both hands towards a green wheelie bin outside the front door. ",
 "water_the_plants": "An animated film character: a teenage boy watering a green potted plant on a windowsill with a small blue watering can. ",
 "feed_my_pet": "An animated film character: a teenage girl pouring dry dog food from a scoop into a bowl on the kitchen floor, a small happy dog waiting beside the bowl. ",
 "set_the_table": "An animated film character: a teenage boy laying a clean dining table, placing a plate, a fork and a knife and a glass on the table, the table already half set. ",
 "clear_the_table": "An animated film character: a teenage girl carrying a stack of used dirty plates with leftover food away from a messy dining table towards the kitchen. ",
 "iron_my_tshirt": "An animated film character: a teenage boy ironing a white T-shirt on an ironing board with a steam iron. ",
 "put_away_my_clothes": "An animated film character: a teenage girl putting a pile of neatly folded clothes into an open wardrobe drawer. ",
 "load_the_washing_machine": "An animated film character: a teenage boy kneeling and putting colourful laundry into an open front-loading washing machine, a laundry basket beside him. ",
 "tidy_my_room": "An animated film character: a teenage girl tidying her bedroom, putting books onto a shelf, toys and clothes already in a basket. ",
 "cook_lunch": "An animated film character: a teenage boy cooking at a hob, stirring vegetables in a frying pan with a wooden spoon. ",
}

url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/{MODEL}"
only = set(sys.argv[2:])
for name, prompt in P.items():
    if only and name not in only:
        continue
    body = json.dumps({"prompt": prompt + STYLE, "steps": 8}).encode()
    req = urllib.request.Request(url, data=body, headers={
        "Authorization": "Bearer dummy", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            res = json.load(r)
    except urllib.error.HTTPError as e:
        print(name, "ОШИБКА", e.code, e.read()[:300].decode("utf-8", "replace")); continue
    img = res.get("result", {}).get("image")
    if not img:
        print(name, "пусто", str(res)[:200]); continue
    open(os.path.join(OUT, name + ".png"), "wb").write(base64.b64decode(img))
    print(name, "ок")
