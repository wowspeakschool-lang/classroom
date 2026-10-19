-- Super Minds 1 · Unit 8 · My body · Homework 7
-- собрано tools/sm1_build.py --lesson u8_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 8 · My body', 8
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 8 · My body');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 8 · My body';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         null, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет, изобретатель! 👋</h2><p>Это последняя домашка перед тестом! Повтори все части тела, I can / I can't и вопросы Can you…?</p><p><img src=\"@@MEDIA@@sm1/u8/inventors_robot.webp\" alt=\"\" style=\"max-width:320px\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Послушай слово и выбери картинку", "needs_review": false, "questions": [{"q": "", "type": "single", "audio_tts": "head", "options": [{"image": "@@MEDIA@@sm1/u8/body_hand.webp"}, {"image": "@@MEDIA@@sm1/u8/body_head.webp"}, {"image": "@@MEDIA@@sm1/u8/body_leg.webp"}], "correct": [1]}, {"q": "", "type": "single", "audio_tts": "fingers", "options": [{"image": "@@MEDIA@@sm1/u8/body_knee.webp"}, {"image": "@@MEDIA@@sm1/u8/body_foot.webp"}, {"image": "@@MEDIA@@sm1/u8/body_fingers.webp"}], "correct": [2]}, {"q": "", "type": "single", "audio_tts": "hand", "options": [{"image": "@@MEDIA@@sm1/u8/body_toes.webp"}, {"image": "@@MEDIA@@sm1/u8/body_hand.webp"}, {"image": "@@MEDIA@@sm1/u8/body_knee.webp"}], "correct": [1]}, {"q": "", "type": "single", "audio_tts": "knee", "options": [{"image": "@@MEDIA@@sm1/u8/body_arms.webp"}, {"image": "@@MEDIA@@sm1/u8/body_foot.webp"}, {"image": "@@MEDIA@@sm1/u8/body_knee.webp"}], "correct": [2]}, {"q": "", "type": "single", "audio_tts": "leg", "options": [{"image": "@@MEDIA@@sm1/u8/body_leg.webp"}, {"image": "@@MEDIA@@sm1/u8/body_head.webp"}, {"image": "@@MEDIA@@sm1/u8/body_hand.webp"}], "correct": [0]}, {"q": "", "type": "single", "audio_tts": "toes", "options": [{"image": "@@MEDIA@@sm1/u8/body_arms.webp"}, {"image": "@@MEDIA@@sm1/u8/body_toes.webp"}, {"image": "@@MEDIA@@sm1/u8/body_head.webp"}], "correct": [1]}, {"q": "", "type": "single", "audio_tts": "foot", "options": [{"image": "@@MEDIA@@sm1/u8/body_head.webp"}, {"image": "@@MEDIA@@sm1/u8/body_foot.webp"}, {"image": "@@MEDIA@@sm1/u8/body_fingers.webp"}], "correct": [1]}, {"q": "", "type": "single", "audio_tts": "arms", "options": [{"image": "@@MEDIA@@sm1/u8/body_knee.webp"}, {"image": "@@MEDIA@@sm1/u8/body_toes.webp"}, {"image": "@@MEDIA@@sm1/u8/body_arms.webp"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'gaps', replace($blk${"title": "Посмотри на картинку. Впиши can или can't.", "mode": "type", "image": "@@MEDIA@@sm1/u8/animals_can_cant.webp", "text": "1. A penguin __can't__ fly.\n2. A fish __can__ swim.\n3. A fish __can't__ walk.\n4. A duck __can__ fly.\n5. A duck __can__ swim.\n6. A penguin __can__ walk."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Прочитай вопрос и посмотри на картинку. Выбери правильный ответ.<br>Can he play tennis?", "type": "single", "options": [{"text": "Yes, he can."}, {"text": "No, he can't."}], "correct": [0], "image": "@@MEDIA@@sm1/u8/boy_tennis_cook.webp"}, {"q": "Can he cook?", "type": "single", "options": [{"text": "Yes, he can."}, {"text": "No, he can't."}], "correct": [1], "image": "@@MEDIA@@sm1/u8/boy_tennis_cook.webp"}, {"q": "Can she dance?", "type": "single", "options": [{"text": "No, she can't."}, {"text": "Yes, she can."}], "correct": [1], "image": "@@MEDIA@@sm1/u8/girl_dance_fly.webp"}, {"q": "Can she fly?", "type": "single", "options": [{"text": "No, she can't."}, {"text": "Yes, she can."}], "correct": [0], "image": "@@MEDIA@@sm1/u8/girl_dance_fly.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'speaking', replace($blk${"title": "Что ты умеешь? 🎤", "html": "<p>Нажми на микрофон и расскажи, что ты умеешь и не умеешь делать.</p><p><b>Пример:</b> <i>I can swim. I can ride a bike. I can't play the piano.</i></p>", "sample_tts": "I can swim. I can ride a bike. I can't play the piano.", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'exact_input', replace($blk${"items": [{"prompt": "Впиши слово.", "image": "@@MEDIA@@sm1/u8/body_head.webp", "accept": ["head", "Head"], "audio_tts": "head"}, {"prompt": "Впиши слово.", "image": "@@MEDIA@@sm1/u8/body_fingers.webp", "accept": ["fingers", "Fingers"], "audio_tts": "fingers"}, {"prompt": "Впиши слово.", "image": "@@MEDIA@@sm1/u8/body_hand.webp", "accept": ["hand", "Hand"], "audio_tts": "hand"}, {"prompt": "Впиши слово.", "image": "@@MEDIA@@sm1/u8/body_knee.webp", "accept": ["knee", "Knee"], "audio_tts": "knee"}, {"prompt": "Впиши слово.", "image": "@@MEDIA@@sm1/u8/body_leg.webp", "accept": ["leg", "Leg"], "audio_tts": "leg"}, {"prompt": "Впиши слово.", "image": "@@MEDIA@@sm1/u8/body_toes.webp", "accept": ["toes", "Toes"], "audio_tts": "toes"}, {"prompt": "Впиши слово.", "image": "@@MEDIA@@sm1/u8/body_foot.webp", "accept": ["foot", "Foot"], "audio_tts": "foot"}, {"prompt": "Впиши слово.", "image": "@@MEDIA@@sm1/u8/body_arms.webp", "accept": ["arms", "Arms"], "audio_tts": "arms"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["I", "can", "touch", "my", "toes."], "sentence": "I can touch my toes.", "audio_tts": "I can touch my toes."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["Can", "you", "ride", "a", "bike?"], "sentence": "Can you ride a bike?", "audio_tts": "Can you ride a bike?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"words": ["She", "can't", "play", "the", "piano."], "sentence": "She can't play the piano.", "audio_tts": "She can't play the piano."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/yes_thumb_up.webp\" alt=\"\" style=\"height:180px\"></p><h3>Молодец! Ты готов к тесту! 💪</h3>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9);
end
$mig$;
