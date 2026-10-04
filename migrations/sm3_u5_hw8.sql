-- Super Minds 3 · Unit 5 · Under the sea · Homework 8
-- собрано tools/sm3_build.py --lesson u5_hw8
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 5 · Under the sea', 5
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 5 · Under the sea');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 5 · Under the sea';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 8', 'homework',
         60, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 8');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 8';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<h2>Привет! Сегодня читаем про морских животных</h2><p>Посмотри на картинку: кого ты узнаёшь?</p><p><img src=\"@@MEDIA@@sm3/u5/scene_sea_playground.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<h3>Read the text:</h3><p><img src=\"@@MEDIA@@sm3/u5/reading_megalodon.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери подходящий вариант", "questions": [{"q": "Extinct animals are ones that ___ now.", "type": "single", "options": [{"text": "do not live"}, {"text": "live"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери подходящий вариант", "questions": [{"q": "Megalodons were ___.", "type": "single", "options": [{"text": "sharks"}, {"text": "dolphins"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери подходящий вариант", "questions": [{"q": "Megalodons were very ___.", "type": "single", "options": [{"text": "big"}, {"text": "small"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери подходящий вариант", "questions": [{"q": "Megalodons were ___.", "type": "single", "options": [{"text": "fast"}, {"text": "slow"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери подходящий вариант", "questions": [{"q": "Megalodons were in ___.", "type": "single", "options": [{"text": "many different places"}, {"text": "only one place"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'task', replace($blk${"title": "Составь предложения по таблице", "needs_review": true, "html": "<p>Выбери по одному слову из каждого столбика и запиши получившиеся предложения.</p><p><i>1. There — was / were / weren’t — many seahorses / many octopuses / many starfish — at / in / on — the sea. / the garden. / the bath.<br>2. The — owl / puffin / lion — was / were / wasn’t — in / next to / opposite — the school. / a net. / the beach.<br>3. Where — was — it — at — four o’clock?</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<h3>А вот как можно рассказать о морском животном</h3><p><img src=\"@@MEDIA@@sm3/u5/project_turtles.webp\" alt=\"\" style=\"max-width:100%\"></p><p>Пригодится на уроке :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_jump.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа!</h3><p>Увидимся на занятии.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9);
end
$mig$;
