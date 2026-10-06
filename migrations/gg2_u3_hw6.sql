-- Go Getter 2 · Unit 3 · Homework 6
-- собрано tools/gg2_build.py --lesson u3_hw6
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 3', 3 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 3');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 6', 'homework', 60, false, 5
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 3'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 6');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 5
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 3' and l.title = 'Homework 6';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 3' and l.title = 'Homework 6';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет, самый лучший ученик! 👋</h2><p>Как твои дела? Сегодня нас ждёт много классных заданий. Let's go 😉</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'text', replace($blk${"audio": "", "html": "<p>Сначала мы с тобой познакомимся с Гарри и Лили. Послушай их разговор и ниже выбери любимый гаджет каждого из ребят.</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'quiz', replace($blk${"questions": [{"q": "Harry: какой его любимый гаджет?", "type": "single", "image": "@@MEDIA@@gg2/u3/harry.webp", "options": [{"text": "phone"}, {"text": "tablet"}], "correct": [1]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'quiz', replace($blk${"questions": [{"q": "Lily: какой её любимый гаджет?", "type": "single", "image": "@@MEDIA@@gg2/u3/lily.webp", "options": [{"text": "phone"}, {"text": "tablet"}], "correct": [0]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'gaps', replace($blk${"title": "Послушай разговор Лили и Гарри ещё раз. Дополни предложения пропущенными словами", "mode": "type", "text": "1. Harry watches __films__ on TV and on his tablet.\n2. Harry likes __downloading__ videos.\n3. Lily chats __online__ a lot with her friends.\n4. Lily also likes __surfing__ the Internet.\n5. Lily takes her __phone__ everywhere. She can put it in her __jeans__ or __jacket__.", "audio": ""}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'sort', replace($blk${"title": "Проверим, насколько хорошо ты запомнил разговор Гарри и Лили :) Распредели их фразы в нужный столбик", "groups": [{"name": "Harry", "items": [{"text": "I've got a TV. I've also got a tablet."}, {"text": "I download my videos to my tablet."}]}, {"name": "Lily", "items": [{"text": "I've got a mobile phone and I've got a laptop too."}, {"text": "I also like surfing the Internet."}, {"text": "I can also put it in my jacket."}]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'gaps', replace($blk${"title": "Молодец! Половина домашки уже позади. Вспомни правило с урока и вставь нужные слова в пропуски", "mode": "drag", "text": "1. Too usually comes __at the end__ of a sentence.\n2. Also usually comes __before__ the verb.\n\nI listen to music on my CDs. I listen to music on my phone too.\nI use the computer to do my homework. I also use it to talk to my grandparents."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6),
('<lesson_id>', 'gaps', replace($blk${"title": "Уррра! А теперь давай всё закрепим. Впиши в пропуски also или too", "mode": "type", "text": "My name is Lily. I love technology. I've got a laptop. I've __also__ got a mobile phone. I chat online to my friends on my phone. I surf the Internet on my phone __too__. I play games on my laptop and I do my homework on my laptop __too__. My friend Harry __also__ likes technology. He's got a TV and a tablet __too__. He downloads videos to his tablet."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 7),
('<lesson_id>', 'task', replace($blk${"title": "Мои гаджеты", "needs_review": true, "html": "<p>Вау! Как отлично ты всё сделал. А теперь расскажи, какие гаджеты есть у тебя. Перепиши текст и заполни пропуски своими идеями.</p><p><i>My technology items: ___ and ___.<br>I use item 1 to ___.<br>I use item 2 to ___.<br>My friend's technology items: ___ and ___.<br>My friend uses ___ to ___.</i></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 8),
('<lesson_id>', 'speaking', replace($blk${"title": "Мой любимый гаджет 🎤", "needs_review": true, "html": "<p>А это задание необязательное, но если ты его сделаешь, то будешь мега крут 💪 Запиши свой рассказ про любимое электронное устройство и любимое электронное устройство твоего друга. Можешь послушать пример перед тем, как записывать своё аудио.</p>", "sample": ""}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 9),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:200px\"></p><h2>Спасибо тебе огромное за твой труд!</h2><p>Всё сделано просто великолепно! До встречи на уроке 😄</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 10)
returning sort_order, type;
