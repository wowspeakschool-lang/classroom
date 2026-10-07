-- Super Minds 1 · Unit 8 · My body · Homework 6
-- собрано tools/sm1_build.py --lesson u8_hw6
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
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание! 👋</h2><p>Сегодня мы выучим слова-движения: вперёд, назад, вбок, шаг, тянуться и прыжок. Вставай — будем двигаться вместе!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'flashcards', replace($blk${"title": "Запомни слова", "cards": [{"text": "forwards", "translation": "вперёд", "audio_tts": "forwards", "image": "@@MEDIA@@sm1/u8/move_forwards.webp"}, {"text": "backwards", "translation": "назад", "audio_tts": "backwards", "image": "@@MEDIA@@sm1/u8/move_backwards.webp"}, {"text": "stretch", "translation": "тянуться", "audio_tts": "stretch", "image": "@@MEDIA@@sm1/u8/move_stretch.webp"}, {"text": "sideways", "translation": "вбок", "audio_tts": "sideways", "image": "@@MEDIA@@sm1/u8/move_sideways.webp"}, {"text": "step", "translation": "шаг", "audio_tts": "step", "image": "@@MEDIA@@sm1/u8/move_step.webp"}, {"text": "jump", "translation": "прыжок", "audio_tts": "jump", "image": "@@MEDIA@@sm1/u8/move_jump.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Послушай слово и выбери его", "type": "single", "audio_tts": "forwards", "options": [{"text": "forwards"}, {"text": "backwards"}, {"text": "stretch"}, {"text": "sideways"}], "correct": [0]}, {"q": "Послушай слово и выбери его", "type": "single", "audio_tts": "backwards", "options": [{"text": "stretch"}, {"text": "backwards"}, {"text": "sideways"}, {"text": "step"}], "correct": [1]}, {"q": "Послушай слово и выбери его", "type": "single", "audio_tts": "stretch", "options": [{"text": "sideways"}, {"text": "step"}, {"text": "stretch"}, {"text": "jump"}], "correct": [2]}, {"q": "Послушай слово и выбери его", "type": "single", "audio_tts": "sideways", "options": [{"text": "step"}, {"text": "jump"}, {"text": "forwards"}, {"text": "sideways"}], "correct": [3]}, {"q": "Послушай слово и выбери его", "type": "single", "audio_tts": "step", "options": [{"text": "step"}, {"text": "jump"}, {"text": "forwards"}, {"text": "backwards"}], "correct": [0]}, {"q": "Послушай слово и выбери его", "type": "single", "audio_tts": "jump", "options": [{"text": "forwards"}, {"text": "jump"}, {"text": "backwards"}, {"text": "stretch"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'match', replace($blk${"title": "Найди пару: соедини картинку и слово", "pairs": [{"left_image": "@@MEDIA@@sm1/u8/move_forwards.webp", "right": "forwards", "right_audio_tts": "forwards"}, {"left_image": "@@MEDIA@@sm1/u8/move_backwards.webp", "right": "backwards", "right_audio_tts": "backwards"}, {"left_image": "@@MEDIA@@sm1/u8/move_stretch.webp", "right": "stretch", "right_audio_tts": "stretch"}, {"left_image": "@@MEDIA@@sm1/u8/move_sideways.webp", "right": "sideways", "right_audio_tts": "sideways"}, {"left_image": "@@MEDIA@@sm1/u8/move_step.webp", "right": "step", "right_audio_tts": "step"}, {"left_image": "@@MEDIA@@sm1/u8/move_jump.webp", "right": "jump", "right_audio_tts": "jump"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'exact_input', replace($blk${"items": [{"prompt": "Собери слово из букв: w a r d s o f r (вперёд)", "accept": ["forwards", "Forwards"], "audio_tts": "forwards"}, {"prompt": "Собери слово из букв: s k b a w r d a c (назад)", "accept": ["backwards", "Backwards"], "audio_tts": "backwards"}, {"prompt": "Собери слово из букв: t c h e r s t (тянуться)", "accept": ["stretch", "Stretch"], "audio_tts": "stretch"}, {"prompt": "Собери слово из букв: y s w a s i d e (вбок)", "accept": ["sideways", "Sideways"], "audio_tts": "sideways"}, {"prompt": "Собери слово из букв: p e t s (шаг)", "accept": ["step", "Step"], "audio_tts": "step"}, {"prompt": "Собери слово из букв: m u p j (прыжок)", "accept": ["jump", "Jump"], "audio_tts": "jump"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'exact_input', replace($blk${"items": [{"prompt": "Напиши по-английски: вперёд", "accept": ["forwards", "Forwards"], "image": "@@MEDIA@@sm1/u8/move_forwards.webp", "audio_tts": "forwards"}, {"prompt": "Напиши по-английски: назад", "accept": ["backwards", "Backwards"], "image": "@@MEDIA@@sm1/u8/move_backwards.webp", "audio_tts": "backwards"}, {"prompt": "Напиши по-английски: тянуться", "accept": ["stretch", "Stretch"], "image": "@@MEDIA@@sm1/u8/move_stretch.webp", "audio_tts": "stretch"}, {"prompt": "Напиши по-английски: вбок", "accept": ["sideways", "Sideways"], "image": "@@MEDIA@@sm1/u8/move_sideways.webp", "audio_tts": "sideways"}, {"prompt": "Напиши по-английски: шаг", "accept": ["step", "Step"], "image": "@@MEDIA@@sm1/u8/move_step.webp", "audio_tts": "step"}, {"prompt": "Напиши по-английски: прыжок", "accept": ["jump", "Jump"], "image": "@@MEDIA@@sm1/u8/move_jump.webp", "audio_tts": "jump"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа! Слова выучены 🎉</h3><p>Давай продолжим — впереди ещё несколько заданий!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p><p><img src=\"@@MEDIA@@sm1/u8/vocab_moves.webp\" alt=\"Vocabulary 2 — Movements\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'match', replace($blk${"title": "Соедини описание с картинкой", "pairs": [{"left_image": "@@MEDIA@@sm1/u8/move_he_stretches_forwards.webp", "right": "He stretches forwards.", "right_audio_tts": "He stretches forwards."}, {"left_image": "@@MEDIA@@sm1/u8/move_she_jumps_forwards.webp", "right": "She jumps forwards.", "right_audio_tts": "She jumps forwards."}, {"left_image": "@@MEDIA@@sm1/u8/move_she_stretches_sideways.webp", "right": "She stretches sideways.", "right_audio_tts": "She stretches sideways."}, {"left_image": "@@MEDIA@@sm1/u8/move_she_jumps_backwards.webp", "right": "She jumps backwards.", "right_audio_tts": "She jumps backwards."}, {"left_image": "@@MEDIA@@sm1/u8/move_he_runs_sideways.webp", "right": "He runs sideways.", "right_audio_tts": "He runs sideways."}, {"left_image": "@@MEDIA@@sm1/u8/move_she_steps_forwards.webp", "right": "She steps forwards.", "right_audio_tts": "She steps forwards."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'speaking', replace($blk${"title": "Что ты умеешь делать? 🎤", "html": "<p>Нажми на микрофон и расскажи, что ты умеешь делать. Используй движения из предыдущего задания.</p><p><b>Пример:</b> <i>I can jump backwards.</i></p>", "sample": "", "sample_tts": "I can jump backwards.", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа! 🎉</h3><p>Увидимся на занятии! :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
