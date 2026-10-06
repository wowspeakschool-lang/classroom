-- Go Getter 1 · Unit 2 · My things · Homework 4
-- собрано tools/gg1_build.py --lesson u2_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 2 · My things', 2
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 2 · My things');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 2 · My things';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>На занятии мы много говорили о нас самих, учились задавать вопросы и отвечать на них. Закрепим?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u2/card_personal_info.webp\" alt=\"Personal information\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'gaps', replace($blk${"title": "Девочка по имени Нэнси попала на телешоу! Во время разговора с ведущим возникли помехи, и некоторые фразы было не слышно. Восстанови их!", "mode": "drag", "image": "@@MEDIA@@gg1/u2/nancy_show.webp", "text": "Man: Hi. Welcome to the show. __What's your name?__\nNancy: My name's Nancy.\nMan: Where are you from?\nNancy: __London, England.__\nMan: __How old are you?__\nNancy: I'm eleven.\nMan: What's your favourite sport?\nNancy: __Swimming. I love it.__\nMan: Who's your favourite actor?\nNancy: __Asa Butterfield.__"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильное вопросительное слово", "questions": [{"q": "___ is your name?", "type": "single", "options": [{"text": "What"}, {"text": "Who"}], "correct": [0]}, {"q": "___ are you from?", "type": "single", "options": [{"text": "What"}, {"text": "Where"}], "correct": [1]}, {"q": "___ old are you?", "type": "single", "options": [{"text": "How"}, {"text": "Where"}], "correct": [0]}, {"q": "___ is your favourite sports person?", "type": "single", "options": [{"text": "Where"}, {"text": "Who"}], "correct": [1]}, {"q": "___ is your favourite film?", "type": "single", "options": [{"text": "What"}, {"text": "Who"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'match', replace($blk${"title": "Соедини вопросы из предыдущего задания с ответами", "pairs": [{"left": "What is your name?", "right": "I'm Danny."}, {"left": "Where are you from?", "right": "Manchester, England."}, {"left": "How old are you?", "right": "Ten."}, {"left": "Who is your favourite sports person?", "right": "Renato Sanches. He's from Portugal."}, {"left": "What is your favourite film?", "right": "The Incredibles."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><b>В школе появилась новая ученица — Эмма. Прочитай статью о ней.</b></p><p><img src=\"@@MEDIA@@gg1/u2/emma_new_girl.webp\" alt=\"Emma\" style=\"height:220px\"></p><p><b>Welcome, Emma!</b> <i>by Ben Carter</i></p><p><i>Emma is new to our school. She's ten, and she's from Cardiff, Wales. Her favourite sport is tennis, and her favourite book is The Hobbit. Her favourite singer is Alicia Keys. Welcome to our school, Emma!</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'gaps', replace($blk${"title": "Какие вопросы задавали Эмме, чтобы написать эту статью? Допиши их", "mode": "type", "text": "1. How old are you?\n2. Where __are you from__?\n3. What __is your favourite sport|'s your favourite sport__?\n4. What __is your favourite book|'s your favourite book__?\n5. Who __is your favourite singer|'s your favourite singer__?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'task', replace($blk${"title": "Задание со звёздочкой ⭐", "needs_review": true, "html": "<p>Если ты его выполнишь, станешь настоящим мастером английского языка! Ответь на вопросы из предыдущего задания:</p><ol><li>How old are you?</li><li>Where are you from?</li><li>What is your favourite sport?</li><li>What is your favourite book?</li><li>Who is your favourite singer?</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:180px\"></p><h3>У тебя отлично получилось! 🎉</h3><p>Увидимся на занятии! Bye!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
