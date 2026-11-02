# Картинки в тестах — что перерисовываем

Проход 02.11.2026 по тестам (`classroom_lessons.kind = 'test'`) шести курсов:
**SM0, SM1, SM3, GG1, GG2, GG3**. Super Minds 2 ведёт другой чат, его здесь нет.

Смотрели все блоки, кроме `text`, `video` и `embed`: 282 блока, 793 ссылки на
картинки, **656 уникальных файлов**. Контактные листы и увеличения —
`/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/testy_check/`.

**Битых ссылок нет ни одной** — все 656 файлов лежат в `media/`.

## Сводка по курсам

| курс | тестов | картинок в заданиях | мельче 300 px | медиана | под перерисовку | листов-промптов |
|---|---|---|---|---|---|---|
| Super Minds 0 | 6 | 45 | 0 | 590 px | 1 | 1 |
| Super Minds 1 | 11 | 186 | 0 | 510 px | 9 | 2 |
| Super Minds 3 | 11 | 100 | 0 | 400 px | 5 | 4 |
| Go Getter 1 | 10 | 160 (4 svg) | 9 | 400 px | 86 | 23 |
| Go Getter 2 | 10 | 56 | 1 | 400 px | 2 | 1 |
| Go Getter 3 | 10 | 109 | 0 | 400 px | 0 | 0 |
| **итого** | **58** | **656** | **10** | — | **103** | **31** |

Коротко по каждому курсу:

* **SM0** — после октябрьской перерисовки курс в порядке: медиана 590 px, стиль
  один, счётные картинки (5/8/10 звёзд, 2 глаза и 2 ноги у монстрика) сходятся
  с ключами. Одна правка — `new/arms.webp` (см. «спорит с ключом»).
* **SM1** — картинки перерисованы 24.10, стиль ровный, мельче 300 px нет ни
  одной. Но здесь **самый тяжёлый куст расхождений с ключами** — блок «can / can't»
  в тесте юнита 8 и четыре отдельных места. Перерисовка нужна только под них.
* **SM3** — предметные картинки свои и однородные, ключи предлогов, времени
  и свечей на торте сходятся. Выбиваются пять картинок: четыре плоских
  клипарт-сцены из учебника и одно фото тумана.
* **GG1** — **курс, ради которого всё затевалось.** Половина картинок в тестах —
  стоковые фотографии (одежда, спорт, мебель), другая половина — 3D-рендер,
  и они стоят рядом в одном блоке. Плюс девять картинок мельче 300 px, четыре
  с чужим фоном (чёрный, «шашечка» прозрачности, рамка) и две чёрно-белые
  страницы-раскраски.
* **GG2** — самый ровный курс: 3D-рендер предметов и Pixar-сцены, почти без
  разнобоя. Две картинки на правку.
* **GG3** — **перерисовывать нечего.** Один стиль от юнита 0 до финального
  теста, минимум 331 px, ключи сходятся. Пары, которые выглядели опасно
  (`load_dishwasher` / `empty_dishwasher`, `plug_in` / `turn_on` / `turn_off`),
  разведены подсказкой в самом задании («4. empty th_ d_shw_sh_r»), так что
  путаницы не будет.

---

## 🟥 Картинка спорит с ключом

Самое важное. Каждое место проверено глазами на увеличении и сверено с payload.

### SM1 · Unit 8 Test · блок 3 — «✓ умеет, ✗ не умеет», шесть вопросов

Заголовок блока: «Посмотри на картинку и выбери подходящее предложение.
**✓ — умеет, ✗ — не умеет**». **Ни на одной из шести картинок нет ни ✓, ни ✗** —
ребёнку не по чему выбрать отрицание. Сверх того четыре картинки спорят с
ключом по существу:

| картинка | ключ | что на картинке | расхождение |
|---|---|---|---|
| `sm1/u8/t_he_piano.webp` | He **can't** play the piano. | **девочка** играет на пианино | пол + она умеет |
| `sm1/u8/t_he_tennis.webp` | He **can't** play tennis. | **девочка** играет в теннис | пол + она умеет |
| `sm1/u8/t_he_swim.webp` | He can swim. | мальчик плывёт | только нет ✓ |
| `sm1/u8/t_she_dance.webp` | She can dance. | девочка танцует | только нет ✓ |
| `sm1/u8/t_she_pony.webp` | She **can't** ride a pony. | девочка **едет** на пони | ключ противоречит картинке |
| `sm1/u8/t_she_bike.webp` | She can ride a bike. | на велосипеде **мальчик** | пол |

Блок в нынешнем виде нерешаем: три вопроса из шести ребёнок не возьмёт никак.
Промпт 24 рисует все шесть заново — с правильным полом и с большой зелёной
галочкой или красным крестом в углу.

### SM1 · Unit 8 Test · блоки 1 и 2 — `hand` и `fingers` одна и та же картинка

`sm1/u8/body_hand.webp` и `sm1/u8/body_fingers.webp` — **две почти одинаковые
раскрытые ладони**. В блоке 1 (диктант) по первой надо написать `fingers`,
по второй `hand`; в блоке 2 (match) та же пара идёт в разные строки. Различить
их нельзя. Нужна картинка именно пальцев — крупный план кисти, где пальцы
занимают почти весь кадр (промпт 25).

Пара `body_foot` (ступня сбоку) / `body_toes` (ступня сверху, пальцы видны)
различима, её не трогаем.

### SM1 · Unit 4 Test · блок 7 — «у меня нет гороха», а горох на картинке

`sm1/legacy/70d72135a807.webp` — стоковое фото **горы зелёного горошка**,
предложение, которое ребёнок собирает: **«I haven't got any peas.»** Картинка
говорит ровно обратное. Это ещё и единственный файл из `legacy/` во всех тестах
SM1 — фотография среди 3D-рендера. Промпт 25 рисует пустую тарелку с
перечёркнутым горохом.

### SM1 · Unit 1 Test · блок 9 — «жёлтая парта» деревянного цвета

`sm1/u1/t_yellow_desk.webp` — предложение **«It is a yellow desk.»**, а парта на
картинке **светло-коричневая, деревянная**, ровно такая же, как `t_wooden_desk`
в блоке 12 того же теста. Нужна явно жёлтая парта (промпт 25).

### SM0 · Final Test · блок 8 — `arms` нарисованы ладонями

`sm0/new/arms.webp` — **две раскрытые ладони**, подписано `arms`. В самом блоке
это дистрактор (верный ответ — `legs`), так что вопрос решается, но если эту же
картинку когда-нибудь поставят как правильный ответ на «arms», ребёнок ответит
`hands`. Нужны две руки целиком, от плеча до кисти (промпт 31).

### SM3 · Final Test · блок 10 — «мальчика в шарфе» на картинке нет

`sm3/ft/scene_house.webp`, утверждение **«The boy with the scarf has curly hair.»**,
ключ — **верно**. На картинке два мальчика: на скейтборде (рыжий, кудрявый, без
шарфа) и в саду (оранжевая футболка). **Шарфа нет ни на ком.** Ребёнок не поймёт,
о ком речь. Либо переписать утверждение под картинку, либо перерисовать сцену
с мальчиком в шарфе — промпт 28 рисует заново со всеми шестью деталями.

Там же мягкое место: «There are some birds on top of the house» — ключ «неверно»,
а птицы в небе есть, просто не на доме. На перерисовке птиц уводим подальше.

### GG1 · Unit 2 Test · блоки 3–7 — «далеко или близко» не читается

Пять картинок (`far_hoodie`, `near_trainers`, `near_tracksuit`, `far_cap`,
`far_boots`) различают *this/that* и *these/those* **только длиной красной
стрелки**: длинная — далеко, короткая — близко. На глаз это не работает —
у `far_hoodie` и `near_trainers` стрелки почти одинаковые. Хуже того, объяснение
стрелки стоит **только в заголовке блока 3**, а в блоках 4–7 его нет вовсе.
Ключи: b3 — `That`, b5 — `This`, b6 — `That`, b7 — `those`; угадать их по
картинке нельзя.

Отдельно `far_boots.webp`: на ней **семь пар разной обуви** (кроссовки, туфли,
ботинки, сандалии), вопрос — «Are those your friends' **boots**?». Стрелка
указывает на одну пару, остальные шесть мешают.

Промпт 7 рисует пять нормальных сцен: девочка рядом с вещью (близко) или
показывает на вещь вдали (далеко), одна вещь в кадре.

### GG1 · Final Test · блок 3 — в комнате нет ни одного предмета из задания

`gg1/final/final_living_room.webp` — аудирование «Послушай аудио выше и расставь
предметы по местам», шесть меток: **radio, ball, kite, clock, robot, bag**.
В комнате на картинке **нет ни радио, ни мяча, ни воздушного змея, ни часов,
ни робота, ни сумки** — только кресла, стол, комод и книжный шкаф. Аудио
оригинальное (`gg1/audio/gg1_ft_test_b2.mp3`), так что задание задумано как
«послушай и положи», но ребёнку не с чем сверить ответ и проверить себя.
Промпт 22 рисует ту же комнату со всеми шестью предметами на своих местах
(координаты меток — радио на книжном шкафу, часы на комоде, робот на столике,
мяч и змей на ковре, сумка на жёлтом кресле).

### GG1 · Final Test · блок 10 — пример в заголовке про «два кресла»

В заголовке пример: «There are two armchairs in the living room — YES».
На `final_family_room.webp` одно красное кресло и один жёлтый диван-кресло;
второй предмет спорный. Само задание сходится полностью (блондин — NO, лампа
на шкафу — YES, дети в кухне — NO, женщина позади — YES, кот под креслом — YES),
но пример лучше поменять на бесспорный.

### Проверено и сошлось (расхождений нет)

* SM1 U3 b10 — читательская сцена «где животные»: лягушка на коробке, паук под
  стулом, ящерица в сумке, собака на диване, крыса под столом — всё точно так.
* SM1 U6 b2 и b4 — счёт: 4 груши (plural), 1 самолёт, 3 велосипеда, 4 собаки.
* SM1 U6 b6 — «There aren't any go-karts in the park»: парк действительно пустой.
* SM3 U4 b2–b7 — все шесть предлогов (near, above, between, opposite, below)
  и «going to the sports centre to go swimming» совпадают с картинками.
* SM3 U3 b2 — восемь часов на картинке: 7:15 собака, 6:00 уроки, 10:30 кровать,
  8:30 уборка, 11:00 двор — все пять нужных совпали.
* SM3 Final b7 — свечи на тортах: 7, 9 и 10, пересчитано по пламени.
* SM3 Final b4 — шесть точек на сцене библиотеки попадают в нужных людей.
* SM0 Final b8 и b13 — eyes / legs / mouth, «How many eyes? — 2», «I've got 5
  legs — No» (у монстрика две ноги).
* GG1 U6 b6, b7, b10 — часы в svg: 2:15, 8:00, 7:30, посчитано по углам стрелок.
* GG1 U4 b11 — описание Тома, Люси и Рекса совпадает с картинкой.
* GG1 U3 b2 — шар на кубе и шар перед кубом стоят правильно (но сам куб
  перерисовываем, см. ниже).
* GG3 — ключи всех десяти тестов сходятся с картинками.

Мягкое место, решать методисту: **SM1 U2 b6 вопрос 3** — «How old is she?
She's seven», на торте шесть пламён и седьмая свеча спрятана за соседней. Ответ
грамматический («How **old**»), так что задание решается, но посчитать семь
нельзя. Если менять — в том же листе, что и остальные правки SM1.

---

## Таблица: что не так с картинками

### Go Getter 1 — 86 файлов

| файл | юнит · блок | что не так |
|---|---|---|
| `gg1/u0/obj_book.webp` | U0 b2 | стоковое фото |
| `gg1/u0/obj_pen.webp` | U0 b2 | стоковое фото |
| `gg1/u0/obj_bag.webp` | U0 b2 | стоковое фото |
| `gg1/u0/obj_chair.webp` | U0 b2 | стоковое фото |
| `gg1/u0/colour_red.svg` | U0 b2 | плоский svg-вектор рядом с фотографиями |
| `gg1/u0/col_red_pen.webp` | U0 b10 | стоковое фото |
| `gg1/u0/col_blue_bag.webp` | U0 b10 | стоковое фото |
| `gg1/u0/col_yellow_ruler.webp` | U0 b10 | стоковое фото |
| `gg1/u0/col_green_notebook.webp` | U0 b10 | стоковое фото |
| `gg1/u0/col_pink_pencil_case.webp` | U0 b10 | стоковое фото |
| `gg1/u0/obj_clock.webp` | Final b9 | стоковое фото |
| `gg1/u0/obj_ruler.webp` | Final b16 | стоковое фото |
| `gg1/u0/test_classroom.webp` | U0 b12 | 900×366, узкая полоска; плоский стиль |
| `gg1/u2/clothes_tshirt.webp` | U2 b2 | каталожное фото |
| `gg1/u2/clothes_skirt.webp` | U2 b2 | каталожное фото |
| `gg1/u2/clothes_dress.webp` | U2 b2 | каталожное фото |
| `gg1/u2/clothes_jeans.webp` | U2 b2 | каталожное фото |
| `gg1/u2/clothes_coat.webp` | U2 b2 | каталожное фото |
| `gg1/u2/clothes_jumper.webp` | U2 b3 | каталожное фото |
| `gg1/u2/clothes_shoes.webp` | U2 b4 | каталожное фото |
| `gg1/u2/clothes_top.webp` | U2 b5 | каталожное фото |
| `gg1/u2/clothes_shirt.webp` | U2 b6 | каталожное фото |
| `gg1/u2/clothes_trousers.webp` | U2 b7 | каталожное фото |
| `gg1/u2/clothes_jacket.webp` | Final b12 | каталожное фото |
| `gg1/u2/far_hoodie.webp` | U2 b3 | 🟥 коллаж со стрелкой, «далеко» не читается |
| `gg1/u2/near_trainers.webp` | U2 b4 | 🟥 четыре пары кроссовок + стрелка |
| `gg1/u2/near_tracksuit.webp` | U2 b5 | 🟥 стрелка + серая полоса-артефакт внизу |
| `gg1/u2/far_cap.webp` | U2 b6 | 🟥 стрелка, фото кепки |
| `gg1/u2/far_boots.webp` | U2 b7 | 🟥 семь пар обуви, из них ботинок две |
| `gg1/u2/pencils_heart.webp` | U2 b8 | стоковое фото |
| `gg1/u2/boot_black.webp` | U2 b10 | фото, чёрная рамка по краю, 377×388 |
| `gg1/u2/cinema.webp` | U2 b11 | фотоклипарт с рамкой, 435×303 |
| `gg1/u2/kevin_birthday.webp` | U2 b17 | чёрно-белая страница-раскраска |
| `gg1/u3/prep_on.webp` | U3 b2 | 240×240, стеклянный куб вместо коробки |
| `gg1/u3/prep_in_front_of.webp` | U3 b2 | 240×240, то же |
| `gg1/u3/furn_wardrobe.webp` | U3 b2 | стоковое фото |
| `gg1/u3/furn_bath.webp` | U3 b2 | стоковое фото |
| `gg1/u3/part_window.webp` | U3 b2 | стоковое фото |
| `gg1/u3/photo_lamp.webp` | U3 b3 | стоковое фото |
| `gg1/u3/furn_carpet.webp` | U3 b3 | стоковое фото |
| `gg1/u3/photo_garden.webp` | U3 b3 | стоковое фото |
| `gg1/u3/photo_bedroom_2.webp` | U3 b3 | стоковое фото |
| `gg1/u3/photo_armchair.webp` | U3 b3 | фото на **чёрном фоне** |
| `gg1/u3/raccoon_squirrel.webp` | U3 b4 | фото енота + клипарт белки в одной картинке, 266×242 |
| `gg1/u3/clowns.webp` | U3 b4 | клипарт, 235×282 |
| `gg1/u3/unicorn.webp` | U3 b4 | плоский рисунок на голубом фоне, 250×222 |
| `gg1/u3/pink_elephant.webp` | U3 b4 | плоский рисунок, 226×240 |
| `gg1/u3/ice_cream_sandwich.webp` | U3 b4 | каваи-стикер, 229×213 |
| `gg1/u3/jellyfish.webp` | U3 b5 | фотография на **чёрном фоне** |
| `gg1/u3/dragon.webp` | U3 b6 | клипарт, прозрачность видна «шашечкой» |
| `gg1/u3/alien.webp` | U3 b7 | клипарт |
| `gg1/u3/cat_sofa.webp` | U3 b8 | фотография кота |
| `gg1/u3/blue_monster.webp` | U3 b9 | дудл фломастером, 232×217 |
| `gg1/u3/kids_room_test.webp` | U3 b14 | плоский вектор, 900×614 |
| `gg1/u4/body_ears.webp` | U4 b2 | фотография (рядом 3D-глаза в том же блоке) |
| `gg1/u4/body_nose.webp` | U4 b2 | фотография |
| `gg1/u4/homework_diary.webp` | U4 b4 | фото тетради с белой рамкой |
| `gg1/u4/rabbit.webp` | U4 b4 | фотография кролика |
| `gg1/u4/english_class.webp` | U4 b5 | живописный стиль, чужой курсу |
| `gg1/u4/bike_yellow.webp` | U4 b6 | фото на **чёрном фоне**, 510×300 |
| `gg1/u4/teacher_board.webp` | U4 b7 | плоский клипарт |
| `gg1/u4/boy_cap.webp` | U4 b9 | плоский клипарт |
| `gg1/u4/sisters_blond.webp` | U4 b10 | плоский клипарт |
| `gg1/u4/monsters_six.webp` | U4 b14 | плоский клипарт, 900×648 |
| `gg1/u5/obj_mixing_bowl.webp` | U5 b4 | фотография |
| `gg1/u5/obj_french_flag.webp` | U5 b7 | 211×293 |
| `gg1/u6/boy_wakes_up.webp` | U6 b3 | кустарный серо-голубой рисунок |
| `gg1/u6/obj_gym.webp` | U6 b8 | фотография |
| `gg1/u6/obj_family_dinner.webp` | U6 b9 | фотография |
| `gg1/u6/pocket_watch.webp` | U6 b12 | **чёрно-белая** фотография, 599×396 |
| `gg1/u6/eric_day_comic.webp` | U6 b17 | чёрно-белая раскраска, 748×698 |
| `gg1/u7/school_walk.webp` | U7 b3 | плоский вектор, надпись «PS 123», 449×424 |
| `gg1/u7/piano.webp` | U7 b6 | фотография рояля |
| `gg1/u8/sport_basketball.webp` | U8 b2 | фотография |
| `gg1/u8/sport_cycling.webp` | U8 b2 | фотография |
| `gg1/u8/sport_hockey.webp` | U8 b2 | фотография |
| `gg1/u8/sport_taekwondo.webp` | U8 b2 | фотография |
| `gg1/u8/sport_volleyball.webp` | U8 b2 | фотография |
| `gg1/u8/sport_football.webp` | U8 b3 | фотография |
| `gg1/u8/sport_tennis.webp` | U8 b10 | фотография |
| `gg1/u8/weather_sunny.webp` | U8 b11 | фотография неба |
| `gg1/u8/life_brush_teeth.webp` | U8 b12 | фотография |
| `gg1/final/final_car.webp` | Final b9 | фотография |
| `gg1/final/final_boot.webp` | Final b9 | фотография |
| `gg1/final/final_living_room.webp` | Final b3 | 🟥 в комнате нет шести предметов задания |

Не трогаем в GG1: `u1/fam_*` и `u1/t1_*` (3D, свои), `u3/room_living_room`,
`u5/verb_*`, `u6/da_*`, `u7/animal_*`, `u6/clock_*.svg`, `u4/granny_curly`,
`u4/body_eyes`, `u4/body_teeth`, `u4/hair_*`, `u4/pers_*`, `u4/tom_lucy_rex`,
`u8/t8_likes`, `final/final_chairs`, `final/final_radio`, `final/final_family_room`.

### Super Minds 3 — 5 файлов

| файл | юнит · блок | что не так |
|---|---|---|
| `sm3/u4/scene_town_busy.webp` | U4 b13 | плотная клипарт-сцена с мелкими вывесками, 900×504, чужой стиль |
| `sm3/u9/weather_foggy.webp` | U9 b1 | **фотография** тумана среди 3D-иконок погоды в том же блоке, 400×397 |
| `sm3/u9/scene_holiday_plans.webp` | U9 b13 | фото-раскладка предметов, 880×587 |
| `sm3/ft/scene_library.webp` | Final b4 | плоский клипарт из учебника, 602×679 на восемь человек |
| `sm3/ft/scene_house.webp` | Final b10 | 🟥 плоский клипарт, 668×664, нет мальчика в шарфе |

Остальное в SM3 оставляем, включая фотореалистичные `ft/opt_*` — внутри своего
блока они однородны.

### Super Minds 1 — 9 файлов

| файл | юнит · блок | что не так |
|---|---|---|
| `sm1/u8/t_he_piano.webp` | U8 b3 | 🟥 девочка вместо мальчика, нет ✗ |
| `sm1/u8/t_he_tennis.webp` | U8 b3 | 🟥 девочка вместо мальчика, нет ✗ |
| `sm1/u8/t_he_swim.webp` | U8 b3 | 🟥 нет ✓ |
| `sm1/u8/t_she_dance.webp` | U8 b3 | 🟥 нет ✓ |
| `sm1/u8/t_she_pony.webp` | U8 b3 | 🟥 ключ «не умеет», а она едет; нет ✗ |
| `sm1/u8/t_she_bike.webp` | U8 b3 | 🟥 мальчик вместо девочки, нет ✓ |
| `sm1/u8/body_fingers.webp` | U8 b1, b2 | 🟥 не отличается от `body_hand` |
| `sm1/legacy/70d72135a807.webp` | U4 b7 | 🟥 горох на картинке при «I haven't got any peas»; единственное фото среди рендера |
| `sm1/u1/t_yellow_desk.webp` | U1 b9 | 🟥 парта не жёлтая |

### Super Minds 0 — 1 файл

| файл | юнит · блок | что не так |
|---|---|---|
| `sm0/new/arms.webp` | Final b8 | 🟥 нарисованы ладони, подписано `arms` |

### Go Getter 2 — 2 файла

| файл | юнит · блок | что не так |
|---|---|---|
| `gg2/u1/calculator.webp` | U1 b2 | 255×299 — единственная мельче 300 px |
| `gg2/u7/underground.webp` | U7 b2 | фотография метро среди 3D-транспорта в том же блоке, 400×371 |

### Go Getter 3 — ничего

Ни одной картинки под перерисовку.

---

## Промпты

Готовы к копированию: каждый — один цельный блок, строка стиля уже внутри.
Нарезаем листы сами, имена файлов оставляем прежними — блоки править не нужно.
Хранить с запасом: предмет 600–800 px по большей стороне, сцена 1200–1600,
webp 88–90.

### Промпты 1–10 (Go Getter 1, юниты 0–3)

**1. GG1 U0 — школьные предметы, лист 1** → `obj_book`, `obj_pen`, `obj_bag`, `obj_chair`, `obj_clock`, `obj_ruler`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of six separate school objects arranged in a 3 by 2 grid on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, each object shown whole at a slight three-quarter angle, no shadow on the background, no text, no letters, no labels, no numbers. Row 1, left to right: a closed blue hardback book; a blue ballpoint pen with its cap on; a blue school backpack with two front pockets. Row 2, left to right: a wooden school chair with metal legs; a round white wall clock with black hands; a yellow wooden ruler with plain unmarked ticks.
```

**2. GG1 U0 — цветные школьные вещи, лист 2** → `col_red_pen`, `col_blue_bag`, `col_yellow_ruler`, `col_green_notebook`, `col_pink_pencil_case`, `colour_red`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of six separate objects arranged in a 3 by 2 grid on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, each object shown whole at a slight three-quarter angle, no shadow on the background, no text, no letters, no labels, no numbers. The colour of each object matters and must be unmistakable. Row 1, left to right: a bright red ballpoint pen; a bright blue school backpack; a bright yellow wooden ruler. Row 2, left to right: a bright green spiral notebook, closed; a bright pink soft zipped pencil case, closed; a single glossy bright red rounded paint blob shaped like a soft splash, nothing else in that cell.
```

**3. GG1 U0 — классная комната** → `test_classroom` (широкая сцена, одна генерация)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One wide classroom scene seen from the back of the room: four wooden desks with chairs in two rows, a green chalkboard on the far wall, a teacher's desk with a globe on it, a window with green trees outside, a bookshelf with colourful books, school bags on the floor beside the desks, and a wall map. The room is empty of people. Generous empty margin all around so nothing is cut off at the edge, plain flat pure white background outside the room walls, no text, no letters, no labels, no numbers, nothing written on the chalkboard or the map.
```

**4. GG1 U2 — одежда, лист 1** → `clothes_tshirt`, `clothes_skirt`, `clothes_dress`, `clothes_jeans`, `clothes_coat`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of five separate pieces of children's clothing arranged in one row on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, each garment shown flat and whole from the front as if laid out, no hangers, no mannequins, no shadow on the background, no text, no letters, no labels, no numbers, no brand marks, no patterns or prints on the fabric. Row 1, left to right: a light blue short-sleeved T-shirt; a dark blue pleated school skirt; a yellow sleeveless summer dress; blue denim jeans; a brown winter coat with buttons and a hood.
```

**5. GG1 U2 — одежда, лист 2** → `clothes_jumper`, `clothes_shoes`, `clothes_top`, `clothes_shirt`, `clothes_trousers`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of five separate pieces of children's clothing arranged in one row on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, each garment shown flat and whole from the front as if laid out, no hangers, no mannequins, no shadow on the background, no text, no letters, no labels, no numbers, no brand marks. Row 1, left to right: a mustard yellow knitted jumper with long sleeves; a pair of black school shoes with velcro straps, side by side; a light blue sleeveless vest top; a pale blue long-sleeved buttoned shirt with a collar; a pair of grey school trousers.
```

**6. GG1 U2 — одежда, лист 3** → `clothes_jacket` плюс пять вещей про запас
(кофта, кепка, кроссовки, спортивный костюм, ботинки — те же, что внутри сцен
промпта 7; пригодятся, если Анна решит оставить формат «предмет + стрелка»)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of six separate pieces of children's clothing arranged in a 3 by 2 grid on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, each garment shown flat and whole from the front, no hangers, no mannequins, no shadow on the background, no text, no letters, no labels, no numbers, no brand marks, no printed patterns. Row 1, left to right: a dark green zipped bomber jacket; a blue baseball cap seen from the side; a grey hooded sweatshirt with a front pocket. Row 2, left to right: a red tracksuit, jacket and matching trousers laid side by side as one set; a pair of white and blue sports trainers, side by side; a pair of brown lace-up ankle boots, side by side.
```

**7. GG1 U2 — «это рядом / то вдали», пять сцен** → `near_trainers`, `near_tracksuit`, `far_hoodie`, `far_cap`, `far_boots`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of five separate small scenes arranged in a 3 by 2 grid, the sixth cell left completely empty and white, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no shadow on the background, no text, no letters, no labels, no numbers, no arrows, no speech bubbles. In every scene exactly one piece of clothing appears and nothing else. Row 1, left to right: a smiling girl standing right beside a pair of white sports trainers on the floor at her feet, pointing straight down at them, the trainers large and close; a smiling boy standing right beside a red tracksuit laid on a chair at his side, his hand touching it, the tracksuit large and close; a girl in the foreground turned away from the viewer pointing far across an empty room at a small grey hooded sweatshirt hanging on a hook on the distant wall, the sweatshirt clearly small and far away. Row 2, left to right: a boy in the foreground turned away from the viewer pointing far across an empty room at a small blue baseball cap lying on a distant shelf, the cap clearly small and far away; a girl in the foreground turned away from the viewer pointing far across an empty room at one small pair of brown ankle boots standing by a distant door, only that one pair of boots in the scene and clearly small and far away.
```

**8. GG1 U2 — предметы из «собери предложение»** → `pencils_heart`, `boot_black`, `cinema`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of three separate objects arranged in one row on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no frames or borders around the objects, no shadow on the background, no text, no letters, no labels, no numbers. Row 1, left to right: a bunch of sharpened colouring pencils of many colours fanned out in the shape of a heart; one single black ankle boot with laces, seen from the side; a cinema building front at night with a lit yellow marquee of round bulbs, a red carpet and two closed glass doors, the marquee board completely blank.
```

**9. GG1 U2 — день рождения Кевина, сцена** → `kevin_birthday`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One wide birthday party scene in full colour: eight children around a table with a big birthday cake with lit candles, paper cups and plates of food, colourful balloons and paper chains on the wall, a pile of wrapped presents on the floor, one boy blowing out the candles and the others clapping, children of different hair colours and skin tones. Generous empty margin all around so nobody is cut off at the edge, plain flat pure white background behind the room, no text, no letters, no labels, no numbers, no writing on the cake or the banner.
```

**10. GG1 U3 — мебель и части дома, лист** → `furn_wardrobe`, `furn_bath`, `part_window`, `furn_carpet`, `photo_lamp`, `photo_armchair`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of six separate pieces of furniture arranged in a 3 by 2 grid on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, each object shown whole at a slight three-quarter angle, no shadow on the background, no dark background anywhere, no text, no letters, no labels, no numbers. Row 1, left to right: a tall wooden wardrobe with two closed doors; a white bathtub with silver taps; a white window with two panes, curtains tied back at the sides and green trees visible outside. Row 2, left to right: a rectangular patterned rug lying flat; a red desk lamp with a flexible neck on a round base; a green soft armchair with a cushion.
```

### Промпты 11–20 (Go Getter 1, юниты 3–8)

**11. GG1 U3 — мяч и коробка, два предлога** → `prep_on`, `prep_in_front_of`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of two separate small scenes side by side in one row on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no shadow on the background, no text, no letters, no labels, no numbers, no arrows. In both scenes the same two objects appear and nothing else: one closed brown cardboard box standing on the floor, and one orange ball. The position of the ball is the whole point and must be unmistakable. Row 1, left to right: the orange ball resting on top of the closed cardboard box, touching its lid; the orange ball standing on the floor clearly in front of the cardboard box, between the box and the viewer, with the box fully visible behind it.
```

**12. GG1 U3 — смешные существа, лист 1** → `unicorn`, `pink_elephant`, `ice_cream_sandwich`, `dragon`, `alien`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of five separate friendly cartoon characters arranged in one row on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, each character shown whole from head to foot, no shadow on the background, no checkered or transparent background, no text, no letters, no labels, no numbers. Row 1, left to right: a white unicorn with a rainbow mane and a golden horn, standing; a pink elephant with big ears, standing and smiling; an ice cream sandwich character with two chocolate biscuits and white ice cream in the middle, with a happy face and little arms and legs; a friendly green dragon with small wings and a long tail, standing; a friendly blue and green alien with one big eye and two antennae, standing.
```

**13. GG1 U3 — животные и монстр, лист 2** → `raccoon_squirrel`, `clowns`, `jellyfish`, `cat_sofa`, `blue_monster`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of five separate items arranged in a 3 by 2 grid, the sixth cell left completely empty and white, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no shadow on the background, no dark or black background anywhere, no text, no letters, no labels, no numbers. Row 1, left to right: a raccoon and a red squirrel standing side by side, both drawn in the same cartoon style and the same size as each other; two cheerful circus clowns in colourful costumes standing side by side; one orange jellyfish with a round bell and long trailing tentacles, on white, not on a dark sea background. Row 2, left to right: a grey striped cat lying curled up and asleep on a blue sofa; a friendly shaggy blue monster with two round eyes, a wide smile and four little arms, standing.
```

**14. GG1 U3 — детская комната, сцена** → `kids_room_test`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One wide children's bedroom scene seen from the open side of the room: a bed with a striped duvet against the left wall, a wooden wardrobe beside it, a desk with a chair and a lamp under the window, a bookshelf with colourful books, a toy box with a teddy bear and a football, a patterned rug on the floor and a framed picture on the wall. The room is empty of people. Generous empty margin all around so nothing is cut off at the edge, plain flat pure white background outside the room walls, no text, no letters, no labels, no numbers, nothing written on the books or the picture.
```

**15. GG1 U4 — части тела и предметы, лист** → `body_ears`, `body_nose`, `homework_diary`, `rabbit`, `obj_mixing_bowl`, `obj_french_flag`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of six separate items arranged in a 3 by 2 grid on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no frames or borders around the items, no shadow on the background, no dark background anywhere, no text, no letters, no labels, no numbers. Row 1, left to right: a close-up of two children's ears, one on each side of a simple head shape, the ears large and clearly the subject; a close-up of a child's nose and the middle of the face, the nose large and clearly the subject; an open spiral school diary lying flat with blank ruled pages and a pencil beside it, nothing written on the pages. Row 2, left to right: a fluffy white rabbit sitting, seen from the side; a large metal mixing bowl with a whisk resting inside it; the flag of France, blue white and red vertical stripes, on a short flagpole with a round base.
```

**16. GG1 U4 — люди, четыре сцены** → `teacher_board`, `boy_cap`, `sisters_blond`, `english_class`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of four separate small scenes arranged in a 2 by 2 grid on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no shadow on the background, no text, no letters, no labels, no numbers, nothing written on the board or the books. Row 1, left to right: a smiling woman teacher standing beside a green chalkboard holding a pointer, the board completely blank; a boy wearing a blue baseball cap and a green T-shirt, standing and waving, shown from head to foot. Row 2, left to right: two blonde sisters of the same age standing side by side holding hands, one in a blue dress and one in a pink dress, shown from head to foot; an English lesson scene with a woman teacher at the front and four children sitting at desks with open books, seen from the back of the classroom.
```

**17. GG1 U4 — шесть монстриков, лист** → `monsters_six`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of six different friendly cartoon monsters arranged in a 3 by 2 grid on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, each monster shown whole from head to foot and standing, no shadow on the background, no text, no letters, no labels, no numbers. Row 1, left to right: a round blue monster with two eyes and two short horns; a tall purple monster with three eyes and long thin arms; a small green monster with one big eye and four short legs. Row 2, left to right: a fluffy yellow monster with two eyes, big ears and no arms; an orange monster with two eyes, two curved horns and big flat feet; a pink monster with four eyes, a wide smile and two little wings.
```

**18. GG1 U5–U6 — предметы дня, лист** → `obj_gym`, `obj_family_dinner`, `pocket_watch`, `piano`, `life_brush_teeth`, `weather_sunny`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of six separate items arranged in a 3 by 2 grid on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, everything in full colour, nothing black and white, no shadow on the background, no text, no letters, no labels, no numbers, no numerals on any dial. Row 1, left to right: a treadmill with two dumbbells beside it; a wooden dining table laid for four with plates, glasses and a small vase of flowers; a round golden pocket watch on a chain, in full colour, with plain tick marks and no numerals on the dial. Row 2, left to right: a black grand piano with the lid open, seen from the side; a blue toothbrush with white toothpaste on it beside a glass of water; a bright yellow sun with soft white clouds in a blue sky.
```

**19. GG1 U6 — мальчик просыпается, сцена** → `boy_wakes_up`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One bedroom scene in the morning: a boy in green pyjamas sitting up in bed and stretching his arms above his head with a sleepy smile, a bedside table with a round alarm clock beside him, bright morning sunlight coming through the open curtains of the window behind the bed, a rug on the floor and slippers beside the bed. The alarm clock has plain tick marks only. Generous empty margin all around so nothing is cut off at the edge, plain flat pure white background outside the room walls, no text, no letters, no labels, no numbers, no numerals on the clock dial.
```

**20. GG1 U6 — день Эрика, комикс из шести кадров** → `eric_day_comic`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of six separate small scenes about one boy's day, arranged in a 3 by 2 grid on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, everything in full colour, nothing black and white, the same brown-haired boy in every scene, no shadow on the background, no comic panel borders, no speech bubbles, no text, no letters, no labels, no numbers. Row 1, left to right: the boy waking up and stretching in bed; the boy eating a bowl of cereal at the kitchen table; the boy walking to school with a backpack. Row 2, left to right: the boy sitting at a school desk writing in a notebook; the boy playing football in a park; the boy brushing his teeth at a bathroom sink before bed.
```

### Промпты 21–30 (Go Getter 1 финал, SM1, SM3, GG2)

**21. GG1 U7–U8 — спорт, лист** → `sport_basketball`, `sport_cycling`, `sport_hockey`, `sport_taekwondo`, `sport_volleyball`, `sport_football`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of six separate sports items arranged in a 3 by 2 grid on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, each item shown whole, no shadow on the background, no text, no letters, no labels, no numbers, no brand marks. Row 1, left to right: an orange basketball in front of a hoop with a white net; a blue road bicycle seen from the side; an ice hockey stick with a black puck beside it. Row 2, left to right: a white taekwondo suit folded with a black belt on top; a blue white and yellow volleyball in front of a net; a black and white football in front of a goal with a white net.
```

**22. GG1 U8 и финал — теннис, машина, ботинок, школа** → `sport_tennis`, `final_car`, `final_boot`, `school_walk`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of four separate items arranged in a 2 by 2 grid on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no shadow on the background, no text, no letters, no labels, no numbers, no signs with writing anywhere. Row 1, left to right: a tennis racket lying beside a yellow tennis ball; a small red car seen from the front three-quarter angle. Row 2, left to right: one single brown leather lace-up boot, seen from the side; a boy with a backpack walking along a path towards a school building with a clock tower and an open front door, the school sign board completely blank.
```

**23. GG1 Final — гостиная для аудирования** → `final_living_room` (сцена; шесть предметов обязательны)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One wide living room scene seen from the open side of the room, empty of people, containing exactly these things in exactly these places and nothing else that could be mistaken for them: a tall wooden bookcase on the left with a brown radio standing on one of its shelves; a yellow armchair on the left with a blue school bag resting on its seat; a round wooden coffee table in the middle with a small silver toy robot standing on it; a long wooden sideboard on the right with a round white wall clock hanging above it; a cream round rug on the floor with a red and blue striped ball lying on its right side and a red and yellow kite with a ribbon tail lying on its left side; a window with curtains at the back. The radio, the bag, the robot, the clock, the ball and the kite must all be clearly visible and easy to recognise. Generous empty margin all around so nothing is cut off at the edge, no text, no letters, no labels, no numbers, no numerals on the clock dial.
```

**24. SM1 U8 — «умеет / не умеет», шесть картинок** → `t_he_piano`, `t_he_tennis`, `t_he_swim`, `t_she_dance`, `t_she_pony`, `t_she_bike`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of six separate small scenes arranged in a 3 by 2 grid on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no shadow on the background, no text, no letters, no labels, no numbers. Each scene shows one child and one activity, and each scene has a large tick or cross mark in its top right corner: a thick bright green tick means the child can do it, a thick bright red cross means the child cannot do it. The sex of the child in each scene matters and must be unmistakable. Row 1, left to right: a boy sitting at a piano looking sadly at the keys with his hands in his lap, with a big red cross in the corner; a boy standing on a tennis court dropping his racket and looking unhappy, with a big red cross in the corner; a boy swimming happily in blue water, with a big green tick in the corner. Row 2, left to right: a girl dancing happily on her toes with her arms raised, with a big green tick in the corner; a girl standing beside a brown pony and not riding it, holding the reins and looking unsure, with a big red cross in the corner; a girl riding a blue bicycle and smiling, wearing a helmet, with a big green tick in the corner.
```

**25. SM1 — три точечные правки** → `body_fingers`, `legacy/70d72135a807` (горох), `t_yellow_desk`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of three separate items arranged in one row on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no shadow on the background, no text, no letters, no labels, no numbers. Row 1, left to right: a very close view of a child's four fingers and thumb held up and spread wide, cropped so that the fingers fill almost the whole cell and only a small part of the palm is visible, the fingers clearly the subject and not the hand as a whole; an empty white dinner plate seen from above with nothing on it at all, and beside the plate a small bunch of green peas with a thick red diagonal line drawn across the peas to show there are none; a school desk with an attached chair where the desk top, the desk frame and the chair are all bright yellow, no brown and no wood colour anywhere on it.
```

**26. SM3 U4 — город, широкая сцена** → `scene_town_busy`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One wide town street scene in the daytime: a library with columns, a bank, a market with striped awnings and crates of fruit, a bus station with a blue bus at the stop, a clock tower, a zebra crossing with people walking across, a few parked bicycles, trees along the pavement and a blue sky with soft clouds. The buildings are large and easy to tell apart, and every shop sign board is completely blank. Generous empty margin all around so nothing is cut off at the edge, no text, no letters, no labels, no numbers, no numerals on the tower clock dial.
```

**27. SM3 U9 — туман и каникулы** → `weather_foggy`, `scene_holiday_plans`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of two separate items side by side in one row on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no shadow on the background, no photographic realism anywhere, no text, no letters, no labels, no numbers. Row 1, left to right: a foggy weather icon drawn as a soft grey cloud with three thick pale grey fog bands below it and the faint outline of two trees and a road showing through the fog; a holiday packing scene seen from above with an open suitcase, a sun hat, swimming goggles, a beach ball, a camera, a guidebook and a pair of sandals laid out neatly around it, the guidebook cover completely blank.
```

**28. SM3 Final — дом и улица для «верно / неверно»** → `scene_house` (все шесть деталей обязательны)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One wide scene of a yellow two-storey house with a brown tiled roof and the street in front of it, containing exactly these things: a round window directly above the green front door; a balcony on the first floor where a man and a woman stand side by side and the woman is clearly taller than the man; in the garden on the left a woman holding a kite by its string while a boy watches her; on the pavement a boy riding a skateboard, wearing a long red scarf around his neck and having curly hair; a girl in a red sweater skipping with a skipping rope in front of the house; a man carrying a small child on his arm and a shopping bag in his other hand; a sky with soft white clouds and no birds anywhere, especially none on the roof. Generous empty margin all around so nobody is cut off at the edge, no text, no letters, no labels, no numbers, no house number and no signs.
```

**29. SM3 Final — библиотека для аудирования** → `scene_library` (шесть человек на своих местах)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One wide library scene seen from the open side of the room, with six people clearly separated from each other and easy to point at: in the top left corner a blond boy standing on a chair taking a book from a high shelf; in the top right corner a boy in a brown coat standing by a coat stand; in the middle left a girl with a ponytail sitting at a yellow table writing in an open notebook; below her on the left a dark-haired boy walking and carrying a tall stack of books; in the middle a small girl sitting cross-legged on the floor under the table reading; in the lower right a woman with curly hair sitting at a desk typing on a computer keyboard. A big window at the back shows a rainy street with a red car. Generous empty margin all around so nobody is cut off at the edge, no text, no letters, no labels, no numbers, nothing written on the books or the screen.
```

**30. GG2 — калькулятор и метро** → `calculator`, `underground`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A sheet of two separate items side by side in one row on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no shadow on the background, no photographic realism anywhere, no text, no letters, no labels, no numbers, no digits on the keys or the display. Row 1, left to right: a pocket calculator seen at a slight three-quarter angle with a blank grey display and plain blank square keys; an underground train coming out of a tunnel towards the viewer on its rails, with a lit front window and a station platform beside it, the destination board completely blank.
```

### Промпт 31 (SM0)

**31. SM0 Final — руки целиком** → `arms`

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One single item on a plain flat pure white background, complete and not touching the edge, with generous empty white margin all around, no shadow on the background, no text, no letters, no labels, no numbers. Two children's arms shown whole from the shoulder down to the hand, one on the left and one on the right, both bent slightly at the elbow with the hands relaxed and the fingers together, the upper arm and the forearm clearly visible on both, wearing short yellow sleeves at the shoulders so that it is obvious these are arms and not just hands.
```

---

## Что сделать после генерации

1. Нарезать листы, сжать в webp 88–90, имена файлов оставить прежние — тогда
   блоки в базе править не придётся.
2. Собрать контактный лист по курсу и показать Анне до замены.
3. Отдельно, **миграцией, а не картинкой**, закрыть три места, где нужен текст:
   * SM1 U8 b3 — если Анна решит не рисовать ✓/✗, переписать варианты так,
     чтобы отрицание читалось из самой картинки;
   * SM3 Final b10 — либо новая сцена (промпт 28), либо утверждение про шарф
     переписать под то, что есть;
   * GG1 Final b10 — поменять пример про «два кресла» в заголовке.

---

## Сделано 02.11.2026 (миграцией, не картинкой)

Миграция `classroom_fix_kartinka_klyuch_20261102`, копия старых payload —
таблица `classroom_backup_kartinka_klyuch_20261102`:

* **SM1 Unit 8 Test, блок 3.** На картинках нет ни ✓, ни ✗, поэтому отрицание
  прочитать неоткуда, а местоимения не совпадали с полом (девочка за пианино
  при «He…», мальчик на велосипеде при «She…»). Ключи сделаны утвердительными
  и по картинке, местоимения — по полу; отрицания и чужое местоимение остались
  среди неверных вариантов, так что грамматика can / can't и he / she
  по-прежнему проверяется. ✓/✗ на картинки не дорисовываем: крестик поверх
  девочки на пони читается как «нельзя», а не «не умеет».
* **SM3 Final Test, блок 10.** Утверждение про шарф заменено на
  «The boy who is riding the skateboard has red hair» (верно) — придаточное
  сохранено, шарфа на картинке нет ни на ком.
* **GG1 Final Test, блок 10.** Пример в заголовке «two armchairs — YES»
  (кресло и диван, спорно) заменён на «The family is playing a board game — YES».

Остаётся по картинкам: `body_hand` / `body_fingers` в SM1 Unit 8 заменены
02.11.2026 (ладонь и отдельно пальцы) — пункт 2 списка закрыт.
