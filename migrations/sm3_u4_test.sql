-- Super Minds 3 · Unit 4 · In the town · Test
-- собрано tools/sm3_build.py --lesson u4_test
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
  select v_unit, 'Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с картинками", "pairs": [{"left_image": "@@MEDIA@@sm3/u4/town_library.webp", "right": "Library", "right_audio_tts": "library"}, {"left_image": "@@MEDIA@@sm3/u4/town_bus_station.webp", "right": "Bus station", "right_audio_tts": "bus station"}, {"left_image": "@@MEDIA@@sm3/u4/town_map.webp", "right": "Map", "right_audio_tts": "map"}, {"left_image": "@@MEDIA@@sm3/u4/town_bank.webp", "right": "Bank", "right_audio_tts": "bank"}, {"left_image": "@@MEDIA@@sm3/u4/town_market.webp", "right": "Market square", "right_audio_tts": "market square"}, {"left_image": "@@MEDIA@@sm3/u4/town_tower.webp", "right": "Tower", "right_audio_tts": "tower"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "The mouse is ___ the TV.", "type": "single", "image": "@@MEDIA@@sm3/u4/prep_mouse_near_tv.webp", "options": [{"text": "near"}, {"text": "opposite"}, {"text": "below"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "The ball is ___ the table.", "type": "single", "image": "@@MEDIA@@sm3/u4/prep_ball_above_table.webp", "options": [{"text": "above"}, {"text": "below"}, {"text": "opposite"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "The mouse is ___ the boxes.", "type": "single", "image": "@@MEDIA@@sm3/u4/prep_mouse_between_boxes.webp", "options": [{"text": "between"}, {"text": "above"}, {"text": "near"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "He ___ the sports centre.", "type": "single", "options": [{"text": "is going to"}, {"text": "going to"}, {"text": "go to"}], "correct": [0]}, {"q": "He is going to the sports centre to ___.", "type": "single", "image": "@@MEDIA@@sm3/u4/going_sports_centre.webp", "options": [{"text": "go swimming"}, {"text": "borrow a book"}, {"text": "buy some apples"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "The dog is ___ the cat.", "type": "single", "image": "@@MEDIA@@sm3/u4/prep_cat_dog_opposite.webp", "options": [{"text": "opposite"}, {"text": "above"}, {"text": "near"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "The picture is ___ the window.", "type": "single", "image": "@@MEDIA@@sm3/u4/prep_picture_below_window.webp", "options": [{"text": "below"}, {"text": "above"}, {"text": "between"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["The tree", "is", "opposite", "the house."], "sentence": "The tree is opposite the house.", "audio_tts": "The tree is opposite the house."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"words": ["I’m", "going", "to", "the park", "to ride", "my bike."], "sentence": "I’m going to the park to ride my bike.", "audio_tts": "I'm going to the park to ride my bike."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"words": ["We", "are", "going", "to", "the library."], "sentence": "We are going to the library.", "audio_tts": "We are going to the library."}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"words": ["The", "bank", "is", "between", "two", "trees."], "sentence": "The bank is between two trees.", "audio_tts": "The bank is between two trees."}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'order', replace($blk${"words": ["Julia", "is", "going", "to", "the", "supermarket."], "sentence": "Julia is going to the supermarket.", "audio_tts": "Julia is going to the supermarket."}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤 Part 1", "needs_review": true, "image": "@@MEDIA@@sm3/u4/scene_town_busy.webp", "html": "<p>Посмотри на картинку и опиши её, используя предлоги места (4–5 предложений).</p><p><i>For example: The library is near the shopping centre. The bench is between two small trees.</i></p><p>Запиши свой ответ, нажав на кнопку микрофона.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤 Part 2", "needs_review": true, "image": "@@MEDIA@@sm3/u4/scene_town_busy.webp", "html": "<p>Посмотри на картинку и опиши, кто куда направляется и зачем (4–5 предложений).</p><p><i>For example: They are going to the market square to buy some apples.</i></p><p>Запиши свой ответ, нажав на кнопку микрофона.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 13);
end
$mig$;
