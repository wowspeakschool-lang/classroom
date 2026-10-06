-- Go Getter 2 · Unit 7 · Travel · Homework 4
-- собрано tools/gg2_build.py --lesson u7_hw4
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 7 · Travel', 7 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 7 · Travel');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 4', 'homework', 60, false, 3
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 7 · Travel'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 4');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 3
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 7 · Travel' and l.title = 'Homework 4';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 7 · Travel' and l.title = 'Homework 4';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>Готов выполнять домашнее задание? Тебя ждёт интересное видео! В конце есть дополнительное упражнение — его можно выполнить по желанию, НО если выполнишь, будешь нереально крут!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'text', replace($blk${"html": "<p>Сегодня мы отправимся в путешествие! Но сначала представь, что тебе нужно купить билет на поезд. Как спросить по-английски, сколько стоит билет? Посмотри видео и выполни задания к нему.</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'video', replace($blk${"title": "Посмотри видео: покупаем билет на поезд 🎫", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'match', replace($blk${"title": "Соедини вопросы с ответами", "pairs": [{"left": "How can I help you?", "right": "I would like to buy a train ticket to California.", "right_audio_tts": "I would like to buy a train ticket to California."}, {"left": "How much is it?", "right": "It costs 40 dollars.", "right_audio_tts": "It costs 40 dollars."}, {"left": "Which platform is the train on?", "right": "Platform Number 2.", "right_audio_tts": "Platform Number 2."}, {"left": "When does it leave?", "right": "It leaves at 6:30 pm.", "right_audio_tts": "It leaves at 6:30 pm."}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'gaps', replace($blk${"title": "Прочитай диалог и перетащи реплики продавщицы в пропуски", "mode": "drag", "text": "Boy: I'd like two tickets to York, please.\nWoman: __Here you are.__\nBoy: How much is it?\nWoman: __It is ten pounds, please.__\nBoy: What time does the train leave?\nWoman: __At 10:30 a.m.__\nBoy: What time does it arrive?\nWoman: __At 11:45 a.m.__"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'text', replace($blk${"html": "<h3>LOOK! Prices 💷</h3><p>Молодец! Теперь узнаем, как по-английски говорят о деньгах. Внимательно посмотри правило!</p><p>£10.50 = <b>ten pounds fifty</b><br>£7.25 = <b>seven pounds twenty-five</b><br>£0.50 = <b>fifty pence</b></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'match', replace($blk${"title": "А теперь соедини цифры со словами", "pairs": [{"left": "£2.50", "right": "two pounds fifty", "right_audio_tts": "two pounds fifty"}, {"left": "£0.75", "right": "seventy-five pence", "right_audio_tts": "seventy-five pence"}, {"left": "£30.40", "right": "thirty pounds forty", "right_audio_tts": "thirty pounds forty"}, {"left": "£22.60", "right": "twenty-two pounds sixty", "right_audio_tts": "twenty-two pounds sixty"}, {"left": "£0.30", "right": "thirty pence", "right_audio_tts": "thirty pence"}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6),
('<lesson_id>', 'text', replace($blk${"html": "<h3>Билет до Оксфорда 🚆</h3><p>Так держать! А теперь чтение. Внимательно прочитай диалог.</p><p><b>A:</b> What time does the next train from London to Oxford leave?<br><b>B:</b> At quarter past one.<br><b>A:</b> I'd like one ticket, please.<br><b>B:</b> Here you are.<br><b>A:</b> How much is it?<br><b>B:</b> It's twelve pounds fifty, please.<br><b>A:</b> What time does it arrive in Oxford?<br><b>B:</b> At half past three.</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 7),
('<lesson_id>', 'gaps', replace($blk${"title": "Прочитай диалог ещё раз и заполни билет (время пиши цифрами, например 2:45)", "mode": "type", "image": "@@MEDIA@@gg2/u7/book_ticket.webp", "text": "From: London\nTo: __Oxford__\nPrice: £__12.50|12,50|12.5__\nLeave: __1:15|01:15|13:15|1.15__\nArrive: __3:30|03:30|15:30|3.30__"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 8),
('<lesson_id>', 'text', replace($blk${"html": "<p>Молодец! Осталось последнее задание. Подумай: в какую страну ты хотел бы сейчас уехать? Напиши данные своего билета, как в предыдущем упражнении.</p><p><i>Например: Train ticket: From: Russia To: London Price: £50 Leave: 2:50 Arrive: 8:30</i></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 9),
('<lesson_id>', 'task', replace($blk${"title": "Мой билет ✍️", "html": "<p>Посмотри на пример ещё раз и напиши данные своего билета: From, To, Price, Leave, Arrive.</p>", "needs_review": true}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 10),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:200px\"></p><h2>Отлично! 🏆</h2><p>Ты справился со всеми заданиями. Ты — большой молодец! Жду тебя на занятии!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 11)
returning sort_order, type;
