-- Go Getter 2 · Unit 2 · Homework 4
-- собрано tools/gg2_build.py --lesson u2_hw4
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 2', 2 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 2');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 4', 'homework', 60, false, 3
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 2'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 4');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 3
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 2' and l.title = 'Homework 4';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 2' and l.title = 'Homework 4';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>Рада снова видеть тебя в домашнем задании! Благодаря сегодняшним упражнениям ты сможешь смело ходить в кафе или ресторан и заказывать себе еду! 😱 Let's start!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'task', replace($blk${"title": "Где лучше поужинать?", "needs_review": true, "html": "<p>Прежде чем приступить к первому заданию, подумай, где лучше поужинать: дома или в кафе/ресторане. Что бы ты выбрал?</p><p>Впиши <b>restaurant/cafe</b>, если предпочитаешь есть в кафе или ресторане, или впиши <b>home</b>, если считаешь, что лучшее место, где можно поесть, — это твой дом.</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'text', replace($blk${"html": "<h3>В кафе ☕</h3><p>Давай вспомним все фразы, которые пригодятся нам в кафе. Смотри, это диалог между официантом и гостем. Давай его разыграем. Я буду официантом, а ты — моим почётным гостем. Включи запись, и ты услышишь слова официанта. Попробуй дополнить мой «монолог» ответами гостя. Я буду делать паузы, но если не будешь успевать — можешь поставить аудио на паузу, а затем включить. У нас получится отличный диалог.</p><p><img src=\"@@MEDIA@@gg2/u2/cafe_waiter.webp\" alt=\"café\" style=\"max-width:100%;max-height:320px\"></p><p><b>Waitress:</b> What would you like?<br><b>Guest:</b> I'd like a ham sandwich, please.<br><b>Waitress:</b> Anything else?<br><b>Guest:</b> Yes. Can I have some chips, please?<br><b>Waitress:</b> Would you like anything to drink?<br><b>Guest:</b> Can I have a lemonade, please?<br><b>Waitress:</b> Great, thanks.</p>", "audio": "", "audio_tts": "What would you like? ... Anything else? ... Would you like anything to drink? ... Great, thanks."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'speaking', replace($blk${"title": "Твоя очередь 🎤", "needs_review": true, "html": "<p>Молодец! Ещё раз посмотри на диалог выше. Теперь твоя очередь записывать! Нажми на микрофон и запиши свои реплики. Твои слова выделены жёлтым.</p><p>Waitress: What would you like?<br>Guest: <mark>I'd like a ham sandwich, please.</mark><br>Waitress: Anything else?<br>Guest: <mark>Yes. Can I have some chips, please?</mark><br>Waitress: Would you like anything to drink?<br>Guest: <mark>Can I have a lemonade, please?</mark><br>Waitress: Great, thanks.</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'sequence', replace($blk${"title": "Расставь реплики в правильном порядке, чтобы получился наш диалог", "items": [{"text": "What would you like?"}, {"text": "I'd like a ham sandwich, please."}, {"text": "Anything else?"}, {"text": "Yes. Can I have some chips, please?"}, {"text": "Would you like anything to drink?"}, {"text": "Can I have a lemonade, please?"}, {"text": "Great, thanks."}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'task', replace($blk${"title": "Дополнительное задание: свой диалог в кафе", "needs_review": true, "html": "<p>Ура! Ты справился со всеми обязательными упражнениями. Осталось последнее — дополнительное. Твоя задача — составить и записать диалог. Используй диалог из предыдущих упражнений как пример.</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Good job!</h3><p>Отлично, ты справился со всеми заданиями. Ты — большой молодец. Жду тебя на занятии!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6)
returning sort_order, type;
