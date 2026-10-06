-- Go Getter 1 · Unit 6 · My day · Homework 5
-- собрано tools/gg1_build.py --lesson u6_hw5
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 6 · My day', 6
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 6 · My day');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 6 · My day';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Как ты помнишь, на уроке мы читали текст и выполняли упражнения по нему. Сегодня ты тоже будешь читать текст и выполнять задания, но уже самостоятельно!</p><p>В конце тебя будет ждать дополнительное упражнение — для самых смелых и самых сильных учеников 💪</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u6/card_months.webp\" alt=\"Months of the year\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p><b>Внимательно прочитай текст, после тебя ждут упражнения.</b></p><p><img src=\"@@MEDIA@@gg1/u6/mike.webp\" alt=\"Mike\" style=\"height:200px\"></p><p><i>Hi. I'm Mike. I'm ten and I'm American. I live in New York. My school is very big. I like sport. I'm not very good at Art but I love it. I have lunch in the classroom. I usually have pizza! After school I always hang out with my friends. We sometimes play basketball or we go to the park.</i></p><p><img src=\"@@MEDIA@@gg1/u6/dasha.webp\" alt=\"Dasha\" style=\"height:200px\"></p><p><i>My name is Dasha and I'm nine. I go to a special school. It's a ballet school! After breakfast we have lessons. My favourite lessons are Maths and English. Then we have lunch. I often have pancakes! After lunch we always dance. I'm always busy.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'sort', replace($blk${"title": "Распредели картинки: что про Майка, а что про Дашу?", "groups": [{"name": "Mike", "items": [{"image": "@@MEDIA@@gg1/u6/md_pizza.webp"}, {"image": "@@MEDIA@@gg1/u6/md_basketball.webp"}, {"image": "@@MEDIA@@gg1/u6/md_new_york.webp"}]}, {"name": "Dasha", "items": [{"image": "@@MEDIA@@gg1/u6/md_ballet.webp"}, {"image": "@@MEDIA@@gg1/u6/md_pancakes.webp"}, {"image": "@@MEDIA@@gg1/u6/md_maths.webp"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'truefalse', replace($blk${"title": "Прочитай текст ещё раз: правда это (true) или ложь (false)? Находи доказательства в тексте", "statements": [{"text": "Mike likes Art.", "correct": true}, {"text": "He eats pizza in the classroom.", "correct": true}, {"text": "He never goes to the park after school.", "correct": false}, {"text": "Dasha likes Maths.", "correct": true}, {"text": "She has pancakes every day.", "correct": false}, {"text": "She has lessons after lunch.", "correct": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "Прочитай текст ещё раз и впиши в предложения 1–2 слова по смыслу", "mode": "type", "text": "1. Mike goes to a __big|very big__ school.\n2. He plays basketball with his __friends__.\n3. Dasha has __lessons__ after breakfast.\n4. Dasha is always __busy__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'sequence', replace($blk${"title": "Дополнительное задание ⭐ Давай вспомним все месяцы! Расставь их в правильном порядке, начиная с January", "image": "@@MEDIA@@gg1/u6/seasons.webp", "items": [{"text": "January"}, {"text": "February"}, {"text": "March"}, {"text": "April"}, {"text": "May"}, {"text": "June"}, {"text": "July"}, {"text": "August"}, {"text": "September"}, {"text": "October"}, {"text": "November"}, {"text": "December"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'speaking', replace($blk${"title": "Мой год 🎤", "html": "<p>Нажми на микрофон и расскажи, что ты делаешь в разные месяцы года.</p><p><i>Пример: In January I go skiing. In March it's my birthday. In July I'm on holiday with my family. In September I go to school again.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_jump.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
