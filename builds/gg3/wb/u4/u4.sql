-- Go Getter 3, юнит 4 «Useful things» по рабочей тетради: домашки 1–7 (черновики)
update classroom_lessons set sort_order = 10 where id = '2763c9bf-4b1a-4bff-830c-6f5da5c98e2d';

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = '1c0998df-b88e-42e9-ba65-5962093f45cd' and title = 'Homework 1';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('1c0998df-b88e-42e9-ba65-5962093f45cd', 'Homework 1', 0, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 0, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_teen_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 4 · Useful things</h2><p>Сегодня — техника дома: как всё это называется по-английски.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'flashcards', $blk${"title": "Повторяем слова урока. Нажми на карточку — услышишь слово и увидишь перевод", "cards": [{"text": "smart TV", "translation": "умный телевизор", "audio": "", "audio_tts": {"text": "smart TV.", "voice": "en_GB-alba"}}, {"text": "remote control", "translation": "пульт", "audio": "", "audio_tts": {"text": "remote control.", "voice": "en_GB-alba"}}, {"text": "games console", "translation": "игровая приставка", "audio": "", "audio_tts": {"text": "games console.", "voice": "en_GB-alba"}}, {"text": "DVD player", "translation": "DVD-плеер", "audio": "", "audio_tts": {"text": "DVD player.", "voice": "en_GB-alba"}}, {"text": "microwave oven", "translation": "микроволновка", "audio": "", "audio_tts": {"text": "microwave oven.", "voice": "en_GB-alba"}}, {"text": "electric toothbrush", "translation": "электрическая зубная щётка", "audio": "", "audio_tts": {"text": "electric toothbrush.", "voice": "en_GB-alba"}}, {"text": "hairdryer", "translation": "фен", "audio": "", "audio_tts": {"text": "hairdryer.", "voice": "en_GB-alba"}}, {"text": "blender", "translation": "блендер", "audio": "", "audio_tts": {"text": "blender.", "voice": "en_GB-alba"}}, {"text": "toaster", "translation": "тостер", "audio": "", "audio_tts": {"text": "toaster.", "voice": "en_GB-alba"}}, {"text": "USB stick", "translation": "флешка", "audio": "", "audio_tts": {"text": "USB stick.", "voice": "en_GB-alba"}}, {"text": "touch screen", "translation": "сенсорный экран", "audio": "", "audio_tts": {"text": "touch screen.", "voice": "en_GB-alba"}}, {"text": "portable charger", "translation": "внешний аккумулятор", "audio": "", "audio_tts": {"text": "portable charger.", "voice": "en_GB-alba"}}, {"text": "battery", "translation": "батарея", "audio": "", "audio_tts": {"text": "battery.", "voice": "en_GB-alba"}}, {"text": "app", "translation": "приложение", "audio": "", "audio_tts": {"text": "app.", "voice": "en_GB-alba"}}, {"text": "ringtone", "translation": "рингтон", "audio": "", "audio_tts": {"text": "ringtone.", "voice": "en_GB-alba"}}]}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'exact_input', $blk${"title": "Прочитай подсказку и напиши слово по-английски", "items": [{"prompt": "You can watch films and surf the Internet on it (sm… TV)", "accept": ["smart TV", "Smart TV", "smart tv"]}, {"prompt": "The photos from the party are on this (U… s…)", "accept": ["USB stick", "usb stick", "a USB stick"]}, {"prompt": "Let's put a film in it to watch (D… p…)", "accept": ["DVD player", "dvd player", "a DVD player"]}, {"prompt": "The toast is in it. Be careful, it's hot! (t…)", "accept": ["toaster", "Toaster", "a toaster"]}, {"prompt": "Let's make strawberry milkshakes in it (b…)", "accept": ["blender", "Blender", "a blender"]}, {"prompt": "My hair is wet and it isn't working (h…)", "accept": ["hairdryer", "Hairdryer", "a hairdryer", "hair dryer"]}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай разговор Пэм и папы за завтраком и выбери правильное слово", "questions": [{"q": "Dad: Can you put the bread in the ___, please?", "type": "single", "correct": [0], "options": [{"text": "toaster"}, {"text": "blender"}]}, {"q": "Pam: Sure. Do you want me to turn it ___ now?", "type": "single", "correct": [1], "options": [{"text": "off"}, {"text": "on"}]}, {"q": "Dad: No, I can do it in a minute. But you can ___.", "type": "single", "correct": [1], "options": [{"text": "unplug it"}, {"text": "plug it in"}]}, {"q": "Dad: Put some milk in the ___.", "type": "single", "correct": [1], "options": [{"text": "remote control"}, {"text": "microwave oven"}]}, {"q": "Dad: There's a problem with the toaster! It didn't turn ___ and the bread is black now.", "type": "single", "correct": [1], "options": [{"text": "on"}, {"text": "off"}]}]}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'sort', $blk${"title": "Распредели технику по комнатам", "groups": [{"name": "🍳 кухня", "items": [{"text": "blender"}, {"text": "toaster"}, {"text": "microwave oven"}]}, {"name": "🛁 ванная", "items": [{"text": "hairdryer"}, {"text": "electric toothbrush"}]}, {"name": "🛋 гостиная", "items": [{"text": "DVD player"}, {"text": "games console"}, {"text": "smart TV"}, {"text": "remote control"}]}]}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'speaking', $blk${"title": "SPEAKING 🎤 Расскажи вслух и запиши ответ", "needs_review": true, "html": "<p>Расскажи, какой техникой дома ты пользуешься чаще всего и для чего. Три-четыре предложения.</p>", "sample": "", "sample_tts": {"text": "I use the microwave oven every morning.", "voice": "en_GB-alba"}}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_star.webp\" alt=\"\" style=\"height:200px\"></p><p>Отлично! Теперь вся домашняя техника — по-английски.</p>"}$blk$::jsonb, 6);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = '1c0998df-b88e-42e9-ba65-5962093f45cd' and title = 'Homework 2';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('1c0998df-b88e-42e9-ba65-5962093f45cd', 'Homework 2', 1, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 1, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_girl_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 4 · Past Continuous</h2><p>Сегодня — что происходило в какой-то момент в прошлом.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Посмотри на время и впиши глагол в Past Continuous", "mode": "type", "text": "At 3 p.m. yesterday Mark and Dan __weren't watching__ TV. They __were playing__ video games.\nAt 10 a.m. last Sunday my sister __wasn't listening__ to music. She __was helping__ me with my homework.\nAt 6.30 p.m. yesterday Aunt Jane __wasn't reading__ a book. She __was cooking__ dinner."}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'match', $blk${"title": "Соедини вопрос с ответом", "pairs": [{"left": "Were you shopping at 1 p.m., Sarah?", "right": "Yes, I was."}, {"left": "Were the crew filming in the park yesterday?", "right": "Yes, they were."}, {"left": "Was Dad watching a DVD at eight o’clock?", "right": "No, he wasn't. He was reading."}, {"left": "Was Mum drinking tea at four o’clock?", "right": "Yes, she was."}, {"left": "Were you two sitting here a minute ago?", "right": "No, we weren't. We were over there."}, {"left": "Was I talking to your grandma?", "right": "No, you weren't. It was my aunt."}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'order', $blk${"title": "Составь вопросы в Past Continuous", "items": [{"words": ["Was", "Adrianna", "filming", "a", "new", "video", "in", "the", "park?"], "sentence": "Was Adrianna filming a new video in the park?", "prompt": "Адрианна снимала видео?"}, {"words": ["Was", "Harry", "playing", "tennis?"], "sentence": "Was Harry playing tennis?", "prompt": "Гарри играл в теннис?"}, {"words": ["Was", "Emma", "studying", "at", "home?"], "sentence": "Was Emma studying at home?", "prompt": "Эмма занималась дома?"}, {"words": ["Were", "Poppy", "and", "her", "mum", "looking", "for", "a", "hairdryer?"], "sentence": "Were Poppy and her mum looking for a hairdryer?", "prompt": "Поппи с мамой искали фен?"}]}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Впиши короткий ответ: ✔ — да, ✘ — нет", "mode": "type", "text": "Were Poppy and Harry hanging out in the park? ✘ No, __they weren't__.\nWas Adrianna filming a new video in the park? ✔ Yes, __she was__.\nWas Harry playing tennis? ✔ Yes, __he was__.\nWas Emma studying at home? ✘ No, __she wasn't__.\nWere Poppy and her mum looking for a hairdryer? ✔ Yes, __they were__."}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'task', $blk${"title": "WRITING ✍️ Напиши вопросы и ответь на них о себе", "needs_review": true, "html": "<p>Составь вопросы в Past Continuous и ответь правдиво.</p><ol><li>you / take photos / yesterday / 10 a.m.?</li><li>your friend / chat online to you / last Saturday / 8 p.m.?</li><li>you and your classmates / have an English lesson / on Monday / 10 a.m.?</li><li>What / you / do / yesterday / 6 a.m.?</li></ol>"}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_trophy.webp\" alt=\"\" style=\"height:200px\"></p><p>Молодец! Past Continuous теперь понятен.</p>"}$blk$::jsonb, 6);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = '1c0998df-b88e-42e9-ba65-5962093f45cd' and title = 'Homework 3';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('1c0998df-b88e-42e9-ba65-5962093f45cd', 'Homework 3', 2, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 2, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 4 · when и наречия</h2><p>Сегодня — что происходило, когда что-то случилось, и как это происходило.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай историю про доктора Кью и выбери правильную форму", "questions": [{"q": "Doctor Q ___ in his lab one day when Pi flew in.", "type": "single", "correct": [0], "options": [{"text": "was working"}, {"text": "worked"}]}, {"q": "Doctor Q was working in his lab one day when Pi ___ in.", "type": "single", "correct": [1], "options": [{"text": "was flying"}, {"text": "flew"}]}, {"q": "'Doctor Q, I ___ in the garden when I found this strange box.'", "type": "single", "correct": [0], "options": [{"text": "was hopping"}, {"text": "hopped"}]}, {"q": "'I was hopping in the garden when I ___ this strange box.'", "type": "single", "correct": [1], "options": [{"text": "was finding"}, {"text": "found"}]}, {"q": "'Thank you, Pi. I ___ for that box when you came in.'", "type": "single", "correct": [0], "options": [{"text": "was looking"}, {"text": "looked"}]}, {"q": "'I was looking for that box when you ___ in.'", "type": "single", "correct": [1], "options": [{"text": "were coming"}, {"text": "came"}]}]}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'order', $blk${"title": "Составь предложения с when", "items": [{"words": ["I", "was", "reading", "a", "book", "when", "my", "parents", "came", "home."], "sentence": "I was reading a book when my parents came home.", "prompt": "читал книгу, когда пришли родители"}, {"words": ["Dad", "was", "cooking", "in", "the", "kitchen", "when", "we", "opened", "the", "front", "door."], "sentence": "Dad was cooking in the kitchen when we opened the front door.", "prompt": "готовил на кухне, когда мы открыли дверь"}, {"words": ["I", "was", "playing", "a", "game", "when", "the", "twins", "arrived."], "sentence": "I was playing a game when the twins arrived.", "prompt": "играл в игру, когда пришли близнецы"}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай разговор Энн с мамой и впиши глагол в нужной форме", "mode": "type", "text": "Ann: Mum, this morning I __was using__ (use) the blender when it __stopped__ (stop) working.\nMum: That's strange. It worked yesterday.\nAnn: Olga was here. We __put__ (put) strawberries into the blender when Dad __came__ (come) in. The blender __was mixing__ (mix) the strawberries and yogurt when suddenly it __turned off__ (turn off).\nMum: Hmm. Did you ask Dad to fix it?\nAnn: Yes, and he says we need a new blender."}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'match', $blk${"title": "Соедини предложение с продолжением", "pairs": [{"left": "Wendy is good at English.", "right": "She speaks it well."}, {"left": "I don't know a lot of French.", "right": "I speak it badly."}, {"left": "Dave is good at Maths.", "right": "He does his homework easily."}, {"left": "Dogs like running.", "right": "They can go fast."}, {"left": "Grandpa is old.", "right": "He walks slowly."}, {"left": "The baby is sleeping.", "right": "Please talk quietly."}]}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Впиши глагол и наречие: carefully · happily · loudly · politely · fast", "mode": "type", "text": "We __were talking__ __loudly__ (talk) when our teacher came in.\nDad __was running__ __fast__ (run) when I saw him in the park.\nThe dog was playing __happily__ in the garden when it __started__ (start) to rain.\nI __was doing__ the exercise __carefully__ (do) when the teacher came to my desk.\nI was answering the nurse __politely__ when the doctor __came__ (come) in."}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_medal.webp\" alt=\"\" style=\"height:200px\"></p><p>Супер! Теперь понятно, что шло, а что вдруг случилось.</p>"}$blk$::jsonb, 6);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = '1c0998df-b88e-42e9-ba65-5962093f45cd' and title = 'Homework 4';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('1c0998df-b88e-42e9-ba65-5962093f45cd', 'Homework 4', 3, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 3, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_teen_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 4 · Сочувствие</h2><p>Сегодня — как поддержать друга, когда у него неприятность.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'match', $blk${"title": "Соедини начало и конец фразы", "pairs": [{"left": "You", "right": "look upset."}, {"left": "You look", "right": "worried."}, {"left": "What's", "right": "wrong?"}, {"left": "What", "right": "happened?"}, {"left": "I'm so sorry", "right": "to hear that."}, {"left": "That's a", "right": "shame."}]}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай реплику и выбери ответ", "questions": [{"q": "A: What happened to your arm?", "type": "single", "correct": [0], "options": [{"text": "I was ice skating when I fell over."}, {"text": "No, not really."}, {"text": "I went ice skating."}]}, {"q": "B: No, I can't. — Какой была реплика A?", "type": "single", "correct": [2], "options": [{"text": "Can I help?"}, {"text": "You look upset."}, {"text": "That's terrible. Can you write?"}]}, {"q": "B: Yes, please. I'd like some help. — Какой была реплика A?", "type": "single", "correct": [0], "options": [{"text": "I'm so sorry. Can I help?"}, {"text": "I'm so sorry to hear that."}, {"text": "What's wrong?"}]}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай разговор Зака и Вики и впиши пропущенное слово", "mode": "type", "text": "Zach: You look upset. What's __wrong__?\nVicky: I __was__ doing my homework __when__ I dropped my calculator. Now it doesn't work.\nZach: That's a __shame__. Can I __help__?\nVicky: __No__, not really. I can't do my Maths without a calculator.\nZach: Why don't __you__ ask your brother for help? He's good at Maths.\nVicky: That's a good idea. Thanks."}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'order', $blk${"title": "Составь фразы поддержки", "items": [{"words": ["You", "look", "worried."], "sentence": "You look worried.", "prompt": "ты выглядишь расстроенным"}, {"words": ["What's", "happened?"], "sentence": "What's happened?", "prompt": "что случилось?"}, {"words": ["I", "was", "calling", "Mum", "when", "my", "phone", "broke."], "sentence": "I was calling Mum when my phone broke.", "prompt": "звонил маме, когда телефон сломался"}, {"words": ["That's", "terrible."], "sentence": "That's terrible.", "prompt": "какой ужас"}]}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'speaking', $blk${"title": "SPEAKING 🎤 Разыграй разговор и запиши ответ", "needs_review": true, "html": "<p>Твой друг промок под дождём, и его собака тоже. Поддержи его: заметь, что он расстроен, спроси, что случилось, посочувствуй и предложи помощь.</p>", "sample": "", "sample_tts": {"text": "You look upset. What happened?", "voice": "en_GB-alba"}}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_thumb.webp\" alt=\"\" style=\"height:200px\"></p><p>Отлично! Теперь ты знаешь, что сказать другу в трудный момент.</p>"}$blk$::jsonb, 6);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = '1c0998df-b88e-42e9-ba65-5962093f45cd' and title = 'Homework 5';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('1c0998df-b88e-42e9-ba65-5962093f45cd', 'Homework 5', 4, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 4, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_girl_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 4 · Reading</h2><p>Сегодня читаем рассказ Джоша про первую игровую приставку его папы.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<h3>Read my dad’s story! <span style=\"color:#888\">by Josh</span></h3><p>‘In 1990 I was a young boy. It was an autumn day in town. I was walking down the High Street with my mum when I stopped because I wanted to look in a shop window. I was feeling very excited because I saw something very special in the shop.</p><p>That special thing was a new games console. But it wasn't just a normal games console. It was the first portable games console.</p><p>That day was my birthday. I had some money to spend and I was looking for a present to buy when I saw that games console.</p><p>I bought it and I was really happy. The games console had four buttons on it, it took headphones and it also had a battery pack that you plugged in. There weren't a lot of games at first – in fact, I had only two. I loved computer games, so I played a lot!’</p><p>And now my dad has a fantastic job! He is a game tester! He plays games before they sell them in the shops. Amazing! So, he still loves computer games and he plays a lot.</p>"}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай рассказ и выбери правильный ответ", "questions": [{"q": "What year was it?", "type": "single", "correct": [0], "options": [{"text": "It was 1990."}, {"text": "It was 1999."}, {"text": "It was 2009."}]}, {"q": "Where was the young boy walking?", "type": "single", "correct": [1], "options": [{"text": "in the park"}, {"text": "down the High Street"}, {"text": "in a shopping centre"}]}, {"q": "Why did he stop?", "type": "single", "correct": [1], "options": [{"text": "because he was tired"}, {"text": "because he wanted to look in a shop window"}, {"text": "because his mum called him"}]}, {"q": "What day was it?", "type": "single", "correct": [0], "options": [{"text": "his birthday"}, {"text": "Christmas Day"}, {"text": "the first day of school"}]}, {"q": "Were there a lot of games for the console?", "type": "single", "correct": [0], "options": [{"text": "No, there weren't. He had only two."}, {"text": "Yes, there were a lot."}]}], "material": "<h3>Read my dad’s story! <span style=\"color:#888\">by Josh</span></h3><p>‘In 1990 I was a young boy. It was an autumn day in town. I was walking down the High Street with my mum when I stopped because I wanted to look in a shop window. I was feeling very excited because I saw something very special in the shop.</p><p>That special thing was a new games console. But it wasn't just a normal games console. It was the first portable games console.</p><p>That day was my birthday. I had some money to spend and I was looking for a present to buy when I saw that games console.</p><p>I bought it and I was really happy. The games console had four buttons on it, it took headphones and it also had a battery pack that you plugged in. There weren't a lot of games at first – in fact, I had only two. I loved computer games, so I played a lot!’</p><p>And now my dad has a fantastic job! He is a game tester! He plays games before they sell them in the shops. Amazing! So, he still loves computer games and he plays a lot.</p>"}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Эти предложения про рассказ неверные. Выбери, как правильно", "questions": [{"q": "It was winter.", "type": "single", "correct": [0], "options": [{"text": "It was autumn."}, {"text": "It was summer."}]}, {"q": "The boy was excited about an old games console in the shop.", "type": "single", "correct": [0], "options": [{"text": "He was excited about a new games console."}, {"text": "He was excited about a new phone."}]}, {"q": "The games console had five buttons.", "type": "single", "correct": [0], "options": [{"text": "It had four buttons."}, {"text": "It had two buttons."}]}, {"q": "Josh's dad had three games.", "type": "single", "correct": [0], "options": [{"text": "He had only two games."}, {"text": "He had ten games."}]}], "material": "<h3>Read my dad’s story! <span style=\"color:#888\">by Josh</span></h3><p>‘In 1990 I was a young boy. It was an autumn day in town. I was walking down the High Street with my mum when I stopped because I wanted to look in a shop window. I was feeling very excited because I saw something very special in the shop.</p><p>That special thing was a new games console. But it wasn't just a normal games console. It was the first portable games console.</p><p>That day was my birthday. I had some money to spend and I was looking for a present to buy when I saw that games console.</p><p>I bought it and I was really happy. The games console had four buttons on it, it took headphones and it also had a battery pack that you plugged in. There weren't a lot of games at first – in fact, I had only two. I loved computer games, so I played a lot!’</p><p>And now my dad has a fantastic job! He is a game tester! He plays games before they sell them in the shops. Amazing! So, he still loves computer games and he plays a lot.</p>"}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай разговор Ребекки с дедушкой и перетащи слова в пропуски", "mode": "drag", "text": "Grandad: I want to buy a smartphone.\nRebecca: Do you know anything about them, Grandad?\nGrandad: Yes, I do. I know they have __touch screens__, not buttons, and that you can download __apps__.\nRebecca: Yes, that's right. You can also choose different __ringtones__ for different people.\nGrandad: Can I get those from the Internet?\nRebecca: Yes. Now look at my phone. It has a very good __battery__. It lasts for ten hours.\nGrandad: That's good. Do I need to buy a __portable charger__ too?\nRebecca: No. It comes with the phone.\nGrandad: Thanks, Rebecca."}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'task', $blk${"title": "WRITING ✍️ Напиши про свой любимый гаджет", "needs_review": true, "html": "<p>Четыре-пять предложений: что это, когда он у тебя появился, что ты с ним делаешь и почему он тебе нравится.</p>"}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_popper.webp\" alt=\"\" style=\"height:200px\"></p><p>Здорово! История прочитана, свой гаджет описан.</p>"}$blk$::jsonb, 6);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = '1c0998df-b88e-42e9-ba65-5962093f45cd' and title = 'Homework 6';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('1c0998df-b88e-42e9-ba65-5962093f45cd', 'Homework 6', 5, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 5, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 4 · Listening and Writing</h2><p>Сегодня слушаем две смешные истории и пишем свою.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'exact_input', $blk${"title": "Напиши название чувства по-английски", "items": [{"prompt": "заинтересованный (i…)", "accept": ["interested", "Interested"]}, {"prompt": "счастливый (h…)", "accept": ["happy", "Happy"]}, {"prompt": "грустный (s…)", "accept": ["sad", "Sad"]}, {"prompt": "уставший (t…)", "accept": ["tired", "Tired"]}, {"prompt": "испуганный (s…)", "accept": ["scared", "Scared"]}, {"prompt": "встревоженный (w…)", "accept": ["worried", "Worried"]}]}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "LISTENING 🎧 Послушай две истории и выбери правильный ответ", "audio": "https://api.wowteach.ru/storage/v1/object/public/classroom-media/gg3%20wb/GG%20L3%20WkBk%20A10.mp3", "skill": "listening", "questions": [{"q": "Story 1 is about …", "type": "single", "correct": [2], "options": [{"text": "an angry brother"}, {"text": "a school ski trip"}, {"text": "birthday food"}, {"text": "an interesting holiday"}]}, {"q": "Story 2 is about …", "type": "single", "correct": [3], "options": [{"text": "an angry brother"}, {"text": "a school ski trip"}, {"text": "birthday food"}, {"text": "an interesting holiday"}]}, {"q": "Why did the cake go wrong in Story 1?", "type": "single", "correct": [1], "options": [{"text": "the oven was broken"}, {"text": "the dog ate the cake mix"}, {"text": "there wasn’t any sugar"}]}, {"q": "Why did they stay two extra days in Story 2?", "type": "single", "correct": [0], "options": [{"text": "the road was closed because of the snow"}, {"text": "the hotel was very cheap"}, {"text": "Dad was ill"}]}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "LISTENING 🎧 Послушай истории ещё раз и впиши по одному слову", "mode": "type", "text": "Story 1\nIt was my __brother's__ birthday. I was making a __cake__. __Twenty__ minutes later I was watching TV. The __dog__ was eating the cake mix when I walked in. Mum ordered __pizza__.\nStory 2\n__Dad__ and I were staying in a hotel in the mountains. We were on a __skiing__ holiday. On __Saturday__ there was snow everywhere. We looked for the __road__, but we couldn't see it. We stayed for __two__ extra days."}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай историю Тины и впиши глагол в нужной форме", "mode": "type", "text": "Last Monday I __was__ sitting in the classroom at my desk. My best friend, Tom, __was__ talking loudly and his brother, Fred, was laughing. We __were__ waiting for our teacher, but she was late. Finally, she came in the classroom with a hamster in a box. It was her pet hamster. Tom and Fred were quiet. We __were__ looking into the box when the hamster came out of its little house. It was brown and it had a pink nose. I think it felt a bit scared at first. But five minutes later it __was__ eating a carrot and it was happy."}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'task', $blk${"title": "WRITING ✍️ Напиши историю про урок с собакой учителя", "needs_review": true, "html": "<p>Представь: учитель принёс в класс свою собаку. Напиши историю из пяти-шести предложений.</p><p>Сначала задай обстановку (Past Continuous), потом расскажи, что случилось (Past Simple или Past Continuous с <b>when</b>), в конце — чем всё закончилось и что ты почувствовал.</p><p>Слова-помощники: big, dark, ears, friendly, jump, (not) interested, legs, long, quickly, run, (not) scared, walk.</p><p>Начни так: <i>Last Friday …</i></p>"}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_certificate.webp\" alt=\"\" style=\"height:200px\"></p><p>Отлично! И послушали, и свою историю написали.</p>"}$blk$::jsonb, 6);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = '1c0998df-b88e-42e9-ba65-5962093f45cd' and title = 'Homework 7';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('1c0998df-b88e-42e9-ba65-5962093f45cd', 'Homework 7', 6, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 6, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_teen_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 4 · Check yourself!</h2><p>Повторяем весь юнит перед тестом.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай короткие разговоры и впиши название техники", "mode": "type", "text": "A: I'd like some hot milk.\nB: Put a mug of milk in the __microwave oven__.\nA: My hair is wet.\nB: You need a __hairdryer__.\nA: Let's watch TV.\nB: OK. Where's the __remote control__?\nA: Can I make a smoothie?\nB: Yes. You have to plug in the __blender__ first.\nA: I bought a new film.\nB: Cool, let's watch it! Put it in the __DVD player__.\nA: Your teeth are very white.\nB: Thanks. I've got a new __electric toothbrush__."}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Выбери правильный вариант", "questions": [{"q": "There's a good film on tonight. Let's watch it on my ___.", "type": "single", "correct": [0], "options": [{"text": "smart TV"}, {"text": "toaster"}, {"text": "portable charger"}]}, {"q": "Grandpa's old mobile phone doesn't have a ___.", "type": "single", "correct": [2], "options": [{"text": "games console"}, {"text": "ringtone"}, {"text": "touch screen"}]}, {"q": "You must speak ___. Grandma can't hear very well.", "type": "single", "correct": [1], "options": [{"text": "quietly"}, {"text": "loudly"}, {"text": "badly"}]}, {"q": "'Why doesn't your TV work?' 'Because you didn't ___.'", "type": "single", "correct": [0], "options": [{"text": "plug it in"}, {"text": "turn it off"}, {"text": "unplug it"}]}, {"q": "I walked to school ___, so I was late.", "type": "single", "correct": [2], "options": [{"text": "easily"}, {"text": "fast"}, {"text": "slowly"}]}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Впиши глагол в Past Continuous: do · listen · play · not tidy · watch", "mode": "type", "text": "A: Where's Fred? He __was doing__ his homework an hour ago.\nB: His friends __were playing__ football in the park an hour ago and he wanted to play too.\nA: Sally and Tina __weren't tidying__ their room at six o'clock because they weren't at home. Where were they?\nB: Don't worry. They did it at five o'clock. I think they __were watching__ TV at Jane's house.\nA: I phoned you at ten, but you didn't answer. __Were you listening__ to your music?\nB: Yes, __I was__! I didn't hear the phone."}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай историю про пса Рекса и впиши глагол в нужной форме", "mode": "type", "text": "I __was walking__ (walk) home when I __saw__ (see) Uncle George in his car. He __was turning__ (turn) right when a tired hungry dog __ran__ (run) into the road. Luckily, Uncle George __was driving__ (drive) slowly when the dog __went__ (go) in front of his car and he stopped. Now Rex lives with Uncle George! Uncle George loves Rex and Rex loves Uncle George."}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай разговор и выбери правильный вариант", "questions": [{"q": "A: You ___ upset.", "type": "single", "correct": [1], "options": [{"text": "worried"}, {"text": "look"}]}, {"q": "A: What's ___?", "type": "single", "correct": [0], "options": [{"text": "wrong"}, {"text": "happened"}]}, {"q": "B: I was shopping ___ I lost my phone.", "type": "single", "correct": [1], "options": [{"text": "where"}, {"text": "when"}]}, {"q": "A: That's ___! Can I help?", "type": "single", "correct": [1], "options": [{"text": "shame"}, {"text": "terrible"}]}, {"q": "A: That's terrible! Can ___ help?", "type": "single", "correct": [0], "options": [{"text": "I"}, {"text": "you"}]}, {"q": "A: I'm ___ to hear that. I hope you find it.", "type": "single", "correct": [0], "options": [{"text": "so sorry"}, {"text": "so worry"}]}]}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'speaking', $blk${"title": "SPEAKING 🎤 Расскажи вслух и запиши ответ", "needs_review": true, "html": "<p>Расскажи про случай, когда техника подвела: что ты делал, что случилось и чем всё закончилось. Три-четыре предложения в прошедшем времени.</p>", "sample": "", "sample_tts": {"text": "Last week I was watching a film when the TV stopped working.", "voice": "en_GB-alba"}}$blk$::jsonb, 6);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_trophy.webp\" alt=\"\" style=\"height:200px\"></p><p>Юнит пройден! Можно браться за тест.</p>"}$blk$::jsonb, 7);
end $$;
