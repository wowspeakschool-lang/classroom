-- Super Minds 3 · Unit 6 · Gadgets · Homework 1
-- собрано tools/sm3_build.py --lesson u6_hw1
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
  select v_unit, 'Homework 1', 'homework',
         60, false, 0
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 1');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 1';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! А ты любишь гаджеты и всякие технологии?</h2><p>Выполни все задания, чтобы выучить слова на 100%!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'flashcards', replace($blk${"cards": [{"text": "mobile phone", "translation": "мобильный телефон", "audio_tts": "mobile phone", "image": "@@MEDIA@@sm3/u6/gad_phone.webp"}, {"text": "tablet", "translation": "планшет", "audio_tts": "tablet", "image": "@@MEDIA@@sm3/u6/gad_tablet.webp"}, {"text": "laptop", "translation": "ноутбук", "audio_tts": "laptop", "image": "@@MEDIA@@sm3/u6/gad_laptop.webp"}, {"text": "torch", "translation": "фонарик", "audio_tts": "torch", "image": "@@MEDIA@@sm3/u6/gad_torch.webp"}, {"text": "walkie-talkie", "translation": "рация", "audio_tts": "walkie-talkie", "image": "@@MEDIA@@sm3/u6/gad_walkie_talkies.webp"}, {"text": "lift", "translation": "лифт", "audio_tts": "lift", "image": "@@MEDIA@@sm3/u6/gad_lift.webp"}, {"text": "games console", "translation": "игровая приставка", "audio_tts": "games console", "image": "@@MEDIA@@sm3/u6/gad_console.webp"}, {"text": "electric toothbrush", "translation": "электрическая зубная щётка", "audio_tts": "electric toothbrush", "image": "@@MEDIA@@sm3/u6/gad_toothbrush.webp"}, {"text": "electric fan", "translation": "вентилятор", "audio_tts": "electric fan", "image": "@@MEDIA@@sm3/u6/gad_fan.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Как по-английски «мобильный телефон»?", "type": "single", "options": [{"text": "laptop"}, {"text": "mobile phone"}, {"text": "tablet"}, {"text": "torch"}], "correct": [1]}, {"q": "Как по-английски «планшет»?", "type": "single", "options": [{"text": "laptop"}, {"text": "tablet"}, {"text": "torch"}, {"text": "walkie-talkie"}], "correct": [1]}, {"q": "Как по-английски «ноутбук»?", "type": "single", "options": [{"text": "laptop"}, {"text": "lift"}, {"text": "torch"}, {"text": "walkie-talkie"}], "correct": [0]}, {"q": "Как по-английски «фонарик»?", "type": "single", "options": [{"text": "games console"}, {"text": "lift"}, {"text": "torch"}, {"text": "walkie-talkie"}], "correct": [2]}, {"q": "Как по-английски «рация»?", "type": "single", "options": [{"text": "electric toothbrush"}, {"text": "games console"}, {"text": "lift"}, {"text": "walkie-talkie"}], "correct": [3]}, {"q": "Как по-английски «лифт»?", "type": "single", "options": [{"text": "electric fan"}, {"text": "electric toothbrush"}, {"text": "games console"}, {"text": "lift"}], "correct": [3]}, {"q": "Как по-английски «игровая приставка»?", "type": "single", "options": [{"text": "electric fan"}, {"text": "electric toothbrush"}, {"text": "games console"}, {"text": "mobile phone"}], "correct": [2]}, {"q": "Как по-английски «электрическая зубная щётка»?", "type": "single", "options": [{"text": "electric fan"}, {"text": "electric toothbrush"}, {"text": "mobile phone"}, {"text": "tablet"}], "correct": [1]}, {"q": "Как по-английски «вентилятор»?", "type": "single", "options": [{"text": "electric fan"}, {"text": "laptop"}, {"text": "mobile phone"}, {"text": "tablet"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'exact_input', replace($blk${"items": [{"image": "@@MEDIA@@sm3/u6/gad_phone.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["mobile phone", "Mobile phone"], "audio_tts": "mobile phone"}, {"image": "@@MEDIA@@sm3/u6/gad_tablet.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["tablet", "Tablet"], "audio_tts": "tablet"}, {"image": "@@MEDIA@@sm3/u6/gad_laptop.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["laptop", "Laptop"], "audio_tts": "laptop"}, {"image": "@@MEDIA@@sm3/u6/gad_torch.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["torch", "Torch"], "audio_tts": "torch"}, {"image": "@@MEDIA@@sm3/u6/gad_walkie_talkies.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["walkie-talkie", "Walkie-talkie"], "audio_tts": "walkie-talkie"}, {"image": "@@MEDIA@@sm3/u6/gad_lift.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["lift", "Lift"], "audio_tts": "lift"}, {"image": "@@MEDIA@@sm3/u6/gad_console.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["games console", "Games console"], "audio_tts": "games console"}, {"image": "@@MEDIA@@sm3/u6/gad_toothbrush.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["electric toothbrush", "Electric toothbrush"], "audio_tts": "electric toothbrush"}, {"image": "@@MEDIA@@sm3/u6/gad_fan.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["electric fan", "Electric fan"], "audio_tts": "electric fan"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/good_luck_clover.webp\" alt=\"\" style=\"height:180px\"></p><h3>А теперь — вторая, дополнительная часть</h3><p>Выполнив эти задания, ты станешь МЕГА крутым учеником!</p><p>Посмотри на ценники и впиши в пропуски, сколько стоит покупка.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "Посмотри на цены и впиши суммы (только число)", "image": "@@MEDIA@@sm3/u6/shop_prices.webp", "text": "1. A: Hello, can I help you? B: Yes, I’d like a laptop, please. A: That’s £__325__.\n2. A: Hello, can I help you? B: Yes, I’d like a games console, please. A: That’s £__200__.\n3. A: Hello, can I help you? B: Yes, I’d like a torch and an electric toothbrush, please. A: That’s £__20__.\n4. A: Hello, can I help you? B: Yes, I’d like a tablet and a walkie-talkie, please. A: That’s £__115__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'task', replace($blk${"title": "Напиши, какие гаджеты есть у тебя", "needs_review": true, "html": "<p>Молодец! Ты справился. А это — твоё последнее задание.</p><p><i>Например: I’ve got a tablet and a torch.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура, ты выполнил все задания — ты супер ученик!</h3><p>За это держи звёздочку. До встречи на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7);
end
$mig$;
