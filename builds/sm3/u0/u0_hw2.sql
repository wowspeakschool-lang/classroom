-- SM3 · Unit 0 · Homework 2 — к уроку Lesson 2
-- Собрано скриптом builds/sm3/u0/build.py. Не заливать, пока не назовут,
-- куда переехала платформа. Проверка:
--   python3.13 tools/val.py builds/sm3/u0 sm3/u0

do $$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm3';
  if v_course is null then raise exception 'курс sm3 не найден'; end if;

  select id into v_unit from classroom_units where course_id = v_course and sort_order = 0;
  if v_unit is null then
    insert into classroom_units (course_id, title, sort_order)
    values (v_course, 'Unit 0 · Meet The Explorers', 0)
    returning id into v_unit;
  end if;

  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and sort_order = 1;
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, kind, sort_order, pass_threshold, is_published)
    values (v_unit, 'Homework 2', 'homework', 1, 60, false)
    returning id into v_lesson;
  else
    update classroom_lessons
       set title = 'Homework 2', kind = 'homework', pass_threshold = 60
     where id = v_lesson;
  end if;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p>Привет! 👋 В этой домашке тренируем <b>be good at + Ving</b> — рассказываем, что получается хорошо, а что не очень.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку и выбери правильный вариант.", "questions": [{"q": "What is she good at?", "type": "single", "correct": [0], "image": "@@MEDIA@@sm3/u0/act_dancing.webp", "options": [{"text": "dancing"}, {"text": "painting"}, {"text": "swimming"}]}, {"q": "What is he good at?", "type": "single", "correct": [1], "image": "@@MEDIA@@sm3/u0/act_painting.webp", "options": [{"text": "climbing"}, {"text": "painting"}, {"text": "riding a bike"}]}, {"q": "What is she good at?", "type": "single", "correct": [2], "image": "@@MEDIA@@sm3/u0/act_swimming.webp", "options": [{"text": "dancing"}, {"text": "playing football"}, {"text": "swimming"}]}, {"q": "What is he good at?", "type": "single", "correct": [1], "image": "@@MEDIA@@sm3/u0/act_football.webp", "options": [{"text": "swimming"}, {"text": "playing football"}, {"text": "painting"}]}, {"q": "What is she good at?", "type": "single", "correct": [0], "image": "@@MEDIA@@sm3/u0/act_riding.webp", "options": [{"text": "riding a bike"}, {"text": "climbing trees"}, {"text": "dancing"}]}, {"q": "What is he good at?", "type": "single", "correct": [2], "image": "@@MEDIA@@sm3/u0/act_climbing.webp", "options": [{"text": "swimming"}, {"text": "painting"}, {"text": "climbing trees"}]}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант.", "questions": [{"q": "I’m good at ___ pictures.", "type": "single", "correct": [0], "options": [{"text": "painting"}, {"text": "paint"}, {"text": "paints"}]}, {"q": "He isn’t good at ___ football.", "type": "single", "correct": [0], "options": [{"text": "playing"}, {"text": "play"}, {"text": "played"}]}, {"q": "___ she good at dancing?", "type": "single", "correct": [0], "options": [{"text": "Is"}, {"text": "Does"}, {"text": "Do"}]}, {"q": "We ___ good at climbing trees.", "type": "single", "correct": [0], "options": [{"text": "are"}, {"text": "is"}, {"text": "am"}]}, {"q": "They aren’t good ___ swimming.", "type": "single", "correct": [0], "options": [{"text": "at"}, {"text": "in"}, {"text": "to"}]}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'exact_input', replace($blk${"title": "Поставь глагол в правильную форму.", "items": [{"prompt": "1. I’m good at ___ (ride) a bike.", "accept": ["riding", "Riding"]}, {"prompt": "2. She’s not good at ___ (tell) lies.", "accept": ["telling", "Telling"]}, {"prompt": "3. Are you good at ___ (dance)?", "accept": ["dancing", "Dancing"]}, {"prompt": "4. He’s good at ___ (climb) trees.", "accept": ["climbing", "Climbing"]}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"words": ["I’m", "good at", "playing", "the guitar."], "sentence": "I’m good at playing the guitar.", "audio": "", "audio_tts": "I’m good at playing the guitar."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["Lucy", "isn’t", "good at", "painting."], "sentence": "Lucy isn’t good at painting.", "audio": "", "audio_tts": "Lucy isn’t good at painting."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["Are", "you", "good at", "doing", "puzzles?"], "sentence": "Are you good at doing puzzles?", "audio": "", "audio_tts": "Are you good at doing puzzles?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "html": "<p>Расскажи, что у тебя получается хорошо, а что не очень — 4–6 предложений. Нажми на микрофон и запиши ответ.</p><p><i>For example:<br>I’m good at swimming and riding a bike.<br>I’m not good at painting.<br>My friend is good at playing football.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p>Отлично! 🌟 Теперь ты умеешь рассказать, в чём ты хорош, и спросить об этом друга.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8)
  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  raise notice 'Homework 2: % блоков', 9;
end $$;
