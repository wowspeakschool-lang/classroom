-- Super Minds 3 · Unit 7 · At the doctor’s · Homework 2
-- собрано tools/sm3_build.py --lesson u7_hw2
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 7 · At the doctor’s', 7
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 7 · At the doctor’s');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 7 · At the doctor’s';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>Выполни все задания, если хочешь выучить тему на все 100! В конце есть дополнительное задание — по желанию, но если сделаешь его, будешь нереально крут.</p><p>Для начала посмотри видео. Как думаешь, кем были родители Хэмми? Посмотри и проверь себя!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Видео: прошедшее время, родители Хэмми", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри видео ещё раз и выбери правильный вариант", "questions": [{"q": "My mum ___ the drums.", "type": "single", "options": [{"text": "played"}, {"text": "play"}, {"text": "plaid"}], "correct": [0]}, {"q": "My dad ___.", "type": "single", "options": [{"text": "danced"}, {"text": "dance"}, {"text": "dancd"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Замечательно! А теперь расставь слова в пропуски по смыслу", "mode": "drag", "text": "Yesterday my friend and I __were__ in the park. Suddenly there was this big, black dog. Jonathan __looked__ at its eyes. ‘Go away!’ he __shouted__.\nOn Sunday, Sue __visited__ her grandma. Grandma __was__ very happy with the flowers and the cake. She __smiled__ a lot. Sue and her grandma __listened__ to a piano concert together."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'task', replace($blk${"title": "Дополнительное задание — для самых больших умников", "needs_review": true, "image": "@@MEDIA@@sm3/u7/scene_football_fans.webp", "html": "<p>Напиши предложения о картинке, используя эти слова: <b>watch · shout · jump · be</b>.</p><p>Начни так: <i>On Sunday I watched a football game.</i></p><p>Не забудь: эти действия уже прошли, писать нужно в прошедшем времени!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание — ты МЕГА КРУТ!</h3><p>Жду тебя на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5);
end
$mig$;
