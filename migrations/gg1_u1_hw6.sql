-- Go Getter 1 · Unit 1 · Family and friends · Homework 6
-- собрано tools/gg1_build.py --lesson u1_hw6
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 1 · Family and friends', 1
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 1 · Family and friends');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 1 · Family and friends';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>На занятии мы сделали много интересных заданий! Повторим?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>Послушай аудио: Роб рассказывает о своём друге Викторе и кузине Мел. Потом выполни задания ниже.</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Послушай аудио и скажи: верно или неверно", "questions": [{"q": "Rob and Victor are best friends.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0], "image": "@@MEDIA@@gg1/u1/rob_victor_console.webp"}, {"q": "They're at Rob's house.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [1]}, {"q": "Rob's mum and Victor's mum are best friends.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0]}, {"q": "Rob's on holiday.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0], "image": "@@MEDIA@@gg1/u1/rob_mel_holiday.webp"}, {"q": "Rob and Mel are in the UK.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [1]}, {"q": "Rob and Mel are cousins.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Послушай аудио и впиши информацию в пропуски", "mode": "type", "text": "Rob — Age: 10 — Nationality: __British__\nVictor — Age: __10|ten__ — Nationality: __French__\nMel — Age: __12|twelve__ — Nationality: __American__"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'task', replace($blk${"title": "Я и мой лучший друг ✍", "needs_review": true, "html": "<p>Напиши короткий рассказ о себе и своём лучшем друге (40–60 слов). Расскажи об имени, возрасте, откуда вы, и о семье.</p><p><i>Пример: Hi! My name's Anna. I'm ten years old. I'm from Poland. I'm Polish. My best friend is Tom. He's eleven. He's British. We're classmates. My mum's name is Maria and my dad's name is Peter. Tom's sister is Lucy. We love our families!</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Так держать! 🎉</h3><p>Увидимся на занятии! Bye!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5);
end
$mig$;
