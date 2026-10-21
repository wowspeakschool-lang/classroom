# SM1 · промпты на картинки — один список на весь курс

Собрано 21.10.2026 по отчётам правок `builds/sm1/fix/u*.md`, отчётам первого
прохода `builds/sm1/review/u*.md` и по собственной проверке размеров
(`python3.13 tools/img_sizes.py media/sm1 300` + сверка с базой: в список попало
только то, что реально стоит в блоках).

Файл разбит на три части:

1. **Обязательные** — картинки нет вовсе или она ломает задание (ответ по ней
   не читается или спорит с ключом). 19 промптов.
2. **Замена мелких** — картинка есть и верная, но мылится в плитке. 5 промптов.
3. **Не перерисовывать** — материал заданий. Трогать нельзя.

Ниже промптов — короткий список того, что **рисовать не надо**: три картинки
берутся из тренажёра слов и две ссылки просто переставляются.

---

## Две строки стиля

В курсе два регистра, и они не смешиваются:

- **ПРЕДМЕТ** — школьные вещи, игрушки, еда, фигуры: объёмный 3D-рендер на белом.
- **СЦЕНА / ПЕРСОНАЖ** — дети, герои, сюжетные картинки: плоская рисованная
  детская иллюстрация с контуром.

Отдельно запоминать их не нужно: **нужная строка уже вклеена в каждый промпт
ниже**, промпт копируется одним блоком целиком.

---

# 1. ОБЯЗАТЕЛЬНЫЕ

## 1.1 `sm1_heroes_sheet.webp` — ЛИСТ 2×3

**Где используется:** юнит 0 · ДЗ 1 блоки 2, 5, 6, 8, 9 и 15 · ДЗ 2 блоки 15, 16, 17 ·
ДЗ 4 блоки 12, 13, 17 · тест блок 3; юнит 2 · ДЗ 2 блок 12.
(Номера блоков — какими они станут после `udalit_u0.sql`.)
**Что на ней:** четыре героя курса, котик Tabby и мальчик. Сейчас это шесть
картинок по 91–138 px — в карточках и в плитках ответа они мылятся сильнее всего
в курсе, а в юните 2 вместо Flash вообще стоит кадр из чужого мультфильма.

🟥 **Ответ зависит от картинки.** В заданиях спрашивают «His name's …» / «Her
name's …», поэтому пол должен читаться с первого взгляда: **Misty — девочка,
Flash — девочка, Thunder — мальчик.** (По ключу юнита 2, ДЗ 2, блок 12 верный
ответ — «Her name's Flash.», а на нынешней картинке Flash похож на мальчика.)

🟥 **Вопрос:** Whisper — мальчик или девочка? Ни в одном задании пол Whisper не
спрашивают, на нынешней картинке стрижка каре. В промпте ниже Whisper — мальчик;
если это не так, скажите, и строку поправим.

```
Flat cartoon children's book illustration, bold clean dark outlines, bright flat
colours, friendly round-faced characters with big expressive eyes, drawn as a
sheet of six separate figures in a 3 by 2 grid. Row 1, left to right: a boy
superhero about seven years old with short brown hair, a blue mask, a blue
superhero suit with a yellow lightning bolt on the chest and a blue cape; a girl
superhero about seven years old with long wavy blonde hair, a purple mask, a
purple superhero suit with a lilac spiral on the chest and a purple cape; a boy
superhero about seven years old with short black hair, a green mask, a green
superhero suit with a yellow leaf on the chest and a green cape. Row 2, left to
right: a girl superhero about seven years old with curly orange hair in a
ponytail, a yellow mask, a yellow superhero suit with an orange sun on the chest
and a yellow cape, clearly a girl; a friendly striped brown tabby kitten sitting
and facing the viewer; a cheerful boy about seven years old in a brown T-shirt
and grey shorts, waving one hand. Every figure stands upright, full body, facing
the viewer. Plain flat pure white background, no shadow on the background, wide
empty white gaps between the figures, every figure complete and not touching any
other figure or the edge. No text, no letters, no labels, no numbers.
```

---

## 1.2 `sm1_u2_toy_ball.webp`

**Где используется:** юнит 2 · ДЗ 1 блоки 2, 4, 5, 8 · ДЗ 5 блок 9 · тест блоки
6 и 12 (диктант); юнит 5 · ДЗ 2 блок 6.
**Что на ней:** жёлтый мяч-игрушка. Сейчас `u2/t_yellow_ball.webp` — 212×228 и
это просто жёлтый шар без признаков мяча; в диктанте по нему пишут слово `ball`.

```
3D rendered object illustration for a children's English app, bright saturated
colours, soft rounded shapes, smooth surfaces, gentle even studio light. A single
yellow toy ball for small children, clearly a ball and not a plain sphere: it has
a visible seam and a wide white band with small orange stars printed around the
middle. The ball is shown whole, from slightly above, filling most of the frame.
Plain flat pure white background, no shadow on the background, generous empty
white margin on every side so the ball is complete and does not touch the edge.
No text, no letters, no labels, no numbers.
```

---

## 1.3 `sm1_u2_shape_kite.webp`

**Где используется:** юнит 2 · ДЗ 6 блок 5, вопрос 3.
**Что на ней:** плоская геометрическая фигура «kite» (ромб-дельтоид). Сейчас
`legacy/17b48218629f.webp` — фотография настоящего воздушного змея в небе, а
остальные четыре фигуры этого же задания — ровные плоские фигуры на белом.

```
Flat geometric shape illustration for a children's maths worksheet, one single
shape drawn in a flat solid colour with a thin darker outline and no gradients
and no shading. The shape is a kite quadrilateral: a four-sided figure standing
on its point, with two short equal sides at the top and two long equal sides at
the bottom, filled in flat light blue with a thin darker blue outline. The shape
is centred and fills most of the frame. Plain flat pure white background, no
shadow on the background, generous empty white margin on every side so the shape
is complete and does not touch the edge. No text, no letters, no labels, no
numbers.
```

---

## 1.4 `sm1_u2_lisa_fiona.webp` — ЛИСТ 1×2

**Где используется:** юнит 2 · ДЗ 2 блок 11, вопросы 2 и 3.
**Что на ней:** две девочки — Lisa и Fiona. Сейчас Lisa — стоковое фото живой
девочки, Fiona — кадр из чужого мультфильма, а Daniel в том же задании —
рисованный мальчик. Три картинки одного задания в трёх разных стилях.

```
Flat cartoon children's book illustration, bold clean dark outlines, bright flat
colours, friendly round-faced children with big expressive eyes, drawn as a sheet
of two separate figures side by side. Left: a girl about seven years old with
long straight blonde hair, in a red T-shirt and blue jeans, standing and smiling
at the viewer. Right: a different girl about seven years old with orange hair in
two short pigtails, in a green dress, standing and smiling at the viewer. Both
figures are full body, facing the viewer, clearly girls and clearly different
from each other. Plain flat pure white background, no shadow on the background,
a wide empty white gap between the two figures, every figure complete and not
touching the other figure or the edge. No text, no letters, no labels, no
numbers.
```

---

## 1.5 `sm1_u3_test_rat_bag.webp`

**Где используется:** юнит 3 · тест юнита.
**Что на ней:** крыса, выглядывающая из сумки. Сейчас на картинке нарисована
мультяшная **мышь**, а целевое слово юнита — **rat**.

```
Flat cartoon children's book illustration, bold clean dark outlines, bright flat
colours, friendly and not scary. A brown rat with a long bare pink tail, large
round ears and whiskers, sitting inside an open red school bag and looking out
over its edge. The rat is clearly a rat and not a small mouse: large body, long
thick tail, visible all the way. Plain flat pure white background, no shadow on
the background, generous empty white margin on every side so the bag and the rat
are complete and do not touch the edge. No text, no letters, no labels, no
numbers.
```

---

## 1.6 `sm1_u3_test_animals_where.webp` — СЦЕНА

**Где используется:** юнит 3 · тест юнита.
**Что на ней:** комната с животными. Ответы задания — где кто находится,
поэтому каждое животное должно узнаваться и лежать ровно там, где сказано:
ящерица **в сумке**, лягушка **на коробке**, собака **на диване**, крыса **под
столом**, кот **под стулом**. Сейчас существо в сумке по ключу `lizard`, а
нарисовано круглоголовым и без хвоста.

```
Flat cartoon children's book illustration, bold clean dark outlines, bright flat
colours, friendly round shapes, a simple living room scene drawn in one wide
picture. In the scene: a green lizard with a long tail sitting INSIDE an open
school bag on the floor, its head and tail clearly visible above the bag; a green
frog sitting ON TOP of a red box; a brown puppy lying ON a light blue sofa; a
brown rat with a long tail standing UNDER a small wooden table; a grey cat
sitting UNDER a wooden chair. Each animal is drawn whole, clearly recognisable
and clearly in its place. The furniture is simple and spaced out so nothing
overlaps. Plain flat pure white background behind the furniture, no shadow on the
background, generous empty white margin on every side so nothing touches the
edge. No text, no letters, no labels, no numbers.
```

---

## 1.7 `sm1_u3_spider_table.webp`

**Где используется:** юнит 3 · ДЗ 4 блок 5.
**Что на ней:** паук под столом. Сейчас `legacy/18a2166a5a38.webp` — тёмный
кадр 300×236, ответ «under the table» по нему почти не читается.

```
Flat cartoon children's book illustration, bold clean dark outlines, bright flat
colours, friendly and not scary. A small friendly black spider with big round
white eyes and eight legs, sitting on the floor clearly UNDERNEATH a wooden
table: the whole table is visible from the side, and the spider is in the open
space between the table legs, below the table top. The spider is drawn large
enough to be seen at a glance. Bright daylight colours, nothing dark or gloomy.
Plain flat pure white background, no shadow on the background, generous empty
white margin on every side so the table and the spider are complete and do not
touch the edge. No text, no letters, no labels, no numbers.
```

---

## 1.8 `sm1_u3_pets_needs.webp` — ЛИСТ 1×3

**Где используется:** юнит 3 · ДЗ 6 блок 8 (три вопроса).
**Что на ней:** три картинки «чего не хватает питомцу». Сейчас две из трёх —
стоковые фото, третья — плоский рисунок, и ответы по ним не читаются: у плачущего
кота стоит **пустая** миска при ключе «water», а «food» в вариантах тоже есть.

🟥 **Ответ зависит от картинки.** Нужно ровно так:
вопрос 1 — кролик, ответ **food**; вопрос 2 — собака, ответ **shelter**;
вопрос 3 — кот, ответ **water**.

```
Flat cartoon children's book illustration, bold clean dark outlines, bright flat
colours, friendly round-faced animals, drawn as a sheet of three separate
pictures in one row. Left: a hungry rabbit with an empty food bowl in front of it
and a carrot lying far away out of its reach, the rabbit stretching towards the
carrot; there is water in a second small bowl next to it, so only the food is
missing. Middle: a sad dog sitting outside in the rain with no kennel and no
roof anywhere, a full food bowl and a full water bowl beside it, so only shelter
is missing. Right: a sad cat sitting next to a completely empty dry water bowl,
with a full plate of food beside it and a cosy cat basket behind it, so only
water is missing. Each picture is a small complete scene. Plain flat pure white
background, no shadow on the background, wide empty white gaps between the three
pictures, every picture complete and not touching any other picture or the edge.
No text, no letters, no labels, no numbers.
```

---

## 1.9 `sm1_u4_have_we_got.webp` — ЛИСТ 2×3

**Где используется:** юнит 4 · ДЗ 3 блок 4 (шесть вопросов «Have we got any…?»).
**Что на ней:** шесть продуктов, у каждого зелёная галочка «есть» или красный
крест «нет». Сейчас пять картинок — разностильные иконки 260 px, а у шестой
(торт) пометки нет вообще, и ребёнок отвечает наугад.

🟥 **Ответ зависит от картинки.** Пометки должны быть ровно такие:
яблоки ✓, бананы ✗, сосиски ✓, сыр ✗, курица ✗, торт ✓.

```
3D rendered food illustration for a children's English app, photographic-looking
appetising food, bright saturated colours, soft rounded shapes, gentle even
studio light, drawn as a sheet of six separate pictures in a 3 by 2 grid. Row 1,
left to right: three red apples, with a large bright green tick mark in the
corner of the picture; a bunch of yellow bananas, with a large red cross mark
drawn over the picture; three grilled sausages on a white plate, with a large
bright green tick mark in the corner of the picture. Row 2, left to right: a
wedge of yellow cheese, with a large red cross mark drawn over the picture; a
whole roast chicken on a white plate, with a large red cross mark drawn over the
picture; a round cake with pink icing and a cherry on top, with a large bright
green tick mark in the corner of the picture. The tick marks and cross marks are
simple flat shapes, thick and clearly visible, and they are the only marks in the
image. Plain flat pure white background, no shadow on the background, wide empty
white gaps between the six pictures, every item complete and not touching any
other item or the edge. No text, no letters, no labels, no numbers.
```

---

## 1.10 `sm1_u4_potatoes_plums.webp` — ЛИСТ 1×2

**Где используется:** юнит 4 · ДЗ 6 блок 6 и ДЗ 7 блок 7 («где растёт еда»).
**Что на ней:** картошка и сливы. Картинок нет вовсе — сейчас оба слова стоят
текстом, и в столбиках `in the soil` и `on a tree` остаётся по одному слову.
Картошка должна быть **сырая, с землёй** (она растёт в земле), сливы — **на
ветке с листьями** (они растут на дереве).

```
3D rendered food illustration for a children's English app, photographic-looking
appetising food, bright saturated colours, soft rounded shapes, gentle even
studio light, drawn as a sheet of two separate pictures side by side. Left: a
small pile of four raw brown potatoes with a little dry soil still on their
skins, unpeeled and uncooked. Right: a small cluster of four ripe dark purple
plums still attached to a short green branch with a few green leaves. Plain flat
pure white background, no shadow on the background, a wide empty white gap
between the two pictures, every item complete and not touching the other item or
the edge. No text, no letters, no labels, no numbers.
```

---

## 1.11 `sm1_u4_food_fish.webp`

**Где используется:** юнит 4 · ДЗ 1 блоки 2, 5, 7 · ДЗ 2 блок 3.
**Что на ней:** рыба как еда. Сейчас на этом месте `legacy/4a17d6ba0ca1.webp` —
220×220 и это мультяшная синяя **аквариумная** рыбка, а весь остальной комплект
юнита 4 — готовые блюда на белой тарелке.

```
3D rendered food illustration for a children's English app, photographic-looking
appetising food, bright saturated colours, soft rounded shapes, gentle even
studio light. A single cooked fish fillet on a round white plate, golden and
lightly grilled, with a thin slice of lemon beside it, seen from slightly above.
It is clearly fish prepared as a meal, not a live fish and not an aquarium fish.
Plain flat pure white background, no shadow on the background, generous empty
white margin on every side so the plate is complete and does not touch the edge.
No text, no letters, no labels, no numbers.
```

---

## 1.12 `sm1_u4_empty_plate.webp`

**Где используется:** юнит 4 · тест блок 4, вопрос 2 («We ___ any steak.»,
ключ `haven't got`).
**Что на ней:** пустая тарелка. Картинка стейка спорила с ответом «у нас нет
стейка» и снята; сейчас вопрос идёт вообще без опоры.

```
3D rendered object illustration for a children's English app, bright saturated
colours, soft rounded shapes, smooth surfaces, gentle even studio light. One
completely empty round white dinner plate with a fork and a knife lying neatly on
either side of it, seen from slightly above. There is no food of any kind on the
plate or anywhere in the picture. Plain flat pure white background, no shadow on
the background, generous empty white margin on every side so the plate and the
cutlery are complete and do not touch the edge. No text, no letters, no labels,
no numbers.
```

---

## 1.13 `sm1_u5_play_ball_go_fishing.webp` — ЛИСТ 1×2

**Где используется:** юнит 5 · ДЗ 2 блок 6 (вопрос 10) — и ДЗ 2 блок 2 (карточки),
куда `go fishing` сейчас добавлен одним текстом.
**Что на ней:** два занятия — `play ball` и `go fishing`. Сейчас `play ball`
показан просто жёлтым шаром (`u2/t_yellow_ball.webp`, 212×228), хотя все
остальные варианты этого задания — дети за делом; картинки `go fishing` нет
совсем, и в задание «посмотри на картинку» это занятие поставить нечем.

```
Flat cartoon children's book illustration, bold clean dark outlines, bright flat
colours, friendly round-faced children about seven years old with big expressive
eyes, drawn as a sheet of two separate pictures side by side. Left: a boy
standing on the grass and throwing a big colourful ball up with both hands,
clearly playing with a ball. Right: a girl sitting on a small wooden jetty by a
lake, holding a fishing rod with the line in the water, clearly fishing. Each
picture is a small complete scene. Plain flat pure white background, no shadow on
the background, a wide empty white gap between the two pictures, every picture
complete and not touching the other picture or the edge. No text, no letters, no
labels, no numbers.
```

---

## 1.14 `sm1_u6_food_count.webp` — ЛИСТ 2×2

**Где используется:** юнит 6 · ДЗ 2 блок 4 (`match` «There are four apples» и т. д.).
**Что на ней:** четыре продукта. Сейчас все четыре — 200 px по большей стороне,
а в юните 4 лежат одиночные предметы и подменить ими нельзя: **ответ завязан на
количество**.

🟥 **Ответ зависит от картинки.** Количество должно быть ровно такое:
**четыре** яблока, **три** банана, **три** сосиски, **один** сэндвич.

```
Flat cartoon children's book illustration, bold clean dark outlines, bright flat
colours, simple friendly shapes, drawn as a sheet of four separate pictures in a
2 by 2 grid. Row 1, left to right: exactly four apples in a yellow bowl, two red
and two green, each apple whole and separately countable; exactly three yellow
bananas joined in one bunch, each banana clearly separate and countable. Row 2,
left to right: exactly three grilled sausages lying side by side on a blue plate,
each sausage clearly separate and countable; exactly one sandwich of two slices
of bread with cheese, on a green plate. The number of items in each picture must
be exactly as described and easy to count at a glance. Plain flat pure white
background, no shadow on the background, wide empty white gaps between the four
pictures, every picture complete and not touching any other picture or the edge.
No text, no letters, no labels, no numbers.
```

---

## 1.15 `sm1_u6_hw3_dogs.webp`

**Где используется:** юнит 6 · ДЗ 3 блок 4 («сколько собак?»).
**Что на ней:** четыре собаки. Сейчас на картинке напечатано слово «DOGS» и
нарисовано сердечко, а фон голубой — по регламенту надписей в кадре быть не
должно.

```
Flat cartoon children's book illustration, bold clean dark outlines, bright flat
colours, friendly round-faced puppies with big eyes, drawn as one picture with
exactly four different dogs arranged in a 2 by 2 group: a beagle puppy sitting, a
pug puppy sitting, a small brown dachshund puppy sitting, and a corgi puppy
standing. Each dog is whole, clearly separate and easy to count at a glance.
There are exactly four dogs and nothing else in the picture. Plain flat pure white
background, no shadow on the background, wide empty white gaps between the dogs,
every dog complete and not touching any other dog or the edge. No text, no
letters, no labels, no numbers, no hearts, no decorations.
```

---

## 1.16 `sm1_u8_body_fingers.webp`

**Где используется:** юнит 8 · ДЗ 1 блоки 4, 6, 8 · ДЗ 7 блок 3 · тест блок 1.
**Что на ней:** мишка, у которого подсвечены **только пальцы**. Сейчас
`body_fingers.webp` и `body_hand.webp` — одна и та же жёлтая лапа: в `match` они
лежат рядом, а в «напиши слово» ребёнок честно пишет `hand` там, где ждут
`fingers`. (Промпт взят из `review/u8.md`, раздел D.)

```
3D rendered cartoon illustration, soft plush teddy bear character, friendly and
cute, rendered in the same style as a children's app icon. The bear holds up one
open paw towards the viewer. ONLY the five fingers of that paw are bright yellow
and glowing; the palm and the rest of the bear stay natural brown plush. Plain
flat pure white background, no shadow on the background, generous empty margin on
every side so nothing touches the edge. No text, no letters, no labels, no
numbers.
```

---

## 1.17 `sm1_u8_can_cant_pairs.webp` — ЛИСТ 1×2

**Где используется:** юнит 8 · ДЗ 3 блок 7 и ДЗ 7 блок 4.
**Что на ней:** мальчик и девочка, у каждого ровно **два** предмета с пометками.
Сейчас на первой картинке рядом с мальчиком нарисован велосипед вообще без
пометки (ребёнок решит, что про него забыли спросить) и сыр с яблоком под
галочкой, а на второй в углу висит зелёная галочка без картинки.

🟥 **Ответ зависит от картинки.** Пометки должны быть ровно такие:
мальчик — ракетка ✓ (Can he play tennis? — Yes), кастрюля ✗ (Can he cook? — No);
девочка — балерина ✓ (Can she dance? — Yes), крылья ✗ (Can she fly? — No).
Больше никаких предметов и никаких лишних галочек в кадре быть не должно.

```
Flat cartoon children's book illustration, bold clean dark outlines, bright flat
colours, friendly round-faced children about seven years old with big expressive
eyes, drawn as a sheet of two separate pictures side by side. Left: a boy in a
blue T-shirt and green shorts standing in the middle, with exactly two objects
beside him and nothing else: a tennis racket above his left shoulder with a large
bright green tick mark next to it, and a cooking pot above his right shoulder with
a large red cross mark over it. Right: a girl in a pink T-shirt and purple skirt
standing in the middle, with exactly two objects beside her and nothing else: a
small ballerina dancing in a tutu above her left shoulder with a large bright
green tick mark next to it, and a pair of feathered wings above her right shoulder
with a large red cross mark over them. Each picture contains exactly one child,
exactly two objects, exactly one green tick and exactly one red cross; there are
no other objects and no stray marks anywhere. Plain flat pure white background, no
shadow on the background, a wide empty white gap between the two pictures, every
picture complete and not touching the other picture or the edge. No text, no
letters, no labels, no numbers.
```

---

## 1.18 `sm1_u8_she_cant_ride_horse.webp`

**Где используется:** юнит 8 · ДЗ 3 блок 7 и ДЗ 5 блок 8.
**Что на ней:** девочка **рядом** с пони, ответ — «No, she can't». В исходнике
девочка едет верхом (то есть умеет), лошадь обрезана по правому краю, и в углу
стоит водяной знак стокового банка. (Промпт взят из `review/u8.md`, раздел D.)

```
3D rendered cartoon illustration in a bright children's book style. A girl in a
riding helmet stands on the grass NEXT TO a small pony, holding the reins and
looking unsure; she is clearly NOT on the pony and not riding it. A large red
cross mark in the top right corner. Plain flat pure white background, no shadow on
the background, generous empty margin on every side so nothing touches the edge.
No text, no letters, no labels, no numbers.
```

---

## 1.19 `sm1_u9_test_pink_shoes.webp`

**Где используется:** юнит 9 · тест блок 6 («Where are your pink shoes?»).
**Что на ней:** розовые **туфли**. Сейчас `test_pink_shoes.webp` — 220×242 и на
ней нарисованы пляжные вьетнамки, а слово юнита — `shoes`. Коричневые туфли
`u7/clothes_shoes.webp` по размеру подходят, но они не розовые.

```
3D rendered object illustration for a children's English app, bright saturated
colours, soft rounded shapes, smooth surfaces, gentle even studio light. A pair
of bright pink children's shoes with white laces and white soles, both shoes
standing side by side and seen from slightly above at a three-quarter angle. They
are proper closed shoes with laces, not sandals and not flip-flops. Plain flat
pure white background, no shadow on the background, generous empty white margin on
every side so both shoes are complete and do not touch the edge. No text, no
letters, no labels, no numbers.
```

---

# 2. ЗАМЕНА МЕЛКИХ

Эти картинки верные, задание по ним решается — но в плитке ответа они мылятся.
Если на всё не хватит времени, они ждут до следующего захода.

## 2.1 `sm1_u1_pencil_case_green.webp`

**Где используется:** юнит 1 · ДЗ 1 блок 19, вопрос 8 («It's a ___ pencil case.»,
ключ `green`).
**Что на ней:** зелёный мягкий пенал. Сейчас 295×180. Пенал `u1/t_pencil_case.webp`
подошёл бы по размеру, но он розовый, а ответ — «green».

```
3D rendered object illustration for a children's English app, bright saturated
colours, soft rounded shapes, smooth surfaces, gentle even studio light. One
closed soft fabric pencil case in bright grass green with a silver zip along the
top, lying flat and seen at a three-quarter angle. The colour is unmistakably
green over the whole case. Plain flat pure white background, no shadow on the
background, generous empty white margin on every side so the pencil case is
complete and does not touch the edge. No text, no letters, no labels, no numbers.
```

---

## 2.2 `sm1_u1_box.webp`

**Где используется:** юнит 1 · ДЗ 2 блок 6 (`match`, «It's a box.»).
**Что на ней:** картонная коробка. Сейчас 235×180.

```
3D rendered object illustration for a children's English app, bright saturated
colours, soft rounded shapes, smooth surfaces, gentle even studio light. One
closed light brown cardboard box with a lid, seen at a three-quarter angle so
that the front and one side and the top are visible. The box is plain, with no
pattern and no tape and nothing printed on it. Plain flat pure white background,
no shadow on the background, generous empty white margin on every side so the box
is complete and does not touch the edge. No text, no letters, no labels, no
numbers.
```

---

## 2.3 `sm1_u4_hw6_science.webp` — ЛИСТ 3+2

**Где используется:** юнит 4 · ДЗ 6 блок 4 (`match` «соедини картинку с названием»).
**Что на ней:** пять понятий CLIL-урока: soil, plant, fruit, vegetables, tree.
Сейчас все пять — 240×240, в разном стиле и на цветных подложках.

```
Flat vector icon illustration for a children's science worksheet, bold clean dark
outlines, bright flat colours, simple friendly shapes, all five icons in one
consistent style, drawn as a sheet of five separate pictures: three in the top row
and two in the bottom row. Row 1, left to right: a low mound of dark brown soil
with a few small stones in it; a small green seedling with two leaves growing out
of a brown pot of soil; a group of fresh fruit together, a red apple, a yellow
banana and a bunch of green grapes. Row 2, left to right: a group of fresh
vegetables together, an orange carrot, a green pepper and a red tomato; a single
round green tree with a brown trunk and small red apples in its crown. Plain flat
pure white background, no shadow on the background, wide empty white gaps between
the five pictures, every picture complete and not touching any other picture or
the edge. No text, no letters, no labels, no numbers.
```

---

## 2.4 `sm1_u8_abilities.webp` — ЛИСТ 1×3

**Где используется:** юнит 8 · ДЗ 2 блоки 5, 7, 8 · ДЗ 5 блок 6.
**Что на ней:** три умения. Сейчас `ab_stand_one_leg` 205×246, `ab_skip` 220×249,
`ab_play_football` 190×257 — а стоят они в вариантах ответа и в плитках `match`,
где ребёнок в них всматривается. Остальные картинки этой серии (`ab_cant_swim`,
`ab_cant_ride_bike`) — нормального размера, стиль надо повторить.

```
Flat cartoon children's book illustration, bold clean dark outlines, bright flat
colours, friendly round-faced children about seven years old with big expressive
eyes, drawn as a sheet of three separate figures in one row. Left: a boy in a
purple T-shirt standing calmly and steadily on one leg, the other leg bent up,
arms out for balance, clearly succeeding. Middle: a boy in a green T-shirt and
blue trousers skipping happily with a skipping rope swinging over his head,
clearly succeeding. Right: a girl in a purple sports kit running and kicking a
black and white football with her foot, clearly succeeding. Every figure is full
body, facing the viewer, and happy. Plain flat pure white background, no shadow
on the background, wide empty white gaps between the three figures, every figure
complete and not touching any other figure or the edge. No text, no letters, no
labels, no numbers.
```

---

## 2.5 `sm1_u9_lets_sheet.webp` — ЛИСТ 2×3

**Где используется:** юнит 9 · ДЗ 2 блок 5 (`match`, шесть пар «Let's …»).
**Что на ней:** шесть сценок. Сейчас все шесть — 209–215 px, и это единственная
опора задания; у каждой в углу ещё и напечатана буква a–f, которой в блоке не
место.

🟥 **Ответ зависит от картинки.** Сценки нужны ровно эти и в этом порядке:
go swimming · listen to music · take a photo · paint a picture · fly a kite ·
look for shells.

```
Flat cartoon children's book illustration, bold clean dark outlines, bright flat
colours, friendly round-faced children about seven years old, drawn as a sheet of
six separate small scenes in a 3 by 2 grid. Row 1, left to right: a boy in
swimming goggles swimming in blue water with one arm raised; two girls sitting on
a bed listening to music from a radio, nodding along; a boy standing outdoors and
taking a photo with a camera held up to his eye. Row 2, left to right: a girl
standing at an easel and painting a picture with a brush and a palette; a boy
running across green grass flying a kite high on a string; a girl kneeling on
yellow sand and picking up seashells into a bucket. Each scene is small, simple
and instantly readable. Plain flat pure white background around the scenes, no
shadow on the background, wide empty white gaps between the six scenes, every
scene complete and not touching any other scene or the edge. No text, no letters,
no labels, no numbers.
```

---

# 3. НЕ ПЕРЕРИСОВЫВАТЬ

Это материал самих заданий: по ним сверяются ответы, к ним привязаны координаты
точек или они и есть разворот учебника. Если их заменить, задания перестанут
решаться.

**Кадры историй и комиксы.** `old/u2_hw4_frame_1…8`, `old/u2_hw4_story_7_8`,
`old/u2_hw4_story_grid`; `u5/story_lost_comic`, `story_lost_flash`,
`story_lost_forest`, `story_lost_rabbit`, `story_lost_whisper`;
`u6/story_old_house`, `story_old_house_shuffled`; `u7/story_cap_1_4`,
`story_cap_5_8`, `story_cap_cover`; `u8/story_robot_1_6`, `story_robot_7_8`,
`story_robot_shuffled`; `u9/hw4_frame_1…8`, `hw4_story_1`, `hw4_story_2`.

**Карточки правил и лексики.** `u2 old/u2_hw3_rule_a_an`,
`old/u2_hw3_rule_adjectives`; `u5/card_go_activities`, `card_lost_phrases`;
`u6/card_grammar_is_there`, `card_types_of_homes`, `grammar_there_is_are`,
`story_key_phrases`; `u7/grammar_is_he_wearing`, `grammar_this_these`,
`story_cap_phrases`; `u8/grammar_can_cant`, `grammar_can_you`,
`story_key_phrases`, `vocab_body`, `vocab_moves`.
На них напечатан текст — генератор его не нарисует, такие карточки собираем мы.

**Сканы разворотов и письма.** `u5/hw5_mila_letter`; `u8/sb_can_cant_kids`,
`pet_forum`; `u9/hw5_poster_usa`, `hw5_poster_sa`, `test_postcard`;
`ft/sp1_sheet`, `sp2_scene`, `sp3_sheet`, `ft_picnic`.

**Картинки с привязанными координатами (`hotspot`).** Менять нельзя вовсе —
точки ответа заданы в пикселях: `ft/ft_picnic`, `old/u2_hw4_story_grid`,
`u1/t_classroom_scenes`, `u2/t_kids_toys`, `u5/sport_places`, `u6/food_numbered`,
`u6/story_old_house_shuffled`, `u8/abilities_sheet`, `u8/sb_can_cant_kids`,
`u8/story_robot_shuffled`, `u9/hw5_beach_scene`, плюс `legacy/1a1ccc74ca98`,
`2b7d0d001037`, `53b4afc45124`, `666306cb2c0c`, `6e398e647694`, `9320fb6fceec`,
`94331ea92ed9`, `987012b3622d`, `9ae6b47a6e2e`, `c416cda60d0b`, `d0ce06140ea0`,
`ed52ad6ee4e2`, `f3c1b6278a2e`.

**Служебные картинки** (приветствие, похвала, прощание, 👍/👎, «good luck»).
Они по 140–200 px, это их штатный размер, на ответы они не влияют:
`legacy/872ffc8cf5ac`, `230077617f69`, `8edf1a3c1391`, `9fd80aa05f06`,
`19057ea62e4f`, `991bce28e595`, `05c609ab8d30`, `5ea8024245d6`, `7defd70f0df5`,
`887a768d628a`, `82a645a06c34`, `51b0cb648597`, `dc459b4a52db`,
`011d04aef137`, `0695f09affc1`.

---

# Рисовать не надо

## Взять из тренажёра слов — 3 картинки

В тренажёре (`words.image_url`) эти слова лежат в 512×512, фотореалистичным
рендером на белом — ровно тот стиль, что у остального комплекта `media/sm1/u4/`
(банан, торт, пицца, стейк). Файлы скачаем и положим в `media/sm1/u4/` сами,
ссылаться на тренажёр из уроков не будем.

| что | куда | ссылка |
|---|---|---|
| apple | юнит 4 · ДЗ 1 блоки 2, 5, 7 · ДЗ 2 блок 3 · ДЗ 6 блок 5 | `https://api.wowteach.ru/storage/v1/object/public/word-images/23/248-1781009768405.webp` |
| carrots | юнит 4 · ДЗ 1 блоки 2, 5 · ДЗ 2 блок 3 · ДЗ 6 блок 5 · ДЗ 7 блок 9 | `https://api.wowteach.ru/storage/v1/object/public/word-images/23/258-1781009817250.webp` |
| peas | юнит 4 · ДЗ 1 блоки 2, 5, 7 · ДЗ 2 блок 3 · ДЗ 6 блок 5 · тест блок 8 | `https://api.wowteach.ru/storage/v1/object/public/word-images/23/257-1781009819051.webp` |

Эти три сейчас стоят на `legacy` 220×220 (`32389194302e`, `5d6af0769340`,
`70d72135a807`) — четвёртое слово из той же четвёрки, **fish**, в тренажёре есть,
но там фото целой сырой рыбы, а не блюдо; на него сделан промпт 1.11.

## Заменить ссылку — 2 места

| где | было | станет |
|---|---|---|
| юнит 7 · ДЗ 5 блок 13 (`exact_input`, «Oscar is ___ football.») | `u7/football_ball.webp` (204×217) | `u5/act_play_football.webp`. **Сделано 21.10.2026** |
| юнит 2 · ДЗ 2 блок 12, все три вопроса (Flash, Thunder, Misty) | `legacy/4a5a6041d17a` · `9e83f1cc97bd` · `11e6279a79c2` — кадры из мультфильма курса, 300 px, фон улицы, головы крупным планом | `geroi/flash.webp` · `thunder.webp` · `misty.webp` — портреты с разворотов учебника, 420 px на белом. **Сделано 21.10.2026** |

---

# Итог

| | сколько |
|---|---|
| промптов — обязательные | **19** |
| промптов — замена мелких | **5** |
| **всего промптов** | **24** (из них 11 — листы по 2–6 картинок, итого 54 отдельных файла после нарезки) |
| строк «заменить ссылку» | **2** |
| «взять из тренажёра» | **3** |
| 🟥 мест, где ответ зависит от картинки | **6** (1.1, 1.8, 1.9, 1.14, 1.17, 2.5) |
| 🟥 вопросов к вам | **2** (пол Whisper — в промпте 1.1; Mabel в юните 7 — внизу) |

## Чего ждём из юнитов 0, 2 и 7

- **Юнит 0** — отчёт `fix/u0.md` готов, его находки по картинкам в списке
  (герои, котик, мальчик — промпт 1.1). Если после вычитки в нём появится
  что-то ещё, допишем сюда.
- **Юнит 2** — отчёт `fix/u2.md` готов, его находки в списке (мяч 1.2,
  ромб-kite 1.3, Lisa и Fiona 1.4, Flash — строка «заменить ссылку»).
  Юнит ещё правится: если найдётся новое, допишем.
- **Юнит 7** — **отчёта `fix/u7.md` ещё нет**, юнит в работе. В список вошло
  только то, что я проверила сама по размерам и по базе: `u7/football_ball`
  (заменить ссылку) и `u7/char_mabel_card` (293×280 — кадр из чужого
  мультфильма «Гравити Фолз», стоит в ДЗ 3 блоках 5 и 13 как «Mabel»).
  🟥 По Mabel нужно решение: это чужой персонаж, в курсе таких быть не должно —
  либо переименовываем героиню и рисуем свою девочку, либо убираем обе пары.
  Промпт сделаю, как только будет ответ. Остальные находки юнита 7 добавятся,
  когда выйдет его отчёт.
