-- Super Minds 3 · Unit 1 · School · Homework 4
-- собрано tools/sm3_build.py --lesson u1_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 1 · School', 1
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 1 · School');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 1 · School';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! Готов к новому домашнему заданию?</h2>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<h3>Давай повторим правило!</h3><p>Мы используем <b>have to</b>, когда говорим о правилах и о том, что мы <b>должны</b> делать.</p><div style=\"border-left:4px solid #2E9E4F;padding:8px 14px;margin:10px 0\"><p><i>Language focus</i></p><p>You <b>have to wear</b> a uniform.<br>You <b>have to climb</b> like me.<br>You <b>have to clean</b> your eyes like this.<br>You can’t? I see. Hehe!</p></div>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"title": "Соедини картинку с предложением", "pairs": [{"left_image": "@@MEDIA@@sm3/u1/haveto_be_on_time.webp", "right": "You have to arrive at school before nine o’clock.", "right_audio_tts": "You have to arrive at school before nine o'clock."}, {"left_image": "@@MEDIA@@sm3/u1/haveto_brush_teeth.webp", "right": "You have to brush your teeth after a meal.", "right_audio_tts": "You have to brush your teeth after a meal."}, {"left_image": "@@MEDIA@@sm3/u1/haveto_wash_hands.webp", "right": "You have to wash your hands before a meal.", "right_audio_tts": "You have to wash your hands before a meal."}, {"left_image": "@@MEDIA@@sm3/u1/haveto_wear_uniform.webp", "right": "You have to get dressed before you can go to school.", "right_audio_tts": "You have to get dressed before you can go to school."}, {"left_image": "@@MEDIA@@sm3/u1/haveto_clean_shoes.webp", "right": "You have to clean your shoes before you go and play.", "right_audio_tts": "You have to clean your shoes before you go and play."}, {"left_image": "@@MEDIA@@sm3/u1/haveto_do_homework.webp", "right": "You have to do your homework before you go and play.", "right_audio_tts": "You have to do your homework before you go and play."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'task', replace($blk${"title": "Write about you", "needs_review": true, "html": "<p>Напиши про себя. Используй <b>before</b>, <b>after</b>, <b>every day</b> или <b>every week</b>.</p><p><b>At school</b></p><ol><li>I have to …</li><li>I …</li><li>…</li></ol><p><b>At home</b></p><ol><li>I have to …</li><li>I …</li><li>…</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Super duper! Nice job!</h3>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4);
end
$mig$;
