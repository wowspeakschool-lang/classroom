-- Go Getter 2 · Unit 1 · School · Homework 6
-- собрано tools/gg2_build.py --lesson u1_hw6
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 1 · School', 1 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 1 · School');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 6', 'homework', 60, false, 5
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 1 · School'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 6');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 5
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 1 · School' and l.title = 'Homework 6';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 1 · School' and l.title = 'Homework 6';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание! 👋</h2><p>Сегодня тебя ждут интересная аудиозапись и увлекательные упражнения. Let's go!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'text', replace($blk${"html": "<p>Давай начнём с аудио. Это — Марк. Он расскажет нам о своих школьных предметах. Но прежде чем слушать Марка, попробуй угадать: какой у него любимый школьный предмет?</p><p><img src=\"@@MEDIA@@gg2/u1/mark.webp\" alt=\"\" style=\"height:240px\"></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'video', replace($blk${"title": "Послушай, как Марк рассказывает о своих предметах", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'quiz', replace($blk${"title": "Послушай аудио и заполни расписание Марка: выбери день недели для каждого предмета", "questions": [{"q": "French: on ___", "type": "single", "options": [{"text": "Monday"}, {"text": "Tuesday"}], "correct": [1]}, {"q": "Science: on ___ (первый день)", "type": "single", "options": [{"text": "Monday"}, {"text": "Tuesday"}], "correct": [0]}, {"q": "Science: and on ___ (второй день)", "type": "single", "options": [{"text": "Thursday"}, {"text": "Friday"}], "correct": [0]}, {"q": "History: on ___ (первый день)", "type": "single", "options": [{"text": "Thursday"}, {"text": "Wednesday"}], "correct": [1]}, {"q": "History: and on ___ (второй день)", "type": "single", "options": [{"text": "Sunday"}, {"text": "Friday"}], "correct": [1]}, {"q": "Football: on ___", "type": "single", "options": [{"text": "Sunday"}, {"text": "Monday"}], "correct": [0]}, {"q": "Chess: on ___", "type": "single", "options": [{"text": "Friday"}, {"text": "Saturday"}], "correct": [1]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'quiz', replace($blk${"title": "Послушай аудио ещё раз. Это правда (True) или неправда (False)?", "questions": [{"q": "Mark's favourite subject is French.", "type": "single", "options": [{"text": "True"}, {"text": "False"}], "correct": [0], "image": "@@MEDIA@@gg2/u1/subj_french.webp"}, {"q": "He likes History.", "type": "single", "options": [{"text": "True"}, {"text": "False"}], "correct": [1], "image": "@@MEDIA@@gg2/u1/history_lesson.webp"}, {"q": "Mark likes Science.", "type": "single", "options": [{"text": "True"}, {"text": "False"}], "correct": [0], "image": "@@MEDIA@@gg2/u1/mark_science.webp"}, {"q": "He plays football at school.", "type": "single", "options": [{"text": "True"}, {"text": "False"}], "correct": [1], "image": "@@MEDIA@@gg2/u1/kids_football.webp"}, {"q": "He always plays chess on Sunday.", "type": "single", "options": [{"text": "True"}, {"text": "False"}], "correct": [1], "image": "@@MEDIA@@gg2/u1/mark_chess.webp"}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'text', replace($blk${"html": "<h3>Молодец! 👏</h3><p>Ты справился с большей частью заданий. А какой твой любимый день недели? Давай почитаем о Лили и её любимом дне.</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'gaps', replace($blk${"title": "Прочитай рассказ Лили и перетащи слова в пропуски", "mode": "drag", "image": "@@MEDIA@@gg2/u1/lily_bus.webp", "text": "Hi! My __name__ is Lily. My __favourite__ day is Tuesday. On Tuesday I get up __at__ 7.30. I meet my friends at 8 __o'clock__ and we get the bus to school. We often talk about our favourite computer __games__. __On__ Tuesday, we have Music, Computer Studies and __English__. They are my favourite __subjects__! __In__ the morning, we have Music. We sometimes sing and I usually play __the piano__. I have __pizza__ at lunchtime. Tuesday is pizza day in the canteen! In the evening, after school, I always __do__ ballet."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6),
('<lesson_id>', 'task', replace($blk${"title": "Мой любимый день ✍️", "needs_review": true, "html": "<p>Ура, это последнее задание! Напиши о своём любимом дне недели. Используй рассказ Лили как пример. Удачи!</p><p><i>Например: My favourite day is … On … I get up at … We have …</i></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 7),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:200px\"></p><h3>Поздравляю! 🌟</h3><p>Ты завершил домашнее задание. Ты — супер ученик! Жду тебя на занятии!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 8)
returning sort_order, type;
