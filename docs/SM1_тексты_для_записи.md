# SM1 — тексты, которые Анна записывает голосом

Решение Анны от 19.10.2026: большой связный текст не синтезируем — Анна
записывает сама и присылает файл с именем из таблицы. Мы кладём его в бакет
`classroom-media/sm1/` и вставляем блок.

## Unit 7 Test — аудирование «Who is speaking?» → `sm1_u7_test_b9.mp3`

Встанет блоком 9 (после 8-го), за ним блок «соедини говорящего и одежду»:
картинки `media/sm1/u7/outfit_*.webp`. Ключ: Speaker 1 — outfit_sam,
2 — outfit_lily, 3 — outfit_any, 4 — outfit_tom, 5 — outfit_anna
(outfit_kate — лишняя картинка в задании «Extra» выгрузки, в match не входит).

```
Speaker 1. Hello! I'm wearing a grey T-shirt and red shorts. I'm wearing a cap, too.
Speaker 2. Hi! I'm wearing a blue shirt with spots and a pink skirt with flowers.
Speaker 3. Hello! I'm wearing a pink sweater and a long red skirt. My shoes are white.
Speaker 4. Hi! I'm wearing a black coat, black trousers and brown boots.
Speaker 5. Hello! I'm wearing a purple sweater with zigzags and a blue skirt.
```

## Final Test — аудирование → `sm1_final_b1.mp3` (одним файлом, две части)

Блок 1 (сейчас `url` пустой). Часть 1 — к квизу в блоке 2, часть 2 — к
«диаграмме» с пикником в блоке 3. Тексты же — в `tools/sm1/final.py`
(`NARRATION_STORY`, `NARRATION_PICNIC`).

Часть 1:
```
Look at these five children. This is Tom. Tom is seven. He has got a new kite. It's red and yellow. He hasn't got a train. This is Anna. Anna likes pizza. She doesn't like cake. This is Sue. Sue has got a pet. It's a dog. It's brown and white. She hasn't got a cat. This is Ben. Ben can't swim and he can't play football. But he can ride a bike! His bike is red. This is Nick. Today Nick is wearing a brown jacket. He isn't wearing a cap.
```

Часть 2:
```
Now look at the picnic. Mike is a boy. He is wearing a blue T-shirt and red shorts. He is running. Paul is Mike's dad. He is wearing a red T-shirt. He is running, too. Jane is the grandma. She has got grey hair. She is eating an apple. Clare is a little girl. She has got yellow hair. She has got a doll. Laura is the mum. She is wearing a pink skirt. She has got a flower.
```
