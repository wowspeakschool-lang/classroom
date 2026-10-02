-- Super Minds 3 · Unit 2 · Food · Homework 3
-- собрано tools/sm3_build.py --lesson u2_hw3
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 2 · Food', 2
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 2 · Food');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 2 · Food';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет, самый лучший ученик!</h2><p>Готов к новой домашней работе? Давай начинать!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Посмотри видео и найди ответ на вопрос: What time is it?", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p>Посмотри видео <b>два раза</b>:</p><ol><li>Первый раз просто послушай.</li><li>Во второй раз повторяй все предложения за нашими ящерицами 🦎</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "What time is it?", "type": "single", "options": [{"text": "it’s seven o’clock"}, {"text": "it’s twelve o’clock"}, {"text": "it’s six o’clock"}, {"text": "it’s nine o’clock"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Вспомни, что говорили ящерицы, и вставь нужные слова", "mode": "drag", "text": "__How about__ some peas?\n__Shall we__ have some bread with cheese?\n__I’d like__ some flies."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "Прочитай диалог и вставь нужные слова", "mode": "drag", "text": "Jack: __Shall__ we make a sandwich for lunch?\nSara: __Good__ idea.\nJack: How __about__ a chicken sandwich?\nSara: __OK__.\nJack: Shall we __have__ some salad with it?\nSara: Yes, please! I like chicken with salad."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'sequence', replace($blk${"title": "Составь диалог — расставь реплики по порядку", "items": [{"text": "Shall we make a pizza?"}, {"text": "Good idea! How about an onion and carrot one?"}, {"text": "Yuk! How about cheese and tomato?"}, {"text": "OK."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'sequence', replace($blk${"title": "И ещё один диалог", "items": [{"text": "Shall we have sandwiches for lunch?"}, {"text": "OK. How about sausage sandwiches?"}, {"text": "Great idea. Oh no! There aren’t any sausages in the fridge."}, {"text": "How about egg sandwiches, then?"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'sequence', replace($blk${"title": "И последний", "items": [{"text": "I’m thirsty. Can I have a drink, please?"}, {"text": "Yes, of course. How about lemonade?"}, {"text": "Sorry. I don’t like that."}, {"text": "That’s OK. How about apple juice?"}, {"text": "Yes, please. I like juice."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'speaking', replace($blk${"title": "Поддержи диалог 🎤", "needs_review": true, "html": "<p>Посмотри видео и поддержи разговор:</p><ul><li>согласись на идею поесть суп;</li><li>вырази сожаление, что нет томатов;</li><li>согласись поесть другой суп.</li></ul>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа!</h3><p>Большое тебе спасибо за твой труд :) Ты отлично постарался. До встречи на уроке 😊</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
