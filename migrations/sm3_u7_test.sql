-- Super Minds 3 · Unit 7 · At the doctor’s · Test
-- собрано tools/sm3_build.py --lesson u7_test
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
  select v_unit, 'Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'match', replace($blk${"title": "Прочитай и подбери слово", "pairs": [{"left": "At night I cough a lot.", "right": "cough", "right_audio_tts": "cough"}, {"left": "My head hurts and I want to lie down.", "right": "headache", "right_audio_tts": "headache"}, {"left": "This person gives you medicine when you are ill.", "right": "doctor", "right_audio_tts": "doctor"}, {"left": "I ate too much cake and now my tummy hurts.", "right": "stomachache", "right_audio_tts": "stomachache"}, {"left": "My ear hurts and I can’t hear well.", "right": "earache", "right_audio_tts": "earache"}, {"left": "This tooth hurts when I eat something sweet.", "right": "toothache", "right_audio_tts": "toothache"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "I ___ up and I felt very sick.", "type": "single", "options": [{"text": "woke"}, {"text": "wake"}, {"text": "waked"}], "correct": [0]}, {"q": "I woke up and I ___ very sick.", "type": "single", "options": [{"text": "felt"}, {"text": "feel"}, {"text": "feeled"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: What did you do after school? We ___ a volleyball game.", "type": "single", "options": [{"text": "watched"}, {"text": "watch"}, {"text": "watching"}], "correct": [0]}, {"q": "B: Oh! And we ___ football.", "type": "single", "options": [{"text": "played"}, {"text": "playing"}, {"text": "play"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "Sam and Dan ___ TV in the living room.", "type": "single", "options": [{"text": "watched"}, {"text": "listening"}, {"text": "play"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "You ___ a letter in the morning.", "type": "single", "options": [{"text": "wrote"}, {"text": "write"}, {"text": "writing"}], "correct": [0]}, {"q": "… and ___ to music.", "type": "single", "options": [{"text": "listened"}, {"text": "listening"}, {"text": "listen"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "Last week ___ difficult.", "type": "single", "options": [{"text": "was"}, {"text": "were"}], "correct": [0]}, {"q": "My mum and my sister ___ sick.", "type": "single", "options": [{"text": "were"}, {"text": "was"}, {"text": "are"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["Pete", "went", "to", "the", "bookstore."], "sentence": "Pete went to the bookstore.", "audio_tts": "Pete went to the bookstore."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["I", "cooked", "dinner", "on", "Thursday."], "sentence": "I cooked dinner on Thursday.", "audio_tts": "I cooked dinner on Thursday."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"words": ["I", "liked", "this", "llama."], "sentence": "I liked this llama.", "audio_tts": "I liked this llama."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"words": ["Miriam", "had", "a", "headache", "yesterday."], "sentence": "Miriam had a headache yesterday.", "audio_tts": "Miriam had a headache yesterday."}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"words": ["The nurse", "went", "to", "the park."], "sentence": "The nurse went to the park.", "audio_tts": "The nurse went to the park."}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "needs_review": true, "html": "<p>Расскажи, чем ты занимался на прошлой неделе (5–7 предложений).</p><p><i>For example:<br>On Monday I played tennis.<br>On Wednesday I had English class.<br>On Friday I went to the swimming pool.</i></p><p>Запиши свой ответ, нажав на кнопку микрофона.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11);
end
$mig$;
