-- Super Minds 3 · Unit 8 · Countries · Homework 3
-- собрано tools/sm3_build.py --lesson u8_hw3
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 8 · Countries', 8
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 8 · Countries');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 8 · Countries';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет-привет! Как здорово, что ты решил сделать домашнюю работу!</h2><p>Послушай песню и выбери правильный вариант ответа.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Послушай песню и выбери правильный вариант", "audio": "", "questions": [{"q": "1. I went to ___ but I didn’t see the wall.", "type": "single", "options": [{"text": "China"}, {"text": "India"}], "correct": [0]}, {"q": "2. In India I didn’t see the ___.", "type": "single", "options": [{"text": "Taj Mahal"}, {"text": "Sphinx"}], "correct": [0]}, {"q": "3. I went to Egypt but I didn’t see the ___.", "type": "single", "options": [{"text": "Sphinx"}, {"text": "lynx"}], "correct": [0]}, {"q": "4. I went to ___ but I didn’t see the sun.", "type": "single", "options": [{"text": "Australia"}, {"text": "Brazil"}], "correct": [0]}, {"q": "5. In Brazil I didn’t see the ___.", "type": "single", "options": [{"text": "Amazon"}, {"text": "wall"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'task', replace($blk${"title": "Заверши песню", "needs_review": true, "html": "<p>Подумай о четырёх местах и интересных фактах о них. Что ты видел? Чего не видел?</p><p><i>I went to …<br>But I didn’t see …<br>In …<br>I didn’t see …<br>I went to …<br>And I saw …<br>I went to …<br>And I saw …</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'task', replace($blk${"title": "А теперь время рисования!", "needs_review": true, "html": "<p>Нарисуй то место, в котором ты побывал, и не забудь показать рисунок учителю :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Классная работа!</h3><p>Спасибо тебе большое :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4);
end
$mig$;
