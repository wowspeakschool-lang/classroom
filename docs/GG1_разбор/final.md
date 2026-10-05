# GG1 · Final Test — разбор выгрузки ShkolaApp

Файл: `Go Getter 1 Final Test` (pdf `1jQdOqph9szCvtJf1gHh_NmPaFp-xIc5c`, 3.2 МБ, скачался; txt `1AuyesYZ_MsOPYD8iFhzQd0zAxS67y7VY`).
PDF — `$S/final/final_test.pdf`, текст по страницам — `$S/final/final_test.dump`, картинки — `$S/final/img/`.
Заливать отдельным юнитом `Final Test`, один урок, `kind='test'`, `pass_threshold=90`.

Похоже на формат Cambridge YLE **Starters** (Listening: «Lucy… Alex… Socks», «Listen and tick the box»; Reading & Writing: yes/no по картинке, спеллинг по картинке).

⚠️ **Главная проблема: в PDF финального теста почти нет картинок.** Распечатка от 14.08.2026 15:30 сделана, пока картинки не подгрузились: на их местах только кнопка удаления. Уцелели две: сцена гостиной к «Диаграмме» и значок радио. Пропали: варианты-картинки в шести вопросах Listening Part 3, картинки к восьми yes/no, сцена к yes/no Part 2, картинки к пяти заданиям на спеллинг. **Аудио нет ни одного** (плееры 00:00). 🟥

## Блоки по порядку

1. **Текст** «LISTENING» (красным).
2. **Медиафайл** — «Послушай аудио и выполни задания ниже.» — **аудио ПУСТОЕ** (Listening Part 1).
3. **Диаграмма** (точки на картинке) → `hotspot`/`match`: «Послушай аудио выше и расставь предметы по местам.»
   Картинка xref 220, 747×474, `img/final_test_220.png` — **рисованная гостиная** (женщина вяжет в синем кресле, второе кресло, книжный шкаф у окна, ковёр, столик с игрушечным роботом, тумба/шкафчик, дверь, картины на стене). Это иллюстрация из экзаменационного сборника, есть рисованный человек.
   Точек 6, места на картинке: ① полка книжного шкафа у окна, ② пол у правого края столика, ③ ковёр, ④ верх тумбы справа, ⑤ столик рядом с роботом, ⑥ картина на стене слева вверху.
   Варианты (подписи точек — картинки): №1 — **радио** (xref 221, 500×500, оранжевый магнитофон «B2B» с нотами, клипарт) → точка ①. Варианты №2–6 — **пустые** («Введите предложение», картинок нет). Лишних вариантов нет.
   🟥 Что ставится в точки ②–⑥, не восстановить: нет ни аудио, ни картинок вариантов.
   → у нас: блок `hotspot` по сцене без людей (`final_living_room`) + аудио и предметы от методиста; строкой в «доработать руками».
4. **Выбери правильный вариант** — «Послушай и выбери верный ответ.» С аудио, **аудио ПУСТОЕ** (Listening Part 2).
   Example: What is the girl's name? Lucy · How old is she? 7
   1. What is Lucy's friend's name? __Alex__ (✗ Bob, Mark)
   2. Which class are the two children in at school? __8__ (✗ 6, 7)
   3. How many dogs are there at Lucy's house? __3__ (✗ 2, 4)
   4. What's the name of Lucy's favourite dog? __Socks__ (✗ Sock, Sockes)
   5. How many fish has Lucy's friend got? __12__ (✗ 20, 11)
5. **Медиафайл** — «Послушай аудио и выполни задания ниже.» — **аудио ПУСТОЕ** (Listening Part 3).
6. **Тест** ×6, задание у каждого «Послушай аудио выше и выбери правильную картинку.» Варианты — **картинки, в выгрузке пустые**. Номер верного (у него нет пустого чекбокса, проверено кропом 2×):
   | вопрос | вариантов | верный № |
   |---|---|---|
   | What's Pat doing? | 3 | **3** |
   | Which is May? | 3 | **1** |
   | Which is Nick's favourite ice-cream? | 3 | **2** |
   | What's Ben doing? | 3 | **2** |
   | Where's Kim's doll? | 3 | **3** |
   | What's Dad doing? | 3 | **1** |
   🟥 Без аудио и картинок вопросы не восстановить. «What's Pat/Ben/Dad doing?» и «Which is May?» — по сути про людей (действия, внешность): генерировать нельзя. Ice-cream и кукла Ким — можно предметами. Решать методисту: найти исходник (Cambridge Starters sample test) или заменить блок.
7. **Текст** «READING AND WRITING» (красным).
8. **Выбери правильный вариант** ×8, «Посмотри на картинку и выбери верно (yes) или неверно (no)», варианты YES / NO. **Картинок нет.** Ответ = слово в пропуске (проверено на рендере):
   | утверждение | ответ |
   |---|---|
   | These are grapes. | YES |
   | This is a house. | NO |
   | It is a clock. | YES |
   | This is a sock. | NO |
   | These are chairs. | YES |
   | It is a television. | NO |
   | Her hair is wavy. | NO |
   | It is a spider. | YES |
   → у нас `truefalse` с картинкой у каждого утверждения. Для NO картинка показывает другой предмет. Предлагаю (СОСТАВ МОЙ): house → картинка `final_tree` или `final_car`; sock → `final_shoe`; television → `final_computer`/`final_radio`. «Her hair is wavy» требует человека → заменить на «The dog's hair is wavy.» с картинкой собачки с прямой шерстью (NO), или взять другое утверждение. 🟥
9. **Выбери правильный вариант** «Посмотри на картинку и выбери yes или no.» **Картинки нет** (по тексту — гостиная с семьёй: мужчина в очках, дети поют, женщина с напитками, кот, кресла, лампа, книжный шкаф, большое окно).
   Example: There are two armchairs in the living room. yes · The big window is open. no
   1. The man has got black hair and glasses. — **yes** (✗ no)
   2. There is a lamp on the bookcase. — **yes**
   3. Some of the children are singing. — **no**
   4. The woman is holding some drinks. — **yes**
   5. The cat is sleeping under an armchair. — **yes**
   🟥 Задание построено на людях (1, 3, 4). Без людей — переделать утверждения на предметы и животных в нашей сцене `final_living_room_cat` (кресла, окно, лампа на шкафу, кот под креслом, напитки на столе). Например: 1 There are two armchairs (yes), 2 There is a lamp on the bookcase (yes), 3 The cat is on the table (no), 4 There are some drinks on the table (yes), 5 The cat is sleeping under an armchair (yes). Строкой в «доработать руками».
10. **Составь предложение** ×5 — спеллинг по буквам (картинки потеряны, по смыслу «посмотри на картинку и собери слово»). Без инструкции.
    - b / u / t / t / e / r / f / l / y  → **butterfly** (в оригинале две t помечены t(1), t(2), чтобы плитки различались)
    - j / a / c / k / e / t → **jacket**
    - k / i / t / c / h / e / n → **kitchen**
    - w / h / a / l / e → **whale**
    - h / o / c / k / e / y → **hockey**
    → у нас `order` по буквам с картинкой и `audio_tts`.
Прощального блока нет.

## Для «доработать руками»
- Аудио Listening Part 1, 2, 3 (три записи) — в выгрузке нет. 🟥
- Диаграмма: предметы для точек ②–⑥ неизвестны.
- Listening Part 3: картинки вариантов (6 × 3) неизвестны, вопросы про людей.
- Reading Part 2: картинка гостиной потеряна, утверждения про людей — переписать (СОСТАВ МОЙ).
- «Her hair is wavy» — заменить.

## Нужны картинки (Final Test)
| key | к чему | что нарисовать |
|---|---|---|
| final_living_room | Диаграмма | гостиная без людей: два кресла, книжный шкаф у окна, ковёр, столик, тумба, картины на стене |
| final_radio | Диаграмма, вариант ① | радио/магнитофон (можно оставить клипарт xref 221) |
| final_grapes | yes/no | гроздь винограда |
| final_house_no | yes/no «house» → NO | дерево или машина (не дом) |
| final_clock | yes/no | настенные часы |
| final_sock_no | yes/no «sock» → NO | ботинок/кроссовка |
| final_chairs | yes/no | два-три стула |
| final_tv_no | yes/no «television» → NO | компьютер или радио |
| final_dog_wavy_no | вместо «Her hair is wavy» | собачка с прямой шерстью (если утверждение про собаку) |
| final_spider | yes/no (можно `gg1/u7/animal_spider`) | паук |
| final_living_room_cat | Reading Part 2 | гостиная с котом под креслом, лампой на шкафу, напитками на столе, закрытым большим окном |
| final_butterfly | спеллинг (можно `gg1/u7/animal_butterfly`) | бабочка |
| final_jacket | спеллинг | куртка |
| final_kitchen | спеллинг | кухня |
| final_whale | спеллинг (можно `gg1/u7/animal_whale`) | кит |
| final_hockey | спеллинг (можно `gg1/u8/sport_hockey`) | клюшка и шайба |
Итого новых картинок: **около 12** (из 16 строк четыре берутся из u7/u8), плюс картинки Listening Part 3, если методист найдёт исходник.
