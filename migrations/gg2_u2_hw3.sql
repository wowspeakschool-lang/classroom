-- Go Getter 2 · Unit 2 · Food · Homework 3
-- собрано tools/gg2_build.py --lesson u2_hw3
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 2 · Food', 2 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 2 · Food');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 3', 'homework', 60, false, 2
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 2 · Food'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 3');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 2
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 2 · Food' and l.title = 'Homework 3';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 2 · Food' and l.title = 'Homework 3';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>В этом уроке мы научимся считать неисчисляемые продукты. Как это возможно? Давай начнём урок и узнаешь!</p><p>Выполни все задания, чтобы выучить слова! У тебя всё получится. Удачи! ❤️</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'flashcards', replace($blk${"cards": [{"text": "a bar of chocolate", "translation": "плитка шоколада", "audio_tts": "a bar of chocolate", "image": "@@MEDIA@@gg2/u2/bar_of_chocolate.webp"}, {"text": "a bottle of water", "translation": "бутылка воды", "audio_tts": "a bottle of water", "image": "@@MEDIA@@gg2/u2/bottle_of_water.webp"}, {"text": "a can of cola", "translation": "банка колы", "audio_tts": "a can of cola", "image": "@@MEDIA@@gg2/u2/can_of_cola.webp"}, {"text": "a carton of juice", "translation": "пачка сока", "audio_tts": "a carton of juice", "image": "@@MEDIA@@gg2/u2/carton_of_juice.webp"}, {"text": "a jar of jam", "translation": "баночка варенья", "audio_tts": "a jar of jam", "image": "@@MEDIA@@gg2/u2/jar_of_jam.webp"}, {"text": "a packet of biscuits", "translation": "пачка печенья", "audio_tts": "a packet of biscuits", "image": "@@MEDIA@@gg2/u2/packet_of_biscuits.webp"}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'match', replace($blk${"title": "Соедини картинку с выражением", "pairs": [{"left_image": "@@MEDIA@@gg2/u2/bar_of_chocolate.webp", "right": "a bar of chocolate", "right_audio_tts": "a bar of chocolate"}, {"left_image": "@@MEDIA@@gg2/u2/bottle_of_water.webp", "right": "a bottle of water", "right_audio_tts": "a bottle of water"}, {"left_image": "@@MEDIA@@gg2/u2/can_of_cola.webp", "right": "a can of cola", "right_audio_tts": "a can of cola"}, {"left_image": "@@MEDIA@@gg2/u2/carton_of_juice.webp", "right": "a carton of juice", "right_audio_tts": "a carton of juice"}, {"left_image": "@@MEDIA@@gg2/u2/jar_of_jam.webp", "right": "a jar of jam", "right_audio_tts": "a jar of jam"}, {"left_image": "@@MEDIA@@gg2/u2/packet_of_biscuits.webp", "right": "a packet of biscuits", "right_audio_tts": "a packet of biscuits"}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'gaps', replace($blk${"title": "Перетащи слова в пропуски", "mode": "drag", "text": "1. a __bar__ of chocolate\n2. a __bottle__ of water\n3. a __can__ of cola\n4. a __carton__ of juice\n5. a __jar__ of jam\n6. a __packet__ of biscuits"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'quiz', replace($blk${"questions": [{"q": "Как по-английски «плитка шоколада»?", "type": "single", "options": [{"text": "a bottle of water"}, {"text": "a bar of chocolate"}, {"text": "a packet of biscuits"}, {"text": "a can of cola"}], "correct": [1]}, {"q": "Как по-английски «бутылка воды»?", "type": "single", "options": [{"text": "a bar of chocolate"}, {"text": "a can of cola"}, {"text": "a carton of juice"}, {"text": "a bottle of water"}], "correct": [3]}, {"q": "Как по-английски «банка колы»?", "type": "single", "options": [{"text": "a bottle of water"}, {"text": "a jar of jam"}, {"text": "a carton of juice"}, {"text": "a can of cola"}], "correct": [3]}, {"q": "Как по-английски «пачка сока»?", "type": "single", "options": [{"text": "a packet of biscuits"}, {"text": "a can of cola"}, {"text": "a carton of juice"}, {"text": "a jar of jam"}], "correct": [2]}, {"q": "Как по-английски «баночка варенья»?", "type": "single", "options": [{"text": "a bar of chocolate"}, {"text": "a packet of biscuits"}, {"text": "a jar of jam"}, {"text": "a carton of juice"}], "correct": [2]}, {"q": "Как по-английски «пачка печенья»?", "type": "single", "options": [{"text": "a packet of biscuits"}, {"text": "a bar of chocolate"}, {"text": "a jar of jam"}, {"text": "a bottle of water"}], "correct": [0]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отлично!</h3><p>Теперь ты умеешь считать даже то, что посчитать нельзя! Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5)
returning sort_order, type;
