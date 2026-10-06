-- Go Getter 1 · Final Test · Final Test
-- собрано tools/gg1_build.py --lesson final_test
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Final Test', 9
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Final Test');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Final Test';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Final Test', 'test',
         90, false, 0
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Final Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Final Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Final Test</h2><p>Это итоговый тест по всему курсу. Не торопись и внимательно слушай аудио!</p><h2 style=\"color:#d32f2f\">LISTENING</h2>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>LISTENING Part 1. Послушай аудио и выполни задание ниже.</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'hotspot', replace($blk${"title": "Послушай аудио выше и расставь предметы по местам", "mode": "label", "image": "@@MEDIA@@gg1/final/final_living_room.webp", "points": [{"x": 36.0, "y": 31.0, "text": "radio"}, {"x": 66.0, "y": 78.0, "text": "ball"}, {"x": 30.0, "y": 86.0, "text": "kite"}, {"x": 60.0, "y": 42.0, "text": "clock"}, {"x": 61.0, "y": 68.0, "text": "robot"}, {"x": 27.0, "y": 60.0, "text": "bag"}], "extras": []}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>LISTENING Part 2. Послушай и выбери верный ответ. Пример: What is the girl's name? — Lucy. How old is she? — 7.</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Послушай и выбери верный ответ", "questions": [{"q": "What is Lucy's friend's name?", "type": "single", "options": [{"text": "Alex"}, {"text": "Bob"}, {"text": "Mark"}], "correct": [0]}, {"q": "Which class are the two children in at school?", "type": "single", "options": [{"text": "6"}, {"text": "8"}, {"text": "7"}], "correct": [1]}, {"q": "How many dogs are there at Lucy's house?", "type": "single", "options": [{"text": "4"}, {"text": "2"}, {"text": "3"}], "correct": [2]}, {"q": "What's the name of Lucy's favourite dog?", "type": "single", "options": [{"text": "Socks"}, {"text": "Sockes"}, {"text": "Sock"}], "correct": [0]}, {"q": "How many fish has Lucy's friend got?", "type": "single", "options": [{"text": "20"}, {"text": "12"}, {"text": "11"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>LISTENING Part 3. Послушай аудио и выполни задания ниже.</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'quiz', replace($blk${"title": "Послушай аудио выше и выбери правильный ответ", "questions": [{"q": "What's Pat doing?", "type": "single", "options": [{"text": "reading a book"}, {"text": "playing football"}, {"text": "swimming"}], "correct": [2]}, {"q": "Which is May?", "type": "single", "options": [{"text": "the girl with long hair"}, {"text": "the girl with short hair"}, {"text": "the girl with glasses"}], "correct": [0]}, {"q": "Which is Nick's favourite ice-cream?", "type": "single", "options": [{"text": "lemon"}, {"text": "chocolate"}, {"text": "strawberry"}], "correct": [1]}, {"q": "What's Ben doing?", "type": "single", "options": [{"text": "riding a bike"}, {"text": "flying a kite"}, {"text": "playing tennis"}], "correct": [1]}, {"q": "Where's Kim's doll?", "type": "single", "options": [{"text": "on the bed"}, {"text": "under the table"}, {"text": "in the box"}], "correct": [2]}, {"q": "What's Dad doing?", "type": "single", "options": [{"text": "cooking"}, {"text": "sleeping"}, {"text": "washing the car"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<h2 style=\"color:#d32f2f\">READING AND WRITING</h2>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку и выбери: верно (YES) или неверно (NO)", "questions": [{"q": "These are grapes.", "type": "single", "options": [{"text": "YES"}, {"text": "NO"}], "correct": [0], "image": "@@MEDIA@@gg1/final/final_grapes.webp"}, {"q": "This is a house.", "type": "single", "options": [{"text": "YES"}, {"text": "NO"}], "correct": [1], "image": "@@MEDIA@@gg1/final/final_car.webp"}, {"q": "It is a clock.", "type": "single", "options": [{"text": "YES"}, {"text": "NO"}], "correct": [0], "image": "@@MEDIA@@gg1/u0/obj_clock.webp"}, {"q": "This is a sock.", "type": "single", "options": [{"text": "YES"}, {"text": "NO"}], "correct": [1], "image": "@@MEDIA@@gg1/final/final_boot.webp"}, {"q": "These are chairs.", "type": "single", "options": [{"text": "YES"}, {"text": "NO"}], "correct": [0], "image": "@@MEDIA@@gg1/final/final_chairs.webp"}, {"q": "It is a television.", "type": "single", "options": [{"text": "YES"}, {"text": "NO"}], "correct": [1], "image": "@@MEDIA@@gg1/final/final_radio.webp"}, {"q": "It is a dog.", "type": "single", "options": [{"text": "YES"}, {"text": "NO"}], "correct": [1], "image": "@@MEDIA@@gg1/u7/animal_cat.webp"}, {"q": "It is a spider.", "type": "single", "options": [{"text": "YES"}, {"text": "NO"}], "correct": [0], "image": "@@MEDIA@@gg1/u7/animal_spider.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку и выбери yes или no. Пример: There are two armchairs in the living room — YES. The big window is open — NO.", "questions": [{"q": "The man has got black hair and glasses.", "type": "single", "options": [{"text": "YES"}, {"text": "NO"}], "correct": [0], "image": "@@MEDIA@@gg1/final/final_family_room.webp"}, {"q": "There is a lamp on the bookcase.", "type": "single", "options": [{"text": "YES"}, {"text": "NO"}], "correct": [0], "image": "@@MEDIA@@gg1/final/final_family_room.webp"}, {"q": "Some of the children are singing.", "type": "single", "options": [{"text": "YES"}, {"text": "NO"}], "correct": [1], "image": "@@MEDIA@@gg1/final/final_family_room.webp"}, {"q": "The woman is holding some drinks.", "type": "single", "options": [{"text": "YES"}, {"text": "NO"}], "correct": [0], "image": "@@MEDIA@@gg1/final/final_family_room.webp"}, {"q": "The cat is sleeping under an armchair.", "type": "single", "options": [{"text": "YES"}, {"text": "NO"}], "correct": [0], "image": "@@MEDIA@@gg1/final/final_family_room.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"title": "Посмотри на картинку и собери слово из букв", "words": ["b", "u", "t", "t", "e", "r", "f", "l", "y"], "sentence": "b u t t e r f l y", "audio_tts": "butterfly", "image": "@@MEDIA@@gg1/u7/animal_butterfly.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'order', replace($blk${"title": "Посмотри на картинку и собери слово из букв", "words": ["j", "a", "c", "k", "e", "t"], "sentence": "j a c k e t", "audio_tts": "jacket", "image": "@@MEDIA@@gg1/u2/clothes_jacket.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'order', replace($blk${"title": "Посмотри на картинку и собери слово из букв", "words": ["k", "i", "t", "c", "h", "e", "n"], "sentence": "k i t c h e n", "audio_tts": "kitchen", "image": "@@MEDIA@@gg1/u3/room_kitchen.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'order', replace($blk${"title": "Посмотри на картинку и собери слово из букв", "words": ["w", "h", "a", "l", "e"], "sentence": "w h a l e", "audio_tts": "whale", "image": "@@MEDIA@@gg1/u7/animal_whale.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'order', replace($blk${"title": "Посмотри на картинку и собери слово из букв", "words": ["h", "o", "c", "k", "e", "y"], "sentence": "h o c k e y", "audio_tts": "hockey", "image": "@@MEDIA@@gg1/u8/sport_hockey.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/congrats_popper.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты прошёл весь курс Go Getter 1! 🎉</h3><p>Ты замечательный ученик. Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 15);
end
$mig$;
