-- Super Minds 1 · Unit 9 · Holidays · Homework 3
-- собрано tools/sm1_build.py --lesson u9_hw3
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 9 · Holidays', 9
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 9 · Holidays');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 9 · Holidays';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>Впереди тебя ждут видео и увлекательные упражнения, а также одно дополнительное задание, которое можно выполнить по желанию.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай начнём с видео. Но прежде чем смотреть, как думаешь, <b>где спрятался котик (cat)?</b></p><p>Теперь посмотри видео один раз, внимательно слушай, что говорит персонаж, и проверь себя — угадал ли ты?</p><p>Затем посмотри видео снова и повторяй за персонажами.</p><p><img src=\"@@MEDIA@@sm1/u9/hw3_cat.webp\" alt=\"Котик\" style=\"max-width:260px\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'video', replace($blk${"title": "Видео: где котик?", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'match', replace($blk${"title": "Посмотри видео ещё раз. Соедини вопросы и ответы.", "pairs": [{"left": "Where are the candies?", "right": "They’re in the jar.", "right_audio_tts": "They're in the jar."}, {"left": "Where’s the rabbit?", "right": "It’s in the hat.", "right_audio_tts": "It's in the hat."}, {"left": "Where’s the cat?", "right": "It’s under the table.", "right_audio_tts": "It's under the table."}, {"left": "Where are the books?", "right": "They’re in the bag.", "right_audio_tts": "They're in the bag."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p>А теперь посмотри на картинку и соедини вопросы с ответами в следующем задании.</p><p><img src=\"@@MEDIA@@sm1/u9/hw3_where_photos.webp\" alt=\"Книга, ракушки, гитара, рыбы\" style=\"max-width:560px\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'match', replace($blk${"title": "Соедини вопросы с ответами", "pairs": [{"left": "Where are the shells?", "right": "They’re in the box.", "right_audio_tts": "They're in the box."}, {"left": "Where’s the guitar?", "right": "It’s on the bed.", "right_audio_tts": "It's on the bed."}, {"left": "Where are the fish?", "right": "They’re in the sea.", "right_audio_tts": "They're in the sea."}, {"left": "Where’s the book?", "right": "It’s on the table.", "right_audio_tts": "It's on the table."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'task', replace($blk${"title": "Look and answer · Где что лежит?", "needs_review": true, "image": "@@MEDIA@@sm1/u9/hw3_bags.webp", "html": "<p>Ты — большой молодец! Посмотри на картинки и впиши ответы на вопросы. Первый вопрос — пример, на него уже есть ответ.</p><ol><li>Where’s the blue book? — <i>It’s in the green bag.</i></li><li>Where’s the green lizard?</li><li>Where are the green books?</li><li>Where’s the black spider?</li><li>Where are the red books?</li><li>Where’s the yellow lizard?</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'task', replace($blk${"title": "Ask and answer · Где животные?", "needs_review": true, "image": "@@MEDIA@@sm1/u9/hw3_house.webp", "html": "<p>Посмотри на картинку и впиши вопросы про животных: <b>crocodiles, cat, spider, snake</b>. Потом ответь на свои вопросы.</p><p>Пример:<br><i>Where’s the lizard?<br>It’s in the bedroom.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Молодец! Ты справился с домашним заданием 👏</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
