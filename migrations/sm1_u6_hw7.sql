-- Super Minds 1 · Unit 6 · My house · Homework 7
-- собрано tools/sm1_build.py --lesson u6_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 6 · My house', 6
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 6 · My house');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 6 · My house';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет, исследователь старого дома!</h2><p>Это последняя домашка перед тестом! Повтори все комнаты, <b>There’s / There are</b> и вопросы <b>Is there / Are there</b>.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Посмотри на картинку и выбери правильное слово.", "type": "single", "image": "@@MEDIA@@sm1/u6/room_cellar_hw7.webp", "options": [{"text": "bedroom"}, {"text": "bathroom"}, {"text": "kitchen"}, {"text": "cellar"}], "correct": [3]}, {"q": "Посмотри на картинку и выбери правильное слово.", "type": "single", "image": "@@MEDIA@@sm1/u6/room_hall_hw7.webp", "options": [{"text": "hall"}, {"text": "dining room"}, {"text": "bathroom"}, {"text": "living room"}], "correct": [0]}, {"q": "Посмотри на картинку и выбери правильное слово.", "type": "single", "image": "@@MEDIA@@sm1/u6/room_stairs_hw7.webp", "options": [{"text": "kitchen"}, {"text": "stairs"}, {"text": "bedroom"}, {"text": "hall"}], "correct": [1]}, {"q": "Посмотри на картинку и выбери правильное слово.", "type": "single", "image": "@@MEDIA@@sm1/u6/room_dining_hw7.webp", "options": [{"text": "cellar"}, {"text": "kitchen"}, {"text": "dining room"}, {"text": "living room"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши There’s или There are.", "mode": "type", "text": "1. __There’s|There's|There is__ a spider in the cellar.\n2. __There are__ three fish in the hall.\n3. __There’s|There's|There is__ a monster in the bedroom.\n4. __There are__ two cats in the living room.\n5. __There are__ four mice in the dining room.\n6. __There’s|There's|There is__ a bat in the bathroom."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Is there a bath in the kitchen?", "type": "single", "audio_tts": "Is there a bath in the kitchen?", "options": [{"text": "Yes, there is."}, {"text": "No, there isn’t."}, {"text": "Yes, there are."}], "correct": [1]}, {"q": "Is there a bed in the bedroom?", "type": "single", "audio_tts": "Is there a bed in the bedroom?", "options": [{"text": "No, there isn’t."}, {"text": "Yes, there are."}, {"text": "Yes, there is."}], "correct": [2]}, {"q": "Is there a fridge in the bathroom?", "type": "single", "audio_tts": "Is there a fridge in the bathroom?", "options": [{"text": "No, there isn’t."}, {"text": "Yes, there is."}, {"text": "Yes, there are."}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"title": "Слова перепутаны! Составь правильное предложение.", "words": ["Is", "there", "a cat", "in", "the kitchen?"], "sentence": "Is there a cat in the kitchen?", "audio_tts": "Is there a cat in the kitchen?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"title": "Составь правильное предложение.", "words": ["There", "are", "three", "cats", "in", "the hall."], "sentence": "There are three cats in the hall.", "audio_tts": "There are three cats in the hall."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Составь правильное предложение.", "words": ["Are", "there", "any", "spiders", "in", "the bathroom?"], "sentence": "Are there any spiders in the bathroom?", "audio_tts": "Are there any spiders in the bathroom?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'speaking', replace($blk${"title": "Расскажи, что ты видишь 🎤", "html": "<p>Посмотри на картинку. Нажми на микрофон и расскажи, что ты видишь (5–7 предложений).</p><p><i>Пример: There is a house. There are 5 rooms. There is a bedroom. There is a bed in the bedroom.</i></p>", "image": "@@MEDIA@@sm1/u6/house_rooms.webp", "sample_tts": "There is a house. There are five rooms. There is a bedroom. There is a bed in the bedroom.", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'match', replace($blk${"title": "⭐ Дополнительное задание для настоящих чемпионов! Соедини картинку со словом", "pairs": [{"left_image": "@@MEDIA@@sm1/u6/room_bathroom.webp", "right": "bathroom", "right_audio_tts": "bathroom"}, {"left_image": "@@MEDIA@@sm1/u6/room_bedroom.webp", "right": "bedroom", "right_audio_tts": "bedroom"}, {"left_image": "@@MEDIA@@sm1/u6/room_living_room.webp", "right": "living room", "right_audio_tts": "living room"}, {"left_image": "@@MEDIA@@sm1/u6/room_hall.webp", "right": "hall", "right_audio_tts": "hall"}, {"left_image": "@@MEDIA@@sm1/u6/room_dining_room.webp", "right": "dining room", "right_audio_tts": "dining room"}, {"left_image": "@@MEDIA@@sm1/u6/room_kitchen.webp", "right": "kitchen", "right_audio_tts": "kitchen"}, {"left_image": "@@MEDIA@@sm1/u6/room_stairs.webp", "right": "stairs", "right_audio_tts": "stairs"}, {"left_image": "@@MEDIA@@sm1/u6/room_cellar.webp", "right": "cellar", "right_audio_tts": "cellar"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "___ a monster in the cellar.", "type": "single", "options": [{"text": "There’s"}, {"text": "There are"}], "correct": [0]}, {"q": "___ two beds in the bedroom.", "type": "single", "options": [{"text": "There’s"}, {"text": "There are"}], "correct": [1]}, {"q": "___ there a sofa in the living room? — Yes, there is.", "type": "single", "options": [{"text": "Are"}, {"text": "Is"}], "correct": [1]}, {"q": "___ there any spiders in the hall? — No, there aren’t.", "type": "single", "options": [{"text": "Are"}, {"text": "Is"}], "correct": [0]}, {"q": "Is there a bath in the bathroom?", "type": "single", "options": [{"text": "Yes, there is."}, {"text": "Yes, there are."}], "correct": [0]}, {"q": "Are there any chairs in the dining room?", "type": "single", "options": [{"text": "Yes, there is."}, {"text": "Yes, there are."}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты повторил все комнаты, There’s / There are и вопросы.</h3><p>Молодец! Ты готов к тесту! 🏆</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
