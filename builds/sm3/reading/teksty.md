# SM3, тесты юнитов 1–8 — чтение (READING) и диктант (DICTATION)

Решение Анны от 03.11.2026, пункт 63: в тестах Super Minds 3 юнитов 1–8 не было
разделов `reading` и `writing` — из шести разделов трекера прогресса два пустовали.
Добавлено по три блока в каждый тест:

| блок | тип | skill |
|---|---|---|
| материал для чтения (текст рассказа) | `text` | — (это материал) |
| «Верно или неверно?», пять утверждений | `truefalse` | `reading` |
| «DICTATION ✍️ Посмотри на картинку и напиши слово.», пять слов | `exact_input` | `writing` |

Образец — тест юнита 0 SM3 (`Test`, блоки 14–17 как в редакторе): там тот же
порядок разделов, та же форма заголовков и тот же состав диктанта (пять слов,
картинка + `accept` со строчным и прописным вариантом, `audio_tts` нет).

Правила, по которым собрано (CLAUDE.md):

* **порядок разделов как в тесте юнита 0**: лексика и грамматика → READING
  (текст + «верно / неверно») → LISTENING → DICTATION → SPEAKING;
* **диктант — картинка, а не звук**: `exact_input`, у пункта `image` и `accept`
  со строчным и прописным вариантом, `audio_tts` нет;
* **пять слов**, SM3 — третий курс, поэтому подсказок с пропущенными гласными
  нет: слово пишется целиком по картинке;
* **картинки только ссылками** на `https://classroom.wowteach.ru/media/sm3/uN/`,
  все файлы уже лежат в репозитории — генерировать ничего не нужно;
* лексика и грамматика — строго того юнита, для которого тест, ничего нового:
  юнит 5 держится на `was/were` (другого прошедшего в нём ещё нет), юниты 7–8 —
  Past Simple;
* текст для чтения **не повторяет сюжет аудирования того же теста** (аудирования
  — `builds/sm3/listening/teksty.md`): другой герой, другая ситуация;
* слова диктанта по возможности **не встречаются в тексте для чтения** того же
  теста, чтобы ребёнок не списывал написание.

Имена героев не заняты ни в SM3, ни в аудированиях: Clara, Bruno, Nadia, Leo,
Lara, Toby, Bella, Oscar.

## Сводка

| юнит | тема | текст для чтения (блок) | «верно / неверно» (блок) | диктант (блок) | пять слов диктанта |
|---|---|---|---|---|---|
| 1 | School | 12 | 13 | 15 | English · Geography · History · Science · Music |
| 2 | Food | 13 | 14 | 16 | cheese · lemonade · sausages · pineapple · vegetables |
| 3 | At home | 13 | 14 | 16 | vet · nurse · teacher · cleaner · firefighter |
| 4 | In the town | 13 | 14 | 16 | funfair · car park · lighthouse · skyscraper · clock tower |
| 5 | Under the sea | 13 | 14 | 16 | octopus · shark · jellyfish · shell · coral |
| 6 | Gadgets | 13 | 14 | 16 | tablet · lift · mobile phone · toothbrush · torch |
| 7 | At the doctor’s | 12 | 13 | 15 | cold · nurse · medicine · headache · toothache |
| 8 | Countries | 12 | 13 | 15 | India · Mexico · Chile · Spain · Australia |

Номера блоков — **как в редакторе** (`sort_order + 1`). Аудирование в каждом
тесте сдвинулось на два блока вниз, SPEAKING TASK — на три.

Заголовки одинаковые у всех восьми тестов:

* текст: «**READING.** Прочитай текст и ответь, верно или неверно.»
* задание: «Верно или неверно?»
* диктант: «DICTATION ✍️ Посмотри на картинку и напиши слово.»

---

## Unit 1 · School — Clara

Грамматика юнита: `Do/Does`, `like / love / hate + -ing`, `have to / has to`.
Лексика: школьные предметы, фигуры (Maths).

**Текст для чтения (69 слов):**

> Clara is nine years old and she goes to Hill Street School. On Monday she has Maths, Art and I.T. She loves drawing animals in her Art book. Clara doesn’t like studying History, but she likes reading about volcanoes in Science. She has to be on time for school every morning, but she doesn’t have to wear a uniform. After school Clara likes playing the guitar with her sister.

| № | утверждение | ключ |
|---|---|---|
| 1 | Clara goes to Hill Street School. | **верно** |
| 2 | On Monday Clara has Maths, Art and I.T. | **верно** |
| 3 | Clara likes studying History. | **неверно** |
| 4 | Clara has to wear a uniform. | **неверно** |
| 5 | After school Clara likes playing the guitar. | **верно** |

**Диктант, пять слов:**

| № | слово | картинка |
|---|---|---|
| 1 | English | `media/sm3/u1/subj_english.webp` |
| 2 | Geography | `media/sm3/u1/subj_geography.webp` |
| 3 | History | `media/sm3/u1/subj_history.webp` |
| 4 | Science | `media/sm3/u1/subj_science.webp` |
| 5 | Music | `media/sm3/u1/subj_music.webp` |

03.11.2026 диктант переделан с фигур (square · circle · triangle · rectangle ·
hexagon) на школьную лексику — тему юнита; решение Анны, пункт 69. Копия
старого блока — `classroom_backup_sm3_u1_diktant_20261103`.

Почему именно эти пять: из девяти предметов юнита `I.T.` и `P.E.` отпадают
(сокращения, писать нечего), `Art` и `Maths` — слишком короткие для диктанта
третьего курса. Из оставшихся `English`, `Geography` и `Music` в тесте больше
нигде не подписаны, а `History` и `Science` стоят подписанными в первом задании
(«соедини слова с картинками») и встречаются в тексте для чтения. Пяти слов
школьной темы без такого пересечения в юните не набирается — как в юнитах 2
и 7, пересечение оставлено.

---

## Unit 2 · Food — Bruno

Грамматика юнита: `there is / there are`, `some / any`, `have got`,
`Shall we…? · How about…? · I’d like…`.
Лексика: еда и напитки.

**Текст для чтения (74 слова):**

> Bruno is helping his mum in the kitchen. There are some onions and some peas on the table. There is some salad in the fridge, but there isn’t any soup. Bruno would like some apple juice, but there isn’t any at home, so he drinks some water. His sister says, “Shall we make some sandwiches?” There are five rolls for dinner. Bruno hasn’t got any chocolate, but he has got a big red apple.

| № | утверждение | ключ |
|---|---|---|
| 1 | There are some onions on the table. | **верно** |
| 2 | There is some soup in the fridge. | **неверно** |
| 3 | Bruno drinks some water. | **верно** |
| 4 | Bruno’s sister would like to make a cake. | **неверно** |
| 5 | There are five rolls for dinner. | **верно** |

**Диктант, пять слов:**

| № | слово | картинка |
|---|---|---|
| 1 | cheese | `media/sm3/u2/food_cheese.webp` |
| 2 | lemonade | `media/sm3/u2/food_lemonade.webp` |
| 3 | sausages | `media/sm3/u2/food_sausages.webp` |
| 4 | pineapple | `media/sm3/u2/food_pineapple.webp` |
| 5 | vegetables | `media/sm3/u2/food_vegetables.webp` |

🟥 Вся еда юнита 2 уже разобрана в первых двух заданиях теста («соедини слова
с картинками»), поэтому слова диктанта пересекаются с ними — как и в тесте
юнита 0, где слова диктанта стоят в тексте для чтения. Если нужно, заменим
на еду из других юнитов — скажите.

---

## Unit 3 · At home — Nadia

Грамматика юнита: `like + -ing`, время (`half past · quarter past · quarter to`),
наречия частотности (`always · sometimes · never`), `have to`.
Лексика: домашние дела, профессии.

**Текст для чтения (78 слов):**

> Nadia lives with her mum, her dad and her baby brother. On Tuesday and Friday she has to dry the dishes after dinner. Her dad cooks and her mum does the shopping on Sunday. Nadia never sweeps the floor, but she always tidies up her room before bed. She has dinner at quarter to seven and she reads a book at half past eight. On Saturday morning Nadia and her dad take the dog for a walk in the park.

| № | утверждение | ключ |
|---|---|---|
| 1 | Nadia has to dry the dishes on Tuesday and Friday. | **верно** |
| 2 | Nadia’s mum does the shopping on Sunday. | **верно** |
| 3 | Nadia always sweeps the floor. | **неверно** |
| 4 | Nadia has dinner at quarter to seven. | **верно** |
| 5 | On Saturday morning Nadia and her dad go to the cinema. | **неверно** |

**Диктант, пять слов:**

| № | слово | картинка |
|---|---|---|
| 1 | vet | `media/sm3/u3/job_vet.webp` |
| 2 | nurse | `media/sm3/u3/job_nurse.webp` |
| 3 | teacher | `media/sm3/u3/job_teacher.webp` |
| 4 | cleaner | `media/sm3/u3/job_cleaner.webp` |
| 5 | firefighter | `media/sm3/u3/job_firefighter.webp` |

Домашние дела — это глагольные фразы («take the dog for a walk»), писать их
в диктант тяжело; профессии того же юнита пишутся одним словом и в тесте
нигде не встречаются.

---

## Unit 4 · In the town — Leo

Грамматика юнита: предлоги места (`near · opposite · between · behind ·
in front of · above · below · under · next to`), `is going to the … to …`.
Лексика: город.

**Текст для чтения (76 слов):**

> Today is Saturday and Leo’s family is very busy. Leo is going to the sports centre to play basketball with his cousin. His mum is going to the market square to buy some fruit. His dad is going to the bus station to meet Grandma. The bus station is behind the big park, next to the bank. Leo’s sister is at home with the cat. The cat is under the table, in front of her ball.

| № | утверждение | ключ |
|---|---|---|
| 1 | Leo is going to the sports centre to play basketball. | **верно** |
| 2 | Leo’s mum is going to the supermarket. | **неверно** |
| 3 | The bus station is behind the big park. | **верно** |
| 4 | The bus station is next to the bank. | **верно** |
| 5 | The cat is above the table. | **неверно** |

**Диктант, пять слов:**

| № | слово | картинка |
|---|---|---|
| 1 | funfair | `media/sm3/u4/town_funfair.webp` |
| 2 | car park | `media/sm3/u4/town_car_park.webp` |
| 3 | lighthouse | `media/sm3/u4/tower_lighthouse.webp` |
| 4 | skyscraper | `media/sm3/u4/tower_skyscraper.webp` |
| 5 | clock tower | `media/sm3/u4/tower_clock.webp` |

Три слова — из урока про башни (cross-curricular этого же юнита), два — из
лексики города. Места, которые уже разобраны в первом задании теста (bank,
library, market, bus station, tower, map), в диктант не взяты.

---

## Unit 5 · Under the sea — Lara

Грамматика юнита: `was / were`, `there was / there were`, `wasn’t / weren’t`.
Другого прошедшего времени в юните ещё нет — текст держится на `was/were`.
Лексика: море и морские животные, места в городе.

**Текст для чтения (78 слов):**

> Last Saturday Lara and her class were at the sea museum. There were a lot of old boats in the first room and there was a big map of the ocean on the wall. Lara’s favourite room was the dinosaur room, because there was a megalodon tooth in it. The children were very quiet, so the teacher was happy. There weren’t any books about the sea in the museum shop. At four o’clock everybody was on the bus.

| № | утверждение | ключ |
|---|---|---|
| 1 | Last Saturday Lara was at the sea museum. | **верно** |
| 2 | There was a big map of the ocean on the wall. | **верно** |
| 3 | Lara’s favourite room was the boat room. | **неверно** |
| 4 | The children were very noisy. | **неверно** |
| 5 | At four o’clock everybody was on the bus. | **верно** |

**Диктант, пять слов:**

| № | слово | картинка |
|---|---|---|
| 1 | octopus | `media/sm3/u5/sea_octopus.webp` |
| 2 | shark | `media/sm3/u5/sea_shark.webp` |
| 3 | jellyfish | `media/sm3/u5/sea_jellyfish.webp` |
| 4 | shell | `media/sm3/u5/sea_shell.webp` |
| 5 | coral | `media/sm3/u5/sea_coral.webp` |

---

## Unit 6 · Gadgets — Toby

Грамматика юнита: сравнительная степень (`bigger · faster · cheaper ·
more expensive`), покупки (`How much is…?`, `I would like to buy it`).
Прошедшего времени в тексте нет — в юните 6 его ещё не проходили.
Лексика: гаджеты.

**Текст для чтения (75 слов):**

> Toby and his dad are in the gadget shop in the town. Toby would like a new games console, because his old console is slower than his friend’s console. The blue laptop is two hundred pounds — it is more expensive than the electric fan. The walkie-talkies are twenty pounds, and they are cheaper than the laptop. Toby’s favourite gadget is his bike, because it is faster than the bus in the morning.

| № | утверждение | ключ |
|---|---|---|
| 1 | Toby and his dad are in the gadget shop. | **верно** |
| 2 | Toby’s old console is faster than his friend’s console. | **неверно** |
| 3 | The blue laptop is more expensive than the electric fan. | **верно** |
| 4 | The walkie-talkies are cheaper than the laptop. | **верно** |
| 5 | Toby’s favourite gadget is his games console. | **неверно** |

**Диктант, пять слов:**

| № | слово | картинка |
|---|---|---|
| 1 | tablet | `media/sm3/u6/gad_tablet.webp` |
| 2 | lift | `media/sm3/u6/gad_lift.webp` |
| 3 | mobile phone (принимается и `phone`) | `media/sm3/u6/gad_phone.webp` |
| 4 | toothbrush (принимается и `electric toothbrush`) | `media/sm3/u6/gad_toothbrush.webp` |
| 5 | torch | `media/sm3/u6/gad_torch.webp` |

---

## Unit 7 · At the doctor’s — Bella

Грамматика юнита: Past Simple (`played · ate · drank · cooked · felt · watched ·
wrote · went`, отрицание `didn’t`).
Лексика: болезни, врач, привычки.

**Текст для чтения (79 слов):**

> Last Saturday Bella played football with her friends in the park. In the evening she had a stomachache, because she ate a lot of chocolate and drank two glasses of cola. Her dad cooked some soup, but Bella didn’t eat it. On Sunday morning she felt better. She watched a film with her brother and wrote a letter to her grandma. On Monday Bella went to school and played volleyball with her class again.

| № | утверждение | ключ |
|---|---|---|
| 1 | On Saturday Bella played football in the park. | **верно** |
| 2 | Bella drank two glasses of water. | **неверно** |
| 3 | Bella’s dad cooked some soup. | **верно** |
| 4 | On Sunday morning Bella felt worse. | **неверно** |
| 5 | On Monday Bella went to school. | **верно** |

**Диктант, пять слов:**

| № | слово | картинка |
|---|---|---|
| 1 | cold (принимается и `a cold`) | `media/sm3/u7/ill_cold.webp` |
| 2 | nurse | `media/sm3/u7/med_nurse.webp` |
| 3 | medicine | `media/sm3/u7/med_medicine.webp` |
| 4 | headache (принимается и `a headache`) | `media/sm3/u7/ill_headache.webp` |
| 5 | toothache (принимается и `a toothache`) | `media/sm3/u7/ill_toothache.webp` |

---

## Unit 8 · Countries — Oscar

Грамматика юнита: Past Simple, вопросы и отрицания с `did / didn’t`.
Лексика: страны и путешествия.

**Текст для чтения (77 слов):**

> Last summer Oscar went to Brazil with his family. They stayed with his uncle in a small house near the river for ten days. Oscar played football on the beach with his cousins every morning. One day they went on a boat on the Amazon river and they saw a lot of birds. Oscar didn’t see any monkeys, but he liked the boat a lot. He sent a postcard to his teacher.

| № | утверждение | ключ |
|---|---|---|
| 1 | Oscar went to Brazil last summer. | **верно** |
| 2 | Oscar and his family stayed in a big hotel. | **неверно** |
| 3 | Oscar played football every morning. | **верно** |
| 4 | Oscar saw a lot of monkeys. | **неверно** |
| 5 | Oscar sent a postcard to his teacher. | **верно** |

**Диктант, пять слов:**

| № | слово | картинка |
|---|---|---|
| 1 | India | `media/sm3/u8/country_india.webp` |
| 2 | Mexico | `media/sm3/u8/country_mexico.webp` |
| 3 | Chile | `media/sm3/u8/country_chile.webp` |
| 4 | Spain | `media/sm3/u8/country_spain.webp` |
| 5 | Australia | `media/sm3/u8/country_australia.webp` |

Те же картинки, по которым страны учили в ДЗ 1 (карточки и «посмотри на картинку
и напиши страну»), поэтому ребёнок узнаёт их без подписи.
