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
