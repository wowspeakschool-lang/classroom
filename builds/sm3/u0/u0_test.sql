-- SM3 · Unit 0 · Test — к уроку Lesson 5 «Revision + Test»
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
   where unit_id = v_unit and sort_order = 5;
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, kind, sort_order, pass_threshold, is_published)
    values (v_unit, 'Test', 'test', 5, 90, false)
    returning id into v_lesson;
  else
    update classroom_lessons
       set title = 'Test', kind = 'test', pass_threshold = 90
     where id = v_lesson;
  end if;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p>Сегодня у нас с тобой тест по нулевому юниту. Проверим числа, be good at, семью и историю про The Explorers. Уверена, ты справишься!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Послушай и выбери число.", "questions": [{"q": "", "type": "single", "correct": [0], "options": [{"text": "24"}, {"text": "42"}, {"text": "14"}], "audio": "", "audio_tts": "twenty-four"}, {"q": "", "type": "single", "correct": [1], "options": [{"text": "93"}, {"text": "39"}, {"text": "49"}], "audio": "", "audio_tts": "thirty-nine"}, {"q": "", "type": "single", "correct": [0], "options": [{"text": "52"}, {"text": "25"}, {"text": "15"}], "audio": "", "audio_tts": "fifty-two"}, {"q": "", "type": "single", "correct": [1], "options": [{"text": "67"}, {"text": "76"}, {"text": "70"}], "audio": "", "audio_tts": "seventy-six"}, {"q": "", "type": "single", "correct": [2], "options": [{"text": "10"}, {"text": "90"}, {"text": "100"}], "audio": "", "audio_tts": "one hundred"}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери пропущенное слово.", "questions": [{"q": "A: Where’s your bedroom?<br>B: It’s ___. My room is on the second floor.", "type": "single", "correct": [0], "options": [{"text": "upstairs"}, {"text": "downstairs"}, {"text": "in the cellar"}]}, {"q": "A: Where’s the kitchen?<br>B: It’s ___, next to the front door.", "type": "single", "correct": [1], "options": [{"text": "upstairs"}, {"text": "downstairs"}, {"text": "in the cellar"}]}, {"q": "A: It’s dark here and there are a lot of old boxes. Where are you?<br>B: I’m ___.", "type": "single", "correct": [2], "options": [{"text": "upstairs"}, {"text": "downstairs"}, {"text": "in the cellar"}]}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант.", "questions": [{"q": "She’s good at ___ the guitar.", "type": "single", "correct": [0], "options": [{"text": "playing"}, {"text": "play"}, {"text": "plays"}]}, {"q": "I’m not good at ___ lies.", "type": "single", "correct": [0], "options": [{"text": "telling"}, {"text": "tell"}, {"text": "to tell"}]}, {"q": "___ you good at swimming?", "type": "single", "correct": [0], "options": [{"text": "Are"}, {"text": "Do"}, {"text": "Is"}]}, {"q": "Ben and Lucy ___ good at climbing trees.", "type": "single", "correct": [0], "options": [{"text": "are"}, {"text": "is"}, {"text": "do"}]}, {"q": "Lucy isn’t good ___ painting.", "type": "single", "correct": [0], "options": [{"text": "at"}, {"text": "in"}, {"text": "on"}]}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"words": ["I’m", "good at", "riding", "a bike."], "sentence": "I’m good at riding a bike.", "audio": "", "audio_tts": "I’m good at riding a bike."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["She", "isn’t", "good at", "playing", "football."], "sentence": "She isn’t good at playing football.", "audio": "", "audio_tts": "She isn’t good at playing football."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["Nick", "is", "Julia’s", "grandson."], "sentence": "Nick is Julia’s grandson.", "audio": "", "audio_tts": "Nick is Julia’s grandson."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["Paula and Zoe", "are", "Nick’s", "cousins."], "sentence": "Paula and Zoe are Nick’s cousins.", "audio": "", "audio_tts": "Paula and Zoe are Nick’s cousins."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант.", "questions": [{"q": "Tom is Simon___ father.", "type": "single", "correct": [0], "options": [{"text": "’s"}, {"text": "s"}, {"text": "s’"}]}, {"q": "She’s Greg___ sister.", "type": "single", "correct": [0], "options": [{"text": "’s"}, {"text": "s"}, {"text": "s’"}]}, {"q": "Nick’s dog is big. Who has got the dog?", "type": "single", "correct": [0], "options": [{"text": "Nick"}, {"text": "the dog"}, {"text": "Nick’s friend"}]}, {"q": "Jack is Nick’s grandfather. So Nick is Jack’s ___.", "type": "single", "correct": [0], "options": [{"text": "grandson"}, {"text": "son"}, {"text": "uncle"}]}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p><b>Посмотри на семейное дерево и впиши слово.</b></p><p style=\"text-align:center\"><img src=\"@@MEDIA@@sm3/u0/family_tree.webp\" alt=\"\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'exact_input', replace($blk${"items": [{"prompt": "1. Julia is Penny’s ___.", "accept": ["grandmother", "Grandmother"]}, {"prompt": "2. Jack is Paula’s ___.", "accept": ["grandfather", "Grandfather"]}, {"prompt": "3. Paula is Zoe’s ___.", "accept": ["sister", "Sister"]}, {"prompt": "4. Zoe is Nick’s ___.", "accept": ["cousin", "Cousin"]}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'truefalse', replace($blk${"title": "История «The old book» — верно или неверно?", "statements": [{"text": "Ben and Lucy are in a castle.", "correct": true}, {"text": "Ben and Lucy find an old book.", "correct": true}, {"text": "Horax and Zelda help Ben and Lucy.", "correct": false}, {"text": "Zelda ties Lucy up.", "correct": true}, {"text": "Buster helps The Explorers to get the book back.", "correct": true}, {"text": "Horax and Zelda have got the book at the end.", "correct": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери слово, в котором такой же гласный звук.", "questions": [{"q": "<b>cat</b>", "type": "single", "correct": [0], "options": [{"text": "hat"}, {"text": "cake"}, {"text": "car"}]}, {"q": "<b>pet</b>", "type": "single", "correct": [0], "options": [{"text": "ten"}, {"text": "tree"}, {"text": "me"}]}, {"q": "<b>big</b>", "type": "single", "correct": [0], "options": [{"text": "fish"}, {"text": "bike"}, {"text": "five"}]}, {"q": "<b>cup</b>", "type": "single", "correct": [0], "options": [{"text": "run"}, {"text": "cube"}, {"text": "blue"}]}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "html": "<p>Расскажи про себя и свою семью, 5–7 предложений. Нажми на микрофон и запиши ответ.</p><p><i>For example:<br>I’m good at swimming, but I’m not good at painting.<br>This is my mum’s sister. She’s my aunt.<br>Her son is my cousin.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'text', replace($blk${"html": "<p>Ты справился! 🌟 Это был тест за весь нулевой юнит: числа, комнаты, be good at, семья и история про The Explorers.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 14)
  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  raise notice 'Test: % блоков', 15;
end $$;
