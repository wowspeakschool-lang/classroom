# Go Getter 3 — что официальные тесты проверяют в каждом юните

Источник: папка Google Диска `go_getter_3_tests` (id `1LmYa_4MvJQeTeGyg_lOqjsgiNIvZT4hy`),
официальные тесты Pearson к учебнику Go Getter 3 (2019). Собрано 22.10.2026 при
вычитке тестов GG3. Программы курса в репозитории нет — этот файл её заменяет.

🔴 **Задания отсюда не переносятся.** Ограничение Анны: официальные тесты нужны
только для ответа на вопрос «попадает ли наш тест в то, что юнит должен
проверять». Ни формулировки, ни тексты, ни наборы вариантов не копируем.

## Что лежит в папке

Перечислено по `parentId` со сквозной прокруткой `nextPageToken` — папок больше,
чем видно на первой странице:

| папка | что внутри |
|---|---|
| `Language_tests` | по юниту, версии A и B: Vocabulary + Grammar + Communication, 30 баллов. Юнит 0 называется `GS` (Get started!) |
| `GrammarCheck`, `VocabularyCheck` | короткие проверки по юнитам |
| `Skills_tests` | на **пару** юнитов (1-2, 3-4, 5-6, 7-8): Listening, Communication, Reading, Writing |
| `Writing_tasks` | по одному письменному заданию на юнит, 70–80 слов |
| `Speaking_tasks` | говорение по юнитам |
| `Mid-Year_test` | тест за юниты 1–4 (словарь, грамматика, аудирование, communication, чтение) |
| `EndofYear_test`, `Exam_tests`, `Placement_tests` | итоговые и входные |
| `AnswerKey.pdf`, `GoGetter3_tests_Intro.pdf` | ключи и описание системы тестов |

**Устройство официальной проверки:** на каждый юнит — Language Test (лексика,
грамматика, communication) + Writing Task + Speaking Task; на каждые два юнита —
Skills Test (аудирование, чтение, письмо). То есть чтение, аудирование и письмо
в официальной системе есть в каждом юните, а у нас — только в юните 0 и в
Final Test.

## Юнит → что проверяется

### Unit 0 · Get started!
- **Лексика:** профессии (doctor, chef); места в городе (hospital, restaurant);
  транспорт (tram, bike); **школа — места** (library, canteen, gym, computer room,
  staff room) и **предметы** (Science, History, Geography); прилагательные с
  предлогами (interested in, worried about); **характер** (intelligent, kind);
  контейнеры (can, bottle, carton, packet, bar); еда (sugar, flour, butter,
  strawberries).
- **Грамматика:** Present Simple + наречия частотности; be going to;
  there is / there are + a / an / some / any.
- **Навыков (чтение, аудирование, письмо) в Language Test нет** — они идут
  отдельными файлами.

### Unit 1 · Life at home
- **Лексика:** домашние обязанности (feed the animals, water the plants, clear
  the table, load the dishwasher, vacuum, hang out the washing, make your bed);
  **характер** (easy-going, messy, organised, patient, bossy, quiet, loud).
- **Грамматика:** Present Continuous (+ вопросы, отрицания); Present Simple vs
  Present Continuous, в том числе глаголы состояния (understand, know, love).
- **Communication:** просьба и предложение помощи — Can you help me…?, Of course,
  I'm sorry, I can't, Do you need any help?, Can I help you?
- **Письмо:** 70–80 слов «что ты делаешь каждые выходные».

### Unit 2 · Shopping
- **Лексика:** покупки (shopping list, trolley, special offer, check the price,
  queue, pay by card / in cash, change); **названия магазинов** (chemist's, shoe
  shop, greengrocer's, newsagent's, baker's, clothes shop).
- **Грамматика:** сравнительная и превосходная степень; too / enough /
  (not) as … as.
- **Communication:** диалог в магазине одежды — Can I help you?, I'm looking
  for…, Do you have it in blue?, What size are you?, Can I try it on?, The
  changing rooms are over there.
- **Письмо:** письмо с сравнением двух товаров и тремя аргументами.

### Unit 3 · Going on holiday
- **Лексика:** отдых (guidebook, explore, day trip, guided tour, try the local
  food, go camping, go hiking); **get + прилагательное** (get wet, get tired,
  get cold, get bored, get lost).
- **Грамматика:** Past Simple — неправильные глаголы, отрицания, вопросы,
  was / were, короткие ответы.
- **Communication:** просьбы и разрешение — Can you…?, Could I…?, Can I borrow…?,
  No problem, Sorry, you can't, Not now.
- **Письмо:** письмо другу о прошедших каникулах (70–80 слов).

### Unit 4 · Useful things
- **Лексика:** приборы (DVD player, blender, USB stick, remote control, electric
  toothbrush, games console, toaster, microwave oven); **телефон** (turn on / off,
  battery, portable charger, touch screen, ringtone, apps).
- **Грамматика:** Past Continuous; Past Simple vs Past Continuous (when-
  предложения); **наречия образа действия** (well, badly, carefully, fast, angrily).
- **Communication:** сочувствие — You look upset, What happened?, I'm sorry to
  hear that, What's wrong?, That's a shame!
- **Письмо:** рассказ о случае из жизни (Past Continuous + Past Simple).

### Unit 5 · Health matters
- **Лексика:** болезни (temperature, headache, sore throat, runny nose, blocked
  nose, sneeze, cough); **травмы** (broken leg, bruise, burn, cut, mosquito bites);
  **тело, CLIL** (muscles, heart, blood, bones, brain).
- **Грамматика:** have to (все формы); should / shouldn't.
- **Communication:** совет — What's the matter?, You should…, Why don't you…?,
  Put some cream on it, That's a good idea, I think you should see a doctor.
- **Письмо:** советы «как быть здоровым» (70–80 слов).

### Unit 6 · Cooking and eating
- **Лексика:** глаголы готовки (boil, beat, add, slice, mix, fry, roast, bake);
  посуда (bowl, oven, pot, cake tin, glass, mug, pan, spoon, fork);
  **прилагательные вкуса** (delicious, sour, sweet, disgusting, spicy).
- **Грамматика:** Present Perfect — утверждение, отрицание, вопрос, короткий
  ответ, ever / never / yet.
- **Communication:** предпочтения — Would you like to…?, You choose, I don't mind,
  I'd like to…, I'd prefer.
- **Письмо:** рецепт по картинкам (ингредиенты, посуда, шаги).

### Unit 7 · Where I live
- **Лексика:** жильё (island, cottage, attic, village, block of flats, floor,
  stairs, balcony); в доме (bookcase, sink, mirror, tap, cupboard);
  **фразовые глаголы** (pick up, check out, clean up, look for, find out).
- **Грамматика:** Present Continuous для будущих договорённостей;
  must / mustn't / can.
- **Communication:** договориться о встрече — Do you want to…?, That sounds great,
  Are you free…?, I'd love to, Can you come?, Sorry, I can't.
- **Письмо:** письмо-приглашение на выходные (70–80 слов).

### Unit 8 · A happy life
- **Лексика:** планы на жизнь (be a writer, have an interesting job, learn
  foreign languages, live abroad, live on your own, have a family); приветствия
  (invite, shake hands, kiss, give a hug, visit); **вежливость** (arrive on time,
  be late, ask for permission, interrupt, wait your turn, polite).
- **Грамматика:** will (все формы); **вопросительные слова** в разных временах
  (Why, How often, What, Where, When, Who).
- **Communication:** согласие и несогласие — I agree, That isn't right, That's
  true, I don't think so, That's what I think too, I disagree.
- **Письмо:** предсказания о своей будущей жизни (70–80 слов).

### Mid-Year Test (юниты 1–4)
Отдельный тест: лексика и грамматика юнитов 1–4, аудирование, communication,
чтение. У нас такого теста нет — вопрос к Анне, нужен ли он.

## Названия юнитов

Темы дописаны в названия юнитов 22.10.2026 по соглашению из `CLAUDE.md`
(«Unit 5 · Clothes» — номер, ` · `, тема): `Unit 0 · Get started!`,
`Unit 1 · Life at home`, `Unit 2 · Shopping`, `Unit 3 · Going on holiday`,
`Unit 4 · Useful things`, `Unit 5 · Health matters`, `Unit 6 · Cooking and eating`,
`Unit 7 · Where I live`, `Unit 8 · A happy life`. Названия уроков остались
`Unit N Test`, юнит `Final Test` не трогали.
