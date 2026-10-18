-- SM3 · Unit 0 · Homework 3 — к уроку Lesson 3
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
   where unit_id = v_unit and sort_order = 2;
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, kind, sort_order, pass_threshold, is_published)
    values (v_unit, 'Homework 3', 'homework', 2, 60, false)
    returning id into v_lesson;
  else
    update classroom_lessons
       set title = 'Homework 3', kind = 'homework', pass_threshold = 60
     where id = v_lesson;
  end if;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p>Привет! 👋 В этой домашке — семья и маленькая буква <b>’s</b>, которая показывает, чей это человек или предмет.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p><b>Посмотри на семейное дерево — оно понадобится в заданиях.</b></p><p style=\"text-align:center\"><img src=\"@@MEDIA@@sm3/u0/family_tree.webp\" alt=\"\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на дерево и выбери правильный вариант.", "questions": [{"q": "Nick is Penny’s ___.", "type": "single", "correct": [0], "options": [{"text": "brother"}, {"text": "father"}, {"text": "cousin"}]}, {"q": "Paula is Zoe’s ___.", "type": "single", "correct": [1], "options": [{"text": "cousin"}, {"text": "sister"}, {"text": "aunt"}]}, {"q": "Ted is Penny’s ___.", "type": "single", "correct": [1], "options": [{"text": "uncle"}, {"text": "father"}, {"text": "grandfather"}]}, {"q": "Lisa is Paula’s ___.", "type": "single", "correct": [0], "options": [{"text": "mother"}, {"text": "sister"}, {"text": "aunt"}]}, {"q": "Oliver is Nick’s ___.", "type": "single", "correct": [0], "options": [{"text": "uncle"}, {"text": "grandfather"}, {"text": "brother"}]}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'exact_input', replace($blk${"title": "Посмотри на дерево и впиши слово.", "items": [{"prompt": "1. Julia is Nick’s ___.", "accept": ["grandmother", "Grandmother"]}, {"prompt": "2. Nick is Jack’s ___.", "accept": ["grandson", "Grandson"]}, {"prompt": "3. Zoe is Penny’s ___.", "accept": ["cousin", "Cousin"]}, {"prompt": "4. Lisa is Nick’s ___.", "accept": ["aunt", "Aunt"]}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант.", "questions": [{"q": "This is Nick___ dog.", "type": "single", "correct": [0], "options": [{"text": "’s"}, {"text": "s"}, {"text": "s’"}]}, {"q": "Penny is Ted___ daughter.", "type": "single", "correct": [0], "options": [{"text": "’s"}, {"text": "s"}, {"text": "s’"}]}, {"q": "«Julia’s son» — у кого есть сын?", "type": "single", "correct": [0], "options": [{"text": "Julia"}, {"text": "the son"}, {"text": "Jack"}]}, {"q": "Paula and Zoe are Oliver and Lisa___ daughters.", "type": "single", "correct": [0], "options": [{"text": "’s"}, {"text": "s"}, {"text": "s’"}]}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["Penny", "is", "Jack’s", "granddaughter."], "sentence": "Penny is Jack’s granddaughter.", "audio": "", "audio_tts": "Penny is Jack’s granddaughter."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["Zoe", "is", "Lisa’s", "daughter."], "sentence": "Zoe is Lisa’s daughter.", "audio": "", "audio_tts": "Zoe is Lisa’s daughter."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["This", "is", "my mum’s", "brother."], "sentence": "This is my mum’s brother.", "audio": "", "audio_tts": "This is my mum’s brother."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "html": "<p>Расскажи про свою семью, 5–6 предложений. Используй ’s. Нажми на микрофон и запиши ответ.</p><p><i>For example:<br>This is my mum’s sister. She’s my aunt.<br>Her son is my cousin.<br>My dad’s father is my grandfather.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p>Молодец! 🌟 Теперь ты умеешь рассказать, кто кому кем приходится, и не путаешь ’s.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9)
  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  raise notice 'Homework 3: % блоков', 10;
end $$;
