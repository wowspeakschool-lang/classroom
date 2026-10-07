-- Super Minds 1 · Unit 6 · My house · Homework 4
-- собрано tools/sm1_build.py --lesson u6_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 6 · My house', 6
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 6 · My house');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 6 · My house';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет!</h2><p>Сегодня мы с тобой послушаем и прочитаем рассказ. А в конце тебя ждёт дополнительное задание, которое выполняется по желанию. Но ты будешь МЕГА крут, когда справишься с ним!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<h3>Давай повторим всё, что выучили с тобой на уроке:</h3><p><img src=\"@@MEDIA@@sm1/u6/story_key_phrases.webp\" alt=\"Story — At the House\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm1/u6/haunted_house.webp\" alt=\"\" style=\"height:200px\"></p><p>Наши супер друзья — Misty, Thunder, Flash и Whisper — отправляются в жуткий дом. Как думаешь, встретят ли ребята в этом доме привидений?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'video', replace($blk${"title": "Для начала прослушай аудио и выполни задание.", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Прослушай историю ещё раз. Какие слова из перечисленных упоминаются в истории? Выбери все верные.", "type": "multiple", "options": [{"text": "house"}, {"text": "stairs"}, {"text": "kitchen"}, {"text": "cellar"}, {"text": "bedroom"}], "correct": [0, 1, 3]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p>Внимательно прочитай историю и выполни упражнения.</p><p><img src=\"@@MEDIA@@sm1/u6/story_old_house.webp\" alt=\"Story\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'hotspot', replace($blk${"title": "Смотри! История запуталась, и картинки стоят не в правильном порядке 😱 Соедини картинку и номер: первую картинку истории — с «Picture 1», вторую — с «Picture 2», и так по порядку. Постарайся не подсматривать, а в конце можешь проверить себя по тексту.", "mode": "label", "image": "@@MEDIA@@sm1/u6/story_old_house_shuffled.webp", "points": [{"x": 25, "y": 36, "text": "Picture 1"}, {"x": 75, "y": 87, "text": "Picture 2"}, {"x": 25, "y": 87, "text": "Picture 3"}, {"x": 25, "y": 12, "text": "Picture 4"}, {"x": 75, "y": 12, "text": "Picture 5"}, {"x": 75, "y": 36, "text": "Picture 6"}, {"x": 25, "y": 61, "text": "Picture 7"}, {"x": 75, "y": 61, "text": "Picture 8"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'match', replace($blk${"title": "Ты запомнил, кто что сказал? Прочитай историю ещё раз и соедини фразы с героями. Удачи ❤", "pairs": [{"left": "Go in? No way!", "right": "Flash", "left_audio_tts": "Go in? No way!"}, {"left": "It's cold here.", "right": "Misty", "left_audio_tts": "It's cold here."}, {"left": "Misty, where are you?", "right": "Whisper", "left_audio_tts": "Misty, where are you?"}, {"left": "Careful, Misty.", "right": "Thunder", "left_audio_tts": "Careful, Misty."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'video', replace($blk${"title": "⭐ ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ. Смотри, наша история ожила и превратилась в мультик! Давай посмотрим его и выполним упражнение!", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'sequence', replace($blk${"title": "Посмотри видео ещё раз. Расставь предложения из видео в правильном порядке:", "items": [{"text": "There's the old house.", "audio_tts": "There's the old house."}, {"text": "Wait for me here.", "audio_tts": "Wait for me here."}, {"text": "The stairs to the cellar.", "audio_tts": "The stairs to the cellar."}, {"text": "It's cold here.", "audio_tts": "It's cold here."}, {"text": "Yuck! Big spiders!", "audio_tts": "Yuck! Big spiders!"}, {"text": "Wow! Big rats!", "audio_tts": "Wow! Big rats!"}, {"text": "There's no problem, you can come in.", "audio_tts": "There's no problem, you can come in."}, {"text": "Misty, where are you?", "audio_tts": "Misty, where are you?"}, {"text": "Here I am.", "audio_tts": "Here I am."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю!</h3><p>Ты завершил домашнее задание, ты замечательный ученик! ✨</p><p>Жду тебя на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
