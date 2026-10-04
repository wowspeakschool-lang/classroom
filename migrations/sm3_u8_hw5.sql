-- Super Minds 3 · Unit 8 · Countries · Homework 5
-- собрано tools/sm3_build.py --lesson u8_hw5
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 8 · Countries', 8
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 8 · Countries');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 8 · Countries';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! Как здорово, что ты решил сделать домашнее задание!</h2><p>Сегодня тебя ждёт текст и интересные задания. В конце — дополнительные: сделаешь их, получишь звание чемпиона английского.</p><p>Начни с того, что прочитай историю ещё раз. Кстати, ты помнишь, что Бен и Люси ели на обед?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u8/story_library_1.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u8/story_library_2.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'sequence', replace($blk${"title": "Прочитай историю ещё раз и расставь предложения в правильном порядке", "items": [{"text": "First Lucy and Ben look at a football stadium in Brazil."}, {"text": "Then they look at the Great Wall of China."}, {"text": "After that they look at the opera house in Sydney."}, {"text": "Then they see Mr Williams, the librarian."}, {"text": "Ben says that he is hungry."}, {"text": "They see that they haven’t got the book."}, {"text": "They want to look for their book."}, {"text": "Finally Lucy finds the missing letters."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/good_luck_clover.webp\" alt=\"\" style=\"height:180px\"></p><h3>А здесь ещё одно задание — для самых крутых учеников!</h3><p>Прочитай текст и выполни упражнение после него. Читай внимательно!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u8/reading_food_culture.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'quiz', replace($blk${"title": "Чему нас учит этот рассказ?", "questions": [{"q": "Выбери правильный ответ", "type": "single", "options": [{"text": "It’s interesting to try food from another culture."}, {"text": "Eat only what you really know."}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился с домашней работой.</h3><p>Вот твой приз — большой кубок победителя. Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7);
end
$mig$;
