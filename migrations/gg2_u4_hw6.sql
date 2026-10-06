-- Go Getter 2 · Unit 4 · Our world · Homework 6
-- собрано tools/gg2_build.py --lesson u4_hw6
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 4 · Our world', 4 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 4 · Our world');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 6', 'homework', 60, false, 5
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 4 · Our world'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 6');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 5
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 4 · Our world' and l.title = 'Homework 6';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 4 · Our world' and l.title = 'Homework 6';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Огромный привет!</h2><p>Как твоё настроение? Как погода? Самое время сделать новое домашнее задание. Сегодня ты будешь много слушать и кое-что напишешь. Давай начнём 😉</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'text', replace($blk${"html": "<p>Для начала послушай аудио. Во время прослушивания представляй друзей, которых описывают ребята.</p>", "audio": ""}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'match', replace($blk${"title": "Послушай аудио ещё раз и соедини друзей.", "pairs": [{"left": "Lenny", "right": "Zach", "right_audio_tts": "Zach"}, {"left": "Bella", "right": "Fiona", "right_audio_tts": "Fiona"}, {"left": "Fred", "right": "Dave", "right_audio_tts": "Dave"}, {"left": "Diana", "right": "Mary", "right_audio_tts": "Mary"}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'gaps', replace($blk${"title": "Прочитай предложения и вставь пропущенные слова. Если трудно — послушай аудио ещё раз.", "mode": "drag", "text": "1. Zach is __older__ than Lenny.\n2. Lenny thinks that Zach is __funny__.\n3. Fiona is __smaller__ than Bella.\n4. Fiona is the most __beautiful__ animal.\n5. Dave is the __fastest__ runner in the family.\n6. Dave is the __best__ friend in the world.\n7. Mary is the most __intelligent__ girl in the class.\n8. Diana thinks that Mary is a __good__ teacher."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'text', replace($blk${"html": "<p>Следующее задание — посмотри видео и узнай, что такое абзац (paragraph).</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'video', replace($blk${"title": "Посмотри видео: что такое абзац (paragraph)", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'quiz', replace($blk${"questions": [{"q": "What is a paragraph?", "type": "single", "options": [{"text": "It’s a book about school."}, {"text": "It’s a big text."}, {"text": "It’s a group of sentences."}], "correct": [2]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6),
('<lesson_id>', 'sequence', replace($blk${"title": "Прочитай текст Ленни о его лучшем друге Заке и расставь абзацы по порядку.", "image": "@@MEDIA@@gg2/u4/zak_lenny.webp", "items": [{"text": "My best friend is called Zach. He’s a lot of fun. We spend a lot of time together. In some ways we are similar, but in other ways we are different."}, {"text": "We both like cycling. We go cycling in the mountains. We both like playing football, but Zach is faster than I am! We also like playing basketball."}, {"text": "But we are also different. I am 12, but Zach is 15. Zach likes pizza, but I like hamburgers. Zach is a worse Maths student, but he’s a better Art student. He’s a great friend."}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 7),
('<lesson_id>', 'gaps', replace($blk${"title": "Отличная работа 👍 Впиши пропущенные слова в табличку о Ленни и Заке.", "mode": "type", "text": "SIMILAR: We both like cycling, __playing football|football|playing basketball|basketball__ and __playing basketball|basketball|playing football|football__.\nDIFFERENT:\nAge — Lenny: __12|twelve__ · Zach: __15|fifteen__\nFood — Lenny: __hamburgers|hamburger__ · Zach: __pizza__\nGood at — Lenny: __Maths|maths|Math|math__ · Zach: __Art|art__"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 8),
('<lesson_id>', 'task', replace($blk${"title": "Опиши Ленни от лица Зака", "needs_review": true, "html": "<p>Великолепно! Сейчас тебя ждёт непростое, но очень интересное задание. Напиши описание Ленни от лица Зака. Используй то, что ты уже знаешь о Ленни.</p><p><i>Можешь начать так: My best friend is called …</i></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 9),
('<lesson_id>', 'text', replace($blk${"html": "<p>Вот это да! Какой отличный рассказ у тебя получился.</p><p><b>Это задание дополнительное</b>, но если ты его сделаешь, будет очень круто! Нарисуй Зака и Ленни такими, какими ты их представляешь. Не забудь показать рисунок учителю :)</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 10),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_jump.webp\" alt=\"\" style=\"height:180px\"></p><h3>Bye-bye! 👋</h3><p>Ты отлично поработал. До встречи на занятии!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 11)
returning sort_order, type;
