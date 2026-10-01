-- Super Minds 3 · Unit 1 · School · Homework 3
-- собрано tools/sm3_build.py --lesson u1_hw3
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 1 · School', 1
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 1 · School');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 1 · School';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! Давай приступим к домашнему заданию :)</h2><p>Сегодня ты сам будешь писать предложения — по тому, что говорят ребята.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'task', replace($blk${"title": "Look, read and write sentences · Tim", "needs_review": true, "html": "<p>Тим рассказывает о школе. Смайлик показывает, как он к этому относится: 😁 — <i>like</i>, 😖 — <i>don’t like</i>, 😁😁 — <i>love</i>. Запиши полные предложения.</p><ol><li>😁 Speaking English. Good at it. — <i>образец: I like speaking English. I’m good at it.</i></li><li>😖 History. Not my favourite subject.</li><li>😁😁 Listening to music.</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'task', replace($blk${"title": "Look, read and write sentences · Anna", "needs_review": true, "html": "<p>Теперь Анна. Продолжай нумерацию — 4, 5, 6.</p><ol start=\"4\"><li>😖 Learning Maths.</li><li>😁 Geography. Very good at it.</li><li>😁😁 Studying History. Love my teacher too.</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'task', replace($blk${"title": "Look and write sentences", "needs_review": true, "html": "<p>Галочка ✔ — нравится, крестик ✖ — не нравится. Напиши про каждого предложение.</p><ol><li>Jim · playing football · ✖ — <i>образец: Jim doesn’t like playing football.</i></li><li>Claire · singing · ✖</li><li>Mary · playing the piano · ✔</li><li>Sam · reading · ✔</li><li>Lisa · watching TV · ✖</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Good job! Thank you!</h3><p>Учитель проверит твои предложения и напишет, что получилось лучше всего.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4);
end
$mig$;
