-- Super Minds 3 · Unit 7 · At the doctor’s · Homework 3
-- собрано tools/sm3_build.py --lesson u7_hw3
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 7 · At the doctor’s', 7
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 7 · At the doctor’s');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 7 · At the doctor’s';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет-привет! Как твои дела?</h2><p>Начнём домашнее задание :) Послушай песню и впиши слова.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'gaps', replace($blk${"title": "Послушай песню и впиши пропущенные слова", "mode": "drag", "audio": "", "text": "The girl was in the kitchen.\nThere __was__ a big apple cake in the kitchen, too.\nShe __swallowed__ the big cake and then __got__ a stomach-ache.\nShe __was__ at a farm and __looked up__ at a snake.\nThen she __walked__ into a tree.\nAt the market a box of apples __landed__ on her knee.\nIt was a bad day."}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'task', replace($blk${"title": "Представь, что у тебя был плохой день", "needs_review": true, "html": "<p>Напиши, где ты был и что случилось.</p><p><i>I was at the …</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'task', replace($blk${"title": "Заверши эту песню и нарисуй к ней картинку", "needs_review": true, "html": "<p>Используй свои идеи из прошлого задания.</p><p><i>I was at the …,<br>I looked — there were …<br>I …<br>And now it really aches.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа!</h3><p>Спасибо за твои труды :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4);
end
$mig$;
