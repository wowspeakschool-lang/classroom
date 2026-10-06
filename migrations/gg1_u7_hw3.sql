-- Go Getter 1 · Unit 7 · Animals · Homework 3
-- собрано tools/gg1_build.py --lesson u7_hw3
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 7 · Animals', 7
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 7 · Animals');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 7 · Animals';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Сегодня мы с тобой закрепим знания, полученные на уроке, и ты без проблем сможешь задавать вопросы в Present Simple. В конце тебя будет ждать дополнительное упражнение — для самых смелых и самых сильных учеников 💪</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u7/card_ps_questions.webp\" alt=\"Present Simple — Questions\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p>Ребята рассказывают, как они обычно проводят выходные. Попробуй угадать: <b>What has Hammy got in his hands?</b> Посмотри видео и проверь, угадал ли ты. Повторяй вопросы и ответы за героями, чтобы хорошенько запомнить правила.</p><p><img src=\"@@MEDIA@@gg1/u7/hammy.webp\" alt=\"Hammy\" style=\"height:200px\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'video', replace($blk${"title": "What has Hammy got in his hands?", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Настало время практики! Внимательно прочитай предложения и выбери правильный вариант. Удачи!", "questions": [{"q": "___ you know Mari?", "type": "single", "options": [{"text": "Do"}, {"text": "Does"}], "correct": [0]}, {"q": "___ Tom live in a house with a garden?", "type": "single", "options": [{"text": "Do"}, {"text": "Does"}], "correct": [1]}, {"q": "___ your friends speak English?", "type": "single", "options": [{"text": "Do"}, {"text": "Does"}], "correct": [0]}, {"q": "___ your mum make nice cakes?", "type": "single", "options": [{"text": "Do"}, {"text": "Does"}], "correct": [1]}, {"q": "___ I sing well?", "type": "single", "options": [{"text": "Do"}, {"text": "Does"}], "correct": [0]}, {"q": "___ you and your sister like cats?", "type": "single", "options": [{"text": "Does"}, {"text": "Do"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'match', replace($blk${"title": "Все вопросы и ответы растерялись… Помоги им найти друг друга! Читай внимательно ;)", "pairs": [{"left": "Do you know Mari?", "right": "Yes, I do."}, {"left": "Does Tom live in a house with a garden?", "right": "Yes, he does."}, {"left": "Do your friends speak English?", "right": "No, they don't."}, {"left": "Does your mum make nice cakes?", "right": "Yes, she does."}, {"left": "Do I sing well?", "right": "No, you don't."}, {"left": "Do you and your sister like cats?", "right": "Yes, we do."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Ты уже на финишной прямой! Расставь слова в правильном порядке так, чтобы получился вопрос. Главное, не торопись ;)", "words": ["Do", "you", "speak", "Chinese?"], "sentence": "Do you speak Chinese?", "audio_tts": "Do you speak Chinese?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова так, чтобы получился вопрос", "words": ["Do", "you", "like", "chocolate?"], "sentence": "Do you like chocolate?", "audio_tts": "Do you like chocolate?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова так, чтобы получился вопрос", "words": ["Do", "your", "friends", "play", "football", "on", "Saturdays?"], "sentence": "Do your friends play football on Saturdays?", "audio_tts": "Do your friends play football on Saturdays?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова так, чтобы получился вопрос", "words": ["Do", "you", "tidy", "your", "room", "at", "the", "weekend?"], "sentence": "Do you tidy your room at the weekend?", "audio_tts": "Do you tidy your room at the weekend?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова так, чтобы получился вопрос", "words": ["Does", "your", "dad", "go", "to", "the", "gym?"], "sentence": "Does your dad go to the gym?", "audio_tts": "Does your dad go to the gym?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'task', replace($blk${"title": "Интервью с другом 🎙️", "needs_review": true, "html": "<p>Представь, что тебе нужно взять интервью у своего лучшего друга или подруги. Какие вопросы ты бы придумал(а)? Напиши как минимум 3 вопроса (но чем больше, тем лучше). Удачи, у тебя всё получится!</p><p><i>Посмотри, это мои вопросы: Do you sing well? Do you speak any foreign languages? Does your best friend like playing with you?</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'match', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Соедини вопросы про животных с ответами ⭐", "pairs": [{"left": "Do birds fly?", "right": "Yes, they do."}, {"left": "Does a whale walk?", "right": "No, it doesn't."}, {"left": "Does a monkey climb trees?", "right": "Yes, it does."}, {"left": "Do snakes have legs?", "right": "No, they don't."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["Does", "a", "frog", "jump?"], "sentence": "Does a frog jump?", "audio_tts": "Does a frog jump?", "image": "@@MEDIA@@gg1/u7/animal_frog.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["Do", "lions", "sleep", "all", "day?"], "sentence": "Do lions sleep all day?", "audio_tts": "Do lions sleep all day?", "image": "@@MEDIA@@gg1/u7/animal_lion.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["Does", "your", "cat", "like", "fish?"], "sentence": "Does your cat like fish?", "audio_tts": "Does your cat like fish?", "image": "@@MEDIA@@gg1/u7/animal_cat.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 15),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 16);
end
$mig$;
