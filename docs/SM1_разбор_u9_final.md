# Super Minds 1 — разбор Unit 9 и Final Test

Шаг 2 регламента: выгрузка разобрана, уроки описаны в `tools/sm1/u9.py` и
`tools/sm1/final.py`, картинки из PDF вырезаны в `media/sm1/u9/` и
`media/sm1/ft/`. В базу ничего не залито.

Выгрузка ShkolaApp, файлы Drive — `docs/SM1_выгрузка_файлы.md` (папки `Unit 9`
и `Test SM1/Final`). Скачанное лежит в скретчпаде агента (`agent_u9/dl/`).

| Ключ | Урок | Блоков | Что есть в выгрузке |
|---|---|---|---|
| `u9_hw2` | Homework 2 | 10 | целиком |
| `u9_hw3` | Homework 3 | 9 | целиком |
| `u9_hw4` | Homework 4 | 10 | целиком |
| `u9_hw6` | Homework 6 | 7 | **только часть (2)**, части (1) нет |
| `u9_test` | Unit 9 Test | 14 | целиком |
| `final_test` | Final Test (юнит `Final Test`, unit_sort 10) | 6 | Listening + Reading-Writing; 5 заданий Listening пустые |

Homework 1, 5, 7 Unit 9 в выгрузке нет — номера уроков не сдвигали
(`lesson_sort` = K − 1, тест — 7).

Название юнита — **`Unit 9 · Holidays`** (лексика: пляж, горы, кемпинг, парк
развлечений; Let's…; Where's…?). По учебнику не сверено — см. «доработать».

Во всех трёх домашках из урока выброшен блок-реклама для родителей
(«3 бесплатных урока по реферальной программе», в HW3 ещё «Новогодний
розыгрыш призов») и «робуксы» за задания. Декоративные картинки (речевой
пузырь, Спанч Боб, Скрудж Макдак, лайк) заменены общими `media/shared/`.

Номера блоков ниже — **как в редакторе** (sort_order + 1).

---

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

## u9_hw6 · Homework 6 (только часть 2)

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие «вторая часть домашнего задания» | бл. 1 + текст бл. 2 |
| 2 | match | 7 пейзажей `place_*` → mountains, countryside, beach, city, theme park, campsite, lake | бл. 2 — **картинок в выгрузке нет**, лист Л9.1/Л9.2 |
| 3 | match | те же пейзажи → We can go to shops / climb up / make a sandcastle / go on a boat / sleep in a tent / ride on fun things / see lots of trees here | бл. 3 «Диаграмма», картинки нет |
| 4 | gaps (drag) | **СОСТАВ МОЙ**: имя дано, ученик вставляет место (campsite, city, mountains, beach, countryside) | бл. 4 «выбери имя по картинке» — картинки нет |
| 5 | gaps (drag) | I like the mountains… 5 пропусков | бл. 5 |
| 6 | task | доп. задание: расскажи о любимых местах | бл. 6 «Открытый вопрос» |
| 7 | text | прощание | бл. 7 |

Соответствие «место → занятие» в бл. 3 восстановлено по смыслу (в выгрузке
точки стоят на пустом месте картинки, которой нет): shops — city, climb up —
mountains, sandcastle — beach, boat — lake, tent — campsite, fun things —
theme park, trees — countryside.

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
(слева направо, сверху вниз). Где: u9_hw6 бл. 2 и 3.

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

Режутся: `place_theme_park`, `place_campsite`, `place_lake`. Где: u9_hw6 бл. 2 и 3.

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
`act_take_photo`, `act_look_shells`, `act_make_sandcastle`. Где: u9_test бл. 2.

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

51 файл, webp. Карточки ≤ 400 px (78–85), кадры истории, открытка и слова
с буквами — качество 88.

* `media/sm1/u9/` (39): `hw2_friends_talk`, `hw2_lets_swim`, `hw2_lets_music`,
  `hw2_lets_photo`, `hw2_lets_paint`, `hw2_lets_park`, `hw2_lets_shells`,
  `smile_sorry`, `smile_not_sure`, `smile_good_idea`, `hw2_beach_umbrella`,
  `hw3_cat`, `hw3_where_photos`, `hw3_bags`, `hw3_house`,
  `hw4_flash_running`, `hw4_friends`, `hw4_story_1`, `hw4_story_2`,
  `hw4_video_cover`, `hw4_frame_1` … `hw4_frame_8`,
  `test_listen_music`, `test_palette`, `test_book`, `test_girl_bucket`,
  `test_birds`, `test_dog`, `test_pink_shoes`, `test_blue_crocodile`,
  `test_selfie`, `test_postcard`, `test_beach_scene`.
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
| 8 | Unit 9 HW6 | часть (1) (словарный тренажёр) не выгрузилась — прислать, если нужна; встанет в начало урока, номера блоков сдвинутся |
| 9 | Unit 9 HW1, HW5, HW7 | в выгрузке нет — будут ли? |
| 10 | Unit 9 HW6 · бл. 4 | **СОСТАВ МОЙ**: в выгрузке «выбери имя по картинке», картинки (дети в разных местах) нет — перестроено: имя дано, ученик вставляет место. Посмотреть |
| 11 | Unit 9 HW6 · бл. 2–3, Test · бл. 2 | ждём картинки листов Л9.1, Л9.2, ЛТ9.1 (до них урок не заливаем) |
| 12 | Unit 9 HW3 · бл. 5, Final · бл. 3 | по желанию: замена стоковых фото листами Л9.3, ЛФ.1 — решить |
| 13 | название юнита | «Unit 9 · Holidays» — сверить с учебником Super Minds 1 |
| 14 | Final Test · бл. 2 | проверить по аудио, кто есть кто: точка 1 Jane (бабушка), 2 Mike (мальчик в синем), 3 Laura (женщина в розовом), 4 Clare (маленькая девочка), 5 Paul (мужчина в красном) — взято из соответствия «точка k = вариант k» выгрузки |
| 15 | все уроки | нажать «Озвучить пачкой» (размечено `audio_tts`; HW2 бл. 8 — диалог целиком: в выгрузке к заданию было своё аудио, можно прислать файлом `sm1_u9_hw2_b8`) |
| 16 | все уроки | включить публикацию (заливаются скрытыми) |

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

**Unit 9 · Homework 6**

| Блок | Что | Подробно |
|---|---|---|
| — | нет части (1) | словарный тренажёр не выгрузился |
| 2–3 | картинки | пейзажи `place_*` — листы Л9.1, Л9.2 |
| 4 | СОСТАВ МОЙ | см. общий список, п. 10 |

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
