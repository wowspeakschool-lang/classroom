# Вычитка картинок — Go Getter 1 (`gg1`)

Проход 03.11.2026 по решению Анны: Go Getter идёт первым, курс делаем целиком
в одном стиле. Смотрели **только картинки** — размер, стиль, мусор по краям,
соответствие ключу. Ничего не генерировали и не заливали: здесь список и промпты.

Контактные листы, по которым смотрели, — `docs/vychitka/kartinki/gg1_listy/`
(26 листов, по юнитам; под каждой картинкой имя файла и реальный размер,
показана в том размере, в каком её видит ребёнок).

## Сводка

| | штук |
|---|---|
| файлов в `media/gg1` | 520 (484 webp + 30 svg + 6 mp3) |
| картинок (webp + svg) | 514 |
| используется в блоках | 497 |
| **не используется нигде** | **17** — не перерисовываем |
| битых ссылок (в базе есть, на диске нет) | 0 |
| **под перерисовку — очередь 1 (брак)** | **35** |
| **под перерисовку — очередь 2 (разнобой в стиле)** | **45** |
| поправить обрезкой, без генерации | 3 |
| оставляем как есть (материал, герои, карточки) | ~430 |

Причины по очереди 1:

| причина | штук |
|---|---|
| мыло (меньше 300 px по большей стороне) | 9 |
| спорит с ключом / мешает решить задание | 5 |
| чужой фон, мусор по краям | 2 (+3 чинятся обрезкой) |
| чужая картинка: скан учебника или сток-фото | 19 |

## 🔴 Два вопроса, которые надо решить до генерации

🔴 **1. Люди.** Правило от 03.11 — «фотография для сцен, мест и людей». Но все
люди в GG1 сейчас 3D-мультяшные и их много: `fam_*` (12), `hair_*` (8),
`pers_*` (6), `t1_*` (9), `she_*`/`he_*`/`they_*` (5) — больше сорока картинок,
и они держатся вместе как один мир. Перевод всех людей в фотографию — это
сорок генераций и потеря единства с персонажами учебника (Hammy, Dug, Superdug
приходят из учебника и мультяшные). **Предлагаем: людей оставляем в 3D,
правило «фотография» применяем к местам и реальным сценам** (дом, парк, город,
школьный двор). Промпты на портреты детей ниже написаны в 3D — если решение
будет другое, у них достаточно поменять первую строку на строку фото.

🔴 **2. Сцены и комнаты.** `room_*` (6), `place_*` (8), `house_danny_*` (3),
`t1_*` (9) — живописные рендеры, между собой согласованы и смотрятся хорошо.
Переводить их в фотографию — ещё около тридцати генераций без выигрыша.
**Предлагаем оставить.** В очередь на перерисовку взяли только те сцены, где
есть настоящий брак (скан учебника, чёрный фон, выцветшая бумага).

## Строки стиля

```
clean photograph, sharp focus, natural colours, bright daylight
```

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting
```

---

# Очередь 1 — брак, перерисовать обязательно

| файл | где используется | что не так | новое имя |
|---|---|---|---|
| `u3/prep_behind.webp` | Ю3 ДЗ2 бл.8 (match), бл.9 (quiz) | 240×240, бледно-голубой фон, серый стеклянный куб; мячик еле виден — «behind» не отличить от «next to» | то же |
| `u3/prep_in.webp` | Ю3 ДЗ2 бл.8, бл.9 | 240×240, тот же бледный набор | то же |
| `u3/prep_next_to.webp` | Ю3 ДЗ2 бл.8, бл.9 | 240×240, тот же бледный набор | то же |
| `u3/prep_under.webp` | Ю3 ДЗ2 бл.8, бл.9 | 240×240, тот же бледный набор | то же |
| `u3/prep_on.webp` | Ю3 ДЗ2 бл.8, бл.9; Ю3 тест бл.2 | сам по себе хорош (619×770, оранжевая коробка + баскетбольный мяч), но в одном задании с четырьмя бледными — **две разные «коробки» в одном вопросе** «The ball is ___ the box» | то же |
| `u3/prep_in_front_of.webp` | Ю3 ДЗ2 бл.8, бл.9; Ю3 тест бл.2 | то же — пересобрать в общем наборе | то же |
| `u0/obj_sharpener.webp` | Ю0 ДЗ3 бл.2 (карточки), бл.4 (match), бл.5 (quiz) | 266×262 — мыло; и фотография среди 3D-предметов | то же |
| `u3/furn_lamp.webp` | Ю3 ДЗ5 бл.2 (карточки), бл.4, бл.5, бл.7 | 124×278 — самая мелкая картинка курса | то же |
| `u4/kid_long_black.webp` | Ю4 ДЗ1 бл.13 (quiz, ключ «black + long») | 264×279, плоский вектор в кружке, поперёк лица светлая полоса от сжатия; рядом в той же домашке портреты `hair_*` в 3D | то же |
| `u4/kid_curly_black.webp` | Ю4 ДЗ1 бл.13 (ключ «black + curly») | 285×285, то же | то же |
| `u4/kid_short_blond.webp` | Ю4 ДЗ1 бл.13 (ключ «short + blond») | 283×296, то же | то же |
| `u4/kid_spiky_red.webp` | Ю4 ДЗ1 бл.13 (ключ «spiky + red») | 266×313, то же | то же |
| `u6/da_hang_out_with_friends.webp` | Ю6 ДЗ1 бл.2 (карточки), бл.4 (quiz), бл.6 (match); Ю6 ДЗ7 бл.15 (match) | **на картинке три самоката.** «Гулять с друзьями» по ней не угадать — задание «слово ↔ картинка» нерешаемо | то же |
| `u2/icons_favourite_things.webp` | Ю2 ДЗ6 бл.2 (hotspot, 6 подписей) | скан учебника: серая бумага, просвечивает текст с обратной стороны, **в первой клетке уже вписан ответ `trainers`**, нумерация 1–6 и линейки для ответа | то же |
| `u6/tv_schedule.webp` | Ю6 ДЗ4 бл.9 (gaps — по картинке читают время) | выцветший скан 900×242, почти пустое белое поле, текст просвечивает; время программ читается с трудом, а на нём держится весь ключ | то же |
| `u8/four_trees.webp` | Ю8 ДЗ4 бл.9 (hotspot: spring / summer / autumn / winter) | скан учебника с **напечатанными цифрами 1–4 и линейками для ответа** поверх hotspot-подписей, просвечивает текст сверху и снизу | то же |
| `u4/bike_yellow.webp` | Ю4 тест бл.6 (order) | **чёрный прямоугольный фон** вместо белого, плоский вектор | то же |
| `u7/animal_parrot.webp` | Ю7 ДЗ2 бл.3 (match) | слева от попугая висит зелёный обрывок — мусор в кадре | то же |
| `u6/cat_sunglasses.webp` | Ю6 ДЗ6 бл.10 (task) | **сток-фото реального кота** в круглых очках и толстовке с иероглифом; ни стиля курса, ни отношения к теме | то же |
| `u4/sorry_boy.webp` | Ю4 ДЗ4 бл.7 (gaps) | плоский клипарт из презентации, **английский текст в кадре** («Not Really!», «I'm Sorry» на листке) | то же |
| `u2/nancy_show.webp` | Ю2 ДЗ4 бл.6 (gaps) | скан учебника, ретро-кубистическая манера, бумажная фактура | то же |
| `u5/fruits_dance.webp` | Ю5 ДЗ3 бл.4 (gaps) | скан учебника, две панели с номерами 1 и 2, розовая бумага | то же |
| `u5/senses_icons.webp` | Ю5 ДЗ5 бл.2 (gaps) | 165×394, скан: серая бумага, просвечивает текст с обратной стороны, **английские подписи see / hear / smell вшиты в картинку** | то же |
| `u3/kids_at_door.webp` | Ю3 ДЗ4 бл.7 (gaps) | скан учебника, **чёрный фон** в дверном проёме и по небу, дети со спины | то же |
| `u1/tf_boy_backpack.webp` | Ю1 ДЗ3 бл.3 (quiz) | 320×211, скан учебника с бумажной фактурой | то же |
| `u1/tf_boys_bench.webp` | Ю1 ДЗ3 бл.3 (quiz) | 319×214, то же | то же |
| `u1/tf_girl_ten.webp` | Ю1 ДЗ3 бл.3 (quiz) | 310×215, то же | то же |
| `u1/teens_skatepark.webp` | Ю1 ДЗ4 бл.7 (gaps) | скан учебника, плоская пастельная манера — рядом в том же юните 3D-персонажи | то же |
| `u6/routine_icons.webp` | Ю6 ДЗ1 бл.10 (task) | бледные плоские иконки на голубом, человечек-палочка; в 3D-юните выглядит чужим | то же |
| `u0/diagram_classroom.webp` | Ю0 ДЗ3 бл.6 (hotspot) | **пять предметов в пяти разных манерах** на одном листе: плоское ведро, 3D-доска, фото-стул, плоские часы, 3D-парта | то же |
| `u7/animals_collage.webp` | Ю7 ДЗ1 бл.11 (task) | **фотоколлаж живых животных** в юните, где все животные 3D-мультяшные | то же |
| `u4/clown_bonzo.webp` | Ю4 ДЗ7 бл.3 (gaps) | фотореалистичный клоун; в Ю3 (`clowns.webp`) клоуны мультяшные — два разных мира | то же |
| `u4/girl_jumping.webp` | Ю4 ДЗ3 бл.2 (hotspot) | плоский вектор среди 3D | то же |
| `u4/english_class.webp` | Ю1 ДЗ2 бл.5 (quiz); Ю4 тест бл.5 (quiz) | плоский вектор среди 3D, используется в двух юнитах | то же |
| `u7/sport_balls.webp` | Ю7 тест бл.11 (order) | фотография мячей на траве с тёмным флагом; в 3D-юните чужая | то же |

## Чинится обрезкой, генерация не нужна

| файл | что | что сделать |
|---|---|---|
| `u4/body_foot.webp` | серая ниточка-линия вдоль верхнего края (остаток обрезки) | срезать 3–4 px сверху |
| `u7/adj_slow.webp` | такая же линия вдоль нижнего края | срезать снизу |
| `u5/verb_climb.webp` | такая же линия вдоль верхнего края | срезать сверху |

---

# Очередь 2 — разнобой в стиле

Везде одно и то же: **в одном блоке рядом стоят фотография и 3D-рендер.**
По решению Анны от 03.11 отдельный предмет в GG1 — 3D-рендер, поэтому
перерисовываем фотографии, а 3D оставляем.

### Юнит 0 — канцелярия (Ю0 ДЗ3 бл.2 карточки, бл.3–4 match, бл.5 quiz; Ю0 тест бл.2)

В одном наборе карточек шесть предметов 3D (`obj_bag`, `obj_bin`, `obj_board`,
`obj_book`, `obj_chair`, `obj_clock`, `obj_coloured_pencil`, `obj_ruler`,
`obj_apple`) и восемь фотографий:

`obj_desk` · `obj_notebook` · `obj_pen` · `obj_pencil` · `obj_pencil_case` ·
`obj_rubber` · `obj_sandwich` · `obj_scissors`
(`obj_sharpener` — в очереди 1 по размеру).

Подтверждение, что 3D здесь родной: те же предметы в `col_*`
(`col_green_notebook`, `col_red_pen`, `col_pink_pencil_case`, `col_yellow_ruler`)
уже нарисованы 3D.

### Юнит 2 — одежда (Ю2 ДЗ1 бл.2 карточки, бл.4–7, бл.9; Ю2 ДЗ7 бл.8; Ю2 тест)

Фотографии среди 3D-одежды:
`adj_new_old` · `clothes_boots` · `clothes_cap` · `clothes_gloves` ·
`clothes_trainers` · `clothes_tracksuit`

### Юнит 3 — мебель (Ю3 ДЗ1 бл.3 карточки, бл.8–10; Ю3 ДЗ5 бл.2, 4, 5, 7; Ю3 тест)

Фотореалистичные предметы рядом с мультяшными `furn_carpet`, `furn_wardrobe`,
`part_window`, `cat_sofa`:
`furn_armchair` · `furn_bath` · `furn_bed` · `furn_cushion` · `furn_fridge` ·
`furn_plant` · `furn_sofa` · `furn_table` · `furn_tv`
(`furn_lamp` — в очереди 1 по размеру).

### Юнит 5 — коллокации и предметы (Ю5 ДЗ7 бл.2; Ю5 тест бл.4, бл.5)

`coll_make_poster` · `coll_play_football` · `obj_broken_laptop` · `obj_mixing_bowl`

### Юнит 6 — распорядок дня (Ю6 ДЗ1; Ю6 тест бл.4, бл.11)

`da_have_breakfast` · `da_have_dinner` · `obj_school_canteen` ·
`birthday_cupcake` (на капкейке к тому же надпись «Happy Birthday»)

### Юнит 7 — прилагательные (Ю7 ДЗ5 бл.2 карточки, бл.4–5; Ю7 ДЗ7 бл.3)

`adj_fast` · `adj_ugly` — фотореалистичные гепард и жаба среди 3D-животных

### Юнит 8 — спорт, погода, здоровье

Спорт (Ю8 ДЗ1 бл.2 карточки, бл.4–10; Ю8 ДЗ7 бл.3; Ю8 тест бл.2):
`sport_ice_skating` · `sport_sailing` · `sport_skateboarding` · `sport_skiing` ·
`sport_swimming` · `sport_table_tennis` · `sport_windsurfing`

Погода (Ю8 ДЗ4 бл.5 match; Ю8 ДЗ7 бл.4 match):
`weather_foggy` · `weather_snowy` · `weather_warm` — живописные пейзажи
рядом с иконками-рендерами `weather_sunny`, `weather_cloudy`, `weather_rainy`,
`weather_hot`, `weather_cold`, `weather_windy`

Здоровье (Ю8 ДЗ5 бл.6 match; Ю8 ДЗ6 бл.2; Ю8 ДЗ7 бл.10):
`life_drink_water` (298 px — ещё и мыло) · `life_fruit_vegetables`

---

# Не перерисовываем

### Герои курса — берём из учебника, не генерируем

`u7/hammy.webp` · `u6/hammy_bedtime.webp` · `u6/hammy_weekend.webp` ·
`u8/dug_autograph.webp` · `u5/superdug_beach.webp` · `u2/comic_kit_dug.webp` ·
`u0/scene_zoo_colours.webp` (в кадре Superdug) · `u8/mandy_phone.webp` ·
`u1/comic_jill_1.webp` · `u1/comic_jill_2.webp`

Если какая-то из них понадобится крупнее — **нужен разворот от методиста**,
режем из него.

### Карточки лексики и грамматики — набранный текст, не рисунок

Все 46 файлов `card_*.webp` (900×506) во всех юнитах, плюс `u0/look_a_an`,
`u0/look_its_theyre`, `u6/adverbs_table`, `u6/before_after`,
`u8/tables_question_pronouns`, `u4/card_possessives`. Текст в них чёткий
в любом размере; перерисовывать нечего.

### Материал задания — по нему сверяются ответы

`u5/beach_actions` (буквы a–h для hotspot) · `u5/oliver_sarah` (таблица can/can't)
· `u5/suggestion_scenes` · `u5/teddy_code` · `u5/table_can` · `u5/verbs_objects`
· `u7/table_routines` · `u8/may_table` · `u4/face_numbers` (цифры 1–6 к частям
лица) · `u4/venn_have_got` · `u3/two_living_rooms` (найди отличия) ·
`u3/card_prepositions` · `u6/eric_day_comic` · `u6/girl_routine` · `u6/seasons` ·
`u3/house_cutaway`, `house_cutaway_cartoon`, `house_cutaway_family` ·
`u3/classroom_scene` · `u3/prepositions_living_room` · `u2/kids_outfits` ·
`u1/tree_mark` (семейное дерево) · `u4/broken_cup`, `u4/kids_hurt`,
`u4/scene_alarm_clock` (кадры истории).

Часть из них — тоже сканы, но на них держится ключ: цифры, буквы, галочки.
Перерисовывать такое — значит переписывать задание, это отдельная работа.

### Сцены, места и комнаты — оставляем по решению вопроса 🔴 2

`room_*` (6) · `place_*` (8) · `house_danny_1–3` · `t1_*` (9) · `far_*` (3) ·
`near_*` (2) · `dem_*` (4) · `scene_*` · `photo_*`.

Отдельно проверено: **`dem_this / dem_that / dem_these / dem_those`** собраны
верно (один футболка близко, один далеко, три близко, три далеко) и
**`house_danny_1/2/3`** различимы (одноэтажный с красной крышей; двухэтажный
с синей крышей и синей дверью; двухэтажный с красной крышей и красной дверью) —
ключ `[2]`, то есть третий дом.

### Не используется ни в одном блоке — 17 файлов

`final/final_computer.webp` · `final/final_grapes.webp` ·
`u0/col_orange_bag.webp` · `u1/place_library.webp` · `u3/furn_bookcase.webp` ·
`u3/furn_shower.webp` · `u3/photo_living_room.webp` ·
`u3/photo_presents_tree.webp` · `u5/animal_labrador.webp` ·
`u5/coll_play_piano.webp` · `u5/obj_goggles.webp` · `u5/obj_newspaper.webp` ·
`u5/obj_screwdriver.webp` · `u8/season_autumn.webp` · `u8/season_spring.webp` ·
`u8/season_summer.webp` · `u8/season_winter.webp`

Отдельно стоит заметить: **`season_spring/summer/autumn/winter` лежат готовыми
и красивыми, а в задании про времена года стоит скан `four_trees`.** Промпт
ниже это чинит; если Анна захочет, лист можно собрать прямо из этих четырёх.

---

# Промпты

Каждый — цельный блок, копируется одним движением. Строка стиля уже внутри.
Один предмет — одна генерация, сеток не просим.

## Очередь 1

### `u3/prep_in.webp` — предлог «in»

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. An open light brown cardboard box standing in the centre of the frame, and one orange basketball lying INSIDE the box, clearly visible above the rim of the box. The ball is in the box, not on it, not next to it. Plain flat pure white background, no shadow on the background, no floor, no table. Generous empty white margin on all four sides, nothing cropped by the edges. No text, no letters, no labels, no numbers, no arrows, no watermark.
```

### `u3/prep_on.webp` — предлог «on»

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A closed light brown cardboard box standing in the centre of the frame, and one orange basketball resting ON TOP of the box, in the middle of its lid. The ball is on the box, not inside it, not beside it. Plain flat pure white background, no shadow on the background, no floor, no table. Generous empty white margin on all four sides, nothing cropped by the edges. No text, no letters, no labels, no numbers, no arrows, no watermark.
```

### `u3/prep_under.webp` — предлог «under»

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A closed light brown cardboard box raised on four short legs in the centre of the frame, and one orange basketball lying on the ground UNDERNEATH the box, fully visible in the gap below it. The ball is under the box, not inside it, not behind it. Plain flat pure white background, no shadow on the background, no floor, no table. Generous empty white margin on all four sides, nothing cropped by the edges. No text, no letters, no labels, no numbers, no arrows, no watermark.
```

### `u3/prep_behind.webp` — предлог «behind»

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A closed light brown cardboard box standing in the centre of the frame, and one orange basketball BEHIND the box, farther from the viewer, so that the box hides the lower half of the ball and only the top of the ball is seen above the box. The ball is behind the box, not next to it, not on it. Plain flat pure white background, no shadow on the background, no floor, no table. Generous empty white margin on all four sides, nothing cropped by the edges. No text, no letters, no labels, no numbers, no arrows, no watermark.
```

### `u3/prep_in_front_of.webp` — предлог «in front of»

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A closed light brown cardboard box standing in the centre of the frame, and one orange basketball IN FRONT of the box, nearer to the viewer, slightly overlapping the lower part of the box. The ball is in front of the box, not beside it, not behind it. Plain flat pure white background, no shadow on the background, no floor, no table. Generous empty white margin on all four sides, nothing cropped by the edges. No text, no letters, no labels, no numbers, no arrows, no watermark.
```

### `u3/prep_next_to.webp` — предлог «next to»

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A closed light brown cardboard box standing in the centre of the frame, and one orange basketball on the ground NEXT TO the box, to its right, at the same distance from the viewer, the ball and the box side by side and not overlapping. The ball is next to the box, not in front of it, not behind it. Plain flat pure white background, no shadow on the background, no floor, no table. Generous empty white margin on all four sides, nothing cropped by the edges. No text, no letters, no labels, no numbers, no arrows, no watermark.
```

### `u0/obj_sharpener.webp` — точилка

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single small red plastic pencil sharpener with a shiny metal blade, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no desk, no surface. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u3/furn_lamp.webp` — лампа

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single tall floor lamp with a warm cream fabric shade and a slim golden stand, standing upright in the centre of the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no floor, no room. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u4/kid_short_blond.webp` — ответ «short + blond»

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A friendly smiling boy of about nine, head and shoulders portrait facing the viewer. His hair is SHORT and BLOND, cut close and neat, clearly light yellow. He wears a plain green t-shirt. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no coloured circle, no badge behind him. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u4/kid_spiky_red.webp` — ответ «spiky + red»

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A cheerful boy of about nine, head and shoulders portrait facing the viewer. His hair is SPIKY and RED, standing up in sharp ginger spikes. He wears a plain dark blue t-shirt. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no coloured circle, no badge behind him. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u4/kid_curly_black.webp` — ответ «curly + black»

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A friendly smiling boy of about nine with brown skin, head and shoulders portrait facing the viewer. His hair is CURLY and BLACK, a short round mass of tight dark curls. He wears a plain red hoodie. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no coloured circle, no badge behind him. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u4/kid_long_black.webp` — ответ «long + black»

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A friendly smiling girl of about nine, head and shoulders portrait facing the viewer. Her hair is LONG and BLACK, straight and smooth, falling well below her shoulders. She wears a plain light purple t-shirt. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no coloured circle, no badge behind her. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u6/da_hang_out_with_friends.webp` — «гулять с друзьями»

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. Three happy children of about ten hanging out together outdoors: they sit side by side on a park bench, laughing and talking, one of them holding a skateboard. It must read at a glance as friends spending time together. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no park scenery behind them, no sky, no grass. Nothing else in the frame, nobody cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u2/icons_favourite_things.webp` — лист из шести предметов для подписи

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A neat grid of six separate objects on one sheet, two columns and three rows, wide empty white gaps between the items so that each one can be cut out. Row 1, left to right: a pair of sports trainers, a school backpack. Row 2, left to right: a mountain bike, a hoodie. Row 3, left to right: a mobile phone, a games console controller. Every item complete, upright, and not touching any other item or the edge. Plain flat pure white background, no shadow on the background, no boxes, no frames, no lines. No text, no letters, no labels, no numbers, no watermark.
```

### `u6/tv_schedule.webp` — расписание телепрограмм

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A bright children's television schedule drawn as a single horizontal strip of five cards in a row, left to right, each card with a large clear digital clock time at the top and an empty white panel below it for a programme name. The five times, left to right, are exactly 06:00, 06:35, 07:05, 07:15 and 07:50. Every digit crisp and easy to read. Plain flat pure white background, no shadow on the background, no television set around the strip. Generous empty white margin above and below. No words, no letters, no labels, only the five times.
```

Названия программ (`Pet Time`, `Super Girl`, `Happy Days`, `That's Magic`,
`The Great Big Talent Show`) **впишем сами поверх пустых панелей** — генератору
надписи не доверяем, а от них зависит ключ.

### `u8/four_trees.webp` — четыре дерева по временам года

```
clean photograph, sharp focus, natural colours, bright daylight. Four separate trees arranged in a two by two grid on one sheet, wide empty white gaps between them. Top left: a tree in full pink and white blossom, spring. Top right: the same tree in thick green summer leaf. Bottom left: the same tree with orange and red autumn leaves. Bottom right: the same tree completely bare, black branches with snow, winter. All four trees the same shape and the same size, each one complete and not touching another tree or the edge. Plain flat pure white background, no shadow on the background, no ground, no sky. No text, no letters, no labels, no numbers, no lines.
```

Или собрать лист из готовых `u8/season_spring|summer|autumn|winter.webp` —
они уже лежат в `media/gg1/u8` и нигде не используются.

### `u4/bike_yellow.webp` — жёлтый велосипед

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single bright yellow bicycle seen from the side, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no road, no ground, no dark rectangle behind the bicycle. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u7/animal_parrot.webp` — попугай

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single cheerful parrot with red, yellow and blue feathers, sitting on a short wooden branch, seen from the side, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no leaves, no jungle. One bird only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u6/cat_sunglasses.webp` — кот (задание «My day»)

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single friendly cartoon tabby cat sitting upright and looking at the viewer, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no furniture, no room. One cat only, nothing else in the frame, no sunglasses, no clothes, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u4/sorry_boy.webp` — мальчик извиняется

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. Two children of about nine facing each other: a boy with a guilty, sorry expression, shoulders down and hands together, apologising to a girl who listens with her arms folded and a slightly cross face. It must read at a glance as an apology. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no furniture, no speech bubbles, no signs, no sheets of paper. No text, no letters, no labels, no numbers, no watermark.
```

### `u2/nancy_show.webp` — Нэнси на выставке

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A girl of about ten standing proudly beside her own painting, which hangs on a gallery wall at a school art show, while a man in a jacket looks at the picture and smiles. Bright gallery, a few visitors blurred in the far background. Centred in the frame with generous empty margin on all sides, nobody cropped by the edges. No text, no letters, no labels, no numbers, no signs, no name plates, no watermark.
```

### `u5/fruits_dance.webp` — две сцены: фруктовый киоск и танец

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. Two separate square scenes side by side on one sheet, with a wide empty white gap between them. Left scene: a boy of about ten helping an elderly woman carry a paper bag of fruit away from a market fruit stall full of apples and oranges. Right scene: a young man and a young woman dancing together on a small stage, she in a long red dress, he in a dark suit. Both scenes complete and not touching each other or the edge. Plain flat pure white background around the two scenes. No text, no letters, no labels, no numbers, no signs, no watermark.
```

### `u5/senses_icons.webp` — три органа чувств

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. Three separate objects in one vertical column on one sheet, wide empty white gaps between them so that each one can be cut out. Top: a single friendly cartoon eye. Middle: a single human ear seen from the side. Bottom: a single human nose seen from the side. All three drawn in the same manner and the same size, each one complete and not touching another item or the edge. Plain flat pure white background, no shadow on the background, no circles, no ribbons, no banners behind the items. No text, no letters, no labels, no numbers, no watermark.
```

### `u3/kids_at_door.webp` — дети у двери в гостях

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. Three children of about ten standing on the path at the open front door of a house, one of them reaching up to ring the doorbell, their bicycles leaning on the grass beside the path. Daytime, bright and friendly, the doorway warmly lit from inside. Centred in the frame with generous empty margin on all sides, nobody cropped by the edges. No dark or black areas, no night sky. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/tf_boy_backpack.webp` — мальчик в своей комнате

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A boy of about ten sitting on the floor of his bedroom leaning against the bed, reading a small book, his school backpack on the floor beside him and a few books stacked next to it. Bright tidy bedroom with a window and a curtain. Centred in the frame with generous empty margin on all sides, nobody cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/tf_boys_bench.webp` — два грустных мальчика на скамейке

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. Two boys of about ten sitting side by side on a park bench, both looking sad and bored, elbows on their knees, a football lying on the ground in front of them. Bright park, a tree and a bin behind the bench. Centred in the frame with generous empty margin on all sides, nobody cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/tf_girl_ten.webp` — девочка на своём дне рождения

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A happy girl of about ten at her own birthday party, arms thrown up in delight, wearing a party hat, pink and blue balloons and confetti around her. Centred in the frame with generous empty margin on all sides, nobody cropped by the edges. Plain light background, nothing written anywhere. No text, no letters, no labels, no numbers, no badges with numbers, no watermark.
```

Число «10» на кофточке, если оно нужно заданию, **ставим сами** — генератору
цифры не доверяем.

### `u1/teens_skatepark.webp` — трое подростков в скейтпарке

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. Three teenagers standing together and talking in a skatepark on a sunny day: a fair haired girl, a boy in a yellow hoodie and a dark haired girl with a skateboard under her arm. Concrete ramps and a basketball hoop behind them, green bushes at the sides. Centred in the frame with generous empty margin on all sides, nobody cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u6/routine_icons.webp` — иконки распорядка дня

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A neat grid of six separate objects on one sheet, three columns and two rows, wide empty white gaps between the items so that each one can be cut out. Row 1, left to right: a red alarm clock, a folded jumper, a cup of tea. Row 2, left to right: a bed with a blue blanket, a stack of school books, a toothbrush with a tube of toothpaste. Every item complete and not touching any other item or the edge. Plain flat pure white background, no shadow on the background, no circles, no badges behind the items. No text, no letters, no labels, no numbers, no watermark.
```

### `u0/diagram_classroom.webp` — пять предметов класса на одном листе

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A neat row of five separate objects on one sheet, wide empty white gaps between the items so that each one can be cut out. Left to right: a blue classroom waste bin, a green chalkboard in a wooden frame, a wooden school chair, a round wall clock with black hands, a wooden school desk. All five drawn in exactly the same manner and the same level of detail. Every item complete, upright, and not touching any other item or the edge. Plain flat pure white background, no shadow on the background, no classroom, no wall, no floor. No text, no letters, no labels, no numbers, no watermark.
```

### `u7/animals_collage.webp` — коллаж диких животных

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A neat grid of six separate wild animals on one sheet, three columns and two rows, wide empty white gaps between them so that each one can be cut out. Row 1, left to right: an elephant, a zebra, a lion. Row 2, left to right: a crocodile, a kangaroo, a giraffe. All six drawn in the same friendly cartoon manner and standing in full profile. Every animal complete and not touching another animal or the edge. Plain flat pure white background, no shadow on the background, no grass, no sky, no savannah. No text, no letters, no labels, no numbers, no watermark.
```

### `u4/clown_bonzo.webp` — клоун Бонзо

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single cheerful circus clown standing and waving, with a round red nose, curly orange hair, a tiny red hat, a bright spotted costume and big red shoes. Friendly and funny, not frightening. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no circus tent. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u4/girl_jumping.webp` — прыгающая девочка

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single happy girl of about nine with blond hair in two bunches, jumping into the air with both arms up and a big smile, seen head to toe. She wears a pink t-shirt and orange trousers. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no ground. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u4/english_class.webp` — урок английского

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A friendly teacher standing beside a big green chalkboard in a bright classroom, speaking to four children of about ten who sit at their wooden desks and look at her. Windows and a world map on the wall behind. Centred in the frame with generous empty margin on all sides, nobody cropped by the edges. The chalkboard is completely blank. No text, no letters, no labels, no numbers, no watermark.
```

### `u7/sport_balls.webp` — спортивные мячи

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A small group of sports balls together in the centre of the frame: a football, a basketball, a volleyball, a tennis ball and a rugby ball, resting side by side. Centred with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no grass, no pitch, no flag. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

## Очередь 2 — предметы из фотографий в 3D

Все по одному шаблону, меняется только предмет. Ниже — готовые блоки.

### Юнит 0 — канцелярия

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single wooden school desk with a light wooden top and slim metal legs, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no classroom, no floor. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u0/obj_desk.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single closed green spiral notebook lying slightly tilted, its metal spiral on the left side, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no desk, no surface. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u0/obj_notebook.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single blue ballpoint pen with its cap clipped on, lying diagonally, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no desk, no surface. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u0/obj_pen.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single sharpened yellow pencil with a pink rubber at the end, lying diagonally, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no desk, no surface. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u0/obj_pencil.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single closed blue fabric pencil case with a zip along the top, lying flat and seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no desk, no surface. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u0/obj_pencil_case.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single rectangular eraser, half red and half white, lying flat and seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no desk, no surface. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u0/obj_rubber.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single sandwich made of two slices of brown bread with cheese, tomato and lettuce showing at the edges, cut in half and standing on its cut side, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no plate, no table. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u0/obj_sandwich.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single pair of children's scissors with blue and yellow plastic handles and rounded metal blades, open, seen from above, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no desk, no surface. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u0/obj_scissors.webp`

### Юнит 2 — одежда

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. Two trainers side by side in one frame: on the left a brand new clean white trainer, on the right a worn, dirty, scuffed old trainer of the same shape. The difference between new and old must be obvious at a glance. Centred with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no floor. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no brand marks, no watermark.
```
→ заменяет `u2/adj_new_old.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single pair of brown leather boots with laces, standing side by side and seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no floor. One pair only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no brand marks, no watermark.
```
→ заменяет `u2/clothes_boots.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single dark blue baseball cap seen from a three quarter angle, peak to the left, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no surface. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no logos, no watermark.
```
→ заменяет `u2/clothes_cap.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single pair of red knitted winter gloves lying side by side, fingers upward, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no surface. One pair only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u2/clothes_gloves.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single pair of navy blue sports trainers with white soles, standing side by side and seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no floor. One pair only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no brand marks, no logos, no watermark.
```
→ заменяет `u2/clothes_trainers.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single navy blue tracksuit shown as a set: the zipped jacket with white stripes on the sleeves above, the matching tracksuit trousers below, both laid out flat and facing the viewer. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no hanger, no surface. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no brand marks, no watermark.
```
→ заменяет `u2/clothes_tracksuit.webp`

### Юнит 3 — мебель

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single comfortable green fabric armchair with short wooden legs, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no floor. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u3/furn_armchair.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single white bathtub with a silver tap at one end, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no bathroom, no tiles, no floor. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u3/furn_bath.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single single bed with a wooden headboard, a white pillow and a folded green blanket, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no bedroom, no floor. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u3/furn_bed.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single square cushion with a simple leaf pattern in warm orange, green and cream, standing on one corner and seen from the front, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no sofa, no surface. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u3/furn_cushion.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single mint green two door fridge with rounded corners and a slim metal handle, closed, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no kitchen, no floor. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u3/furn_fridge.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single green house plant with broad glossy leaves in a plain white pot, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no floor. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u3/furn_plant.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single blue three seat fabric sofa with two cushions and short wooden legs, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no floor. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u3/furn_sofa.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single rectangular wooden dining table with four straight legs, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no floor, no chairs. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u3/furn_table.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single flat screen television with a black screen standing on a low wooden stand, seen from the front, centred in the frame with generous empty margin on all sides. The screen is completely blank and dark. Plain flat pure white background, no shadow on the background, no room, no wall, no floor. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u3/furn_tv.webp`

### Юнит 5 — коллокации и предметы

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A large blank white poster lying flat with a set of paint pots, a paint brush and a round palette beside it, ready for making a poster. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no table, no surface. Nothing else in the frame, nothing cropped by the edges. The poster is completely blank. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u5/coll_make_poster.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single black and white football resting in front of a small white goal with a net, seen from the front, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no grass, no pitch, no sky. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u5/coll_play_football.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single open laptop with a cracked dark screen, clearly broken, and a yellow screwdriver lying in front of it, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no table, no surface. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u5/obj_broken_laptop.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single metal mixing bowl with a blue handled whisk standing in it, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no kitchen, no table. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u5/obj_mixing_bowl.webp`

### Юнит 6 — распорядок дня

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A breakfast set in the centre of the frame: a bowl of cereal with a spoon, a slice of toast on a small plate and a glass of orange juice. Centred with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no table, no tablecloth. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u6/da_have_breakfast.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A dinner plate with chicken, potatoes and vegetables, a knife and fork beside it and a glass of water, all in the centre of the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no table, no candle, no tablecloth. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u6/da_have_dinner.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A school canteen lunch tray holding a sandwich, an apple, a few carrot sticks and a carton of milk, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no canteen, no table. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u6/obj_school_canteen.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single birthday cupcake with swirled cream frosting, colourful sprinkles and one lit candle on top, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no plate, no table, no bunting. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no banner, no topper with writing, no watermark.
```
→ заменяет `u6/birthday_cupcake.webp`

### Юнит 7 — прилагательные

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single cheetah running at full speed, legs stretched out, seen from the side, drawn in the same friendly cartoon manner as the other animals of the course. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no grass, no savannah, no motion lines. One animal only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u7/adj_fast.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single warty toad sitting and looking at the viewer, drawn in a friendly cartoon manner, funny rather than frightening. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no pond, no grass. One animal only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u7/adj_ugly.webp`

### Юнит 8 — спорт

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single pair of white figure skates with silver blades, standing side by side and seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no ice, no rink. One pair only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u8/sport_ice_skating.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single small white sailing boat with one tall white sail, seen from the side, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no sea, no waves, no sky. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u8/sport_sailing.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single skateboard with a dark deck and bright wheels, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no ramp, no floor. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u8/sport_skateboarding.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single pair of red and white skis standing upright side by side with two ski poles beside them, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no snow, no mountain. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u8/sport_skiing.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single blue swimming cap with a pair of swimming goggles lying beside it, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no pool, no water, no tiles. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u8/sport_swimming.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. Two table tennis bats with red rubber faces and one small white ball, lying together in the centre of the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no table, no net. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u8/sport_table_tennis.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single windsurfing board with a tall orange and white sail standing on it, seen from the side, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no sea, no waves, no sky. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u8/sport_windsurfing.webp`

### Юнит 8 — погода

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single weather icon for fog: a grey cloud low down with three soft grey horizontal fog bands beneath it, drawn in the same manner as the other weather icons. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no landscape, no trees, no field. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u8/weather_foggy.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single weather icon for snow: a soft white and grey cloud with several white snowflakes falling below it, drawn in the same manner as the other weather icons. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no landscape, no trees, no ground. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u8/weather_snowy.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A single weather icon for warm weather: a bright yellow sun with a small white cloud in front of its lower edge and a thermometer beside it showing a middle level of red, drawn in the same manner as the other weather icons. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no landscape, no meadow, no flowers. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u8/weather_warm.webp`

### Юнит 8 — здоровый образ жизни

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A tall glass of clear water beside a closed blue water bottle, both standing upright in the centre of the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no table, no surface. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no brand marks, no watermark.
```
→ заменяет `u8/life_drink_water.webp`

```
3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting. A wooden bowl filled with fresh fruit and vegetables: a banana, a red apple, an orange, a tomato, green broccoli and a carrot, all clearly visible. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no table, no cloth. Nothing else in the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```
→ заменяет `u8/life_fruit_vegetables.webp`

---

# Как проверять то, что сгенерится

По каждой картинке, прежде чем ставить в блок (требование Анны от 03.11.2026):

1. нарисовано именно то, что просили;
2. предмет один, без дублей и лишних объектов;
3. фон белый, без тени и подложки;
4. предмет не обрезан краем, поле по кругу есть;
5. нет текста, букв, цифр и подписей;
6. стиль совпадает с остальными картинками курса;
7. если от картинки зависит ключ — на ней ровно то, что в ключе
   (особенно `prep_*`, `kid_*`, `four_trees`, `tv_schedule`,
   `icons_favourite_things`);
8. после обрезки не меньше 600 px по большей стороне для карточки
   и 1200 px для сцены (правило «хранить с запасом» от 23.10.2026).

Имена файлов не меняются ни у одной картинки — блоки в базе править не надо.
