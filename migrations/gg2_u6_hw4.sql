-- Go Getter 2 · Unit 6 · Homework 4
-- собрано tools/gg2_build.py --lesson u6_hw4
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 6', 6 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 6');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 4', 'homework', 60, false, 3
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 6'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 4');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 3
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 6' and l.title = 'Homework 4';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 6' and l.title = 'Homework 4';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет, самый старательный и классный ученик! 😎</h2><p>Сегодня мы будем вспоминать слова, которые ты учил на занятии. Давай начнём?</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'text', replace($blk${"html": "<h3>Asking for and giving permission</h3><p>Начнём с небольшой таблички — узнаёшь? Так просят разрешения и отвечают на просьбу.</p><p><b>Can I borrow a pen, please?</b><br>Yes, you can. / No, sorry, you can't. / Sure, no problem.</p><p><b>Is it OK if I use your mobile?</b><br>No, sorry, it isn't OK. / Oh, all right. / Yes, that's fine.</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'text', replace($blk${"html": "<p>Итак, приступим к упражнению! Подглядывай в табличку и расставь слова в правильном порядке.</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'order', replace($blk${"words": ["Can", "I", "borrow", "a", "pen,", "please?"], "sentence": "Can I borrow a pen, please?", "audio_tts": "Can I borrow a pen, please?"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'order', replace($blk${"words": ["Yes,", "you", "can."], "sentence": "Yes, you can.", "audio_tts": "Yes, you can."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'order', replace($blk${"words": ["Is", "it", "OK", "if", "I", "use", "your", "mobile?"], "sentence": "Is it OK if I use your mobile?", "audio_tts": "Is it OK if I use your mobile?"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'order', replace($blk${"words": ["No,", "sorry,", "it", "isn't", "OK."], "sentence": "No, sorry, it isn't OK.", "audio_tts": "No, sorry, it isn't OK."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6),
('<lesson_id>', 'order', replace($blk${"words": ["Sure,", "no", "problem."], "sentence": "Sure, no problem.", "audio_tts": "Sure, no problem."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 7),
('<lesson_id>', 'gaps', replace($blk${"title": "Следующее задание немного посложнее… Можно подглядывать в табличку ;) Прочитай диалоги и заполни пропуски", "mode": "drag", "text": "Dialogue 1\nElena: We've got a Maths test today. Have you got your calculator this time?\nTom: Oh no, I forgot it. __Is it OK if I use yours__?\nElena: __No, it isn't.__ I need it for the test!\nTom: OK, I understand. I hope the test is easy!\n\nDialogue 2\nJess: Hi Tom. Do you want to go to the cinema?\nMatt: Sure, but I have to ask my mum first. __Can I borrow your mobile, please?__ I don't have my phone with me.\nJess: __Yes, you can__. Here you are.\nMatt: Thanks. Oh, hi mum. __Please can I go to the cinema?__\nMum: __Sure, no problem.__"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 8),
('<lesson_id>', 'task', replace($blk${"title": "Напиши 2 вежливые просьбы", "needs_review": true, "html": "<p>Ты отлично справляешься! Осталось одно задание из основной части. Напиши каждую просьбу двумя способами. Не забудь <b>please</b> — будь вежливым!</p><p><i>Пример. You want to go to the cinema.<br>a) Please can I go to the cinema?<br>b) Can I go to the cinema, please?</i></p><ol><li>You want to use your dad's laptop.<br>a) …<br>b) …</li><li>You want to borrow a friend's mobile.<br>a) …<br>b) …</li></ol>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 9),
('<lesson_id>', 'task', replace($blk${"title": "Дополнительное задание — для самых стойких и терпеливых! ⭐", "needs_review": true, "html": "<p>Внимательно посмотри на записку. Пол и Лео хотят пойти в бассейн и спрашивают разрешения у папы Лео. Напиши их диалог: как они просят и как папа отвечает. У тебя получится!</p><p><img src=\"@@MEDIA@@gg2/u6/book_permission_note.webp\" alt=\"Who: Paul and Leo. Where: go to the swimming pool. Ask Leo's dad for permission. Permission: No. Why: homework\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 10),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Hurray! 🌟</h3><p>Домашняя работа выполнена на отлично — всё благодаря твоим стараниям. Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 11)
returning sort_order, type;
