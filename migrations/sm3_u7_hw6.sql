-- Super Minds 3 · Unit 7 · At the doctor’s · Homework 6
-- собрано tools/sm3_build.py --lesson u7_hw6
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
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>В этом уроке тебя ждут текст и несколько упражнений. В конце есть дополнительное задание — по желанию, НО если сделаешь его, будешь чемпионом английского!</p><p>Для начала прочитай текст ещё раз.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u7/reading_best_friend_1.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u7/reading_best_friend_2.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'sequence', replace($blk${"title": "Прочитай текст ещё раз и расставь предложения в правильном порядке по смыслу", "items": [{"text": "Emma Woodward had a bad headache."}, {"text": "Her parents took her to hospital."}, {"text": "The doctor said, ‘You have to sit in a wheelchair or use crutches.’"}, {"text": "Emma’s mum and dad went to the Helper Dog Project with Emma."}, {"text": "Emma liked the biggest dog, Jasper, a lot."}, {"text": "With Jasper’s help, Emma learnt to walk again."}, {"text": "Jasper got a big prize, The Best Animal of the Year!"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни краткое содержание текста. Осторожно: среди слов есть лишние — help · visit · say · feel · learn", "text": "Emma liked swimming and riding her bike. Emma’s headache got worse and worse and she __felt__ very ill. The doctor __said__ Emma needed an operation. After the operation, Emma couldn’t remember how to do anything. She had to use a wheelchair or crutches. Emma didn’t try to walk because she was very tired. One day Emma and her parents __visited__ the Helper Dog Project. One of the big dogs came to Emma and put his paw on Emma’s leg. His name was Jasper. He and Emma became best friends. Jasper __helped__ Emma and she slowly __learned__ to walk again with no crutches. Last week a magazine gave Jasper a big prize: The Best Animal of the Year! Emma said to Jasper, ‘You are now the most famous dog in the world!’ Jasper put his paw on Emma’s leg. She __remembered__ the first time she saw Jasper and smiled."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "Дополнительное задание: послушай краткий пересказ — в нём четыре ошибки. С первой я тебе помогу, остальные найди сам", "audio": "", "text": "1. stomach-ache instead of a headache.\n2. __smallest__ instead of __biggest__.\n3. __George__ instead of __Jasper__.\n4. __Film__ instead of __Animal__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа!</h3><p>Увидимся на занятии :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6);
end
$mig$;
