-- Go Getter 1 · Unit 4 · Look at me · Homework 4
-- собрано tools/gg1_build.py --lesson u4_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 4 · Look at me', 4
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 4 · Look at me');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 4 · Look at me';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Welcome back! 👋</h2><p>Добро пожаловать на страничку домашнего задания! Будем проверять твои силы и знания, полученные на уроке! Do your best! (Постарайся!)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u4/card_sorry.webp\" alt=\"Sorry about that!\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'sequence', replace($blk${"title": "Мы должны быть вежливыми! Фразы с урока нам в этом помогут. Расставь предложения в диалоге по порядку", "image": "@@MEDIA@@gg1/u4/broken_cup.webp", "items": [{"text": "Oh no, my favourite cup is broken!"}, {"text": "I'm so sorry."}, {"text": "That's all right. I have a new one."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'sequence', replace($blk${"title": "Расставь предложения в диалоге по порядку", "image": "@@MEDIA@@gg1/u4/scene_alarm_clock.webp", "items": [{"text": "Jane! It's 9:30! You're late again!"}, {"text": "Sorry about that."}, {"text": "It's OK, be careful next time!"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'sequence', replace($blk${"title": "Расставь предложения в диалоге по порядку", "image": "@@MEDIA@@gg1/u4/kids_hurt.webp", "items": [{"text": "Are you OK? I hurt you…"}, {"text": "It's OK."}, {"text": "Are you sure?"}, {"text": "I'm fine."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный ответ", "questions": [{"q": "A: I'm sorry. B: ___", "type": "single", "options": [{"text": "Are you OK?"}, {"text": "I'm fine."}, {"text": "That's all right."}], "correct": [2]}, {"q": "A: I'm so sorry. B: ___", "type": "single", "options": [{"text": "That's all right."}, {"text": "Sorry, my mistake."}, {"text": "Are you OK?"}], "correct": [0]}, {"q": "A: Are you OK? B: ___", "type": "single", "options": [{"text": "That's all right."}, {"text": "Yes, I'm fine."}, {"text": "No problem."}], "correct": [1]}, {"q": "A: Sorry about that! B: ___", "type": "single", "options": [{"text": "I'm OK."}, {"text": "I'm fine."}, {"text": "No problem!"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'gaps', replace($blk${"title": "Вставь в пропуски слова, чтобы получились диалоги", "mode": "drag", "image": "@@MEDIA@@gg1/u4/sorry_boy.webp", "text": "1. A: I can't find my phone! B: I've got it! __Sorry__ about that! A: That's __all right__.\n2. A: Ohhh! I'm so __sorry__! B: It's OK! A: Are you __sure__? B: Yes, I'm __fine__!\n3. A: These aren't my keys. B: Sorry, my __mistake__. Here you are. A: No __problem__!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'video', replace($blk${"title": "Посмотри видео про Генри и Эмму и ответь: верно или неверно", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'truefalse', replace($blk${"title": "Верно или неверно? (по видео)", "statements": [{"text": "Henry hurts his cat.", "correct": false}, {"text": "Emma opens Henry's parcel.", "correct": true}, {"text": "Mother spills orange juice.", "correct": false}, {"text": "Henry drives his toy car into Emma's toys.", "correct": true}, {"text": "Henry eats his sweet.", "correct": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'speaking', replace($blk${"title": "Что ты скажешь? 🎤", "html": "<p>Представь, что бы ты сказал в этих случаях. Нажми на микрофон и ответь:</p><ol><li>You break your mum's cup.</li><li>You forget to call your friend back.</li><li>You are late for school.</li><li>You don't buy a present for your friend.</li></ol>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_jump.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! У тебя всё получилось! 🎉</h3><p>Great job! Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
