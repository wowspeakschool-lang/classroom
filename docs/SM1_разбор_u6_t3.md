# Super Minds 1 — разбор Unit 6 и теста Unit 3

Разбор выгрузки ShkolaApp, шаг 2 регламента: **в базу ничего не залито**.
Сборка уроков — `tools/sm1/u6.py`, `tools/sm1/u3.py`; картинки из PDF — `media/sm1/u6/`,
`media/sm1/u3/`. Номера блоков везде **как в редакторе** (`sort_order + 1`).

| Урок | Ключ | Блоков | Откуда |
|---|---|---|---|
| Unit 6 · Homework 1 | `u6_hw1` | 15 | `Homework 1 (1)` — только словарный тренажёр |
| Unit 6 · Homework 2 | `u6_hw2` | 12 | `Homework 2` |
| Unit 6 · Homework 4 | `u6_hw4` | 11 | `Homework 4` |
| Unit 6 · Homework 7 | `u6_hw7` | 11 | `Homework 7` |
| Unit 6 · Unit 6 Test | `u6_test` | 12 | `Super Minds 1 Unit 6 Test` |
| Unit 3 · Unit 3 Test | `u3_test` | 11 | `Super Minds 1 Unit 3 Test` |

Homework 3, 5, 6 юнита 6 в выгрузке нет — уроки пропущены, номера не сдвигались
(HW4 — `sort_order` 3, HW7 — 6, тест — 7).

`python3 tools/sm1_build.py --check-all`: по моим урокам ошибок, кроме «нет файла» под
листы Л6.1, ЛТ6.1, ЛТ3.1 — **ноль**. HW2 и HW4 проходят полностью.

---

## Unit 6 · Homework 1 — `u6_hw1`

Слова: bathroom, bedroom, living room, hall, dining room, kitchen, stairs, cellar.
Задания тренажёра (Запомни · Послушай · Найди пару · Скрэмбл · Тест) переложены
штатными блоками, как в уже залитом Unit 3 HW1.

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие + картинка дома | выгрузка, текст; `house_outside` — Л6.1 |
| 2 | flashcards | 8 комнат, перевод, `audio_tts` | «Запомни»; картинки Л6.1 |
| 3 | quiz | «Послушай слово и выбери» ×8 | «Послушай» |
| 4 | match | слово ↔ перевод | «Найди пару» |
| 5–12 | order | собери слово из букв ×8, с картинкой | «Скрэмбл» |
| 13 | quiz | картинка → слово ×8 | «Тест» |
| 14 | exact_input | перевод → слово ×8 | «Тест» (Введи слова) |
| 15 | text | прощание | моё |

Из приветствия убрана фраза про «ДОПОЛНИТЕЛЬНОЕ задание»: оно было во второй части.

## Unit 6 · Homework 2 — `u6_hw2`

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие | бл. 1–2 выгрузки |
| 2 | text | «Давай повторим…» + карточка `grammar_there_is_are` | бл. 2, x209 |
| 3 | video | девочка описывает любимую комнату | бл. 3–4 (файла нет) |
| 4 | match | There is → one bed. · There are → two pillows. | бл. 5 |
| 5 | hotspot | 6 предметов (`food_numbered`), точки по меткам PDF | бл. 6 «Диаграмма» |
| 6 | text | переход + картинка `cats_house` | бл. 7–8 |
| 7 | truefalse | 5 утверждений: T F F F T | бл. 8 (5 отдельных блоков) |
| 8 | text | «рисунок моего домика» `my_house_drawing` | бл. 9 |
| 9 | speaking | расскажи про свой дом, `sample_tts` | бл. 10 |
| 10 | match | ⭐ картинки ↔ There is/are — **СОСТАВ МОЙ** | бл. 11 Wordwall |
| 11 | quiz | ⭐ There is / There are ×6 — **СОСТАВ МОЙ** | бл. 12 Wordwall |
| 12 | text | прощание | бл. 13 |

## Unit 6 · Homework 4 — `u6_hw4`

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие | бл. 1–2 (рекламная картинка «для родителей» не взята) |
| 2 | text | карточка `story_key_phrases` | бл. 3, x220 |
| 3 | text | друзья идут в жуткий дом + `haunted_house` | бл. 4–5 |
| 4 | video | аудио истории (файла нет) | бл. 6 |
| 5 | quiz (multiple) | какие слова есть в истории: house, stairs, cellar | бл. 7; ключ по PDF |
| 6 | text | история целиком `story_old_house` | бл. 8–9 |
| 7 | hotspot | кадры вперемешку → Picture 1…8 | бл. 10 |
| 8 | match | реплика → герой (4 пары) | бл. 11 |
| 9 | video | ⭐ мультфильм по истории (файла нет) | бл. 12 |
| 10 | sequence | 9 реплик в порядке видео | бл. 13 |
| 11 | text | прощание | бл. 14 |

В бл. 7 номера кадров стояли прямо на картинке и выдавали ответ — закрасил их
(`story_old_house_shuffled`), точки поставил в центры кадров.

## Unit 6 · Homework 7 — `u6_hw7`

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие | бл. 1 (картинка-мальчик не взята) |
| 2 | quiz | картинка комнаты → слово ×4 (cellar, hall, stairs, dining room) | бл. 2, x208/232/247/256 |
| 3 | gaps | There’s / There are ×6 | бл. 3 |
| 4 | quiz | Is there…? ×3 | бл. 4 (3 блока) |
| 5–7 | order | 3 вопроса/предложения | бл. 5 |
| 8 | speaking | опиши дом `house_rooms`, 5–7 предложений | бл. 6 |
| 9 | match | ⭐ комната ↔ слово — **СОСТАВ МОЙ** (Wordwall «SM1 U6 matching») | бл. 7 |
| 10 | quiz | ⭐ There’s/There are, Is/Are there ×6 — **СОСТАВ МОЙ** (Wordwall «SM1 U6 there is / there are») | бл. 7 |
| 11 | text | прощание | бл. 8 |

## Unit 6 Test — `u6_test`

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | exact_input | 8 комнат по переводу | бл. 1 словарный тест |
| 2 | match | картинка → слово (6 комнат) | бл. 2; картинок в выгрузке нет, Л6.1 |
| 3 | quiz | 5 вопросов «выбери вариант», с картинками | бл. 3 (выпадающие списки) |
| 4–8 | order | 5 предложений с картинками | бл. 4 |
| 9 | gaps (drag) | текст про дом Бена, 5 пропусков | бл. 5 |
| 10 | video | диалог Тома и Сары (аудио, файла нет) | бл. 6 |
| 11 | truefalse | 5 утверждений: F T F T T | бл. 6 |
| 12 | speaking | опиши картинку `test_fishing_scene` | бл. 7 |

## Unit 3 Test — `u3_test`

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | exact_input | 9 животных по переводу | бл. 1 словарный тест |
| 2 | match | картинка → слово (6 животных) | бл. 2; картинок в выгрузке нет, ЛТ3.1 |
| 3 | speaking | прочитай 5 предложений вслух | бл. 3 |
| 4 | quiz | 5 вопросов «выбери вариант», с картинками | бл. 4 |
| 5–9 | order | 5 предложений с картинками | бл. 5 |
| 10 | gaps (drag) | где животные (5 пропусков) + `test_animals_where` | бл. 6 |
| 11 | speaking | расскажи, кто где, `test_attic_animals` | бл. 8 |

Бл. 7 выгрузки (LISTENING) по-настоящему пустой — в урок не положен, см. доработку.

---

## Промпты на картинки

Строки стиля (уже вклеены в промпты):

* **ПРЕДМЕТ:** Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left.
* **СЦЕНА:** Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, one single scene filling the frame, no people.

### 1. Обязательные — картинок нет

#### Л6.1 · Комнаты дома — 9 карточек (3×3)
Режется: `room_bathroom`, `room_bedroom`, `room_living_room` · `room_hall`, `room_dining_room`,
`room_kitchen` · `room_stairs`, `room_cellar`, `house_outside` → `media/sm1/u6/`.
Где: HW1 бл. 1, 2, 5–14; HW7 бл. 9; Unit 6 Test бл. 2.
```
A sheet of 9 separate picture cards in a 3 x 3 grid. Each card is a small cosy room seen as an open cutaway box from a three-quarter view (two walls and a floor), so the room type is obvious at a glance.
Row 1, left to right: a bathroom with a bathtub, a toilet and a washbasin; a bedroom with a bed, a pillow and a bedside lamp; a living room with a sofa, an armchair and a television.
Row 2, left to right: a hall with a front door, a coat rack with coats and a doormat; a dining room with a table, four chairs and plates on the table; a kitchen with a cooker, a fridge and a sink.
Row 3, left to right: a wooden staircase going up to the next floor; a dim cellar with stone walls, a few steps leading up, boxes and old barrels; the outside of a cute two-storey family house with a red roof and a front door.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge. No text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces. Generic design, not resembling any real product.
Output size: 1536 x 1536 px.
```

#### ЛТ6.1 · Картинки к «Составь предложение» теста — 4 карточки (2×2)
Режется: `test_frog_piano`, `test_park_empty` · `test_kitten_kitchen`, `test_books_bedroom` → `media/sm1/u6/`.
Где: Unit 6 Test бл. 4, 7, 6, 8. Почему обязательно: в выгрузке лягушка сидит на ветке, а не на
пианино; вместо парка — фото фирменного карта (виден логотип); вместо книг в спальне — фото
девочки-подростка.
Котёнок из PDF снят крупным планом, кухни на фото нет — тоже заменяем.
```
A sheet of 4 separate picture cards in a 2 x 2 grid.
Row 1, left to right: a happy green frog sitting on top of a small upright piano; an empty sunny park with green trees, a path and a bench, with no cars and no go-karts.
Row 2, left to right: a fluffy kitten sitting on a kitchen floor next to a cooker and a fridge; a tall pile of colourful books lying on a bed in a bedroom.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge. No text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces. Generic design, not resembling any real product.
Output size: 1536 x 1536 px.
```

#### ЛТ3.1 · Животные Unit 3 — 9 карточек (3×3)
Режется: `animal_elephant`, `animal_rat`, `animal_lizard` · `animal_frog`, `animal_spider`, `animal_dog` ·
`animal_cat`, `animal_duck`, `animal_donkey` → `media/sm1/u3/`.
Где: Unit 3 Test бл. 2 (6 из 9; остальные три — в запас для «Unit 3», в старых уроках
картинки только в base64).
```
A sheet of 9 separate animal cards in a 3 x 3 grid, each animal shown whole, standing, friendly and smiling.
Row 1, left to right: a grey elephant; a grey rat; a green lizard.
Row 2, left to right: a green frog; a black spider; a brown dog.
Row 3, left to right: a ginger cat; a white duck with an orange beak; a grey donkey.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge. No text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces.
Output size: 1536 x 1536 px.
```

### 2. По желанию — в выгрузке стоковое фото, ответы не пострадают

#### ЛТ6.2 · Фото к квизу теста Unit 6 — 6 карточек (2×3)
Режется (заменяет файлы с тем же именем): `test_pears`, `test_lizard`, `test_plane` ·
`test_crocodile`, `test_bikes`, `test_dogs` → `media/sm1/u6/`. Где: Unit 6 Test бл. 3, 5.
Сейчас стоят фото и клипарт разного стиля.
```
A sheet of 6 separate picture cards in a grid of 2 rows and 3 columns.
Row 1, left to right: an open fridge with yellow pears on the shelf; a green lizard; a passenger plane flying in a blue sky with small clouds.
Row 2, left to right: a green crocodile; two bicycles standing side by side on grass; four puppies sitting in a row.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge. No text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces. Generic design, not resembling any real product.
Output size: 1536 x 1024 px.
```

#### ЛТ3.2 · Фото к тесту Unit 3 — 3 карточки (1×3)
Режется (заменяет): `test_dogs`, `test_dog_desk`, `test_cat` → `media/sm1/u3/`.
Где: Unit 3 Test бл. 4 (вопрос 5), бл. 8, бл. 9. На `test_dog_desk` сейчас видны ноги человека.
```
A sheet of 3 separate picture cards in one row.
Row 1, left to right: five different puppies sitting in a row; a fluffy dog sitting under a wooden desk; a happy white and grey cat.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge. No text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces.
Output size: 1536 x 1024 px.
```

#### Л6.2 · Жуткий дом (сцена)
Файл: `haunted_house` (заменяет клипарт 243 px) → `media/sm1/u6/`. Где: HW4 бл. 3.
```
A spooky but friendly old two-storey house at night on a small hill, crooked windows glowing warm yellow, bare twisted trees, a full moon, a few bats in the sky, an old fence. Not scary, cosy and fun for young children.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, one single scene filling the frame, no people. No text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces.
Output size: 1536 x 1024 px.
```

### 3. Не перерисовывать — вырезано из PDF

`media/sm1/u6/`: `grammar_there_is_are`, `food_numbered`, `food_bananas`, `food_sandwich`, `food_doll`,
`food_apples`, `food_sausages`, `food_dog` (вырезаны из `food_numbered`), `cats_house`, `my_house_drawing`,
`story_key_phrases`, `haunted_house`, `story_old_house`, `story_old_house_shuffled` (номера закрашены),
`room_cellar_hw7`, `room_hall_hw7`, `room_stairs_hw7`, `room_dining_hw7`, `house_rooms`,
`test_pears`, `test_lizard`, `test_plane`, `test_crocodile`, `test_bikes`, `test_dogs`,
`test_fishing_scene` — 26 файлов.

`media/sm1/u3/`: `test_elephant_plane`, `test_frog_table`, `test_rat_bag`, `test_spider`, `test_dogs`,
`test_elephants_ruler`, `test_lizards`, `test_ducks_books`, `test_dog_desk`, `test_cat`,
`test_animals_where`, `test_attic_animals` — 12 файлов.

Не взяты: галерея фонов 900×506, приветствия/прощания (миньоны, Микки, Спанч Боб — заменены
на `media/shared/`), реклама «для родителей» (HW4), мальчик-исследователь (HW7), фото девочки с
книгами и фото карта Ninebot (Unit 6 Test), лягушка на ветке и котёнок крупным планом (не совпадают с предложениями).

---

## Доработать руками

### Что нужно от вас — весь список

| Урок | Блок | Что сделать |
|---|---|---|
| U6 HW1 | — | В выгрузке только часть (1), словарный тренажёр. Части (2) нет — пришлите, если она была, добавлю в этот же урок |
| U6 HW3, HW5, HW6 | — | В выгрузке их нет совсем — пришлите, если есть |
| U6 HW2 | 3 | Видео «девочка описывает любимую комнату» → `sm1_u6_hw2_b3.mp4` |
| U6 HW2 | 9 | Образец ответа к записи голоса в выгрузке пустой — размечен `sample_tts`, можно озвучить пачкой или прислать `sm1_u6_hw2_b9.mp3` |
| U6 HW2 | 10, 11 | Игры Wordwall, обложки пустые — пересобрал сам, **СОСТАВ МОЙ**, посмотрите |
| U6 HW4 | 4 | Аудио истории «The old house» → `sm1_u6_hw4_b4.mp3` |
| U6 HW4 | 9 | Мультфильм по истории → `sm1_u6_hw4_b9.mp4` |
| U6 HW4 | 7 | Номера кадров на картинке закрашены (выдавали ответ) — проверьте, что так и задумано |
| U6 HW7 | 9, 10 | Игры Wordwall «SM1 U6 matching» и «SM1 U6 there is / there are» — пересобрал, **СОСТАВ МОЙ** |
| U6 Test | 10 | Аудио диалога Тома и Сары → `sm1_u6_test_b10.mp3` |
| U6 Test | 2 | В выгрузке у «Соедини слова с картинками» нет картинок — поставлены карточки Л6.1 |
| U6 Test | 8 | Опечатка выгрузки «any book» исправлена на «any books» |
| U6 Test | 9 | В выгрузке в банке слов было лишнее «are» — в нашем блоке лишних слов нет, задание стало без «ловушки» |
| U6 Test | 3 | Выпадающие списки заменены квизом: в вопросе с двумя пропусками варианты даны парой |
| U3 Test | — | Бл. 7 LISTENING «Какое животное нравится каждому ребёнку?» (Tom, Lucy, Ben, Ann, Kim): справа плейсхолдеры, аудио нет — **в урок не положен**. Пришлите аудио и ответы — добавлю match + аудио (`sm1_u3_test_b11.mp3`, перед speaking) |
| U3 Test | 2 | Картинок у «Соедини слова с картинками» в выгрузке нет — карточки ЛТ3.1 |
| U3 Test | 6 | В выгрузке «I don't like lizards, too.» — с отрицанием так нельзя; оставил «I don't like lizards.» Можно вернуть «…, either.» |
| U3 Test | 4 | В вопросе 2 текст «under the desk», а на картинке стол — оставил как в выгрузке |
| все | — | Нажать «Озвучить пачкой» (размечено `audio_tts`/`sample_tts`) |
| все | — | Включить публикацию — уроки зальются скрытыми |
| все | — | Картинки по листам Л6.1, ЛТ6.1, ЛТ3.1 (обязательно), ЛТ6.2, ЛТ3.2, Л6.2 (по желанию) |

Подробности по урокам — в таблицах блоков выше.

---

## Странности, найденные по дороге

1. **`truefalse` в SM3 размечены не тем полем.** Сервер (`classroom_submit_block`) и редактор берут
   верный ответ из `statements[].correct`, а `tools/sm3_build.py` пишет `answer`. Значит, во всех
   truefalse-блоках SM3 сервер считает все утверждения «неверными» и засчитывает ответ «Неверно».
   В SM1 (база и мои уроки) — `correct`, всё правильно. Чужой файл не трогал.
2. **`order` из букв не проходит `check()`**, если `sentence` — слово целиком: проверка клеит буквы
   через пробел. В моих уроках `sentence` = буквы через пробел — так же делает редактор
   (`edOrder` режет `sentence` по пробелам). Сервер оценивает по `words`, `sentence` не читает.
3. **У `truefalse` в прохождении нет ни картинки, ни звука** — картинку кладу в text перед блоком,
   аудио — блоком video перед ним.
4. **Название юнита «Unit 6 · My house»** — по теме словаря; сверить с оглавлением учебника.
