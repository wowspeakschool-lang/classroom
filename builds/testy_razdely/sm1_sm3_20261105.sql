-- Добавляем недостающие разделы в четыре теста (решение Анны 05.11.2026, «5 да»).
-- SM1 Unit 0 Test: диктант + reading
-- SM1 Unit 1 Test: reading
-- SM3 Unit 9 Test: диктант + reading + listening
-- SM3 Final Test:  диктант + speaking
-- Существующие блоки не переставляем, только вставляем новые и сдвигаем нумерацию.

do $$
declare
  v_media text := 'https://classroom.wowteach.ru/media/';
  L1 uuid := '436d7600-4022-4e42-967c-f30e9e8f16b4'; -- SM1 Unit 0 Test
  L2 uuid := 'bb8d9c5c-f3c0-4551-9bfe-a7a1e029f83e'; -- SM1 Unit 1 Test
  L3 uuid := '4e03c20d-2801-4854-9149-4f5f2fa7c67f'; -- SM3 Unit 9 Test
  L4 uuid := 'c14c128d-fcfc-461a-9854-b6014237565f'; -- SM3 Final Test
begin

-- копия всех блоков четырёх уроков
create table if not exists classroom_backup_razdely_testov_20261105 as
  select * from classroom_blocks where lesson_id in (L1, L2, L3, L4);

-- ---------- сдвиг ----------
update classroom_blocks set sort_order = sort_order + 1000 where lesson_id in (L1, L2, L3, L4);

-- ---------- SM1 Unit 0 Test ----------
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
(L1, 'exact_input', replace($b$ {"skill": "writing",
  "title": "DICTATION ✍️ Посмотри на картинку и напиши слово",
  "items": [
    {"image": "@@MEDIA@@sm1/old/color_red.webp",    "accept": ["red", "Red"],       "prompt": "r _ d    (красный)"},
    {"image": "@@MEDIA@@sm1/old/color_blue.webp",   "accept": ["blue", "Blue"],     "prompt": "b l _ e    (синий)"},
    {"image": "@@MEDIA@@sm1/old/color_green.webp",  "accept": ["green", "Green"],   "prompt": "g r _ _ n    (зелёный)"},
    {"image": "@@MEDIA@@sm1/old/color_yellow.webp", "accept": ["yellow", "Yellow"], "prompt": "y _ l l _ w    (жёлтый)"},
    {"image": "@@MEDIA@@sm1/old/color_orange.webp", "accept": ["orange", "Orange"], "prompt": "o r _ n g e    (оранжевый)"}
  ]} $b$, '@@MEDIA@@', v_media)::jsonb, 2),
(L1, 'quiz', $b$ {"skill": "reading",
  "title": "READING. Прочитай и выбери: верно или неверно",
  "material": "<p>Hi! I’m Misty. I’m seven. My favourite colour is blue.</p><p>Hi! I’m Flash. I’m nine. My favourite colour is red.</p>",
  "questions": [
    {"q": "<p><b>Misty is seven.</b></p>",            "type": "single", "correct": [0], "options": [{"text": "Верно"}, {"text": "Неверно"}]},
    {"q": "<p><b>Misty’s favourite colour is red.</b></p>", "type": "single", "correct": [1], "options": [{"text": "Верно"}, {"text": "Неверно"}]},
    {"q": "<p><b>Flash is nine.</b></p>",             "type": "single", "correct": [0], "options": [{"text": "Верно"}, {"text": "Неверно"}]},
    {"q": "<p><b>Flash’s favourite colour is blue.</b></p>", "type": "single", "correct": [1], "options": [{"text": "Верно"}, {"text": "Неверно"}]}
  ]} $b$::jsonb, 7);

update classroom_blocks set sort_order = case sort_order - 1000
    when 0 then 0 when 1 then 1
    when 2 then 3 when 3 then 4 when 4 then 5 when 5 then 6
    when 6 then 8 when 7 then 9 end
  where lesson_id = L1 and sort_order >= 1000;

-- ---------- SM1 Unit 1 Test ----------
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
(L2, 'quiz', $b$ {"skill": "reading",
  "title": "READING. Прочитай и выбери: верно или неверно",
  "material": "<p>This is my school bag. I’ve got a red pen and a blue book. My pencil case is yellow. I’ve got a ruler, too. I haven’t got a rubber.</p>",
  "questions": [
    {"q": "<p><b>The pen is red.</b></p>",                  "type": "single", "correct": [0], "options": [{"text": "Верно"}, {"text": "Неверно"}]},
    {"q": "<p><b>The book is green.</b></p>",               "type": "single", "correct": [1], "options": [{"text": "Верно"}, {"text": "Неверно"}]},
    {"q": "<p><b>The pencil case is yellow.</b></p>",       "type": "single", "correct": [0], "options": [{"text": "Верно"}, {"text": "Неверно"}]},
    {"q": "<p><b>There is a rubber in the bag.</b></p>",    "type": "single", "correct": [1], "options": [{"text": "Верно"}, {"text": "Неверно"}]}
  ]} $b$::jsonb, 8);

update classroom_blocks set sort_order = case when sort_order - 1000 <= 7 then sort_order - 1000
                                              else sort_order - 1000 + 1 end
  where lesson_id = L2 and sort_order >= 1000;

-- ---------- SM3 Unit 9 Test ----------
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
(L3, 'exact_input', replace($b$ {"skill": "writing",
  "title": "DICTATION ✍️ Посмотри на картинку и напиши слово",
  "items": [
    {"image": "@@MEDIA@@sm3/u9/clothes_umbrella.webp", "accept": ["umbrella", "Umbrella"], "prompt": "зонт"},
    {"image": "@@MEDIA@@sm3/u9/clothes_boots.webp",    "accept": ["boots", "Boots"],       "prompt": "резиновые сапоги"},
    {"image": "@@MEDIA@@sm3/u9/clothes_raincoat.webp", "accept": ["raincoat", "Raincoat"], "prompt": "дождевик"},
    {"image": "@@MEDIA@@sm3/u9/weather_cloudy.webp",   "accept": ["cloudy", "Cloudy"],     "prompt": "облачно"},
    {"image": "@@MEDIA@@sm3/u9/weather_foggy.webp",    "accept": ["foggy", "Foggy"],       "prompt": "туманно"}
  ]} $b$, '@@MEDIA@@', v_media)::jsonb, 2),
(L3, 'quiz', $b$ {"skill": "reading",
  "title": "READING. Прочитай рассказ Норы и выбери: верно или неверно",
  "material": "<p>Hello! My name is Nora. Tomorrow is Saturday. In the morning it’s going to be rainy and windy, so I’m going to stay at home and bake a cake with my mum. In the afternoon it’s going to be sunny. I’m going to put on my boots and go to the park with my dog. On Sunday it’s going to be foggy and cold. I’m not going to go out. I’m going to read my new book about dolphins.</p>",
  "questions": [
    {"q": "<p><b>Tomorrow morning it’s going to be rainy.</b></p>",        "type": "single", "correct": [0], "options": [{"text": "Верно"}, {"text": "Неверно"}]},
    {"q": "<p><b>Nora is going to bake a cake with her dad.</b></p>",           "type": "single", "correct": [1], "options": [{"text": "Верно"}, {"text": "Неверно"}]},
    {"q": "<p><b>In the afternoon Nora is going to go to the park.</b></p>",    "type": "single", "correct": [0], "options": [{"text": "Верно"}, {"text": "Неверно"}]},
    {"q": "<p><b>On Sunday Nora is going to go out.</b></p>",                   "type": "single", "correct": [1], "options": [{"text": "Верно"}, {"text": "Неверно"}]},
    {"q": "<p><b>Nora’s new book is about dolphins.</b></p>",              "type": "single", "correct": [0], "options": [{"text": "Верно"}, {"text": "Неверно"}]}
  ]} $b$::jsonb, 5),
(L3, 'quiz', $b$ {"skill": "listening", "audio": "",
  "title": "LISTENING 🎧 Послушай рассказ про Лиама и выбери правильный ответ. Можно послушать два раза",
  "questions": [
    {"q": "Where does Liam’s grandma live?",                "type": "single", "correct": [1], "options": [{"text": "in London"}, {"text": "in Scotland"}, {"text": "in Italy"}]},
    {"q": "What is the weather going to be like on Monday?",     "type": "single", "correct": [1], "options": [{"text": "sunny"}, {"text": "cloudy"}, {"text": "foggy"}]},
    {"q": "What are Liam and his grandma going to do on Monday?","type": "single", "correct": [2], "options": [{"text": "ride their bikes"}, {"text": "watch a film"}, {"text": "make pizza"}]},
    {"q": "When are they going to watch a film?",                "type": "single", "correct": [1], "options": [{"text": "on Monday"}, {"text": "on Tuesday"}, {"text": "on Wednesday"}]},
    {"q": "What is Liam going to take photos of?",               "type": "single", "correct": [1], "options": [{"text": "the forest"}, {"text": "the old castle"}, {"text": "his new bike"}]}
  ]} $b$::jsonb, 6);

update classroom_blocks set sort_order = case sort_order - 1000
    when 0 then 0 when 1 then 1
    when 2 then 3 when 3 then 4
    when 4 then 7 when 5 then 8 when 6 then 9 end
  where lesson_id = L3 and sort_order >= 1000;

-- ---------- SM3 Final Test ----------
insert into classroom_blocks (lesson_id, type, payload, sort_order) values
(L4, 'exact_input', replace($b$ {"skill": "writing",
  "title": "DICTATION ✍️ Посмотри на картинку и напиши слово",
  "items": [
    {"image": "@@MEDIA@@sm3/ft/gift_bicycle.webp",  "accept": ["bicycle", "Bicycle"], "prompt": "велосипед"},
    {"image": "@@MEDIA@@sm3/ft/bowl_soup.webp",     "accept": ["soup", "Soup"],       "prompt": "суп"},
    {"image": "@@MEDIA@@sm3/ft/riddle_cheese.webp", "accept": ["cheese", "Cheese"],   "prompt": "сыр"},
    {"image": "@@MEDIA@@sm3/ft/riddle_cinema.webp", "accept": ["cinema", "Cinema"],   "prompt": "кинотеатр"},
    {"image": "@@MEDIA@@sm3/ft/opt_football.webp",  "accept": ["football", "Football"],"prompt": "футбол"}
  ]} $b$, '@@MEDIA@@', v_media)::jsonb, 5),
(L4, 'speaking', $b$ {"skill": "speaking",
  "title": "SPEAKING 🎤 Расскажи о себе",
  "html": "<p>Нажми на микрофон 🎤 и ответь на вопросы полными предложениями.</p><ul><li>What are you good at?</li><li>What do you usually do at the weekend?</li><li>What is your favourite food?</li><li>What are you going to do next summer?</li></ul>"} $b$::jsonb, 8);

update classroom_blocks set sort_order = case when sort_order - 1000 <= 4 then sort_order - 1000
                                              when sort_order - 1000 = 7 then 9
                                              else sort_order - 1000 + 1 end
  where lesson_id = L4 and sort_order >= 1000;

end $$;
