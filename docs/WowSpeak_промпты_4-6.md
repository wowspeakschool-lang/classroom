# Промпты: лид-магнит 4–6 лет («Дорога на праздник»)

Мир: три плавучих острова, гид — **светлячок**, финал — яйцо в пещере.
Стиль тот же объёмный мультяшный, что в версии 7–9: версии должны выглядеть
роднёй. Всё горизонтальное.

## Как генерировать

1. **Первой сгенерируйте картинку №1** (фон карты). Она задаёт стиль.
   Строка «Match the art style of the attached image exactly» есть почти в каждом
   промпте — к каждому запросу надо что-то прикладывать. Что именно:

   | Что генерируем | Что прикрепить |
   |---|---|
   | №1 фон карты | ничего, это первая картинка |
   | №2 полянка (первый остров) | **фон карты** |
   | №3–4 остальные острова | **полянку** — она задаёт размер и ракурс |
   | №5 светлячок neutral | **фон карты** |
   | №6–8 светлячок smile / excited / lantern | **светлячка neutral** |
   | №9–13 предметы, пещера, яйцо | **фон карты** |
   | №14 зайчик | **светлячка neutral** — он задаёт лицо: глаза, щёчки, блеск |
   | №15–16 ёжик и лисёнок | **зайчика** — от него берётся рост |
   | №17 зверята двигают камень | **зайчика** |

   Правило простое: если у картинки есть глаза — прикрепляем героя, если нет —
   прикрепляем фон карты.
2. Сохраняйте **строго по именам** из заголовков, кладите в `assets/kids-4-6/`.
3. Под каждым промптом строка «проверить» — что должно быть на картинке.
   Генератор любит упирать фигуры в край: если макушка или ступни обрезаны,
   перегенерируйте.
4. Размеры: где написано **горизонталь** — 16:9 (как первая картинка), остальное 1024×1024.

## Одежду заново не рисуем

Пять вещей (a cap, a top, jeans, shoes, a skirt) уже нарисованы для версии 7–9
и лежат в `assets/lesson-1/`. Они в нужном стиле, их переносит скрипт. Рисовать
заново нечего — сэкономим вам полчаса.

---

## 1. map-background-wide — фон карты (горизонталь)

```
A wide empty background for a children's fantasy map, horizontal composition: a calm turquoise sea with soft rolling waves along the bottom third, a warm blue sky above with fluffy pink and lilac clouds, a few golden sparkles floating in the air, gentle morning light. The centre of the image is open and uncluttered so that islands can be placed on top later. No islands, no characters, no buildings, no text. Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colors, soft warm lighting from the top-left, chunky simple forms with no tiny details, friendly and safe for very young children.
```

**Проверить:** середина картинки пустая, никаких островов и героев.

---

## 2. island-meadow — Остров 1 (солнечная полянка)

```
A small floating island with a sunny green meadow, seen from a slight angle: soft green grass on top, a wooden washing line strung between two poles with a few colourful clothes pegged on it, small flowers, two round mushroom stools, and a rocky brown underside with earth and a couple of hanging roots, as if the island had been lifted out of the ground. The whole island is visible with clear empty margin around it. Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colors, soft warm lighting from the top-left. No characters, no text. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

**Проверить:** видна нижняя скалистая часть острова, остров не обрезан по краям,
фон чисто белый.

---

## 3. island-clouds — Остров 2 (облачный)

**Прикрепить: island-meadow** (принятую полянку). Острова должны быть одного
размера и с одного ракурса — иначе на карте они не встанут в ряд.

```
A small floating island made of soft fluffy clouds, seen from the same slightly raised angle as the island in the attached picture and drawn at the same size: a springy platform of white and pale pink cloud puffs with plump rounded edges, three or four smaller cloudlets floating around it, a pale rainbow ribbon curving over the top, tiny golden sparkles in the air. The platform reads as solid enough to stand on, with a clearly visible flat top surface. The whole island is visible with clear empty margin around it. Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colors, soft warm lighting from the top-left. No characters, no text. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

**Проверить:** облачный остров читается как площадка, на которую можно встать;
он того же размера, что полянка.

---

## 4. island-dragon — Остров 3 (остров Дракона, праздничный)

**Прикрепить две картинки: island-meadow и cave-closed.** Пещера с камнем на
острове должна быть той же, которую ребёнок потом увидит крупным планом.

```
A small floating island with warm sandy rock and green grass on top, seen from the same slightly raised angle as the green island in the attached picture and drawn at the same size, with the same rocky underside and a couple of hanging roots. The island is decorated for a party: strings of little colourful flags and glowing paper lanterns stretched above the grass, a low table with cupcakes and juice, soft cushions on the grass. On the right side of the island there is a cave entrance in warm sandy rock, blocked by a big round smooth pale cream-white boulder — exactly the cave and the boulder from the second attached picture, just smaller. The whole island is visible with clear empty margin around it. Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colors, soft warm lighting from the top-left. No characters, no text. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

**Проверить:** видны и праздник (флажки, фонарики), и вход в пещеру с камнем;
камень светлый, как на крупном плане; остров того же размера, что полянка.

---

## 5–7. Светлячок: три состояния

Сначала сгенерируйте **firefly-neutral**, потом **прикрепляйте именно его**
к запросам 6 и 7, чтобы это был один и тот же герой.

### 5. firefly-neutral

```
A tiny friendly cartoon firefly character, facing the viewer: a plump round body in soft yellow-green, two small arms, big kind dark eyes with light reflections, a gentle closed-mouth smile, two delicate translucent wings, and a rounded tail tip that glows warm golden like a little lantern. A few soft golden sparkles float around him. Head and body centred in the frame with clear empty margin around. Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colors, soft warm lighting from the top-left. No text. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

**Проверить:** светящийся кончик хвоста, добрые глаза, крылышки не обрезаны.

### 6. firefly-smile

```
Keep this exact character completely unchanged: same body, same colors, same wings, same glowing tail, same framing and scale, same art style, same lighting, same plain white background. Change only his expression: a warm open smile, eyes slightly narrowed with joy, as if he is encouraging a friend.
```

### 7. firefly-excited

```
Keep this exact character completely unchanged: same body, same colors, same wings, same glowing tail, same framing and scale, same art style, same lighting, same plain white background. Change only his expression and pose: delighted and excited, a big happy smile, wide bright eyes, both little arms raised up, his tail glowing brighter with a few extra golden sparkles around him.
```

---

## 8. firefly-lantern — светлячок светит в темноте (для пещеры)

```
The same tiny cartoon firefly character, now in the dark: his tail glows brightly like a lantern and casts a soft round pool of warm golden light around him, lighting his face from below. The background is deep dark blue-violet cave darkness with a few faint sparkles, no details visible. The character is centred with clear empty margin around him. Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes. No text. Match the art style of the attached image exactly.
```

**Проверить:** это тот же светлячок; фон тёмный (единственная картинка, где фон
не белый).

---

## 9. stone — волшебный камушек

```
A single magic pebble: a smooth rounded stone in soft turquoise with a pearly sheen, glowing gently from within, with a few tiny golden sparkles around it. One object centred in the frame with empty space around it, nothing else. Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colors, soft lighting from the top-left. No text. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

**Проверить:** камушек один, крупный, светится.

---

## 10. cloudlet — облачко-подушка

```
A single small fluffy cloud puff, soft white with pale pink edges, plump and springy like a pillow, with a few tiny golden sparkles around it. One object centred in the frame with empty space around it, nothing else. Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, soft lighting from the top-left. No face, no text. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

---

## 11. cave-closed — пещера с камнем

```
A cave entrance in warm sandy rock, blocked by a big round grey boulder that sits tightly in the opening; a few small stones and green tufts of grass at the base; a narrow dark gap visible at the top edge of the boulder, hinting at the darkness inside. The whole rock is visible with clear empty margin around it. Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colors, soft warm lighting from the top-left. No characters, no text. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

**Проверить:** понятно, что вход завален и внутри темно.

---

## 12. cave-open — пещера открыта, внутри гнездо

```
The same cave entrance in warm sandy rock, now open: the big round boulder has been rolled aside and rests next to the opening, and inside the cave a cosy nest of soft straw and colourful fabric is lit by a warm golden glow. The nest is empty. The whole rock is visible with clear empty margin around it. Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colors, soft warm lighting from the top-left. No characters, no text. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

**Проверить:** камень откатился и лежит рядом, гнездо пустое (яйцо — отдельной
картинкой).

---

## 13. egg — яйцо в гнезде (крупно)

```
A large speckled egg resting in a cosy nest: the egg is creamy white with soft turquoise and violet speckles and a gentle pearly shine, the nest is woven from straw with a few colourful fabric scraps and soft feathers tucked in, warm golden light falling on the egg from the top-left, a few sparkles in the air. One object centred in the frame with empty space around it, nothing else. Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colors. No characters, no text. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

**Проверить:** яйцо крупное и целое — не треснувшее; никого не видно внутри.

---

## 14–16. Зверята: зайчик, ёжик, лисёнок

Одна поза на всех троих — они стоят рядом в заданиях и должны быть одного роста.

### 14. animal-bunny

```
A cute cartoon bunny cub standing straight and facing the viewer, arms relaxed down at the sides, feet together: soft cream-white fur, long floppy ears, round cheeks, big friendly dark eyes, a small pink nose. No clothes at all. Full body from head to toe, the whole figure centred with clear empty margin above the head and below the feet. Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colors, soft warm lighting from the top-left. No text. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

### 15. animal-hedgehog

```
A cute cartoon hedgehog cub standing straight and facing the viewer, arms relaxed down at the sides, feet together: warm brown soft spines on the back and head, a lighter cream face and belly, round cheeks, big friendly dark eyes, a small dark nose. No clothes at all. Full body from head to toe, the whole figure centred with clear empty margin above the head and below the feet, drawn at the same height as the bunny in the attached image. Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colors, soft warm lighting from the top-left. No text. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

### 16. animal-fox

```
A cute cartoon fox cub standing straight and facing the viewer, arms relaxed down at the sides, feet together: warm orange fur with a white chest and white tail tip, pointed ears, round cheeks, big friendly dark eyes. No clothes at all. Full body from head to toe, the whole figure centred with clear empty margin above the head and below the feet, drawn at the same height as the bunny in the attached image. Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colors, soft warm lighting from the top-left. No text. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

**Проверить у всех троих:** без одежды, руки опущены, один рост, ступни и уши
не обрезаны.

---

## 17. friends-push — зверята двигают камень (горизонталь)

**Прикрепить две картинки: зайчика и cave-closed.** Валун должен быть тот же
самый, что лежит во входе в пещеру — светлый кремово-белый, а не серый.
Пещеру в кадр не берём: она у нас уже есть отдельной картинкой, а когда
генератор рисует её здесь, сцена не помещается в кадр и скалу срезает краем.

```
Three cute cartoon animal cubs — a cream-white bunny, a brown hedgehog and an orange fox, exactly the characters from the attached picture with the same fur colors and the same faces — pushing together against a big round smooth pale cream-white boulder with soft rounded facets, the same stone as in the second attached picture. The boulder has already started to roll aside and a narrow dark gap is visible behind it. Nothing else in the scene: no cave, no rock arch, no grass, only the three cubs, the boulder and the dark gap. All three lean into the boulder with their paws, cheerful and determined, a few effort sparkles around them. Horizontal composition, zoomed out so that every figure is complete, with a wide empty white margin on all four sides and nothing touching the edges of the frame. Bright 3D rendered cartoon style, Pixar-like, soft rounded glossy shapes, vivid saturated colors, soft warm lighting from the top-left. No text. Plain flat pure white background, no shadow on the background.
```

**Проверить:** ничего не упирается в край кадра; валун светлый, как у входа
в пещеру; это те же три зверька; камень уже сдвинулся, за ним видна щель.
