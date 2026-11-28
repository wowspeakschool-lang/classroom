-- Go Getter 3, юнит 6 «Cooking and eating» по рабочей тетради: домашки 1–7 (черновики)
update classroom_lessons set sort_order = 10 where id = 'e6eeecd4-070f-4818-9cfb-cdc837c7361c';

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = 'a4f27767-6f35-491b-8def-f7efd9caacee' and title = 'Homework 1';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('a4f27767-6f35-491b-8def-f7efd9caacee', 'Homework 1', 0, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 0, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_teen_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 6 · Cooking and eating</h2><p>Сегодня — кухня: что с едой делают и чем это делают.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'flashcards', $blk${"title": "Повторяем слова урока. Нажми на карточку — услышишь слово и увидишь перевод", "cards": [{"text": "peel", "translation": "чистить от кожуры", "audio": "", "audio_tts": {"text": "peel.", "voice": "en_GB-alba"}}, {"text": "chop", "translation": "нарезать кубиками", "audio": "", "audio_tts": {"text": "chop.", "voice": "en_GB-alba"}}, {"text": "slice", "translation": "нарезать ломтиками", "audio": "", "audio_tts": {"text": "slice.", "voice": "en_GB-alba"}}, {"text": "add", "translation": "добавлять", "audio": "", "audio_tts": {"text": "add.", "voice": "en_GB-alba"}}, {"text": "mix", "translation": "смешивать", "audio": "", "audio_tts": {"text": "mix.", "voice": "en_GB-alba"}}, {"text": "beat", "translation": "взбивать", "audio": "", "audio_tts": {"text": "beat.", "voice": "en_GB-alba"}}, {"text": "bake", "translation": "печь в духовке", "audio": "", "audio_tts": {"text": "bake.", "voice": "en_GB-alba"}}, {"text": "boil", "translation": "варить в воде", "audio": "", "audio_tts": {"text": "boil.", "voice": "en_GB-alba"}}, {"text": "fry", "translation": "жарить на масле", "audio": "", "audio_tts": {"text": "fry.", "voice": "en_GB-alba"}}, {"text": "roast", "translation": "запекать мясо в духовке", "audio": "", "audio_tts": {"text": "roast.", "voice": "en_GB-alba"}}, {"text": "a pot", "translation": "кастрюля", "audio": "", "audio_tts": {"text": "a pot.", "voice": "en_GB-alba"}}, {"text": "a frying pan", "translation": "сковорода", "audio": "", "audio_tts": {"text": "a frying pan.", "voice": "en_GB-alba"}}, {"text": "a cake tin", "translation": "форма для выпечки", "audio": "", "audio_tts": {"text": "a cake tin.", "voice": "en_GB-alba"}}, {"text": "a bowl", "translation": "миска", "audio": "", "audio_tts": {"text": "a bowl.", "voice": "en_GB-alba"}}]}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'match', $blk${"title": "Соедини глагол с его значением", "pairs": [{"left": "chop", "right": "cut food into small pieces"}, {"left": "boil", "right": "cook food in water"}, {"left": "fry", "right": "cook food in butter or oil"}, {"left": "roast", "right": "cook meat in the oven"}, {"left": "beat", "right": "mix eggs fast with a fork"}, {"left": "peel", "right": "cut off the skin of an apple"}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай рецепт яблочно-морковного пирога и перетащи слова в пропуски", "mode": "drag", "text": "Today I'm making an apple carrot cake. Look, it's easy! First, peel the apples and the carrots.\nThen __chop__ the apples and the carrots.\nNext __add__ sugar, two eggs and flour to the butter.\nThe apples and carrots are in the bowl now. It's time to __mix__ everything with a spoon.\n__Bake__ the cake in the oven for 45 minutes.\nHere is my apple carrot cake. __Slice__ it and give everyone some cake!"}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Впиши глагол: bake · beat · boil · fry · roast", "mode": "type", "text": "You can mix strawberries and yoghurt for a nice snack.\nSome people always __roast__ chicken and potatoes in the oven on Sundays.\nYou can __fry__ eggs in butter for a hot breakfast.\nYou can eat carrots in salad or __boil__ them in water for a hot meal.\nIt's fun to learn with Mum how to __bake__ biscuits in the oven.\nYou have to __beat__ eggs first to make an omelette."}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай рецепт пасты с курицей и выбери правильное слово", "questions": [{"q": "First slice or chop the chicken and put it in a ___.", "type": "single", "correct": [0], "options": [{"text": "bowl"}, {"text": "pot"}]}, {"q": "Choose the pasta you like and boil it in water in a big ___.", "type": "single", "correct": [0], "options": [{"text": "pot"}, {"text": "frying pan"}]}, {"q": "Then fry the chicken in some butter in a ___.", "type": "single", "correct": [1], "options": [{"text": "cake tin"}, {"text": "frying pan"}]}, {"q": "Add some cheese and cream to the chicken and ___ them all together.", "type": "single", "correct": [0], "options": [{"text": "mix"}, {"text": "peel"}]}, {"q": "Put the pasta in a ___ and the chicken on top. Enjoy!", "type": "single", "correct": [0], "options": [{"text": "bowl"}, {"text": "cake tin"}]}]}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'exact_input', $blk${"title": "Прочитай, что делают с продуктом, и напиши глагол по-английски", "items": [{"prompt": "onions and carrots — режут кубиками (ch…)", "accept": ["chop", "Chop", "to chop"]}, {"prompt": "eggs and rice — варят в воде (b…)", "accept": ["boil", "Boil", "to boil"]}, {"prompt": "cheese and bread — режут ломтиками (s…)", "accept": ["slice", "Slice", "to slice"]}, {"prompt": "fish and pancakes — жарят на масле (f…)", "accept": ["fry", "Fry", "to fry"]}, {"prompt": "cake and biscuits — пекут в духовке (b…)", "accept": ["bake", "Bake", "to bake"]}]}$blk$::jsonb, 6);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_star.webp\" alt=\"\" style=\"height:200px\"></p><p>Готово! Теперь кухня тебе по-английски понятна.</p>"}$blk$::jsonb, 7);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = 'a4f27767-6f35-491b-8def-f7efd9caacee' and title = 'Homework 2';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('a4f27767-6f35-491b-8def-f7efd9caacee', 'Homework 2', 1, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 1, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_girl_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 6 · Present Perfect</h2><p>Сегодня — что уже сделано, а что ещё нет.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'match', $blk${"title": "Соедини глагол с его третьей формой (Past Participle)", "pairs": [{"left": "eat", "right": "eaten"}, {"left": "chop", "right": "chopped"}, {"left": "drink", "right": "drunk"}, {"left": "buy", "right": "bought"}, {"left": "make", "right": "made"}, {"left": "bring", "right": "brought"}]}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'sort', $blk${"title": "Распредели посуду по назначению", "groups": [{"name": "🥤 из этого пьют", "items": [{"text": "a cup"}, {"text": "a mug"}, {"text": "a glass"}]}, {"name": "🍴 этим едят", "items": [{"text": "a fork"}, {"text": "a knife"}, {"text": "a spoon"}]}, {"name": "🍽 на это кладут еду", "items": [{"text": "a plate"}, {"text": "a bowl"}]}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай разговор Эммы с бабушкой и перетащи отрицательную форму в пропуск", "mode": "drag", "text": "Emma: I want to make a chocolate cake, but the chef hasn't put any nice recipes on my favourite cooking blog.\nGran: There's a good chocolate cake recipe in my cookbook. But, oh dear. Harry __hasn't bought__ any chocolate!\nEmma: Hmm. I __haven't looked__ at your cookbook. Is there a lemon cake recipe in it?\nGran: Let's look. Yes, there's a recipe on page 12. We __haven't made__ it yet, but it looks nice. Let's try it.\nEmma: OK. We need two lemons, three eggs, some flour, butter and sugar.\nTen minutes later …\nEmma: OK. The cake is in the oven.\nGran: Oh dear! We __haven't added__ the lemon juice!\nEmma: Don't worry! Let's put some jam on the cake."}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'order', $blk${"title": "Составь предложения про сегодняшний день в Present Perfect", "items": [{"words": ["Mum", "has", "made", "pizza."], "sentence": "Mum has made pizza.", "prompt": "мама приготовила пиццу"}, {"words": ["I", "haven't", "tidied", "my", "room."], "sentence": "I haven't tidied my room.", "prompt": "я не убрал свою комнату"}, {"words": ["Dad", "has", "put", "the", "mugs", "in", "the", "wrong", "cupboard."], "sentence": "Dad has put the mugs in the wrong cupboard.", "prompt": "папа поставил кружки не в тот шкаф"}, {"words": ["We", "have", "eaten", "all", "the", "cake."], "sentence": "We have eaten all the cake.", "prompt": "мы съели весь торт"}]}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Впиши глагол в Present Perfect: полная форма has/have + третья форма", "mode": "type", "text": "I have finished (finish) my soup. Can I have some more, please?\nThis is Fred's plate. He __has eaten__ (eat) all his food.\nOh, there isn't any water in the cat's bowl. It __has drunk__ (drink) it all.\nWe __have chopped__ (chop) all the vegetables, Mum. Now what do we do?\nYou __have boiled__ (boil) the water, so now you can add the pasta.\nLook, everyone! I __have brought__ (bring) a dessert. It's chocolate ice cream!"}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'task', $blk${"title": "WRITING ✍️ Напиши, что ты уже сделал сегодня", "needs_review": true, "html": "<p>Напиши три предложения в Present Perfect — правдиво про себя.</p><ol><li>do my homework → I …</li><li>write a text on my phone → I …</li><li>send me an email → My friend …</li></ol><p>Если что-то ещё не сделано, пиши отрицание: <b>I haven't …</b></p>"}$blk$::jsonb, 6);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_trophy.webp\" alt=\"\" style=\"height:200px\"></p><p>Present Perfect разобран: has/have и третья форма глагола.</p>"}$blk$::jsonb, 7);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = 'a4f27767-6f35-491b-8def-f7efd9caacee' and title = 'Homework 3';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('a4f27767-6f35-491b-8def-f7efd9caacee', 'Homework 3', 2, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 2, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 6 · Вопросы в Present Perfect</h2><p>Сегодня — как спросить «ты когда-нибудь…?» и как коротко ответить.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай разговор Энди и Беллы и выбери короткий ответ", "questions": [{"q": "Andy: Have you ever made popcorn? — Bella: Yes, ___.", "type": "single", "correct": [0], "options": [{"text": "I have"}, {"text": "it has"}]}, {"q": "Andy: Have your friends ever eaten your dishes? — Bella: Yes, ___.", "type": "single", "correct": [1], "options": [{"text": "you have"}, {"text": "they have"}]}, {"q": "Andy: Have you ever tried banana cookies? — Bella: No, ___.", "type": "single", "correct": [1], "options": [{"text": "you haven't"}, {"text": "I haven't"}]}, {"q": "Andy: Has your pet ever eaten chicken ice cream? — Bella: No, ___.", "type": "single", "correct": [0], "options": [{"text": "it hasn't"}, {"text": "they haven't"}]}, {"q": "Andy: Have you ever won a cooking competition? — Bella: Yes, ___.", "type": "single", "correct": [1], "options": [{"text": "I haven't"}, {"text": "I have"}]}]}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'order', $blk${"title": "Составь вопросы для Дэйва из списка дел к ужину", "items": [{"words": ["Have", "you", "bought", "the", "drinks?"], "sentence": "Have you bought the drinks?", "prompt": "ты купил напитки?"}, {"words": ["Has", "John", "washed", "the", "vegetables?"], "sentence": "Has John washed the vegetables?", "prompt": "Джон помыл овощи?"}, {"words": ["Have", "we", "bought", "enough", "pasta?"], "sentence": "Have we bought enough pasta?", "prompt": "мы купили достаточно пасты?"}, {"words": ["Have", "your", "aunts", "brought", "the", "dessert?"], "sentence": "Have your aunts brought the dessert?", "prompt": "твои тёти привезли десерт?"}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Впиши слова, чтобы получился вопрос и короткий ответ (bake · use · watch)", "mode": "type", "text": "Has Doctor Q made pancakes for everyone? Yes, he has. ✔\n__Have__ Millie and Rob __baked__ a cake? Yes, they __have__. ✔\n__Has__ Millie __used__ all the sugar? No, she __hasn't__. ✘\n__Have__ Pi and Doctor Q __watched__ their show on TV? No, they __haven't__. ✘"}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай разговоры и впиши по одному слову в каждый пропуск", "mode": "type", "text": "A: Have you ever baked biscuits?\nB: No, I haven't. I've __never__ baked anything!\nA: Has Dave __ever__ won a football competition?\nB: Yes, I think he __has__. He's the best footballer in the school.\nA: Have __you__ ever eaten at that restaurant?\nB: __No__, I haven't. Is the food nice there?\nA: __Has__ your mum ever tried Chinese food?\nB: No, she hasn't. She __has__ never eaten at a Chinese restaurant."}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'task', $blk${"title": "WRITING ✍️ Напиши вопросы и правдивые короткие ответы", "needs_review": true, "html": "<p>Прочитай предложение и составь к нему вопрос с <b>ever</b>, а потом ответь правдиво про себя.</p><ol><li>I've never won a competition. → Have you ever …?</li><li>My best friend has cooked at my house. → Has your best friend ever …?</li><li>I've never drunk fresh lemonade. → Have you ever …?</li></ol>"}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'speaking', $blk${"title": "SPEAKING 🎤 Расскажи вслух и запиши ответ", "needs_review": true, "html": "<p>Расскажи, что ты когда-нибудь готовил или пробовал, а чего не пробовал никогда. Три-четыре предложения с <b>ever</b> и <b>never</b>.</p>", "sample": "", "sample_tts": {"text": "I have never eaten a samosa.", "voice": "en_GB-alba"}}$blk$::jsonb, 6);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_medal.webp\" alt=\"\" style=\"height:200px\"></p><p>Теперь ты умеешь спрашивать про опыт и коротко отвечать.</p>"}$blk$::jsonb, 7);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = 'a4f27767-6f35-491b-8def-f7efd9caacee' and title = 'Homework 4';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('a4f27767-6f35-491b-8def-f7efd9caacee', 'Homework 4', 3, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 3, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_teen_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 6 · Что ты предпочитаешь</h2><p>Сегодня — как спросить о предпочтениях и как ответить на такой вопрос.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'match', $blk${"title": "Соедини начало и конец фразы", "pairs": [{"left": "Would you like chips", "right": "or rice?"}, {"left": "Would you like to", "right": "play football or video games?"}, {"left": "Would you", "right": "like tea or coffee?"}, {"left": "I'd", "right": "like tea."}, {"left": "I'd prefer", "right": "chips."}, {"left": "I don't", "right": "mind."}]}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай, что рассказали Бет и Джон, и выбери правильный ответ", "questions": [{"q": "Where does Beth like having picnics?", "type": "single", "correct": [0], "options": [{"text": "at the park"}, {"text": "on the beach"}, {"text": "at home"}]}, {"q": "What food does Beth prefer at picnics?", "type": "single", "correct": [1], "options": [{"text": "sandwiches"}, {"text": "pizza"}, {"text": "fish and chips"}]}, {"q": "What does Beth say about drinks?", "type": "single", "correct": [0], "options": [{"text": "She doesn't mind."}, {"text": "She prefers lemonade."}, {"text": "She only drinks water."}]}, {"q": "Which sport does Beth prefer?", "type": "single", "correct": [1], "options": [{"text": "badminton"}, {"text": "volleyball"}, {"text": "football"}]}, {"q": "What does John prefer to drink?", "type": "single", "correct": [1], "options": [{"text": "lemonade"}, {"text": "cola"}, {"text": "water"}]}, {"q": "Which sport does John prefer?", "type": "single", "correct": [1], "options": [{"text": "football"}, {"text": "volleyball"}, {"text": "badminton"}]}], "material": "<p><b>Beth:</b> I like picnics at the park. People usually have sandwiches at picnics, but I don't like them. I prefer pizza! I don't mind what I drink. I like cola or water. My best friend, Jess, likes playing badminton at picnics. I prefer volleyball.</p><p><b>John:</b> I like picnics at the park or on the beach. My good friend, Matt, says lemonade is the best picnic drink, but I prefer cola. I like sandwiches. And my favourite sport at picnics? Yes, I like playing football at picnics, but I prefer volleyball.</p>"}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'order', $blk${"title": "Составь фразы про предпочтения", "items": [{"words": ["Would", "you", "like", "tea", "or", "coffee?"], "sentence": "Would you like tea or coffee?", "prompt": "спроси, что он хочет: чай или кофе"}, {"words": ["I'd", "prefer", "pizza."], "sentence": "I'd prefer pizza.", "prompt": "скажи, что предпочитаешь пиццу"}, {"words": ["I", "don't", "mind."], "sentence": "I don't mind.", "prompt": "скажи, что тебе всё равно"}, {"words": ["Would", "you", "like", "to", "go", "to", "the", "beach?"], "sentence": "Would you like to go to the beach?", "prompt": "спроси, хочет ли он пойти на пляж"}]}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай разговор Джона и Бет и впиши по одному слову в каждый пропуск", "mode": "type", "text": "John: Would you like to have a picnic at the park or on the __beach__?\nBeth: __I'd__ like to have a picnic at the __park__.\nJohn: OK. __Would__ you __like__ sandwiches or pizza at the picnic?\nBeth: I'd prefer __pizza__.\nJohn: Cool. What about drinks? Would you like cola or water?\nBeth: I don't __mind__. You __choose__. Would you like to play football or volleyball at the picnic?\nJohn: I'd like to play __volleyball__.\nBeth: Me too."}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'task', $blk${"title": "WRITING ✍️ Запиши разговор в кафе", "needs_review": true, "html": "<p>Вы с мамой в кафе и хотите что-нибудь сладкое: капкейк или шоколадное мороженое. Запиши разговор из четырёх реплик.</p><p>Мама спрашивает про выбор, ты отвечаешь, что предпочитаешь, мама спрашивает про напиток, ты говоришь, что тебе всё равно.</p>"}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'speaking', $blk${"title": "SPEAKING 🎤 Разыграй разговор и запиши ответ", "needs_review": true, "html": "<p>Вы с другом на отдыхе и выбираете, чем заняться: покататься на каяке по озеру или поплавать в озере. Спроси друга о его выборе, скажи, что предпочитаешь ты, и почему.</p>", "sample": "", "sample_tts": {"text": "Would you like to go for a bike ride or go to the beach?", "voice": "en_GB-alba"}}$blk$::jsonb, 6);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_thumb.webp\" alt=\"\" style=\"height:200px\"></p><p>Отлично! Теперь ты умеешь выбирать и спрашивать о выборе.</p>"}$blk$::jsonb, 7);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = 'a4f27767-6f35-491b-8def-f7efd9caacee' and title = 'Homework 5';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('a4f27767-6f35-491b-8def-f7efd9caacee', 'Homework 5', 4, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 4, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_girl_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 6 · Reading</h2><p>Сегодня читаем блог Саши про пироги разных стран.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<h3>Pies from around the world <span style=\"color:#888\">by Sasha</span></h3><p>People make pies all around the world. Here are my favourite pies.</p><p><b>1</b> I'm English and I like our traditional apple pie. It's a sweet pie and it's a popular dessert.</p><p><b>2</b> Another sweet pie is pumpkin pie from America. Pumpkins are vegetables, but they add sugar to this pie, so it is sweet. I usually have apple pie and pumpkin pie with sour cream, but you can have ice cream as well.</p><p><b>3</b> Not all pies are sweet. My best friend's mum is from Ukraine and she makes a delicious Ukrainian fish pie. She mixes fish, boiled eggs and rice and puts them in the pie.</p><p><b>4</b> Another pie is quiche. This is an open pie from France and it has fish or meat in it with eggs, cheese and vegetables. You can eat hot or cold quiche, so it's great for picnics.</p><p><b>5</b> In Greece they make little pies for snacks. The best pies are the little cheese pies – I've eaten them for breakfast there.</p><p><b>6</b> The last pie on my list is an Indian spicy pie – a samosa. It has vegetables and sometimes meat in it. My brother has never tried them. He thinks samosas are disgusting because he doesn't like spicy food, but I love them!</p>"}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'match', $blk${"title": "Соедини пирог со страной, откуда он", "pairs": [{"left": "apple pie", "right": "England"}, {"left": "pumpkin pie", "right": "America"}, {"left": "fish pie", "right": "Ukraine"}, {"left": "quiche", "right": "France"}, {"left": "little cheese pies", "right": "Greece"}, {"left": "samosas", "right": "India"}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай блог ещё раз и реши: верно, неверно или в тексте этого нет", "questions": [{"q": "Sasha is from America.", "type": "single", "correct": [1], "options": [{"text": "Верно"}, {"text": "Неверно"}, {"text": "В тексте этого нет"}]}, {"q": "Apple pies aren't popular desserts.", "type": "single", "correct": [1], "options": [{"text": "Верно"}, {"text": "Неверно"}, {"text": "В тексте этого нет"}]}, {"q": "Pumpkin pie has sugar in it.", "type": "single", "correct": [0], "options": [{"text": "Верно"}, {"text": "Неверно"}, {"text": "В тексте этого нет"}]}, {"q": "Sasha's best friend makes fish pies.", "type": "single", "correct": [1], "options": [{"text": "Верно"}, {"text": "Неверно"}, {"text": "В тексте этого нет"}]}, {"q": "In Greece, Sasha has had a pie for breakfast.", "type": "single", "correct": [0], "options": [{"text": "Верно"}, {"text": "Неверно"}, {"text": "В тексте этого нет"}]}, {"q": "Sasha's brother has never eaten spicy food.", "type": "single", "correct": [2], "options": [{"text": "Верно"}, {"text": "Неверно"}, {"text": "В тексте этого нет"}]}], "material": "<h3>Pies from around the world <span style=\"color:#888\">by Sasha</span></h3><p>People make pies all around the world. Here are my favourite pies.</p><p><b>1</b> I'm English and I like our traditional apple pie. It's a sweet pie and it's a popular dessert.</p><p><b>2</b> Another sweet pie is pumpkin pie from America. Pumpkins are vegetables, but they add sugar to this pie, so it is sweet. I usually have apple pie and pumpkin pie with sour cream, but you can have ice cream as well.</p><p><b>3</b> Not all pies are sweet. My best friend's mum is from Ukraine and she makes a delicious Ukrainian fish pie. She mixes fish, boiled eggs and rice and puts them in the pie.</p><p><b>4</b> Another pie is quiche. This is an open pie from France and it has fish or meat in it with eggs, cheese and vegetables. You can eat hot or cold quiche, so it's great for picnics.</p><p><b>5</b> In Greece they make little pies for snacks. The best pies are the little cheese pies – I've eaten them for breakfast there.</p><p><b>6</b> The last pie on my list is an Indian spicy pie – a samosa. It has vegetables and sometimes meat in it. My brother has never tried them. He thinks samosas are disgusting because he doesn't like spicy food, but I love them!</p>"}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Впиши слово: delicious · disgusting · salty · sour · spicy", "mode": "type", "text": "Chocolate ice cream is sweet because it has lots of sugar in it.\nI love fish pie. It's __delicious__!\nDad adds chilli to chicken, so it is __spicy__.\nDon't try the pumpkin ice cream – it's __disgusting__! Yuk!\nIs it really apple pie? I think it's lemon pie – it's very __sour__.\n__Salty__ popcorn is my favourite snack."}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'speaking', $blk${"title": "SPEAKING 🎤 Ответь вслух и запиши ответ", "needs_review": true, "html": "<p>Ответь на вопросы по блогу Саши:</p><ol><li>Which pie would you like to try? Why?</li><li>What is your favourite pie? Where is it from?</li><li>Do you prefer fish or meat pies? Why?</li><li>Have you ever eaten quiche?</li></ol>", "sample": "", "sample_tts": {"text": "My favourite pie is a cherry pie and it is from my grandma's kitchen.", "voice": "en_GB-alba"}}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_popper.webp\" alt=\"\" style=\"height:200px\"></p><p>Блог прочитан — и про пироги мира ты теперь знаешь.</p>"}$blk$::jsonb, 6);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = 'a4f27767-6f35-491b-8def-f7efd9caacee' and title = 'Homework 6';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('a4f27767-6f35-491b-8def-f7efd9caacee', 'Homework 6', 5, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 5, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 6 · Listening and Writing</h2><p>Сегодня слушаем рецепт от телеповара и пишем свой.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай описание блюда и выбери, как оно называется", "questions": [{"q": "Fish with chips and green peas on a plate.", "type": "single", "correct": [1], "options": [{"text": "Chicken soup"}, {"text": "Fish and chips"}, {"text": "Chicken pie and chips"}]}, {"q": "Chicken, potatoes, onion and water — everything goes in the blender.", "type": "single", "correct": [0], "options": [{"text": "Chicken soup"}, {"text": "Fish and chips"}, {"text": "Chicken pie and chips"}]}, {"q": "A hot pie with chicken inside and chips next to it.", "type": "single", "correct": [2], "options": [{"text": "Chicken soup"}, {"text": "Fish and chips"}, {"text": "Chicken pie and chips"}]}]}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "LISTENING 🎧 Послушай рецепт телеповара и выбери правильный ответ", "audio": "https://api.wowteach.ru/storage/v1/object/public/classroom-media/gg3%20wb/GG%20L3%20WkBk%20A15.mp3", "skill": "listening", "questions": [{"q": "Which meal is the chef preparing?", "type": "single", "correct": [0], "options": [{"text": "chicken soup"}, {"text": "fish and chips"}, {"text": "chicken pie and chips"}]}, {"q": "How many potatoes do you need?", "type": "single", "correct": [1], "options": [{"text": "two"}, {"text": "three"}, {"text": "four"}]}, {"q": "How much water do you need?", "type": "single", "correct": [1], "options": [{"text": "one litre"}, {"text": "two litres"}, {"text": "three litres"}]}, {"q": "How long do you boil the chicken?", "type": "single", "correct": [2], "options": [{"text": "fifteen minutes"}, {"text": "twenty minutes"}, {"text": "thirty minutes"}]}, {"q": "What do you do when the chicken is ready?", "type": "single", "correct": [0], "options": [{"text": "You take the bones out of the meat."}, {"text": "You throw the water away."}, {"text": "You put the chicken in the oven."}]}, {"q": "What do you use at the end?", "type": "single", "correct": [1], "options": [{"text": "a frying pan"}, {"text": "a blender"}, {"text": "a cake tin"}]}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "LISTENING 🎧 Послушай рецепт ещё раз и перетащи слова в пропуски", "mode": "drag", "text": "Ingredients:\none chicken\n__three__ potatoes\none __onion__\n__two__ litres of water\nsalt and pepper\nsome __oil__\nInstructions:\nCut the chicken in pieces.\nBoil the chicken for thirty minutes.\nTake the bones out of the __meat__.\nKeep the __water__.\nPeel and chop the vegetables.\nFry the onion in oil.\nAdd the vegetables to the chicken and water.\nCook for __thirty__ minutes and then blend in the blender.\nAdd some salt and pepper.", "audio": "https://api.wowteach.ru/storage/v1/object/public/classroom-media/gg3%20wb/GG%20L3%20WkBk%20A15.mp3", "skill": "listening"}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай рецепт французских тостов из блога бабушки и выбери правильный вариант. В рецептах пишут командами: Slice the bread.", "questions": [{"q": "Two slices of bread, one egg, one cup of milk, some honey. Как называется этот список?", "type": "single", "correct": [0], "options": [{"text": "Ingredients"}, {"text": "Instructions"}]}, {"q": "You ___ need: a frying pan, a fork, a spoon.", "type": "single", "correct": [0], "options": [{"text": "also"}, {"text": "never"}]}, {"q": "Slice the bread. Break the egg into a bowl. Как называется этот список?", "type": "single", "correct": [1], "options": [{"text": "Ingredients"}, {"text": "Instructions"}]}, {"q": "___ the bread.", "type": "single", "correct": [0], "options": [{"text": "Slice"}, {"text": "You slice"}]}, {"q": "___ the egg into a bowl.", "type": "single", "correct": [0], "options": [{"text": "Break"}, {"text": "Broke"}]}, {"q": "___ the milk and mix.", "type": "single", "correct": [1], "options": [{"text": "It adds"}, {"text": "Add"}]}, {"q": "___ the toast on a plate and put a spoonful of honey on the toast.", "type": "single", "correct": [1], "options": [{"text": "You put"}, {"text": "Put"}]}]}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'task', $blk${"title": "WRITING ✍️ Напиши свой рецепт перекуса с хлебом", "needs_review": true, "html": "<p>Сначала составь заметки: продукты (<i>some bread, …</i>), что ещё нужно (<i>a knife, …</i>) и что делать (<i>slice the bread, …</i>).</p><p>Потом напиши рецепт по образцу французских тостов: список продуктов, список нужных вещей и инструкции командами (Beat the eggs and sugar.).</p><p>Начни так: <i>Ingredients: …</i></p>"}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_certificate.webp\" alt=\"\" style=\"height:200px\"></p><p>И рецепт на слух понят, и свой записан.</p>"}$blk$::jsonb, 6);
end $$;

do $$
declare v_lesson uuid;
begin
  select id into v_lesson from classroom_lessons
   where unit_id = 'a4f27767-6f35-491b-8def-f7efd9caacee' and title = 'Homework 7';
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, sort_order, kind, is_published)
    values ('a4f27767-6f35-491b-8def-f7efd9caacee', 'Homework 7', 6, 'homework', false) returning id into v_lesson;
  else
    update classroom_lessons set sort_order = 6, kind = 'homework' where id = v_lesson;
    delete from classroom_blocks where lesson_id = v_lesson;
  end if;
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/hello_teen_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Unit 6 · Check yourself!</h2><p>Повторяем весь юнит перед тестом.</p>"}$blk$::jsonb, 0);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай рецепт традиционного английского воскресного обеда и выбери правильное слово", "questions": [{"q": "First peel the potatoes. Then ___ the chicken and the potatoes in the oven for two hours.", "type": "single", "correct": [1], "options": [{"text": "bake"}, {"text": "roast"}]}, {"q": "___ the carrots.", "type": "single", "correct": [0], "options": [{"text": "Slice"}, {"text": "Fry"}]}, {"q": "Always use a sharp ___. Be careful.", "type": "single", "correct": [1], "options": [{"text": "cup"}, {"text": "knife"}]}, {"q": "___ the vegetables for fifteen minutes.", "type": "single", "correct": [0], "options": [{"text": "Boil"}, {"text": "Mix"}]}, {"q": "Add salt and pepper and your ___ meal is ready! Yum yum!", "type": "single", "correct": [1], "options": [{"text": "awful"}, {"text": "delicious"}]}]}$blk$::jsonb, 1);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'match', $blk${"title": "Соедини вопрос с ответом", "pairs": [{"left": "Have you ever made pizza?", "right": "Yes, I have! I love Italian food."}, {"left": "Have your parents ever won anything?", "right": "No, they haven't."}, {"left": "Has Fred bought a new phone?", "right": "No. He hasn't got enough money."}, {"left": "Have you tried Grandma's apple pie?", "right": "Yes, we have. It's very good."}, {"left": "Have you and Jack finished your meal?", "right": "No, Dad. We're still eating."}]}$blk$::jsonb, 2);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'quiz', $blk${"title": "Прочитай разговоры и выбери правильный вариант", "questions": [{"q": "A: ___ like a hot drink?", "type": "single", "correct": [0], "options": [{"text": "Would you"}, {"text": "You would"}]}, {"q": "B: ___ something cold, please.", "type": "single", "correct": [1], "options": [{"text": "I like"}, {"text": "I'd like"}]}, {"q": "A: Would you like to watch TV ___ a DVD?", "type": "single", "correct": [0], "options": [{"text": "or"}, {"text": "and"}]}, {"q": "B: I'd ___ watch TV.", "type": "single", "correct": [0], "options": [{"text": "prefer to"}, {"text": "prefer"}]}, {"q": "A: Would you like to go to the park or ___ to the beach?", "type": "single", "correct": [0], "options": [{"text": "go"}, {"text": "going"}]}, {"q": "B: I don't ___.", "type": "single", "correct": [1], "options": [{"text": "choose"}, {"text": "mind"}]}]}$blk$::jsonb, 3);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Прочитай разговор мамы и Дэна и впиши пропущенное слово", "mode": "type", "text": "Mum: Can you set the table, please? We need knives and forks for everyone.\nDan: OK. What about __spoons__ for soup?\nMum: Yes, and we also need __bowls__ to put the soup in and plates for the fish pie.\nDan: Fish pie? Oh! I love fish pie. But please don't make it __spicy__, Mum. I don't like chilli.\nMum: There isn't any chilli in the pie! And there's something __sweet__ for dessert.\nDan: Great! What are we drinking? Do we need big or small __glasses__?\nMum: Big please. I've bought some lemonade."}$blk$::jsonb, 4);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'gaps', $blk${"title": "Впиши глагол в Present Perfect", "mode": "type", "text": "We have made (make) popcorn for everyone!\nDad __has bought__ (buy) some yummy bananas!\nMy friends __haven't brought__ (not bring) a cake for my birthday – it's a big pizza! It smells great.\n__Has Doug tried__ (Doug / try) a fish pie?\nI __have chopped__ (chop) the tomatoes for the salad.\n__Have you watched__ (you / watch) this cooking competition on TV? Let's watch it. It's great!"}$blk$::jsonb, 5);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'speaking', $blk${"title": "SPEAKING 🎤 Расскажи вслух и запиши ответ", "needs_review": true, "html": "<p>Расскажи про блюдо, которое ты уже готовил сам: что это было, что ты делал с продуктами и каким оно получилось на вкус. Четыре-пять предложений.</p>", "sample": "", "sample_tts": {"text": "I have cooked pancakes with my dad and they were delicious.", "voice": "en_GB-alba"}}$blk$::jsonb, 6);
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values (v_lesson, 'text', $blk${"html": "<p><img src=\"https://classroom.wowteach.ru/media/shared/gg/bye_trophy.webp\" alt=\"\" style=\"height:200px\"></p><p>Юнит пройден! Можно браться за тест.</p>"}$blk$::jsonb, 7);
end $$;
