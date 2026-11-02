# Wow Dragon 1 — вычитка картинок, план перерисовки

Собрано 02.11.2026 по базе (`classroom_courses.slug = 'wow-dragon-1'`) и по файлам
в `media/wow-dragon-1/`. Генерировать картинки не нужно: ниже список того, что
плохо, и готовые промпты для методиста.

## Сколько всего

| что | сколько |
|---|---|
| картинок в заданиях (все блоки, кроме `text`, `video`, `embed`) | **587** |
| из них в `media/wow-dragon-1/` | 583 — `legacy/` 529, `new/` 43, `fix/` 11 |
| карточки букв `fix/hw59_letter_Bb`, `fix/hw67_letter_Tt` | 2 |
| общие 👍/👎 из `media/shared/` | 2 |
| файлов в `media/wow-dragon-1/` всего | 691 (`legacy/` 604, `new/` 68, `fix/` 19) |
| **мельче 300 px по большей стороне — в заданиях** | **110** (все из `legacy/`) |
| мельче 300 px на диске, но в заданиях не стоят | 16 |
| 300–400 px в заданиях | 213 |
| медиана размера используемой картинки | 391 px |
| битых ссылок (файла нет на диске) | **0** |

Четыре картинки Дракоши из `media/wow-dragon-1/legacy/` стоят ещё и в Wow Dragon 2
(`03073aaae67a`, `30f787178c40`, `7801b60b6af1`, `ce6f5fe872e5`, юнит 300, ДЗ 57 и 62) —
если их трогать, поменяется и второй курс. Мы их не трогаем: это герой.

## Что это за 110 мелких картинок

| группа | штук | что делаем |
|---|---|---|
| тени предметов для игры «найди тень» | 11 | **не трогаем** — это материал задания |
| плоские геометрические фигуры и цветные плашки (круг, квадрат, треугольник в 8 цветах) | 21 | **рисуем сами скриптом** — это чистая векторная заливка, промпт не нужен |
| цифры 1–5 | 5 | **рисуем сами скриптом** — в промпте нельзя просить цифры («no numbers») |
| остальные предметы | 73 | из них 16 мельче 250 px — перерисовываем; 57 в диапазоне 250–299 px оставляем |

Курс рисован ровно, одним плоским клипартом с тёмно-фиолетовым контуром. Это не
SM0: мыла почти нет, размеры 210–299 px, по правилу «не больше чем в полтора раза»
такая картинка доживает до 400 px на экране. Поэтому **сплошной перерисовки курс
не требует** — перерисовываем 39 позиций: самые мелкие (меньше 250 px), обрезанные
кадры, чужой стиль и три места, где картинка спорит с ключом.

## Чего не трогаем

* **Кадры историй и герой.** `new/dragon_*.webp` (15 файлов), `new/scene_race`,
  `new/scene_competition` — Дракоша и сцены из учебника. Генерация героя даст не того героя.
* **Карточки букв.** `fix/hw59_letter_Bb`, `fix/hw67_letter_Tt`, `fix/hw59_u_lower`,
  `new/lc_b`, `new/lc_d`, `new/lc_q`, `new/lc_s`, `new/lc_u` — по ним сверяются ответы.
* **Тени** (11 файлов: `0134972ef497`, `05819031b952`, `1c849f33f572`, `1f510c5a2aeb`,
  `26f97ddcd3d2`, `469f0eb25aba`, `628242b26e52`, `6528d9a7cdc6`, `962291dbe099`,
  `cb8d115375c0`, `e76fc3646b66`). Но: если перерисовываем предмет, у которого есть
  тень (джинсы, кукла, кеды, юбка, футболка, книга, круг, квадрат, треугольник),
  **тень надо пересобрать из новой картинки** — заливкой силуэта одним цветом,
  скриптом, не промптом. Иначе в игре «найди тень» ответ перестанет сходиться.
* **Широкие листы из `fix/`** (850–1250 px) — они крупные и чёткие.
* **Карточки лексики, стоящие не вторым блоком**, — устройство Wow Dragon,
  решение Анны от 02.11.2026.

## 🟥 Картинка спорит с ключом — три места

1. **ДЗ 18, блок 6** (юнит 1, «Сколько их? Посчитай.»): на картинке `0f1443c8387f`
   один торт, но на нём **три свечи**, а верный ответ — «one». Ребёнок считает свечи
   и отвечает «three». Перерисовать торт без свечей (промпт 8).
2. **ДЗ 65 блок 6 и ДЗ 68 блок 4** (юнит 3, «Где это?»): верный ответ «next to»,
   а на `3634ef027da5` ягоды и гнездо нарисованы порознь, между ними белый зазор —
   это не «рядом», а просто два предмета. Остальные картинки серии («eagle in the
   nest», «bear under the tree», «honey in the tree») — полноценные сцены.
   Перерисовать одной сценой (промпт 7).
3. **ДЗ 78, блок 7** (юнит 3, match «swing»): `aaae7d559703` и `f88d4a9d9074` —
   обрезанные кадры, рама качелей уходит за край. Рядом в том же юните стоит целая
   картинка качелей, разнобой виден. Перерисовать (промпт 5).

Проверены и оказались в порядке: счёт окон (ДЗ 15 блок 6 — 1/2/3 окна, ряд читается),
счёт колёс (ДЗ 70 блок 6), счёт карандашей (ДЗ 78 блок 9), игра «найди тень»
(ДЗ 33/37/45, блок 41 — тёмные силуэты так и задуманы).

## Что перерисовываем — таблица

| файл | размер | где стоит | что не так |
|---|---|---|---|
| `legacy/9bee3e0930bc.webp` | 114×220 | u2 HW48 b21 (flashcards), u2 HW48 b31 (quiz), u2 HW48 b41 (match), u2 HW50 b91 (quiz) … всего 5 | цифра 1 — 114 px, самая мелкая картинка курса |
| `legacy/e3041aed900e.webp` | 173×215 | u2 HW48 b21 (flashcards), u2 HW48 b31 (quiz), u2 HW50 b91 (quiz), u2 HW53 b61 (quiz) | цифра 2 — 173 px |
| `legacy/85912d0f7859.webp` | 158×220 | u2 HW48 b21 (flashcards), u2 HW48 b31 (quiz), u2 HW48 b41 (match), u2 HW48 b81 (quiz) … всего 7 | цифра 3 — 158 px |
| `legacy/be10df0ec183.webp` | 180×220 | u2 HW48 b21 (flashcards), u2 HW48 b31 (quiz), u2 HW48 b81 (quiz), u2 HW53 b61 (quiz) … всего 5 | цифра 4 — 180 px |
| `legacy/404cfc671a52.webp` | 170×225 | u2 HW48 b21 (flashcards), u2 HW48 b31 (quiz), u2 HW48 b41 (match), u2 HW48 b81 (quiz) … всего 6 | цифра 5 — 170 px |
| `legacy/8221aa0ede83.webp` | 145×206 | u3 HW78 b7 (match) | лодка — 145 px, на карточке мыло |
| `legacy/39b21efb5a5e.webp` | 146×206 | u3 HW78 b7 (match) | лодка — 146 px, дубль предыдущей |
| `legacy/bcdd7348842c.webp` | 288×206 | u3 HW66 b8 (quiz), u3 HW69 b4 (quiz), u3 HW70 b10 (quiz), u3 HW77 b6 (quiz) | красная лодка — перерисовать вместе с синими, иначе ряд разностильный |
| `legacy/005475a05920.webp` | 178×225 | u3 HW78 b7 (match), u3 HW79 b3 (match) | автобус — 178 px |
| `legacy/3a88394e72fa.webp` | 178×225 | u3 HW78 b7 (match), u3 HW79 b3 (match) | автобус — 178 px, дубль предыдущего |
| `legacy/aaae7d559703.webp` | 142×282 | u3 HW78 b7 (match) | качели — 142 px и рама обрезана по краям кадра |
| `legacy/f88d4a9d9074.webp` | 142×282 | u3 HW78 b7 (match) | качели — 142 px, рама обрезана |
| `legacy/7c2ca990d569.webp` | 284×282 | u3 HW74 b3 (flashcards), u3 HW74 b4 (quiz), u3 HW74 b9 (quiz), u3 HW74 b10 (quiz) … всего 15 | качели целиком — перерисовать вместе с двумя обрезанными |
| `legacy/5572a198f077.webp` | 271×220 | u3 HW67 b3 (flashcards), u3 HW67 b4 (quiz), u3 HW69 b9 (quiz), u3 HW70 b3 (quiz) … всего 19 | розовый трицикл — перерисовать вместе со «старым» |
| `legacy/b4de6c439dbc.webp` | 272×179 | u3 HW69 b9 (quiz), u3 HW70 b3 (quiz), u3 HW71 b3 (flashcards), u3 HW71 b5 (sort) … всего 7 | зелёный трицикл — то же |
| `legacy/1e254d97c974.webp` | 287×180 | u3 HW69 b9 (quiz), u3 HW70 b3 (quiz) | «старый» трицикл — выбивается из стиля: серо-коричневый фотореализм |
| `legacy/1060de4cadd6.webp` | 218×215 | u3 HW70 b9 (match) | розовое колесо — 218 px |
| `legacy/883d4d3f5ea2.webp` | 218×215 | u3 HW70 b9 (match) | зелёное колесо — 218 px |
| `legacy/47bf49ee7638.webp` | 215×221 | u3 HW70 b9 (match) | оранжевое колесо — 215 px |
| `legacy/9658e145bfaf.webp` | 218×221 | u3 HW70 b6 (quiz) | одно синее колесо — 218 px, ключ «one» |
| `legacy/99d32fb0d5e1.webp` | 400×192 | u3 HW70 b6 (quiz) | два колеса — перерисовать вместе, ключ «two» |
| `legacy/d661f6d1f6dc.webp` | 400×126 | u3 HW70 b6 (quiz) | три колеса — ключ «three» |
| `legacy/92a7cd9b7083.webp` | 229×245 | u3 HW65 b3 (flashcards), u3 HW65 b4 (quiz), u3 HW65 b7 (match), u3 HW68 b5 (match) … всего 6 | красные ягоды — 229 px |
| `legacy/39138a8f35bf.webp` | 226×245 | u3 HW65 b7 (match) | синие ягоды — 226 px |
| `legacy/cc7396a1580e.webp` | 223×245 | u3 HW65 b7 (match) | жёлтые ягоды — 223 px |
| `legacy/3634ef027da5.webp` | 296×151 | u3 HW65 b6 (quiz), u3 HW68 b4 (quiz), u3 HW80 b10 (quiz) | КЛЮЧ: ответ «next to», а на картинке ягоды и гнездо порознь, между ними белый зазор |
| `legacy/0f1443c8387f.webp` | 257×280 | u1 HW18 b6 (quiz) | КЛЮЧ: ответ «one», а на торте три свечи — ребёнок считает свечи |
| `legacy/7fffc526df4e.webp` | 400×190 | u1 HW18 b6 (quiz) | две пиццы — перерисовать вместе с тортом, ключ «two» |
| `legacy/be54adde645b.webp` | 400×177 | u1 HW18 b6 (quiz) | три мороженых — ключ «three» |
| `legacy/c7fa6f00b265.webp` | 212×274 | u2 HW37 b21 (flashcards), u2 HW37 b31 (quiz), u2 HW37 b41 (match), u2 HW37 b51 (quiz) … всего 29 | джинсы — 212 px, карточка лексики юнита 2 |
| `legacy/823ba47ef7eb.webp` | 249×275 | u2 HW45 b21 (flashcards), u2 HW45 b31 (quiz), u2 HW45 b41 (match), u2 HW45 b51 (quiz) … всего 11 | кукла — 249 px, карточка лексики |
| `legacy/a7aaad30331d.webp` | 267×203 | u2 HW37 b31 (quiz), u2 HW38 b21 (flashcards), u2 HW38 b31 (quiz), u2 HW38 b51 (quiz) … всего 23 | кеды — 273×203, карточка лексики |
| `legacy/c5b5fa0f3242.webp` | 278×198 | u2 HW37 b31 (quiz), u2 HW37 b61 (sort), u2 HW37 b71 (quiz), u2 HW37 b81 (quiz) … всего 21 | юбка — 278×198, карточка лексики |
| `legacy/f91ea8f7e69f.webp` | 273×203 | u2 HW37 b51 (quiz), u2 HW38 b61 (sort), u2 HW39 b21 (flashcards), u2 HW39 b31 (quiz) … всего 14 | жёлтые кеды — 273×203, карточка лексики |
| `legacy/0099c0ea54f7.webp` | 278×197 | u2 HW37 b21 (flashcards), u2 HW37 b31 (quiz), u2 HW37 b41 (match), u2 HW37 b61 (sort) … всего 13 | фиолетовая юбка — 278×197, карточка лексики |
| `legacy/06dbc844112c.webp` | 188×244 | u2 HW49 b91 (sequence) | следы лап — 188 px |
| `legacy/86466d361dc9.webp` | 235×214 | u2 HW50 b91 (quiz), u2 HW51 b41 (sequence), u2 HW51 b91 (speaking) | фигуры из бумаги — 235 px, по ней считают предметы |
| `legacy/e893a6b7b83a.webp` | 231×288 | u3 HW78 b4 (flashcards), u3 HW78 b6 (quiz), u3 HW78 b8 (match), u3 HW78 b10 (sequence) | клей-карандаш — 231 px |
| `legacy/f48cc750447c.webp` | 268×220 | u2 HW47 b21 (flashcards) | палитра — 268×220 |

Плюс **скриптом, без промпта**: цифры 1–5 (`9bee3e0930bc`, `e3041aed900e`,
`85912d0f7859`, `be10df0ec183`, `404cfc671a52`) и 21 геометрическая фигура —
круги, квадраты и треугольники в цветах юнита 2 (`0858978ee8ad`, `0cf8eda10681`,
`17997560fe4f`, `1eae7f05e7c4`, `201dc41adce1`, `27e2a65e1816`, `2d14ed0bf4ef`,
`2da77e88dfa2`, `47bb72934615`, `55ed5736b76d`, `5b3e230745ed`, `7c51f5af1f25`,
`7e49ed7d639f`, `947c77d584b8`, `9fdc61cc8960`, `c8e4e04f9d99`, `cd0c2f33438d`,
`df8f6d02ecbe`, `e76d8b6c306f`, `f757c42af477`, `fa75825f9f11`). Цвет и форма —
это ответ задания, поэтому цвета оставляем ровно те же.

**Восемь файлов из этого списка лежат такими же копиями и в Wow Dragon 2** —
`9bee3e0930bc`, `85912d0f7859`, `404cfc671a52` (цифры 1, 3, 5), `5572a198f077`
(розовый трицикл), `1e254d97c974` («старый» трицикл), `3634ef027da5` (ягода и
гнездо), `c7fa6f00b265` (джинсы), `e893a6b7b83a` (клей-карандаш). Новую картинку
кладём в обе папки, иначе курсы разойдутся по стилю. План второго курса —
`builds/wd2/kartinki_plan.md`.

## Промпты 1–10

Каждый промпт — цельный блок, копируется одним нажатием. Лист режем мы.
Хранить с запасом: карточка 600–800 px по большей стороне, сцена 1200–1600, webp 88–90.


**1. Колёса в четырёх цветах**

Заменяет: 1060de4cadd6 (розовое), 883d4d3f5ea2 (зелёное), 47bf49ee7638 (оранжевое), 9658e145bfaf (синее)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with four separate toy cart wheels, arranged in a single row, all four drawn at exactly the same size and from exactly the same straight side-on angle, each wheel a thick dark grey rubber tyre with eight straight spokes and a round hub in the middle, the spokes and the hub painted in the colour named below while the tyre stays dark grey. Row 1, left to right: a wheel with bright sky-blue spokes and hub, a wheel with bright pink spokes and hub, a wheel with bright green spokes and hub, a wheel with bright orange spokes and hub. The colour of the spokes is what the child has to name, so keep the four colours clearly different and do not tint the grey tyre. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```

**2. Счёт колёс: одно, два, три**

Заменяет: 99d32fb0d5e1 (два колеса), d661f6d1f6dc (три колеса). Картинку «одно колесо»
(`9658e145bfaf`) берём из листа 1 — она уже синяя, пересоздавать не нужно

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with three separate groups of identical toy cart wheels, every wheel a thick dark grey rubber tyre with eight straight sky-blue spokes and a round hub, all wheels drawn at the same size and from the same straight side-on angle. Row 1, left to right: a group of exactly one wheel, a group of exactly two wheels standing side by side with a small gap between them, a group of exactly three wheels standing side by side in a straight line with small gaps between them. The number of wheels in each group is the answer to the task, so draw exactly one, exactly two and exactly three, never more and never fewer, and keep the three groups far apart from each other. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```

**3. Лодки и автобусы**

Заменяет: 8221aa0ede83 и 39b21efb5a5e (две одинаковые синие лодки — новая синяя лодка
кладётся в оба файла), bcdd7348842c (красная лодка), 005475a05920 и 3a88394e72fa
(два автобуса, на листе они с разных ракурсов)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with four separate vehicles for small children, all drawn from a straight side-on angle and at a similar size. Row 1, left to right: a small bright blue wooden rowing boat with two light brown oars resting across it, a small bright red wooden rowing boat with two light brown oars resting across it. Row 2, left to right: a cheerful yellow city bus with large light blue windows, black wheels and a door on the side, a cheerful yellow school bus seen slightly from the front corner with large light blue windows and black wheels. The colour of each boat is the answer to the task, so keep one boat clearly blue and the other clearly red, and keep both buses yellow. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```

**4. Трициклы: розовый, зелёный, старый**

Заменяет: 5572a198f077 (розовый), b4de6c439dbc (зелёный), 1e254d97c974 (старый)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with three separate tricycles-for-three (a long bike frame with three saddles, three sets of handlebars and two wheels), all drawn from the same straight side-on angle and at the same size. Row 1, left to right: a brand new shiny bright pink tricycle-for-three with sky-blue wheels, a brand new shiny bright green tricycle-for-three with orange wheels, an old worn-out tricycle-for-three painted dull grey-brown with rusty patches, a bent handlebar and a dusty cracked saddle, clearly old but drawn in exactly the same cartoon style and with the same thick outline as the other two. The child has to tell the new tricycles from the old one, so make the third one obviously shabby while the first two stay bright and glossy. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```

**5. Качели**

Заменяет: aaae7d559703, f88d4a9d9074 (обрезанные), 7c2ca990d569 (целые)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with three separate wooden garden swings, each one complete with the whole A-shaped frame, both ropes and the seat visible inside the picture, nothing cut off at the edges, all three drawn from the same straight front angle and at the same size. Row 1, left to right: a wooden swing with a flat plank seat hanging on two light ropes, a wooden swing with a wider plank seat hanging on two thicker ropes, a wooden swing frame with two plank seats hanging side by side. The whole frame must fit inside the picture with empty white space around it, because in the current pictures the frame is cut off at the sides. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```

**6. Ягоды и гнездо**

Заменяет: 92a7cd9b7083 (красные), 39138a8f35bf (синие), cc7396a1580e (жёлтые), новое пустое гнездо

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with four separate forest items, all drawn at the same size and from the same slightly-above angle. Row 1, left to right: a sprig with three round bright red berries and two green leaves, a sprig with three round deep blue berries and two green leaves. Row 2, left to right: a sprig with three round bright yellow berries and two green leaves, an empty round bird nest woven from light brown twigs with a few small green leaves tucked in. The colour of the berries is the answer to the task, so keep the three sprigs identical in shape and different only in colour: red, blue, yellow. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```

**7. Сцена «ягода рядом с гнездом» (широкая картинка, не лист)**

Заменяет: 3634ef027da5

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One single wide picture, not a grid: a round bird nest woven from light brown twigs standing on a patch of green grass, and right beside it, almost touching its left side, a small bush sprig with three round bright red berries and green leaves. The nest and the berries stand together on the same patch of grass at the same scale, so that it is obvious at a glance that the berries are NEXT TO the nest — not inside it, not on top of it and not under it. The nest is empty, there is no bird and no egg in it. Draw the whole scene complete inside the picture with a wide empty margin around it. plain flat pure white background outside the grass patch, no shadow on the background, no text, no letters, no labels, no numbers.
```

**8. Счёт «Сколько их?»: один торт, две пиццы, три мороженых**

Заменяет: 0f1443c8387f (1), 7fffc526df4e (2), be54adde645b (3)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with three separate groups of food, all drawn at the same size and from the same slightly-above angle. Row 1, left to right: exactly one round birthday cake with pink icing and white cream, with NO candles on it at all and nothing standing on top of it, exactly two identical round pizzas with tomato, cheese and basil seen from above, exactly three identical ice-cream cones with two scoops each. The number of objects in each group is the answer to the task, so the first group must contain exactly one object and nothing else that a child could count — the cake must have no candles, no cherries and no decorations that look countable. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```

**9. Одежда и игрушки юнита 2**

Заменяет: c7fa6f00b265 (джинсы), 823ba47ef7eb (кукла), a7aaad30331d, f91ea8f7e69f (кеды), c5b5fa0f3242, 0099c0ea54f7 (юбки)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with six separate items of children's clothing and toys, each shown alone, flat and straight on, all at the same size. Row 1, left to right: a pair of blue denim jeans with a yellow button and light stitching, a pair of lilac-purple canvas sneakers with white laces and white soles standing side by side, a pair of bright yellow canvas sneakers with white laces and white soles standing side by side. Row 2, left to right: a bright yellow pleated skirt, a light purple pleated skirt, a small toy doll girl with brown braided hair in a pink dress and pink shoes. The colour of each item is the answer to the task, so keep the colours exactly as named: blue jeans, purple sneakers, yellow sneakers, yellow skirt, purple skirt, pink doll dress. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```

**10. Мелкие предметы: следы, поделка, клей, палитра**

Заменяет: 06dbc844112c (следы), 86466d361dc9 (фигуры из бумаги), e893a6b7b83a (клей), f48cc750447c (палитра)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with four separate small objects, each shown alone and straight on, all at the same size. Row 1, left to right: a trail of four purple cat paw prints going up to the right, four flat paper shapes lying together on the table — one orange triangle, two pink circles and one green square, exactly four shapes and no more. Row 2, left to right: an open purple glue stick with its cap lying next to it, a wooden artist palette with six round blobs of paint (red, blue, green, yellow, orange, white) and a paintbrush lying across it. In the paper-shapes picture the child counts the shapes, so draw exactly four shapes, clearly separated and all fully visible. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```
