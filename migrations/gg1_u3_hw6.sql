-- Go Getter 1 · Unit 3 · My home · Homework 6
-- собрано tools/gg1_build.py --lesson u3_hw6
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 3 · My home', 3
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 3 · My home');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 3 · My home';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать! 👋</h2><p>Сегодня тебя ждут интересные задания, поехали!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>Послушай диалог. О чём он?</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "О чём диалог? Выбери правильный ответ", "questions": [{"q": "The dialogue is about…", "type": "single", "options": [{"text": "Nancy's bedroom"}, {"text": "Nancy's new house"}, {"text": "Nancy's family"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'task', replace($blk${"title": "Послушай ещё раз. Перепиши предложения, чтобы они стали верными ✍", "needs_review": true, "html": "<ol><li>In Nancy's house there are five rooms.</li><li>The bathroom is upstairs.</li><li>There are two bedrooms.</li><li>There's a TV in Nancy's bedroom.</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери дом Нэнси. Если нужно — можно прослушать диалог ещё раз", "questions": [{"q": "Which is Nancy's house?", "type": "single", "options": [{"text": "House 1"}, {"text": "House 2"}, {"text": "House 3"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "Исправь текст — добавь апострофы. Впиши в каждый пропуск слово с апострофом, используй картинку с правилом", "mode": "type", "image": "@@MEDIA@@gg1/u3/card_apostrophes.webp", "text": "In my dream bedroom __there's|there’s__ (theres) a big bed. __It's|It’s__ (Its) blue. Next to the bed __there's|there’s__ (theres) a table with a lamp. On the floor __there's|there’s__ (theres) a big carpet. It's red, yellow and orange. There __aren't|aren’t__ (arent) any plants in the room but there are lots of posters and photos of my friends. There __isn't|isn’t__ (isnt) a TV but __there's|there’s__ (theres) a computer."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'task', replace($blk${"title": "Комната моей мечты ✍", "needs_review": true, "image": "@@MEDIA@@gg1/u3/house_cutaway_cartoon.webp", "html": "<p>Теперь напиши о своей комнате мечты. Используй текст из предыдущего задания как пример.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура, ты справился с домашним заданием, ты — супер ученик! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7);
end
$mig$;
