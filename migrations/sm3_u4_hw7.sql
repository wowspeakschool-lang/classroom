-- Super Minds 3 · Unit 4 · In the town · Homework 7
-- собрано tools/sm3_build.py --lesson u4_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 4 · In the town', 4
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 4 · In the town');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 4 · In the town';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>HELLO! Добро пожаловать в домашнее задание!</h2><p>Сегодня мы повторим с тобой слова, которые ты изучал на уроке!</p><p>Готов начать тренироваться?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'match', replace($blk${"title": "Внимательно посмотри на картинки и соедини слова с подходящими изображениями", "pairs": [{"left_image": "@@MEDIA@@sm3/u4/tower_lighthouse.webp", "right": "lighthouse", "right_audio_tts": "lighthouse"}, {"left_image": "@@MEDIA@@sm3/u4/tower_skyscraper.webp", "right": "skyscraper", "right_audio_tts": "skyscraper"}, {"left_image": "@@MEDIA@@sm3/u4/tower_control.webp", "right": "airport tower", "right_audio_tts": "airport tower"}, {"left_image": "@@MEDIA@@sm3/u4/tower_clock.webp", "right": "clock tower", "right_audio_tts": "clock tower"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"title": "МОЛОДЕЦ! Давай ещё потренируемся. Прочитай описание и выбери подходящее здание", "pairs": [{"left": "It’s very tall and old. It shows the time.", "right": "clock tower", "right_audio_tts": "clock tower"}, {"left": "People can check the traffic in the sky there.", "right": "airport tower", "right_audio_tts": "airport tower"}, {"left": "It keeps boats safe.", "right": "lighthouse", "right_audio_tts": "lighthouse"}, {"left": "It’s very tall. People work in offices there.", "right": "skyscraper", "right_audio_tts": "skyscraper"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"html": "<h3>УРА! ОСТАЛОСЬ ПОСЛЕДНЕЕ ЗАДАНИЕ! ВНИМАТЕЛЬНО ПРОЧИТАЙ ЕГО!</h3><p>Which tall buildings do you want to visit? Why? Write sentences.</p><p><i>Например: I want to visit a clock tower so that I can see how big the clock in it is.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'task', replace($blk${"title": "Напиши, какие места ты бы хотел посетить! Почему?", "needs_review": true, "html": "<p>Внимательно посмотри на пример выше и приступай к заданию!</p><p>Не забудь показать свой текст учителю на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты на финишной прямой! Остался последний рывок!</h3><p>Сегодня мы повторим всё, что ты изучил :) ПОЕХАЛИ!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши above, near, below, opposite, next to, in front of", "image": "@@MEDIA@@sm3/u4/prep_cat_below_shelf.webp", "text": "The cat is __below__ the shelf."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши above, near, below, opposite, next to, in front of", "image": "@@MEDIA@@sm3/u4/prep_ball_above_table.webp", "text": "The ball is __above__ the table."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши above, near, below, opposite, next to, in front of", "image": "@@MEDIA@@sm3/u4/prep_teddy_next_to_ball.webp", "text": "The bear is __next to__ the ball."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши above, near, below, opposite, next to, in front of", "image": "@@MEDIA@@sm3/u4/prep_elephant_in_front_of_chair.webp", "text": "The elephant is __in front of__ the chair."}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши above, near, below, opposite, next to, in front of", "image": "@@MEDIA@@sm3/u4/prep_mouse_near_tv.webp", "text": "The mouse is __near__ the TV."}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши above, near, below, opposite, next to, in front of", "image": "@@MEDIA@@sm3/u4/prep_cats_opposite.webp", "text": "The white cat is __opposite__ the grey cat."}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'text', replace($blk${"html": "<h3>SUPER! С первым заданием ты справился!</h3><p>Теперь давай вспомним конструкцию <b>to be going to</b>. Сделай задание ниже!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку и выбери, куда и зачем он идёт", "questions": [{"q": "1. Where is he going and why?", "type": "single", "image": "@@MEDIA@@sm3/u4/going_cinema.webp", "options": [{"text": "He’s going to the cinema to watch a film."}, {"text": "He’s going to the library to read a book."}, {"text": "He’s going to the market square to buy apples."}], "correct": [0]}, {"q": "2. Where is she going and why?", "type": "single", "image": "@@MEDIA@@sm3/u4/going_library.webp", "options": [{"text": "She’s going to the library to borrow a book."}, {"text": "She’s going to the café to have a milkshake."}, {"text": "She’s going to the sports centre to go swimming."}], "correct": [0]}, {"q": "3. Where are they going and why?", "type": "single", "image": "@@MEDIA@@sm3/u4/going_sports_centre.webp", "options": [{"text": "They’re going to the sports centre to go swimming."}, {"text": "They’re going to the supermarket to buy some bread."}, {"text": "They’re going to the cinema to watch a film."}], "correct": [0]}, {"q": "4. Where is he going and why?", "type": "single", "image": "@@MEDIA@@sm3/u4/going_cafe.webp", "options": [{"text": "He’s going to the café to have a milkshake."}, {"text": "He’s going to the bank to get some money."}, {"text": "He’s going to the library to borrow a book."}], "correct": [0]}, {"q": "5. Where is she going and why?", "type": "single", "image": "@@MEDIA@@sm3/u4/going_supermarket.webp", "options": [{"text": "She’s going to the supermarket to do the shopping."}, {"text": "She’s going to the funfair to have fun."}, {"text": "She’s going to the café to have a milkshake."}], "correct": [0]}, {"q": "6. Where are they going and why?", "type": "single", "image": "@@MEDIA@@sm3/u4/going_market.webp", "options": [{"text": "They’re going to the market square to buy a present."}, {"text": "They’re going to the bus station to take a bus."}, {"text": "They’re going to the sports centre to play football."}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'text', replace($blk${"html": "<h3>Ты хорошо справляешься!</h3><p>А теперь посмотри на картинку ниже! Какие места изображены на ней?</p><p><img src=\"@@MEDIA@@sm3/u4/scene_town_prepositions.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'task', replace($blk${"title": "Посмотри на картинку ещё раз и опиши её!", "needs_review": true, "html": "<p>Напиши 4–5 предложений о том, где что находится.</p><p><i>Например: The cinema is next to the sports centre …</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 15),
    (v_lesson, 'task', replace($blk${"title": "Напиши свой диалог — дополнительное задание", "needs_review": true, "html": "<p>Мы почти на финишной прямой. Посмотри внимательно на карту города выше и на диалог ниже! Попробуй написать такой же диалог, используя свои имена и слова.</p><p><i>Vic: Hi, Daisy! I’m in town, next to the school. I’m looking for the new café. Can you tell me where it is?<br>Daisy: No problem! Can you see the sports centre? The café is next to it, opposite the bus station.<br>Vic: Oh, I know! It’s near the cinema.<br>Daisy: That’s right!<br>Vic: Thank you!</i></p><p>Это задание дополнительное, но добавит 3 балла к контрольной работе в конце юнита! ;)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 16),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Good Job! Ты большой молодец!</h3><p>Теперь ты точно готов к тесту! Желаю удачи — у тебя обязательно всё получится!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 17);
end
$mig$;
