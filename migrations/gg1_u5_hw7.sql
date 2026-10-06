-- Go Getter 1 · Unit 5 · I can do it · Homework 7
-- собрано tools/gg1_build.py --lesson u5_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 5 · I can do it', 5
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 5 · I can do it');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 5 · I can do it';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Рада тебя видеть на домашнем задании! Сегодня ты проверишь, как хорошо ты запомнил материал Unit 5. Готов? Поехали! 🚀</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'exact_input', replace($blk${"title": "Что они умеют делать? Напиши глаголы действия", "items": [{"prompt": "Какое это действие?", "accept": ["fly", "Fly"], "image": "@@MEDIA@@gg1/u5/verb_fly.webp"}, {"prompt": "Какое это действие?", "accept": ["jump", "Jump"], "image": "@@MEDIA@@gg1/u5/verb_jump.webp"}, {"prompt": "Какое это действие?", "accept": ["write", "Write"], "image": "@@MEDIA@@gg1/u5/verb_write.webp"}, {"prompt": "Какое это действие?", "accept": ["climb", "Climb"], "image": "@@MEDIA@@gg1/u5/verb_climb.webp"}, {"prompt": "Какое это действие?", "accept": ["cook", "Cook"], "image": "@@MEDIA@@gg1/u5/verb_cook.webp"}, {"prompt": "Какое это действие?", "accept": ["skateboard", "Skateboard"], "image": "@@MEDIA@@gg1/u5/verb_skateboard.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильное слово", "questions": [{"q": "___ a picture", "type": "single", "options": [{"text": "read"}, {"text": "draw"}], "correct": [1], "image": "@@MEDIA@@gg1/u5/verb_draw.webp"}, {"q": "___ the guitar", "type": "single", "options": [{"text": "play"}, {"text": "ride"}], "correct": [0], "image": "@@MEDIA@@gg1/u5/obj_guitar.webp"}, {"q": "___ a cupcake", "type": "single", "options": [{"text": "play"}, {"text": "make"}], "correct": [1], "image": "@@MEDIA@@gg1/u5/coll_make_cupcakes.webp"}, {"q": "___ a book", "type": "single", "options": [{"text": "read"}, {"text": "sing"}], "correct": [0], "image": "@@MEDIA@@gg1/u5/verb_read.webp"}, {"q": "___ a bike", "type": "single", "options": [{"text": "dive"}, {"text": "ride"}], "correct": [1], "image": "@@MEDIA@@gg1/u5/coll_ride_bike.webp"}, {"q": "___ computer games", "type": "single", "options": [{"text": "play"}, {"text": "act"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Посмотри на таблицу. Дополни предложения словами can, can't, and или but", "mode": "drag", "image": "@@MEDIA@@gg1/u5/table_can.webp", "text": "Anna can swim and she can run fast.\nTom __can__ run fast __and__ he can fix a bike.\nSam and Joe can swim __but__ they __can't__ fix a bike.\nTom and Anna __can__ run fast."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'speaking', replace($blk${"title": "Что я умею и не умею 🎤", "html": "<p>Нажми на микрофон и расскажи, что ты умеешь и что не умеешь делать. Используй can и can't.</p><p><i>Пример: I can swim and ride a bike, but I can't fix a bike.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'match', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Соедини слово и перевод ⭐", "pairs": [{"left": "act", "right": "выступать на сцене", "left_audio_tts": "act"}, {"left": "climb", "right": "лазать, карабкаться", "left_audio_tts": "climb"}, {"left": "dive", "right": "нырять", "left_audio_tts": "dive"}, {"left": "fix", "right": "чинить", "left_audio_tts": "fix"}, {"left": "ride", "right": "ездить верхом, кататься", "left_audio_tts": "ride"}, {"left": "sing", "right": "петь", "left_audio_tts": "sing"}, {"left": "write", "right": "писать", "left_audio_tts": "write"}, {"left": "skateboard", "right": "кататься на скейтборде", "left_audio_tts": "skateboard"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски словами can или can't ⭐", "mode": "drag", "text": "1. Fish __can__ swim, but they __can't__ walk.\n2. I __can't__ fly, but I __can__ run fast.\n3. A: __Can__ your brother ride a horse? B: No, he __can't__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный ответ ⭐", "questions": [{"q": "Can you swim? — Yes, I ___.", "type": "single", "options": [{"text": "am"}, {"text": "can"}, {"text": "can't"}], "correct": [1]}, {"q": "Can your dad cook? — No, he ___.", "type": "single", "options": [{"text": "can"}, {"text": "isn't"}, {"text": "can't"}], "correct": [2]}, {"q": "___ they play the piano?", "type": "single", "options": [{"text": "Can"}, {"text": "Cans"}, {"text": "Are"}], "correct": [0]}, {"q": "Can she ride a bike? — Yes, ___ can.", "type": "single", "options": [{"text": "her"}, {"text": "she"}, {"text": "he"}], "correct": [1]}, {"q": "What can your dog do? — It ___ run fast.", "type": "single", "options": [{"text": "cans"}, {"text": "is"}, {"text": "can"}], "correct": [2]}, {"q": "Can the birds sing? — Yes, ___.", "type": "single", "options": [{"text": "they can"}, {"text": "it can"}, {"text": "they can't"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Молодец! 🎉</h3><p>Ты справился со всеми заданиями и показал, как хорошо знаешь тему. Ты настоящая звезда! ⭐ До встречи на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
