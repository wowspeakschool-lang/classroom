# Go Getter 2 — ЛИСТЫ ПРОМПТОВ НА КАРТИНКИ

Собирается из `tools/gg2_sheets.py` — **правится там**, не здесь.

Один промпт = один лист. Генерирует Анна, присылает в чат с подписью номера
листа («Лист 7»). Номера сквозные на GG2 и GG3: у GG2 листы 1–60, у GG3
дальше (`docs/GG3_листы_промптов.md`). Номер не переиспользуется.

Каждый промпт самодостаточный: сетка, порядок ячеек по рядам, стиль, запрет
текста и размер уже внутри — копируется целиком.

Стиль тот же, что у GG1: предметы — реалистичный 3D, животные — мультяшный
глянец, места и люди — 3D-мультяшные (Pixar-like), люди стилизованные, не фото.
Людей рисуем (решение Анны 05.10.2026); на листах без людей это прописано в
промпте.

## Чего не генерируем

| Что | Откуда |
|---|---|
| Кадры учебника: Anna, Max, Hammy, Carla, Rocco, Big Al, Mrs Dee, Billy и Patti, карты, билеты, постеры, таблицы | вырезаются из PDF выгрузки — по ним сверяются ответы |
| Карточки методиста с текстом (правила, тексты для чтения) | переносим текстом |
| Приветствия, похвалы, прощания | `media/shared/` |
| Фото реальных людей, Микки Маус, Гарфилд, Angry Birds, Стич | не берём — вместо них листы «Герои» |


**Листы 1–60: всего 60, картинок 356.**


---

# UNIT 0 — листов: 2

### Лист 1 · Комната подростка — одна картинка, сцены с персонажами
Тест Unit 0, SPEAKING I. Вопросы остаются как в выгрузке: Where is the boy? Where is his bag? What has he got on his shelves? Can the boy play the guitar?
```
One single picture filling the frame: a cosy teenager's bedroom. A boy of about thirteen sits on his bed playing a small guitar. A mobile phone lies on the bed beside him. Next to the bed stands a tall bookshelf with books and a green plant in a pot. A dartboard and two colourful picture posters hang on the wall. A yellow school backpack lies on the floor next to the bookshelf.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, landscape.
```

### Лист 2 · Слова теста Unit 0 — 6 карт., сетка 3×2, предметы, реалистичный 3D
По желанию: картинки-подсказки к блоку 1 теста (впиши слово).
```
A sheet of 6 separate picture cards arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a skateboard with colourful wheels; a soft cosy armchair; a wooden wardrobe for clothes with two doors.
Row 2, left to right: three wooden wall shelves with books and a small plant; an open sketchbook with a drawing of a house and a tree, colour pencils beside it; a wall calendar page with a snowflake picture on top and a plain grid of empty day squares.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```


---

# UNIT 1 — листов: 9

### Лист 3 · Школьные предметы — 9 карт., сетка 3×3, предметы, реалистичный 3D
Словарь Homework 1, тест. Каждый предмет — набором вещей.
```
A sheet of 9 separate picture cards arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a paint palette with brushes and paint tubes; a computer monitor with a keyboard and a mouse; a stack of school books with a small British flag on a stand.
Row 2, left to right: a school book, a small Eiffel Tower souvenir and a small French flag on a stand; a globe and a folded paper map; an old paper scroll, a sand timer and a small ancient stone column.
Row 3, left to right: a calculator with blank buttons, a ruler and a set square; an acoustic guitar with a small keyboard and floating music notes; a football, a basketball, a pair of trainers and a whistle.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 4 · Наука и школьные вещи — 9 карт., сетка 3×3, предметы, реалистичный 3D
Science + школьные принадлежности (Homework 1, 7, тест).
```
A sheet of 9 separate picture cards arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a glass flask with green liquid, a microscope and a horseshoe magnet; a pocket calculator with blank buttons; a thick hardcover dictionary.
Row 2, left to right: an open laptop; an unfolded world map; a box of watercolour paints with a brush.
Row 3, left to right: a zipped pencil case; a rubber eraser; a plastic ruler with plain tick marks.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 5 · Вещи, обед, дорога — 9 карт., сетка 3×3, предметы, реалистичный 3D
Школьные вещи (Homework 1) и еда / дорога в школу (Homework 2, 5, 7).
```
A sheet of 9 separate picture cards arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a pair of scissors with rounded tips; a pair of trainers; a school backpack.
Row 2, left to right: a yellow pencil with a pink eraser tip; chicken and chips on a plate; fish and chips in a paper cone.
Row 3, left to right: an open lunch box with a sandwich, an apple and a carton of juice; a yellow school bus; a flat TV on a stand.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 6 · Места в школе — 9 карт., сетка 3×3, места и сцены, без людей
Словарь Homework 5. Без людей.
```
A sheet of 9 separate illustrations arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a school canteen with a serving counter, trays and tables; a classroom with desks, chairs and a board; a computer room with rows of computers.
Row 2, left to right: a school gym with climbing bars, mats and a basketball hoop; a school hall with a row of lockers along the wall; a school library with tall bookshelves and a reading table.
Row 3, left to right: a school playground with a slide, swings and a hopscotch court; a staff room with a big table, piles of exercise books and coffee mugs; a modern school building with a big basketball court in front.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 7 · Хобби — 9 карт., сетка 3×3, предметы, реалистичный 3D
Homework 3–7: do ballet, play chess… Каждое хобби — набором вещей.
```
A sheet of 9 separate picture cards arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: ballet pointe shoes and a pink tutu; a white karate kimono with a black belt; a pottery wheel with a clay pot.
Row 2, left to right: a basketball hoop and a basketball; a chessboard with chess pieces; a football in front of a small goal.
Row 3, left to right: a tennis racket and a tennis ball; an easel with a painting of flowers; big headphones and a small music player.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 8 · Стив и его школа — 9 карт., сетка 3×3, сцены с персонажами
Homework 5 (2): картинки к «верно/неверно» про Стива; последняя — Лили (Homework 6). Вместо фото детей.
```
A sheet of 9 separate illustrations arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: Steve, a cheerful eleven-year-old boy with red hair and a green school jumper, standing in front of his school; Steve hurrying through the classroom door, a round wall clock above the door; Steve at the board in a maths lesson, the board covered with simple sums.
Row 2, left to right: Steve at an easel in an art lesson, looking bored; Steve carrying a lunch tray in the school canteen; Steve running happily in a P.E. lesson in the school gym.
Row 3, left to right: Steve playing basketball with his classmates; two children playing tennis on a tennis court; Lily, a girl of eleven with a backpack, waiting at a bus stop with two friends.
Steve is the same boy in cells 1-7: red hair, green school jumper.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 9 · Марк, интервью — 6 карт., сетка 3×2, сцены с персонажами
Homework 6: Марк и «верно/неверно»; Homework 4: интервью. Вместо фото.
```
A sheet of 6 separate illustrations arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: Mark, a smiling boy of eleven with dark curly hair and a blue hoodie; a history lesson: pupils at their desks, a teacher pointing at a picture of a castle; Mark doing a science experiment with colourful flasks.
Row 2, left to right: children playing football in a school yard; Mark playing chess at a table; a young woman reporter with a microphone interviewing a man on a city street.
Mark is the same boy in cells 1, 3 and 5: dark curly hair, blue hoodie.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 10 · Клуб, балет, дорога в школу — 4 карт., сетка 2×2, сцены с персонажами
Homework 4 (Карен в шахматном клубе), Homework 7 (составь предложение).
```
A sheet of 4 separate illustrations arranged in a clean grid of two columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a girl of eleven talking to a friendly male teacher at a chess club table with chessboards; a girl doing ballet in a dance studio.
Row 2, left to right: a boy with a backpack walking to school along a path; a group of children playing football on a green field in the morning.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 11 · Школьная столовая — одна картинка, сцены с персонажами
Тест Unit 1, SPEAKING I. Вопросы остаются: Where are the students? How many students can you see?…
```
One single picture filling the frame: two friendly school students in school uniforms, a boy and a girl, sitting at a table in a bright school canteen and smiling. On the table: a tray with apples, bananas and oranges, two sandwiches, a glass of orange juice and a bottle of water. A serving counter with food in the background.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, landscape.
```


---

# UNIT 2 — листов: 7

### Лист 12 · Еда 1 — 9 карт., сетка 3×3, предметы, реалистичный 3D
Словарь Homework 1.
```
A sheet of 9 separate picture cards arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a red apple; a small pile of round biscuits; a loaf of bread.
Row 2, left to right: a bowl of breakfast cereal with milk; a wedge of yellow cheese; a roast chicken on a plate.
Row 3, left to right: a portion of chips; a whole fish on a plate with a lemon slice; a bowl of mixed fruit.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 13 · Еда 2 — 9 карт., сетка 3×3, предметы, реалистичный 3D
Словарь Homework 1.
```
A sheet of 9 separate picture cards arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: slices of ham on a small board; a raw steak on a board; a glass of orange juice with an orange beside it.
Row 2, left to right: a stack of pancakes; a plate of spaghetti with tomato sauce; two potatoes.
Row 3, left to right: a bowl of white rice; a bowl of green salad; a sandwich cut in half.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 14 · Еда 3 и блюда — 9 карт., сетка 3×3, предметы, реалистичный 3D
Словарь Homework 1; три блюда Сьюзи — Homework 5.
```
A sheet of 9 separate picture cards arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: two sausages; a red tomato; an open tin of tuna.
Row 2, left to right: a pile of fresh vegetables; a bottle of water and a glass of water; a small pot of yoghurt with a spoon.
Row 3, left to right: an English breakfast on a plate: sausages, two fried eggs, a grilled tomato and beans; fish and chips on a plate; chicken and rice on a plate.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 15 · Еда 4 — 9 карт., сетка 3×3, предметы, реалистичный 3D
Словарь Homework 2.
```
A sheet of 9 separate picture cards arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a block of butter on a dish; a bar of chocolate, partly unwrapped; two eggs.
Row 2, left to right: a paper bag of flour with a little flour spilled; a lemon; a glass of milk and a milk carton.
Row 3, left to right: three strawberries; a sugar bowl with sugar cubes; a bunch of bananas.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 16 · Ёмкости — 6 карт., сетка 3×2, предметы, реалистичный 3D
Словарь Homework 3, Homework 7.
```
A sheet of 6 separate picture cards arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a bar of chocolate; a bottle of water; a can of cola with plain colours.
Row 2, left to right: a carton of juice; a jar of strawberry jam; a packet of biscuits.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 17 · Герои Unit 2 — 9 карт., сетка 3×3, сцены с персонажами
Вместо фото людей: Макс (Homework 1), Аня (Homework 2), Том и Мэтт (Homework 2), кафе (Homework 4), Сьюзи (Homework 5), Пенни с папой (Homework 6), хот-доги и тосты (Homework 7).
```
A sheet of 9 separate illustrations arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: Max, a boy of eleven, eating a red apple; Anya, a girl of twelve in an apron, holding a plate of pancakes with banana and cream; two young men, Tom and Matt, sitting on a sofa and writing a shopping list.
Row 2, left to right: a waiter taking an order from two girls at a café table with menus; Susie, a smiling British girl of twelve, holding a plate of fish and chips; Penny, a girl of ten, and her dad at the kitchen table at breakfast: an egg, bread with ham and a glass of milk.
Row 3, left to right: a girl buying a hot dog from a friendly man at a hot dog cart in a park; French toast on a plate next to a toaster; three plates in a row on a table: breakfast with cereal, lunch with soup and a sandwich, dinner with chicken and rice.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 18 · Семейный завтрак — одна картинка, сцены с персонажами
Тест Unit 2, SPEAKING I. Вопросы остаются: How many people…? What food can you see? Is there any cheese?
```
One single picture filling the frame: a family of four having breakfast at a kitchen table in the morning: mum, dad, a girl and a boy. On the table: bread, a plate of cheese, eggs, butter, a bowl of fruit, a jug of orange juice, a carton of milk and cups of tea.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, landscape.
```


---

# UNIT 3 — листов: 9

### Лист 19 · Гаджеты 1 — 6 карт., сетка 3×2, предметы, реалистичный 3D
Словарь Homework 1, тест.
```
A sheet of 6 separate picture cards arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a smartphone; a desktop computer: a monitor and a computer tower; an open laptop.
Row 2, left to right: a digital camera; a tablet; a flat TV.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 20 · Гаджеты 2 — 6 карт., сетка 3×2, предметы, реалистичный 3D
Словарь Homework 1, тест.
```
A sheet of 6 separate picture cards arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a pair of headphones; a computer keyboard; a computer mouse.
Row 2, left to right: a printer with a sheet of paper; a computer screen with a bright colourful picture; a pair of speakers.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 21 · Что делаем с гаджетами — 9 карт., сетка 3×3, персонажи на белом
Словарь Homework 1 (2); последние две — Джек (Homework 1) и Сара (Homework 2).
```
A sheet of 9 separate picture cards arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a boy chatting online on a laptop, chat bubbles on the screen; a girl downloading a song on her phone, a music note and a download arrow above the phone; a girl sending an email from a laptop, an envelope flying out of the screen.
Row 2, left to right: a boy surfing the Internet on a tablet with colourful pictures on the screen; a girl taking a selfie with her phone, smiling; a boy talking on the phone.
Row 3, left to right: a girl texting a friend, message bubbles above the phone; Jack, a little boy in a yellow hat, holding a phone with a laptop and headphones beside him; Sarah, a girl in a yellow jumper, checking her phone in the morning, sitting on her bed.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 22 · Эмоции — 9 карт., сетка 3×3, персонажи на белом
Homework 3: соедини эмоцию с картинкой; две последние — к открытым вопросам 18 и 19.
```
A sheet of 9 separate picture cards arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a worried boy with wide-open eyes and a slightly open mouth; an angry red-haired girl with frowning eyebrows; a happy girl with pigtails, smiling broadly.
Row 2, left to right: a tired girl yawning; a scared boy hiding behind his hands; a sad boy with a tear on his cheek.
Row 3, left to right: a bored girl resting her chin on her hand; a group of bored teenage students sitting in a lecture hall; a worried woman holding her head with both hands.
Every person is shown head and shoulders, facing the viewer, the emotion is very clear.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 23 · Зверята: что они делают — 9 карт., сетка 3×3, мультяшный глянец
Homework 2: соедини действие с персонажем, составь предложение.
```
A sheet of 9 separate picture cards arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a cat sitting; a fox running; a rabbit and a hedgehog eating at a little table.
Row 2, left to right: a bear cub and a puppy reading a book together; a bunny dancing; a puppy sitting on a chair looking at a phone.
Row 3, left to right: two kittens crying; a bear and a panda walking side by side; two pandas sitting on the floor next to a mop and a bucket, not cleaning.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 24 · Зверята: эмоции — 2 карт., сетка 2×1, мультяшный глянец
Homework 3, открытые вопросы 15–16.
```
A sheet of 2 separate picture cards arranged in a clean grid of two columns and one row, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a tired cat stretched out on a sofa; an angry little blue songbird with ruffled feathers, frowning and stamping its foot, an ordinary bird, not resembling any famous cartoon or game character.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1024 px, each cell at least 600 px.
```

### Лист 25 · Герои Unit 3 — 6 карт., сетка 3×2, сцены с персонажами
Вместо фото: селфи (Homework 1, 2), Гарри и Лили (Homework 6), звонок (Homework 4), изобретатель (Homework 5), видеозвонок (тест).
```
A sheet of 6 separate illustrations arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: three teenagers taking a selfie together in a park; Harry, a boy of twelve with curly hair, holding a tablet; Lily, a girl of twelve with a bob haircut, holding a phone.
Row 2, left to right: a boy and a girl talking to each other on the phone, each in their own room; a boy building an electronic gadget at a desk with a laptop and headphones; a girl on a video call on a laptop, her grandparents waving on the screen.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 26 · У бассейна — одна картинка, сцены с персонажами
Homework 2, задание 17: три предложения «да» и три «нет» по картинке.
```
One single picture filling the frame: a busy outdoor swimming pool on a sunny day: a boy and a girl jumping into the water, a woman reading on a sun lounger, a man eating an ice cream, two children playing with a ball, a dog sleeping in the shade and a cat watching the birds.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, landscape.
```

### Лист 27 · Завтрак с гаджетами — одна картинка, сцены с персонажами
Тест Unit 3, SPEAKING I. Вопросы остаются: What is each person doing? Who is using headphones?
```
One single picture filling the frame: a family of four at the breakfast table, everybody busy with a gadget: a girl with a tablet, mum looking at her phone, a teenage boy with headphones and a phone, dad typing on a laptop.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, landscape.
```


---

# UNIT 4 — листов: 8

### Лист 28 · Природа 1 — 6 карт., сетка 3×2, места и сцены, без людей
Словарь Homework 1, тест.
```
A sheet of 6 separate illustrations arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a sandy beach with the sea; a desert with sand dunes; a green forest.
Row 2, left to right: a small green island in the sea; a calm lake among hills; a tall mountain with a snowy top.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 29 · Природа 2 — 6 карт., сетка 3×2, места и сцены, без людей
Словарь Homework 1, тест.
```
A sheet of 6 separate illustrations arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a river flowing through a valley; the open sea with waves; a volcano with smoke coming out.
Row 2, left to right: a waterfall; a big city with tall buildings; a small town with houses and a church.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 30 · Какое? Цена, риск, высота — 6 карт., сетка 3×2, предметы, реалистичный 3D
Словарь Homework 2.
```
A sheet of 6 separate picture cards arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a single small coin next to a simple paper price tag; a sparkling diamond ring next to a gold price tag; a shark fin in the water next to a red warning triangle.
Row 2, left to right: a bicycle helmet, knee pads and elbow pads; a very tall thin tower; a very low little garden fence.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 31 · Какое? Трудность, интерес — 4 карт., сетка 2×2, предметы, реалистичный 3D
Словарь Homework 2.
```
A sheet of 4 separate picture cards arranged in a clean grid of two columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a puzzle of just two big pieces; a huge complicated puzzle with hundreds of tiny pieces.
Row 2, left to right: a roller coaster with a big loop; a grey rainy window with a ticking clock and a pile of grey papers on the sill.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 32 · Какой? Животные — 9 карт., сетка 3×3, мультяшный глянец
Словарь Homework 3; тигр — Homework 3, задание 8.
```
A sheet of 9 separate picture cards arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a beautiful butterfly on a flower; a cheetah running fast; a friendly puppy wagging its tail.
Row 2, left to right: a funny monkey pulling a face; an owl in glasses reading a book; an ant carrying a huge crumb.
Row 3, left to right: a bear sharing a pot of honey with a little rabbit; a tiger looking back over its shoulder; a slow tortoise.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 33 · Спорт на природе — 6 карт., сетка 3×2, предметы, реалистичный 3D
Homework 7 (1), задание 23.
```
A sheet of 6 separate picture cards arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a kayak and a paddle; a climbing rope, carabiners and a helmet next to a rock; an open parachute in the sky.
Row 2, left to right: a sailing boat; a fishing rod with a float; a mountain bike.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 34 · Герои Unit 4 — 9 карт., сетка 3×3, сцены с персонажами
Вместо фото: Платон (Homework 1), Джейк и Майкл (Homework 2), Зак и Ленни (Homework 6), Дэн (Homework 7), сцены отдыха (Homework 7 (1), задания 19–21), кино (Homework 4).
```
A sheet of 9 separate illustrations arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: Plato, a Greek boy of twelve, standing on a hill above a white island town by the blue sea; two teenage boys, Jake and Michael, in a kayak for two on a lake near a wooden jetty; two boys at a fast-food table: one eating a hamburger, the other eating pizza.
Row 2, left to right: a boy reading on a laptop at his desk, wearing headphones; two teenagers kayaking on a river; a girl cycling on a forest path.
Row 3, left to right: a family in a rowing boat on a lake; a group of friends watching a film at the cinema with popcorn; a family walking in the mountains with backpacks.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 35 · Три картины — одна картинка, места и сцены, без людей
Homework 3, задания 7, 10, 11: картины Рокко, Большого Эла и Карлы.
```
One single picture filling the frame: three framed paintings hanging side by side on a gallery wall, clearly different in size: on the left a medium painting of messy childish scribbles, in the middle a small painting of a funny cat, on the right the biggest painting of a neat landscape with mountains and a lake.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, landscape.
```


---

# UNIT 5 — листов: 7

### Лист 36 · Город 1 — 9 карт., сетка 3×3, места и сцены, без людей
Словарь Homework 1, тест. Узнаваемо без вывесок.
```
A sheet of 9 separate illustrations arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a bank building with columns and a cash machine; a small café with tables and umbrellas outside; a cinema building with a big poster frame and film reels decoration.
Row 2, left to right: a tall hotel with a revolving door and a luggage trolley outside; a hospital with an ambulance in front and a red cross on the wall; a library building with stone steps and big windows showing bookshelves.
Row 3, left to right: a museum with columns and a big dinosaur skeleton visible through the glass; a city park with trees, a pond and benches; a restaurant with tables laid with white tablecloths behind big windows.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 37 · Город 2 — 9 карт., сетка 3×3, места и сцены, без людей
Словарь Homework 1, тест.
```
A sheet of 9 separate illustrations arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a supermarket with shopping trolleys outside; a clothes shop with clothes on hangers in the window; a football stadium.
Row 2, left to right: a theatre with a red curtain visible through the open doors; a sports centre with a running track; an indoor swimming pool.
Row 3, left to right: a post office with a red post box in front; a police station with a police car in front and a blue lamp above the door; a train station with a train at the platform.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 38 · Город 3, дома и музей — 6 карт., сетка 3×2, места и сцены, без людей
Homework 5, 6.
```
A sheet of 6 separate illustrations arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a big modern shopping centre; a film studio with a big camera, lights and a set; a theme park with a big wheel and a roller coaster.
Row 2, left to right: a small house; a big house; a museum hall with a huge dinosaur skeleton.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 39 · Какой город — 6 карт., сетка 3×2, места и сцены, без людей
Homework 6, задание 4: пары прилагательных.
```
A sheet of 6 separate illustrations arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a busy street full of cars and buses; a quiet empty street with trees; a clean cinema hall with neat rows of red seats.
Row 2, left to right: a dirty cinema hall with popcorn and cups on the floor; an old stadium with broken seats; a shiny new stadium.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 40 · Город раньше и сейчас — 2 карт., сетка 2×1, места и сцены, без людей
Homework 6, задание 5: кадр учебника в выгрузке обрезан — вместо него. Один и тот же город.
```
A sheet of 2 separate illustrations arranged in a clean grid of two columns and one row, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a small town street a hundred years ago: old shops, horse carts and gas lamps; the same town street today: modern shops, cars, a bus stop and a café.
Both pictures show the same street from the same viewpoint.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1024 px, each cell at least 600 px.
```

### Лист 41 · Улица с кафе — одна картинка, сцены с персонажами
Тест Unit 5, SPEAKING I (вместо фото улицы с людьми).
```
One single picture filling the frame: an old European street on a sunny day: a café with tables outside where people are drinking coffee, a bakery, a small bookshop, a bicycle by a lamp post and flower boxes on the windows.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, landscape.
```

### Лист 42 · Где ты был — 3 карт., сетка 3×1, места и сцены, без людей
По желанию: Homework 3, задание 4.
```
A sheet of 3 separate illustrations arranged in a clean grid of three columns and one row, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a garden with flower beds; a small park with a bench; a kitchen.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1024 px, each cell at least 600 px.
```


---

# UNIT 6 — листов: 3

### Лист 43 · Профессии 1 — 9 карт., сетка 3×3, персонажи на белом
Словарь Homework 1, тест.
```
A sheet of 9 separate picture cards arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: an artist painting at an easel; a builder in a hard hat laying bricks; a bus driver at the wheel of a bus.
Row 2, left to right: a chef in a white hat stirring a pot; a doctor with a stethoscope; a farmer with a basket of eggs next to a tractor.
Row 3, left to right: a footballer kicking a ball; a nurse holding a thermometer and a bandage; an office worker at a desk with a computer.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 44 · Профессии 2 — 6 карт., сетка 3×2, персонажи на белом
Словарь Homework 1, тест.
```
A sheet of 6 separate picture cards arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a pilot in uniform in front of a plane; a police officer with a radio; a shop assistant at a till.
Row 2, left to right: a singer with a microphone; a teacher at a board with a globe on the desk; a vet examining a cat on a table.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 45 · Семья убирает дом — одна картинка, сцены с персонажами
Тест Unit 6, SPEAKING I. Вопросы остаются: How many people? What is each person doing?
```
One single picture filling the frame: a family cleaning their living room together: mum ironing, dad washing the window, a girl carrying a basket of washing, a boy picking up toys, and a cat watching from the sofa.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, landscape.
```


---

# UNIT 7 — листов: 8

### Лист 46 · Транспорт 1 — 6 карт., сетка 3×2, предметы, реалистичный 3D
Словарь Homework 1.
```
A sheet of 6 separate picture cards arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a car; a rowing boat with oars; a bicycle.
Row 2, left to right: a city bus; a motorbike; a passenger plane.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 47 · Транспорт 2 — 6 карт., сетка 3×2, предметы, реалистичный 3D
Словарь Homework 1.
```
A sheet of 6 separate picture cards arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a yellow taxi; a passenger train; a tram.
Row 2, left to right: an underground train in a tunnel; a lorry; a yellow school bus at a bus stop with its door open.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 48 · Как едем — 6 карт., сетка 3×2, сцены с персонажами
Словарь Homework 1 (2).
```
A sheet of 6 separate illustrations arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a train arriving at a station platform, people waiting; people getting on a bus through its open doors; people getting off a train onto the platform.
Row 2, left to right: a train leaving the station, a woman waving goodbye; a boy taking a bus at a bus stop; a girl walking to school on foot.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 49 · На каникулах — 6 карт., сетка 3×2, сцены с персонажами
Homework 3, 6.
```
A sheet of 6 separate illustrations arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a family eating pizza at a restaurant; a girl taking photos with a camera; children visiting a museum with a statue and paintings.
Row 2, left to right: a family with suitcases arriving at a hotel reception; a boy buying a souvenir at a stall with magnets and small towers; tourists with a map going sightseeing in front of an old tower.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 50 · Вещи в поездку — 6 карт., сетка 3×2, предметы, реалистичный 3D
Homework 2, 6. Телефон, планшет и фотоаппарат — с листов Unit 3.
```
A sheet of 6 separate picture cards arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a guidebook; a sun hat with flowers; a suitcase.
Row 2, left to right: a pair of socks; a passport; a pair of sunglasses.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 51 · Открытый чемодан — одна картинка, места и сцены, без людей
Homework 2, задание 17: что положили в чемодан.
```
One single picture filling the frame: an open suitcase on a bedroom floor with things scattered around it, every item clearly separate: a guidebook, a sun hat, a pair of socks, a camera, a passport, sunglasses, a toothbrush, a towel and a tube of sun cream.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, landscape.
```

### Лист 52 · Герои Unit 7 — 9 карт., сетка 3×3, сцены с персонажами
Вместо фото и обрезанных картинок: Homework 1 (Энзо), 2 (составь предложение), 6 (Пенни, фото на память, автобус).
```
A sheet of 9 separate illustrations arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a boy, Tim, eating pizza at a pizzeria; a dad drinking coffee in the kitchen; a girl, Tina, wearing a sun hat with flowers.
Row 2, left to right: a mum and her son Stan in a supermarket; Enzo, a fourteen-year-old boy, travelling on the underground in New York with his school bag; Penny, a girl of twelve, on a skateboard.
Row 3, left to right: a dad taking pictures of his two children on holiday by the sea; children getting off a school bus; mountain climbers with tents near a snowy mountain top.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 53 · В аэропорту — одна картинка, сцены с персонажами
Тест Unit 7, SPEAKING I. Вопросы остаются: Where are the people? What are they wearing? Plane or train?
```
One single picture filling the frame: a family of three - a dad, a mum and a child - standing at the big window of an airport with a suitcase, planes on the airfield outside.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, landscape.
```


---

# UNIT 8 — листов: 7

### Лист 54 · Мероприятия — 9 карт., сетка 3×3, места и сцены, без людей
Словарь Homework 1.
```
A sheet of 9 separate illustrations arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a barbecue grill with sausages and smoke in a garden; a birthday table with a cake with candles, balloons and presents; a concert stage with a microphone, lights and speakers.
Row 2, left to right: a dance show stage with a curtain and spotlights; a football stadium with a ball on the pitch; a rail of fancy dress costumes: a cape, a wizard hat, a mask and a crown.
Row 3, left to right: a picnic blanket on the grass with a basket and sandwiches; a theatre stage with a red curtain and a castle set; sleeping bags and pillows on a bedroom floor with a torch and fairy lights.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 55 · Что делают на празднике — 9 карт., сетка 3×3, сцены с персонажами
Словарь Homework 1 (2); последние две — Homework 1 (3).
```
A sheet of 9 separate illustrations arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a girl singing in a talent competition on a stage, judges holding up score cards; a boy cooking food in the kitchen; a girl getting presents at her birthday party.
Row 2, left to right: children singing Happy Birthday around a cake with candles; two children sleeping in sleeping bags on the floor; children taking part in a running competition.
Row 3, left to right: a boy wearing a superhero costume; three girls having a sleepover with pillows and popcorn; Anna, a smiling girl of twelve with long dark hair.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 56 · Планы: be going to — 9 карт., сетка 3×3, сцены с персонажами
Homework 2 (1), задания 5–13; Homework 3, задания 6 и 10.
```
A sheet of 9 separate illustrations arranged in a clean grid of three columns and three rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: a grandmother's cottage with a garden and a bench; blossoming cherry trees with Mount Fuji in the distance; a girl doing her homework at a desk in the evening.
Row 2, left to right: a half-painted pink bedroom wall with a paint roller and a bucket; a beach with a palm tree and a sun lounger; a cinema hall with red seats and popcorn.
Row 3, left to right: a boy reading a book on his bed; a girl carrying a big armful of clothes; a clothes shop window with dresses and jackets on hangers.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

### Лист 57 · Музыка — 6 карт., сетка 3×2, предметы, реалистичный 3D
Homework 3: вместо игры Wordwall «types of music» (состав мой).
```
A sheet of 6 separate picture cards arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: an electric guitar and an amplifier; a sparkly microphone with little stars; a violin with sheet music.
Row 2, left to right: one boombox with a baseball cap lying on top of it, both together as one single object; a shiny golden saxophone; a banjo and a cowboy hat.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 58 · Билеты и подарки — 6 карт., сетка 3×2, предметы, реалистичный 3D
Homework 3, 6.
```
A sheet of 6 separate picture cards arranged in a clean grid of three columns and two rows, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every item is complete and centred in its cell with a generous empty margin, not touching any other item or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: two concert tickets with a star picture; a bouquet of flowers with a heart-shaped card; bowling pins and a bowling ball.
Row 2, left to right: a restaurant table with plates, cutlery and a candle; two cinema tickets with a box of popcorn; a party invitation card decorated with balloons.
No people at all - no humans, no children, no hands, no faces, no silhouettes of people anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### Лист 59 · Забеги — 3 карт., сетка 3×1, сцены с персонажами
Homework 5, задание 4: соедини картинки с забегами из постера «Running for fun!».
```
A sheet of 3 separate illustrations arranged in a clean grid of three columns and one row, equal cells separated by wide empty pure-white gaps, no lines and no frames between the cells. Every picture is complete and centred in its cell with a generous empty margin, not touching any other picture or the edge of the sheet, nothing crossing between cells.
Row 1, left to right: Winter Run: children running on a snowy forest path, a pot of hot soup at the finish; Fun Races: children in an egg-and-spoon race and a sack race at a school sports field, a basketball hoop behind; Costume Run: children in capes and masks running along a park path.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1024 px, each cell at least 600 px.
```

### Лист 60 · День рождения — одна картинка, сцены с персонажами
Тест Unit 8, SPEAKING I. Вопросы остаются: What event is this? How many people? What are they wearing?
```
One single picture filling the frame: a birthday party at home: a girl blowing out the candles on a cake, four friends in party hats around the table, presents, balloons, sandwiches, cups of juice.
Bright 3D-rendered cartoon style, Pixar-like friendly characters with expressive faces, stylised and clearly not photorealistic, soft rounded shapes, vivid saturated colours, warm soft light, everything clearly visible and easy to recognise. Absolutely no text, no letters, no numbers, no labels, no signs, no brand marks anywhere.
Output size: 2048 x 1365 px, landscape.
```
