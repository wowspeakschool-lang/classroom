-- Super Minds 3 · Unit 5 · Under the sea · Homework 5
-- собрано tools/sm3_build.py --lesson u5_hw5
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 5 · Under the sea', 5
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 5 · Under the sea');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 5 · Under the sea';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! Вперёд к новым знаниям!</h2><p>Прочитай историю и сделай задания к ней.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u5/story_giant_shell_1.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u5/story_giant_shell_2.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'truefalse', replace($blk${"title": "Выбери true (верно) или false (неверно)", "statements": [{"text": "The next letter is in the giant shell.", "correct": true}, {"text": "Lucy can’t get her arm out of the giant shell.", "correct": false}, {"text": "The shark was in Horax’s cage.", "correct": true}, {"text": "The shark likes Horax and Zelda.", "correct": false}, {"text": "The octopus can’t help the children.", "correct": false}, {"text": "The fish make the letter S.", "correct": true}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'sequence', replace($blk${"title": "Расставь предложения в правильном порядке по смыслу", "items": [{"text": "First Lucy and Ben dive down to a giant shell."}, {"text": "Ben can’t see a letter in the shell."}, {"text": "Then Ben can’t get his arm out of the shell."}, {"text": "They see Horax and Zelda and the shark."}, {"text": "The shark doesn’t get the children. It follows Horax and Zelda."}, {"text": "The octopus helps Ben to get his arm out."}, {"text": "Finally the children look at the fish and see the letter S."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Спасибо! Ты огромный молодец!</h3><p>Увидимся на занятии :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5);
end
$mig$;
