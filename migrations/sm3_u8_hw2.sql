-- Super Minds 3 · Unit 8 · Countries · Homework 2
-- собрано tools/sm3_build.py --lesson u8_hw2
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 8 · Countries', 8
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 8 · Countries');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 8 · Countries';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! Добро пожаловать в домашнее задание!</h2><p>В конце есть дополнительное задание — для самых крутых и смелых, обязательно попробуй его сделать!</p><p>Прежде чем начать, обязательно посмотри видео — так будет легче и понятнее.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Видео: прошедшее время, отрицания", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"title": "Супер! Давай найдём пары — повторим неправильные глаголы", "pairs": [{"left": "go", "right": "went", "right_audio_tts": "went"}, {"left": "feel", "right": "felt", "right_audio_tts": "felt"}, {"left": "ride", "right": "rode", "right_audio_tts": "rode"}, {"left": "give", "right": "gave", "right_audio_tts": "gave"}, {"left": "say", "right": "said", "right_audio_tts": "said"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант. Образец: We went to the beach but we didn’t go swimming.", "questions": [{"q": "1. We rode an elephant in the zoo but we ___ ride a horse.", "type": "single", "options": [{"text": "didn’t"}, {"text": "don’t"}, {"text": "doesn’t"}], "correct": [0]}, {"q": "2. I saw Bill at the birthday party but I ___ see Harry.", "type": "single", "options": [{"text": "didn’t"}, {"text": "not"}, {"text": "isn’t"}], "correct": [0]}, {"q": "3. They gave the horse an apple but they ___ him any sweets.", "type": "single", "options": [{"text": "didn’t give"}, {"text": "not gave"}, {"text": "didn’t gave"}], "correct": [0]}, {"q": "4. She said a lot but she ___ say her name.", "type": "single", "options": [{"text": "didn’t"}, {"text": "don’t"}, {"text": "isn’t"}], "correct": [0]}, {"q": "5. He ate all the chocolates but he ___ the ice cream.", "type": "single", "options": [{"text": "didn’t eat"}, {"text": "not ate"}, {"text": "didn’t ate"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'task', replace($blk${"title": "Дополнительное задание — перепиши предложения в отрицательной форме с didn’t", "needs_review": true, "html": "<p>Не забудь: после didn’t глагол встаёт в начальную форму.</p><p><i>Например: I bought a new car yesterday. → I didn’t buy a car yesterday.</i></p><p>1. I went to school yesterday.<br>2. We took photographs of the Great Wall of China.<br>3. We ate burritos in Spain.<br>4. We travelled to 3 countries: Spain, Italy and Portugal.<br>5. I walked in the park on Sunday.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание — ты замечательный ученик!</h3><p>За это лови звёздочку :) Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5);
end
$mig$;
