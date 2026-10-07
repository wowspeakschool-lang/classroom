-- Super Minds 1 · Unit 5 · My week · Homework 6
-- собрано tools/sm1_build.py --lesson u5_hw6
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 5 · My week', 5
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 5 · My week');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 5 · My week';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнюю работу!</h2><p>Здесь мы с тобой повторим тему, которую ты уже прошёл на уроке. Как всегда, тебя ждут классные задания 😄</p><p>В конце есть вторая, дополнительная часть. Её не обязательно делать, но если у тебя получится её выполнить, то ты будешь мега крут!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p><p><img src=\"@@MEDIA@@sm1/u5/card_go_activities.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"title": "Для начала давай соединим картинку с фразой. Вспомним спортивные занятия!", "pairs": [{"left_image": "@@MEDIA@@sm1/u5/act_go_swimming.webp", "right": "go swimming", "right_audio_tts": "go swimming"}, {"left_image": "@@MEDIA@@sm1/u5/act_go_climbing.webp", "right": "go climbing", "right_audio_tts": "go climbing"}, {"left_image": "@@MEDIA@@sm1/u5/act_go_running.webp", "right": "go running", "right_audio_tts": "go running"}, {"left_image": "@@MEDIA@@sm1/u5/act_go_sledging.webp", "right": "go sledging", "right_audio_tts": "go sledging"}, {"left_image": "@@MEDIA@@sm1/u5/act_go_surfing.webp", "right": "go surfing", "right_audio_tts": "go surfing"}, {"left_image": "@@MEDIA@@sm1/u5/act_go_skiing.webp", "right": "go skiing", "right_audio_tts": "go skiing"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'sort', replace($blk${"title": "Смотри, какие красивые места! Давай выберем, какими видами спорта где можно заниматься. Разложи фразы: Beach — пляж, Mountains — горы.", "groups": [{"name": "Beach 🏖️", "items": [{"text": "go running", "audio_tts": "go running"}, {"text": "go surfing", "audio_tts": "go surfing"}, {"text": "go swimming", "audio_tts": "go swimming"}]}, {"name": "Mountains 🏔️", "items": [{"text": "go climbing", "audio_tts": "go climbing"}, {"text": "go skiing", "audio_tts": "go skiing"}, {"text": "go sledging", "audio_tts": "go sledging"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'hotspot', replace($blk${"title": "А вот ещё несколько мест, где мы можем заниматься спортом. Давай соединим предложения с местами 😀", "mode": "label", "image": "@@MEDIA@@sm1/u5/sport_places.webp", "points": [{"x": 15.3, "y": 36, "text": "We ride a horse there.", "audio_tts": "We ride a horse there."}, {"x": 50.0, "y": 36, "text": "We play football here.", "audio_tts": "We play football here."}, {"x": 84.7, "y": 36, "text": "We go fishing here.", "audio_tts": "We go fishing here."}, {"x": 15.3, "y": 89, "text": "We go running here.", "audio_tts": "We go running here."}, {"x": 50.0, "y": 89, "text": "We go climbing here.", "audio_tts": "We go climbing here."}, {"x": 84.7, "y": 89, "text": "We play tennis here.", "audio_tts": "We play tennis here."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'speaking', replace($blk${"title": "Моё идеальное место для спорта 🎤", "html": "<p>Ты большой-большой молодец! Самое время пофантазировать!</p><p>Придумай своё идеальное место для занятий спортом, нарисуй его. Затем нажми на микрофон и опиши его.</p><p><b>Пример:</b> <i>It’s big and green. I can go climbing and go running there.</i></p>", "sample_tts": "It's big and green. I can go climbing and go running there.", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:180px\"></p><h3>Вау! Отличная работа!</h3><p>Не забудь показать свой рисунок учителю. Он очень-очень хочет его увидеть.</p><p>А теперь — дополнительная часть. Соедини английские фразы с переводом!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'match', replace($blk${"title": "Соедини фразу с переводом", "pairs": [{"left": "go swimming", "right": "заниматься плаванием", "left_audio_tts": "go swimming"}, {"left": "go climbing", "right": "заниматься скалолазанием", "left_audio_tts": "go climbing"}, {"left": "go running", "right": "заниматься бегом", "left_audio_tts": "go running"}, {"left": "go sledging", "right": "кататься на санках", "left_audio_tts": "go sledging"}, {"left": "go surfing", "right": "заниматься серфингом", "left_audio_tts": "go surfing"}, {"left": "go skiing", "right": "кататься на лыжах", "left_audio_tts": "go skiing"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты справился со всем домашним заданием!</h3><p>Увидимся на уроке 🥰</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
