-- Super Minds 3 · Unit 6 · Gadgets · Homework 2
-- собрано tools/sm3_build.py --lesson u6_hw2
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
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет, добро пожаловать в домашнее задание!</h2><p>Сегодня мы посмотрим видео и выполним упражнения. А в конце тебя ждёт дополнительное задание — оно по желанию, но ты будешь МЕГА крут, когда справишься с ним!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Видео: сравнительная степень прилагательных", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'sort', replace($blk${"title": "Распредели прилагательные: к каким прибавляем -er, а к каким ставим more перед прилагательным?", "groups": [{"name": "+ er", "items": [{"text": "big"}, {"text": "small"}, {"text": "easy"}, {"text": "cheap"}, {"text": "happy"}, {"text": "fast"}]}, {"name": "more …", "items": [{"text": "interesting"}, {"text": "beautiful"}, {"text": "expensive"}, {"text": "dangerous"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"image": "@@MEDIA@@sm3/u6/pair_tv_watch.webp", "words": ["A TV", "is", "more", "expensive", "than", "a watch."], "sentence": "A TV is more expensive than a watch.", "audio_tts": "A TV is more expensive than a watch."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"image": "@@MEDIA@@sm3/u6/pair_cake_cookie.webp", "words": ["A cake", "is", "bigger", "than", "a cookie."], "sentence": "A cake is bigger than a cookie.", "audio_tts": "A cake is bigger than a cookie."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"image": "@@MEDIA@@sm3/u6/pair_plane_bicycle.webp", "words": ["A plane", "is", "faster", "than", "a bike."], "sentence": "A plane is faster than a bike.", "audio_tts": "A plane is faster than a bike."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"image": "@@MEDIA@@sm3/u6/pair_football_golfball.webp", "words": ["Football", "is", "more", "interesting", "than", "golf."], "sentence": "Football is more interesting than golf.", "audio_tts": "Football is more interesting than golf."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["Cartoons", "are", "funnier", "than", "books."], "sentence": "Cartoons are funnier than books.", "audio_tts": "Cartoons are funnier than books."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ответа", "questions": [{"q": "A tiger is ___ than a cat.", "type": "single", "image": "@@MEDIA@@sm3/u6/pair_tiger_cat.webp", "options": [{"text": "stronger"}, {"text": "more strong"}, {"text": "more stronger"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ответа", "questions": [{"q": "An elephant is ___ than a mouse.", "type": "single", "image": "@@MEDIA@@sm3/u6/pair_elephant_mouse.webp", "options": [{"text": "bigger"}, {"text": "biger"}, {"text": "more big"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ответа", "questions": [{"q": "A butterfly is ___ than a caterpillar.", "type": "single", "image": "@@MEDIA@@sm3/u6/pair_butterfly_caterpillar.webp", "options": [{"text": "more beautiful"}, {"text": "more beautifuller"}, {"text": "beautifuller"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ответа", "questions": [{"q": "PE is ___ than Maths.", "type": "single", "options": [{"text": "funnier"}, {"text": "more funny"}, {"text": "funnyer"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ответа", "questions": [{"q": "A computer is ___ than a torch.", "type": "single", "image": "@@MEDIA@@sm3/u6/pair_computer_torch.webp", "options": [{"text": "more expensive"}, {"text": "expensiver"}, {"text": "more expensiver"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'speaking', replace($blk${"title": "Дополнительное задание 🎤", "needs_review": true, "html": "<p>Его можно сделать по желанию. Но если сделаешь, будешь нереально крут!</p><p>Ниже картинка с двумя собачками — Lucky и Mister. Скажи 3–4 предложения, сравнивая их. Не забудь про сравнительную степень прилагательных.</p><p><i>Например: Lucky is more beautiful than Mister.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u6/scene_two_dogs.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/congrats_popper.webp\" alt=\"\" style=\"height:180px\"></p><h3>Вау, поздравляю! Ты завершил всё домашнее задание — ты просто МЕГА КРУТ!</h3><p>Увидимся на занятии ;)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 15);
end
$mig$;
