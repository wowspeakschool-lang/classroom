-- Super Minds 1 · Unit 5 · My week · Homework 7
-- собрано tools/sm1_build.py --lesson u5_hw7
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
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! Как здорово, что ты решил сделать домашнее задание!</h2><p>Это повторение перед тестом — давай вспомним всё!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'match', replace($blk${"title": "Вспомни дни недели: соедини слово с переводом", "pairs": [{"left": "Monday", "right": "понедельник", "left_audio_tts": "Monday"}, {"left": "Tuesday", "right": "вторник", "left_audio_tts": "Tuesday"}, {"left": "Wednesday", "right": "среда", "left_audio_tts": "Wednesday"}, {"left": "Thursday", "right": "четверг", "left_audio_tts": "Thursday"}, {"left": "Friday", "right": "пятница", "left_audio_tts": "Friday"}, {"left": "Saturday", "right": "суббота", "left_audio_tts": "Saturday"}, {"left": "Sunday", "right": "воскресенье", "left_audio_tts": "Sunday"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'sort', replace($blk${"title": "Раздели занятия на 2 группы: PLAY или GO", "groups": [{"name": "PLAY", "items": [{"text": "football", "audio_tts": "football"}, {"text": "tennis", "audio_tts": "tennis"}, {"text": "board games", "audio_tts": "board games"}]}, {"name": "GO", "items": [{"text": "swimming", "audio_tts": "swimming"}, {"text": "skiing", "audio_tts": "skiing"}, {"text": "surfing", "audio_tts": "surfing"}, {"text": "climbing", "audio_tts": "climbing"}, {"text": "running", "audio_tts": "running"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши нужный день недели", "mode": "type", "text": "1. I play football on __Monday__. (понедельник)\n2. I go swimming on __Wednesday__. (среда)\n3. I ride my bike on __Friday__. (пятница)\n4. I watch TV on __Saturday__. (суббота)\n5. I play tennis on __Thursday__. (четверг)"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай вопрос и выбери ответ. Смайлик поможет тебе догадаться, да или нет.", "questions": [{"q": "Do you play football at the weekend? 😊", "type": "single", "options": [{"text": "Yes, I do."}, {"text": "Yes, I am."}, {"text": "Yes, I like."}], "correct": [0]}, {"q": "Do you ride your bike on Mondays? 😊", "type": "single", "options": [{"text": "No, I not."}, {"text": "Yes, I doing."}, {"text": "Yes, I do."}], "correct": [2]}, {"q": "Do you watch TV at the weekend? 😞", "type": "single", "options": [{"text": "Yes, I don’t."}, {"text": "No, I don’t."}, {"text": "No, I do."}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["I", "play", "football", "on", "Mondays."], "sentence": "I play football on Mondays.", "audio_tts": "I play football on Mondays."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Do", "you", "play", "tennis", "at", "the weekend?"], "sentence": "Do you play tennis at the weekend?", "audio_tts": "Do you play tennis at the weekend?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'speaking', replace($blk${"title": "Расскажи про свою неделю 🎤", "html": "<p>Запиши рассказ о своей неделе — минимум 5 предложений! Нажми на микрофон и расскажи про свою неделю.</p><p><b>Пример:</b> <i>I play football on Mondays. I go swimming on Wednesdays.</i></p>", "sample_tts": "I play football on Mondays. I go swimming on Wednesdays.", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<h3>Ты выполнил все задания из основной части!</h3><p>А это дополнительное задание — для настоящих чемпионов! 🏆</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'exact_input', replace($blk${"items": [{"prompt": "Составь слово из букв: d · a · y · M · o · n", "accept": ["Monday"], "audio_tts": "Monday"}, {"prompt": "Составь слово из букв: s · d · u · e · y · T · a", "accept": ["Tuesday"], "audio_tts": "Tuesday"}, {"prompt": "Составь слово из букв: n · e · s · W · d · a · y · d · e", "accept": ["Wednesday"], "audio_tts": "Wednesday"}, {"prompt": "Составь слово из букв: r · s · h · u · d · a · y · T", "accept": ["Thursday"], "audio_tts": "Thursday"}, {"prompt": "Составь слово из букв: i · d · r · F · y · a", "accept": ["Friday"], "audio_tts": "Friday"}, {"prompt": "Составь слово из букв: t · u · r · a · S · d · a · y", "accept": ["Saturday"], "audio_tts": "Saturday"}, {"prompt": "Составь слово из букв: n · u · d · S · y · a", "accept": ["Sunday"], "audio_tts": "Sunday"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'gaps', replace($blk${"title": "Перетащи слова в пропуски", "mode": "drag", "text": "Hi! I’m Sue. On __Mondays__ I go __swimming__. On Tuesdays I __play__ football. On Wednesdays I __ride__ my bike. On Saturdays I __watch__ TV. Do you play the piano at the __weekend__?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Молодец! Ты готов к тесту!</h3><p>До встречи на уроке.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11);
end
$mig$;
