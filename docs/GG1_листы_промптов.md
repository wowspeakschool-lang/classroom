# Go Getter 1 — ЛИСТЫ ПРОМПТОВ НА КАРТИНКИ

Собирается из `tools/gg1_sheets.py` — **правится там**, не здесь: тот же
список ячеек режет `tools/gg1_cut.py`, и промпт с нарезкой не расходятся.

Один промпт = один лист с сеткой. Генерирует Анна, присылает в чат с
подписью номера листа (Л0.1, Л2.3, ЛФ.1…), лист режется на карточки webp в
`media/gg1/uN/`. Номер листа не переиспользуется: выброшенный лист оставляет
пустой номер.

Каждый промпт самодостаточный — сетка, стиль, запрет людей и текста, размер
внутри, копируется целиком. Ячейки нумеруются слева направо, сверху вниз.

## Правила (те же, что у SM3 — см. `docs/SM3_листы_промптов.md`)

1. **Люди — только на листах с персонажами** (регистры «персонажи» и «сцены с
   персонажами»): стилизованные 3D-мультяшные, не фото. Решение Анны 05.10.2026 —
   для GG1 «генерируем что нужно, делаем красиво»; правило SM3 «без людей» здесь
   снято. На остальных листах людей нет, и это прописано в промпте.
2. **Не больше 3 колонок** — иначе ячейка мельче 512 px и мылит при нарезке.
3. **Никаких узнаваемых товаров** — `generic design, not resembling any real product`.
4. **Один стилевой регистр на лист**: предметы — реалистичный 3D, животные и
   символы действий — мультяшный глянец, комнаты и места — полу-мультяшные сцены,
   люди — 3D-мультяшные персонажи.

## Чего не генерируем

| Что | Откуда |
|---|---|
| Кляксы цветов (Unit 0) | скрипт `tools/gg1_colours.py`, svg |
| Флаги стран (Unit 1) | скрипт, svg — генератор путает полосы и звёзды |
| Циферблаты (Unit 6) | скрипт, svg — генератор путает стрелки |
| Обучающие карточки методиста, картинки учебника | вырезаются из PDF выгрузки (`tools/gg1_pdf_frames.py`) |
| Фото без людей из выгрузки (Лондон, Париж, библиотека, парк) | из PDF выгрузки |
| Приветствия, похвалы, прощания | `media/shared/`; Микки, Минни, Шрек, Чип и Дейл, Мистер Бин из выгрузки не берём |
| Мультяшные иллюстрации учебника с людьми (Kit & Dug, Oliver и Sarah, девочка с метками частей тела…) | из PDF выгрузки — на них уже стоят ответы и координаты |
| Вещь, которая уже нарисована в другом юните | берётся по старому ключу (ручка из Л0.1, кроссовки из Л2.2, животные Unit 7 в финальном тесте…) |

## Что изменилось после первой версии (05.10.2026)

Людей теперь рисуем, поэтому переделаны листы, которые обходили людей предметами:
**Л1.2, Л2.3, Л2.6, Л4.1, ЛФ.1** — промпты новые. Добавлены листы с людьми:
**Л1.3–Л1.6, Л3.5, Л4.3–Л4.6, Л5.6, Л6.4, ЛФ.3**. Остальные листы не менялись.


**Всего листов: 48, картинок: 305.**


---

# UNIT 0 · GET STARTED! — листов: 3

### Л0.1 · В рюкзаке — 9 карт. (3×3), реалистичный 3D
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a closed hardcover school book; 2) one coloured pencil, bright red, lying diagonally; 3) a spiral notebook with a plain cover; 4) a ballpoint pen with its cap; 5) a yellow graphite pencil with a pink eraser tip; 6) a zipped fabric pencil case; 7) a small plastic pencil sharpener; 8) a rectangular rubber eraser; 9) a plastic ruler with plain tick marks.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л0.2 · Класс и школьные вещи — 9 карт. (3×3), реалистичный 3D
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a pair of children's scissors with rounded tips; 2) a sandwich cut in half showing cheese and lettuce; 3) a school backpack with two straps; 4) a plastic waste bin; 5) a green classroom chalkboard in a wooden frame, completely blank; 6) a wooden school chair; 7) a round wall clock with plain tick marks and no numbers; 8) a wooden school desk; 9) a shiny red apple with a leaf.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л0.3 · Цветные вещи — 6 карт. (3×2), реалистичный 3D
Для теста Unit 0: «My pen is red», «My bag is blue»… Одна вещь — один цвет.
```
A sheet of 6 separate picture cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a bright red ballpoint pen; 2) a bright blue school backpack; 3) a bright yellow plastic ruler with plain tick marks; 4) a bright green spiral notebook; 5) a bright pink zipped pencil case; 6) a bright orange school backpack.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```


---

# UNIT 1 — листов: 6

### Л1.1 · Места — 6 карт. (3×2), сцены, полу-мультяшный 3D
Где ты? — at a party, at school, in the garden, in the park, at home, in the library.
```
A sheet of 6 separate illustrations in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a party table with a birthday cake with candles, colourful balloons, wrapped presents and a garland, nobody there; 2) a school building from outside with a big clock on the front and a yellow school bus parked in front; 3) a garden with flower beds, a watering can, an apple tree and a wooden fence; 4) a park with a path, a bench, green trees and a street lamp; 5) a cosy family house from outside with a red roof, a front door and a little front garden; 6) a library room with tall bookshelves full of books and an open book on a reading table.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л1.2 · Кто где — Homework 6 и 7 — 6 карт. (3×2), сцены с персонажами
Вместо фото людей. Ответы заданий держатся на деталях — их не менять.
```
A sheet of 6 separate illustrations in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) two ten-year-old boys, best friends, laughing and playing a video game on a sofa; 2) a ten-year-old boy and his twelve-year-old cousin, a girl, on holiday on a sunny beach with palm trees, a suitcase beside them; 3) a smiling young woman holding a small white-and-red Polish flag; 4) a man sitting on the grass in a garden with a laptop, flower beds and an apple tree behind; 5) a smiling young woman waving a small American flag; 6) a group of happy schoolchildren sitting at desks in a bright classroom.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л1.3 · Тест Unit 1 — 9 карт. (3×3), сцены с персонажами
Картинки к «выбери слово» и «составь предложение» теста.
```
A sheet of 9 separate illustrations in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a man asleep in bed and a happy dog sleeping on the pillow next to him, an alarm clock on the bedside table; 2) a girl with a laptop sitting in a cosy armchair at home; 3) a birthday party: a girl called Anna receiving a wrapped present from a friend, balloons and a cake; 4) two friends in berets and striped tops waving a French flag; 5) a group of classmates having fun in a park, not at school; 6) two neighbours seen from behind relaxing on sun loungers on a beach; 7) a smiling dad wearing a red superhero cape, his child cheering beside him; 8) a girl of eleven and her younger brother in a park; 9) a boy called Robin reading a book in a library with tall bookshelves.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л1.4 · Семья — портреты — 9 карт. (3×3), персонажи, 3D-мультяшные, на белом
Все девять — одна семья: похожи друг на друга, одинаковый стиль, каждый по пояс.
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) the grandfather, an old man with grey hair and glasses; 2) the grandmother, an old woman with white hair in a red cardigan; 3) the father, a man of forty in a pink shirt; 4) the mother, a woman of forty in a yellow dress; 5) the uncle, a man with a beard in a green jumper; 6) the aunt, a woman with curly hair in a blue top; 7) the son, a boy of eight in a T-shirt; 8) the daughter, a girl of eleven with a ponytail; 9) the cousin, a boy of nine with glasses.
All nine are members of ONE family and clearly look related; every character is shown waist-up, facing the viewer, in the same style and scale.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л1.5 · Семья — вместе — 3 карт. (3×1), персонажи, 3D-мультяшные, на белом
Те же люди, что на Л1.4: родители, бабушка с дедушкой, вся семья.
```
A sheet of 3 separate picture cards in a clean 3x1 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) the mother and the father standing together, smiling; 2) the grandmother and the grandfather standing together, smiling; 3) the whole family together: grandparents, parents, a son and a daughter.
The same family as on the portrait sheet: the same faces, hair and clothes - grandfather with grey hair and glasses, grandmother with white hair in a red cardigan, father in a pink shirt, mother in a yellow dress, a girl of eleven with a ponytail, a boy of eight.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1024 px, each cell at least 650 px.
```

### Л1.6 · Семья Салли на пикнике — сцена, сцены с персонажами
Для задания «Где кто?»: люди стоят раздельно, чтобы на каждого можно было поставить метку.
```
One single scene filling the frame: a family picnic on the grass in a park, seven people clearly separated from each other: from left to right a grandfather, a grandmother in a red cardigan, a father in a pink shirt, a mother in a yellow dress, a girl of eleven called Sally in the middle, her little sister of five, and her brother of eight.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```


---

# UNIT 2 — листов: 6

### Л2.1 · Одежда 1 — 9 карт. (3×3), реалистичный 3D
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a long warm winter coat with buttons; 2) a pair of blue jeans; 3) a pair of black school shoes; 4) a pleated skirt; 5) a plain T-shirt; 6) a pair of smart dark trousers; 7) a pair of brown boots; 8) a baseball cap; 9) a summer dress.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л2.2 · Одежда 2 — 9 карт. (3×3), реалистичный 3D
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a hoodie with a hood and a front pocket; 2) a zipped jacket; 3) a button-up shirt with a collar; 4) a knitted jumper; 5) a tracksuit: a zipped top and matching trousers laid side by side; 6) a pair of warm gloves; 7) a long knitted scarf; 8) a pair of shorts; 9) a pair of trainers.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л2.3 · Люди Unit 2 — 6 карт. (3×2), персонажи, 3D-мультяшные, на белом
Цвета одежды важны — по ним задания.
```
A sheet of 6 separate picture cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a girl in a grey jacket, a pink jumper, blue jeans and brown boots next to a boy in a blue cap, a green hoodie, black trousers and white shoes; 2) a boy standing with a skateboard, wearing a cap, a shirt, jeans and trainers, holding a mobile phone; 3) a friendly girl of ten holding a tennis racket and a book; 4) two young brothers giving each other a high five; 5) two girls, best friends, hugging and smiling; 6) a boy of thirteen with a red backpack, a cat peeking out of its pocket.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л2.4 · Прилагательные и супер-рюкзак — 6 карт. (3×2), реалистичный 3D
Пары: big/small, long/short, new/old, cool/boring, too big.
```
A sheet of 6 separate picture cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a very big T-shirt and a very small T-shirt side by side; 2) a very long scarf and a very short scarf side by side; 3) a shiny new trainer and a worn old dirty trainer side by side; 4) a bright cool cap with a lightning bolt next to a plain grey boring cap; 5) a huge jacket hanging on a tiny coat hanger, much too big for it; 6) a red backpack with small wheels and a little pocket with a cat peeking out of it.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л2.5 · this / that / these / those — 4 карт. (2×2), сцены, полу-мультяшный 3D
Близко — крупно на переднем плане, далеко — маленькое в глубине комнаты. Ячейки: this, these, that, those.
```
A sheet of 4 separate illustrations in a clean 2x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) one T-shirt very close in the foreground, a long empty room behind; 2) three T-shirts very close in the foreground, a long empty room behind; 3) one small T-shirt far away at the end of a long empty room; 4) three small T-shirts far away at the end of a long empty room.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л2.6 · Гаджеты и топ — 6 карт. (3×2), реалистичный 3D
```
A sheet of 6 separate picture cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a games console with a controller; 2) a smartphone; 3) a mountain bike; 4) an open laptop; 5) a skateboard; 6) a sleeveless top.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```


---

# UNIT 3 — листов: 5

### Л3.1 · Комнаты — 6 карт. (3×2), сцены, полу-мультяшный 3D
```
A sheet of 6 separate illustrations in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a bathroom with a bath, a washbasin, a mirror and a towel; 2) a bedroom with a bed and pillow and a bedside table with a lamp; 3) a kitchen with a cooker, a fridge, a table and a pot; 4) a garage with its door open and a car inside; 5) a garden in front of a house with grass, flowers and a tree; 6) a living room with a sofa, a TV, a rug and a floor lamp.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л3.2 · Части дома и угощение — 6 карт. (3×2), реалистичный 3D
floor, door, wall, window + бутерброд и чай для фраз гостя (Homework 4).
```
A sheet of 6 separate picture cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a square piece of wooden parquet floor seen at an angle; 2) a wooden front door with a handle; 3) a piece of painted brick wall; 4) a window with a white frame and curtains; 5) a sandwich on a plate; 6) a cup of tea and biscuits on a small tray.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л3.3 · Мебель 1 — 9 карт. (3×3), реалистичный 3D
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a soft armchair; 2) a bath on little legs; 3) a bed with a duvet and a pillow; 4) a dining table; 5) a fridge; 6) a sofa; 7) a wardrobe with two doors; 8) a patterned carpet seen at an angle; 9) a decorative cushion.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л3.4 · Мебель 2 и фразы гостя — 9 карт. (3×3), реалистичный 3D
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a floor lamp; 2) a plant in a pot; 3) a poster with a picture of a rocket pinned to a wall; 4) a TV on a low stand; 5) a bookcase full of books; 6) a shower cabin with a glass door; 7) an open front door with a doormat in front of it; 8) a wooden staircase going up; 9) a pair of trainers on a doormat by a door.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л3.5 · Гости у двери — сцена, сцены с персонажами
Вместо фото людей в Homework 7.
```
One single scene filling the frame: a boy opening the front door of a house to welcome two smiling guests, a hallway with stairs going up behind him.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```


---

# UNIT 4 — листов: 6

### Л4.1 · Характер — 6 карт. (3×2), персонажи, 3D-мультяшные, на белом
clever, friendly, funny, helpful, nice, sporty — дети, по которым это видно.
```
A sheet of 6 separate picture cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a girl with glasses reading a big book, a lightbulb idea above her; 2) a smiling boy waving hello; 3) a boy making a funny face and laughing; 4) a girl carrying shopping bags for an old woman; 5) a girl hugging a puppy; 6) a boy in sports clothes holding a football.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л4.2 · Сцены к Homework 3 и 4 — 2 карт. (2×1), сцены, полу-мультяшный 3D
Два монстра — вместо кадра со Шреком.
```
A sheet of 2 separate illustrations in a clean 2x1 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) two friendly green cartoon monsters standing side by side, one tall and thin, one short and round; 2) an alarm clock with plain tick marks, its hands at half past nine, on a bedside table next to a school backpack, morning light.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1024 px, each cell at least 650 px.
```

### Л4.3 · Лицо — 6 карт. (3×2), персонажи, 3D-мультяшные, на белом
Крупно одна часть лица мультяшного ребёнка, остальное мягко размыто.
```
A sheet of 6 separate picture cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a close-up of a cartoon child's eyes; 2) a close-up of a cartoon child's nose; 3) a close-up of a cartoon child's smiling mouth; 4) a close-up of a cartoon child's ear; 5) a close-up of a cartoon child's big white smile showing teeth; 6) a cartoon child seen from behind with thick shiny hair.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л4.4 · Тело — 9 карт. (3×3), персонажи, 3D-мультяшные, на белом
Нужная часть тела у мультяшного ребёнка подсвечена мягким золотым свечением.
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a cartoon child with the head glowing softly; 2) a cartoon child with the neck glowing softly; 3) a cartoon child with one arm glowing softly; 4) a cartoon child's open hand; 5) a cartoon child's hand with the fingers spread; 6) a cartoon child with one leg glowing softly; 7) one bare cartoon child's foot; 8) two bare cartoon child's feet; 9) a cartoon child's bare foot with wiggling toes.
It is the same cartoon child in every cell, in the same clothes: a T-shirt and shorts, barefoot.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л4.5 · Волосы и тело целиком — 9 карт. (3×3), персонажи, 3D-мультяшные, на белом
Портреты детей по плечи: у каждого свои волосы. Последняя — ребёнок в полный рост.
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a girl with red hair; 2) a boy with spiky hair; 3) a girl with wavy hair; 4) a boy with dark hair; 5) a girl with curly hair; 6) a girl with long straight hair; 7) a boy with blond hair; 8) a girl with fair light-brown hair; 9) a cartoon child standing in full height with arms slightly out.
Every child is shown head and shoulders, facing the viewer, so the hair is clearly visible; the last cell shows a whole child.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л4.6 · Сцены Unit 4 — 4 карт. (2×2), сцены с персонажами
Клоун Бонзо — по тексту задания: детали лица важны.
```
A sheet of 4 separate illustrations in a clean 2x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a friendly clown with big ears, big brown eyes, a big red mouth, very white teeth, a red nose and grey curly hair; 2) a boy who has fallen on the playground and a girl helping him up and asking if he is OK; 3) a smiling grandmother with curly grey hair; 4) children at their desks in an English class, a teacher at the board.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```


---

# UNIT 5 — листов: 6

### Л5.1 · Глаголы 1 — 9 карт. (3×3), мультяшный глянец
Действие без людей — предметом или животным.
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) comedy and tragedy theatre masks on a small stage with red curtains; 2) a monkey climbing up a tree trunk; 3) a frying pan with eggs on a cooker and a pot of vegetables; 4) a diving mask, a snorkel and flippers under water with bubbles; 5) a spanner and a screwdriver next to a bicycle with a loose chain; 6) a small colourful bird flying; 7) a kangaroo jumping high; 8) an open book with a bookmark; 9) a bicycle.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л5.2 · Глаголы 2 — 6 карт. (3×2), мультяшный глянец
```
A sheet of 6 separate picture cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a microphone with music notes floating around it; 2) a cheetah running fast; 3) a dolphin swimming in the waves; 4) a pen writing lines in a notebook; 5) a skateboard jumping off a ramp; 6) a palette, a brush, coloured pencils and a drawing of a house.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л5.3 · Вещи к заданиям Unit 5 — 9 карт. (3×3), реалистичный 3D
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a folded newspaper; 2) a screwdriver; 3) swimming goggles; 4) an acoustic guitar; 5) wax crayons next to a child's drawing of a sun and a tree; 6) a mixing bowl with a whisk and vegetables beside it; 7) an open laptop with a screwdriver lying next to it; 8) a small French flag on a little stand; 9) a stack of books with an apple on top.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л5.4 · Чем заняться: play / ride / make — 6 карт. (3×2), мультяшный глянец
```
A sheet of 6 separate picture cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) piano keys with music notes above them; 2) a horse with a saddle in a meadow; 3) cupcakes with cream and a piping bag; 4) a football in front of a goal; 5) a bicycle with a helmet hanging on the handlebars; 6) a big poster sheet with paints and brushes around it.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л5.5 · Собаки, хомяк и мишки — 6 карт. (3×2), мультяшный глянец
Три мишки — варианты ответа в Homework 6: верный — с голубыми глазами.
```
A sheet of 6 separate picture cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a friendly labrador sitting; 2) a beagle puppy running; 3) a hamster; 4) a teddy bear with black button eyes; 5) an old torn teddy bear with one eye missing; 6) a teddy bear with new bright blue eyes.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л5.6 · Люди Unit 5 — 2 карт. (2×1), сцены с персонажами
Вместо фото в Homework 5.
```
A sheet of 2 separate illustrations in a clean 2x1 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) two women talking to each other in sign language with their hands; 2) a girl of twelve with her labrador dog wearing a 'hearing dog' vest without any text.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1024 px, each cell at least 650 px.
```


---

# UNIT 6 — листов: 4

### Л6.1 · Распорядок дня 1 — 9 карт. (3×3), мультяшный глянец
Действие — предметом, без людей.
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a ringing alarm clock on a bedside table next to an unmade bed, morning sun; 2) a school building with a backpack on the path in front; 3) a bed with a pillow and a duvet, the moon in the window; 4) a shower head with running water, soap and a towel; 5) a bowl of cereal with milk, a glass of juice and toast; 6) a lunch box with a sandwich and an apple; 7) a plate with dinner and a candle, evening; 8) a school desk with textbooks in front of a green board with simple chalk drawings of shapes; 9) a notebook with a pencil and a textbook on a desk.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л6.2 · Распорядок дня 2 — 9 карт. (3×3), мультяшный глянец
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) three scooters leaning on a bench in a park; 2) headphones with music notes; 3) a mop, a box of toys and a pile of folded clothes; 4) a TV with a remote control; 5) two tennis rackets and a ball by a net; 6) an alarm clock with little legs running away; 7) a diary covered with sticky notes and a phone; 8) a treadmill and dumbbells; 9) a school lunch on a tray.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л6.3 · Майк и Даша, еда и игры — 9 карт. (3×3), реалистичный 3D
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a pizza; 2) a basketball by a hoop; 3) a city skyline with tall skyscrapers; 4) a pair of pink ballet pointe shoes; 5) a stack of pancakes with berries; 6) an open maths notebook with a ruler, a protractor and a calculator; 7) a game controller in front of a monitor with a game; 8) a dinner table laid with four plates; 9) a chocolate ice cream cone.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л6.4 · Майк, Даша, Джен — 3 карт. (3×1), персонажи, 3D-мультяшные, на белом
Портреты к текстам — вместо фото детей.
```
A sheet of 3 separate picture cards in a clean 3x1 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) Mike, an American boy of ten holding a basketball; 2) Dasha, a girl of nine in a ballet outfit; 3) Jen, a girl of eleven with a skateboard.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1024 px, each cell at least 650 px.
```


---

# UNIT 7 — листов: 4

### Л7.1 · Дикие животные 1 — 9 карт. (3×3), мультяшный глянец
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a small bright bird on a branch; 2) a butterfly with open wings; 3) a green crocodile, whole body, side view; 4) a grey elephant with its trunk up; 5) a goldfish; 6) a friendly little fly; 7) a green frog; 8) a giraffe, whole body; 9) a kangaroo with a baby in its pouch.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л7.2 · Дикие животные 2 — 9 карт. (3×3), мультяшный глянец
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a lion with a big mane; 2) a monkey hanging from a vine; 3) a snake curled up; 4) a spider on its web; 5) a tiger; 6) a blue whale, side view, with a water spout; 7) a grey cat; 8) a white and grey rabbit with leaves and carrots; 9) a fluffy kitten with big eyes.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л7.3 · Какие они? И котята — 6 карт. (3×2), мультяшный глянец
```
A sheet of 6 separate picture cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a shark with its mouth open; 2) a cheetah running with speed lines; 3) a snail; 4) a gorilla lifting a big log; 5) a warty toad; 6) a basket with six kittens: three black, two black and white, one grey.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л7.4 · Сцены Unit 7 — 3 карт. (3×1), сцены, полу-мультяшный 3D
```
A sheet of 3 separate illustrations in a clean 3x1 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a shark swimming under water among small fish; 2) a zoo ticket office window with tickets on the counter; 3) a cafe counter with a cheese sandwich on a plate and a till.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1024 px, each cell at least 650 px.
```


---

# UNIT 8 — листов: 5

### Л8.1 · Спорт 1 — 9 карт. (3×3), реалистичный 3D
Спорт — инвентарём, без людей.
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a badminton racket and a shuttlecock; 2) a basketball by a hoop; 3) a racing bicycle; 4) a football and a goal; 5) an ice hockey stick and a puck on ice; 6) a pair of white figure skates on ice; 7) a pair of roller skates; 8) a sailing boat on the water; 9) a skateboard on a ramp.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л8.2 · Спорт 2 и здоровье — 9 карт. (3×3), реалистичный 3D
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) skis and poles in the snow; 2) a swimming pool with lane ropes, goggles and a swimming cap; 3) table tennis bats and a ball on a table; 4) a white taekwondo uniform folded with a black belt; 5) a tennis racket and a yellow ball; 6) a volleyball by a net; 7) a windsurfing board with a sail on a wave; 8) a toothbrush with toothpaste and a glass; 9) a glass and a bottle of water.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л8.3 · Погода — 9 карт. (3×3), мультяшный глянец
```
A sheet of 9 separate picture cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a bright sun in a blue sky; 2) fluffy grey and white clouds; 3) a dark cloud with rain and puddles below; 4) snow falling on snowy ground; 5) a tree bending in the wind with leaves flying; 6) fog over a field and trees; 7) a blazing sun and a thermometer with the red line very high; 8) a thermometer with the line very low and icicles; 9) a gentle sun over a spring meadow with flowers.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л8.4 · Времена года — 4 карт. (2×2), сцены, полу-мультяшный 3D
Одно и то же дерево в четыре времени года.
```
A sheet of 4 separate illustrations in a clean 2x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) the same tree in spring with pink blossom; 2) the same tree in summer, full green leaves; 3) the same tree in autumn with orange leaves falling; 4) the same tree in winter, bare branches covered with snow.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л8.5 · Здоровый образ жизни — 6 карт. (3×2), мультяшный глянец
```
A sheet of 6 separate picture cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) dumbbells, trainers and a skipping rope; 2) a bowl of fruit and vegetables; 3) a bed, the moon in the window, an alarm clock on the bedside table; 4) two puppies playing together; 5) a pillow and a duvet with a crescent moon above; 6) a heart shape made of fruit, a dumbbell and a water bottle.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```


---

# FINAL TEST — листов: 3

### ЛФ.1 · Гостиная к финальному тесту — сцена, сцены, полу-мультяшный 3D
Для «диаграммы»: подписать вещи в комнате.
```
One single scene filling the frame: a living room with two armchairs, a bookcase by the window, a rug, a small coffee table, a cabinet and pictures on the wall.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### ЛФ.3 · Семья в гостиной — Reading Part 2 — сцена, сцены с персонажами
Ответы задания держатся на деталях: мужчина с чёрными волосами и в очках, дети НЕ поют, женщина держит напитки, кот спит под креслом, лампа на книжном шкафу, два кресла, большое окно закрыто.
```
One single scene filling the frame: a family in a living room: a man with black hair and glasses sitting in one of two armchairs, two children playing a board game on the rug, a woman holding a tray of drinks, a cat sleeping under the other armchair, a lamp on top of a bookcase, a big closed window.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### ЛФ.2 · Вещи к финальному тесту — 6 карт. (3×2), реалистичный 3D
```
A sheet of 6 separate picture cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each subject centred with a generous empty margin on all sides, never touching the cell edges:
1) a bunch of grapes; 2) a small red car; 3) one brown boot; 4) three chairs in a row; 5) a desktop computer with a keyboard; 6) an old-fashioned radio.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```
