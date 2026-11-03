# Go Getter 2 — вычитка картинок (03.11.2026)

Проход по решению Анны от 03.11.2026: начинаем вычитку картинок с Go Getter,
каждый курс делаем целиком в одном стиле. Здесь только осмотр и промпты —
**ничего не сгенерировано и ничего в базе не изменено**.

Контактные листы, по которым смотрели, — `docs/vychitka/kartinki/gg2_listy/`
(24 листа, картинки показаны в том размере, в каком их видит ребёнок).

## Стиль курса

| что | строка стиля |
|---|---|
| сцены, места, люди | `clean photograph, sharp focus, natural colours, bright daylight` |
| отдельные предметы | `3D rendered cartoon illustration, soft rounded shapes, bright friendly colours, clean studio lighting` |

Предметы курса уже сделаны 3D-рендером и стилю соответствуют — их не трогаем.
Перерисовываем то, что по стилю должно быть фотографией, а сейчас нарисовано
3D-мультяшкой: людей, сцены и места.

## Сводка

| | штук |
|---|---|
| всего файлов в `media/gg2/` | 424 |
| из них используются в базе | 375 |
| **не используются ни в одном блоке** | **49** |
| оставляем как есть (3D-предмет, стиль курса) | 134 |
| оставляем как есть (материал из учебника, `book_*`) | 42 |
| оставляем как есть (новые фотографии от 03.11, `photo_*`) | 9 |
| **перерисовать** | **190** |

Причины перерисовки:

| причина | штук |
|---|---|
| разнобой в стиле: 3D-мультперсонаж или рисованное место там, где по стилю курса нужна фотография | 177 |
| мыло: зернистый вырез из учебника ~200 px | 6 |
| ключ: предлоги «собачка и будка» (плюс те же 230 px и зерно) | 5 |
| водяной знак в кадре | 1 |
| плоский вектор посреди 3D-курса | 1 |

Генерация — 190 картинок. При лимите Cloudflare ~50 в сутки это **четыре дня**.

## 🟥 ВОПРОСЫ И РЕШЕНИЯ

🟥 **1. Юнит 5, Homework 1, блок 9 — ключи предлогов похоже перепутаны.**
Блок `match` «Где собачка? Соедини картинку с предлогом». Сейчас:
`book_dog_2` → **next to**, `book_dog_3` → **opposite**. А на картинках наоборот:
на `book_dog_2` собака сидит **в стороне от будки и лицом к ней** (это *opposite*),
на `book_dog_3` собака лежит **вплотную к стенке будки** (это *next to*).
Если не поправить, два пункта из пяти ребёнок не сможет решить правильно.
**Блок в базе не трогали** — ждём «да», тогда поменяем местами ключи.
В промптах ниже `book_dog_2` и `book_dog_3` описаны уже по правильным ключам.

🟥 **2. Юнит 8, Homework 6, блок 3 — `photo_mummy.webp`.**
Пункт «Sleep with an Egyptian mummy!», а на фотографии золотая погребальная
маска Тутанхамона, а не мумия. Ребёнок соберёт пару по исключению, но картинка
спорит с подписью. Перерисовать на забинтованную мумию в музейной витрине?

🟥 **3. Юнит 4, Homework 7, блок 8 — `book_pizza.webp` с водяным знаком.**
В кадре подпись «designed by @freepik.com». Это чужая стоковая картинка, в
курсе её быть не должно. Перерисовываем — промпт ниже.

🟥 **4. 49 файлов в `media/gg2/` ни в одном блоке не используются** (список в
таблице). Половина — набор про мальчика Стива (`steve_*`, 7 картинок) и
дублирующая лексика юнита 1. Удалять не стали. Оставляем лежать или вычистить?

## Как заменяем

**Имена файлов не меняются.** Новая картинка кладётся на место старой по тому же
пути — блоки в базе править не надо. Исключений нет.

Размер под хранение: карточка 600–800 px по большей стороне, сцена 1200–1600,
webp 88–90 (правило из `docs/vychitka/kartinki/plan.md`). Сейчас у карточек
курса 300–400 px — это и есть вторая причина, по которой они мягкие на платформе.

## Таблица по файлам

### final

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `book_tom_surprise.webp` | 900×601 | ю9 · Final Test · б.8 (speaking) | не перерисовываем | кадры истории из учебника |

### u0

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `armchair.webp` | 400×381 | ю0 · Unit 0 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `draw.webp` | 400×299 | ю0 · Unit 0 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `february.webp` | 269×381 | — | **не используется** | в базе ссылок нет |
| `scene_bedroom.webp` | 880×587 | ю0 · Unit 0 Test · б.13 (speaking) | перерисовать фотографией | рисованная сцена с подростком — по стилю курса должна быть фотография |
| `shelves.webp` | 376×400 | ю0 · Unit 0 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `skateboard.webp` | 400×240 | ю0 · Unit 0 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `wardrobe.webp` | 276×400 | ю0 · Unit 0 Test · б.2 (exact_input)<br>ю9 · Final Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |

### u1

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `ballet.webp` | 393×347 | — | **не используется** | в базе ссылок нет |
| `ballet_girl.webp` | 390×400 | ю1 · Homework 7 · б.7 (order) | перерисовать фотографией | 3D-мультперсонаж рядом с настоящими фотографиями — по стилю курса фотография |
| `basketball.webp` | 287×388 | — | **не используется** | в базе ссылок нет |
| `book_after_school.webp` | 403×233 | ю1 · Homework 2 · б.2 (text) | не перерисовываем | разворот учебника, City Creatures — не генерируем |
| `book_carla_rocco.webp` | 527×264 | ю1 · Homework 3 · б.10 (gaps) | не перерисовываем | разворот учебника, City Creatures — не генерируем |
| `book_carla_rocco_table.webp` | 397×223 | ю1 · Homework 3 · б.11 (task) | не перерисовываем | разворот учебника, City Creatures — не генерируем |
| `book_football_question.webp` | 307×364 | ю1 · Homework 3 · б.2 (text) | не перерисовываем | разворот учебника, City Creatures — не генерируем |
| `book_park.webp` | 900×466 | ю1 · Homework 3 · б.5 (quiz) | не перерисовываем | разворот учебника, City Creatures — не генерируем |
| `calculator.webp` | 674×690 | ю1 · Homework 1 · б.7 (flashcards)<br>ю1 · Homework 1 · б.8 (match)<br>ю1 · Homework 1 · б.9 (exact_input)<br>ю1 · Unit 1 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `canteen.webp` | 352×335 | ю1 · Homework 5 · б.2 (flashcards)<br>ю1 · Homework 5 · б.3 (match) | перерисовать фотографией | помещение школы — по стилю курса фотография |
| `chess.webp` | 400×231 | — | **не используется** | в базе ссылок нет |
| `chicken_chips.webp` | 393×267 | — | **не используется** | в базе ссылок нет |
| `classroom.webp` | 362×335 | ю1 · Homework 5 · б.2 (flashcards)<br>ю1 · Homework 5 · б.3 (match) | перерисовать фотографией | помещение школы — по стилю курса фотография |
| `computer_room.webp` | 354×336 | ю1 · Homework 5 · б.2 (flashcards)<br>ю1 · Homework 5 · б.3 (match) | перерисовать фотографией | помещение школы — по стилю курса фотография |
| `dictionary.webp` | 366×285 | ю1 · Homework 1 · б.7 (flashcards)<br>ю1 · Homework 1 · б.8 (match)<br>ю1 · Homework 1 · б.9 (exact_input)<br>ю1 · Unit 1 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `fish_chips.webp` | 318×343 | — | **не используется** | в базе ссылок нет |
| `football.webp` | 356×321 | — | **не используется** | в базе ссылок нет |
| `football_morning.webp` | 400×377 | ю1 · Homework 7 · б.9 (order) | перерисовать фотографией | 3D-мультперсонаж рядом с настоящими фотографиями — по стилю курса фотография |
| `gym.webp` | 352×352 | ю1 · Homework 5 · б.2 (flashcards)<br>ю1 · Homework 5 · б.3 (match) | перерисовать фотографией | помещение школы — по стилю курса фотография |
| `hall.webp` | 361×351 | ю1 · Homework 5 · б.2 (flashcards)<br>ю1 · Homework 5 · б.3 (match) | перерисовать фотографией | помещение школы — по стилю курса фотография |
| `history_lesson.webp` | 400×350 | ю1 · Homework 6 · б.5 (quiz) | перерисовать фотографией | 3D-мультперсонаж рядом с настоящими фотографиями — по стилю курса фотография |
| `interview.webp` | 400×386 | ю1 · Homework 4 · б.2 (text) | перерисовать фотографией | 3D-мультперсонаж рядом с настоящими фотографиями — по стилю курса фотография |
| `karate.webp` | 268×372 | — | **не используется** | в базе ссылок нет |
| `karen_chess_club.webp` | 400×398 | ю1 · Homework 4 · б.6 (gaps) | перерисовать фотографией | 3D-мультперсонаж рядом с настоящими фотографиями — по стилю курса фотография |
| `kids_football.webp` | 400×391 | ю1 · Homework 6 · б.5 (quiz) | перерисовать фотографией | 3D-мультперсонаж рядом с настоящими фотографиями — по стилю курса фотография |
| `laptop.webp` | 366×317 | ю1 · Homework 1 · б.7 (flashcards)<br>ю1 · Homework 1 · б.8 (match)<br>ю1 · Homework 1 · б.9 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `library.webp` | 354×352 | ю1 · Homework 5 · б.2 (flashcards)<br>ю1 · Homework 5 · б.3 (match) | перерисовать фотографией | помещение школы — по стилю курса фотография |
| `lily_bus.webp` | 357×381 | — | **не используется** | в базе ссылок нет |
| `lunch_box.webp` | 349×342 | ю1 · Homework 7 · б.10 (order) | оставляем | 3D-предмет, стиль курса |
| `map.webp` | 395×263 | ю1 · Homework 1 · б.7 (flashcards)<br>ю1 · Homework 1 · б.8 (match)<br>ю1 · Homework 1 · б.9 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `mark.webp` | 324×400 | ю1 · Homework 6 · б.2 (text) | перерисовать фотографией | 3D-мультперсонаж рядом с настоящими фотографиями — по стилю курса фотография |
| `mark_chess.webp` | 400×375 | ю1 · Homework 6 · б.5 (quiz) | перерисовать фотографией | 3D-мультперсонаж рядом с настоящими фотографиями — по стилю курса фотография |
| `mark_science.webp` | 400×383 | ю1 · Homework 6 · б.5 (quiz) | перерисовать фотографией | 3D-мультперсонаж рядом с настоящими фотографиями — по стилю курса фотография |
| `music.webp` | 376×332 | — | **не используется** | в базе ссылок нет |
| `painting.webp` | 241×400 | — | **не используется** | в базе ссылок нет |
| `paints.webp` | 343×297 | ю1 · Homework 1 · б.7 (flashcards)<br>ю1 · Homework 1 · б.8 (match)<br>ю1 · Homework 1 · б.9 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `pencil.webp` | 310×281 | — | **не используется** | в базе ссылок нет |
| `pencil_case.webp` | 374×261 | ю1 · Homework 1 · б.7 (flashcards)<br>ю1 · Homework 1 · б.8 (match)<br>ю1 · Homework 1 · б.9 (exact_input)<br>ю1 · Unit 1 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `photo_boarding_school.webp` | 900×675 | ю1 · Homework 5 · б.6 (text) | оставляем | новая фотография (03.11), ключу не противоречит |
| `playground.webp` | 351×352 | ю1 · Homework 5 · б.2 (flashcards)<br>ю1 · Homework 5 · б.3 (match) | перерисовать фотографией | помещение школы — по стилю курса фотография |
| `pottery.webp` | 360×319 | — | **не используется** | в базе ссылок нет |
| `rubber.webp` | 282×217 | ю1 · Homework 1 · б.7 (flashcards)<br>ю1 · Homework 1 · б.8 (match)<br>ю1 · Homework 1 · б.9 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `ruler.webp` | 376×250 | ю1 · Homework 1 · б.7 (flashcards)<br>ю1 · Homework 1 · б.8 (match)<br>ю1 · Homework 1 · б.9 (exact_input)<br>ю1 · Unit 1 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `scene_canteen.webp` | 880×587 | ю1 · Unit 1 Test · б.13 (speaking) | перерисовать фотографией | 3D-мультперсонаж рядом с настоящими фотографиями — по стилю курса фотография |
| `school_bag.webp` | 308×353 | — | **не используется** | в базе ссылок нет |
| `school_bus.webp` | 400×247 | — | **не используется** | в базе ссылок нет |
| `scissors.webp` | 318×299 | ю1 · Homework 1 · б.7 (flashcards)<br>ю1 · Homework 1 · б.8 (match)<br>ю1 · Homework 1 · б.9 (exact_input)<br>ю1 · Unit 1 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `sports_school.webp` | 354×353 | — | **не используется** | в базе ссылок нет |
| `staff_room.webp` | 361×353 | ю1 · Homework 5 · б.2 (flashcards)<br>ю1 · Homework 5 · б.3 (match) | перерисовать фотографией | помещение школы — по стилю курса фотография |
| `steve.webp` | 362×365 | — | **не используется** | в базе ссылок нет |
| `steve_art.webp` | 350×360 | — | **не используется** | в базе ссылок нет |
| `steve_basketball.webp` | 352×381 | — | **не используется** | в базе ссылок нет |
| `steve_late.webp` | 333×389 | — | **не используется** | в базе ссылок нет |
| `steve_lunch.webp` | 372×365 | — | **не используется** | в базе ссылок нет |
| `steve_maths.webp` | 362×392 | — | **не используется** | в базе ссылок нет |
| `steve_pe.webp` | 352×364 | — | **не используется** | в базе ссылок нет |
| `subj_art.webp` | 344×315 | ю1 · Homework 1 · б.2 (flashcards)<br>ю1 · Homework 1 · б.3 (quiz)<br>ю1 · Homework 1 · б.4 (match)<br>ю1 · Homework 7 · б.2 (match) | оставляем | 3D-предмет, стиль курса |
| `subj_computer.webp` | 314×222 | ю1 · Homework 1 · б.2 (flashcards)<br>ю1 · Homework 1 · б.3 (quiz)<br>ю1 · Homework 1 · б.4 (match)<br>ю1 · Homework 7 · б.2 (match) | оставляем | 3D-предмет, стиль курса |
| `subj_english.webp` | 368×292 | ю1 · Homework 1 · б.2 (flashcards)<br>ю1 · Homework 1 · б.3 (quiz)<br>ю1 · Homework 1 · б.4 (match)<br>ю1 · Homework 7 · б.2 (match) | оставляем | 3D-предмет, стиль курса |
| `subj_french.webp` | 386×281 | ю1 · Homework 1 · б.2 (flashcards)<br>ю1 · Homework 1 · б.3 (quiz)<br>ю1 · Homework 1 · б.4 (match)<br>ю1 · Homework 6 · б.5 (quiz) | оставляем | 3D-предмет, стиль курса |
| `subj_geography.webp` | 364×322 | ю1 · Homework 1 · б.2 (flashcards)<br>ю1 · Homework 1 · б.3 (quiz)<br>ю1 · Homework 1 · б.4 (match)<br>ю1 · Homework 7 · б.2 (match) | оставляем | 3D-предмет, стиль курса |
| `subj_history.webp` | 380×272 | ю1 · Homework 1 · б.2 (flashcards)<br>ю1 · Homework 1 · б.3 (quiz)<br>ю1 · Homework 1 · б.4 (match)<br>ю1 · Homework 7 · б.2 (match) | оставляем | 3D-предмет, стиль курса |
| `subj_maths.webp` | 364×289 | ю1 · Homework 1 · б.2 (flashcards)<br>ю1 · Homework 1 · б.3 (quiz)<br>ю1 · Homework 1 · б.4 (match)<br>ю1 · Homework 7 · б.2 (match) | оставляем | 3D-предмет, стиль курса |
| `subj_music.webp` | 383×358 | ю1 · Homework 1 · б.2 (flashcards)<br>ю1 · Homework 1 · б.3 (quiz)<br>ю1 · Homework 1 · б.4 (match)<br>ю1 · Homework 7 · б.2 (match) | оставляем | 3D-предмет, стиль курса |
| `subj_pe.webp` | 376×320 | ю1 · Homework 1 · б.2 (flashcards)<br>ю1 · Homework 1 · б.3 (quiz)<br>ю1 · Homework 1 · б.4 (match)<br>ю1 · Homework 7 · б.2 (match) | оставляем | 3D-предмет, стиль курса |
| `subj_science.webp` | 355×391 | ю1 · Homework 1 · б.2 (flashcards)<br>ю1 · Homework 1 · б.3 (quiz)<br>ю1 · Homework 1 · б.4 (match)<br>ю1 · Homework 7 · б.2 (match) | оставляем | 3D-предмет, стиль курса |
| `tennis.webp` | 328×338 | — | **не используется** | в базе ссылок нет |
| `tennis_players.webp` | 348×379 | — | **не используется** | в базе ссылок нет |
| `trainers.webp` | 376×245 | ю1 · Homework 1 · б.7 (flashcards)<br>ю1 · Homework 1 · б.8 (match)<br>ю1 · Homework 1 · б.9 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `tv.webp` | 328×289 | — | **не используется** | в базе ссылок нет |
| `walk_to_school.webp` | 400×390 | ю1 · Homework 6 · б.8 (gaps)<br>ю1 · Homework 7 · б.8 (order) | перерисовать фотографией | 3D-мультперсонаж рядом с настоящими фотографиями — по стилю курса фотография |

### u2

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `anya_pancakes.webp` | 314×400 | ю2 · Homework 2 · б.10 (text) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `apple.webp` | 276×279 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.3 (quiz)<br>ю2 · Homework 1 · б.4 (match) | оставляем | 3D-предмет, стиль курса |
| `banana.webp` | 380×347 | — | **не используется** | в базе ссылок нет |
| `bar_of_chocolate.webp` | 400×298 | ю2 · Homework 4 · б.2 (flashcards)<br>ю2 · Homework 4 · б.3 (quiz)<br>ю2 · Homework 4 · б.4 (match) | оставляем | 3D-предмет, стиль курса |
| `biscuits.webp` | 365×238 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.4 (match)<br>ю2 · Homework 7 · б.2 (match)<br>ю2 · Unit 2 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `book_bake_perfect.webp` | 654×591 | ю2 · Homework 2 · б.6 (text) | не перерисовываем | разворот учебника (Hammy) — не генерируем |
| `bottle_of_water.webp` | 139×400 | ю2 · Homework 4 · б.2 (flashcards)<br>ю2 · Homework 4 · б.3 (quiz)<br>ю2 · Homework 4 · б.4 (match) | оставляем | 3D-предмет, стиль курса |
| `bread.webp` | 365×303 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.3 (quiz)<br>ю2 · Homework 1 · б.4 (match) | оставляем | 3D-предмет, стиль курса |
| `butter.webp` | 390×251 | ю2 · Homework 2 · б.2 (flashcards)<br>ю2 · Homework 2 · б.3 (match)<br>ю2 · Homework 2 · б.4 (exact_input)<br>ю2 · Homework 7 · б.2 (match) | оставляем | 3D-предмет, стиль курса |
| `cafe_waiter.webp` | 400×377 | ю2 · Homework 4 · б.7 (text) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `can_of_cola.webp` | 208×391 | ю2 · Homework 4 · б.2 (flashcards)<br>ю2 · Homework 4 · б.3 (quiz)<br>ю2 · Homework 4 · б.4 (match) | оставляем | 3D-предмет, стиль курса |
| `carton_of_juice.webp` | 209×400 | ю2 · Homework 4 · б.2 (flashcards)<br>ю2 · Homework 4 · б.3 (quiz)<br>ю2 · Homework 4 · б.4 (match) | оставляем | 3D-предмет, стиль курса |
| `cereal.webp` | 355×281 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.4 (match)<br>ю2 · Homework 7 · б.2 (match)<br>ю2 · Unit 2 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `cheese.webp` | 313×266 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.3 (quiz)<br>ю2 · Homework 1 · б.4 (match) | оставляем | 3D-предмет, стиль курса |
| `chicken.webp` | 400×309 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.3 (quiz)<br>ю2 · Homework 1 · б.4 (match) | оставляем | 3D-предмет, стиль курса |
| `chicken_rice.webp` | 398×285 | — | **не используется** | в базе ссылок нет |
| `chips.webp` | 365×266 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.3 (quiz)<br>ю2 · Homework 1 · б.4 (match) | оставляем | 3D-предмет, стиль курса |
| `chocolate.webp` | 372×298 | ю2 · Homework 2 · б.2 (flashcards)<br>ю2 · Homework 2 · б.3 (match)<br>ю2 · Homework 2 · б.4 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `egg.webp` | 334×237 | ю2 · Homework 2 · б.2 (flashcards)<br>ю2 · Homework 2 · б.3 (match)<br>ю2 · Homework 2 · б.4 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `english_breakfast.webp` | 399×291 | — | **не используется** | в базе ссылок нет |
| `fish.webp` | 400×232 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.3 (quiz)<br>ю2 · Homework 1 · б.4 (match) | оставляем | 3D-предмет, стиль курса |
| `fish_and_chips.webp` | 388×292 | — | **не используется** | в базе ссылок нет |
| `flour.webp` | 329×357 | ю2 · Homework 2 · б.2 (flashcards)<br>ю2 · Homework 2 · б.3 (match)<br>ю2 · Homework 2 · б.4 (exact_input)<br>ю2 · Homework 7 · б.2 (match) | оставляем | 3D-предмет, стиль курса |
| `fruit.webp` | 371×302 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.5 (match) | оставляем | 3D-предмет, стиль курса |
| `ham.webp` | 379×224 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.5 (match)<br>ю2 · Homework 7 · б.2 (match)<br>ю2 · Unit 2 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `hot_dog_cart.webp` | 400×385 | ю2 · Homework 7 · б.6 (gaps) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `jar_of_jam.webp` | 260×390 | ю2 · Homework 4 · б.2 (flashcards)<br>ю2 · Homework 4 · б.3 (quiz)<br>ю2 · Homework 4 · б.4 (match) | оставляем | 3D-предмет, стиль курса |
| `lemon.webp` | 310×255 | ю2 · Homework 2 · б.2 (flashcards)<br>ю2 · Homework 2 · б.3 (match)<br>ю2 · Homework 2 · б.4 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `max.webp` | 361×391 | ю2 · Homework 1 · б.9 (text) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `meat.webp` | 380×224 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.5 (match) | оставляем | 3D-предмет, стиль курса |
| `milk.webp` | 319×338 | ю2 · Homework 2 · б.2 (flashcards)<br>ю2 · Homework 2 · б.3 (match)<br>ю2 · Homework 2 · б.4 (exact_input)<br>ю2 · Homework 7 · б.2 (match) | оставляем | 3D-предмет, стиль курса |
| `orange_juice.webp` | 322×297 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.5 (match) | оставляем | 3D-предмет, стиль курса |
| `packet_of_biscuits.webp` | 400×293 | ю2 · Homework 4 · б.2 (flashcards)<br>ю2 · Homework 4 · б.3 (quiz)<br>ю2 · Homework 4 · б.4 (match) | оставляем | 3D-предмет, стиль курса |
| `pancakes.webp` | 316×275 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.3 (quiz)<br>ю2 · Homework 1 · б.5 (match)<br>ю2 · Homework 5 · б.2 (text)<br>ю2 · Homework 7 · б.2 (match) | оставляем | 3D-предмет, стиль курса |
| `pasta.webp` | 400×246 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.3 (quiz)<br>ю2 · Homework 1 · б.5 (match) | оставляем | 3D-предмет, стиль курса |
| `penny_breakfast.webp` | 400×374 | ю2 · Homework 6 · б.2 (text) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `potato.webp` | 345×237 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.5 (match) | оставляем | 3D-предмет, стиль курса |
| `rice.webp` | 338×266 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.3 (quiz)<br>ю2 · Homework 1 · б.5 (match) | оставляем | 3D-предмет, стиль курса |
| `salad.webp` | 373×291 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.6 (match) | оставляем | 3D-предмет, стиль курса |
| `sandwich.webp` | 380×231 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.3 (quiz)<br>ю2 · Homework 1 · б.6 (match) | оставляем | 3D-предмет, стиль курса |
| `sausage.webp` | 356×271 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.6 (match)<br>ю2 · Unit 2 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `scene_breakfast.webp` | 880×587 | ю2 · Homework 3 · б.5 (task)<br>ю2 · Unit 2 Test · б.13 (speaking) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `strawberry.webp` | 359×316 | ю2 · Homework 2 · б.2 (flashcards)<br>ю2 · Homework 2 · б.3 (match)<br>ю2 · Homework 2 · б.4 (exact_input)<br>ю2 · Homework 7 · б.2 (match) | оставляем | 3D-предмет, стиль курса |
| `sugar.webp` | 338×262 | ю2 · Homework 2 · б.2 (flashcards)<br>ю2 · Homework 2 · б.3 (match)<br>ю2 · Homework 2 · б.4 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `susie.webp` | 324×389 | — | **не используется** | в базе ссылок нет |
| `three_meals.webp` | 400×287 | ю2 · Homework 1 · б.12 (task) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `toast.webp` | 400×351 | ю2 · Homework 7 · б.8 (gaps) | оставляем | 3D-предмет, стиль курса |
| `tom_matt_list.webp` | 400×349 | ю2 · Homework 2 · б.13 (text) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `tomato.webp` | 280×285 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.3 (quiz)<br>ю2 · Homework 1 · б.6 (match) | оставляем | 3D-предмет, стиль курса |
| `tuna.webp` | 318×352 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.6 (match) | оставляем | 3D-предмет, стиль курса |
| `vegetables.webp` | 372×316 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.6 (match)<br>ю9 · Final Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `water.webp` | 265×348 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.6 (match) | оставляем | 3D-предмет, стиль курса |
| `yoghurt.webp` | 270×334 | ю2 · Homework 1 · б.2 (flashcards)<br>ю2 · Homework 1 · б.3 (quiz)<br>ю2 · Homework 1 · б.6 (match)<br>ю2 · Homework 7 · б.2 (match)<br>ю2 · Unit 2 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |

### u3

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `angry.webp` | 380×367 | ю3 · Homework 4 · б.3 (match) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `angry_bird.webp` | 378×400 | ю3 · Homework 4 · б.6 (task) | оставляем | мультживотные в действии — фотографией не снимается, набор однороден |
| `animals_eating.webp` | 371×306 | ю3 · Homework 2 · б.4 (match) | оставляем | мультживотные в действии — фотографией не снимается, набор однороден |
| `animals_reading.webp` | 343×324 | ю3 · Homework 2 · б.4 (match) | оставляем | мультживотные в действии — фотографией не снимается, набор однороден |
| `bear_panda_walking.webp` | 362×359 | ю3 · Homework 2 · б.12 (order) | оставляем | мультживотные в действии — фотографией не снимается, набор однороден |
| `book_billy_janet.webp` | 900×467 | ю3 · Homework 4 · б.18 (gaps) | не перерисовываем | разворот учебника — не генерируем |
| `book_boy_selfie.webp` | 196×203 | ю3 · Homework 7 · б.3 (exact_input) | перерисовать | крошечный зернистый вырез из учебника (~200 px) — мылится; у нас уже есть свои картинки на те же действия |
| `book_carla_big_al.webp` | 542×518 | ю3 · Homework 3 · б.13 (gaps) | не перерисовываем | разворот учебника — не генерируем |
| `book_dad_phone.webp` | 200×208 | ю3 · Homework 7 · б.3 (exact_input) | перерисовать | крошечный зернистый вырез из учебника (~200 px) — мылится; у нас уже есть свои картинки на те же действия |
| `book_download_song.webp` | 202×201 | ю3 · Homework 7 · б.3 (exact_input) | перерисовать | крошечный зернистый вырез из учебника (~200 px) — мылится; у нас уже есть свои картинки на те же действия |
| `book_janet_mrs_dee.webp` | 900×480 | ю3 · Homework 4 · б.17 (gaps) | не перерисовываем | разворот учебника — не генерируем |
| `book_penny_diary.webp` | 319×900 | — | **не используется** | в базе ссылок нет |
| `book_pets_site.webp` | 210×212 | ю3 · Homework 7 · б.3 (exact_input) | перерисовать | крошечный зернистый вырез из учебника (~200 px) — мылится; у нас уже есть свои картинки на те же действия |
| `book_short_answers.webp` | 480×354 | ю3 · Homework 3 · б.4 (text) | не перерисовываем | разворот учебника — не генерируем |
| `book_text_hi.webp` | 196×202 | ю3 · Homework 7 · б.3 (exact_input) | перерисовать | крошечный зернистый вырез из учебника (~200 px) — мылится; у нас уже есть свои картинки на те же действия |
| `book_video_chat.webp` | 207×210 | ю3 · Homework 7 · б.3 (exact_input) | перерисовать | крошечный зернистый вырез из учебника (~200 px) — мылится; у нас уже есть свои картинки на те же действия |
| `bored.webp` | 369×377 | ю3 · Homework 4 · б.3 (match) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `bored_students.webp` | 400×327 | ю3 · Homework 4 · б.8 (task) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `bunny_dancing.webp` | 248×346 | ю3 · Homework 2 · б.9 (order) | оставляем | мультживотные в действии — фотографией не снимается, набор однороден |
| `camera.webp` | 400×286 | ю3 · Homework 1 · б.2 (flashcards)<br>ю3 · Homework 1 · б.5 (quiz)<br>ю3 · Homework 1 · б.6 (match)<br>ю3 · Unit 3 Test · б.2 (exact_input)<br>ю7 · Homework 3 · б.3 (match)<br>ю7 · Homework 7 · б.6 (match) | оставляем | 3D-предмет, стиль курса |
| `cat_sitting.webp` | 240×326 | ю3 · Homework 2 · б.4 (match) | оставляем | мультживотные в действии — фотографией не снимается, набор однороден |
| `cat_tired.webp` | 400×227 | ю3 · Homework 4 · б.5 (task) | оставляем | мультживотные в действии — фотографией не снимается, набор однороден |
| `chat_online.webp` | 359×353 | ю3 · Homework 1 · б.3 (flashcards)<br>ю3 · Homework 1 · б.10 (match)<br>ю3 · Homework 1 · б.13 (exact_input) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `computer.webp` | 400×286 | ю3 · Homework 1 · б.2 (flashcards)<br>ю3 · Homework 1 · б.5 (quiz)<br>ю3 · Homework 1 · б.6 (match) | оставляем | 3D-предмет, стиль курса |
| `dog_not_jumping.webp` | 255×339 | ю3 · Homework 2 · б.10 (order) | оставляем | мультживотные в действии — фотографией не снимается, набор однороден |
| `download_song.webp` | 260×340 | ю3 · Homework 1 · б.3 (flashcards)<br>ю3 · Homework 1 · б.10 (match)<br>ю3 · Homework 1 · б.13 (exact_input) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `fox_running.webp` | 337×316 | ю3 · Homework 2 · б.4 (match) | оставляем | мультживотные в действии — фотографией не снимается, набор однороден |
| `happy.webp` | 389×348 | ю3 · Homework 4 · б.3 (match) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `harry.webp` | 338×400 | ю3 · Homework 6 · б.2 (quiz) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `headphones.webp` | 377×400 | ю3 · Homework 1 · б.2 (flashcards)<br>ю3 · Homework 1 · б.5 (quiz)<br>ю3 · Homework 1 · б.7 (match)<br>ю3 · Unit 3 Test · б.2 (exact_input)<br>ю9 · Final Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `inventor.webp` | 400×374 | — | **не используется** | в базе ссылок нет |
| `jack.webp` | 356×366 | ю3 · Homework 1 · б.8 (gaps) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `keyboard.webp` | 400×104 | ю3 · Homework 1 · б.2 (flashcards)<br>ю3 · Homework 1 · б.5 (quiz)<br>ю3 · Homework 1 · б.7 (match)<br>ю3 · Unit 3 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `kittens_crying.webp` | 367×273 | ю3 · Homework 2 · б.11 (order) | оставляем | мультживотные в действии — фотографией не снимается, набор однороден |
| `laptop.webp` | 400×281 | ю3 · Homework 1 · б.2 (flashcards)<br>ю3 · Homework 1 · б.5 (quiz)<br>ю3 · Homework 1 · б.6 (match) | оставляем | 3D-предмет, стиль курса |
| `lily.webp` | 261×400 | ю3 · Homework 6 · б.3 (quiz) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `mobile_phone.webp` | 183×380 | ю3 · Homework 1 · б.2 (flashcards)<br>ю3 · Homework 1 · б.5 (quiz)<br>ю3 · Homework 1 · б.6 (match)<br>ю7 · Homework 7 · б.6 (match) | оставляем | 3D-предмет, стиль курса |
| `mouse.webp` | 369×267 | ю3 · Homework 1 · б.2 (flashcards)<br>ю3 · Homework 1 · б.5 (quiz)<br>ю3 · Homework 1 · б.7 (match) | оставляем | 3D-предмет, стиль курса |
| `pandas_not_cleaning.webp` | 391×307 | ю3 · Homework 2 · б.13 (order) | оставляем | мультживотные в действии — фотографией не снимается, набор однороден |
| `phone_call.webp` | 400×366 | ю3 · Homework 4 · б.16 (sequence) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `photo_space_camp.webp` | 900×675 | ю3 · Homework 5 · б.2 (text) | оставляем | новая фотография (03.11), ключу не противоречит |
| `printer.webp` | 400×313 | ю3 · Homework 1 · б.2 (flashcards)<br>ю3 · Homework 1 · б.5 (quiz)<br>ю3 · Homework 1 · б.7 (match)<br>ю3 · Unit 3 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `sad.webp` | 311×376 | ю3 · Homework 4 · б.3 (match) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `sarah.webp` | 387×396 | ю3 · Homework 2 · б.14 (gaps) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `scared.webp` | 301×377 | ю3 · Homework 4 · б.3 (match)<br>ю3 · Homework 4 · б.7 (task) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `scene_gadgets_breakfast.webp` | 880×587 | ю3 · Unit 3 Test · б.13 (speaking) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `scene_pool.webp` | 880×587 | ю3 · Homework 2 · б.16 (task) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `screen.webp` | 400×248 | ю3 · Homework 1 · б.2 (flashcards)<br>ю3 · Homework 1 · б.5 (quiz)<br>ю3 · Homework 1 · б.7 (match) | оставляем | 3D-предмет, стиль курса |
| `selfie_teens.webp` | 400×358 | ю3 · Homework 2 · б.18 (speaking) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `send_email.webp` | 374×355 | ю3 · Homework 1 · б.3 (flashcards)<br>ю3 · Homework 1 · б.10 (match)<br>ю3 · Homework 1 · б.13 (exact_input) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `speakers.webp` | 400×293 | ю3 · Homework 1 · б.2 (flashcards)<br>ю3 · Homework 1 · б.5 (quiz)<br>ю3 · Homework 1 · б.7 (match) | оставляем | 3D-предмет, стиль курса |
| `surf_internet.webp` | 360×368 | ю3 · Homework 1 · б.3 (flashcards)<br>ю3 · Homework 1 · б.10 (match)<br>ю3 · Homework 1 · б.13 (exact_input) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `tablet.webp` | 274×400 | ю3 · Homework 1 · б.2 (flashcards)<br>ю3 · Homework 1 · б.5 (quiz)<br>ю3 · Homework 1 · б.6 (match)<br>ю3 · Unit 3 Test · б.2 (exact_input)<br>ю7 · Homework 7 · б.6 (match) | оставляем | 3D-предмет, стиль курса |
| `take_selfie.webp` | 356×354 | ю3 · Homework 1 · б.3 (flashcards)<br>ю3 · Homework 1 · б.10 (match)<br>ю3 · Homework 1 · б.12 (gaps)<br>ю3 · Homework 1 · б.13 (exact_input) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `talk_phone.webp` | 272×377 | ю3 · Homework 1 · б.3 (flashcards)<br>ю3 · Homework 1 · б.10 (match)<br>ю3 · Homework 1 · б.13 (exact_input) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `text_friend.webp` | 363×382 | ю3 · Homework 1 · б.3 (flashcards)<br>ю3 · Homework 1 · б.10 (match)<br>ю3 · Homework 1 · б.13 (exact_input) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `tired.webp` | 366×370 | ю3 · Homework 4 · б.3 (match) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `tv.webp` | 400×322 | ю3 · Homework 1 · б.2 (flashcards)<br>ю3 · Homework 1 · б.5 (quiz)<br>ю3 · Homework 1 · б.6 (match) | оставляем | 3D-предмет, стиль курса |
| `video_call.webp` | 400×363 | ю3 · Unit 3 Test · б.10 (text) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `worried.webp` | 291×372 | ю3 · Homework 4 · б.3 (match) | перерисовать фотографией | люди и сцены — по стилю курса фотография |
| `worried_woman.webp` | 377×392 | ю3 · Homework 4 · б.9 (task) | перерисовать фотографией | люди и сцены — по стилю курса фотография |

### u4

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `beach.webp` | 400×359 | ю4 · Homework 1 · б.2 (flashcards)<br>ю4 · Homework 1 · б.3 (quiz)<br>ю4 · Homework 1 · б.4 (match)<br>ю4 · Homework 7 · б.9 (order)<br>ю4 · Unit 4 Test · б.2 (exact_input) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `beautiful.webp` | 334×390 | ю4 · Homework 3 · б.2 (flashcards)<br>ю4 · Homework 3 · б.3 (quiz)<br>ю4 · Homework 3 · б.4 (match) | оставляем | мультживотное — прилагательное читается, набор однороден |
| `bike_forest.webp` | 399×375 | ю4 · Homework 7 · б.16 (quiz) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `boat_lake.webp` | 399×397 | ю4 · Homework 7 · б.16 (quiz) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `book_billy_patty.webp` | 469×177 | ю4 · Homework 4 · б.13 (gaps) | не перерисовываем | разворот/таблица учебника — не генерируем |
| `book_city_park.webp` | 768×512 | ю4 · Homework 7 · б.17 (gaps) | не перерисовываем | разворот/таблица учебника — не генерируем |
| `book_comparative_rule.webp` | 621×900 | ю4 · Homework 2 · б.9 (text) | не перерисовываем | разворот/таблица учебника — не генерируем |
| `book_dog_attila.webp` | 900×598 | ю4 · Homework 7 · б.22 (text) | не перерисовываем | разворот/таблица учебника — не генерируем |
| `book_five_boys.webp` | 700×497 | ю4 · Homework 2 · б.20 (task) | не перерисовываем | разворот/таблица учебника — не генерируем |
| `book_game_ads.webp` | 900×241 | ю4 · Homework 7 · б.28 (task) | не перерисовываем | разворот/таблица учебника — не генерируем |
| `book_giraffe_hippo_elephant.webp` | 285×204 | ю4 · Homework 3 · б.11 (gaps) | не перерисовываем | разворот/таблица учебника — не генерируем |
| `book_icecream.webp` | 564×789 | ю4 · Homework 7 · б.10 (order) | не перерисовываем | разворот/таблица учебника — не генерируем |
| `book_kitchen_robot.webp` | 900×642 | ю4 · Homework 7 · б.21 (text) | не перерисовываем | разворот/таблица учебника — не генерируем |
| `book_lion_dog_monkey.webp` | 287×209 | ю4 · Homework 3 · б.12 (gaps) | не перерисовываем | разворот/таблица учебника — не генерируем |
| `book_look_sizes.webp` | 900×341 | ю4 · Homework 5 · б.7 (text) | не перерисовываем | разворот/таблица учебника — не генерируем |
| `book_mountain_cartoon.webp` | 320×320 | ю4 · Homework 7 · б.7 (order) | перерисовать | плоский вектор 320 px посреди 3D-курса, рядом свои горы в другой манере |
| `book_mountain_lake.webp` | 900×900 | ю4 · Unit 4 Test · б.13 (speaking) | не перерисовываем | разворот/таблица учебника — не генерируем |
| `book_opinions.webp` | 484×365 | ю4 · Homework 4 · б.7 (text) | не перерисовываем | разворот/таблица учебника — не генерируем |
| `book_pizza.webp` | 564×564 | ю4 · Homework 7 · б.8 (order) | перерисовать | ВОДЯНОЙ ЗНАК «designed by @freepik.com» в кадре + плоский вектор |
| `book_places_ai.webp` | 724×900 | ю4 · Homework 1 · б.6 (hotspot) | не перерисовываем | разворот/таблица учебника — не генерируем |
| `book_river_scene.webp` | 900×798 | ю4 · Homework 7 · б.25 (gaps)<br>ю4 · Homework 7 · б.26 (task) | не перерисовываем | разворот/таблица учебника — не генерируем |
| `book_school_records.webp` | 592×344 | — | **не используется** | в базе ссылок нет |
| `book_superlative_rule.webp` | 857×900 | ю4 · Homework 3 · б.7 (text) | не перерисовываем | разворот/таблица учебника — не генерируем |
| `boring.webp` | 400×377 | ю4 · Homework 2 · б.2 (flashcards)<br>ю4 · Homework 2 · б.3 (quiz)<br>ю4 · Homework 2 · б.4 (match) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `cheap.webp` | 388×333 | ю4 · Homework 2 · б.2 (flashcards)<br>ю4 · Homework 2 · б.3 (quiz)<br>ю4 · Homework 2 · б.4 (match) | оставляем | 3D-предмет, стиль курса |
| `cinema.webp` | 364×400 | ю4 · Homework 4 · б.1 (text) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `city.webp` | 400×389 | ю4 · Homework 1 · б.2 (flashcards)<br>ю4 · Homework 1 · б.3 (quiz)<br>ю4 · Homework 1 · б.4 (match)<br>ю4 · Homework 7 · б.16 (quiz) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `climbing.webp` | 400×333 | ю4 · Homework 7 · б.18 (match) | оставляем | 3D-предмет, стиль курса |
| `cycling.webp` | 400×362 | — | **не используется** | в базе ссылок нет |
| `dan_laptop.webp` | 399×373 | ю4 · Homework 7 · б.23 (text) | перерисовать фотографией | 3D-мультперсонаж — по стилю курса фотография |
| `dangerous.webp` | 400×221 | ю4 · Homework 2 · б.2 (flashcards)<br>ю4 · Homework 2 · б.3 (quiz)<br>ю4 · Homework 2 · б.4 (match)<br>ю4 · Homework 2 · б.5 (quiz) | оставляем | 3D-предмет, стиль курса |
| `desert.webp` | 400×282 | ю4 · Homework 1 · б.2 (flashcards)<br>ю4 · Homework 1 · б.3 (quiz)<br>ю4 · Homework 1 · б.4 (match)<br>ю4 · Homework 7 · б.3 (quiz)<br>ю4 · Unit 4 Test · б.2 (exact_input) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `difficult.webp` | 400×321 | ю4 · Homework 2 · б.2 (flashcards)<br>ю4 · Homework 2 · б.3 (quiz)<br>ю4 · Homework 2 · б.4 (match)<br>ю4 · Homework 2 · б.5 (quiz) | оставляем | 3D-предмет, стиль курса |
| `easy.webp` | 400×235 | ю4 · Homework 2 · б.2 (flashcards)<br>ю4 · Homework 2 · б.3 (quiz)<br>ю4 · Homework 2 · б.4 (match)<br>ю4 · Homework 2 · б.5 (quiz) | оставляем | 3D-предмет, стиль курса |
| `exciting.webp` | 400×332 | ю4 · Homework 2 · б.2 (flashcards)<br>ю4 · Homework 2 · б.3 (quiz)<br>ю4 · Homework 2 · б.4 (match)<br>ю4 · Homework 2 · б.5 (quiz) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `expensive.webp` | 400×323 | ю4 · Homework 2 · б.2 (flashcards)<br>ю4 · Homework 2 · б.3 (quiz)<br>ю4 · Homework 2 · б.4 (match)<br>ю4 · Homework 2 · б.5 (quiz) | оставляем | 3D-предмет, стиль курса |
| `fast.webp` | 389×287 | ю4 · Homework 3 · б.2 (flashcards)<br>ю4 · Homework 3 · б.3 (quiz)<br>ю4 · Homework 3 · б.4 (match) | оставляем | мультживотное — прилагательное читается, набор однороден |
| `fishing.webp` | 400×362 | ю4 · Homework 7 · б.18 (match) | оставляем | 3D-предмет, стиль курса |
| `forest.webp` | 400×355 | ю4 · Homework 1 · б.2 (flashcards)<br>ю4 · Homework 1 · б.3 (quiz)<br>ю4 · Homework 1 · б.4 (match)<br>ю4 · Homework 7 · б.3 (quiz) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `friendly.webp` | 292×361 | ю4 · Homework 3 · б.2 (flashcards)<br>ю4 · Homework 3 · б.3 (quiz)<br>ю4 · Homework 3 · б.4 (match) | оставляем | мультживотное — прилагательное читается, набор однороден |
| `funny.webp` | 338×361 | ю4 · Homework 3 · б.2 (flashcards)<br>ю4 · Homework 3 · б.3 (quiz)<br>ю4 · Homework 3 · б.4 (match) | оставляем | мультживотное — прилагательное читается, набор однороден |
| `high.webp` | 87×400 | ю4 · Homework 2 · б.2 (flashcards)<br>ю4 · Homework 2 · б.3 (quiz)<br>ю4 · Homework 2 · б.4 (match)<br>ю4 · Homework 2 · б.5 (quiz) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `hiking_family.webp` | 373×400 | — | **не используется** | в базе ссылок нет |
| `intelligent.webp` | 313×344 | ю4 · Homework 3 · б.2 (flashcards)<br>ю4 · Homework 3 · б.3 (quiz)<br>ю4 · Homework 3 · б.4 (match)<br>ю4 · Homework 7 · б.12 (order) | оставляем | мультживотное — прилагательное читается, набор однороден |
| `island.webp` | 400×344 | ю4 · Homework 1 · б.2 (flashcards)<br>ю4 · Homework 1 · б.3 (quiz)<br>ю4 · Homework 1 · б.4 (match)<br>ю4 · Unit 4 Test · б.2 (exact_input) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `jake_michael.webp` | 390×388 | ю4 · Homework 2 · б.18 (gaps) | перерисовать фотографией | 3D-мультперсонаж — по стилю курса фотография |
| `kayak_river.webp` | 390×373 | ю4 · Homework 7 · б.16 (quiz) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `kayaking.webp` | 400×347 | ю4 · Homework 2 · б.13 (order)<br>ю4 · Homework 7 · б.18 (match) | оставляем | 3D-предмет, стиль курса |
| `kind.webp` | 400×344 | ю4 · Homework 3 · б.2 (flashcards)<br>ю4 · Homework 3 · б.3 (quiz)<br>ю4 · Homework 3 · б.4 (match) | оставляем | мультживотное — прилагательное читается, набор однороден |
| `lake.webp` | 400×327 | ю4 · Homework 1 · б.2 (flashcards)<br>ю4 · Homework 1 · б.3 (quiz)<br>ю4 · Homework 1 · б.4 (match)<br>ю4 · Homework 7 · б.3 (quiz) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `low.webp` | 400×127 | ю4 · Homework 2 · б.2 (flashcards)<br>ю4 · Homework 2 · б.3 (quiz)<br>ю4 · Homework 2 · б.4 (match)<br>ю4 · Homework 2 · б.5 (quiz) | оставляем | 3D-предмет, стиль курса |
| `mountain.webp` | 400×362 | ю4 · Homework 1 · б.2 (flashcards)<br>ю4 · Homework 1 · б.3 (quiz)<br>ю4 · Homework 1 · б.4 (match)<br>ю4 · Homework 7 · б.3 (quiz) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `parachute.webp` | 400×396 | ю4 · Homework 7 · б.18 (match) | оставляем | 3D-предмет, стиль курса |
| `plato.webp` | 399×388 | ю4 · Homework 1 · б.8 (text) | перерисовать фотографией | 3D-мультперсонаж — по стилю курса фотография |
| `river.webp` | 400×352 | ю4 · Homework 1 · б.2 (flashcards)<br>ю4 · Homework 1 · б.3 (quiz)<br>ю4 · Homework 1 · б.4 (match) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `safe.webp` | 400×397 | ю4 · Homework 2 · б.2 (flashcards)<br>ю4 · Homework 2 · б.3 (quiz)<br>ю4 · Homework 2 · б.4 (match)<br>ю4 · Homework 2 · б.5 (quiz) | оставляем | 3D-предмет, стиль курса |
| `sailing.webp` | 339×400 | ю4 · Homework 7 · б.18 (match) | оставляем | 3D-предмет, стиль курса |
| `sea.webp` | 400×312 | ю4 · Homework 1 · б.2 (flashcards)<br>ю4 · Homework 1 · б.3 (quiz)<br>ю4 · Homework 1 · б.4 (match)<br>ю4 · Homework 7 · б.3 (quiz) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `slow.webp` | 366×282 | ю4 · Homework 2 · б.15 (order) | оставляем | мультживотное — прилагательное читается, набор однороден |
| `strong.webp` | 352×291 | ю4 · Homework 3 · б.2 (flashcards)<br>ю4 · Homework 3 · б.3 (quiz)<br>ю4 · Homework 3 · б.4 (match) | оставляем | мультживотное — прилагательное читается, набор однороден |
| `three_paintings.webp` | 880×587 | ю4 · Homework 3 · б.10 (quiz) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `tiger.webp` | 278×396 | ю4 · Homework 3 · б.13 (gaps) | оставляем | мультживотное — прилагательное читается, набор однороден |
| `town.webp` | 400×368 | ю4 · Homework 1 · б.2 (flashcards)<br>ю4 · Homework 1 · б.3 (quiz)<br>ю4 · Homework 1 · б.4 (match) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `volcano.webp` | 400×388 | ю4 · Homework 1 · б.2 (flashcards)<br>ю4 · Homework 1 · б.3 (quiz)<br>ю4 · Homework 1 · б.4 (match)<br>ю4 · Homework 7 · б.3 (quiz)<br>ю4 · Unit 4 Test · б.2 (exact_input) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `waterfall.webp` | 399×400 | ю4 · Homework 1 · б.2 (flashcards)<br>ю4 · Homework 1 · б.3 (quiz)<br>ю4 · Homework 1 · б.4 (match)<br>ю4 · Unit 4 Test · б.2 (exact_input) | перерисовать фотографией | место и пейзаж — по стилю курса фотография |
| `zak_lenny.webp` | 399×388 | ю4 · Homework 6 · б.7 (sequence) | перерисовать фотографией | 3D-мультперсонаж — по стилю курса фотография |

### u5

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `bank.webp` | 400×346 | ю5 · Homework 1 · б.2 (flashcards)<br>ю5 · Homework 1 · б.3 (quiz)<br>ю5 · Homework 1 · б.4 (match) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `big_house.webp` | 400×316 | ю5 · Homework 7 · б.2 (flashcards) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `book_dog_1.webp` | 235×205 | ю5 · Homework 1 · б.9 (match) | перерисовать | 230 px, зерно и шум; ПЛЮС ключ: dog_2 и dog_3 похоже перепутаны («next to» / «opposite») |
| `book_dog_2.webp` | 235×135 | ю5 · Homework 1 · б.9 (match) | перерисовать | 230 px, зерно и шум; ПЛЮС ключ: dog_2 и dog_3 похоже перепутаны («next to» / «opposite») |
| `book_dog_3.webp` | 230×155 | ю5 · Homework 1 · б.9 (match) | перерисовать | 230 px, зерно и шум; ПЛЮС ключ: dog_2 и dog_3 похоже перепутаны («next to» / «opposite») |
| `book_dog_4.webp` | 230×168 | ю5 · Homework 1 · б.9 (match) | перерисовать | 230 px, зерно и шум; ПЛЮС ключ: dog_2 и dog_3 похоже перепутаны («next to» / «opposite») |
| `book_dog_5.webp` | 235×168 | ю5 · Homework 1 · б.9 (match) | перерисовать | 230 px, зерно и шум; ПЛЮС ключ: dog_2 и dog_3 похоже перепутаны («next to» / «opposite») |
| `book_hammy_boat.webp` | 598×658 | ю5 · Homework 2 · б.6 (text) | не перерисовываем | карта/разворот учебника — не генерируем |
| `book_london.webp` | 900×576 | — | **не используется** | в базе ссылок нет |
| `book_map_hospital.webp` | 900×587 | ю5 · Homework 5 · б.6 (gaps) | не перерисовываем | карта/разворот учебника — не генерируем |
| `book_map_north_south.webp` | 900×352 | ю5 · Homework 1 · б.10 (gaps) | не перерисовываем | карта/разворот учебника — не генерируем |
| `book_map_river.webp` | 900×543 | ю5 · Homework 5 · б.9 (gaps)<br>ю5 · Homework 5 · б.10 (task) | не перерисовываем | карта/разворот учебника — не генерируем |
| `book_street.webp` | 900×171 | ю5 · Homework 1 · б.7 (hotspot) | не перерисовываем | карта/разворот учебника — не генерируем |
| `book_town_map.webp` | 802×503 | ю5 · Homework 1 · б.11 (task) | не перерисовываем | карта/разворот учебника — не генерируем |
| `busy_street.webp` | 400×384 | ю5 · Homework 7 · б.2 (flashcards) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `cafe.webp` | 398×361 | ю5 · Homework 1 · б.2 (flashcards)<br>ю5 · Homework 1 · б.3 (quiz)<br>ю5 · Homework 1 · б.4 (match) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `cinema.webp` | 380×355 | ю5 · Homework 1 · б.2 (flashcards)<br>ю5 · Homework 1 · б.3 (quiz)<br>ю5 · Homework 1 · б.4 (match)<br>ю5 · Unit 5 Test · б.2 (exact_input) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `clean_cinema.webp` | 400×383 | ю5 · Homework 7 · б.2 (flashcards) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `clothes_shop.webp` | 366×280 | ю5 · Homework 1 · б.2 (flashcards)<br>ю5 · Homework 1 · б.3 (quiz)<br>ю5 · Homework 1 · б.5 (match) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `dirty_cinema.webp` | 400×386 | ю5 · Homework 7 · б.2 (flashcards) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `film_studio.webp` | 400×349 | ю5 · Homework 6 · б.8 (exact_input) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `garden.webp` | 400×394 | ю5 · Homework 4 · б.3 (match) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `hospital.webp` | 400×329 | ю5 · Homework 1 · б.2 (flashcards)<br>ю5 · Homework 1 · б.3 (quiz)<br>ю5 · Homework 1 · б.4 (match) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `hotel.webp` | 400×363 | ю5 · Homework 1 · б.2 (flashcards)<br>ю5 · Homework 1 · б.3 (quiz)<br>ю5 · Homework 1 · б.4 (match) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `interesting_museum.webp` | 400×357 | ю5 · Homework 7 · б.2 (flashcards) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `kitchen.webp` | 400×395 | ю5 · Homework 4 · б.3 (match) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `library.webp` | 400×357 | ю5 · Homework 1 · б.2 (flashcards)<br>ю5 · Homework 1 · б.3 (quiz)<br>ю5 · Homework 1 · б.4 (match)<br>ю5 · Unit 5 Test · б.2 (exact_input) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `museum.webp` | 400×348 | ю5 · Homework 1 · б.2 (flashcards)<br>ю5 · Homework 1 · б.3 (quiz)<br>ю5 · Homework 1 · б.5 (match)<br>ю5 · Unit 5 Test · б.2 (exact_input)<br>ю9 · Final Test · б.2 (exact_input) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `new_stadium.webp` | 400×386 | ю5 · Homework 7 · б.2 (flashcards) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `old_stadium.webp` | 400×384 | ю5 · Homework 7 · б.2 (flashcards) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `park.webp` | 400×353 | ю5 · Homework 1 · б.2 (flashcards)<br>ю5 · Homework 1 · б.3 (quiz)<br>ю5 · Homework 1 · б.4 (match) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `park_small.webp` | 400×391 | ю5 · Homework 4 · б.3 (match) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `photo_hollywood.webp` | 900×675 | ю5 · Homework 6 · б.2 (text) | оставляем | новая фотография (03.11), ключу не противоречит |
| `photo_portree.webp` | 900×675 | ю5 · Homework 7 · б.8 (quiz) | оставляем | новая фотография (03.11), ключу не противоречит |
| `police_station.webp` | 393×347 | ю5 · Homework 6 · б.8 (exact_input) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `post_office.webp` | 392×361 | ю5 · Homework 6 · б.8 (exact_input) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `quiet_street.webp` | 400×382 | ю5 · Homework 7 · б.2 (flashcards) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `restaurant.webp` | 400×323 | ю5 · Homework 1 · б.2 (flashcards)<br>ю5 · Homework 1 · б.3 (quiz)<br>ю5 · Homework 1 · б.5 (match)<br>ю5 · Unit 5 Test · б.2 (exact_input) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `scene_street.webp` | 880×495 | ю5 · Unit 5 Test · б.13 (speaking) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `shopping_centre.webp` | 400×302 | ю5 · Homework 6 · б.8 (exact_input) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `small_house.webp` | 400×331 | ю5 · Homework 7 · б.2 (flashcards) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `sports_centre.webp` | 387×312 | ю5 · Homework 6 · б.8 (exact_input) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `stadium.webp` | 400×307 | ю5 · Homework 1 · б.2 (flashcards)<br>ю5 · Homework 1 · б.3 (quiz)<br>ю5 · Homework 1 · б.5 (match)<br>ю5 · Unit 5 Test · б.2 (exact_input) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `supermarket.webp` | 400×294 | ю5 · Homework 1 · б.2 (flashcards)<br>ю5 · Homework 1 · б.3 (quiz)<br>ю5 · Homework 1 · б.5 (match) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `swimming_pool.webp` | 378×330 | ю5 · Homework 6 · б.8 (exact_input) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `theatre.webp` | 397×351 | ю5 · Homework 1 · б.2 (flashcards)<br>ю5 · Homework 1 · б.3 (quiz)<br>ю5 · Homework 1 · б.5 (match) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `theme_park.webp` | 400×353 | ю5 · Homework 6 · б.8 (exact_input) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `town_now.webp` | 400×362 | ю5 · Homework 7 · б.7 (task) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `town_past.webp` | 400×362 | ю5 · Homework 7 · б.7 (task) | перерисовать фотографией | место в городе — по стилю курса фотография |
| `train_station.webp` | 381×358 | ю5 · Homework 6 · б.8 (exact_input) | перерисовать фотографией | место в городе — по стилю курса фотография |

### u6

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `artist.webp` | 374×386 | ю6 · Homework 1 · б.2 (flashcards)<br>ю6 · Homework 1 · б.3 (quiz)<br>ю6 · Homework 1 · б.5 (match) | перерисовать фотографией | человек по профессии — по стилю курса фотография |
| `book_jobs_chores.webp` | 800×362 | ю6 · Homework 6 · б.8 (task) | не перерисовываем | разворот/записка учебника — не генерируем |
| `book_permission_note.webp` | 869×478 | ю6 · Homework 5 · б.11 (task) | не перерисовываем | разворот/записка учебника — не генерируем |
| `book_time_now.webp` | 900×586 | ю6 · Homework 3 · б.7 (gaps) | не перерисовываем | разворот/записка учебника — не генерируем |
| `builder.webp` | 331×386 | ю6 · Homework 1 · б.2 (flashcards)<br>ю6 · Homework 1 · б.3 (quiz)<br>ю6 · Homework 1 · б.5 (match)<br>ю6 · Homework 7 · б.9 (match)<br>ю6 · Unit 6 Test · б.2 (exact_input) | перерисовать фотографией | человек по профессии — по стилю курса фотография |
| `bus_driver.webp` | 374×381 | ю6 · Homework 1 · б.2 (flashcards)<br>ю6 · Homework 1 · б.3 (quiz)<br>ю6 · Homework 1 · б.5 (match)<br>ю6 · Homework 1 · б.8 (exact_input) | перерисовать фотографией | человек по профессии — по стилю курса фотография |
| `chef.webp` | 324×386 | ю6 · Homework 1 · б.2 (flashcards)<br>ю6 · Homework 1 · б.3 (quiz)<br>ю6 · Homework 1 · б.5 (match)<br>ю6 · Homework 1 · б.8 (exact_input)<br>ю6 · Homework 7 · б.9 (match) | перерисовать фотографией | человек по профессии — по стилю курса фотография |
| `doctor.webp` | 223×380 | ю6 · Homework 1 · б.2 (flashcards)<br>ю6 · Homework 1 · б.3 (quiz)<br>ю6 · Homework 1 · б.8 (exact_input)<br>ю6 · Homework 7 · б.9 (match) | перерисовать фотографией | человек по профессии — по стилю курса фотография |
| `farmer.webp` | 400×387 | ю6 · Homework 1 · б.2 (flashcards)<br>ю6 · Homework 1 · б.3 (quiz)<br>ю6 · Homework 1 · б.5 (match)<br>ю6 · Homework 7 · б.9 (match) | перерисовать фотографией | человек по профессии — по стилю курса фотография |
| `footballer.webp` | 363×374 | ю6 · Homework 1 · б.2 (flashcards)<br>ю6 · Homework 1 · б.3 (quiz) | перерисовать фотографией | человек по профессии — по стилю курса фотография |
| `nurse.webp` | 226×400 | ю6 · Homework 1 · б.2 (flashcards)<br>ю6 · Homework 1 · б.3 (quiz)<br>ю6 · Homework 7 · б.9 (match)<br>ю6 · Unit 6 Test · б.2 (exact_input) | перерисовать фотографией | человек по профессии — по стилю курса фотография |
| `office_worker.webp` | 400×369 | ю6 · Homework 1 · б.2 (flashcards)<br>ю6 · Homework 1 · б.3 (quiz)<br>ю6 · Homework 1 · б.5 (match) | перерисовать фотографией | человек по профессии — по стилю курса фотография |
| `pilot.webp` | 400×331 | ю6 · Homework 1 · б.2 (flashcards)<br>ю6 · Homework 1 · б.3 (quiz)<br>ю6 · Unit 6 Test · б.2 (exact_input) | перерисовать фотографией | человек по профессии — по стилю курса фотография |
| `police_officer.webp` | 254×400 | ю6 · Homework 1 · б.2 (flashcards)<br>ю6 · Homework 1 · б.3 (quiz)<br>ю6 · Homework 1 · б.5 (match)<br>ю6 · Homework 7 · б.9 (match)<br>ю6 · Unit 6 Test · б.2 (exact_input) | перерисовать фотографией | человек по профессии — по стилю курса фотография |
| `scene_cleaning.webp` | 880×587 | ю6 · Unit 6 Test · б.13 (speaking) | перерисовать фотографией | человек по профессии — по стилю курса фотография |
| `shop_assistant.webp` | 400×354 | ю6 · Homework 1 · б.2 (flashcards)<br>ю6 · Homework 1 · б.3 (quiz)<br>ю6 · Homework 1 · б.5 (match)<br>ю6 · Unit 6 Test · б.2 (exact_input) | перерисовать фотографией | человек по профессии — по стилю курса фотография |
| `singer.webp` | 400×398 | ю6 · Homework 1 · б.2 (flashcards)<br>ю6 · Homework 1 · б.3 (quiz)<br>ю6 · Homework 1 · б.5 (match) | перерисовать фотографией | человек по профессии — по стилю курса фотография |
| `teacher.webp` | 400×396 | ю6 · Homework 1 · б.2 (flashcards)<br>ю6 · Homework 1 · б.3 (quiz)<br>ю6 · Homework 7 · б.9 (match) | перерисовать фотографией | человек по профессии — по стилю курса фотография |
| `vet.webp` | 372×400 | ю6 · Homework 1 · б.2 (flashcards)<br>ю6 · Homework 1 · б.3 (quiz)<br>ю6 · Homework 1 · б.5 (match)<br>ю6 · Homework 7 · б.9 (match) | перерисовать фотографией | человек по профессии — по стилю курса фотография |

### u7

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `arrive.webp` | 400×374 | ю7 · Homework 1 · б.4 (flashcards)<br>ю7 · Homework 1 · б.6 (match)<br>ю7 · Homework 1 · б.11 (exact_input) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `bike.webp` | 400×330 | ю7 · Homework 1 · б.2 (flashcards)<br>ю7 · Homework 1 · б.5 (match)<br>ю7 · Homework 1 · б.10 (exact_input)<br>ю7 · Homework 7 · б.11 (match)<br>ю7 · Homework 7 · б.14 (quiz) | оставляем | 3D-предмет, стиль курса |
| `boat.webp` | 400×240 | ю7 · Homework 1 · б.2 (flashcards)<br>ю7 · Homework 1 · б.5 (match)<br>ю7 · Homework 1 · б.10 (exact_input)<br>ю7 · Homework 7 · б.11 (match)<br>ю7 · Homework 7 · б.14 (quiz)<br>ю7 · Unit 7 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `book_hammy_explorer.webp` | 788×717 | ю7 · Homework 4 · б.2 (text) | не перерисовываем | разворот учебника (Hammy) / бланк билета — не генерируем |
| `book_hammy_rain.webp` | 332×274 | ю7 · Homework 2 · б.2 (text) | не перерисовываем | разворот учебника (Hammy) / бланк билета — не генерируем |
| `book_ticket.webp` | 655×256 | ю7 · Homework 5 · б.10 (gaps) | не перерисовываем | разворот учебника (Hammy) / бланк билета — не генерируем |
| `bus.webp` | 400×250 | ю7 · Homework 1 · б.2 (flashcards)<br>ю7 · Homework 1 · б.5 (match)<br>ю7 · Homework 1 · б.10 (exact_input)<br>ю7 · Homework 7 · б.11 (match) | оставляем | 3D-предмет, стиль курса |
| `car.webp` | 400×278 | ю7 · Homework 1 · б.2 (flashcards)<br>ю7 · Homework 1 · б.5 (match)<br>ю7 · Homework 1 · б.10 (exact_input)<br>ю7 · Homework 7 · б.11 (match)<br>ю7 · Homework 7 · б.14 (quiz) | оставляем | 3D-предмет, стиль курса |
| `dad_coffee.webp` | 358×370 | ю7 · Homework 2 · б.8 (order) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `dad_photos.webp` | 377×399 | ю7 · Homework 7 · б.14 (quiz) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `enzo.webp` | 362×375 | ю7 · Homework 1 · б.8 (gaps) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `everest.webp` | 385×389 | — | **не используется** | в базе ссылок нет |
| `get_off.webp` | 400×376 | ю7 · Homework 1 · б.4 (flashcards)<br>ю7 · Homework 1 · б.6 (match)<br>ю7 · Homework 1 · б.11 (exact_input) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `get_on.webp` | 400×375 | ю7 · Homework 1 · б.4 (flashcards)<br>ю7 · Homework 1 · б.6 (match)<br>ю7 · Homework 1 · б.11 (exact_input) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `guidebook.webp` | 261×400 | ю7 · Homework 3 · б.3 (match) | оставляем | 3D-предмет, стиль курса |
| `hotel.webp` | 400×374 | ю7 · Homework 4 · б.12 (quiz)<br>ю7 · Homework 7 · б.6 (match) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `kids_off_bus.webp` | 360×398 | ю7 · Homework 7 · б.14 (quiz) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `leave.webp` | 400×385 | ю7 · Homework 1 · б.4 (flashcards)<br>ю7 · Homework 1 · б.6 (match)<br>ю7 · Homework 1 · б.11 (exact_input) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `lorry.webp` | 400×290 | ю7 · Homework 7 · б.11 (match) | оставляем | 3D-предмет, стиль курса |
| `motorbike.webp` | 400×362 | ю7 · Homework 1 · б.2 (flashcards)<br>ю7 · Homework 1 · б.5 (match)<br>ю7 · Homework 1 · б.10 (exact_input)<br>ю7 · Unit 7 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `mum_stan_shop.webp` | 367×372 | ю7 · Homework 2 · б.10 (order) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `museum.webp` | 400×362 | ю7 · Homework 4 · б.12 (quiz) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `on_foot.webp` | 400×384 | — | **не используется** | в базе ссылок нет |
| `passport.webp` | 350×400 | ю7 · Homework 3 · б.3 (match) | оставляем | 3D-предмет, стиль курса |
| `penny_skateboard.webp` | 373×382 | ю7 · Homework 7 · б.2 (text) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `photo_antarctic.webp` | 900×675 | ю7 · Homework 6 · б.3 (text) | оставляем | новая фотография (03.11), ключу не противоречит |
| `photo_tenerife.webp` | 900×675 | ю7 · Homework 7 · б.7 (text) | оставляем | новая фотография (03.11), ключу не противоречит |
| `plane.webp` | 400×169 | ю7 · Homework 1 · б.2 (flashcards)<br>ю7 · Homework 1 · б.5 (match)<br>ю7 · Homework 1 · б.10 (exact_input)<br>ю7 · Homework 7 · б.11 (match)<br>ю7 · Unit 7 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `restaurant.webp` | 400×338 | ю7 · Homework 4 · б.12 (quiz) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `scene_airport.webp` | 880×587 | ю7 · Unit 7 Test · б.13 (speaking) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `scene_suitcase.webp` | 880×587 | ю7 · Homework 3 · б.2 (text) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `school_bus.webp` | 400×252 | — | **не используется** | в базе ссылок нет |
| `sightseeing.webp` | 400×378 | — | **не используется** | в базе ссылок нет |
| `socks.webp` | 380×400 | ю7 · Homework 3 · б.3 (match) | оставляем | 3D-предмет, стиль курса |
| `souvenir.webp` | 367×400 | ю7 · Homework 4 · б.12 (quiz) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `suitcase.webp` | 254×400 | ю7 · Homework 3 · б.3 (match) | оставляем | 3D-предмет, стиль курса |
| `sun_hat.webp` | 400×252 | ю7 · Homework 3 · б.3 (match) | оставляем | 3D-предмет, стиль курса |
| `sunglasses.webp` | 400×195 | ю7 · Homework 3 · б.3 (match) | оставляем | 3D-предмет, стиль курса |
| `take_bus.webp` | 400×382 | ю7 · Homework 1 · б.4 (flashcards)<br>ю7 · Homework 1 · б.6 (match)<br>ю7 · Homework 1 · б.11 (exact_input) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `take_photos.webp` | 342×400 | ю7 · Homework 4 · б.12 (quiz) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `taxi.webp` | 400×231 | ю7 · Homework 1 · б.2 (flashcards)<br>ю7 · Homework 1 · б.5 (match)<br>ю7 · Homework 1 · б.10 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `tim_pizza.webp` | 370×367 | ю7 · Homework 2 · б.7 (order) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `tina_hat.webp` | 369×375 | ю7 · Homework 2 · б.9 (order) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `train.webp` | 400×260 | ю7 · Homework 1 · б.2 (flashcards)<br>ю7 · Homework 1 · б.5 (match)<br>ю7 · Homework 1 · б.10 (exact_input)<br>ю7 · Homework 7 · б.11 (match)<br>ю7 · Unit 7 Test · б.2 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `tram.webp` | 400×310 | ю7 · Homework 1 · б.2 (flashcards)<br>ю7 · Homework 1 · б.5 (match)<br>ю7 · Homework 1 · б.10 (exact_input) | оставляем | 3D-предмет, стиль курса |
| `underground.webp` | 800×526 | ю7 · Homework 1 · б.2 (flashcards)<br>ю7 · Homework 1 · б.5 (match)<br>ю7 · Homework 1 · б.10 (exact_input)<br>ю7 · Unit 7 Test · б.2 (exact_input) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |

### u8

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `anna.webp` | 356×385 | — | **не используется** | в базе ссылок нет |
| `armful_clothes.webp` | 313×400 | ю8 · Homework 4 · б.6 (order) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `barbecue.webp` | 352×368 | ю8 · Homework 1 · б.2 (flashcards)<br>ю8 · Homework 1 · б.6 (match)<br>ю8 · Homework 1 · б.9 (quiz)<br>ю8 · Homework 1 · б.10 (exact_input)<br>ю8 · Homework 7 · б.12 (match)<br>ю8 · Unit 8 Test · б.2 (exact_input) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `beach_holiday.webp` | 384×382 | ю8 · Homework 2 · б.6 (quiz)<br>ю8 · Homework 3 · б.9 (order) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `birthday_party.webp` | 363×368 | ю8 · Homework 1 · б.2 (flashcards)<br>ю8 · Homework 1 · б.6 (match)<br>ю8 · Homework 1 · б.9 (quiz)<br>ю8 · Homework 1 · б.10 (exact_input)<br>ю8 · Homework 2 · б.10 (order)<br>ю8 · Homework 7 · б.12 (match) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `book_hammy_angry.webp` | 407×462 | ю8 · Homework 4 · б.2 (text) | не перерисовываем | разворот учебника / бланк билета — не генерируем |
| `book_hammy_holiday.webp` | 900×518 | ю8 · Homework 2 · б.2 (text) | не перерисовываем | разворот учебника / бланк билета — не генерируем |
| `book_running_poster.webp` | 529×900 | — | **не используется** | в базе ссылок нет |
| `book_tickets.webp` | 759×474 | ю8 · Homework 5 · б.15 (task) | не перерисовываем | разворот учебника / бланк билета — не генерируем |
| `bowling.webp` | 400×370 | — | **не используется** | в базе ссылок нет |
| `boy_reading.webp` | 382×383 | ю8 · Homework 2 · б.6 (quiz) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `cinema_tickets.webp` | 381×400 | — | **не используется** | в базе ссылок нет |
| `cinema_tonight.webp` | 384×381 | ю8 · Homework 2 · б.6 (quiz) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `classical.webp` | 347×400 | ю8 · Homework 4 · б.13 (quiz) | оставляем | 3D-предмет, стиль курса |
| `competition.webp` | 365×345 | ю8 · Homework 1 · б.4 (flashcards)<br>ю8 · Homework 1 · б.5 (quiz)<br>ю8 · Homework 1 · б.7 (match) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `concert.webp` | 353×367 | ю8 · Homework 1 · б.2 (flashcards)<br>ю8 · Homework 1 · б.6 (match)<br>ю8 · Homework 1 · б.10 (exact_input)<br>ю8 · Homework 7 · б.12 (match) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `concert_tickets.webp` | 400×303 | ю8 · Homework 4 · б.8 (order) | оставляем | 3D-предмет, стиль курса |
| `cook_food.webp` | 362×346 | ю8 · Homework 1 · б.4 (flashcards)<br>ю8 · Homework 1 · б.5 (quiz)<br>ю8 · Homework 1 · б.7 (match) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `costume_run.webp` | 311×400 | — | **не используется** | в базе ссылок нет |
| `country.webp` | 367×400 | ю8 · Homework 4 · б.13 (quiz) | оставляем | 3D-предмет, стиль курса |
| `dance_show.webp` | 420×420 | ю8 · Homework 1 · б.2 (flashcards)<br>ю8 · Homework 1 · б.6 (match)<br>ю8 · Homework 1 · б.9 (quiz)<br>ю8 · Homework 1 · б.10 (exact_input)<br>ю8 · Homework 7 · б.12 (match) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `fancy_dress.webp` | 420×420 | ю8 · Homework 1 · б.2 (flashcards)<br>ю8 · Homework 1 · б.6 (match)<br>ю8 · Homework 1 · б.10 (exact_input)<br>ю8 · Homework 7 · б.12 (match)<br>ю8 · Unit 8 Test · б.2 (exact_input) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `flowers.webp` | 371×400 | ю8 · Homework 4 · б.9 (order) | оставляем | 3D-предмет, стиль курса |
| `football_match.webp` | 364×350 | ю8 · Homework 1 · б.2 (flashcards)<br>ю8 · Homework 1 · б.6 (match)<br>ю8 · Homework 1 · б.10 (exact_input)<br>ю8 · Homework 7 · б.12 (match) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `fun_races.webp` | 363×400 | — | **не используется** | в базе ссылок нет |
| `get_presents.webp` | 365×346 | ю8 · Homework 1 · б.4 (flashcards)<br>ю8 · Homework 1 · б.5 (quiz)<br>ю8 · Homework 1 · б.7 (match) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `grandma_cottage.webp` | 400×371 | ю8 · Homework 2 · б.9 (order) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `homework_girl.webp` | 393×356 | ю8 · Homework 2 · б.12 (order) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `invitation.webp` | 400×350 | ю8 · Homework 7 · б.5 (text) | оставляем | 3D-предмет, стиль курса |
| `jazz.webp` | 320×391 | ю8 · Homework 4 · б.13 (quiz) | оставляем | 3D-предмет, стиль курса |
| `paint_bedroom.webp` | 384×381 | ю8 · Homework 2 · б.6 (quiz) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `photo_dinosaur.webp` | 900×675 | ю8 · Homework 6 · б.3 (match) | оставляем | новая фотография (03.11); по photo_mummy — вопрос в блоке «Вопросы и решения» |
| `photo_mummy.webp` | 900×675 | ю8 · Homework 6 · б.3 (match) | оставляем | новая фотография (03.11); по photo_mummy — вопрос в блоке «Вопросы и решения» |
| `photo_shark.webp` | 900×675 | ю8 · Homework 6 · б.3 (match) | оставляем | новая фотография (03.11); по photo_mummy — вопрос в блоке «Вопросы и решения» |
| `picnic.webp` | 352×369 | ю8 · Homework 1 · б.2 (flashcards)<br>ю8 · Homework 1 · б.6 (match)<br>ю8 · Homework 1 · б.10 (exact_input)<br>ю8 · Homework 3 · б.10 (order)<br>ю8 · Homework 7 · б.12 (match)<br>ю8 · Unit 8 Test · б.2 (exact_input) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `play.webp` | 367×371 | ю8 · Homework 1 · б.2 (flashcards)<br>ю8 · Homework 1 · б.6 (match)<br>ю8 · Homework 1 · б.10 (exact_input)<br>ю8 · Homework 7 · б.12 (match) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `pop.webp` | 351×391 | ю8 · Homework 4 · б.13 (quiz) | оставляем | 3D-предмет, стиль курса |
| `rap.webp` | 400×304 | ю8 · Homework 4 · б.13 (quiz) | оставляем | 3D-предмет, стиль курса |
| `restaurant_table.webp` | 400×354 | — | **не используется** | в базе ссылок нет |
| `rock.webp` | 348×400 | ю8 · Homework 4 · б.13 (quiz) | оставляем | 3D-предмет, стиль курса |
| `sakura.webp` | 384×349 | ю8 · Homework 2 · б.11 (order) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `scene_birthday.webp` | 880×587 | ю8 · Unit 8 Test · б.13 (speaking) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `shop_window.webp` | 387×388 | ю8 · Homework 4 · б.10 (order) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `sing_birthday.webp` | 365×346 | ю8 · Homework 1 · б.4 (flashcards)<br>ю8 · Homework 1 · б.5 (quiz)<br>ю8 · Homework 1 · б.7 (match) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `sleep_floor.webp` | 362×346 | ю8 · Homework 1 · б.4 (flashcards)<br>ю8 · Homework 1 · б.5 (quiz)<br>ю8 · Homework 1 · б.7 (match)<br>ю8 · Homework 6 · б.2 (text) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `sleepover.webp` | 353×372 | ю8 · Homework 1 · б.2 (flashcards)<br>ю8 · Homework 1 · б.6 (match)<br>ю8 · Homework 1 · б.10 (exact_input)<br>ю8 · Homework 6 · б.2 (text)<br>ю8 · Homework 7 · б.12 (match)<br>ю8 · Unit 8 Test · б.2 (exact_input)<br>ю9 · Final Test · б.2 (exact_input) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `sleepover_girls.webp` | 362×373 | ю8 · Homework 1 · б.9 (quiz)<br>ю8 · Homework 6 · б.2 (text) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `talent_competition.webp` | 365×346 | ю8 · Homework 1 · б.2 (flashcards)<br>ю8 · Homework 1 · б.6 (match)<br>ю8 · Homework 1 · б.10 (exact_input)<br>ю8 · Homework 7 · б.12 (match)<br>ю8 · Unit 8 Test · б.2 (exact_input) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `wear_costume.webp` | 298×400 | ю8 · Homework 1 · б.4 (flashcards)<br>ю8 · Homework 1 · б.5 (quiz)<br>ю8 · Homework 1 · б.7 (match) | перерисовать фотографией | люди, сцены и места — по стилю курса фотография |
| `winter_run.webp` | 306×400 | — | **не используется** | в базе ссылок нет |
## Не перерисовываем — и почему

**3D-предметы (134 файла).** Еда юнита 2, школьные принадлежности и значки
предметов юнита 1, гаджеты юнита 3, транспорт и вещи в чемодан юнита 7,
билеты и музыкальные инструменты юнита 8, предметы-прилагательные юнита 4.
Все сделаны в одной манере и ровно по строке стиля курса для предметов.

**Мультживотные (20 файлов, юниты 3 и 4).** `angry_bird`, `animals_eating`,
`animals_reading`, `bear_panda_walking`, `bunny_dancing`, `cat_sitting`,
`cat_tired`, `dog_not_jumping`, `fox_running`, `kittens_crying`,
`pandas_not_cleaning`, `beautiful`, `fast`, `friendly`, `funny`, `intelligent`,
`kind`, `slow`, `strong`, `tiger`. Их задача — показать действие или свойство
(«панды не убираются», «кот устал», «муравей сильный»), фотографией такое не
снимается. Набор однородный, менять его не на что.

**Материал из учебника (42 файла `book_*`).** Развороты, комиксы, таблицы правил,
карты города, записки, бланки билетов, кадры историй с героями City Creatures
(Big Al, Carla, Rocco, Billy, Janet, Hammy). Героев курса **не генерируем** —
решение Анны от 21.10.2026: они приходят из учебника, своя версия будет не та.
Если такая картинка понадобится крупнее — нужен разворот от методиста.

Исключения из этого правила, которые всё-таки перерисовываем: шесть крошечных
зернистых вырезов юнита 3 (`book_boy_selfie`, `book_dad_phone`,
`book_download_song`, `book_pets_site`, `book_text_hi`, `book_video_chat` —
около 200 px, героев на них нет), пять картинок с собачкой и будкой юнита 5
(230 px, зерно, плюс перепутанный ключ), `book_pizza` (водяной знак) и
`book_mountain_cartoon` (плоский вектор 320 px, героев нет).

**Новые фотографии от 03.11 (9 файлов `photo_*`).** `photo_boarding_school`,
`photo_space_camp`, `photo_hollywood`, `photo_portree`, `photo_antarctic`,
`photo_tenerife`, `photo_dinosaur`, `photo_mummy`, `photo_shark`. Сверили с
ключами заданий: расхождений нет нигде, кроме `photo_mummy` — вопрос 2 выше.

## Промпты

Один предмет — один промпт, сеток не просим. Каждый промпт — цельный блок,
строка стиля уже внутри, копируется одним нажатием.

### u0

**`media/gg2/u0/scene_bedroom.webp`** — в блоке speaking по этой картинке ребёнок называет мебель — шкаф, полка, кресло, скейтборд должны быть видны

```
clean photograph, sharp focus, natural colours, bright daylight. a teenage boy sitting on his bed in a tidy modern bedroom, reading a book; a wardrobe, a bookshelf with books, an armchair and a skateboard against the wall are all clearly visible. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u1

**`media/gg2/u1/ballet_girl.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten years old in a pink ballet leotard and tutu, standing on tiptoe in a ballet pose, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/canteen.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. an empty school canteen: a serving counter with trays and food, long tables and stools, large windows. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/classroom.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. an empty school classroom: rows of desks and chairs, a green board on the wall, a world map, a window with daylight. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/computer_room.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. an empty school computer room: rows of desks with desktop computers and chairs, bright windows. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/football_morning.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. four schoolchildren playing football on a green school pitch on a sunny morning. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/gym.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. an empty school gymnasium: wooden floor with court lines, wall bars, a basketball hoop, gym mats stacked at the side. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/hall.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. an empty school corridor with rows of blue lockers along the walls and a shiny floor. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/history_lesson.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a history lesson: a woman teacher standing beside a projector screen showing an old castle, schoolchildren sitting at desks watching. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/interview.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a woman reporter holding a microphone and interviewing a man in the street of an old European city. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/karen_chess_club.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a schoolgirl and a man teacher sitting opposite each other at a chess board in a school club room, other children in the background. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/kids_football.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. four schoolchildren running after a football in a school playground, a school building behind them. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/library.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. an empty school library: tall bookshelves full of books, reading tables with chairs, a bright window. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/mark.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a cheerful schoolboy about eleven years old with curly dark hair, in a blue hoodie, head and shoulders, looking at the camera. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/mark_chess.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a schoolboy about eleven with curly dark hair in a blue hoodie sitting at a chess board, resting his chin on his hands. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/mark_science.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a schoolboy about eleven with curly dark hair in a blue hoodie and safety goggles pouring a blue liquid into a flask at a school science bench, coloured test tubes beside him. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/playground.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. an empty school playground: climbing frame with a red slide, swings, hopscotch squares painted on the tarmac, trees around. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/scene_canteen.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a schoolboy and a schoolgirl in school uniform sitting at a table in a busy school canteen with lunch trays of food in front of them, other pupils and the serving counter behind. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/staff_room.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. an empty school staff room: a large table with chairs, piles of exercise books and mugs on the table, a noticeboard on the wall. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u1/walk_to_school.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a schoolboy with a backpack walking along a path towards a school building on a sunny morning. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u2

**`media/gg2/u2/anya_pancakes.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a smiling girl about eleven years old in an apron holding a plate of pancakes with her two hands, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u2/cafe_waiter.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a waiter with a notepad taking an order from two teenage girls reading menus at a table on a cafe terrace. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u2/hot_dog_cart.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about eleven buying a hot dog from a man at a street hot dog cart with a red and yellow awning in a park. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u2/max.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about eleven in a blue hoodie taking a big bite out of a red apple, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u2/penny_breakfast.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a father and his young daughter having breakfast together at a sunny kitchen table with milk, toast and eggs. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u2/scene_breakfast.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a family of five — mother, father, two children and a grandmother — having a big breakfast together at a kitchen table laid with bread, fruit, juice and eggs. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u2/three_meals.webp`** — задание про breakfast / lunch / dinner — три блюда должны быть разными и стоять раздельно

```
clean photograph, sharp focus, natural colours, bright daylight. a wooden table from above with three separate placemats, each holding one meal: breakfast cereal with berries on the left, a sandwich with soup in the middle, chicken with vegetables on the right. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u2/tom_matt_list.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. two teenage boys sitting at a table, one writing a shopping list on a sheet of paper while the other watches. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u3

**`media/gg2/u3/angry.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten years old with red hair, frowning and clearly angry, arms crossed, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/book_boy_selfie.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about eleven holding a smartphone at arm’s length and taking a selfie, smiling, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/book_dad_phone.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a man about forty with a moustache talking on a mobile phone held to his ear, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/book_download_song.webp`** — на экране должна быть именно загрузка песни, без букв и слов

```
clean photograph, sharp focus, natural colours, bright daylight. a smartphone held in a hand, the screen showing a music download progress bar with a note icon. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/book_pets_site.webp`** — без читаемого текста на экране

```
clean photograph, sharp focus, natural colours, bright daylight. an open laptop standing on a desk, the screen showing a website about pets with photographs of a cat and a dog. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/book_text_hi.webp`** — без читаемого текста

```
clean photograph, sharp focus, natural colours, bright daylight. a hand holding a smartphone, the screen showing a messaging app with one short speech bubble. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/book_video_chat.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy wearing headphones sitting in front of an open laptop, the laptop screen showing another child waving during a video call. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/bored.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a teenage girl with long fair hair looking bored, chin resting on her hand, eyes half closed, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/bored_students.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a row of bored teenagers sitting in a lecture hall, resting their chins on their hands. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/chat_online.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about eleven in a blue hoodie sitting at a laptop and chatting online, smiling at the screen. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/download_song.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about eleven in pink headphones looking at her smartphone and downloading music, full upper body. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/happy.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about seven with brown pigtails laughing happily, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/harry.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about eleven in a green hoodie holding a tablet in both hands and smiling, upper body. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/jack.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten in a blue hoodie and a yellow cap sitting cross-legged on the floor with a smartphone and a laptop in front of him. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/lily.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about eleven in a purple jumper looking at her smartphone and smiling, upper body. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/phone_call.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy and a girl in two separate rooms, side by side in one frame, each talking on a mobile phone to the other. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/sad.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about eight looking sad, mouth turned down, a tear on his cheek, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/sarah.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about eleven in yellow pyjamas sitting on her bed in a bright bedroom, looking at her smartphone. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/scared.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about eight looking frightened, eyes wide, both hands covering his mouth, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/scene_gadgets_breakfast.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a family at a kitchen breakfast table where everyone is using a gadget: the father on a laptop, the mother on a tablet, one child on a phone, another child in headphones. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/scene_pool.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a sunny outdoor swimming pool with children swimming and playing with a beach ball, adults on sun loungers, palm trees around. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/selfie_teens.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. four teenagers standing close together in a park and taking a group selfie with a smartphone held at arm’s length. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/send_email.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about eleven in a purple jumper sitting at an open laptop and clicking send, upper body. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/surf_internet.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten in a green hoodie holding a tablet in both hands and scrolling a web page, upper body. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/take_selfie.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about eleven in a denim jacket holding a pink smartphone at arm’s length and taking a selfie. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/talk_phone.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten in a red hoodie talking on a mobile phone held to his ear, upper body. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/text_friend.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about eleven in a purple jumper typing a message on her smartphone with both thumbs, upper body. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/tired.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a teenage girl yawning with her hand over her mouth, eyes closed, looking very tired, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/video_call.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about eleven sitting at an open laptop and waving at the screen, where an elderly couple is waving back during a video call. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/worried.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten looking worried, eyebrows raised, biting his lip, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u3/worried_woman.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a woman about thirty-five looking worried, both hands at the sides of her head, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u4

**`media/gg2/u4/beach.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a tropical sandy beach with turquoise sea, gentle waves and palm trees, empty of people. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/bike_forest.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about twelve in a helmet riding a mountain bike along a forest trail between tall trees. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/boat_lake.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a family of four rowing a small wooden boat on a calm mountain lake. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/book_mountain_cartoon.webp`** — задание «This is the highest mountain in my country» — гора должна быть явно высокой и снежной

```
clean photograph, sharp focus, natural colours, bright daylight. a very high snow-capped mountain peak rising above green foothills under a blue sky. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/book_pizza.webp`** — заменяет картинку с водяным знаком freepik — на новой никаких подписей и логотипов

```
clean photograph, sharp focus, natural colours, bright daylight. one whole round pizza on a wooden board seen from directly above, cut into eight slices. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/boring.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a grey rainy day seen through a window, raindrops on the glass, a clock and a pile of books on the windowsill. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/cinema.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a cinema auditorium from the front: rows of red seats with an audience of children and adults watching the screen, tubs of popcorn in their hands. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/city.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a big modern city with tall glass skyscrapers, a river and a bridge in the foreground, blue sky. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/dan_laptop.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a teenage boy in headphones sitting at a desk in his room and working at a laptop, a desk lamp lit beside him. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/desert.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a sandy desert with high dunes, red rocks on the horizon and a clear blue sky, no people. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/exciting.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a big red rollercoaster with a loop at an amusement park against a blue sky. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/forest.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a green summer forest with tall trees and a narrow path going into the distance. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/high.webp`** — пара к low — башня должна читаться как «высокая»

```
clean photograph, sharp focus, natural colours, bright daylight. a very tall television tower rising high into a clear blue sky, seen from the ground. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/island.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a small tropical island with palm trees in the middle of a turquoise ocean, seen from above. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/kayak_river.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. two teenage boys in life jackets paddling one kayak down a fast mountain river. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/lake.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a calm blue mountain lake surrounded by pine forest and hills, reflections in the water. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/mountain.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a high snow-capped mountain peak above a green valley with pine trees under a blue sky. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/plato.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about twelve in a simple light tunic standing on a rocky Greek hillside above a village of white houses with blue domes and the sea behind. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/river.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a clear mountain river with stones in the water running through a green valley towards distant mountains. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/sea.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the open sea with blue waves and white foam under a sky with white clouds, no land in sight. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/three_paintings.webp`** — задание сравнивает три картины — они должны быть разными и все три видны целиком

```
clean photograph, sharp focus, natural colours, bright daylight. three framed paintings hanging in a row on a gallery wall: an abstract painting on the left, a portrait in the middle, a mountain landscape on the right. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/town.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a small old European town with red-roofed houses, a church tower and a stone bridge over a river, green hills behind. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/volcano.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. an active volcano with a plume of grey smoke rising from the crater, green slopes below. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/waterfall.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a tall waterfall falling from a rocky cliff into a turquoise pool, green forest around. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/jake_michael.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. two teenage boys sitting at a table in a fast food restaurant eating a burger and pizza with drinks in paper cups. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u4/zak_lenny.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. two teenage boys sitting at a table in a fast food restaurant, one eating a burger and the other a slice of pizza, both laughing. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u5

**`media/gg2/u5/bank.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the front of a classical city bank building with stone columns and a cash machine beside the entrance. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/big_house.webp`** — пара к small_house — дом должен читаться как «большой»

```
clean photograph, sharp focus, natural colours, bright daylight. a very large expensive house with many windows, a wide drive and a fountain in front of it. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/book_dog_1.webp`** — ключ «between»: собака ровно между деревом и будкой

```
clean photograph, sharp focus, natural colours, bright daylight. a brown dog sitting on green grass exactly between a tall tree on the left and a small wooden kennel on the right, all three clearly separated. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/book_dog_2.webp`** — ключ «opposite» (сейчас в блоке стоит «next to» — см. вопрос 1)

```
clean photograph, sharp focus, natural colours, bright daylight. a brown dog sitting on green grass a few steps away from a small wooden kennel and facing it directly, the dog and the kennel opposite each other across an empty gap. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/book_dog_3.webp`** — ключ «next to» (сейчас в блоке стоит «opposite» — см. вопрос 1)

```
clean photograph, sharp focus, natural colours, bright daylight. a brown dog lying on green grass right beside a small wooden kennel, its body touching the side wall of the kennel. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/book_dog_4.webp`** — ключ «in front of»

```
clean photograph, sharp focus, natural colours, bright daylight. a brown dog sitting on green grass directly in front of a small wooden kennel, partly covering the kennel door. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/book_dog_5.webp`** — ключ «behind»

```
clean photograph, sharp focus, natural colours, bright daylight. a small wooden kennel on green grass with a brown dog hidden behind it, only the dog’s tail and part of its back showing from behind the kennel. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/busy_street.webp`** — пара к quiet_street — здесь должно быть много машин и людей

```
clean photograph, sharp focus, natural colours, bright daylight. a busy city street at midday full of cars, buses and taxis in several lanes, crowds of people on the pavements. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/cafe.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the front of a small street cafe with a striped awning, tables and chairs outside and flowers in window boxes. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/cinema.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the front of a cinema at dusk with a lit marquee, a red carpet and posters beside the entrance. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/clean_cinema.webp`** — пара к dirty_cinema — ни мусора, ни попкорна на полу

```
clean photograph, sharp focus, natural colours, bright daylight. a clean empty cinema auditorium: tidy rows of red seats, spotless floor, bright screen. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/clothes_shop.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the front of a small clothes shop with a pink awning and two window displays showing dresses and shirts on mannequins. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/dirty_cinema.webp`** — пара к clean_cinema — мусор должен быть очевиден

```
clean photograph, sharp focus, natural colours, bright daylight. a messy cinema auditorium after a film: spilt popcorn, empty cups and litter all over the floor between the rows of red seats. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/film_studio.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a film studio set with a professional camera on a tripod, big studio lights, a director’s chair and a street facade in the background. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/garden.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a pretty garden with flower beds, a stone path, a green arch with roses and a lawn. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/hospital.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the front of a modern hospital building with a red cross sign and an ambulance parked at the entrance. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/hotel.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the front of a grand hotel with a revolving door, a canopy over the entrance and a luggage trolley beside it. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/interesting_museum.webp`** — карточка «interesting» — внутри музея, интересно и людно

```
clean photograph, sharp focus, natural colours, bright daylight. a bright museum hall with a huge dinosaur skeleton in the middle and glass display cases with exhibits around it. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/kitchen.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a bright home kitchen with green cupboards, a cooker, a wooden island with two stools and plants on the shelves. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/library.webp`** — в этом же юните есть внутренний вид школьной библиотеки — здесь нужен именно фасад здания

```
clean photograph, sharp focus, natural colours, bright daylight. the front of a classical public library building with stone columns and wide steps up to the door. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/museum.webp`** — сейчас сквозь фасад виден скелет динозавра — на новой картинке только здание снаружи

```
clean photograph, sharp focus, natural colours, bright daylight. the front of a classical museum building with tall stone columns and wide steps, a banner-free facade. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/new_stadium.webp`** — пара к old_stadium — всё новое и целое

```
clean photograph, sharp focus, natural colours, bright daylight. a brand new football stadium with a perfect green pitch, clean blue seats and a modern roof, empty. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/old_stadium.webp`** — пара к new_stadium — разруха должна быть очевидна

```
clean photograph, sharp focus, natural colours, bright daylight. an old abandoned football stadium with cracked concrete steps, broken and missing seats and weeds growing on the pitch. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/park.webp`** — пара к park_small — этот парк должен быть большим

```
clean photograph, sharp focus, natural colours, bright daylight. a large city park with old trees, a pond with a small bridge, benches and flower beds. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/park_small.webp`** — пара к park — этот должен быть маленьким

```
clean photograph, sharp focus, natural colours, bright daylight. a tiny city park: one tree, one bench and a small patch of grass between buildings. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/police_station.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the front of a police station with a blue lamp over the door and a police car parked outside. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/post_office.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the front of a post office with a red post box beside the door and a letter sign over the entrance. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/quiet_street.webp`** — пара к busy_street — ни машин, ни людей

```
clean photograph, sharp focus, natural colours, bright daylight. an empty quiet residential street lined with trees, no cars and no people. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/restaurant.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the front of a smart restaurant in the evening with laid tables visible through big windows and lanterns beside the door. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/scene_street.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a lively town street with shops, a cafe, a post office and a bus stop, people walking on the pavement and cars on the road. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/shopping_centre.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a big modern shopping centre with a glass facade, a fountain in front and people going in. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/small_house.webp`** — пара к big_house — дом должен читаться как «маленький»

```
clean photograph, sharp focus, natural colours, bright daylight. a small cottage with a red roof, one front door and two windows, a little garden in front. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/sports_centre.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a modern sports centre building with a running track and sports pitch beside it. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/stadium.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a large football stadium seen from outside with floodlights and the stands above the walls. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/supermarket.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the front of a supermarket with a green sign, big windows and a row of shopping trolleys beside the door. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/swimming_pool.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. an indoor swimming pool with lane ropes, a glass roof and starting blocks at the near end, no people. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/theatre.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the front of a theatre in the evening: a grand entrance with red doors, columns and lamps on either side. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/theme_park.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a theme park with a big wheel, a rollercoaster and a carousel under a blue sky. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/town_now.webp`** — пара к town_past — задание сравнивает «тогда и сейчас»

```
clean photograph, sharp focus, natural colours, bright daylight. a modern town street today: asphalt road with parked cars, street lamps, shops with glass windows and a church spire behind. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/town_past.webp`** — пара к town_now — ни одной машины в кадре

```
clean photograph, sharp focus, natural colours, bright daylight. the same town street a hundred years ago: cobbled road, horse-drawn carts, gas lamps, old shop fronts and the same church spire behind, no cars. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u5/train_station.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a railway station platform under a glass roof with a modern train standing at the platform and a bench beside it. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u6

**`media/gg2/u6/artist.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a woman artist in an apron with a beret, holding a palette and a brush and painting a landscape on an easel, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u6/builder.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a builder in a yellow hard hat and high-visibility vest laying bricks with a trowel, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u6/bus_driver.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a bus driver in uniform and cap sitting at the wheel of a blue bus, seen through the open door. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u6/chef.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a chef in a white jacket and tall chef’s hat stirring a big pot on a stove, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u6/doctor.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a woman doctor in a white coat with a stethoscope round her neck holding a clipboard, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u6/farmer.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a farmer in dungarees and a straw hat holding a basket of eggs, a red tractor behind him. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u6/footballer.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a footballer in a red kit kicking a football, full figure in mid-action. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u6/nurse.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a nurse in a white uniform holding a syringe and a plaster, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u6/office_worker.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. an office worker in a shirt and tie sitting at a desk with a computer monitor, keyboard and a pile of folders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u6/pilot.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. an airline pilot in uniform with a cap and epaulettes standing with arms folded, an aeroplane behind him. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u6/police_officer.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a woman police officer in uniform with a cap holding a radio, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u6/scene_cleaning.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a family cleaning the house together: the mother ironing, the father cleaning a window, one child carrying a basket of laundry and another picking up toys from the floor. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u6/shop_assistant.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a woman shop assistant in a green apron at a supermarket checkout scanning an apple, fruit and vegetables on the belt. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u6/singer.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a woman singer in a red dress singing into a microphone on a stage, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u6/teacher.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a man teacher with glasses standing at a green board with a piece of chalk, a globe and books on the desk beside him. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u6/vet.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a woman vet in a white coat examining a grey cat on an examination table with a stethoscope. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u7

**`media/gg2/u7/arrive.webp`** — пара к leave — здесь поезд именно приезжает, двери к перрону

```
clean photograph, sharp focus, natural colours, bright daylight. a family with a child standing on a railway platform as a train pulls in and stops beside them. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/dad_coffee.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a man about forty standing in a bright kitchen holding a mug of coffee and smiling. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/dad_photos.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a man crouching on a rocky seashore and photographing two children who are posing for him, blue sea behind. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/enzo.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a teenage boy in a red hoodie with a backpack sitting on a seat inside an underground train carriage, other passengers behind him. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/get_off.webp`** — пара к get_on — здесь выходят ИЗ транспорта

```
clean photograph, sharp focus, natural colours, bright daylight. a family with two children stepping down out of a train onto the platform, their backs to the open doors. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/get_on.webp`** — пара к get_off — здесь заходят В транспорт

```
clean photograph, sharp focus, natural colours, bright daylight. a family with two children queuing at the open door of a red bus and climbing up into it. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/hotel.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a family with suitcases standing at a hotel reception desk while a receptionist checks them in. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/kids_off_bus.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. three schoolchildren with backpacks jumping down from the open door of a yellow school bus. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/leave.webp`** — пара к arrive — здесь поезд уезжает

```
clean photograph, sharp focus, natural colours, bright daylight. a woman on a railway platform waving goodbye to a train that is pulling away from her at sunset. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/mum_stan_shop.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a mother and her young son in a supermarket aisle pushing a trolley full of fruit and vegetables. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/museum.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. four schoolchildren with backpacks looking up at a marble statue in a museum hall, paintings in gold frames on the wall behind. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/penny_skateboard.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about eleven in a helmet and knee pads riding a skateboard in a skate park, palm trees behind. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/restaurant.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a family of four sitting round a restaurant table sharing a pizza, with drinks in glasses. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/scene_airport.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a family with a suitcase standing at the big window of an airport terminal looking out at an aeroplane on the apron. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/scene_suitcase.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. an open suitcase on a bed being packed for a holiday: sun hat, sunglasses, towel, camera, passport and folded clothes laid out around it. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/souvenir.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten choosing a souvenir from a street stall full of small figurines and postcards, the stallholder behind the counter. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/take_bus.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten with a backpack getting on a red bus at a bus stop, the driver visible in the cab. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/take_photos.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about twelve in a sun hat and denim jacket taking a photograph with a big camera held up to her eye, upper body. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/tim_pizza.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about eleven sitting at a table in a pizzeria eating a slice of pizza, a drink beside him. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/tina_hat.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about eleven in a summer dress wearing a straw sun hat decorated with flowers, upper body. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u7/underground.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. an underground station platform with a train standing at the platform, tiled walls and a curved tunnel ceiling. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u8

**`media/gg2/u8/armful_clothes.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a teenage girl carrying a big armful of folded clothes, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/barbecue.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a round charcoal barbecue with sausages cooking on the grill in a sunny green garden. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/beach_holiday.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a sun lounger with a towel and a straw hat under a palm tree on a white sandy beach with turquoise sea behind. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/birthday_party.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a birthday table indoors with a chocolate cake with lit candles, wrapped presents, paper cups and coloured balloons above. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/boy_reading.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten lying on his bed reading a book, a bedside lamp lit beside him. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/cinema_tonight.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. an empty cinema auditorium with red seats and a bucket of popcorn on one seat, the screen lit. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/competition.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. four children racing along the lanes of a running track at a sports competition, flags and spectators behind. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/concert.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a concert stage with a microphone on a stand, loudspeakers and coloured stage lights, no people. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/cook_food.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten in an apron cooking vegetables in a frying pan on a kitchen hob. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/dance_show.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. four young dancers in bright costumes performing on a theatre stage under spotlights, a dark auditorium in front. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/fancy_dress.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a group of children at a fancy dress party in different costumes — pirate, princess, superhero, wizard — with balloons behind them. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/football_match.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a football stadium pitch with a ball in front of the goal, full stands behind. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/get_presents.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl opening a wrapped birthday present while her friends watch, balloons and more presents around. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/grandma_cottage.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a small country cottage with a tiled roof covered with climbing flowers, a bench in the garden and blossom trees around. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/homework_girl.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about eleven in headphones sitting at a desk and writing in an exercise book under a desk lamp, a pile of books beside her. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/paint_bedroom.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a bedroom being decorated: one wall half painted pink, a paint roller on a tray and a stepladder standing in the room. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/picnic.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a picnic blanket on green grass with a wicker basket, sandwiches, fruit and a flask laid out on it. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/play.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. an empty theatre stage with red curtains open, a painted castle backdrop and stage lights above. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/sakura.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. pink cherry blossom branches in full bloom beside a lake with a snow-capped mountain in the distance. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/scene_birthday.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a children’s birthday party indoors: a group of children round a table with a cake with lit candles, presents, balloons and party hats. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/shop_window.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a clothes shop window display with dresses and jackets on mannequins and folded clothes on a shelf. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/sing_birthday.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a group of children standing round a birthday cake with lit candles, singing and clapping. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/sleep_floor.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. two children asleep in sleeping bags on the bedroom floor at a sleepover, a lantern beside them. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/sleepover.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a bedroom floor laid out for a sleepover: three sleeping bags side by side, cushions, fairy lights and a torch. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/sleepover_girls.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. three girls in pyjamas sitting together on the floor at a sleepover sharing a bowl of popcorn and laughing. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/talent_competition.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl singing into a microphone on a stage lit by a star-shaped light, three judges at a table in front of the stage. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg2/u8/wear_costume.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about nine dressed in a superhero costume with a red cape and mask, standing with hands on hips, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```
