-- Super Minds 3 · Unit 1 · School · Test
-- собрано tools/sm3_build.py --lesson u1_test
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
  select v_unit, 'Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с картинками", "pairs": [{"left_image": "@@MEDIA@@sm3/u1/subj_art.webp", "right": "Art", "right_audio_tts": "Art"}, {"left_image": "@@MEDIA@@sm3/u1/subj_english.webp", "right": "English", "right_audio_tts": "English"}, {"left_image": "@@MEDIA@@sm3/u1/subj_geography.webp", "right": "Geography", "right_audio_tts": "Geography"}, {"left_image": "@@MEDIA@@sm3/u1/subj_science.webp", "right": "Science", "right_audio_tts": "Science"}, {"left_image": "@@MEDIA@@sm3/u1/subj_history.webp", "right": "History", "right_audio_tts": "History"}, {"left_image": "@@MEDIA@@sm3/u1/subj_maths.webp", "right": "Maths", "right_audio_tts": "Maths"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: ___ he like eating chocolate?", "type": "single", "options": [{"text": "Do"}, {"text": "Does"}, {"text": "Is"}], "correct": [1]}, {"q": "B: Yes, he ___.", "type": "single", "options": [{"text": "do"}, {"text": "does"}, {"text": "like"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: Do you ___ wear uniform to school?", "type": "single", "options": [{"text": "have"}, {"text": "have to"}, {"text": "do"}], "correct": [1]}, {"q": "B: No, we ___.", "type": "single", "options": [{"text": "don’t"}, {"text": "have"}, {"text": "do"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "Sarah ___ swimming.", "type": "single", "options": [{"text": "like"}, {"text": "doesn’t like"}, {"text": "doesn’t likes"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: Do you ___ watching TV?", "type": "single", "options": [{"text": "like"}, {"text": "likes"}], "correct": [0]}, {"q": "B: Yes, I do. But today I ___ do my homework before I can watch TV.", "type": "single", "options": [{"text": "have"}, {"text": "has to"}, {"text": "have to"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: What do you like ___?", "type": "single", "options": [{"text": "do"}, {"text": "doing"}], "correct": [1]}, {"q": "B: I like ___ computer games.", "type": "single", "options": [{"text": "play"}, {"text": "playing"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["Alice", "has", "to", "walk", "to school."], "sentence": "Alice has to walk to school.", "audio_tts": "Alice has to walk to school."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["July", "doesn’t", "like", "studying", "Geography."], "sentence": "July doesn’t like studying Geography.", "audio_tts": "July doesn't like studying Geography."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"words": ["We", "love", "reading", "about", "knights and queens."], "sentence": "We love reading about knights and queens.", "audio_tts": "We love reading about knights and queens."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"words": ["Caspar", "has", "to", "tidy up", "his room."], "sentence": "Caspar has to tidy up his room.", "audio_tts": "Caspar has to tidy up his room."}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"words": ["Eliot", "and Noah", "hate", "playing", "tennis."], "sentence": "Eliot and Noah hate playing tennis.", "audio_tts": "Eliot and Noah hate playing tennis."}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "needs_review": true, "html": "<p>Расскажи о любимых и нелюбимых школьных предметах (5–7 предложений). Запиши свой ответ, нажав на кнопку микрофона.</p><p><i>For example:<br>I love learning English.<br>I hate Maths. It’s boring.<br>I like studying Music.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11);
end
$mig$;
