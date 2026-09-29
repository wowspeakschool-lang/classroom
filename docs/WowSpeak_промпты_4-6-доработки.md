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
