-- Go Getter 2 · Unit 5 · My town · Homework 4
-- собрано tools/gg2_build.py --lesson u5_hw4
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 5 · My town', 5 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 5 · My town');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 4', 'homework', 60, false, 3
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 5 · My town'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 4');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 3
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 5 · My town' and l.title = 'Homework 4';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 5 · My town' and l.title = 'Homework 4';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет!</h2><p>Здесь тебя ждёт новая домашняя работа. Сегодня мы будем вспоминать, как правильно указывать дорогу, разговаривать и делать разные упражнения. У тебя всё получится, как и всегда 😃 Давай приступим :)</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'text', replace($blk${"html": "<h3>Communication: Directions</h3><p>Узнаёшь табличку? Внимательно изучи её, а затем выполни упражнения.</p><p><b>Asking for directions</b><br>Excuse me. Where's <i>North Street</i>?<br>I'm looking for <i>a library</i>.<br>How can I get to <i>the Science Museum</i>?<br>Is it far?</p><p><b>Giving directions</b><br>It's in/on <i>Green Street</i>.<br>Go straight on.<br>Go past <i>the cinema</i>.<br>Turn left. / Turn right.<br>It's on the left. / It's on the right.</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'text', replace($blk${"html": "<h3>Excuse me. Where's the hospital?</h3><p>Внимательно посмотри на карту: красная стрелка — это начало пути. В следующем задании заполни пропуски, удачи! ;)</p><p><img src=\"@@MEDIA@@gg2/u5/book_map_hospital.webp\" alt=\"Карта: путь к больнице\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'gaps', replace($blk${"title": "Заполни пропуски по карте", "mode": "drag", "text": "1. __Go__ straight on.\n2. Then __turn__ right.\n3. Go __past__ the bank.\n4. Turn __left__.\n5. Go __straight__ on and then turn right.\n6. The hospital is __on__ the right.\n7. It's __opposite__ the museum."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'gaps', replace($blk${"title": "Задание посложнее — но в табличку можно подглядывать ;) Прочитай диалог и впиши недостающие слова", "mode": "type", "text": "A: __Excuse__ me. I'm __looking__ for the History Museum. Is it __far__?\nB: No, it's not far. It's __in|on__ Brown Street. Go __past__ the bank. Then __turn__ right — that's Brown Street.\nA: OK.\nB: Go __straight__ __on__. The museum is __on__ the left, opposite the park.\nA: Thank you."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'text', replace($blk${"html": "<h3>Карта: River Street и Smith Street</h3><p>Посмотри на карту. Красная точка — это ты. В следующем задании заполни пропуски в диалогах, вписывай слова внимательно!</p><p><img src=\"@@MEDIA@@gg2/u5/book_map_river.webp\" alt=\"Карта River Street и Smith Street\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'gaps', replace($blk${"title": "Впиши слова в диалоги по карте (красная точка — это ты)", "mode": "type", "text": "1. A: Excuse me. Where's the cinema?\nB: It's in __River__ Street. __Go__ past the supermarket. Turn __right__ at the __café|cafe__. Then go straight on. The cinema is on the __right__, opposite the __restaurant__.\n\n2. A: Excuse me. How can I get to the park?\nB: It's not far. Go __straight__ on. Go past the __supermarket__, café and the __bank__. They are all on the right. The park is next to the bank, __on__ the right.\n\n3. A: Excuse me. I'm looking for the shoe shop.\nB: It's in River Street. Go __straight__ __on__. Then __turn__ __left__. The shoe shop is on the left."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6),
('<lesson_id>', 'task', replace($blk${"title": "Дополнительное задание — для самых стойких и терпеливых! ⭐", "needs_review": true, "html": "<p>Представь, что ты помогаешь кому-то найти дорогу. Напиши диалог, используя примеры выше и карту из предыдущего задания. У тебя получится!</p><p><img src=\"@@MEDIA@@gg2/u5/book_map_river.webp\" alt=\"Карта\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 7),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Bye-bye! 🚌</h3><p>Ты отлично справился. До встречи на уроке!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 8)
returning sort_order, type;
