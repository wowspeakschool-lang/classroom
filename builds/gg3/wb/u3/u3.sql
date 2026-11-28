-- Go Getter 3, юнит 3 «Going on holiday» по рабочей тетради: домашки 1–7 (черновики)
update classroom_lessons set sort_order = 10 where id = '58db3616-b9e6-4113-8f1a-d87ab4f7bff4';

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = '30796c5f-452a-448f-b057-ba8daa32201b' and title = 'Homework 1';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('30796c5f-452a-448f-b057-ba8daa32201b', 'Homework 1', 0, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 0, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_teen_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 3 · Going on holiday</h2><p>Сегодня — отдых и путешествия: чем заняться и как об этом рассказать.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'flashcards', $blk${"title": "Повторяем слова урока. Нажми на карточку — услышишь слово и увидишь перевод", "cards": [{"text": "go to the beach", "translation": "ходить на пляж", "audio": "", "audio_tts": {"text": "go to the beach.", "voice": "en_GB-alba"}}, {"text": "go cycling", "translation": "кататься на велосипеде", "audio": "", "audio_tts": {"text": "go cycling.", "voice": "en_GB-alba"}}, {"text": "go snorkelling", "translation": "нырять с маской", "audio": "", "audio_tts": {"text": "go snorkelling.", "voice": "en_GB-alba"}}, {"text": "go hiking", "translation": "ходить в поход", "audio": "", "audio_tts": {"text": "go hiking.", "voice": "en_GB-alba"}}, {"text": "go camping", "translation": "жить в палатке", "audio": "", "audio_tts": {"text": "go camping.", "voice": "en_GB-alba"}}, {"text": "go on a boat trip", "translation": "кататься на лодке", "audio": "", "audio_tts": {"text": "go on a boat trip.", "voice": "en_GB-alba"}}, {"text": "go on a day trip", "translation": "ездить на экскурсию на день", "audio": "", "audio_tts": {"text": "go on a day trip.", "voice": "en_GB-alba"}}, {"text": "go on a guided tour", "translation": "ходить на экскурсию с гидом", "audio": "", "audio_tts": {"text": "go on a guided tour.", "voice": "en_GB-alba"}}, {"text": "explore the area", "translation": "исследовать местность", "audio": "", "audio_tts": {"text": "explore the area.", "voice": "en_GB-alba"}}, {"text": "try the local food", "translation": "пробовать местную еду", "audio": "", "audio_tts": {"text": "try the local food.", "voice": "en_GB-alba"}}, {"text": "go sightseeing", "translation": "осматривать достопримечательности", "audio": "", "audio_tts": {"text": "go sightseeing.", "voice": "en_GB-alba"}}, {"text": "get bored", "translation": "скучать", "audio": "", "audio_tts": {"text": "get bored.", "voice": "en_GB-alba"}}]}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'match', $blk${"title": "Соедини начало и конец совета для отпуска", "pairs": [{"left": "A good idea is to go on a day", "right": "boat trip on a lake and take photos of birds."}, {"left": "Maybe you can go on a guided", "right": "tour of a museum."}, {"left": "It's a good idea to explore the", "right": "city in the evening and see the lights."}, {"left": "Why don't you go on", "right": "a trip to the beach?"}, {"left": "It's nice to explore the area", "right": "near your hotel."}, {"left": "Don't forget to try", "right": "the local food because it is often delicious."}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай блог Мирны про Хорватию и впиши пропущенные слова", "mode": "type", "text": "We have beautiful forests. You can go __hiking__ and you can go __cycling__ there. They are both great ways to explore the __area__.\nIt's a good idea to go on a day __trip__ to Dubrovnik and to explore the __city__.\nWhen you are there, try the __local__ food. Croatian food is delicious. You can go on a __guided__ tour of the city and I think it is also a good idea to go on a __boat__ trip because the blue sea is wonderful."}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'sort', $blk${"title": "Распредели слова по глаголам", "groups": [{"name": "go …", "items": [{"text": "cycling"}, {"text": "camping"}, {"text": "hiking"}, {"text": "snorkelling"}]}, {"name": "go on …", "items": [{"text": "a boat trip"}, {"text": "a guided tour"}]}, {"name": "go to …", "items": [{"text": "the beach"}]}, {"name": "try …", "items": [{"text": "the local food"}]}, {"name": "explore …", "items": [{"text": "the area"}]}]}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'speaking', $blk${"title": "SPEAKING 🎤 Расскажи вслух и запиши ответ", "needs_review": true, "html": "<p>Расскажи, какой отдых тебе нравится: куда ты любишь ездить и чем там занимаешься. Скажи три-четыре предложения.</p>", "sample": "", "sample_tts": {"text": "I like going camping with my family.", "voice": "en_GB-alba"}}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_star.webp\" alt=\"\" style=\"height:200px\"></p><p>Отлично! Теперь ты можешь рассказать про любой отдых.</p>"}$blk$::jsonb, 6);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = '30796c5f-452a-448f-b057-ba8daa32201b' and title = 'Homework 2';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('30796c5f-452a-448f-b057-ba8daa32201b', 'Homework 2', 1, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 1, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_girl_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 3 · Past Simple</h2><p>Сегодня — прошедшее время: что было и чего не было.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай предложение и выбери правильную форму", "questions": [{"q": "My friend Tony ___ on an island last week. His photos are amazing.", "type": "single", "correct": [0], "options": [{"text": "was"}, {"text": "were"}]}, {"q": "My sisters ___ in the hotel room an hour ago. Where are they now?", "type": "single", "correct": [1], "options": [{"text": "was"}, {"text": "were"}]}, {"q": "We ___ happy in the tent because it rained all the time.", "type": "single", "correct": [1], "options": [{"text": "wasn't"}, {"text": "weren't"}]}, {"q": "The museum ___ interesting, so we explored the city.", "type": "single", "correct": [0], "options": [{"text": "wasn't"}, {"text": "weren't"}]}, {"q": "I ___ in Paris last summer. I had a great time!", "type": "single", "correct": [0], "options": [{"text": "was"}, {"text": "were"}]}, {"q": "Our passports ___ in Mum's handbag. She forgot them!", "type": "single", "correct": [1], "options": [{"text": "wasn't"}, {"text": "weren't"}]}]}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'sort', $blk${"title": "Распредели глаголы в прошедшем времени: правильные или неправильные", "groups": [{"name": "правильные (-ed)", "items": [{"text": "locked"}, {"text": "loved"}, {"text": "played"}, {"text": "tried"}, {"text": "wanted"}]}, {"name": "неправильные", "items": [{"text": "drank"}, {"text": "ate"}, {"text": "got up"}, {"text": "went"}, {"text": "knew"}]}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Впиши глагол в Past Simple", "mode": "type", "text": "Today I am on holiday, but yesterday I __was__ (am) at home.\nI'd like to try a different pizza. I __tried__ (try) the 'quattro stagioni' last time.\nI don't want to read Gulliver's Travels because I __read__ (read) it last year.\nDave usually sleeps for eight hours, but last night he only __slept__ (sleep) for seven hours.\nDon't stay at that hotel. We __stayed__ (stay) there last summer and it was dirty.\nJim often goes to the beach. He __went__ (go) there yesterday, last Monday and last Saturday!"}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай дневник Поппи и впиши глагол в нужной форме", "mode": "type", "text": "Dear Diary,\nHarry is back from his holidays, so we __went__ (go) on a trip to London. It __was__ (be) fun! I loved it. But Emma __wasn't__ (not be) there! She was ill at home. We __explored__ (explore) the area near the River Thames and we __ate__ (eat) at a nice restaurant there. I __tried__ (try) fish pie for the first time. It was tasty, but Harry __didn't like__ (not like) it – he said it was horrible! Then we __went__ (go) on a boat trip on the river – we __were__ (be) really excited, but Harry's grandma __didn't want__ (not want) to go on the boat trip because she's scared of the water. But in the end, she came with us and she __had__ (have) fun.\nPoppy"}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'task', $blk${"title": "WRITING ✍️ Напиши пять правдивых предложений о себе", "needs_review": true, "html": "<p>Закончи предложения своими словами, в прошедшем времени.</p><ol><li>I … to the beach last … . It was a great day.</li><li>My friends and I … snorkelling three … ago.</li><li>We … the local … . But today I want a sandwich.</li><li>I … go hiking last … because it rained.</li><li>We … our cousins in Paris last … .</li></ol>"}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_trophy.webp\" alt=\"\" style=\"height:200px\"></p><p>Молодец! Прошедшее время теперь слушается.</p>"}$blk$::jsonb, 6);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = '30796c5f-452a-448f-b057-ba8daa32201b' and title = 'Homework 3';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('30796c5f-452a-448f-b057-ba8daa32201b', 'Homework 3', 2, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 2, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 3 · Вопросы о прошлом</h2><p>Сегодня — как спросить про прошлые выходные и коротко ответить.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'match', $blk${"title": "Соедини вопрос с коротким ответом", "pairs": [{"left": "Did you go to the park, Ann?", "right": "Yes, I did."}, {"left": "Did your little sister go cycling?", "right": "No, she didn't."}, {"left": "Was the weather good?", "right": "Yes, it was."}, {"left": "Did you and your brothers have a picnic?", "right": "Yes, we did."}, {"left": "Were your grandparents with you?", "right": "No, they weren't."}, {"left": "What was in your sandwich?", "right": "Cheese and tomato."}]}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'order', $blk${"title": "Составь вопросы, которые Энн задаёт Тому", "items": [{"words": ["Did", "your", "sister", "go", "with", "you?"], "sentence": "Did your sister go with you?", "prompt": "сестра пошла с тобой?"}, {"words": ["Did", "you", "and", "your", "sister", "eat", "some", "popcorn?"], "sentence": "Did you and your sister eat some popcorn?", "prompt": "вы ели попкорн?"}, {"words": ["Was", "the", "film", "funny?"], "sentence": "Was the film funny?", "prompt": "фильм был смешной?"}, {"words": ["Did", "it", "rain?"], "sentence": "Did it rain?", "prompt": "шёл ли дождь?"}, {"words": ["Did", "your", "dad", "drive", "you", "home?"], "sentence": "Did your dad drive you home?", "prompt": "папа отвёз тебя домой?"}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай разговор доктора Кью и Пи и впиши пропущенные слова", "mode": "type", "text": "Dr Q: __Did__ you and Millie play chess?\nPi: Yes, __I did__. I won three games and Millie won two.\nDr Q: Did you tidy the lab?\nPi: __We didn't__. Sorry!\nDr Q: __What__ did you watch on TV?\nPi: We watched a film. It was very funny.\nDr Q: __Was__ the weather good?\nPi: Yes, __it was__. It was great.\nDr Q: __Did__ you cook?\nPi: Yes, __we did__. We were hungry.\nDr Q: __What__ did you eat?\nPi: We __ate__ pizza."}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'task', $blk${"title": "WRITING ✍️ Ответь на вопросы анкеты про свой последний отпуск", "needs_review": true, "html": "<p>Ответь полными предложениями.</p><ol><li>Did you go sightseeing on your last holiday?</li><li>Where did you go?</li><li>Did it rain then?</li><li>Was it cold in the morning or in the evening?</li><li>Were your parents with you?</li><li>Did you all go to the beach?</li><li>What did you do on the first day of your last holiday?</li><li>Did you go hiking?</li></ol>"}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'speaking', $blk${"title": "SPEAKING 🎤 Расскажи вслух и запиши ответ", "needs_review": true, "html": "<p>Расскажи про свои прошлые выходные: куда ходил, что делал, какая была погода. Три-четыре предложения в прошедшем времени.</p>", "sample": "", "sample_tts": {"text": "Last Saturday I went to my grandparents.", "voice": "en_GB-alba"}}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_medal.webp\" alt=\"\" style=\"height:200px\"></p><p>Супер! Теперь ты умеешь и спрашивать, и отвечать о прошлом.</p>"}$blk$::jsonb, 6);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = '30796c5f-452a-448f-b057-ba8daa32201b' and title = 'Homework 4';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('30796c5f-452a-448f-b057-ba8daa32201b', 'Homework 4', 3, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 3, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_teen_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 3 · Просьбы</h2><p>Сегодня — как вежливо попросить и как ответить на просьбу.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'order', $blk${"title": "Составь вежливые просьбы и ответы", "items": [{"words": ["Can", "you", "bring", "me", "my", "torch,", "please?"], "sentence": "Can you bring me my torch, please?", "prompt": "просьба про фонарик"}, {"words": ["Yes,", "no", "problem."], "sentence": "Yes, no problem.", "prompt": "ответ на неё"}, {"words": ["Can", "I", "have", "the", "map?"], "sentence": "Can I have the map?", "prompt": "просьба про карту"}, {"words": ["Sorry,", "I'm", "using", "it", "right", "now."], "sentence": "Sorry, I'm using it right now.", "prompt": "вежливый отказ"}, {"words": ["Could", "you", "give", "me", "the", "train", "timetable?"], "sentence": "Could you give me the train timetable?", "prompt": "просьба про расписание"}, {"words": ["Yes,", "of", "course."], "sentence": "Yes, of course.", "prompt": "согласие"}]}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'sequence', $blk${"title": "Расставь реплики по порядку — получится разговор сына с папой", "items": [{"text": "Can I have the camera, Dad?"}, {"text": "Sorry, you can't. I'm taking some photos now."}, {"text": "OK Dad. So Dad, can I borrow your smartphone? I want to take a photo."}, {"text": "Yes, no problem. Here you are."}, {"text": "Thank you, Dad. Could you stand there, please? I’d like you to be in the photo."}, {"text": "Yes, of course. Is here OK?"}, {"text": "Yes, it's fine. Smile!"}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай просьбу и выбери ответ", "questions": [{"q": "A: Could you bring me the menu?", "type": "single", "correct": [2], "options": [{"text": "Sorry, you can't."}, {"text": "Oh, never mind."}, {"text": "Yes, of course."}]}, {"q": "A: Can you lend me some money, please?", "type": "single", "correct": [1], "options": [{"text": "Yes, you can."}, {"text": "Yes, no problem."}, {"text": "Sorry, you can't."}]}, {"q": "B: Sorry, not now. I'm looking at it. — Какой была просьба?", "type": "single", "correct": [1], "options": [{"text": "Could you buy me a map?"}, {"text": "Can I have the map now, please?"}, {"text": "Can you see the map?"}]}]}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Впиши пропущенные слова в вежливые просьбы", "mode": "type", "text": "A: Can I __borrow your torch__, please?\nB: __Yes, of__ course.\nA: Could __you give me__ the key to the garage?\nB: __Yes, no__ problem.\nA: Can __I wear your sunglasses__, please?\nB: Sorry, __you can't__. I'm wearing them right now.\nA: Could __you lend me your phone__?\nB: Not __now, sorry__. I'm using it."}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'speaking', $blk${"title": "SPEAKING 🎤 Разыграй две просьбы и запиши ответ", "needs_review": true, "html": "<p>Попроси у мамы фотоаппарат, а у брата — планшет. На одну просьбу придумай согласие, на другую — вежливый отказ.</p>", "sample": "", "sample_tts": {"text": "Could you lend me your tablet, please?", "voice": "en_GB-alba"}}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_thumb.webp\" alt=\"\" style=\"height:200px\"></p><p>Отлично! Просить и отказывать вежливо — тоже навык.</p>"}$blk$::jsonb, 6);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = '30796c5f-452a-448f-b057-ba8daa32201b' and title = 'Homework 5';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('30796c5f-452a-448f-b057-ba8daa32201b', 'Homework 5', 4, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 4, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_girl_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 3 · Reading</h2><p>Сегодня читаем блог Томми про отдых в Шотландии.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<h3>My holidays in Scotland <span style=\"color:#888\">by Tommy</span></h3><p><b>A</b> My mum and I don't stay at home in the holidays. We love sports, so last year we went to Scotland. Scotland has lots of mountains and wild countryside, so it is great for outdoor activities. The place we stayed at is a holiday village called Glencoe Mountain. We went there in the summer and in the winter.</p><p><b>B</b> We drove to Glencoe Mountain in August. There is a campsite there and we put up our tent together at 10 p.m. It wasn't dark because it gets dark late in Scotland in the summer. We went cycling on our mountain bikes for the first two days. We got tired, but the views were amazing. Then we went hiking and we saw some wild rabbits and a fox.</p><p><b>C</b> We went to Glencoe Mountain again in December. On the first day, we travelled by coach and the coach got lost on the way! But our holiday was great. It was sunny all the time, so we didn't get cold. My mum and I went skiing every day. Glencoe Mountain is my favourite place for a holiday. There is so much to do. You never get bored.</p>"}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай блог и подбери заголовок к каждому абзацу", "questions": [{"q": "Абзац A", "type": "single", "correct": [1], "options": [{"text": "Summer fun"}, {"text": "Two holidays in one year"}, {"text": "Bad weather"}, {"text": "A winter holiday"}]}, {"q": "Абзац B", "type": "single", "correct": [0], "options": [{"text": "Summer fun"}, {"text": "Two holidays in one year"}, {"text": "Bad weather"}, {"text": "A winter holiday"}]}, {"q": "Абзац C", "type": "single", "correct": [3], "options": [{"text": "Summer fun"}, {"text": "Two holidays in one year"}, {"text": "Bad weather"}, {"text": "A winter holiday"}]}], "material": "<h3>My holidays in Scotland <span style=\"color:#888\">by Tommy</span></h3><p><b>A</b> My mum and I don't stay at home in the holidays. We love sports, so last year we went to Scotland. Scotland has lots of mountains and wild countryside, so it is great for outdoor activities. The place we stayed at is a holiday village called Glencoe Mountain. We went there in the summer and in the winter.</p><p><b>B</b> We drove to Glencoe Mountain in August. There is a campsite there and we put up our tent together at 10 p.m. It wasn't dark because it gets dark late in Scotland in the summer. We went cycling on our mountain bikes for the first two days. We got tired, but the views were amazing. Then we went hiking and we saw some wild rabbits and a fox.</p><p><b>C</b> We went to Glencoe Mountain again in December. On the first day, we travelled by coach and the coach got lost on the way! But our holiday was great. It was sunny all the time, so we didn't get cold. My mum and I went skiing every day. Glencoe Mountain is my favourite place for a holiday. There is so much to do. You never get bored.</p>"}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай блог ещё раз и впиши по одному слову", "mode": "type", "text": "Tommy went on holiday with his __mum__.\nIn August it wasn't __dark__ at 10 p.m.\n__Cycling__ was their first activity.\nThey saw some rabbits and a fox when they went __hiking__.\nTommy and his mum didn't __travel__ by car for the winter holiday.\nTommy and his mum went __skiing__ in December.\nGlencoe Mountain is Tommy's __favourite__ place to go on holiday.", "material": "<h3>My holidays in Scotland <span style=\"color:#888\">by Tommy</span></h3><p><b>A</b> My mum and I don't stay at home in the holidays. We love sports, so last year we went to Scotland. Scotland has lots of mountains and wild countryside, so it is great for outdoor activities. The place we stayed at is a holiday village called Glencoe Mountain. We went there in the summer and in the winter.</p><p><b>B</b> We drove to Glencoe Mountain in August. There is a campsite there and we put up our tent together at 10 p.m. It wasn't dark because it gets dark late in Scotland in the summer. We went cycling on our mountain bikes for the first two days. We got tired, but the views were amazing. Then we went hiking and we saw some wild rabbits and a fox.</p><p><b>C</b> We went to Glencoe Mountain again in December. On the first day, we travelled by coach and the coach got lost on the way! But our holiday was great. It was sunny all the time, so we didn't get cold. My mum and I went skiing every day. Glencoe Mountain is my favourite place for a holiday. There is so much to do. You never get bored.</p>"}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Выбери правильное слово после get", "questions": [{"q": "In winter it gets ___ in my town at 10 p.m.", "type": "single", "correct": [1], "options": [{"text": "bored"}, {"text": "dark"}]}, {"q": "It gets ___ in winter in my town.", "type": "single", "correct": [1], "options": [{"text": "tired"}, {"text": "cold"}]}, {"q": "People sometimes get ___ when they go hiking.", "type": "single", "correct": [0], "options": [{"text": "lost"}, {"text": "dark"}]}, {"q": "Last night I got ___ at 9 p.m., so I went to bed early.", "type": "single", "correct": [0], "options": [{"text": "tired"}, {"text": "cold"}]}, {"q": "I never get ___ when I go sightseeing.", "type": "single", "correct": [0], "options": [{"text": "bored"}, {"text": "dark"}]}]}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'task', $blk${"title": "WRITING ✍️ Напиши про своё любимое место для отдыха", "needs_review": true, "html": "<p>Четыре-пять предложений: где это, когда ты там был, что вы делали и почему тебе там нравится.</p>"}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_popper.webp\" alt=\"\" style=\"height:200px\"></p><p>Здорово! Шотландия прочитана, а своё место описано.</p>"}$blk$::jsonb, 6);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = '30796c5f-452a-448f-b057-ba8daa32201b' and title = 'Homework 6';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('30796c5f-452a-448f-b057-ba8daa32201b', 'Homework 6', 5, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 5, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 3 · Listening and Writing</h2><p>Сегодня слушаем рассказы об отпуске и пишем письмо дяде.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'sort', $blk${"title": "Распредели слова по группам", "groups": [{"name": "🏖 пляж", "items": [{"text": "beach"}, {"text": "swimming"}, {"text": "snorkelling"}]}, {"name": "⛺ горы", "items": [{"text": "camping"}, {"text": "hiking"}, {"text": "mountains"}]}, {"name": "🏙 город", "items": [{"text": "city"}, {"text": "museums"}, {"text": "restaurants"}]}]}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "LISTENING 🎧 Послушай запись и выбери правильный ответ", "audio": "https://api.wowteach.ru/storage/v1/object/public/classroom-media/gg3%20wb/GG%20L3%20WkBk%20A8.mp3", "skill": "listening", "questions": [{"q": "Where did Anna go on holiday?", "type": "single", "correct": [0], "options": [{"text": "to the beach"}, {"text": "to the mountains"}, {"text": "to a campsite"}]}, {"q": "What did Steve do on holiday?", "type": "single", "correct": [2], "options": [{"text": "he went snorkelling"}, {"text": "he went cycling"}, {"text": "he went hiking"}]}, {"q": "Why didn’t Jane like her holiday?", "type": "single", "correct": [1], "options": [{"text": "the weather was bad"}, {"text": "the city wasn’t interesting"}, {"text": "the hotel was dirty"}]}, {"q": "Where did Bob stay?", "type": "single", "correct": [0], "options": [{"text": "at a campsite next to a lake"}, {"text": "in a hotel in the city"}, {"text": "at his grandparents’ house"}]}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "LISTENING 🎧 Послушай запись ещё раз и впиши по одному слову", "mode": "type", "text": "Anna: She took __photos__ on her holiday. She went __swimming__ every day.\nSteve: He went to the __mountains__. He went __hiking__.\nJane: She didn't __like__ her holiday. The __city__ wasn't interesting.\nBob: He stayed at a __campsite__ next to a lake. He loves __camping__."}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай письмо Ребекки и перетащи слова в пропуски", "mode": "drag", "text": "Dear Uncle Paul,\nI hope you're __well__. We're having a great time on the island. I wish __you__ were here! There are lots of __things__ to do here. Last Sunday we went snorkelling with Aunt Jess. We swam for an hour. I saw lots of pretty fish and an octopus. Dan saw a starfish and Aunt Jess saw a crab. Yesterday we __went__ cycling in the countryside. It was windy, but I had a jacket, so I didn't __get__ cold. I need to help Aunt Jess with the cooking now, so I can't write any __more__. __See__ you soon!\nLots of __love__,\nRebecca"}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'task', $blk${"title": "WRITING ✍️ Напиши письмо дяде от имени Дэна", "needs_review": true, "html": "<p>Используй заметки о двух днях отдыха:</p><p><b>Понедельник:</b> ресторан с тётей Джесс; попробовали местную еду; Ребекка — курица, Дэн — рыба с картошкой, тётя Джесс — рис с овощами.<br><b>Вторник:</b> поход в горы; Ребекка устала, Дэн — нормально, тётя Джесс очень довольна.</p><p>Начни так: <i>Dear Uncle Paul, I hope …</i></p>"}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_certificate.webp\" alt=\"\" style=\"height:200px\"></p><p>Отлично! И послушали, и написали настоящее письмо.</p>"}$blk$::jsonb, 6);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = '30796c5f-452a-448f-b057-ba8daa32201b' and title = 'Homework 7';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('30796c5f-452a-448f-b057-ba8daa32201b', 'Homework 7', 6, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 6, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_teen_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 3 · Check yourself!</h2><p>Повторяем весь юнит перед тестом.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай про выходные Джо и Роба и выбери правильное слово", "questions": [{"q": "Last Saturday Joe and Rob went ___ in the morning.", "type": "single", "correct": [0], "options": [{"text": "cycling"}, {"text": "hiking"}]}, {"q": "They got on their bikes and they went ___.", "type": "single", "correct": [1], "options": [{"text": "camping"}, {"text": "to the beach"}]}, {"q": "They swam and then they got ___.", "type": "single", "correct": [1], "options": [{"text": "lost"}, {"text": "cold"}]}, {"q": "In the afternoon they explored the ___.", "type": "single", "correct": [0], "options": [{"text": "area"}, {"text": "city"}]}, {"q": "They were hungry, so they decided to ___.", "type": "single", "correct": [1], "options": [{"text": "go snorkelling"}, {"text": "try the local food"}]}, {"q": "They went home at eight o'clock because it got ___.", "type": "single", "correct": [0], "options": [{"text": "dark"}, {"text": "tired"}]}]}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай объявление про поездку в Лондон и перетащи слова в пропуски", "mode": "drag", "text": "Why don't you __go on__ a day trip to London and visit the Tower of London!\nHow to get there: You can go on a boat __trip__ on the River Thames. Or you can go __cycling__ on your bike along the river paths.\nWhat to do there: We have great __guided__ tours for kids and families. You can also __explore__ the Tower on your own. Find out interesting facts about the kings and queens of England. You won't get __bored__!"}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Впиши глагол в Past Simple", "mode": "type", "text": "My neighbours, the Greens, spent their last summer holidays on an island. They __arrived__ (arrive) at the airport early, but the plane was late. Mr Green __left__ (leave) the guidebook at home. Mrs Green __didn't like__ (not like) the hotel. The weather __was__ (be) windy. Their son __got__ (get) lost on the beach. They __didn't take__ (not take) any photos. That holiday wasn't their favourite."}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай разговор Марко и Джейн и впиши пропущенное слово", "mode": "type", "text": "Marco: How __was__ your month in Italy? __Did__ you try Italian food?\nJayne: Yes, I __did__. It was tasty.\nMarco: __Were__ the museums interesting?\nJayne: Yes, they were. I went sightseeing a lot.\nMarco: Was the weather good?\nJayne: No, it __wasn't__. The first week it rained.\nMarco: Oh no. Did you stay in the hotel?\nJayne: No, I __didn't__. I went out. I had an umbrella, so I was OK."}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай разговор в ресторане и выбери правильный вариант", "questions": [{"q": "A: ___ bring me the menu, please?", "type": "single", "correct": [0], "options": [{"text": "Can you"}, {"text": "You can"}]}, {"q": "B: Yes, ___.", "type": "single", "correct": [0], "options": [{"text": "of course"}, {"text": "not now"}]}, {"q": "A: And could ___ also bring me some water?", "type": "single", "correct": [1], "options": [{"text": "I"}, {"text": "you"}]}, {"q": "B: ___, no problem.", "type": "single", "correct": [1], "options": [{"text": "No"}, {"text": "Yes"}]}, {"q": "A: ___ have the fish, please?", "type": "single", "correct": [0], "options": [{"text": "Can I"}, {"text": "Can you"}]}, {"q": "B: ___ There isn't any fish today.", "type": "single", "correct": [1], "options": [{"text": "Not now, sorry."}, {"text": "Sorry, you can't."}]}]}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'speaking', $blk${"title": "SPEAKING 🎤 Расскажи вслух и запиши ответ", "needs_review": true, "html": "<p>Расскажи о поездке, которая тебе запомнилась: куда вы поехали, что делали, какая была погода и что понравилось больше всего.</p>", "sample": "", "sample_tts": {"text": "Last summer we went to the mountains.", "voice": "en_GB-alba"}}$blk$::jsonb, 6);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_trophy.webp\" alt=\"\" style=\"height:200px\"></p><p>Юнит пройден! Можно браться за тест.</p>"}$blk$::jsonb, 7);
end $$;
