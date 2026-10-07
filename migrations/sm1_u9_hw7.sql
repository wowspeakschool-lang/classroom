-- Super Minds 1 · Unit 9 · Holidays · Homework 7
-- собрано tools/sm1_build.py --lesson u9_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 9 · Holidays', 9
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 9 · Holidays');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 9 · Holidays';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! Как здорово, что ты открыл домашнее задание!</h2><p>Сегодня мы повторяем всё перед тестом: лексику, грамматику и не только! Ты справишься, я уверен!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Соедини фразы с картинкой: послушай и выбери, что прозвучало", "type": "single", "audio_tts": "catch a fish", "options": [{"text": "catch a fish"}, {"text": "paint a picture"}, {"text": "eat ice cream"}, {"text": "take a photo"}], "correct": [0]}, {"q": "Соедини фразы с картинкой: послушай и выбери, что прозвучало", "type": "single", "audio_tts": "paint a picture", "options": [{"text": "eat ice cream"}, {"text": "paint a picture"}, {"text": "take a photo"}, {"text": "listen to music"}], "correct": [1]}, {"q": "Соедини фразы с картинкой: послушай и выбери, что прозвучало", "type": "single", "audio_tts": "eat ice cream", "options": [{"text": "take a photo"}, {"text": "listen to music"}, {"text": "eat ice cream"}, {"text": "look for shells"}], "correct": [2]}, {"q": "Соедини фразы с картинкой: послушай и выбери, что прозвучало", "type": "single", "audio_tts": "take a photo", "options": [{"text": "listen to music"}, {"text": "look for shells"}, {"text": "read a book"}, {"text": "take a photo"}], "correct": [3]}, {"q": "Соедини фразы с картинкой: послушай и выбери, что прозвучало", "type": "single", "audio_tts": "listen to music", "options": [{"text": "listen to music"}, {"text": "look for shells"}, {"text": "read a book"}, {"text": "make a sandcastle"}], "correct": [0]}, {"q": "Соедини фразы с картинкой: послушай и выбери, что прозвучало", "type": "single", "audio_tts": "look for shells", "options": [{"text": "read a book"}, {"text": "look for shells"}, {"text": "make a sandcastle"}, {"text": "play the guitar"}], "correct": [1]}, {"q": "Соедини фразы с картинкой: послушай и выбери, что прозвучало", "type": "single", "audio_tts": "read a book", "options": [{"text": "make a sandcastle"}, {"text": "play the guitar"}, {"text": "read a book"}, {"text": "catch a fish"}], "correct": [2]}, {"q": "Соедини фразы с картинкой: послушай и выбери, что прозвучало", "type": "single", "audio_tts": "make a sandcastle", "options": [{"text": "play the guitar"}, {"text": "catch a fish"}, {"text": "paint a picture"}, {"text": "make a sandcastle"}], "correct": [3]}, {"q": "Соедини фразы с картинкой: послушай и выбери, что прозвучало", "type": "single", "audio_tts": "play the guitar", "options": [{"text": "play the guitar"}, {"text": "catch a fish"}, {"text": "paint a picture"}, {"text": "eat ice cream"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку. Правда или нет? Выбери True или False", "questions": [{"q": "The boy is reading a book.", "type": "single", "image": "@@MEDIA@@sm1/u9/hw7_boy_guitar.webp", "options": [{"text": "True ✅"}, {"text": "False ❌"}], "correct": [1]}, {"q": "The girl is listening to music.", "type": "single", "image": "@@MEDIA@@sm1/u9/hw7_girl_music.webp", "options": [{"text": "True ✅"}, {"text": "False ❌"}], "correct": [0]}, {"q": "The boy is catching a fish.", "type": "single", "image": "@@MEDIA@@sm1/u9/hw7_boy_fishing.webp", "options": [{"text": "True ✅"}, {"text": "False ❌"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски", "mode": "drag", "text": "1. Let’s __listen__ to music. – Good __idea__!\n2. Let’s paint a __picture__. – I’m not __sure__.\n3. Let’s __eat__ ice cream. – __Good__ idea!\n4. Let’s __catch__ a fish. – __Sorry__, I don’t want to.\n5. __Let’s__ look for __shells__. – Good idea!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный ответ.", "questions": [{"q": "Where’s the shell?", "type": "single", "options": [{"text": "They’re on the rocks."}, {"text": "It’s on the rocks."}], "correct": [1]}, {"q": "Where are the kites?", "type": "single", "options": [{"text": "They aren’t in the box. They’re on the bed."}, {"text": "It isn’t in the box. It’s on the bed."}], "correct": [0]}, {"q": "Where’s my hat?", "type": "single", "options": [{"text": "They aren’t in my bag. They’re on my head!"}, {"text": "It isn’t in my bag. It’s on my head!"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'speaking', replace($blk${"title": "Где что? 🎤", "needs_review": true, "image": "@@MEDIA@@sm1/u9/hw7_where_tiles.webp", "html": "<p>Посмотри на картинки. Ответь на вопросы — нажми на микрофон и запиши ответ голосом.</p><ol><li>Where is the apple?</li><li>Where are the frogs?</li><li>Where are the pencils?</li><li>Where is the frog?</li><li>Where are the apples?</li><li>Where is the pencil?</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился! 🏆</h3><p>Ты отлично подготовился к тесту! Увидимся на уроке! 👋</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6);
end
$mig$;
