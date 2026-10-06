-- Go Getter 2 · Unit 3 · Homework 4
-- собрано tools/gg2_build.py --lesson u3_hw4
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 3', 3 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 3');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 4', 'homework', 60, false, 3
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 3'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 4');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 3
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 3' and l.title = 'Homework 4';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 3' and l.title = 'Homework 4';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>Здесь тебя ждёт новая домашняя работа. Сегодня мы будем смотреть видео, разговаривать и делать разные упражнения. У тебя всё получится, как и всегда 😃 Давай приступим :)</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'text', replace($blk${"html": "<p>Начнём с видео!</p><ol><li>Сначала посмотри его и найди ответ на вопросы: <i>Where is Samantha? Where is Tony?</i></li><li>После этого выбери персонажа, который понравился тебе больше — Тони или Саманту. Включи видео ещё раз и повторяй за своим героем.</li></ol>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'video', replace($blk${"title": "Посмотри видео: Where is Samantha? Where is Tony?", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'match', replace($blk${"title": "Вот это круто! Теперь давай соединим вопросы с ответами. Если нужно что-то вспомнить — посмотри видео ещё раз", "pairs": [{"left": "What are you doing, Tony?", "right": "I'm reading my newspaper.", "right_audio_tts": "I'm reading my newspaper."}, {"left": "How about you, Samantha?", "right": "I'm shopping at the grocery store.", "right_audio_tts": "I'm shopping at the grocery store."}, {"left": "What is Poppy doing?", "right": "She's practising violin in her room.", "right_audio_tts": "She's practising violin in her room."}, {"left": "What is Philipp doing?", "right": "He's playing with Fluffy.", "right_audio_tts": "He's playing with Fluffy."}, {"left": "What is Junior doing?", "right": "He's watching TV and singing.", "right_audio_tts": "He's watching TV and singing."}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'text', replace($blk${"html": "<p>А теперь давай попробуем сыграть ситуацию, похожую на ту, что мы уже изучили. Представь, что ты Елена или Миша. Включи запись и в паузах зачитывай свои реплики (они выделены). Давай попробуем!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'text', replace($blk${"audio": "", "html": "<p><b>Elena/Misha: Hello?</b><br>Amy's Dad: Hi, it's Amy's dad. How are you doing?<br><b>Elena/Misha: Oh, hi! I'm good, thanks.</b><br>Amy's Dad: Good to hear. Amy's just upstairs. Amy, it's for you!<br><b>Elena/Misha: Thank you!</b><br>Amy: Hi! It's great to hear from you!<br><b>Elena/Misha: Hi Amy! What are you doing?</b><br>Amy: I'm watching TV. What about you?<br><b>Elena/Misha: I'm reading a book. I'm bored… Do you want to go to the park?</b><br>Amy: Sounds great! See you in fifteen minutes.<br><b>Elena/Misha: See you soon!</b></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'sequence', replace($blk${"title": "Супер! Расставь диалог между Нилом, миссис Грин и Викки в правильном порядке", "image": "@@MEDIA@@gg2/u3/phone_call.webp", "items": [{"text": "Hello Mrs Green. It's Neil here. Can I speak to Vicky?"}, {"text": "Yes, Neil. Hang on. Vicky, it's for you!"}, {"text": "Hi Vicky. What are you doing?"}, {"text": "I'm watching TV. What about you, Neil?"}, {"text": "Nothing. Do you want to go swimming at five, Vicky?"}, {"text": "Yes. Great idea. See you soon."}, {"text": "Bye! See you later."}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6),
('<lesson_id>', 'gaps', replace($blk${"title": "Вау! На картинке Джанет и миссис Ди, мама Билли. Прочитай их диалог и впиши пропущенные слова", "mode": "type", "text": "Janet: Hello. It's Janet __here__. Can I __speak__ to Billy, please?\nMrs Dee: __Hello|Hi__ Janet. __Just__ a minute. Billy, it's __for__ you.", "image": "@@MEDIA@@gg2/u3/book_janet_mrs_dee.webp"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 7),
('<lesson_id>', 'gaps', replace($blk${"title": "Молодец! С Джанет начал разговаривать Билли. Дочитай разговор и впиши пропущенные слова", "mode": "type", "text": "Janet: Hi Billy. __What__ are you doing at the moment?\nBilly: Nothing. What __about__ you?\nJanet: __I'm|I’m|I am__ bored. Do you want to go to the cinema?\nBilly: Great __idea__! See you in ten minutes.\nJanet: Bye. See you __later__.", "image": "@@MEDIA@@gg2/u3/book_billy_janet.webp"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 8),
('<lesson_id>', 'task', replace($blk${"title": "Напиши телефонный разговор", "needs_review": true, "html": "<p>А это дополнительное задание для самых стойких и терпеливых! Представь, что ты, твоя мама и твой друг разговариваете по телефону. Напиши диалог, используя примеры выше. У тебя получится!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 9),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/congrats_popper.webp\" alt=\"\" style=\"height:200px\"></p><h2>Уррррааа! 🌟</h2><p>Домашняя работа выполнена на отлично, всё благодаря твоим стараниям. Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 10)
returning sort_order, type;
