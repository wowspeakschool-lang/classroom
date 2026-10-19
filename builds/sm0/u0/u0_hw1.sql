-- SM0 · Unit 0 · Homework 1 — восстановлена по плану Lesson 1 (Hello)
-- Собрано скриптом builds/sm0/u0/build.py. Не заливать, пока не назовут,
-- куда переехала платформа: is_published остаётся false в любом случае.
-- Проверка: python3.13 tools/val.py builds/sm0/u0 sm0/legacy

do $$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm0';
  if v_course is null then raise exception 'курс sm0 не найден'; end if;

  select id into v_unit from classroom_units where course_id = v_course and sort_order = 0;
  if v_unit is null then raise exception 'юнит 0 курса sm0 не найден'; end if;

  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and sort_order = 0;
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, kind, sort_order, pass_threshold, is_published)
    values (v_unit, 'Homework 1', 'homework', 0, 60, false)
    returning id into v_lesson;
  else
    update classroom_lessons
       set title = 'Homework 1', kind = 'homework', pass_threshold = 60
     where id = v_lesson;
  end if;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p>Привет! 👋 Сегодня повторим, как знакомиться по-английски, и выучим буквы <b>S</b> и <b>A</b>.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "", "type": "single", "audio": "", "correct": [0], "options": [{"text": "s"}, {"text": "a"}]}, {"q": "", "type": "single", "audio": "", "correct": [1], "options": [{"text": "s"}, {"text": "a"}]}], "needs_review": false, "title": "Послушай звук и выбери букву."}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "<b>S</b>", "type": "single", "correct": [0], "options": [{"text": "s"}, {"text": "a"}, {"text": "t"}]}, {"q": "<b>A</b>", "type": "single", "correct": [1], "options": [{"text": "s"}, {"text": "a"}, {"text": "p"}]}], "needs_review": false, "title": "Это большая буква. Выбери её маленькую пару."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "", "type": "single", "correct": [0], "audio": "", "audio_tts": "What's your name?", "options": [{"text": "I'm Misty.", "audio": "", "audio_tts": "I'm Misty."}, {"text": "How are you?", "audio": "", "audio_tts": "How are you?"}, {"text": "Hello, hello!", "audio": "", "audio_tts": "Hello, hello!"}]}, {"q": "", "type": "single", "correct": [1], "audio": "", "audio_tts": "How are you?", "options": [{"text": "I'm Misty.", "audio": "", "audio_tts": "I'm Misty."}, {"text": "I'm happy!", "audio": "", "audio_tts": "I'm happy!"}, {"text": "What's your name?", "audio": "", "audio_tts": "What's your name?"}]}], "needs_review": false, "title": "Послушай вопрос и выбери ответ."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"words": ["a", "s"], "sentence": "as", "audio": "", "audio_tts": "as"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["s", "a"], "sentence": "sa", "audio": "", "audio_tts": "sa"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'speaking', replace($blk${"title": "Нажми на микрофон и прочитай слоги вслух 🎤", "html": "<p><b>as &nbsp;·&nbsp; sa &nbsp;·&nbsp; AS &nbsp;·&nbsp; SA</b></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'speaking', replace($blk${"title": "Поздоровайся и назови своё имя 🎤", "html": "<p>Нажми на микрофон и скажи: <b>Hello! I’m …</b></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p>Молодец! 🌟 Ты познакомился по-английски и сам прочитал первые слоги — <b>as</b> и <b>sa</b>.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8)
  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  raise notice 'Homework 1: % блоков', 9;
end $$;
