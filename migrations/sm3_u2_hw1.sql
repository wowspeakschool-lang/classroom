-- Super Minds 3 · Unit 2 · Food · Homework 1
-- собрано tools/sm3_build.py --lesson u2_hw1
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 2 · Food', 2
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 2 · Food');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 2 · Food';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 1', 'homework',
         60, false, 0
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 1');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 1';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет-привет!</h2><p>Готов к домашнему заданию? Тогда давай начинать :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'flashcards', replace($blk${"cards": [{"text": "apple juice", "translation": "яблочный сок", "audio_tts": "apple juice", "image": "@@MEDIA@@sm3/u2/food_apple_juice.webp"}, {"text": "rolls", "translation": "булочки", "audio_tts": "rolls", "image": "@@MEDIA@@sm3/u2/food_bread_rolls.webp"}, {"text": "cheese", "translation": "сыр", "audio_tts": "cheese", "image": "@@MEDIA@@sm3/u2/food_cheese.webp"}, {"text": "water", "translation": "вода", "audio_tts": "water", "image": "@@MEDIA@@sm3/u2/food_water.webp"}, {"text": "soup", "translation": "суп", "audio_tts": "soup", "image": "@@MEDIA@@sm3/u2/food_soup.webp"}, {"text": "vegetables", "translation": "овощи", "audio_tts": "vegetables", "image": "@@MEDIA@@sm3/u2/food_vegetables.webp"}, {"text": "lemonade", "translation": "лимонад", "audio_tts": "lemonade", "image": "@@MEDIA@@sm3/u2/food_lemonade.webp"}, {"text": "salad", "translation": "салат", "audio_tts": "salad", "image": "@@MEDIA@@sm3/u2/food_salad.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'exact_input', replace($blk${"items": [{"image": "@@MEDIA@@sm3/u2/food_apple_juice.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["apple juice", "apple juice", "Apple juice"], "audio_tts": "apple juice"}, {"image": "@@MEDIA@@sm3/u2/food_bread_rolls.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["rolls", "rolls", "Rolls"], "audio_tts": "rolls"}, {"image": "@@MEDIA@@sm3/u2/food_cheese.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["cheese", "cheese", "Cheese"], "audio_tts": "cheese"}, {"image": "@@MEDIA@@sm3/u2/food_water.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["water", "water", "Water"], "audio_tts": "water"}, {"image": "@@MEDIA@@sm3/u2/food_soup.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["soup", "soup", "Soup"], "audio_tts": "soup"}, {"image": "@@MEDIA@@sm3/u2/food_vegetables.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["vegetables", "vegetables", "Vegetables"], "audio_tts": "vegetables"}, {"image": "@@MEDIA@@sm3/u2/food_lemonade.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["lemonade", "lemonade", "Lemonade"], "audio_tts": "lemonade"}, {"image": "@@MEDIA@@sm3/u2/food_salad.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["salad", "salad", "Salad"], "audio_tts": "salad"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски словами из кроссворда", "mode": "drag", "text": "1. Can I have two chicken __rolls__, please?\n2. Carrots and potatoes are __vegetables__.\n3. It’s usually yellow or white. — __cheese__!\n4. You wash your face with it, and you can drink it. — __water__!\n5. You drink this, it’s sweet. — __apple juice__!\n6. It’s usually hot and you need a spoon to eat it. — __soup__!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'sequence', replace($blk${"title": "Составь диалог — расставь реплики по порядку", "items": [{"text": "I’m hungry."}, {"text": "Would you like a chicken roll?"}, {"text": "No, thanks. I don’t like chicken."}, {"text": "Would you like a cheese sandwich?"}, {"text": "Yes, please. I’d love one."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Супер!</h3><p>Большое спасибо за домашнее задание. Ты отлично поработал сегодня. Увидимся на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5);
end
$mig$;
