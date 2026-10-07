-- Super Minds 1 · Unit 7 · Get dressed · Homework 7
-- собрано tools/sm1_build.py --lesson u7_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 7 · Get dressed', 7
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 7 · Get dressed');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 7 · Get dressed';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>👕 Привет, модник!</h2><p>Это последняя домашка перед тестом! Выполни все задания, чтобы хорошенько подготовиться!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку и прочитай слово. Правильно (True) или нет (False)?", "questions": [{"q": "Посмотри на картинку и прочитай слово. Правильно (True) или нет (False)?<br><b>shoes</b>", "type": "single", "image": "@@MEDIA@@sm1/u7/clothes_shoes.webp", "options": [{"text": "True"}, {"text": "False"}], "correct": [0]}, {"q": "<b>trousers</b>", "type": "single", "image": "@@MEDIA@@sm1/u7/clothes_jacket.webp", "options": [{"text": "True"}, {"text": "False"}], "correct": [1]}, {"q": "<b>skirt</b>", "type": "single", "image": "@@MEDIA@@sm1/u7/clothes_shorts.webp", "options": [{"text": "True"}, {"text": "False"}], "correct": [1]}, {"q": "<b>sweater</b>", "type": "single", "image": "@@MEDIA@@sm1/u7/clothes_sweater.webp", "options": [{"text": "True"}, {"text": "False"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'sort', replace($blk${"title": "Разложи одежду по группам: ноги 🦿, туловище 👕 или голова 🧢.", "groups": [{"name": "ноги 🦿", "items": [{"text": "shorts"}, {"text": "trousers"}, {"text": "jeans"}, {"text": "skirt"}, {"text": "socks"}, {"text": "shoes"}]}, {"name": "туловище 👕", "items": [{"text": "sweater"}, {"text": "jacket"}, {"text": "T-shirt"}]}, {"name": "голова 🧢", "items": [{"text": "baseball cap"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши this или these.", "text": "1. Do you like __these__ shoes?\n2. Do you like __this__ skirt?\n3. Do you like __these__ jeans?\n4. Do you like __this__ baseball cap?\n5. Do you like __these__ socks?\n6. Do you like __this__ jacket?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку и ответь на вопрос.", "questions": [{"q": "Посмотри на картинку и ответь на вопрос.<br>Is he wearing a green sweater?", "type": "single", "image": "@@MEDIA@@sm1/u7/char_boy_blue_sweater.webp", "options": [{"text": "Yes, she is."}, {"text": "No, she isn’t."}, {"text": "Yes, he is."}, {"text": "No, he isn’t."}], "correct": [3]}, {"q": "Is he wearing trousers?", "type": "single", "image": "@@MEDIA@@sm1/u7/char_boy_red_jacket.webp", "options": [{"text": "Yes, she is."}, {"text": "No, she isn’t."}, {"text": "Yes, he is."}, {"text": "No, he isn’t."}], "correct": [2]}, {"q": "Is she wearing a purple skirt?", "type": "single", "image": "@@MEDIA@@sm1/u7/char_girl_green_sweater.webp", "options": [{"text": "Yes, she is."}, {"text": "No, she isn’t."}, {"text": "Yes, he is."}, {"text": "No, he isn’t."}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'speaking', replace($blk${"title": "Что он/она носит? 🎤", "needs_review": true, "image": "@@MEDIA@@sm1/u7/kids_thumbs_up.webp", "html": "<p>Посмотри на картинку. Нажми на микрофон и расскажи: что он/она носит?</p><p><i>Пример: He’s wearing a blue jacket, black trousers and white shoes.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'exact_input', replace($blk${"items": [{"image": "@@MEDIA@@sm1/u7/clothes_jacket.webp", "prompt": "Дополнительное задание! Посмотри на картинку и напиши слово", "accept": ["jacket", "Jacket", "a jacket"], "audio_tts": "jacket"}, {"image": "@@MEDIA@@sm1/u7/clothes_skirt.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["skirt", "Skirt", "a skirt"], "audio_tts": "skirt"}, {"image": "@@MEDIA@@sm1/u7/clothes_socks.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["socks", "Socks"], "audio_tts": "socks"}, {"image": "@@MEDIA@@sm1/u7/clothes_tshirt.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["T-shirt", "t-shirt", "a T-shirt", "T shirt", "tshirt"], "audio_tts": "T-shirt"}, {"image": "@@MEDIA@@sm1/u7/clothes_trousers.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["trousers", "Trousers"], "audio_tts": "trousers"}, {"image": "@@MEDIA@@sm1/u7/clothes_cap.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["cap", "baseball cap", "Cap", "a cap"], "audio_tts": "cap"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант", "questions": [{"q": "Выбери правильный вариант:<br>___ he wearing a jacket?", "type": "single", "image": "@@MEDIA@@sm1/u7/char_boy_red_jacket.webp", "options": [{"text": "Is"}, {"text": "Are"}, {"text": "Do"}], "correct": [0]}, {"q": "She ___ wearing a green sweater.", "type": "single", "image": "@@MEDIA@@sm1/u7/char_girl_green_sweater.webp", "options": [{"text": "are"}, {"text": "is"}, {"text": "am"}], "correct": [1]}, {"q": "Is he wearing a red sweater? — No, he ___.", "type": "single", "image": "@@MEDIA@@sm1/u7/char_boy_blue_sweater.webp", "options": [{"text": "is"}, {"text": "isn’t"}, {"text": "aren’t"}], "correct": [1]}, {"q": "Is she wearing a skirt? — Yes, she ___.", "type": "single", "image": "@@MEDIA@@sm1/u7/char_girl_green_sweater.webp", "options": [{"text": "isn’t"}, {"text": "does"}, {"text": "is"}], "correct": [2]}, {"q": "He is wearing a blue ___.", "type": "single", "image": "@@MEDIA@@sm1/u7/char_boy_blue_sweater.webp", "options": [{"text": "sweater"}, {"text": "skirt"}, {"text": "dress"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_jump.webp\" alt=\"\" style=\"height:180px\"></p><h3>Молодец!</h3><p>Ты повторил всю одежду, this/these и Is he/she wearing.</p><p>Ты готов к тесту!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
