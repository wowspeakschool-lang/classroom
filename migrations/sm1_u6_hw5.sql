-- Super Minds 1 · Unit 6 · My house · Homework 5
-- собрано tools/sm1_build.py --lesson u6_hw5
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 6 · My house', 6
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 6 · My house');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 6 · My house';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>Тебя ждут интересные упражнения и увлекательное видео, а также ДОПОЛНИТЕЛЬНОЕ задание, которое можно выполнить ПО ЖЕЛАНИЮ и получить дополнительные кристаллы 💎</p><p>Чтобы стать ЧЕМПИОНОМ — собери все кристаллы, которые ты будешь получать за выполнение каждого задания.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Сейчас тебе нужно будет посмотреть видео. Герой видео проведёт небольшую экскурсию по своему дому. Попробуй угадать, какие комнаты есть у него в доме 🏡", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p>Внимательно посмотри на картинку. Под картинкой есть предложения: прочитай их и скажи, правда это (True) или неправда (False). За задания под картинкой ты можешь заработать 2 💎💎</p><p><img src=\"@@MEDIA@@sm1/u6/hw5_house_attic.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'truefalse', replace($blk${"title": "Посмотри на картинку и выбери True, если предложение верно, False — если не верно.", "statements": [{"text": "There are three rooms in the house.", "correct": false}, {"text": "There is a living room.", "correct": true}, {"text": "There is a kitchen.", "correct": true}, {"text": "There isn't a bathroom.", "correct": false}, {"text": "There is a cellar.", "correct": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/good_luck_clover.webp\" alt=\"\" style=\"height:160px\"></p><p>А в следующем упражнении мы с тобой потренируемся составлять предложения.</p><p>Расставь слова в правильном порядке, чтобы получилось предложение. Тебя ждут 5 таких предложений. Составь их и получи 2 💎💎</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке.", "image": "@@MEDIA@@sm1/u6/hw5_bedroom.webp", "words": ["There", "are", "two", "bedrooms", "in", "the house."], "sentence": "There are two bedrooms in the house.", "audio_tts": "There are two bedrooms in the house."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке.", "image": "@@MEDIA@@sm1/u6/hw5_living_room.webp", "words": ["There", "isn't", "a", "living", "room."], "sentence": "There isn't a living room.", "audio_tts": "There isn't a living room."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке.", "image": "@@MEDIA@@sm1/u6/hw5_floorplan.webp", "words": ["There", "aren't", "five", "bedrooms."], "sentence": "There aren't five bedrooms.", "audio_tts": "There aren't five bedrooms."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке.", "image": "@@MEDIA@@sm1/u6/hw5_kitchen.webp", "words": ["There", "is", "a", "kitchen."], "sentence": "There is a kitchen.", "audio_tts": "There is a kitchen."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке.", "image": "@@MEDIA@@sm1/u6/hw5_house.webp", "words": ["How", "many", "rooms", "are", "there", "in", "the house?"], "sentence": "How many rooms are there in the house?", "audio_tts": "How many rooms are there in the house?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'speaking', replace($blk${"title": "Прочитай вслух 🎤", "html": "<p>Следующее упражнение оценивается в целых 3 💎💎💎</p><p>Посмотри ещё раз на картинку домика и прочитай его описание. Прочитай текст вслух. Запиши себя на диктофон.</p><p><i>I live in a nice house.<br>There are 4 rooms. There is a bedroom, a bathroom, a living room and a kitchen. There isn't a cellar. There isn't a hall.<br>I like my house!</i></p>", "image": "@@MEDIA@@sm1/u6/hw5_house_attic.webp", "sample": "", "sample_tts": "I live in a nice house. There are 4 rooms. There is a bedroom, a bathroom, a living room and a kitchen. There isn't a cellar. There isn't a hall. I like my house!", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'task', replace($blk${"title": "Опиши свой дом ✏️", "needs_review": true, "html": "<p>Здесь тебя ждёт ещё одно задание. За него ты получишь 4 💎💎💎💎</p><p>Опиши свой дом, используя <b>there is / there are / there isn't / there aren't</b>. Используй предыдущее упражнение как пример.</p><p>Напиши 5–7 предложений.</p><p>(По желанию можешь нарисовать рисунок своего дома и показать учителю на уроке. За рисунок я подарю тебе дополнительный 💎)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'exact_input', replace($blk${"items": [{"image": "@@MEDIA@@sm1/u6/room_bathroom.webp", "prompt": "⭐ Дополнительное задание. Впиши слово: ванная", "accept": ["bathroom", "Bathroom", "a bathroom"]}, {"image": "@@MEDIA@@sm1/u6/room_bedroom.webp", "prompt": "⭐ Дополнительное задание. Впиши слово: спальня", "accept": ["bedroom", "Bedroom", "a bedroom"]}, {"image": "@@MEDIA@@sm1/u6/room_living_room.webp", "prompt": "⭐ Дополнительное задание. Впиши слово: гостиная", "accept": ["living room", "Living room", "a living room"]}, {"image": "@@MEDIA@@sm1/u6/room_hall.webp", "prompt": "⭐ Дополнительное задание. Впиши слово: коридор", "accept": ["hall", "Hall", "a hall"]}, {"image": "@@MEDIA@@sm1/u6/room_kitchen.webp", "prompt": "⭐ Дополнительное задание. Впиши слово: кухня", "accept": ["kitchen", "Kitchen", "a kitchen"]}, {"image": "@@MEDIA@@sm1/u6/room_cellar.webp", "prompt": "⭐ Дополнительное задание. Впиши слово: подвал", "accept": ["cellar", "Cellar", "a cellar"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "⭐ Посмотри на картинку домика и выбери правильный вариант: ___ a bedroom.", "type": "single", "image": "@@MEDIA@@sm1/u6/hw5_house_attic.webp", "options": [{"text": "There is"}, {"text": "There are"}, {"text": "There isn't"}], "correct": [0]}, {"q": "___ a hall.", "type": "single", "options": [{"text": "There is"}, {"text": "There isn't"}, {"text": "There aren't"}], "correct": [1]}, {"q": "___ four rooms.", "type": "single", "options": [{"text": "There is"}, {"text": "There isn't"}, {"text": "There are"}], "correct": [2]}, {"q": "___ any spiders in the kitchen.", "type": "single", "options": [{"text": "There aren't"}, {"text": "There isn't"}, {"text": "There is"}], "correct": [0]}, {"q": "___ a cellar.", "type": "single", "options": [{"text": "There are"}, {"text": "There aren't"}, {"text": "There isn't"}], "correct": [2]}, {"q": "How many rooms are there?", "type": "single", "options": [{"text": "There is four rooms."}, {"text": "There are four rooms."}, {"text": "There aren't four rooms."}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание! Молодец! 💎</h3><p>За прохождение домашнего задания держи ещё 1 дополнительный 💎</p><p>Жду тебя на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 14);
end
$mig$;
