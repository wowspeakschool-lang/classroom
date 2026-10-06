-- Go Getter 2 · Unit 6 · Homework 3
-- собрано tools/gg2_build.py --lesson u6_hw3
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 6', 6 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 6');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 3', 'homework', 60, false, 2
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 6'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 3');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 2
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 6' and l.title = 'Homework 3';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 6' and l.title = 'Homework 3';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Огромный привет! 😉</h2><p>В этой домашней работе мы повторим всё то, что ты прошёл на уроке с учителем. Это поможет тебе не только всё запомнить, но и использовать :)) Давай начинать!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'text', replace($blk${"html": "<h3>Неправильные глаголы</h3><p>Давай повторим неправильные глаголы! Помни: у них совсем другая форма в прошедшем времени.</p><ul><li>come – <b>came</b></li><li>drink – <b>drank</b></li><li>eat – <b>ate</b></li><li>feel – <b>felt</b></li><li>go – <b>went</b></li><li>have – <b>had</b></li><li>make – <b>made</b></li><li>meet – <b>met</b></li><li>take – <b>took</b></li></ul>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'video', replace($blk${"title": "Посмотри видео, а потом сделай задание ниже.", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'sequence', replace($blk${"title": "Посмотри видео ещё раз и расставь предложения по порядку", "items": [{"text": "Yesterday I went to school."}, {"text": "Hammy came too."}, {"text": "Hammy drank something!"}, {"text": "Hammy ate my Maths book!"}, {"text": "Later we had a cookery class."}, {"text": "We made chocolate cakes."}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'gaps', replace($blk${"title": "Здорово! Давай ещё немного потренируемся! Впиши глагол в прошедшем времени", "mode": "type", "text": "1. We __had__ (have) lunch at 2 o'clock yesterday.\n2. I __made__ (make) a pizza last Sunday.\n3. We __went__ (go) to the cinema last month.\n4. You __took__ (take) a photo of me two minutes ago.\n5. They __drank__ (drink) tea after the meal yesterday evening.\n6. I __ate__ (eat) a sandwich for lunch an hour ago.\n7. We first __met__ (meet) three years ago.\n8. Everyone __came__ (come) to my party last Sunday."}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'match', replace($blk${"title": "Молодец! Ещё одно задание: соедини неправильные глаголы по парам", "pairs": [{"left": "have", "right": "had", "right_audio_tts": "had"}, {"left": "make", "right": "made", "right_audio_tts": "made"}, {"left": "feel", "right": "felt", "right_audio_tts": "felt"}, {"left": "take", "right": "took", "right_audio_tts": "took"}, {"left": "come", "right": "came", "right_audio_tts": "came"}, {"left": "drink", "right": "drank", "right_audio_tts": "drank"}, {"left": "meet", "right": "met", "right_audio_tts": "met"}, {"left": "go", "right": "went", "right_audio_tts": "went"}, {"left": "eat", "right": "ate", "right_audio_tts": "ate"}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'task', replace($blk${"title": "Задание для чемпионов! За него ты получишь дополнительный балл ;)", "needs_review": true, "html": "<p>Напиши 5 предложений о том, что ты делал на выходных.</p><p><i>For example: I walked with my dog on Saturday.</i></p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Спасибо тебе огромное! ⭐</h3><p>Ты так сегодня здорово потрудился. Твой учитель тобой гордится, и ты тоже можешь собой гордиться. До встречи на занятии!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 7)
returning sort_order, type;
