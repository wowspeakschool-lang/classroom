-- Super Minds 1 · Unit 2 · My toys · Unit 2 Test
-- собрано tools/sm1_build.py --lesson u2_test
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 2 · My toys', 2
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 2 · My toys');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 2 · My toys';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Unit 2 Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Unit 2 Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Unit 2 Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'exact_input', replace($blk${"items": [{"prompt": "Впиши слово целиком: d _ l l (кукла)", "accept": ["doll"], "audio_tts": "doll"}, {"prompt": "Впиши слово целиком: b _ l l (мяч)", "accept": ["ball"], "audio_tts": "ball"}, {"prompt": "Впиши слово целиком: k _ t e (воздушный змей)", "accept": ["kite"], "audio_tts": "kite"}, {"prompt": "Впиши слово целиком: c _ r (машина)", "accept": ["car"], "audio_tts": "car"}, {"prompt": "Впиши слово целиком: b i _ e (велосипед)", "accept": ["bike"], "audio_tts": "bike"}, {"prompt": "Впиши слово целиком: g o - k _ r t (картинг)", "accept": ["go-kart"], "audio_tts": "go-kart"}, {"prompt": "Впиши слово целиком: t r _ _ n (поезд)", "accept": ["train"], "audio_tts": "train"}, {"prompt": "Впиши слово целиком: m o n s _ e r (монстр)", "accept": ["monster"], "audio_tts": "monster"}, {"prompt": "Впиши слово целиком: p l _ n e (самолёт)", "accept": ["plane"], "audio_tts": "plane"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с картинками", "pairs": [{"left_image": "@@MEDIA@@sm1/u2/toy_doll.webp", "right": "doll", "right_audio_tts": "doll"}, {"left_image": "@@MEDIA@@sm1/u2/toy_kite.webp", "right": "kite", "right_audio_tts": "kite"}, {"left_image": "@@MEDIA@@sm1/u2/toy_go_kart.webp", "right": "go-kart", "right_audio_tts": "go-kart"}, {"left_image": "@@MEDIA@@sm1/u2/toy_monster.webp", "right": "monster", "right_audio_tts": "monster"}, {"left_image": "@@MEDIA@@sm1/u2/toy_car.webp", "right": "car", "right_audio_tts": "car"}, {"left_image": "@@MEDIA@@sm1/u2/toy_train.webp", "right": "train", "right_audio_tts": "train"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'speaking', replace($blk${"title": "Прочитай предложения вслух 🎤", "html": "<p>Внимательно прочитай предложения глазками 👀</p><p>Нажми на микрофон 🎤 и проговори их вслух. У тебя получится! 🌟</p><ol><li>I can see a big tree.</li><li>The car is in the yard.</li><li>This is a long string.</li><li>The boat is old.</li><li>The kite flies high in the sky.</li></ol>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: ___ her favourite toy?<br>B: Her favourite toy is a plane.", "type": "single", "options": [{"text": "Who’s"}, {"text": "What’s"}, {"text": "Whose"}], "correct": [1], "image": "@@MEDIA@@sm1/u2/t_plane.webp"}, {"q": "A: What’s her favourite toy?<br>B: Her ___ toy is a plane.", "type": "single", "options": [{"text": "favourite"}, {"text": "the"}, {"text": "a"}], "correct": [0]}, {"q": "A: How ___ is she?<br>B: She’s seven.", "type": "single", "options": [{"text": "young"}, {"text": "happy"}, {"text": "old"}], "correct": [2], "image": "@@MEDIA@@sm1/u2/t_girl_seven.webp"}, {"q": "A: How old is she?<br>B: ___ seven.", "type": "single", "options": [{"text": "She’re"}, {"text": "She’s"}, {"text": "She"}], "correct": [1]}, {"q": "A: What’s ___ name?<br>B: My name is Alex.", "type": "single", "options": [{"text": "your"}, {"text": "you"}, {"text": "my"}], "correct": [0], "image": "@@MEDIA@@sm1/u2/t_meeting.webp"}, {"q": "A: What’s your name?<br>B: ___ name is Alex.", "type": "single", "options": [{"text": "You"}, {"text": "Your"}, {"text": "My"}], "correct": [2]}, {"q": "A: What ___ it?<br>B: It’s an ugly monster.", "type": "single", "options": [{"text": "am"}, {"text": "is"}, {"text": "are"}], "correct": [1], "image": "@@MEDIA@@sm1/u2/t_monster_blue.webp"}, {"q": "A: What is it?<br>B: It’s ___ ugly monster.", "type": "single", "options": [{"text": "a"}, {"text": "an"}], "correct": [1]}, {"q": "It’s ___ small yellow ball.", "type": "single", "options": [{"text": "a"}, {"text": "an"}], "correct": [0], "image": "@@MEDIA@@sm1/u2/t_yellow_ball.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["His", "favourite", "number", "is", "ten."], "sentence": "His favourite number is ten.", "audio_tts": "His favourite number is ten.", "image": "@@MEDIA@@sm1/u2/t_number_ten.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["It’s", "a", "new", "beautiful", "bike."], "sentence": "It’s a new beautiful bike.", "audio_tts": "It’s a new beautiful bike.", "image": "@@MEDIA@@sm1/u2/t_bike.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["What", "is", "her", "favourite", "toy?"], "sentence": "What is her favourite toy?", "audio_tts": "What is her favourite toy?", "image": "@@MEDIA@@sm1/u2/t_toys.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["It’s", "a", "short", "green", "train."], "sentence": "It’s a short green train.", "audio_tts": "It’s a short green train.", "image": "@@MEDIA@@sm1/u2/t_green_train.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["It’s", "a", "funny", "purple", "monster."], "sentence": "It’s a funny purple monster.", "audio_tts": "It’s a funny purple monster.", "image": "@@MEDIA@@sm1/u2/t_purple_monster.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'video', replace($blk${"title": "Послушай аудио и выполни задание ниже 🎧", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'hotspot', replace($blk${"title": "Послушай аудио выше и соедини имя с ребёнком", "mode": "label", "image": "@@MEDIA@@sm1/u2/t_kids_toys.webp", "points": [{"x": 11.0, "y": 70, "text": "Amy", "audio_tts": "Amy"}, {"x": 30.0, "y": 70, "text": "Tom", "audio_tts": "Tom"}, {"x": 53.0, "y": 70, "text": "Sam", "audio_tts": "Sam"}, {"x": 70.0, "y": 70, "text": "Ben", "audio_tts": "Ben"}, {"x": 88.0, "y": 70, "text": "Lily", "audio_tts": "Lily"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'text', replace($blk${"html": "<p>Посмотри на картинку. Прочитай предложения ниже и укажи, верно или неверно.</p><p><img src=\"@@MEDIA@@sm1/u2/t_toy_shelf.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'truefalse', replace($blk${"title": "Верно или неверно?", "statements": [{"text": "The ball is big.", "correct": true}, {"text": "The car is big.", "correct": false}, {"text": "The train is short.", "correct": false}, {"text": "The kite is old.", "correct": false}, {"text": "The doll is beautiful.", "correct": true}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "html": "<p>Ответь на вопросы:</p><ol><li>What’s your favourite toy?</li><li>What’s your favourite number?</li><li>What’s your favourite colour?</li><li>What’s your name?</li><li>How old are you?</li><li>What’s your sister’s/brother’s favourite toy?</li><li>What’s your sister’s/brother’s favourite number?</li><li>What’s your sister’s/brother’s favourite colour?</li><li>What’s your sister’s/brother’s name?</li><li>How old is your sister/brother?</li></ol><p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 13);
end
$mig$;
