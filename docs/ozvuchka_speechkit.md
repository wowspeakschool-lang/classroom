# Аудирования через Yandex SpeechKit — что осталось озвучить

Задача для сессии, у которой есть ключ Яндекса (домен `tts.api.cloud.yandex.net`,
`YANDEX_API_KEY`, `YANDEX_FOLDER_ID`). Поставлена Анной 20.10.2026.

**Почему не «Озвучить пачкой».** В этих блоках намеренно **нет** `audio_tts`:
кнопка синтеза (Piper) нашла бы такую пару и затёрла место под нормальную
запись. Поэтому у блока стоит пустой `audio`, а текст лежит отдельно — здесь и
в сборке. Ставить `audio_tts` в блок аудирования нельзя.

**Как делать.** Английский голос SpeechKit, одна дорожка на текст. Между
предложениями пауза ~1 с; если в тексте есть «Number N», перед ним ~2 с.
Готовый mp3 кладётся в бакет `classroom-media` (папка курса), после чего
ссылка вписывается в поле `audio` блока и проверяется, что запись играет.

**Словарь подмен — применять при каждом синтезе** (проверено 05.11.2026).
SpeechKit (голос `john`, en-US) читает часть слов неправильно. Подмена делается
**только в тексте, который уходит в синтез**: текст в документе и в сборке не
меняется, ребёнок его не видит, произносимое слово то же.

| слово | как читает SpeechKit | писать для синтеза |
|---|---|---|
| headache · stomachache · toothache · earache | «хэдэч», «стомачэч» — `ch` как «ч» | head ake · stomak ake · tooth ake · ear ake |
| cough | «cuff» | coff |
| TV | «div», «to» (и `T V`, `T.V.` тоже) | tee vee |
| recipe | «rasik» | ressipee |
| café, cafe | «calf», «cave» | caffay |
| anchor | «answer» | anker |
| library (в конце фразы) | «livery» | lybrary |
| bowl | «ball» | bowle |
| Liam | «Lime», «Lam» | Leeam |
| Jim | «Yim» | Jimm |
| Amy | «Emma» — как контрольное `Emma` | Aymee |
| Zoe | «so» | Zowee |
| Iris | «Eris» | Eyeris |
| Ada | «Adda» | Ayda |
| Ava | «ever», как контрольное `Eva` | Ayva |
| Dylan | «Dailan» | Dillan |
| Nina | «Nenah» | Neena |
| queue | «kui» | kew |
| karate | «carry it» | ka-rah-tee |
| laughed | «left» | larfed |
| bus (в конце фразы) | «buzzer» | buss |
| lives · live (жить) | «лайвз», «лайв» — читает как live «живой» | livz · liv |
| Geography | странное, не «джиогрэфи» | Jeeography |
| Oliver | «a lever»; неправильное ударение и гласная | Olivver |
| Ellie | то «элли», то «эллай» (распознаётся «L.A.») | Elly |

**Заглавные буквы и дефисы в подмене SpeechKit читает по буквам** (проверено
06.11.2026): `EL-lee` звучит как «L Lee», `Jee-OG-ra-fee` — как «G O G rafi»,
в `OLL-i-ver` появляется пауза. Поэтому в таблице для синтеза — слитные
написания без капса: `Elly`, `Jeeography`, `Olivver`. Прежняя подмена `Olliver`
тоже была плохой — распознаётся «I'll ever».

Шесть строк снизу нашла Анна 06.11.2026, прослушав новые аудирования:
«lives через ai, хотя тут имеется в виду „живёт"», «странное произношение
в слове Geography», «Oliver — неправильно имя произносит», «Ellie иногда
правильно, а иногда эллай говорит».

**Под перезапись из-за произношения — шесть файлов** (версия `_v3`):

| блок | файл | что чинит |
|---|---|---|
| GG3 Unit 1 Test, блок 9 | `gg3_u1_test_b9_v3.mp3` | Oliver |
| GG3 Unit 7 Test, блок 10 | `gg3_u7_test_b10_v3.mp3` | lives · live |
| GG3 Unit 8 Test, блок 9 | `gg3_u8_test_b9_v3.mp3` | live · Ellie |
| SM3 Unit 1 Test, блок 7 | `sm3_u1_test_b7_v3.mp3` | Geography |
| SM3 Unit 4 Test, блок 7 | `sm3_u4_test_b7_v3.mp3` | lives |
| SM3 Unit 9 Test, блок 7 | `sm3_u9_test_b7_v3.mp3` | lives |

Тексты у них прежние — те, что в `builds/listening_v2/teksty.py`. Меняется
только написание для синтеза по таблице выше. Ссылки в блоках уже переставлены
на `_v3`, так что достаточно положить файлы в бакет под этими именами.

Как нашли: каждую запись прогоняли через распознавание речи (faster-whisper
`small.en`) и сверяли с текстом; подозрительное слово синтезировали отдельно в
нескольких написаниях и брали то, которое распознаётся верно. «ache» сверх
того проверен по спектру: у `headache` на конце 80 мс шипения, как в `match`,
у `head ake` — короткий взрыв 20–30 мс, как в `make`. Расхождения вида
grey/gray, цифры вместо чисел и написание имён — особенность распознавателя,
не синтеза. Новое слово, прочитанное неверно, дописывать сюда.

**Не подменять — распознаватель ошибается, синтез читает верно** (проверено по
спектру 05.11.2026):

- `guitar` — оставлять как есть. Распознаватель слышит то «guitur», то
  «gitter», но начало слова — короткий взрыв «г», как в `give`. Подмена
  `gitar` **хуже**: её SpeechKit читает через «дж», как контрольное `jitar`
  (распознаётся «Jaitar»). 05.11 так испорчен и переозвучен `sm3_ft_b4.mp3`
  (→ `sm3_ft_b4_v2.mp3`).
- имена Mia, Noah, Ellie, Maya, Rex, Ruby, Orla, Elena, Leo, слова foggy, tidying —
  по отдельности распознаются верно, в рассказе распознаватель их путает сам.
- `sofa` в конце фразы — распознаётся «Sova», но в слове глухой «ф» (80 мс
  шума, у `sova` его нет вовсе).

Одному распознавателю не верить: подозрительное слово проверять ещё и по
спектру против двух контрольных слов («make»/«match», «give»/«jitar»).

## Осталось

### 1. SM3, Unit 0, Test, блок 16 → `sm3_u0_test_b16.mp3`

Рассказ про Пенни. **Текст сверен с ключами 22.10.2026** — это тот вариант,
по которому собраны вопросы блока 17: «in the cellar» как неверный вариант,
«her mum» как неверный у вопроса про торты, «14» как неверный у вопроса про
книги. Прежняя, короткая версия (Claire, Ted, Nick, бабушка Julia) этих трёх
подсказок не содержала и устарела — в сборке `builds/sm3/u0/build.py`
(`NARRATION_SM3`) она тоже заменена.

```
This is a story about a girl. Her name is Penny. Penny is seven years old. She lives in an old house with her mother, her father and her brother Sam. Sam is nine. Penny's bedroom is upstairs, next to Sam's room. Downstairs there is a kitchen and a big living room. Under the house there is a cellar. It is dark and cold, and Penny doesn't like it. Penny is very good at dancing, and she is good at telling stories. But she isn't good at swimming. She wants to learn in the summer. On Sundays the family goes to Penny's grandmother. Her grandmother is very good at making cakes. Penny's mother isn't good at making cakes, but she is good at painting. Penny loves books. In her bedroom there are twenty-four books. Sam has got fourteen books.
```

### 2. GG3, Unit 0, Test, блок 19 → `gg3_u0_test_b19.mp3`

Рассказ про Эмму. Текст в сборке — `builds/gg3/u0/build.py`, `NARRATION`.

⚠️ Блок переехал с 17-го места на 19-е 22.10.2026: в тест добавлены приветствие
и два словарных блока. Имя файла изменено под новый номер — запись ещё не
сделана, старого файла нет.

```
This is Emma. Emma is thirteen years old. She lives with her mum and her gran Bertie. Emma usually goes to school by bike, but when it rains her mum drives her. Emma is good at dancing and she has got dance classes twice a week. This year she is going to study Geography more. Emma is scared of spiders. Her favourite food is pancakes: her gran always makes pancakes for breakfast on Sunday.
```

## Уже сделано

- **SM1, Unit 7 Test, блок 9** — «Who is speaking?», файл в блоке стоит.
- **SM1, Final Test, блок 1** — две части одной дорожкой, файл в блоке стоит.

Тексты обоих — `docs/SM1_тексты_для_записи.md`.

## Проверить после заливки

```sql
select c.slug, u.sort_order as unit, l.title, b.sort_order + 1 as block_no
from classroom_courses c
join classroom_units u on u.course_id = c.id
join classroom_lessons l on l.unit_id = u.id
join classroom_blocks b on b.lesson_id = l.id
where b.payload ? 'audio' and coalesce(b.payload->>'audio', '') = ''
  and not (b.payload ? 'audio_tts')
order by c.slug, u.sort_order, l.sort_order, b.sort_order;
```

Пустой результат — значит все аудирования озвучены.


## SM1 · Юнит 9 · ДЗ 5 · блок 2 → `sm1_u9_hw5_b2.mp3`

Добавлено 21.10.2026. Аудирование урока 5 («Listen and draw»): ребёнок слушает
рассказ и находит предметы на пляжной картинке (`media/sm1/u9/hw5_beach_scene.webp`).
Блок 3 той же домашки — `hotspot` с шестью точками: the ball, the sandcastle,
the bucket, the boat, the crab, the umbrella.

Голос английский, темп спокойный, паузы между предложениями около секунды.

```
Look at the beach. It's a sunny day.
The ball is next to the pink towel.
A girl is reading a book on the towel.
The sandcastle is on the sand, next to the girl in the hat.
The bucket is next to the sandcastle.
The boat is in the sea.
A boy is swimming in the water.
The crab is on the sand, next to the blue umbrella.
```

В блоке 2 поле `url` пустое и `audio_tts` намеренно не стоит — чтобы «Озвучить
пачкой» не затёрла место под эту запись.


## SM1 · Юнит 8 · Unit 8 Test · блок 11 → `sm1_u8_test_b11.mp3`

Добавлено 21.10.2026 при вычитке юнита 8. Прежняя запись была **диалогом**
Лили и Тома и почти дословно повторяла письмо из блока 9 с подменёнными
деталями (`Bloop` вместо `Beep`, `four arms` вместо `two long arms`) — ребёнок,
который доверился прочитанному тексту, ошибался именно там, где задание
проверяло слух. Текст переписан рассказом в третьем лице (решение от
20.10.2026), `url` блока обнулён, `audio_tts` не ставили.

Блок — `video` с `provider: 'file'`, поэтому контрольный `select` выше его
не находит: проверять по пустому `url`. Ключи к пропускам — блок 12 того же
теста (`Lily is seven`, `ride a bike`, `can't play the piano`, `Max`, `fast`).

```
This is Lily. Lily is seven. She can swim and she can ride a bike. She can't play the piano, but she can sing! Lily has got a dog. His name is Max. Max can run fast and he can jump, but he can't play football.
```

Старый файл `sm1_u8_test_b11.mp3` в бакете `classroom-media/sm1/` нужно
**перезалить** — использовать его больше нельзя.

## GG3, тесты юнитов 1–8 — восемь рассказов

Добавлено 22.10.2026 при вычитке тестов Go Getter 3. До этого чтение и
аудирование были только в нулевом юните и в итоговом тесте; домашек в GG3 нет,
поэтому за весь курс ребёнок слушал английскую речь два раза. В каждый тест
юнита добавлен блок-заготовка: пустой `audio`, **`audio_tts` намеренно нет**.

Все восемь — рассказ в третьем лице, без диалогов (голос SpeechKit один).
Темп спокойный, пауза между предложениями около секунды. Длина 130–150 слов.
Текст на экране ученику не показывается — он только слушает; вопросы идут
следующим блоком.

Файл кладётся в бакет `classroom-media`, папка `gg3/`, ссылка вписывается в
поле `audio` блока-заготовки. Тексты продублированы константами в
`builds/gg3/tests/narration.py`.

Номер блока — как в редакторе, на 22.10.2026. ⚠️ После запуска
`builds/gg_tests/udalit_gg3.sql` блок аудирования юнита 1 переедет с 17-го
места на 13-е; имя файла при этом не меняем.


### Unit 1 Test, блок 17 → `gg3_u1_test_b17.mp3`

Рассказ про Оливер.

```
This is a story about a boy called Oliver. Oliver is eleven and he lives in a flat with his mum, his dad and his little brother Ben. In Oliver's family everybody helps at home. Oliver sets the table every evening and he takes out the rubbish on Mondays and Thursdays. He doesn't like taking out the rubbish, but he doesn't mind setting the table. His brother Ben is only five, so he doesn't do many chores. Ben feeds the cat and puts away his toys. Oliver's mum says Ben is very patient for a small boy. Oliver's dad irons the shirts on Sunday mornings and he always listens to music when he irons. Right now Oliver isn't at home. He is at his grandmother's house and he is helping her in the garden. He is watering the plants. His grandmother is making a cake for him.
```


### Unit 2 Test, блок 13 → `gg3_u2_test_b13.mp3`

Рассказ про Зои.

```
This is a story about a girl called Zoe. Zoe is twelve and she lives in a small town. She goes shopping with her dad every Saturday morning. They always make a shopping list at home first. There are three shops near Zoe's house: a baker's, a greengrocer's and a big supermarket. The supermarket is the biggest shop in the town, but Zoe's dad says the fruit at the greengrocer's is fresher and cheaper. So they buy their bread at the baker's, their fruit at the greengrocer's and everything else at the supermarket. Zoe's dad never pays in cash. He always pays by card. The queue at the supermarket is usually long on Saturdays, but today it isn't too long. Zoe carries the shopping home. The bags are heavy, but she is strong enough.
```


### Unit 3 Test, блок 12 → `gg3_u3_test_b12.mp3`

Рассказ про Дэниел.

```
This is a story about a boy called Daniel and his holiday last year. Daniel went to Italy with his parents and his sister. They were there for two weeks. They stayed in a small flat near the beach. Every morning Daniel went to the beach and went snorkelling with his father. He saw a lot of colourful fish. In the afternoon it was too hot, so the family stayed inside. One day they went on a day trip to a big city. They explored the old streets and visited a museum. Daniel didn't like the museum and he got bored, but his sister loved it. On the last day the family tried the local food in a small restaurant. Daniel ate pizza and his sister ate fish. Daniel didn't want to go home. He was sad at the airport.
```


### Unit 4 Test, блок 13 → `gg3_u4_test_b13.mp3`

Рассказ про Нина.

```
This is a story about a girl called Nina and a strange evening at her house. Last Friday Nina was doing her homework in her bedroom. Her laptop battery was low, so she plugged in the charger. Her brother was watching a film on the smart TV downstairs and her mother was making toast in the kitchen. The toaster was very old. Suddenly there was a loud noise and all the lights in the house went off. Nina ran quickly downstairs. Her brother was angry, because the film was very good. Her mother looked at the toaster carefully. It was black inside. Nina's father came home ten minutes later. He unplugged the old toaster and the lights came back on. The next day the family bought a new toaster.
```


### Unit 5 Test, блок 13 → `gg3_u5_test_b13.mp3`

Рассказ про Макс.

```
This is a story about a boy called Max and a bad week. Max is ten years old. On Monday he fell off his bike in the park and he got a bruise on his leg and a small cut on his hand. His mother put some cream on the cut. On Tuesday Max had a bad headache and a temperature, so he stayed at home. His mother says he has to drink a lot of water when he has a temperature. On Wednesday the doctor visited him. The doctor says Max shouldn't play football for a week and he has to rest. Max doesn't like this, because football is his favourite sport. On Thursday Max felt better. His throat wasn't sore and his headache was gone. On Friday he went back to school, but he didn't play football.
```


### Unit 6 Test, блок 13 → `gg3_u6_test_b13.mp3`

Рассказ про Феликс.

```
This is a story about a boy called Felix and his first dinner. Felix is thirteen and he has never cooked dinner for his family. Last Sunday he decided to try. He chose a simple recipe: pasta with tomato sauce. First he chopped an onion and some garlic. Then he fried them in a pan with a little oil. He added the tomatoes and some salt. While the sauce was cooking, he boiled the water for the pasta in a big pot. Felix put too much salt in the sauce, so it was very salty. His sister said it was disgusting, but his mother said it was delicious. His father ate two plates. Felix was happy. He has cooked dinner three times since that Sunday, and now he never puts too much salt in his food.
```


### Unit 7 Test, блок 14 → `gg3_u7_test_b14.mp3`

Рассказ про Руби.

```
This is a story about a girl called Ruby. Ruby lives in a terraced house in a small village near the sea. Her house isn't big, but it has got a basement and a balcony. Ruby's favourite place is the balcony, because she can see the sea from it. There is an old bookcase in her bedroom and a big mirror next to the window. Ruby is twelve and she has got two brothers, so she must share her room with her little brother. She doesn't like that. Next month the family are moving to a bigger house. The new house is a detached house with four bedrooms, and Ruby is getting her own room. This weekend the family are cleaning up the new house. On Sunday Ruby's cousins are coming to help. Ruby must pack all her books on Saturday.
```


### Unit 8 Test, блок 13 → `gg3_u8_test_b13.mp3`

Рассказ про Элли.

```
This is a story about a girl called Ellie and her plans. Ellie is thirteen and she lives in a small town. She says she will not live in this town when she is older. She thinks she will live in a big city, or maybe abroad. Ellie wants to be a vet, because she loves animals. She has got two dogs and a cat. Her mother says the job is difficult, but Ellie says she will study hard. Ellie will learn Spanish at school next year. She says she will need it, because she wants to work in South America for a few years. Ellie doesn't think she will be rich, but she thinks she will be happy. She also says she will have a big family one day, with three or four children and a lot of animals.
```


## GG1 · Final Test · блок 9 → `gg1_final_b7.mp3` — готово

Добавлено 22.10.2026 при вычитке тестов GG1. Прежняя запись
(`classroom-media/gg1/gg1_ft_test_b6.mp3`) была **целиком на Present
Continuous** («What's Pat doing?», «flying a kite»), которого курс не даёт ни
на одном уроке. Решение Анны от 22.10 — перезаписать. Задание переписано на
грамматику курса: по вопросу на юниты 2, 4, 5, 6, 3 и 8 (возраст, have got,
can, время и Present Simple, предлоги места, like + -ing).

Рассказ в третьем лице, без диалогов. Голос английский, темп спокойный, паузы
между предложениями около секунды.

```
This is the Brown family. They live in a small house in London. Jack is eleven years old. He has got short dark hair and green eyes. He can swim very well, but he can't ride a bike. His sister Emma is nine. She has got long curly hair. Emma can ride a horse. Jack always gets up at half past seven. He has breakfast with his family and then he goes to school. In Jack's bedroom there is a big desk next to the window. His guitar is under the bed. On Saturday Jack plays football with his friends. Emma doesn't like football. She likes listening to music. They have got a dog. His name is Rex. Rex is big and very friendly.
```

Ключи к вопросам блока 9: eleven · long curly hair · swim · half past seven ·
under the bed · listening to music.

Старая запись `gg1_ft_test_b6.mp3` из бакета **не удалена**, на неё просто
больше нет ссылки. Новая запись уже стоит в блоке 9 («LISTENING Part 3.
Послушай рассказ о семье Браун») — пункт закрыт. Номер блока сменился с 7 на 9
после правки порядка заданий 05.11.2026.


## SM3, тесты юнитов 1–8 — восемь рассказов

Добавлено 03.11.2026. Решение Анны от 03.11.2026: «в тестах Super Minds 3
юнитов 1–8 нужно добавить аудирование» — до этого аудирование в SM3 было только
в тесте нулевого юнита и в финальном тесте. В каждый тест добавлен один блок
`quiz` с пятью вопросами: пустой `audio`, **`audio_tts` намеренно нет**,
`skill = 'listening'`.

Все восемь — рассказ в третьем лице, без диалогов (голос SpeechKit один).
Длина 76–85 слов, темп спокойный, пауза между предложениями около секунды.
Текст на экране ученику не показывается — он только слушает; вопросы в том же
блоке. Лексика и грамматика — строго того юнита, для которого тест.

Файл кладётся в бакет `classroom-media`, папка `sm3/`, ссылка вписывается в
поле `audio` блока. Тексты и ключи — `builds/sm3/listening/teksty.md`,
SQL — `builds/sm3/listening/listening.sql`.

Номера блоков — как в редакторе, на 03.11.2026 (блок стоит перед SPEAKING TASK).

| юнит | блок | файл | герой |
|---|---|---|---|
| 1 · School | 14 | `sm3_u1_test_b14.mp3` | Milo |
| 2 · Food | 15 | `sm3_u2_test_b15.mp3` | Freya |
| 3 · At home | 15 | `sm3_u3_test_b15.mp3` | Hugo |
| 4 · In the town | 15 | `sm3_u4_test_b15.mp3` | Greta |
| 5 · Under the sea | 15 | `sm3_u5_test_b15.mp3` | Otis |
| 6 · Gadgets | 15 | `sm3_u6_test_b15.mp3` | Maisie |
| 7 · At the doctor’s | 14 | `sm3_u7_test_b14.mp3` | Rufus |
| 8 · Countries | 14 | `sm3_u8_test_b14.mp3` | Tessa |

### Unit 1 Test, блок 14 → `sm3_u1_test_b14.mp3`

```
Milo is a pupil at Green Hill School. He likes studying Science and Art, but he doesn't like Maths. His favourite subject is Geography, because he loves looking at maps. Milo has to wear a uniform to school every day. He doesn't have to wear it on Saturday. After school he likes playing computer games with his friend. On Friday Milo has Music, and he hates singing. He has got nine books in his school bag.
```

Ключи: Geography · Maths · a uniform · singing · nine.

### Unit 2 Test, блок 15 → `sm3_u2_test_b15.mp3`

```
Freya is making a picnic basket for her family. There are some rolls and some cheese in the basket. There is a big bottle of water, too. There aren't any sausages, because Freya doesn't like them. There is some salad with onions and peas. There isn't any pineapple in the shop today, so Freya has got six apples. Her brother would like some lemonade, but there isn't any lemonade in the fridge. There is some soup for dinner.
```

Ключи: No, there aren't. · six · onions and peas · some lemonade · some soup.

### Unit 3 Test, блок 15 → `sm3_u3_test_b15.mp3`

```
Hugo helps his family at home every day. He gets up at half past seven and has breakfast. He always takes the dog for a walk before school. After school Hugo tidies up his room, but he doesn't like washing up. His sister washes up on Monday and Wednesday. Hugo likes sweeping the floor and he sometimes does the shopping with his mum on Saturday. He never feeds the cat. Hugo goes to bed at quarter past nine.
```

Ключи: at half past seven · He takes the dog for a walk. · washing up ·
on Saturday · at quarter past nine.

### Unit 4 Test, блок 15 → `sm3_u4_test_b15.mp3`

```
Greta lives in a small town. Her house is opposite the library, and there is a big tower near the market square. On Monday Greta is going to the library to borrow a book about animals. The bank is between the supermarket and the car park. There is a big clock above the door of the bank. On Saturday Greta is going to the sports centre to go swimming with her friends. She has got a map of the town.
```

Ключи: the library · near the market square · to borrow a book ·
between the supermarket and the car park · to the sports centre.

### Unit 5 Test, блок 15 → `sm3_u5_test_b15.mp3`

```
Yesterday Otis was at the beach with his family. The water was warm. There were two dolphins near the boat and there was a big turtle on the sand. Otis's sister was in the sea with her friend. There weren't any jellyfish, so the children were happy. There was a starfish and a small seahorse in Otis's bucket. The anchor of the old boat was under the water. At six o'clock Otis was in the café.
```

Ключи: at the beach · two · No, there weren't. · a starfish and a seahorse ·
in the café.

### Unit 6 Test, блок 15 → `sm3_u6_test_b15.mp3`

```
Maisie has got a lot of gadgets at home. Her new tablet is bigger than her mobile phone, but her laptop is bigger than the tablet. Maisie thinks her games console is more exciting than her digital radio. Her small torch is cheaper than the electric fan. Maisie's walkie-talkies are louder than her phone. Her favourite gadget is her laptop, because it is faster than the old computer in the kitchen. The lift in her building is slower than the stairs.
```

Ключи: Yes, it is. · the laptop · her laptop · the torch · the lift.

### Unit 7 Test, блок 14 → `sm3_u7_test_b14.mp3`

```
Last week Rufus felt very ill. On Monday he woke up with a bad headache and a cough. His mum phoned the doctor. The doctor looked at Rufus and talked to his mum about the medicine. On Tuesday Rufus had a stomachache, so he stayed at home and watched TV. His sister cooked some soup for him. On Wednesday Rufus felt better. He listened to music and wrote a letter to his friend. On Thursday he went to school again.
```

Ключи: a headache and a cough · his mum · He watched TV. · his sister ·
on Thursday.

### Unit 8 Test, блок 14 → `sm3_u8_test_b14.mp3`

```
Last summer Tessa went to Egypt with her family. They stayed in a small hotel near the sea for two weeks. Tessa saw the pyramids and she had a lot of fun. She didn't go to the museum, because it was closed on Monday. Her brother played football on the beach every day. They ate fish and rice every evening. Tessa sent five postcards to her friends. She didn't swim in the sea, but she liked the hotel a lot.
```

Ключи: to Egypt · two weeks · No, she didn't. · five · fish and rice.

## SM1 Final Test, задание 2 (добавлено 03.11.2026)

Файл `sm1_final_b2.mp3` → бакет `classroom-media`, папка `sm1/`. Своей записи у
задания «подпиши людей на картинке» не было никогда — стояла ссылка на запись
соседнего задания 1. Текст и ключ «кто где на картинке» — `builds/sm1/ft_picnic_tekst.md`.

> Look at the picnic. Mike is the boy with the kite. He is wearing a red T-shirt.
> Paul has got a football. He is wearing a blue T-shirt. Clare is eating a
> sandwich. She has got a yellow dress. Sam is drinking orange juice. He is
> wearing a green T-shirt. Jane is reading a book. She has got a purple T-shirt.

## SM1 Unit 9 ДЗ 5, задание 2 (добавлено 03.11.2026)

Файл `sm1_u9_hw5_b2.mp3` → бакет `classroom-media`, папка `sm1/`, **перезаписать
поверх старого**. Старая запись перечисляла bucket, umbrella, crab и boat —
этих слов в SM1 не давали (решение Анны от 03.11). Задание пересобрано на
занятиях юнита, картинка новая.

> Look at the beach. A girl is making a sandcastle. A boy is looking for shells.
> A girl is eating ice cream. A boy is taking a photo. A girl is reading a book.
> A boy is playing the guitar.

## Переозвучить: SpeechKit читает «ache» через «ч» (найдено Анной 05.11.2026)

В записи SM3 Unit 7 Test («рассказ про Руфуса») слова `headache` и
`stomachache` звучат с «ч» на конце — как «хэдэч», «стомачэч». Правильно —
«хэдэйк», «стомакэйк». Виновата не разметка, а синтез: буквосочетание `ch`
в конце слова читается по общему правилу.

**Что сделать** в сессии, где есть ключ Яндекса:

1. Переозвучить файлы, в тексте которых есть слова на `-ache` и `stomach`:
   - `sm3_u7_test_b14.mp3` — рассказ про Руфуса (headache, stomachache);
   - `gg3_u5_test_b13.mp3` — рассказ про Макса (headache);
   - проверить на слух и остальные: `gg3_u7_test_b14.mp3`,
     `gg3_u8_test_b13.mp3`, `gg3_final_b2.mp3`, `gg1_u0_test_b10.mp3`,
     `sm2_u0_test_b7.mp3`.
2. Если движок снова читает через «ч», подменить написание **только в тексте
   для синтеза** (на экране ребёнок текст не видит, поэтому подмена безопасна):
   `headache` → `head ake`, `stomachache` → `stomak ake`,
   `toothache` → `tooth ake`, `earache` → `ear ake`, `stomach` → `stomak`.
   Прослушать и выбрать написание, которое звучит верно.
3. Залить файлы в бакет `classroom-media` под теми же именами — ссылки в
   блоках менять не придётся.

**То же может быть и в «Озвучить пачкой»** (движок другой, Piper): разметок
`audio_tts` со словами на `-ache` — 39 (Wow Dragon 1 — 19, SM0 — 13, SM3 — 5,
GG2 — 2). Там звук уже синтезирован; прежде чем переозвучивать, надо
послушать одно слово и понять, та же это беда или нет.

## SM3 Final Test — записи не совпадают с заданиями (нашла Анна 05.11.2026)

Три задания подряд помечены listening, но записей на них две, и обе не о том:

- блок 2 «подпиши людей на картинке» (точки: Peter, Paul, Jane, Fred, Daisy,
  Sally; лишнее имя Mary) — `sm3_ft_b3.mp3`;
- блок 3 «соедини дни недели и занятия» — **тот же** `sm3_ft_b3.mp3`;
- блок 4 «послушай и выбери картинку», шесть вопросов — `sm3_ft_b6.mp3`.

Одна запись на два разных задания не работает: в первом нужны люди в
библиотеке, во втором — расписание на неделю. Текстов этих записей в
репозитории нет, поэтому ниже — новые, написанные точно под ключи. Озвучить
SpeechKit, залить в бакет `classroom-media/sm3/` под теми же именами, плюс
один новый файл.

**`sm3_ft_b3.mp3` — для блока 6 (люди в библиотеке). 05.11 Анна посмотрела
задание и сказала: старая запись подходит, менять не надо.** Новая версия
`sm3_ft_b3_v2.mp3` из блока убрана, ссылка возвращена на `sm3_ft_b3.mp3`.
Текст ниже оставлен на случай, если запись всё-таки решат переписать.

Прежний текст для блока 6: Имена идут по порядку
точек, последнее имя Mary в картинке лишнее:

> Look at the picture of the library. Peter is reading a book at the table.
> Paul is standing next to the bookcase. Jane is looking for a book on the
> shelf. Fred is sitting on the floor with a comic. Daisy is talking to the
> librarian. Sally is writing in her notebook.

**`sm3_ft_b4.mp3` — новый файл, для блока 7 (дни недели и занятия). Готово,
стоит в блоке.** Заголовок блока исправлен с «Послушай **ещё раз** и соедини»
на «Послушай и соедини»: запись теперь своя, а не та же, что у блока 6.

> This is Emma's week. On Monday she goes swimming. On Tuesday she plays
> football with her friends. On Wednesday she plays the guitar. On Thursday
> she goes shopping with her mum. On Friday she rides a bike in the park. On
> Saturday she bakes a cake.

**`sm3_ft_b6.mp3` → переписать в `sm3_ft_b6_v3.mp3`, блок 8 (шесть вопросов).**
05.11.2026 Анна послушала: «слишком лёгкое аудио. Для SM3 можно посложнее…
чтобы три варианта как-то прозвучали». Прежний текст просто называл ответ
одной строкой — ребёнок мог не слушать до конца. Новый вариант в каждом
пункте проговаривает и неверные варианты: сначала вопрос с неправильным
предположением, отрицание, потом верный ответ. Ключи прежние: теннис ·
школьный автобус · сад · девять лет · щенок · суп.

```
One. Does John play football? No, he doesn't. He plays tennis every Saturday. And he doesn't like swimming.
Two. Did Jack go to school by bike yesterday? No, he didn't. He didn't walk either, because it was raining. He went by bus.
Three. Is Vicky in the kitchen? No, she isn't. She isn't in her bedroom either. She's in the garden with the dog.
Four. Is Jim ten years old today? No, he isn't. He was eight last year, so now he is nine.
Five. Did Nick get a bicycle for his birthday? No, he didn't. He wanted a games console, but he got a puppy. He is very happy.
Six. Is there any salad in the bowl on the table? No, there isn't. There isn't any fruit either. There is some hot soup.
```

Пока запись не придёт, в блоке остаётся `sm3_ft_b6_v2.mp3` — задание рабочее,
просто лёгкое.

## SM3 Unit 9 Test, блок 7 → `sm3_u9_test_b7.mp3` (05.11.2026)

Аудирование нового блока (`quiz`, listening), рассказ про Лиама. Записано
05.11.2026, бакет `classroom-media/sm3/`.

```
This is Liam. Liam lives in London. Next week Liam is going to visit his grandma in Scotland. On Monday it's going to be cloudy, so Liam and his grandma are going to make pizza. On Tuesday it's going to be a thunderstorm, so they are going to watch a film at home. On Wednesday it's going to be sunny and warm. They are going to ride their bikes in the forest. Liam is going to take his camera and take photos of the old castle.
```

`sm3_ft_b6_v3.mp3` для блока 8 SM3 Final Test записан 05.11.2026 тем же
текстом, что выше в разделе SM3 Final Test.

## GG1 · Final Test · блок 7 → `gg1_ft_b7_v2.mp3`

Добавлено 05.11.2026. Задание «послушай и расставь предметы по местам»
пересобирается: на картинке будет пустая комната, предметы ребёнок ставит сам
(раньше они были нарисованы, и слушать было незачем). Прежние слова — radio,
robot, kite — в Go Getter 1 не встречаются вовсе; новые взяты из курса.

Шесть предметов: bag · book · guitar · clock · skateboard · laptop.
Шесть мест: under the desk · on the bed · next to the sofa · on the shelf ·
next to the door · on the small table.

```
One. The bag is under the desk.
Two. The book is on the bed.
Three. The guitar is next to the sofa.
Four. The clock is on the shelf.
Five. The skateboard is next to the door.
Six. The laptop is on the small table.
```

Старый файл `gg1_ft_test_b2.mp3` остаётся в бакете, ссылки на него больше нет.

## SM1 · Юнит 9 · ДЗ 5 · блок 2 → `sm1_u9_hw5_b2_v2.mp3`

Переписано 05.11.2026 («11 давай»). Задание «расставь по местам» решалось
глазами: подписи были действиями (make a sandcastle, read a book), а на
картинке каждый ребёнок занят ровно этим. Теперь подписи — имена, и узнать,
кто есть кто, можно только по записи: в рассказе каждый ребёнок назван по
одежде. Прежняя запись описывала другую картинку (мяч, ведёрко, краб,
зонт) — её больше не используем.

Порядок детей на картинке слева направо: Lily · Tom · Amy · Ben · Clare · Sam.

**Переписано ещё раз 06.11.2026.** Анна посмотрела готовое задание: «аудио всё
говорит по порядку — как идут дети, слева направо, и описывает их, а должен
в разнобой». Так ребёнок подписывал кружки подряд, не слушая. Новый порядок
рассказа — **Ben · Clare · Lily · Sam · Amy · Tom**: ни один ребёнок не идёт
следом за своим соседом по картинке. Запись `sm1_u9_hw5_b2_v2.mp3` больше
не используется.

Новый файл — `sm1_u9_hw5_b2_v3.mp3`, папка `sm1`:

```
Look at the children on the beach. Ben has got a yellow T-shirt and a blue cap. He is taking a photo.
Clare has got red hair and a green top. She is reading a book.
Lily has got a pink swimsuit. She is making a sandcastle.
Sam has got a green hoodie. He is playing the guitar.
Amy has got a big hat and a purple dress. She is eating an ice cream.
Tom has got a blue and white T-shirt. He is looking for shells.
```

## SM2 · Юнит 7 · ДЗ 5 · блок 6 → `sm2_u7_hw5_v2.mp3`

Переписано 05.11.2026 («11 давай»). Было: картинка-раскраска (чёрно-белый
контур), и все шесть предметов на ней нарисованы — слушать незачем, да и
раскрасок у нас нет по решению от 03.11. Картинка рисуется заново: пустой
городской парк, предметы ребёнок ставит сам. Подписи — картинки предметов,
они уже есть (`media/sm2/u7/hw5_boat.webp` и другие).

Места в новом парке: озеро · дерево · скамейка · фонтан · каменная стена ·
окно кафе.

**Переписано ещё раз 06.11.2026.** Анна нашла два изъяна: рассказ шёл по
порядку слева направо (как и в SM1), и — главное — **слов `fountain` и `bench`
в курсе SM2 нет вообще**. Проверил по базе: `fountain` не встречается ни в
одном блоке курса, `bench` тоже. То есть два места из шести ребёнку незнакомы.

Поэтому меняется и картинка: скамейка и фонтан заменяются на **автобусную
остановку** и **машину** — оба слова в SM2 есть (`bus stop` — юнит 3,
`car` — 61 урок). Остальные четыре места знакомы: `lake`, `tree`, `wall`,
`cafe window`. Предлоги все из курса: `on`, `in`, `next to`, `in front of`.

Новый файл — `sm2_u7_hw5_v3.mp3`, порядок вразнобой:

```
One. The lizard is on the wall.
Two. The boat is on the lake.
Three. The flowers are in front of the cafe window.
Four. The bird is in the tree.
Five. The girl is next to the car.
Six. The boy is next to the bus stop.
```
