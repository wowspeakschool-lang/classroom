-- Go Getter 2 · Unit 6 · Jobs · Homework 5
-- собрано tools/gg2_build.py --lesson u6_hw5
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 6 · Jobs', 6 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 6 · Jobs');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 5', 'homework', 60, false, 4
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 6 · Jobs'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 5');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 4
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 6 · Jobs' and l.title = 'Homework 5';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 6 · Jobs' and l.title = 'Homework 5';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 😎</h2><p>Сегодня тебе предстоит много читать :) Но ты точно справишься, ведь для тебя нет ничего невозможного. Давай начнём?</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'text', replace($blk${"html": "<h3>Для начала давай прочитаем текст</h3><p><i>Do you think that a child's life was different in the past? I asked my dad and grandpa.</i></p><p><b>Dad:</b> When I was a boy I helped my mum with jobs in the house every weekend. She gave me 50p when I washed the car or I tidied the living room. It wasn't a lot of money, but I did many jobs! When I had the money, I bought an expensive football. It was really cool and all my friends liked it.</p><p><b>Grandpa:</b> My family was poor, so there wasn't any pocket money! But I wanted some money, so I got a Saturday job at a restaurant. I washed the dishes and the floor, and I put the plates on the tables. I made a lot of money and when I was sixteen I bought a bicycle. I went everywhere on that bike!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'quiz', replace($blk${"title": "Прочитай статью ещё раз и выбери подходящее для неё название", "questions": [{"q": "What is the best title for the article?", "type": "single", "options": [{"text": "The house jobs my dad did"}, {"text": "How Grandpa bought a bike"}, {"text": "When Dad and Grandpa were children"}], "correct": [2]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'truefalse', replace($blk${"title": "Прочитай текст ещё раз: True (правда) или False (неправда)? Читай внимательно и не торопись", "statements": [{"text": "Dad helped his mum every Saturday and Sunday.", "correct": true}, {"text": "Dad's mum gave him a lot of money.", "correct": false}, {"text": "Dad tidied the living room.", "correct": true}, {"text": "Dad's friends liked his football.", "correct": true}, {"text": "Grandpa worked every Sunday.", "correct": false}, {"text": "Grandpa bought a bike when he was 16.", "correct": true}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'task', replace($blk${"title": "Опиши картинку в прошедшем времени", "needs_review": true, "html": "<p>Ты уже на финишной прямой! Посмотри внимательно на картинку и опиши, что делали люди разных профессий. Напиши не меньше 5 предложений. Не забудь про Past Simple!</p><p><i>For example: An artist emptied the bin.</i></p><p><img src=\"@@MEDIA@@gg2/u6/book_jobs_chores.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! 🎉</h3><p>Ты справился с домашним заданием просто прекрасно. Самое время немножко отдохнуть. Увидимся на занятии :)</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5)
returning sort_order, type;
