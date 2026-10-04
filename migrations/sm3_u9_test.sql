-- Super Minds 3 · Unit 9 · Weather · Unit 9 Test
-- собрано tools/sm3_build.py --lesson u9_test
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
  select v_unit, 'Unit 9 Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Unit 9 Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Unit 9 Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с картинками", "pairs": [{"left": "umbrella", "right_image": "@@MEDIA@@sm3/u9/clothes_umbrella.webp", "right": "umbrella picture"}, {"left": "boots", "right_image": "@@MEDIA@@sm3/u9/clothes_boots.webp", "right": "boots picture"}, {"left": "thunderstorm", "right_image": "@@MEDIA@@sm3/u9/weather_thunderstorm.webp", "right": "thunderstorm picture"}, {"left": "cloudy", "right_image": "@@MEDIA@@sm3/u9/weather_cloudy.webp", "right": "cloudy picture"}, {"left": "raincoat", "right_image": "@@MEDIA@@sm3/u9/clothes_raincoat.webp", "right": "raincoat picture"}, {"left": "foggy", "right_image": "@@MEDIA@@sm3/u9/weather_foggy.webp", "right": "foggy picture"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "On Wednesday it’s going to be ___ and foggy.", "type": "single", "options": [{"text": "sunny"}, {"text": "cloudy"}], "correct": [1]}, {"q": "On Wednesday it’s going to be cloudy and ___.", "type": "single", "options": [{"text": "foggy"}, {"text": "rainy"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "I’m going to ___ and read my favourite book.", "type": "single", "options": [{"text": "go out"}, {"text": "stay at home"}], "correct": [1]}, {"q": "I’m going to stay at home and ___ my favourite book.", "type": "single", "options": [{"text": "draw"}, {"text": "read"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "I’m ___ to travel to Italy.", "type": "single", "options": [{"text": "go"}, {"text": "going"}, {"text": "went"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: ___ you going to play in the garden?", "type": "single", "options": [{"text": "Am"}, {"text": "Are"}, {"text": "Is"}], "correct": [1]}, {"q": "B: ___, I’m not.", "type": "single", "options": [{"text": "No"}, {"text": "Yes"}], "correct": [0]}, {"q": "B: I’m going to ___ with my aunt.", "type": "single", "options": [{"text": "swim"}, {"text": "read"}, {"text": "cook"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: ___ are you going to do on holidays?", "type": "single", "options": [{"text": "Why"}, {"text": "What"}, {"text": "When"}], "correct": [1]}, {"q": "A: What are you ___ to do on holidays?", "type": "single", "options": [{"text": "go"}, {"text": "going"}], "correct": [1]}, {"q": "B: I’m going ___ to the library.", "type": "single", "options": [{"text": "go"}, {"text": "to go"}, {"text": "going"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: What ___ you going to do this weekend?", "type": "single", "options": [{"text": "is"}, {"text": "am"}, {"text": "are"}], "correct": [2]}, {"q": "B: ___ going to swim in the sea.", "type": "single", "options": [{"text": "I"}, {"text": "I’m"}, {"text": "I is"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["Are", "you", "going", "to", "swim?"], "sentence": "Are you going to swim?", "audio_tts": "Are you going to swim?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"words": ["I’m", "going", "to", "read", "a", "book."], "sentence": "I’m going to read a book.", "audio_tts": "I’m going to read a book."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"words": ["What", "are", "you", "going", "to", "do?"], "sentence": "What are you going to do?", "audio_tts": "What are you going to do?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"words": ["It’s", "going", "to", "be", "cloudy", "on", "Monday."], "sentence": "It’s going to be cloudy on Monday.", "audio_tts": "It’s going to be cloudy on Monday."}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'order', replace($blk${"words": ["I’m", "not", "going", "to", "watch", "YouTube."], "sentence": "I’m not going to watch YouTube.", "audio_tts": "I’m not going to watch YouTube."}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK · Part 1", "image": "@@MEDIA@@sm3/u9/scene_holiday_plans.webp", "html": "<p>Посмотри на картинку и составь предложения о своих планах на выходные или праздники (5–7 предложений)! Используй be going to.</p><p><i>For example: I’m going to read my favourite book at the weekend.</i></p><p>Запиши свой ответ, нажав на кнопку микрофона.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK · Part 2", "image": "@@MEDIA@@sm3/u9/weather_week_board.webp", "html": "<p>Посмотри на картинку и опиши, какая будет погода.</p><p><i>For example: On Wednesday it’s going to be cloudy.</i></p><p>Запиши свой ответ, нажав на кнопку микрофона.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 13);
end
$mig$;
