-- Go Getter 1 · Unit 3 · My home · Homework 3
-- собрано tools/gg1_build.py --lesson u3_hw3
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
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет-привет! 👋</h2><p>Наше путешествие по стране ДЗ продолжается! Давай начнём нашу домашнюю работу!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u3/card_there_isnt_questions.webp\" alt=\"There isn't / There aren't / Questions\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'video', replace($blk${"title": "Посмотри видео и вспомни, о чём мы с тобой узнали на уроке!", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку с урока в стране ДЗ и выбери правильные ответы", "questions": [{"q": "___ seven students in the classroom.", "type": "single", "options": [{"text": "There is"}, {"text": "There are"}], "correct": [1], "image": "@@MEDIA@@gg1/u3/classroom_scene.webp"}, {"q": "___ a teacher in the classroom.", "type": "single", "options": [{"text": "There is"}, {"text": "There are"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/classroom_scene.webp"}, {"q": "___ a board in the classroom.", "type": "single", "options": [{"text": "There are"}, {"text": "There is"}], "correct": [1], "image": "@@MEDIA@@gg1/u3/classroom_scene.webp"}, {"q": "___ two tables in the classroom.", "type": "single", "options": [{"text": "There are"}, {"text": "There is"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/classroom_scene.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку и выбери: are, is, aren't или isn't", "questions": [{"q": "There ___ 2 bikes in the picture.", "type": "single", "options": [{"text": "aren't"}, {"text": "isn't"}, {"text": "are"}, {"text": "is"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/kids_room_two_beds.webp"}, {"q": "There ___ four pencils in the picture.", "type": "single", "options": [{"text": "is"}, {"text": "are"}, {"text": "isn't"}, {"text": "aren't"}], "correct": [1], "image": "@@MEDIA@@gg1/u3/kids_room_two_beds.webp"}, {"q": "There ___ three cushions on the bed.", "type": "single", "options": [{"text": "isn't"}, {"text": "is"}, {"text": "aren't"}, {"text": "are"}], "correct": [2], "image": "@@MEDIA@@gg1/u3/kids_room_two_beds.webp"}, {"q": "There ___ a teddy bear.", "type": "single", "options": [{"text": "isn't"}, {"text": "are"}, {"text": "aren't"}, {"text": "is"}], "correct": [3], "image": "@@MEDIA@@gg1/u3/kids_room_two_beds.webp"}, {"q": "There ___ a dog under the table.", "type": "single", "options": [{"text": "isn't"}, {"text": "aren't"}, {"text": "is"}, {"text": "are"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/kids_room_two_beds.webp"}, {"q": "There ___ a rabbit on the bed.", "type": "single", "options": [{"text": "is"}, {"text": "isn't"}, {"text": "are"}, {"text": "aren't"}], "correct": [1], "image": "@@MEDIA@@gg1/u3/kids_room_two_beds.webp"}, {"q": "There ___ two computers on the desk.", "type": "single", "options": [{"text": "are"}, {"text": "is"}, {"text": "aren't"}, {"text": "isn't"}], "correct": [2], "image": "@@MEDIA@@gg1/u3/kids_room_two_beds.webp"}, {"q": "There ___ three posters on the wall.", "type": "single", "options": [{"text": "isn't"}, {"text": "aren't"}, {"text": "is"}, {"text": "are"}], "correct": [3], "image": "@@MEDIA@@gg1/u3/kids_room_two_beds.webp"}, {"q": "There ___ four books on the shelf.", "type": "single", "options": [{"text": "are"}, {"text": "is"}, {"text": "isn't"}, {"text": "aren't"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/kids_room_two_beds.webp"}, {"q": "There ___ two presents on the bed.", "type": "single", "options": [{"text": "isn't"}, {"text": "aren't"}, {"text": "is"}, {"text": "are"}], "correct": [1], "image": "@@MEDIA@@gg1/u3/kids_room_two_beds.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'task', replace($blk${"title": "Задание для самых-самых ⭐", "needs_review": true, "image": "@@MEDIA@@gg1/u3/two_living_rooms.webp", "html": "<p>Посмотри на картинку, задай вопросы и напиши ответы (5–6 предложений).</p><p><i>Пример: Is there a dog in picture 2? — No, there isn't.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'gaps', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Вставь isn't или aren't ⭐", "mode": "drag", "text": "1. There __isn't__ a dog in my bedroom.\n2. There __aren't__ any plants in the kitchen.\n3. There __isn't__ a TV in the bathroom.\n4. There __aren't__ any chairs in the garden.\n5. There __isn't__ a car in the garage.\n6. There __aren't__ any books on the desk."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["Is", "there", "a", "sofa", "in", "the", "living", "room?"], "sentence": "Is there a sofa in the living room?", "audio_tts": "Is there a sofa in the living room?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["There", "aren't", "any", "posters", "on", "the", "wall."], "sentence": "There aren't any posters on the wall.", "audio_tts": "There aren't any posters on the wall."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["Are", "there", "any", "chairs", "in", "the", "kitchen?"], "sentence": "Are there any chairs in the kitchen?", "audio_tts": "Are there any chairs in the kitchen?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:180px\"></p><h3>Добро пожаловать во вторую часть! 👋</h3><p>Давай с тобой вспомним сначала There is / There are. Расставь слова по порядку, чтобы получились целые предложения!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'order', replace($blk${"title": "Составь предложение", "words": ["There", "are", "four books", "on", "the shelf."], "sentence": "There are four books on the shelf.", "audio_tts": "There are four books on the shelf."}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'order', replace($blk${"title": "Составь предложение", "words": ["Where", "is", "the living room?"], "sentence": "Where is the living room?", "audio_tts": "Where is the living room?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'order', replace($blk${"title": "Составь предложение", "words": ["It", "is", "next to", "the bathroom."], "sentence": "It is next to the bathroom.", "audio_tts": "It is next to the bathroom."}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'order', replace($blk${"title": "Составь предложение", "words": ["There", "is", "my bedroom."], "sentence": "There is my bedroom.", "audio_tts": "There is my bedroom."}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'order', replace($blk${"title": "Составь предложение", "words": ["Is", "there", "a garden", "in", "the house?"], "sentence": "Is there a garden in the house?", "audio_tts": "Is there a garden in the house?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 15),
    (v_lesson, 'video', replace($blk${"title": "Посмотри видео про дом Итана", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 16),
    (v_lesson, 'task', replace($blk${"title": "Посмотри видео и ответь на вопросы ✍", "needs_review": true, "html": "<ol><li>What is there in their living room?</li><li>Is there a kitchen?</li><li>What is there in Ethan's bedroom?</li><li>What rooms are there in the house?</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 17),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку и выбери: верно или неверно", "questions": [{"q": "There is a bed.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/messy_bedroom.webp"}, {"q": "There are books.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0]}, {"q": "There is a TV.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [1]}, {"q": "There is a computer.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0]}, {"q": "There is a desk in the room.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 18),
    (v_lesson, 'speaking', replace($blk${"title": "Моя комната 🎤", "image": "@@MEDIA@@gg1/u3/bedroom_rocket.webp", "html": "<p>Нажми на микрофон и расскажи, что есть у тебя в комнате.</p><p><i>Например: There is a bed. There are 2 chairs.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 19),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ну что же! Держи свой приз и до скорых встреч! 🎉</h3><p>Мы с тобой хорошо постарались!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 20);
end
$mig$;
