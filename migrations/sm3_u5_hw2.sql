-- Super Minds 3 · Unit 5 · Under the sea · Homework 2
-- собрано tools/sm3_build.py --lesson u5_hw2
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 5 · Under the sea', 5
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 5 · Under the sea');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 5 · Under the sea';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! Как здорово, что ты решил сделать домашнюю работу!</h2><p>Она будет небольшая и интересная. Вперёд!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Видео: was / were", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'order', replace($blk${"image": "@@MEDIA@@sm3/u5/place_restaurant.webp", "words": ["He", "was", "at", "the", "restaurant", "yesterday."], "sentence": "He was at the restaurant yesterday.", "audio_tts": "He was at the restaurant yesterday."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"image": "@@MEDIA@@sm3/u5/place_museum.webp", "words": ["They", "weren’t", "in", "the", "museum", "last", "week."], "sentence": "They weren’t in the museum last week.", "audio_tts": "They weren't in the museum last week."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"image": "@@MEDIA@@sm3/u5/place_park.webp", "words": ["She", "wasn’t", "in", "the", "park", "last", "weekend."], "sentence": "She wasn’t in the park last weekend.", "audio_tts": "She wasn't in the park last weekend."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"image": "@@MEDIA@@sm3/u5/place_hospital.webp", "words": ["The", "dog", "was", "in", "hospital", "yesterday."], "sentence": "The dog was in hospital yesterday.", "audio_tts": "The dog was in hospital yesterday."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"image": "@@MEDIA@@sm3/u5/place_supermarket.webp", "words": ["They", "were", "in", "the", "supermarket", "two", "days", "ago."], "sentence": "They were in the supermarket two days ago.", "audio_tts": "They were in the supermarket two days ago."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ответа", "questions": [{"q": "1. She ___ at school yesterday.", "type": "single", "options": [{"text": "was"}, {"text": "were"}], "correct": [0]}, {"q": "2. They ___ at the restaurant, they were at the café.", "type": "single", "options": [{"text": "weren’t"}, {"text": "were"}, {"text": "was"}, {"text": "wasn’t"}], "correct": [0]}, {"q": "3. Mathew was sick yesterday, so he ___ in the hospital.", "type": "single", "options": [{"text": "was"}, {"text": "were"}, {"text": "wasn’t"}, {"text": "weren’t"}], "correct": [0]}, {"q": "4. Maria and Peter ___ at the cinema yesterday, they liked the film!", "type": "single", "options": [{"text": "were"}, {"text": "weren’t"}, {"text": "was"}, {"text": "wasn’t"}], "correct": [0]}, {"q": "5. There ___ cats in the box next to the supermarket, they were very cold!", "type": "single", "options": [{"text": "were"}, {"text": "was"}], "correct": [0]}, {"q": "6. I ___ at school yesterday, it was Sunday!", "type": "single", "options": [{"text": "wasn’t"}, {"text": "was"}, {"text": "were"}, {"text": "weren’t"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/good_luck_clover.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа! Самое время отдохнуть :)</h3><p>А потом — вторая половина задания. Готов? Давай начинать!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши was, wasn’t, were или weren’t так, чтобы получился связный текст", "text": "Yesterday __was__ a busy day! We __were__ in the park in the morning. There __was__ a football match, but there __weren’t__ many goals. Only one! In the afternoon we __were__ at my cousin’s house. There __were__ cheese sandwiches, but there __wasn’t__ any cake this time. In the evening we __were__ at the cinema for that new film about life under the sea. It __was__ interesting! We all __were__ very tired at the end of the day."}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'task', replace($blk${"title": "Перепиши предложения в прошедшем времени, используя was или were", "needs_review": true, "html": "<p>1. There is a small shark too.<br>2. I’m scared!<br>3. We’re at the beach.<br>4. There are dolphins, seals and turtles in the sea.<br>5. It’s hot.<br>6. I’m in the sea in my new swimsuit.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'task', replace($blk${"title": "Напиши, где ты был(а) в каждый из дней недели", "needs_review": true, "html": "<p><i>Например:<br>On Monday I was at the swimming pool.<br>On Tuesday I was in the supermarket.</i></p><p>Прояви фантазию — предложения можно просто придумать.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты отлично потрудился!</h3><p>Спасибо тебе большое. Увидимся на уроке :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12);
end
$mig$;
