-- Super Minds 3 · Unit 6 · Gadgets · Homework 3
-- собрано tools/sm3_build.py --lesson u6_hw3
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 6 · Gadgets', 6
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 6 · Gadgets');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 6 · Gadgets';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет-привет! Давай начинать домашнюю работу :)</h2><p>Послушай песню и исправь предложения.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'task', replace($blk${"title": "Послушай песню и исправь предложения", "needs_review": true, "audio": "", "html": "<p><i>My gadget is smaller than yours. → My gadget is bigger than yours.</i></p><p>My gadget is uglier than yours. → …<br>My gadget is older than yours. → …<br>My gadget is cheaper than yours. → …</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'hotspot', replace($blk${"title": "Послушай песенку ещё раз. Посмотри на гаджет и подпиши, что происходит, когда нажимаешь каждую кнопку", "mode": "label", "image": "@@MEDIA@@sm3/u6/scene_four_button_gadget.webp", "points": [{"x": 11.0, "y": 16.0, "text": "torch comes on", "audio_tts": "torch comes on"}, {"x": 83.0, "y": 18.0, "text": "plays a song", "audio_tts": "plays a song"}, {"x": 12.0, "y": 64.0, "text": "fan comes on", "audio_tts": "fan comes on"}, {"x": 83.0, "y": 65.0, "text": "phone someone", "audio_tts": "phone someone"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Заверши диалоги о гаджете", "text": "1. A: What happens when you press the red button?\nB: The torch comes on. I use it to __see everything__.\n2. A: What happens when you press the blue button?\nB: The __song__ comes on. I use it to __have fun__.\n3. A: What happens when you press the brown button?\nB: The __fan__ comes on. I use it to __feel colder__.\n4. A: What happens when you press the green button?\nB: The __phone__ comes on. I use it to __phone someone__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты отлично потрудился!</h3><p>Самое время отдохнуть :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4);
end
$mig$;
