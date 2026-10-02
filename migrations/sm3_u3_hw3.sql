-- Super Minds 3 · Unit 3 · At home · Homework 3
-- собрано tools/sm3_build.py --lesson u3_hw3
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 3 · At home', 3
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 3 · At home');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 3 · At home';

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
    (v_lesson, 'hotspot', replace($blk${"title": "Послушай песню ещё раз и выбери подходящее время для каждой картинки", "mode": "label", "image": "@@MEDIA@@sm3/u3/scene_astronaut_day.webp", "points": [{"x": 4.2, "y": 7.1, "text": "quarter to three", "audio_tts": "quarter to three"}, {"x": 72.6, "y": 5.1, "text": "nine o’clock", "audio_tts": "nine o'clock"}, {"x": 6.5, "y": 56.7, "text": "half past nine", "audio_tts": "half past nine"}, {"x": 38.3, "y": 60.1, "text": "half past ten", "audio_tts": "half past ten"}, {"x": 70.6, "y": 57.0, "text": "half past three", "audio_tts": "half past three"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "МОЛОДЕЦ! Послушай песню ещё раз и вставь пропущенные слова ⬇", "mode": "drag", "text": "1. She __gets up__ at quarter to three.\n2. She __is at her door__ at nine o’clock.\n3. She __is in her spaceship__ at half past nine.\n4. She __is on the moon__ at half past ten.\n5. She __is back home__ at half past three.\n6. She __works__ at night."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Здорово! Ты сделал все основные задания!</h3><p>У меня для тебя есть ещё одно задание. Оно дополнительное, но если ты его сделаешь, будешь ПРОСТО ГУРУ английского!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'task', replace($blk${"title": "Представь, что ты пилот космического корабля!", "needs_review": true, "html": "<p>Внимательно прочитай пример ниже и заполни его по-своему. Опиши свой день!</p><p><i>I’m in my spaceship. It’s …<br>I’m the pilot and …<br>It’s …, I’m on the moon.<br>… . … .</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты справился, молодец!</h3><p>Не забудь показать свой ответ на уроке учителю — он даст тебе дополнительный балл. BYE :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6);
end
$mig$;
