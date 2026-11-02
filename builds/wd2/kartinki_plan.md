# Wow Dragon 2 — вычитка картинок, план перерисовки

Собрано 02.11.2026 по базе (курс «Wow Dragon 2», `slug` пустой,
id `2b4c8528-ae7e-4e97-bfca-c34ac2ed4efa`) и по файлам в `media/wow-dragon-2/`.
Генерировать картинки не нужно: ниже список того, что плохо, и готовые промпты
для методиста.

## Сколько всего

| что | сколько |
|---|---|
| картинок в заданиях (все блоки, кроме `text`, `video`, `embed`) | **544** |
| из них в `media/wow-dragon-2/` | 540 — `legacy/` 429, `new/` 79, `comics/` 32 |
| взято из чужой папки `media/wow-dragon-1/legacy/` (картинки Дракоши) | 4 |
| файлов в `media/wow-dragon-2/` всего | 617 (`legacy/` 475, `new/` 82, `comics/` 60) |
| **мельче 300 px по большей стороне — в заданиях** | **159** (156 `legacy/`, 3 `new/`) |
| мельче 300 px на диске, но в заданиях не стоят | 12 |
| 300–400 px в заданиях | 215 |
| медиана размера используемой картинки | 337 px |
| битых ссылок (файла нет на диске) | **0** |

## Что это за 159 мелких картинок

| группа | штук | что делаем |
|---|---|---|
| тени предметов для игры «найди тень» | 16 | **не трогаем** — это материал задания |
| карточки букв `f_big`, `f_small`, `sh_small` | 3 | **не трогаем** — по ним сверяются ответы |
| цифры 1, 3, 5 | 3 | **рисуем сами скриптом** — в промпте нельзя просить цифры («no numbers») |
| круг, квадрат, треугольник (юнит 0) | 3 | **рисуем сами скриптом**, цвет — ответ задания |
| остальные предметы | 134 | из них 22 мельче 250 px — перерисовываем; 110 в диапазоне 250–299 px оставляем |

Стиль у курса ровный: тот же плоский клипарт с тёмно-фиолетовым контуром, что и
в Wow Dragon 1. Мыла почти нет; беда в другом — **космический юнит 300 нарисован
самыми мелкими картинками курса** (двигатель 142 px при тридцати использованиях,
корпус ракеты 130 px, топливный бак 147 px), и часть предметов там не узнаётся
сама по себе. Поэтому перерисовываем 48 позиций, а не курс целиком.

## Чего не трогаем

* **Комиксы.** `media/wow-dragon-2/comics/` — девять домашек с историей:
  ДЗ 11, 18, 26, 34, 42, 50, 59, 67, 75 (лист `hwNN.webp` плюс кадры
  `hwNN_k1…k5`, всего 54 файла). Реплики привязаны к кадрам.
* **Герои.** `comics/hero_bunny`, `hero_dragon`, `hero_granny`, `hero_martian`,
  `hero_princess`, `hero_unicorn`, а также `new/dragon_*`, `new/granny_*`,
  `new/princess_weak`, `new/penguin_compass`. Своя версия героя будет не та.
  Сюда же четыре картинки Дракоши, которые курс берёт из `wow-dragon-1/legacy/`
  (`03073aaae67a`, `30f787178c40`, `7801b60b6af1`, `ce6f5fe872e5` — юнит 300, ДЗ 57 и 62).
* **Карточки букв и буквосочетаний:** `new/f_big`, `new/f_small`, `new/sh_big`,
  `new/sh_small`, `new/ea_big`, `new/ea_small`, `new/th_big`, `new/th_small`.
* **Тени** (16 файлов: `0997c3ee4e9d`, `0c1e8b08d0da`, `467320231127`, `522b46ff7cd8`,
  `6e1aaa224d09`, `73620ec1f5a9`, `8227ba22e193`, `83d888c41fb6`, `9d3debe5d2f9`,
  `c0d8c6510ea3`, `d428bb0b3e43`, `dbf070dffccd`, `e32e87af20e9`, `e849a305d24c`,
  `f96376422d15`, `fadee89a770d`). Но: у чашки, кошелька, двигателя и плавников
  тень есть, и если предмет перерисован, **тень надо пересобрать из новой картинки**
  заливкой силуэта одним цветом — скриптом, не промптом. Иначе в игре «найди тень»
  (ДЗ 56 блок 41 и другие) ответ перестанет сходиться.
* **Карточки лексики, стоящие не вторым блоком**, — устройство Wow Dragon,
  решение Анны от 02.11.2026.

## 🟥 Картинка спорит с ключом

1. **ДЗ 17, блок 7** (юнит 100, «Сколько апельсинов? Посчитай и выбери»): во всех
   трёх вопросах рядом с целыми апельсинами нарисованы ещё и половинки —
   `40e8aad2a6d0` (ответ «one», видно апельсин и половинку), `2b97f270263d`
   («two», два и две половинки), `941b864c7a95` («three», три и три половинки).
   Ребёнок считает половинки и отвечает вдвое больше. Перерисовать все три
   без разрезанных долек (промпт 7).
2. **Плавники ракеты** `5fd8a3c5c3aa` (250×161, 27 использований, юнит 300,
   ДЗ 56–78): две красные загогулины без ракеты. Ребёнок не узнаёт предмет, а по
   нему идут и карточка, и «выбери на слух», и «разложи по группам», и «какой
   части не хватает». Перерисовать так, чтобы было видно: это пара крыльев
   ракеты (промпт 1).
3. **Счёт в кафе** `2c8f53139cbf` (юнит 200, ДЗ 51, карточка «bill» и блоки 31, 71, 81):
   бумажка на тарелке читается как салфетка. Перерисовать как счёт (промпт 5).

Проверено и оказалось в порядке: «Сколько монет?» (ДЗ 1 блок 6), «Сколько девочек?»
(ДЗ 13 блок 5), «Сколько детей?» (ДЗ 5 блок 8), зелёный треугольник ↔ зелёный мишка
(ДЗ 1 блок 5 — задание на цвет, не на предмет), «старый трицикл» в ДЗ 24 блок 6
(серо-коричневый он намеренно, ответ — «old»; перерисовывается в плане Wow Dragon 1).

## Что перерисовываем — таблица

| файл | размер | где стоит | что не так |
|---|---|---|---|
| `legacy/26eba2cff048.webp` | 130×274 | u300 HW56 b21 (flashcards), u300 HW56 b31 (quiz), u300 HW56 b71 (quiz), u300 HW58 b61 (match) … всего 15 | корпус ракеты — 130 px, читается как патрон, а не как корпус |
| `legacy/d2832581d228.webp` | 142×226 | u300 HW56 b21 (flashcards), u300 HW56 b31 (quiz), u300 HW56 b41 (match), u300 HW56 b51 (quiz) … всего 30 | двигатель — 142 px, 30 использований по юниту |
| `legacy/5fd8a3c5c3aa.webp` | 250×161 | u300 HW56 b21 (flashcards), u300 HW56 b31 (quiz), u300 HW56 b41 (match), u300 HW56 b51 (quiz) … всего 27 | плавники — 250×161, две красные загогулины без ракеты, ребёнок не узнаёт предмет |
| `legacy/fc969e6293a3.webp` | 147×257 | u300 HW56 b21 (flashcards), u300 HW56 b31 (quiz), u300 HW56 b51 (quiz), u300 HW56 b61 (sort) … всего 21 | топливный бак — 147 px |
| `legacy/e8f51ea575bd.webp` | 196×328 | u300 HW56 b21 (flashcards), u300 HW56 b41 (match), u300 HW56 b51 (quiz), u300 HW57 b31 (quiz) … всего 39 | ракета целиком — перерисовать вместе с деталями |
| `legacy/92c958dabbab.webp` | 114×317 | u300 HW60 b41 (quiz), u300 HW60 b91 (quiz), u300 HW60 b101 (speaking), u300 HW61 b41 (match) … всего 5 | КЛЮЧ: ракета без плавников, 114 px; по ней выбирают недостающую деталь |
| `legacy/14d128c66579.webp` | 202×283 | u300 HW60 b41 (quiz), u300 HW61 b41 (match) | КЛЮЧ: ракета без корпуса, 202 px |
| `new/rocket_no_engine.webp` | 323×353 | u300 HW61 b41 (match) | КЛЮЧ: ракета без двигателя — перерисовать в одном листе с двумя предыдущими |
| `legacy/1edf7f331f83.webp` | 217×216 | u300 HW55 b21 (flashcards), u300 HW55 b31 (quiz), u300 HW55 b61 (sort), u300 HW55 b91 (sequence) … всего 9 | Меркурий — 217 px |
| `legacy/6087bee739ea.webp` | 241×240 | u300 HW55 b21 (flashcards), u300 HW55 b31 (quiz), u300 HW55 b41 (match), u300 HW55 b51 (quiz) … всего 11 | Венера — 241 px |
| `legacy/7ad7d139180e.webp` | 244×244 | u300 HW54 b21 (flashcards), u300 HW54 b31 (quiz), u300 HW54 b51 (quiz), u300 HW54 b61 (sort) … всего 29 | Земля — 244 px, 29 использований |
| `legacy/d0af30982398.webp` | 249×247 | u300 HW54 b41 (match), u300 HW54 b71 (quiz), u300 HW55 b21 (flashcards), u300 HW55 b31 (quiz) … всего 38 | Марс — 249 px, 38 использований |
| `legacy/e1e60d2d0dd5.webp` | 243×245 | u300 HW54 b41 (match), u300 HW55 b21 (flashcards), u300 HW55 b31 (quiz), u300 HW55 b41 (match) … всего 12 | Нептун — 243 px |
| `legacy/e11b7418f131.webp` | 287×293 | u300 HW55 b21 (flashcards), u300 HW55 b31 (quiz), u300 HW55 b41 (match), u300 HW55 b51 (quiz) … всего 11 | Юпитер — 287 px, перерисовать вместе с остальными |
| `legacy/922e292095c8.webp` | 373×226 | u300 HW54 b71 (quiz), u300 HW55 b21 (flashcards), u300 HW55 b31 (quiz), u300 HW55 b51 (quiz) … всего 17 | Сатурн — перерисовать вместе с остальными |
| `legacy/270e4debc8a2.webp` | 154×249 | u200 HW38 b21 (flashcards), u200 HW38 b31 (quiz), u200 HW38 b71 (quiz), u200 HW38 b81 (quiz) … всего 18 | карабин — 154 px, 18 использований |
| `legacy/ee6b82d12858.webp` | 191×244 | u200 HW32 b21 (flashcards), u200 HW32 b31 (quiz), u200 HW32 b51 (quiz), u200 HW32 b61 (sort) … всего 15 | метро — 191 px |
| `legacy/a03eb0399eb7.webp` | 233×233 | u200 HW37 b21 (flashcards), u200 HW38 b21 (flashcards), u200 HW38 b31 (quiz), u200 HW38 b41 (match) … всего 23 | кошелёк — 233 px, 23 использования |
| `legacy/5866c7047d69.webp` | 245×249 | u200 HW41 b31 (quiz), u200 HW41 b41 (sequence), u200 HW41 b71 (quiz), u200 HW41 b101 (speaking) | собранный чемодан — 245 px |
| `legacy/aeccdef06700.webp` | 281×212 | u200 HW35 b31 (quiz), u200 HW36 b31 (quiz), u200 HW36 b41 (match), u200 HW36 b51 (quiz) … всего 30 | билеты — 281×212 |
| `legacy/11200c4b36d3.webp` | 282×224 | u200 HW29 b31 (quiz), u200 HW30 b51 (quiz), u200 HW30 b61 (sort), u200 HW35 b21 (flashcards) … всего 22 | карта — 282×224 |
| `legacy/dd86c00c6fd2.webp` | 229×175 | u300 HW68 b51 (quiz), u300 HW71 b21 (flashcards), u300 HW71 b51 (quiz), u300 HW71 b61 (sort) … всего 12 | чашка — 229×175, 12 использований |
| `legacy/1624260a7909.webp` | 225×213 | u200 HW49 b21 (flashcards), u200 HW49 b31 (quiz), u200 HW49 b51 (quiz), u200 HW49 b61 (quiz) … всего 7 | киви — 225 px |
| `legacy/26eaa8b0ceac.webp` | 236×197 | u300 HW65 b21 (flashcards), u300 HW65 b31 (quiz), u300 HW65 b41 (match), u300 HW65 b51 (quiz) … всего 11 | космическая еда — 236×197 |
| `legacy/76bbf6f8984f.webp` | 266×164 | u200 HW38 b21 (flashcards), u200 HW38 b31 (quiz), u200 HW38 b51 (quiz), u200 HW38 b71 (quiz) … всего 9 | мятные драже — 266×164 |
| `legacy/c7949ac1a18b.webp` | 220×291 | u200 HW49 b31 (quiz), u200 HW51 b21 (flashcards), u200 HW51 b31 (quiz), u200 HW51 b51 (quiz) … всего 13 | сок — 220 px |
| `legacy/2c8f53139cbf.webp` | 283×208 | u200 HW51 b21 (flashcards), u200 HW51 b31 (quiz), u200 HW51 b71 (quiz), u200 HW51 b81 (quiz) | счёт в кафе — читается как салфетка на тарелке, а не как счёт |
| `legacy/85f522fcd1a7.webp` | 220×228 | u0 HW1 b3 (flashcards) | серебряная монета — 220 px, по ней ключ «silver» |
| `legacy/08f50699c06f.webp` | 218×229 | u0 HW1 b3 (flashcards), u0 HW1 b7 (quiz) | золотая монета — 218 px, ключ «golden» |
| `legacy/d7284e9c852d.webp` | 214×223 | u200 HW31 b41 (match) | кристалл — 214 px |
| `legacy/cb88c9c962ee.webp` | 221×266 | u300 HW74 b31 (quiz), u300 HW74 b61 (match), u300 HW74 b81 (quiz), u300 HW76 b21 (flashcards) … всего 7 | розовый кристалл — 221 px |
| `legacy/40e8aad2a6d0.webp` | 296×270 | u100 HW17 b7 (quiz) | КЛЮЧ: ответ «one», а нарисованы целый апельсин и половинка — ребёнок считает два |
| `legacy/2b97f270263d.webp` | 400×173 | u100 HW17 b7 (quiz) | КЛЮЧ «two»: два апельсина и две половинки |
| `legacy/941b864c7a95.webp` | 400×113 | u100 HW17 b7 (quiz) | КЛЮЧ «three»: три апельсина и три половинки |
| `legacy/39a564d4c408.webp` | 292×88 | u300 HW66 b21 (flashcards), u300 HW66 b31 (quiz), u300 HW66 b41 (sequence) | пять шариков в ряд — 292×88, полоска в два пальца высотой |
| `legacy/76f6b2f98191.webp` | 196×230 | u200 HW34 b31 (quiz), u200 HW38 b31 (quiz) | ключик — 196 px |
| `legacy/1bd3010223d1.webp` | 242×234 | u300 HW72 b31 (quiz), u300 HW73 b31 (quiz), u300 HW73 b51 (quiz), u300 HW73 b71 (quiz) … всего 10 | звезда — 242 px |
| `legacy/d9cbdd7a3544.webp` | 287×279 | u300 HW72 b21 (flashcards), u300 HW72 b31 (quiz), u300 HW72 b41 (quiz), u300 HW72 b51 (sort) … всего 16 | ложка — 287 px, 16 использований |
| `legacy/5042ef644b95.webp` | 279×215 | u300 HW71 b21 (flashcards), u300 HW71 b61 (sort), u300 HW72 b61 (match), u300 HW73 b31 (quiz) … всего 5 | стол — 279×215 |
| `legacy/d3da0f780cfc.webp` | 221×288 | u100 HW25 b3 (flashcards), u100 HW25 b4 (quiz), u100 HW25 b5 (quiz), u100 HW25 b8 (sort) … всего 8 | носок — 221×288 |
| `legacy/88f72597c14b.webp` | 288×182 | u300 HW54 b51 (quiz), u300 HW66 b51 (quiz), u300 HW67 b21 (flashcards), u300 HW67 b31 (quiz) … всего 9 | перчатки — 288×182 |
| `legacy/16b4ebd9ff88.webp` | 185×226 | u200 HW53 b61 (quiz) | стрелка вниз — 185 px |
| `legacy/f88257420465.webp` | 186×226 | u200 HW48 b71 (quiz), u200 HW53 b21 (quiz) | стрелка вверх — 186 px |
| `legacy/bab0eef99bb0.webp` | 246×177 | u200 HW48 b21 (flashcards), u200 HW48 b31 (quiz), u200 HW48 b41 (match), u200 HW48 b71 (quiz) … всего 8 | стрелка вправо — 246×177 |
| `legacy/753b3bf4f872.webp` | 252×180 | u200 HW48 b21 (flashcards), u200 HW48 b31 (quiz), u200 HW48 b41 (match), u200 HW48 b71 (quiz) … всего 9 | стрелка влево — 252×180 |
| `legacy/9bee3e0930bc.webp` | 114×220 | u300 HW79 b61 (quiz) | цифра 1 — 114 px |
| `legacy/85912d0f7859.webp` | 158×220 | u300 HW79 b61 (quiz) | цифра 3 — 158 px |
| `legacy/404cfc671a52.webp` | 170×225 | u300 HW79 b61 (quiz) | цифра 5 — 170 px |

Плюс **скриптом, без промпта**: цифры 1, 3, 5 (`9bee3e0930bc`, `85912d0f7859`,
`404cfc671a52`), четыре стрелки (`16b4ebd9ff88` вниз, `f88257420465` вверх,
`bab0eef99bb0` вправо, `753b3bf4f872` влево) и три фигуры юнита 0 —
красный круг `1eae7f05e7c4`, синий квадрат `e76d8b6c306f`, зелёный треугольник
`5b3e230745ed` (цвет фигуры — ответ в ДЗ 1 блок 5, менять его нельзя).

**Цифры 1, 3 и 5 — те же файлы, что в Wow Dragon 1** (`9bee3e0930bc`,
`85912d0f7859`, `404cfc671a52`), плюс курс берёт у соседа розовый и «старый»
трициклы, сцену с гнездом, джинсы и клей-карандаш. Перерисованное кладём в обе
папки сразу. План первого курса — `builds/wd1/kartinki_plan.md`.

## Промпты 1–9

Каждый промпт — цельный блок, копируется одним нажатием. Лист режем мы.
Хранить с запасом: карточка 600–800 px по большей стороне, сцена 1200–1600, webp 88–90.


**1. Части ракеты**

Заменяет: 26eba2cff048 (корпус), d2832581d228 (двигатель), 5fd8a3c5c3aa (плавники), fc969e6293a3 (топливный бак), e8f51ea575bd (ракета целиком)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with five separate parts of a toy space rocket, all drawn from the same straight side-on angle and at the same size, each part clearly recognisable on its own. Row 1, left to right: a complete toy rocket standing upright — white body, red pointed nose cone, round light blue porthole, two red fins at the bottom and a grey engine nozzle with an orange flame; the white cylindrical rocket body alone, with the red nose cone on top, no fins and no engine. Row 2, left to right: a grey cone-shaped rocket engine nozzle alone with a short orange and yellow flame coming out of it; a pair of two red rocket fins alone, drawn as two curved triangular wings standing slightly apart and clearly shaped like parts that attach to a rocket, not like two abstract red strokes; a white metal fuel tank alone, a rounded cylinder lying upright with a red stripe around the middle and a grey cap on top. The child learns these words from the pictures, so each part must be recognisable without the rest of the rocket. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```

**2. Ракеты без одной детали**

Заменяет: 92c958dabbab (без плавников), 14d128c66579 (без корпуса), new/rocket_no_engine (без двигателя)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with three separate toy rockets, all drawn from the same straight side-on angle and at the same size, each one missing exactly one part. Row 1, left to right: a rocket with a white body, red nose cone, round light blue porthole and a grey engine nozzle with an orange flame, but with NO fins at the bottom at all; a rocket that has only the red nose cone, the two red fins and the grey engine nozzle with an orange flame, with NO white body between them, so that the middle of the rocket is clearly empty; a rocket with a white body, red nose cone, porthole and two red fins, but with NO engine nozzle and NO flame at the bottom. The child has to see which part is missing, so draw each rocket complete except for that one part, and keep the missing place obviously empty. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```

**3. Планеты**

Заменяет: 1edf7f331f83 (Меркурий), 6087bee739ea (Венера), 7ad7d139180e (Земля), d0af30982398 (Марс), e11b7418f131 (Юпитер), 922e292095c8 (Сатурн), e1e60d2d0dd5 (Нептун)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with seven separate planets, each a round ball seen from the front, all drawn at the same size except Saturn which is slightly wider because of its ring. Row 1, left to right: Mercury — a small dull grey planet with a few soft craters, drawn as a solid planet and clearly not a crescent moon; Venus — a creamy yellow-orange planet with soft swirling cloud bands; Earth — a blue planet with green continents and small white clouds; Mars — a red-orange planet with darker red patches and a small white polar cap on top. Row 2, left to right: Jupiter — a large pale orange planet with wide cream and brown stripes and one big red oval spot; Saturn — a pale yellow planet with a wide flat ring around it; Neptune — a deep blue planet with lighter blue bands. The colour and the pattern are how the child tells one planet from another, so keep the seven clearly different from each other. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```

**4. Путешествие**

Заменяет: 5866c7047d69 (чемодан), 270e4debc8a2 (карабин), ee6b82d12858 (метро), aeccdef06700 (билеты), a03eb0399eb7 (кошелёк), 11200c4b36d3 (карта)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with six separate travel objects, each shown alone and straight on, all at the same size. Row 1, left to right: a brown suitcase standing closed with its handle up and two silver latches; a silver metal climbing carabiner hook with the spring gate on one side; a modern blue and white underground train carriage seen from the front with big windows and a round headlight. Row 2, left to right: two paper travel tickets lying one behind the other, plain cream-coloured with a small aeroplane shape printed on each and no writing on them; an open brown leather wallet with two round gold coins sticking out of it; a folded paper city map with green parks, blue river and a red location pin on it. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```

**5. Кафе и еда**

Заменяет: dd86c00c6fd2 (чашка), 1624260a7909 (киви), 26eaa8b0ceac (космическая еда), 76bbf6f8984f (драже), c7949ac1a18b (сок), 2c8f53139cbf (счёт)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with six separate cafe objects, each shown alone and straight on, all at the same size. Row 1, left to right: a white porcelain tea cup with a purple rim seen from the side, empty; half a kiwi fruit cut across, bright green inside with black seeds and a brown furry skin; a silver foil food pouch for astronauts, a flat sealed square packet with a purple label area and no writing on it. Row 2, left to right: a small round tin of white mint sweets, open, with three white round sweets lying beside it; a tall glass of orange juice with a purple straw and a slice of orange on the rim; a paper restaurant bill — a small white paper slip with a torn bottom edge and faint printed lines, lying on a round silver tray, clearly a paper bill and not a napkin. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```

**6. Монеты и кристаллы**

Заменяет: 85f522fcd1a7 (серебряная монета), 08f50699c06f (золотая монета), d7284e9c852d (фиолетовый кристалл), cb88c9c962ee (розовый кристалл), e39ac445238c (кристаллы на камне)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with five separate shiny objects, each shown alone and straight on, all at the same size. Row 1, left to right: a round silver coin seen from the front with a raised five-pointed star in the middle and a milled rim, clearly silver-grey metal; a round golden coin seen from the front with a raised five-pointed star in the middle and a milled rim, clearly warm yellow gold; a single tall purple crystal standing upright, with sharp facets and two small sparkles beside it. Row 2, left to right: a single tall pink crystal standing upright, with sharp facets and two small sparkles beside it; a grey stone with three crystals growing out of it — one pink, one purple and one light blue. Silver and gold are the answer to the task, so the first coin must read as cold silver-grey and the second as warm yellow gold at a glance. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```

**7. Счёт апельсинов: один, два, три**

Заменяет: 40e8aad2a6d0 (1), 2b97f270263d (2), 941b864c7a95 (3)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with three separate groups of oranges, all fruits drawn at the same size and from the same slightly-above angle, every orange whole and uncut with a small green leaf on top. Row 1, left to right: exactly one whole orange; exactly two whole oranges side by side; exactly three whole oranges side by side. The number of fruits is the answer to the task, so there must be no cut halves, no slices and no extra pieces anywhere — a child must be able to count one, two and three and get exactly that. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```

**8. Лепим модель из пластилина**

Заменяет: 39a564d4c408 (ряд из шариков), c50faf10b65a (пластилин), e0ae584fbdd3 (готовая модель)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with three separate plasticine objects, all drawn at the same size and from the same slightly-above angle. Row 1, left to right: five round plasticine balls of different sizes and colours (purple, blue, green, yellow, red) lying in one straight row with small gaps between them, drawn big enough to fill the cell; a soft block of modelling plasticine with a few bright strips of different colours pressed together; a finished model of the solar system — a big yellow ball in the middle on a small purple stand, with four smaller coloured balls on thin wire arms around it. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```

**9. Мелкие предметы: ключ, звезда, ложка, стол, носок, перчатки**

Заменяет: 76f6b2f98191 (ключ), 1bd3010223d1 (звезда), d9cbdd7a3544 (ложка), 5042ef644b95 (стол), d3da0f780cfc (носок), 88f72597c14b (перчатки)

```
Children's coursebook illustration in a friendly 3D-rendered cartoon style, soft rounded shapes, smooth matte surfaces with gentle glossy highlights, bright saturated colours, thick clean silhouettes, soft even studio light. One sheet with six separate everyday objects, each shown alone and straight on, all at the same size. Row 1, left to right: an old golden key with a round decorated head and two small sparkles beside it; a single bright yellow five-pointed star with soft rounded tips; a silver metal teaspoon lying with the bowl up. Row 2, left to right: a simple wooden table with four legs seen from the side; one light blue knitted sock with two white stripes near the top; a pair of white knitted gloves lying side by side. plain flat pure white background, no shadow on the background, wide empty white gaps between the items, every item complete and not touching any other item or the edge, a wide empty margin around the whole sheet, no text, no letters, no labels, no numbers.
```
