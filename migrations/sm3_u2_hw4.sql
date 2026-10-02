-- Super Minds 3 · Unit 2 · Food · Homework 4
-- собрано tools/sm3_build.py --lesson u2_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 2 · Food', 2
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 2 · Food');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 2 · Food';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет-привет, самый лучший ученик!</h2><p>Сегодня будем вспоминать историю, которую читали на уроке. Ну что, готов начинать?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Послушай аудио и найди ответ на вопрос: What happened to Buster?", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<h3>Ben and Lucy and the golden apple</h3><p><img src=\"@@MEDIA@@sm3/u2/story_buster.webp\" alt=\"Кадры истории\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "What happened to Buster?", "type": "single", "options": [{"text": "The dog bit him."}, {"text": "Horax and Zelda hurt him."}, {"text": "The snake bit him."}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант", "questions": [{"q": "Ben and Lucy want to go to the ___.", "type": "single", "options": [{"text": "school"}, {"text": "library"}, {"text": "village"}], "correct": [2]}, {"q": "An old man tells them to go to the ___ at the top of the mountain.", "type": "single", "options": [{"text": "cellar"}, {"text": "waterfall"}, {"text": "village"}], "correct": [1]}, {"q": "Only the golden ___ can help Buster.", "type": "single", "options": [{"text": "tomato"}, {"text": "orange"}, {"text": "apple"}], "correct": [2]}, {"q": "Horax and Zelda want to ___ the apple, too.", "type": "single", "options": [{"text": "take"}, {"text": "eat"}, {"text": "cook"}], "correct": [0]}, {"q": "The children write ___ in the book.", "type": "single", "options": [{"text": "an apple"}, {"text": "the letter"}, {"text": "an idea"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "Что ещё мог сказать Бен? Соедини начало и конец предложений", "mode": "drag", "text": "Shall we __call the police__?\nLet’s __take him to the vet__.\nWe can __make some tea for Buster__.\nDo you want __any help__?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'speaking', replace($blk${"title": "Расскажи историю от лица Бена 🎤", "needs_review": true, "html": "<p>Представь, что ты Бен, и расскажи историю от его лица — так, будто она происходит прямо сейчас. Обязательно скажи, что ты чувствуешь и о чём думаешь 😊</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/congrats_popper.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа!</h3><p>Все задания выполнены. Ты большущий молодец 😊</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7);
end
$mig$;
