-- Super Minds 1 · Final Test · Final Test
-- собрано tools/sm1_build.py --lesson final_test
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Final Test', 10
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Final Test');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Final Test';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Final Test', 'test',
         80, false, 0
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Final Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Final Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'video', replace($blk${"title": "Final test · Listening. Послушай рассказ", "url": "https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/sm1/sm1_final_b1%20(1).mp3", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Послушай рассказ ещё раз и выбери правильную картинку.", "questions": [{"q": "What has Tom got?", "type": "single", "options": [{"image": "@@MEDIA@@sm1/u2/toy_train.webp"}, {"image": "@@MEDIA@@sm1/u2/toy_kite.webp"}, {"image": "@@MEDIA@@sm1/u2/toy_car.webp"}], "correct": [1]}, {"q": "What does Anna like?", "type": "single", "options": [{"image": "@@MEDIA@@sm1/u4/food_cake.webp"}, {"image": "@@MEDIA@@sm1/u4/food_banana.webp"}, {"image": "@@MEDIA@@sm1/u4/food_pizza.webp"}], "correct": [2]}, {"q": "What pet has Sue got?", "type": "single", "options": [{"image": "@@MEDIA@@sm1/u3/animal_dog.webp"}, {"image": "@@MEDIA@@sm1/u3/animal_cat.webp"}, {"image": "@@MEDIA@@sm1/u3/animal_rat.webp"}], "correct": [0]}, {"q": "What can Ben do?", "type": "single", "options": [{"image": "@@MEDIA@@sm1/u5/act_go_swimming.webp"}, {"image": "@@MEDIA@@sm1/u5/act_ride_bike.webp"}, {"image": "@@MEDIA@@sm1/u5/act_play_football.webp"}], "correct": [1]}, {"q": "What is Nick wearing today?", "type": "single", "options": [{"image": "@@MEDIA@@sm1/u7/clothes_cap.webp"}, {"image": "@@MEDIA@@sm1/u7/clothes_shorts.webp"}, {"image": "@@MEDIA@@sm1/u7/clothes_jacket.webp"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'hotspot', replace($blk${"title": "Послушай аудио и соедини имена людей с их изображениями", "mode": "label", "image": "@@MEDIA@@sm1/ft/ft_picnic.webp", "points": [{"x": 30.7, "y": 70.1, "text": "Jane", "audio_tts": "Jane"}, {"x": 18.2, "y": 27.3, "text": "Mike", "audio_tts": "Mike"}, {"x": 63.5, "y": 65.6, "text": "Laura", "audio_tts": "Laura"}, {"x": 15.2, "y": 70.1, "text": "Clare", "audio_tts": "Clare"}, {"x": 40.9, "y": 26.2, "text": "Paul", "audio_tts": "Paul"}], "extras": []}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку и прочитай предложение. Выбери ✅, если картинка и предложение совпадают, и ❌, если они отличаются.", "questions": [{"q": "This is a ruler.", "type": "single", "image": "@@MEDIA@@sm1/ft/ft_eraser.webp", "options": [{"text": "✅ совпадает"}, {"text": "❌ не совпадает"}], "correct": [1]}, {"q": "This is a spider.", "type": "single", "image": "@@MEDIA@@sm1/ft/ft_spider.webp", "options": [{"text": "✅ совпадает"}, {"text": "❌ не совпадает"}], "correct": [0]}, {"q": "This is a bike.", "type": "single", "image": "@@MEDIA@@sm1/ft/ft_bike.webp", "options": [{"text": "✅ совпадает"}, {"text": "❌ не совпадает"}], "correct": [0]}, {"q": "This is a face.", "type": "single", "image": "@@MEDIA@@sm1/ft/ft_arm.webp", "options": [{"text": "✅ совпадает"}, {"text": "❌ не совпадает"}], "correct": [1]}, {"q": "This is a chicken.", "type": "single", "image": "@@MEDIA@@sm1/ft/ft_chicken.webp", "options": [{"text": "✅ совпадает"}, {"text": "❌ не совпадает"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p>Посмотри на картинку. В следующем задании прочитай предложения и выбери <b>Верно</b>, если предложение соответствует картинке, и <b>Неверно</b>, если нет.</p><p><img src=\"@@MEDIA@@sm1/ft/ft_kitchen.webp\" alt=\"Семья за завтраком\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'truefalse', replace($blk${"title": "Верно или неверно?", "statements": [{"text": "There is a banana on the table.", "correct": true}, {"text": "They are sitting in the bedroom.", "correct": false}, {"text": "There is 1 girl.", "correct": true}, {"text": "There is a red lamp under the table.", "correct": false}, {"text": "There is one chair.", "correct": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'exact_input', replace($blk${"items": [{"prompt": "Посмотри на картинку и буквы и напиши слово (6 букв)", "image": "@@MEDIA@@sm1/ft/ft_word_pencil.webp", "accept": ["pencil"]}, {"prompt": "Посмотри на картинку и буквы и напиши слово (7 букв)", "image": "@@MEDIA@@sm1/ft/ft_word_monster.webp", "accept": ["monster"]}, {"prompt": "Посмотри на картинку и буквы и напиши слово (4 буквы)", "image": "@@MEDIA@@sm1/ft/ft_word_duck.webp", "accept": ["duck"]}, {"prompt": "Посмотри на картинку и буквы и напиши слово (8 букв)", "image": "@@MEDIA@@sm1/ft/ft_word_bathroom.webp", "accept": ["bathroom"]}, {"prompt": "Посмотри на картинку и буквы и напиши слово (7 букв)", "image": "@@MEDIA@@sm1/ft/ft_word_sweater.webp", "accept": ["sweater"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6);
end
$mig$;
