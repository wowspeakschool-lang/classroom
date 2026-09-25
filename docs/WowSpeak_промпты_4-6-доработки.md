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

## 2. tracks — следы, ведущие к пещере (новая)

По сюжету Искорка говорит «следы ведут к пещере», а следов на картинке нет.

```
A row of small animal footprints on a grassy island path, horizontal
composition: five or six rounded paw prints pressed into soft earth, going from
the lower left corner towards the upper right, getting smaller with distance.
The path is bright green grass with a few little white daisies and small
pebbles. Nothing else in the picture — no cave, no animals, no characters. Cute
chunky 3D cartoon render for small children, smooth glossy surfaces, soft
rounded shapes, bright and friendly, warm daylight. Plain flat pure white
background, no shadow on the background, generous margin around the whole
shape. No text, no letters, no numbers.
```

**Проверить:** следы идут по диагонали и их видно издали; в кадре нет ни
пещеры, ни зверей — пещера у нас отдельной картинкой.

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
