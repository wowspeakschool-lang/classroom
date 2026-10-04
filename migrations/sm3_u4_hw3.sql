-- Super Minds 3 · Unit 4 · In the town · Homework 3
-- собрано tools/sm3_build.py --lesson u4_hw3
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
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет!</h2><p>Сегодня мы послушаем с тобой песню и сделаем несколько интересных заданий. Удачи тебе!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Итак, поехали! Послушай песню. Кто главный герой?", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'hotspot', replace($blk${"title": "Послушай песню ещё раз и расставь пропущенные слова. Осторожно: в задании ДВА ЛИШНИХ СЛОВА!", "mode": "label", "image": "@@MEDIA@@sm3/u4/song_lost_in_town.webp", "points": [{"x": 19.0, "y": 11.4, "text": "Opposite", "audio_tts": "opposite"}, {"x": 23.0, "y": 41.0, "text": "below", "audio_tts": "below"}, {"x": 18.0, "y": 46.0, "text": "near", "audio_tts": "near"}, {"x": 18.0, "y": 66.8, "text": "in front of", "audio_tts": "in front of"}], "extras": ["between", "above"]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'task', replace($blk${"title": "Придумай свою версию песни", "needs_review": true, "html": "<p>У меня для тебя есть ещё одно задание. Оно дополнительное, но если ты его сделаешь, будешь ПРОСТО ГУРУ английского!</p><p>Послушай песню ещё раз и заполни пропуски своими местами в городе:</p><p><i>Opposite the …,<br>In the …,<br>I’m looking for the …<br>But it’s not there.</i></p><p><i>Just below the …,<br>Near the …,<br>My map says there’s a …<br>But there is not.</i></p><p><i>In front of the …,<br>In the …,<br>There’s a place<br>Where people always meet.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты справился, молодец!</h3><p>Не забудь показать свой ответ на уроке учителю — он даст тебе дополнительный балл. BYE :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4);
end
$mig$;
