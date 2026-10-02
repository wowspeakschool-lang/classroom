-- Super Minds 3 · Unit 2 · Food · Homework 6
-- собрано tools/sm3_build.py --lesson u2_hw6
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
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет!</h2><p>Как твои дела? Ты большой молодец, что решил сделать домашнюю работу. Время пролетит незаметно, ты как всегда со всем справишься. Вперёд!</p><p>Давай посмотрим видео про съедобные части растений. Пока будешь смотреть, найди единственный оранжевый продукт в видео и запомни его!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Видео: съедобные части растений", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'task', replace($blk${"title": "What orange vegetable is in the video?", "needs_review": true, "html": "<p>Самое время написать ответ на вопрос: <i>What orange vegetable is in the video?</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'match', replace($blk${"title": "Вспомни видео и соедини название съедобной части с её картинкой", "pairs": [{"left_image": "@@MEDIA@@sm3/u2/part_roots.webp", "right": "roots", "right_audio_tts": "roots"}, {"left_image": "@@MEDIA@@sm3/u2/part_seeds.webp", "right": "seeds", "right_audio_tts": "seeds"}, {"left_image": "@@MEDIA@@sm3/u2/part_stems.webp", "right": "stems", "right_audio_tts": "stems"}, {"left_image": "@@MEDIA@@sm3/u2/part_leaves.webp", "right": "leaves", "right_audio_tts": "leaves"}, {"left_image": "@@MEDIA@@sm3/u2/part_fruit.webp", "right": "fruit", "right_audio_tts": "fruit"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Прочитай письмо Марка и поставь слова на свои места ⬇", "mode": "drag", "text": "Dear Penny,\n\nTonight, we’re having a nice dinner. There’s a delicious salad with spinach and lettuce — __leaves__. There’s also a delicious soup with asparagus — __stems__. We have some chicken with pumpkin __seeds__. We also have a salad with __roots__: carrots and beetroot. There’s also a glass of __fruit__ juice for me with strawberries and mango — my favourite.\n\nWhat’s for dinner at your home?\n\nMark"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "Из каких частей растений делают эти блюда и напиток? Впиши их", "text": "soup: __stems|leaves|seeds|roots__, __leaves|stems|seeds|roots__\njuice: __fruit|fruits|stems|leaves|roots__, __stems|leaves|roots|fruit|fruits__\nsalad: __fruit|fruits|leaves|seeds|roots|stems__, __seeds|leaves|fruit|fruits|roots|stems__"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'video', replace($blk${"title": "Послушай образец — в нём говорится о животном, которого на картинке нет :)", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'speaking', replace($blk${"title": "Теперь — твоя очередь 🎤", "needs_review": true, "image": "@@MEDIA@@sm3/u2/scene_who_eats_what.webp", "html": "<p>Выбери двух животных с картинки и расскажи, какими частями растений любит питаться каждое из них.</p><p><i>Образец: The rabbit eats roots. It likes carrots.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Супер! Справился со всеми заданиями.</h3><p>Огромное тебе спасибо. Ты отлично поработал 😊 Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
