-- Super Minds 3 · Unit 5 · Under the sea · Test
-- собрано tools/sm3_build.py --lesson u5_test
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
  select v_unit, 'Test', 'test',
         90, false, 8
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с картинками", "pairs": [{"left_image": "@@MEDIA@@sm3/u5/sea_dolphin.webp", "right": "dolphin", "right_audio_tts": "dolphin"}, {"left_image": "@@MEDIA@@sm3/u5/sea_seal.webp", "right": "seal", "right_audio_tts": "seal"}, {"left_image": "@@MEDIA@@sm3/u5/sea_turtle.webp", "right": "turtle", "right_audio_tts": "turtle"}, {"left_image": "@@MEDIA@@sm3/u5/sea_anchor.webp", "right": "anchor", "right_audio_tts": "anchor"}, {"left_image": "@@MEDIA@@sm3/u5/sea_starfish.webp", "right": "starfish", "right_audio_tts": "starfish"}, {"left_image": "@@MEDIA@@sm3/u5/sea_seahorse.webp", "right": "seahorse", "right_audio_tts": "seahorse"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "Millions of years ago ___ dinosaurs.", "type": "single", "options": [{"text": "there were"}, {"text": "there was"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: ___ you in the sea, Julia?", "type": "single", "options": [{"text": "Were"}, {"text": "Was"}], "correct": [0]}, {"q": "B: No, I ___.", "type": "single", "options": [{"text": "wasn’t"}, {"text": "was"}, {"text": "weren’t"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: Was Paul in the cinema? B: ___", "type": "single", "options": [{"text": "Yes, he was."}, {"text": "No, he was."}, {"text": "Yes, he wasn’t."}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: Where ___ you on Saturday, Lucas?", "type": "single", "options": [{"text": "were"}, {"text": "was"}], "correct": [0]}, {"q": "B: I ___ in the supermarket.", "type": "single", "options": [{"text": "was"}, {"text": "were"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "Lily and Ella ___ in the park,", "type": "single", "options": [{"text": "weren’t"}, {"text": "wasn’t"}], "correct": [0]}, {"q": "… they ___ in the sports centre.", "type": "single", "options": [{"text": "were"}, {"text": "was"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: ___ Charlotte in the swimming pool on Monday?", "type": "single", "options": [{"text": "Was"}, {"text": "Were"}], "correct": [0]}, {"q": "B: No, she ___.", "type": "single", "options": [{"text": "wasn’t"}, {"text": "was"}, {"text": "weren’t"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["Max", "was", "at", "the beach."], "sentence": "Max was at the beach.", "audio_tts": "Max was at the beach."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"words": ["There", "was", "a house", "behind", "the swimming pool."], "sentence": "There was a house behind the swimming pool.", "audio_tts": "There was a house behind the swimming pool."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"words": ["Was", "Mina", "in", "a boat?"], "sentence": "Was Mina in a boat?", "audio_tts": "Was Mina in a boat?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"words": ["Were", "there", "seahorses", "in", "the sea?"], "sentence": "Were there seahorses in the sea?", "audio_tts": "Were there seahorses in the sea?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'order', replace($blk${"words": ["Where", "were", "you", "at", "6 o’clock", "yesterday?"], "sentence": "Where were you at 6 o’clock yesterday?", "audio_tts": "Where were you at 6 o'clock yesterday?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "needs_review": true, "html": "<p>Ответь на вопросы:</p><p>1. Where were you yesterday?<br>2. Where was your mum 2 hours ago?<br>3. Where were you two days ago?<br>4. Where was your friend last Sunday?<br>5. Where were you last summer?</p><p>Запиши свой ответ, нажав на кнопку микрофона.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12);
end
$mig$;
