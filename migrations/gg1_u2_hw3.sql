-- Go Getter 1 · Unit 2 · My things · Homework 3
-- собрано tools/gg1_build.py --lesson u2_hw3
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 2 · My things', 2
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 2 · My things');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 2 · My things';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>На занятии мы учились задавать вопросы! Потренируемся ещё?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u2/card_questions_be.webp\" alt=\"Вопросы с to be\" style=\"max-width:100%\"></p><p><img src=\"@@MEDIA@@gg1/u2/card_short_answers.webp\" alt=\"Short answers\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Поставь в конце предложения правильный знак: ? или .", "questions": [{"q": "Is he French ___", "type": "single", "options": [{"text": "?"}, {"text": "."}], "correct": [0]}, {"q": "My brother is eight years old ___", "type": "single", "options": [{"text": "?"}, {"text": "."}], "correct": [1]}, {"q": "Are you a student ___", "type": "single", "options": [{"text": "?"}, {"text": "."}], "correct": [0]}, {"q": "Is Lee your friend ___", "type": "single", "options": [{"text": "."}, {"text": "?"}], "correct": [1]}, {"q": "I'm cool ___", "type": "single", "options": [{"text": "."}, {"text": "?"}], "correct": [0]}, {"q": "Are they happy ___", "type": "single", "options": [{"text": "."}, {"text": "?"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"html": "<p><b>Посмотри на картинку: это Даг и Кит.</b></p><p><img src=\"@@MEDIA@@gg1/u2/comic_kit_dug.webp\" alt=\"Kit and Dug\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'match', replace($blk${"title": "Посмотри на картинку и ответь на вопросы", "pairs": [{"left": "Is Kit a cat?", "right": "Yes, she is."}, {"left": "Is she black?", "right": "No, she isn't."}, {"left": "Are Kit and Dug friends?", "right": "Yes, they are."}, {"left": "Is Dug's suit blue and red?", "right": "Yes, it is."}, {"left": "Are they at school?", "right": "No, they aren't."}, {"left": "Is his suit too small?", "right": "No, it isn't."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"title": "Составь вопрос", "words": ["What", "is", "your", "name?"], "sentence": "What is your name?", "audio_tts": "What is your name?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Составь вопрос", "words": ["Are", "you", "eleven?"], "sentence": "Are you eleven?", "audio_tts": "Are you eleven?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Составь вопрос", "words": ["Is", "your", "best", "friend", "ten?"], "sentence": "Is your best friend ten?", "audio_tts": "Is your best friend ten?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'speaking', replace($blk${"title": "В магазине 🎤", "html": "<p>Представь, что ты в магазине. Задай вопросы про одежду и ответь на них.</p><p><i>Пример: Is this jacket new? — Yes, it is. Are these shoes too big? — No, they aren't. Is the dress too small? — Yes, it is.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'match', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Соедини вопросы с ответами ⭐", "pairs": [{"left": "Are you a student?", "right": "Yes, I am."}, {"left": "Is she your sister?", "right": "No, she isn't."}, {"left": "Are they OK?", "right": "Yes, they are."}, {"left": "Is it your bag?", "right": "Yes, it is."}, {"left": "Is he French?", "right": "No, he isn't."}, {"left": "Are we late?", "right": "No, we aren't."}, {"left": "Am I right?", "right": "Yes, you are."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["Is", "this", "jacket", "new?"], "sentence": "Is this jacket new?", "audio_tts": "Is this jacket new?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["Are", "these", "your", "shoes?"], "sentence": "Are these your shoes?", "audio_tts": "Are these your shoes?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа! 🎉</h3><p>Увидимся на занятии! Bye!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12);
end
$mig$;
