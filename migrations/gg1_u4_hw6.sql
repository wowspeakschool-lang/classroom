-- Go Getter 1 · Unit 4 · Look at me · Homework 6
-- собрано tools/gg1_build.py --lesson u4_hw6
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 4 · Look at me', 4
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 4 · Look at me');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 4 · Look at me';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Сегодня нас ждут приключения в стране Listening! Мы будем слушать, смотреть разные интересные видео и узнавать новые вещи!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>Наше первое задание — послушать и запомнить как можно больше о Дарле (Darla).</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'gaps', replace($blk${"title": "А теперь заполни пропуски нужным словом. Ты можешь прослушать аудио ещё раз", "mode": "type", "text": "1. Darla is from Dublin, __Ireland__.\n2. She's got a __long__ face.\n3. Her hair is red and __curly__.\n4. Darla gets good marks at school — she's __clever__.\n5. Her dog's got big brown __eyes__.\n6. He's got a funny __little__ face."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'video', replace($blk${"title": "What is she like?", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'task', replace($blk${"title": "What is she like?", "needs_review": true, "html": "<p>Посмотри видео и запиши как можно больше слов, которые помогут рассказать о характере.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'sort', replace($blk${"title": "Распредели слова по двум колонкам: Good или Bad", "groups": [{"name": "Good", "items": [{"text": "cheerful"}, {"text": "hardworking"}, {"text": "famous"}, {"text": "nice"}, {"text": "funny"}, {"text": "lovely"}, {"text": "helpful"}]}, {"name": "Bad", "items": [{"text": "rude"}, {"text": "lazy"}, {"text": "shy"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><b>Нам предстоит подготовиться к сложному заданию — мы будем рассказывать о нашем любимом герое. Прочитай текст и ответь на вопросы.</b></p><p><i>My favourite cartoon character is Minnie Mouse. She is a mouse and she can talk. I like Minnie because she is always nice to her friends. Minnie Mouse's best friends are Mickey Mouse, Pluto, Donald Duck and Goofy. Minnie likes to wear a bow in her hair, pretty dresses, white gloves and colourful shoes. Today, she has a pink bow in her hair. She is wearing a blue dress and pink shoes.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'task', replace($blk${"title": "Запиши свои ответы на вопросы", "needs_review": true, "html": "<ol><li>What can Minnie Mouse do?</li><li>What is she like?</li><li>What does she like to wear?</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'speaking', replace($blk${"title": "Мой любимый герой 🎤", "html": "<p>Мы уже умеем описывать любимых героев. Давай попробуем сделать это устно! Вспомни своего любимого героя и скажи о нём 3–4 предложения.</p><p><b>Tell me about your favourite cartoon character.</b></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Спасибо большое тебе за ответы! Ты молодец! 🎉</h3><p>До новых встреч!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9);
end
$mig$;
