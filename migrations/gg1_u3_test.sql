-- Go Getter 1 · Unit 3 · My home · Test
-- собрано tools/gg1_build.py --lesson u3_test
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 3 · My home', 3
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 3 · My home');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 3 · My home';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'match', replace($blk${"title": "Соедини слова и картинки", "pairs": [{"left_image": "@@MEDIA@@gg1/u3/prep_on.webp", "right": "on the box"}, {"left_image": "@@MEDIA@@gg1/u3/room_living_room.webp", "right": "living room"}, {"left_image": "@@MEDIA@@gg1/u3/furn_wardrobe.webp", "right": "wardrobe"}, {"left_image": "@@MEDIA@@gg1/u3/prep_in_front_of.webp", "right": "in front of the box"}, {"left_image": "@@MEDIA@@gg1/u3/furn_shower.webp", "right": "shower"}, {"left_image": "@@MEDIA@@gg1/u3/part_window.webp", "right": "window"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'exact_input', replace($blk${"title": "Посмотри на картинку, вставь пропущенные буквы и впиши слово целиком", "items": [{"prompt": "un_er the tree", "accept": ["under the tree", "under", "Under the tree", "Under"], "image": "@@MEDIA@@gg1/u3/photo_presents_tree.webp"}, {"prompt": "l_mp", "accept": ["lamp", "Lamp"], "image": "@@MEDIA@@gg1/u3/photo_lamp.webp"}, {"prompt": "c_rp_t", "accept": ["carpet", "Carpet"], "image": "@@MEDIA@@gg1/u3/furn_carpet.webp"}, {"prompt": "gar_en", "accept": ["garden", "Garden"], "image": "@@MEDIA@@gg1/u3/photo_garden.webp"}, {"prompt": "b_dro_m", "accept": ["bedroom", "Bedroom"], "image": "@@MEDIA@@gg1/u3/photo_bedroom_2.webp"}, {"prompt": "arm_hair", "accept": ["armchair", "Armchair"], "image": "@@MEDIA@@gg1/u3/photo_armchair.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери пропущенное слово", "questions": [{"q": "A: ___ there a raccoon on my head? B: Yes, there is. And there's a squirrel too.", "type": "single", "options": [{"text": "Is"}, {"text": "Are"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/raccoon_squirrel.webp"}, {"q": "A: Is there a raccoon on my head? B: ___, there is. And there's a squirrel too.", "type": "single", "options": [{"text": "No"}, {"text": "Yes"}], "correct": [1]}, {"q": "A: ___ there two clowns on the table? B: Yes, there are.", "type": "single", "options": [{"text": "Are"}, {"text": "Is"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/clowns.webp"}, {"q": "A: Are there two clowns on the table? B: Yes, there ___.", "type": "single", "options": [{"text": "is"}, {"text": "are"}, {"text": "aren't"}, {"text": "isn't"}], "correct": [1]}, {"q": "A: Is ___ a unicorn in the kitchen? B: No, there isn't.", "type": "single", "options": [{"text": "there"}, {"text": "here"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/unicorn.webp"}, {"q": "A: Is there a unicorn in the kitchen? B: ___, there isn't.", "type": "single", "options": [{"text": "Yes"}, {"text": "No"}], "correct": [1]}, {"q": "A: ___ there a big pink elephant in the garage? B: Yes, there is! But there isn't a big pink elephant in the house!", "type": "single", "options": [{"text": "Is"}, {"text": "Are"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/pink_elephant.webp"}, {"q": "A: Is there a big pink elephant in the garage? B: ___, there is! But there isn't a big pink elephant in the house!", "type": "single", "options": [{"text": "No"}, {"text": "Yes"}], "correct": [1]}, {"q": "A: ___ you like an ice cream sandwich? B: Yes, please!", "type": "single", "options": [{"text": "Would"}, {"text": "Do"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/ice_cream_sandwich.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["There", "isn't", "a jellyfish", "on", "the table."], "sentence": "There isn't a jellyfish on the table.", "audio_tts": "There isn't a jellyfish on the table.", "image": "@@MEDIA@@gg1/u3/jellyfish.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["There", "aren't", "four", "funny dragons", "in", "the garden."], "sentence": "There aren't four funny dragons in the garden.", "audio_tts": "There aren't four funny dragons in the garden.", "image": "@@MEDIA@@gg1/u3/dragon.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["There", "isn't", "a small green", "alien", "in", "the garage."], "sentence": "There isn't a small green alien in the garage.", "audio_tts": "There isn't a small green alien in the garage.", "image": "@@MEDIA@@gg1/u3/alien.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["There", "are", "twenty lazy cats", "in", "my grandma's", "bedroom."], "sentence": "There are twenty lazy cats in my grandma's bedroom.", "audio_tts": "There are twenty lazy cats in my grandma's bedroom.", "image": "@@MEDIA@@gg1/u3/cat_sofa.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["There", "is", "a crazy blue", "monster", "in", "my bedroom."], "sentence": "There is a crazy blue monster in my bedroom.", "audio_tts": "There is a crazy blue monster in my bedroom.", "image": "@@MEDIA@@gg1/u3/blue_monster.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<h3>READING</h3><p>Прочитай описание комнаты подростка.</p><p><i>This is my bedroom. There is a bed next to the window. There is a small desk in front of the bed. My laptop is on the desk. There is a wardrobe behind the door. There are two posters on the wall. There aren't any plants in my room. My skateboard is under the bed. There isn't a TV in my bedroom — I watch films in the living room.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'truefalse', replace($blk${"title": "READING. Правда или неправда?", "statements": [{"text": "The bed is next to the window.", "correct": true}, {"text": "The desk is behind the bed.", "correct": false}, {"text": "The laptop is on the desk.", "correct": true}, {"text": "There are three posters on the wall.", "correct": false}, {"text": "There are plants in the bedroom.", "correct": false}, {"text": "The skateboard is under the bed.", "correct": true}, {"text": "There is a TV in the bedroom.", "correct": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>LISTENING. Прослушай 5 коротких описаний.</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'match', replace($blk${"title": "LISTENING. Соедини каждый номер с названием комнаты в доме", "pairs": [{"left": "Description 1", "right": "kitchen"}, {"left": "Description 2", "right": "living room"}, {"left": "Description 3", "right": "bathroom"}, {"left": "Description 4", "right": "bedroom"}, {"left": "Description 5", "right": "garage"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "image": "@@MEDIA@@gg1/u3/kids_room_test.webp", "html": "<p>Посмотри на картинку и опиши её. Эти вопросы могут тебе помочь. Запиши свой ответ, нажав на кнопку микрофона 🙌</p><ol><li>Where is the guitar?</li><li>Where is the teddy bear?</li><li>How many boxes are there on the wardrobe?</li><li>Where is the book?</li><li>Where is the school bag?</li><li>Where is the skateboard?</li><li>Where is the ball?</li><li>How many books are there on the shelf?</li><li>Where is the chair?</li><li>Where is the carpet?</li><li>How many lamps are there in the room?</li></ol>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 12);
end
$mig$;
