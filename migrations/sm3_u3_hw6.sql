-- Super Minds 3 · Unit 3 · At home · Homework 6
-- собрано tools/sm3_build.py --lesson u3_hw6
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 3 · At home', 3
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 3 · At home');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 3 · At home';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>ПРИВЕТ-ПРИВЕТ!</h2><p>Сегодня мы с тобой будем читать сказку. Ты любишь сказки?</p><p>Как думаешь, кто главный герой истории? Прочитай текст ниже и ответь на вопрос :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u3/story_shoemaker_1.webp\" alt=\"The shoemaker and the elves\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u3/story_shoemaker_2.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'truefalse', replace($blk${"title": "Прочитай предложения и скажи, это правда (True) или неправда (False)", "statements": [{"text": "The shoemaker works a lot of hours.", "correct": true}, {"text": "The shoemaker works hard but has little money.", "correct": true}, {"text": "Every morning he finds new shoes on the table.", "correct": true}, {"text": "The elves work after 5 o’clock in the morning.", "correct": false}, {"text": "The shoemaker makes nice clothes for the elves to thank them.", "correct": true}, {"text": "The elves still make shoes for the shoemaker.", "correct": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Расставь слова на свои места ⬇", "mode": "drag", "text": "There is a __shoemaker__ who works very hard. One night, he cuts some __leather__ and leaves it on the kitchen table. In the morning, there are ten pairs of beautiful shoes. The __next__ morning there are twenty pairs of beautiful shoes. Every night, he leaves leather on the table and __every__ morning there are beautiful new shoes. Soon, everyone in the town wants more shoes from the shoemaker. But the shoemaker __doesn’t__ know who makes the shoes. One night he hides under a table and sees five elves making shoes. They are wearing __old__ clothes. The shoemaker makes nice clothes for the elves. The elves take the clothes but they don’t come back to make new shoes. The shoemaker doesn’t mind because he wants the elves to be __happy__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Молодец! Ты отлично справляешься!</h3><p>Осталось последнее задание. Оно дополнительное, но если ты его сделаешь, получишь ⭐</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'task', replace($blk${"title": "Кто твой любимый сказочный герой?", "needs_review": true, "html": "<p>Напиши его имя.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'task', replace($blk${"title": "Опиши день своего героя", "needs_review": true, "html": "<p>Используй выражения из текста сказки.</p><p><i>Например: William wakes up at 8 o’clock and brushes his teeth. He has breakfast at 9 o’clock…</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>SUPER! Ты выполнил все задания!</h3><p>Ты БОЛЬШОЙ МОЛОДЕЦ! Увидимся на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
