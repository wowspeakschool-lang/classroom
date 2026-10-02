-- Super Minds 3 · Unit 3 · At home · Homework 2
-- собрано tools/sm3_build.py --lesson u3_hw2
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
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет!</h2><p>Сегодня тебя ждёт много интересных заданий. Удачи тебе!</p><p>Готов начать? Внимательно посмотри видео.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Видео: который час?", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"title": "Посмотри видео ещё раз и соедини картинки с описанием", "pairs": [{"left_image": "@@MEDIA@@sm3/u3/clock_quarter_past_eight.svg", "right": "It’s quarter past eight", "right_audio_tts": "It's quarter past eight"}, {"left_image": "@@MEDIA@@sm3/u3/clock_half_past_eight.svg", "right": "It’s half past eight", "right_audio_tts": "It's half past eight"}, {"left_image": "@@MEDIA@@sm3/u3/clock_quarter_past_five.svg", "right": "It’s quarter past five", "right_audio_tts": "It's quarter past five"}, {"left_image": "@@MEDIA@@sm3/u3/clock_quarter_to_seven.svg", "right": "It’s quarter to seven", "right_audio_tts": "It's quarter to seven"}, {"left_image": "@@MEDIA@@sm3/u3/clock_half_past_six.svg", "right": "It’s half past six", "right_audio_tts": "It's half past six"}, {"left_image": "@@MEDIA@@sm3/u3/clock_twelve_oclock.svg", "right": "It’s twelve o’clock", "right_audio_tts": "It's twelve o'clock"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"html": "<h3>Супер! Ты прекрасно справляешься!</h3><p>Давай ещё немного потренируемся. Посмотри на картинки и опиши время, которое на них указано.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'task', replace($blk${"title": "Сколько времени на картинке?", "needs_review": true, "html": "<p><img src=\"@@MEDIA@@sm3/u3/digital_two_fifteen.svg\" alt=\"\" style=\"height:150px\"></p><p>Опиши время по-английски.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'task', replace($blk${"title": "Сколько времени на картинке?", "needs_review": true, "html": "<p><img src=\"@@MEDIA@@sm3/u3/digital_eleven_oclock.svg\" alt=\"\" style=\"height:150px\"></p><p>Опиши время по-английски.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'task', replace($blk${"title": "Сколько времени на картинке?", "needs_review": true, "html": "<p><img src=\"@@MEDIA@@sm3/u3/digital_twelve_forty_five.svg\" alt=\"\" style=\"height:150px\"></p><p>Опиши время по-английски.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'task', replace($blk${"title": "Сколько времени на картинке?", "needs_review": true, "html": "<p><img src=\"@@MEDIA@@sm3/u3/digital_nine_thirty.svg\" alt=\"\" style=\"height:150px\"></p><p>Опиши время по-английски.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'task', replace($blk${"title": "Сколько времени на картинке?", "needs_review": true, "html": "<p><img src=\"@@MEDIA@@sm3/u3/digital_five_forty_five.svg\" alt=\"\" style=\"height:150px\"></p><p>Опиши время по-английски.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'task', replace($blk${"title": "Сколько времени на картинке?", "needs_review": true, "html": "<p><img src=\"@@MEDIA@@sm3/u3/digital_eight_oclock.svg\" alt=\"\" style=\"height:150px\"></p><p>Опиши время по-английски.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>SUPER! Ты сделал все основные задания!</h3><p>У меня есть для тебя ещё одно задание. Оно дополнительное, но если ты его сделаешь, получишь дополнительную ⭐</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'task', replace($blk${"title": "Опиши свой день по времени", "needs_review": true, "html": "<p>Напиши своё расписание и расскажи его учителю на уроке.</p><p><i>Пример:<br>I go to school at 8:30.<br>I have lunch at 12 o’clock.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_jump.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты справился, молодец!</h3><p>Встретимся на уроке :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12);
end
$mig$;
