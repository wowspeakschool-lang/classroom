-- Super Minds 1 · Unit 8 · My body · Unit 8 Test
-- собрано tools/sm1_build.py --lesson u8_test
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
  select v_unit, 'Unit 8 Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Unit 8 Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Unit 8 Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'exact_input', replace($blk${"items": [{"prompt": "Впиши недостающие буквы — напиши слово целиком: h _ _ d", "image": "@@MEDIA@@sm1/u8/body_head.webp", "accept": ["head", "Head"], "audio_tts": "head"}, {"prompt": "Впиши недостающие буквы — напиши слово целиком: f _ n g _ r s", "image": "@@MEDIA@@sm1/u8/body_fingers.webp", "accept": ["fingers", "Fingers"], "audio_tts": "fingers"}, {"prompt": "Впиши недостающие буквы — напиши слово целиком: h _ n _", "image": "@@MEDIA@@sm1/u8/body_hand.webp", "accept": ["hand", "Hand"], "audio_tts": "hand"}, {"prompt": "Впиши недостающие буквы — напиши слово целиком: k n _ _", "image": "@@MEDIA@@sm1/u8/body_knee.webp", "accept": ["knee", "Knee"], "audio_tts": "knee"}, {"prompt": "Впиши недостающие буквы — напиши слово целиком: l _ g", "image": "@@MEDIA@@sm1/u8/body_leg.webp", "accept": ["leg", "Leg"], "audio_tts": "leg"}, {"prompt": "Впиши недостающие буквы — напиши слово целиком: t _ _ s", "image": "@@MEDIA@@sm1/u8/body_toes.webp", "accept": ["toes", "Toes"], "audio_tts": "toes"}, {"prompt": "Впиши недостающие буквы — напиши слово целиком: f _ _ t", "image": "@@MEDIA@@sm1/u8/body_foot.webp", "accept": ["foot", "Foot"], "audio_tts": "foot"}, {"prompt": "Впиши недостающие буквы — напиши слово целиком: a _ m s", "image": "@@MEDIA@@sm1/u8/body_arms.webp", "accept": ["arms", "Arms"], "audio_tts": "arms"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с картинками", "pairs": [{"left_image": "@@MEDIA@@sm1/u8/body_hand.webp", "right": "hand", "right_audio_tts": "hand"}, {"left_image": "@@MEDIA@@sm1/u8/body_foot.webp", "right": "foot", "right_audio_tts": "foot"}, {"left_image": "@@MEDIA@@sm1/u8/body_toes.webp", "right": "toes", "right_audio_tts": "toes"}, {"left_image": "@@MEDIA@@sm1/u8/body_head.webp", "right": "head", "right_audio_tts": "head"}, {"left_image": "@@MEDIA@@sm1/u8/body_fingers.webp", "right": "fingers", "right_audio_tts": "fingers"}, {"left_image": "@@MEDIA@@sm1/u8/body_arms.webp", "right": "arm", "right_audio_tts": "arm"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Заполни пропуск — выбери подходящий вариант:<br>He ___ play the piano.", "type": "single", "image": "@@MEDIA@@sm1/u8/t_he_piano.webp", "options": [{"text": "can"}, {"text": "can't"}], "correct": [1]}, {"q": "He ___ play tennis.", "type": "single", "image": "@@MEDIA@@sm1/u8/t_he_tennis.webp", "options": [{"text": "can't"}, {"text": "can"}], "correct": [0]}, {"q": "He ___ swim.", "type": "single", "image": "@@MEDIA@@sm1/u8/t_he_swim.webp", "options": [{"text": "can"}, {"text": "can't"}], "correct": [0]}, {"q": "She ___ dance.", "type": "single", "image": "@@MEDIA@@sm1/u8/t_she_dance.webp", "options": [{"text": "can't"}, {"text": "can"}], "correct": [1]}, {"q": "She ___ ride a pony.", "type": "single", "image": "@@MEDIA@@sm1/u8/t_she_pony.webp", "options": [{"text": "can't"}, {"text": "can"}], "correct": [0]}, {"q": "She ___ ride a bike.", "type": "single", "image": "@@MEDIA@@sm1/u8/t_she_bike.webp", "options": [{"text": "can"}, {"text": "can't"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"words": ["Can", "you", "stand", "on", "one leg?"], "sentence": "Can you stand on one leg?", "audio_tts": "Can you stand on one leg?", "image": "@@MEDIA@@sm1/u8/t_stand_one_leg.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"words": ["My dog", "can", "play", "football."], "sentence": "My dog can play football.", "audio_tts": "My dog can play football.", "image": "@@MEDIA@@sm1/u8/t_dog_football.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["I", "can't", "touch", "my toes."], "sentence": "I can't touch my toes.", "audio_tts": "I can't touch my toes.", "image": "@@MEDIA@@sm1/u8/t_touch_toes.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["Can", "your cat", "play", "the guitar?"], "sentence": "Can your cat play the guitar?", "audio_tts": "Can your cat play the guitar?", "image": "@@MEDIA@@sm1/u8/t_cat_guitar.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["Can", "your", "sister", "fly", "a kite?"], "sentence": "Can your sister fly a kite?", "audio_tts": "Can your sister fly a kite?", "image": "@@MEDIA@@sm1/u8/kite_sky.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p>Прочитай текст и выбери правильный вариант ответа к каждому вопросу после текста.</p><p><img src=\"@@MEDIA@@sm1/u8/t_letter_jake.webp\" alt=\"A Letter from Jake\" style=\"max-width:100%\"></p><h3>A Letter from Jake</h3><p>Dear Grandma,</p><p>Today I am very happy! I have got a new robot! His name is Beep. He is very funny!</p><p>Beep has got a big head and small hands. He has got two long arms and two short legs. He has got eight fingers but he hasn't got toes!</p><p>Beep can dance very well! He can jump and he can run fast. But he can't swim — he doesn't like water. Can he fly? No, he can't! But he can sing funny songs.</p><p>My friend Lily is here today. “Can you play football?” she asks Beep. “Yes, I can!” says Beep. But he can't kick the ball with his feet — they are too small! We all laugh.</p><p>I love my robot! Can you come and see him? He can say “Hello” to you!</p><p>Love, Jake</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "How many fingers has Beep got?", "type": "single", "options": [{"text": "ten"}, {"text": "eight"}, {"text": "six"}], "correct": [1]}, {"q": "What can Beep do?", "type": "single", "options": [{"text": "He can swim."}, {"text": "He can fly."}, {"text": "He can dance."}], "correct": [2]}, {"q": "Can Beep play football?", "type": "single", "options": [{"text": "No, he can't."}, {"text": "Yes, he can."}, {"text": "He doesn't want to."}], "correct": [1]}, {"q": "Why can't Beep kick the ball?", "type": "single", "options": [{"text": "His feet are too small."}, {"text": "His arms are too long."}, {"text": "His legs are too short."}], "correct": [0]}, {"q": "What does Jake want Grandma to do?", "type": "single", "options": [{"text": "Buy a robot."}, {"text": "Play football."}, {"text": "Come and see Beep."}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'video', replace($blk${"title": "Послушай разговор Лили и Тома о новом роботе", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши только ОДНО недостающее слово в пропуски", "mode": "type", "text": "1. The robot's name is __Bloop__.\n2. He's got a __big__ head.\n3. He's got __four|4__ arms.\n4. He __can't|cant|can not|cannot__ swim.\n5. He can __jump__ very high."}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "html": "<p>Посмотри на картинку и ответь на вопросы:</p><ol><li>Can the girl run?</li><li>Can the boy ride a bike?</li><li>Can the children play football?</li><li>Can the dog fly?</li><li>Can the baby walk?</li></ol><p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>", "image": "@@MEDIA@@sm1/u8/t_town_scene.webp", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 12);
end
$mig$;
