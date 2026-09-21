# Super Minds 3 — ЛИСТЫ ПРОМПТОВ НА КАРТИНКИ

Один промпт = одна картинка-лист с сеткой внутри. Потом лист режется на отдельные PNG.
**89 листов** на 9 юнитов + Final Test.

## Два жёстких правила

**1. Людей нет нигде.** Ни героев учебника, ни безымянных детей, ни рук, ни лиц.
Все картинки — предметы, места, животные и «следы действий». Герои и сюжеты есть
в учебнике и в видео — кадры режем оттуда.

**2. Максимум 3 колонки в сетке.** Генератор отдаёт 1536 px по длинной стороне;
на трёх колонках это 512 px на ячейку — нижняя рабочая граница. На четырёх и пяти
карточка выходит мелкой и мылит при нарезке. Поэтому наборы из 10–12 карточек
разбиты на два листа.

## Правила листа

- Промпт копируется целиком, дописывать ничего не надо: сетка, разделители,
  запрет текста, запрет людей и разрешение уже внутри.
- Ячейки нумеруются слева направо, сверху вниз — в том же порядке, в каком
  перечислены в промпте.
- Разрешение указано в каждом промпте. Если инструмент не умеет столько —
  ставим максимум, который умеет, но лист **не переупаковываем** в более плотную
  сетку: лучше два листа, чем мелкие ячейки.
- «Сцена» (solo) — там, где ребёнок описывает картинку или ищет детали:
  одна большая картинка, в сетку не складывается.
- Животные разрешены: кошка, собака, дельфин — это предметы задания, а не герои.

## Стилевые регистры

Сложились сами по ходу генерации, дальше держим осознанно. В одном листе — **один** регистр,
иначе после нарезки карточки не встанут в ряд.

| Что | Регистр |
|---|---|
| Обложки юнитов и сюжетные сцены (пикник, магазин, кабинет) | полу-мультяшный 3D, как Л1.1 и Л2.8 |
| Предметные карточки (еда, гаджеты, достопримечательности) | реалистичный 3D — узнаваемость важнее |
| Символы и схемы (предметы школы, погода, экология, части растений) | мультяшный глянец |
| Фигуры и коллажи из фигур | плоский вектор |
| Животные в мультяшной манере | только на отдельном листе, не в одной сетке с фото-едой |

## Что берём из книги, а не генерируем

| Из учебника / видео | Где это было |
|---|---|
| Все кадры истории Ben & Lucy | U1 библиотека, U3 деревня, U4 башня, U5 под водой, U6 пещеры, U7 больница, U8 глобус, U9 замок |
| Рассказ про Оливера, интервью с Кейт | U1 |
| Ящерицы-повара, видео | U2 |
| Песня про астронавтку, «Эльфы и башмачник» | U3 |
| Открытка от Али, «кто куда идёт» | U4 |
| Монстр Crocorox, Кайли и дельфины | U5 |
| Наскальные рисунки (фото), класс 6C, сад с мальчиками | U6 |
| **Болезни и симптомы, врач и медсестра** (там нужны люди — в книге есть флешкарты) | U7 |
| Песня «плохой день», Эмма и Джаспер, Джо Фриз | U7 |
| Машина времени, Макс в Чили | U8 |
| Лиам во Флориде, Брайтон 100 лет назад | U9 |
| Шесть человек на аудирование, большая картинка «верно/неверно», Джим и клоун | Final Test |

Кадры режем из PDF учебника и из видео, жмём в webp (карточка 180–420 px,
сцена 760–900 px) и кладём в `media/sm3/uN/` — ссылками, как весь остальной проект.

---

# UNIT 1 · SCHOOL — 9 листов

### Л1.1 · Обложка юнита (сцена)
```
A cheerful empty cartoon classroom, wide view from inside the room with nothing in the foreground - no door, no door frame, no doorknob. Rows of desks with colourful backpacks hanging on the chairs, a big sunny window with potted plants, a globe on the teacher's desk, bookshelves, a blank green board, an open notebook and colour pencils on the front desk. Warm morning light.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, one single scene filling the frame. Absolutely no text, no letters, no numbers, no signs, no labels, no brand marks anywhere.
Output size: 2048 x 1365 px.
```

### Л1.2 · Школьные предметы — 9 карточек (3×3)
```
A sheet of nine separate object cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells. Each cell shows one glossy 3D icon-object standing for a school subject:
1) an open book with a quill and a ribbon bookmark; 2) a calculator with a ruler, a compass and small floating geometric shapes; 3) a globe with a magnifying glass and a folded paper map; 4) a laptop with a mouse and a small glowing circuit board; 5) a trumpet with a small keyboard and floating music notes; 6) a bubbling flask, a test-tube rack and a microscope; 7) a paint palette with brushes and colourful paint blobs; 8) a football with a skipping rope and a whistle; 9) an old scroll with a knight's helmet and a sand timer.
No people at all - no humans, no hands, no faces anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Absolutely no text, no letters, no numbers, no labels, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л1.3 · have to — 6 предметных сцен (3×2)
```
A sheet of six separate illustrations in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone scene, nothing crossing between cells. Each cell shows the objects of one daily duty, with nobody doing it:
1) an open school gate in the morning with a round wall clock beside it, the clock face has plain ticks and no numbers;
2) a bathroom shelf with a toothbrush in a cup and a tube of toothpaste in front of a mirror;
3) a kitchen tap with running water, a soap dispenser and foam in the sink, a laid dinner table behind;
4) a school uniform laid out on a bed beside an open wardrobe;
5) a pair of plain unbranded trainers and a shoe brush on a doorstep with a football beside them;
6) a finished open notebook with a pencil on a desk, a bicycle and a ball waiting by the door.
No people at all - no humans, no children, no hands, no faces anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Absolutely no text, no letters, no numbers, no labels, no brand logos, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л1.4 · Геометрические фигуры — 6 карточек (3×2)
```
A sheet of six separate shape cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell on pure white, one single flat geometric shape per cell, centred, thick black outline, one flat bright colour each:
1) a red triangle; 2) a blue square; 3) a green circle; 4) an orange rectangle; 5) a yellow pentagon; 6) a purple hexagon.
Clean children's-textbook vector look, crisp edges, soft drop shadow. Absolutely no text, no letters, no numbers, no labels, no measurements anywhere.
Output size: 2048 x 1365 px.
```

### Л1.5 · Картинки из фигур — 4 карточки (2×2)
```
A sheet of four separate pictures in a clean 2x2 grid, equal cells separated by thin light-grey gutters, each cell on pure white. Each cell shows one simple cartoon figure built entirely out of flat geometric shapes - triangles, circles, squares and rectangles - like a children's shape collage, the individual shapes clearly visible:
1) a cat; 2) a simple shape-person made of a circle head, a square body and rectangle limbs; 3) a sailing boat; 4) a snake.
Flat bright colours, thick black outlines, clean children's-textbook look. Absolutely no text, no letters, no numbers, no labels anywhere.
Output size: 2048 x 2048 px.
```

### Л1.6 · Расписание на неделю (сцена)
```
A school timetable board on a classroom wall shown as a picture grid only: five vertical columns for five school days, each column filled with small subject icons stacked from top to bottom - a book, a calculator, a football, a globe, a laptop, a trumpet, a flask, a paint palette, a scroll - and a lunch tray icon in the middle row of every column. The icons are clearly drawn and easy to compare between columns.
No people at all anywhere.
Bright 3D-rendered cartoon style, Pixar-like, glossy rounded icons, vivid saturated colours, clean and orderly. Absolutely no text, no letters, no numbers, no day names, no labels anywhere - the days must be readable only from the icons.
Output size: 2048 x 1365 px.
```

### Л1.7 · Раскраска: фигуры (сцена)
```
A children's colouring page: a friendly robot and a house built out of large geometric shapes - several squares, circles, pentagons, triangles and rectangles - every shape big, closed and clearly separated so it can be coloured one by one.
No people anywhere. Black and white line art, clean even outlines, no shading, no grey, no fills, pure white background. Absolutely no text, no letters, no numbers anywhere.
Output size: 1536 x 2048 px.
```

### Л1.8 · Раскраска: школьный двор (сцена)
```
A children's colouring page of an empty school yard: a backpack on a bench, a football, a tree, a bicycle in a rack, a cat sitting on a wall, a window with a flowerpot, a skipping rope on the ground - all drawn with big simple closed outlines, well separated, easy to colour.
No people anywhere. Black and white line art, clean even outlines, no shading, no grey, no fills, pure white background. Absolutely no text, no letters, no numbers anywhere.
Output size: 1536 x 2048 px.
```

### Л1.9 · Speaking: шесть уголков класса (сцена)
```
One wide classroom scene with six clearly separated corners, each set up for a different school subject but with nobody there: an easel with wet paint and brushes; a desk with a calculator, a ruler and a compass; a music corner with a recorder and a small keyboard; a globe and an open atlas on a stand; a science table with a flask and a microscope; a gym doorway with a football and a skipping rope.
No people at all - no humans, no children, no hands, no faces anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, soft even light, everything clearly visible and countable. Absolutely no text, no letters, no numbers, no labels anywhere.
Output size: 2048 x 1365 px.
```

---

# UNIT 2 · FOOD — 11 листов

### Л2.1 · Обложка юнита (сцена)
```
A bright kitchen table seen from slightly above, loaded with a friendly spread: a jug of apple juice, bread rolls, a wedge of cheese, a bowl of soup, a salad bowl, fresh vegetables and a bottle of water. Warm daylight from a window.
No people at all - no humans, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, appetising, vivid saturated colours, one single scene filling the frame. Absolutely no text, no letters, no numbers, no labels, no packaging writing, no brand marks anywhere.
Output size: 2048 x 1365 px.
```

### Л2.2 · Еда — 9 карточек (3×3)
```
A sheet of nine separate food cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell one appetising food item centred on pure white:
1) a tall glass of apple juice with a red apple beside it; 2) three bread rolls on a small wooden board; 3) a wedge of yellow cheese with holes; 4) a clear glass of water with a bottle; 5) a bowl of vegetable soup with a spoon and light steam; 6) a small pile of vegetables - carrot, tomato, broccoli, pepper; 7) a glass of lemonade with a lemon slice and a straw; 8) a bowl of green salad with tomato; 9) a small bowl of green peas with an open pod.
No people, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Absolutely no text, no letters, no numbers, no labels, no packaging writing, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л2.3 · Еда, продолжение — 3 карточки (3×1)
```
A three-panel strip in one horizontal row, equal panels separated by thin light-grey gutters, each panel one food item centred on pure white:
1) a whole pineapple; 2) three sausages on a plate; 3) two onions, one of them halved.
No people, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no labels, no brand marks anywhere.
Output size: 2048 x 683 px.
```

### Л2.4 · Подносы для there is / there are — 6 картинок (3×2)
```
A sheet of six separate pictures in a clean 3x2 grid, equal cells separated by thin light-grey gutters. Each cell shows one tray on a table seen from slightly above, holding exactly the listed items, clearly separated and easy to count:
1) potatoes, peas and onions; 2) a jug of milk, a glass of lemonade and a glass of orange juice; 3) biscuits, a slice of cake and a bar of chocolate; 4) a whole cake, biscuits and sandwiches; 5) peas, potatoes and nuts; 6) a bottle of water, a glass of apple juice and a glass of milk.
No people, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, appetising, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no labels, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л2.5 · Корзинки, ланчбокс, холодильник — 6 картинок (3×2)
```
A sheet of six separate pictures in a clean 3x2 grid, equal cells separated by thin light-grey gutters:
1) a wicker shopping basket holding only vegetables - carrots, potatoes, onions - and no fruit at all;
2) a wicker basket holding only fruit - apples, bananas, grapes - and no vegetables at all;
3) a wicker basket holding both fruit and vegetables together;
4) a wicker basket with bananas and a bottle of apple juice and no tomatoes at all;
5) an open school lunch box on a desk with one bread roll filled with cheese and a small bottle of water, nothing else;
6) an open fridge seen from the front with cheese, a bottle of water, vegetables and rolls on the shelves and no cake and no sausages.
No people, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, appetising, vivid saturated colours, everything clearly countable. Absolutely no text, no letters, no numbers, no labels, no packaging writing, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л2.6 · Части растений — 6 карточек (3×2)
```
A sheet of six separate botanical cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell on pure white. In cells 1-5 one edible plant part is shown in bright colour while the rest of the plant stays pale grey, so the highlighted part is obvious:
1) roots - a carrot and a beetroot with the roots highlighted; 2) stems - asparagus and celery; 3) leaves - spinach and lettuce; 4) seeds - sunflower seeds and peas in an open pod; 5) fruit - a strawberry and a mango;
6) a whole simple plant diagram with all five parts visible at once, each part in a different bright colour.
No people, no hands anywhere.
Clean cartoon-botanical style, soft rounded shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no labels, no arrows with writing anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л2.7 · Блюда из растений — 5 картинок (3+2)
```
A sheet of five separate pictures in a clean grid of three cells in the top row and two cells in the bottom row, equal cells separated by thin light-grey gutters, the empty sixth position left as plain white:
1) a green salad of spinach and lettuce in a bowl; 2) a bowl of asparagus soup; 3) roast pumpkin with chicken on a plate; 4) a salad of carrots and beetroot; 5) a tall glass of strawberry and mango smoothie.
No people, no humans, no hands anywhere.
Realistic appetising food photography look, soft natural light, shallow depth of field, warm wooden surfaces. Absolutely no text, no letters, no numbers, no labels anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л2.12 · Кто какую часть растения ест (сцена)
```
A sunny meadow with six animals, each one clearly eating a different part of a plant, well separated across the frame so every pair is unmistakable:
a rabbit biting an orange carrot pulled from the ground (root); a giraffe pulling green leaves from a branch (leaves); a parrot cracking sunflower seeds from a large sunflower head (seeds, not leaves); a panda chewing a thick bamboo stem (stem); a monkey holding a mango (fruit); a goat nibbling grass.
No people at all - no humans, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, friendly animal faces, vivid saturated colours, one single scene. Absolutely no text, no letters, no numbers, no labels anywhere.
Output size: 2048 x 1365 px.
```

### Л2.8 · Пикник (сцена)
```
A picnic laid out on a sunny meadow with nobody there: a checked blanket, an open wicker basket, sandwiches on a plate, tomatoes, a jar of jam, a bottle of lemonade, paper cups, and a kite lying on the grass beside them.
No people at all - no humans, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, everything clearly visible and countable. Absolutely no text, no letters, no numbers, no labels anywhere.
Output size: 2048 x 1365 px.
```

### Л2.9 · Пиццерия (сцена)
```
An empty pizza counter with nobody behind it: bowls of toppings on display - cheese, onions, peppers, tomatoes - a rolled-out pizza base on a board, a pizza peel, and one bowl that is completely empty where the mushrooms should be.
No people at all - no humans, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, everything clearly visible. Absolutely no text, no letters, no numbers, no menu writing, no signs anywhere.
Output size: 2048 x 1365 px.
```

### Л2.10 · Ужин на столе (сцена)
```
A family dinner table laid for four with nobody sitting at it: four plates with chicken, peas and chips, a jug of water, four glasses, cutlery, and a round wall clock behind whose face has plain ticks and no numbers, the hands showing seven o'clock.
No people at all - no humans, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, warm evening light, vivid saturated colours. Absolutely no text, no letters, no numbers anywhere, including on the clock face.
Output size: 2048 x 1365 px.
```

### Л2.11 · Кафе с меню-картинками (сцена)
```
A cosy empty children's cafe: a table laid for two, a tray on the counter, and a standing menu board showing pictures only - a chicken roll, a cheese sandwich, a bowl of soup, a salad, a glass of lemonade, a glass of apple juice - each picture in its own empty frame.
No people at all - no humans, no waiters, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, everything clearly visible. Absolutely no text, no letters, no numbers, no prices, no writing on the menu board anywhere.
Output size: 2048 x 1365 px.
```

---

# UNIT 3 · AT HOME / TIME / JOBS — 9 листов

### Л3.1 · Обложка юнита (сцена)
```
A cheerful cutaway view of an empty family home: a broom leaning by a swept floor, a sink full of foam with plates beside it, a dog lead hanging by the front door with a small dog waiting under it, a cat on a chair, and a big round wall clock with plain ticks and no numbers.
No people at all - no humans, no hands anywhere; the dog and the cat are fine.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, warm light, one single scene. Absolutely no text, no letters, no numbers anywhere.
Output size: 2048 x 1365 px.
```

### Л3.2 · Домашние дела — 6 карточек (3×2)
```
A sheet of six separate cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell showing the objects of one household chore with nobody doing it:
1) tidy up - a tidy bedroom shelf with a big box of toys beside it, a few toys still on the floor;
2) do the shopping - a full shopping bag of vegetables standing on a kitchen floor;
3) take the dog for a walk - a dog lead hanging by the front door with a small dog sitting under it, waiting;
4) wash up - a kitchen sink full of foam with dirty plates stacked beside it;
5) sweep - a broom and a dustpan on a wooden floor with a small pile of dust;
6) cook - a pot simmering on a cooker with a wooden spoon and chopped vegetables on a board.
No people at all - no humans, no hands, no faces anywhere; the dog is fine.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no labels, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л3.3 · Домашние дела, продолжение — 2 карточки (2×1)
```
A two-panel strip in one horizontal row, equal panels separated by a thin light-grey gutter, each panel showing the objects of one household chore with nobody doing it:
1) dry the dishes - a stack of clean dry plates with a folded tea towel over the edge of a draining board;
2) feed the dog - a dog bowl full of food on the kitchen floor with a scoop beside it and a small dog waiting.
No people at all - no humans, no hands anywhere; the dog is fine.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no labels, no brand marks anywhere.
Output size: 2048 x 1024 px.
```

### Л3.4 · Циферблаты, часть 1 — 6 карточек (3×2)
```
A sheet of six separate clock cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell one simple round wall clock on a plain pastel wall. Every clock has a white face, bold black hour and minute hands and twelve plain tick marks with absolutely no numbers on the dial. The hands show, in order:
1) quarter past eight; 2) half past eight; 3) quarter past five; 4) quarter to seven; 5) half past six; 6) twelve o'clock.
No people anywhere. Clean 3D cartoon style, soft rounded shapes, soft even light, crisp readable hands, hour hand clearly shorter than the minute hand. Absolutely no text, no letters, no numbers, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л3.5 · Циферблаты, часть 2 — 6 карточек (3×2)
```
A sheet of six separate clock cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell one simple round wall clock on a plain pastel wall. Every clock has a white face, bold black hour and minute hands and twelve plain tick marks with absolutely no numbers on the dial. The hands show, in order:
1) twenty to four; 2) quarter past three; 3) quarter to five; 4) six o'clock; 5) half past ten; 6) quarter to eight.
No people anywhere. Clean 3D cartoon style, soft rounded shapes, soft even light, crisp readable hands, hour hand clearly shorter than the minute hand. Absolutely no text, no letters, no numbers, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л3.6 · Профессии — 9 карточек (3×3)
```
A sheet of nine separate profession cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a neat flat-lay of the uniform and tools of one job on pure white, with nobody wearing them:
1) firefighter - a helmet, a coiled hose and heavy boots; 2) cleaner - a mop, a bucket and a folded high-vis vest; 3) vet - a folded white coat, a stethoscope and a pet carrier with a cat looking out; 4) police officer - a peaked cap, a radio and a pair of handcuffs; 5) teacher - a stack of books, a small blank board and a pointer; 6) security guard - a dark cap, a torch and a radio; 7) ambulance driver - an ambulance with open rear doors and a medical bag on the ground; 8) shopkeeper - a folded apron, a crate of fruit and a set of scales with a blank dial; 9) nurse - folded scrubs, a thermometer and a roll of bandage.
No people at all - no humans, no hands, no faces, no mannequins anywhere; the cat is fine.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no badges with writing, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л3.7 · Кухня после дел (сцена)
```
A family kitchen where four chores have just been done and nobody is there: a sink of foam with a sponge, a stack of dry plates under a tea towel, a cat bowl with food on the floor, a pot simmering on the cooker. On the wall a calendar shown only as a grid of empty squares and a round clock with plain ticks and no numbers.
No people at all - no humans, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, everything clearly visible. Absolutely no text, no letters, no numbers anywhere.
Output size: 2048 x 1365 px.
```

### Л3.8 · Ночные профессии (сцена)
```
An empty night-time street: a torch lying lit on a security desk behind a glass door, a lit hospital window, a mop and bucket left on the pavement, an ambulance parked with its lights on, a dark starry sky above.
No people at all - no humans, no silhouettes in the windows anywhere.
Bright 3D-rendered cartoon style, Pixar-like, night lighting with warm lamp pools, vivid saturated colours. Absolutely no text, no letters, no numbers, no signs anywhere.
Output size: 2048 x 1365 px.
```

### Л3.9 · Распорядок дня (сцена)
```
One wide sheet showing six small object vignettes in a left-to-right row, each one standing for a moment of the day, with a small round clock face beside it that has plain ticks and no numbers and shows a different time: an alarm clock on a bedside table with the bed just left; a breakfast bowl and a glass of juice; a backpack by the front door; a lunch tray; a dog lead and a ball on the doorstep; a bedside lamp with a closed book.
No people at all - no humans, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, clean and orderly, one single composition. Absolutely no text, no letters, no numbers anywhere, including on the clock faces.
Output size: 2048 x 683 px.
```

---

# UNIT 4 · IN THE TOWN — 10 листов

### Л4.1 · Обложка юнита (сцена)
```
A friendly cartoon town square seen from a three-quarter aerial view, empty of people: a bank, a tall tower with a clock face without numbers, a library, a supermarket, a bus station with a bus, a car park with a few cars, and a small funfair wheel in the distance. Sunny day, trees and benches.
No people at all - no humans, no tiny figures in the street anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, one single scene. Absolutely no text, no letters, no numbers, no shop signs, no labels anywhere.
Output size: 2048 x 1365 px.
```

### Л4.2 · Места в городе — 9 карточек (3×3)
```
A sheet of nine separate building cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell one small cartoon building or place standing alone on pure white in three-quarter view:
1) a bank - a solid building with columns and a blank façade; 2) a tall stone tower with a pointed roof and a clock face with plain ticks and no numbers; 3) a folded paper street map with a compass rose; 4) a library with a big arched window and a blank book-shaped sign; 5) a market square with striped market stalls; 6) a supermarket shop front with trolleys outside; 7) a bus station shelter with a bus pulling in; 8) a modern sports centre with a ball and a swimming symbol on the wall; 9) a flat car park with three parked cars and a barrier.
No people at all - no humans, no drivers, no figures anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no shop signs, no labels, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л4.3 · Ярмарка и направления — 4 карточки (2×2)
```
A sheet of four separate cards in a clean 2x2 grid, equal cells separated by thin light-grey gutters, each cell on pure white:
1) a funfair with a ferris wheel and a carousel; 2) a road running straight ahead with a big bold arrow pointing forward; 3) a road junction with a big bold arrow bending to the left; 4) a road junction with a big bold arrow bending to the right.
No people at all anywhere.
Bright 3D-rendered cartoon style, Pixar-like, glossy rounded shapes, thick soft outlines, vivid saturated colours. Absolutely no text, no letters, no numbers, no road markings that look like writing anywhere.
Output size: 2048 x 2048 px.
```

### Л4.4 · Предлоги места, часть 1 — 6 карточек (3×2)
```
A sheet of six separate cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a simple unmistakable arrangement on a plain pastel background where the spatial relation is obvious at a glance:
1) a cat under a sofa; 2) a cat and a dog facing each other across a rug, opposite one another; 3) a cat standing below a wall shelf; 4) a fox sitting in front of a cardboard box; 5) a mouse between two boxes; 6) a monkey behind a tree, peeping out.
No people at all - no humans, no hands anywhere; the animals are fine.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light, uncluttered. Absolutely no text, no letters, no numbers, no arrows, no labels anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л4.5 · Предлоги места, часть 2 — 6 карточек (3×2)
```
A sheet of six separate cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a simple unmistakable arrangement on a plain pastel background where the spatial relation is obvious at a glance:
1) a ball floating above a table; 2) a teddy bear next to a ball; 3) an elephant in front of a chair; 4) a mouse near a television; 5) a white cat opposite a grey cat; 6) a framed picture hanging below a window on a wall.
No people at all - no humans, no hands anywhere; the animals and toys are fine.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light, uncluttered. Absolutely no text, no letters, no numbers, no arrows, no labels anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л4.6 · be going to — 6 карточек (3×2)
```
A sheet of six separate cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters. Each cell is a split card: on the left the object that shows the purpose, on the right the destination building, with a dotted arrow between them and nobody in the picture:
1) two milkshake glasses and a cafe; 2) a cinema ticket-free popcorn box and a cinema with a blank poster board; 3) an empty rucksack and a library; 4) a wrapped present and a market stall; 5) a swimming bag with goggles and a sports centre; 6) a shopping list-free basket and a supermarket.
No people at all - no humans, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, soft even light, clear and uncluttered. Absolutely no text, no letters, no numbers, no shop signs, no writing on the poster board anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л4.7 · CLIL: башни — 4 карточки (2×2)
```
A sheet of four separate structure cards in a clean 2x2 grid, equal cells separated by thin light-grey gutters, each cell one tall structure standing alone on pure white in three-quarter view:
1) a striped lighthouse on rocks with a beam of light; 2) a modern glass skyscraper; 3) an airport control tower with a glass top and a plane taking off behind it; 4) a stone clock tower with a big clock face that has plain ticks and no numbers.
No people at all anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no signs anywhere.
Output size: 2048 x 2048 px.
```

### Л4.8 · Карта города (сцена)
```
A top-down cartoon town map: streets and crossings, a market square in the middle, a park opposite it, a museum, a cinema, a library, a sports centre, a cafe, a castle on a hill, a bridge over a river with a small boat below it, a tower and a school. Buildings drawn as little 3D icons standing on the map, roads clearly visible, trees and benches between them.
No people at all - no humans, no tiny figures anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, clean and readable, one single map filling the frame. Absolutely no text, no letters, no numbers, no street names, no labels, no compass letters anywhere.
Output size: 2048 x 2048 px.
```

### Л4.9 · Городская сцена под предлоги (сцена)
```
One town street scene, empty of people, arranged so that these relations are unmistakable: the cinema stands opposite the library, a tall tower rises behind the cinema, a park lies opposite the school, a small boat floats below a bridge, the sports centre stands between the cinema and a cafe, and a castle rises behind the sports centre.
No people at all anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, clear uncluttered composition, everything clearly visible. Absolutely no text, no letters, no numbers, no signs, no labels anywhere.
Output size: 2048 x 1365 px.
```

### Л4.10 · Speaking: предлоги (сцена)
```
A tidy empty town corner: a library standing near a shopping centre, a bench between two small trees, a bicycle in front of a cafe, a bird above a lamp post, a dog sitting opposite a cat, a postbox next to a door, a parked car behind a hedge.
No people at all - no humans anywhere; the dog, the cat and the bird are fine.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, everything clearly visible and countable. Absolutely no text, no letters, no numbers, no signs anywhere.
Output size: 2048 x 1365 px.
```

---

# UNIT 5 · UNDER THE SEA — 8 листов

### Л5.1 · Обложка юнита (сцена)
```
A sunny underwater scene: a colourful coral reef, a dolphin, a sea turtle, a shoal of small fish, an old iron anchor half-buried in the sand, sunbeams coming down from the surface.
No people at all - no divers, no swimmers anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, soft underwater light, one single scene. Absolutely no text, no letters, no numbers anywhere.
Output size: 2048 x 1365 px.
```

### Л5.2 · Море — 9 карточек (3×3)
```
A sheet of nine separate cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell one sea creature or object centred on pure white:
1) a friendly grey seal on a rock; 2) a dolphin mid-leap; 3) an old iron anchor with a rope; 4) a green sea turtle swimming; 5) a large pink spiral shell; 6) a smiling purple octopus; 7) a yellow seahorse; 8) an orange starfish; 9) a translucent blue jellyfish.
No people at all - no divers, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no labels anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л5.3 · Ныряние и обитатели — 4 карточки (2×2)
```
A sheet of four separate cards in a clean 2x2 grid, equal cells separated by thin light-grey gutters, each cell on pure white:
1) to dive - a diving mask, a snorkel and a pair of flippers laid out together, with a few bubbles rising above them; 2) a shark swimming, friendly cartoon look, not frightening; 3) a shoal of small silver fish swimming together; 4) a bright coral branch.
No people at all - no divers, no hands, no bodies anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers anywhere.
Output size: 2048 x 2048 px.
```

### Л5.4 · Места для was/were — 9 карточек (3×3)
```
A sheet of nine separate place cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell one simple recognisable place, completely empty of people:
1) a restaurant interior with laid tables; 2) a museum hall with exhibits; 3) a park with a bench and trees; 4) a supermarket aisle with a trolley; 5) a hospital room with a made bed; 6) a cinema hall with red seats and a blank screen; 7) a sandy beach with an umbrella and a towel; 8) a swimming pool with lane ropes; 9) a garden with flowers and a watering can.
No people at all - no humans, no figures, no silhouettes anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no signs, no labels anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л5.5 · Экология: климат и загрязнение — 6 иконок (3×2)
```
A sheet of six separate icon-scenes in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell one clear idea on pure white:
1) a globe with a thermometer and a hot sun beside it; 2) a house standing half-submerged in flood water; 3) a small melting ice floe with a polar bear on it; 4) plastic bags floating in blue water; 5) a sad-eyed fish with a plastic bag near its mouth; 6) a huge cargo ship with a dark plume of smoke behind it.
No people at all anywhere; the polar bear and the fish are fine.
Flat-ish 3D icon style, glossy rounded shapes, thick soft outlines, vivid saturated colours, one clear idea per cell. Absolutely no text, no letters, no numbers, no labels anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л5.6 · Кораллы, мегалодон, вымершие — 4 картинки (2×2)
```
A sheet of four separate pictures in a clean 2x2 grid, equal cells separated by thin light-grey gutters:
1) a healthy coral reef full of bright pink, orange and purple corals with many small fish;
2) the same reef completely bleached white and empty, almost no fish;
3) a giant prehistoric shark swimming in deep blue water with a modern great white shark beside it for scale, the prehistoric one far larger;
4) a museum hall with skeletons and models of extinct animals - a dinosaur, a mammoth, a dodo, a giant shark jaw on a stand.
No people at all - no visitors, no divers, no figures for scale anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, kid-safe. Absolutely no text, no letters, no numbers, no museum labels anywhere.
Output size: 2048 x 2048 px.
```

### Л5.7 · Пляж тогда и сейчас — 2 картинки (2×1)
```
A two-panel comparison strip in one horizontal row, equal panels separated by a thin light-grey gutter, the same beach in both panels from the same viewpoint, completely empty of people:
1) a clean sandy beach on a sunny day - clear blue water, fish and dolphins visible in the shallows, a beach umbrella and a towel, no rubbish at all;
2) the same beach today - plastic bottles and bags all over the sand, cloudy grey-green water, no fish at all, the same umbrella now faded and leaning.
No people at all - no swimmers, no figures anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, identical composition in both panels so the difference is obvious. Absolutely no text, no letters, no numbers, no dates anywhere.
Output size: 2048 x 1024 px.
```

### Л5.8 · Что радует и что злит — 6 картинок (3×2)
```
A sheet of six separate small scenes in a clean 3x2 grid, equal cells separated by thin light-grey gutters. The top row shows three sights that clearly feel good, the bottom row three that clearly feel wrong:
1) dolphins jumping in a clean blue sea; 2) a young tree freshly planted on a clean beach with a watering can beside it; 3) a turtle swimming freely in clear water;
4) rubbish scattered all over a beach; 5) a turtle tangled in a plastic bag; 6) a bare patch of cut-down forest with stumps.
No people at all anywhere; the animals are fine.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, emotionally clear but kid-safe, nothing gruesome. Absolutely no text, no letters, no numbers anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

---

# UNIT 6 · GADGETS — 11 листов

### Л6.1 · Обложка юнита (сцена)
```
A desk covered with friendly cartoon gadgets: a laptop, a tablet, a mobile phone, a torch, a pair of walkie-talkies, a games console with a controller, an electric fan, a mug of pencils. Warm desk lamp light. All screens completely blank.
No people at all - no humans, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, one single scene. Absolutely no text, no letters, no numbers, no brand marks, no logos anywhere.
Output size: 2048 x 1365 px.
```

### Л6.2 · Гаджеты — 9 карточек (3×3)
```
A sheet of nine separate gadget cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell one modern gadget centred on pure white in three-quarter view, all screens completely blank:
1) a mobile phone; 2) a tablet; 3) a laptop; 4) a torch switched on with a light beam; 5) a pair of walkie-talkies; 6) open lift doors in a hallway; 7) a games console with a controller; 8) an electric toothbrush; 9) an electric fan.
No people at all - no humans, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no brand marks, no logos, no screen content anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л6.3 · Пары для сравнения, часть 1 — 6 карточек (3×2)
```
A sheet of six separate comparison cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters. Each cell shows exactly two objects side by side on pure white, same viewpoint, the difference obvious at a glance:
1) a big television and a small wristwatch; 2) a big cake and a small cookie; 3) an aeroplane and a bicycle; 4) a football and a golf ball with a club; 5) a tiger and a house cat; 6) an elephant and a mouse.
No people at all - no humans, no hands anywhere; the animals are fine.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, screens blank. Absolutely no text, no letters, no numbers, no price tags, no logos anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л6.4 · Пары для сравнения, часть 2 — 4 карточки (2×2)
```
A sheet of four separate comparison cards in a clean 2x2 grid, equal cells separated by thin light-grey gutters. Each cell shows exactly two objects side by side on pure white, same viewpoint, the difference obvious at a glance:
1) a butterfly and a caterpillar; 2) a desktop computer and a small torch; 3) a fancy white smartphone and a plain black smartphone; 4) a boxy 1970s game console with a wired controller and a slim modern console with a wireless controller.
No people at all - no humans, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, screens blank. Absolutely no text, no letters, no numbers, no logos, no brand marks anywhere.
Output size: 2048 x 2048 px.
```

### Л6.5 · Наскальная живопись: материалы — 6 карточек (3×2)
```
A sheet of six separate cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell one item on pure white:
1) small heaps of red, ochre and white mineral rock powder on a flat stone; 2) an old stone oil lamp with a small flame; 3) a rough rocky cave ceiling seen from below with a few bats; 4) a thin bare twig; 5) pieces of black charcoal; 6) a shallow stone bowl of ochre paint with a frayed brush beside it.
No people at all - no humans, no hands, no handprints anywhere.
Bright 3D-rendered cartoon style with a slightly earthy palette, soft rounded shapes, soft even light. Absolutely no text, no letters, no numbers, no labels anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л6.6 · Две собаки Lucky и Mister (сцена)
```
Two funny dogs standing side by side on a lawn, same viewpoint, easy to compare: on the left a small fluffy white dog with a pink bow, elegant and neat; on the right a big shaggy brown dog with muddy paws and a goofy grin.
No people at all - no humans, no hands, no leads held by anyone anywhere.
Bright 3D-rendered cartoon style, Pixar-like, expressive dog faces, vivid saturated colours. Absolutely no text, no letters, no numbers, no name tags with writing anywhere.
Output size: 2048 x 1365 px.
```

### Л6.7 · Магазин гаджетов с ценниками (сцена)
```
An electronics shop counter with nobody behind it: a laptop, a games console, a tablet, a pair of walkie-talkies, a torch, an electric toothbrush and a small digital radio on display, each item standing beside its own small price tag that is completely blank and empty.
No people at all - no shop assistant, no customers, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, all screens blank, every price tag empty. Absolutely no text, no letters, no numbers, no prices, no logos anywhere.
Output size: 2048 x 1365 px.
```

### Л6.8 · Два фонарика на прилавке (сцена)
```
A shop counter with nobody behind it: two torches standing side by side, one blue and one green, each beside its own completely blank price tag, a till with a blank display at the edge of the counter.
No people at all - no shop assistant, no customers, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours. Absolutely no text, no letters, no numbers, no prices, no logos anywhere.
Output size: 2048 x 1365 px.
```

### Л6.9 · Гаджет с четырьмя кнопками (сцена)
```
A chunky handheld gadget in the middle of the frame with exactly four big round buttons - red, blue, brown and green - and around it four small inset illustrations connected by thin lines showing what each button does: a beam of torchlight, floating music notes, a spinning fan, and a ringing phone handset.
No people at all - no humans, no hands holding the gadget anywhere.
Bright 3D-rendered cartoon style, Pixar-like, glossy rounded shapes, vivid saturated colours, clean diagram-like layout. Absolutely no text, no letters, no numbers, no labels anywhere.
Output size: 2048 x 1365 px.
```

### Л6.10 · Сад с мячами и рациями (сцена)
```
A garden scene with nobody in it, containing exactly: three balls on the grass, a red T-shirt and a smaller blue T-shirt hanging on a washing line, two grey T-shirts on the same line, two walkie-talkies lying on a garden table, and a bicycle standing behind a tree.
No people at all - no humans, no children, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, everything clearly visible and countable. Absolutely no text, no letters, no numbers, no brand marks anywhere.
Output size: 2048 x 1365 px.
```

### Л6.11 · Лифт и радио — 2 карточки (2×1)
```
A two-panel strip in one horizontal row, equal panels separated by a thin light-grey gutter, both objects on pure white:
1) open lift doors in a hallway with a blank call panel beside them; 2) a small digital radio with a blank display.
No people at all anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours. Absolutely no text, no letters, no numbers, no floor numbers, no brand marks anywhere.
Output size: 2048 x 1024 px.
```

---

# UNIT 7 · HEALTH — 4 листа

> Симптомы, врач и медсестра требуют людей — эти карточки берём из флешкарт учебника.
> Генерируем только предметное.

### Л7.1 · Обложка: кабинет врача (сцена)
```
A friendly empty doctor's surgery: a desk with a stethoscope and a thermometer on it, an examination couch with clean paper, a plant, a sunny window, a blank wall chart, a glass of water and a small medicine bottle on a side table.
No people at all - no doctor, no nurse, no patients, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, warm reassuring colours, kid-safe. Absolutely no text, no letters, no numbers, no medical writing anywhere.
Output size: 2048 x 1365 px.
```

### Л7.2 · Что в кабинете врача — 6 карточек (3×2)
```
A sheet of six separate cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell one object on pure white:
1) a stethoscope; 2) a thermometer; 3) a roll of bandage with two sticking plasters; 4) a bottle of medicine with a measuring spoon; 5) an open first-aid box with plasters and a bandage inside; 6) a glass of water and a small jug on a bedside table.
No people at all - no humans, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light, friendly and not clinical. Absolutely no text, no letters, no numbers, no labels on the bottle, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л7.3 · Прошедшее время: следы действий — 6 карточек (3×2)
```
A sheet of six separate cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters. Each cell shows the traces of a finished action, with nobody in the picture:
1) ate - an empty plate with crumbs and a fork laid across it; 2) drank - an empty glass with one last drop inside; 3) woke up - a rumpled bed with the covers thrown back and morning light on it; 4) went - footprints leading away along a sandy path; 5) came - a coat and a school bag just dropped by the front door with a wet umbrella beside them; 6) felt better - a thermometer put away in its case, curtains opened wide, an empty medicine spoon on a clean plate.
No people at all - no humans, no hands, no faces anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л7.4 · Здоровые и нездоровые привычки — 6 карточек (3×2)
```
A sheet of six separate cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters. The top row shows healthy habits, the bottom row unhealthy ones, all shown through objects with nobody in the picture:
1) swimming goggles and a swimming cap on the edge of a pool; 2) plain unbranded trainers and a school backpack on a sunny path; 3) a picnic of fruit, sandwiches and two glasses of water on a blanket;
4) a dark room with a glowing blank screen, an empty snack bowl and a clock face without numbers showing late; 5) a bed at night with a phone glowing face-up on the pillow and a dark window; 6) a lunch plate holding only three ice creams.
No people at all - no humans, no hands, no faces anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, kid-safe, nothing shaming. Absolutely no text, no letters, no numbers, no brand marks, no screen content anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

---

# UNIT 8 · COUNTRIES — 10 листов

### Л8.1 · Обложка юнита (сцена)
```
A travel desk seen from above: an open atlas with blank pages, a globe, a camera, a small suitcase covered in picture-only travel stickers, a pair of sunglasses, a paper aeroplane.
No people at all - no humans, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, one single scene. Absolutely no text, no letters, no numbers, no country names, no writing on the atlas or stickers anywhere.
Output size: 2048 x 1365 px.
```

### Л8.2 · Страны, часть 1 — 6 карточек (3×2)
```
A sheet of six separate country cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell on pure white. Each cell shows the recognisable silhouette shape of one country in one flat bright colour, with one or two iconic 3D symbols standing on top of it:
1) Egypt with pyramids and a camel; 2) Chile - long and narrow - with an Andes peak and a stone head statue; 3) Mexico with a cactus, a sombrero and a step pyramid; 4) China with a segment of great wall and a panda; 5) Spain with a guitar, a sun and a folding fan; 6) India with a domed white palace and an elephant.
No people at all anywhere; the animals are fine.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no country names, no writing anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л8.3 · Страны, часть 2 — 4 карточки (2×2)
```
A sheet of four separate country cards in a clean 2x2 grid, equal cells separated by thin light-grey gutters, each cell on pure white. Each cell shows the recognisable silhouette shape of one country in one flat bright colour, with one or two iconic 3D symbols standing on top of it:
1) Argentina with a football and a pair of tango shoes; 2) Australia with a kangaroo and white shell-shaped roofs; 3) Brazil with a rainforest tree and a football; 4) Turkey with a domed mosque silhouette and hot-air balloons over rock spires.
No people at all anywhere; the kangaroo is fine.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no country names anywhere.
Output size: 2048 x 2048 px.
```

### Л8.4 · Флаги, часть 1 — 6 карточек (3×2)
```
A sheet of six separate flag cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell one national flag on pure white, gently waving, accurate colours and accurate proportions, clean crisp vector-like rendering, nothing else in the cell. In this order:
1) Egypt; 2) Argentina; 3) Chile; 4) Mexico; 5) Spain; 6) China.
No people anywhere. Absolutely no text, no letters, no numbers, no country names, no captions anywhere - flag emblems only where the real flag has them.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л8.5 · Флаги, часть 2 — 4 карточки (2×2)
```
A sheet of four separate flag cards in a clean 2x2 grid, equal cells separated by thin light-grey gutters, each cell one national flag on pure white, gently waving, accurate colours and accurate proportions, clean crisp vector-like rendering, nothing else in the cell. In this order:
1) India; 2) Turkey; 3) Brazil; 4) Australia.
No people anywhere. Absolutely no text, no letters, no numbers, no country names, no captions anywhere - flag emblems only where the real flag has them, and the Brazilian banner must carry no words.
Output size: 2048 x 2048 px.
```
> Флаги генераторы искажают чаще всего. Если с 2–3 попыток не выходит точно — брать готовые SVG.

### Л8.6 · Достопримечательности, часть 1 — 6 карточек (3×2)
```
A sheet of six separate landmark cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell one famous landmark on pure white in three-quarter view:
1) the Great Wall of China winding over hills; 2) the Taj Mahal; 3) the Great Sphinx with a pyramid behind it; 4) the Amazon river winding through rainforest; 5) the Sydney Opera House; 6) a big football stadium seen from outside.
No people at all - no tourists, no figures for scale anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, soft even light, recognisable silhouettes. Absolutely no text, no letters, no numbers, no place names anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л8.7 · Достопримечательности, часть 2 — 2 карточки (2×1)
```
A two-panel strip in one horizontal row, equal panels separated by a thin light-grey gutter, each panel one landmark on pure white:
1) the Easter Island moai statues on a grassy slope; 2) the Great Pyramid of Giza with a camel standing beside it for scale.
No people at all - no tourists, no figures anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no place names anywhere.
Output size: 2048 x 1024 px.
```

### Л8.8 · Чудеса света, часть 1 — 6 карточек (3×2)
```
A sheet of six separate wonder cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell one natural wonder on pure white:
1) the Grand Canyon - a layered red canyon with a river below; 2) the harbour of Rio de Janeiro - a bay with islands, beaches and green peaks; 3) the Northern Lights - green and violet aurora over snow and pines; 4) Mount Everest - a snow peak with a plume of cloud; 5) the Great Barrier Reef seen from above - reef patterns in turquoise water; 6) Victoria Falls - a huge waterfall with mist and a rainbow.
No people at all anywhere.
Bright 3D-rendered cartoon style with a touch of realism, Pixar-like lighting, vivid saturated colours. Absolutely no text, no letters, no numbers, no place names anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л8.9 · Компас и карта — 2 карточки (2×1)
```
A two-panel strip in one horizontal row, equal panels separated by a thin light-grey gutter, both objects on pure white:
1) an old brass compass lying open on a blank parchment map with no writing on it; 2) a small suitcase with picture-only travel stickers and a camera beside it.
No people at all anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no compass letters, no map writing anywhere.
Output size: 2048 x 1024 px.
```

### Л8.10 · Машина времени (сцена)
```
A friendly cartoon time machine standing alone in a garden: a round glass capsule with copper pipes, levers and a big dial with plain ticks and no numbers, the door standing open, a faint glow inside.
No people at all - no traveller, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no dial numbers anywhere.
Output size: 2048 x 1365 px.
```

---

# UNIT 9 · WEATHER / BE GOING TO — 10 листов

### Л9.1 · Обложка юнита (сцена)
```
A window seen from inside a cosy empty room: heavy rain running down the glass, a thunderstorm with a lightning bolt outside, an umbrella and a pair of yellow rubber boots by the door inside, a warm lamp and a mug on the sill.
No people at all - no humans, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, cosy warm interior against a cool stormy exterior, vivid saturated colours. Absolutely no text, no letters, no numbers anywhere.
Output size: 2048 x 1365 px.
```

### Л9.2 · Погода — 6 карточек (3×2)
```
A sheet of six separate weather cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell one clear weather type on pure white:
1) a thunderstorm - a dark cloud with heavy rain and a lightning bolt over a small house; 2) rainy - a grey cloud with heavy rain and puddles below; 3) cloudy - thick grey and white clouds with no sun; 4) windy - a bent tree with leaves and a kite flying sideways; 5) foggy - a road and trees half-hidden in thick fog; 6) sunny - a bright sun in a clear blue sky.
No people at all anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no temperature figures anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л9.3 · Молния и одежда — 4 карточки (2×2)
```
A sheet of four separate cards in a clean 2x2 grid, equal cells separated by thin light-grey gutters, each cell one item on pure white:
1) a single white-yellow lightning bolt on a dark cloud; 2) a pair of yellow rubber boots; 3) a bright yellow child's raincoat with a hood, hanging on a hook; 4) an open red umbrella.
No people at all - nobody wearing the coat or the boots anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no brand marks anywhere.
Output size: 2048 x 2048 px.
```

### Л9.4 · Планы на неделю — 6 карточек (3×2)
```
A sheet of six separate cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell showing the objects of one activity with nobody doing it:
1) sleep - a made bed with a pillow and an alarm clock without numbers; 2) watch TV - a sofa facing a television with a completely blank screen, a remote on the cushion; 3) cook food - a pot on a cooker with a wooden spoon and chopped vegetables; 4) play tennis - a tennis racket and a ball on a court; 5) fly a kite - a kite in the sky above an empty grassy field with the string running down to a spool on the grass; 6) ride a horse - a saddled pony standing by a fence.
No people at all - no humans, no hands, no riders anywhere; the pony is fine.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no screen content anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л9.5 · be going to — 6 карточек (3×2)
```
A sheet of six separate cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters. Each cell shows a plan about to happen, told only through objects, with nobody in the picture:
1) a car in a showroom with a big ribbon bow on it; 2) a cat carrier and a dog lead waiting by a vet's door; 3) an open piano with the lid up and a stool pulled out, a music stand with blank paper; 4) a phone with a blank screen on a table and a pizza box arriving on a doorstep; 5) a sofa with a remote on the cushion in front of a blank television; 6) rubber boots and an umbrella by the front door with rain falling outside the glass.
No people at all - no humans, no hands anywhere; the cat and dog are fine.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, clear intention in every cell. Absolutely no text, no letters, no numbers, no screen content, no logos anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л9.6 · Отдых 100 лет назад, часть 1 — 6 карточек (3×2)
```
A sheet of six separate cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell one item on pure white in a vintage early-1900s seaside style with slightly muted sepia-tinted colours:
1) a striped Punch-and-Judy style puppet booth with two puppets on the rail; 2) a donkey with a saddle standing on sand; 3) a small steam locomotive with a plume of smoke; 4) old-fashioned lace-up bathing boots; 5) a hand ice-cream cart with a striped awning; 6) a wicker picnic basket with sandwiches, a bottle and fruit.
No people at all - no bathers, no vendors, no hands anywhere; the donkey and the puppets are fine.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, soft even light. Absolutely no text, no letters, no numbers, no signs on the booth or the cart anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### Л9.7 · Отдых: тогда и сейчас — 3 карточки (3×1)
```
A three-panel strip in one horizontal row, equal panels separated by thin light-grey gutters, each panel one item on pure white:
1) a crowded old-fashioned beach full of striped bathing tents and parasols, seen from a distance so no figures are needed; 2) a modern electric train in bright colours; 3) a modern pair of flip-flops.
No people at all - no bathers, no figures anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, soft even light, panel 1 slightly sepia-tinted and panels 2-3 brightly modern. Absolutely no text, no letters, no numbers, no signs anywhere.
Output size: 2048 x 683 px.
```

### Л9.8 · Прогноз погоды на неделю (сцена)
```
A television weather board showing seven equal vertical columns, each column containing one big weather icon only and nothing else, in this order from left to right: rainy, sunny, cloudy, windy, cloudy, rainy, sunny. A clean empty studio around it.
No people at all - no presenter, no hands, no pointer held by anyone anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, clean studio look. Absolutely no text, no letters, no numbers, no day names, no temperatures anywhere - the days must be readable only from the position of the icons.
Output size: 2048 x 1365 px.
```

### Л9.9 · Кемпинг в грозу (сцена)
```
A small tent alone in a field at night in heavy rain, a big lightning bolt in the dark sky, a torch lying lit at the tent flap. There is no umbrella, no raincoat and no boots anywhere in the scene.
No people at all - nobody in or near the tent, no silhouette inside it.
Bright 3D-rendered cartoon style, Pixar-like, dramatic but kid-safe lighting, vivid colours against the dark. Absolutely no text, no letters, no numbers anywhere.
Output size: 2048 x 1365 px.
```

### Л9.10 · Speaking: планы на каникулы (сцена)
```
A holiday plans collage laid out flat on a table: a snorkel and mask, an open book in a hammock, a bicycle helmet, a wrapped present for grandparents, a kite, an ice cream in a cone, a suitcase in the middle - each item clearly separate and easy to name.
No people at all - no humans, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, clean flat-lay composition. Absolutely no text, no letters, no numbers anywhere.
Output size: 2048 x 1365 px.
```

---

# FINAL TEST — 6 листов

### ЛФ.1 · Обложка (сцена)
```
A festive empty school hall at the end of the year: balloons and confetti in the air, a table with medals and a small trophy on it, a big banner stretched across the wall that is completely blank and empty.
No people at all - no children, no teachers, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, festive, vivid saturated colours. Absolutely no text, no letters, no numbers, no writing on the banner or the medals anywhere.
Output size: 2048 x 1365 px.
```

### ЛФ.2 · Дни недели: занятия — 6 карточек (3×2)
```
A sheet of six separate cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell showing the objects of one activity on pure white, with nobody doing it:
1) swimming goggles and a swimming cap by a pool; 2) a guitar leaning on a stool; 3) a bicycle with a helmet hanging on the handlebar; 4) a shopping basket full of groceries; 5) a football and boots on grass; 6) a cake, a mixing bowl and a whisk on a kitchen worktop.
No people at all - no humans, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### ЛФ.3 · Аудирование: варианты ответов, часть 1 — 9 карточек (3×3)
```
A sheet of nine separate answer cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell one simple unambiguous object or place on pure white. Row by row, left to right:
Row 1 - a tennis racket with a ball / a football with boots / swimming goggles with a swimming cap.
Row 2 - a yellow school bus / a bicycle with a backpack hanging on it / a pair of walking shoes on a pavement.
Row 3 - an empty kitchen / an empty garden with a swing / an empty bedroom with a made bed.
No people at all - no humans, no children, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### ЛФ.4 · Аудирование: варианты ответов, часть 2 — 9 карточек (3×3)
```
A sheet of nine separate answer cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell one simple unambiguous object on pure white. Row by row, left to right:
Row 1 - a birthday cake with eight candles / a birthday cake with nine candles / a birthday cake with ten candles.
Row 2 - a bicycle with a ribbon bow / a games console with a ribbon bow / a puppy with a ribbon bow.
Row 3 - a bowl of soup / a bowl of salad / a bowl of fruit.
No people at all - no humans, no hands anywhere; the puppy is fine. The candles must be clearly countable.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### ЛФ.5 · Карточки-загадки, часть 1 — 6 картинок (3×2)
```
A sheet of six separate cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell one clear object or place on pure white:
1) a wedge of cheese with a cheese sandwich behind it; 2) a friendly simple cartoon drawing of a stomach organ on its own, with a sandwich and a glass shown going down into it from above; 3) a cup of brown coffee with a small milk jug; 4) a cinema hall with rows of red seats and a blank screen; 5) a dolphin jumping through a hoop of water; 6) a hot bowl of soup with vegetables and meat.
No people at all - no humans, no bodies, no hands, no faces anywhere; cell 2 shows the organ alone, not a person.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, friendly and not clinical. Absolutely no text, no letters, no numbers, no labels anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```

### ЛФ.6 · Карточки-загадки, часть 2 — 2 картинки (2×1)
```
A two-panel strip in one horizontal row, equal panels separated by a thin light-grey gutter, each panel one place on pure white:
1) open lift doors between two floors with a blank call panel; 2) a supermarket aisle with a trolley standing in it.
No people at all - no shoppers, no hands anywhere.
Bright 3D-rendered cartoon style, Pixar-like, vivid saturated colours, soft even light. Absolutely no text, no letters, no numbers, no floor numbers, no shelf labels anywhere.
Output size: 2048 x 1024 px.
```

---

# Сводка

| Юнит | Листов |
|---|---|
| Unit 1 School | 9 |
| Unit 2 Food | 12 |
| Unit 3 Home / Time / Jobs | 9 |
| Unit 4 Town | 10 |
| Unit 5 Sea | 8 |
| Unit 6 Gadgets | 11 |
| Unit 7 Health | 4 |
| Unit 8 Countries | 10 |
| Unit 9 Weather | 10 |
| Final Test | 6 |
| **Итого** | **89** |

## Порядок запуска

1. **Л1.3** (have to, 3×2) — пробный: это первый предметный лист вместо людей,
   на нём видно, читается ли «долг» без человека. Не читается — значит эти
   шесть карточек тоже уходят в книгу.
2. Дальше юниты в любом порядке: сквозных героев нет, согласовывать листы
   между собой не нужно.
3. Флаги (Л8.4, Л8.5) — если с 2–3 попыток не точно, берём SVG.
4. Циферблаты (Л3.4, Л3.5) — надёжнее сгенерировать кодом (SVG).
