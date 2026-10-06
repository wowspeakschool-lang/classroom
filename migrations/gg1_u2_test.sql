-- Go Getter 1 · Unit 2 · My things · Test
-- собрано tools/gg1_build.py --lesson u2_test
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
  select v_unit, 'Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'exact_input', replace($blk${"title": "Посмотри на картинку и впиши слово целиком", "items": [{"prompt": "T-_h_rt", "accept": ["T-shirt", "t-shirt"], "image": "@@MEDIA@@gg1/u2/clothes_tshirt.webp"}, {"prompt": "sk_rt", "accept": ["skirt", "skirt"], "image": "@@MEDIA@@gg1/u2/clothes_skirt.webp"}, {"prompt": "dr_s_", "accept": ["dress", "dress"], "image": "@@MEDIA@@gg1/u2/clothes_dress.webp"}, {"prompt": "tro_s_rs", "accept": ["trousers", "trousers"], "image": "@@MEDIA@@gg1/u2/clothes_trousers.webp"}, {"prompt": "je_ns", "accept": ["jeans", "jeans"], "image": "@@MEDIA@@gg1/u2/clothes_jeans.webp"}, {"prompt": "co_t", "accept": ["coat", "coat"], "image": "@@MEDIA@@gg1/u2/clothes_coat.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери пропущенные слова. Стрелка показывает, далеко вещь или близко", "questions": [{"q": "A: ___ is my hoodie. B: Nice! Is it new?", "type": "single", "options": [{"text": "These"}, {"text": "Those"}, {"text": "That"}, {"text": "This"}], "correct": [2], "image": "@@MEDIA@@gg1/u2/far_hoodie.webp"}, {"q": "A: That is my ___. B: Nice! Is it new?", "type": "single", "options": [{"text": "hoodie"}, {"text": "T-shirt"}, {"text": "jacket"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери пропущенные слова", "questions": [{"q": "A: Whose ___ are these? B: They are mine.", "type": "single", "options": [{"text": "trainers"}, {"text": "boots"}, {"text": "trousers"}], "correct": [0], "image": "@@MEDIA@@gg1/u2/near_trainers.webp"}, {"q": "A: Whose trainers are ___? B: They are mine.", "type": "single", "options": [{"text": "that"}, {"text": "those"}, {"text": "this"}, {"text": "these"}], "correct": [3]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери пропущенные слова", "questions": [{"q": "A: ___ isn't my tracksuit. B: Whose is it then?", "type": "single", "options": [{"text": "Those"}, {"text": "These"}, {"text": "This"}, {"text": "That"}], "correct": [2], "image": "@@MEDIA@@gg1/u2/near_tracksuit.webp"}, {"q": "A: This isn't my ___. B: Whose is it then?", "type": "single", "options": [{"text": "trousers"}, {"text": "tracksuit"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери пропущенные слова", "questions": [{"q": "A: ___ is Alex's favourite cap. B: No, it's not! It's mine!", "type": "single", "options": [{"text": "These"}, {"text": "This"}, {"text": "That"}, {"text": "Those"}], "correct": [2], "image": "@@MEDIA@@gg1/u2/far_cap.webp"}, {"q": "A: That is Alex's favourite ___. B: No, it's not! It's mine!", "type": "single", "options": [{"text": "hat"}, {"text": "cap"}, {"text": "top"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери пропущенные слова", "questions": [{"q": "A: Are ___ your friends' boots? B: I'm not sure.", "type": "single", "options": [{"text": "these"}, {"text": "this"}, {"text": "those"}, {"text": "that"}], "correct": [2], "image": "@@MEDIA@@gg1/u2/far_boots.webp"}, {"q": "A: Are those your friends' ___? B: I'm not sure.", "type": "single", "options": [{"text": "trainers"}, {"text": "boots"}, {"text": "shoes"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["What", "is", "your", "favourite", "colour?"], "sentence": "What is your favourite colour?", "audio_tts": "What is your favourite colour?", "image": "@@MEDIA@@gg1/u2/pencils_heart.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Are", "you", "David Smith's", "brother?"], "sentence": "Are you David Smith's brother?", "audio_tts": "Are you David Smith's brother?", "image": "@@MEDIA@@gg1/u2/brothers_highfive.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["These", "boots", "are", "too", "small."], "sentence": "These boots are too small.", "audio_tts": "These boots are too small.", "image": "@@MEDIA@@gg1/u2/boot_black.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["What", "is", "your", "favourite", "film?"], "sentence": "What is your favourite film?", "audio_tts": "What is your favourite film?", "image": "@@MEDIA@@gg1/u2/cinema.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Is", "Anna", "your", "best", "friend?"], "sentence": "Is Anna your best friend?", "audio_tts": "Is Anna your best friend?", "image": "@@MEDIA@@gg1/u2/best_friends_girls.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'text', replace($blk${"html": "<h3>READING</h3><p>Прочитай текст.</p><p><i>Today I'm packing my backpack for a school trip. My new red T-shirt is in my backpack. My old jeans are in my backpack too. My favourite hoodie is too big — it's not in my backpack. My boots are too old. They are not in my backpack. My phone and my keys are in my backpack. My tablet is too big — it's not in my backpack. My small pencil case is in my backpack.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'sort', replace($blk${"title": "READING. Распредели вещи по двум столбикам", "groups": [{"name": "В рюкзаке", "items": [{"text": "T-shirt"}, {"text": "jeans"}, {"text": "phone"}, {"text": "keys"}, {"text": "pencil case"}]}, {"name": "Не в рюкзаке", "items": [{"text": "hoodie"}, {"text": "boots"}, {"text": "tablet"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>LISTENING. Прослушай Эмму: она показывает свои школьные вещи.</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'gaps', replace($blk${"title": "LISTENING. Перетащи правильное прилагательное в каждый пропуск", "mode": "drag", "text": "1. The school bag is __new__.\n2. The school shoes are __black__.\n3. The favourite jumper is __red__.\n4. The old trainers are __boring__.\n5. The cap is __cool__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "image": "@@MEDIA@@gg1/u2/kevin_birthday.webp", "html": "<p>Посмотри на картинку и ответь на вопросы. Запиши свой ответ, нажав на кнопку микрофона 🙌</p><ol><li>This is Kevin and his family. Are they in the garden?</li><li>Where are they?</li><li>How old is Kevin?</li><li>Who is Emma? Who is Charles?</li><li>Look at Kevin. Where are Kevin and his family from?</li><li>Where is Giorgio from?</li></ol>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 15);
end
$mig$;
