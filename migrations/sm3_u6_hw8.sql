-- Super Minds 3 · Unit 6 · Gadgets · Homework 8
-- собрано tools/sm3_build.py --lesson u6_hw8
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 6 · Gadgets', 6
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 6 · Gadgets');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 6 · Gadgets';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 8', 'homework',
         60, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 8');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 8';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет-привет!</h2><p>Самое время повторить всё-всё, что ты узнал в этом юните. Ты наверняка помнишь то, что выучил. Давай начинать!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'sequence', replace($blk${"title": "Послушай разговор продавца и покупателя, а затем расставь предложения диалога в правильном порядке", "audio": "", "items": [{"text": "A: Good morning. Can I help you?"}, {"text": "B: Yes. Have you got any torches?"}, {"text": "A: Yes, we have. We’ve got this blue torch and this green one."}, {"text": "B: How much is the green one?"}, {"text": "A: It’s 14 pounds. The blue one is cheaper. It’s only eight pounds."}, {"text": "B: That’s great. Can I buy the blue one, please?"}, {"text": "A: Of course!"}, {"text": "B: Thank you."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'task', replace($blk${"title": "Напиши свой диалог", "needs_review": true, "image": "@@MEDIA@@sm3/u6/scene_tablet_shop.webp", "html": "<p>Ты лучше всех! Просмотри диалог из предыдущего задания ещё раз и напиши свой, но по картинке — посмотри, девочка покупает планшет.</p><p>Я помогу тебе с началом:</p><p><i>Assistant: Good morning. Can I help you?</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'task', replace($blk${"title": "Дополнительное задание — для мастеров английского языка", "needs_review": true, "html": "<p>Напиши небольшой рассказ о своём любимом гаджете и сравни его со своим старым гаджетом. Если нарисуешь картинку — будет просто супер!</p><p>Ниже образец такого рассказа. Успехов!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<h3>Образец рассказа</h3><p><i>My favourite gadget is my bike.</i></p><p><i>It was my birthday present from my parents. My old bike was very small. This bike is bigger.</i></p><p><i>It’s red and black. It’s the most beautiful bike in the world.</i></p><p><i>I love my bike. I cycle to lots of places on it. I sometimes ride my bike to visit my grandmother at the weekend.</i></p><p>Writing tip: прочитай написанное медленно и проверь, нет ли ошибок.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/congrats_popper.webp\" alt=\"\" style=\"height:180px\"></p><h3>Великолепная работа!</h3><p>Поздравляю тебя с окончанием большой-пребольшой темы. Ты узнал много нового о технологиях и научился сравнивать предметы. Твой учитель очень гордится тобой! Увидимся на занятии :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5);
end
$mig$;
