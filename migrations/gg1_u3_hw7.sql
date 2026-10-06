-- Go Getter 1 · Unit 3 · My home · Homework 7
-- собрано tools/gg1_build.py --lesson u3_hw7
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
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Добро пожаловать в мир домашнего задания! Давай приступим к повторению.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски: there is / there are. Это могут быть вопросы, отрицания или утверждения", "mode": "type", "text": "1. __There is|There's|There’s__ a table in the kitchen. (+)\n2. __Is there__ a phone on the table? (?)\n3. __There aren't|There aren’t|There are not__ two beds in the bedroom. (−)\n4. __There is|There's|There’s__ a desk in the bedroom. (+)\n5. __There isn't|There isn’t|There is not__ a rat behind the door. (−)\n6. __Are there__ four people at home? (?)"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'order', replace($blk${"title": "Составь предложения из слов — расставь слова по порядку", "words": ["There", "isn't", "a ruler", "on", "the table."], "sentence": "There isn't a ruler on the table.", "audio_tts": "There isn't a ruler on the table."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"title": "Составь предложение", "words": ["Are", "there", "any", "students", "in", "the classroom?"], "sentence": "Are there any students in the classroom?", "audio_tts": "Are there any students in the classroom?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"title": "Составь предложение", "words": ["Is", "there", "a television", "in", "your bedroom?"], "sentence": "Is there a television in your bedroom?", "audio_tts": "Is there a television in your bedroom?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "Заверши диалог, используя there, isn't, a, any", "mode": "drag", "image": "@@MEDIA@@gg1/u3/photo_modern_house.webp", "text": "Sally: This is my new house. There's __a__ big garden.\nMarina: Are there __any__ trees in the garden?\nSally: No, there aren't __any__ trees. The garden is too small for trees. But the house is big.\nMarina: Is your bedroom big?\nSally: Yes, it is. There's a bed, a desk and a chair. __There__ are four posters on the wall too.\nMarina: Is there __a__ games console?\nSally: No, there __isn't__, but there's a computer!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'gaps', replace($blk${"title": "Вставь пропущенные слова в диалог", "mode": "drag", "image": "@@MEDIA@@gg1/u3/scene_guests_door.webp", "text": "A: Hello. Please __come__ in.\nB: Thank you.\nA: __Would__ you like a sandwich?\nB: Yes, __please__. Where's the bathroom, please?\nA: It's __upstairs__. It's next to Andrew's bedroom. __Let__ me show you.\nB: Thanks."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'task', replace($blk${"title": "Задание для самых-самых ⭐", "needs_review": true, "image": "@@MEDIA@@gg1/u3/kids_bedroom.webp", "html": "<p>Расскажи нам про комнату своей мечты! Напиши 4–5 предложений.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'exact_input', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Расшифруй и впиши слова ⭐", "items": [{"prompt": "B M O D E O R", "accept": ["bedroom", "Bedroom"], "image": "@@MEDIA@@gg1/u3/room_bedroom.webp", "audio_tts": "bedroom"}, {"prompt": "E C T N K I H", "accept": ["kitchen", "Kitchen"], "image": "@@MEDIA@@gg1/u3/room_kitchen.webp", "audio_tts": "kitchen"}, {"prompt": "N E D R A G", "accept": ["garden", "Garden"], "image": "@@MEDIA@@gg1/u3/room_garden.webp", "audio_tts": "garden"}, {"prompt": "I R C A R H M A", "accept": ["armchair", "Armchair"], "image": "@@MEDIA@@gg1/u3/furn_armchair.webp", "audio_tts": "armchair"}, {"prompt": "F G R I D E", "accept": ["fridge", "Fridge"], "image": "@@MEDIA@@gg1/u3/furn_fridge.webp", "audio_tts": "fridge"}, {"prompt": "A R R D O W E B", "accept": ["wardrobe", "Wardrobe"], "image": "@@MEDIA@@gg1/u3/furn_wardrobe.webp", "audio_tts": "wardrobe"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку и выбери правильный вариант ⭐", "questions": [{"q": "Where is the trophy? It's ___ the shelf.", "type": "single", "options": [{"text": "under"}, {"text": "in front of"}, {"text": "on"}, {"text": "behind"}, {"text": "next to"}, {"text": "in"}], "correct": [2], "image": "@@MEDIA@@gg1/u3/prepositions_living_room.webp"}, {"q": "Where is the lamp? It's ___ the sofa.", "type": "single", "options": [{"text": "on"}, {"text": "behind"}, {"text": "under"}, {"text": "next to"}, {"text": "in"}, {"text": "in front of"}], "correct": [3], "image": "@@MEDIA@@gg1/u3/prepositions_living_room.webp"}, {"q": "Where is the fish bowl? It's ___ the small table.", "type": "single", "options": [{"text": "in front of"}, {"text": "under"}, {"text": "next to"}, {"text": "behind"}, {"text": "on"}, {"text": "in"}], "correct": [4], "image": "@@MEDIA@@gg1/u3/prepositions_living_room.webp"}, {"q": "Where are the dogs? They're ___ the coffee table.", "type": "single", "options": [{"text": "in front of"}, {"text": "on"}, {"text": "behind"}, {"text": "in"}, {"text": "next to"}, {"text": "under"}], "correct": [5], "image": "@@MEDIA@@gg1/u3/prepositions_living_room.webp"}, {"q": "Where is the plane? It's ___ the box.", "type": "single", "options": [{"text": "in"}, {"text": "next to"}, {"text": "under"}, {"text": "in front of"}, {"text": "on"}, {"text": "behind"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/prepositions_living_room.webp"}, {"q": "Where is the window? It's ___ the sofa.", "type": "single", "options": [{"text": "next to"}, {"text": "behind"}, {"text": "on"}, {"text": "in"}, {"text": "in front of"}, {"text": "under"}], "correct": [1], "image": "@@MEDIA@@gg1/u3/prepositions_living_room.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ⭐", "questions": [{"q": "___ a TV in your bedroom?", "type": "single", "options": [{"text": "Are there"}, {"text": "Is there"}], "correct": [1]}, {"q": "___ any plants in the kitchen?", "type": "single", "options": [{"text": "Are there"}, {"text": "Is there"}], "correct": [0]}, {"q": "There ___ any posters on the wall.", "type": "single", "options": [{"text": "isn't"}, {"text": "aren't"}], "correct": [1]}, {"q": "There ___ a lamp on the desk.", "type": "single", "options": [{"text": "isn't"}, {"text": "aren't"}], "correct": [0]}, {"q": "Is there a garden? — No, there ___.", "type": "single", "options": [{"text": "aren't"}, {"text": "isn't"}], "correct": [1]}, {"q": "Are there two bedrooms? — Yes, there ___.", "type": "single", "options": [{"text": "are"}, {"text": "is"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/good_luck_clover.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты здорово потрудился! 🎉</h3><p>До скорой встречи в нашей World of Homework! Удачи на тесте!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11);
end
$mig$;
