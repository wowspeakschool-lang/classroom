-- Super Minds 3 · Unit 4 · In the town · Homework 6
-- собрано tools/sm3_build.py --lesson u4_hw6
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 4 · In the town', 4
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 4 · In the town');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 4 · In the town';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>ПРИВЕТ-ПРИВЕТ!</h2><p>Сегодня мы с тобой будем читать. Какая твоя любимая книга?</p><p>Прочти диалог с начала до конца и выбери наиболее подходящий вариант ответа.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u4/dialog_paul_daisy_1.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u4/dialog_paul_daisy_2.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"words": ["Let’s", "look", "at", "the", "map."], "sentence": "Let’s look at the map.", "audio_tts": "Let's look at the map."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"words": ["Can", "you", "see", "the", "museum?"], "sentence": "Can you see the museum?", "audio_tts": "Can you see the museum?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["Where", "are", "we", "going", "now?"], "sentence": "Where are we going now?", "audio_tts": "Where are we going now?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["We’re", "going", "on", "Sunday."], "sentence": "We’re going on Sunday.", "audio_tts": "We're going on Sunday."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["Let’s", "go", "to", "the", "funfair."], "sentence": "Let’s go to the funfair.", "audio_tts": "Let's go to the funfair."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"words": ["There’s", "a", "park", "opposite", "the", "market", "square."], "sentence": "There’s a park opposite the market square.", "audio_tts": "There's a park opposite the market square."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'task', replace($blk${"title": "Напиши свои два диалога", "needs_review": true, "html": "<p>SUPER! Давай ещё потренируемся. Прочитай диалоги ещё раз, выбери два из них и напиши свои варианты по этому образцу.</p><p><i>Например:<br>Anya: Can you see the museum?<br>Masha: Yes, it’s near the market square.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>SUPER! Ты выполнил все задания!</h3><p>Ты БОЛЬШОЙ МОЛОДЕЦ! Увидимся на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
