-- Super Minds 1 · Unit 6 · My house · Homework 2
-- собрано tools/sm1_build.py --lesson u6_hw2
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
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>В этом уроке тебя ждут интересные упражнения и видео!</p><p>В конце урока есть два дополнительных задания — их можно выполнить по желанию! Их выполняют самые смелые и крутые ученики.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<h3>Давай повторим всё, что выучили с тобой на уроке:</h3><p><img src=\"@@MEDIA@@sm1/u6/grammar_there_is_are.webp\" alt=\"There’s … / There are …\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'video', replace($blk${"title": "Для начала посмотри видео. В видео девочка описывает свою любимую комнату. Как думаешь, какая её любимая комната? Внимательно слушай, что говорит персонаж. Посмотри видео ещё раз и повторяй за персонажами.", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'match', replace($blk${"title": "Посмотри видео ещё раз и соедини левый столбик с правым, чтобы получились правильные предложения!", "pairs": [{"left": "There is", "right": "one bed.", "right_audio_tts": "There is one bed."}, {"left": "There are", "right": "two pillows.", "right_audio_tts": "There are two pillows."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'hotspot', replace($blk${"title": "Давай теперь попрактикуемся! Соедини предложения с картинками. Вперёд! У тебя всё получится ❤", "mode": "label", "image": "@@MEDIA@@sm1/u6/food_numbered.webp", "points": [{"x": 13, "y": 48, "text": "There are 3 bananas.", "audio_tts": "There are three bananas."}, {"x": 37, "y": 19, "text": "There is a sandwich.", "audio_tts": "There is a sandwich."}, {"x": 64, "y": 24, "text": "There is a doll.", "audio_tts": "There is a doll."}, {"x": 84, "y": 46, "text": "There are four apples.", "audio_tts": "There are four apples."}, {"x": 37, "y": 70, "text": "There are three sausages.", "audio_tts": "There are three sausages."}, {"x": 62, "y": 75, "text": "There is a dog.", "audio_tts": "There is a dog."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<h3>Отлично, ты справился с первой частью домашнего задания!</h3><p>Настало время следующего задания — внимательно посмотри на картинку. Под картинкой есть предложения: скажи, правда это (True) или неправда (False). Ты можешь всегда смотреть на картинку, чтобы проверить себя.</p><p><img src=\"@@MEDIA@@sm1/u6/cats_house.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'truefalse', replace($blk${"title": "Посмотри на картинку и выбери True, если предложение верно, False — если не верно.", "statements": [{"text": "There are two bedrooms in the house.", "correct": true}, {"text": "There are three rooms in the house.", "correct": false}, {"text": "There are two cats in the kitchen.", "correct": false}, {"text": "There are three dogs in the bedroom.", "correct": false}, {"text": "There are four cats in the kitchen.", "correct": true}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p>Смотри, это рисунок моего домика. Как тебе? Нравится?</p><p>Обязательно нарисуй свой дом и покажи мне рисунок на уроке.</p><p><img src=\"@@MEDIA@@sm1/u6/my_house_drawing.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'speaking', replace($blk${"title": "Расскажи про свой дом 🎤", "html": "<p>Посмотри на рисунок, который ты нарисовал. Запиши голосом, какие комнаты ты нарисовал. Не забудь использовать <b>there is / there are</b> (послушай пример ответа).</p><p><i>Например: There is a kitchen. There are two bedrooms. There is a bathroom.</i></p>", "sample": "", "sample_tts": "There is a kitchen. There are two bedrooms. There is a bathroom.", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'match', replace($blk${"title": "⭐ Дополнительное задание для настоящих чемпионов! Соедини картинки с описанием", "pairs": [{"left_image": "@@MEDIA@@sm1/u6/food_apples.webp", "right": "There are four apples.", "right_audio_tts": "There are four apples."}, {"left_image": "@@MEDIA@@sm1/u6/food_dog.webp", "right": "There is a dog.", "right_audio_tts": "There is a dog."}, {"left_image": "@@MEDIA@@sm1/u6/food_bananas.webp", "right": "There are three bananas.", "right_audio_tts": "There are three bananas."}, {"left_image": "@@MEDIA@@sm1/u6/food_doll.webp", "right": "There is a doll.", "right_audio_tts": "There is a doll."}, {"left_image": "@@MEDIA@@sm1/u6/food_sausages.webp", "right": "There are three sausages.", "right_audio_tts": "There are three sausages."}, {"left_image": "@@MEDIA@@sm1/u6/food_sandwich.webp", "right": "There is a sandwich.", "right_audio_tts": "There is a sandwich."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "___ a bed in the bedroom.", "type": "single", "options": [{"text": "There is"}, {"text": "There are"}], "correct": [0]}, {"q": "___ two pillows on the bed.", "type": "single", "options": [{"text": "There is"}, {"text": "There are"}], "correct": [1]}, {"q": "___ four cats in the kitchen.", "type": "single", "options": [{"text": "There is"}, {"text": "There are"}], "correct": [1]}, {"q": "___ a dog in the hall.", "type": "single", "options": [{"text": "There is"}, {"text": "There are"}], "correct": [0]}, {"q": "___ three bananas on the table.", "type": "single", "options": [{"text": "There is"}, {"text": "There are"}], "correct": [1]}, {"q": "___ a sandwich on the plate.", "type": "single", "options": [{"text": "There is"}, {"text": "There are"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание, ты молодец! 🌟</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11);
end
$mig$;
