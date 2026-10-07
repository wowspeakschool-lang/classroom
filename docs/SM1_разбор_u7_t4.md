# Super Minds 1 — разбор Unit 7 (HW2, HW4, HW6, HW7, тест) и теста Unit 4

Шаг 2 регламента: выгрузка разобрана, уроки описаны в `tools/sm1/u7.py` и
`tools/sm1/u4.py`, картинки из PDF вырезаны в `media/sm1/u7/` и `media/sm1/u4/`.
**Ничего не залито.** Ждём картинки по листам ниже.

Название юнита — по учебнику: **Unit 7 · Get dressed** (одежда, Do you like
this / these?, He's / She's wearing, узоры). Unit 4 — существующее в базе
`Unit 4 · Food`.

Выгрузка: ShkolaApp, пары `.txt` + `.pdf`. Все шесть PDF скачались целиком,
включая тест Unit 4 (5.9 МБ). Текст брался из текстового слоя PDF, каждая
страница просмотрена картинкой, верные варианты сверены по чекбоксам.

Сводка:

| Урок | Блоков | Ключ |
|---|---|---|
| Unit 7 · Homework 2 | 20 | `u7_hw2` |
| Unit 7 · Homework 4 | 3 | `u7_hw4` — в выгрузке только часть (2), видео |
| Unit 7 · Homework 6 | 7 | `u7_hw6` |
| Unit 7 · Homework 7 | 9 | `u7_hw7` |
| Unit 7 Test | 12 | `u7_test` |
| Unit 4 Test | 12 | `u4_test` |

Homework 1, 3, 5 Unit 7 в выгрузке нет — пропущены, номера уроков не сдвинуты
(`lesson_sort` = K − 1, тесты — 7).

---

## Unit 7 · Homework 2

Выгрузка: 23 нумерованных блока + один безномерной Embed.

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие «Привет! … ГРОССМЕЙСТЕРА английского» | бл. 1 (картинка Hello-мальчик → `shared/hello_wave`) |
| 2 | text | «Давай повторим…» + карточка Grammar 1 — Do you like this / these? | бл. 3, карточка вырезана из PDF |
| 3 | text | «Мы начнём с видео…» | бл. 4 (стоковый мультяшный мальчик не взят) |
| 4 | video | видео 1 (flower / rabbit), `url` пустой | бл. 5 |
| 5 | match | This is a flower / a rabbit, These are flowers / rabbits → картинки | бл. 6; **картинки справа не выгрузились** (плейсхолдеры) — наши, Л7.6 |
| 6 | text | «Посмотри ещё одно видео… A T-shirt? A cap? Shoes?» | бл. 7 |
| 7 | video | видео 2 (Do you like this cap?), `url` пустой | бл. 8 |
| 8 | match | Do you like this cap? → Yes, I do. · these socks? → No, I don't. | бл. 9 |
| 9 | quiz | this / these, 6 вопросов с картинками — **СОСТАВ МОЙ** | бл. 11, Wordwall, обложка пустая |
| 10 | text | «Отлично! Ты справился с половиной…» | бл. 12 (смайлик → `shared/well_done_smiley`) |
| 11 | quiz | Do you like this skirt? 👍 → Yes, I do. · these trousers? 👎 → No, I don't. | бл. 13 и 14 (два «Теста» по вопросу) |
| 12 | text | «А теперь давай расставим слова…» | бл. 15 (красная стрелка не взята) |
| 13–16 | order | Do you like this jacket? / these jeans? / these shoes? / this cap? | бл. 16–19, картинки — Л7.1, Л7.2 |
| 17 | speaking | «Расскажи, какая одежда тебе нравится», картинка-набор одежды, образец `sample` | бл. 20 (текст + аудио-образец) и 21 (запись голоса) |
| 18 | quiz | 👍/👎 → Yes, I do / No, I don't, 5 вопросов — **СОСТАВ МОЙ** | бл. 22, Wordwall «дополнительное задание», обложка пустая |
| 19 | sort | столбики this / these, 10 вещей — **СОСТАВ МОЙ** | безномерной Embed «Перенеси вещи в подходящие столбики», Wordwall, обложка пустая |
| 20 | text | «Поздравляю! … Увидимся на занятии!» | бл. 23 (Микки Маус → `shared/well_done_trophy`) |

Не перенесено: бл. 2 — реклама для родителей «3 бесплатных урока по
реферальной программе»; декоративные смайлик и стрелки бл. 10, 15.

## Unit 7 · Homework 4

В выгрузке только **Homework 4 (2)** — интерактивное видео «SM2ed Animated
story video …» (Rutube, 1:39) с девятью заданиями по таймкодам. Содержимого
заданий в выгрузке нет: видны только тип и время. **Части (1) нет совсем.**

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие, «Сегодня тебя ждёт мультфильм» | комментарий к уроку (2) |
| 2 | video | мультфильм Unit 7, `url` пустой | видео урока (2) |
| 3 | text | прощание | наше |

Задания видео (в урок не положены, ждут текста): 00:02, 00:04, 00:07, 00:08 —
«Верно / неверно»; 00:29, 00:41 — «Составь предложение»; 00:47 — «Верно /
неверно»; 01:05, 01:30 — «Составь предложение».

## Unit 7 · Homework 6

**Ни одна картинка урока в PDF не выгрузилась** — на их месте только кнопки
удаления. Все картинки — наши (Л7.3–Л7.5).

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | «Привет! Сегодня мы выучим названия разных узоров…» | бл. 1 (надпись hello → `shared/hello_book`) |
| 2 | text | «Давай повторим…» — 5 узоров с подписями | бл. 3, карточка не выгрузилась — **собрана нами** из Л7.3 |
| 3 | match | stripes, spots, flowers, plain, zigzags → образцы узоров | бл. 4, картинки не выгрузились |
| 4 | quiz | Anna / Lily / Kate: по описанию найти одежду девочки (3 вопроса, варианты — картинки Л7.4) | бл. 5 — **переделан**, см. «спорное» |
| 5 | gaps | «Look! These are my favourite clothes…» — 5 пропусков (flowers, zigzags, plain, stripes, spots), картинка Л7.5 | бл. 6 |
| 6 | task | «Ура! Это последнее задание… опиши свою любимую одежду с узорами» | бл. 7, «Открытый вопрос» |
| 7 | text | «Поздравляю! … За это лови сердечко ❤️» | бл. 8 |

Бл. 2 выгрузки — «Картинка» без описания, картинка не выгрузилась; по образцу
HW2 это, скорее всего, та же реклама для родителей. Не перенесён.

## Unit 7 · Homework 7

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | «👕 Привет, модник! Это последняя домашка перед тестом!» | бл. 1 (клипарт детей → `shared/hello_highfive`) |
| 2 | quiz | True / False: shoes ✔, trousers (на картинке куртка) ✘, skirt (шорты) ✘, sweater ✔ | четыре безномерных «Теста» бл. 1; картинки — Л7.1 |
| 3 | sort | ноги 🦿 / туловище 👕 / голова 🧢 — 10 вещей | бл. 2 «Классификация» |
| 4 | gaps | this / these, 6 пропусков | бл. 3 |
| 5 | quiz | Is he wearing a green sweater? → No, he isn’t · trousers? → Yes, he is · purple skirt? → Yes, she is | бл. 4, кадры героев мультфильма вырезаны из PDF |
| 6 | speaking | «Что он/она носит?», пример He’s wearing a blue jacket… | бл. 5, клипарт мальчика и девочки из PDF |
| 7 | exact_input | впиши слово по картинке, 6 вещей — **СОСТАВ МОЙ** | бл. 6, Wordwall «Впиши слова», обложка пустая |
| 8 | quiz | Is / is / isn’t, 5 вопросов по героям — **СОСТАВ МОЙ** | безномерной Embed «Выбери правильный вариант», Wordwall, обложка пустая |
| 9 | text | «Молодец! Ты повторил всю одежду… Ты готов к тесту!» | бл. 7 (картинка See you → `shared/well_done_jump`) |

## Unit 7 Test

Приветствия и прощания нет (тест).

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | exact_input | 10 слов: джинсы, свитер, пиджак, юбка, шорты, бейсболка, обувь, носки, футболка, брюки | бл. 1, словарный тренажёр «Заполни пропуски» |
| 2 | match | sweater, T-shirt, baseball cap, jacket, jeans, skirt → картинки | бл. 2; **картинки не выгрузились** — Л7.1, Л7.2 |
| 3 | quiz | 9 пропусков: this hat / do · these socks / don't · wearing · Is / isn't · Is / is | бл. 3, пять блоков «Выбери правильный вариант»; варианты — из выпадающих списков |
| 4–8 | order | Are Amy and Hannah riding bikes? · Do you like these shoes? · They are playing computer games. · Do you like these shorts? · Is Bobby eating a sandwich? | бл. 4; картинки — ЛТ7.1, Л7.1 |
| 9 | text | текст «Today is a fun day! … fashion show» | описание бл. 6 |
| 10 | quiz | 5 вопросов по тексту: C brown · B plain · B flowers · A No, he isn't · C pink | бл. 6 |
| 11 | speaking | SPEAKING Part 1: какая одежда нравится, картинка — витрина магазина (ЛТ7.2) | бл. 7 |
| 12 | speaking | SPEAKING Part 2: кто во что одет, картинка — три героя мультфильма из PDF HW7 | бл. 8 |

**Бл. 5 выгрузки не перенесён** — аудирование «Speaker 1–5 + Extra → кто во
что одет»: нет ни аудио, ни картинок (правая колонка — плейсхолдеры «Введите
слово»), ни ответов.

## Unit 4 Test (Unit 4 · Food)

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | exact_input | 11 слов: banana, cake, sandwich, apple, pizza, sausage, chicken, steak, peas, carrots, fish | бл. 1, словарный тренажёр «Впиши буквы» |
| 2 | match | chicken, cheese sandwich, cake, sausage, banana, steak → картинки | бл. 2; **картинки не выгрузились** — ЛТ4.1 |
| 3 | speaking | прочитать вслух 5 скороговорок (turtle, crow, cube, cloud, giraffe) | бл. 3 |
| 4 | quiz | 9 пропусков: got / have · haven't got · have / got · Have / haven't · have / have got | бл. 4, пять блоков «Выбери правильный вариант»; картинки — ЛТ4.1, ЛТ4.2 |
| 5–9 | order | Have we got any cake? · I've got chicken and carrots. · Have we got any pizza? · I haven't got orange juice. · Have you got any ice cream? | бл. 5; картинки — ЛТ4.1, ЛТ4.2 |
| 10 | truefalse | READING, текст Бена: sandwich ✔ · banana ✘ · apple ✔ · cake ✘ · carrots ✔ | бл. 6; текст был картинкой 900×94, переписан текстом |
| 11 | quiz | LISTENING, 5 вопросов: No, they haven't · a cake · Yes, they have · a chicken · Yes, they have; `audio` пустой | бл. 7 |
| 12 | speaking | «Представь, что это твой холодильник», картинка холодильника | бл. 8, картинка из PDF |

---

## Промпты на картинки

Две строки стиля — один раз:

* **ПРЕДМЕТ:** Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left.
* **СЦЕНА:** Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, one single scene filling the frame, no people.

В промптах ниже строка стиля уже вклеена — копировать целиком.

### 1. Обязательные — картинок в выгрузке нет

**Л7.1 · одежда, 3×3** → `media/sm1/u7/`: `clothes_tshirt`, `clothes_sweater`,
`clothes_jacket` / `clothes_skirt`, `clothes_shorts`, `clothes_jeans` /
`clothes_trousers`, `clothes_socks`, `clothes_shoes`.
Где: U7 HW2 бл. 9, 11, 13–15, 18, 19 · HW7 бл. 2, 7 · Test бл. 2, 5, 7.

```
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. A 3×3 grid of nine separate children's clothing items, each laid flat and seen from the front, one item per cell. Row 1, left to right: a plain red short-sleeved T-shirt; a plain green knitted sweater; a brown zip-up jacket. Row 2, left to right: a plain pink pleated skirt; plain blue shorts; a pair of blue denim jeans. Row 3, left to right: a pair of plain grey trousers; a pair of white socks; a pair of brown lace-up children's shoes, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces. 1536×1536.
```

**Л7.2 · головные уборы, носки, свитер для теста, 2×2** → `clothes_cap`,
`clothes_hat_elephant` / `clothes_socks_faces`, `clothes_sweater_red`.
Где: U7 HW2 бл. 16, 18, 19 · HW7 бл. 7 · Test бл. 2, 3.

```
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. A 2×2 grid of four separate items, one per cell. Row 1, left to right: a yellow baseball cap, generic design, not resembling any real product; a funny grey plush hat shaped like an elephant head with big floppy ears and a trunk. Row 2, left to right: a pair of funny purple and white socks with cartoon faces with open mouths printed on them; a bright red chunky knitted sweater. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces. 1024×1024.
```

**Л7.3 · узоры, 3 + 2** → `pattern_stripes`, `pattern_spots`, `pattern_flowers`
/ `pattern_plain`, `pattern_zigzags`.
Где: U7 HW6 бл. 2, 3.

```
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Five separate square pieces of soft fabric, each with slightly rounded corners, arranged in two rows. Row 1, left to right: a fabric square with blue and white horizontal stripes; a fabric square with big white spots on red; a fabric square with small colourful flowers on light yellow. Row 2, left to right, centred: a plain green fabric square with no pattern at all; a fabric square with orange and white zigzags. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces. 1536×1024.
```

**Л7.4 · три комплекта одежды, 1×3** → `outfit_anna`, `outfit_lily`, `outfit_kate`.
Где: U7 HW6 бл. 4. В каждой ячейке верх лежит над юбкой — как будто одежда
разложена на кровати.

```
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Three separate girls' outfits in one row, each outfit is two clothing items laid flat, the top placed above the skirt. Row 1, left to right: a sweater with bold purple and white zigzags above a plain dark blue skirt with no pattern; a light blue shirt with white spots above a pink skirt with small flowers; a T-shirt with red and white horizontal stripes above a yellow skirt with big black spots. Plain flat pure white background, no shadow on the background, wide empty white gaps between the outfits, every item complete and not touching any other outfit or the edge, no text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces. 1536×1024.
```

**Л7.5 · «мои любимые вещи», одна картинка, не резать** → `fav_clothes`.
Где: U7 HW6 бл. 5. Цвета должны совпасть с текстом задания: шорты красно-белые,
свитер чёрно-белый, носки жёлтые.

```
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Five children's clothing items laid flat in two rows. Row 1, left to right: a white T-shirt with colourful flowers; red and white shorts with a zigzag pattern; plain brown trousers with no pattern. Row 2, left to right, centred: a black and white striped sweater; a pair of yellow socks with white spots. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces. 1536×1024.
```

**Л7.6 · цветок и кролик, 2×2** → `pic_flower`, `pic_rabbit` / `pic_flowers`,
`pic_rabbits`.
Где: U7 HW2 бл. 5.

```
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. A 2×2 grid, one picture per cell. Row 1, left to right: one single red flower with a green stem; one single white fluffy rabbit sitting. Row 2, left to right: a group of four colourful flowers growing together; a group of three fluffy rabbits sitting together, white, brown and grey. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces. 1024×1024.
```

**ЛТ7.1 · предметы к тесту Unit 7, 3 + 2** → `obj_tv`, `obj_microphone`,
`obj_bikes` / `obj_game_controllers`, `obj_sandwich`.
Где: U7 Test бл. 3, 4, 6, 8. Заменяют стоковые фото людей (в бл. 6 — фото
детей, его брать нельзя).

```
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Five separate objects in two rows. Row 1, left to right: a television with a green football field on the screen and a remote control lying in front of it, generic design, not resembling any real product; a silver microphone on a stand with small musical notes floating around it; two children's bicycles standing side by side, one red and one blue, generic design, not resembling any real product. Row 2, left to right, centred: two game controllers lying in front of a small game console, generic design, not resembling any real product; a big sandwich with lettuce, tomato and cheese on a white plate. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces. 1536×1024.
```

**ЛТ7.2 · витрина магазина одежды, сцена** → `scene_clothes_shop`.
Где: U7 Test бл. 11 (вместо фото шестерых детей).

```
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, one single scene filling the frame, no people. Inside a bright children's clothes shop: a long clothes rail with hangers holding a yellow dress with flowers, a red T-shirt, a green sweater, a blue jacket and a pink skirt; below it a low shelf with folded blue jeans, orange shorts, striped socks and a pair of white trainers, generic design, not resembling any real product; on top of the shelf a purple baseball cap and a straw sun hat. Soft daylight, clean simple wall behind. No text, no letters, no labels, no numbers, no price tags, no signs. No people at all - no humans, no hands, no faces, no mannequins. 1536×1024.
```

**ЛТ4.1 · еда, 3×3** → `media/sm1/u4/`: `food_chicken`, `food_cheese_sandwich`,
`food_cake` / `food_sausage`, `food_banana`, `food_steak` / `food_pizza`,
`food_ice_cream`, `food_milk`.
Где: U4 Test бл. 2, 4, 5, 7, 9.

```
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. A 3×3 grid of nine separate food items, one per cell. Row 1, left to right: a golden roast chicken on a small plate; a cheese sandwich cut in half with yellow cheese showing; a round cake with pink icing and a cherry on top. Row 2, left to right: two sausages on a small plate; one yellow banana; a grilled steak on a plate. Row 3, left to right: one slice of pepperoni pizza with melted cheese; a pink ice cream in a waffle cone standing upright in a small cone holder; a tall glass of milk. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces. 1536×1536.
```

**ЛТ4.2 · еда к пропускам и предложениям, 2×2** → `food_apple_banana`,
`food_peas_carrots` / `food_chicken_carrots`, `food_orange_juice`.
Где: U4 Test бл. 4, 6, 8.

```
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. A 2×2 grid of four separate food items, one per cell. Row 1, left to right: a red apple and a yellow banana lying together; a white bowl full of green peas and orange carrot slices. Row 2, left to right: a baking dish with roasted chicken pieces and carrots; a glass of orange juice with two orange halves beside it. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces. 1024×1024.
```

Итого: **10 листов** (8 сеток, Л7.5 целиком, ЛТ7.2 — сцена), **45 картинок**
(Unit 7 — 32, Unit 4 — 13).

### 2. По желанию — в выгрузке стоковое фото

Отдельных листов нет: стоковые фото одежды (HW2: юбка, брюки на человеке,
пиджак, джинсы, туфли на шпильке, кепка; HW7: клипарт ботинок, куртки, шорт,
свитера) и еды (тест Unit 4) **уже заменены** картинками обязательных листов
Л7.1, Л7.2, ЛТ4.1, ЛТ4.2 — чтобы юнит вышел одним стилем и не было людей.

### 3. Не перерисовывать — взято из PDF

| Файл | Откуда | Где |
|---|---|---|
| `media/sm1/u7/grammar_this_these.webp` 900×506 | HW2, карточка Grammar 1 | HW2 бл. 2 |
| `media/sm1/u7/clothes_set_speaking.webp` 720×520 | HW2, клипарт 9 вещей к записи голоса | HW2 бл. 17 |
| `media/sm1/u7/char_boy_blue_sweater.webp` | HW7, кадр героя мультфильма | HW7 бл. 5, 8 |
| `media/sm1/u7/char_boy_red_jacket.webp` | HW7, кадр героя | HW7 бл. 5, 8 |
| `media/sm1/u7/char_girl_green_sweater.webp` | HW7, кадр героини | HW7 бл. 5, 8 |
| `media/sm1/u7/kids_thumbs_up.webp` | HW7, клипарт мальчик и девочка (прозрачный фон → белый) | HW7 бл. 6 |
| `media/sm1/u7/chars_three.webp` | три кадра героев HW7, собраны в ряд | Test бл. 12 |
| `media/sm1/u4/fridge.webp` | тест Unit 4, холодильник | U4 Test бл. 12 |

Вырезано 8 файлов (7 из PDF + 1 сборный).

---

## Доработать руками

### Что нужно от вас — весь список

| Урок | Блок | Что сделать |
|---|---|---|
| U7 HW2 | 4 | видео 1 (This is a flower / These are rabbits) → файл `sm1_u7_hw2_b4` |
| U7 HW2 | 7 | видео 2 (Do you like this cap?) → файл `sm1_u7_hw2_b7` |
| U7 HW2 | 17 | аудио-образец ответа → `sm1_u7_hw2_b17`; или нажать «Озвучить пачкой» (размечен наш образец «I like this T-shirt. I like these jeans. I don't like this skirt.») |
| U7 HW2 | 9, 18, 19 | Wordwall, обложки пустые — **СОСТАВ МОЙ**, посмотреть |
| U7 HW4 | — | **части (1) нет** в выгрузке — прислать, если есть |
| U7 HW4 | 2 | мультфильм Unit 7 («SM2ed Animated story video», Rutube, 1:39) → файл или ссылка `sm1_u7_hw4_b2` |
| U7 HW4 | после 2 | 9 заданий интерактивного видео (00:02, 00:04, 00:07, 00:08, 00:47 — верно/неверно; 00:29, 00:41, 01:05, 01:30 — составь предложение): в выгрузке только тип и время. Прислать тексты — добавим блоками после видео |
| U7 HW6 | 4 | решить: задание переделано (см. «спорное») |
| U7 HW7 | 7, 8 | Wordwall, обложки пустые — **СОСТАВ МОЙ**, посмотреть |
| U7 Test | после 8 | аудирование «Speaker 1–5 + Extra»: нет аудио, картинок и ключа — **в урок не положено**. Прислать аудио, картинку и ответы — добавим блоком после 8-го (номера 9–12 сдвинутся на один, файл обновим) |
| U4 Test | 11 | аудио LISTENING → файл `sm1_u4_test_b11` |
| все шесть | — | нажать «Озвучить пачкой» (размечено `audio_tts` / `left_audio_tts` / `right_audio_tts`) — по желанию, озвучку по курсу решили не прогонять |
| все шесть | — | включить публикацию (заливаем с `is_published = false`) |

### По урокам — подробности

**U7 HW2.** Не перенесены: бл. 2 выгрузки — реклама для родителей; смайлики
и стрелки-украшения. Блоки «Тест» 13 и 14 выгрузки сведены в один quiz (11).
Текст 20 и запись голоса 21 — в один speaking (17). Картинки к «соедини» (5) в
выгрузке не выгрузились — наши. Wordwall: бл. 9 — this / these по картинкам,
бл. 18 — Yes, I do / No, I don't по смайлику, бл. 19 — столбики this / these.

**U7 HW6.** В PDF не выгрузилась ни одна картинка урока. Карточка «Давай
повторим» (бл. 2) собрана нами из образцов узоров. В ключе бл. 5 выгрузки
опечатка «zigzagz» — принимаем zigzags и zigzag.

**U7 HW7.** Четыре безномерных «Теста» True/False сведены в один quiz (бл. 2).
Wordwall: бл. 7 — впиши слово по картинке, бл. 8 — Is / is / isn't по героям.

**U7 Test.** Пять блоков «Выбери правильный вариант» сведены в один quiz
(бл. 3), вопрос на каждый пропуск, варианты — из выпадающих списков выгрузки.
Стоковые фото людей к пропускам и «составь предложение» заменены предметами
(в бл. 6 было фото детей).

**U4 Test.** Текст READING в выгрузке был картинкой — переписан текстом. В
бл. 4 выгрузки опечатка «ccarrots» — исправлено на carrots.

### Спорное

1. **U7 HW6 бл. 4.** В выгрузке: картинка с тремя девочками (Anna, Lily,
   Kate), по описанию выбрать имя. Картинка не выгрузилась, а людей мы не
   генерируем. Сделано наоборот: читаешь описание девочки — выбираешь её
   одежду из трёх комплектов (Л7.4). Если нужен исходный вид — пришлите
   картинку с девочками.
2. **U7 Test бл. 11.** В выгрузке «(используй this / that)», а юнит про
   this / these — поставлено this / these.
3. **U7 Test бл. 11 и 12.** Фото шестерых детей заменено: в Part 1 — витриной
   магазина (ЛТ7.2), в Part 2 — тремя героями мультфильма; пример ответа в
   Part 2 переписан под героя («He is wearing a red jacket, a white T-shirt…»).
4. **U7 HW2 бл. 2 и HW6 бл. 2 выгрузки** — реклама «3 бесплатных урока по
   реферальной программе» (в HW6 картинка не выгрузилась, догадка по HW2).
   В уроки не переносили.

---

## Для сборщика

`python3 tools/sm1_build.py --check-all`: все шесть уроков — ok.

⚠️ **Проверка ссылок на картинки в `tools/sm1_build.py` сейчас не срабатывает
вовсе.** Регулярка `r"@@MEDIA@@([^\"'\\s)<]+)"` в raw-строке исключает из
класса символов букву `s` (а не пробел), а все пути начинаются с `sm1/` или
`shared/` — совпадений ноль, «нет файла» не выдаётся никогда. Правильно:
`r"@@MEDIA@@([^\"'\s)<\\]+)"`. Файл не мой — не правил; своей проверкой
нашёл, что не хватает ровно 45 будущих картинок из листов выше, остальные
ссылки на месте.
