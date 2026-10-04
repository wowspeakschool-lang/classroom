-- Super Minds 3 · Unit 8 · Countries · Homework 6
-- собрано tools/sm3_build.py --lesson u8_hw6
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 8 · Countries', 8
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 8 · Countries');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 8 · Countries';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет!</h2><p>В этом задании тебя ждут текст и аудирование, а ещё дополнительное задание — для чемпионов английского!</p><p>Прочитай текст и ответь на вопрос: <b>Why did Max get sick?</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u8/reading_max_chile.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'gaps', replace($blk${"title": "Прочитай текст ещё раз и заполни пропуски — в каждом 1, 2 или 3 слова", "text": "1. The family went on holiday to Chile.\n2. They __visited some|visited__ big rocks that looked like people.\n3. Max wanted to go swimming because it __was__ very hot.\n4. Max ran to the beach but he __didn’t read|did not read__ the sign.\n5. There __was__ some rubbish on the beach.\n6. Max __didn’t have|did not have__ anything to eat at the restaurant.\n7. Max was __sick__ for three days.\n8. Max said not reading the sign was __very silly|silly__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"html": "<h3>А это Дэвид отправился в путешествие на машине времени</h3><p><img src=\"@@MEDIA@@sm3/u8/story_david_time_machine.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Задание на аудирование: Лили побывала в Африке. Послушай её рассказ и заполни таблицу — в каждом пропуске одно слово", "audio": "", "text": "Lily went to: South Africa\n1. She showed the people she was: __hungry__\n2. Food she ate: __fish__\n3. The beach was very: __clean__\n4. She stayed for one or two: __hours__"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'task', replace($blk${"title": "Дополнительное задание — напиши рассказ о путешествии Дэвида", "needs_review": true, "html": "<p>Посмотри на картинку выше: Дэвид отправился в путешествие на машине времени. Напиши небольшой рассказ о его приключениях в прошедшем времени.</p><p>Начни так: <i>David visited Greenland in the time machine…</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание и готов к уроку.</h3><p>Ты — СУПЕР КРУТ! Жду тебя на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6);
end
$mig$;
