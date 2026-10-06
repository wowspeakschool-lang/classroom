-- Go Getter 1 · Unit 6 · My day · Homework 4
-- собрано tools/gg1_build.py --lesson u6_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 6 · My day', 6
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 6 · My day');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 6 · My day';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Сегодня мы закрепим знания, полученные на уроке, и ты без проблем сможешь определять время по часам и подсказывать время другим.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u6/card_time.webp\" alt=\"Telling the time\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p>Внимательно посмотри видео и постарайся запомнить, как правильно определять время на английском. Повторяй фразы за видео, чтобы хорошенько запомнить.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'video', replace($blk${"title": "Telling the time", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'match', replace($blk${"title": "Соедини предложения с часами", "pairs": [{"left": "It's quarter to five.", "right_image": "@@MEDIA@@gg1/u6/clock_0445.svg", "left_audio_tts": "It's quarter to five."}, {"left": "It's six o'clock.", "right_image": "@@MEDIA@@gg1/u6/clock_0600.svg", "left_audio_tts": "It's six o'clock."}, {"left": "It's ten past nine.", "right_image": "@@MEDIA@@gg1/u6/clock_0910.svg", "left_audio_tts": "It's ten past nine."}, {"left": "It's quarter past one.", "right_image": "@@MEDIA@@gg1/u6/clock_0115.svg", "left_audio_tts": "It's quarter past one."}, {"left": "It's twenty to nine.", "right_image": "@@MEDIA@@gg1/u6/clock_0840.svg", "left_audio_tts": "It's twenty to nine."}, {"left": "It's half past two.", "right_image": "@@MEDIA@@gg1/u6/clock_0230.svg", "left_audio_tts": "It's half past two."}, {"left": "It's five past five.", "right_image": "@@MEDIA@@gg1/u6/clock_0505.svg", "left_audio_tts": "It's five past five."}, {"left": "It's five to one.", "right_image": "@@MEDIA@@gg1/u6/clock_1255.svg", "left_audio_tts": "It's five to one."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "Расставь фразы в диалоги. Расписание телепрограмм поможет тебе!", "mode": "drag", "image": "@@MEDIA@@gg1/u6/tv_schedule.webp", "text": "1. A: What time is Pet Time? B: It's at six o'clock. (пример)\n2. A: What time is That's Magic? B: __It's at quarter past seven.__\n3. A: __What time is Happy Days?__ B: It's at five past seven.\n4. A: __What time is Super Girl?__ B: It's at twenty-five to seven.\n5. A: What time is The Great Big Talent Show? B: __It's at ten to eight.__\n6. A: OK. __What time is it__ now? B: It's five to six. Hurry up!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'sequence', replace($blk${"title": "Расставь предложения так, чтобы получился складный диалог", "items": [{"text": "What time is it, Mandy?"}, {"text": "It's half past five. Oh no!"}, {"text": "What's wrong? Are you OK?"}, {"text": "No, I'm not. I'm late for my music lesson."}, {"text": "Oh dear. What time is your music lesson?"}, {"text": "It's at quarter to six. Bye!"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'task', replace($blk${"title": "Во сколько? ✍️", "needs_review": true, "html": "<p>Продолжи предложения о себе. Во сколько ты делаешь все эти дела? Пиши время словами, например, <i>twenty to seven</i> или <i>six o'clock</i>.</p><ol><li>I get up at ______.</li><li>I have breakfast at ______.</li><li>I go to school at ______.</li><li>I do my homework at ______.</li><li>I go to bed at ______.</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
