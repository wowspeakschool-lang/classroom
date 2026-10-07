-- Super Minds 1 · Unit 7 · Get dressed · Homework 6
-- собрано tools/sm1_build.py --lesson u7_hw6
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 7 · Get dressed', 7
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 7 · Get dressed');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 7 · Get dressed';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет!</h2><p>Сегодня мы выучим названия разных узоров, которые частенько встречаются на одежде.</p><p>Тебя ждут интересные увлекательные упражнения, и ты будешь супер учеником, когда справишься с ними!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили с тобой на уроке:</p><table style=\"border-collapse:collapse;text-align:center\"><tr><td style=\"padding:6px\"><img src=\"@@MEDIA@@sm1/u7/pattern_stripes.webp\" alt=\"\" style=\"height:110px\"><br><b>stripes</b></td><td style=\"padding:6px\"><img src=\"@@MEDIA@@sm1/u7/pattern_spots.webp\" alt=\"\" style=\"height:110px\"><br><b>spots</b></td><td style=\"padding:6px\"><img src=\"@@MEDIA@@sm1/u7/pattern_flowers.webp\" alt=\"\" style=\"height:110px\"><br><b>flowers</b></td><td style=\"padding:6px\"><img src=\"@@MEDIA@@sm1/u7/pattern_plain.webp\" alt=\"\" style=\"height:110px\"><br><b>plain</b></td><td style=\"padding:6px\"><img src=\"@@MEDIA@@sm1/u7/pattern_zigzags.webp\" alt=\"\" style=\"height:110px\"><br><b>zigzags</b></td></tr></table>", "audio_tts": "stripes, spots, flowers, plain, zigzags"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"title": "Для начала давай вспомним наши узоры. Соедини название с картинкой.", "pairs": [{"left": "stripes", "left_audio_tts": "stripes", "right": "узор stripes", "right_image": "@@MEDIA@@sm1/u7/pattern_stripes.webp"}, {"left": "spots", "left_audio_tts": "spots", "right": "узор spots", "right_image": "@@MEDIA@@sm1/u7/pattern_spots.webp"}, {"left": "flowers", "left_audio_tts": "flowers", "right": "узор flowers", "right_image": "@@MEDIA@@sm1/u7/pattern_flowers.webp"}, {"left": "plain", "left_audio_tts": "plain", "right": "узор plain", "right_image": "@@MEDIA@@sm1/u7/pattern_plain.webp"}, {"left": "zigzags", "left_audio_tts": "zigzags", "right": "узор zigzags", "right_image": "@@MEDIA@@sm1/u7/pattern_zigzags.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай описание и найди одежду девочки", "questions": [{"q": "Внимательно прочитай описание девочек и найди их одежду.<br><b>Anna</b>: She is wearing a plain skirt and a sweater with zigzags.", "type": "single", "audio_tts": "She is wearing a plain skirt and a sweater with zigzags.", "options": [{"image": "@@MEDIA@@sm1/u7/outfit_lily.webp"}, {"image": "@@MEDIA@@sm1/u7/outfit_anna.webp"}, {"image": "@@MEDIA@@sm1/u7/outfit_kate.webp"}], "correct": [1]}, {"q": "<b>Lily</b>: She is wearing a shirt with spots and a skirt with flowers.", "type": "single", "audio_tts": "She is wearing a shirt with spots and a skirt with flowers.", "options": [{"image": "@@MEDIA@@sm1/u7/outfit_lily.webp"}, {"image": "@@MEDIA@@sm1/u7/outfit_kate.webp"}, {"image": "@@MEDIA@@sm1/u7/outfit_anna.webp"}], "correct": [0]}, {"q": "<b>Kate</b>: She is wearing a T-shirt with stripes and a skirt with spots.", "type": "single", "audio_tts": "She is wearing a T-shirt with stripes and a skirt with spots.", "options": [{"image": "@@MEDIA@@sm1/u7/outfit_anna.webp"}, {"image": "@@MEDIA@@sm1/u7/outfit_lily.webp"}, {"image": "@@MEDIA@@sm1/u7/outfit_kate.webp"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Внимательно посмотри на картинку. Это мои любимые вещи с узорами. Прочитай их описание и впиши в пропуск название нужного узора.", "image": "@@MEDIA@@sm1/u7/fav_clothes.webp", "text": "Look! These are my favourite clothes.\nIt's a T-shirt with __flowers__.\nThey are shorts with __zigzags|zigzag__. They are red and white.\nThey are __plain__ trousers.\nIt's a sweater with __stripes__. It's black and white.\nThey are socks with __spots__. They are yellow.\nI like my clothes!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'task', replace($blk${"title": "Ура! Это последнее задание на сегодня", "needs_review": true, "html": "<p>Письменно опиши свою любимую одежду с узорами (если у тебя такой нет — можешь пофантазировать и описать выдуманную).</p><p>Используй предыдущее упражнение как пример.</p><p><i>It's a T-shirt with … They are …</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание, ты замечательный ученик!</h3><p>За это лови сердечко ❤️</p><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6);
end
$mig$;
