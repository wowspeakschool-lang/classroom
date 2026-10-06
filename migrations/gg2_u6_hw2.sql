-- Go Getter 2 · Unit 6 · Homework 2
-- собрано tools/gg2_build.py --lesson u6_hw2
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 6', 6 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 6');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 2', 'homework', 60, false, 1
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 6'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 2');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 1
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 6' and l.title = 'Homework 2';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 6' and l.title = 'Homework 2';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Огромный привет! 😉</h2><p>В этой домашней работе мы повторим всё то, что ты прошёл на уроке с учителем. Это поможет тебе не только всё запомнить, но и использовать :))</p><p>К этому домашнему заданию есть дополнение! Оно необязательное, но если ты его выполнишь, учитель даст тебе дополнительную ⭐ Давай начинать!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'video', replace($blk${"title": "Давай начнём с видео. Посмотри его, а потом сделай задания ниже.", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'match', replace($blk${"title": "Супер! Посмотри видео ещё раз и соедини глаголы по парам", "pairs": [{"left": "play", "right": "played", "right_audio_tts": "played"}, {"left": "dance", "right": "danced", "right_audio_tts": "danced"}, {"left": "try", "right": "tried", "right_audio_tts": "tried"}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'text', replace($blk${"html": "<h3>Молодец! 👍</h3><p>Посмотри видео ещё раз и расставь слова в предложениях по смыслу.</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'order', replace($blk${"words": ["My", "mum", "played", "the", "drums."], "sentence": "My mum played the drums.", "audio_tts": "My mum played the drums."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'order', replace($blk${"words": ["My", "dad", "danced."], "sentence": "My dad danced.", "audio_tts": "My dad danced."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'order', replace($blk${"words": ["They", "wanted", "to", "be", "pop stars."], "sentence": "They wanted to be pop stars.", "audio_tts": "They wanted to be pop stars."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6),
('<lesson_id>', 'order', replace($blk${"words": ["They", "tried", "hard."], "sentence": "They tried hard.", "audio_tts": "They tried hard."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 7),
('<lesson_id>', 'gaps', replace($blk${"title": "Перейдём к практике! Расставь пропущенные слова в предложения по смыслу", "mode": "drag", "text": "1. My aunt __phoned__ me last Saturday on my mobile.\n2. She __invited__ me to Harry's birthday party.\n3. I __stopped__ on the way at the toy shop for a present.\n4. Harry and his friends __listened__ to music.\n5. I __helped__ my aunt with the food.\n6. Harry __liked__ his party!"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 8),
('<lesson_id>', 'task', replace($blk${"title": "Задание для чемпионов! За него ты получишь дополнительный балл ;)", "needs_review": true, "html": "<p>Напиши 4 предложения о себе, используя Past Simple.</p><p><i>For example:<br>I played computer games on Monday.<br>I danced at school on Thursday.</i></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 9),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты МЕГАКРУТ! ⭐</h3><p>Основная часть готова — ты так здорово потрудился!</p><p>Дальше — <b>дополнительная часть</b>. Она необязательная, но если ты её сделаешь, получишь дополнительную ⭐ Давай начинать 😉</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 10),
('<lesson_id>', 'text', replace($blk${"html": "<h3>Маркеры прошедшего времени</h3><p>Внимательно изучи табличку: эти слова подсказывают, что действие было в прошлом — значит, нужен Past Simple.</p><p><b>Past Simple:</b></p><ul><li><b>last week</b> — на прошлой неделе</li><li><b>2 days ago</b> — 2 дня назад</li><li><b>in 1999</b> — в 1999 году</li><li><b>yesterday</b> — вчера</li></ul>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 11),
('<lesson_id>', 'gaps', replace($blk${"title": "Посмотри на картинку: сейчас 04:00, май, вторник. Сколько времени прошло? Заполни пропуски. Первый ответ подсказан на картинке.", "mode": "drag", "image": "@@MEDIA@@gg2/u6/book_time_now.webp", "text": "1. 03:00 — __an hour ago__\n2. 03:50 — __10 minutes ago__\n3. March — __2 months ago__\n4. Saturday — __3 days ago__"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 12),
('<lesson_id>', 'match', replace($blk${"title": "Здорово! Ты так хорошо справляешься! Посмотри на маркеры Past Simple и соедини их с переводом", "pairs": [{"left": "yesterday", "right": "вчера"}, {"left": "last week", "right": "на прошлой неделе"}, {"left": "last year", "right": "в прошлом году"}, {"left": "last Saturday", "right": "в прошлую субботу"}, {"left": "two days ago", "right": "два дня назад"}, {"left": "an hour ago", "right": "час назад"}, {"left": "in 1999", "right": "в 1999 году"}, {"left": "this morning", "right": "сегодня утром"}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 13),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Hurray! 🌟</h3><p>Домашняя работа выполнена на отлично — всё благодаря твоим стараниям. Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 14)
returning sort_order, type;
