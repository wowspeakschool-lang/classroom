# SM1 — разбор: Unit 5 (HW4, HW6, HW7, тест), тест Unit 1, тест Unit 2

Шаг 2 регламента: выгрузка разобрана, уроки описаны в `tools/sm1/u5.py`,
`tools/sm1/u1.py`, `tools/sm1/u2.py`, картинки из PDF вырезаны в
`media/sm1/u5/`, `media/sm1/u1/`, `media/sm1/u2/`. В базу ничего не залито.

`python3 tools/sm1_build.py --check-all` по этим урокам: единственные ошибки —
«нет файла» под картинки, которые ещё будут сгенерированы (листы раздела 1).

| Урок | Ключ | Блоков | Источник |
|---|---|---|---|
| Unit 5 · Homework 4 | `u5_hw4` | 11 | «SM1 Unit 5 Homework 4 (1)» + «(2)» (интерактивное видео) |
| Unit 5 · Homework 6 | `u5_hw6` | 9 | «Homework 6 (2)» (основная часть) + «Homework 6 (1)» (игра) |
| Unit 5 · Homework 7 | `u5_hw7` | 12 | «SM1 Unit 5 Homework 7» |
| Unit 5 · Unit 5 Test | `u5_test` | 12 | «Super Minds 1 Unit 5 Test» |
| Unit 1 · Unit 1 Test | `u1_test` | 14 | «Super Minds 1 Unit 1 Test» |
| Unit 2 · Unit 2 Test | `u2_test` | 14 | «Super Minds 1 Unit 2 Test» |

Homework 5 Unit 5 в выгрузке нет — пропущен, номера уроков не сдвинуты
(`lesson_sort` = K − 1, тесты — 7, `kind='test'`).

Общее для всех уроков:

* **Реклама для родителей** («3 бесплатных урока по реферальной программе»,
  900×900) стоит первым блоком в каждой домашке выгрузки — не перенесена.
  В залитых HW1–3 Unit 5 она стоит отдельным блоком-картинкой; если нужна —
  скажите, добавим.
* Картинки «HELLO / BRAVO / BYE» выгрузки заменены общими `media/shared/`.
* Галерея фонов после «Выберите новое задание для урока» не взята.
* Озвучка размечена `audio_tts` / `right_audio_tts` / `sample_tts`.

---

## Unit 5 · Homework 4 (`u5_hw4`)

Порядок частей подтверждён содержимым: «(1)» — домашка по истории «We're lost!»
и в приветствии обещает «вторую часть — интерактивное видео»; «(2)» —
интерактивное видео «SM2ed Animated story video L1 U5» (Rutube, 1:44) с семью
вопросами по таймкодам. Прощание (1) и приветствие (2) сведены в блок 9.

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие, `shared/hello_wave` | (1) блок 2 |
| 2 | text | «Давай повторим…» + карточки `card_lost_phrases`, `card_phonics_u` | (1) блок 3, PDF |
| 3 | text | вопрос до чтения (lake / forest / river) + кадр `story_lost_forest` | (1) блок 4, PDF |
| 4 | video | **аудио истории** — пустой `url`, `provider: file` | (1) блок 5 «Медиафайл» без файла |
| 5 | text | комикс `story_lost_comic` + текст истории репликами | (1) блок 6, PDF |
| 6 | quiz (multiple) | что сказал зайчик: Yippee! / Come with me. / Now, I'm lost. | (1) блок 7, ключ по чекбоксам PDF |
| 7 | quiz | Where's the lake? · Wait and see. · Are you OK, rabbit? — с кадрами `story_lost_flash/whisper/rabbit` | (1) блоки 8–10 |
| 8 | match | Where's my bag? → I don't know. и ещё 2 пары | (1) блок 11 |
| 9 | text | перемычка: «первая часть выполнена» + вход в доп. часть | (1) блок 12 + (2) комментарий |
| 10 | video | **интерактивное видео** — пустой `url`, `provider: file` | (2) |
| 11 | text | прощание, `shared/well_done_star` | — |

## Unit 5 · Homework 6 (`u5_hw6`)

**Имена файлов врут.** Основная часть лежит в «Homework 6 (2)» (8 блоков,
приветствие говорит о «второй, дополнительной части»). «Homework 6 (1)», внутри
озаглавленная «SM1 Unit 5 Homework 6 (2)», — игра Activity Matching Columns на
те же 6 занятий. Порядок в уроке: файл «(2)» → перемычка 7 → файл «(1)».

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие, `shared/hello_highfive` | «(2)» блок 2 |
| 2 | text | «Давай повторим…» + карточка `card_go_activities` | «(2)» блок 3, PDF |
| 3 | match | картинка ↔ go swimming / climbing / running / sledging / surfing / skiing | «(2)» блок 4; **картинок в выгрузке нет — лист Л5.1** |
| 4 | sort | Beach 🏖️: running, surfing, swimming · Mountains 🏔️: climbing, skiing, sledging | «(2)» блок 5 |
| 5 | hotspot | 6 фото мест (`sport_places`) ↔ We ride a horse there / play football / go fishing / go running / go climbing / play tennis | «(2)» блок 6, PDF |
| 6 | speaking | «придумай идеальное место для спорта» | «(2)» блок 7 |
| 7 | text | перемычка: прощание основной части + вход в игру | «(2)» блок 8 |
| 8 | match | go swimming ↔ заниматься плаванием и ещё 5 пар | «(1)» игра Matching Columns |
| 9 | text | прощание, `shared/well_done_trophy` | — |

## Unit 5 · Homework 7 (`u5_hw7`)

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | text | приветствие «повторение перед тестом», `shared/hello_book` | блок 1 |
| 2 | match | дни недели ↔ перевод (7) | блок 2 «Найди слово» (поиск слов) — механика заменена |
| 3 | sort | PLAY: football, tennis, board games · GO: swimming, skiing, surfing, climbing, running | блок 3 |
| 4 | gaps (type) | 5 предложений, впиши день недели по русской подсказке | блок 4 |
| 5 | quiz | 3 вопроса «Do you…? 😊/😞» | блок 5, ключ по чекбоксам |
| 6 | order | I play football on Mondays. | блок 6 |
| 7 | order | Do you play tennis at the weekend? | блок 6 |
| 8 | speaking | рассказ о своей неделе, минимум 5 предложений | блок 7 |
| 9 | text | «а это дополнительное задание — для настоящих чемпионов» | блок 8 |
| 10 | exact_input | 7 анаграмм дней недели — **СОСТАВ МОЙ** | блок 8, Wordwall Anagram «SM1 Unit 5 Days of the week» |
| 11 | gaps (drag) | текст про неделю Сью, 6 пропусков — **СОСТАВ МОЙ** | блок 9, Wordwall Complete the sentence «SM1-5» |
| 12 | text | прощание «Ты готов к тесту!», `shared/well_done_medal` | блок 10 |

## Unit 5 · Unit 5 Test (`u5_test`)

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | exact_input | 7 дней недели: «Напиши по-английски: понедельник» | блок 1 «Впиши буквы» |
| 2 | match | картинка ↔ ride a pony / go swimming / watch TV / play football / play computer games / ride a bike | блок 2; **картинок в выгрузке нет — листы ЛТ5.1, Л5.1** |
| 3 | quiz | 5 диалогов «Do you…? — Yes, I do / No, I don't», с картинками `t_*` | блок 3, PDF |
| 4 | order | Do you watch TV at the weekend? · `t_order_watch_tv` | блок 4 |
| 5 | order | Do you play the piano on Mondays? · `t_order_piano` | блок 4 |
| 6 | order | Do you go swimming on Wednesdays? · `act_go_swimming` | блок 4 (в выгрузке фото детей) |
| 7 | order | Do you play hide-and-seek on Saturdays? · `act_hide_and_seek` | блок 4 (в выгрузке фото детей) |
| 8 | order | Do you ride a pony every Friday? · `act_ride_pony` | блок 4 (в выгрузке фото ребёнка) |
| 9 | match | READING: текст Сэма в заголовке, день ↔ занятие (5 пар) | блок 5 |
| 10 | video | **аудио LISTENING** — пустой `url`, `provider: file` | блок 6, аудио без файла |
| 11 | sort | Tom / Lucy / Ben: дни и занятия | блок 6 |
| 12 | speaking | SPEAKING TASK, 12 вопросов | блок 7 |

## Unit 1 · Unit 1 Test (`u1_test`)

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | task | «Смотри и пиши»: впиши названия школьных вещей, картинка `t_school_things` | блок 1 «Открытый вопрос», PDF |
| 2 | speaking | прочитай вслух 7 предложений (I spin a top…), `t_reading_kids` | блок 2 |
| 3 | video | **аудио к блоку 4** — пустой `url`, `provider: file` | блок 3, аудио без файла |
| 4 | quiz (multiple) | выбери услышанные предметы: notebook, pencil, pencil case, rubber, bag (из 10), `t_listen_boy` | блок 3, ключ по чекбоксам |
| 5 | video | **аудио к «Диаграмме»** — пустой `url`, `provider: file` | блок 4 «Текст» с аудио |
| 6 | hotspot | 5 картинок класса (`t_classroom_scenes`), подписи-номера 1–5 | блок 4 «Диаграмма», PDF |
| 7 | match | картинка ↔ book / pen / rubber / pencil / bag / ruler | блок 5; **картинок в выгрузке нет — лист ЛТ1.1** |
| 8 | quiz | 5 диалогов, вопрос на каждый пропуск (9 вопросов), картинки `t_*` | блок 6 |
| 9 | order | It is a yellow desk. · `t_yellow_desk` | блок 7 |
| 10 | order | Pass me a pencil, please. · `t_pencil` | блок 7 |
| 11 | order | Open your pencil case, please. · `t_pencil_case_open` | блок 7 |
| 12 | order | Sit at your desk, please. · `t_wooden_desk` | блок 7 |
| 13 | order | It is a blue notebook. · `t_blue_notebook` | блок 7 |
| 14 | speaking | SPEAKING TASK по картинке класса `t_classroom` | блок 8 |

## Unit 2 · Unit 2 Test (`u2_test`)

| № | Тип | Что внутри | Откуда |
|---|---|---|---|
| 1 | exact_input | 9 слов с пропущенными буквами (d _ l l — кукла …) | блок 1 «Заполни пропуски» (игра); маска букв моя |
| 2 | match | картинка ↔ doll / kite / go-kart / monster / car / train | блок 2; **картинок в выгрузке нет — лист ЛТ2.1** |
| 3 | speaking | прочитай вслух 5 предложений (I can see a big tree…) | блок 3 |
| 4 | quiz | 5 диалогов, вопрос на каждый пропуск (9 вопросов), картинки `t_*` | блок 4 |
| 5 | order | His favourite number is ten. · `t_number_ten` | блок 5 |
| 6 | order | It's a new beautiful bike. · `t_bike` | блок 5 |
| 7 | order | What is her favourite toy? · `t_toys` | блок 5 |
| 8 | order | It's a short green train. · `t_green_train` | блок 5 |
| 9 | order | It's a funny purple monster. · `t_purple_monster` | блок 5 |
| 10 | video | **аудио к «Диаграмме»** — пустой `url`, `provider: file` | блок 6, аудио без файла |
| 11 | hotspot | 5 детей с игрушками (`t_kids_toys`) ↔ Amy, Tom, Sam, Ben, Lily | блок 6 «Диаграмма», PDF |
| 12 | text | картинка полки с игрушками `t_toy_shelf` | блок 7 (картинка) |
| 13 | truefalse | The ball is big ✔ · car big ✘ · train short ✘ · kite old ✘ · doll beautiful ✔ | блок 7 |
| 14 | speaking | SPEAKING TASK, 10 вопросов | блок 8 |

---

## Промпты на картинки

Две строки стиля — один раз:

* **ПРЕДМЕТ:** Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left.
* **СЦЕНА:** Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, one single scene filling the frame, no people.

Людей нет ни в одном листе: занятия показаны через предметы и место
(бассейн с очками, санки на горке), «прятки» — через зверят.

### 1. Обязательные — картинок в выгрузке нет

**Л5.1 · занятия go + -ing** — 6 ячеек.
Режется: ряд 1 — `u5/act_go_swimming`, `u5/act_go_climbing`, `u5/act_go_running`;
ряд 2 — `u5/act_go_sledging`, `u5/act_go_surfing`, `u5/act_go_skiing`.
Где: `u5_hw6` блок 3 (все шесть); `u5_test` блок 2 и блок 6 (`act_go_swimming`).

```
A sheet of 6 separate illustrations in a grid of 3 columns and 2 rows, landscape 1536x1024, each illustration a small self-contained vignette showing a sport through its place and equipment. Row 1, left to right: a small blue swimming pool corner with a ladder, swimming goggles and a swim cap lying on the edge; a short colourful indoor climbing wall section with holds, a coiled rope and a climbing helmet at its foot; a short piece of red running track with white lane lines and a pair of running shoes (generic design, not resembling any real product) on it. Row 2, left to right: a small snowy hill with a wooden sledge on top; a turquoise ocean wave with a bright surfboard riding on it; a pair of skis and ski poles stuck upright in a small snow drift. Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, generous white margin around the whole sheet. No text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces.
```

**ЛТ5.1 · занятия теста Unit 5** — 6 ячеек.
Режется: ряд 1 — `u5/act_ride_pony`, `u5/act_watch_tv`, `u5/act_play_football`;
ряд 2 — `u5/act_computer_games`, `u5/act_ride_bike`, `u5/act_hide_and_seek`.
Где: `u5_test` блок 2 (все, кроме hide-and-seek), блок 7 (`act_hide_and_seek`),
блок 8 (`act_ride_pony`).

```
A sheet of 6 separate illustrations in a grid of 3 columns and 2 rows, landscape 1536x1024, each illustration a small self-contained vignette. Row 1, left to right: a cute small brown pony wearing a red saddle and bridle, standing on a patch of green grass; a cosy small sofa facing a television on a low stand (generic design, not resembling any real product) with a cartoon on the screen and a remote control on the sofa; a black-and-white football on a patch of green grass in front of a small white goal with a net. Row 2, left to right: a computer monitor showing a colourful maze game, with a keyboard and a game controller in front of it (generic design, not resembling any real product); a bright red children's bicycle with a bell and a basket (generic design, not resembling any real product); a playful game of hide-and-seek between animals: a puppy covering its eyes with its paws next to a tree while a kitten peeks out from behind a bush. Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, generous white margin around the whole sheet. No text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces.
```

**ЛТ1.1 · школьные вещи** — 6 ячеек.
Режется: ряд 1 — `u1/school_book`, `u1/school_pen`, `u1/school_rubber`;
ряд 2 — `u1/school_pencil`, `u1/school_bag`, `u1/school_ruler`.
Где: `u1_test` блок 7.

```
A sheet of 6 separate school objects in a grid of 3 columns and 2 rows, landscape 1536x1024. Row 1, left to right: a closed red hardcover book with a plain cover; a blue ballpoint pen with its cap off; a pink-and-blue rubber eraser. Row 2, left to right: a yellow wooden pencil with a pink rubber on the end, lying diagonally; a bright orange school backpack with two straps; a green plastic ruler with plain tick marks and no numbers, lying diagonally. Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, generous white margin around the whole sheet. No text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces.
```

**ЛТ2.1 · игрушки** — 6 ячеек.
Режется: ряд 1 — `u2/toy_doll`, `u2/toy_kite`, `u2/toy_go_kart`;
ряд 2 — `u2/toy_monster`, `u2/toy_car`, `u2/toy_train`.
Где: `u2_test` блок 2.

```
A sheet of 6 separate toys in a grid of 3 columns and 2 rows, landscape 1536x1024. Row 1, left to right: a cloth rag doll with yellow woollen hair and a pink dress, sitting; a diamond-shaped red-and-yellow kite with a long tail of bows; a small red toy go-kart with big black wheels and an empty seat (generic design, not resembling any real product). Row 2, left to right: a cute soft green plush monster toy with three eyes and small horns; a small blue toy car (generic design, not resembling any real product); a colourful wooden toy train with an engine and two wagons. Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, generous white margin around the whole sheet. No text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces.
```

### 2. По желанию — в выгрузке стоковое фото или клипарт

Ответы от замены не пострадают. Если листа не будет — остаются вырезанные из PDF.

**Л5.2 · места для спорта** — 6 ячеек, из них мы сами соберём коллаж 3×2
`u5/sport_places` взамен стокового (у нынешнего коллажа ряды разной высоты;
при замене точки блока перейдут на центры ровной сетки, y 25 / 75).
Ряд 1 — конюшня/манеж, футбольное поле, озеро с рыбалкой; ряд 2 — беговая
дорожка, скалодром, теннисный корт. Где: `u5_hw6` блок 5.

```
A sheet of 6 separate square place vignettes in a grid of 3 columns and 2 rows, landscape 1536x1024, each vignette a small rounded tile showing one empty place for sport. Row 1, left to right: a sandy horse riding arena with a white wooden fence and a saddled pony standing in it; a green football pitch with white lines and two goals; a calm lake with reeds and a small wooden pier with a fishing rod and a bucket on it. Row 2, left to right: a red running track curving around green grass; an indoor climbing wall covered with colourful holds and a hanging rope; a blue tennis court with a net, a racket and a yellow ball. Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, generous white margin around the whole sheet. No text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces.
```

**ЛТ5.2 · пианино и домашка** — 2 ячейки, ряд из двух.
Режется: `u5/t_piano`, `u5/t_order_piano` (одна и та же картинка пианино) и
`u5/t_homework`. Остальной клипарт теста Unit 5 (`t_computer_games`,
`t_football`, `t_watch_tv`, `t_order_watch_tv`) при замене берётся из ячеек
листа ЛТ5.1. Где: `u5_test` блоки 3, 5.

```
A sheet of 2 separate illustrations side by side in 1 row of 2 columns, landscape 1536x1024. Left to right: a small black grand piano with an open lid, a music book on the stand and a round piano stool; a school desk with an open exercise book, a pencil, a ruler and a small stack of textbooks for doing homework. Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, generous white margin around the whole sheet. No text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces.
```

**ЛТ1.2 · школьная мебель и пеналы** — 6 ячеек, взамен стоковых фото теста
Unit 1 (две из них на чёрном фоне). Цвета важны — их называют предложения.
Режется: ряд 1 — `u1/t_pencil_case`, `u1/t_desk_chair`, `u1/t_notebook` и
`u1/t_blue_notebook` (одна картинка); ряд 2 — `u1/t_yellow_desk`,
`u1/t_wooden_desk`, `u1/t_pencil_case_open`. `t_book`, `t_rubber`, `t_pencil`
при замене берутся из ячеек ЛТ1.1. Где: `u1_test` блоки 8, 9, 11, 12, 13.

```
A sheet of 6 separate school objects in a grid of 3 columns and 2 rows, landscape 1536x1024. Row 1, left to right: a closed pink zip pencil case; a school desk with a matching chair tucked under it; a blue spiral notebook with a plain cover. Row 2, left to right: a bright yellow school desk with two drawers; a brown wooden teacher's desk with drawers; an open pencil case full of colourful felt-tip pens and pencils. Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, generous white margin around the whole sheet. No text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces.
```

**ЛТ2.2 · игрушки для диалогов и предложений** — 6 ячеек, взамен стоковых
фото теста Unit 2. Цвета важны (yellow ball, green train, purple monster).
Режется: ряд 1 — `u2/t_plane`, `u2/t_yellow_ball`, `u2/t_bike`; ряд 2 —
`u2/t_green_train`, `u2/t_purple_monster`, `u2/t_toys`. Где: `u2_test` блоки 4, 6–9.

```
A sheet of 6 separate toys in a grid of 3 columns and 2 rows, landscape 1536x1024. Row 1, left to right: a light-blue toy aeroplane with round windows; a small shiny yellow ball; a new turquoise children's bicycle (generic design, not resembling any real product). Row 2, left to right: a short green toy steam engine with red wheels; a funny purple one-eyed monster toy with small bat wings and two little horns; a small heap of toys - a toy boat, plain coloured building blocks, a toy robot, a rubber duck and a teddy bear. Bright 3D-rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colours, soft even light from the top-left. Plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, generous white margin around the whole sheet. No text, no letters, no labels, no numbers. No people at all - no humans, no hands, no faces.
```

### 3. Не перерисовывать — уже вырезано из PDF

Материал заданий: кадры мультфильма, карточки методиста, картинки, по которым
сверяются ответы, клипарт с людьми (генерировать людей нельзя).

* `media/sm1/u5/`: `card_lost_phrases`, `card_phonics_u`, `card_go_activities`
  (карточки методиста, q88), `story_lost_forest`, `story_lost_comic`,
  `story_lost_flash`, `story_lost_whisper`, `story_lost_rabbit` (кадры истории),
  `sport_places` (стоковый коллаж, см. Л5.2), `t_computer_games`, `t_piano`,
  `t_football`, `t_watch_tv`, `t_homework`, `t_order_watch_tv`, `t_order_piano`
  (клипарт теста, см. ЛТ5.2) — 16 файлов.
* `media/sm1/u1/`: `t_school_things` (карточка методиста), `t_reading_kids`,
  `t_listen_boy`, `t_classroom_scenes` (материал «Диаграммы»), `t_classroom`
  (сцена для SPEAKING), `t_pencil_case`, `t_desk_chair`, `t_notebook`, `t_book`,
  `t_rubber`, `t_yellow_desk`, `t_pencil`, `t_pencil_case_open`, `t_wooden_desk`,
  `t_blue_notebook` (стоковые фото, см. ЛТ1.2) — 15 файлов.
* `media/sm1/u2/`: `t_kids_toys` (материал «Диаграммы»), `t_toy_shelf`
  (материал «Верно / неверно»), `t_girl_seven`, `t_meeting`, `t_monster_blue`,
  `t_number_ten`, `t_plane`, `t_yellow_ball`, `t_bike`, `t_toys`,
  `t_green_train`, `t_purple_monster` — 12 файлов.

Не взяты: фото детей в «Составь предложение» теста Unit 5 (бассейн, прятки,
пони) — заменены ячейками Л5.1 / ЛТ5.1; реклама для родителей; HELLO / BRAVO /
BYE; галерея фонов.

---

## Доработать руками

### Что нужно от вас — весь список

| # | Урок | Блок | Что сделать |
|---|---|---|---|
| 1 | все шесть | — | сгенерировать листы **Л5.1, ЛТ5.1, ЛТ1.1, ЛТ2.1** (обязательно) и по желанию Л5.2, ЛТ5.2, ЛТ1.2, ЛТ2.2 — промпты выше |
| 2 | Unit 5 · HW4 | 4 | аудио истории «We're lost!» → файл **`sm1_u5_hw4_b4`** |
| 3 | Unit 5 · HW4 | 10 | интерактивное видео «SM2ed Animated story video L1 U5» → **`sm1_u5_hw4_b10`** (или ссылка) |
| 4 | Unit 5 · HW4 | 10 | решить: нужны ли 7 вопросов интерактивного видео отдельными блоками (см. ниже) |
| 5 | Unit 5 · Test | 10 | аудио LISTENING → **`sm1_u5_test_b10`**; сверить ключ блока 11 по записи |
| 6 | Unit 1 · Test | 3 | аудио «выбери предметы» → **`sm1_u1_test_b3`**; сверить ключ блока 4 |
| 7 | Unit 1 · Test | 5 | аудио к «Диаграмме» → **`sm1_u1_test_b5`**; сверить ключ блока 6 |
| 8 | Unit 2 · Test | 10 | аудио к «Диаграмме» → **`sm1_u2_test_b10`**; сверить ключ блока 11 |
| 9 | Unit 5 · HW7 | 10, 11 | посмотреть пересобранные игры Wordwall — **СОСТАВ МОЙ** |
| 10 | все шесть | — | нажать «Озвучить пачкой» (если решите озвучивать) |
| 11 | все шесть | — | включить публикацию — уроки заливаются скрытыми |
| 12 | Unit 5 · HW4, HW6, HW7 | 1 | решить, нужен ли рекламный баннер для родителей (в HW1–3 он есть) |

### Unit 5 · Homework 4

| Блок | Что |
|---|---|
| 4 | «Медиафайл» в выгрузке без файла — аудио истории. Нужен файл `sm1_u5_hw4_b4`. |
| 10 | Интерактивное видео «SM2ed Animated story video L1 U5» (Rutube, 1:44) — `sm1_u5_hw4_b10`. В ShkolaApp к нему 7 вопросов по таймкодам: 00:26 Тест, 00:33 Составь предложение, 00:40 Выбери правильный вариант, 01:02 Заполни пропуски, 01:14 Верно / неверно, 01:18 Заполни пропуски, 01:31 Найди пару. **Содержимого вопросов в выгрузке нет**, в уроке стоит только видео (так же сделаны HW4 Unit 3 и Unit 4). Пришлёте вопросы — соберём блоками после видео. |
| 2 | Карточки методиста «Story — We're lost! (Key Phrases)» и «Phonics — /ʌ/» перенесены как есть. |

### Unit 5 · Homework 6

| Блок | Что |
|---|---|
| — | Части переставлены: основная часть в файле «Homework 6 (2)», игра — в «(1)» (внутри озаглавлена «(2)»). |
| 3 | Картинок в «Найди пару» в выгрузке нет — лист Л5.1. |
| 4 | В «Классификации» нет пейзажей пляжа и гор; у блока sort картинок групп нет — названия «Beach 🏖️», «Mountains 🏔️», в заголовке перевод. По ключу выгрузки **go running отнесён к Beach** — оставлено как есть. |
| 5 | «Диаграмма»: стоковый коллаж из 6 фото. Точки поставлены по центрам кадров; ключ — точка k ↔ вариант k выгрузки, по содержимому фото сходится (ипподром, стадион, озеро, беговая дорожка, скалодром, корт). |

### Unit 5 · Homework 7

| Блок | Что |
|---|---|
| 2 | «Найди слово» (поиск слов в сетке) с 7 днями недели — у нас такой механики нет, собран match «день — перевод». |
| 5 | Опечатка выгрузки «Do you ride your bike at the on Mondays?» исправлена на «on Mondays». |
| 10 | Wordwall Anagram «SM1 Unit 5 Days of the week» — содержимого нет, по названию собраны 7 анаграмм дней недели (exact_input). **СОСТАВ МОЙ.** |
| 11 | Wordwall Complete the sentence «SM1-5» — обложка без содержимого, собран текст на 6 пропусков по материалу юнита (gaps, drag). **СОСТАВ МОЙ.** |

### Unit 5 · Unit 5 Test

| Блок | Что |
|---|---|
| 1 | «Впиши буквы» — какие буквы были скрыты, выгрузка не показывает; ученик вписывает день недели целиком по переводу. |
| 2 | Картинок в «Соедини слова с картинками» нет — листы ЛТ5.1 и Л5.1. |
| 6–8 | В выгрузке — фото детей (бассейн, прятки, пони); заменены ячейками Л5.1 / ЛТ5.1. Прятки показаны зверятами. |
| 10 | LISTENING: аудио в выгрузке без файла — `sm1_u5_test_b10`. Ключ блока 11 по выгрузке: Tom — Sunday, Saturday, play football, watch TV; Lucy — Monday, go swimming, sing; Ben — Wednesday, play hide-and-seek, play computer games. Сверить с записью. |
| 3 | В диалоге про футбол на картинке мальчик с мячом, а верный ответ по ключу «No, I don't. I go swimming.» — так в выгрузке, оставлено. |

### Unit 1 · Unit 1 Test

| Блок | Что |
|---|---|
| 3 | Аудио к «Выбери предметы, которые ты услышишь» — `sm1_u1_test_b3`. Ключ блока 4 по чекбоксам: notebook, pencil, pencil case, rubber, bag. Сверить с записью. |
| 5 | Аудио к «Диаграмме» — `sm1_u1_test_b5`. |
| 6 | «Диаграмма»: подписи — номера 1–5. Метки методиста стояли так: 2 — верх слева, 4 — верх в центре, 3 — верх справа, 5 — низ слева, 1 — низ справа; у нас точки на тех же картинках, по центрам. Сверить с записью. |
| 7 | Картинок в «Соедини слова с картинками» нет — лист ЛТ1.1. |
| 8 | Пять «Выбери правильный вариант» с двумя пропусками — по вопросу на пропуск, 9 вопросов, позиции верных разведены. |

### Unit 2 · Unit 2 Test

| Блок | Что |
|---|---|
| 1 | Игра «впиши недостающие буквы»: какие буквы были скрыты, выгрузка не показывает — маска моя, ученик вписывает слово целиком. |
| 2 | Картинок в «Соедини слова с картинками» нет — лист ЛТ2.1. |
| 10 | Аудио к «Диаграмме» — `sm1_u2_test_b10`. Ключ блока 11 по выгрузке: точка k ↔ вариант k — 1 Amy, 2 Tom, 3 Sam, 4 Ben, 5 Lily (слева направо: девочка с мячом, мальчик с поездом, мальчик со змеем, мальчик с самолётом, девочка с куклой). Сверить с записью. |
| 12–13 | У блока «Верно / неверно» в рендере нет картинки, поэтому полка с игрушками стоит текстом-картинкой перед ним (блок 12). |
