-- Super Minds 3 · Unit 5 · Under the sea · Homework 3
-- собрано tools/sm3_build.py --lesson u5_hw3
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 5 · Under the sea', 5
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 5 · Under the sea');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 5 · Under the sea';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет-привет! Давай скорее приступать к домашней работе!</h2><p>Сначала послушай песню, а потом дополни предложения.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'gaps', replace($blk${"title": "Послушай песню и дополни предложения", "mode": "drag", "audio": "", "text": "1. The octopus was sad.\n2. The __Crocorox__ was bad.\n3. The __turtle__ hid inside its shell.\n4. The __starfish__ were all very scared."}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'gaps', replace($blk${"title": "Прочитай и дополни предложения", "text": "1. Its face was pretty. No, it wasn’t. It was ugly.\n2. Its eyes were small. Yes, __they were__.\n3. Its teeth were short. No, __they weren’t__. They __were long__.\n4. Its face was square. Yes, __it was__.\n5. There were scales on its head. Yes, __there were__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'task', replace($blk${"title": "Нарисуй своё страшное морское животное", "needs_review": true, "html": "<p>Закончи стихотворение о нём, а потом напиши о других морских животных. Не забудь показать рисунок учителю :)</p><p><i>Its face …<br>Its eyes …<br>Its teeth …<br>The dolphins were …<br>The seals were …<br>…</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:180px\"></p><h3>Great job! Thank you!</h3><p>Увидимся на уроке :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4);
end
$mig$;
