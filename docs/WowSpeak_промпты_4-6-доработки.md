# Промпты 4–6: четыре картинки на замену и добавление

К каждому запросу прикладывайте готовую картинку набора — проще всего
светлячка (`assets/kids-4-6/firefly-neutral.webp`). Сохранять строго по
именам из заголовков, класть в `assets/kids-4-6/` (кроме одежды — она
лежит в `assets/lesson-1/`). Общее правило: фигура не упирается в край,
вокруг есть поле.

---

## 1. cave-open — пещера с гнездом и яйцом (замена)

Сейчас в пещере своё пустое гнездо, а яйцо вклеивается отдельной картинкой,
и получается два гнезда. Нужна одна картинка, где гнездо с яйцом уже внутри.

```
A cosy small cave opening in warm sandy rock, seen from the front, horizontal
composition. Inside the cave, on the ground, one round nest of dry straw with a
single large pastel egg lying in it — the egg is cream white with soft mint and
lilac speckles and a gentle glow. A big round pale stone has been rolled aside
to the right of the entrance. A few small stones and tufts of green grass at the
base. Warm golden light inside the cave, soft shadows. Exactly one nest and
exactly one egg in the whole picture. Cute chunky 3D cartoon render for small
children, smooth glossy surfaces, soft rounded shapes, bright and friendly.
Plain flat pure white background, no shadow on the background, generous margin
around the whole shape. No characters, no text, no letters, no numbers.
```

**Проверить:** гнездо ровно одно, яйцо ровно одно, яйцо видно целиком и оно
не в тени, камень откатан в сторону и не закрывает вход.

---

## 2. tracks — следы к пещере (переделать)

По сюжету это следы **дракончика**, того самого, что вылупится из яйца.
Первый вариант вышел кошачьей лапкой: круглая подушечка и четыре пальчика.
Нужны три пальца с коготками — и **сами следы поменьше**: дракончик ещё
маленький, след с детскую ладошку, а не с тазик.

```
A trail of small three-toed dragon footprints on a grassy island path,
horizontal composition: six little prints going from the lower left corner
towards the upper right, getting smaller with distance. Each print is a small
reptile track — three slender forward toes ending in tiny pointed claw marks,
and a narrow heel; the prints are small, about the size of a child's hand, not
massive. No round cat pad, no toe beans, no soft paw shape. The prints are
pressed into soft brown earth on bright green grass with a few little white
daisies and small pebbles. Nothing else in the picture — no cave, no dragon,
no characters. Cute chunky 3D cartoon render for small children, smooth glossy
surfaces, soft rounded shapes, bright and friendly, warm daylight. Plain flat
pure white background, no shadow on the background, generous margin around the
whole shape. No text, no letters, no numbers.
```

**Проверить:** у каждого следа **три** пальца с коготками, круглой
подушечки нет; следы мелкие рядом с ромашками, а не во весь кадр; в кадре
нет ни пещеры, ни дракона — пещера у нас отдельной картинкой.

Искорка на этом экране теперь говорит «Следы — и с коготками! Чьи же они?» —
так вопрос остаётся открытым до яйца.

---

## 3. jeans — джинсы (замена)

Нынешние джинсы взяты из набора 7–9, и под ними **запечена серая тень**. На
белой карточке её не видно, а у нас фон цветной — и тень читается грязной
полосой. Вырезать её нельзя: по цвету она совпадает со светлыми местами
самих джинсов. Нужна та же вещь, но без тени под ней.

```
A pair of child's denim jeans, front view, standing upright, horizontal folded
cuffs at the bottom. Plain denim with yellow-orange stitching along the seams,
a small round button at the waist, two front pockets. Cute chunky 3D cartoon
render for small children, smooth glossy surfaces, soft rounded shapes, bright
and friendly. Plain flat pure white background, absolutely no shadow and no
grey gradient under the object, generous margin around the whole shape. Single
object, centred. No text, no letters, no numbers.
```

Файл: `assets/lesson-1/jeans.webp` (перезаписать).

**Проверить:** под джинсами чисто белое, без серого пятна и без «пола».

---

## 4. shoes — ботинки (замена)

Та же беда: тень под подошвой по цвету не отличается от самой белой подошвы,
и порог, который убирает одну, начинает съедать другую.

```
A pair of child's slip-on sneakers standing side by side, three-quarter view.
Plain coloured upper with a thick white rounded sole and a small loop at the
heel. Cute chunky 3D cartoon render for small children, smooth glossy surfaces,
soft rounded shapes, bright and friendly. Plain flat pure white background,
absolutely no shadow and no grey gradient under the objects, generous margin
around the whole shape. No text, no letters, no numbers.
```

Файл: `assets/lesson-1/shoes.webp` (перезаписать).

**Проверить:** под подошвой чисто белое; сама подошва белая и хорошо видна
на фоне верха ботинка.

---

## Почему «no shadow» написано дважды

Генератор любит подрисовывать предмету опору — мягкое серое пятно снизу.
Пока предмет лежит на белой карточке, это красиво. У нас предмет летает над
цветным фоном, и тень превращается в грязный след. Скрипт вырезает фон по
двум правилам — «светлое и бесцветное» и «серое холодное», — но тень,
совпадающую по цвету с самой вещью, не отличит никакое правило.

---

## tracks-glade — полянка со следами и друзьями (Урок 3, экран 15, замена)

Сейчас на экране две отдельные картинки — следы и пещера под камнем. Нужна
одна сцена: реплика «Ой, смотри! Следы — и с коготками! Чьи же они? Ведут
прямо к пещере. А вход завален камнем. Одному не сдвинуть… Хорошо, что с
нами друзья!» — значит, на картинке и следы, и пещера, и зверята.

**Приложить к запросу пять картинок** (все из `assets/kids-4-6/`):
`animal-bunny.webp`, `animal-hedgehog.webp`, `animal-fox.webp` — зверята,
`tracks.webp` — следы, `cave-closed.webp` — пещера под камнем.

```
Use the attached pictures as exact references: the cream bunny, the brown
hedgehog and the orange fox must look exactly like the attached characters
(same faces, same colours, same proportions); the footprints must look
exactly like the attached three-toed clawed footprints; the cave must look
exactly like the attached sandy-rock cave with a big round grey stone
blocking the entrance.

A small sunny grassy meadow, seen from the front, wide horizontal
composition. On the right, the sandy-rock cave with the round grey stone
completely blocking its entrance. A trail of the same small three-toed
clawed footprints goes across the meadow from the lower left and leads
straight to the stone. On the left, the bunny, the hedgehog and the fox
stand together next to the trail, looking down at the footprints with
curious, surprised, happy faces; the fox points at the footprints with one
paw. The footprints are small — each about the size of the bunny's foot —
and clearly visible. A few tufts of grass, tiny white daisies and small
pebbles. The meadow is a soft rounded patch of grass under the whole scene,
not a floating island.

Cute chunky 3D cartoon render for small children, smooth glossy surfaces,
soft rounded shapes, bright and friendly, same style as the attached
pictures. Plain flat pure white background, no shadow on the background,
generous margin around the whole scene, nothing touches the edges of the
picture. No other characters, no dragon, no text, no letters, no numbers.
```

**Размер** 1536×1024 (горизонтальный). **Сохранить** как
`assets/kids-4-6/tracks-glade.webp` — или просто прислать в чат.

**Проверить:**
* зверята те же, что на экране 3-16, где толкают камень: зайчик кремовый с
  длинными ушами, ёжик коричневый, лисёнок оранжевый с белой грудкой;
* следы трёхпалые, с коготками, маленькие — это следы дракончика, а не
  кошачьи и не огромные;
* цепочка следов ведёт именно к камню, а камень закрывает вход целиком;
* дракончика на картинке нет — он ещё в яйце;
* по краям белое поле, сцена нигде не обрезана.

---

## mia — Волшебница Мия, новый гид вместо Искорки (три портрета)

Гид — девушка-волшебница, и голос у неё обычный взрослый женский. Она не
должна быть похожа на Хранительницу Слов из версии 7–9: та взрослая и
серьёзная, Мия — юная, лёгкая, солнечная. Сначала звалась Лучик, но
«лучик» — мужского рода, а гид — девушка; в образе от него остались
солнышко на заколке и звёздочки.

**Порядок.** Сначала `mia-neutral`, **только** с образцом стиля. Потом
`mia-smile` и `mia-excited` — каждый **одной правкой** готового
`mia-neutral` (приложить его), не цепочкой: на второй-третьей правке
плывут лицо и цвета.

**Образец стиля** — приложить светлячка `assets/kids-4-6/firefly-neutral.webp`.
**Размер** 1024×1024. **Сохранить** в `assets/kids-4-6/` под именами из
заголовков.

### mia-neutral — обычная (стоит рядом с репликами)

```
Use the attached picture of a firefly only as a style reference: the same
cute chunky 3D cartoon render, smooth glossy surfaces, soft rounded shapes,
big shiny eyes. Do not draw the firefly itself.

A young cheerful girl sorceress named Mia, about 16 years old, cute and
friendly, for small children. Upper body from the waist up, facing the
viewer, slightly turned. Warm golden hair in two soft buns with a small
glowing golden sun clip. Big warm brown eyes, rosy cheeks, gentle friendly
smile. A short cape and dress in bright clear colours: green, blue and
yellow — clean colours, not pastel. She holds a small magic wand with a
glowing little golden star on top. A few tiny golden sparkles around the
wand. Calm, kind, welcoming pose.

Plain flat pure white background, no shadow on the background, generous
margin around the whole figure, nothing touches the edges of the picture.
No other characters, no text, no letters, no numbers.
```

### mia-smile — радуется (на карте)

Приложить готовый `mia-neutral`.

```
Edit the attached picture. Keep the same girl exactly: same face, hair,
clothes, colours, wand and style. Change only the expression and pose: a
big happy open smile, eyes smiling, one hand waving hello, the wand in the
other hand. Keep the plain flat pure white background and the same margins.
```

### mia-excited — восторг (награды, сюжетные экраны)

Приложить готовый `mia-neutral`.

```
Edit the attached picture. Keep the same girl exactly: same face, hair,
clothes, colours, wand and style. Change only the expression and pose:
delighted and amazed, eyebrows up, mouth open in a happy "wow", the wand
raised up high with a burst of golden sparkles and tiny stars around it.
Keep the plain flat pure white background and the same margins.
```

**Проверить:**
* во всех трёх — одна и та же девушка: лицо, причёска, цвета одежды;
* в одежде явно видны наши три цвета — зелёный, синий, жёлтый;
* на палочке звёздочка, по краям белое поле, фигура не обрезана;
* не похожа на Хранительницу Слов из 7–9 и не выглядит взрослой тётей.

### mia-invite — с приглашением (первый экран Урока 1)

Реплика: «Привет! Я волшебница Мия. Смотри, что мне принесли — приглашение!
Нас зовут на праздник на Драконий Остров. Полетели!» Приложить готовый
`mia-neutral` — правка одной картинки, не цепочкой.

```
Edit the attached picture. Keep the same girl exactly: same face, hair,
clothes, colours, wand and style. Change only her pose and expression:
excited and happy, mouth open in a joyful smile. In her free hand she
proudly shows the viewer an open festive invitation card, held up next to
her face: a cream card with a golden edge and a golden star seal,
decorated with tiny colourful party flags and a small picture of a green
floating island with bunting and paper lanterns. The card has no words,
no letters and no numbers on it. The wand stays in her other hand with a
few golden sparkles. Keep the plain flat pure white background, no shadow
on the background, and generous margins; nothing touches the edges.
```

**Проверить:** та же девушка, что в `mia-neutral`; открытка повёрнута к
зрителю и хорошо видна; на ней нет букв (генератор любит вписывать
«Invitation» — такую не брать); палочка на месте; вокруг белое поле.

---

## friends-push — зверята толкают камень (Урок 3, экран 16, перерисовать)

Сейчас зверята и камень висят в воздухе: ни пещеры, ни земли. Нужна та же
сцена, но в мире соседних экранов: сзади пещера из песчаных камней, камень
закрывает её вход, под лапами трава. Следующий экран — та же пещера уже
открытая, изнутри.

**Приложить** (все из `assets/kids-4-6/`): `friends-push.webp` — эту сцену
переделываем, `cave-closed.webp` — пещера, `tracks-glade.webp` — трава и
земля в том же стиле.

```
Edit the first attached picture. Keep the bunny, the hedgehog and the fox
exactly as they are: same faces, colours, poses and the same pushing
action, all three leaning into the big round pale stone with effort and
happy faces, with the small yellow effort marks around them.

Add the world around them, taken from the other attached pictures: behind
the stone, the sandy-rock cave from the second picture, so that the big
round stone is right in front of the cave entrance and still covers it
completely. Under the characters and the stone, a soft rounded patch of
bright green meadow with a sandy path, like in the third picture. Tufts of
grass, a few tiny white daisies and small pebbles on both sides of the
scene, at the left and at the right. Wide horizontal composition, the
whole scene fully visible.

Same cute chunky 3D cartoon render, smooth glossy surfaces, soft rounded
shapes, bright and friendly. Plain flat pure white background, no shadow
on the background, generous margin around the whole scene, nothing
touches the edges of the picture. No other characters, no text, no
letters, no numbers.
```

**Размер** 1536×1024 (горизонтальный). **Сохранить** как
`assets/kids-4-6/friends-push.webp` — или просто прислать в чат.

**Проверить:**
* зверята те же и толкают тот же камень, позы не поменялись;
* камень стоит прямо перед входом в пещеру и закрывает его целиком;
* пещера та же, что на экране 3-15 (песчаные камни), трава с обеих сторон;
* вокруг белое поле, сцена нигде не обрезана — у прошлой полянки трава
  справа упёрлась в край.

---

## Ладошки: счёт с большого пальца (hand-1 … hand-4)

Анна: на каждой фразе пальцы загибаются **с большого и по порядку**.
Сейчас `hand-1…4` считают с указательного, а большой палец прижат — на
фразе из четырёх слов («I have blue jeans») стрелка начинала с
указательного, на фразе из пяти — с большого. Нужны четыре новые
ладошки; `hand-5` (раскрытая) остаётся как есть и служит образцом.

**Прикреплять `hand-5.webp`** к каждому запросу: это та же рука, мы
меняем только загнутые пальцы. Делать каждую **одной правкой от hand-5**,
а не цепочкой (hand-4 → hand-3 → …): на второй-третьей правке плывут
форма и цвет кожи.

Что важно для стрелки (кончики пальцев ищутся по картинке
автоматически):

* большой палец — слева от зрителя (как на hand-5), смотрит **вверх и
  чуть в сторону**, не горизонтально: стрелка указывает на кончик сверху;
* между поднятыми пальцами видны просветы;
* загнутые пальцы прижаты к ладони плотно, ни один не торчит выше
  костяшек — иначе его примут за поднятый.

### hand-4 — большой, указательный, средний, безымянный

```
The same cartoon child's hand as in the attached image, in the same position, same size, same skin tone, same lighting and same plain white background. Change only this: four fingers are up and spread wide with visible gaps between them — the thumb, the index finger, the middle finger and the ring finger. The thumb is on the left side of the image and points up and slightly outward, not sideways. The little finger is folded tightly down against the palm and does not stick up. The whole hand is visible with clear empty margin around it. No text. Plain flat pure white background, no shadow on the background.
```

### hand-3 — большой, указательный, средний

```
The same cartoon child's hand as in the attached image, in the same position, same size, same skin tone, same lighting and same plain white background. Change only this: three fingers are up and spread wide with visible gaps between them — the thumb, the index finger and the middle finger. The thumb is on the left side of the image and points up and slightly outward, not sideways. The ring finger and the little finger are folded tightly down against the palm and do not stick up. The whole hand is visible with clear empty margin around it. No text. Plain flat pure white background, no shadow on the background.
```

### hand-2 — большой и указательный

```
The same cartoon child's hand as in the attached image, in the same position, same size, same skin tone, same lighting and same plain white background. Change only this: two fingers are up with a wide gap between them — the thumb and the index finger. The thumb is on the left side of the image and points up and slightly outward, not sideways. The middle, ring and little fingers are folded tightly down against the palm and do not stick up. The whole hand is visible with clear empty margin around it. No text. Plain flat pure white background, no shadow on the background.
```

### hand-1 — только большой

```
The same cartoon child's hand as in the attached image, in the same position, same size, same skin tone, same lighting and same plain white background. Change only this: only the thumb is up, pointing straight up like a thumbs-up, on the left side of the hand. All four other fingers are folded tightly down against the palm and do not stick up. The palm still faces the viewer. The whole hand is visible with clear empty margin around it. No text. Plain flat pure white background, no shadow on the background.
```

Готовые картинки — в `assets/kids-4-6/` под теми же именами
(`hand-1.webp` … `hand-4.webp`), квадрат, как сейчас (1254×1254).
