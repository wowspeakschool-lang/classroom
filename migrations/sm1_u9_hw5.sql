-- Super Minds 1 · Unit 9 · Holidays · Homework 5
-- собрано tools/sm1_build.py --lesson u9_hw5
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
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>Тебя ждут интересные упражнения и 1 ДОПОЛНИТЕЛЬНОЕ задание, которое можно выполнить ПО ЖЕЛАНИЮ. Но ты будешь МЕГА КРУТ, когда выполнишь его.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Внимательно посмотри на картинку. Прочитай предложение и скажи, это правда (True) или неправда (False).", "questions": [{"q": "She is eating ice-cream.", "type": "single", "image": "@@MEDIA@@sm1/u9/hw5_girl_icecream.webp", "options": [{"text": "True ✅"}, {"text": "False ❌"}], "correct": [0]}, {"q": "She is reading a book.", "type": "single", "image": "@@MEDIA@@sm1/u9/act_listen_music.webp", "options": [{"text": "True ✅"}, {"text": "False ❌"}], "correct": [1]}, {"q": "They are making a sandcastle.", "type": "single", "image": "@@MEDIA@@sm1/u9/act_make_sandcastle.webp", "options": [{"text": "True ✅"}, {"text": "False ❌"}], "correct": [0]}, {"q": "He is taking a photo.", "type": "single", "image": "@@MEDIA@@sm1/u9/act_catch_fish.webp", "options": [{"text": "True ✅"}, {"text": "False ❌"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'order', replace($blk${"words": ["She", "is", "painting", "a", "picture."], "sentence": "She is painting a picture.", "audio_tts": "She is painting a picture.", "image": "@@MEDIA@@sm1/u9/act_paint_picture.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"words": ["He", "is", "taking", "a", "photo."], "sentence": "He is taking a photo.", "audio_tts": "He is taking a photo.", "image": "@@MEDIA@@sm1/u9/act_take_photo.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"words": ["They", "are", "looking", "for", "shells."], "sentence": "They are looking for shells.", "audio_tts": "They are looking for shells.", "image": "@@MEDIA@@sm1/u9/act_look_shells.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["She", "is", "reading", "a", "book."], "sentence": "She is reading a book.", "audio_tts": "She is reading a book.", "image": "@@MEDIA@@sm1/u9/act_read_book.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'video', replace($blk${"title": "Аудио: послушай и узнай, как зовут детей на пляже", "url": "", "provider": "file"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'hotspot', replace($blk${"title": "Послушай аудио и подпиши детей на картинке их именами.", "mode": "label", "image": "@@MEDIA@@sm1/u9/hw5_beach_kids.webp", "points": [{"x": 19, "y": 44, "text": "Tom", "audio_tts": "Tom"}, {"x": 36, "y": 77, "text": "Jim", "audio_tts": "Jim"}, {"x": 50, "y": 64, "text": "Sue", "audio_tts": "Sue"}, {"x": 67, "y": 78, "text": "Mia", "audio_tts": "Mia"}, {"x": 87, "y": 55, "text": "Bob", "audio_tts": "Bob"}], "extras": []}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p>Ты большой молодец! Ты выполнил основную часть домашнего задания, класс!</p><p>Осталось одно ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ! Его можно выполнить по желанию.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'speaking', replace($blk${"title": "Дополнительное задание ⭐ Что делают на пляже? 🎤", "needs_review": true, "image": "@@MEDIA@@sm1/u9/hw5_beach_scene.webp", "html": "<p>Посмотри на картинку и запиши аудио, где ты описываешь, чем занимаются дети и взрослые.</p><p>Послушай пример: <i>The girl is making a sandcastle.</i></p><p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>", "sample": "", "sample_tts": "The girl is making a sandcastle. The boy is swimming. The woman is reading a book."}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание! 👏</h3><p>Горжусь тобой! Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
