-- Super Minds 1 · Unit 8 · My body · Homework 4
-- собрано tools/sm1_build.py --lesson u8_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 8 · My body', 8
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 8 · My body');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 8 · My body';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>Добро пожаловать в домашнее задание! Нас сегодня ждёт много интересных упражнений!</p><p>В конце тебя ждёт интерактивное видео — оно дополнительное, но ты будешь большой молодец, если справишься с ним!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p><p><img src=\"@@MEDIA@@sm1/u8/story_key_phrases.webp\" alt=\"The Problem — key phrases\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p>Сегодня Misty, Flash, Thunder и Whisper подготовили для тебя историю!</p><p>Как думаешь, что с ними случилось на этот раз? Послушай историю, прочитай текст и выполни задания!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'video', replace($blk${"title": "Послушай историю «The Problem»", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<h3>The Problem</h3><p><img src=\"@@MEDIA@@sm1/u8/story_robot_1_6.webp\" alt=\"Кадры 1–6\" style=\"max-width:100%\"></p><p><img src=\"@@MEDIA@@sm1/u8/story_robot_7_8.webp\" alt=\"Кадры 7–8\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'hotspot', replace($blk${"title": "Картинки перемешались! Давай поможем героям восстановить порядок истории! Подпиши каждую картинку: первая картинка истории — «Picture 1», вторая — «Picture 2», и так по порядку. Постарайся не подсматривать, а в конце проверь себя по тексту.", "mode": "label", "image": "@@MEDIA@@sm1/u8/story_robot_shuffled.webp", "points": [{"x": 62, "y": 75, "text": "Picture 1"}, {"x": 12, "y": 25, "text": "Picture 2"}, {"x": 37, "y": 25, "text": "Picture 3"}, {"x": 12, "y": 75, "text": "Picture 4"}, {"x": 37, "y": 75, "text": "Picture 5"}, {"x": 87, "y": 25, "text": "Picture 6"}, {"x": 62, "y": 25, "text": "Picture 7"}, {"x": 87, "y": 75, "text": "Picture 8"}], "extras": []}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'match', replace($blk${"title": "Молодец! Вспомни, кто что говорил в истории, и соедини фразу с героем. Если нужно, перечитай текст ещё раз!", "pairs": [{"left": "Here's the head.", "right": "Whisper", "right_audio_tts": "Whisper"}, {"left": "No problem.", "right": "Flash", "right_audio_tts": "Flash"}, {"left": "It can't speak.", "right": "Thunder", "right_audio_tts": "Thunder"}, {"left": "Robot, can you speak now?", "right": "Misty", "right_audio_tts": "Misty"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Основная часть позади, ты большой молодец! ✨</h3><p>А теперь дополнительное задание — интерактивное видео. Внимательно посмотри видео и выполни все задания в нём. Удачи!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'video', replace($blk${"title": "Интерактивное видео", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты завершил домашнее задание, ты большой молодец! 🌟</h3><p>До встречи на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9);
end
$mig$;
