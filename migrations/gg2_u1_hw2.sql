-- Go Getter 2 · Unit 1 · Homework 2
-- собрано tools/gg2_build.py --lesson u1_hw2
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 1', 1 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 1');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 2', 'homework', 60, false, 1
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 1'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 2');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 1
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 1' and l.title = 'Homework 2';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 1' and l.title = 'Homework 2';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание! 👋</h2><p>Сегодня мы с тобой научимся рассказывать о своём распорядке дня. Выполни все задания — и получишь звание чемпиона английского 💪</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'text', replace($blk${"html": "<p>Для начала посмотри видео. <b>What do Anna, Max and Hammy do after school?</b></p><p><img src=\"@@MEDIA@@gg2/u1/book_after_school.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'video', replace($blk${"title": "Видео: Anna, Max and Hammy after school", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'quiz', replace($blk${"title": "Выбери правильный вариант ответа для каждого пропуска", "questions": [{"q": "We ___ sandwiches.", "type": "single", "options": [{"text": "eat"}, {"text": "eats"}], "correct": [0]}, {"q": "Hammy ___ them too.", "type": "single", "options": [{"text": "eat"}, {"text": "eats"}], "correct": [1]}, {"q": "We ___ up.", "type": "single", "options": [{"text": "tidies"}, {"text": "tidy"}], "correct": [1]}, {"q": "Hammy ___ up too.", "type": "single", "options": [{"text": "tidies"}, {"text": "tidy"}], "correct": [0]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'sequence', replace($blk${"title": "Посмотри видео ещё раз и расставь предложения в том порядке, как они идут в рассказе. У тебя получится!", "items": [{"text": "I go to Max's house."}, {"text": "We do our homework."}, {"text": "Hammy helps."}, {"text": "We have some drinks."}, {"text": "We eat sandwiches."}, {"text": "Hammy eats them too."}, {"text": "We tidy up."}, {"text": "Hammy tidies up too."}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'gaps', replace($blk${"title": "Отлично! А теперь практика: перетащи нужный глагол в каждый пропуск", "mode": "drag", "text": "1. My sister __likes__ going to the cinema.\n2. Frank __goes__ to school with his sister.\n3. My parents __like__ reading.\n4. We __play__ basketball at school.\n5. I __go__ to bed at 8 o'clock.\n6. She __plays__ computer games on Sunday."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:200px\"></p><h3>Ура! 🎉</h3><p>Ты справился с домашней работой. Ты молодец! Увидимся на занятии! Bye!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6)
returning sort_order, type;
