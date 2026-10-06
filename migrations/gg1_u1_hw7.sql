-- Go Getter 1 · Unit 1 · Family and friends · Homework 7
-- собрано tools/gg1_build.py --lesson u1_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 1 · Family and friends', 1
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 1 · Family and friends');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 1 · Family and friends';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>На следующем занятии тебя ждёт очень интересный тест. А сейчас давай повторим то, что мы прошли?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'match', replace($blk${"title": "Найди пару", "pairs": [{"left": "mum", "right": "dad"}, {"left": "aunt", "right": "uncle"}, {"left": "mother", "right": "father"}, {"left": "brother", "right": "sister"}, {"left": "son", "right": "daughter"}, {"left": "granny", "right": "grandad"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'exact_input', replace($blk${"title": "Посмотри на картинку и впиши недостающее слово целиком", "items": [{"prompt": "She is from P….", "accept": ["Poland", "poland"], "image": "@@MEDIA@@gg1/u1/she_poland.webp", "audio_tts": "She is from Poland."}, {"prompt": "He is in the g….", "accept": ["garden"], "image": "@@MEDIA@@gg1/u1/he_garden.webp", "audio_tts": "He is in the garden."}, {"prompt": "She is A….", "accept": ["American", "american"], "image": "@@MEDIA@@gg1/u1/she_american.webp", "audio_tts": "She is American."}, {"prompt": "They are at s….", "accept": ["school"], "image": "@@MEDIA@@gg1/u1/they_school.webp", "audio_tts": "They are at school."}, {"prompt": "Paris is in F….", "accept": ["France", "france"], "image": "@@MEDIA@@gg1/u1/place_paris.webp", "audio_tts": "Paris is in France."}, {"prompt": "She's at h….", "accept": ["home"], "image": "@@MEDIA@@gg1/u1/place_home.webp", "audio_tts": "She's at home."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши положительную (+) или отрицательную (−) форму глагола to be. Используй полные формы, не сокращения", "mode": "type", "text": "My best friends __are__ Maya and Jane. (+)\nMaya __is__ Italian. (+)\nJane and I __are not__ Italian. (−)\nWe __are__ from the UK. (+)\nI __am not__ in the UK in this photo. (−)"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски словами из списка", "mode": "drag", "text": "A: Jack, __this__ __is__ my friend, Harry.\nB: __Hi__, Harry. __Nice__ to meet you.\nC: Hi, Jack. Nice to __meet__ you __too__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ответа", "questions": [{"q": "This is Jack, and this is ___ cousin.", "type": "single", "options": [{"text": "her"}, {"text": "Jack"}, {"text": "Jack's"}], "correct": [2]}, {"q": "This is Clara, and this is ___ best friend, Nadia.", "type": "single", "options": [{"text": "her"}, {"text": "Nadia's"}, {"text": "his"}], "correct": [0]}, {"q": "Hi, Mum! This is ___ best friend, Nina.", "type": "single", "options": [{"text": "his"}, {"text": "my"}, {"text": "your"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'speaking', replace($blk${"title": "Расскажи о себе 🎤", "html": "<p>Нажми на микрофон и расскажи о себе: имя, возраст, откуда ты, твоя семья.</p><p><i>Пример: Hi! I'm Anna. I'm ten years old. I'm from Poland. I'm Polish. This is my family: my mum, my dad and my brother. My granny is Spanish. We're in the park today.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'hotspot', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Это семейное древо Марка. Кто они для Марка? ⭐", "mode": "label", "image": "@@MEDIA@@gg1/u1/tree_mark.webp", "points": [{"x": 45.0, "y": 70.0, "text": "grandfather"}, {"x": 67.0, "y": 70.0, "text": "grandmother"}, {"x": 33.0, "y": 32.0, "text": "father"}, {"x": 6.0, "y": 50.0, "text": "mother"}, {"x": 58.0, "y": 32.0, "text": "uncle"}, {"x": 68.0, "y": 48.0, "text": "aunt"}, {"x": 80.0, "y": 15.0, "text": "cousin"}], "extras": ["brother", "son"]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ⭐", "questions": [{"q": "My dad ___ a doctor.", "type": "single", "options": [{"text": "is"}, {"text": "am"}, {"text": "are"}], "correct": [0]}, {"q": "I ___ from Poland.", "type": "single", "options": [{"text": "is"}, {"text": "am"}, {"text": "are"}], "correct": [1]}, {"q": "Tom and Ben ___ brothers.", "type": "single", "options": [{"text": "is"}, {"text": "am"}, {"text": "are"}], "correct": [2]}, {"q": "Her name ___ Sophie.", "type": "single", "options": [{"text": "is"}, {"text": "are"}, {"text": "am"}], "correct": [0]}, {"q": "We ___ in the garden.", "type": "single", "options": [{"text": "is"}, {"text": "are"}, {"text": "am"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'quiz', replace($blk${"title": "И ещё раз: выбери правильный вариант ⭐", "questions": [{"q": "I ___ eleven. I'm ten.", "type": "single", "options": [{"text": "isn't"}, {"text": "aren't"}, {"text": "am not"}], "correct": [2]}, {"q": "My aunt ___ British. She's Italian.", "type": "single", "options": [{"text": "isn't"}, {"text": "am not"}, {"text": "aren't"}], "correct": [0]}, {"q": "We ___ at school today.", "type": "single", "options": [{"text": "isn't"}, {"text": "aren't"}, {"text": "am not"}], "correct": [1]}, {"q": "The dog ___ in the garden.", "type": "single", "options": [{"text": "aren't"}, {"text": "am not"}, {"text": "isn't"}], "correct": [2]}, {"q": "My cousins ___ from China.", "type": "single", "options": [{"text": "aren't"}, {"text": "am not"}, {"text": "isn't"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/good_luck_clover.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа! 🎉</h3><p>Удачи на тесте! Bye!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
