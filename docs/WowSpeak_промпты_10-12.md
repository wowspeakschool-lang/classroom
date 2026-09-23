# Промпты: лид-магнит 10–12 лет («Застрял в игре»)

Мир: ребёнок попал внутрь игры, выход заблокирован. На каждом уровне сканер
проверяет твой скин по описанию — чтобы пройти, надо собрать аватара и описать
его по-английски. Стиль неоновый, игровой, **ничего сказочного**. Всё
горизонтальное.

## Как генерировать

1. **Первой сгенерируйте картинку №1** — она задаёт неоновый стиль всему
   комплекту. Дальше **прикрепляйте её к каждому следующему запросу** и
   оставляйте строку «Match the art style of the attached image exactly».
2. Имена файлов — из заголовков, папка `assets/teens-10-12/`.
3. Размеры: **горизонталь** — 1536×1024, предметы и персонажи — 1024×1024.
4. У предметов и персонажей фон **чисто белый** — его срежет скрипт. У сцен
   фон рисованный, белый не нужен.

---

## 1. bg-plaza — ключевая картинка стиля: цифровая площадь (горизонталь)

```
A wide digital game world plaza seen from eye level, horizontal composition: a dark indigo and deep violet space with a glowing cyan grid floor stretching to the horizon, tall abstract neon skyline shapes in magenta and cyan in the distance, floating translucent holographic UI panels with blank glowing frames, soft particle sparks in the air, subtle scanlines over everything. The centre of the image is open and uncluttered. Modern neon cyber game-interface art style: high contrast, crisp clean vector shapes, magenta-cyan glow, holographic sheen, a hint of pixel-art accents. Cool and stylish, not childish, not fairy-tale. No characters, no text, no letters, no numbers, no logos.
```

**Проверить:** середина пустая, никаких надписей и цифр, стиль «интерфейс игры»,
а не киберпанк-город с людьми.

---

## 2. bg-wardrobe — Уровень 1: гардеробная (горизонталь)

```
A wide neon inventory room inside a game, horizontal composition: glowing racks and shelves along the walls holding blank holographic garment slots, a round platform in the centre lit from below with a cyan ring of light, floating empty UI frames on both sides, soft particles in the air. The centre platform is empty and open. Modern neon cyber game-interface art style, dark indigo background, magenta-cyan glow, crisp vector shapes. No characters, no text, no letters, no numbers. Match the art style of the attached image exactly.
```

---

## 3. bg-gate — Уровень 2: турникет-сканер (горизонталь)

```
A wide neon security gate inside a game, horizontal composition: two tall glowing pillars forming a doorway, a horizontal scanning beam of cyan light sweeping across the opening, a hovering scanner eye above the gate, a blank holographic panel beside the gate, glowing floor markings leading up to it. Beyond the gate the space is dark and unknown. Modern neon cyber game-interface art style, dark indigo background, magenta-cyan glow, crisp vector shapes. No characters, no text, no letters, no numbers. Match the art style of the attached image exactly.
```

---

## 4. bg-crowd — Уровень 3: площадь с игроками (горизонталь)

```
A wide neon meeting plaza inside a game, horizontal composition: a broad circular floor with a glowing cyan ring pattern, holographic direction arrows hovering in the air, distant silhouettes of other players rendered as faint dark shapes with neon outlines far in the background, floating UI panels around the edges. The foreground is open and empty. Modern neon cyber game-interface art style, dark indigo background, magenta-cyan glow, crisp vector shapes. No readable faces, no text, no letters, no numbers. Match the art style of the attached image exactly.
```

---

## 5. bg-exit — Уровень 4: портал выхода (горизонталь)

```
A wide neon exit portal inside a game, horizontal composition: a tall oval portal of swirling cyan and white light standing on a raised platform, magenta warning glow spilling from cracks in the floor around it, broken glitched fragments of the floor floating in the air nearby, dramatic light. The area in front of the portal is open and empty. Modern neon cyber game-interface art style, dark indigo background, magenta-cyan glow, crisp vector shapes. No characters, no text, no letters, no numbers. Match the art style of the attached image exactly.
```

---

## 6. boss-glitch — босс-Глитч

```
A menacing but not scary game boss made of corrupted data: a floating humanoid shape assembled from shifting pixel blocks and broken polygons, magenta and cyan glitch bands tearing across its body, hollow glowing eyes, fragments breaking off and drifting around it. It looks like a video-game error come to life. Full figure centred with clear empty margin around it. Modern neon cyber game-interface art style, high contrast, crisp vector shapes with pixel-art fragments. No text, no letters, no numbers. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

**Проверить:** не пугающий монстр, а «сбой в игре»: пиксели, полосы, обломки.

---

## 7. mannequin — голограмма-аватар (основа для сборки образа)

```
A neutral holographic mannequin figure standing straight and facing the viewer, arms relaxed down at the sides, feet together: a stylised genderless teenage body made of translucent cyan light with a soft inner glow and thin bright contour lines, no face features, no hair, no clothes. Full body from head to toe, centred with clear empty margin above the head and below the feet. Modern neon cyber game-interface art style. No text, no letters, no numbers. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

**Проверить:** фигура ровно по центру, руки опущены, ноги вместе — на неё будут
накладываться вещи.

---

## 8–15. Восемь вещей — иконки инвентаря

Все восемь рисуются **одинаково**: предмет анфас, как иконка в инвентаре игры.
Прикрепляйте к каждому запросу картинку №8, когда она готова, — так комплект
получится одинаковым.

Общий хвост для всех восьми (уже вписан в каждый промпт):
`Single object centred in the frame, seen straight from the front like a game inventory icon, with clear empty margin around it. Modern neon cyber game-interface art style: crisp clean shapes, subtle magenta-cyan rim glow along the edges, slight holographic sheen. No text, no letters, no numbers, no brand logos. Plain flat pure white background, no shadow on the background.`

### 8. item-hoodie
```
A dark grey hoodie with the hood up empty, drawstrings hanging, a thin cyan neon line along the seams. Single object centred in the frame, seen straight from the front like a game inventory icon, with clear empty margin around it. Modern neon cyber game-interface art style: crisp clean shapes, subtle magenta-cyan rim glow along the edges, slight holographic sheen. No text, no letters, no numbers, no brand logos. Plain flat pure white background, no shadow on the background.
```

### 9. item-tshirt
```
A plain black T-shirt with short sleeves and a thin magenta neon line along the collar and sleeve hems. Single object centred in the frame, seen straight from the front like a game inventory icon, with clear empty margin around it. Modern neon cyber game-interface art style: crisp clean shapes, subtle magenta-cyan rim glow along the edges, slight holographic sheen. No text, no letters, no numbers, no brand logos. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

### 10. item-jeans
```
A pair of dark blue jeans laid out straight, front view, with a thin cyan neon line along the side seams. Single object centred in the frame, seen straight from the front like a game inventory icon, with clear empty margin around it. Modern neon cyber game-interface art style: crisp clean shapes, subtle magenta-cyan rim glow along the edges, slight holographic sheen. No text, no letters, no numbers, no brand logos. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

### 11. item-shorts
```
A pair of dark grey sports shorts, front view, with a thin magenta neon stripe down each side. Single object centred in the frame, seen straight from the front like a game inventory icon, with clear empty margin around it. Modern neon cyber game-interface art style: crisp clean shapes, subtle magenta-cyan rim glow along the edges, slight holographic sheen. No text, no letters, no numbers, no brand logos. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

### 12. item-sneakers
```
A pair of white high-top sneakers standing side by side, front view, with glowing cyan soles and thin neon accents on the laces. Single object centred in the frame, seen straight from the front like a game inventory icon, with clear empty margin around it. Modern neon cyber game-interface art style: crisp clean shapes, subtle magenta-cyan rim glow along the edges, slight holographic sheen. No text, no letters, no numbers, no brand logos. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

### 13. item-cap
```
A black baseball cap seen straight from the front, peak forward, with a thin cyan neon line along the peak edge. Single object centred in the frame, seen straight from the front like a game inventory icon, with clear empty margin around it. Modern neon cyber game-interface art style: crisp clean shapes, subtle magenta-cyan rim glow along the edges, slight holographic sheen. No text, no letters, no numbers, no brand logos. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

### 14. item-scarf
```
A knitted scarf in deep violet, laid in a soft loop, with thin magenta neon threads woven through it. Single object centred in the frame, seen straight from the front like a game inventory icon, with clear empty margin around it. Modern neon cyber game-interface art style: crisp clean shapes, subtle magenta-cyan rim glow along the edges, slight holographic sheen. No text, no letters, no numbers, no brand logos. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

### 15. item-dress
```
A simple sleeveless dress in deep teal, front view, knee length, with a thin cyan neon line along the hem and neckline. Single object centred in the frame, seen straight from the front like a game inventory icon, with clear empty margin around it. Modern neon cyber game-interface art style: crisp clean shapes, subtle magenta-cyan rim glow along the edges, slight holographic sheen. No text, no letters, no numbers, no brand logos. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

---

## 16–21. Шесть игроков для задания «найди игрока по описанию»

Одна поза и один рост у всех шестерых: они стоят рядом в задании. Сгенерируйте
первого, дальше прикрепляйте его как образец.

Общая часть: `A stylised teenage game avatar standing straight and facing the viewer, arms relaxed down at the sides, feet together, seen full body from head to toe, centred with clear empty margin above the head and below the feet. Simplified face with no strong features, neon rim light along the silhouette. Modern neon cyber game-interface art style. No text, no letters, no numbers, no brand logos. Plain flat pure white background, no shadow on the background.`

| Файл | Что надето |
|---|---|
| **16. player-1** | серый худи, синие джинсы, белые кроссовки, короткие тёмные волосы |
| **17. player-2** | чёрная футболка, серые шорты, белые кроссовки, рыжие волосы |
| **18. player-3** | бирюзовое платье, белые кроссовки, длинные тёмные волосы |
| **19. player-4** | чёрная кепка, чёрная футболка, синие джинсы, светлые волосы |
| **20. player-5** | фиолетовый шарф, серый худи, синие джинсы, кудрявые волосы |
| **21. player-6** | чёрная кепка, бирюзовое платье, белые кроссовки, тёмные волосы |

Пример промпта для №16 (остальные — та же формула, меняется только одежда):

```
A stylised teenage game avatar standing straight and facing the viewer, arms relaxed down at the sides, feet together, wearing a dark grey hoodie, blue jeans and white high-top sneakers, with short dark hair. Seen full body from head to toe, centred with clear empty margin above the head and below the feet. Simplified face with no strong features, neon rim light along the silhouette. Modern neon cyber game-interface art style. No text, no letters, no numbers, no brand logos. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

**Проверить у всех шести:** одинаковый рост и поза, одежда ровно из таблицы —
по ней ребёнок будет искать нужного игрока, лишняя вещь ломает задание.

---

## 22. badge-pass — пропуск-ачивка

```
A glowing hexagonal game achievement badge: a holographic cyan hexagon with a thick magenta neon rim, a simple keyhole symbol glowing in the centre, light particles drifting around it. Single object centred in the frame with clear empty margin around it. Modern neon cyber game-interface art style. No text, no letters, no numbers. Plain flat pure white background, no shadow on the background. Match the art style of the attached image exactly.
```

---

## 23. certificate-bg — фон именного пропуска (горизонталь)

```
A wide empty holographic certificate panel, horizontal composition: a translucent dark indigo card with a bright cyan neon frame, softly glowing corners, faint grid texture inside, small light particles around the edges. The inside of the panel is completely empty so that a name can be placed there later. Modern neon cyber game-interface art style. No text, no letters, no numbers, no seals, no signatures. Match the art style of the attached image exactly.
```

**Проверить:** внутри панели пусто — имя впишет код.
