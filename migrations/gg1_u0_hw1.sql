-- Go Getter 1 · Unit 0 · Get started! · Homework 1
-- собрано tools/gg1_build.py --lesson u0_hw1
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 0 · Get started!', 0
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 0 · Get started!');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 0 · Get started!';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 1', 'homework',
         60, false, 0
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 1');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 1';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать! 👋</h2><p>Сегодня тебя ждёт много интересных упражнений!</p><p>В конце тебя будет ждать дополнительное задание. Если ты его сделаешь, получишь дополнительную звёздочку! ⭐</p><p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u0/card_greetings.webp\" alt=\"Greetings & Introductions\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Для начала посмотри видео! Обязательно повторяй буквы из видео, постарайся запомнить — так ты быстрее выучишь алфавит!", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"title": "Супер! А теперь помоги растерявшимся буковкам найти продолжения, чтобы получились слова — у тебя получится!", "pairs": [{"left": "c", "right": "upcake"}, {"left": "m", "right": "usic"}, {"left": "s", "right": "port"}, {"left": "a", "right": "pple"}, {"left": "h", "right": "obby"}, {"left": "n", "right": "ame"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'sequence', replace($blk${"title": "Отлично, а теперь задание посложнее. Мы только что составили слова — расставь их в алфавитном порядке ;)", "items": [{"text": "apple", "audio_tts": "apple"}, {"text": "cupcake", "audio_tts": "cupcake"}, {"text": "hobby", "audio_tts": "hobby"}, {"text": "music", "audio_tts": "music"}, {"text": "name", "audio_tts": "name"}, {"text": "sport", "audio_tts": "sport"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"words": ["What's", "your", "name?"], "sentence": "What's your name?", "audio_tts": "What's your name?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["How", "old", "are", "you?"], "sentence": "How old are you?", "audio_tts": "How old are you?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["Where", "are", "you", "from?"], "sentence": "Where are you from?", "audio_tts": "Where are you from?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["What", "is", "your", "hobby?"], "sentence": "What is your hobby?", "audio_tts": "What is your hobby?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'speaking', replace($blk${"title": "Расскажи о себе 🎤", "html": "<p>Прекрасная работа! Запиши небольшой рассказ на английском о себе, воспользуйся шаблоном:</p><p><i>My name is…<br>I'm … years old.<br>I'm from…<br>My hobby is…</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'match', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Соедини вопросы с ответами ⭐", "pairs": [{"left": "What's your name?", "right": "My name's Tom."}, {"left": "How old are you?", "right": "I'm ten."}, {"left": "Where are you from?", "right": "I'm from Poland."}, {"left": "What is your hobby?", "right": "My hobby is football."}, {"left": "How do you spell that?", "right": "T-O-M."}, {"left": "Nice to meet you!", "right": "Nice to meet you too!"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"title": "Расставь в правильном порядке ⭐", "words": ["Hello!", "My", "name's", "Anna.", "Nice", "to", "meet", "you!"], "sentence": "Hello! My name's Anna. Nice to meet you!", "audio_tts": "Hello! My name's Anna. Nice to meet you!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание, ты замечательный ученик! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11);
end
$mig$;
