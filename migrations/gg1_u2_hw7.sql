-- Go Getter 1 · Unit 2 · My things · Homework 7
-- собрано tools/gg1_build.py --lesson u2_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 2 · My things', 2
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 2 · My things');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 2 · My things';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>На следующем занятии тебя ждёт очень интересный тест! Давай подготовимся к нему получше?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Найди лишнее слово и отметь его", "questions": [{"q": "T-shirt / boots / shoes", "type": "single", "options": [{"text": "boots"}, {"text": "T-shirt"}, {"text": "shoes"}], "correct": [1]}, {"q": "cool / fantastic / boring", "type": "single", "options": [{"text": "fantastic"}, {"text": "cool"}, {"text": "boring"}], "correct": [2]}, {"q": "backpack / top / dress", "type": "single", "options": [{"text": "backpack"}, {"text": "dress"}, {"text": "top"}], "correct": [0]}, {"q": "long / big / top", "type": "single", "options": [{"text": "long"}, {"text": "top"}, {"text": "big"}], "correct": [1]}, {"q": "jacket / skirt / coat", "type": "single", "options": [{"text": "coat"}, {"text": "jacket"}, {"text": "skirt"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'hotspot', replace($blk${"title": "Посмотри на картинку и соедини слова с предметами", "mode": "label", "image": "@@MEDIA@@gg1/u2/boy_skater.webp", "points": [{"x": 55.0, "y": 7.0, "text": "cap"}, {"x": 88.0, "y": 30.0, "text": "mobile phone"}, {"x": 76.0, "y": 38.0, "text": "shirt"}, {"x": 60.0, "y": 70.0, "text": "jeans"}, {"x": 78.0, "y": 92.0, "text": "trainers"}, {"x": 22.0, "y": 72.0, "text": "skateboard"}], "extras": []}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ответа", "questions": [{"q": "My shoes ___ too small.", "type": "single", "options": [{"text": "are"}, {"text": "is"}], "correct": [0]}, {"q": "___ T-shirt isn't big.", "type": "single", "options": [{"text": "These"}, {"text": "This"}], "correct": [1]}, {"q": "What ___ it?", "type": "single", "options": [{"text": "is"}, {"text": "are"}], "correct": [0]}, {"q": "___ are my brothers.", "type": "single", "options": [{"text": "That"}, {"text": "Those"}], "correct": [1]}, {"q": "Her boots ___ cool.", "type": "single", "options": [{"text": "are"}, {"text": "is"}], "correct": [0]}, {"q": "___ they your books?", "type": "single", "options": [{"text": "Is"}, {"text": "Are"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'sequence', replace($blk${"title": "Расставь предложения так, чтобы получился диалог", "items": [{"text": "Hello, I'm Benjamin. What's your name?"}, {"text": "Hi. I'm Jackie. I'm from England. Where are you from?"}, {"text": "I'm from England too. How old are you?"}, {"text": "Eleven. Are you 11 too?"}, {"text": "No, I'm not. I'm 12. What's your favourite book?"}, {"text": "Harry Potter, Book One."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'speaking', replace($blk${"title": "Моя любимая футболка 🎤", "html": "<p>Нажми на микрофон и опиши свою любимую футболку или топ.</p><p><i>Пример: This is my favourite top. It's blue with red squares, yellow triangles and green lines. I love it!</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'exact_input', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Впиши слова ⭐", "items": [{"prompt": "6 букв", "accept": ["jacket", "jacket", "Jacket"], "image": "@@MEDIA@@gg1/u2/clothes_jacket.webp", "audio_tts": "jacket"}, {"prompt": "5 букв", "accept": ["skirt", "skirt", "Skirt"], "image": "@@MEDIA@@gg1/u2/clothes_skirt.webp", "audio_tts": "skirt"}, {"prompt": "8 букв", "accept": ["trousers", "trousers", "Trousers"], "image": "@@MEDIA@@gg1/u2/clothes_trousers.webp", "audio_tts": "trousers"}, {"prompt": "6 букв", "accept": ["jumper", "jumper", "Jumper"], "image": "@@MEDIA@@gg1/u2/clothes_jumper.webp", "audio_tts": "jumper"}, {"prompt": "5 букв", "accept": ["scarf", "scarf", "Scarf"], "image": "@@MEDIA@@gg1/u2/clothes_scarf.webp", "audio_tts": "scarf"}, {"prompt": "9 букв", "accept": ["tracksuit", "tracksuit", "Tracksuit"], "image": "@@MEDIA@@gg1/u2/clothes_tracksuit.webp", "audio_tts": "tracksuit"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'match', replace($blk${"title": "Соедини ⭐", "pairs": [{"left_image": "@@MEDIA@@gg1/u2/adj_big_small.webp", "right": "big and small"}, {"left_image": "@@MEDIA@@gg1/u2/adj_long_short.webp", "right": "long and short"}, {"left_image": "@@MEDIA@@gg1/u2/adj_new_old.webp", "right": "new and old"}, {"left_image": "@@MEDIA@@gg1/u2/adj_cool_boring.webp", "right": "cool and boring"}, {"left_image": "@@MEDIA@@gg1/u2/adj_too_big.webp", "right": "too big"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'match', replace($blk${"title": "Соедини вопросы с ответами ⭐", "pairs": [{"left": "What's your name?", "right": "My name's Lucas."}, {"left": "How old are you?", "right": "I'm eleven."}, {"left": "Where are you from?", "right": "I'm from Spain."}, {"left": "What's your favourite music?", "right": "Rock, I think!"}, {"left": "Who's your favourite singer?", "right": "Alicia Keys."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/good_luck_clover.webp\" alt=\"\" style=\"height:180px\"></p><h3>У тебя отлично получилось! 🎉</h3><p>Уверена, ты справишься с тестом на все сто! Удачи!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9);
end
$mig$;
