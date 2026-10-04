-- Super Minds 3 · Unit 8 · Countries · Test
-- собрано tools/sm3_build.py --lesson u8_test
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
  select v_unit, 'Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с картинками", "pairs": [{"left_image": "@@MEDIA@@sm3/u8/country_australia.webp", "right": "Australia", "right_audio_tts": "Australia"}, {"left_image": "@@MEDIA@@sm3/u8/country_china.webp", "right": "China", "right_audio_tts": "China"}, {"left_image": "@@MEDIA@@sm3/u8/country_turkey.webp", "right": "Turkey", "right_audio_tts": "Turkey"}, {"left_image": "@@MEDIA@@sm3/u8/country_egypt.webp", "right": "Egypt", "right_audio_tts": "Egypt"}, {"left_image": "@@MEDIA@@sm3/u8/country_argentina.webp", "right": "Argentina", "right_audio_tts": "Argentina"}, {"left_image": "@@MEDIA@@sm3/u8/country_brazil.webp", "right": "Brazil", "right_audio_tts": "Brazil"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: ___ you buy me a present?", "type": "single", "options": [{"text": "Did"}, {"text": "Are"}, {"text": "Were"}], "correct": [0]}, {"q": "B: No, I ___.", "type": "single", "options": [{"text": "didn’t"}, {"text": "did"}, {"text": "weren’t"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: Did you ___ shopping with Maya on Sunday?", "type": "single", "options": [{"text": "go"}, {"text": "went"}, {"text": "going"}], "correct": [0]}, {"q": "B: Yes, we ___.", "type": "single", "options": [{"text": "did"}, {"text": "go"}, {"text": "didn’t"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "He ___ see the pyramids in Egypt.", "type": "single", "options": [{"text": "didn’t"}, {"text": "don’t"}, {"text": "isn’t"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: Where ___ you stay in Mexico?", "type": "single", "options": [{"text": "did"}, {"text": "were"}, {"text": "are"}], "correct": [0]}, {"q": "B: We ___ in a hotel on the beach.", "type": "single", "options": [{"text": "stayed"}, {"text": "stay"}, {"text": "staying"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: ___ he eat a lot of pizza yesterday?", "type": "single", "options": [{"text": "Did"}, {"text": "Does"}, {"text": "Do"}], "correct": [0]}, {"q": "B: Yes, he ___.", "type": "single", "options": [{"text": "did"}, {"text": "does"}, {"text": "didn’t"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["Did", "you", "have", "fun", "in", "Spain?"], "sentence": "Did you have fun in Spain?", "audio_tts": "Did you have fun in Spain?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["How", "long", "did", "she", "stay", "there?"], "sentence": "How long did she stay there?", "audio_tts": "How long did she stay there?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"words": ["We", "went", "to", "Chile", "for", "a week."], "sentence": "We went to Chile for a week.", "audio_tts": "We went to Chile for a week."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"words": ["Did", "you", "go", "to", "a", "museum?"], "sentence": "Did you go to a museum?", "audio_tts": "Did you go to a museum?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"words": ["Did", "she", "send", "lots of", "postcards?"], "sentence": "Did she send lots of postcards?", "audio_tts": "Did she send lots of postcards?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "needs_review": true, "html": "<p>Представь, что ты берёшь интервью у космонавта. Составь 5 вопросов со словами <b>Where · How · Who · What · How long</b> и ответь на них.</p><p><i>For example:<br>Where did you go? — I went to Mars.<br>How did you get there? — I flew in a rocket.<br>Who did you meet there? — I met friendly purple aliens. / I didn’t meet anyone.</i></p><p>Запиши свой ответ, нажав на кнопку микрофона.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11);
end
$mig$;
