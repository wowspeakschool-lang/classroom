-- Super Minds 3 · Unit 1 · School · Homework 6
-- собрано tools/sm3_build.py --lesson u1_hw6
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
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет!</h2><p>Сегодня ты будешь много работать с текстом. Скорее приступай к заданиям :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<h3>Puzzles are great fun</h3><p>Прочитай историю Оливера — она понадобится в обоих заданиях.</p><p><img src=\"@@MEDIA@@sm3/u1/story_oliver.webp\" alt=\"История Оливера\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'gaps', replace($blk${"title": "Вставь пропущенные слова так, чтобы предложения совпали с рассказом", "mode": "drag", "text": "1. The children think Oliver is silly because he doesn't like __football and computer games__.\n2. Oliver thinks stories are boring because they don't have __numbers and dates__.\n3. Oliver can say what __day__ it is when he looks at a date.\n4. The children think Oliver is a __computer__.\n5. Oliver wants to start a __puzzle club__ at school.\n6. Everyone __likes__ Oliver's idea."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'truefalse', replace($blk${"title": "Отметь верные и неверные утверждения", "statements": [{"text": "The boys and girls think Oliver is different.", "correct": true}, {"text": "Oliver likes sitting under a tree and thinking.", "correct": true}, {"text": "Oliver likes listening to Ms Sanders’ stories.", "correct": false}, {"text": "Ms Sanders writes the date of her birthday on the board.", "correct": true}, {"text": "The computer and Oliver say different days.", "correct": false}, {"text": "Mike wants to learn to do the same thing as Oliver.", "correct": true}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_jump.webp\" alt=\"\" style=\"height:180px\"></p><h3>Урааа, ты справился, поздравляю!</h3><p>До скорой встречи!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4);
end
$mig$;
