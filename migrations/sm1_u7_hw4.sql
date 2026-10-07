-- Super Minds 1 · Unit 7 · Get dressed · Homework 4
-- собрано tools/sm1_build.py --lesson u7_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 7 · Get dressed', 7
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 7 · Get dressed');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 7 · Get dressed';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>Сегодня мы с тобой послушаем и прочитаем рассказ о наших супердрузьях!</p><p>В конце урока тебя ждёт интерактивное видео — оно дополнительное, его можно сделать по желанию, но ты будешь МЕГА крут, когда справишься с ним!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p><p><img src=\"@@MEDIA@@sm1/u7/story_cap_phrases.webp\" alt=\"Story — The Cap (Key Phrases)\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p>Твоё первое задание — послушать аудио и выполнить тест под ним.</p><p><img src=\"@@MEDIA@@sm1/u7/story_cap_cover.webp\" alt=\"The cap\" style=\"max-width:480px\"></p><p>Но сначала попробуй угадать, какое приключение ждёт наших Супердрузей в этот раз. Название истории — <b>The cap</b>. Может, что-то случится с кепкой?</p><p>Прослушай аудио и узнай, угадал ли ты.</p>", "audio": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Сколько раз звучит слово cap?", "questions": [{"q": "Прослушай историю ещё раз. Посчитай, сколько раз звучит слово <b>cap</b>, и выбери правильный ответ. (Название истории тоже считается.)", "type": "single", "image": "@@MEDIA@@sm1/u7/cap_yellow_clipart.webp", "options": [{"text": "8"}, {"text": "10"}, {"text": "4"}, {"text": "6"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p>Внимательно прочитай историю и выполни упражнение, которое ты увидишь сразу после рассказа.</p><p><img src=\"@@MEDIA@@sm1/u7/story_cap_1_4.webp\" alt=\"The cap, 1–4\" style=\"max-width:100%\"></p><p><img src=\"@@MEDIA@@sm1/u7/story_cap_5_8.webp\" alt=\"The cap, 5–8\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'sequence', replace($blk${"title": "Сейчас прочитай текст ещё раз и выполни задание — расставь предложения в правильном порядке, как они идут в рассказе! У тебя получится!", "image": "@@MEDIA@@sm1/u7/cap_yellow_clipart.webp", "items": [{"text": "My cap isn't here.", "audio_tts": "My cap isn't here."}, {"text": "Look! Gary's wearing my cap.", "audio_tts": "Look! Gary's wearing my cap."}, {"text": "That's my cap, Gary.", "audio_tts": "That's my cap, Gary."}, {"text": "No, it's my cap.", "audio_tts": "No, it's my cap."}, {"text": "Oh no! That's my cap!", "audio_tts": "Oh no! That's my cap!"}, {"text": "I'm very sorry, Gary.", "audio_tts": "I'm very sorry, Gary."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:160px\"></p><h3>Поздравляю! Основная часть готова, ты замечательный ученик! ✨</h3><p>А теперь — дополнительное задание: мультфильм. Посмотри его внимательно, а потом посмотри ещё раз и повторяй за героями.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'video', replace($blk${"title": "Мультфильм Unit 7", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа!</h3><p>Жду тебя на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
