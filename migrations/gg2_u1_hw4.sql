-- Go Getter 2 · Unit 1 · Homework 4
-- собрано tools/gg2_build.py --lesson u1_hw4
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 1', 1 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 1');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 4', 'homework', 60, false, 3
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 1'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 4');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 3
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 1' and l.title = 'Homework 4';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 1' and l.title = 'Homework 4';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание! 👋</h2><p>Сегодня мы с тобой научимся узнавать и рассказывать личную информацию. Let's start!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'text', replace($blk${"html": "<p>Начнём с видеоинтервью. Но сначала представь, что ты стал журналистом. У кого из знаменитостей ты бы хотел взять интервью? Посмотри видео ниже и выполни задания к нему.</p><p><img src=\"@@MEDIA@@gg2/u1/interview.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'video', replace($blk${"title": "Видеоинтервью: Molly Greenberg", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'match', replace($blk${"title": "Посмотри видео и соедини вопросы с ответами", "pairs": [{"left": "What's your name?", "right": "My name is Molly.", "right_audio_tts": "My name is Molly."}, {"left": "What's your last name?", "right": "My last name is Greenberg.", "right_audio_tts": "My last name is Greenberg."}, {"left": "How do you spell it?", "right": "G-R-E-E-N-B-E-R-G.", "right_audio_tts": "G, R, E, E, N, B, E, R, G."}, {"left": "Where are you from?", "right": "I'm from New York City.", "right_audio_tts": "I'm from New York City."}, {"left": "What do you do?", "right": "I'm a teacher.", "right_audio_tts": "I'm a teacher."}, {"left": "What's your phone number?", "right": "It's 2032548652.", "right_audio_tts": "It's 2 0 3 2 5 4 8 6 5 2."}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'gaps', replace($blk${"title": "Прочитай диалог и перетащи слова в пропуски", "mode": "drag", "image": "@@MEDIA@@gg2/u1/karen_chess_club.webp", "text": "Karen: Good morning.\nMr Tims: Good morning.\nKaren: I'd like to join the chess club, please.\nMr Tims: OK. What's your __name__?\nKaren: My name is Karen Browne.\nMr Tims: How do you __spell__ that?\nKaren: K-A-R-E-N B-R-O-W-N-E.\nMr Tims: Thanks. Where do you __live__?\nKaren: 23 Green Street, Kingston.\nMr Tims: What's your __e-mail address__?\nKaren: It's k.browne@mymail.com.\nMr Tims: And what's your phone number?\nKaren: It's __08974942345__.\nMr Tims: Thanks.\nKaren: What time does the club __start__?\nMr Tims: At 4 p.m."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'gaps', replace($blk${"title": "Прочитай диалог ещё раз и впиши информацию о Карен", "mode": "type", "text": "Name: __Karen Browne|karen browne__\nAddress: __23 Green Street, Kingston|23 Green Street Kingston|23 green street, kingston|23 green street kingston__\nE-mail address: __k.browne@mymail.com|K.browne@mymail.com__\nPhone number: __08974942345__"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'quiz', replace($blk${"title": "В вопросах чего-то не хватает. Выбери правильный вариант", "questions": [{"q": "1. ___ your name?", "type": "single", "options": [{"text": "What's"}, {"text": "Who's"}], "correct": [0]}, {"q": "2. ___ do you spell that?", "type": "single", "options": [{"text": "Why"}, {"text": "How"}], "correct": [1]}, {"q": "3. ___ do you live?", "type": "single", "options": [{"text": "What's"}, {"text": "Where"}], "correct": [1]}, {"q": "4. ___ your e-mail address?", "type": "single", "options": [{"text": "Where's"}, {"text": "What's"}], "correct": [1]}, {"q": "5. ___ your phone number?", "type": "single", "options": [{"text": "What's"}, {"text": "Where's"}], "correct": [0]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6),
('<lesson_id>', 'task', replace($blk${"title": "Расскажи о себе ✍️", "needs_review": true, "html": "<p>Молодец! Осталось последнее задание. Письменно ответь о себе на вопросы:</p><ol><li>What's your name?</li><li>How do you spell that?</li><li>Where do you live?</li><li>What's your e-mail address?</li><li>What's your phone number?</li></ol><p><i>Можно придумать адрес и телефон — настоящие писать не обязательно.</i></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 7),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:200px\"></p><h3>Отлично! 🏆</h3><p>Ты справился со всеми заданиями — ты большой молодец. Держи за это кубок победителя. Жду тебя на занятии!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 8)
returning sort_order, type;
