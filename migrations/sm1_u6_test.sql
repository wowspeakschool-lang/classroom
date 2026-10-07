-- Super Minds 1 · Unit 6 · My house · Unit 6 Test
-- собрано tools/sm1_build.py --lesson u6_test
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
  select v_unit, 'Unit 6 Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Unit 6 Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Unit 6 Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'exact_input', replace($blk${"items": [{"prompt": "Напиши по-английски: ванная", "accept": ["bathroom", "Bathroom"]}, {"prompt": "Напиши по-английски: спальня", "accept": ["bedroom", "Bedroom"]}, {"prompt": "Напиши по-английски: гостиная", "accept": ["living room", "Living room"]}, {"prompt": "Напиши по-английски: коридор", "accept": ["hall", "Hall"]}, {"prompt": "Напиши по-английски: столовая", "accept": ["dining room", "Dining room"]}, {"prompt": "Напиши по-английски: кухня", "accept": ["kitchen", "Kitchen"]}, {"prompt": "Напиши по-английски: лестница", "accept": ["stairs", "Stairs"]}, {"prompt": "Напиши по-английски: подвал", "accept": ["cellar", "Cellar"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с картинками", "pairs": [{"left_image": "@@MEDIA@@sm1/u6/room_bathroom.webp", "right": "bathroom"}, {"left_image": "@@MEDIA@@sm1/u6/room_bedroom.webp", "right": "bedroom"}, {"left_image": "@@MEDIA@@sm1/u6/room_living_room.webp", "right": "living room"}, {"left_image": "@@MEDIA@@sm1/u6/room_hall.webp", "right": "hall"}, {"left_image": "@@MEDIA@@sm1/u6/room_dining_room.webp", "right": "dining room"}, {"left_image": "@@MEDIA@@sm1/u6/room_kitchen.webp", "right": "kitchen"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "A: ___ there any pears in the fridge?<br>B: Yes, there ___.", "type": "single", "image": "@@MEDIA@@sm1/u6/test_pears.webp", "options": [{"text": "Is … is"}, {"text": "Are … are"}, {"text": "Is … isn't"}, {"text": "Are … aren't"}], "correct": [1]}, {"q": "There ___ a lizard in the bedroom.", "type": "single", "image": "@@MEDIA@@sm1/u6/test_lizard.webp", "options": [{"text": "is"}, {"text": "are"}, {"text": "got"}], "correct": [0]}, {"q": "A: How many planes ___?<br>B: There ___ one plane.", "type": "single", "image": "@@MEDIA@@sm1/u6/test_plane.webp", "options": [{"text": "is there … are"}, {"text": "have got … is"}, {"text": "are there … is"}, {"text": "are there … are"}], "correct": [2]}, {"q": "A: ___ there a crocodile in the picture?<br>B: No, there ___.", "type": "single", "image": "@@MEDIA@@sm1/u6/test_crocodile.webp", "options": [{"text": "Has … hasn't"}, {"text": "Are … aren't"}, {"text": "Is … aren't"}, {"text": "Is … isn't"}], "correct": [3]}, {"q": "A: ___ there any bikes?<br>B: No, there ___.", "type": "single", "image": "@@MEDIA@@sm1/u6/test_bikes.webp", "options": [{"text": "Are … aren't"}, {"text": "Is … isn't"}, {"text": "Do … haven't"}, {"text": "Are … isn't"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке.", "image": "@@MEDIA@@sm1/u6/test_frog_piano.webp", "words": ["There", "is", "a", "frog", "on", "the piano."], "sentence": "There is a frog on the piano."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке.", "image": "@@MEDIA@@sm1/u6/test_dogs.webp", "words": ["How", "many", "dogs", "are", "there?"], "sentence": "How many dogs are there?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке.", "image": "@@MEDIA@@sm1/u6/test_kitten_kitchen.webp", "words": ["Is", "there", "a", "cat", "in", "the kitchen?"], "sentence": "Is there a cat in the kitchen?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке.", "image": "@@MEDIA@@sm1/u6/test_park_empty.webp", "words": ["There", "aren't", "any", "go-karts", "in the park."], "sentence": "There aren't any go-karts in the park."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке.", "image": "@@MEDIA@@sm1/u6/test_books_bedroom.webp", "words": ["Are", "there", "any", "books", "in the bedroom?"], "sentence": "Are there any books in the bedroom?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'gaps', replace($blk${"title": "Прочитай текст и перетащи слова в пропуски.", "mode": "drag", "text": "This is Ben's house. It is old and very big. There are six rooms!\nBen's favourite room is the __kitchen__. He loves food! There's a big table and there are five chairs. There's a fridge and a cat! The cat is under the table.\nUpstairs, there's Ben's __bedroom__. There's a bed, a desk, and two lamps. There are lots of books on the desk. Ben reads every night!\nThere are __three__ bathrooms — one upstairs and two downstairs. That's a lot of bathrooms!\nOutside, there's a beautiful __garden__. There are four trees, lots of flowers, and a little pond with fish!\nBut there __isn't__ a living room. That's OK — Ben and his family sit in the kitchen together!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'video', replace($blk${"title": "Послушай диалог Тома и Сары: Том пришёл к Саре в гости.", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'truefalse', replace($blk${"title": "Прочитай предложения и отметь — True (верно) или False (неверно).", "statements": [{"text": "The kitchen is big.", "correct": false}, {"text": "There are four chairs in the kitchen.", "correct": true}, {"text": "There's a television in the living room.", "correct": false}, {"text": "There are books in the bedroom.", "correct": true}, {"text": "There is a garden.", "correct": true}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "html": "<p>Посмотри на картинку. Опиши, кого ты видишь (используй <b>there is / there are</b>).</p><p><i>For example: There are two boys. There is one dog. There is a frog on the bag.</i></p><p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>", "image": "@@MEDIA@@sm1/u6/test_fishing_scene.webp", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 11);
end
$mig$;
