-- Super Minds 3 · Unit 9 · Weather · Homework 5
-- собрано tools/sm3_build.py --lesson u9_hw5
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 9 · Weather', 9
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 9 · Weather');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 9 · Weather';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! Welcome to your homework!</h2><p>Прочитай текст, который мы разбирали на уроке, и выполни два упражнения к нему.</p><p>В конце домашнего задания есть дополнительное задание — для чемпионов! Его можно сделать по желанию, но те, кто сделают его добросовестно, получат дополнительный балл!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Прежде чем читать, попробуй вспомнить: What colour is the statue? Прочитай текст и проверь себя!", "type": "single", "options": [{"text": "silver"}, {"text": "red"}, {"text": "golden"}, {"text": "white"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u9/story_castle_1.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u9/story_castle_2.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Замечательно, ты отлично справляешься! Это краткий пересказ истории, но в нём пропущены слова — постарайся вставить их по смыслу", "mode": "drag", "text": "Ben and Lucy go to the castle. They see Horax and Zelda near a door. The door has a __message__ with a missing word above it. Horax and Zelda need the letters. They __hear__ Ben and they get the children. Ben gives Zelda the letters. Buster pulls off Horax’s __glasses__. Horax is Mr Williams, the librarian! Horax makes the word ‘__finders__’ and Zelda writes it above the door. Horax and Zelda try to go in, but they can’t. Ben and Lucy make the word ‘__friends__’. They go in and find the __treasure__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'task', replace($blk${"title": "Дополнительное задание для настоящих чемпионов!", "needs_review": true, "html": "<p><img src=\"@@MEDIA@@sm3/u9/task_treasure.webp\" alt=\"\" style=\"max-width:100%\"></p><p>Разгадай текст с помощью шифра — на уроке мы будем обсуждать, что там спрятано!</p><p>Можешь записать свой ответ здесь или в тетради — как тебе больше нравится!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u9/cipher_alphabet.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u9/cipher_text.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание, ты замечательный ученик!</h3><p>За это лови звёздочку :)</p><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
