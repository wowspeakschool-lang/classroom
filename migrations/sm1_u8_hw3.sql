-- Super Minds 1 · Unit 8 · My body · Homework 3
-- собрано tools/sm1_build.py --lesson u8_hw3
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
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание! 👋</h2><p>В этом уроке тебя ждут интерактивные видео и много интересных упражнений!</p><p>В конце урока есть дополнительные задания — их можно выполнить по желанию, но если ты их сделаешь, то получишь дополнительный балл от учителя! ⭐</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p><p><img src=\"@@MEDIA@@sm1/u8/grammar_can_you.webp\" alt=\"Can you …?\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p>Ура! Мы посмотрим видео! Как думаешь, с какими персонажами ты познакомишься?</p><p>Для начала посмотри видео один раз, внимательно слушай, что говорят персонажи.</p><p>Посмотри видео ещё раз и повторяй за персонажами.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'video', replace($blk${"title": "Видео: Can you …?", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'match', replace($blk${"title": "Посмотри видео ещё раз и соедини вопросы и ответы", "pairs": [{"left": "Can you swim?", "right": "Yes, I can.", "right_audio_tts": "Yes, I can."}, {"left": "Can you fly?", "right": "No, I can't.", "right_audio_tts": "No, I can't."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'hotspot', replace($blk${"title": "У тебя есть ещё одно практическое задание! Внимательно посмотри на картинку. Соедини предложения с подходящей картинкой.", "mode": "label", "image": "@@MEDIA@@sm1/u8/abilities_sheet.webp", "points": [{"x": 16, "y": 25, "text": "I can't swim.", "audio_tts": "I can't swim."}, {"x": 48, "y": 25, "text": "I can stand on one leg.", "audio_tts": "I can stand on one leg."}, {"x": 78, "y": 30, "text": "I can't ride a bike.", "audio_tts": "I can't ride a bike."}, {"x": 14, "y": 75, "text": "I can play football.", "audio_tts": "I can play football."}, {"x": 37, "y": 75, "text": "I can skip.", "audio_tts": "I can skip."}, {"x": 75, "y": 78, "text": "I can't play the piano.", "audio_tts": "I can't play the piano."}], "extras": []}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'gaps', replace($blk${"title": "Молодец! Внимательно прочитай предложения. Посмотри на смайлик перед предложением и выбери can или can't", "mode": "drag", "text": "✗ I __can't__ swim.\n✓ He __can__ ride a horse.\n✓ She __can__ play tennis.\n✗ He __can't__ play the piano.\n✓ She __can__ ride a bike.\n✓ She __can__ do ballet."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'speaking', replace($blk${"title": "Мой монстрик 🎤", "html": "<p>Посмотри, это мой монстрик! Послушай, что он умеет делать!</p><p>Нарисуй своего монстрика, раскрась и расскажи: что он умеет делать?</p><p><b>Пример:</b> It can jump. It can fly!</p>", "image": "@@MEDIA@@sm1/u8/monster.webp", "sample": "", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов!<br>Can a fish swim?", "type": "single", "options": [{"text": "Yes, it can."}, {"text": "No, it can't."}], "correct": [0]}, {"q": "Can a dog fly?", "type": "single", "options": [{"text": "Yes, it can."}, {"text": "No, it can't."}], "correct": [1]}, {"q": "Can a bird fly?", "type": "single", "options": [{"text": "No, it can't."}, {"text": "Yes, it can."}], "correct": [1]}, {"q": "Can a penguin fly?", "type": "single", "options": [{"text": "No, it can't."}, {"text": "Yes, it can."}], "correct": [0]}, {"q": "Can a monkey climb trees?", "type": "single", "options": [{"text": "Yes, it can."}, {"text": "No, it can't."}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"words": ["Can", "you", "swim?"], "sentence": "Can you swim?", "audio_tts": "Can you swim?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"words": ["Can", "you", "ride", "a", "bike?"], "sentence": "Can you ride a bike?", "audio_tts": "Can you ride a bike?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'order', replace($blk${"words": ["No,", "I", "can't", "play", "the", "piano."], "sentence": "No, I can't play the piano.", "audio_tts": "No, I can't play the piano."}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание, ты молодец!</h3><p>Лови звёздочку! ⭐ Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12);
end
$mig$;
