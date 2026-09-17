# Промпты для иконок WOW Speak

## Эталонные формулировки стиля (от Анны — использовать их, а не свои)

**10-12.** Дружелюбный учебный cartoon / flat illustration style для детей 10–12 лет: чистые
чёткие контуры, яркие, но не кислотные цвета, мягкие тени, простые формы, понятные детали,
аккуратный современный вид, без реализма и без слишком детского «малышового» стиля. Объекты
должны выглядеть как отдельные учебные иллюстрации или стикеры на белом фоне.

**13+.** Современная учебная иллюстрация для подростков 14–17 лет. Чистые, яркие, слегка
реалистичные изображения объектов с аккуратными контурами, мягкими тенями и умеренной
детализацией. Не детский мультяшный стиль и не фотореализм. Цвета насыщенные, но естественные.
Каждый объект хорошо читается с первого взгляда.

**Композиция (для обоих).** Несколько отдельных объектов на чистом белом фоне, расположенных на
большом расстоянии друг от друга, без пересечений и лишних декоративных элементов, чтобы каждый
объект можно было легко вырезать отдельно.

**Визуально (для 13+).** Polished educational illustration, semi-realistic vector-like style,
clean outlines, soft 3D shading, crisp edges, isolated objects, white background, teen-friendly,
textbook/workbook aesthetic.


Настройки генерации: `gpt-image-1`, `background: opaque` (НЕ transparent), `quality: medium`
(в `high` — только если medium дал брак).
Размер: лист — `1536x1024`, одна иконка — `1024x1024`.

Готовые промпты текущей темы — в конце файла, их можно копировать целиком. Выше — шаблоны на
будущие темы: меняется только список предметов, блоки про раскладку и стиль копируются как есть.

Предметы описывать **конкретной сценой**, а не словом урока: не «holidays», а «a closed suitcase
with a sun hat and a beach ball on top». Абстрактные слова следить, чтобы не выглядели одинаково
(chill / break / tired легко сливаются).

---

## 1. Лист иконок для 10-12 (младшие)

> Six separate 3D-rendered objects on one plain white sheet, laid out in two rows of three, far
> apart from each other. Each is one compact object. The drawings must never touch, overlap or be
> connected — leave empty white space at least the width of a whole drawing between neighbours.
> No frames, no boxes, no borders, no dividing lines, no panels, no background scenery.
> ABSOLUTELY NO text, letters, captions or labels anywhere.
> The six objects are: 1) …; 2) …; 3) …; 4) …; 5) …; 6) … .
> Style: cute glossy 3D character-art render, the look of a modern animated film for children —
> soft rounded friendly shapes, smooth shiny surfaces, bright saturated candy colours, even soft
> studio lighting, gentle contact shadows, cheerful and warm, cut out on pure white.
> Polished and appealing, never flat vector, never a 2D outline cartoon.

## 2. Лист иконок для 13+ (старшие)

> Six separate 3D-rendered objects on one plain white sheet, laid out in two rows of three, far
> apart from each other. Each is one compact object. The drawings must never touch, overlap or be
> connected — leave empty white space at least the width of a whole drawing between neighbours.
> No frames, no boxes, no borders, no dividing lines, no panels, no background scenery.
> ABSOLUTELY NO text, letters, captions or labels anywhere.
> The six objects are: 1) …; 2) …; 3) …; 4) …; 5) …; 6) … .
> Style: polished stylised 3D render for teenagers — real object proportions and believable
> materials, crisp modelling and fine detail, soft studio lighting with clean highlights and
> gentle shadows, cut out on pure white. Colours stay BRIGHT and SATURATED (strong blues, greens,
> yellows, reds, purples) — absolutely no muted, beige, brown, grey or washed-out palette.
> NO cartoon faces or eyes on objects, NO toy-like puffy rounded shapes, nothing cute or babyish,
> never flat vector, never a 2D outline cartoon. A high-quality modern product render, not a toy.

## 3. Одна иконка отдельной картинкой (надёжнее всего)

Убрать первый абзац про раскладку и написать:

> One single 3D-rendered object on a plain white background: <предмет>.
> Nothing else in the frame, no second object, no background scenery, no shadow of other things.
> ABSOLUTELY NO text, letters, captions or labels.

и дальше тот же блок Style из пункта 1 или 2.

---

## Что нельзя писать в промпте

- **«grid», «cells», «panels»** — модель понимает буквально и рисует разделительные линии;
  все картинки склеиваются в один объект, и нарезать лист становится нечем.
- **«transparent background»** — прозрачность съедает белые части предметов, а нарезка и белые
  плитки в деке рассчитаны на белый фон.
- Приглушённые «взрослые» слова про цвет (muted, earthy, sophisticated palette) — от них
  получается бежево-серая гамма, которая не подходит ни одному возрасту.

## Что проверить на готовом листе

1. Предметов ровно столько, сколько заказано (модель любит слепить два в один или потерять один).
2. Никакие два предмета не соприкасаются.
3. Ничего не обрезано краем листа.
4. **Нет текста и подписей — в том числе вывесок на самих предметах.** Модель любит написать
   SCHOOL над входом в школу, дни недели на календаре, надпись на коробке. Для слайда New Words
   это не страшно, а в игре «Which one is "school"?» вывеска — прямая подсказка, и задание
   начинает проверять чтение вместо знания слова (правило 2). Для предметов, которые модель
   норовит подписать, добавлять в промпт: `no sign, no lettering, no writing on the building`.

Если пункт 1 или 2 не выполнен — перегенерировать лист, а не пытаться нарезать.

---

## Текущая тема «Small talk I hate» — готовые промпты целиком

Копировать как есть, ничего не подставляя.

### 10-12 Beginners

> Six separate 3D-rendered objects on one plain white sheet, laid out in two rows of three, far
> apart from each other. Each is one compact object. The drawings must never touch, overlap or be
> connected — leave empty white space at least the width of a whole drawing between neighbours.
> No frames, no boxes, no borders, no dividing lines, no panels, no background scenery.
> ABSOLUTELY NO text, letters, captions or labels anywhere.
> The six objects are: 1) a sun partly behind a cloud with raindrops falling; 2) a school building
> with a clock on the front; 3) a round plate with a slice of pizza and a green salad on it;
> 4) a family of four standing close together and smiling; 5) a dog and a cat sitting side by side;
> 6) a closed suitcase with a sun hat and a beach ball on top.
> Style: cute glossy 3D character-art render, the look of a modern animated film for children —
> soft rounded friendly shapes, smooth shiny surfaces, bright saturated candy colours, even soft
> studio lighting, gentle contact shadows, cheerful and warm, cut out on pure white.
> Polished and appealing, never flat vector, never a 2D outline cartoon.

### 13+ Beginners

> Six separate 3D-rendered objects on one plain white sheet, laid out in two rows of three, far
> apart from each other. Each is one compact object. The drawings must never touch, overlap or be
> connected — leave empty white space at least the width of a whole drawing between neighbours.
> No frames, no boxes, no borders, no dividing lines, no panels, no background scenery.
> ABSOLUTELY NO text, letters, captions or labels anywhere.
> The six objects are: 1) a sun partly behind a cloud with raindrops falling; 2) a school building
> with a clock on the front; 3) a round plate with a slice of pizza and a green salad on it;
> 4) a pair of modern over-ear headphones; 5) a wall calendar with one date circled and a pencil
> beside it; 6) a closed suitcase with a sun hat and a beach ball on top.
> Style: polished stylised 3D render for teenagers — real object proportions and believable
> materials, crisp modelling and fine detail, soft studio lighting with clean highlights and
> gentle shadows, cut out on pure white. Colours stay BRIGHT and SATURATED (strong blues, greens,
> yellows, reds, purples) — absolutely no muted, beige, brown, grey or washed-out palette.
> NO cartoon faces or eyes on objects, NO toy-like puffy rounded shapes, nothing cute or babyish,
> never flat vector, never a 2D outline cartoon. A high-quality modern product render, not a toy.

Слова дек: 10-12 — weather · school · food · family · pets · holidays;
13+ — weather · school · food · music · plans · holidays.
