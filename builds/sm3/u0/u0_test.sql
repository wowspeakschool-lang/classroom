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
    (v_lesson, 'text', replace($blk${"html": "<p><b>READING.</b> Прочитай текст и ответь, верно или неверно.</p><p>Nick is nine years old. He lives in a big house with his mum, his dad and his sister Penny. His bedroom is upstairs and the kitchen is downstairs. There are a lot of old boxes in the cellar. Nick is good at riding a bike and playing football, but he isn’t good at swimming. His cousin Zoe is eight. She is good at painting, and she loves her grandmother Julia.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'truefalse', replace($blk${"title": "Верно или неверно?", "statements": [{"text": "Nick is nine years old.", "correct": true}, {"text": "Nick’s bedroom is downstairs.", "correct": false}, {"text": "There are old boxes in the cellar.", "correct": true}, {"text": "Nick is good at swimming.", "correct": false}, {"text": "Zoe is Nick’s cousin.", "correct": true}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'text', replace($blk${"html": "<p><b>LISTENING 🎧</b> Послушай рассказ про Пенни. Текста не будет — слушай и отвечай на вопросы ниже. Можно послушать два раза.</p>", "audio": "", "audio_tts": "This is Penny. Penny is seven years old. She lives with her mum Claire, her dad Ted and her brother Nick. Penny’s bedroom is upstairs. Penny is good at dancing and she is good at telling stories, but she isn’t good at swimming. Her grandmother Julia is good at making cakes. Penny has got twenty-four books in her room."}$blk$, '@@MEDIA@@', v_media)::jsonb, 15),
    (v_lesson, 'quiz', replace($blk${"title": "Послушай ещё раз и выбери правильный ответ.", "questions": [{"q": "How old is Penny?", "type": "single", "correct": [0], "options": [{"text": "seven"}, {"text": "nine"}, {"text": "twenty-four"}]}, {"q": "Where is Penny’s bedroom?", "type": "single", "correct": [0], "options": [{"text": "upstairs"}, {"text": "downstairs"}, {"text": "in the cellar"}]}, {"q": "What is Penny NOT good at?", "type": "single", "correct": [0], "options": [{"text": "swimming"}, {"text": "dancing"}, {"text": "telling stories"}]}, {"q": "Who is good at making cakes?", "type": "single", "correct": [0], "options": [{"text": "her grandmother"}, {"text": "her mum"}, {"text": "her brother"}]}, {"q": "How many books has Penny got?", "type": "single", "correct": [0], "options": [{"text": "24"}, {"text": "14"}, {"text": "42"}]}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 16),
    (v_lesson, 'exact_input', replace($blk${"title": "DICTATION ✍️ Послушай предложение и запиши его целиком.", "needs_review": false, "items": [{"audio": "", "audio_tts": "Nick is good at playing football.", "prompt": "1.", "accept": ["Nick is good at playing football.", "Nick is good at playing football"]}, {"audio": "", "audio_tts": "The cellar is under the house.", "prompt": "2.", "accept": ["The cellar is under the house.", "The cellar is under the house"]}, {"audio": "", "audio_tts": "Penny is Jack’s granddaughter.", "prompt": "3.", "accept": ["Penny is Jack’s granddaughter.", "Penny is Jack’s granddaughter", "Penny is Jack's granddaughter.", "Penny is Jack's granddaughter"]}, {"audio": "", "audio_tts": "There are twenty-four books in the room.", "prompt": "4.", "accept": ["There are twenty-four books in the room.", "There are twenty-four books in the room"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 17),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "html": "<p>Расскажи про себя и свою семью, 5–7 предложений. Нажми на микрофон и запиши ответ.</p><p><i>For example:<br>I’m good at swimming, but I’m not good at painting.<br>This is my mum’s sister. She’s my aunt.<br>Her son is my cousin.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 18),
    (v_lesson, 'text', replace($blk${"html": "<p>Ты справился! 🌟 Это был тест за весь нулевой юнит: числа, комнаты, be good at, семья и история про The Explorers.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 19)
  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  raise notice 'Test: % блоков', 20;
end $$;
