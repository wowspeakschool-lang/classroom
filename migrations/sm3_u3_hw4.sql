-- Super Minds 3 · Unit 3 · At home · Homework 4
-- собрано tools/sm3_build.py --lesson u3_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 3 · At home', 3
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 3 · At home');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 3 · At home';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет!</h2><p>Сегодня мы повторим с тобой тему <b>Time</b>. Тебя ждёт много крутых упражнений для тренировки. Поехали!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'match', replace($blk${"title": "Первое задание: сопоставь время с картинками", "pairs": [{"left_image": "@@MEDIA@@sm3/u3/clock_twenty_to_four.svg", "right": "It’s twenty to four.", "right_audio_tts": "It's twenty to four."}, {"left_image": "@@MEDIA@@sm3/u3/clock_quarter_past_three.svg", "right": "It’s quarter past three.", "right_audio_tts": "It's quarter past three."}, {"left_image": "@@MEDIA@@sm3/u3/clock_half_past_six.svg", "right": "It’s half past six.", "right_audio_tts": "It's half past six."}, {"left_image": "@@MEDIA@@sm3/u3/clock_quarter_to_five.svg", "right": "It’s quarter to five.", "right_audio_tts": "It's quarter to five."}, {"left_image": "@@MEDIA@@sm3/u3/clock_six_oclock.svg", "right": "It’s six o’clock.", "right_audio_tts": "It's six o'clock."}, {"left_image": "@@MEDIA@@sm3/u3/clock_quarter_past_eight.svg", "right": "It’s quarter past eight.", "right_audio_tts": "It's quarter past eight."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<h3>Внимательно прочитай правило!</h3><p><img src=\"@@MEDIA@@sm3/u3/rule_adverbs_time.webp\" alt=\"Adverbs for time\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"words": ["I", "always", "brush", "my", "teeth", "after", "dinner."], "sentence": "I always brush my teeth after dinner.", "audio_tts": "I always brush my teeth after dinner."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"words": ["My", "father", "never", "goes", "to", "bed", "early."], "sentence": "My father never goes to bed early.", "audio_tts": "My father never goes to bed early."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["My", "sister", "usually", "does", "lots", "of", "homework", "at", "the weekend."], "sentence": "My sister usually does lots of homework at the weekend.", "audio_tts": "My sister usually does lots of homework at the weekend."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["My", "mother", "sometimes", "does", "the shopping", "on", "Fridays."], "sentence": "My mother sometimes does the shopping on Fridays.", "audio_tts": "My mother sometimes does the shopping on Fridays."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["My", "brother", "always", "goes", "to", "bed", "at", "ten", "o’clock."], "sentence": "My brother always goes to bed at ten o’clock.", "audio_tts": "My brother always goes to bed at ten o'clock."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<h3>Прочитай новое правило!</h3><p><img src=\"@@MEDIA@@sm3/u3/table_family_chores.webp\" alt=\"\" style=\"max-width:100%\"></p><p><b>Always</b> ✔✔✔ · <b>Usually</b> ✔✔ · <b>Sometimes</b> ✔ · <b>Never</b> ✖</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'gaps', replace($blk${"title": "Прочитай правило ещё раз и выполни упражнение ⬇", "mode": "drag", "text": "1. I __never__ feed the cat.\n2. Mum __usually__ dries the dishes.\n3. Dad __always__ washes up.\n4. My brother __sometimes__ dries the dishes.\n5. My sister __never__ washes up.\n6. My brother __never__ feeds the cat.\n7. I __never__ cook."}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'task', replace($blk${"title": "Напиши 6 предложений про свою семью", "needs_review": true, "html": "<p>Молодец! Ты выполнил все основные задания. Осталось последнее — оно необязательное, но если ты его сделаешь, будешь СУПЕР КРУТЫМ учеником!</p><p><i>Например: Mum cooks every day. Dad always feeds the dog.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'flashcards', replace($blk${"title": "Дни недели", "cards": [{"text": "Monday", "translation": "понедельник", "audio_tts": "Monday"}, {"text": "Tuesday", "translation": "вторник", "audio_tts": "Tuesday"}, {"text": "Wednesday", "translation": "среда", "audio_tts": "Wednesday"}, {"text": "Thursday", "translation": "четверг", "audio_tts": "Thursday"}, {"text": "Friday", "translation": "пятница", "audio_tts": "Friday"}, {"text": "Saturday", "translation": "суббота", "audio_tts": "Saturday"}, {"text": "Sunday", "translation": "воскресенье", "audio_tts": "Sunday"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'quiz', replace($blk${"title": "Как это по-английски?", "questions": [{"q": "Как по-английски «понедельник»?", "type": "single", "options": [{"text": "Monday"}, {"text": "Thursday"}, {"text": "Tuesday"}, {"text": "Wednesday"}], "correct": [0]}, {"q": "Как по-английски «вторник»?", "type": "single", "options": [{"text": "Friday"}, {"text": "Thursday"}, {"text": "Tuesday"}, {"text": "Wednesday"}], "correct": [2]}, {"q": "Как по-английски «среда»?", "type": "single", "options": [{"text": "Friday"}, {"text": "Saturday"}, {"text": "Thursday"}, {"text": "Wednesday"}], "correct": [3]}, {"q": "Как по-английски «четверг»?", "type": "single", "options": [{"text": "Friday"}, {"text": "Saturday"}, {"text": "Sunday"}, {"text": "Thursday"}], "correct": [3]}, {"q": "Как по-английски «пятница»?", "type": "single", "options": [{"text": "Friday"}, {"text": "Monday"}, {"text": "Saturday"}, {"text": "Sunday"}], "correct": [0]}, {"q": "Как по-английски «суббота»?", "type": "single", "options": [{"text": "Monday"}, {"text": "Saturday"}, {"text": "Sunday"}, {"text": "Tuesday"}], "correct": [1]}, {"q": "Как по-английски «воскресенье»?", "type": "single", "options": [{"text": "Monday"}, {"text": "Sunday"}, {"text": "Tuesday"}, {"text": "Wednesday"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'exact_input', replace($blk${"items": [{"prompt": "Напиши по-английски: понедельник", "accept": ["Monday", "monday"], "audio_tts": "Monday"}, {"prompt": "Напиши по-английски: вторник", "accept": ["Tuesday", "tuesday"], "audio_tts": "Tuesday"}, {"prompt": "Напиши по-английски: среда", "accept": ["Wednesday", "wednesday"], "audio_tts": "Wednesday"}, {"prompt": "Напиши по-английски: четверг", "accept": ["Thursday", "thursday"], "audio_tts": "Thursday"}, {"prompt": "Напиши по-английски: пятница", "accept": ["Friday", "friday"], "audio_tts": "Friday"}, {"prompt": "Напиши по-английски: суббота", "accept": ["Saturday", "saturday"], "audio_tts": "Saturday"}, {"prompt": "Напиши по-английски: воскресенье", "accept": ["Sunday", "sunday"], "audio_tts": "Sunday"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание!</h3><p>Ты замечательный ученик. За это лови звёздочку :) Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 14);
end
$mig$;
