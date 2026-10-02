-- Super Minds 3 · Unit 2 · Food · Homework 7
-- собрано tools/sm3_build.py --lesson u2_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 2 · Food', 2
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 2 · Food');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 2 · Food';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'sequence', replace($blk${"title": "Расставь предложения в правильном порядке, чтобы получился диалог. Подсказка: начинаем с фразы «Hello. Can I help you?»", "items": [{"text": "A: Hello. Can I help you?", "audio_tts": "Hello. Can I help you?"}, {"text": "B: I’d like a pizza with cheese, mushrooms and onions, please.", "audio_tts": "I'd like a pizza with cheese, mushrooms and onions, please."}, {"text": "A: Sorry, we haven’t got any mushrooms.", "audio_tts": "Sorry, we haven't got any mushrooms."}, {"text": "B: No mushrooms? Have you got any peppers?", "audio_tts": "No mushrooms? Have you got any peppers?"}, {"text": "A: Let me see. Yes, we’ve got peppers.", "audio_tts": "Let me see. Yes, we've got peppers."}, {"text": "B: That’s great. Can I have some tomatoes, too?", "audio_tts": "That's great. Can I have some tomatoes, too?"}, {"text": "A: OK, so that’s pizza with cheese, onions, peppers and tomatoes.", "audio_tts": "OK, so that's pizza with cheese, onions, peppers and tomatoes."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'task', replace($blk${"title": "Посмотри на картинку и составь диалог", "needs_review": true, "html": "<p><img src=\"@@MEDIA@@sm3/u2/scene_canteen_order.webp\" alt=\"\" style=\"max-width:100%\"></p><p>Можешь использовать предыдущее задание как пример.</p><p><b>Assistant:</b> <i>Hello! Can I help you?</i><br><b>Boy:</b> …</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Это семья Джона. Прочитай рассказ о его ужине и заполни пропуски ⬇", "mode": "drag", "image": "@@MEDIA@@sm3/u2/scene_john_dinner.webp", "text": "My __favourite__ dinner is chicken, peas and __chips__. I have __dinner__ at 7 __o’clock__. I __don’t__ like fish and rice."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'speaking', replace($blk${"title": "Расскажи о своём ужине 🎤", "needs_review": true, "html": "<p>Нажми на микрофон и расскажи о своём ужине. Используй рассказ Джона как пример.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_jump.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты справился со всеми заданиями, так держать!</h3>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5);
end
$mig$;
