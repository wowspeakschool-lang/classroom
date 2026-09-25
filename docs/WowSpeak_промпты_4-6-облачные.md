# Промпты 4–6: пять предметов для Облачного Острова

Нужны, чтобы в Уроке 2 цвета отрабатывались не на тех же мячике, машинке и
чашке, что в Уроке 1. Эти — «небесные», под остров из облаков.

**К каждому запросу прикладывайте светлячка** (`assets/kids-4-6/firefly-neutral.webp`) —
он задаёт объём, блеск и мягкий свет. Сохранять строго по именам из
заголовков, класть в `assets/kids-4-6/`.

**Рисуете каждый предмет один раз, в любом цвете.** В зелёный, синий и
жёлтый его перекрасит скрипт — и тогда зелёный на змее, на топе и на кляксе
будет одним и тем же зелёным. Если рисовать три раза, они разойдутся, и на
уроке цветов ребёнок запутается.

**Важно про цвет.** Скрипт красит господствующий цвет предмета. Поэтому у
предмета должен быть **один явный основной цвет** и максимум одна-две мелкие
детали другого — они останутся как есть (у машинки так остались синие стёкла).

Общее правило проверки: фигура не упирается в край, вокруг есть поле, фон
чисто белый, тени под предметом нет.

---

## 1. obj-kite — воздушный змей

```
A simple diamond-shaped toy kite seen from the front, with a short curly tail
made of three small bows. One plain bright colour over the whole kite, a thin
lighter cross-frame. Cute chunky 3D cartoon render for small children, smooth
glossy surfaces, soft rounded shapes, bright and friendly. Plain flat pure white
background, absolutely no shadow under the object, generous margin around the
whole shape. Single object, centred. No text, no letters, no numbers.
```

**Проверить:** змей одного цвета, хвост не уезжает за край.

---

## 2. obj-bird — птичка

```
A tiny plump cartoon bird sitting facing the viewer, small wings folded, big
friendly eyes, a small orange beak. The whole body is one plain bright colour;
only the beak and feet are orange. Cute chunky 3D cartoon render for small
children, smooth glossy surfaces, soft rounded shapes, bright and friendly.
Plain flat pure white background, absolutely no shadow under the object,
generous margin around the whole shape. Single object, centred. No text, no
letters, no numbers.
```

**Проверить:** тело одного цвета, клюв и лапки оранжевые — они останутся
оранжевыми во всех трёх вариантах, это нормально.

---

## 3. obj-umbrella — зонтик

```
A small open umbrella seen from the side, dome-shaped canopy, a short curved
handle. The canopy is one plain bright colour all over, no stripes, no
segments in a different colour; the handle is light wood. Cute chunky 3D
cartoon render for small children, smooth glossy surfaces, soft rounded
shapes, bright and friendly. Plain flat pure white background, absolutely no
shadow under the object, generous margin around the whole shape. Single
object, centred. No text, no letters, no numbers.
```

**Проверить:** купол **без полосок** — полосатый зонтик перекрасится пятнами.

---

## 4. obj-star — звёздочка

```
A plump five-pointed star with softly rounded tips, seen from the front, with a
small glossy highlight. One plain bright colour over the whole star. Cute chunky
3D cartoon render for small children, smooth glossy surfaces, soft rounded
shapes, bright and friendly. Plain flat pure white background, absolutely no
shadow under the object, generous margin around the whole shape. Single object,
centred. No text, no letters, no numbers.
```

**Проверить:** лучи с круглыми кончиками, не острые.

---

## 5. obj-plane — самолётик

```
A tiny toy aeroplane seen from the side at a slight angle, short stubby wings,
a rounded nose, a small tail fin. The body and wings are one plain bright
colour; only the round window and the propeller are light grey. Cute chunky 3D
cartoon render for small children, smooth glossy surfaces, soft rounded shapes,
bright and friendly. Plain flat pure white background, absolutely no shadow
under the object, generous margin around the whole shape. Single object,
centred. No text, no letters, no numbers.
```

**Проверить:** корпус и крылья одного цвета, иллюминатор серый.

---

## Что будет дальше

Как пришлёте — скрипт вырежет фон, перекрасит каждый в три цвета и положит в
Урок 2 вместо предметов первого урока. Превью каждой обработанной картинки
пришлю до сборки.
