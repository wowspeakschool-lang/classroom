"""Промпты ВУ 4–6 для ChatGPT → prompty.md.  python3 builds/mvu_46/prompty_gen.py

26.11.2026: 23 генерации (листы объединены), в каждом промпте — стиль приложенной картинки
и прозрачный фон (кроме полноэкранных фонов, они сами фон).
"""
import os

STYLE_REF = ("Draw in EXACTLY the same art style as the attached picture of the purple dragon "
             "(use it only as a style reference, do not draw the dragon).")
STYLE = ("Style: the same as the attached picture — cute 2D cartoon illustration for children aged 4–6, "
         "soft rounded shapes, clean smooth dark outlines, bright cheerful flat colours with gentle soft shading, friendly and warm. "
         "No text, no letters, no numbers, no logos, no watermark.")
NOBG = ("TRANSPARENT BACKGROUND: output a PNG with a fully transparent background — no background colour, no white, "
        "no floor, no ground, no shadow under the objects.")
SHEET = ("Wide empty gaps between the items; every item complete, centred in its own cell and not touching any other item or the edge.")
SCENE = ("This is a full-screen background picture: wide landscape 16:9, filling the whole frame. Nobody in it: no people, "
         "no animals, no dragon (characters will be added separately).")
DRAGON = ("The attached picture is our hero, the purple dragon. Draw EXACTLY this character in EXACTLY this art style: "
          "the same purple colour, yellow belly, orange-yellow horns, small orange-yellow wings, flame on the tail tip, "
          "the same face, eyes, orange swirl on the cheek and proportions. Do not redesign him.")
GRANNY = ("Two pictures are attached: the purple dragon (use it as the STYLE reference) and the old dragon granny "
          "(yellow headscarf, red coat, walking stick) — draw EXACTLY this granny, the same character, colours, face and clothes, "
          "in the same art style. Do not redesign her and do not draw the young dragon.")

P = []
def add(sec, name, title, body, ref='дракоша'): P.append((sec, name, title, body, ref))

# ── фоны на весь экран: по одному на лист
F = 'Фоны (на весь экран, по одному на лист — они сами фон, прозрачными их не делаем)'
add(F, 'map', 'карта сокровищ', STYLE_REF + " " + "Wide landscape 16:9 picture of an old treasure map on crumpled warm-beige parchment, seen from above and filling the whole frame. Five small places drawn on the map, each with empty space around it and connected by dashed paths: a cosy little house with a red roof (bottom centre), a forest of round green trees (left), a park with a playground and a small pond (right), a jungle with palm trees and a big red X mark (top left), and a very small, pale planet with a ring drawn faintly in the bottom-right corner, almost hidden in the paper texture. A small compass rose in the top-right corner. No characters, no people, no animals. " + STYLE)
add(F, 'room', 'детская комната', STYLE_REF + " " + SCENE + " A bright child's bedroom seen from the front: a bed on the left with a clear empty space under it, a wardrobe, a small desk with a chair, a shelf on the wall, a window with curtains and sunshine, a round rug on the floor. The room is tidy and has NO toys, NO clothes and NO school things anywhere — the floor, bed, desk and shelf are empty (objects will be added separately). " + STYLE)
add(F, 'forest', 'лес', STYLE_REF + " " + SCENE + " A friendly sunny forest clearing: tall trees in the background, soft green grass, flowers, a small pond on the left. The right third of the picture is an open grassy area with NO tree (a big tree will be added there), and the front of the picture is empty grass (bushes will be added there). " + STYLE)
add(F, 'park', 'парк', STYLE_REF + " " + SCENE + " A sunny city park: an empty wooden bench in the front left, a playground with a slide and a swing frame in the background, green trees, a path, a small pond with a little bridge, blue sky. Plenty of open space on the path and grass in the middle (children will be added separately). " + STYLE)
add(F, 'launch', 'стартовая площадка', STYLE_REF + " " + SCENE + " Evening sky above a green hill with a small rocket launch pad in the centre — an empty launch pad, no rocket (the rocket will be added separately). First stars appear in the deep blue sky. " + STYLE)
add(F, 'space', 'космос', STYLE_REF + " " + SCENE + " Deep space: a dark blue-violet starry sky with soft nebula clouds, completely empty in the middle — no planets, no rockets, no big stars (they will be added separately), only tiny distant twinkles. " + STYLE)
add(F, 'jungle', 'джунгли', STYLE_REF + " " + SCENE + " A magical jungle: a waterfall and a small river on the left, big leaves, vines and tropical flowers, warm light through the leaves. The front centre is an open flat patch of ground (a treasure chest will be added there). " + STYLE)

# ── предметы листами, без фона
L = 'Предметы листами (без фона)'
add(L, 'sheet_portholes', 'планеты крупно — 4 иллюминатора', STYLE_REF + " A sheet of 4 separate round porthole views in a 2×2 grid — each one a big circle with a thick golden rim, like looking through a spaceship window at a planet surface up close. Nobody inside: no people, no animals, no dragon. Row 1, left to right: a warm red-orange desert planet with smooth dunes and round red rocks, the middle of the ground empty and flat; a calm blue ice planet with a cold sea and small white ice floes. Row 2, left to right: a grey moon surface with soft round craters under a black starry sky, the middle of the ground empty and flat; a bright green Earth meadow with flowers, round trees and a big friendly yellow sun in the sky. Outside the circles everything is transparent. " + NOBG + " " + SHEET + " " + STYLE)
add(L, 'sheet_keys_chest', 'ключи, сундук, книга', STYLE_REF + " A sheet of 7 separate objects. Row 1, left to right: four big old-fashioned fairy-tale keys with round decorated heads, all the same shape and size, lying horizontally — a red key, a blue key, a green key, a yellow key. Row 2, left to right: a closed wooden pirate treasure chest with gold trim and FOUR keyholes on the front — a red one, a blue one, a green one and a yellow one; the same chest wide open with golden light shining out; a thick magic book with a plain purple cover glowing with golden sparkles (no writing on the cover). " + NOBG + " " + SHEET + " " + STYLE)
add(L, 'sheet_toys', 'игрушки и школьные вещи', STYLE_REF + " A sheet of 8 separate objects in a 4×2 grid. Row 1, left to right: a red toy car, a colourful ball, a doll, a toy robot. Row 2, left to right: a toy plane, a pencil, a book, a ruler. " + NOBG + " " + SHEET + " " + STYLE)
add(L, 'sheet_clothes', 'одежда, мишка, рюкзак', STYLE_REF + " A sheet of 8 separate objects in a 4×2 grid. Row 1, left to right: a yellow T-shirt, a pair of striped socks, a hat, a pair of sneakers. Row 2, left to right: a brown teddy bear sitting, an open empty school backpack (front view), an open empty wooden toy box (front view), a small rug. " + NOBG + " " + SHEET + " " + STYLE)
add(L, 'sheet_animals1', 'лесные животные 1', STYLE_REF + " A sheet of 4 separate forest animals in a 2×2 grid, each sitting and facing the viewer, friendly and cute. Row 1, left to right: a fox, a rabbit. Row 2, left to right: an owl, a hedgehog. " + NOBG + " " + SHEET + " " + STYLE)
add(L, 'sheet_animals2', 'лесные животные 2', STYLE_REF + " A sheet of 4 separate animals in a 2×2 grid, friendly and cute. Row 1, left to right: a brown bear, a squirrel. Row 2, left to right: a small blue butterfly with open wings, a small yellow bird. " + NOBG + " " + SHEET + " " + STYLE)
add(L, 'sheet_pairs', 'животные парами', STYLE_REF + " A sheet of 4 separate pairs of animals in a 2×2 grid — in every cell exactly TWO of the same animal sitting side by side. Row 1, left to right: two kittens, two ducks. Row 2, left to right: two frogs, two little rabbits. " + NOBG + " " + SHEET + " " + STYLE)
add(L, 'sheet_bushes', 'кусты', STYLE_REF + " A row of 3 separate big round green leafy bushes, each a little different in shape, wide and dense enough to hide a fox behind it. " + NOBG + " " + SHEET + " " + STYLE)
add(L, 'tree', 'большое дерево', STYLE_REF + " One big friendly tree with a thick trunk and a round green crown, with one long strong branch sticking out to the left (a key on a rope will hang from it). The whole tree is visible from the roots to the top. Nothing else in the picture, no grass under it. " + NOBG + " The tree does not touch the edges. " + STYLE)
add(L, 'sheet_food', 'еда и тарелка', STYLE_REF + " A sheet of 9 separate objects in a 3×3 grid. Row 1, left to right: a pizza, broccoli, an ice cream cone. Row 2, left to right: a fish on a small plate, a birthday cake, a red apple. Row 3, left to right: a banana, a carrot, a big empty white plate. " + NOBG + " " + SHEET + " " + STYLE)
add(L, 'sheet_kids', 'дети в парке', STYLE_REF + " A sheet of 6 separate animated cartoon children, about six years old, full body, in a 3×2 grid, each doing one clear action. Row 1, left to right: a boy running, a girl jumping with a skipping rope, a boy riding a bike. Row 2, left to right: a girl on a swing (with the swing seat and ropes), a boy kicking a football, a girl eating an ice cream. " + NOBG + " " + SHEET + " " + STYLE)
add(L, 'sheet_space', 'планеты, ракета, открытка', STYLE_REF + " A sheet of 8 separate objects in a 4×2 grid. Row 1, left to right: a red planet, a blue planet with wavy stripes, the planet Earth, a grey moon with craters. Row 2, left to right: a small pale planet with a ring, a white-and-red cartoon rocket standing upright, a picture postcard showing a sea and a sun (no writing), a smiling yellow star. " + NOBG + " " + SHEET + " " + STYLE)

# ── герои, без фона
H = 'Дракоша и бабушка (без фона)'
add(H, 'dragon_moves', 'Дракоша машет, идёт, прыгает — 6 кадров', DRAGON + " A sheet of 6 animation frames in a 3×2 grid, full body, all the same size. Row 1, left to right: waving — right arm raised with the palm open; waving — the same arm raised higher and tilted the other way (otherwise identical to the first frame); walking to the right with the left foot forward. Row 2, left to right: walking to the right with the right foot forward; crouching happily before a jump; jumping high with joy, arms up, holding a key in one hand. " + NOBG + " " + SHEET + " " + STYLE)
add(H, 'dragon_says', 'Дракоша показывает действия', DRAGON + " A sheet of 6 poses in a 3×2 grid, full body, each a clear action for the game 'Dragon says'. Row 1, left to right: jumping, swimming in a little splash of water, flying with his small wings spread. Row 2, left to right: running, dancing, clapping his hands. " + NOBG + " " + SHEET + " " + STYLE)
add(H, 'dragon_moods', 'Дракоша: настроения и космонавт — 6 поз', DRAGON + " A sheet of 6 poses in a 3×2 grid, full body, all the same size. Row 1, left to right: sad with a little frown; thinking with a finger on his chin; pointing to the side with one hand. Row 2, left to right: happily holding up a thick open book glowing with golden sparkles; dressed as a little astronaut in a white space suit and a round clear glass helmet (his horns and face visible inside), standing and waving; the same astronaut floating in the air with arms spread happily. " + NOBG + " " + SHEET + " " + STYLE)
add(H, 'granny', 'бабушка — 5 поз', GRANNY + " A sheet of 5 poses, all sitting (as if on a bench, but draw no bench), all the same size. Row 1, left to right: sad and hungry, holding her tummy with one hand, a small tear in the corner of her eye; exactly the same pose, but the tear has rolled down her cheek; happily eating with a fork, eyes closed with pleasure. Row 2, left to right: frowning and turning her head away with a 'yuck' face; smiling and holding out a green key with both hands. " + NOBG + " " + SHEET + " " + STYLE, ref='дракоша + бабушка')

# ── добавка 27.11: бабушка ест именно ту еду, которую выбрал ребёнок; птица в полёте
D2 = 'Доборные (27.11.2026)'
EATP = (" A sheet of 4 poses in a 2×2 grid, all the same size, sitting (as if on a bench, but draw no bench), the same body position in every pose "
        "— only the food in her hand changes. In every pose she is happily eating, eyes closed with pleasure, the food clearly visible right at her mouth. ")
add(D2, 'granny_eat_1', 'бабушка ест: пицца, брокколи, мороженое, рыба', GRANNY + EATP + "Row 1, left to right: biting a slice of pizza; eating a piece of broccoli. Row 2, left to right: licking a pink ice cream cone; eating a fish from a fork. " + NOBG + " " + SHEET + " " + STYLE, ref='дракоша + бабушка')
add(D2, 'granny_eat_2', 'бабушка ест: торт, яблоко, банан, морковка', GRANNY + EATP + "Row 1, left to right: eating a slice of birthday cake from a small plate; biting a red apple. Row 2, left to right: eating a peeled yellow banana; biting an orange carrot. " + NOBG + " " + SHEET + " " + STYLE, ref='дракоша + бабушка')
add(D2, 'bird_fly', 'птица летит', STYLE_REF + " One small yellow bird flying, side view, facing right, both wings spread wide in flight, friendly face, no branch, nothing else in the picture. " + NOBG + " The bird does not touch the edges. " + STYLE)

# ── добавка 27.11 (вторая): комната, где видно «под», и мишка в коробке
D3 = 'Доборные 2 (27.11.2026)'
add(D3, 'room2', 'комната заново: место под кроватью и под столом', "Two pictures are attached: a child's bedroom (use it as the LAYOUT and STYLE reference) and the purple dragon (STYLE reference only, do not draw it). Redraw the attached bedroom in exactly the same art style, colours and layout — the bed on the left, the window with yellow curtains, the cream wardrobe in the middle, the shelf on the right wall, the desk on the right, the round purple-and-yellow rug — with these changes: the bed stands on tall legs, so there is a big clearly visible empty space on the floor UNDER the bed; the desk also has a big clearly visible empty space UNDER it, and the yellow chair stands next to the desk on its left side, NOT under it; the floor in front of the wardrobe is empty. The room is tidy and has NO toys, NO clothes and NO school things anywhere — the floor, bed, desk and shelf are empty. " + SCENE + " " + STYLE, ref='комната + дракоша')
add(D3, 'teddy_box', 'мишка сидит в открытой коробке', "Two pictures are attached: a brown teddy bear with a red bow tie (draw EXACTLY this teddy) and the purple dragon (STYLE reference only, do not draw it). One open wooden toy box seen from the front, slightly from above, the lid open behind; the teddy bear sits INSIDE the box — its head, shoulders and paws stick out over the front edge, the lower half of its body is hidden inside the box. Nothing else in the picture. " + NOBG + " The picture does not touch the edges. " + STYLE, ref='мишка + дракоша')

out = ['# ВУ 4–6 · Wow Dragon — промпты для ChatGPT (26.11.2026)', '',
       'Игры (решение Анны 24.11, «51»): А «Что пропало?», Б «Где мишка?», В «Кто прячется в кустах?», Д «Потряси дерево», '
       'Е «Покорми бабушку», Ж «Дракоша говорит», И отсчёт и звёзды (космос проходят все: слабые считают звёзды, сильные ещё и разбирают планеты), К ключи по цвету.', '',
       '**К каждому промпту прикладывать `obrazcy/drakosha_dlya_chatgpt.png`** (стиль). К промпту бабушки — ещё и '
       '`obrazcy/babushka_dlya_chatgpt.png`. Предметы и герои — без фона (прозрачный PNG); фоны 1–7 — на весь экран, '
       'по одному на лист. Планеты крупно — круглыми иллюминаторами поверх космоса. Анимация героев — из кадров.', '']
sec = None; n = 0
for s, name, title, body, ref in P:
    if s != sec: out += ['## ' + s, '']; sec = s
    n += 1
    out += [f'### {n} · {title} → `{name}` · приложить: {ref}', '', '```', body, '```', '']
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'prompty.md'), 'w').write('\n'.join(out))
print(n, 'prompts')
