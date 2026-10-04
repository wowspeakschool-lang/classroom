-- Super Minds 3 · Unit 6 · Gadgets · Homework 6
-- собрано tools/sm3_build.py --lesson u6_hw6
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
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>Тебя ждут интересные упражнения, а ещё ДОПОЛНИТЕЛЬНОЕ задание — его можно сделать по желанию, НО если сделаешь, будешь нереально крут!</p><p>Начнём с аудирования.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'sort', replace($blk${"title": "Прослушай аудио и укажи, кому какой гаджет принадлежит СЕЙЧАС. Три картинки лишние — отправь их в колонку Extra", "audio": "", "groups": [{"name": "Jenny", "items": [{"image": "@@MEDIA@@sm3/u6/gad_tablet.webp"}]}, {"name": "Tim", "items": [{"image": "@@MEDIA@@sm3/u6/gad_console.webp"}]}, {"name": "Olivia", "items": [{"image": "@@MEDIA@@sm3/u6/gad_phone.webp"}]}, {"name": "Extra", "items": [{"image": "@@MEDIA@@sm3/u6/gad_torch.webp"}, {"image": "@@MEDIA@@sm3/u6/gad_walkie_talkies.webp"}, {"image": "@@MEDIA@@sm3/u6/gad_fan.webp"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Супер! Прочитай текст про игровые приставки и выбери подходящее слово в каждый пропуск. There are many games consoles that we can play with. The (1) ___ games console is more than 40 years old! It’s bigger (2) ___ the ones we have today. It is slower too. Modern consoles are smaller and faster. You can play games on these consoles and (3) ___ DVDs too. Some games consoles also connect to the internet. Games consoles are not very cheap. Today, the (4) ___ expensive games consoles cost around £800 and the cheapest ones cost about £50. Many people like games consoles because the games (5) ___ fun and many people can play together with one console.", "questions": [{"q": "(1)", "type": "single", "options": [{"text": "oldest"}, {"text": "young"}, {"text": "old"}], "correct": [0]}, {"q": "(2)", "type": "single", "options": [{"text": "than"}, {"text": "more"}, {"text": "the"}], "correct": [0]}, {"q": "(3)", "type": "single", "options": [{"text": "watch"}, {"text": "have"}, {"text": "open"}], "correct": [0]}, {"q": "(4)", "type": "single", "options": [{"text": "most"}, {"text": "more"}, {"text": "than"}], "correct": [0]}, {"q": "(5)", "type": "single", "options": [{"text": "are"}, {"text": "do"}, {"text": "is"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/good_luck_clover.webp\" alt=\"\" style=\"height:180px\"></p><h3>А это дополнительное задание — для ЧЕМПИОНОВ!</h3><p>Его можно выполнить по желанию. Ниже картинка, а после неё задание: внимательно посмотри и впиши правильные ответы.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u6/scene_garden_count.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "Посмотри на картинку и закончи предложения", "text": "1. There are __three|3__ balls in the garden.\n2. The red T-shirt is bigger than the blue __T-shirt|t-shirt|tshirt__.\n3. Where is the bicycle? — __Behind the tree|behind the tree__.\n4. What can you see on the table? — __Walkie-talkies|walkie-talkies|two walkie-talkies|2 walkie-talkies__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание — ты замечательный ученик!</h3><p>За это лови звёздочку :) Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6);
end
$mig$;
