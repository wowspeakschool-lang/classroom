-- Инструкции заданий по-русски (решение Анны 05.11.2026: «Инструкции на русском же должны быть»)
-- Копия затронутых блоков — classroom_backup_russkie_zagolovki_20261105

-- 1. Говорение: единый русский заголовок вместо английской метки
update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb('SPEAKING 🎤 Расскажи вслух и запиши ответ'::text))
where type='speaking' and payload->>'title' in
  ('SPEAKING TASK 🎤','SPEAKING 🎤','SPEAKING TASK');

update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb('SPEAKING 🎤 Часть 1 · Расскажи вслух и запиши ответ'::text))
where type='speaking' and payload->>'title' in
  ('SPEAKING I 🎤','SPEAKING TASK 1 🎤','SPEAKING TASK · Part 1 🎤','SPEAKING TASK · Part 1',
   'SPEAKING TASK 🎤 Part 1','SPEAKING TASK PART 1 🎤','SPEAKING TASK. PART 1 🎤');

update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb('SPEAKING 🎤 Часть 2 · Расскажи вслух и запиши ответ'::text))
where type='speaking' and payload->>'title' in
  ('SPEAKING II 🎤','SPEAKING TASK 2 🎤','SPEAKING TASK · Part 2 🎤','SPEAKING TASK · Part 2',
   'SPEAKING TASK 🎤 Part 2','SPEAKING TASK PART 2 🎤','SPEAKING TASK. PART 2 🎤');

update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb('SPEAKING 🎤 Часть 3 · Расскажи вслух и запиши ответ'::text))
where type='speaking' and payload->>'title' = 'SPEAKING TASK · Part 3 🎤';

-- 2. Письменное задание
update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb('WRITING ✍️ Письменное задание'::text))
where payload->>'title' = 'WRITING TASK ✍️';

-- 3. Квизы и прочие задания с английским заголовком
update classroom_blocks set payload = jsonb_set(payload, '{title}', to_jsonb(v.ru))
from (values
 ('True or false?',                                        'Верно или неверно?'),
 ('Match the place with what you can do there.',           'Соедини место и то, что там можно делать'),
 ('Containers — write the missing word.',                  'Упаковки и ёмкости. Впиши пропущенное слово'),
 ('People — choose the right word.',                       'Какие это люди? Выбери подходящее слово'),
 ('Which shop is it?',                                     'Какой это магазин? Выбери ответ'),
 ('Phones — choose the right word.',                       'Телефоны. Выбери подходящее слово'),
 ('What is the problem?',                                  'Что случилось? Выбери ответ'),
 ('The body — choose the right word.',                     'Тело человека. Выбери подходящее слово'),
 ('How does the food taste?',                              'Какая еда на вкус? Выбери подходящее слово'),
 ('Homes and things in the house — choose the right word.','Дом и вещи в доме. Выбери подходящее слово'),
 ('Choose the correct phrasal verb.',                      'Выбери подходящий фразовый глагол'),
 ('Being polite — choose the right word.',                 'Вежливость. Выбери подходящее слово'),
 ('Choose the correct answer.',                            'Выбери правильный вариант'),
 ('Look at the picture. Choose True or False.',            'Посмотри на картинку. Верно или неверно?'),
 ('What is she like?',                                     'Какая она? Посмотри видео и запиши слова'),
 ('Make the word: hen',                                    'Собери слово: hen'),
 ('Make the word: hat',                                    'Собери слово: hat'),
 ('Make the word: ham',                                    'Собери слово: ham'),
 ('Match big and small.',                                  'Соедини большое и маленькое'),
 ('Whose · this / that / these / those',                   'Чей это предмет? Выбери this / that / these / those'),
 ('Look, read and write sentences · Tim',                  'Посмотри, прочитай и напиши предложения · Тим'),
 ('Look, read and write sentences · Anna',                 'Посмотри, прочитай и напиши предложения · Анна'),
 ('Look and write sentences',                              'Посмотри на таблицу и напиши предложения'),
 ('Write about you',                                       'Напиши о себе'),
 ('Answer the questions about the story',                  'Ответь на вопросы по истории'),
 ('Read the story again and answer the questions',         'Прочитай историю ещё раз и ответь на вопросы'),
 ('Read the story and choose: True or False',              'Прочитай историю и выбери: верно или неверно'),
 ('What orange vegetable is in the video?',                'Какой оранжевый овощ показан в видео? Напиши ответ'),
 ('🏆',                                                     '🏆 Скажи вслух и запиши ответ'),
 ('✏️',                                                     '✏️ Последнее задание'),
 ('🎤 My Sense Story',                                      '🎤 Расскажи про то, что тебя окружает')
) as v(en, ru)
where classroom_blocks.payload->>'title' = v.en;

-- 4. Заголовки из одного значка 🎤 — по смыслу задания
update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb('🎤 Назови предметы на картинке'::text))
where id = (select b.id from classroom_blocks b
  join classroom_lessons l on l.id=b.lesson_id join classroom_units u on u.id=l.unit_id
  join classroom_courses c on c.id=u.course_id
  where c.slug='sm1' and u.sort_order=1 and l.title='Homework 7' and b.sort_order+1=8);

update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb('🎤 Ответь вслух и запиши ответ'::text))
where type='speaking' and payload->>'title' = '🎤';

update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb('🎤 Расскажи, чем ты занимаешься в разные дни недели'::text))
where payload->>'title' = 'What do you do on Mondays? 🎤';

-- 5. Смешанные заголовки: английское начало — на русский
update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb('Какие это люди? Прочитай описание и впиши слово'::text))
where payload->>'title' = 'What are these people like? Прочитай описание и впиши слово';

update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb('Вставь слова из рамки в текст. Первое слово (cottage) — пример, оно уже вставлено.'::text))
where payload->>'title' = 'Complete the text with the words in the box. Первое слово (cottage) — пример, оно уже вставлено.';

update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb('Посмотри на картинку и ответь · Где что лежит?'::text))
where payload->>'title' = 'Look and answer · Где что лежит?';

update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb('Спроси и ответь · Где животные?'::text))
where payload->>'title' = 'Ask and answer · Где животные?';

update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb('Сколько их? Посмотри на картинку и посчитай'::text))
where payload->>'title' = 'How many? Посмотри на картинку и посчитай';

-- 6. GG3 Final Test: письменное задание целиком по-английски
update classroom_blocks set payload = jsonb_set(payload, '{html}', to_jsonb(
 '<p>Напиши 70–80 слов о самом лучшем дне в этом году. Ответь на вопросы:</p><ol><li>Where were you and who were you with?</li><li>What were you doing?</li><li>What happened?</li><li>Why was it the best day? How did you feel?</li></ol>'::text))
where id = '660bfae4-2df7-4201-baea-3b1ccbb578e6';
