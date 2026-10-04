-- Super Minds 3 · Unit 5 · Under the sea · Homework 6
-- собрано tools/sm3_build.py --lesson u5_hw6
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
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<h3>Read the story:</h3><p><img src=\"@@MEDIA@@sm3/u5/story_dolphins_1.webp\" alt=\"\" style=\"max-width:100%\"></p><p><img src=\"@@MEDIA@@sm3/u5/story_dolphins_2.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'task', replace($blk${"title": "Read the story again and answer the questions", "needs_review": true, "html": "<p>1. Who are they? <i>— Kylie Morgan and her dad</i><br>2. Where are they?<br>3. What does Kylie see?<br>4. What dangerous animal does Kylie’s dad see?<br>5. How many teeth does it have?<br>6. Why do the dolphins swim around Kylie?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'truefalse', replace($blk${"title": "Read the story and choose: True or False", "statements": [{"text": "The dolphins hit their tails on the water to scare the sharks.", "answer": true}, {"text": "The dolphins get close to Kylie to protect her.", "answer": true}, {"text": "The white shark plays with the dolphins.", "answer": false}, {"text": "Sharks aren’t dangerous animals.", "answer": false}, {"text": "The dolphins save Kylie from the shark.", "answer": true}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Great job!</h3><p>Увидимся на уроке :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3);
end
$mig$;
