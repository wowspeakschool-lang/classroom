-- Go Getter 1 · Unit 4 · Look at me · Homework 5
-- собрано tools/gg1_build.py --lesson u4_hw5
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 4 · Look at me', 4
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 4 · Look at me');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 4 · Look at me';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Welcome to the HOMEWORK world! 👋</h2><p>Добро пожаловать в мир домашнего задания! Сегодня мы будем читать и выполнять интересные задания по тексту!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'flashcards', replace($blk${"cards": [{"text": "clever", "translation": "умный", "audio_tts": "clever", "image": "@@MEDIA@@gg1/u4/pers_clever.webp"}, {"text": "friendly", "translation": "дружелюбный", "audio_tts": "friendly", "image": "@@MEDIA@@gg1/u4/pers_friendly.webp"}, {"text": "funny", "translation": "смешной, весёлый", "audio_tts": "funny", "image": "@@MEDIA@@gg1/u4/pers_funny.webp"}, {"text": "helpful", "translation": "отзывчивый", "audio_tts": "helpful", "image": "@@MEDIA@@gg1/u4/pers_helpful.webp"}, {"text": "sporty", "translation": "спортивный", "audio_tts": "sporty", "image": "@@MEDIA@@gg1/u4/pers_sporty.webp"}, {"text": "nice", "translation": "приятный, добрый", "audio_tts": "nice", "image": "@@MEDIA@@gg1/u4/pers_nice.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u4/card_personality.webp\" alt=\"Personality adjectives\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши пропущенные слова", "mode": "drag", "text": "1. Max is very __clever__. He always reads books and gets good marks at school.\n2. Maria has got a lot of friends. She is __friendly__.\n3. Antonio always makes me laugh. He is very __funny__.\n4. Dan is usually __helpful__. He helps me with homework.\n5. My family is __sporty__. We regularly play tennis and go to the gym."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><b>Давай прочитаем текст про Тима и выполним задания!</b></p><p><i>Hi. My name's Tim. I'm eleven and I'm from London. I've got two brothers, three sisters and … ten cousins! My favourite hobby is reading and I've got a lot of books on my desk. I've got a bike and a skateboard, but I'm not very sporty. My best friend is good at football. His name is Max and he's very nice. Max is my neighbour too. Our favourite place is his garden. We've got a little house in a tree! Max has got a sister. Her name is Lucy and she's very clever. Max and I are not very good at Maths, but she is very helpful! I like Lucy!</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'truefalse', replace($blk${"title": "Прочитай текст ещё раз и выбери: верно или неверно", "statements": [{"text": "Tim is twenty years old.", "correct": false}, {"text": "There are seven children in his family.", "correct": false}, {"text": "He's got lots of books on his desk.", "correct": true}, {"text": "Tim is really sporty.", "correct": false}, {"text": "Max is good at football.", "correct": true}, {"text": "Max lives far away from Tim.", "correct": false}, {"text": "Lucy is very helpful.", "correct": true}, {"text": "Max and Tim have got a big house in a tree.", "correct": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски нужными словами", "mode": "drag", "text": "1. Tim's hobby is __reading__.\n2. I've got a bike and a __skateboard__.\n3. My best __friend__ is good at football.\n4. Our favourite place is his __garden__.\n5. Max and Tim are not very good at __Maths__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'task', replace($blk${"title": "Мой характер ✍️", "needs_review": true, "html": "<p>А теперь напиши о своём характере и о характере своего лучшего друга.</p><p><i>Пример: I'm friendly and helpful. I'm sporty too. My best friend is funny and clever. We're nice people!</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:180px\"></p><h3>Спасибо тебе за твои ответы! 🎉</h3><p>See you soon! До скорой встречи!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
