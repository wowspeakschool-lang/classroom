-- Super Minds 3 · Unit 1 · School · Homework 5
-- собрано tools/sm3_build.py --lesson u1_hw5
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 1 · School', 1
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 1 · School');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 1 · School';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>Сегодня мы вспомним историю, с которой познакомились на уроке, и выполним по ней задания.</p><p>Для начала прочитай текст ещё раз — вспомни, в какое приключение попали Lucy и Ben.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<h3>Ben and Lucy in the library</h3><p><img src=\"@@MEDIA@@sm3/u1/story_library_1.webp\" alt=\"Кадры 1–6\" style=\"max-width:100%\"></p><p><img src=\"@@MEDIA@@sm3/u1/story_library_2.webp\" alt=\"Кадры 7–8\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Who is Mr Williams?", "type": "single", "options": [{"text": "teacher"}, {"text": "librarian"}, {"text": "shop assistant"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'truefalse', replace($blk${"title": "Выбери «верно» или «неверно» для каждого предложения. Не торопись!", "statements": [{"text": "Ben and Lucy are in the library.", "answer": true}, {"text": "The book is easy to read.", "answer": false}, {"text": "The book is in code.", "answer": true}, {"text": "The librarian, Mr Williams, helps the explorers to read the code.", "answer": false}, {"text": "Lucy finds the secret to the book.", "answer": true}, {"text": "Horax understands the code.", "answer": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'task', replace($blk${"title": "А теперь задание посложнее!", "needs_review": true, "html": "<p>Мы узнали, что Lucy и Ben могут прочесть книгу с помощью секретной записки. А сможешь ли ты расшифровать их послание, используя код?</p><p><img src=\"@@MEDIA@@sm3/u1/story_code.webp\" alt=\"Код\" style=\"max-width:100%\"></p><p>Запиши в поле ниже, что получилось.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/congrats_popper.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился с домашней работой 🎉</h3><p>Ты молодец! Увидимся на занятии.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5);
end
$mig$;
