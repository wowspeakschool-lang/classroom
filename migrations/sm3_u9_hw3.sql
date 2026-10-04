-- Super Minds 3 · Unit 9 · Weather · Homework 3
-- собрано tools/sm3_build.py --lesson u9_hw3
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 9 · Weather', 9
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 9 · Weather');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 9 · Weather';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! Давай начинать домашнюю работу :)</h2><p>Послушай песню и исправь предложения.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'task', replace($blk${"title": "Послушай песню и исправь предложения", "needs_review": true, "audio": "", "html": "<p>1. I’m going to read my Science book.<br>2. I’m not going to travel far away.<br>3. I’m going to walk in the rain.<br>4. We aren’t going to go back to school.<br>5. We’re going to see our friends before our holiday.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'task', replace($blk${"title": "Напиши свой припев", "needs_review": true, "html": "<p>Можешь использовать идеи из песни :)</p><p><i>I’m going to …<br>And …<br>Then I’m going to …<br>I’m going to have lots of fun.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа!</h3><p>Самое время отдохнуть :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3);
end
$mig$;
