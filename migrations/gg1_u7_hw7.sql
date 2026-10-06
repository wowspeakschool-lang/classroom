-- Go Getter 1 · Unit 7 · Animals · Homework 7
-- собрано tools/gg1_build.py --lesson u7_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 7 · Animals', 7
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 7 · Animals');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 7 · Animals';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>Здорово, что ты решил сделать домашнюю работу.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильную форму глагола", "questions": [{"q": "A cat ___ milk.", "type": "single", "options": [{"text": "like"}, {"text": "likes"}, {"text": "liks"}], "correct": [1]}, {"q": "Lions ___ in Africa.", "type": "single", "options": [{"text": "livs"}, {"text": "lives"}, {"text": "live"}], "correct": [2]}, {"q": "My dog ___ in the garden every day.", "type": "single", "options": [{"text": "plays"}, {"text": "plais"}, {"text": "play"}], "correct": [0]}, {"q": "Elephants ___ plants.", "type": "single", "options": [{"text": "eates"}, {"text": "eat"}, {"text": "eats"}], "correct": [1]}, {"q": "He ___ a pet rabbit.", "type": "single", "options": [{"text": "have"}, {"text": "haves"}, {"text": "has"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'exact_input', replace($blk${"title": "Перепиши предложения — сделай их отрицательными. Пример: I like milk. → I don't like milk.", "items": [{"prompt": "A snake likes milk.", "accept": ["A snake doesn't like milk.", "A snake doesn’t like milk.", "A snake doesn't like milk", "A snake doesn’t like milk", "A snake does not like milk.", "A snake does not like milk"]}, {"prompt": "My cat lives in the jungle.", "accept": ["My cat doesn't live in the jungle.", "My cat doesn’t live in the jungle.", "My cat doesn't live in the jungle", "My cat doesn’t live in the jungle", "My cat does not live in the jungle.", "My cat does not live in the jungle"]}, {"prompt": "Tigers eat grass.", "accept": ["Tigers don't eat grass.", "Tigers don’t eat grass.", "Tigers don't eat grass", "Tigers don’t eat grass", "Tigers do not eat grass.", "Tigers do not eat grass"]}, {"prompt": "I have a wild animal at home.", "accept": ["I don't have a wild animal at home.", "I don’t have a wild animal at home.", "I don't have a wild animal at home", "I don’t have a wild animal at home", "I do not have a wild animal at home.", "I do not have a wild animal at home"]}, {"prompt": "Dogs fly.", "accept": ["Dogs don't fly.", "Dogs don’t fly.", "Dogs don't fly", "Dogs don’t fly", "Dogs do not fly.", "Dogs do not fly"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши пропущенные слова: do / does / don't / doesn't", "mode": "drag", "text": "1. A: __Do__ you have a pet? B: Yes, I __do__. I have a dog.\n2. A: __Do__ cats like milk? B: Yes, they __do__.\n3. A: __Does__ your dog like cats? B: No, it __doesn't__.\n4. A: Where __do__ lions live? B: They live in Africa.\n5. A: __Do__ snakes drink milk? B: No, they __don't__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'speaking', replace($blk${"title": "Ответь на вопросы 🎤", "html": "<ol><li>Do you have a pet?</li><li>What does your pet eat?</li><li>Do crocodiles live in your house?</li><li>Does your friend go to school?</li><li>Do your parents have a car?</li></ol>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'match', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Найди название каждого животного: соедини слово и картинку ⭐", "pairs": [{"left": "bird", "right_image": "@@MEDIA@@gg1/u7/animal_bird.webp", "left_audio_tts": "bird"}, {"left": "fish", "right_image": "@@MEDIA@@gg1/u7/animal_fish.webp", "left_audio_tts": "fish"}, {"left": "fly", "right_image": "@@MEDIA@@gg1/u7/animal_fly.webp", "left_audio_tts": "fly"}, {"left": "frog", "right_image": "@@MEDIA@@gg1/u7/animal_frog.webp", "left_audio_tts": "frog"}, {"left": "kangaroo", "right_image": "@@MEDIA@@gg1/u7/animal_kangaroo.webp", "left_audio_tts": "kangaroo"}, {"left": "monkey", "right_image": "@@MEDIA@@gg1/u7/animal_monkey.webp", "left_audio_tts": "monkey"}, {"left": "tiger", "right_image": "@@MEDIA@@gg1/u7/animal_tiger.webp", "left_audio_tts": "tiger"}, {"left": "whale", "right_image": "@@MEDIA@@gg1/u7/animal_whale.webp", "left_audio_tts": "whale"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ⭐", "questions": [{"q": "Crocodiles ___ live in the desert.", "type": "single", "options": [{"text": "doesn't"}, {"text": "don't"}], "correct": [1], "image": "@@MEDIA@@gg1/u7/animal_crocodile.webp"}, {"q": "An elephant ___ fly.", "type": "single", "options": [{"text": "doesn't"}, {"text": "don't"}], "correct": [0], "image": "@@MEDIA@@gg1/u7/animal_elephant.webp"}, {"q": "Butterflies ___ eat meat.", "type": "single", "options": [{"text": "doesn't"}, {"text": "don't"}], "correct": [1], "image": "@@MEDIA@@gg1/u7/animal_butterfly.webp"}, {"q": "A spider ___ have wings.", "type": "single", "options": [{"text": "doesn't"}, {"text": "don't"}], "correct": [0], "image": "@@MEDIA@@gg1/u7/animal_spider.webp"}, {"q": "My rabbit doesn't ___ fish.", "type": "single", "options": [{"text": "eats"}, {"text": "eat"}], "correct": [1], "image": "@@MEDIA@@gg1/u7/animal_rabbit.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ⭐", "questions": [{"q": "___ giraffes eat leaves? — Yes, they do.", "type": "single", "options": [{"text": "Does"}, {"text": "Do"}], "correct": [1], "image": "@@MEDIA@@gg1/u7/animal_giraffe.webp"}, {"q": "___ a kangaroo jump? — Yes, it does.", "type": "single", "options": [{"text": "Does"}, {"text": "Do"}], "correct": [0], "image": "@@MEDIA@@gg1/u7/animal_kangaroo.webp"}, {"q": "Does a whale live in the sea? — Yes, it ___.", "type": "single", "options": [{"text": "do"}, {"text": "does"}], "correct": [1], "image": "@@MEDIA@@gg1/u7/animal_whale.webp"}, {"q": "Do frogs fly? — No, they ___.", "type": "single", "options": [{"text": "don't"}, {"text": "doesn't"}], "correct": [0], "image": "@@MEDIA@@gg1/u7/animal_frog.webp"}, {"q": "___ your cat like milk? — Yes, it does.", "type": "single", "options": [{"text": "Do"}, {"text": "Does"}], "correct": [1], "image": "@@MEDIA@@gg1/u7/animal_cat.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/good_luck_clover.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты проделал отличную работу! Молодец 💕</h3><p>Уверена, ты справишься с тестом на все сто! Удачи!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
