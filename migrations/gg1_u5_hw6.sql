-- Go Getter 1 · Unit 5 · I can do it · Homework 6
-- собрано tools/gg1_build.py --lesson u5_hw6
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
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Самое время выполнять домашнюю работу!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'exact_input', replace($blk${"title": "Что это? Поставь буквы в правильном порядке", "items": [{"prompt": "Подставь буквы по номерам: 4 1 9 2 5 / 8 7 3 6", "accept": ["teddy bear", "Teddy bear", "Teddy Bear", "teddy-bear", "teddybear"], "image": "@@MEDIA@@gg1/u5/teddy_code.webp", "audio_tts": "teddy bear"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>Послушай рассказ о кружке и выполни задания ниже.</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Послушай и выбери правильный вариант ответа", "questions": [{"q": "At this club you can ___.", "type": "single", "options": [{"text": "make a new teddy bear"}, {"text": "fix an old teddy bear"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Послушай и выбери правильного мишку", "questions": [{"q": "Which teddy bear is it?", "type": "single", "options": [{"image": "@@MEDIA@@gg1/u5/teddy_black_eyes.webp"}, {"image": "@@MEDIA@@gg1/u5/teddy_torn.webp"}, {"image": "@@MEDIA@@gg1/u5/teddy_blue_eyes.webp"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ответа", "questions": [{"q": "What is the girl's name? Her name is ___.", "type": "single", "options": [{"text": "Sarah"}, {"text": "Erin"}], "correct": [0]}, {"q": "Is the teddy bear Tommy's or his sister's? It's ___.", "type": "single", "options": [{"text": "Tommy's"}, {"text": "his sister's"}], "correct": [1]}, {"q": "Can Sarah fix it?", "type": "single", "options": [{"text": "Yes, she can."}, {"text": "No, she can't."}], "correct": [0]}, {"q": "What colour are the new eyes?", "type": "single", "options": [{"text": "They're black."}, {"text": "They're blue."}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'task', replace($blk${"title": "Объявление о школьном кружке 📝", "needs_review": true, "html": "<p>Напиши короткое объявление о школьном кружке (40–60 слов). Расскажи, чем там занимаются, когда встречаются и кто может прийти.</p><p><i>Пример: Come to the Football Club! You can play football and have fun with friends. We meet on Mondays and Wednesdays at 4 o'clock. You can be a boy or a girl, but you must be 8–12 years old. We can run, jump and play together. See you there!</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/congrats_popper.webp\" alt=\"\" style=\"height:180px\"></p><h3>Огромное спасибо тебе за работу! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7);
end
$mig$;
