-- Go Getter 1 · Unit 2 · My things · Homework 5
-- собрано tools/gg1_build.py --lesson u2_hw5
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 2 · My things', 2
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 2 · My things');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 2 · My things';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>На занятии ты нарисовал свой суперрюкзак. Расскажешь мне про него? Но сначала давай вспомним некоторые слова и соединим половинки друг с другом.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'match', replace($blk${"title": "Соедини половинки слов", "pairs": [{"left": "back", "right": "pack"}, {"left": "games", "right": "console"}, {"left": "mobile", "right": "phone"}, {"left": "mountain", "right": "bike"}, {"left": "laptop", "right": "computer"}, {"left": "skate", "right": "board"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p><b>Прочитай статью про суперрюкзак Джейми.</b></p><p><img src=\"@@MEDIA@@gg1/u2/jamie_super_backpack.webp\" alt=\"Jamie\" style=\"height:240px\"></p><p><i>Jamie Cooper's 13. He's from Liverpool in the UK. Jamie's super backpack is our gadget of the week. Why? Read on.</i></p><p><img src=\"@@MEDIA@@gg1/u2/super_backpack.webp\" alt=\"Super backpack\" style=\"height:220px\"></p><p><i>What's in the picture? Yes, that's right. It's a red backpack. It's a super backpack! It's very, very cool. Look again. This super backpack is also a mountain bike. It's small but it isn't too small. It's fantastic! And that's not all. Think about it. You're in the park with your friends. You're cold and your jumper is at home. No problem. This super backpack is a big jacket too. What about your other things? Don't worry! Super backpack is just the right size for your laptop computer, your mobile phone, your new games and other favourites. There's even a pocket for a small pet like my cat Fiona. How cool is that?</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'task', replace($blk${"title": "Мой суперрюкзак 🎒", "needs_review": true, "html": "<p>Теперь пришло время рассказать про суперрюкзак, который ты нарисовал! А если ты ещё и прикрепишь фотографию своего рисунка, будет вообще здорово!</p><p><i>Пример: My super backpack is blue. It's big but it isn't too big. It's a skateboard too! There's a pocket for my mobile phone.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ух ты! Вот это рюкзак! 🎉</h3><p>Он и правда СУПЕРрюкзак! До встречи на занятии! Bye!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4);
end
$mig$;
