-- Super Minds 1 · Unit 8 · My body · Homework 2
-- собрано tools/sm1_build.py --lesson u8_hw2
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
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>В этом уроке тебя ждут несколько интересных заданий! Выполни все упражнения, если хочешь выучить тему на все 100!</p><p>В конце тебя будет ждать дополнительное задание. Если ты его сделаешь, то получишь дополнительную ⭐ от учителя!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p><p><img src=\"@@MEDIA@@sm1/u8/grammar_can_cant.webp\" alt=\"I can / I can't\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p>Для начала давай посмотрим видео! Как думаешь, каких животных ты увидишь там?</p><p>Посмотри видео один раз, внимательно слушай и проверь — угадал ли ты?</p><p>Затем посмотри видео снова и повторяй за животными.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'video', replace($blk${"title": "Видео: что умеют животные?", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'hotspot', replace($blk${"title": "Отлично! У меня для тебя есть ещё одно задание! Посмотри внимательно на картинку. Соедини предложения с подходящей картинкой!", "mode": "label", "image": "@@MEDIA@@sm1/u8/sb_can_cant_kids.webp", "points": [{"x": 67, "y": 12, "text": "I can stand on one leg.", "audio_tts": "I can stand on one leg."}, {"x": 37, "y": 14, "text": "I can't stand on one leg.", "audio_tts": "I can't stand on one leg."}, {"x": 45, "y": 42, "text": "I can't skip.", "audio_tts": "I can't skip."}, {"x": 28, "y": 65, "text": "I can skip.", "audio_tts": "I can skip."}, {"x": 45, "y": 72, "text": "I can't touch my toes.", "audio_tts": "I can't touch my toes."}, {"x": 77, "y": 89, "text": "I can touch my toes.", "audio_tts": "I can touch my toes."}], "extras": []}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Отлично! Это ещё не всё! Посмотри внимательно на картинку и выбери правильный вариант.", "type": "single", "image": "@@MEDIA@@sm1/u8/ab_cant_swim.webp", "options": [{"text": "I can swim."}, {"text": "I can't swim."}], "correct": [1]}, {"q": "Посмотри на картинку и выбери правильный вариант.", "type": "single", "image": "@@MEDIA@@sm1/u8/ab_stand_one_leg.webp", "options": [{"text": "I can stand on one leg."}, {"text": "I can't stand on one leg."}], "correct": [0]}, {"q": "Посмотри на картинку и выбери правильный вариант.", "type": "single", "image": "@@MEDIA@@sm1/u8/she_cant_skip.webp", "options": [{"text": "I can skip."}, {"text": "I can't skip."}], "correct": [1]}, {"q": "Посмотри на картинку и выбери правильный вариант.", "type": "single", "image": "@@MEDIA@@sm1/u8/ab_can_ski.webp", "options": [{"text": "I can't ski."}, {"text": "I can ski."}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'speaking', replace($blk${"title": "Познакомься с Бобом 🎤", "html": "<p>Давай познакомимся с новым героем! Это — Боб. Он расскажет тебе, что он умеет делать! Послушай запись и узнай, что умеет Боб.</p><p>А теперь настала твоя очередь! Расскажи, что ты умеешь делать, и запиши свой ответ на платформе!</p>", "sample": "", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'match', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Соедини описание с картинкой.", "pairs": [{"left_image": "@@MEDIA@@sm1/u8/ab_cant_swim.webp", "right": "I can't swim.", "right_audio_tts": "I can't swim."}, {"left_image": "@@MEDIA@@sm1/u8/ab_stand_one_leg.webp", "right": "I can stand on one leg.", "right_audio_tts": "I can stand on one leg."}, {"left_image": "@@MEDIA@@sm1/u8/ab_cant_ride_bike.webp", "right": "I can't ride a bike.", "right_audio_tts": "I can't ride a bike."}, {"left_image": "@@MEDIA@@sm1/u8/ab_play_football.webp", "right": "I can play football.", "right_audio_tts": "I can play football."}, {"left_image": "@@MEDIA@@sm1/u8/ab_skip.webp", "right": "I can skip.", "right_audio_tts": "I can skip."}, {"left_image": "@@MEDIA@@sm1/u8/ab_cant_piano.webp", "right": "I can't play the piano.", "right_audio_tts": "I can't play the piano."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "A fish ___ swim.", "type": "single", "options": [{"text": "can"}, {"text": "can't"}], "correct": [0]}, {"q": "A dog ___ fly.", "type": "single", "options": [{"text": "can"}, {"text": "can't"}], "correct": [1]}, {"q": "A bird ___ fly.", "type": "single", "options": [{"text": "can't"}, {"text": "can"}], "correct": [1]}, {"q": "A fish ___ walk.", "type": "single", "options": [{"text": "can't"}, {"text": "can"}], "correct": [0]}, {"q": "A monkey ___ climb trees.", "type": "single", "options": [{"text": "can"}, {"text": "can't"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился с домашней работой. Вот твой приз — звезда победителя! ⭐</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9);
end
$mig$;
