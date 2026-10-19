-- SM3 · Unit 0 · Homework 4 — к уроку Lesson 4
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
   where unit_id = v_unit and sort_order = 3;
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, kind, sort_order, pass_threshold, is_published)
    values (v_unit, 'Homework 4', 'homework', 3, 60, false)
    returning id into v_lesson;
  else
    update classroom_lessons
       set title = 'Homework 4', kind = 'homework', pass_threshold = 60
     where id = v_lesson;
  end if;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p>Привет! 👋 В этой домашке вспоминаем историю <b>«The old book»</b> и тренируем короткие гласные звуки.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'sequence', replace($blk${"title": "Расставь кадры истории по порядку.", "items": [{"text": "", "image": "@@MEDIA@@sm3/u0/story_1.webp"}, {"text": "", "image": "@@MEDIA@@sm3/u0/story_2.webp"}, {"text": "", "image": "@@MEDIA@@sm3/u0/story_3.webp"}, {"text": "", "image": "@@MEDIA@@sm3/u0/story_4.webp"}, {"text": "", "image": "@@MEDIA@@sm3/u0/story_5.webp"}, {"text": "", "image": "@@MEDIA@@sm3/u0/story_6.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'truefalse', replace($blk${"title": "Верно или неверно?", "statements": [{"text": "Lucy and Ben find a secret door.", "correct": true}, {"text": "Buster goes down with Ben and Lucy.", "correct": false}, {"text": "The book is old.", "correct": true}, {"text": "Horax and Zelda want the book.", "correct": true}, {"text": "Zelda ties Ben up.", "correct": false}, {"text": "At the end The Explorers have got the book.", "correct": true}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Кто это сказал?", "questions": [{"q": "“Let’s get them.”", "type": "single", "correct": [0], "options": [{"text": "Zelda"}, {"text": "Lucy"}, {"text": "Buster"}]}, {"q": "“Good dog, Buster!”", "type": "single", "correct": [0], "options": [{"text": "Ben"}, {"text": "Horax"}, {"text": "Zelda"}]}, {"q": "“You can’t keep the book. It’s ours.”", "type": "single", "correct": [0], "options": [{"text": "Lucy"}, {"text": "Horax"}, {"text": "Ben"}]}, {"q": "“It’s ours now! And all the treasure it brings.”", "type": "single", "correct": [0], "options": [{"text": "Horax"}, {"text": "Ben"}, {"text": "Lucy"}]}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери слово, в котором такой же гласный звук.", "questions": [{"q": "<b>cat</b>", "type": "single", "correct": [0], "options": [{"text": "hat"}, {"text": "cake"}, {"text": "car"}]}, {"q": "<b>pet</b>", "type": "single", "correct": [0], "options": [{"text": "ten"}, {"text": "tree"}, {"text": "me"}]}, {"q": "<b>big</b>", "type": "single", "correct": [0], "options": [{"text": "fish"}, {"text": "bike"}, {"text": "five"}]}, {"q": "<b>dog</b>", "type": "single", "correct": [0], "options": [{"text": "box"}, {"text": "nose"}, {"text": "go"}]}, {"q": "<b>cup</b>", "type": "single", "correct": [0], "options": [{"text": "run"}, {"text": "cube"}, {"text": "blue"}]}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["Gus", "pats", "his pets", "a lot."], "sentence": "Gus pats his pets a lot.", "audio": "", "audio_tts": "Gus pats his pets a lot."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "html": "<p>Расскажи историю своими словами, 4–6 предложений: что случилось сначала, что потом и чем всё закончилось. Нажми на микрофон и запиши ответ.</p><p><i>For example:<br>Ben and Lucy are in a castle. Buster finds a secret door…</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p>Молодец! 🌟 Ты вспомнил всю историю и научился слышать короткие гласные звуки.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7)
  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  raise notice 'Homework 4: % блоков', 8;
end $$;
