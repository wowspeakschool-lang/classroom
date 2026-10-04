-- Super Minds 3 · Unit 6 · Gadgets · Homework 7
-- собрано tools/sm3_build.py --lesson u6_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 6 · Gadgets', 6
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 6 · Gadgets');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 6 · Gadgets';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Огромный привет! Как твоё настроение?</h2><p>Самое время сделать новое домашнее задание. Сегодня будет много интересного, и ты кое-что нарисуешь. Давай начнём!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'match', replace($blk${"title": "Давай вспомним, что мы проходили на занятии! Соедини слова с картинками", "pairs": [{"left_image": "@@MEDIA@@sm3/u6/cave_pigments.webp", "right": "rock powder", "right_audio_tts": "rock powder"}, {"left_image": "@@MEDIA@@sm3/u6/cave_lamp.webp", "right": "lamp", "right_audio_tts": "lamp"}, {"left_image": "@@MEDIA@@sm3/u6/cave_ceiling_bats.webp", "right": "cave ceiling", "right_audio_tts": "cave ceiling"}, {"left_image": "@@MEDIA@@sm3/u6/cave_twig.webp", "right": "twig", "right_audio_tts": "twig"}, {"left_image": "@@MEDIA@@sm3/u6/cave_charcoal.webp", "right": "charcoal", "right_audio_tts": "charcoal"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'gaps', replace($blk${"title": "Супер! А теперь прочитай предложения и вставь пропущенные слова", "mode": "drag", "text": "1. Artists still use __charcoal__ to draw pictures.\n2. I drew a picture with a __twig__ from a tree in our Art lesson today.\n3. Cave artists used __rock powder__ to make coloured paint.\n4. We saw some bats sleeping on the __cave ceiling__.\n5. Dad had an old oil __lamp__ so we could see in the dark."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'match', replace($blk${"title": "Прочитай описания наскальных рисунков и соедини описание с тем, что на нём изображено. Обращай внимание на детали!", "pairs": [{"left": "This painting is in the Sahara Desert. It shows a man with a tall giraffe. It tells us that giraffes are thousands of years old and live in the desert.", "right": "a man and a tall giraffe", "right_audio_tts": "a man and a tall giraffe"}, {"left": "This painting tells us how people travelled. Some people are on camels and some are walking. This picture is from a cave in Algeria.", "right": "people on camels and people walking", "right_audio_tts": "people on camels and people walking"}, {"left": "In this picture we can see people hunting. Some people are talking, too. You can see this picture in a cave in Thailand.", "right": "people hunting and talking", "right_audio_tts": "people hunting and talking"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'task', replace($blk${"title": "Нарисуй свой наскальный рисунок и опиши его", "needs_review": true, "html": "<p>Задание дополнительное, но настоящие чемпионы обязательно с ним справятся! Рисовать можно самыми разными материалами.</p><p>Потом напиши небольшое описание по плану:</p><p><i>1. I draw my pictures on …<br>2. I use …<br>3. In this picture you can see …</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Спасибо тебе огромное за твой труд!</h3><p>Ты невероятно потрудился сегодня. До встречи на занятии :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5);
end
$mig$;
