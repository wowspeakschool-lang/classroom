# SM3, тесты юнитов 1–8 — аудирование (LISTENING)

Решение Анны от 03.11.2026: в тестах Super Minds 3 юнитов 1–8 добавлено
аудирование — по одному блоку `quiz` на тест (пять вопросов), `skill = listening`.

Правила, по которым собрано (CLAUDE.md):

* рассказ **только в третьем лице, без диалогов** — синтез читает одним
  мужским голосом (решение Анны от 20.10.2026);
* текст рассказа **на экране не показывается**, отдельного текстового блока нет;
* `audio` — пустая строка, `audio_tts` **не ставим** ни в блоке, ни в вопросах:
  иначе «Озвучить пачкой» затрёт место под запись (решение от 18.10.2026);
* озвучивает **Yandex SpeechKit** из отдельной сессии (решение от 20.10.2026),
  файл кладётся в бакет `classroom-media`, папка `sm3/`;
* лексика и грамматика — строго того юнита, для которого тест; ничего нового;
* имена героев не повторяют занятые в GG3 (Эмма, Оливер, Зои, Дэниел, Нина,
  Макс, Феликс, Руби, Элли) и в SM3 Unit 0 (Пенни).

Заголовок у всех восьми блоков одинаковый по форме:
«LISTENING 🎧 Послушай рассказ про <Имя> и выбери правильный ответ. Можно послушать два раза».

Блок стоит перед SPEAKING TASK — там же, где в тесте юнита 0 (после чтения,
перед диктантом и говорением; в тестах 1–8 чтения и диктанта нет).

## Что озвучить — сводка

| юнит | тема | блок (как в редакторе) | файл | герой |
|---|---|---|---|---|
| 1 | School | 14 | `sm3_u1_test_b14.mp3` | Milo (Майло) |
| 2 | Food | 15 | `sm3_u2_test_b15.mp3` | Freya (Фрея) |
| 3 | At home | 15 | `sm3_u3_test_b15.mp3` | Hugo (Хьюго) |
| 4 | In the town | 15 | `sm3_u4_test_b15.mp3` | Greta (Грета) |
| 5 | Under the sea | 15 | `sm3_u5_test_b15.mp3` | Otis (Отис) |
| 6 | Gadgets | 15 | `sm3_u6_test_b15.mp3` | Maisie (Мейзи) |
| 7 | At the doctor’s | 14 | `sm3_u7_test_b14.mp3` | Rufus (Руфус) |
| 8 | Countries | 14 | `sm3_u8_test_b14.mp3` | Tessa (Тесса) |

Ссылка, которую впишем в `audio` после записи:
`https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm3/<имя файла>`

---

## Unit 1 · School — Milo, блок 14, `sm3_u1_test_b14.mp3`

Грамматика юнита: `Do/Does`, `like/love/hate + -ing`, `have to / has to`.
Лексика: школьные предметы.

**Текст для записи (76 слов):**

> Milo is a pupil at Green Hill School. He likes studying Science and Art, but he doesn’t like Maths. His favourite subject is Geography, because he loves looking at maps. Milo has to wear a uniform to school every day. He doesn’t have to wear it on Saturday. After school he likes playing computer games with his friend. On Friday Milo has Music, and he hates singing. He has got nine books in his school bag.

| № | вопрос | варианты | верный |
|---|---|---|---|
| 1 | What is Milo’s favourite subject? | Geography · Science · Maths | **Geography** |
| 2 | Which subject does Milo NOT like? | Maths · Art · Geography | **Maths** |
| 3 | What does Milo have to wear to school? | a uniform · a hat · trainers | **a uniform** |
| 4 | What does Milo hate doing? | singing · dancing · swimming | **singing** |
| 5 | How many books has Milo got in his school bag? | nine · five · nineteen | **nine** |

---

## Unit 2 · Food — Freya, блок 15, `sm3_u2_test_b15.mp3`

Грамматика юнита: `there is / there are`, `some / any`, `have got`.
Лексика: еда и напитки.

**Текст для записи (79 слов):**

> Freya is making a picnic basket for her family. There are some rolls and some cheese in the basket. There is a big bottle of water, too. There aren’t any sausages, because Freya doesn’t like them. There is some salad with onions and peas. There isn’t any pineapple in the shop today, so Freya has got six apples. Her brother would like some lemonade, but there isn’t any lemonade in the fridge. There is some soup for dinner.

| № | вопрос | варианты | верный |
|---|---|---|---|
| 1 | Are there any sausages in the basket? | No, there aren’t. · Yes, there are. · Yes, there is. | **No, there aren’t.** |
| 2 | How many apples has Freya got? | six · seven · sixteen | **six** |
| 3 | What is there in the salad? | onions and peas · cheese and rolls · soup and water | **onions and peas** |
| 4 | What would Freya’s brother like? | some lemonade · some water · some soup | **some lemonade** |
| 5 | What is there for dinner? | some soup · some salad · some rolls | **some soup** |

---

## Unit 3 · At home — Hugo, блок 15, `sm3_u3_test_b15.mp3`

Грамматика юнита: время (`half past`, `quarter past`), наречия частотности
(`always · sometimes · never`), `like + -ing`, дни недели.
Лексика: домашние дела.

**Текст для записи (78 слов):**

> Hugo helps his family at home every day. He gets up at half past seven and has breakfast. He always takes the dog for a walk before school. After school Hugo tidies up his room, but he doesn’t like washing up. His sister washes up on Monday and Wednesday. Hugo likes sweeping the floor and he sometimes does the shopping with his mum on Saturday. He never feeds the cat. Hugo goes to bed at quarter past nine.

| № | вопрос | варианты | верный |
|---|---|---|---|
| 1 | What time does Hugo get up? | at half past seven · at quarter past seven · at half past nine | **at half past seven** |
| 2 | What does Hugo always do before school? | He takes the dog for a walk. · He does the shopping. · He washes up. | **He takes the dog for a walk.** |
| 3 | What doesn’t Hugo like doing? | washing up · sweeping the floor · tidying up his room | **washing up** |
| 4 | When does Hugo do the shopping? | on Saturday · on Monday · on Wednesday | **on Saturday** |
| 5 | What time does Hugo go to bed? | at quarter past nine · at quarter to nine · at half past nine | **at quarter past nine** |

---

## Unit 4 · In the town — Greta, блок 15, `sm3_u4_test_b15.mp3`

Грамматика юнита: предлоги места (`near · opposite · above · below · between`),
`is going to the … to …`.
Лексика: город.

**Текст для записи (85 слов):**

> Greta lives in a small town. Her house is opposite the library, and there is a big tower near the market square. On Monday Greta is going to the library to borrow a book about animals. The bank is between the supermarket and the car park. There is a big clock above the door of the bank. On Saturday Greta is going to the sports centre to go swimming with her friends. She has got a map of the town.

| № | вопрос | варианты | верный |
|---|---|---|---|
| 1 | What is opposite Greta’s house? | the library · the bank · the tower | **the library** |
| 2 | Where is the tower? | near the market square · opposite the library · between two trees | **near the market square** |
| 3 | Why is Greta going to the library on Monday? | to borrow a book · to go swimming · to buy some apples | **to borrow a book** |
| 4 | Where is the bank? | between the supermarket and the car park · near the bus station · opposite the tower | **between the supermarket and the car park** |
| 5 | Where is Greta going on Saturday? | to the sports centre · to the library · to the market square | **to the sports centre** |

---

## Unit 5 · Under the sea — Otis, блок 15, `sm3_u5_test_b15.mp3`

Грамматика юнита: `was / were`, `there was / there were`, `wasn’t / weren’t`.
Лексика: море и морские животные. Других прошедших времён в юните ещё нет —
рассказ держится на `was/were`.

**Текст для записи (76 слов):**

> Yesterday Otis was at the beach with his family. The water was warm. There were two dolphins near the boat and there was a big turtle on the sand. Otis’s sister was in the sea with her friend. There weren’t any jellyfish, so the children were happy. There was a starfish and a small seahorse in Otis’s bucket. The anchor of the old boat was under the water. At six o’clock Otis was in the café.

| № | вопрос | варианты | верный |
|---|---|---|---|
| 1 | Where was Otis yesterday? | at the beach · in the park · at school | **at the beach** |
| 2 | How many dolphins were there near the boat? | two · three · twelve | **two** |
| 3 | Were there any jellyfish? | No, there weren’t. · Yes, there were. · Yes, there was. | **No, there weren’t.** |
| 4 | What was in Otis’s bucket? | a starfish and a seahorse · a turtle and a seal · a dolphin and a shell | **a starfish and a seahorse** |
| 5 | Where was Otis at six o’clock? | in the café · in the sea · in a boat | **in the café** |

---

## Unit 6 · Gadgets — Maisie, блок 15, `sm3_u6_test_b15.mp3`

Грамматика юнита: сравнительная степень (`bigger · faster · more expensive ·
friendlier · stronger`).
Лексика: гаджеты.

**Текст для записи (81 слово):**

> Maisie has got a lot of gadgets at home. Her new tablet is bigger than her mobile phone, but her laptop is bigger than the tablet. Maisie thinks her games console is more exciting than her digital radio. Her small torch is cheaper than the electric fan. Maisie’s walkie-talkies are louder than her phone. Her favourite gadget is her laptop, because it is faster than the old computer in the kitchen. The lift in her building is slower than the stairs.

| № | вопрос | варианты | верный |
|---|---|---|---|
| 1 | Is Maisie’s tablet bigger than her mobile phone? | Yes, it is. · No, it isn’t. · Yes, it does. | **Yes, it is.** |
| 2 | What is bigger than the tablet? | the laptop · the mobile phone · the torch | **the laptop** |
| 3 | What is Maisie’s favourite gadget? | her laptop · her games console · her torch | **her laptop** |
| 4 | Which gadget is cheaper than the electric fan? | the torch · the laptop · the tablet | **the torch** |
| 5 | What is slower than the stairs? | the lift · the electric fan · the digital radio | **the lift** |

---

## Unit 7 · At the doctor’s — Rufus, блок 14, `sm3_u7_test_b14.mp3`

Грамматика юнита: Past Simple (`woke · felt · watched · played · wrote ·
listened · cooked · went · had · was/were`).
Лексика: болезни и врач.

**Текст для записи (80 слов):**

> Last week Rufus felt very ill. On Monday he woke up with a bad headache and a cough. His mum phoned the doctor. The doctor looked at Rufus and talked to his mum about the medicine. On Tuesday Rufus had a stomachache, so he stayed at home and watched TV. His sister cooked some soup for him. On Wednesday Rufus felt better. He listened to music and wrote a letter to his friend. On Thursday he went to school again.

| № | вопрос | варианты | верный |
|---|---|---|---|
| 1 | What did Rufus have on Monday? | a headache and a cough · a stomachache · an earache | **a headache and a cough** |
| 2 | Who phoned the doctor? | his mum · his sister · the nurse | **his mum** |
| 3 | What did Rufus do on Tuesday? | He watched TV. · He went to school. · He played football. | **He watched TV.** |
| 4 | Who cooked some soup for Rufus? | his sister · his mum · the doctor | **his sister** |
| 5 | When did Rufus go to school again? | on Thursday · on Tuesday · on Wednesday | **on Thursday** |

---

## Unit 8 · Countries — Tessa, блок 14, `sm3_u8_test_b14.mp3`

Грамматика юнита: Past Simple, вопросы и отрицания с `did / didn’t`
(`Did you have fun…?`, `How long did she stay…?`, `send postcards`).
Лексика: страны и путешествия.

**Текст для записи (80 слов):**

> Last summer Tessa went to Egypt with her family. They stayed in a small hotel near the sea for two weeks. Tessa saw the pyramids and she had a lot of fun. She didn’t go to the museum, because it was closed on Monday. Her brother played football on the beach every day. They ate fish and rice every evening. Tessa sent five postcards to her friends. She didn’t swim in the sea, but she liked the hotel a lot.

| № | вопрос | варианты | верный |
|---|---|---|---|
| 1 | Where did Tessa go last summer? | to Egypt · to Spain · to China | **to Egypt** |
| 2 | How long did they stay in the hotel? | two weeks · two days · two months | **two weeks** |
| 3 | Did Tessa go to the museum? | No, she didn’t. · Yes, she did. · No, she wasn’t. | **No, she didn’t.** |
| 4 | How many postcards did Tessa send? | five · four · fifteen | **five** |
| 5 | What did they eat every evening? | fish and rice · pizza and salad · soup and rolls | **fish and rice** |
