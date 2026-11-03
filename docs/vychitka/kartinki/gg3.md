# Go Getter 3 — вычитка картинок (03.11.2026)

Проход по решению Анны от 03.11.2026: начинаем вычитку картинок с Go Getter,
каждый курс делаем целиком в одном стиле. Здесь только осмотр и промпты —
**ничего не сгенерировано и ничего в базе не изменено**.

Контактные листы — `docs/vychitka/kartinki/gg3_listy/` (10 листов, картинки
показаны в том размере, в каком их видит ребёнок).

## Стиль курса

Go Getter 3 — **фотография**, и сцены, и места, и люди, и предметы:

```
clean photograph, sharp focus, natural colours, bright daylight
```

Сейчас курс почти целиком нарисован 3D-мультяшкой (дети с большими глазами,
мультяшные дома). Это и есть главная работа по курсу: заменить её фотографией.
Предметы, снятые как товар на белом (техника юнита 4, посуда юнита 6, корзина
и тележка юнита 2, зеркало, кран и комод юнита 7), от фотографии не отличаются —
их оставляем.

## Сводка

| | штук |
|---|---|
| всего файлов в `media/gg3/` | 111 |
| из них используются в базе | 110 |
| **не используется** | **1** (`u4/plug_socket.webp`) |
| оставляем как есть (предмет снят как товар) | 19 |
| **перерисовать** | **91** |

Причины перерисовки:

| причина | штук |
|---|---|
| разнобой в стиле: 3D-мультяшка там, где курс идёт фотографией | 84 |
| плоский вектор (пять видов транспорта юнита 0) | 5 |
| ключ: `plug_in` и `unplug` неразличимы | 2 |

Мелких картинок (меньше 300 px) в курсе нет ни одной. Самая мелкая сторона —
148 px у `u0/plane.webp`, но это узкий силуэт самолёта, по большей стороне 360.

Генерация — 91 картинка. При лимите Cloudflare ~50 в сутки это **два дня**.

## 🟥 ВОПРОСЫ И РЕШЕНИЯ

🟥 **1. Юнит 4, Unit 4 Test, блок 2 — `plug_in` и `unplug` различить нельзя.**
В блоке `match` обе картинки стоят рядом: на обеих ребёнок держит вилку возле
розетки, и по картинке не понять, вставляет он её или вынимает. Два пункта из
шести решаются угадыванием. Перерисовываем обе так, чтобы разница была видна с
первого взгляда: на `plug_in` вилка **в розетке**, на `unplug` — **вынута, между
штырями и розеткой зазор, провод висит**. Промпты ниже.

🟥 **2. Юнит 0, Unit 0 Test, блок 20 (диктант) — `bus.webp`.**
Ответ в ключе — `bus`, а нарисован **жёлтый американский школьный автобус**.
Ребёнок с большой вероятностью напишет `school bus`, и ответ не зачтётся.
Перерисовываем на обычный городской автобус. Там же `train.webp` — один тепловоз
без вагонов; на новой картинке будет состав.

🟥 **3. Юнит 0, пять видов транспорта — единственный плоский вектор в курсе.**
`bus`, `taxi`, `train`, `motorbike`, `plane` нарезаны из листа Анны и сделаны в
совсем другой манере, чем всё остальное. В диктанте это не мешает решать, но
выбивается. Перерисовываем вместе с пунктом 2.

🟥 **4. `media/gg3/u4/plug_socket.webp` ни в одном блоке не используется.**
Удалять не стали. Оставляем лежать или вычистить?

## Как заменяем

**Имена файлов не меняются.** Новая картинка кладётся на место старой по тому же
пути — блоки в базе править не надо.

Размер под хранение: карточка 600–800 px по большей стороне, сцена 1200–1600,
webp 88–90. Сейчас у карточек курса 300–400 px.

## Таблица по файлам

### final

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `scene_camping.webp` | 880×587 | ю9 · Final Test · б.4 (text)<br>ю9 · Final Test · б.5 (quiz) | перерисовать фотографией | рисованная сцена — курс идёт фотографией |

### u0

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `bus.webp` | 360×187 | ю0 · Unit 0 Test · б.20 (exact_input) | перерисовать | плоский вектор + ключ: нарисован жёлтый школьный автобус, а ответ «bus» |
| `motorbike.webp` | 360×224 | ю0 · Unit 0 Test · б.20 (exact_input) | перерисовать | плоский вектор 360 px — единственный такой набор в курсе |
| `plane.webp` | 360×148 | ю0 · Unit 0 Test · б.20 (exact_input) | перерисовать | плоский вектор 360 px — единственный такой набор в курсе |
| `taxi.webp` | 360×205 | ю0 · Unit 0 Test · б.20 (exact_input) | перерисовать | плоский вектор 360 px — единственный такой набор в курсе |
| `train.webp` | 360×201 | ю0 · Unit 0 Test · б.20 (exact_input) | перерисовать | плоский вектор 360 px — единственный такой набор в курсе |

### u1

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `clear_table.webp` | 310×382 | ю1 · Unit 1 Test · б.2 (match) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `empty_dishwasher.webp` | 313×400 | ю1 · Unit 1 Test · б.3 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `feed_dog.webp` | 348×400 | ю1 · Unit 1 Test · б.2 (match) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `hang_washing.webp` | 400×337 | ю1 · Unit 1 Test · б.2 (match) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `iron_tshirt.webp` | 353×376 | ю1 · Unit 1 Test · б.2 (match) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `load_dishwasher.webp` | 360×353 | ю1 · Unit 1 Test · б.3 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `make_bed.webp` | 385×374 | ю1 · Unit 1 Test · б.3 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `put_away_clothes.webp` | 266×400 | ю1 · Unit 1 Test · б.3 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `scene_chores.webp` | 880×587 | ю1 · Unit 1 Test · б.15 (speaking) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `set_table.webp` | 356×400 | ю1 · Unit 1 Test · б.3 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `take_rubbish.webp` | 364×361 | ю1 · Unit 1 Test · б.2 (match) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `vacuum_room.webp` | 331×343 | ю1 · Unit 1 Test · б.3 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `water_plants.webp` | 321×366 | ю1 · Unit 1 Test · б.2 (match)<br>ю9 · Final Test · б.6 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |

### u2

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `basket.webp` | 400×380 | ю2 · Unit 2 Test · б.2 (match) | оставляем | предмет снят как товар, от фотографии не отличается |
| `carry_shopping.webp` | 400×400 | ю2 · Unit 2 Test · б.3 (exact_input) | перерисовать фотографией | люди, сцены и места — курс идёт фотографией |
| `cashier.webp` | 400×393 | ю2 · Unit 2 Test · б.2 (match)<br>ю9 · Final Test · б.6 (exact_input) | перерисовать фотографией | люди, сцены и места — курс идёт фотографией |
| `chemists.webp` | 400×338 | ю2 · Unit 2 Test · б.3 (exact_input) | перерисовать фотографией | люди, сцены и места — курс идёт фотографией |
| `department_store.webp` | 400×394 | ю2 · Unit 2 Test · б.2 (match) | перерисовать фотографией | люди, сцены и места — курс идёт фотографией |
| `get_change.webp` | 395×400 | ю2 · Unit 2 Test · б.3 (exact_input) | перерисовать фотографией | люди, сцены и места — курс идёт фотографией |
| `greengrocers.webp` | 400×328 | ю2 · Unit 2 Test · б.2 (match) | перерисовать фотографией | люди, сцены и места — курс идёт фотографией |
| `list.webp` | 371×400 | ю2 · Unit 2 Test · б.2 (match) | перерисовать фотографией | люди, сцены и места — курс идёт фотографией |
| `pay_card.webp` | 400×363 | ю2 · Unit 2 Test · б.2 (match) | перерисовать фотографией | люди, сцены и места — курс идёт фотографией |
| `pay_cash.webp` | 400×380 | ю2 · Unit 2 Test · б.3 (exact_input) | перерисовать фотографией | люди, сцены и места — курс идёт фотографией |
| `queue.webp` | 400×329 | ю2 · Unit 2 Test · б.3 (exact_input) | перерисовать фотографией | люди, сцены и места — курс идёт фотографией |
| `scene_shop.webp` | 880×587 | ю2 · Unit 2 Test · б.15 (speaking) | перерисовать фотографией | люди, сцены и места — курс идёт фотографией |
| `trolley.webp` | 393×400 | ю2 · Unit 2 Test · б.3 (exact_input) | оставляем | предмет снят как товар, от фотографии не отличается |

### u3

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `beach.webp` | 373×373 | ю3 · Unit 3 Test · б.3 (exact_input) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `boat_trip.webp` | 372×324 | ю3 · Unit 3 Test · б.2 (match) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `camping.webp` | 382×361 | ю3 · Unit 3 Test · б.2 (match) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `cycling.webp` | 367×347 | ю3 · Unit 3 Test · б.2 (match) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `explore_city.webp` | 366×363 | ю3 · Unit 3 Test · б.2 (match) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `get_bored.webp` | 188×400 | ю3 · Unit 3 Test · б.3 (exact_input) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `get_lost.webp` | 206×400 | ю3 · Unit 3 Test · б.3 (exact_input) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `get_tired.webp` | 255×400 | ю3 · Unit 3 Test · б.3 (exact_input) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `guided_tour.webp` | 365×372 | ю3 · Unit 3 Test · б.3 (exact_input) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `hiking.webp` | 372×366 | ю3 · Unit 3 Test · б.2 (match) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `local_food.webp` | 367×363 | ю3 · Unit 3 Test · б.2 (match) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `scene_trip.webp` | 880×587 | ю3 · Unit 3 Test · б.14 (speaking) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `snorkelling.webp` | 370×381 | ю3 · Unit 3 Test · б.3 (exact_input) | перерисовать фотографией | люди и сцены — курс идёт фотографией |

### u4

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `blender.webp` | 197×361 | ю4 · Unit 4 Test · б.2 (match) | оставляем | предмет снят как товар, от фотографии не отличается |
| `games_console.webp` | 377×274 | ю4 · Unit 4 Test · б.3 (exact_input) | оставляем | предмет снят как товар, от фотографии не отличается |
| `hairdryer.webp` | 344×371 | ю4 · Unit 4 Test · б.3 (exact_input)<br>ю9 · Final Test · б.6 (exact_input) | оставляем | предмет снят как товар, от фотографии не отличается |
| `microwave.webp` | 381×228 | ю4 · Unit 4 Test · б.2 (match) | оставляем | предмет снят как товар, от фотографии не отличается |
| `plug_in.webp` | 400×385 | ю4 · Unit 4 Test · б.2 (match) | перерисовать | две почти одинаковые картинки с противоположными ключами — в тесте юнита 4 различить нельзя |
| `plug_socket.webp` | 365×315 | — | **не используется** | в базе ссылок нет |
| `remote.webp` | 280×344 | ю4 · Unit 4 Test · б.3 (exact_input) | оставляем | предмет снят как товар, от фотографии не отличается |
| `scene_hairdryer.webp` | 880×587 | ю4 · Unit 4 Test · б.15 (speaking) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `smart_tv.webp` | 372×288 | ю4 · Unit 4 Test · б.2 (match) | оставляем | предмет снят как товар, от фотографии не отличается |
| `toaster.webp` | 336×335 | ю4 · Unit 4 Test · б.3 (exact_input) | оставляем | предмет снят как товар, от фотографии не отличается |
| `turn_off.webp` | 400×342 | ю4 · Unit 4 Test · б.3 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `turn_on.webp` | 400×372 | ю4 · Unit 4 Test · б.3 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `unplug.webp` | 400×397 | ю4 · Unit 4 Test · б.2 (match) | перерисовать | две почти одинаковые картинки с противоположными ключами — в тесте юнита 4 различить нельзя |
| `usb_stick.webp` | 331×268 | ю4 · Unit 4 Test · б.2 (match) | оставляем | предмет снят как товар, от фотографии не отличается |

### u5

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `blocked_nose.webp` | 381×371 | ю5 · Unit 5 Test · б.2 (match) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `bruise.webp` | 254×400 | ю5 · Unit 5 Test · б.3 (exact_input)<br>ю9 · Final Test · б.6 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `cough.webp` | 318×395 | ю5 · Unit 5 Test · б.2 (match) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `earache.webp` | 360×400 | ю5 · Unit 5 Test · б.3 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `headache.webp` | 354×379 | ю5 · Unit 5 Test · б.2 (match) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `runny_nose.webp` | 325×400 | ю5 · Unit 5 Test · б.3 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `scene_ill.webp` | 880×587 | ю5 · Unit 5 Test · б.15 (speaking) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `sneeze.webp` | 309×400 | ю5 · Unit 5 Test · б.3 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `sore_throat.webp` | 340×381 | ю5 · Unit 5 Test · б.2 (match) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `stomachache.webp` | 302×400 | ю5 · Unit 5 Test · б.2 (match) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `temperature.webp` | 392×377 | ю5 · Unit 5 Test · б.2 (match) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `toothache.webp` | 280×400 | ю5 · Unit 5 Test · б.3 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |

### u6

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `bake.webp` | 348×400 | ю6 · Unit 6 Test · б.2 (match)<br>ю9 · Final Test · б.6 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `bowl.webp` | 400×259 | ю6 · Unit 6 Test · б.2 (match) | оставляем | предмет снят как товар, от фотографии не отличается |
| `cake_tin.webp` | 400×269 | ю6 · Unit 6 Test · б.3 (exact_input) | оставляем | предмет снят как товар, от фотографии не отличается |
| `chop.webp` | 400×370 | ю6 · Unit 6 Test · б.3 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `fork.webp` | 342×360 | ю6 · Unit 6 Test · б.2 (match) | оставляем | предмет снят как товар, от фотографии не отличается |
| `fry.webp` | 313×400 | ю6 · Unit 6 Test · б.2 (match) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `mix.webp` | 271×400 | ю6 · Unit 6 Test · б.2 (match) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `oven.webp` | 392×339 | ю6 · Unit 6 Test · б.3 (exact_input) | оставляем | предмет снят как товар, от фотографии не отличается |
| `peel.webp` | 343×400 | ю6 · Unit 6 Test · б.2 (match) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `pot.webp` | 400×295 | ю6 · Unit 6 Test · б.3 (exact_input) | оставляем | предмет снят как товар, от фотографии не отличается |
| `scene_cooking.webp` | 880×587 | ю6 · Unit 6 Test · б.15 (speaking) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `slice.webp` | 343×400 | ю6 · Unit 6 Test · б.3 (exact_input) | перерисовать фотографией | 3D-мультребёнок — курс идёт фотографией |
| `spoon.webp` | 377×397 | ю6 · Unit 6 Test · б.3 (exact_input) | оставляем | предмет снят как товар, от фотографии не отличается |

### u7

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `attic.webp` | 382×364 | ю7 · Unit 7 Test · б.2 (match) | перерисовать фотографией | дом и помещение — курс идёт фотографией |
| `balcony.webp` | 375×375 | ю7 · Unit 7 Test · б.2 (match) | перерисовать фотографией | дом и помещение — курс идёт фотографией |
| `basement.webp` | 373×362 | ю7 · Unit 7 Test · б.3 (exact_input) | перерисовать фотографией | дом и помещение — курс идёт фотографией |
| `block_of_flats.webp` | 400×362 | ю7 · Unit 7 Test · б.3 (exact_input) | перерисовать фотографией | дом и помещение — курс идёт фотографией |
| `cottage.webp` | 392×383 | ю9 · Final Test · б.6 (exact_input) | перерисовать фотографией | дом и помещение — курс идёт фотографией |
| `detached.webp` | 400×323 | ю7 · Unit 7 Test · б.2 (match) | перерисовать фотографией | дом и помещение — курс идёт фотографией |
| `drawer.webp` | 368×362 | ю7 · Unit 7 Test · б.3 (exact_input) | оставляем | предмет снят как товар, от фотографии не отличается |
| `lift.webp` | 279×364 | ю7 · Unit 7 Test · б.2 (match) | перерисовать фотографией | дом и помещение — курс идёт фотографией |
| `mirror.webp` | 222×379 | ю7 · Unit 7 Test · б.3 (exact_input) | оставляем | предмет снят как товар, от фотографии не отличается |
| `scene_moving.webp` | 880×587 | ю7 · Unit 7 Test · б.16 (speaking) | перерисовать фотографией | дом и помещение — курс идёт фотографией |
| `semi_detached.webp` | 400×305 | ю7 · Unit 7 Test · б.3 (exact_input) | перерисовать фотографией | дом и помещение — курс идёт фотографией |
| `stairs.webp` | 378×380 | ю7 · Unit 7 Test · б.2 (match) | перерисовать фотографией | дом и помещение — курс идёт фотографией |
| `tap.webp` | 396×386 | ю7 · Unit 7 Test · б.3 (exact_input) | оставляем | предмет снят как товар, от фотографии не отличается |
| `terraced.webp` | 400×266 | ю7 · Unit 7 Test · б.2 (match) | перерисовать фотографией | дом и помещение — курс идёт фотографией |

### u8

| файл | размер | где используется | вердикт | что не так |
|---|---|---|---|---|
| `arrive_on_time.webp` | 400×398 | ю8 · Unit 8 Test · б.3 (exact_input) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `be_doctor.webp` | 217×400 | ю8 · Unit 8 Test · б.3 (exact_input) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `be_famous.webp` | 400×392 | ю8 · Unit 8 Test · б.3 (exact_input) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `be_rich.webp` | 400×390 | ю8 · Unit 8 Test · б.2 (match) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `call.webp` | 206×400 | ю8 · Unit 8 Test · б.3 (exact_input) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `foreign_language.webp` | 397×400 | ю8 · Unit 8 Test · б.2 (match) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `have_family.webp` | 365×400 | ю8 · Unit 8 Test · б.2 (match) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `hug.webp` | 300×400 | ю8 · Unit 8 Test · б.2 (match) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `invite.webp` | 400×341 | ю8 · Unit 8 Test · б.3 (exact_input) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `learn_drive.webp` | 396×400 | ю8 · Unit 8 Test · б.3 (exact_input) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `scene_greeting.webp` | 880×587 | ю8 · Unit 8 Test · б.15 (speaking) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `shake_hands.webp` | 359×400 | ю8 · Unit 8 Test · б.2 (match)<br>ю9 · Final Test · б.6 (exact_input) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
| `wait_turn.webp` | 400×323 | ю8 · Unit 8 Test · б.2 (match) | перерисовать фотографией | люди и сцены — курс идёт фотографией |
## Не перерисовываем — и почему

**19 предметов, снятых как товар на белом.** Их уже нельзя отличить от
фотографии, менять не на что:

- юнит 2: `basket`, `trolley`;
- юнит 4: `blender`, `games_console`, `hairdryer`, `microwave`, `remote`,
  `smart_tv`, `toaster`, `usb_stick`;
- юнит 6: `bowl`, `cake_tin`, `fork`, `oven`, `pot`, `spoon`;
- юнит 7: `drawer`, `mirror`, `tap`.

Героев курса в Go Getter 3 в картинках нет — генерировать нечего, ограничение
«героев не генерируем» здесь ни на что не влияет.

Фотографий `photo_*` в этом курсе нет: сегодняшняя переделка по учебнику
касалась только Go Getter 2.

## Промпты

Один предмет — один промпт, сеток не просим. Каждый промпт — цельный блок,
строка стиля уже внутри, копируется одним нажатием.

### final

**`media/gg3/final/scene_camping.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a family camping by a mountain lake at sunset: a tent, a campfire, a man playing a guitar, a woman and children sitting on logs, a boy fishing from the shore. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u0

**`media/gg3/u0/bus.webp`** — диктант, ответ «bus» — нужен обычный городской автобус, НЕ жёлтый школьный, иначе ребёнок пишет school bus

```
clean photograph, sharp focus, natural colours, bright daylight. an ordinary modern red city bus seen from the front and side, doors closed. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u0/taxi.webp`** — диктант, ответ «taxi»

```
clean photograph, sharp focus, natural colours, bright daylight. a yellow taxi car with a taxi sign on the roof, seen from the front and side. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u0/train.webp`** — диктант, ответ «train» — нужен состав с вагонами, а не один тепловоз

```
clean photograph, sharp focus, natural colours, bright daylight. a modern passenger train with a locomotive and two carriages on a track, seen from the front and side. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u0/motorbike.webp`** — диктант, ответ «motorbike»

```
clean photograph, sharp focus, natural colours, bright daylight. a modern motorbike seen from the side. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u0/plane.webp`** — диктант, ответ «plane»

```
clean photograph, sharp focus, natural colours, bright daylight. a white passenger aeroplane in flight seen from the front and side. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u1

**`media/gg3/u1/clear_table.webp`** — пара к set_table — здесь посуду УНОСЯТ со стола

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten carrying a stack of dirty plates away from a dining table. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u1/empty_dishwasher.webp`** — пара к load_dishwasher — здесь посуду ДОСТАЮТ

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten taking a clean plate out of an open dishwasher and holding it up. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u1/feed_dog.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten pouring dry dog food from a packet into a red bowl while a golden dog waits beside her. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u1/hang_washing.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten pegging a wet T-shirt onto a washing line, a laundry basket at her feet. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u1/iron_tshirt.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten ironing a white T-shirt on an ironing board. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u1/load_dishwasher.webp`** — пара к empty_dishwasher — здесь посуду СТАВЯТ внутрь

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten putting a dirty plate into an open dishwasher. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u1/make_bed.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten making his bed, pulling a blue duvet straight over the mattress. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u1/put_away_clothes.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten putting folded clothes onto a shelf inside an open wardrobe. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u1/set_table.webp`** — пара к clear_table — здесь стол НАКРЫВАЮТ

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten laying a table: putting a plate down beside knives and forks already on the table. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u1/take_rubbish.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten dropping a black rubbish bag into a green wheelie bin. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u1/vacuum_room.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten vacuuming a carpet with an upright vacuum cleaner. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u1/water_plants.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten watering potted flowers with a green watering can. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u1/scene_chores.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a family doing housework together at home: the mother sweeping the floor, the father washing up at the sink, a girl dusting a shelf, a dog watching. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u2

**`media/gg3/u2/carry_shopping.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a man carrying several full shopping bags in both hands, walking, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u2/cashier.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a woman cashier in a green apron at a supermarket checkout scanning a red pepper, fruit and vegetables on the belt. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u2/chemists.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the front of a chemist’s shop with a green cross sign and a window display of medicine boxes. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u2/department_store.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the front of a large department store building with big glass display windows on several floors. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u2/get_change.webp`** — ключ «get change» — видно, что сдачу ОТДАЮТ покупателю

```
clean photograph, sharp focus, natural colours, bright daylight. a cashier handing coins and a receipt back across the counter into a customer’s open hand. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u2/greengrocers.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the front of a greengrocer’s shop with wooden crates of fruit and vegetables displayed under a green striped awning. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u2/list.webp`** — без читаемых слов — только строчки

```
clean photograph, sharp focus, natural colours, bright daylight. a small spiral notepad lying on a table with a handwritten shopping list on it and a pencil beside it. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u2/pay_card.webp`** — пара к pay_cash — здесь платят КАРТОЙ

```
clean photograph, sharp focus, natural colours, bright daylight. a customer holding a bank card against a card reader at a shop counter, the cashier behind the till. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u2/pay_cash.webp`** — пара к pay_card — здесь платят НАЛИЧНЫМИ

```
clean photograph, sharp focus, natural colours, bright daylight. a customer handing banknotes across the counter to a cashier at a shop till. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u2/queue.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. five people standing one behind another in a queue at a supermarket checkout, baskets and a trolley in their hands. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u2/scene_shop.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a busy supermarket: shoppers with trolleys and baskets along the fruit and vegetable aisle, a cashier at the till in the background. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u3

**`media/gg3/u3/beach.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a family walking along a sandy beach with beach bags, a ball and rolled towels, turquoise sea behind them. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u3/boat_trip.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a family of four on a small motorboat speeding across a blue lake, mountains behind. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u3/camping.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a family sitting round a campfire beside an orange tent in a forest clearing, mountains in the distance. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u3/cycling.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about twelve in a helmet cycling along a country road between olive trees, a hill town behind. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u3/explore_city.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. two tourists with backpacks standing in an old European city square with a map, a cathedral dome behind them. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u3/get_bored.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten standing with his arms down and yawning, looking thoroughly bored, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u3/get_lost.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten with a backpack holding an open map upside down and looking around, confused, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u3/get_tired.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten sitting on his rucksack, wiping his forehead, looking exhausted, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u3/guided_tour.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a tour guide with a raised red flag leading a small group of tourists past a grand old building. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u3/hiking.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. two hikers with big rucksacks and walking poles climbing a stony mountain path, snowy peaks behind. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u3/local_food.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about eleven eating noodles from a bowl at a busy street food market stall, the stallholder behind the counter. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u3/snorkelling.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl snorkelling underwater in a clear blue sea above a coral reef with bright tropical fish. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u3/scene_trip.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a family hiking along a stony path above a mountain lake, pine forest and snowy peaks around them. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u4

**`media/gg3/u4/plug_in.webp`** — ключ «plug in» — вилка ВСТАВЛЕНА в розетку, пара к unplug должна отличаться с первого взгляда

```
clean photograph, sharp focus, natural colours, bright daylight. a hand pushing a plug firmly INTO a wall socket, the plug pins already inside the socket, the cable going to a laptop. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u4/unplug.webp`** — ключ «unplug» — вилка ВЫНУТА и висит в воздухе; сейчас эта картинка не отличается от plug_in

```
clean photograph, sharp focus, natural colours, bright daylight. a hand pulling a plug OUT of a wall socket, the plug already clear of the socket with a visible gap between the pins and the socket holes, the cable hanging loose. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u4/turn_on.webp`** — пара к turn_off — свет ВКЛЮЧЁН

```
clean photograph, sharp focus, natural colours, bright daylight. a hand switching on a table lamp, the lamp clearly lit and glowing. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u4/turn_off.webp`** — пара к turn_on — экран ВЫКЛЮЧЕН

```
clean photograph, sharp focus, natural colours, bright daylight. a hand pointing a remote control at a television whose screen is completely black and dark. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u4/scene_hairdryer.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl drying her hair with a hairdryer in front of a bathroom mirror while her mother watches. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u5

**`media/gg3/u5/blocked_nose.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten holding a tissue to her blocked nose, looking unwell, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u5/bruise.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten sitting on the floor looking at a large purple bruise on his knee. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u5/cough.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten coughing into his elbow, eyes shut, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u5/earache.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten holding her hand to her ear with a pained expression, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u5/headache.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten pressing both hands to his temples with his eyes closed, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u5/runny_nose.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten wiping her runny nose with a tissue, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u5/sneeze.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten sneezing into a tissue held in both hands, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u5/sore_throat.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten holding his hand to the front of his throat with a pained expression, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u5/stomachache.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten holding both hands on her stomach and bending forward slightly, upper body. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u5/temperature.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten lying in bed under a blanket with a digital thermometer in her mouth. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u5/toothache.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten holding his hand to a swollen red cheek with a pained expression, head and shoulders. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u5/scene_ill.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a child lying ill in bed in a dim bedroom while the mother sits beside the bed holding a mug, medicine and a glass of water on the bedside table. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u6

**`media/gg3/u6/bake.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten in oven gloves taking a baked cake out of an open oven. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u6/chop.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten chopping carrots with a knife on a wooden board, slices already cut. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u6/fry.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten frying two eggs in a frying pan on a hob, spatula in hand. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u6/mix.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl about ten whisking yellow batter in a glass bowl with a hand whisk. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u6/peel.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten peeling a potato with a peeler, peelings falling onto the board. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u6/slice.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten slicing a loaf of bread with a bread knife on a wooden board. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u6/scene_cooking.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a woman cooking in a bright home kitchen: chopping vegetables on a board, a pot on the hob and a cake tin on the worktop beside her. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u7

**`media/gg3/u7/attic.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the inside of a loft attic with sloping wooden beams, a skylight and cardboard boxes and an old trunk stored there. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u7/balcony.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a small balcony on the front of a house with an iron railing and pots of red flowers on it. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u7/basement.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the inside of a house basement: concrete walls, shelves with boxes and jars, a washing machine. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u7/block_of_flats.webp`** — ряд «виды жилья» — здесь многоквартирный дом

```
clean photograph, sharp focus, natural colours, bright daylight. a modern five-storey block of flats with balconies on every floor, seen from the street. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u7/cottage.webp`** — ряд «виды жилья» — отдельный деревенский дом

```
clean photograph, sharp focus, natural colours, bright daylight. an old stone cottage with a thatched roof and a flower garden in front. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u7/detached.webp`** — ряд «виды жилья» — дом стоит ОТДЕЛЬНО

```
clean photograph, sharp focus, natural colours, bright daylight. one detached family house standing alone in its own garden, no other house touching it. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u7/semi_detached.webp`** — ряд «виды жилья» — РОВНО два дома, соединённые одной стеной

```
clean photograph, sharp focus, natural colours, bright daylight. a pair of semi-detached houses: two mirror-image houses joined together along one wall, each with its own front door. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u7/terraced.webp`** — ряд «виды жилья» — длинный ряд сросшихся домов

```
clean photograph, sharp focus, natural colours, bright daylight. a long terrace of identical brick houses joined in a row, each with its own front door of a different colour. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u7/lift.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. the open doors of a lift inside a building, the empty lit cabin visible inside. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u7/stairs.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a wooden staircase with a banister going up inside a house. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u7/scene_moving.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a family moving house: a removal van at the kerb, the parents and two children carrying cardboard boxes up the path to the front door. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```


### u8

**`media/gg3/u8/arrive_on_time.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a schoolgirl with a backpack walking in through the school door, a large clock above the entrance showing on the hour. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u8/be_doctor.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a young woman doctor in a white coat with a stethoscope round her neck, arms folded, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u8/be_famous.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a woman in a long evening gown waving on a red carpet with camera flashes around her. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u8/be_rich.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a man in a suit standing beside an expensive red sports car with his arms folded. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u8/call.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a boy about ten standing and talking on a mobile phone held to his ear, full figure. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u8/foreign_language.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl sitting cross-legged with an open book, the flags of Britain, France, Germany, Spain, Italy and Japan floating around her. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u8/have_family.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a family of four — mother, father, a boy and a girl — sitting close together and smiling, full figures. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u8/hug.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. two boys about ten hugging each other, full figures. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u8/invite.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a girl handing a party invitation card to another girl, both full figures. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u8/learn_drive.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a teenager at the wheel of a car during a driving lesson with an instructor in the passenger seat, both seen through the windscreen. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u8/shake_hands.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. a young man and an older man shaking hands, full figures. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u8/wait_turn.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. four children standing in a patient queue at the steps of a playground slide while one child slides down. The whole subject centred in the frame with generous empty margin on every side, nothing cut by the edge. Plain flat pure white background, no shadow on the background, no floor, no furniture and no props except the ones named. No text, no letters, no labels, no numbers, no watermark, no logo.
```

**`media/gg3/u8/scene_greeting.webp`**

```
clean photograph, sharp focus, natural colours, bright daylight. two schoolboys hugging each other in greeting outside a school building while other pupils walk past. Wide horizontal shot, the whole scene inside the frame, nothing important cut by the edge. No text, no letters, no labels, no numbers, no watermark, no logo.
```
