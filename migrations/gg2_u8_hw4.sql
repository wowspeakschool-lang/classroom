-- Go Getter 2 · Unit 8 · Homework 4
-- собрано tools/gg2_build.py --lesson u8_hw4
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 8', 8 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 8');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 4', 'homework', 60, false, 3
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 8'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 4');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 3
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 8' and l.title = 'Homework 4';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 8' and l.title = 'Homework 4';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>Готов выполнять домашнее задание? В этом уроке тебя ждёт интересное видео и классные задания!</p><p>В конце урока есть дополнительное задание — его можно выполнить по желанию, НО если выполнишь, то будешь нереально крут!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'text', replace($blk${"html": "<p>Давай начнём с просмотра видео! Куда собираются пойти ребята?</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'video', replace($blk${"title": "Посмотри видео: куда собираются пойти ребята?", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'match', replace($blk${"title": "Посмотри видео выше и соедини вопросы с ответами.", "pairs": [{"left": "Are you busy next Thursday?", "right": "No. Why?", "right_audio_tts": "No. Why?"}, {"left": "Would you like to come?", "right": "That sounds great! I'd love to come.", "right_audio_tts": "That sounds great! I'd love to come."}, {"left": "What time does it start?", "right": "At half past six.", "right_audio_tts": "At half past six."}, {"left": "Where shall we meet?", "right": "Let's meet outside the Arena at six o'clock.", "right_audio_tts": "Let's meet outside the Arena at six o'clock."}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'gaps', replace($blk${"title": "Прочитай диалог и впиши пропущенные слова", "mode": "type", "text": "Maria: Hi Alison. Are you __busy__ next Tuesday?\nAlison: No. Why?\nMaria: I've got four tickets for a dance show. __Would you__ and your mum like to come?\nAlison: __I'd love|I'd like|I would love|I would like|I’d love|I’d like__ to come. Let's text my mum and ask. What time does it start?\nMaria: At half past seven. It's at the Old Theatre near the underground.\nAlison: Great, Mum texted me and said yes. Where __shall we__ meet?\nMaria: __Let's meet|Let’s meet|Let us meet__ outside the underground station at seven o'clock.\nAlison: Great. See you then."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'text', replace($blk${"html": "<p>Давай ещё немного потренируемся! Соедини первую часть предложения со второй!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'match', replace($blk${"title": "Посмотри внимательно на предложения! Попробуй соединить их!", "pairs": [{"left": "Are you", "right": "busy next Tuesday?", "right_audio_tts": "busy next Tuesday?"}, {"left": "I've got tickets", "right": "for a football match.", "right_audio_tts": "for a football match."}, {"left": "Would you", "right": "like to come?", "right_audio_tts": "like to come?"}, {"left": "That sounds", "right": "great.", "right_audio_tts": "great."}, {"left": "I'd", "right": "love to come.", "right_audio_tts": "love to come."}, {"left": "What time", "right": "does it start?", "right_audio_tts": "does it start?"}, {"left": "Where shall", "right": "we meet?", "right_audio_tts": "we meet?"}, {"left": "Let's meet at five", "right": "o'clock at my house.", "right_audio_tts": "o'clock at my house."}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6),
('<lesson_id>', 'text', replace($blk${"html": "<p>Ты такой молодец! Давай ещё немного потренируемся! Расставь слова в предложениях в правильном порядке!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 7),
('<lesson_id>', 'order', replace($blk${"words": ["Are", "you", "busy", "next", "Thursday?"], "sentence": "Are you busy next Thursday?", "audio_tts": "Are you busy next Thursday?"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 8),
('<lesson_id>', 'order', replace($blk${"words": ["Would", "you", "like", "to", "come?"], "sentence": "Would you like to come?", "audio_tts": "Would you like to come?"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 9),
('<lesson_id>', 'order', replace($blk${"words": ["Where", "shall", "we", "meet?"], "sentence": "Where shall we meet?", "audio_tts": "Where shall we meet?"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 10),
('<lesson_id>', 'order', replace($blk${"words": ["I'd", "love", "to", "come."], "sentence": "I'd love to come.", "audio_tts": "I'd love to come."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 11),
('<lesson_id>', 'order', replace($blk${"words": ["What", "time", "does", "it", "start?"], "sentence": "What time does it start?", "audio_tts": "What time does it start?"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 12),
('<lesson_id>', 'text', replace($blk${"html": "<p>Молодец! Осталось ДОПОЛНИТЕЛЬНОЕ задание. Оно необязательное, но если ты его сделаешь, получишь дополнительный балл на уроке! У тебя обязательно получится! Так держать!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 13),
('<lesson_id>', 'task', replace($blk${"title": "Дополнительное задание: напиши свой диалог ✍️", "needs_review": true, "html": "<p>Посмотри внимательно на билеты и изучи информацию на них! Выбери один из билетов и напиши свой диалог-приглашение. Для примера ты можешь использовать диалог из предыдущих заданий!</p><p><img src=\"@@MEDIA@@gg2/u8/book_tickets.webp\" alt=\"Tickets\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 14),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отлично! 🏆</h3><p>Ты справился со всеми заданиями. Ты — большой молодец. Держи за это кубок победителя. Жду тебя на занятии!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 15)
returning sort_order, type;
