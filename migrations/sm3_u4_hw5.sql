-- Super Minds 3 · Unit 4 · In the town · Homework 5
-- собрано tools/sm3_build.py --lesson u4_hw5
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 4 · In the town', 4
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 4 · In the town');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 4 · In the town';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет-привет!</h2><p>Сегодня мы вспомним историю, которую ты смотрел на уроке. Кто в ней главный герой?</p><p>Прочитай историю ниже и сделай задания к ней.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u4/story_pirate_ship_1.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u4/story_pirate_ship_2.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Прочитай текст ещё раз и впиши слова в пропуски по смыслу. Слова: letter · dog · near · going · high · cat · museum. Два слова лишние!", "text": "1. Lucy and Ben are going to the tower to get the next __letter__.\n2. Lucy and Ben have got their __dog__ with them.\n3. Look, the tower’s over there, the school’s __near__.\n4. ‘Lucy! Where are you __going__?’\n5. Lucy and Ben are really __high__ on the Pirate Ship."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'sequence', replace($blk${"title": "Молодец! Расставь предложения в правильном порядке по смыслу", "items": [{"text": "Ben and Lucy know that the tower is near the market square."}, {"text": "Ben wants to go to the funfair. Lucy says, ‘We’re going to the tower.’"}, {"text": "Then Lucy doesn’t go to the tower. She goes to the funfair."}, {"text": "Ben and Lucy go on the Pirate Ship. They are above the tower."}, {"text": "Horax and Zelda are in the tower. It’s the wrong place."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты со всем справился!</h3><p>Увидимся на уроке :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5);
end
$mig$;
