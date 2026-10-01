-- Super Minds 3 · Unit 1 · School · Homework 1
-- собрано tools/sm3_build.py --lesson u1_hw1
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 1 · School', 1
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 1 · School');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 1 · School';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 1', 'homework',
         60, false, 0
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 1');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 1';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>Сегодня мы повторим названия школьных предметов и дни недели.</p><p>Сначала выучим слова, потом разберёмся с расписанием. Поехали!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'flashcards', replace($blk${"cards": [{"text": "English", "translation": "английский", "audio_tts": "English", "image": "@@MEDIA@@sm3/u1/subj_english.webp"}, {"text": "Maths", "translation": "математика", "audio_tts": "Maths", "image": "@@MEDIA@@sm3/u1/subj_maths.webp"}, {"text": "Geography", "translation": "география", "audio_tts": "Geography", "image": "@@MEDIA@@sm3/u1/subj_geography.webp"}, {"text": "I.T.", "translation": "информационные технологии", "audio_tts": "I.T.", "image": "@@MEDIA@@sm3/u1/subj_it.webp"}, {"text": "Music", "translation": "музыка", "audio_tts": "Music", "image": "@@MEDIA@@sm3/u1/subj_music.webp"}, {"text": "Science", "translation": "наука", "audio_tts": "Science", "image": "@@MEDIA@@sm3/u1/subj_science.webp"}, {"text": "Art", "translation": "изобразительное искусство", "audio_tts": "Art", "image": "@@MEDIA@@sm3/u1/subj_art.webp"}, {"text": "P.E.", "translation": "физкультура", "audio_tts": "P.E.", "image": "@@MEDIA@@sm3/u1/subj_pe.webp"}, {"text": "History", "translation": "история", "audio_tts": "History", "image": "@@MEDIA@@sm3/u1/subj_history.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"pairs": [{"left_image": "@@MEDIA@@sm3/u1/subj_english.webp", "right": "English", "right_audio_tts": "English"}, {"left_image": "@@MEDIA@@sm3/u1/subj_maths.webp", "right": "Maths", "right_audio_tts": "Maths"}, {"left_image": "@@MEDIA@@sm3/u1/subj_geography.webp", "right": "Geography", "right_audio_tts": "Geography"}, {"left_image": "@@MEDIA@@sm3/u1/subj_it.webp", "right": "I.T.", "right_audio_tts": "I.T."}, {"left_image": "@@MEDIA@@sm3/u1/subj_music.webp", "right": "Music", "right_audio_tts": "Music"}, {"left_image": "@@MEDIA@@sm3/u1/subj_science.webp", "right": "Science", "right_audio_tts": "Science"}, {"left_image": "@@MEDIA@@sm3/u1/subj_art.webp", "right": "Art", "right_audio_tts": "Art"}, {"left_image": "@@MEDIA@@sm3/u1/subj_pe.webp", "right": "P.E.", "right_audio_tts": "P.E."}, {"left_image": "@@MEDIA@@sm3/u1/subj_history.webp", "right": "History", "right_audio_tts": "History"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Как по-английски «английский»?", "type": "single", "options": [{"text": "English"}, {"text": "Geography"}, {"text": "I.T."}, {"text": "Maths"}], "correct": [0]}, {"q": "Как по-английски «математика»?", "type": "single", "options": [{"text": "Geography"}, {"text": "I.T."}, {"text": "Maths"}, {"text": "Music"}], "correct": [2]}, {"q": "Как по-английски «география»?", "type": "single", "options": [{"text": "Geography"}, {"text": "I.T."}, {"text": "Music"}, {"text": "Science"}], "correct": [0]}, {"q": "Как по-английски «информационные технологии»?", "type": "single", "options": [{"text": "Art"}, {"text": "I.T."}, {"text": "Music"}, {"text": "Science"}], "correct": [1]}, {"q": "Как по-английски «музыка»?", "type": "single", "options": [{"text": "Art"}, {"text": "Music"}, {"text": "P.E."}, {"text": "Science"}], "correct": [1]}, {"q": "Как по-английски «наука»?", "type": "single", "options": [{"text": "Art"}, {"text": "History"}, {"text": "P.E."}, {"text": "Science"}], "correct": [3]}, {"q": "Как по-английски «изобразительное искусство»?", "type": "single", "options": [{"text": "Art"}, {"text": "English"}, {"text": "History"}, {"text": "P.E."}], "correct": [0]}, {"q": "Как по-английски «физкультура»?", "type": "single", "options": [{"text": "English"}, {"text": "History"}, {"text": "Maths"}, {"text": "P.E."}], "correct": [3]}, {"q": "Как по-английски «история»?", "type": "single", "options": [{"text": "English"}, {"text": "Geography"}, {"text": "History"}, {"text": "Maths"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'exact_input', replace($blk${"items": [{"prompt": "Напиши по-английски: английский", "accept": ["English", "english"], "audio_tts": "English"}, {"prompt": "Напиши по-английски: математика", "accept": ["Maths", "maths"], "audio_tts": "Maths"}, {"prompt": "Напиши по-английски: география", "accept": ["Geography", "geography"], "audio_tts": "Geography"}, {"prompt": "Напиши по-английски: информационные технологии", "accept": ["I.T.", "i.t."], "audio_tts": "I.T."}, {"prompt": "Напиши по-английски: музыка", "accept": ["Music", "music"], "audio_tts": "Music"}, {"prompt": "Напиши по-английски: наука", "accept": ["Science", "science"], "audio_tts": "Science"}, {"prompt": "Напиши по-английски: изобразительное искусство", "accept": ["Art", "art"], "audio_tts": "Art"}, {"prompt": "Напиши по-английски: физкультура", "accept": ["P.E.", "p.e."], "audio_tts": "P.E."}, {"prompt": "Напиши по-английски: история", "accept": ["History", "history"], "audio_tts": "History"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<h3>Расписание на неделю</h3><p>Внимательно изучи расписание. Столбцы — это дни недели, слева направо: понедельник, вторник, среда, четверг, пятница. Поднос с обедом делит день на уроки <b>до обеда</b> и <b>после обеда</b>.</p><p><img src=\"@@MEDIA@@sm3/u1/scene_timetable.webp\" alt=\"Timetable\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'gaps', replace($blk${"title": "Определи, какой день описан, и впиши его название", "mode": "type", "text": "1. This is what I've got today. P.E., English and Music before lunch. I.T. and History after lunch. Today is __Wednesday__.\n2. This is what I've got today. Science, Art and English before lunch. Maths and Geography after lunch. Today is __Friday__.\n3. This is what I've got today. Maths, English and Geography before lunch. Music and History after lunch. Today is __Monday__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["When", "have", "you", "got", "English?", "On", "Mondays."], "sentence": "When have you got English? On Mondays.", "audio_tts": "When have you got English? On Mondays."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'speaking', replace($blk${"title": "Расскажи про свой любимый предмет 🎤", "html": "<p>Нажми на микрофон и расскажи, какой предмет тебе нравится и когда он у тебя.</p><p><i>Например: I like Art. I've got Art on Tuesdays.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа! 🎉</h3><p>До встречи на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9);
end
$mig$;
