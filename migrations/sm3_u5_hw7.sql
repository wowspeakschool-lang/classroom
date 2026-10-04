-- Super Minds 3 · Unit 5 · Under the sea · Homework 7
-- собрано tools/sm3_build.py --lesson u5_hw7
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
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! Как твои дела?</h2><p>Самое время начинать домашнюю работу!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'task', replace($blk${"title": "Посмотри на картинки и закончи предложения", "needs_review": true, "image": "@@MEDIA@@sm3/u5/eco_six_pictures.webp", "html": "<p><i>Pictures …, … and … make me feel happy because …<br>Pictures …, … and … make me feel angry because …</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'gaps', replace($blk${"title": "Посмотри на картинки и заполни пропуски: is / isn’t, aren’t, was / were", "image": "@@MEDIA@@sm3/u5/beach_then_now.webp", "text": "In 1990 …\n1. The beach __was__ clean.\n2. People __were__ in the sea.\n3. There __were__ fish and dolphins in the sea too.\n4. Paul __was__ happy.\nToday …\n5. The beach __isn’t__ clean.\n6. There __is__ rubbish on the beach.\n7. There __aren’t__ any fish in the sea.\n8. Paul __isn’t__ happy."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'sort', replace($blk${"title": "Вставь слова в подходящую колонку", "groups": [{"name": "Climate change", "items": [{"text": "world getting hotter"}, {"text": "floods"}, {"text": "poles melting"}]}, {"name": "Pollution", "items": [{"text": "plastic bags"}, {"text": "sea creatures eat plastic"}, {"text": "big boats"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант", "questions": [{"q": "1. Sea plants give us ___.", "type": "single", "options": [{"text": "oxygen"}, {"text": "pollution"}], "correct": [0]}, {"q": "2. Cities by the sea are in danger because there is ___ water in the sea.", "type": "single", "options": [{"text": "more"}, {"text": "less"}], "correct": [0]}, {"q": "3. ___ water is bad for corals.", "type": "single", "options": [{"text": "Hot"}, {"text": "Cold"}], "correct": [0]}, {"q": "4. Fish are losing their homes because coral ___.", "type": "single", "options": [{"text": "is turning white"}, {"text": "has beautiful colours"}], "correct": [0]}, {"q": "5. Sea creatures die because ___ eat plastic.", "type": "single", "options": [{"text": "they"}, {"text": "we"}], "correct": [0]}, {"q": "6. Big boats are ___ for our seas.", "type": "single", "options": [{"text": "bad"}, {"text": "good"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/congrats_popper.webp\" alt=\"\" style=\"height:180px\"></p><h3>Всё просто отлично! Ты большой молодец!</h3><p>Спасибо тебе :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5);
end
$mig$;
