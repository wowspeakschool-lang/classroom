# Go Getter 1 — ЛИСТЫ ПРОМПТОВ НА КАРТИНКИ

Один промпт = одна картинка-лист с сеткой внутри. Генерирует Анна, присылает
в чат, лист режется на карточки (`tools/sm3_cut.py`, своя таблица листов для
GG1) и ложится webp в `media/gg1/uN/`.

**Номер листа — Л<юнит>.<номер>**: Л0.1, Л0.2, Л1.1… Номер не переиспользуется:
если лист выброшен, его номер остаётся пустым, как Л1.7–Л1.8 у SM3. Присылая
картинку, подписывать её номером листа — по нему лист находится в таблице
нарезки.

Каждый промпт самодостаточный: сетка, стиль, запрет людей и текста, размер —
всё внутри, копируется целиком.

## Правила (те же, что у SM3 — см. `docs/SM3_листы_промптов.md`)

1. **Людей нет нигде** — ни детей, ни рук, ни лиц, ни силуэтов.
2. **Не больше 3 колонок** — иначе ячейка мельче 512 px и мылит при нарезке.
3. **Никаких узнаваемых товаров** — у техники, обуви, рюкзаков
   `generic design, not resembling any real product`.
4. **Один стилевой регистр на лист.** Для GG1 предметные карточки —
   реалистичный 3D (как предметы SM3): узнаваемость важнее.
5. Ячейки нумеруются слева направо, сверху вниз, в порядке промпта.

## Чего не генерируем

| Что | Откуда |
|---|---|
| Цветные кляксы для слов-цветов | рисует скрипт (SVG), чтобы red на всех экранах был одним и тем же red |
| Обучающие карточки методиста (правила, таблицы слов, 900×506) | вырезаются из PDF выгрузки |
| Картинки учебника (сцены, иллюстрации заданий) | вырезаются из PDF выгрузки |
| Приветствия, похвалы, прощания | `media/shared/` |
| Картинки из выгрузки с чужими персонажами (пингвины, Микки) | не берём, заменяем на `media/shared/` |

---

# UNIT 0 · HELLO! — 3 листа

### Л0.1 · В рюкзаке — 9 карточек (3×3)
```
A sheet of nine separate object cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each object centred with a generous empty margin on all sides, never touching the cell edges:
1) a closed hardcover school book; 2) one coloured pencil, bright red, lying diagonally; 3) a spiral notebook with a plain cover; 4) a ballpoint pen with its cap; 5) a yellow graphite pencil with a pink eraser tip; 6) a zipped fabric pencil case; 7) a small plastic pencil sharpener; 8) a rectangular rubber eraser; 9) a plastic ruler with plain tick marks.
No people at all - no humans, no hands, no faces anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л0.2 · Класс и школьные вещи — 9 карточек (3×3)
```
A sheet of nine separate object cards in a clean 3x3 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each object centred with a generous empty margin on all sides, never touching the cell edges:
1) a pair of children's scissors with rounded tips; 2) a sandwich cut in half showing cheese and lettuce; 3) a school backpack with two straps; 4) a plastic waste bin; 5) a green classroom chalkboard in a wooden frame, completely blank; 6) a wooden school chair; 7) a round wall clock with plain tick marks and no numbers; 8) a wooden school desk; 9) a shiny red apple with a leaf.
No people at all - no humans, no hands, no faces anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no brand marks anywhere.
Output size: 2048 x 2048 px, each cell at least 650 px.
```

### Л0.3 · Цветные вещи — 6 карточек (3×2)
Для теста Unit 0: «My pen is red», «My bag is blue»… Цвет каждой вещи
должен читаться сразу — одна вещь, один цвет.
```
A sheet of six separate object cards in a clean 3x2 grid, equal cells separated by thin light-grey gutters, each cell a complete standalone picture on pure white, nothing crossing between cells, each object centred with a generous empty margin on all sides, never touching the cell edges. Each object is clearly one single bright colour:
1) a bright red ballpoint pen; 2) a bright blue school backpack; 3) a bright yellow plastic ruler with plain tick marks; 4) a bright green spiral notebook; 5) a bright pink zipped pencil case; 6) a bright orange school backpack.
No people at all - no humans, no hands, no faces anywhere.
Realistic 3D render, soft studio lighting from the top-left, clean product-style but friendly and colourful, generic design, not resembling any real product. Plain flat pure white background, no shadow on the background. Absolutely no text, no letters, no numbers, no labels, no brand marks anywhere.
Output size: 2048 x 1365 px, each cell at least 650 px.
```
