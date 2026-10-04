-- Super Minds 3 · Unit 3 · At home · Homework 7
-- собрано tools/sm3_build.py --lesson u3_hw7
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
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет!</h2><p>Сегодня мы повторим с тобой профессии, которые ты изучил на занятии. Тебя ждёт много интересных заданий. Готов начать?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'flashcards', replace($blk${"cards": [{"text": "firefighter", "translation": "пожарный", "audio_tts": "firefighter", "image": "@@MEDIA@@sm3/u3/job_firefighter.webp"}, {"text": "cleaner", "translation": "уборщик", "audio_tts": "cleaner", "image": "@@MEDIA@@sm3/u3/job_cleaner.webp"}, {"text": "vet", "translation": "ветеринар", "audio_tts": "vet", "image": "@@MEDIA@@sm3/u3/job_vet.webp"}, {"text": "police officer", "translation": "полицейский", "audio_tts": "police officer", "image": "@@MEDIA@@sm3/u3/job_police.webp"}, {"text": "teacher", "translation": "учитель", "audio_tts": "teacher", "image": "@@MEDIA@@sm3/u3/job_teacher.webp"}, {"text": "security guard", "translation": "охранник", "audio_tts": "security guard", "image": "@@MEDIA@@sm3/u3/job_security.webp"}, {"text": "ambulance driver", "translation": "водитель скорой помощи", "audio_tts": "ambulance driver", "image": "@@MEDIA@@sm3/u3/job_ambulance_driver.webp"}, {"text": "shopkeeper", "translation": "продавец", "audio_tts": "shopkeeper", "image": "@@MEDIA@@sm3/u3/job_shopkeeper.webp"}, {"text": "nurse", "translation": "медсестра", "audio_tts": "nurse", "image": "@@MEDIA@@sm3/u3/job_nurse.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'exact_input', replace($blk${"items": [{"image": "@@MEDIA@@sm3/u3/job_firefighter.webp", "prompt": "Посмотри на картинку и напиши профессию", "accept": ["firefighter", "Firefighter"], "audio_tts": "firefighter"}, {"image": "@@MEDIA@@sm3/u3/job_cleaner.webp", "prompt": "Посмотри на картинку и напиши профессию", "accept": ["cleaner", "Cleaner"], "audio_tts": "cleaner"}, {"image": "@@MEDIA@@sm3/u3/job_vet.webp", "prompt": "Посмотри на картинку и напиши профессию", "accept": ["vet", "Vet"], "audio_tts": "vet"}, {"image": "@@MEDIA@@sm3/u3/job_police.webp", "prompt": "Посмотри на картинку и напиши профессию", "accept": ["police officer", "Police officer"], "audio_tts": "police officer"}, {"image": "@@MEDIA@@sm3/u3/job_teacher.webp", "prompt": "Посмотри на картинку и напиши профессию", "accept": ["teacher", "Teacher"], "audio_tts": "teacher"}, {"image": "@@MEDIA@@sm3/u3/job_security.webp", "prompt": "Посмотри на картинку и напиши профессию", "accept": ["security guard", "Security guard"], "audio_tts": "security guard"}, {"image": "@@MEDIA@@sm3/u3/job_ambulance_driver.webp", "prompt": "Посмотри на картинку и напиши профессию", "accept": ["ambulance driver", "Ambulance driver"], "audio_tts": "ambulance driver"}, {"image": "@@MEDIA@@sm3/u3/job_shopkeeper.webp", "prompt": "Посмотри на картинку и напиши профессию", "accept": ["shopkeeper", "Shopkeeper"], "audio_tts": "shopkeeper"}, {"image": "@@MEDIA@@sm3/u3/job_nurse.webp", "prompt": "Посмотри на картинку и напиши профессию", "accept": ["nurse", "Nurse"], "audio_tts": "nurse"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/good_luck_clover.webp\" alt=\"\" style=\"height:180px\"></p><h3>HELLO! Добро пожаловать в дополнительное домашнее задание!</h3><p>Сегодня мы повторим слова, которые ты изучал на уроке. Готов начать тренироваться?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'match', replace($blk${"title": "Внимательно посмотри на картинки и соедини слова с подходящими изображениями", "pairs": [{"left_image": "@@MEDIA@@sm3/u3/job_firefighter.webp", "right": "firefighter", "right_audio_tts": "firefighter"}, {"left_image": "@@MEDIA@@sm3/u3/job_cleaner.webp", "right": "cleaner", "right_audio_tts": "cleaner"}, {"left_image": "@@MEDIA@@sm3/u3/job_vet.webp", "right": "vet", "right_audio_tts": "vet"}, {"left_image": "@@MEDIA@@sm3/u3/job_police.webp", "right": "police officer", "right_audio_tts": "police officer"}, {"left_image": "@@MEDIA@@sm3/u3/job_teacher.webp", "right": "teacher", "right_audio_tts": "teacher"}, {"left_image": "@@MEDIA@@sm3/u3/job_security.webp", "right": "security guard", "right_audio_tts": "security guard"}, {"left_image": "@@MEDIA@@sm3/u3/job_ambulance_driver.webp", "right": "ambulance driver", "right_audio_tts": "ambulance driver"}, {"left_image": "@@MEDIA@@sm3/u3/job_shopkeeper.webp", "right": "shopkeeper", "right_audio_tts": "shopkeeper"}, {"left_image": "@@MEDIA@@sm3/u3/job_nurse.webp", "right": "nurse", "right_audio_tts": "nurse"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'match', replace($blk${"title": "МОЛОДЕЦ! Давай ещё потренируемся — прочитай описание и выбери соответствующую профессию", "pairs": [{"left": "cleaner", "right": "This person cleans the town.", "right_audio_tts": "This person cleans the town."}, {"left": "police officer", "right": "This person helps people.", "right_audio_tts": "This person helps people."}, {"left": "teacher", "right": "This person teaches people.", "right_audio_tts": "This person teaches people."}, {"left": "vet", "right": "This person looks after animals.", "right_audio_tts": "This person looks after animals."}, {"left": "firefighter", "right": "This person stops fire.", "right_audio_tts": "This person stops fire."}, {"left": "ambulance driver", "right": "This person takes ill people to hospital.", "right_audio_tts": "This person takes ill people to hospital."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<h3>УРА! Осталось последнее задание — внимательно прочитай текст</h3><p><b>Project.</b> Choose a job that people do at night. Write a diary for their day or night.</p><p><b>A Police Officer’s Diary</b><br><i>Night</i><br>6 o’clock — I wake up and have breakfast.<br>7 o’clock — I feed the dog and then I cycle to work.<br>9 o’clock — I usually have a break and drink some tea.<br>12 o’clock — I have a sandwich for lunch.<br>5 o’clock — I finish work and I sometimes have dinner with the other police officers.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'task', replace($blk${"title": "Выбери работу, которую люди выполняют по ночам", "needs_review": true, "html": "<p><img src=\"@@MEDIA@@sm3/u3/scene_night_jobs.webp\" alt=\"\" style=\"max-width:100%\"></p><p>Опиши график работы как в примере выше. Не забудь показать свой текст учителю :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_jump.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты выполнил все задания!</h3><p>ТЫ СУПЕР КРУТ! BYE :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
