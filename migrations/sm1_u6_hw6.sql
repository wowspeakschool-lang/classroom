-- Super Minds 1 · Unit 6 · My house · Homework 6
-- собрано tools/sm1_build.py --lesson u6_hw6
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
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет!</h2><p>Сегодня мы узнаем о разных домах. Тебя ждут интересные увлекательные упражнения и видео.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<h3>Давай повторим всё, что выучили с тобой на уроке:</h3><p><img src=\"@@MEDIA@@sm1/u6/card_types_of_homes.webp\" alt=\"Types of Homes\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'video', replace($blk${"title": "Посмотри видео и выполни задание под ним. В этом видео Сэм путешествует по всему миру и узнаёт о различных видах домов. А где живёшь ты?", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'match', replace($blk${"title": "А теперь давай вспомним названия домиков, которые мы выучили на уроке. Соедини название с картинкой.", "pairs": [{"left_image": "@@MEDIA@@sm1/u6/home_tree.webp", "right": "It's a tree house.", "right_audio_tts": "It's a tree house."}, {"left_image": "@@MEDIA@@sm1/u6/home_boat.webp", "right": "It's a house boat.", "right_audio_tts": "It's a house boat."}, {"left_image": "@@MEDIA@@sm1/u6/home_yurt.webp", "right": "It's a yurt.", "right_audio_tts": "It's a yurt."}, {"left_image": "@@MEDIA@@sm1/u6/home_cave.webp", "right": "It's a cave house.", "right_audio_tts": "It's a cave house."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Молодец, ты справился с большей частью заданий! А теперь прочитай текст и заполни пропуски.", "mode": "drag", "image": "@@MEDIA@@sm1/u6/homes_many.webp", "text": "1) My house is in water. I live in a __house boat__.\n2) My house is in a tree. I live in a __tree house__.\n3) My house is round. I live in a __yurt__.\n4) My house is in a cave. I live in a __cave house__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Посмотри! Я очень хочу побывать в этом доме. Прочитай его описание и выбери правильный вариант для каждого пропуска.<br>Look! It's a ___.", "type": "single", "image": "@@MEDIA@@sm1/u6/cave_house_room.webp", "options": [{"text": "tree house"}, {"text": "cave house"}, {"text": "house boat"}, {"text": "yurt"}], "correct": [1]}, {"q": "There are ___ rooms.", "type": "single", "image": "@@MEDIA@@sm1/u6/cave_house_room.webp", "options": [{"text": "two"}, {"text": "five"}, {"text": "ten"}], "correct": [0]}, {"q": "It has got a ___ and a bathroom.", "type": "single", "image": "@@MEDIA@@sm1/u6/cave_house_room.webp", "options": [{"text": "kitchen"}, {"text": "garden"}, {"text": "bedroom"}], "correct": [2]}, {"q": "It hasn't got a ___.", "type": "single", "image": "@@MEDIA@@sm1/u6/cave_house_room.webp", "options": [{"text": "bedroom"}, {"text": "kitchen"}, {"text": "bathroom"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'speaking', replace($blk${"title": "Мой домик мечты 🎤", "html": "<p>Ура! Осталось всего 1 задание.</p><p>Выбери один из домиков, которые мы сегодня выучили. Может быть тот, который тебе больше всего понравился, в котором ты бы хотел жить или просто побывать. Нарисуй его, нажми на микрофон и опиши. Используй предыдущее задание как пример.</p><p><i>Look! It's a tree house. There are two rooms. It has got a bedroom and a bathroom. It hasn't got a kitchen. I like it!</i></p>", "image": "@@MEDIA@@sm1/u6/homes_four.webp", "sample": "", "sample_tts": "Look! It's a tree house. There are two rooms. It has got a bedroom and a bathroom. It hasn't got a kitchen. I like it!", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание, ты замечательный ученик!</h3><p>За это лови звёздочку ⭐</p><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7);
end
$mig$;
