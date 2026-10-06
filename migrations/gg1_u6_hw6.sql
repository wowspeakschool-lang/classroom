-- Go Getter 1 · Unit 6 · My day · Homework 6
-- собрано tools/gg1_build.py --lesson u6_hw6
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 6 · My day', 6
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 6 · My day');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 6 · My day';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Как ты помнишь, на уроке мы слушали рассказы ребят о том, как они проводят выходные. Сегодня ты тоже будешь слушать и выполнять задания, но уже самостоятельно!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>Послушай рассказ Энди о его каникулах. Потом выполни два задания ниже.</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни таблицу. В каждом пропуске — только ОДНО слово", "mode": "type", "text": "Country: __Italy__\nAunt's nationality: __British__\nAunt's job: __teacher|Teacher__\nFavourite place: __beach|Beach__\nFavourite game: __catch|Catch__"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Послушай рассказ Энди ещё раз и выбери правильный ответ. Сначала внимательно прочитай предложения", "questions": [{"q": "Andy ___ goes on holiday in August.", "type": "single", "options": [{"text": "usually"}, {"text": "always"}], "correct": [1]}, {"q": "After breakfast they ___ go to the beach.", "type": "single", "options": [{"text": "usually"}, {"text": "often"}], "correct": [0]}, {"q": "They ___ have a picnic on the beach.", "type": "single", "options": [{"text": "always"}, {"text": "often"}], "correct": [1]}, {"q": "They ___ go to bed after lunch.", "type": "single", "options": [{"text": "often"}, {"text": "usually"}], "correct": [0]}, {"q": "He ___ gets up early.", "type": "single", "options": [{"text": "never"}, {"text": "always"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><b>Прочитай небольшой текст о том, как Джен обычно проводит выходные. Подумай, похоже ли ваше времяпрепровождение?</b></p><p><img src=\"@@MEDIA@@gg1/u6/jen.webp\" alt=\"Jen\" style=\"height:200px\"></p><p><b>My weekend</b></p><p><i>I usually get up at 8 o'clock on Saturdays. After breakfast I skateboard with my friends. I love my skateboard and I love Saturdays! Before dinner I watch TV or play computer games. I get up at 9 o'clock on Sundays. Before lunch I tidy my room and I do my homework. I always have lunch with my family! After lunch I often draw or listen to music.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><b>Правило: before (до) и after (после)</b></p><p><img src=\"@@MEDIA@@gg1/u6/before_after.webp\" alt=\"before, after\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'task', replace($blk${"title": "Мои выходные ✍️", "needs_review": true, "html": "<p><img src=\"@@MEDIA@@gg1/u6/cat_sunglasses.webp\" alt=\"Cat\" style=\"height:180px\"></p><p>Напиши небольшой рассказ о себе по примеру рассказа Джен. Чтобы сделать его интереснее, используй <b>after</b> (после) и <b>before</b> (до) — правило выше. Котик желает тебе удачи! 😉</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7);
end
$mig$;
