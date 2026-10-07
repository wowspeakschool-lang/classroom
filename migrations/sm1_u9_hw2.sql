-- Super Minds 1 · Unit 9 · Holidays · Homework 2
-- собрано tools/sm1_build.py --lesson u9_hw2
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 9 · Holidays', 9
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 9 · Holidays');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 9 · Holidays';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>В этом уроке тебя ждут интересные упражнения и видео!</p><p>В конце урока есть дополнительное задание — его можно выполнить по желанию! Его делают самые смелые и крутые ученики.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Для начала посмотри видеоролик.</p><p>В видео подружки решают, чем им заняться. Как думаешь, что предложит одна из подружек? <i>Listen to music? Look for shells? Paint a picture?</i></p><p>Внимательно слушай, что говорят девочки в видео. Потом посмотри видео ещё раз и повторяй за подружками.</p><p><img src=\"@@MEDIA@@sm1/u9/hw2_friends_talk.webp\" alt=\"Подружки\" style=\"max-width:420px\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'video', replace($blk${"title": "Видео: чем займутся подружки?", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'match', replace($blk${"title": "Посмотри видео ещё раз и соедини левый столбик с правым, чтобы получились правильные предложения!", "pairs": [{"left": "Let’s eat ice cream.", "right": "Good idea!", "right_audio_tts": "Good idea!"}, {"left": "Let’s listen to music.", "right": "Sorry, I don’t want to.", "right_audio_tts": "Sorry, I don't want to."}, {"left": "Let’s paint a picture.", "right": "I’m not sure.", "right_audio_tts": "I'm not sure."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'match', replace($blk${"title": "Внимательно посмотри на картинки. Соедини предложения с подходящей картинкой.", "pairs": [{"left_image": "@@MEDIA@@sm1/u9/hw2_lets_swim.webp", "right": "Let’s go swimming.", "right_audio_tts": "Let's go swimming."}, {"left_image": "@@MEDIA@@sm1/u9/hw2_lets_music.webp", "right": "Let’s listen to music.", "right_audio_tts": "Let's listen to music."}, {"left_image": "@@MEDIA@@sm1/u9/hw2_lets_photo.webp", "right": "Let’s take a photo.", "right_audio_tts": "Let's take a photo."}, {"left_image": "@@MEDIA@@sm1/u9/hw2_lets_paint.webp", "right": "Let’s paint a picture.", "right_audio_tts": "Let's paint a picture."}, {"left_image": "@@MEDIA@@sm1/u9/hw2_lets_park.webp", "right": "Let’s go to the park.", "right_audio_tts": "Let's go to the park."}, {"left_image": "@@MEDIA@@sm1/u9/hw2_lets_shells.webp", "right": "Let’s look for shells.", "right_audio_tts": "Let's look for shells."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'match', replace($blk${"title": "Посмотри! Здесь три смайлика. Соедини ответы с подходящим смайликом.", "pairs": [{"left_image": "@@MEDIA@@sm1/u9/smile_sorry.webp", "right": "Sorry, I don’t want to.", "right_audio_tts": "Sorry, I don't want to."}, {"left_image": "@@MEDIA@@sm1/u9/smile_not_sure.webp", "right": "I’m not sure.", "right_audio_tts": "I'm not sure."}, {"left_image": "@@MEDIA@@sm1/u9/smile_good_idea.webp", "right": "Good idea!", "right_audio_tts": "Good idea!"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски словами из таблички", "mode": "drag", "image": "@@MEDIA@@sm1/u9/hw2_beach_umbrella.webp", "text": "1. A: Let's __read__ a book.\nB: Good __idea__!\n2. A: Let's __make__ a sandcastle.\nB: __Sorry__, I don't want to!\n3. A: Let's __paint__ a picture.\nB: __Good__ idea!\n4. A: Let's __catch__ a fish.\nB: I'm not __sure__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'sequence', replace($blk${"title": "Молодец! Осталось немного. Послушай аудио и расставь предложения в правильном порядке, чтобы получился диалог.", "audio": "", "audio_tts": "Let's read a book. Sorry, I don't want to. Let's catch a fish. I'm not sure. Let's paint a picture. Good idea!", "items": [{"text": "– Let's read a book."}, {"text": "– Sorry, I don't want to."}, {"text": "– Let's catch a fish."}, {"text": "– I'm not sure."}, {"text": "– Let's paint a picture."}, {"text": "– Good idea!"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'task', replace($blk${"title": "Дополнительное задание ⭐ Твой диалог", "needs_review": true, "html": "<p>Здесь тебя ждёт ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ. Это задание для самых смелых учеников!</p><p>В предыдущем упражнении ты расставил предложения в правильном порядке, и у тебя получился диалог. Используй его как пример. <b>Составь и впиши свой диалог!</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание, ты молодец! 🌟</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9);
end
$mig$;
