# SM2 — вычитка картинок: что перерисовываем и промпты

Проход по картинкам Super Minds 2 — домашки и тесты, все типы блоков кроме
`text`, `video`, `embed`. Сделано 02.11.2026 по правилам `CLAUDE.md`
(разделы «Картинки», «Регламент работы над юнитом», «Вычитка картинок»)
и `docs/vychitka/kartinki/plan.md`.

## Сколько работы

| что считали | сколько |
|---|---|
| картинок стоит в заданиях SM2 (уникальных файлов) | **364** |
| ссылок на них из блоков | 945 |
| битых ссылок (файла нет на диске) | **0** |
| меньше 300 px по большей стороне | **13** |
| меньше 400 px | 145 (медиана по большей стороне — 420 px) |
| **под перерисовку** | **91 файл** |
| **листов-промптов** | **29** |
| собираем сами из готовых картинок, генерация не нужна | 5 файлов |
| переносим в блок текстом, картинка не нужна | 1 файл |

Все 13 мелких (`shared/yes_thumb_up`, `shared/no_thumb_down`, восемь
`u7/ac_*`, `u7/t_bike`, `u7/t_scooter`, `u6/f_nose`) попали в список
перерисовки — кроме `t_bike` и `t_scooter`: там 273×194 и 288×262, рисунок
чистый, а увеличение до карточки в полтора раза ещё держит (правило Анны от
23.10). Их смотрим глазами на контактном листе вместе с остальным транспортом.

Главная беда SM2 — не размер, а **разнобой**: целый юнит 4 собран из стоковых
фотографий еды, в юните 5 в одном блоке стоят фотография, клипарт и 3D-рендер,
в юните 7 среди мультяшных картинок — фотография мотоциклиста. Второе по
важности — **картинки, спорящие с ключом** (список ниже первым).

## Где картинка спорит с ключом — чинить в первую очередь

| файл | где | в чём расхождение |
|---|---|---|
| `u3/b_in_front_of.webp` и `u3/b_next_to.webp` | ю3 ДЗ 3 блок 16 (quiz), ДЗ 7 блок 13 (match) | на обеих картинках мяч лежит **справа у угла коробки** — геометрия одна и та же. Ключи разные: «in front of» и «next to». Ребёнок не может выбрать правильно |
| `u3/fish_behind.webp` | ю3 ДЗ 3 блоки 5 и 6 | ключ «behind», а из-за камня торчит только хвост у самого края кадра — читается как «рядом». Картинка обрезана по краю |
| `u3/fish_next_to.webp` | ю3 ДЗ 3 блоки 5 и 6 | ключ «next to», рыбка плавает в воде далеко от камня — связи с камнем не видно |
| `u2/test_wakeup.webp` | ю2 тест блок 9 (gaps) | текст про **брата**: «Does your brother get up at 6 o'clock? — Yes, **he** does», а на картинке просыпается **девочка** |
| `u6/h_our.webp` | ю6 ДЗ 3 блок 14 (gaps) | ключ «It's **our** house», а дома на картинке нет вообще: кадр обрезан, видно кусок жёлтого фона, реплику и двух детей по нижнему краю |
| `u6/h_their.webp` | ю6 ДЗ 3 блок 15 (gaps) | ключ «It's **their** house», дом ушёл в левый край кадра, дети обрезаны |
| `u0/wall.webp` | ю0 ДЗ 1 блоки 2, 5, 6, 7 | ключ «wall», а картинка — ровный голубой квадрат без единой детали. Опознать стену нельзя |
| `u0/floor.webp` | ю0 ДЗ 1 блоки 2, 5, 6, 7 | ключ «floor», а картинка — текстура досок без перспективы: так же читается как стол или стена |
| `u5/w_posters.webp` и остальные `w_*` | ю5 ДЗ 2 блоки 16–19 (order) | задания про **this / that / these / those**, то есть про «близко — далеко», а на фотографиях близости и дальности не видно совсем. Плюс `w_posters` — это постеры фильма «Железный человек», чужая картинка в учебнике |
| `u4/weights_one.webp` | ю4 ДЗ 6 блок 13 (gaps) | веса сходятся (виноград 5 г, яйцо 50 г, киви 75 г, манго 200 г), но картинка — кусок страницы учебника с чёрными полосами сверху и снизу |

Проверено и **сошлось**, не трогаем:

* `u4/scales.webp` — все шесть стрелок стоят ровно там, где ждёт ключ
  (50 · 150 · 800 · 250 · 600 · 300 г). Любой новый рендер стрелок разойдётся
  с ответами — перерисовывать нельзя;
* `u1/paul_day.webp` — часы на кадрах 1, 4, 5, 7 показывают 7, 1, 5 и 8 часов,
  ровно как в ключе. Это разворот учебника;
* `u5/materials_five.webp`, `u5/my_things.webp`, `u8/places3.webp` — по составу
  сходятся с ключом, вопрос только к стилю (фотоколлажи);
* `u6/monster.webp`, `u3/t_dog_behind.webp`, `u5/t_bedroom.webp`,
  `u8/g_bat.webp` — это картинки из прошлого списка `builds/sm2/prompts_redraw.md`,
  они уже перерисованы и ключам соответствуют;
* `u2/man_snake.webp` — имя файла врёт (там мальчик, а не мужчина), но ключ
  «He doesn't like snakes» картинке не противоречит.

## Что перерисовываем — таблица

«Блок» — номер **как в редакторе** (`sort_order + 1`).

### Юнит 0

| файл | где стоит | что не так |
|---|---|---|
| `wall.webp` | ДЗ 1 блоки 2, 5, 6, 7 | голубой квадрат вместо стены, спорит с ключом |
| `floor.webp` | ДЗ 1 блоки 2, 5, 6, 7 | текстура досок без перспективы, спорит с ключом |
| `hw2_desk.webp` | ДЗ 2 блоки 4, 5 | плоский клипарт на жёлтом фоне, чужой стиль |
| `test_classroom.webp` | тест блок 10 | плоский клипарт-класс, чужой стиль |

### Юнит 2

| файл | где стоит | что не так |
|---|---|---|
| `test_wakeup.webp` | тест блок 9 | девочка вместо брата — спорит с ключом; плоский клипарт |
| `speaking_pairs.webp` | ДЗ 5 блок 10 | скан страницы учебника, мелкие значки не читаются — **пересобираем таблицей из готовых картинок юнита, генерация не нужна** |
| `test_likes.webp` | тест блок 21 | таблица из фотографий еды и смайликов — **пересобираем сами из `u4/f_*` после их перерисовки** |

### Юнит 3

| файл | где стоит | что не так |
|---|---|---|
| `fish_behind.webp` · `fish_between.webp` · `fish_in_front_of.webp` · `fish_next_to.webp` | ДЗ 3 блоки 5, 6 | кадры из истории, обрезаны по краю, положение рыбки не читается; два из четырёх спорят с ключом |
| `b_in_front_of.webp` · `b_next_to.webp` · `b_between.webp` | ДЗ 3 блок 16, ДЗ 7 блок 13 | «перед» и «рядом» нарисованы одинаково |
| `town_test.webp` | тест блок 14 | полоса из учебника с вывесками, чужой стиль, текст вшит в картинку |

### Юнит 4 — весь набор еды снят фотостоком

| файл | где стоит | что не так |
|---|---|---|
| `f_apple` `f_bread` `f_cake` `f_cheese` `f_egg` `f_grapes` `f_greens` `f_kiwi` `f_lemon` `f_mango` `f_potato` `f_strawberries` `f_tomato` `f_watermelon` `f_beans` `f_basket` | ДЗ 1 блоки 2, 3, 6, 7, 11, 14, 15; ДЗ 5 блок 12; ДЗ 7 блок 5; тест блоки 3, 4 | шестнадцать стоковых фотографий подряд: в карточках лексики и в вариантах ответа они стоят рядом с 3D-рисунками остальных юнитов |
| `hy_apple_mandarin` `hy_banana_orange` `hy_orange_kiwi` `hy_pineapple_banana` `hy_strawberry_apple` `hy_tomato_lemon` | ДЗ 7 блок 20 | фотоколлажи-гибриды, склейка видна швом |
| `weights_one.webp` | ДЗ 6 блок 13 | скан страницы с чёрными полосами по краям |

### Юнит 5 — самый разнобойный

| файл | где стоит | что не так |
|---|---|---|
| `mat_wood` `mat_metal` `mat_plastic` `mat_glass` `mat_fabric` | ДЗ 6 блок 3 | в одном блоке: фотография ткани, клипарт стакана, 3D-брёвна, фото бутылки |
| `my_things.webp` | ДЗ 6 блок 11 | коллаж из пяти фотографий мебели |
| `materials_five.webp` | ДЗ 6 блок 9 | коллаж из пяти фотографий, у каждой свой фон |
| `m_bed` `m_mirror` `m_armchair` `m_lamp` | ДЗ 7 блок 19 | четыре каталожные фотографии мебели |
| `w_wardrobe` `w_chair` `w_posters` `w_lamps` | ДЗ 2 блоки 16–19 | фотографии, близость-дальность не показана; `w_posters` — чужие постеры фильма |
| `dream_room.webp` | ДЗ 7 блок 20 | фотография интерьера; ключ требует белую деревянную кровать, розовый пластиковый стул и белую лампу |
| `dream_room2.webp` | ДЗ 7 блок 21 | фотография интерьера, чужой стиль |
| `family.webp` | ДЗ 5 блок 7 | **не перерисовываем**: иллюстрация учебника с пустыми табличками, а задание привязано к настоящей записи (`sm2_u5_hw5_b6.mp3`). Переделка разойдётся с записью |

### Юнит 6

| файл | где стоит | что не так |
|---|---|---|
| `h_my` `h_your` `h_his` `h_her` `h_our` `h_their` | ДЗ 3 блоки 10–15 | палочные человечки, два кадра обрезаны и спорят с ключом |
| `q_forest` `q_tall` `q_rhino` `q_family` | ДЗ 7 блоки 6–9 | четыре стоковые фотографии с тёплым фильтром |
| `girl_hair.webp` | тест блок 4 | плоский клипарт в белой рамке |
| `emotions5.webp` | ДЗ 7 блоки 13, 18 | кадры из мультфильма «Головоломка» — чужая картинка. **Генерация не нужна: собираем коллаж из готовых `e_sad` `e_happy` `e_angry` `e_scared` `e_excited` в тех же точках (16/25, 50/25, 84/25, 16/75, 50/75)** |
| `hw5_q1a … hw5_q5c` (15 штук) | ДЗ 5 блок 3 | плоский клипарт, но между собой набор согласован, а ответы завязаны на запись (очки, цвет волос, порода собаки). **Перерисовывать только вместе с текстом записи — сначала Анна её переслушивает** |
| `quotes6.webp` · `story_scene.webp` · `portraits4.webp` | ДЗ 4 блок 7, ДЗ 4 блок 3, ДЗ 6 блок 4 | кадры истории с героями курса (Misty, Flash) — **не трогаем** |

### Юнит 7

| файл | где стоит | что не так |
|---|---|---|
| `ac_basketball` `ac_reading` `ac_bike` `ac_sleeping` `ac_singing` `ac_flying` `ac_eating` `ac_jumping` | ДЗ 3 блок 19 | восемь плоских картинок 225×265 — самые мелкие в курсе |
| `tt_skate` `tt_football` `tt_heli` `tt_kite` | тест блок 5 | в одном вопросе три фотографии и два клипарта |
| `tt_bike` `tt_plane` `tt_book` | тест блоки 5, 7, 8 | то же: клипарт из учебника и фотографии |
| `p_motorbike.webp` | ДЗ 6 блок 5 | единственная фотография среди четырёх мультяшных картинок того же блока |

### Юнит 8

| файл | где стоит | что не так |
|---|---|---|
| `i_ballet` `i_bike` `i_swim` | ДЗ 3 блоки 8, 10, 11, 12 | обрезки страницы учебника: в кадре остались галочки, крестики и обрывки слов |
| `places3.webp` | ДЗ 6 блок 7 | коллаж из трёх фотографий (track · court · pitch) |
| `sports6.webp` | ДЗ 5 блок 11 | коллаж из шести фотографий. **Генерация не нужна: собираем из готовых `s_*`** |
| `park_scene` · `dialogs4` · `a_dancing … a_tennis` | ДЗ 5 блоки 3, 4, 6; ДЗ 3 блок 7; ДЗ 2 блоки 8, 13, 14 | иллюстрации учебника, по ним сверяются ответы — **не трогаем** |

### Юнит 9

| файл | где стоит | что не так |
|---|---|---|
| `tt_grandma` `tt_riding` `tt_treehouse` `tt_bike` | тест блок 4 | три фотографии и один клипарт в одном вопросе |
| `n_bins` `n_nature` `n_path` `n_recycle` `n_rubbish` | ДЗ 6 блок 4 | в одном блоке 3D-рендер, живописный пейзаж и фотография мусора |
| `act_box.webp` | ДЗ 6 блок 8 | это не картинка, а скан рамки со словами (go fishing, go hiking…). **Переносим текстом в сам блок, картинку убираем** |
| `pen_fish` `pen_ride` `pen_tree` · `party_scene` · `proj1–3` | ДЗ 2 блок 5; финальный тест блок 4; ДЗ 5 блоки 6, 7 | кадры истории и развороты учебника — **не трогаем** |

### Общие

| файл | где стоит | что не так |
|---|---|---|
| `shared/yes_thumb_up.webp` · `shared/no_thumb_down.webp` | ю0 ДЗ 2 блоки 4, 5, 7, 14, 15 и дальше по курсам | 149×150 — мельче всех в SM2; иконка общая для всех курсов, менять только с «да» Анны |

### Юнит 1 — перерисовывать нечего

Набор `get_up`, `brush_your_teeth`, `have_breakfast` и остальные — ровный 3D,
стиль держится. `routine_six.webp` (ДЗ 3 блок 4) — плоский коллаж, но
**генерация не нужна: собираем его сами** из уже готовых картинок юнита и
дорисовываем циферблаты (7:00 · 8:00 · 8:00 · 9:00 · 3:00 · 10:00 в точках
17/27, 48/27, 80/27, 17/72, 48/72, 80/72). `test_schedule.webp` и
`hw3_hero.webp` — чужой стиль, но стоят в speaking и в задании без проверки;
смотрим их на контактном листе вместе с Анной.

---

# Промпты

Каждый промпт — цельный блок, копируется одним нажатием. Строка стиля уже
внутри. Листы режем мы: порядок предметов в каждом промпте перечислен
построчно, по нему и нарежем.

Хранить присланные листы **без уменьшения**: карточка нам нужна 600–800 px по
большей стороне, сцена 1200–1600.

Промпты 2, 3 и 7 — одиночные широкие сцены (парта, класс, улица): в сетку они
не влезают, поэтому строки «wide empty white gaps between the items» в них нет,
остальные требования те же.

## Пачка 1 — промпты 1–10

### 1. `u0/wall.webp` + `u0/floor.webp` — стена и пол класса

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with two separate pictures in a row, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) the inside corner of a classroom wall painted light blue, seen at a slight angle so that the vertical corner line and the white skirting board along the bottom are both visible, the wall completely empty with nothing hanging on it; 2) a classroom floor of warm honey-coloured wooden boards seen from above at a slight angle, with the very bottom of a light blue wall and its white skirting board running along the top edge of the picture so it clearly reads as a floor of a room, nothing standing on the floor.
```

### 2. `u0/hw2_desk.webp` — парта с яблоком (сцена)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A single scene on a plain flat pure white background, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. A wooden school desk seen from the front at a slight angle. On the desk top, clearly separated from one another: one red apple, a group of five coloured crayons lying side by side, and a stack of three closed books. On the light blue classroom wall behind the desk hangs one round clock with a red rim, high above the desk, clearly on the wall and not on the desk. The clock face has plain tick marks and two hands and no digits at all. IMPORTANT: exactly one apple, several crayons, several books, and the clock is on the wall. IMPORTANT FRAMING: the whole scene is small in the frame and fully visible, with a generous empty white margin on all four sides.
```

### 3. `u0/test_classroom.webp` — класс целиком (широкая сцена)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A single wide scene on a plain flat pure white background, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. A bright, friendly primary-school classroom seen from the front. In the picture, each clearly visible and not overlapping: a big green board on the wall, a wooden bookcase full of colourful books, a tall wooden cupboard with closed doors, a window with a blue sky outside, a wooden door, a round wall clock with plain tick marks and two hands and no digits, three small desks with a chair at each, and a few coloured crayons lying on the nearest desk. The floor is made of honey-coloured wooden boards. No people in the room. IMPORTANT: the board on the wall is completely empty, with nothing written or drawn on it. IMPORTANT FRAMING: the whole room is fully visible, with a generous empty white margin on all four sides.
```

### 4. `u2/test_wakeup.webp` + `u6/girl_hair.webp` — мальчик просыпается и девочка с рыжими волосами

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with two separate pictures in a row, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) a boy of about eight waking up in his bed in the morning, sitting up with his arms stretched wide above his head and his mouth open in a big yawn, a blue blanket over his legs, a window with bright morning sunshine behind the bed — it must be clearly a boy with short hair, not a girl; 2) a friendly head-and-shoulders portrait of a girl of about eight with bright orange hair falling to her shoulders and big light blue eyes, smiling straight at the viewer, wearing a plain light green T-shirt — her hair is clearly orange and her eyes are clearly blue.
```

### 5. `u3/fish_behind` `fish_in_front_of` `fish_next_to` `fish_between` — четыре предлога с рыбкой

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with four separate small scenes in a two-by-two grid, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. The same three things appear in every scene: a small bright orange cartoon fish, one big smooth grey rock, and snowy white ground. Row 1, left to right: 1) the fish is BEHIND the rock — the rock stands in the middle, and only the fish's head peeks out past the left side of the rock and only its tail past the right side, the whole middle of the fish hidden by the rock; 2) the fish is IN FRONT OF the rock — the fish is between the viewer and the rock, overlapping the lower middle of the rock, its whole body visible. Row 2, left to right: 3) the fish is NEXT TO the rock — the fish lies on the snow at the right-hand side of the rock, touching nothing, clearly beside it and not overlapping it at all; 4) the fish is BETWEEN a tree and the rock — a dark green fir tree stands on the left, the grey rock stands on the right, and the fish lies exactly in the middle of the empty gap between them.
```

### 6. `u3/b_in_front_of` `b_next_to` `b_between` — коробка и мяч

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with three separate small scenes in a row, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. The same two things appear in every scene: a light brown cardboard box and a bright red ball. Row 1, left to right: 1) the ball is IN FRONT OF the box — the box is seen straight from the front, and the ball stands between the viewer and the box, in the middle, overlapping the bottom edge of the box's front face so it is obviously nearer to the viewer than the box; 2) the ball is NEXT TO the box — the box is seen straight from the front, and the ball stands on the ground at the right-hand side of the box, level with the box's side wall, clearly beside it and not overlapping it and not nearer to the viewer; 3) the ball is BETWEEN two boxes — one box on the left, one box on the right, both the same size, and the ball exactly in the middle of the empty gap between them, touching neither. IMPORTANT: pictures 1 and 2 must look clearly different from each other — in picture 1 the ball is nearer to the viewer than the box, in picture 2 the ball is at the side of the box and the same distance away.
```

### 7. `u3/town_test.webp` — улица города (широкая сцена)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. A single wide scene on a plain flat pure white background, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. A friendly town street seen straight from the front, with a pavement and a road along the bottom. Standing in a row along the street, left to right and clearly separated: a school with a bell tower and a yellow door, a café with a striped awning and two small round tables outside, a cinema with a round marquee and light bulbs, a hospital with a red cross, and a train station with a small blue and white train standing at the platform. A green park with three trees and a bench stands behind the row of buildings. A yellow car and a red bus drive along the road. Above the entrance of each of the five buildings hangs a plain blank white rectangular sign board. IMPORTANT: every sign board is completely empty, with no writing, letters or symbols on it anywhere in the picture. IMPORTANT FRAMING: the whole street is fully visible, with a generous empty white margin on all four sides.
```

### 8. `u4/f_apple` `f_bread` `f_cake` `f_cheese` `f_egg` — еда, лист 1

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with five separate food items, three in the top row and two in the bottom row, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) three shiny red apples with green leaves lying together; 2) one golden loaf of bread with two cut slices leaning against it; 3) one round birthday cake with white icing and pink and blue cream swirls around the top edge, no candles. Row 2, left to right: 4) one big wedge of yellow cheese with round holes, with two small cheese cubes next to it; 5) three white chicken eggs lying together.
```

### 9. `u4/f_grapes` `f_greens` `f_kiwi` `f_lemon` `f_mango` — еда, лист 2

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with five separate food items, three in the top row and two in the bottom row, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) one bunch of light green grapes with two green leaves on the stem; 2) a small bunch of fresh green herbs — parsley and dill tied together with string; 3) one whole brown fuzzy kiwi fruit with one half cut open beside it showing the bright green inside with black seeds. Row 2, left to right: 4) one whole yellow lemon with one half cut open beside it and a green leaf; 5) one whole red and yellow mango with one half cut open beside it showing the orange flesh.
```

### 10. `u4/f_potato` `f_strawberries` `f_tomato` `f_watermelon` `f_beans` `f_basket` — еда, лист 3

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with six separate food items in two rows of three, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) three brown potatoes lying together; 2) three bright red strawberries with green tops, one of them cut in half; 3) one big round red tomato with a green star-shaped top. Row 2, left to right: 4) one whole green striped watermelon with one triangular red slice with black seeds leaning against it; 5) a small neat pile of about fifteen dark red kidney beans; 6) a woven wicker shopping basket full of food — a loaf of bread, a bottle of milk, a green pepper, two red tomatoes and a bunch of green herbs sticking out of the top.
```

## Пачка 2 — промпты 11–20

### 11. `u4/hy_*` — шесть фруктов-гибридов

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with six separate imaginary hybrid fruits in two rows of three, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Each hybrid is one single whole fruit whose left half is one fruit and whose right half is another, joined smoothly down the middle so both halves are easy to recognise. Row 1, left to right: 1) left half a red apple with a green leaf, right half an orange mandarin; 2) left half a yellow banana, right half a round orange; 3) left half an orange, right half a green kiwi with black seeds. Row 2, left to right: 4) left half a spiky yellow-brown pineapple with a green crown, right half a yellow banana; 5) left half a red strawberry with a green top, right half a red apple; 6) left half a red tomato with a green star-shaped top, right half a yellow lemon.
```

### 12. `u4/weights_one.webp` — ряд продуктов для задания про вес

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with six separate food items standing in one single horizontal row, all the same height in the picture, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) one whole brown fuzzy kiwi fruit; 2) one small round red tomato with a green top; 3) one single light green grape with a short stem; 4) one whole red and yellow mango with a green leaf; 5) one brown chicken egg; 6) one brown potato. IMPORTANT: leave a wide empty white strip under the row, about one third of the height of the picture, completely empty and pure white — the weights will be written there afterwards.
```

Подписи «75 g · 100 g · 5 g · 200 g · 50 g · 150 g» ставим мы сами, ровным
шрифтом, под нужными предметами — генератору цифры не доверяем.

### 13. `u5/mat_wood` `mat_metal` `mat_plastic` `mat_glass` `mat_fabric` — пять материалов

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with five separate groups of objects, three in the top row and two in the bottom row, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Each group shows things made of one material only, so the material is obvious at a glance. Row 1, left to right: 1) WOOD — a short round log with visible tree rings lying next to two smooth planks of pale wood; 2) METAL — a shiny silver spoon lying next to a shiny silver key; 3) PLASTIC — a bright blue plastic water bottle with a screw cap standing next to a red plastic cup. Row 2, left to right: 4) GLASS — a clear empty drinking glass standing next to a clear empty glass jar; 5) FABRIC — a folded soft red woollen blanket with an orange ball of yarn resting on it.
```

### 14. `u5/my_things.webp` — пять предметов для «из чего сделано»

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with five separate pieces of furniture, three in the top row and two in the bottom row, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) a table with a clear glass top and four thick wooden legs — both materials clearly visible; 2) a coral-pink plastic chair with a smooth moulded seat and back, obviously made of plastic only; 3) a desk lamp made of shiny silver metal with a round metal base and a jointed metal arm. Row 2, left to right: 4) a round wall mirror in a thin dark metal frame; 5) an armchair with a polished brown wooden frame and arms and soft patterned beige fabric on the seat and back.
```

Из этого листа мы соберём коллаж 900×686 той же раскладки, что сейчас: стол
слева вверху, зеркало справа вверху, стул слева внизу, лампа в середине внизу,
кресло справа внизу.

### 15. `u5/materials_five.webp` — четыре предмета для задания с метками

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with four separate objects in two rows of two, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) a rectangular woven rug with a bright geometric pattern in red, orange, yellow, green and blue — many different colours at once, obviously made of fabric; 2) a wooden wall shelf unit with three empty shelves, made of pale honey-coloured wood, nothing standing on the shelves. Row 2, left to right: 3) a round wall mirror in a wide white carved wooden frame with a lacy cut-out pattern; 4) an open silver laptop computer with a plain dark empty screen, standing on a white desk.
```

Кресло дерево + ткань для этого задания берём из листа 14 — пятым предметом
коллажа. Раскладка та же, что сейчас: ковёр (22/13), полка (78/23), кресло
(44/43), зеркало (21/78), ноутбук (67/78).

### 16. `u5/m_bed` `m_mirror` `m_armchair` `m_lamp` — четыре предмета для теста «made of»

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with four separate pieces of furniture in two rows of two, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) a single bed with a white painted METAL frame of thin round bars at the head and foot, made up with a grey fabric blanket and a white fabric pillow — metal and fabric and nothing else, no wood anywhere; 2) a tall standing mirror in a wide polished brown WOODEN frame with clear glass — wood and glass and nothing else. Row 2, left to right: 3) an armchair with a brown WOODEN frame and arms and soft patterned FABRIC on the seat and back — wood and fabric and nothing else, no metal; 4) a desk lamp with a black PLASTIC shade and a black plastic base and a shiny silver METAL arm between them — plastic and metal and nothing else, no wood and no glass.
```

### 17. `u5/w_wardrobe` `w_chair` `w_posters` `w_lamps` — this · that · these · those

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with four separate small scenes in a two-by-two grid, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. The same boy of about eight appears in all four scenes, standing in a simple empty room with a wooden floor, and the difference between the scenes is only how near or far the furniture is. Row 1, left to right: 1) THIS — the boy stands beside one tall wooden wardrobe that is right next to him, big in the picture, and he touches it with his outstretched hand; 2) THAT — the boy stands in the front of the picture and points at one single wooden chair that is far away on the other side of the room, small in the distance, with a wide empty floor between them. Row 2, left to right: 3) THESE — the boy stands beside the wall and points at two colourful posters hanging right next to him, big in the picture, within arm's reach; 4) THOSE — the boy stands in the front of the picture and points at two tall floor lamps that are far away on the other side of the room, small in the distance, with a wide empty floor between them. IMPORTANT: in scenes 1 and 3 the thing is very close and large, in scenes 2 and 4 it is clearly far away and small — the difference must be obvious at first glance. Posters and pictures in the scenes show only simple shapes and have no writing on them.
```

### 18. `u5/dream_room.webp` и `dream_room2.webp` — две комнаты мечты

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with two separate wide room scenes, one above the other, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Picture 1 (top): a child's dream bedroom seen from the front, with a WHITE WOODEN bed with a soft blanket in the middle, a PINK CHAIR made of smooth pink plastic with thin silver metal legs standing beside a small table, a WHITE PLASTIC table lamp standing on that table, a window with curtains on the left wall and a soft round rug on the floor. IMPORTANT for picture 1: the bed is white and made of wood, the chair is pink, the lamp on the table is white, and there are exactly these three things to notice. Picture 2 (bottom): a different child's dream bedroom seen from the front, cheerful and cosy, with a bunk bed with a ladder, a bookcase full of colourful books, a big beanbag chair, a desk with a chair, a round blue rug and a window with a blue sky outside. Any posters on the walls show only simple shapes and have no writing on them.
```

### 19. `u6/h_my` `h_your` `h_his` `h_her` `h_our` `h_their` — мой · твой · его · её · наш · их

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with six separate small scenes in two rows of three, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) MY — one boy standing alone, facing the viewer, with a big red heart shape on the front of his T-shirt, tapping that heart with his own finger and smiling; 2) YOUR — a girl standing on the left turned to the right and pointing her finger at a boy standing on the right, and the big red heart shape is on the boy's T-shirt; 3) HIS — a boy standing on the right with a big red heart shape on his T-shirt, and a girl standing on the left looking at him and pointing at his heart with her hand. Row 2, left to right: 4) HER — a girl standing on the right with a big red heart shape on her T-shirt, and a boy standing on the left looking at her and pointing at her heart with his hand; 5) OUR — a boy and a girl standing side by side directly in front of one small house with a red roof, their arms around each other's shoulders, both of their free hands pointing up at the house right behind them; 6) THEIR — one boy stands large in the front of the picture facing the viewer and points sideways across the picture at a small house with a blue roof standing in the distance, and two other children stand in the doorway of that faraway house. IMPORTANT: in scene 5 the two children are touching the house they point at, in scene 6 the pointing child is far from the house and the other two children are at the house. Every house must be whole and clearly visible, nothing cut off by the edge of its picture.
```

### 20. `u6/q_forest` `q_tall` `q_rhino` `q_family` — четыре сценки для вопросов yes / no

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with four separate small scenes in a two-by-two grid, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) a girl in a yellow summer dress hugging a small brown and white goat, both standing on a narrow path in a thick forest with tall trees all around them and more trees deep in the background — it must be obviously a forest and not a lawn or a garden; 2) a girl of about seven laughing out loud with her arms wide open, standing in a sunny meadow, clearly happy and cheerful — she must not look sad in any way. Row 2, left to right: 3) a boy of about eight walking along a path with a ginger CAT walking beside him, the cat seen from the side with pointed ears, long tail and whiskers so that it is obviously a cat — there is no dog anywhere in the picture; 4) a mother, a son and a daughter standing close together in a happy hug, all three smiling at the viewer — obviously one family.
```

## Пачка 3 — промпты 21–29

### 21. `u7/ac_basketball` `ac_reading` `ac_bike` `ac_sleeping` — что он делает, лист 1

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with four separate small scenes in a two-by-two grid, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) a BOY throwing an orange basketball up with both hands, the ball in the air above him; 2) a GIRL sitting and reading an open book, holding it in both hands and looking down at the pages. Row 2, left to right: 3) a BOY riding a blue bicycle, seen from the side, pedalling and smiling; 4) a BOY sleeping in a bed under a blue blanket, his eyes closed and his head on a pillow. IMPORTANT: scenes 1, 3 and 4 show a boy and scene 2 shows a girl.
```

### 22. `u7/ac_singing` `ac_flying` `ac_eating` `ac_jumping` — что он делает, лист 2

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with four separate small scenes in a two-by-two grid, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) a GIRL singing into a microphone, her mouth open wide and her eyes happy; 2) a bright pink and blue BIRD flying in a blue sky with its wings spread wide and two small white clouds behind it — no people in this scene. Row 2, left to right: 3) a BOY sitting at a table eating his lunch with a fork, a plate of food and a glass of juice in front of him; 4) a BOY jumping high into the air with both arms raised and both feet off the green grass. IMPORTANT: scene 1 shows a girl, scenes 3 and 4 show a boy, scene 2 shows only a bird.
```

### 23. `u7/tt_skate` `tt_football` `tt_heli` `tt_kite` — тест юнита 7, лист 1

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with four separate small scenes in a two-by-two grid, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) a boy riding a skateboard along a path, standing on the board with his arms out for balance, seen from the side; 2) four children in sports kit playing football on green grass, one of them kicking the ball towards a white goal. Row 2, left to right: 3) a red helicopter flying in a blue sky with two small white clouds, seen from the side with its rotor blades turning; 4) a boy running on green grass and flying a red diamond-shaped kite high on a string behind him. Any sports shirts in the scenes are plain and have no writing or numbers on them.
```

### 24. `u7/tt_bike` `tt_plane` `tt_book` + `u7/p_motorbike` — тест юнита 7, лист 2

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with four separate small scenes in a two-by-two grid, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) a boy in a blue helmet riding a green bicycle along a path, seen from the side; 2) a smiling pilot in a blue uniform and cap sitting in the cockpit of a small white aeroplane, seen from the side through the open cockpit window, the nose and wing of the plane visible. Row 2, left to right: 3) a boy sitting on a big stack of books and reading an open book on his knees; 4) a man in a black jacket and a red helmet riding a dark blue motorbike along a road, seen from the side, both wheels on the ground. The plane and the motorbike have no writing, letters or numbers anywhere on them.
```

### 25. `u8/i_ballet` `i_bike` `i_swim` — три картинки к диалогу про спорт

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with three separate small scenes in a row, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) a girl in a pink ballet dress and pink ballet shoes dancing on tiptoe with both arms raised above her head; 2) a bright pink bicycle with a basket on the handlebars, standing on its own on the grass, seen from the side, nobody riding it; 3) a boy in blue swimming goggles swimming in the bright blue water of a swimming pool, his head above the water and one arm reaching forward.
```

### 26. `u8/places3.webp` — три места для спорта

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with three separate small scenes in one single row, all the same size, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) a running TRACK — a red-orange athletics track with white lane lines curving round a green field, empty, seen from a low angle; 2) a tennis COURT — a green and blue hard tennis court with white lines and a net across the middle, empty, seen from the side; 3) a football PITCH — a green grass football field with white markings, a centre circle and a white goal with a net at the far end, empty. No people in any of the three scenes. The white lines are painted markings only and must not form any letters or numbers.
```

### 27. `u9/tt_grandma` `tt_riding` `tt_treehouse` `tt_bike` — тест юнита 9

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with four separate small scenes in a two-by-two grid, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) a girl of about nine visiting her grandmother — the two of them sitting side by side on a sofa, the grey-haired grandmother with glasses smiling and the girl showing her something in a photo album; 2) a girl in a riding helmet riding a brown horse at a walk across green grass, seen from the side. Row 2, left to right: 3) a wooden tree house with a small window and a rope ladder, built in the branches of a big green tree, nobody in it; 4) a boy in a blue helmet riding a red bicycle along a path, seen from the side.
```

### 28. `u9/n_bins` `n_nature` `n_path` `n_recycle` `n_rubbish` — природа и мусор

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with five separate pictures, three in the top row and two in the bottom row, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) RECYCLING BINS — three wheeled bins standing side by side, one green, one blue and one yellow, each with a round white three-arrow recycling symbol on the front and nothing else on it; 2) NATURAL ENVIRONMENT — a clean, beautiful piece of wild nature: a green meadow with a small blue river, a few leafy trees and hills behind, no buildings and no people; 3) A PATH — a narrow winding dirt path with grassy edges leading into a wood between tall trees, nobody on it. Row 2, left to right: 4) RECYCLE — a smiling boy in a red jumper dropping an empty plastic bottle into a green recycling bin with a white three-arrow recycling symbol on it; 5) RUBBISH — an untidy pile of litter on the ground: crumpled paper, an empty tin can, a plastic bottle, a banana skin and a cardboard box. IMPORTANT: the only symbol allowed anywhere on the sheet is the plain three-arrow recycling triangle; there are no words, letters or numbers on the bins or anywhere else.
```

### 29. `shared/yes_thumb_up.webp` и `shared/no_thumb_down.webp` — две служебные иконки

Только с «да» Анны: иконки общие для всех курсов, заменятся сразу везде.

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with two separate round icons in a row, on a plain flat pure white background, with wide empty white gaps between the items, every item complete and not touching any other item or the edge, no text, no letters, no labels, no numbers. Row 1, left to right: 1) a bright green circle with a friendly cartoon hand inside it giving a thumbs up, the thumb pointing straight up; 2) a bright red circle with the same friendly cartoon hand inside it giving a thumbs down, the thumb pointing straight down. Both circles are the same size, both hands are drawn in the same style and seen from the same side, and nothing sticks out past the edge of the circle.
```

---

## Что делаем, когда листы придут

1. Режем по строкам, как перечислено в промпте, обрезаем по краю предмета,
   проверяем долю не-белых пикселей вдоль каждой стороны.
2. Жмём в webp: карточка 600–800 px по большей стороне, сцена 1200–1600,
   качество 88–90. Мелкое не растягиваем.
3. Подписываем сами то, что генератору не доверяли: граммы в листе 12,
   вывески в листе 7.
4. Собираем из готовых картинок, без генерации: `u1/routine_six` (из картинок
   юнита 1 плюс нарисованные циферблаты), `u6/emotions5` (из `e_*`),
   `u8/sports6` (из `s_*`), `u5/my_things` и `u5/materials_five` (из листов 14
   и 15), `u2/test_likes` (из новых `u4/f_*`), `u2/speaking_pairs` (таблицей из
   картинок юнита 2). `u9/act_box` переносим в блок текстом и картинку убираем.
5. Показываем превью контактным листом по юнитам — в том размере, в каком
   картинку увидит ребёнок.
6. После «да» Анны кладём файлы в `media/sm2/…` **под теми же именами** —
   тогда блоки в базе править не нужно.

## Что ещё спросить у Анны

1. 🟥 Пятнадцать портретов `u6/hw5_q*` (ДЗ 5 блок 3) — перерисовывать их можно
   только вместе с текстом записи: ответы завязаны на очки, цвет волос и породу
   собаки. Нужно переслушать запись.
2. 🟥 `u5/family.webp` (ДЗ 5 блок 7) — иллюстрация учебника с пустыми
   табличками, привязана к настоящей записи `sm2_u5_hw5_b6.mp3`. Предлагаем
   оставить как есть.
3. 🟥 Две общие иконки 👍 / 👎 (промпт 29) меняются сразу во всех курсах.
4. 🟥 `u9/act_box.webp` — рамка со словами: переносим её текстом в блок?
