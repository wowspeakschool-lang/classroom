# Промпты: восемь детей-аватаров для заданий (av1–av8)

Эти фигурки показываются в заданиях «He has got a cap / She hasn't got jeans»
в Уроках 2, 3 и 4. Сейчас они плоские, из старого набора, — перерисовываем
в том же объёмном стиле, что и фигурка одевалки.

## Как генерировать

1. **Прикрепите к запросу картинку-образец стиля** — `assets/lesson-4/fig_boy_000.webp`
   (мальчик в жёлтой футболке и джинсах из одевалки Урока 4). Без образца слова
   «cartoon» перебиваются словами про строчку и карманы, и выходит товарный
   рендер для маркетплейса.
2. Пишите рядом с промптом: **«Match the art style of the attached image exactly.»**
3. Сгенерируйте сначала **только av1**, сравните с образцом. Если стиль сошёлся —
   гоните остальные семь.
4. Сохраняйте файлы **строго по именам**: `av1.png`, `av2.png` … `av8.png`,
   кладите в папку `assets/avatars/`.

## Что должно быть на каждой картинке

* ребёнок 7–9 лет, **в полный рост, от макушки до ступней**, лицом к зрителю,
  руки опущены вдоль тела, ноги вместе;
* фигура по центру, **поля по краям** — генератор любит упирать макушку и ступни
  в край и обрезать их;
* фон **plain flat pure white**, без тени на фоне;
* никаких надписей, цифр, логотипов;
* одежда видна целиком и читается с первого взгляда — по ней ребёнок решает
  задание.

## 🟥 Главное: состав одежды менять нельзя

Задания проверяют ответ по списку вещей. Если на картинке появится лишняя вещь
(например, куртка на av2), задание станет неправильным. Под каждым промптом —
строка «проверить»: что обязано быть и чего быть не должно.

---

## av1 — Мия, девочка

```
A cheerful cartoon girl about eight years old, standing straight and facing the viewer,
arms relaxed down at her sides, feet together. Long chestnut hair in two ponytails,
friendly smile. She is wearing a purple baseball cap worn straight with the peak forward,
a yellow short-sleeve T-shirt, a pink skirt down to the knees, and red-orange sneakers
with white soles. Bare legs between the skirt and the sneakers - no socks, no trousers.
Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated
colors, warm soft lighting from the top-left. Full body from head to toe, the whole figure
centred with clear empty margin above the head and below the feet so nothing is cut off.
No text, no letters, no numbers. Plain flat pure white background, no shadow on the background.
Match the art style of the attached image exactly.
```

**Проверить:** кепка, футболка, юбка, кроссовки. **Нет** джинсов, куртки, гольфов.

---

## av2 — мальчик без кепки и без куртки

```
A cheerful cartoon boy about eight years old, standing straight and facing the viewer,
arms relaxed down at his sides, feet together. Short red-ginger hair, freckles, friendly
smile, no hat of any kind - his hair is fully visible. He is wearing a green short-sleeve
T-shirt, blue denim jeans, and white sneakers. No jacket, no cap.
Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated
colors, warm soft lighting from the top-left. Full body from head to toe, the whole figure
centred with clear empty margin above the head and below the feet so nothing is cut off.
No text, no letters, no numbers. Plain flat pure white background, no shadow on the background.
Match the art style of the attached image exactly.
```

**Проверить:** футболка, джинсы, кроссовки. **Нет кепки и нет куртки** — на нём
строятся задания «I haven't got a cap» и «He hasn't got a jacket».

---

## av3 — девочка в куртке

```
A cheerful cartoon girl about eight years old, standing straight and facing the viewer,
arms relaxed down at her sides, feet together. Short dark bob haircut, warm brown skin,
friendly smile, no hat. She is wearing an open coral-pink zip-up jacket over a yellow
short-sleeve T-shirt, blue denim jeans, and white sneakers. The yellow T-shirt is clearly
visible in the middle under the open jacket.
Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated
colors, warm soft lighting from the top-left. Full body from head to toe, the whole figure
centred with clear empty margin above the head and below the feet so nothing is cut off.
No text, no letters, no numbers. Plain flat pure white background, no shadow on the background.
Match the art style of the attached image exactly.
```

**Проверить:** куртка (открытая, футболка видна), футболка, джинсы, кроссовки.
**Нет** кепки и юбки.

---

## av4 — мальчик в кепке

```
A cheerful cartoon boy about eight years old, standing straight and facing the viewer,
arms relaxed down at his sides, feet together. Light blond hair under the cap, friendly
smile. He is wearing a blue baseball cap worn straight with the peak forward, an orange
short-sleeve T-shirt, blue denim jeans, and red-orange sneakers with white soles. No jacket.
Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated
colors, warm soft lighting from the top-left. Full body from head to toe, the whole figure
centred with clear empty margin above the head and below the feet so nothing is cut off.
No text, no letters, no numbers. Plain flat pure white background, no shadow on the background.
Match the art style of the attached image exactly.
```

**Проверить:** кепка, футболка, джинсы, кроссовки. **Нет куртки** — на нём
задание «I have got a cap» и «He has got a cap».

---

## av5 — другой мальчик в кепке

Тот же состав одежды, что у av4, но это **другой ребёнок**: в задании они стоят
рядом, и их нужно различать с первого взгляда.

```
A cheerful cartoon boy about eight years old, standing straight and facing the viewer,
arms relaxed down at his sides, feet together. Dark curly hair under the cap, deep brown
skin, friendly smile. He is wearing a red baseball cap worn straight with the peak forward,
a light blue short-sleeve T-shirt, dark blue denim jeans, and grey sneakers. No jacket.
Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated
colors, warm soft lighting from the top-left. Full body from head to toe, the whole figure
centred with clear empty margin above the head and below the feet so nothing is cut off.
No text, no letters, no numbers. Plain flat pure white background, no shadow on the background.
Match the art style of the attached image exactly.
```

**Проверить:** кепка, футболка, джинсы, кроссовки. **Нет куртки** — на нём
задание «I haven't got a jacket». И он **не похож** на av4.

---

## av6 — девочка в гольфах

```
A cheerful cartoon girl about eight years old, standing straight and facing the viewer,
arms relaxed down at her sides, feet together. Light wavy blonde hair, friendly smile,
no hat. She is wearing a turquoise short-sleeve T-shirt, a yellow skirt down to the knees,
tall purple knee socks pulled up so they are clearly visible between the skirt and the
shoes, and white sneakers. No trousers and no jeans.
Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated
colors, warm soft lighting from the top-left. Full body from head to toe, the whole figure
centred with clear empty margin above the head and below the feet so nothing is cut off.
No text, no letters, no numbers. Plain flat pure white background, no shadow on the background.
Match the art style of the attached image exactly.
```

**Проверить:** футболка, юбка, **высокие гольфы видны**, кроссовки. **Нет
джинсов** — на ней задание «I haven't got jeans» и «She has got socks».

---

## av7 — Бен, мальчик в куртке

```
A cheerful cartoon boy about eight years old, standing straight and facing the viewer,
arms relaxed down at his sides, feet together. Short brown hair, friendly smile, no hat -
his hair is fully visible. He is wearing an open turquoise zip-up jacket over a yellow
short-sleeve T-shirt, blue denim jeans, and red-orange sneakers with white soles.
The yellow T-shirt is clearly visible in the middle under the open jacket.
Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated
colors, warm soft lighting from the top-left. Full body from head to toe, the whole figure
centred with clear empty margin above the head and below the feet so nothing is cut off.
No text, no letters, no numbers. Plain flat pure white background, no shadow on the background.
Match the art style of the attached image exactly.
```

**Проверить:** куртка (открытая, футболка видна), футболка, джинсы, кроссовки.
**Нет кепки** — на нём задание «He hasn't got a cap».

---

## av8 — девочка в кепке и джинсах

```
A cheerful cartoon girl about eight years old, standing straight and facing the viewer,
arms relaxed down at her sides, feet together. Long dark hair in two braids under the cap,
friendly smile. She is wearing a yellow baseball cap worn straight with the peak forward,
a pink short-sleeve T-shirt, blue denim jeans, and white sneakers. No skirt, no jacket.
Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated
colors, warm soft lighting from the top-left. Full body from head to toe, the whole figure
centred with clear empty margin above the head and below the feet so nothing is cut off.
No text, no letters, no numbers. Plain flat pure white background, no shadow on the background.
Match the art style of the attached image exactly.
```

**Проверить:** кепка, футболка, джинсы, кроссовки. **Нет юбки** — на ней задание
«I have got a skirt» с неправильным ответом, и «I have got jeans» с правильным.

---

## Когда картинки готовы

Положите восемь файлов в `assets/avatars/` и скажите мне — я прогоню
`python3 tools/embed_avatars.py`: он срежет белый фон, приведёт всех к одному
росту, вставит в Уроки 2, 3 и 4 и пересоберёт единый файл. Скрипт сам проверит,
что все восемь файлов на месте и что на картинке нет обрезанных краёв.
