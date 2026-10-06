-- Go Getter 1 · Unit 6 · My day · Homework 2
-- собрано tools/gg1_build.py --lesson u6_hw2
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
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Сегодня мы закрепим знания, полученные на уроке, и ты без проблем сможешь использовать время Present Simple.</p><p>В конце тебя будет ждать дополнительное упражнение — для самых смелых и самых сильных учеников 💪</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u6/card_present_simple.webp\" alt=\"Present Simple\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p>Макс и Хэмми рассказывают, как они проводят время перед сном. Посмотри на картинку и попробуй угадать: <b>What movies does Hammy like watching before sleeping?</b> 😴</p><p><img src=\"@@MEDIA@@gg1/u6/hammy_bedtime.webp\" alt=\"Hammy\" style=\"height:240px\"></p><p>Посмотри видео и проверь, угадал ли ты. Повторяй вопросы и ответы за героями, чтобы хорошенько запомнить правила.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'video', replace($blk${"title": "Max and Hammy: before bed", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант. Внимательно смотри на главное слово!", "questions": [{"q": "Jen ___ TV after dinner.", "type": "single", "options": [{"text": "watch"}, {"text": "watches"}], "correct": [1]}, {"q": "Alex ___ his homework in his room.", "type": "single", "options": [{"text": "does"}, {"text": "do"}], "correct": [0]}, {"q": "Lucas and Alex ___ football in the park.", "type": "single", "options": [{"text": "plays"}, {"text": "play"}], "correct": [1]}, {"q": "Jen and Alex ___ late.", "type": "single", "options": [{"text": "get up"}, {"text": "gets up"}], "correct": [0]}, {"q": "Lucas's mum ___ to music in the kitchen.", "type": "single", "options": [{"text": "listen"}, {"text": "listens"}], "correct": [1]}, {"q": "Lucas ___ to school with Jen and Alex.", "type": "single", "options": [{"text": "goes"}, {"text": "go"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши правильную форму глагола. Смотри, как в первой строке — это пример!", "mode": "type", "text": "I / You / We / They — He / She / It\nplay — plays\n__do__ — does\ndraw — __draws__\n__drink__ — drinks\n__look__ — looks\nwash — __washes__\n__carry__ — carries"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши в пропуски слова, раскрыв скобки. Посмотри, как это сделано в первом предложении!", "mode": "type", "text": "0. I usually walk (walk) to school but my friend always rides (ride) his bike.\n1. My brother and I __like__ (like) juice but my sister __drinks__ (drink) milk.\n2. Mum and Dad __watch__ (watch) TV and my sister and I __play__ (play) computer games after dinner.\n3. Rob __tidies__ (tidy) his room and he __helps__ (help) in the kitchen too.\n4. Sue __has__ (have) sandwiches for lunch. She __eats__ (eat) them in the classroom.\n5. I __hang out__ (hang out) with my friends after school. Then I __have__ (have) dinner.\n6. Harry __does__ (do) his homework and then he __watches__ (watch) TV."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'task', replace($blk${"title": "Обо мне и о друге ✍️", "needs_review": true, "html": "<p>Напиши 3 предложения о себе и 3 предложения о своём члене семьи, друге или даже учителе! Чем вы занимаетесь каждый день?</p><p><i>Посмотри, это мои предложения: I get up at 9 o'clock. I watch TV in the evening. I read a book before sleeping. My best friend Anna gets up at 7 o'clock. She plays computer games after school. She has dinner at 8 o'clock in the evening.</i></p><p>Обрати внимание на окончания глаголов, когда я рассказываю о своей подруге 😉</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'quiz', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Выбери правильный вариант ⭐", "questions": [{"q": "My sister ___ to school by bus.", "type": "single", "options": [{"text": "goes"}, {"text": "go"}], "correct": [0]}, {"q": "We ___ breakfast at 8 o'clock.", "type": "single", "options": [{"text": "has"}, {"text": "have"}], "correct": [1]}, {"q": "Tom ___ TV in the evening.", "type": "single", "options": [{"text": "watches"}, {"text": "watch"}], "correct": [0]}, {"q": "I ___ my room on Saturdays.", "type": "single", "options": [{"text": "tidies"}, {"text": "tidy"}], "correct": [1]}, {"q": "Anna ___ English and Maths.", "type": "single", "options": [{"text": "studies"}, {"text": "studys"}], "correct": [0]}, {"q": "They ___ to music after school.", "type": "single", "options": [{"text": "listens"}, {"text": "listen"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски ⭐", "mode": "drag", "text": "My dad __gets__ up at 7 o'clock.\nHe __has__ a shower and __makes__ breakfast.\nMy brother __goes__ to school with me.\nAfter school he __does__ his homework.\nIn the evening my mum __watches__ TV."}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
