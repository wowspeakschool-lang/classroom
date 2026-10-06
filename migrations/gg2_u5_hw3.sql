-- Go Getter 2 · Unit 5 · Homework 3
-- собрано tools/gg2_build.py --lesson u5_hw3
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 5', 5 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 5');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 3', 'homework', 60, false, 2
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 5'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 3');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 2
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 5' and l.title = 'Homework 3';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 5' and l.title = 'Homework 3';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Огромный привет!</h2><p>В этой домашней работе мы повторим всё, что ты прошёл на уроке с учителем. Это поможет тебе не только всё запомнить, но и использовать :) Давай начинать 😉</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'video', replace($blk${"title": "Давай начнём с видео. Посмотри его, а потом сделай задание ниже", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'match', replace($blk${"title": "Посмотри видео ещё раз и соедини вопросы с ответами, как в видео", "pairs": [{"left": "Were you in the garden?", "left_image": "@@MEDIA@@gg2/u5/garden.webp", "right": "No, I wasn't. I was with my friends.", "right_audio_tts": "No, I wasn't. I was with my friends."}, {"left": "Were you in the park?", "left_image": "@@MEDIA@@gg2/u5/park_small.webp", "right": "No, we weren't.", "right_audio_tts": "No, we weren't."}, {"left": "Were you in the kitchen?", "left_image": "@@MEDIA@@gg2/u5/kitchen.webp", "right": "Yes, we were!", "right_audio_tts": "Yes, we were!"}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'quiz', replace($blk${"title": "Время серьёзной практики! Прочитай и выбери правильный ответ", "questions": [{"q": "A: Were you at the bank?<br>B: Yes, I ___.", "type": "single", "options": [{"text": "was"}, {"text": "wasn't"}], "correct": [0]}, {"q": "A: Was Andy sad?<br>B: No, he ___.", "type": "single", "options": [{"text": "were"}, {"text": "wasn't"}], "correct": [1]}, {"q": "A: Was it cold yesterday?<br>B: No, it ___.", "type": "single", "options": [{"text": "wasn't"}, {"text": "weren't"}], "correct": [0]}, {"q": "A: Were your friends at your house?<br>B: Yes, ___.", "type": "single", "options": [{"text": "we were"}, {"text": "they were"}], "correct": [1]}, {"q": "A: Was Anna there?<br>B: Yes, ___.", "type": "single", "options": [{"text": "she was"}, {"text": "he was"}], "correct": [0]}, {"q": "A: Were you late to work?<br>B: No, we ___.", "type": "single", "options": [{"text": "wasn't"}, {"text": "weren't"}], "correct": [1]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'gaps', replace($blk${"title": "Впиши в вопросы was или were, а потом дополни ответы: ✓ — ответ «да», ✗ — ответ «нет». Первый пункт — пример", "mode": "type", "text": "1. Were you at home last night? ✓ Yes, I was.\n2. __Was__ Oliver happy yesterday? ✗ __No__, __he wasn't|he wasn’t__.\n3. __Were__ you and Ted at the cinema together? ✓ __Yes__, __we were__.\n4. __Were__ all your friends at your party? ✗ __No__, __they weren't|they weren’t__.\n5. __Was__ I the fastest in the race? ✓ __Yes__, __you were__.\n6. __Was__ Katy at school last Friday? ✓ __Yes__, __she was__."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'task', replace($blk${"title": "Составь вопросы и ответы по примеру", "needs_review": true, "html": "<p>Ты уже на финишной прямой! Посмотри на пункт 1 — это пример: мы задали вопрос и дали ответ (отрицательный, потому что стоит крестик). Напиши так же вопросы и ответы к пунктам 2–5.</p><ol><li>Carla / angry yesterday ✗ — <i>Was Carla angry yesterday? No, she wasn't.</i></li><li>the muffins / in the fridge / yesterday ✓</li><li>the muffins / good yesterday ✓</li><li>the muffins / next to the eggs yesterday ✗</li><li>the muffins / next to the pizzas ✓</li></ol>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'task', replace($blk${"title": "Дополнительное задание — для чемпионов! ⭐", "needs_review": true, "html": "<p>За него ты получишь дополнительный балл! ;) Напиши 2 предложения о том, где ты был, и 2 предложения о том, где ты не был на выходных.</p><p><i>Например: I was at the cinema on Saturday. I wasn't at the supermarket.</i></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:180px\"></p><h3>Bye! 👋</h3><p>Отличная работа! До встречи на уроке!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 7)
returning sort_order, type;
