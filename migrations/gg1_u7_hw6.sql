-- Go Getter 1 · Unit 7 · Animals · Homework 6
-- собрано tools/gg1_build.py --lesson u7_hw6
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 7 · Animals', 7
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 7 · Animals');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 7 · Animals';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>Готов к домашней работе? Тогда вперёд!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>Послушай аудио: Эмма рассказывает о своих домашних питомцах.</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'task', replace($blk${"title": "Какое домашнее животное есть у Эммы?", "needs_review": true, "html": "<p>Послушай аудио выше и напиши, какое домашнее животное есть у Эммы.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'task', replace($blk${"title": "Послушай ещё раз и ответь на вопросы", "needs_review": true, "html": "<ol><li>Where are the pets?</li><li>Are they brothers or sisters?</li><li>What colour is Ted's favourite pet?</li><li>What do they need every day?</li><li>Where does their special food come from?</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "А теперь выбери правильный вариант ответа", "questions": [{"q": "There are ___ pets.", "type": "single", "options": [{"text": "three"}, {"text": "two"}], "correct": [1]}, {"q": "The pets ___ easy to look after.", "type": "single", "options": [{"text": "aren't"}, {"text": "are"}], "correct": [0]}, {"q": "They ___ oranges.", "type": "single", "options": [{"text": "like"}, {"text": "don't like"}], "correct": [1]}, {"q": "Ted has got some ___.", "type": "single", "options": [{"text": "rabbits"}, {"text": "hamsters"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><b>Прочитай письмо и выбери верные ответы.</b></p><p><img src=\"@@MEDIA@@gg1/u7/kittens_basket.webp\" alt=\"Kittens\" style=\"height:220px\"></p><p><i>Hi Sam,<br>I know you like cats. Well, our cat has got some kittens. Would you like one? They are cute. Three are black, two are black and white and one is grey. They haven't got names. They are very young!<br>Kittens are easy to look after. They don't go for walks! They sleep a lot and they don't eat much. They're very friendly too.<br>Can you ask your mum and dad? Let me know.<br>Ben</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай письмо и выбери верные ответы", "questions": [{"q": "Does Sam like cats?", "type": "single", "options": [{"text": "Yes, he does."}, {"text": "No, he doesn't."}], "correct": [0]}, {"q": "How many kittens are there?", "type": "single", "options": [{"text": "There are three."}, {"text": "There are six."}], "correct": [1]}, {"q": "Have they got names?", "type": "single", "options": [{"text": "No, they haven't."}, {"text": "Yes, they have."}], "correct": [0]}, {"q": "Do they eat a lot?", "type": "single", "options": [{"text": "Yes, they do."}, {"text": "No, they don't."}], "correct": [1]}, {"q": "Can Sam have a kitten?", "type": "single", "options": [{"text": "We don't know."}, {"text": "Yes, he can."}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'task', replace($blk${"title": "Письмо другу ✉️", "needs_review": true, "html": "<p>Напиши короткое письмо другу про своих домашних животных или животных в зоопарке (50–70 слов).</p><p><i>Пример: Hi Tom! How are you? I'm great! I want to tell you about my pets. I've got a dog and a goldfish. My dog's name is Rex. He's big and friendly. He likes running and playing in the park. My goldfish doesn't have a name. It's small and orange. Do you have a pet? Bye! Anna</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:180px\"></p><h3>Супер-пупер! Хорошая работа. Спасибо тебе :) 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
