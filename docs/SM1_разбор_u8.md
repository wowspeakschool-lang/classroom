# Super Minds 1 · Unit 8 — разбор выгрузки и черновая сборка

Сборка: `tools/sm1/u8.py`, картинки: `media/sm1/u8/`. Ничего не залито.
Номера блоков везде **как в редакторе** (`sort_order + 1`), сверены с
итоговой сборкой.

Выгрузка (папка Drive `Unit 8` и `Test SM1/Unit 8`): HW1 (1), HW2, HW3,
HW4 (1)+(2), HW5, HW6 (1), HW7, Unit 8 Test. Скачаны и txt, и pdf; все PDF
меньше 4.2 МБ, легли целиком.

**Название юнита — `Unit 8 · My body`.** Слова юнита — части тела и
can / can't, история про робота. Точное название раздела в учебнике
Super Minds 1 по выгрузке не проверить — 🟥 сверить с учебником.

Во всех домашках вторым блоком стоит картинка «Информация для родителей! Мы
дарим 3 бесплатных урока по реферальной программе…» — **не переносим**,
это реклама, а не задание. Поэтому номера наших блоков расходятся с
номерами в выгрузке.

## Сводка

| Урок | Блоков | Что из выгрузки | Пометки |
|---|---|---|---|
| u8_hw1 · Homework 1 | 6 | HW1 (1) — словарный тренажёр, 8 слов | части (2) в выгрузке нет |
| u8_hw2 · Homework 2 | 10 | HW2 | пустое «Найди пару» не перенесено; 2 Wordwall — СОСТАВ МОЙ |
| u8_hw3 · Homework 3 | 13 | HW3 | 2 Wordwall — СОСТАВ МОЙ |
| u8_hw4 · Homework 4 | 10 | HW4 (1) + (2) | перемычка — блок 8; вопросы интерактивного видео не выгрузились |
| u8_hw5 · Homework 5 | 14 | HW5 | 2 Wordwall — СОСТАВ МОЙ |
| u8_hw6 · Homework 6 | 7 | HW6 (1) — словарный тренажёр, 6 слов | части (2) нет; переводов в выгрузке нет — наши |
| u8_hw7 · Homework 7 | 10 | HW7 | 2 Wordwall — СОСТАВ МОЙ |
| u8_test · Unit 8 Test | 13 | Super Minds 1 Unit 8 Test | kind `test`, без приветствия/прощания |

## Блоки по урокам

### u8_hw1 · Homework 1

Тренажёр «vocabulary-drilling»: head, fingers, hand, knee, leg, toes, foot,
arms + переводы; задания «Карточки», «Запомни», «Послушай», «Найди пару».
Картинок у слов в выгрузке нет — лист Л8.1.

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие + мишка body_teddy | текст комментария к уроку |
| 2 | flashcards | 8 слов с переводом и картинкой | список слов |
| 3 | quiz | «Как по-английски …?» ×8 | «Запомни» |
| 4 | quiz | «Послушай слово и выбери» ×8, `audio_tts` | «Послушай» |
| 5 | match | картинка ↔ слово ×8 | «Найди пару» |
| 6 | text | прощание | наше |

### u8_hw2 · Homework 2

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие | блок 1 |
| 2 | text | карточка Grammar 1 — I can / I can't | блок 3 (grammar_can_cant) |
| 3 | text | вступление к видео | блок 4 |
| 4 | video | видео про животных, пустой url | блок 5 (медиафайл) |
| 5 | hotspot | 6 подписей к ученикам на картинке учебника | блок 8 «Диаграмма» (sb_can_cant_kids) |
| 6 | quiz | 4 вопроса с картинкой: I can / can't swim, stand on one leg, skip, ski | блок 9 «Выбери правильный вариант» |
| 7 | speaking | «Познакомься с Бобом», пустой `sample` | блок 10 «Запись голоса» |
| 8 | match | 6 картинок ↔ I can / can't … — СОСТАВ МОЙ | блок 11 Wordwall «Соедини описание с картинкой» |
| 9 | quiz | 5 вопросов A fish ___ swim — СОСТАВ МОЙ | блок 12 Wordwall «Выбери правильный вариант» |
| 10 | text | прощание | блок 12 (текст) |

Не перенесено: блок 7 выгрузки «Найди пару» после видео — правые
значения есть (I can swim, I can't walk, I can climb trees, I can't fly,
I can ski, I can't stop), левый столбец пустой («Введите слово»), картинок
нет.

В блоке 9 выгрузки у каждого из четырёх предложений была своя картинка,
но в PDF дошла только обрезанная первая. Поставлены клипарт из HW3
(ab_cant_swim, ab_stand_one_leg), девочка со скакалкой из HW5
(she_cant_skip) и новая ab_can_ski.

### u8_hw3 · Homework 3

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие | блок 1 |
| 2 | text | карточка Grammar 2 — Can you …? | блок 3 (grammar_can_you) |
| 3 | text | вступление к видео | блок 4 |
| 4 | video | видео Can you …?, пустой url | блок 5 |
| 5 | match | Can you swim? ↔ Yes, I can.; Can you fly? ↔ No, I can't. | блок 6 |
| 6 | hotspot | 6 подписей на листе клипарта | блок 7 «Диаграмма» (abilities_sheet) |
| 7 | gaps (drag) | ✗/✓ + can / can't, 6 предложений | блок 8 «Выбери правильный вариант» ×6 |
| 8 | speaking | «Мой монстрик», картинка monster, пустой `sample` | «Запись голоса» + картинка |
| 9 | quiz | 5 вопросов Can a fish swim? — СОСТАВ МОЙ | блок 9 Wordwall «Выбери правильный вариант» |
| 10 | order | Can you swim? — СОСТАВ МОЙ | блок 9′ Wordwall «Расставь слова» |
| 11 | order | Can you ride a bike? — СОСТАВ МОЙ | то же |
| 12 | order | No, I can't play the piano. — СОСТАВ МОЙ | то же |
| 13 | text | прощание | блок 10 |

### u8_hw4 · Homework 4

(1) и (2) одним уроком: прощание (1) и приветствие (2) сведены в блок 8.

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие | (1) блок 1–2 |
| 2 | text | карточка Story «The Problem» (Key Phrases) | (1) блок 3 (story_key_phrases) |
| 3 | text | вступление к истории | (1) блок 4 |
| 4 | video | аудио истории, пустой url | (1) блок 5 (медиафайл) |
| 5 | text | кадры истории 1–6 и 7–8 | (1) блок 6 (story_robot_1_6, story_robot_7_8) |
| 6 | hotspot | перемешанные кадры → Picture 1…8 | (1) блок 7 «Диаграмма» (story_robot_shuffled) |
| 7 | match | фраза ↔ герой ×4 | (1) блок 8 |
| 8 | text | перемычка: конец основной части, дальше видео | (1) блок 9 + (2) комментарий |
| 9 | video | интерактивное видео 2:11, пустой url | (2) |
| 10 | text | прощание | наше |

В «Диаграмме» (блок 6) **точки в выгрузке стоят неправильно**: метки 3 и 4
обе на втором кадре верхнего ряда, метка 2 — на краю первого. Расставлены
по содержанию кадров: верхний ряд — 2, 3, 7, 6; нижний — 4, 5, 1, 8.

### u8_hw5 · Homework 5

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие | блок 1 |
| 2 | text | «Начнём с практики!» | блок 3 |
| 3 | quiz | 5 вопросов Can she skip? … с картинкой | «Выбери правильный вариант» ×5 |
| 4 | text | переход к «Составь предложение» | блок 4 |
| 5 | order | He can stand on one leg. (ab_stand_one_leg) | «Составь предложение» |
| 6 | order | He can swim. (ab_dog_swim) | то же |
| 7 | order | She can't ride a horse. (she_cant_ride_horse) | то же |
| 8 | order | He can't play tennis. (he_cant_play_tennis) | то же |
| 9 | text | форум о питомцах (pet_forum) | блок «Картинка» |
| 10 | truefalse | Patch can swim ✓, Jazzy is a horse ✓, Jazzy can't skip ✗ | блок 5 |
| 11 | speaking | «Мой питомец», пустой `sample` | блок 6 |
| 12 | gaps (type) | can / can't по тексту форума, 7 пропусков — СОСТАВ МОЙ | блок 7 Wordwall «Впиши слова» |
| 13 | match | описание ↔ Bob / Patch / Jazzy — СОСТАВ МОЙ | блок 8 Wordwall «Соедини описание с картинкой» |
| 14 | text | прощание | блок 8 (текст) |

Картинки к вопросам блока 3: в PDF есть «Can she skip?» (she_cant_skip) и
«Can he touch his toes?» (he_touch_toes); у «Can she dance?» картинка
обрезана, у «Can he ride his bike?» и «Can this dog swim?» — нет совсем.
Новые — с животными (людей не генерируем): ab_cat_dance,
ab_bear_cant_ride_bike, ab_dog_swim. У «Составь предложение» в PDF не
дошли картинки к первым двум предложениям — ab_stand_one_leg из HW3 и
ab_dog_swim.

### u8_hw6 · Homework 6

Тренажёр: forwards, backwards, stretch, sideways, step, jump. Перевода в
выгрузке нет (заглушка «Определение») — переводы наши: вперёд, назад,
тянуться, вбок, шагать, прыгать. Задания «Послушай», «Найди пару»,
«Скрэмбл» ×2, «Введи слова» ×2.

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие | наше (комментария к уроку нет) |
| 2 | flashcards | 6 слов, картинки Л8.2 | список слов |
| 3 | quiz | «Послушай слово и выбери» ×6 | «Послушай» |
| 4 | match | картинка ↔ слово ×6 | «Найди пару» |
| 5 | exact_input | собери слово из перемешанных букв ×6 | «Скрэмбл» |
| 6 | exact_input | напиши по-английски ×6 | «Введи слова» |
| 7 | text | прощание | наше |

### u8_hw7 · Homework 7

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | «Привет, изобретатель!» + inventors_robot | блок 1 |
| 2 | quiz | «Что значит head?» ×8, с картинкой | блок 2 «Найди определение» |
| 3 | gaps (type) | A penguin can't fly … ×6, картинка animals_can_cant | блок 3 «Впиши в пропуски» |
| 4 | quiz | Can he play tennis? ✓ / cook? ✗ / Can she dance? ✓ / fly? ✗ | блок 4 «Тест» ×4 |
| 5 | speaking | что ты умеешь и не умеешь | блок 5 |
| 6 | exact_input | впиши слово по картинке ×8 — СОСТАВ МОЙ | блок 6 Wordwall «Super Minds 1 Unit 8 Voc spelling» |
| 7 | order | I can touch my toes. — СОСТАВ МОЙ | блок 6′ Wordwall «Unit 8 Can / Can't» (Unjumble) |
| 8 | order | Can you ride a bike? — СОСТАВ МОЙ | то же |
| 9 | order | She can't play the piano. — СОСТАВ МОЙ | то же |
| 10 | text | «Молодец! Ты готов к тесту!» | блок 7 |

Верные ответы блока 4 сверены по чекбоксам: tennis — Yes, cook — No,
dance — Yes, fly — No; совпадают с галочками на картинках.

### u8_test · Unit 8 Test

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | exact_input | впиши недостающие буквы ×8 | блок 1 «Заполни пропуски» (тренажёр на 8 слов) |
| 2 | match | картинка ↔ hand, foot, toes, head, fingers, arm | блок 2 «Найди пару» |
| 3 | quiz | He/She ___ … ×6 с картинкой, can / can't | блок 3 «Выбери правильный вариант» ×6 |
| 4 | order | Can you stand on one leg? | блок 4 «Составь предложение» |
| 5 | order | My dog can play football. | то же |
| 6 | order | I can't touch my toes. | то же |
| 7 | order | Can your cat play the guitar? | то же |
| 8 | order | Can your sister fly a kite? (kite_sky) | то же |
| 9 | text | письмо Jake (картинка + текст) | блок 5, картинка |
| 10 | quiz | 5 вопросов к письму | блок 5 «Тест» |
| 11 | video | аудио: разговор Лили и Тома, пустой url | блок 6, аудиоплеер |
| 12 | gaps (type) | Bloop / big / four / can't / jump | блок 6 «Впиши в пропуски» |
| 13 | speaking | 5 вопросов по картинке города (t_town_scene) | блок 7 |

Блок 1: в выгрузке это тренажёр без текста задания — маски с пропущенными
буквами (h _ _ d …) наши. Блок 2: в выгрузке картинок нет (левый столбец
«Введите слово»), но правые слова есть — ставим картинки Л8.1; «arm»
показываем картинкой body_arms. Блок 3, верные: piano — can't, tennis —
can't, swim — can, dance — can, pony — can't, bike — can. Блок 8: в
выгрузке фото девочки с воздушным змеем — фото детей не берём, ставим
kite_sky. Блок 10, верные: eight; He can dance; Yes, he can; His feet are
too small; Come and see Beep — совпадают с текстом письма. Блок 12: в
выгрузке написано «Прочитай разговор», но текста разговора нет, только
аудиоплеер — заголовок поправлен на «Послушай».

## Промпты на картинки

Две строки стиля (уже вклеены в промпты):

* **ПРЕДМЕТ:** Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left.
* **СЦЕНА:** Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, one single scene filling the frame, no people.

Людей нет нигде — части тела и действия показаны на плюшевом мишке,
котёнке и других животных.

### 1. Обязательные — картинок в выгрузке нет

#### Л8.1 · Части тела — 9 карточек (3×3)

Режется на: body_head, body_arms, body_hand / body_fingers, body_leg,
body_knee / body_foot, body_toes, body_teddy.
Где: HW1 блоки 1, 2, 3, 5 (body_teddy — блок 1); HW7 блоки 2, 6; Test
блоки 1, 2.

```
A sheet of nine separate pictures arranged in a 3x3 grid on a plain flat pure white background, wide empty white gaps between the items, every item complete and not touching any other item or the edge. Each picture shows the same cute light-brown plush teddy bear toy facing the viewer; in each picture exactly ONE body part of the bear glows bright yellow while the rest of the bear stays light brown, so it is obvious which part is meant.
Row 1, left to right: the bear's head glows yellow; both arms glow yellow, held out wide; one paw (the hand) glows yellow, held up open.
Row 2, left to right: a close view of one raised open paw with five separate fingers spread wide, the fingers glow yellow; one whole leg glows yellow; only the knee of one bent leg glows yellow.
Row 3, left to right: one foot glows yellow, the sole turned to the viewer; a close view of one foot with five separate little toes clearly drawn, only the toes glow yellow; the whole bear standing and waving, nothing highlighted.
No people at all - no humans, no human hands, no faces of people. No text, no letters, no labels, no numbers, no arrows. No shadow on the background.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left.
Output size: 2048 x 2048 px, each cell at least 600 px.
```

#### Л8.2 · Движения — 6 карточек (3×2)

Режется на: move_forwards, move_backwards, move_sideways / move_step,
move_stretch, move_jump.
Где: HW6 блоки 2, 4, 6.

```
A sheet of six separate pictures arranged in a 3x2 grid on a plain flat pure white background, wide empty white gaps between the items, every item complete and not touching any other item or the edge. Each picture shows the same cute orange cartoon kitten doing one movement.
Row 1, left to right: the kitten walking forwards to the right, a big bright green arrow on the ground in front of it pointing the way it faces; the kitten facing right but stepping backwards to the left, a big orange arrow behind it pointing to the left; the kitten facing the viewer and sliding sideways, a big blue arrow at its side pointing sideways.
Row 2, left to right: the kitten taking one big step, a short trail of small paw prints behind it; the kitten stretching its whole body up tall with both front paws high above its head; the kitten jumping high in the air, small motion lines under its paws.
No people at all - no humans, no hands, no faces. No text, no letters, no labels, no numbers. No shadow on the background.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

#### Л8.3 · Умею / не умею — 6 карточек (3×2)

Режется на: ab_can_ski, ab_cat_dance, ab_bear_cant_ride_bike /
ab_dog_swim, kite_sky, robot_beep (запасная, в уроки не поставлена).
Где: ab_can_ski — HW2 блок 6; ab_cat_dance, ab_bear_cant_ride_bike — HW5
блок 3; ab_dog_swim — HW5 блоки 3, 6; kite_sky — Test блок 8.

```
A sheet of six separate pictures arranged in a 3x2 grid on a plain flat pure white background, wide empty white gaps between the items, every item complete and not touching any other item or the edge.
Row 1, left to right: a happy fox skiing down a small snowy hill on red skis with ski poles; a cat ballerina in a pink tutu dancing on tiptoe; a sad brown bear sitting on the ground next to a small bicycle that has fallen over on its side.
Row 2, left to right: a happy dog swimming in a small round pool of blue water, its head above the waves; a colourful diamond kite with a long ribbon tail flying against a small round patch of blue sky with two little clouds; a friendly small toy robot with a big round head and short legs, waving, generic design, not resembling any real product.
No people at all - no humans, no hands, no faces. No text, no letters, no labels, no numbers. No shadow on the background.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left.
Output size: 2048 x 1365 px, each cell at least 600 px.
```

### 2. По желанию — в выгрузке стоковое фото или клипарт

#### Л8.4 · Замена стоковых картинок — 4 карточки (2×2)

Режется на: monster, t_dog_football, t_cat_guitar, inventors_robot
(заменят уже вырезанные файлы с теми же именами).
Где: monster — HW3 блок 8; t_dog_football — Test блок 5; t_cat_guitar —
Test блок 7; inventors_robot — HW7 блок 1 (в выгрузке клипарт с детьми).
Ответы от замены не пострадают.

```
A sheet of four separate pictures arranged in a 2x2 grid on a plain flat pure white background, wide empty white gaps between the items, every item complete and not touching any other item or the edge.
Row 1, left to right: a friendly fluffy purple one-eyed monster with a big smile, jumping happily; a white dog with brown patches playing with a black-and-white football on a small patch of green grass.
Row 2, left to right: a cat wearing red sunglasses playing a red electric guitar, generic design, not resembling any real product; a half-built friendly toy robot standing next to a red toolbox with a screwdriver, a wrench and a light bulb on the floor.
No people at all - no humans, no hands, no faces. No text, no letters, no labels, no numbers. No shadow on the background.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left.
Output size: 2048 x 2048 px, each cell at least 900 px.
```

### 3. Не перерисовывать — уже вырезано из PDF в `media/sm1/u8/` (36 файлов)

* карточки методиста: grammar_can_cant, grammar_can_you, story_key_phrases, t_letter_jake, pet_forum;
* история «The Problem»: story_robot_1_6, story_robot_7_8, story_robot_shuffled;
* картинки учебника и заданий: sb_can_cant_kids, abilities_sheet, animals_can_cant, boy_tennis_cook, girl_dance_fly, t_town_scene;
* клипарт из листа HW3: ab_cant_swim, ab_stand_one_leg, ab_cant_ride_bike, ab_play_football, ab_skip, ab_cant_piano;
* картинки к вопросам: she_cant_skip, he_touch_toes, she_cant_ride_horse, he_cant_play_tennis;
* тест (чёрно-белые картинки учебника): t_he_piano, t_he_tennis, t_he_swim, t_she_dance, t_she_pony, t_she_bike, t_stand_one_leg, t_touch_toes;
* сток (есть замена в Л8.4): monster, t_dog_football, t_cat_guitar, inventors_robot.

sb_can_cant_kids, she_cant_skip и she_cant_ride_horse в PDF лежат с маской
прозрачности — `sm1_pdf_frames.py` её не учитывает, эти три сведены на белый
фон отдельно.

## Доработать руками

### Что нужно от вас — весь список

| # | Урок · блок | Что сделать |
|---|---|---|
| 1 | HW2 · 4 | прислать видео про животных → `sm1_u8_hw2_b4` |
| 2 | HW2 · 7 | прислать аудио «Боб рассказывает, что умеет» → `sm1_u8_hw2_b7`; картинки Боба в выгрузке нет — нужна ли? |
| 3 | HW3 · 4 | прислать видео «Can you …?» → `sm1_u8_hw3_b4` |
| 4 | HW3 · 8 | прислать аудио «что умеет мой монстрик» → `sm1_u8_hw3_b8` |
| 5 | HW4 · 4 | прислать аудио истории «The Problem» → `sm1_u8_hw4_b4` |
| 6 | HW4 · 9 | прислать интерактивное видео (2:11) → `sm1_u8_hw4_b9` и тексты шести вопросов к нему (0:13 верно/неверно, 0:14, 0:48, 1:37, 1:47 — выбор варианта, 1:54 — открытый вопрос): в выгрузке только типы и таймкоды |
| 7 | HW5 · 11 | прислать аудио «как я описала своего питомца» → `sm1_u8_hw5_b11` |
| 8 | Test · 11 | прислать аудио разговора Лили и Тома → `sm1_u8_test_b11` |
| 9 | HW2 | пустой блок «Найди пару» после видео (I can swim / I can't walk / I can climb trees / I can't fly / I can ski / I can't stop — без картинок) не перенесён: прислать картинки к нему или решить, что без него |
| 10 | HW1 | в выгрузке только часть (1) — словарный тренажёр; будет ли часть (2)? |
| 11 | HW6 | в выгрузке только часть (1) — тренажёр на 6 слов движения; будет ли часть (2)? Переводы слов наши (в выгрузке заглушка «Определение») — проверить |
| 12 | HW2 · 8, 9 | Wordwall пересобраны, обложки пустые — СОСТАВ МОЙ, посмотреть |
| 13 | HW3 · 9–12 | Wordwall пересобраны, обложки пустые — СОСТАВ МОЙ, посмотреть |
| 14 | HW5 · 12, 13 | Wordwall пересобраны по тексту форума, обложки пустые — СОСТАВ МОЙ, посмотреть |
| 15 | HW7 · 6–9 | Wordwall «Voc spelling» и «Can / Can't» (Unjumble) пересобраны — СОСТАВ МОЙ, посмотреть |
| 16 | HW4 · 6 | в выгрузке точки «Диаграммы» стояли неверно (3 и 4 на одном кадре) — расставлены по содержанию, проверить |
| 16а | HW4 · 6 | на перемешанной картинке в углах кадров видны их номера из учебника (2, 3, 7, 6 / 4, 5, 1, 8) — задание решается подглядыванием; так было и в выгрузке. Оставить или закрасить номера? |
| 17 | Test · 1 | маски с пропущенными буквами наши — проверить |
| 18 | все | название юнита «Unit 8 · My body» — сверить с учебником |
| 19 | все | нажать «Озвучить пачкой» (размечено `audio_tts`) — по решению Анны, когда понадобится |
| 20 | все | после проверки включить публикацию (заливаем скрытыми) |

### По урокам

**HW2.** Блок 6: у четырёх предложений в выгрузке были свои картинки, в
PDF дошла одна обрезанная — поставлены наши (клипарт HW3, she_cant_skip,
ab_can_ski). Блок 8 — match «картинка ↔ I can / can't …» на клипарте HW3;
блок 9 — quiz «A fish ___ swim» и т. п.

**HW3.** Блок 9 — quiz «Can a fish swim?» …; блоки 10–12 — три «Составь
предложение».

**HW4.** Перемычка — блок 8. Блок 9 — интерактивное видео, вопросы внутри
видео в нашем плеере не работают; если нужны — сделаем отдельными
блоками после видео, когда придут тексты.

**HW5.** В блоке 3 картинки к «Can she dance?», «Can he ride his bike?»,
«Can this dog swim?» в выгрузке не дошли — наши, с животными. Блок 12 —
gaps can / can't по тексту форума, блок 13 — match описание ↔ имя
питомца.

**HW7.** Блок 6 — exact_input «впиши слово по картинке»; блоки 7–9 —
«Составь предложение».

**Test.** Блок 8: фото ребёнка с воздушным змеем заменено на kite_sky.
Реклама для родителей из домашек не перенесена ни в один урок.

## Проверка

`python3 tools/sm1_build.py --check-all` по u8: все ошибки — только «нет
файла» под 20 будущих картинок из листов Л8.1–Л8.3 (body_* ×9, move_* ×6,
ab_can_ski, ab_cat_dance, ab_bear_cant_ride_bike, ab_dog_swim, kite_sky).
Других ошибок нет. u8_hw3 и u8_hw4 проходят полностью.
