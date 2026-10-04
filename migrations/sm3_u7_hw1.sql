-- Super Minds 3 · Unit 7 · At the doctor’s · Homework 1
-- собрано tools/sm3_build.py --lesson u7_hw1
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 7 · At the doctor’s', 7
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 7 · At the doctor’s');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 7 · At the doctor’s';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 1', 'homework',
         60, false, 0
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 1');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 1';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>Сегодня мы выучим слова, связанные со здоровьем. Выполни все задания, если хочешь выучить тему на все 100!</p><p>А в конце тебя ждёт дополнительная часть — её можно сделать по желанию, НО если сделаешь, будешь нереально крут!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'flashcards', replace($blk${"cards": [{"text": "earache", "translation": "боль в ухе", "audio_tts": "earache"}, {"text": "toothache", "translation": "зубная боль", "audio_tts": "toothache"}, {"text": "headache", "translation": "головная боль", "audio_tts": "headache"}, {"text": "doctor", "translation": "врач", "audio_tts": "doctor"}, {"text": "nurse", "translation": "медсестра", "audio_tts": "nurse"}, {"text": "stomachache", "translation": "боль в животе", "audio_tts": "stomachache"}, {"text": "cold", "translation": "простуда", "audio_tts": "cold"}, {"text": "cough", "translation": "кашель", "audio_tts": "cough"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Как по-английски «боль в ухе»?", "type": "single", "options": [{"text": "doctor"}, {"text": "earache"}, {"text": "headache"}, {"text": "toothache"}], "correct": [1]}, {"q": "Как по-английски «зубная боль»?", "type": "single", "options": [{"text": "doctor"}, {"text": "headache"}, {"text": "nurse"}, {"text": "toothache"}], "correct": [3]}, {"q": "Как по-английски «головная боль»?", "type": "single", "options": [{"text": "doctor"}, {"text": "headache"}, {"text": "nurse"}, {"text": "stomachache"}], "correct": [1]}, {"q": "Как по-английски «врач»?", "type": "single", "options": [{"text": "cold"}, {"text": "doctor"}, {"text": "nurse"}, {"text": "stomachache"}], "correct": [1]}, {"q": "Как по-английски «медсестра»?", "type": "single", "options": [{"text": "cold"}, {"text": "cough"}, {"text": "nurse"}, {"text": "stomachache"}], "correct": [2]}, {"q": "Как по-английски «боль в животе»?", "type": "single", "options": [{"text": "cold"}, {"text": "cough"}, {"text": "earache"}, {"text": "stomachache"}], "correct": [3]}, {"q": "Как по-английски «простуда»?", "type": "single", "options": [{"text": "cold"}, {"text": "cough"}, {"text": "earache"}, {"text": "toothache"}], "correct": [0]}, {"q": "Как по-английски «кашель»?", "type": "single", "options": [{"text": "cough"}, {"text": "earache"}, {"text": "headache"}, {"text": "toothache"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'exact_input', replace($blk${"items": [{"prompt": "Напиши по-английски: «боль в ухе»", "accept": ["earache", "Earache"], "audio_tts": "earache"}, {"prompt": "Напиши по-английски: «зубная боль»", "accept": ["toothache", "Toothache"], "audio_tts": "toothache"}, {"prompt": "Напиши по-английски: «головная боль»", "accept": ["headache", "Headache"], "audio_tts": "headache"}, {"prompt": "Напиши по-английски: «врач»", "accept": ["doctor", "Doctor"], "audio_tts": "doctor"}, {"prompt": "Напиши по-английски: «медсестра»", "accept": ["nurse", "Nurse"], "audio_tts": "nurse"}, {"prompt": "Напиши по-английски: «боль в животе»", "accept": ["stomachache", "Stomachache"], "audio_tts": "stomachache"}, {"prompt": "Напиши по-английски: «простуда»", "accept": ["cold", "Cold"], "audio_tts": "cold"}, {"prompt": "Напиши по-английски: «кашель»", "accept": ["cough", "Cough"], "audio_tts": "cough"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/good_luck_clover.webp\" alt=\"\" style=\"height:180px\"></p><h3>А теперь — вторая, дополнительная часть</h3><p>Выполнив эти задания, ты станешь МЕГА крутым учеником!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'match', replace($blk${"title": "Прочитай, на что жалуется человек, и подбери диагноз", "pairs": [{"left": "My ear hurts.", "right": "earache", "right_audio_tts": "earache"}, {"left": "My head hurts.", "right": "headache", "right_audio_tts": "headache"}, {"left": "My tooth hurts.", "right": "toothache", "right_audio_tts": "toothache"}, {"left": "My stomach hurts.", "right": "stomachache", "right_audio_tts": "stomachache"}, {"left": "I sneeze and my nose runs.", "right": "cold", "right_audio_tts": "a cold"}, {"left": "I can’t stop coughing.", "right": "cough", "right_audio_tts": "a cough"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'task', replace($blk${"title": "Нарисуй очередь к доктору", "needs_review": true, "html": "<p>Твоё творческое задание — нарисовать очередь к доктору в больнице. Постарайся нарисовать самых разных пациентов!</p><p>На уроке обязательно расскажи учителю о проблемах людей, которые ждут приёма.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание — ты МЕГА КРУТ!</h3><p>Жду тебя на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7);
end
$mig$;
