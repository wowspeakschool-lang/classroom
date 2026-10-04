-- Super Minds 3 · Unit 4 · In the town · Homework 2
-- собрано tools/sm3_build.py --lesson u4_hw2
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 4 · In the town', 4
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 4 · In the town');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 4 · In the town';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>HELLO! Добро пожаловать в домашнее задание!</h2><p>Сегодня мы будем повторять предлоги. Внимательно посмотри видео и сделай задания ниже.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Видео: предлоги места", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'order', replace($blk${"image": "@@MEDIA@@sm3/u4/prep_cat_under_sofa.webp", "words": ["The", "cat", "is", "under", "the", "sofa."], "sentence": "The cat is under the sofa.", "audio_tts": "The cat is under the sofa."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"image": "@@MEDIA@@sm3/u4/prep_cat_dog_opposite.webp", "words": ["The", "cat", "is", "opposite", "the", "dog."], "sentence": "The cat is opposite the dog.", "audio_tts": "The cat is opposite the dog."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"image": "@@MEDIA@@sm3/u4/prep_cat_below_shelf.webp", "words": ["The", "cat", "is", "below", "the", "shelf."], "sentence": "The cat is below the shelf.", "audio_tts": "The cat is below the shelf."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"image": "@@MEDIA@@sm3/u4/prep_fox_in_front_of_box.webp", "words": ["The", "fox", "is", "in front of", "the", "box."], "sentence": "The fox is in front of the box.", "audio_tts": "The fox is in front of the box."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"image": "@@MEDIA@@sm3/u4/prep_mouse_between_boxes.webp", "words": ["The", "mouse", "is", "between", "the", "boxes."], "sentence": "The mouse is between the boxes.", "audio_tts": "The mouse is between the boxes."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"image": "@@MEDIA@@sm3/u4/prep_monkey_behind_tree.webp", "words": ["The", "monkey", "is", "behind", "the", "tree."], "sentence": "The monkey is behind the tree.", "audio_tts": "The monkey is behind the tree."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<h3>Посмотри на картинку — какие места есть в городе?</h3><p><img src=\"@@MEDIA@@sm3/u4/scene_town_prepositions.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант", "questions": [{"q": "1. The cinema is ___ the library.", "type": "single", "options": [{"text": "opposite"}, {"text": "between"}], "correct": [0]}, {"q": "2. The tower is ___ the cinema.", "type": "single", "options": [{"text": "behind"}, {"text": "above"}], "correct": [0]}, {"q": "3. The park is ___ the school.", "type": "single", "options": [{"text": "opposite"}, {"text": "near"}], "correct": [0]}, {"q": "4. The boat is ___ the bridge.", "type": "single", "options": [{"text": "below"}, {"text": "above"}], "correct": [0]}, {"q": "5. The sports centre is ___ the cinema and the cafe.", "type": "single", "options": [{"text": "between"}, {"text": "in front of"}], "correct": [0]}, {"q": "6. The castle is ___ the sports centre.", "type": "single", "options": [{"text": "behind"}, {"text": "opposite"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'task', replace($blk${"title": "Напиши три предложения про свой город", "needs_review": true, "html": "<p>СУПЕР! Ты прекрасно со всем справляешься. У меня есть для тебя ещё одно задание — оно дополнительное, но если ты его сделаешь, получишь дополнительную ⭐</p><p><i>Например: The cinema is behind the shop.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_jump.webp\" alt=\"\" style=\"height:180px\"></p><h3>УРА! У тебя получилось!</h3><p>Не забудь показать свой текст на занятии. Увидимся!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11);
end
$mig$;
