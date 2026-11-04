# Go Getter 1 — перегенерация в стиле C. Юниты 0, 1 и 2

Решение Анны от 03.11.2026: Go Getter переводится в **полуреалистичный 3D**
(вариант C, лист проб — `docs/makety/stili_cloudflare/list_stili_3d.png`).
Перегенерация идёт **юнитами целиком**, чтобы внутри одной домашки не стояли
рядом картинка старого стиля и картинка нового.

Здесь — только промпты. Ничего не генерировалось: суточный лимит Cloudflare
на 04.11 исчерпан.

Имена файлов **не меняются**: новая картинка ложится на место старой, блоки в
базе править не нужно.

## Строка стиля

Она уже вклеена в каждый промпт ниже, отдельно копировать не надо:

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours
```

**Ловушка.** Чем реалистичнее стиль, тем чаще модель отбивает промпт с ребёнком
как «неприемлемый контент». Поэтому людей во всех промптах ниже описаны как
`an animated film character: a young schoolboy…` / `a young schoolgirl…`, а не
`a boy` / `a girl`. Если промпт всё-таки отбился — добавить в начало описания
человека ещё раз `an animated film character`.

## Сводка

| юнит | всего картинок | перегенерируем | оставляем | собираем скриптом |
|---|---|---|---|---|
| Юнит 0 | 46 | 25 | 20 | 1 |
| Юнит 1 | 54 | 38 | 16 | 0 |
| Юнит 2 | 60 | 40 | 12 | 8 |
| **итого** | **160** | **103** | **48** | **9** |

Промптов написано **113**: 103 на сами картинки плюс 10 на детали, из которых
скрипт собирает составные листы юнита 2.

## Как проверять готовое (требование Анны от 03.11.2026)

По каждой картинке, прежде чем ставить её в блок:

1. нарисовано именно то, что просили (не похожий предмет);
2. предмет один, без дублей и лишних объектов в кадре;
3. фон белый, без тени и подложки;
4. предмет не обрезан краем, поле по кругу есть;
5. нет текста, букв, цифр и подписей;
6. стиль совпадает с остальными картинками курса;
7. если от картинки зависит ответ — на ней ровно то, что в ключе;
8. размер после обрезки не меньше 300 px по большей стороне (карточка —
   600–800 px, сцена — 1200–1600, webp 88–90).

---

# Юнит 0 — Welcome

Всего 46 картинок, все используются в блоках.
**Перегенерируем 25, оставляем 20, одну собираем скриптом.**

## Что перегенерируем

| файл | где используется | что на ней должно быть |
|---|---|---|
| `obj_apple.webp` | Ю0 ДЗ3 бл.16 (quiz, ключ «an apple», отвлекающие «an egg», «a sandwich») | одно целое красное яблоко, не яйцо и не бутерброд |
| `obj_bag.webp` | Ю0 ДЗ3 бл.16 (quiz, ключ «a bag»); Ю0 тест бл.2 (диктант «bag») | школьный рюкзак, синий |
| `obj_bin.webp` | Ю0 ДЗ3 бл.2 (карточки), бл.3 (match), бл.5 (quiz, ключ «bin») | классное ведро для бумаги, синее, пустое |
| `obj_board.webp` | Ю0 ДЗ3 бл.2, 3, 5 (ключ «board») | школьная доска в деревянной раме, зелёная, чистая |
| `obj_book.webp` | Ю0 ДЗ3 бл.16 (ключ «a book»); Ю0 тест бл.2 (диктант «book») | одна закрытая книга в твёрдой обложке |
| `obj_chair.webp` | Ю0 ДЗ3 бл.2, 3, 5 (ключ «chair»); Ю0 тест бл.2 (диктант «chair») | школьный стул, деревянное сиденье и спинка |
| `obj_clock.webp` | Ю0 ДЗ3 бл.2, 3, 5, 17 (ключ «clock») | круглые настенные часы, стрелки чёрные, цифр на циферблате нет |
| `obj_coloured_pencil.webp` | Ю0 ДЗ3 бл.2, 3, 5 (ключ «coloured pencil», рядом «pen» и «sharpener») | один цветной карандаш, корпус окрашен в цвет грифеля |
| `obj_desk.webp` | Ю0 ДЗ3 бл.2, 3, 5, 17 (ключ «desk») | школьная парта на четырёх ножках, пустая |
| `obj_notebook.webp` | Ю0 ДЗ3 бл.2, 3, 5, 17 (ключ «notebook») | тетрадь на пружине, закрытая, обложка без надписей |
| `obj_pen.webp` | Ю0 ДЗ3 бл.2, 4, 5 (ключ «pen», рядом «pencil»); Ю0 тест бл.2 (диктант «pen») | шариковая ручка с колпачком — сразу видно, что не карандаш |
| `obj_pencil.webp` | Ю0 ДЗ3 бл.16 (ключ «a pencil», рядом «a pen», «a pencil case») | простой деревянный карандаш с заточенным грифелем и резинкой |
| `obj_pencil_case.webp` | Ю0 ДЗ3 бл.2, 4, 5 (ключ «pencil case») | закрытый пенал на молнии |
| `obj_rubber.webp` | Ю0 ДЗ3 бл.2, 4, 5, 17 (ключ «rubber») | школьная стирательная резинка |
| `obj_ruler.webp` | Ю0 ДЗ3 бл.2, 4, 5, 17 (ключ «ruler») | прямая линейка, деления есть, цифр нет |
| `obj_sandwich.webp` | Ю0 ДЗ3 бл.16 (ключ «a sandwich») | бутерброд из двух половинок |
| `obj_scissors.webp` | Ю0 ДЗ3 бл.2, 4, 5, 17 (ключ «scissors») | одни детские ножницы с цветными кольцами |
| `obj_sharpener.webp` | Ю0 ДЗ3 бл.2, 4, 5 (ключ «sharpener») | точилка для карандашей; сейчас 266×262 — самая мелкая в юните |
| `col_red_pen.webp` | Ю0 тест бл.10 (match «Anna → red pen») | ручка, **красная** |
| `col_blue_bag.webp` | Ю0 тест бл.10 (match «Tom → blue bag») | рюкзак, **синий** |
| `col_yellow_ruler.webp` | Ю0 тест бл.10 (match «Olivia → yellow ruler») | линейка, **жёлтая** |
| `col_green_notebook.webp` | Ю0 тест бл.10 (match «Daniel → green notebook») | тетрадь, **зелёная** |
| `col_pink_pencil_case.webp` | Ю0 тест бл.10 (match «Sophie → pink pencil case») | пенал, **розовый** |
| `colour_red.webp` | Ю0 тест бл.2 (диктант, ответ «red») | клякса красной краски, больше ничего |
| `test_classroom.webp` | Ю0 тест бл.12 (speaking, 6 вопросов по картинке) | класс: доска, парты, стулья, рюкзак, книги — см. 🟥 ниже |

🟥 **`test_classroom.webp` — проверить после генерации.** Три вопроса задания
сверяются по картинке: «What colour is the bag?», «What colour is the chair?»,
«Count the books on the desk». В промпте цвета и число книг названы прямо, но
число предметов генератору доверять нельзя: когда картинка придёт, пересчитать
книги и посмотреть цвета. Не сошлось — перегенерировать (бесплатно), а не
переписывать вопросы.

## Промпты юнита 0

### `u0/obj_apple.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single ripe red apple with a short brown stalk and one small green leaf, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no table, no plate, no surface. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u0/obj_bag.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single blue school backpack with two shoulder straps, a front zip pocket and a side mesh pocket, standing upright and seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no floor, no desk, no surface. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no logos, no watermark.
```

### `u0/obj_bin.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single blue plastic classroom waste bin, empty, open at the top, seen from a three quarter angle slightly above, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no floor, no wall, no rubbish. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u0/obj_board.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single classroom chalkboard with a dark green writing surface in a plain wooden frame, completely clean and empty, hanging straight and seen almost from the front, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no classroom wall, no chalk, no duster. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no drawings on the board, no watermark.
```

### `u0/obj_book.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single closed hardback book with a plain dark blue cover and visible cream page edges, lying at a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no desk, no stack of books, no surface. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no title on the cover, no watermark.
```

### `u0/obj_chair.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single school chair with a warm wooden seat and back rest and slim grey metal legs, standing upright and seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no floor, no classroom, no desk beside it. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u0/obj_clock.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single round wall clock with a red rim, a plain white face, black hour and minute hands and small black tick marks around the edge, seen straight from the front, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no wall, no shelf. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers on the clock face, no brand name, no watermark.
```

### `u0/obj_coloured_pencil.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single red coloured pencil, the whole barrel painted bright red, sharpened to a red point, lying at a diagonal, centred in the frame with generous empty margin on all sides. It must read clearly as a coloured pencil and not as a pen. Plain flat pure white background, no shadow on the background, no paper, no desk, no other pencils. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u0/obj_desk.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single school desk with a warm wooden top, a shallow open shelf underneath and four slim grey metal legs, empty, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no floor, no classroom, no chair, nothing on the desk. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u0/obj_notebook.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single closed spiral notebook with a plain green cover and a silver wire spiral along the top edge, lying at a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no desk, no pen beside it, no surface. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, nothing printed on the cover, no watermark.
```

### `u0/obj_pen.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single blue ballpoint pen with a glossy blue plastic barrel, a blue clip and a fine metal tip, lying at a diagonal, centred in the frame with generous empty margin on all sides. It must read clearly as a pen and not as a pencil: no wood, no sharpened point, no rubber on the end. Plain flat pure white background, no shadow on the background, no paper, no desk. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no brand name, no watermark.
```

### `u0/obj_pencil.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single yellow wooden pencil, sharpened to a grey graphite point, with a metal band and a pink rubber at the other end, lying at a diagonal, centred in the frame with generous empty margin on all sides. It must read clearly as a wooden pencil and not as a pen. Plain flat pure white background, no shadow on the background, no paper, no desk, no other pencils. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u0/obj_pencil_case.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single soft fabric pencil case, closed, with a zip running along the top and a small zip pull, lying flat and seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no desk, no pencils around it. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, nothing printed on the fabric, no watermark.
```

### `u0/obj_rubber.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single school eraser, a small rectangular block, one half soft red and one half pale cream, slightly worn at one corner, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no paper, no desk, no pencil beside it. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, nothing printed on the eraser, no watermark.
```

### `u0/obj_ruler.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single straight flat ruler with a warm yellow body and a row of small black measuring tick marks along one edge, lying at a slight diagonal, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no paper, no desk. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no printed numbers along the scale, no brand name, no watermark.
```

### `u0/obj_sandwich.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single sandwich cut into two triangular halves standing one behind the other, brown bread with cheese, lettuce and tomato visible at the cut, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no plate, no board, no table. Nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u0/obj_scissors.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single pair of children's school scissors, slightly open, with rounded steel blades and bright blue and yellow plastic finger rings, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no paper, no desk. One pair of scissors only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u0/obj_sharpener.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single small red plastic pencil sharpener with a shiny steel blade and one round hole, seen from a three quarter angle slightly above, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no desk, no pencil in the hole, no shavings. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u0/col_red_pen.webp` — ключ «red pen»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single ballpoint pen that is clearly and unmistakably RED: bright red barrel, red clip, red cap, with a fine metal tip, lying at a diagonal, centred in the frame with generous empty margin on all sides. No other colour anywhere on the pen. Plain flat pure white background, no shadow on the background, no paper, no desk. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no brand name, no watermark.
```

### `u0/col_blue_bag.webp` — ключ «blue bag»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single school backpack that is clearly and unmistakably BLUE all over, with two shoulder straps and a front zip pocket, standing upright and seen from a three quarter angle, centred in the frame with generous empty margin on all sides. No other colour anywhere on the bag. Plain flat pure white background, no shadow on the background, no floor, no desk. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no logos, no watermark.
```

### `u0/col_yellow_ruler.webp` — ключ «yellow ruler»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single straight flat ruler that is clearly and unmistakably YELLOW all over, with small black measuring tick marks along one edge, lying at a slight diagonal, centred in the frame with generous empty margin on all sides. No other colour anywhere on the ruler. Plain flat pure white background, no shadow on the background, no paper, no desk. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no printed numbers along the scale, no watermark.
```

### `u0/col_green_notebook.webp` — ключ «green notebook»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single closed spiral notebook whose cover is clearly and unmistakably GREEN all over, with a silver wire spiral along one edge, lying at a three quarter angle, centred in the frame with generous empty margin on all sides. No other colour on the cover. Plain flat pure white background, no shadow on the background, no desk, no pen beside it. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, nothing printed on the cover, no watermark.
```

### `u0/col_pink_pencil_case.webp` — ключ «pink pencil case»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single soft fabric pencil case that is clearly and unmistakably PINK all over, closed, with a zip running along the top, lying flat and seen from a three quarter angle, centred in the frame with generous empty margin on all sides. No other colour on the fabric. Plain flat pure white background, no shadow on the background, no desk, no pencils around it. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u0/colour_red.webp` — ответ диктанта «red»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single glossy splash of thick bright red paint with soft rounded edges and a few small drops, lying flat, centred in the frame with generous empty margin on all sides. Pure saturated red and nothing else: no orange, no pink, no second colour. Plain flat pure white background, no shadow on the background, no paper, no brush, no paint pot. Nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u0/test_classroom.webp` — сцена для speaking

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A horizontal view of an empty bright primary school classroom seen from the back of the room: a large clean dark green board on the far wall, a row of wooden school desks with orange chairs, one blue school backpack standing on the floor beside the nearest desk, exactly three books stacked flat on the nearest desk, a round wall clock on the side wall and a window with daylight. Nobody in the room. Wide horizontal composition, everything important inside the frame and nothing cropped by the edges. No text, no letters, no labels, no numbers, no writing on the board, no posters with words, no watermark.
```

## Не перегенерируем — юнит 0

| файл | причина |
|---|---|
| `card_a_an.webp`, `card_classroom_language.webp`, `card_colours.webp`, `card_greetings.webp`, `card_in_my_bag.webp`, `card_numbers.webp` | карточки лексики и грамматики 900×506 — набранный текст, а не рисунок; перерисовывать нечего |
| `look_a_an.webp`, `look_its_theyre.webp` | грамматические плашки LOOK! — тоже набранный текст |
| `colour_black/blue/brown/green/grey/orange/pink/purple/red/white/yellow.svg` (11) | цветовые квадраты, вектор — стиля не имеют, в любом размере чистые |
| `scene_zoo_colours.webp` | в кадре герой учебника Superdug — героев не генерируем; к тому же на картинке висит hotspot с восемью координатами (Ю0 ДЗ2 бл.12), перерисовка собьёт точки |

## Собрать скриптом — юнит 0

### `u0/diagram_classroom.webp` — пять предметов класса на одном листе

Используется в Ю0 ДЗ3 бл.6 (hotspot, пять подписей). Сейчас пять предметов
нарисованы в пяти разных манерах. Генератору лист не заказываем — собираем из
**уже перегенерированных** `obj_bin`, `obj_board`, `obj_chair`, `obj_clock`,
`obj_desk`.

Раскладка жёсткая: координаты точек hotspot записаны в блоке и менять блок мы
не будем, поэтому центры предметов должны попасть ровно сюда (проценты от
ширины и высоты листа):

| предмет | x | y |
|---|---|---|
| `obj_bin` | 25 % | 27 % |
| `obj_board` | 68 % | 25 % |
| `obj_chair` | 13 % | 72 % |
| `obj_clock` | 46 % | 76 % |
| `obj_desk` | 83 % | 70 % |

Лист 900×541, фон чисто белый, предметы не касаются друг друга и краёв,
масштаб подобрать так, чтобы доска и парта не подавляли ведро и часы.

---

# Юнит 1 — Family and friends

Всего 54 картинки, все используются в блоках.
**Перегенерируем 38, оставляем 16, скриптом ничего не собираем.**

## Что перегенерируем

| файл | где используется | что на ней должно быть |
|---|---|---|
| `fam_mother.webp` | Ю1 ДЗ1 бл.2 (карточки), бл.3 (match), бл.4 (quiz), бл.10 (exact_input); Ю1 тест бл.2 (диктант «mother») | женщина лет сорока, жёлтое платье в цветочек — она же в `fam_parents` и `fam_family` |
| `fam_father.webp` | там же, ключ «father» | мужчина лет сорока, розовая рубашка — он же в `fam_parents` и `fam_family` |
| `fam_parents.webp` | Ю1 ДЗ1 бл.2, 3, 4, 10; тест бл.2 (ключ «parents») | **те же двое вместе** — видно, что это пара взрослых |
| `fam_grandmother.webp` | Ю1 ДЗ1 бл.2, 3, 4, 10; тест бл.2 | пожилая женщина, седые волосы, красная кофта |
| `fam_grandfather.webp` | Ю1 ДЗ1 бл.2, 3, 4, 10; тест бл.2 | пожилой мужчина, очки, коричневый кардиган |
| `fam_grandparents.webp` | Ю1 ДЗ1 бл.2, 3, 4, 10 (ключ «grandparents») | **те же двое вместе** |
| `fam_son.webp` | Ю1 ДЗ1 бл.2, 3, 4, 10 (ключ «son») | мальчик лет девяти, сине-белая футболка |
| `fam_daughter.webp` | Ю1 ДЗ1 бл.2, 3, 4, 10 (ключ «daughter») | девочка лет одиннадцати, сиреневая толстовка |
| `fam_cousin.webp` | Ю1 ДЗ1 бл.2, 3, 4 (ключ «cousin») | мальчик в очках, зелёная футболка в полоску — отличается от `fam_son` |
| `fam_aunt.webp` | Ю1 ДЗ1 бл.2, 3, 4 (ключ «aunt») | женщина лет тридцати пяти, кудрявые каштановые волосы, синяя блузка |
| `fam_uncle.webp` | Ю1 ДЗ1 бл.2, 3, 4 (ключ «uncle») | мужчина с бородой, зелёный свитер |
| `fam_family.webp` | Ю1 ДЗ1 бл.1 (текст), бл.2, 3, 4 (ключ «family») | все шестеро вместе: бабушка, дедушка, мама, папа, сын, дочь |
| `he_garden.webp` | Ю1 ДЗ7 бл.8 (exact_input, ответ «garden»: «He is in the g…») | **мужчина** в саду — ребёнок пишет «garden», значит сад должен читаться сразу |
| `she_poland.webp` | Ю1 ДЗ7 бл.8 (ответ «Poland») | девушка с **польским** флагом (белый верх, красный низ) |
| `she_american.webp` | Ю1 ДЗ7 бл.8 (ответ «American») | девушка с **американским** флагом |
| `they_school.webp` | Ю1 ДЗ7 бл.8 (ответ «school») | несколько детей за партами в классе |
| `place_garden.webp` | Ю1 ДЗ5 бл.7 (ответ «garden») | сад с клумбами и яблоней, людей нет |
| `place_home.webp` | Ю1 ДЗ7 бл.8 (ответ «home») | жилой дом снаружи, дорожка, палисадник |
| `place_school.webp` | Ю1 ДЗ5 бл.7 (ответ «school») | школьное здание, школьный автобус |
| `place_park.webp` | Ю1 ДЗ5 бл.7 (ответ «park»); тест бл.12 (order «Tommy isn't in the park.») | парк: дорожка, скамейка, деревья |
| `place_party.webp` | Ю1 ДЗ2 бл.4 (quiz); ДЗ5 бл.7 (ответ «party») | стол с тортом, шарами и подарками |
| `place_paris.webp` | Ю1 ДЗ7 бл.8 (ответ «France»: «Paris is in F…») | **Эйфелева башня** — узнаётся с первого взгляда |
| `place_london.webp` | Ю1 тест бл.11 (order «Mary's family is from London.») | **Биг-Бен и лондонское колесо обозрения** |
| `rob_victor_console.webp` | Ю1 ДЗ6 бл.2 (аудирование, «Rob and Victor are best friends» — верно) | два мальчика на диване с геймпадами |
| `rob_mel_holiday.webp` | Ю1 ДЗ6 бл.2 («Rob's on holiday» — верно, «Rob and Mel are in the UK» — неверно) | мальчик и девочка на **южном пляже**, с чемоданом; погода явно не британская |
| `t1_dog_best_friend.webp` | Ю1 тест бл.3 (quiz «Your dog is very big!») | **очень большая собака** рядом с ребёнком |
| `t1_friend_home.webp` | Ю1 тест бл.4 («My friends are at home today») | девочка дома в кресле с ноутбуком |
| `t1_birthday.webp` | Ю1 тест бл.5 («Happy Birthday, Anna! Here's your present») | день рождения: одна девочка дарит другой подарок |
| `t1_robin_library.webp` | Ю1 тест бл.6 («Robin isn't in the garden. He's in the library») | мальчик читает **в библиотеке**, сада в кадре нет |
| `t1_french_friends.webp` | Ю1 тест бл.7 («My friends aren't from Poland. They are from France») | двое друзей с **французским** флагом на фоне Эйфелевой башни |
| `t1_classmates_park.webp` | Ю1 тест бл.8 (order «My classmates aren't at school.») | пятеро одноклассников на траве **в парке**, не в школе |
| `t1_neighbours_beach.webp` | Ю1 тест бл.9 (order «My neighbours are on holiday.») | двое взрослых в шезлонгах на пляже |
| `t1_super_dad.webp` | Ю1 тест бл.10 (order «My dad is the best.») | папа в плаще супергероя и сын рядом |
| `t1_emma_park.webp` | Ю1 тест бл.15–16 (аудирование: «They are at the park» — верно, брат Макс) | девочка и мальчик **в парке** |
| `teens_skatepark.webp` | Ю1 ДЗ4 бл.7 (gaps) | трое подростков разговаривают в скейтпарке |
| `tf_boy_backpack.webp` | Ю1 ДЗ3 бл.3 (quiz: «He's a teacher» — неверно, «He isn't ready for school» — верно) | мальчик в своей комнате, вещи разбросаны, в школу он явно не собран |
| `tf_boys_bench.webp` | Ю1 ДЗ3 бл.3 («They aren't happy» — верно, «They're at home» — неверно) | два грустных мальчика на скамейке **на улице** |
| `tf_girl_ten.webp` | Ю1 ДЗ3 бл.3 («She isn't eleven» — верно, «She's at school» — неверно) | девочка на своём дне рождения, **на кофте цифра 10** — см. 🟥 ниже |

🟥 **`tf_girl_ten.webp` — цифру наносим сами.** Ключ держится на том, что
девочке десять, а не одиннадцать. Цифры генератору не доверяем: промпт просит
пустую кофту, «10» наносим скриптом поверх готовой картинки.

🟥 **Флаги — тоже накладкой.** В `she_poland`, `she_american` и
`t1_french_friends` генератор путает полосы и звёзды. Промпт просит фигуру с
**пустым однотонным флажком** в руке, а правильный флаг кладём скриптом из
готовых `u1/flag_poland.svg`, `u1/flag_usa.svg`, `u1/flag_france.svg`.

## Промпты юнита 1

### `u1/fam_mother.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film character: a friendly woman of about forty with shoulder length brown hair, smiling warmly at the viewer, wearing a soft yellow summer dress with a small flower pattern. Head and shoulders portrait, facing the viewer, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no coloured circle or badge behind her. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/fam_father.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film character: a friendly man of about forty with short dark brown hair and a kind smile, wearing a plain pink shirt with the sleeves rolled up. Head and shoulders portrait, facing the viewer, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no coloured circle or badge behind him. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/fam_parents.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: a married couple of about forty standing close together and smiling at the viewer — the woman has shoulder length brown hair and a soft yellow summer dress with a small flower pattern, the man has short dark brown hair and a plain pink shirt. Both shown from the knees up, side by side, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no furniture. Two characters only, nobody else in the frame, nobody cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/fam_grandmother.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film character: a kind grandmother of about seventy with short wavy white hair and small round glasses, smiling gently at the viewer, wearing a soft red knitted cardigan over a cream blouse. Head and shoulders portrait, facing the viewer, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no coloured circle or badge behind her. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/fam_grandfather.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film character: a kind grandfather of about seventy with short grey hair and dark rimmed glasses, smiling gently at the viewer, wearing a brown knitted cardigan over a pale blue shirt. Head and shoulders portrait, facing the viewer, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no coloured circle or badge behind him. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/fam_grandparents.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: an elderly couple of about seventy standing close together and smiling at the viewer — the woman has short wavy white hair, round glasses and a soft red knitted cardigan, the man has short grey hair, dark rimmed glasses and a brown knitted cardigan. Both shown from the knees up, side by side, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no furniture. Two characters only, nobody else in the frame, nobody cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/fam_son.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film character: a cheerful young schoolboy of about nine with tousled brown hair, grinning at the viewer, wearing a white t-shirt with blue sleeves. Head and shoulders portrait, facing the viewer, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no coloured circle or badge behind him. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/fam_daughter.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film character: a cheerful young schoolgirl of about eleven with long brown hair tied back, smiling at the viewer, wearing a soft lilac hoodie. Head and shoulders portrait, facing the viewer, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no coloured circle or badge behind her. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/fam_cousin.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film character: a friendly young schoolboy of about ten with wavy dark hair and round glasses, smiling at the viewer, wearing a green and white striped t-shirt. He must look clearly different from a boy in a white and blue t-shirt. Head and shoulders portrait, facing the viewer, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no coloured circle or badge behind him. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/fam_aunt.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film character: a friendly woman of about thirty five with curly shoulder length chestnut hair, smiling at the viewer, wearing a plain blue blouse. Head and shoulders portrait, facing the viewer, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no coloured circle or badge behind her. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/fam_uncle.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film character: a friendly man of about forty with dark hair and a short dark beard, smiling at the viewer, wearing a plain dark green knitted jumper. Head and shoulders portrait, facing the viewer, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no coloured circle or badge behind him. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/fam_family.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: a family of six standing together in one group and smiling at the viewer — a grandmother with white hair in a red cardigan, a grandfather with grey hair and glasses in a brown cardigan, a mother of about forty in a yellow flowered dress, a father of about forty in a pink shirt, a young schoolboy of about nine in a white and blue t-shirt and a young schoolgirl of about eleven in a lilac hoodie. All six shown from the knees up, nobody hidden behind anyone else. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no furniture. Exactly six characters, nobody else in the frame, nobody cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/he_garden.webp` — ответ «garden»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: a man of about thirty sitting on the grass in a sunny back garden with a laptop on his knees, smiling. Around him the garden reads at a glance: a green lawn, flower beds in bloom, a small apple tree and a wooden fence behind him. Horizontal composition, the man centred, everything important inside the frame and nobody cropped by the edges. No text, no letters, no labels, no numbers, no signs, no watermark.
```

### `u1/she_poland.webp` — ответ «Poland» (флаг накладываем скриптом)

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: a cheerful young woman of about twenty with long light brown hair, standing and smiling at the viewer, holding up a small plain blank flag on a short wooden stick in her raised right hand. The flag cloth is completely plain and empty, one flat neutral light grey, with no pattern and no colours on it. Behind her, softly out of focus, the old town square of a European city with pastel townhouses and a church tower. Shown from the knees up, centred in the frame, nobody cropped by the edges. No text, no letters, no labels, no numbers, no signs, no watermark.
```

### `u1/she_american.webp` — ответ «American» (флаг накладываем скриптом)

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: a cheerful young woman of about twenty with long wavy brown hair, wearing a red t-shirt and jeans, standing and smiling at the viewer, holding up a small plain blank flag on a short wooden stick in her raised right hand. The flag cloth is completely plain and empty, one flat neutral light grey, with no stars, no stripes and no pattern. Behind her, softly out of focus, a big city skyline of tall glass towers across the water. Shown from the knees up, centred in the frame, nobody cropped by the edges. No text, no letters, no labels, no numbers, no signs, no watermark.
```

### `u1/they_school.webp` — ответ «school»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: four animated film characters, young schoolchildren of about ten, sitting at wooden school desks in a bright classroom, two of them with a hand raised and all of them smiling. Open exercise books on the desks, a clean green board and a window with daylight behind them. It must read at a glance as a school lesson. Horizontal composition, everything important inside the frame and nobody cropped by the edges. No text, no letters, no labels, no numbers, no writing on the board, no posters with words, no watermark.
```

### `u1/place_garden.webp` — ответ «garden»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A horizontal view of a sunny back garden: a neat green lawn, raised flower beds full of blooming flowers, a small apple tree with red apples, a wooden watering can standing on the grass and a low wooden fence at the back. Nobody in the garden. It must read at a glance as a garden and not as a park. Horizontal composition, everything important inside the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no signs, no watermark.
```

### `u1/place_home.webp` — ответ «home»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A horizontal view of a small friendly family house seen from the street on a sunny day: cream walls, a red tiled roof, a chimney, a dark red front door with two steps, windows with white frames, a short paved path through a tidy front garden and a low white picket fence. Nobody in the picture. It must read at a glance as somebody's home. Horizontal composition, the whole house inside the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no house number, no signs, no watermark.
```

### `u1/place_school.webp` — ответ «school»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A horizontal view of a school building from the street on a sunny morning: a two storey brick school with a clock above the main entrance and tall windows, a yellow school bus standing in front of it and a paved yard with a few trees. Nobody in the picture. It must read at a glance as a school. Horizontal composition, everything important inside the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no signs over the door, no words on the bus, no watermark.
```

### `u1/place_park.webp` — ответ «park»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A horizontal view of a city park on a sunny day: a winding paved path, a green wooden bench under a big leafy tree, flower beds along the path, a small pond with a low stone bridge further back. Nobody in the park. It must read at a glance as a public park and not as a private garden. Horizontal composition, everything important inside the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no signs, no watermark.
```

### `u1/place_party.webp` — ответ «party»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A horizontal view of a birthday party table: a round table with a spotted paper tablecloth, a tall white birthday cake with lit candles in the middle, a few wrapped presents with ribbons beside it, paper cups, and a bunch of bright balloons and a string of bunting above. Nobody at the table. It must read at a glance as a birthday party. Horizontal composition, everything important inside the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no writing on the cake, no words on the bunting, no watermark.
```

### `u1/place_paris.webp` — ответ «France»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A horizontal view of Paris with the Eiffel Tower standing tall and complete in the middle of the frame, seen across the gardens and fountains in front of it on a clear bright day, with Paris rooftops low on both sides. The Eiffel Tower must be unmistakable and must not be cut off at the top. Horizontal composition, everything important inside the frame. No text, no letters, no labels, no numbers, no signs, no watermark.
```

### `u1/place_london.webp` — предложение «Mary's family is from London.»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A horizontal view of London across the river on a bright day: the Big Ben clock tower and the Houses of Parliament on the left, a tall white observation wheel on the right, a red double decker bus crossing the bridge in front of them. It must be unmistakably London, with the clock tower complete and not cut off at the top. Horizontal composition, everything important inside the frame. No text, no letters, no labels, no numbers, no signs, no advertising on the bus, no watermark.
```

### `u1/rob_victor_console.webp` — «Rob and Victor are best friends»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: two animated film characters, young schoolboys of about eleven, sitting side by side on a grey sofa in a cosy living room, each holding a games controller and laughing, clearly enjoying the game together. One boy has dark hair and a blue top, the other has fair hair and a green top. A lamp and a cushion behind them. Horizontal composition, both boys inside the frame and nobody cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/rob_mel_holiday.webp` — «Rob's on holiday», «не в Великобритании»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: two animated film characters, a young schoolboy and a young schoolgirl of about eleven, standing together on a hot tropical beach in sun hats and summer clothes, a blue suitcase beside them, smiling at the viewer. Behind them palm trees, white sand and a turquoise sea under a bright sky — clearly a holiday somewhere hot and clearly not a grey northern country. Horizontal composition, both children inside the frame and nobody cropped by the edges. No text, no letters, no labels, no numbers, no signs, no watermark.
```

### `u1/t1_dog_best_friend.webp` — «Your dog is very big!»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: an animated film character, a young schoolboy of about ten, standing on the grass with his arm around a very large friendly dog that is nearly as tall as he is, both looking happily at the viewer. The size of the dog must be obvious at first glance. A simple sunny lawn behind them. Horizontal composition, boy and dog complete inside the frame, nobody cropped by the edges. One boy and one dog only. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/t1_friend_home.webp` — «My friends are at home today»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: an animated film character, a young schoolgirl of about eleven, curled up in a soft mustard armchair at home with a laptop on her knees, a blanket over her legs, smiling. A cosy living room behind her: a bookshelf, a house plant, a mug on a side table, warm daylight from a window. It must read at a glance as being at home. Horizontal composition, everything important inside the frame, nobody cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/t1_birthday.webp` — «Here's your present»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: two animated film characters, young schoolgirls of about ten in party hats, one handing a wrapped present with a ribbon to the other, both delighted. Behind them a birthday table with a cake with candles, balloons and bunting. Horizontal composition, both girls inside the frame and nobody cropped by the edges. No text, no letters, no labels, no numbers, no writing on the cake, no words on the bunting, no watermark.
```

### `u1/t1_robin_library.webp` — «isn't in the garden, he's in the library»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: an animated film character, a young schoolboy of about eleven, sitting cross legged on the floor of a library reading an open book, tall shelves full of books rising on both sides behind him and warm daylight from a high window. It must read at a glance as a library and there must be no garden, no grass and no plants in the picture. Horizontal composition, the boy inside the frame and nobody cropped by the edges. No text, no letters, no labels, no numbers, no titles on the book spines, no watermark.
```

### `u1/t1_french_friends.webp` — «from France, not from Poland» (флаг накладываем скриптом)

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: two animated film characters, a young schoolboy and a young schoolgirl of about eleven in striped tops and berets, standing together on a bridge and waving happily, one of them holding up a small plain blank flag on a short wooden stick. The flag cloth is completely plain and empty, one flat neutral light grey, with no stripes and no pattern. Behind them the Eiffel Tower against a bright sky. Horizontal composition, both children inside the frame and nobody cropped by the edges. No text, no letters, no labels, no numbers, no signs, no watermark.
```

### `u1/t1_classmates_park.webp` — «My classmates aren't at school.»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: five animated film characters, schoolchildren of about eleven, sitting together on the grass in a sunny park, talking and laughing. Trees, a path and flower beds behind them. It must read at a glance as a park, and there must be no school building, no desks, no classroom and no school bus anywhere in the picture. Horizontal composition, all five children inside the frame and nobody cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/t1_neighbours_beach.webp` — «My neighbours are on holiday.»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: two adults in sun hats relaxing side by side in striped deckchairs on a sunny beach, seen from behind, looking out at a turquoise sea with palm trees at the edge of the sand. It must read at a glance as a holiday. Horizontal composition, both deckchairs complete inside the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no signs, no watermark.
```

### `u1/t1_super_dad.webp` — «My dad is the best.»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: a cheerful father of about forty standing in a heroic pose with a red superhero cape over his ordinary shirt and jeans, and beside him an animated film character, his young son of about eight, in a matching small red cape, both laughing. Nothing else around them. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no city, no sky. Two characters only, nobody cropped by the edges. No text, no letters, no labels, no numbers, no emblem on the cape, no watermark.
```

### `u1/t1_emma_park.webp` — аудирование, «They are at the park»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: two animated film characters, a young schoolgirl of about eleven and her younger brother of about nine, sitting together on the grass in a sunny park, smiling at the viewer. Behind them park trees, a path and a flower bed. It must read at a glance as a park. Horizontal composition, both children inside the frame and nobody cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/teens_skatepark.webp` — gaps «в скейтпарке»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: three teenagers of about fourteen standing together and talking in a skatepark on a sunny day — a fair haired girl, a boy in a yellow hoodie, and a dark haired girl holding a skateboard under her arm. Concrete ramps and a basketball hoop behind them, green bushes at the sides. Horizontal composition, all three inside the frame and nobody cropped by the edges. No text, no letters, no labels, no numbers, no graffiti, no signs, no watermark.
```

### `u1/tf_boy_backpack.webp` — «He isn't ready for school»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: an animated film character, a young schoolboy of about ten, sitting on the floor of his bedroom leaning against the bed and reading a small book, with his school backpack lying open on the floor beside him and school books scattered around it — he is clearly not packed and not ready to leave. A bright tidy bedroom with a window and a curtain behind him. He is a schoolboy, not a teacher: no suit, no board, no classroom. Horizontal composition, the boy inside the frame and nobody cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/tf_boys_bench.webp` — «They aren't happy», «не дома»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: two animated film characters, young schoolboys of about ten, sitting side by side on a park bench, both clearly sad and bored, elbows on their knees and chins in their hands, a football lying on the ground in front of them. They are outdoors in a park: grass, a tree and a bin behind the bench, daylight. There must be no room, no sofa, no furniture and nothing indoors in the picture. Horizontal composition, both boys inside the frame and nobody cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u1/tf_girl_ten.webp` — «She isn't eleven», «не в школе» (цифру наносим скриптом)

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: an animated film character, a young schoolgirl of about ten, at her own birthday party, throwing her arms up in delight and laughing, wearing a party hat and a plain long sleeved green top with nothing printed on it. Pink and blue balloons, bunting and confetti around her, a birthday cake on a table behind her. It must read at a glance as a party at home and not as a school. Centred in the frame with generous empty margin on all sides, not cropped by the edges. No text, no letters, no labels, no numbers, nothing written on her top, no numbers on the balloons or the cake, no watermark.
```

## Не перегенерируем — юнит 1

| файл | причина |
|---|---|
| `card_countries.webp`, `card_family.webp`, `card_introductions.webp`, `card_to_be.webp`, `card_to_be_negative.webp` | карточки лексики и грамматики — набранный текст, а не рисунок |
| `flag_china.svg`, `flag_france.svg`, `flag_italy.svg`, `flag_poland.svg`, `flag_spain.svg`, `flag_uk.svg`, `flag_usa.svg` | флаги, вектор — стиля не имеют; к тому же флаг — ключ задания (Ю1 ДЗ3 бл.12–13), генератору его не доверяем |
| `comic_jill_1.webp`, `comic_jill_2.webp` | комикс из учебника с героями и с номерами кадров 1–4 прямо в картинке; на номерах держится hotspot (Ю1 ДЗ4 бл.4–5) |
| `scene_sally_family.webp` | материал hotspot (Ю1 ДЗ1 бл.6): шесть подписей привязаны к координатам людей на картинке, перерисовка собьёт все точки |
| `tree_mark.webp` | семейное дерево с именами — материал для gaps (Ю1 ДЗ1 бл.8) и hotspot (Ю1 ДЗ7 бл.3); имена и семь координат держат весь ключ |

## Собрать скриптом — юнит 1

Составных листов в юните нет. Две доработки поверх готовых картинок:

* **`tf_girl_ten.webp`** — нанести цифру **10** на кофту девочки (ключ: «She
  isn't eleven»);
* **`she_poland.webp`, `she_american.webp`, `t1_french_friends.webp`** —
  наложить флаг на пустое полотнище из `u1/flag_poland.svg`, `u1/flag_usa.svg`,
  `u1/flag_france.svg` соответственно.

---

# Юнит 2 — Clothes and things

Всего 60 картинок, все используются в блоках.
**Перегенерируем 40, оставляем 12, восемь собираем скриптом** (для них нужны
ещё 10 отдельных деталей — промпты в конце раздела).

## Что перегенерируем

| файл | где используется | что на ней должно быть |
|---|---|---|
| `clothes_tshirt.webp` | Ю2 ДЗ1 бл.2 (карточки), бл.4–5 (match), бл.7 (quiz, ключ «T-shirt»), бл.12 (ключ «It's»); Ю2 тест бл.2 (диктант «T-shirt») | футболка с короткими рукавами, голубая — видно, что не майка |
| `clothes_top.webp` | Ю2 ДЗ1 бл.2, 6, 9; тест бл.5 (ключ «top», отвлекающие «coat», «cap») | майка **без рукавов**, голубая — видно, что не футболка |
| `clothes_shirt.webp` | Ю2 ДЗ1 бл.2, 6, 9; тест бл.6 (ключ «shirt», отвлекающие «skirt», «shoes») | рубашка с воротником и пуговицами, светло-голубая |
| `clothes_jumper.webp` | Ю2 ДЗ1 бл.2, 6, 9; ДЗ7 бл.8; тест бл.3 (ключ «jumper», отвлекающие «jacket», «jeans») | вязаный свитер без капюшона и молнии, жёлтый |
| `clothes_hoodie.webp` | Ю2 ДЗ1 бл.2, 4–5, 7, 11 (ключ «hoodie», отвлекающие «jacket», «jumper») | толстовка **с капюшоном** и карманом-кенгуру, синяя |
| `clothes_jacket.webp` | Ю2 ДЗ1 бл.2, 6, 9; ДЗ7 бл.8 (ответ «jacket») | лёгкая куртка-бомбер на молнии, зелёная — короче пальто |
| `clothes_coat.webp` | Ю2 ДЗ1 бл.2, 4–5, 7, 12; тест бл.2 (диктант «coat») | длинное тёплое пальто на пуговицах, коричневое |
| `clothes_dress.webp` | Ю2 ДЗ1 бл.2, 4–5, 7, 11 (ключ «dress», отвлекающие «top», «skirt»); тест бл.2 (диктант) | платье целиком, жёлтое |
| `clothes_skirt.webp` | Ю2 ДЗ1 бл.2, 4–5, 7, 12; ДЗ7 бл.8; тест бл.2 (диктант «skirt») | юбка, тёмно-синяя в складку — не платье |
| `clothes_jeans.webp` | Ю2 ДЗ1 бл.2, 4–5, 7, 12; тест бл.2 (диктант «jeans») | джинсы, синий деним — видно, что не брюки |
| `clothes_trousers.webp` | Ю2 ДЗ1 бл.2, 4–5, 7, 12; ДЗ7 бл.8; тест бл.7 (ключ «trousers») | классические брюки, серые — не джинсы |
| `clothes_shorts.webp` | Ю2 ДЗ1 бл.2, 6, 9, 11 (ключ «shorts», отвлекающие «trousers», «jeans») | шорты до колена, бежевые |
| `clothes_tracksuit.webp` | Ю2 ДЗ1 бл.2, 6, 9; ДЗ7 бл.8 (ответ «tracksuit») | спортивный костюм: куртка и штаны одного цвета рядом |
| `clothes_shoes.webp` | Ю2 ДЗ1 бл.2, 4–5, 7; тест бл.4 (ключ «shoes», отвлекающие «shirt», «skirt») | **пара** чёрных школьных туфель — не кроссовки и не ботинки |
| `clothes_trainers.webp` | Ю2 ДЗ1 бл.2, 6, 9, 12 (ключ «trainers», отвлекающие «shoes») | **пара** спортивных кроссовок со шнурками и рифлёной подошвой |
| `clothes_boots.webp` | Ю2 ДЗ1 бл.2, 4–5, 7, 11 (ключ «boots», отвлекающие «trainers», «shoes») | **пара** высоких ботинок на толстой подошве |
| `clothes_cap.webp` | Ю2 ДЗ1 бл.2, 4–5, 7 (ключ «cap») | бейсболка с козырьком, тёмно-синяя |
| `clothes_scarf.webp` | Ю2 ДЗ1 бл.2, 6, 9, 11 (ключ «scarf», отвлекающие «coat», «cap»); ДЗ7 бл.8 | вязаный шарф, серый |
| `clothes_gloves.webp` | Ю2 ДЗ1 бл.2, 6, 9, 11 (ключ «gloves», отвлекающие «shoes», «trainers») | **пара** вязаных перчаток, тёмно-красные |
| `adj_too_big.webp` | Ю2 ДЗ2 бл.2 (карточки); ДЗ7 бл.3 (match, подпись «too big») | вещь, которая **явно велика** — по картинке должно читаться «слишком большая» |
| `gadget_backpack.webp` | Ю2 ДЗ5 бл.2 (match), бл.3 (quiz, ключ «backpack»), бл.5 (exact_input) | обычный школьный рюкзак, синий — не красный суперрюкзак с котом |
| `gadget_games_console.webp` | Ю2 ДЗ5 бл.2, 3, 5 (ключ «games console») | игровая приставка с геймпадом |
| `gadget_laptop.webp` | Ю2 ДЗ5 бл.2, 3, 5 (ключ «laptop computer») | раскрытый ноутбук |
| `gadget_mobile_phone.webp` | Ю2 ДЗ5 бл.2, 3, 5 (ключ «mobile phone») | смартфон стоймя, экран пустой |
| `gadget_mountain_bike.webp` | Ю2 ДЗ5 бл.2, 3, 5 (ключ «mountain bike») | горный велосипед сбоку |
| `gadget_skateboard.webp` | Ю2 ДЗ5 бл.2, 3, 5 (ключ «skateboard») | скейтборд |
| `far_hoodie.webp` | Ю2 тест бл.3 (quiz, ключ «That» — вещь **далеко**) | ребёнок показывает на толстовку, висящую **в дальнем конце комнаты**; одна вещь |
| `far_cap.webp` | Ю2 тест бл.6 (ключ «That» — далеко) | ребёнок показывает на кепку **далеко** на полке; одна вещь |
| `far_boots.webp` | Ю2 тест бл.7 (ключ «those» — далеко, **много**) | ребёнок показывает на **пару** ботинок у двери в дальнем конце комнаты |
| `near_trainers.webp` | Ю2 тест бл.4 (ключ «these» — рядом, **много**) | ребёнок стоит вплотную к **паре** кроссовок и показывает вниз |
| `near_tracksuit.webp` | Ю2 тест бл.5 (ключ «This» — рядом, одна вещь) | ребёнок держит руку на спортивном костюме, лежащем рядом на стуле |
| `boot_black.webp` | Ю2 тест бл.10 (order «These boots are too small.») | **пара** чёрных ботинок — сейчас в кадре один, а предложение про «these boots» |
| `best_friends_girls.webp` | Ю2 тест бл.12 (order «Is Anna your best friend?») | две подруги обнимаются |
| `brothers_highfive.webp` | Ю2 тест бл.9 (order «Are you David Smith's brother?») | два брата дают друг другу «пять» |
| `cinema.webp` | Ю2 тест бл.11 (order «What is your favourite film?») | вход в кинотеатр, вывеска **пустая** |
| `pencils_heart.webp` | Ю2 тест бл.8 (order «What is your favourite colour?») | цветные карандаши веером, все цвета радуги |
| `emma_new_girl.webp` | Ю2 ДЗ4 бл.8 (текст статьи про Эмму) | девочка лет десяти с теннисной ракеткой и книгой |
| `nancy_show.webp` | Ю2 ДЗ4 бл.6 (gaps, диалог ведущего и Нэнси) | телестудия: ведущий с микрофоном и девочка лет одиннадцати |
| `jamie_super_backpack.webp` | Ю2 ДЗ5 бл.6 (текст про суперрюкзак) | подросток лет тринадцати с **красным** рюкзаком за спиной |
| `super_backpack.webp` | Ю2 ДЗ5 бл.6 (текст: «It's a red backpack», карман для питомца) | **красный** рюкзак, из переднего кармана выглядывает котёнок |

## Промпты юнита 2

### `u2/clothes_tshirt.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single light blue cotton t-shirt with short sleeves and a round neck, laid out flat and seen from the front, centred in the frame with generous empty margin on all sides. It must clearly have short sleeves so that it reads as a t-shirt and not as a sleeveless top. Plain flat pure white background, no shadow on the background, no hanger, no person, no table. One garment only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no print on the fabric, no watermark.
```

### `u2/clothes_top.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single light blue sleeveless top with wide shoulder straps and no sleeves at all, laid out flat and seen from the front, centred in the frame with generous empty margin on all sides. It must clearly have no sleeves so that it reads as a sleeveless top and not as a t-shirt. Plain flat pure white background, no shadow on the background, no hanger, no person, no table. One garment only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no print on the fabric, no watermark.
```

### `u2/clothes_shirt.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single light blue button up shirt with a pointed collar, a row of buttons down the front, long sleeves and a breast pocket, laid out flat and seen from the front, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no hanger, no person, no table. One garment only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no print on the fabric, no watermark.
```

### `u2/clothes_jumper.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single warm yellow knitted jumper with a cable pattern, long sleeves and a round ribbed neck, laid out flat and seen from the front, centred in the frame with generous empty margin on all sides. It must have no hood, no zip and no front pocket, so that it reads as a knitted jumper and not as a hoodie or a jacket. Plain flat pure white background, no shadow on the background, no hanger, no person, no table. One garment only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no print on the fabric, no watermark.
```

### `u2/clothes_hoodie.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single blue cotton hoodie with a clearly visible hood, drawstrings and a large kangaroo pocket across the front, laid out flat and seen from the front, centred in the frame with generous empty margin on all sides. The hood must be obvious at first glance. Plain flat pure white background, no shadow on the background, no hanger, no person, no table. One garment only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no print on the fabric, no watermark.
```

### `u2/clothes_jacket.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single dark green light bomber jacket with a front zip, ribbed collar, ribbed cuffs and a ribbed hem, hip length, laid out flat and seen from the front, centred in the frame with generous empty margin on all sides. It must be clearly short and light so that it reads as a jacket and not as a long winter coat. Plain flat pure white background, no shadow on the background, no hanger, no person, no table. One garment only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no print on the fabric, no watermark.
```

### `u2/clothes_coat.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single long warm brown winter coat reaching below the knee, with a row of large buttons down the front, a soft collar and two side pockets, laid out flat and seen from the front, centred in the frame with generous empty margin on all sides. It must be clearly long and warm so that it reads as a winter coat and not as a short jacket. Plain flat pure white background, no shadow on the background, no hanger, no person, no table. One garment only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u2/clothes_dress.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single yellow summer dress, one whole garment from the shoulders down to the hem with a gathered skirt, laid out flat and seen from the front, centred in the frame with generous empty margin on all sides. It must read as one single dress and not as a separate top and skirt. Plain flat pure white background, no shadow on the background, no hanger, no person, no table. One garment only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no print on the fabric, no watermark.
```

### `u2/clothes_skirt.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single navy blue pleated school skirt with a plain waistband, knee length, laid out flat and seen from the front, centred in the frame with generous empty margin on all sides. It must read as a skirt only, with no top and no shoulders attached to it. Plain flat pure white background, no shadow on the background, no hanger, no person, no table. One garment only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u2/clothes_jeans.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single pair of blue denim jeans with visible denim texture, contrast stitching, a metal button, a zip fly and five pockets, laid out flat and seen from the front, centred in the frame with generous empty margin on all sides. The denim must be obvious so that they read as jeans and not as plain trousers. Plain flat pure white background, no shadow on the background, no hanger, no person, no table. One garment only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no brand patch, no watermark.
```

### `u2/clothes_trousers.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single pair of smart grey school trousers in smooth plain fabric with a crease down each leg, full length, laid out flat and seen from the front, centred in the frame with generous empty margin on all sides. There must be no denim texture and no contrast stitching, so that they read as formal trousers and not as jeans. Plain flat pure white background, no shadow on the background, no hanger, no person, no table. One garment only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u2/clothes_shorts.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single pair of beige cotton shorts ending well above the knee, with a plain waistband and two side pockets, laid out flat and seen from the front, centred in the frame with generous empty margin on all sides. They must be clearly short so that they read as shorts and not as trousers. Plain flat pure white background, no shadow on the background, no hanger, no person, no table. One garment only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u2/clothes_tracksuit.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single navy blue tracksuit shown as a matching set: the zip up tracksuit top on the left and the matching tracksuit trousers on the right, both in the same navy fabric with a white stripe down the sleeve and the leg, laid out flat side by side with a clear white gap between them, seen from the front. Exactly two pieces, nothing else. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no hanger, no person, no table. Nothing cropped by the edges. No text, no letters, no labels, no numbers, no logos, no watermark.
```

### `u2/clothes_shoes.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single pair of plain black leather school shoes, flat soled and closed with a simple strap, standing side by side and seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Exactly two shoes, a matching left and right. They must look like formal school shoes: no laces, no sporty sole, no high ankle, so that they do not read as trainers or boots. Plain flat pure white background, no shadow on the background, no floor, no box. Nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no logos, no watermark.
```

### `u2/clothes_trainers.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single pair of sporty navy and grey trainers with white laces, a mesh upper and a thick white rubber running sole, standing side by side and seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Exactly two trainers, a matching left and right. They must look clearly sporty so that they do not read as formal school shoes or as boots. Plain flat pure white background, no shadow on the background, no floor, no box. Nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no logos, no watermark.
```

### `u2/clothes_boots.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single pair of brown leather ankle boots with laces and a thick chunky rubber sole, covering the ankle, standing side by side and seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Exactly two boots, a matching left and right. The high ankle and the heavy sole must be obvious so that they do not read as shoes or trainers. Plain flat pure white background, no shadow on the background, no floor, no box. Nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no logos, no watermark.
```

### `u2/clothes_cap.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single navy blue baseball cap with a curved peak and a small button on top, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain fabric with nothing printed or embroidered on it. Plain flat pure white background, no shadow on the background, no head, no shelf, no table. One cap only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no logos, no watermark.
```

### `u2/clothes_scarf.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single grey knitted winter scarf with visible ribbed knitting and short fringes at both ends, loosely coiled and laid flat, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no neck, no person, no table. One scarf only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no pattern with letters, no watermark.
```

### `u2/clothes_gloves.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single pair of dark red knitted winter gloves with five fingers each and ribbed cuffs, lying flat side by side, a left and a right, centred in the frame with generous empty margin on all sides. Exactly two gloves. Plain flat pure white background, no shadow on the background, no hands, no table. Nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u2/adj_too_big.webp` — подпись «too big»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film character: a young schoolboy of about nine wearing a padded winter coat that is enormously too big for him — the sleeves hang far past his hands, the shoulders droop down his arms and the hem reaches below his knees — looking at the viewer with a puzzled face and his arms held out. The coat being far too big must be obvious at first glance. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no furniture. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u2/gadget_backpack.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single blue school backpack with two shoulder straps, a front zip pocket and two side mesh pockets, standing upright and seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain blue fabric, nothing printed on it, nothing inside it and no animal in it. Plain flat pure white background, no shadow on the background, no floor, no desk. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no logos, no watermark.
```

### `u2/gadget_games_console.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single modern games console: a slim white console box standing behind, with one matching white and blue game controller resting in front of it. Exactly these two parts and nothing more. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no television, no cables, no table. Nothing cropped by the edges. No text, no letters, no labels, no numbers, no brand name, no watermark.
```

### `u2/gadget_laptop.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single open silver laptop computer seen from a three quarter angle, the screen showing a plain soft colour gradient and nothing else, the keyboard keys blank, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no desk, no mouse, no cables. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no icons on the screen, no brand name, no watermark.
```

### `u2/gadget_mobile_phone.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single modern smartphone standing upright on its short edge, seen almost from the front, with a dark slim body and a screen showing a plain soft colour gradient and nothing else, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no hand, no table, no case. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no icons on the screen, no brand name, no watermark.
```

### `u2/gadget_mountain_bike.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single mountain bike seen straight from the side, standing upright with both wheels on the ground, a dark green frame, thick knobbly tyres, straight handlebars and front suspension, centred in the frame with generous empty margin on all sides. The whole bike inside the frame, both wheels complete. Plain flat pure white background, no shadow on the background, no road, no grass, no rider. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no brand name on the frame, no watermark.
```

### `u2/gadget_skateboard.webp`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single skateboard seen from a three quarter angle slightly from below, a wooden deck with a plain dark grip tape top, visible trucks and four red wheels, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no ramp, no ground, no rider. One object only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no graphics on the deck, no watermark.
```

### `u2/far_hoodie.webp` — ключ «That» (далеко, одна вещь)

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still seen from behind: an animated film character, a young schoolgirl of about ten, standing in the near foreground of an empty room with her arm stretched out, pointing at one grey hoodie hanging on a hook on the far wall at the other end of the room. The hoodie is clearly far away from her and looks small in the distance; there is only one hoodie and nothing else on the walls. The long empty floor between the girl and the hoodie must make the distance obvious. Horizontal composition, everything inside the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no arrows, no watermark.
```

### `u2/far_cap.webp` — ключ «That» (далеко, одна вещь)

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still seen from behind: an animated film character, a young schoolboy of about ten, standing in the near foreground of an empty room with his arm stretched out, pointing at one blue baseball cap lying on a shelf on the far wall at the other end of the room. The cap is clearly far away from him and looks small in the distance; there is only one cap and nothing else on the shelf. The long empty floor between the boy and the shelf must make the distance obvious. Horizontal composition, everything inside the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no arrows, no watermark.
```

### `u2/far_boots.webp` — ключ «those» (далеко, пара)

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still seen from behind: an animated film character, a young schoolgirl of about ten, standing in the near foreground of an empty room with her arm stretched out, pointing at a pair of brown boots standing side by side on the floor by a door at the far end of the room. There are exactly two boots, clearly far away from her and small in the distance, and nothing else on the floor. The long empty floor between the girl and the boots must make the distance obvious. Horizontal composition, everything inside the frame, nothing cropped by the edges. No text, no letters, no labels, no numbers, no arrows, no watermark.
```

### `u2/near_trainers.webp` — ключ «these» (рядом, пара)

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: an animated film character, a young schoolgirl of about ten in a pink top and jeans, standing right beside a pair of white and blue trainers that are on the floor directly at her feet, bending slightly and pointing straight down at them, smiling at the viewer. There are exactly two trainers and they are clearly close to her, within arm's reach. Nothing in the distance, no far wall, no corridor. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background. Nothing cropped by the edges. No text, no letters, no labels, no numbers, no arrows, no watermark.
```

### `u2/near_tracksuit.webp` — ключ «This» (рядом, одна вещь)

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: an animated film character, a young schoolboy of about ten in a green jumper and jeans, standing right next to a wooden chair with one red tracksuit laid over its back, his hand resting on the tracksuit, smiling at the viewer. The tracksuit is clearly close to him, right under his hand. There is only one tracksuit, nothing in the distance, no far wall, no corridor. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background. Nothing cropped by the edges. No text, no letters, no labels, no numbers, no arrows, no watermark.
```

### `u2/boot_black.webp` — предложение «These boots are too small.»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single pair of black leather ankle boots with laces and a thick chunky sole, standing side by side, a left and a right, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Exactly two boots — the sentence of the task is about boots in the plural, so one boot alone is wrong. Plain flat pure white background, no shadow on the background, no floor, no box. Nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no logos, no watermark.
```

### `u2/best_friends_girls.webp` — «Is Anna your best friend?»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: two animated film characters, young schoolgirls of about eleven, hugging each other and laughing, clearly best friends — one with long dark wavy hair in a lilac top, the other with fair hair tied up in a green top, both in jeans and trainers. Shown from head to foot, standing. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no street. Two characters only, nobody cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u2/brothers_highfive.webp` — «Are you David Smith's brother?»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: two animated film characters, brothers of about nine and eleven with the same brown curly hair, giving each other a high five with raised hands and laughing — one in a yellow hoodie and blue jeans, the other in a red hoodie and beige trousers. Shown from head to foot, in mid movement. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no room, no street. Two characters only, nobody cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u2/cinema.webp` — «What is your favourite film?»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. The entrance of a small cinema seen from the street in the evening: double glass doors under a wide illuminated marquee board edged with round lamps, a red carpet and two rope posts leading to the doors, a striped popcorn cart beside the entrance. The marquee board and every panel on the building are completely blank and empty. Centred in the frame with generous empty margin on all sides. Nothing cropped by the edges. No text, no letters, no labels, no numbers, no film titles, no posters with words, no watermark.
```

### `u2/pencils_heart.webp` — «What is your favourite colour?»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A group of sharpened coloured pencils laid out in a neat fan, their points meeting at the bottom and spreading outwards, in the colours of the rainbow — red, orange, yellow, green, light blue, dark blue, purple and pink — each barrel painted in its own colour. Seen straight from above, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no paper, no desk, no pencil case. Nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u2/emma_new_girl.webp` — статья про новую ученицу

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film character: a young schoolgirl of about ten with long brown hair in a ponytail, smiling at the viewer, wearing a pink sports top and a pink tennis skirt, holding a tennis racket in one hand and a closed book under her other arm. Standing, shown from head to foot, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no court, no classroom. One character only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, nothing written on the book, no watermark.
```

### `u2/nancy_show.webp` — диалог ведущего и Нэнси на телешоу

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film still: a friendly television presenter in a smart jacket holding a microphone towards an animated film character, a young schoolgirl of about eleven standing beside him and smiling, both on a brightly lit television studio stage with coloured spotlights and a blank curved backdrop behind them. It must read at a glance as a television show. The backdrop and every panel on it are completely blank. Horizontal composition, both figures inside the frame and nobody cropped by the edges. No text, no letters, no labels, no numbers, no show name, no screens with words, no watermark.
```

### `u2/jamie_super_backpack.webp` — «Jamie Cooper's 13»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. An animated film character: a cheerful teenage boy of about thirteen with tousled dark hair, wearing a dark red hoodie and jeans, standing and smiling at the viewer with a bright red backpack on his back, the head of a small grey kitten peeking out of the backpack's side pocket. Shown from head to foot, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no street, no room. One boy and one kitten only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u2/super_backpack.webp` — «It's a red backpack», карман для питомца

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single bright red backpack standing upright on two small wheels, with a pull handle, two shoulder straps and a wide front pocket, seen from a three quarter angle, and the head of a small grey kitten peeking out of the front pocket. The backpack must be unmistakably red. Centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no floor, no room. One backpack and one kitten only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no logos, no watermark.
```

## Промпты деталей для составных листов (юнит 2)

Эти файлы в блоки не ставятся: из них скрипт собирает `dem_*` и `adj_*`.
Класть в `media/gg1/u2/_parts/`.

### `u2/_parts/corridor_empty.webp` — фон для четырёх листов `dem_*`

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A long empty school corridor seen straight down its length from one end, perfectly symmetrical: a polished pale wooden floor, plain cream walls with tall windows on both sides letting in soft daylight, and a plain wall closing the corridor far away at the other end. Completely empty: nobody in the corridor and nothing standing on the floor. The strong perspective of the floor and the windows must make the distance to the far wall obvious. Square composition, nothing cropped by the edges. No text, no letters, no labels, no numbers, no signs, no doors with signs, no watermark.
```

### `u2/_parts/tshirt_red.webp` — для листа «these»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single plain red cotton t-shirt with short sleeves and a round neck, laid out flat and seen from the front, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no hanger, no person, no table. One garment only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no print on the fabric, no watermark.
```

### `u2/_parts/tshirt_green.webp` — для листа «these»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single plain green cotton t-shirt with short sleeves and a round neck, laid out flat and seen from the front, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no hanger, no person, no table. One garment only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no print on the fabric, no watermark.
```

### `u2/_parts/tshirt_small_yellow.webp` — для листа «big and small»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single tiny yellow cotton t-shirt for a toddler, with short sleeves and a round neck, laid out flat and seen from the front, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no hanger, no person, no table. One garment only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no print on the fabric, no watermark.
```

### `u2/_parts/scarf_long_red.webp` — для листа «long and short»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single very long red knitted scarf with ribbed knitting and long fringes at both ends, hanging straight down its full length, clearly much longer than it is wide, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no neck, no person, no table. One scarf only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u2/_parts/scarf_short_green.webp` — для листа «long and short»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single very short green knitted scarf with ribbed knitting and short fringes at both ends, hanging straight down, clearly stubby and barely longer than it is wide, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no neck, no person, no table. One scarf only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no watermark.
```

### `u2/_parts/trainer_new_white.webp` — для листа «new and old»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single brand new white sports trainer, spotlessly clean, bright white laces neatly tied, crisp white rubber sole without a mark on it, seen from the side at a three quarter angle, centred in the frame with generous empty margin on all sides. It must look obviously new. Plain flat pure white background, no shadow on the background, no floor, no box. One trainer only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no logos, no watermark.
```

### `u2/_parts/trainer_old_worn.webp` — для листа «new and old»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single very old worn out sports trainer, the fabric grey and dirty, the laces frayed and loose, the toe scuffed and the rubber sole worn down and stained, seen from the side at a three quarter angle, centred in the frame with generous empty margin on all sides. It must look obviously old and worn. Plain flat pure white background, no shadow on the background, no floor, no mud on the background. One trainer only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no logos, no watermark.
```

### `u2/_parts/cap_cool_red.webp` — для листа «cool and boring»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single bright red baseball cap with a curved peak and a bold yellow lightning bolt shape stitched on the front, looking sporty and striking, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no head, no shelf. One cap only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no brand name, no watermark.
```

### `u2/_parts/cap_boring_grey.webp` — для листа «cool and boring»

```
semi-realistic 3D render, natural proportions, detailed fabric and hair, soft cinematic lighting, restrained natural colours. A single plain dull grey baseball cap with a curved peak, completely flat and featureless fabric with nothing on it at all, looking deliberately dull, seen from a three quarter angle, centred in the frame with generous empty margin on all sides. Plain flat pure white background, no shadow on the background, no head, no shelf. One cap only, nothing else in the frame, not cropped by the edges. No text, no letters, no labels, no numbers, no pattern, no watermark.
```

## Не перегенерируем — юнит 2

| файл | причина |
|---|---|
| `card_adjectives.webp`, `card_clothes.webp`, `card_personal_info.webp`, `card_questions_be.webp`, `card_short_answers.webp`, `card_this_that.webp`, `card_too.webp` | карточки лексики и грамматики — набранный текст, а не рисунок |
| `comic_kit_dug.webp` | герои учебника Kit и Dug; нужна крупнее — режем из разворота, который присылает методист |
| `icons_favourite_things.webp` | пересобрана скриптом 03.11.2026 из предметов курса (коммит `a16c691d`), перерисовывать нечего |
| `kids_outfits.webp` | материал gaps (Ю2 ДЗ1 бл.8): восемь ответов — названия и цвета одежды на двух детях; перерисовка меняет ключ |
| `kevin_birthday.webp` | материал speaking (Ю2 тест бл.16): по картинке ребёнок отвечает, где семья, сколько лет Сильвии, кто Эмма и Чарльз, откуда они; перерисовка меняет все шесть ответов |
| `boy_skater.webp` | материал hotspot (Ю2 ДЗ7 бл.2): шесть подписей привязаны к координатам кепки, телефона, рубашки, джинсов, кроссовок и скейта на фигуре; перерисовка собьёт все точки |

## Собрать скриптом — юнит 2

Везде одно и то же: на листе несколько предметов сразу, а модель раскладку не
держит. Генерируем детали по отдельности (промпты выше), лист собирает скрипт.

### `dem_this.webp`, `dem_that.webp`, `dem_these.webp`, `dem_those.webp`

Используются в Ю2 ДЗ2 бл.7 (match) и бл.10 (quiz). Ключ держится на двух
вещах: **далеко или близко** и **одна вещь или несколько**. Все четыре листа
собираются из одного фона `_parts/corridor_empty.webp` и футболок:
голубая — готовая `clothes_tshirt.webp`, красная и зелёная —
`_parts/tshirt_red.webp` и `_parts/tshirt_green.webp`.

| файл | что ставим на фон |
|---|---|
| `dem_this.webp` | **одна** голубая футболка, крупно, в переднем плане по центру — занимает примерно половину высоты кадра |
| `dem_that.webp` | **одна** голубая футболка, мелко, у дальней стены коридора — примерно 7 % высоты кадра |
| `dem_these.webp` | **три** футболки (синяя, красная, зелёная), крупно, в ряд в переднем плане — красная в середине чуть выше |
| `dem_those.webp` | **те же три** футболки, мелко, в ряд у дальней стены — примерно 7 % высоты кадра |

Лист 400×400, как сейчас. Важно, чтобы `this`/`these` и `that`/`those`
отличались только размером и местом, а футболки были одни и те же: задание
проверяет расстояние, а не цвет.

### `adj_big_small.webp`, `adj_long_short.webp`, `adj_new_old.webp`, `adj_cool_boring.webp`

Используются в Ю2 ДЗ2 бл.2 (карточки) и ДЗ7 бл.3 (match с подписями «big and
small», «long and short», «new and old», «cool and boring»). На каждом листе
два предмета рядом, и ключ читается только из их сравнения.

| файл | слева | справа | раскладка |
|---|---|---|---|
| `adj_big_small.webp` | большая голубая футболка — готовая `clothes_tshirt.webp` | `_parts/tshirt_small_yellow.webp` | оба предмета в один ряд, нижние края на одной линии, разница в высоте не меньше чем в два с половиной раза — «большая» и «маленькая» должны читаться сразу |
| `adj_long_short.webp` | `_parts/scarf_long_red.webp` | `_parts/scarf_short_green.webp` | оба шарфа висят вертикально, верхние края на одной линии, длинный не меньше чем втрое длиннее короткого |
| `adj_new_old.webp` | `_parts/trainer_new_white.webp` | `_parts/trainer_old_worn.webp` | обе кроссовки одного размера и под одним углом, рядом, нижние края на одной линии |
| `adj_cool_boring.webp` | `_parts/cap_cool_red.webp` | `_parts/cap_boring_grey.webp` | обе кепки одного размера и под одним углом, рядом |

Фон листа чисто белый, между предметами широкий белый просвет, ничего не
касается краёв и друг друга, подписей на листе нет — слова ребёнок берёт из
задания.
