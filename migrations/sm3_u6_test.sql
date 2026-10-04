-- Super Minds 3 · Unit 6 · Gadgets · Test
-- собрано tools/sm3_build.py --lesson u6_test
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 6 · Gadgets', 6
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 6 · Gadgets');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 6 · Gadgets';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Test', 'test',
         90, false, 8
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с картинками", "pairs": [{"left_image": "@@MEDIA@@sm3/u6/gad_torch.webp", "right": "Torch", "right_audio_tts": "torch"}, {"left_image": "@@MEDIA@@sm3/u6/gad_walkie_talkies.webp", "right": "Walkie-talkie", "right_audio_tts": "walkie-talkie"}, {"left_image": "@@MEDIA@@sm3/u6/gad_laptop.webp", "right": "Laptop", "right_audio_tts": "laptop"}, {"left_image": "@@MEDIA@@sm3/u6/gad_fan.webp", "right": "Electric fan", "right_audio_tts": "electric fan"}, {"left_image": "@@MEDIA@@sm3/u6/gad_console.webp", "right": "Games console", "right_audio_tts": "games console"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'gaps', replace($blk${"title": "Прочитай и заполни пропуски", "mode": "drag", "text": "1. We use it to go from one floor to another — __lift__.\n2. We use it to listen to music — __digital radio__.\n3. We use this gadget to call friends — __mobile phone__.\n4. We use it to study or work in the internet — __laptop__.\n5. We use it when it is dark or at night — __torch__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "The tablet is ___ than the phone.", "type": "single", "options": [{"text": "bigger"}, {"text": "big"}, {"text": "more big"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "Is a car ___ than a bike?", "type": "single", "options": [{"text": "faster"}, {"text": "fast"}, {"text": "more fast"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "The white phone is ___ than the black phone.", "type": "single", "options": [{"text": "more expensive"}, {"text": "expensive"}, {"text": "expensiver"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: Are dogs ___ than cats?", "type": "single", "options": [{"text": "friendlier"}, {"text": "more friendly"}, {"text": "friendly"}], "correct": [0]}, {"q": "B: I think yes, they ___.", "type": "single", "options": [{"text": "are"}, {"text": "is"}, {"text": "aren’t"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: Who is ___?", "type": "single", "options": [{"text": "stronger"}, {"text": "more strong"}, {"text": "strong"}], "correct": [0]}, {"q": "B: Hulk is ___ than a sportsman.", "type": "single", "options": [{"text": "stronger"}, {"text": "more strong"}, {"text": "strong"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["The TV", "is", "bigger", "than", "the phone."], "sentence": "The TV is bigger than the phone.", "audio_tts": "The TV is bigger than the phone."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"words": ["My bike", "is", "faster", "than", "yours."], "sentence": "My bike is faster than yours.", "audio_tts": "My bike is faster than yours."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"words": ["How", "much", "is", "the torch?"], "sentence": "How much is the torch?", "audio_tts": "How much is the torch?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"words": ["I", "would", "like", "to", "buy", "it."], "sentence": "I would like to buy it.", "audio_tts": "I would like to buy it."}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'order', replace($blk${"words": ["My", "favourite", "gadget", "is", "my bike."], "sentence": "My favourite gadget is my bike.", "audio_tts": "My favourite gadget is my bike."}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤 Part 1", "needs_review": true, "image": "@@MEDIA@@sm3/u6/shop_prices.webp", "html": "<p>Посмотри на картинку, составь диалог и разыграй его.</p><p><i>For example:<br>A: Hello, can I help you?<br>B: Yes, I’d like a laptop, please.<br>A: That’s £325.</i></p><p>Запиши свой ответ, нажав на кнопку микрофона.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤 Part 2", "needs_review": true, "image": "@@MEDIA@@sm3/u6/scene_gadgets_desk.webp", "html": "<p>Сравни предметы на картинке (4–5 предложений).</p><p><i>For example: The laptop is bigger than the mobile phone.</i></p><p>Запиши свой ответ, нажав на кнопку микрофона.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 13);
end
$mig$;
