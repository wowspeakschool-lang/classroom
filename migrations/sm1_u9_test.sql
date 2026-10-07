-- Super Minds 1 · Unit 9 · Holidays · Unit 9 Test
-- собрано tools/sm1_build.py --lesson u9_test
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
  select v_unit, 'Unit 9 Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Unit 9 Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Unit 9 Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'exact_input', replace($blk${"items": [{"prompt": "Напиши по-английски: поймать рыбу", "accept": ["catch a fish"], "audio_tts": "catch a fish"}, {"prompt": "Напиши по-английски: рисовать картину", "accept": ["paint a picture"], "audio_tts": "paint a picture"}, {"prompt": "Напиши по-английски: есть мороженое", "accept": ["eat ice cream"], "audio_tts": "eat ice cream"}, {"prompt": "Напиши по-английски: фотографировать", "accept": ["take a photo"], "audio_tts": "take a photo"}, {"prompt": "Напиши по-английски: слушать музыку", "accept": ["listen to music"], "audio_tts": "listen to music"}, {"prompt": "Напиши по-английски: искать ракушки", "accept": ["look for shells"], "audio_tts": "look for shells"}, {"prompt": "Напиши по-английски: читать книгу", "accept": ["read a book"], "audio_tts": "read a book"}, {"prompt": "Напиши по-английски: строить замок из песка", "accept": ["make a sandcastle"], "audio_tts": "make a sandcastle"}, {"prompt": "Напиши по-английски: играть на гитаре", "accept": ["play the guitar"], "audio_tts": "play the guitar"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с картинками", "pairs": [{"left_image": "@@MEDIA@@sm1/u9/act_paint_picture.webp", "right": "paint a picture", "right_audio_tts": "paint a picture"}, {"left_image": "@@MEDIA@@sm1/u9/act_listen_music.webp", "right": "listen to music", "right_audio_tts": "listen to music"}, {"left_image": "@@MEDIA@@sm1/u9/act_catch_fish.webp", "right": "catch a fish", "right_audio_tts": "catch a fish"}, {"left_image": "@@MEDIA@@sm1/u9/act_take_photo.webp", "right": "take a photo", "right_audio_tts": "take a photo"}, {"left_image": "@@MEDIA@@sm1/u9/act_look_shells.webp", "right": "look for shells", "right_audio_tts": "look for shells"}, {"left_image": "@@MEDIA@@sm1/u9/act_make_sandcastle.webp", "right": "make a sandcastle", "right_audio_tts": "make a sandcastle"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: Let's listen to music!<br>B: ___ idea.", "type": "single", "options": [{"text": "No"}, {"text": "Good"}, {"text": "Thanks"}], "correct": [1], "image": "@@MEDIA@@sm1/u9/test_listen_music.webp"}, {"q": "A: Let's paint a picture!<br>B: I'm not ___.", "type": "single", "options": [{"text": "sure"}, {"text": "like it"}, {"text": "good idea"}], "correct": [0], "image": "@@MEDIA@@sm1/u9/test_palette.webp"}, {"q": "A: Where's the book?<br>B: ___ under the bed.", "type": "single", "options": [{"text": "It"}, {"text": "They are"}, {"text": "It's"}], "correct": [2], "image": "@@MEDIA@@sm1/u9/test_book.webp"}, {"q": "A: Let's look for shells!<br>B: Sorry, I ___.", "type": "single", "options": [{"text": "don't"}, {"text": "want to"}, {"text": "don't want to"}], "correct": [2], "image": "@@MEDIA@@sm1/u9/test_girl_bucket.webp"}, {"q": "A: Where are the birds?<br>B: ___ in the shower.", "type": "single", "options": [{"text": "They"}, {"text": "They are"}, {"text": "They is"}], "correct": [1], "image": "@@MEDIA@@sm1/u9/test_birds.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"words": ["Where", "is", "the", "dog?"], "sentence": "Where is the dog?", "audio_tts": "Where is the dog?", "image": "@@MEDIA@@sm1/u9/test_dog.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"words": ["Where", "are", "your", "pink shoes?"], "sentence": "Where are your pink shoes?", "audio_tts": "Where are your pink shoes?", "image": "@@MEDIA@@sm1/u9/test_pink_shoes.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["The blue", "crocodiles", "are", "in", "the bathroom."], "sentence": "The blue crocodiles are in the bathroom.", "audio_tts": "The blue crocodiles are in the bathroom.", "image": "@@MEDIA@@sm1/u9/test_blue_crocodile.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["Let's", "take", "a", "photo!"], "sentence": "Let's take a photo!", "audio_tts": "Let's take a photo!", "image": "@@MEDIA@@sm1/u9/test_selfie.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["They", "are", "on", "my head."], "sentence": "They are on my head.", "audio_tts": "They are on my head."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'video', replace($blk${"title": "Послушай аудио: Бен и его семья проводят выходной на пляже", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'quiz', replace($blk${"title": "Послушай аудио и выбери правильные ответы на вопросы", "questions": [{"q": "What does Ben want to do?", "type": "single", "options": [{"text": "swim in the sea"}, {"text": "make a sandcastle"}, {"text": "paint a picture"}], "correct": [1]}, {"q": "Where is the bucket?", "type": "single", "options": [{"text": "in the bag"}, {"text": "on the chair"}, {"text": "under the towel"}], "correct": [2]}, {"q": "Where are the shells?", "type": "single", "options": [{"text": "in the bag"}, {"text": "under the towel"}, {"text": "on the chair"}], "correct": [0]}, {"q": "What is Dad doing?", "type": "single", "options": [{"text": "eating ice cream"}, {"text": "listening to music"}, {"text": "catching a fish"}], "correct": [2]}, {"q": "What is Grandma doing?", "type": "single", "options": [{"text": "taking a photo"}, {"text": "reading a book"}, {"text": "playing in the sand"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p>Прочитай открытку Эммы. Потом впиши в пропуски недостающие слова — <b>только ОДНО слово</b> в каждый пропуск.</p><p><img src=\"@@MEDIA@@sm1/u9/test_postcard.webp\" alt=\"Emma’s Postcard\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'gaps', replace($blk${"title": "Прочитай текст и впиши недостающее слово в пропуски. Только ОДНО слово.", "mode": "type", "text": "1. Emma and Max __swim__ in the sea every morning.\n2. Emma’s shells are in a box __on__ her table.\n3. Mum is __under__ the umbrella.\n4. Max is __painting__ a picture of the sea.\n5. Tomorrow Emma wants to __read__ a book."}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK · Part 1 🎤", "needs_review": true, "image": "@@MEDIA@@sm1/u9/test_beach_scene.webp", "html": "<p>Посмотри на картинку и ответь на вопросы:</p><ol><li>Where are the shells?</li><li>Where is the sandcastle?</li><li>Where is the big boat?</li><li>Where is the bird?</li><li>Where is the snail?</li><li>Where are the fish?</li><li>Where is the kite?</li></ol><p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK · Part 2 🎤", "needs_review": true, "html": "<p>Выбери свои любимые занятия (3–4) и предложи ими заняться.</p><p><i>For example:<br>Let’s fly a kite.<br>Let’s paint a picture.<br>Let’s catch the fish.</i></p><p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 13);
end
$mig$;
