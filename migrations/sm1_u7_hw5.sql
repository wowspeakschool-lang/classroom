-- Super Minds 1 · Unit 7 · Get dressed · Homework 5
-- собрано tools/sm1_build.py --lesson u7_hw5
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 7 · Get dressed', 7
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 7 · Get dressed');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 7 · Get dressed';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание! 👋</h2><p>Тебя ждут интересные упражнения и увлекательное видео, а также ДОПОЛНИТЕЛЬНОЕ задание, которое можно выполнить ПО ЖЕЛАНИЮ и получить дополнительные кристаллы 💎.</p><p>Чтобы стать ЧЕМПИОНОМ — собери все кристаллы, которые ты будешь получать за выполнение каждого упражнения.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Сейчас тебе нужно посмотреть видео и выполнить задание.</p><p>Главные герои видео выступают на шоу талантов и показывают фокусы с помощью одежды. Как думаешь, какие фокусы они показывают?</p><p>Посмотри видео и узнай, угадал ли ты 🎩</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'video', replace($blk${"title": "Видео: шоу талантов", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"html": "<p>Внимательно посмотри на картинку.</p><p><img src=\"@@MEDIA@@sm1/u7/party_scene_names.webp\" alt=\"Emma, Ken, Lara, Paul\" style=\"max-width:100%\"></p><p>Под картинкой есть предложения. Прочитай их и скажи, это правда (True) или неправда (False). Если по картинке нельзя определить, правда это или неправда, выбери <b>Not stated</b>.</p><p>За это задание ты можешь заработать 2 💎💎</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "True, False или Not stated?", "questions": [{"q": "Emma is watching TV.", "type": "single", "image": "@@MEDIA@@sm1/u7/party_scene_names.webp", "options": [{"text": "True"}, {"text": "False"}, {"text": "Not stated"}], "correct": [0]}, {"q": "Ken is playing a game.", "type": "single", "image": "@@MEDIA@@sm1/u7/party_scene_names.webp", "options": [{"text": "True"}, {"text": "False"}, {"text": "Not stated"}], "correct": [0]}, {"q": "Lara is wearing pink jeans.", "type": "single", "image": "@@MEDIA@@sm1/u7/party_scene_names.webp", "options": [{"text": "True"}, {"text": "False"}, {"text": "Not stated"}], "correct": [2]}, {"q": "Paul is playing computer games.", "type": "single", "image": "@@MEDIA@@sm1/u7/party_scene_names.webp", "options": [{"text": "True"}, {"text": "False"}, {"text": "Not stated"}], "correct": [1]}, {"q": "Ken is wearing a yellow sweater.", "type": "single", "image": "@@MEDIA@@sm1/u7/party_scene_names.webp", "options": [{"text": "True"}, {"text": "False"}, {"text": "Not stated"}], "correct": [0]}, {"q": "Emma is wearing a green T-shirt.", "type": "single", "image": "@@MEDIA@@sm1/u7/party_scene_names.webp", "options": [{"text": "True"}, {"text": "False"}, {"text": "Not stated"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p>А в следующем упражнении мы с тобой потренируемся составлять предложения.</p><p>Расставь слова в правильном порядке, чтобы получилось предложение. Тебя ждут 6 таких предложений. Составь их и получи 2 💎💎</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["Anna", "is", "wearing", "a", "blue", "skirt."], "sentence": "Anna is wearing a blue skirt.", "audio_tts": "Anna is wearing a blue skirt.", "image": "@@MEDIA@@sm1/u7/outfit_anna.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["What", "is", "Bob", "doing?"], "sentence": "What is Bob doing?", "audio_tts": "What is Bob doing?", "image": "@@MEDIA@@sm1/u7/boy_singing.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"words": ["Are", "Amy and Hannah", "riding", "bikes?"], "sentence": "Are Amy and Hannah riding bikes?", "audio_tts": "Are Amy and Hannah riding bikes?", "image": "@@MEDIA@@sm1/u7/obj_bikes.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"words": ["Emma and Tom", "are", "watching", "TV."], "sentence": "Emma and Tom are watching TV.", "audio_tts": "Emma and Tom are watching TV.", "image": "@@MEDIA@@sm1/u7/watching_tv_clipart.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"words": ["Is", "Sam", "eating", "a sandwich?"], "sentence": "Is Sam eating a sandwich?", "audio_tts": "Is Sam eating a sandwich?", "image": "@@MEDIA@@sm1/u7/obj_sandwich.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'order', replace($blk${"words": ["Is", "Oscar", "playing", "football?"], "sentence": "Is Oscar playing football?", "audio_tts": "Is Oscar playing football?", "image": "@@MEDIA@@sm1/u7/football_ball.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'speaking', replace($blk${"title": "Прочитай вслух 🎤", "needs_review": true, "image": "@@MEDIA@@sm1/u7/emma_singing.webp", "sample": "", "sample_tts": "Emma is my best friend. Emma is wearing a pink T-shirt, green trousers and black shoes. She is singing.", "html": "<p>Посмотри! На картинке моя подруга. Её зовут Эмма!</p><p>Посмотри на картинку и прочитай описание девочки. Нажми на микрофон и запиши, как ты читаешь текст вслух. За это задание ты получишь 3 💎💎💎</p><p><b>Emma is my best friend.<br>Emma is wearing a pink T-shirt, green trousers and black shoes.<br>She is singing.</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'task', replace($blk${"title": "Нарисуй своего друга", "needs_review": true, "html": "<p>Нарисуй своего друга, опиши его и покажи рисунок на уроке. Используй предыдущее упражнение как пример.</p><p>Напиши 3–5 предложений. За это задание ты получишь 4 💎💎💎💎</p><p><i>My best friend is … He/She is wearing … He/She is …</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'exact_input', replace($blk${"items": [{"image": "@@MEDIA@@sm1/u7/watching_tv_clipart.webp", "prompt": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Впиши слово с -ing.<br>Emma and Tom are ___ TV. (watch)", "accept": ["watching"]}, {"image": "@@MEDIA@@sm1/u7/boy_singing.webp", "prompt": "Bob is ___. (sing)", "accept": ["singing"]}, {"image": "@@MEDIA@@sm1/u7/obj_sandwich.webp", "prompt": "Sam is ___ a sandwich. (eat)", "accept": ["eating"]}, {"image": "@@MEDIA@@sm1/u7/obj_bikes.webp", "prompt": "Amy and Hannah are ___ bikes. (ride)", "accept": ["riding"]}, {"image": "@@MEDIA@@sm1/u7/football_ball.webp", "prompt": "Oscar is ___ football. (play)", "accept": ["playing"]}, {"image": "@@MEDIA@@sm1/u7/emma_singing.webp", "prompt": "Emma is ___ a pink T-shirt. (wear)", "accept": ["wearing"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант", "questions": [{"q": "Выбери правильный вариант:<br>Emma ___ watching TV.", "type": "single", "image": "@@MEDIA@@sm1/u7/party_scene_names.webp", "options": [{"text": "is"}, {"text": "are"}, {"text": "am"}], "correct": [0]}, {"q": "___ Ken playing a game? — Yes, he is.", "type": "single", "image": "@@MEDIA@@sm1/u7/party_scene_names.webp", "options": [{"text": "Are"}, {"text": "Is"}, {"text": "Do"}], "correct": [1]}, {"q": "Is Paul eating cake? — Yes, he ___.", "type": "single", "image": "@@MEDIA@@sm1/u7/party_scene_names.webp", "options": [{"text": "isn't"}, {"text": "does"}, {"text": "is"}], "correct": [2]}, {"q": "Lara ___ playing football. She's playing a computer game.", "type": "single", "image": "@@MEDIA@@sm1/u7/party_scene_names.webp", "options": [{"text": "is"}, {"text": "isn't"}, {"text": "aren't"}], "correct": [1]}, {"q": "Ken is ___ a yellow sweater.", "type": "single", "image": "@@MEDIA@@sm1/u7/party_scene_names.webp", "options": [{"text": "wear"}, {"text": "wearing"}, {"text": "wears"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 15),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание! Молодец!</h3><p>За прохождение домашнего задания держи ещё 1 дополнительный 💎</p><p>Жду тебя на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 16);
end
$mig$;
