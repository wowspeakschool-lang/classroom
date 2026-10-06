-- Go Getter 2 · Unit 2 · Food · Homework 5
-- собрано tools/gg2_build.py --lesson u2_hw5
-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник
insert into classroom_units (course_id, title, sort_order)
select c.id, 'Unit 2 · Food', 2 from classroom_courses c
where c.slug = 'gg2'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = 'Unit 2 · Food');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, 'Homework 5', 'homework', 60, false, 4
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 2 · Food'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = 'Homework 5');
update classroom_lessons l set kind = 'homework', pass_threshold = 60, sort_order = 4
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = 'gg2' and u.title = 'Unit 2 · Food' and l.title = 'Homework 5';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = 'gg2' and u.title = 'Unit 2 · Food' and l.title = 'Homework 5';

-- затем: delete блоков урока (CTE) и вставка:
-- кусок 1
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>Добро пожаловать в домашнее задание! Сегодня мы с тобой потренируем навык чтения. Поехали!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 0),
('<lesson_id>', 'text', replace($blk${"html": "<h3>Susie's favourite meals</h3><p>Это Сьюзи. Она из Великобритании, и она подготовила нам интересный рассказ о своих любимых блюдах. Как думаешь, о скольких блюдах она нам расскажет? 1? 3? 5? Давай прочитаем и узнаем.</p><p><img src=\"@@MEDIA@@gg2/u2/susie.webp\" alt=\"Susie\" style=\"max-width:100%;max-height:320px\"></p><p><b>English breakfast</b><br>This is a hot breakfast. My mum cooks it for me at the weekend. You can have different things for this breakfast, but I like some sausages, two eggs and a tomato.</p><p><b>Fish and chips</b><br>People usually order this meal from a restaurant. But my dad makes the best fish and chips in the world! There's always some fish in the fridge at my house because he cooks fish and chips for the whole family every Friday.</p><p><b>Chicken and rice</b><br>Is there any chicken on the menu at my house? No, there isn't. But there is some chicken and some rice at my aunt's house. She cooks this meal for me when I visit her. There's always a lot of food so she gives me some to take home!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 1),
('<lesson_id>', 'match', replace($blk${"title": "Внимательно прочитай текст и соедини блюдо с картинкой", "pairs": [{"left_image": "@@MEDIA@@gg2/u2/english_breakfast.webp", "right": "English breakfast", "right_audio_tts": "English breakfast"}, {"left_image": "@@MEDIA@@gg2/u2/fish_and_chips.webp", "right": "Fish and chips", "right_audio_tts": "Fish and chips"}, {"left_image": "@@MEDIA@@gg2/u2/chicken_rice.webp", "right": "Chicken and rice", "right_audio_tts": "Chicken and rice"}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 2),
('<lesson_id>', 'quiz', replace($blk${"questions": [{"q": "Is Susie from England?", "type": "single", "options": [{"text": "Yes, she is."}, {"text": "No, she isn't."}], "correct": [0]}, {"q": "Is an English breakfast cold?", "type": "single", "options": [{"text": "Yes, it is."}, {"text": "No, it isn't."}], "correct": [1]}, {"q": "Does Susie like sausages?", "type": "single", "options": [{"text": "Yes, she does."}, {"text": "No, she doesn't."}], "correct": [0]}, {"q": "Does Susie order fish and chips from a restaurant?", "type": "single", "options": [{"text": "Yes, she does."}, {"text": "No, she doesn't."}], "correct": [1]}, {"q": "Does Susie's mum cook fish and chips?", "type": "single", "options": [{"text": "No, she doesn't."}, {"text": "Yes, she does."}], "correct": [0]}, {"q": "Is there any chicken and rice at her aunt's house?", "type": "single", "options": [{"text": "No, there isn't."}, {"text": "Yes, there is."}], "correct": [1]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 3),
('<lesson_id>', 'sort', replace($blk${"title": "Перетащи утверждения к подходящему блюду. Если не помнишь — подсмотри в тексте", "groups": [{"name": "English breakfast", "items": [{"text": "There are some eggs in this meal."}, {"text": "Susie's mum cooks it at the weekend."}]}, {"name": "Fish and chips", "items": [{"text": "There isn't any meat in this meal."}, {"text": "A lot of people order this meal."}, {"text": "Susie's dad cooks it every week."}]}, {"name": "Chicken and rice", "items": [{"text": "Susie's aunt cooks it for Susie."}]}]}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 4),
('<lesson_id>', 'task', replace($blk${"title": "Ответь на вопросы о себе", "needs_review": true, "html": "<p>Ура, это последнее задание на сегодня! Письменно ответь на вопросы о себе:</p><ol><li>What's your favourite meal?</li><li>Who cooks it?</li><li>How often do you go to restaurants?</li><li>What do you usually have for breakfast?</li></ol>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 5),
('<lesson_id>', 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура, ты справился с домашним заданием!</h3><p>Ты — большой молодец и супер ученик! Увидимся на занятии. Bye!</p>"}$blk$, '@@MEDIA@@', 'https://classroom.wowteach.ru/media/')::jsonb, 6)
returning sort_order, type;
