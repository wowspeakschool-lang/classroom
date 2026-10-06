-- Go Getter 1 · Unit 5 · I can do it · Homework 2
-- собрано tools/gg1_build.py --lesson u5_hw2
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 5 · I can do it', 5
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 5 · I can do it');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 5 · I can do it';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>На уроке мы с тобой познакомились с новым глаголом <b>CAN</b>. Сегодня будем выполнять разные задания, чтобы попрактиковаться в этой теме.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u5/card_can.webp\" alt=\"can / can't\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'video', replace($blk${"title": "Посмотри видео", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Посмотри на картинку и подумай, что ребята умеют и не умеют делать. Впиши в пропуски can или can't", "mode": "drag", "image": "@@MEDIA@@gg1/u5/oliver_sarah.webp", "text": "1. Sarah __can't__ dance.\n2. Oliver __can__ play video games.\n3. Oliver __can't__ play basketball.\n4. Oliver __can__ climb.\n5. Sarah __can't__ paint.\n6. Sarah __can__ swim.\n7. Sarah __can__ play tennis.\n8. Sarah __can't__ ride a bike.\n9. Sarah __can__ write.\n10. Oliver __can't__ sing."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Вспомним животных и подумаем, что мы умеем делать как они. Заполни пропуски", "mode": "drag", "text": "1. You can't __jump__ like a monkey.\n2. She can't __fly__ like a butterfly.\n3. My dad can't __run__ like a cheetah.\n4. My mom can __stomp__ like an elephant.\n5. My sister can __swim__ like a fish."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "А теперь подумаем, что животные умеют и не умеют делать. Заполни пропуски словами can или can't", "mode": "drag", "text": "1. A monkey __can't__ fly, but it __can__ climb a tree.\n2. A bird __can__ fly, but it __can't__ play volleyball.\n3. An elephant __can__ run, but it __can't__ sing a song.\n4. A kangaroo __can__ jump, but it __can't__ play the guitar.\n5. A frog __can't__ speak English, but it __can__ jump.\n6. A mouse __can__ run fast, but it __can't__ ride a bike.\n7. A spider __can't__ fly a plane, but it __can__ make a web.\n8. A rabbit __can't__ write an e-mail, but it __can__ eat carrots.\n9. A bee __can't__ swim, but it __can__ make honey."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'task', replace($blk${"title": "Что я умею 📝", "needs_review": true, "html": "<p>Напиши несколько предложений о том, что ты уже умеешь делать.</p><p><i>Пример: I can swim. I can ride a bike. I can't play the piano.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'quiz', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Посмотри на картинку с Оливером и Сарой. Верно или неверно? ⭐", "questions": [{"q": "Oliver can play the drums.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0], "image": "@@MEDIA@@gg1/u5/oliver_sarah.webp"}, {"q": "Oliver can skateboard.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [1]}, {"q": "Oliver can rollerblade.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0]}, {"q": "Sarah can sing.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0]}, {"q": "Sarah can ride a bike.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [1]}, {"q": "Oliver can play video games.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'sort', replace($blk${"title": "Расставь занятия к подходящим глаголам ⭐", "groups": [{"name": "make", "items": [{"text": "a poster"}, {"text": "cupcakes"}, {"text": "a cake"}]}, {"name": "play", "items": [{"text": "football"}, {"text": "computer games"}, {"text": "the piano"}, {"text": "tennis"}]}, {"name": "ride", "items": [{"text": "a bike"}, {"text": "a horse"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_jump.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа! 🎉</h3><p>See you soon!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9);
end
$mig$;
