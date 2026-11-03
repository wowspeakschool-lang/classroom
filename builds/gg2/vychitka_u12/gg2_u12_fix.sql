-- GG2 юниты 1-2: перенумерация и правки payload (вычитка 03.11.2026)
begin;

-- 1. перенумерация: сдвиг в запас, потом на место
update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234';
update classroom_blocks set sort_order = 0 where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 1000;
update classroom_blocks set sort_order = 1 where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 1001;
update classroom_blocks set sort_order = 2 where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 1003;
update classroom_blocks set sort_order = 3 where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 1002;
update classroom_blocks set sort_order = 4 where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 1009;
update classroom_blocks set sort_order = 5 where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 1004;
update classroom_blocks set sort_order = 6 where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 1005;
update classroom_blocks set sort_order = 7 where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 1006;
update classroom_blocks set sort_order = 8 where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 1007;
update classroom_blocks set sort_order = 9 where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 1008;
update classroom_blocks set sort_order = 10 where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 1010;
update classroom_blocks set sort_order = 11 where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 1011;
update classroom_blocks set sort_order = 12 where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 1012;
update classroom_blocks set sort_order = 13 where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 1013;

update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = '829ba270-7377-43f0-b5ad-093441ba6b07';
update classroom_blocks set sort_order = 0 where lesson_id = '829ba270-7377-43f0-b5ad-093441ba6b07' and sort_order = 1000;
update classroom_blocks set sort_order = 1 where lesson_id = '829ba270-7377-43f0-b5ad-093441ba6b07' and sort_order = 1001;
update classroom_blocks set sort_order = 2 where lesson_id = '829ba270-7377-43f0-b5ad-093441ba6b07' and sort_order = 1002;
update classroom_blocks set sort_order = 3 where lesson_id = '829ba270-7377-43f0-b5ad-093441ba6b07' and sort_order = 1003;
update classroom_blocks set sort_order = 6 where lesson_id = '829ba270-7377-43f0-b5ad-093441ba6b07' and sort_order = 1004;
update classroom_blocks set sort_order = 7 where lesson_id = '829ba270-7377-43f0-b5ad-093441ba6b07' and sort_order = 1005;
update classroom_blocks set sort_order = 10 where lesson_id = '829ba270-7377-43f0-b5ad-093441ba6b07' and sort_order = 1006;

update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = '851d9b90-f06b-46e5-8fd5-96cec97d6d69';
update classroom_blocks set sort_order = 0 where lesson_id = '851d9b90-f06b-46e5-8fd5-96cec97d6d69' and sort_order = 1000;
update classroom_blocks set sort_order = 1 where lesson_id = '851d9b90-f06b-46e5-8fd5-96cec97d6d69' and sort_order = 1001;
update classroom_blocks set sort_order = 2 where lesson_id = '851d9b90-f06b-46e5-8fd5-96cec97d6d69' and sort_order = 1002;
update classroom_blocks set sort_order = 3 where lesson_id = '851d9b90-f06b-46e5-8fd5-96cec97d6d69' and sort_order = 1003;
update classroom_blocks set sort_order = 4 where lesson_id = '851d9b90-f06b-46e5-8fd5-96cec97d6d69' and sort_order = 1006;
update classroom_blocks set sort_order = 5 where lesson_id = '851d9b90-f06b-46e5-8fd5-96cec97d6d69' and sort_order = 1004;
update classroom_blocks set sort_order = 6 where lesson_id = '851d9b90-f06b-46e5-8fd5-96cec97d6d69' and sort_order = 1005;
update classroom_blocks set sort_order = 10 where lesson_id = '851d9b90-f06b-46e5-8fd5-96cec97d6d69' and sort_order = 1007;
update classroom_blocks set sort_order = 11 where lesson_id = '851d9b90-f06b-46e5-8fd5-96cec97d6d69' and sort_order = 1008;

update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = '3894f232-5143-4498-aa0c-c575e0760cc1';
update classroom_blocks set sort_order = 0 where lesson_id = '3894f232-5143-4498-aa0c-c575e0760cc1' and sort_order = 1000;
update classroom_blocks set sort_order = 1 where lesson_id = '3894f232-5143-4498-aa0c-c575e0760cc1' and sort_order = 1001;
update classroom_blocks set sort_order = 2 where lesson_id = '3894f232-5143-4498-aa0c-c575e0760cc1' and sort_order = 1002;
update classroom_blocks set sort_order = 3 where lesson_id = '3894f232-5143-4498-aa0c-c575e0760cc1' and sort_order = 1003;
update classroom_blocks set sort_order = 5 where lesson_id = '3894f232-5143-4498-aa0c-c575e0760cc1' and sort_order = 1004;
update classroom_blocks set sort_order = 6 where lesson_id = '3894f232-5143-4498-aa0c-c575e0760cc1' and sort_order = 1005;
update classroom_blocks set sort_order = 7 where lesson_id = '3894f232-5143-4498-aa0c-c575e0760cc1' and sort_order = 1006;
update classroom_blocks set sort_order = 8 where lesson_id = '3894f232-5143-4498-aa0c-c575e0760cc1' and sort_order = 1007;
update classroom_blocks set sort_order = 9 where lesson_id = '3894f232-5143-4498-aa0c-c575e0760cc1' and sort_order = 1008;

update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = '17a7a056-ec35-467b-8b6d-031c50fe937a';
update classroom_blocks set sort_order = 0 where lesson_id = '17a7a056-ec35-467b-8b6d-031c50fe937a' and sort_order = 1000;
update classroom_blocks set sort_order = 1 where lesson_id = '17a7a056-ec35-467b-8b6d-031c50fe937a' and sort_order = 1001;
update classroom_blocks set sort_order = 2 where lesson_id = '17a7a056-ec35-467b-8b6d-031c50fe937a' and sort_order = 1002;
update classroom_blocks set sort_order = 3 where lesson_id = '17a7a056-ec35-467b-8b6d-031c50fe937a' and sort_order = 1003;
update classroom_blocks set sort_order = 4 where lesson_id = '17a7a056-ec35-467b-8b6d-031c50fe937a' and sort_order = 1004;
update classroom_blocks set sort_order = 5 where lesson_id = '17a7a056-ec35-467b-8b6d-031c50fe937a' and sort_order = 1005;
update classroom_blocks set sort_order = 7 where lesson_id = '17a7a056-ec35-467b-8b6d-031c50fe937a' and sort_order = 1006;
update classroom_blocks set sort_order = 9 where lesson_id = '17a7a056-ec35-467b-8b6d-031c50fe937a' and sort_order = 1007;
update classroom_blocks set sort_order = 10 where lesson_id = '17a7a056-ec35-467b-8b6d-031c50fe937a' and sort_order = 1008;

update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b';
update classroom_blocks set sort_order = 0 where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 1000;
update classroom_blocks set sort_order = 1 where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 1001;
update classroom_blocks set sort_order = 2 where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 1005;
update classroom_blocks set sort_order = 3 where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 1002;
update classroom_blocks set sort_order = 4 where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 1003;
update classroom_blocks set sort_order = 5 where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 1004;
update classroom_blocks set sort_order = 6 where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 1006;
update classroom_blocks set sort_order = 7 where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 1007;
update classroom_blocks set sort_order = 8 where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 1008;
update classroom_blocks set sort_order = 9 where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 1009;
update classroom_blocks set sort_order = 10 where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 1010;
update classroom_blocks set sort_order = 11 where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 1011;
update classroom_blocks set sort_order = 12 where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 1012;

update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = 'd8fbeb71-a2ef-4bfd-a0d9-eb73dae5d5e0';
update classroom_blocks set sort_order = 0 where lesson_id = 'd8fbeb71-a2ef-4bfd-a0d9-eb73dae5d5e0' and sort_order = 1000;
update classroom_blocks set sort_order = 1 where lesson_id = 'd8fbeb71-a2ef-4bfd-a0d9-eb73dae5d5e0' and sort_order = 1001;
update classroom_blocks set sort_order = 2 where lesson_id = 'd8fbeb71-a2ef-4bfd-a0d9-eb73dae5d5e0' and sort_order = 1004;
update classroom_blocks set sort_order = 3 where lesson_id = 'd8fbeb71-a2ef-4bfd-a0d9-eb73dae5d5e0' and sort_order = 1002;
update classroom_blocks set sort_order = 4 where lesson_id = 'd8fbeb71-a2ef-4bfd-a0d9-eb73dae5d5e0' and sort_order = 1003;
update classroom_blocks set sort_order = 9 where lesson_id = 'd8fbeb71-a2ef-4bfd-a0d9-eb73dae5d5e0' and sort_order = 1005;

update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = 'edb04172-9975-4411-bda8-74f5592a7a13';
update classroom_blocks set sort_order = 0 where lesson_id = 'edb04172-9975-4411-bda8-74f5592a7a13' and sort_order = 1000;
update classroom_blocks set sort_order = 1 where lesson_id = 'edb04172-9975-4411-bda8-74f5592a7a13' and sort_order = 1001;
update classroom_blocks set sort_order = 2 where lesson_id = 'edb04172-9975-4411-bda8-74f5592a7a13' and sort_order = 1002;
update classroom_blocks set sort_order = 4 where lesson_id = 'edb04172-9975-4411-bda8-74f5592a7a13' and sort_order = 1004;
update classroom_blocks set sort_order = 6 where lesson_id = 'edb04172-9975-4411-bda8-74f5592a7a13' and sort_order = 1003;
update classroom_blocks set sort_order = 7 where lesson_id = 'edb04172-9975-4411-bda8-74f5592a7a13' and sort_order = 1005;
update classroom_blocks set sort_order = 8 where lesson_id = 'edb04172-9975-4411-bda8-74f5592a7a13' and sort_order = 1006;

update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = 'ccb8ec26-8db1-4014-ba1e-500fc48b8624';
update classroom_blocks set sort_order = 0 where lesson_id = 'ccb8ec26-8db1-4014-ba1e-500fc48b8624' and sort_order = 1000;
update classroom_blocks set sort_order = 1 where lesson_id = 'ccb8ec26-8db1-4014-ba1e-500fc48b8624' and sort_order = 1001;
update classroom_blocks set sort_order = 2 where lesson_id = 'ccb8ec26-8db1-4014-ba1e-500fc48b8624' and sort_order = 1002;
update classroom_blocks set sort_order = 3 where lesson_id = 'ccb8ec26-8db1-4014-ba1e-500fc48b8624' and sort_order = 1003;
update classroom_blocks set sort_order = 4 where lesson_id = 'ccb8ec26-8db1-4014-ba1e-500fc48b8624' and sort_order = 1004;
update classroom_blocks set sort_order = 7 where lesson_id = 'ccb8ec26-8db1-4014-ba1e-500fc48b8624' and sort_order = 1005;
update classroom_blocks set sort_order = 8 where lesson_id = 'ccb8ec26-8db1-4014-ba1e-500fc48b8624' and sort_order = 1006;

update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f';
update classroom_blocks set sort_order = 0 where lesson_id = '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f' and sort_order = 1000;
update classroom_blocks set sort_order = 1 where lesson_id = '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f' and sort_order = 1001;
update classroom_blocks set sort_order = 2 where lesson_id = '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f' and sort_order = 1002;
update classroom_blocks set sort_order = 3 where lesson_id = '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f' and sort_order = 1003;
update classroom_blocks set sort_order = 4 where lesson_id = '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f' and sort_order = 1004;
update classroom_blocks set sort_order = 5 where lesson_id = '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f' and sort_order = 1005;
update classroom_blocks set sort_order = 6 where lesson_id = '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f' and sort_order = 1006;
update classroom_blocks set sort_order = 9 where lesson_id = '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f' and sort_order = 1007;
update classroom_blocks set sort_order = 10 where lesson_id = '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f' and sort_order = 1008;

update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = '4d349ca7-4b58-48e8-824a-fcde5e710f54';
update classroom_blocks set sort_order = 0 where lesson_id = '4d349ca7-4b58-48e8-824a-fcde5e710f54' and sort_order = 1000;
update classroom_blocks set sort_order = 1 where lesson_id = '4d349ca7-4b58-48e8-824a-fcde5e710f54' and sort_order = 1001;
update classroom_blocks set sort_order = 2 where lesson_id = '4d349ca7-4b58-48e8-824a-fcde5e710f54' and sort_order = 1002;
update classroom_blocks set sort_order = 4 where lesson_id = '4d349ca7-4b58-48e8-824a-fcde5e710f54' and sort_order = 1003;
update classroom_blocks set sort_order = 5 where lesson_id = '4d349ca7-4b58-48e8-824a-fcde5e710f54' and sort_order = 1004;
update classroom_blocks set sort_order = 6 where lesson_id = '4d349ca7-4b58-48e8-824a-fcde5e710f54' and sort_order = 1005;
update classroom_blocks set sort_order = 7 where lesson_id = '4d349ca7-4b58-48e8-824a-fcde5e710f54' and sort_order = 1006;
update classroom_blocks set sort_order = 8 where lesson_id = '4d349ca7-4b58-48e8-824a-fcde5e710f54' and sort_order = 1007;
update classroom_blocks set sort_order = 9 where lesson_id = '4d349ca7-4b58-48e8-824a-fcde5e710f54' and sort_order = 1008;

-- 2. правки payload (по НОВЫМ номерам)
update classroom_blocks set payload = jsonb_set(jsonb_set(payload,'{title}','"Посмотри на картинку и напиши слово по-английски"'),'{items,1,prompt}','""'), updated_at = now()
  where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 8;
update classroom_blocks set payload = jsonb_set(payload,'{html}','"<p><img src=\"https://classroom.wowteach.ru/media/shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h3>Время почитать 📖</h3><p>Ты выучил и школьные предметы, и школьные принадлежности — молодец! Осталось совсем немного.</p>"'), updated_at = now()
  where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 9;
update classroom_blocks set payload = jsonb_set(payload,'{html}','"<h3>Karen и её расписание</h3><p>Прочитай, что рассказывает Karen, и отметь её любимые школьные предметы.</p><blockquote><p>My name is Karen. I''m 11 years old. My favourite subjects are P.E. and Computer Studies. I have P.E. on Monday and Wednesday and Computer Studies on Friday.</p></blockquote>"'), updated_at = now()
  where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 10;
update classroom_blocks set payload = jsonb_set(jsonb_set(payload,'{title}','"Мои любимые предметы ✍️"'),'{html}','"<p>А вот и последнее задание. Прочитай ещё раз текст о Karen и письменно перечисли свои любимые школьные предметы.</p><p><i>Например: My favourite subjects are English and Art.</i></p>"'), updated_at = now()
  where lesson_id = '852fc4ee-b710-458f-8957-3a446e9dc234' and sort_order = 12;
update classroom_blocks set payload = jsonb_set(payload,'{html}','"<p><img src=\"https://classroom.wowteach.ru/media/shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашку! 👋</h2><p>В этом уроке тебя ждёт интересное видео и классные задания!</p>"'), updated_at = now()
  where lesson_id = 'ed03a12f-2fd8-4e50-96a6-e889f97107e5' and sort_order = 0;
update classroom_blocks set payload = jsonb_set(jsonb_set(payload,'{title}','"Посмотри видео ещё раз и выбери только верные утверждения"'),'{questions,0,q}','""'), updated_at = now()
  where lesson_id = 'ed03a12f-2fd8-4e50-96a6-e889f97107e5' and sort_order = 4;
update classroom_blocks set payload = jsonb_set(jsonb_set(payload,'{title}','"Ответь на вопросы ✍️"'),'{html}','"<p>Осталось последнее задание.</p><p>В таблице отмечено, чем любят и не любят заниматься Carla (кошка) и Rocco (енот). Письменно ответь на вопросы из предыдущего упражнения (например: <i>Yes, she does. / No, he doesn''t.</i>).</p><p><img src=\"https://classroom.wowteach.ru/media/gg2/u1/book_carla_rocco_table.webp\" alt=\"\" style=\"height:220px\"></p><ol><li>Does Carla paint pictures?</li><li>Does Rocco paint pictures?</li><li>Do Rocco and Carla like music?</li><li>Do Rocco and Carla play football?</li><li>Does Rocco play chess?</li><li>Does Carla play chess?</li></ol>"'), updated_at = now()
  where lesson_id = 'ed03a12f-2fd8-4e50-96a6-e889f97107e5' and sort_order = 10;
update classroom_blocks set payload = jsonb_set(payload,'{questions,0}', (payload->'questions'->0) - 'image'), updated_at = now()
  where lesson_id = '3894f232-5143-4498-aa0c-c575e0760cc1' and sort_order = 6;
update classroom_blocks set payload = jsonb_set(payload,'{html}','"<h3>Теперь соберём предложения 📝</h3><p>Молодец! Ты выполнил бóльшую часть заданий. Дальше — четыре задания, в каждом нужно собрать предложение из слов.</p>"'), updated_at = now()
  where lesson_id = '5c0e4d0a-b796-409e-a120-c1e6267d130b' and sort_order = 5;
update classroom_blocks set payload = jsonb_set(jsonb_set(payload,'{title}','"Составь вопросы ✍️"'),'{html}','"<p>Это последнее задание. Вспомни вопросы, которые мы учили несколько уроков назад. Обычно я задаю вопрос, а ты отвечаешь. А сейчас наоборот: я напишу ответы, а ты составь и запиши к ним вопросы.</p><p><i>Например: ответ «I''m eleven». Вопрос к нему — «How old are you?»</i></p><ol><li>I''m Paul.</li><li>P-A-U-L.</li><li>22 North Street, Oldtown.</li><li>It''s 02465 438967.</li><li>It''s paulharris@mymail.com.</li></ol>"'), updated_at = now()
  where lesson_id = '5c0e4d0a-b796-409e-a120-c1e6267d130b' and sort_order = 10;
update classroom_blocks set payload = jsonb_set(payload,'{html}','"<p><img src=\"https://classroom.wowteach.ru/media/shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>Надеюсь, ты перекусил перед домашним заданием, так как сегодня нас с тобой ждут вкусняшки 😋</p><p>Выполни все задания, чтобы выучить слова на 100%!</p>"'), updated_at = now()
  where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 0;
update classroom_blocks set payload = jsonb_set(payload,'{html}','"<p><img src=\"https://classroom.wowteach.ru/media/shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h3>Теперь слова в предложениях 🚀</h3><p>Ты уже узнаёшь продукты на картинках и на слух. Теперь поставим эти слова в предложения.</p>"'), updated_at = now()
  where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 6;
update classroom_blocks set payload = jsonb_set(jsonb_set(payload,'{title}','"Прочитай рассказ Макса и выбери подходящий вариант для каждого пропуска"'),'{questions,0}','{"q": "Hi! I have breakfast at 7 a.m. I usually have ___ and milk.", "type": "single", "correct": [0], "options": [{"text": "cereal"}, {"text": "chips"}]}'::jsonb), updated_at = now()
  where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 9;
update classroom_blocks set payload = jsonb_set(jsonb_set(payload,'{title}','"Вспомни рассказ Макса. Что Макс ест на завтрак, обед и ужин?"'),'{groups}','[{"name": "breakfast", "items": [{"text": "cereal"}, {"text": "milk"}]}, {"name": "lunch", "items": [{"text": "pasta"}, {"text": "tuna"}]}, {"name": "dinner", "items": [{"text": "chicken"}]}]'::jsonb), updated_at = now()
  where lesson_id = 'abf66c3b-2936-433e-adbf-e516a4552c8b' and sort_order = 10;
update classroom_blocks set payload = jsonb_set(jsonb_set(payload,'{title}','"Посмотри на картинку и напиши слово по-английски"'),'{items}', (select jsonb_agg(jsonb_set(it,'{prompt}','""') order by ord) from jsonb_array_elements(payload->'items') with ordinality t(it,ord))), updated_at = now()
  where lesson_id = '0c683af2-bcf7-4b35-9a5a-ca9b82ed81d6' and sort_order = 3;
update classroom_blocks set payload = jsonb_set(payload,'{html}','"<p><img src=\"https://classroom.wowteach.ru/media/shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h3>Новое правило 💪</h3><p>Слова ты уже знаешь — теперь разберёмся с исчисляемыми и неисчисляемыми существительными. После этих заданий ты будешь легко их различать.</p>"'), updated_at = now()
  where lesson_id = '0c683af2-bcf7-4b35-9a5a-ca9b82ed81d6' and sort_order = 4;
update classroom_blocks set payload = jsonb_set(payload,'{title}','"Прочитай рецепт Ани и выбери правильный вариант для каждого пропуска"'), updated_at = now()
  where lesson_id = '0c683af2-bcf7-4b35-9a5a-ca9b82ed81d6' and sort_order = 10;
update classroom_blocks set payload = jsonb_set(jsonb_set(payload,'{title}','"А теперь потренируемся составлять вопросы. Выбери правильный вариант"'),'{questions,0,q}','"___ there ___ sugar?"'), updated_at = now()
  where lesson_id = '0c683af2-bcf7-4b35-9a5a-ca9b82ed81d6' and sort_order = 11;
update classroom_blocks set payload = jsonb_set(jsonb_set(payload,'{title}','"Диалог о списке продуктов ✍️"'),'{html}','"<p>А это последнее задание. Составь и запиши диалог о списке продуктов. Можешь взять диалог из предыдущего упражнения в качестве примера. Удачи, ты обязательно справишься!</p><p><i>Shopping list: apples, carrots, chicken, cheese, curry sauce, doughnuts</i></p>"'), updated_at = now()
  where lesson_id = '0c683af2-bcf7-4b35-9a5a-ca9b82ed81d6' and sort_order = 14;
update classroom_blocks set payload = jsonb_set(payload,'{html}','"<p><img src=\"https://classroom.wowteach.ru/media/shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>В этом уроке мы научимся считать неисчисляемые продукты и спрашивать, сколько чего есть: <b>How much</b> и <b>How many</b>. Как это возможно? Давай начнём — и узнаешь!</p><p>У тебя всё получится. Удачи! ❤️</p>"'), updated_at = now()
  where lesson_id = 'd8fbeb71-a2ef-4bfd-a0d9-eb73dae5d5e0' and sort_order = 0;
update classroom_blocks set payload = jsonb_set(jsonb_set(payload,'{title}','"Свой диалог в кафе ✍️"'),'{html}','"<p>Осталось последнее задание. Твоя задача — составить и записать диалог. Используй диалог из предыдущих упражнений как пример.</p>"'), updated_at = now()
  where lesson_id = 'edb04172-9975-4411-bda8-74f5592a7a13' and sort_order = 7;
update classroom_blocks set payload = jsonb_set(payload,'{title}','"Прочитай текст о Сьюзи и ответь на вопросы"'), updated_at = now()
  where lesson_id = 'ccb8ec26-8db1-4014-ba1e-500fc48b8624' and sort_order = 3;
update classroom_blocks set payload = payload - 'audio', updated_at = now()
  where lesson_id = '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f' and sort_order = 1;
update classroom_blocks set payload = jsonb_set(jsonb_set(jsonb_set(payload,'{title}','"Прослушай аудио и выбери, что Пенни будет на завтрак. Верных ответов несколько"'),'{questions,0,q}','"What would Penny like for breakfast?"'),'{questions,0,audio}','"https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg2%20%2B%20gg3/gg2_u2_hw6_b2.mp3"'), updated_at = now()
  where lesson_id = '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f' and sort_order = 2;
update classroom_blocks set payload = jsonb_set(jsonb_set(jsonb_set(payload,'{title}','"Прослушай аудио ещё раз и выбери правильный вариант"'),'{questions,0,q}','"Penny has P.E. ___."'),'{questions,0,audio}','"https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg2%20%2B%20gg3/gg2_u2_hw6_b2.mp3"'), updated_at = now()
  where lesson_id = '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f' and sort_order = 3;
update classroom_blocks set payload = jsonb_set(payload,'{audio}','"https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg2%20%2B%20gg3/gg2_u2_hw6_b2.mp3"'), updated_at = now()
  where lesson_id = '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f' and sort_order = 4;
update classroom_blocks set payload = jsonb_set(payload,'{title}','"Прочитай письмо Стива и выбери because или so для каждого пропуска"'), updated_at = now()
  where lesson_id = '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f' and sort_order = 6;
update classroom_blocks set payload = jsonb_set(payload,'{html}','"<p><img src=\"https://classroom.wowteach.ru/media/shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>Рада, что ты заглянул в домашку! Сегодня мы с тобой выполним несколько полезных упражнений, которые помогут тебе закрепить полученные знания. Let''s go!</p>"'), updated_at = now()
  where lesson_id = '4d349ca7-4b58-48e8-824a-fcde5e710f54' and sort_order = 0;
update classroom_blocks set payload = jsonb_set(jsonb_set(payload,'{title}','"Рецепт любимого завтрака ✍️"'),'{html}','"<p>А это последнее задание. Напиши рецепт своего любимого завтрака. Можешь использовать рецепт тостов из предыдущего задания как пример.</p>"'), updated_at = now()
  where lesson_id = '4d349ca7-4b58-48e8-824a-fcde5e710f54' and sort_order = 8;

commit;
