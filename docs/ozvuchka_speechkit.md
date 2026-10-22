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

## Осталось — два места

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

### 2. GG3, Unit 0, Test, блок 17 → `gg3_u0_test_b17.mp3`

Рассказ про Эмму. Текст в сборке — `builds/gg3/u0/build.py`, `NARRATION`.

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
