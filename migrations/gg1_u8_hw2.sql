-- Go Getter 1 · Unit 8 · Sport and health · Homework 2
-- собрано tools/gg1_build.py --lesson u8_hw2
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 8 · Sport and health', 8
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 8 · Sport and health');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 8 · Sport and health';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Добро пожаловать на домашнее задание! Сегодня мы с тобой закрепим знания, полученные на уроке, и ты без проблем сможешь говорить о том, что тебе нравится или не нравится. В конце тебя будет ждать дополнительное упражнение — для самых смелых и самых сильных учеников 💪</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u8/card_like_ing.webp\" alt=\"love / like / hate + -ing\" style=\"max-width:100%\"></p><p><img src=\"@@MEDIA@@gg1/u8/card_object_pronouns.webp\" alt=\"Объектные местоимения\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'video', replace($blk${"title": "Макс и Хэмми рассказывают, как они сходили в поход! Повторяй вопросы и ответы за героями, чтобы хорошенько запомнить правила.", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Мы посмотрели видео и немного размялись, теперь пришло время практики! Впиши правильную форму слова", "mode": "type", "text": "1. This person loves (play) __playing__ the guitar.\n2. This person likes (make) __making__ cupcakes.\n3. This person hates (get up) __getting up__ early and (cook) __cooking__.\n4. This person likes (skateboard) __skateboarding__ and (climb) __climbing__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"title": "Отлично, двигаемся дальше! Теперь давай расставим слова в правильном порядке, чтобы получились предложения", "words": ["Lisa", "loves", "playing", "the", "guitar."], "sentence": "Lisa loves playing the guitar.", "audio_tts": "Lisa loves playing the guitar."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке, чтобы получилось предложение", "words": ["What", "does", "Monica", "like", "doing?"], "sentence": "What does Monica like doing?", "audio_tts": "What does Monica like doing?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке, чтобы получилось предложение", "words": ["Janet", "doesn't like", "getting", "up", "early."], "sentence": "Janet doesn't like getting up early.", "audio_tts": "Janet doesn't like getting up early."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке, чтобы получилось предложение", "words": ["Mark", "loves", "watching", "funny", "films."], "sentence": "Mark loves watching funny films.", "audio_tts": "Mark loves watching funny films."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке, чтобы получилось предложение", "words": ["Wendy", "likes", "sailing", "and", "windsurfing."], "sentence": "Wendy likes sailing and windsurfing.", "audio_tts": "Wendy likes sailing and windsurfing."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке, чтобы получилось предложение", "words": ["Does", "Tim", "like", "doing", "taekwondo?"], "sentence": "Does Tim like doing taekwondo?", "audio_tts": "Does Tim like doing taekwondo?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'gaps', replace($blk${"title": "Внимательно посмотри на смайлики — о чём они говорят? Вставь слова по смыслу так, чтобы они грамматически подходили в предложения. 😊😊 — love, 😊 — like, 😫 — don't like, 😫😫 — hate", "mode": "drag", "text": "1. We 😫😫 __hate__ rock climbing.\n2. My parents 😊 __like__ skiing.\n3. Ann 😫 __doesn't like__ playing football.\n4. My grandad 😊😊 __loves__ cooking.\n5. My friends 😫 __don't like__ getting up early.\n6. I 😊😊 __love__ cycling.\n7. Mark 😊 __likes__ playing basketball.\n8. My cat 😫😫 __hates__ getting wet."}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'gaps', replace($blk${"title": "Мы уже на финишной прямой! Внимательно посмотри на правило и заполни пропуски в предложениях", "mode": "type", "image": "@@MEDIA@@gg1/u8/card_object_pronouns.webp", "text": "1. Emma is nice. I like __her__.\n2. Skating is fun. I love __it__.\n3. You are great at football. I like watching __you__.\n4. Amy and Tom are my best friends. I like __them__.\n5. Tom is my baby brother. I love __him__.\n6. We're good at dancing. Watch __us__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'task', replace($blk${"title": "Что мне нравится ✍️", "needs_review": true, "html": "<p>Напиши 3 предложения о себе и 3 предложения о своём члене семьи, друге или даже учителе! Что тебе нравится, что тебе не нравится и что ты ненавидишь? И то же самое о другом человеке.</p><p>Посмотри, это мои предложения:</p><p><i>I like playing basketball. I don't like cleaning. I hate watching football. She likes playing tennis. She doesn't like cooking. She hates watching cartoons.</i></p><p>Обрати внимание на окончания глаголов, когда я рассказываю о своей подруге 😉</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'order', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Расставь слова в правильном порядке ⭐", "words": ["I", "love", "playing", "football."], "sentence": "I love playing football.", "audio_tts": "I love playing football."}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["She", "doesn't like", "cooking."], "sentence": "She doesn't like cooking.", "audio_tts": "She doesn't like cooking."}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["My", "brother", "hates", "getting", "up", "early."], "sentence": "My brother hates getting up early.", "audio_tts": "My brother hates getting up early."}$blk$, '@@MEDIA@@', v_media)::jsonb, 15),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["Do", "you", "like", "swimming?"], "sentence": "Do you like swimming?", "audio_tts": "Do you like swimming?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 16),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ⭐", "questions": [{"q": "I love ___ volleyball.", "type": "single", "options": [{"text": "playing"}, {"text": "plays"}, {"text": "play"}], "correct": [0]}, {"q": "My sister ___ cooking.", "type": "single", "options": [{"text": "liking"}, {"text": "likes"}, {"text": "like"}], "correct": [1]}, {"q": "We don't like ___ TV.", "type": "single", "options": [{"text": "watches"}, {"text": "watch"}, {"text": "watching"}], "correct": [2]}, {"q": "Ben is my friend. I like ___.", "type": "single", "options": [{"text": "him"}, {"text": "his"}, {"text": "he"}], "correct": [0]}, {"q": "Where are my keys? I can't see ___.", "type": "single", "options": [{"text": "they"}, {"text": "them"}, {"text": "their"}], "correct": [1]}, {"q": "Can you help ___, please?", "type": "single", "options": [{"text": "I"}, {"text": "my"}, {"text": "me"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 17),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 18);
end
$mig$;
