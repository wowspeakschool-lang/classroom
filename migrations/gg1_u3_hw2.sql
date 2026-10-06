-- Go Getter 1 · Unit 3 · My home · Homework 2
-- собрано tools/gg1_build.py --lesson u3_hw2
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 3 · My home', 3
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 3 · My home');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 3 · My home';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет, герой! 👋</h2><p>Сегодня мы с тобой повторяем материал нашего урока! Проверяем наши знания! Удачи!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u3/card_there_is_are.webp\" alt=\"There is / There are\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'video', replace($blk${"title": "Посмотри видео, вспомни правила", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'sort', replace($blk${"title": "Распредели слова между двумя колонками: что идёт с there is, а что — с there are?", "groups": [{"name": "There is", "items": [{"text": "a book"}, {"text": "an armchair"}, {"text": "a carpet"}, {"text": "a curtain"}]}, {"name": "There are", "items": [{"text": "desks"}, {"text": "chairs"}, {"text": "lamps"}, {"text": "cushions"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "А теперь давай потренируемся! Выбери правильный ответ", "questions": [{"q": "There ___ a fridge in the kitchen.", "type": "single", "options": [{"text": "are"}, {"text": "is"}], "correct": [1]}, {"q": "There ___ many toys in the toy box.", "type": "single", "options": [{"text": "are"}, {"text": "is"}], "correct": [0]}, {"q": "There ___ five apples on the table.", "type": "single", "options": [{"text": "is"}, {"text": "are"}], "correct": [1]}, {"q": "There ___ a big dog in the garden.", "type": "single", "options": [{"text": "is"}, {"text": "are"}], "correct": [0]}, {"q": "There ___ three birds in the tree.", "type": "single", "options": [{"text": "is"}, {"text": "are"}], "correct": [1]}, {"q": "There ___ tasty cookies in the oven.", "type": "single", "options": [{"text": "are"}, {"text": "is"}], "correct": [0]}, {"q": "There ___ six chairs in the classroom.", "type": "single", "options": [{"text": "is"}, {"text": "are"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'task', replace($blk${"title": "Комнаты в моём доме ✍", "needs_review": true, "html": "<p>А какие комнаты есть в твоём доме? Напиши, используя there is / there are.</p><p><i>Пример: There are 3 bedrooms. There is 1 kitchen.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<h3>Добро пожаловать во вторую часть домашнего задания! 👋</h3><p>Давай повторим предлоги места:</p><p><img src=\"@@MEDIA@@gg1/u3/card_prepositions.webp\" alt=\"Prepositions of place\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку и выбери правильный ответ", "questions": [{"q": "There is a cat ___ the sofa.", "type": "single", "options": [{"text": "on"}, {"text": "under"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/prepositions_living_room.webp"}, {"q": "There are two dogs ___ the table.", "type": "single", "options": [{"text": "behind"}, {"text": "under"}], "correct": [1], "image": "@@MEDIA@@gg1/u3/prepositions_living_room.webp"}, {"q": "There is a toy plane ___ the box.", "type": "single", "options": [{"text": "in"}, {"text": "in front of"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/prepositions_living_room.webp"}, {"q": "There is a picture ___ the wall.", "type": "single", "options": [{"text": "under"}, {"text": "on"}], "correct": [1], "image": "@@MEDIA@@gg1/u3/prepositions_living_room.webp"}, {"q": "There is a guitar ___ the plant.", "type": "single", "options": [{"text": "next to"}, {"text": "in"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/prepositions_living_room.webp"}, {"q": "There is a backpack ___ the TV.", "type": "single", "options": [{"text": "between"}, {"text": "in front of"}], "correct": [1], "image": "@@MEDIA@@gg1/u3/prepositions_living_room.webp"}, {"q": "There is a window ___ the sofa.", "type": "single", "options": [{"text": "behind"}, {"text": "next to"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/prepositions_living_room.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'task', replace($blk${"title": "Опиши картинку ✍", "needs_review": true, "image": "@@MEDIA@@gg1/u3/kids_bedroom.webp", "html": "<p>Опиши картинку. Используй There is / There are и предлоги места.</p><p><i>Пример: There is a skateboard under the bed.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'task', replace($blk${"title": "Задание со звёздочкой ⭐", "needs_review": true, "image": "@@MEDIA@@gg1/u3/photo_bedroom.webp", "html": "<p>Для тех, кто хочет знать больше! Расскажи нам о своей комнате.</p><p><b>Tell me about your bedroom:</b></p><p><i>Пример: There is a bed …</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'match', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Соедини слова с картинкой ⭐", "pairs": [{"left_image": "@@MEDIA@@gg1/u3/prep_on.webp", "right": "on", "right_audio_tts": "on"}, {"left_image": "@@MEDIA@@gg1/u3/prep_under.webp", "right": "under", "right_audio_tts": "under"}, {"left_image": "@@MEDIA@@gg1/u3/prep_in.webp", "right": "in", "right_audio_tts": "in"}, {"left_image": "@@MEDIA@@gg1/u3/prep_behind.webp", "right": "behind", "right_audio_tts": "behind"}, {"left_image": "@@MEDIA@@gg1/u3/prep_next_to.webp", "right": "next to", "right_audio_tts": "next to"}, {"left_image": "@@MEDIA@@gg1/u3/prep_in_front_of.webp", "right": "in front of", "right_audio_tts": "in front of"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ⭐", "questions": [{"q": "The ball is ___ the box.", "type": "single", "options": [{"text": "on"}, {"text": "in front of"}, {"text": "in"}, {"text": "behind"}, {"text": "under"}, {"text": "next to"}], "correct": [3], "image": "@@MEDIA@@gg1/u3/prep_behind.webp"}, {"q": "The ball is ___ the box.", "type": "single", "options": [{"text": "behind"}, {"text": "in front of"}, {"text": "next to"}, {"text": "in"}, {"text": "on"}, {"text": "under"}], "correct": [4], "image": "@@MEDIA@@gg1/u3/prep_on.webp"}, {"q": "The ball is ___ the box.", "type": "single", "options": [{"text": "on"}, {"text": "next to"}, {"text": "in"}, {"text": "behind"}, {"text": "under"}, {"text": "in front of"}], "correct": [5], "image": "@@MEDIA@@gg1/u3/prep_in_front_of.webp"}, {"q": "The ball is ___ the box.", "type": "single", "options": [{"text": "in"}, {"text": "on"}, {"text": "under"}, {"text": "behind"}, {"text": "next to"}, {"text": "in front of"}], "correct": [0], "image": "@@MEDIA@@gg1/u3/prep_in.webp"}, {"q": "The ball is ___ the box.", "type": "single", "options": [{"text": "in front of"}, {"text": "next to"}, {"text": "in"}, {"text": "under"}, {"text": "behind"}, {"text": "on"}], "correct": [1], "image": "@@MEDIA@@gg1/u3/prep_next_to.webp"}, {"q": "The ball is ___ the box.", "type": "single", "options": [{"text": "in front of"}, {"text": "next to"}, {"text": "under"}, {"text": "behind"}, {"text": "on"}, {"text": "in"}], "correct": [2], "image": "@@MEDIA@@gg1/u3/prep_under.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>На сегодня твоё путешествие в страну ДЗ подошло к концу! 🎉</h3><p>Ты отлично со всем справился! До скорых встреч!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12);
end
$mig$;
