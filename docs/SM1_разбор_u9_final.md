# Super Minds 1 — разбор Unit 9 и Final Test

Шаг 2 регламента: выгрузка разобрана, уроки описаны в `tools/sm1/u9.py` и
`tools/sm1/final.py`, картинки из PDF вырезаны в `media/sm1/u9/` и
`media/sm1/ft/`. В базу ничего не залито.

Выгрузка ShkolaApp, файлы Drive — `docs/SM1_выгрузка_файлы.md` (папки `Unit 9`
и `Test SM1/Final`). Скачанное лежит в скретчпаде агента (`agent_u9/dl/`).

| Ключ | Урок | Блоков | Что есть в выгрузке |
|---|---|---|---|
| `u9_hw1` | Homework 1 | 10 | части (1) + (2), догружены 07.10 в корень SM1 |
| `u9_hw2` | Homework 2 | 10 | целиком |
| `u9_hw3` | Homework 3 | 9 | целиком |
| `u9_hw4` | Homework 4 | 10 | целиком |
| `u9_hw5` | Homework 5 | 11 | целиком, догружена 07.10 |
| `u9_hw6` | Homework 6 | 12 | части (1) + (2); (1) догружена 07.10 |
| `u9_hw7` | Homework 7 | 7 | целиком, догружена 07.10 |
| `u9_test` | Unit 9 Test | 14 | целиком |
| `final_test` | Final Test (юнит `Final Test`, unit_sort 10) | 6 | Listening + Reading-Writing; 5 заданий Listening пустые |

Homework 1, 5, 7 и HW6 (1) догружены вторым заходом (корень папки SM1, id —
`docs/SM1_выгрузка_файлы.md`, раздел «Догружено»). `lesson_sort` = K − 1, тест — 7.

Догруженные файлы — **другой вид выгрузки**: «ученический» вид VZNANIYA
(Interactive lesson / Memorization), а не редактор. Верные ответы отмечены
только в HW7 (галочки у вариантов True/False); в HW5 ответы восстановлены
по картинкам, в HW5 бл. 16 — угаданы (см. «доработать»). Словарные тренажёры
HW1 (1) и HW6 (1) выгружены со **свёрнутым списком слов**: видно только
«Words 9» / «Words 7» и названия заданий. Слова взяты из материала юнита
(9 занятий на море — те же, что в словаре теста и в HW7; 7 мест — те же,
что в HW6 (2)), задания тренажёра пересобраны штатными блоками — СОСТАВ МОЙ.

Название юнита — **`Unit 9 · Holidays`** (лексика: пляж, горы, кемпинг, парк
развлечений; Let's…; Where's…?). По учебнику не сверено — см. «доработать».

Во всех домашках из урока выброшен блок-реклама для родителей
(«3 бесплатных урока по реферальной программе», в HW3 ещё «Новогодний
розыгрыш призов») и «робуксы» за задания. Декоративные картинки (речевой
пузырь, Спанч Боб, Скрудж Макдак, лайк) заменены общими `media/shared/`.

Номера блоков ниже — **как в редакторе** (sort_order + 1).

---

## u9_hw1 · Homework 1 (части 1 + 2)

Часть (1) — тренажёр «Memorization» на 9 слов: Remember, Listen, Match;
дополнительные — Unscramble, Fill in (+ Final test тренажёра, не переносим).
Часть (2) — «Interactive lesson»: бл. 1 фото «Hello» на песке + реклама
(выброшены), бл. 2 приветствие, бл. 3 **раскраска (выброшена)**, бл. 4
нарисуй свой отдых, бл. 5 прощание.

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие «я не знаю человека, который не любил бы море» | (1), Teacher's note |
| 2 | flashcards | 9 занятий с переводом и картинкой `act_*`, `audio_tts` | (1), список слов — **СОСТАВ МОЙ**; картинки ЛТ9.1 + Л9.4 |
| 3 | quiz | «Как по-английски …?» ×9 | (1) «Remember» |
| 4 | quiz | «Послушай и выбери» ×9, `audio_tts` | (1) «Listen» |
| 5 | match | картинка ↔ фраза ×9 | (1) «Match» |
| 6 | exact_input | собери слова из букв ×9 | (1) доп. «Unscramble» |
| 7 | exact_input | впиши пропущенные буквы ×9, с картинкой | (1) доп. «Fill in» |
| 8 | text | перемычка: «вторая, ДОПОЛНИТЕЛЬНАЯ часть» | (2) бл. 2 |
| 9 | task | доп.: нарисуй свой отдых на море, пришли рисунок; пример `hw1_drawing_example` | (2) бл. 4 |
| 10 | text | прощание | (2) бл. 5 |

## u9_hw2 · Homework 2

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие, «в конце есть дополнительное задание» | бл. 1 + текст бл. 2 (картинка-реклама выброшена) |
| 2 | text | «подружки решают, чем заняться» + картинка `hw2_friends_talk` | бл. 3 |
| 3 | video | видео с подружками — **пустой url** | бл. 4 |
| 4 | match | Let's eat ice cream → Good idea! и ещё 2 пары | бл. 5 |
| 5 | match | 6 кадров `hw2_lets_*` → Let's go swimming / listen to music / take a photo / paint a picture / go to the park / look for shells | бл. 6 «Диаграмма», кадры вырезаны |
| 6 | match | 3 смайлика `smile_*` → Sorry, I don't want to / I'm not sure / Good idea! | бл. 7 «Диаграмма» |
| 7 | gaps (drag) | 4 мини-диалога, 8 пропусков, картинка `hw2_beach_umbrella` | бл. 8 |
| 8 | sequence | диалог из 6 реплик по аудио, `audio_tts` | бл. 9 (текст) + бл. 10 |
| 9 | task | доп. задание: составь свой диалог | бл. 11 «Открытый вопрос» |
| 10 | text | прощание | бл. 12 |

## u9_hw3 · Homework 3

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие | бл. 1 + текст бл. 2 (реклама выброшена) |
| 2 | text | «где спрятался котик?» + `hw3_cat` | бл. 3 |
| 3 | video | видео «где котик» — **пустой url** | бл. 4 |
| 4 | match | Where are the candies? → They're in the jar. + 3 пары | бл. 5 |
| 5 | text | картинка `hw3_where_photos` (4 стоковых фото) | бл. 6 |
| 6 | match | Where are the shells? → They're in the box. + 3 пары | бл. 6 |
| 7 | task | рюкзаки `hw3_bags`: ответь на 5 вопросов (1-й — пример) | бл. 7 «Открытый вопрос» |
| 8 | task | дом `hw3_house`: составь вопросы про crocodiles, cat, spider, snake и ответь | бл. 8 «Открытый вопрос» |
| 9 | text | прощание | бл. 9 (бл. 10 — реклама, выброшен) |

## u9_hw4 · Homework 4

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие | бл. 1 (бл. 2 — реклама, выброшен) |
| 2 | text | «кто первым доберётся до вершины?» + `hw4_flash_running` | бл. 3 |
| 3 | video | **аудио** истории «The top of the hill» — пустой url | бл. 4 |
| 4 | sequence | 6 фраз истории по порядку, картинка `hw4_friends` | бл. 5 |
| 5 | text | история целиком: `hw4_story_1`, `hw4_story_2` (кадры с репликами) | бл. 7 + бл. 8 (бл. 6 — битая картинка, выброшен) |
| 6 | sequence | 8 кадров `hw4_frame_1…8` расставить по порядку | бл. 9 «Диаграмма» (Picture #1…#8) |
| 7 | text | «история ожила — мультик», доп. задание + `hw4_video_cover` | бл. 10 |
| 8 | video | мультфильм — **пустой url** | бл. 11 |
| 9 | gaps (drag) | 7 фраз, 8 пропусков (go, top, good, walk, run, race, together, idea) | бл. 12 |
| 10 | text | прощание | бл. 13 |

Порядок кадров в бл. 6 снят с номеров точек на странице PDF и сверен с
комиксом: 1 — «A race?», 2 — Flash убегает, 3 — «A race is not a good idea»,
4 — пещера/камень, 5 — «end of the race», 6 — «Let me try», 7 — Thunder держит
камень, 8 — «What a good idea!».

## u9_hw5 · Homework 5

Выгрузка: 21 блок. Не перенесены: бл. 1 (фото «hello» с ракушками), бл. 2
(реклама), «ракушки в коллекцию» за задания (бл. 9, 14, 17, 18 — картинки
ракушек) и стоковое фото в прощании.

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие | бл. 3 |
| 2 | quiz | True/False ×4 с картинками: She is eating ice-cream ✅ (`hw5_girl_icecream`), She is reading a book ❌ (`act_listen_music`), They are making a sandcastle ✅ (`act_make_sandcastle`), He is taking a photo ❌ (`act_catch_fish`) | бл. 4–8 |
| 3 | order | She is painting a picture. + `act_paint_picture` | бл. 10 |
| 4 | order | He is taking a photo. + `act_take_photo` | бл. 11 |
| 5 | order | They are looking for shells. + `act_look_shells` | бл. 12 |
| 6 | order | She is reading a book. + `act_read_book` | бл. 13 |
| 7 | video | **аудио** «как зовут детей» — пустой url | бл. 15 |
| 8 | hotspot (label) | пляж `hw5_beach_kids`, 5 имён: Tom, Jim, Sue, Mia, Bob — **распределение угадано** | бл. 16 «Диаграмма» |
| 9 | text | «основная часть выполнена, осталось доп. задание» | бл. 17–18 |
| 10 | speaking | доп.: опиши, что делают люди на пляже, картинка `hw5_beach_scene`; образец `sample_tts` наш | бл. 19–20 |
| 11 | text | прощание | бл. 21 |

Бл. 2: выгрузка «ученическая», отметок верного нет — ответы по картинкам
(девочка с мороженым; девочка в наушниках; семья строит замок; мальчик с
удочкой). В инструкции выгрузки упомянут вариант «Not stated», но кнопок
у заданий только две — True/False, упоминание убрано. Фото детей (бл. 6–8,
10–13) заменены картинками тех же занятий без людей — ответы не меняются.

Бл. 8: точки сняты с маркеров на картинке (в процентах): мальчик с удочкой
(19, 44), мальчик с мороженым (36, 77), девочка с фотоаппаратом (50, 64),
девочка в наушниках (67, 78), мальчик у замка из песка (87, 55). Кто есть
кто — только в аудио, которого нет; взяли: мальчики Tom, Jim, Bob, девочки
Sue, Mia — **сверить по аудио**.

## u9_hw6 · Homework 6 (части 1 + 2)

Часть (1) — тренажёр «Memorization» на 7 слов: Cards, Remember, Find the
definition, Listen (+ Final test тренажёра). Txt у неё 203 байта, в PDF две
страницы — шапка и дорожка заданий, список слов свёрнут. Приветствия нет.

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие — **наше** (в части (1) его нет) | — |
| 2 | flashcards | 7 мест `place_*` с переводом, `audio_tts` | (1) «Cards», список слов — **СОСТАВ МОЙ**; картинки Л9.1/Л9.2 |
| 3 | quiz | «Как по-английски …?» ×7 | (1) «Remember» |
| 4 | quiz | «Что значит …?» ×7, с картинкой | (1) «Find the definition» |
| 5 | quiz | «Послушай и выбери» ×7 | (1) «Listen» |
| 6 | text | перемычка: «уверена, что ты хорошо выучил новые слова» | (2) бл. 1 + текст бл. 2 |
| 7 | match | 7 пейзажей `place_*` → mountains, countryside, beach, city, theme park, campsite, lake | (2) бл. 2 — **картинок в выгрузке нет**, лист Л9.1/Л9.2 |
| 8 | match | те же пейзажи → We can go to shops / climb up / make a sandcastle / go on a boat / sleep in a tent / ride on fun things / see lots of trees here | (2) бл. 3 «Диаграмма», картинки нет |
| 9 | gaps (drag) | **СОСТАВ МОЙ**: имя дано, ученик вставляет место (campsite, city, mountains, beach, countryside) | (2) бл. 4 «выбери имя по картинке» — картинки нет |
| 10 | gaps (drag) | I like the mountains… 5 пропусков | (2) бл. 5 |
| 11 | task | доп. задание: расскажи о любимых местах | (2) бл. 6 «Открытый вопрос» |
| 12 | text | прощание | (2) бл. 7 |

Соответствие «место → занятие» в бл. 8 восстановлено по смыслу (в выгрузке
точки стоят на пустом месте картинки, которой нет): shops — city, climb up —
mountains, sandcastle — beach, boat — lake, tent — campsite, fun things —
theme park, trees — countryside.

## u9_hw7 · Homework 7

Выгрузка: 7 блоков, повторение перед тестом. Верные True/False отмечены
галочками у вариантов.

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие «повторяем всё перед тестом» | бл. 1 (картинка-мальчик → общая) |
| 2 | quiz | «послушай и выбери фразу» ×9, `audio_tts` | бл. 2 «Найди пару» на слух (9 кнопок-аудио ↔ 9 фраз) |
| 3 | quiz | True/False ×3: The boy is reading a book ❌ (`hw7_boy_guitar`), The girl is listening to music ✅ (`hw7_girl_music`), The boy is catching a fish ✅ (`hw7_boy_fishing`) | бл. 3 |
| 4 | gaps (drag) | 5 мини-диалогов Let's… – Good idea!, 10 пропусков (listen, idea, picture, sure, eat, Good, catch, Sorry, Let's, shells) | бл. 4 |
| 5 | quiz | 3 вопроса: Where's the shell? → It's on the rocks; Where are the kites? → They aren't in the box…; Where's my hat? → It isn't in my bag… | бл. 5 |
| 6 | speaking | «Где что?» — 6 вопросов по картинке `hw7_where_tiles` | бл. 6 |
| 7 | text | прощание | бл. 7 (Микки Маус → общая картинка) |

Бл. 2: девятая карточка фразы попала на стык страниц PDF и пустая; это
**eat ice cream** — единственное слово словаря, которого нет среди восьми
видимых. Бл. 5: верные — по грамматике (it/they), отметок в выгрузке нет;
позицию верного развели (1, 0, 1).

## u9_test · Unit 9 Test (kind `test`, без приветствия и прощания)

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | exact_input | 9 слов: «Напиши по-английски: поймать рыбу» … «играть на гитаре» | бл. 1 (словарный «Заполни пропуски») |
| 2 | match | 6 картинок `act_*` → paint a picture, listen to music, catch a fish, take a photo, look for shells, make a sandcastle | бл. 2 — **картинок нет**, лист ЛТ9.1 |
| 3 | quiz | 5 вопросов «выбери подходящий вариант» с картинками: Good / sure / It's / don't want to / They are | бл. 3 (5 подзаданий) |
| 4 | order | Where is the dog? + `test_dog` | бл. 4.1 |
| 5 | order | Where are your pink shoes? + `test_pink_shoes` | бл. 4.2 |
| 6 | order | The blue crocodiles are in the bathroom. + `test_blue_crocodile` | бл. 4.3 |
| 7 | order | Let's take a photo! + `test_selfie` | бл. 4.4 |
| 8 | order | They are on my head. — **без картинки** (в выгрузке фото взрослой женщины, не берём) | бл. 4.5 |
| 9 | video | **аудио** «Бен и его семья на пляже» — пустой url | бл. 5 (аудио) |
| 10 | quiz | 5 вопросов по аудио; верные b, c, a, c, a | бл. 5 |
| 11 | text | открытка Эммы `test_postcard` | бл. 6 (картинка) |
| 12 | gaps (type) | 5 пропусков: swim, on, under, painting, read | бл. 6 |
| 13 | speaking | Part 1: 7 вопросов «Where is…?» по картинке `test_beach_scene` | бл. 7 |
| 14 | speaking | Part 2: предложи 3–4 занятия (Let's…) | бл. 8 |

Верные варианты бл. 3: в «Выбери правильный вариант» ShkolaApp верный —
основной, остальные — «альтернативные»; сверено по PDF. Бл. 10: у верного
варианта нет пустого чекбокса, вырезано и увеличено.

## final_test · Final Test (юнит `Final Test`, kind `test`)

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | video | **аудио** Listening, 2:46 — пустой url | Listening, бл. 1 |
| 2 | hotspot (label) | пикник `ft_picnic`, 5 точек: Jane, Mike, Laura, Clare, Paul | Listening, бл. 1 «Диаграмма» |
| 3 | quiz | 5 вопросов ✅/❌ с картинками: ruler ❌ (на фото ластик), spider ✅, bike ✅, face ❌ (на фото рука), chicken ✅ | Reading-Writing, бл. 1–5 |
| 4 | text | картинка `ft_kitchen` (семья за завтраком) | RW, бл. 6 |
| 5 | truefalse | banana on the table — верно; bedroom — неверно; 1 girl — верно; red lamp under the table — неверно; one chair — неверно | RW, бл. 6 |
| 6 | exact_input | 5 слов по картинке и буквам: pencil, monster, duck, bathroom, sweater | RW, бл. 7–11 «Открытый вопрос» |

**Не перенесены** Listening бл. 2–6 — по-настоящему пустые (см. «доработать»).

Точки бл. 2 сняты с маркеров на странице PDF (в процентах от картинки);
в ShkolaApp точка k соответствует варианту k: 1 Jane — бабушка в оранжевом,
2 Mike — мальчик в синем, 3 Laura — женщина в розовом платье, 4 Clare —
маленькая девочка, 5 Paul — мужчина в красном.

---

## Промпты на картинки

Строки стиля (уже вклеены в промпты):

* **ПРЕДМЕТ** — Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left.
* **СЦЕНА** — Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, one single scene filling the frame, no people.

### 1. Обязательные — картинок в выгрузке нет

#### Л9.1 · Места отдыха — 4 карточки (2×2)

Режутся: `place_mountains`, `place_countryside`, `place_beach`, `place_city`
(слева направо, сверху вниз). Где: u9_hw6 бл. 2, 4, 7, 8.

```
A sheet of 4 separate small landscape vignettes arranged in a grid of 2 columns and 2 rows, each vignette a rounded self-contained little scene like a game icon.
Row 1, left to right: snowy mountains with pointed white peaks and a few pine trees; green countryside with rolling hills, a wooden fence, a small farmhouse, trees and a meadow with flowers.
Row 2, left to right: a sunny sandy beach with blue sea, gentle waves, a striped beach umbrella and a few seashells; a city with colourful tall buildings, windows, a street and small trees, generic buildings with no signs.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left.
No people at all - no humans, no hands, no faces.
Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge.
No text, no letters, no labels, no numbers, no signs.
Output size: 1536 x 1536 px.
```

#### Л9.2 · Места отдыха — 3 карточки (1 ряд × 3)

Режутся: `place_theme_park`, `place_campsite`, `place_lake`. Где: u9_hw6 бл. 2, 4, 7, 8.

```
A sheet of 3 separate small landscape vignettes in one row, each vignette a rounded self-contained little scene like a game icon, all three the same size.
Row 1, left to right: a theme park with a big Ferris wheel, a colourful roller coaster and a carousel; a campsite with two bright tents, a small campfire and pine trees; a calm blue lake with a small rowing boat, reeds and green hills behind.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left.
No people at all - no humans, no hands, no faces.
Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge.
No text, no letters, no labels, no numbers, no signs.
Output size: 1536 x 1024 px.
```

#### ЛТ9.1 · Занятия на пляже — 6 карточек (3×2)

Режутся: `act_paint_picture`, `act_listen_music`, `act_catch_fish`,
`act_take_photo`, `act_look_shells`, `act_make_sandcastle`. Где: u9_test бл. 2;
u9_hw1 бл. 2, 5, 7; u9_hw5 бл. 2 (listen_music, make_sandcastle, catch_fish),
бл. 3–5 (paint_picture, take_photo, look_shells).

```
A sheet of 6 separate objects arranged in a grid of 3 columns and 2 rows, each object shows one holiday activity without any person.
Row 1, left to right: a wooden painter's palette with bright paint blobs, a paintbrush and a small easel with a picture of the sea; big over-ear headphones connected to a small music player with a few floating musical notes; a fishing rod with a fish hanging on the line.
Row 2, left to right: a compact photo camera, generic design, not resembling any real product; a few colourful seashells on a small patch of sand with a magnifying glass; a sandcastle with towers, a small red bucket and a spade.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left.
No people at all - no humans, no hands, no faces.
Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge.
No text, no letters, no labels, no numbers.
Output size: 1536 x 1024 px.
```

#### Л9.4 · Занятия на пляже, дополнение — 3 карточки (1 ряд × 3)

Режутся: `act_eat_ice_cream`, `act_read_book`, `act_play_guitar`.
Где: u9_hw1 бл. 2, 5, 7 (словарь из 9 занятий: шесть с листа ЛТ9.1 + эти
три); u9_hw5 бл. 6 (`act_read_book`). Стиль и размер карточек — как у ЛТ9.1,
чтобы девять карточек одного урока не различались.

```
A sheet of 3 separate objects in one row, all three the same size, each object shows one holiday activity without any person.
Row 1, left to right: a big ice cream cone with two scoops, pink and white, with a few sprinkles; an open book lying on a small beach towel with a pair of sunglasses next to it; an acoustic guitar leaning on a small sand dune with a seashell beside it.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left.
No people at all - no humans, no hands, no faces.
Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge.
No text, no letters, no labels, no numbers.
Output size: 1536 x 1024 px.
```

### 2. По желанию — в выгрузке стоковые фото, ответы от замены не пострадают

#### Л9.3 · «Где что?» — 4 сцены (2×2), замена `hw3_where_photos`

Лист берётся **целиком** как одна картинка (сетка совпадает с исходной: в том
же порядке), резать не нужно. Где: u9_hw3 бл. 5 (вопросы бл. 6).

```
A sheet of 4 separate small scenes arranged in a grid of 2 columns and 2 rows, all four the same size, each one a rounded self-contained little scene.
Row 1, left to right: an open book lying on a wooden table; lots of small seashells inside an open cardboard box.
Row 2, left to right: an acoustic guitar lying on a bed with a white blanket and pillows; colourful tropical fish swimming in the blue sea among corals.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left.
No people at all - no humans, no hands, no faces.
Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge.
No text, no letters, no labels, no numbers.
Output size: 1536 x 1536 px.
```

#### ЛФ.1 · Предметы Final Test — 3 карточки (1 ряд × 3)

Режутся: `ft_eraser`, `ft_bike`, `ft_chicken` (замена стоковых фото).
Где: final_test бл. 3. Ответы не меняются: ластик ≠ ruler, bike = bike,
курица = chicken. Фото руки (`ft_arm`, «This is a face» ❌) не перерисовываем —
на ней человек.

```
A sheet of 3 separate objects in one row, all three the same size.
Row 1, left to right: a rectangular school eraser, half blue and half red; a bicycle, generic design, not resembling any real product; a friendly brown hen chicken standing.
Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left.
No people at all - no humans, no hands, no faces.
Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge.
No text, no letters, no labels, no numbers.
Output size: 1536 x 1024 px.
```

### 3. Не перерисовывать — вырезано из PDF

59 файлов, webp. Карточки ≤ 400 px (78–85), кадры истории, открытка и слова
с буквами — качество 88.

* `media/sm1/u9/` (47): `hw2_friends_talk`, `hw2_lets_swim`, `hw2_lets_music`,
  `hw2_lets_photo`, `hw2_lets_paint`, `hw2_lets_park`, `hw2_lets_shells`,
  `smile_sorry`, `smile_not_sure`, `smile_good_idea`, `hw2_beach_umbrella`,
  `hw3_cat`, `hw3_where_photos`, `hw3_bags`, `hw3_house`,
  `hw4_flash_running`, `hw4_friends`, `hw4_story_1`, `hw4_story_2`,
  `hw4_video_cover`, `hw4_frame_1` … `hw4_frame_8`,
  `test_listen_music`, `test_palette`, `test_book`, `test_girl_bucket`,
  `test_birds`, `test_dog`, `test_pink_shoes`, `test_blue_crocodile`,
  `test_selfie`, `test_postcard`, `test_beach_scene`;
  догружено 07.10: `hw1_drawing_example` (детский рисунок-пример),
  `hw5_girl_icecream`, `hw5_beach_kids`, `hw5_beach_scene`, `hw7_boy_guitar`,
  `hw7_girl_music`, `hw7_boy_fishing`, `hw7_where_tiles` (все — рисованные,
  не фото).
* `media/sm1/ft/` (12): `ft_picnic`, `ft_eraser`, `ft_spider`, `ft_bike`,
  `ft_arm`, `ft_chicken`, `ft_kitchen`, `ft_word_pencil`, `ft_word_monster`,
  `ft_word_duck`, `ft_word_bathroom`, `ft_word_sweater`.

Кадры `hw2_lets_*` маленькие (≈210×125): в выгрузке вся картинка 474×423.
На кадрах дети — перегенерировать нельзя, оставляем.

---

## Доработать руками

### Что нужно от вас — весь список

| # | Урок · блок | Что сделать |
|---|---|---|
| 1 | Unit 9 HW2 · бл. 3 | прислать видео «подружки решают, чем заняться» — `sm1_u9_hw2_b3` |
| 2 | Unit 9 HW3 · бл. 3 | прислать видео «где котик?» — `sm1_u9_hw3_b3` |
| 3 | Unit 9 HW4 · бл. 3 | прислать **аудио** истории «The top of the hill» — `sm1_u9_hw4_b3` |
| 4 | Unit 9 HW4 · бл. 8 | прислать мультфильм «The top of the hill» — `sm1_u9_hw4_b8` |
| 5 | Unit 9 Test · бл. 9 | прислать **аудио** «Бен и семья на пляже» (к вопросам бл. 10) — `sm1_u9_test_b9` |
| 6 | Final Test · бл. 1 | прислать **аудио** Final test Listening (2:46) — `sm1_final_b1` |
| 7 | Final Test, Listening бл. 2–6 | **пустые в выгрузке** — прислать картинки вариантов (по 3 на вопрос) и проверить, что аудио бл. 1 их покрывает; добавим 5 вопросов после бл. 2 (номера бл. 3–6 сдвинутся). Верные по отметкам выгрузки: Which boy is Tom? — 2; What is Anna drawing? — 2; What is Sue painting? — 3; What is Ben reading about? — 2; Where is Nick? — 2 |
| 8 | Unit 9 HW5 · бл. 7 | прислать **аудио** «как зовут детей на пляже» (к бл. 8) — `sm1_u9_hw5_b7` |
| 9 | Unit 9 HW5 · бл. 8 | **сверить по аудио, кто есть кто**: имена на точках угаданы — Tom (мальчик с удочкой), Jim (мальчик с мороженым), Sue (девочка с фотоаппаратом), Mia (девочка в наушниках), Bob (мальчик у замка из песка). Выгрузка «ученическая», ответа в ней нет |
| 10 | Unit 9 HW6 · бл. 9 | **СОСТАВ МОЙ**: в выгрузке «выбери имя по картинке», картинки (дети в разных местах) нет — перестроено: имя дано, ученик вставляет место. Посмотреть |
| 11 | Unit 9 HW1 · бл. 2, 5, 7; HW5 · бл. 2–6; HW6 · бл. 2, 4, 7, 8; Test · бл. 2 | ждём картинки листов Л9.1, Л9.2, Л9.4, ЛТ9.1 (до них уроки не заливаем) |
| 12 | Unit 9 HW3 · бл. 5, Final · бл. 3 | по желанию: замена стоковых фото листами Л9.3, ЛФ.1 — решить |
| 13 | название юнита | «Unit 9 · Holidays» — сверить с учебником Super Minds 1 |
| 14 | Final Test · бл. 2 | проверить по аудио, кто есть кто: точка 1 Jane (бабушка), 2 Mike (мальчик в синем), 3 Laura (женщина в розовом), 4 Clare (маленькая девочка), 5 Paul (мужчина в красном) — взято из соответствия «точка k = вариант k» выгрузки |
| 15 | Unit 9 HW1 · бл. 2–7, HW6 · бл. 2–5 | **СОСТАВ МОЙ**: в словарных тренажёрах список слов свёрнут (видно «Words 9» / «Words 7»). Взяли 9 занятий на море (как в тесте и HW7) и 7 мест (как в HW6 (2)), задания тренажёра пересобраны штатными блоками. Сверить слова с тренажёром на платформе |
| 16 | Unit 9 HW1 · бл. 9 | раскраска (бл. 3 части (2)) выброшена; в бл. 9 «нарисуй свой отдых» ученик присылает рисунок файлом (в выгрузке — «расскажи учителю на уроке», это оставлено) |
| 17 | Unit 9 HW5 · бл. 10 | образец ответа наш (`sample_tts`); в выгрузке было своё аудио-образец — можно прислать `sm1_u9_hw5_b10` |
| 18 | Unit 9 HW5 · бл. 2–6 | фото детей заменены картинками занятий без людей (Л9.4, ЛТ9.1); девочка с мороженым — рисованная, из PDF. Ответы не меняются |
| 19 | Unit 9 HW7 · бл. 2 | в выгрузке «Найди пару» на слух, 9 кнопок-аудио; одна карточка пропала на стыке страниц PDF — восстановлено **eat ice cream**. Звук размечен `audio_tts` |
| 20 | все уроки | нажать «Озвучить пачкой» (размечено `audio_tts`; HW2 бл. 8 — диалог целиком: в выгрузке к заданию было своё аудио, можно прислать файлом `sm1_u9_hw2_b8`) |
| 21 | все уроки | включить публикацию (заливаются скрытыми) |

Аудио и видео — в бакет `classroom-media`, папка `sm1/u9/` (медиа
финального теста — туда же, в папку последнего юнита).

### Подробности по урокам

**Unit 9 · Homework 2**

| Блок | Что | Подробно |
|---|---|---|
| 3 | видео | `sm1_u9_hw2_b3`, provider `file` |
| 5 | спорное | в выгрузке «Диаграмма» с 4 точками и двумя «лишними» вариантами (go to the park, look for shells), но на картинке шесть кадров и лишние явно подходят к кадрам e, f. Сделали match на все шесть |
| 8 | аудио | диалог размечен `audio_tts`; если есть исходное аудио — `sm1_u9_hw2_b8` |

**Unit 9 · Homework 3**

| Блок | Что | Подробно |
|---|---|---|
| 3 | видео | `sm1_u9_hw3_b3` |
| 5 | по желанию | стоковые фото `hw3_where_photos` → лист Л9.3 |
| 7–8 | проверка | задания с ручной проверкой (были «Открытый вопрос») |

**Unit 9 · Homework 4**

| Блок | Что | Подробно |
|---|---|---|
| 3 | аудио | `sm1_u9_hw4_b3` (mp3), provider `file` |
| 8 | видео | `sm1_u9_hw4_b8` |
| 6 | пересобрано | «Диаграмма» с 8 перепутанными кадрами → «расставь кадры по порядку» (sequence). Посмотреть |

**Unit 9 · Homework 1**

| Блок | Что | Подробно |
|---|---|---|
| 2–7 | СОСТАВ МОЙ | слова и задания тренажёра — см. п. 15 |
| 2, 5, 7 | картинки | `act_*` — листы ЛТ9.1, Л9.4 |
| 9 | раскраска выброшена | см. п. 16 |

**Unit 9 · Homework 5**

| Блок | Что | Подробно |
|---|---|---|
| 2–6 | картинки | `act_*` — листы ЛТ9.1, Л9.4 (вместо фото детей) |
| 7 | аудио | `sm1_u9_hw5_b7`, provider `file` |
| 8 | спорное | имена угаданы — п. 9 |
| 10 | аудио-образец | `sm1_u9_hw5_b10` — п. 17 |

**Unit 9 · Homework 6**

| Блок | Что | Подробно |
|---|---|---|
| 1 | наше | у части (1) приветствия нет |
| 2–5 | СОСТАВ МОЙ | слова и задания тренажёра — см. п. 15 |
| 2, 4, 7, 8 | картинки | пейзажи `place_*` — листы Л9.1, Л9.2 |
| 9 | СОСТАВ МОЙ | см. общий список, п. 10 |

**Unit 9 · Homework 7**

| Блок | Что | Подробно |
|---|---|---|
| 2 | восстановлено | девятая фраза — см. п. 19 |
| 5 | ключ | отметок в выгрузке нет, верные по грамматике it/they |

**Unit 9 Test**

| Блок | Что | Подробно |
|---|---|---|
| 2 | картинки | `act_*` — лист ЛТ9.1 |
| 8 | без картинки | в выгрузке фото взрослой женщины с руками на голове — не берём; можно прислать другую |
| 9 | аудио | `sm1_u9_test_b9` |

**Final Test**

| Блок | Что | Подробно |
|---|---|---|
| 1 | аудио | `sm1_final_b1` |
| после 2 | пустые | Listening бл. 2–6, см. п. 7 |
| 3 | по желанию | ЛФ.1. «This is a chicken» в выгрузке — жареная курица, ключ ✅ |

---

## Замечания по выгрузке

* Расхождений txt и PDF по ключам не найдено: ответы Final RW «Верно/Неверно»
  из txt совпали с PDF; ✅/❌ и тест Unit 9 сверены по чекбоксам PDF.
* HW6 (2): у трёх блоков нет картинок вообще (match, «Диаграмма», «выбери
  имя по картинке») — в PDF пусто, на месте точек «Диаграммы» висят маркеры
  без изображения.
* HW4 бл. 6: вместо картинки — зелёная дуга на чёрном (битая), выброшено.
* Догруженные 07.10 файлы (HW1 (1)/(2), HW5, HW6 (1), HW7) — «ученический»
  вид VZNANIYA, а не редактор ShkolaApp: заданий-«Диаграмм» с отметками нет,
  ответы видны только там, где у варианта стоит ✅/❌ (HW7 бл. 3).
* HW6 (1): txt 203 байта — только шапка тренажёра; PDF (2 стр.) показывает
  то же самое: «Words 7», «Tasks 4» (Cards, Remember, Find the definition,
  Listen) и Final test. Скрытого содержимого в нём нет.
* HW5: в инструкции к True/False упомянут вариант «Not stated», а кнопок
  две; в HW7 бл. 2 одна карточка фразы пустая на стыке страниц.
