-- Super Minds 3 · Unit 7 · At the doctor’s · Homework 7
-- собрано tools/sm3_build.py --lesson u7_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 7 · At the doctor’s', 7
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 7 · At the doctor’s');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 7 · At the doctor’s';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>Выполни все задания, если хочешь стать чемпионом английского! А в конце тебя ждёт дополнительное задание — по желанию, НО если выполнишь, будешь мега крут.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<h3>Have you got a healthy lifestyle?</h3><p>Давай вспомним, о чём мы говорили на уроке, и прочитаем текст.</p><p><img src=\"@@MEDIA@@sm3/u7/reading_keep_healthy.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'sort', replace($blk${"title": "Внимательно посмотри на фразы и распредели их по категориям", "groups": [{"name": "HEALTHY", "items": [{"text": "swimming"}, {"text": "walking to school"}, {"text": "laughing with friends"}]}, {"name": "UNHEALTHY", "items": [{"text": "playing computer games for four hours"}, {"text": "always going to bed very late"}, {"text": "always eating ice cream for lunch"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'match', replace($blk${"title": "Соедини фразы с картинками по смыслу", "pairs": [{"left": "These are bad for the teeth.", "right_image": "@@MEDIA@@sm3/u7/habit_ice_creams.webp", "right": "ice creams"}, {"left": "It gets me outdoors.", "right_image": "@@MEDIA@@sm3/u7/habit_walking.webp", "right": "walking"}, {"left": "Sometimes it makes my eyes ache.", "right_image": "@@MEDIA@@sm3/u7/habit_screen_late.webp", "right": "screen"}, {"left": "I always make healthy food.", "right_image": "@@MEDIA@@sm3/u7/habit_picnic.webp", "right": "healthy food"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'task', replace($blk${"title": "Напиши, как ты поддерживаешь здоровый образ жизни", "needs_review": true, "html": "<p>Несколько предложений — по образцу.</p><p><i>Например: I play tennis to keep healthy. I usually play tennis with my friends on Saturdays.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/good_luck_clover.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты выполнил основную часть — супер!</h3><p>Осталась вторая часть: упражнения про приём у врача и ещё одно дополнительное задание.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'quiz', replace($blk${"title": "Read and choose: doctor or patient?", "questions": [{"q": "1. What’s the matter?", "type": "single", "options": [{"text": "doctor"}, {"text": "patient"}], "correct": [0]}, {"q": "2. Have you got a headache?", "type": "single", "options": [{"text": "doctor"}, {"text": "patient"}], "correct": [0]}, {"q": "3. When can I go to school again?", "type": "single", "options": [{"text": "patient"}, {"text": "doctor"}], "correct": [0]}, {"q": "4. Have you got any other aches?", "type": "single", "options": [{"text": "doctor"}, {"text": "patient"}], "correct": [0]}, {"q": "5. I’m so hot. Can I drink some cold orange juice?", "type": "single", "options": [{"text": "patient"}, {"text": "doctor"}], "correct": [0]}, {"q": "6. What have I got?", "type": "single", "options": [{"text": "patient"}, {"text": "doctor"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'match', replace($blk${"title": "Соедини вопросы и ответы", "pairs": [{"left": "What’s the matter?", "right": "I’ve got a stomach-ache.", "right_audio_tts": "I've got a stomach-ache."}, {"left": "Have you got a headache?", "right": "Yes, but it’s not strong.", "right_audio_tts": "Yes, but it's not strong."}, {"left": "Have you got any other aches?", "right": "No, just the stomach-ache.", "right_audio_tts": "No, just the stomach-ache."}, {"left": "I’m so hot. Can I drink some cold orange juice?", "right": "You have to drink a lot, but you can’t drink anything cold.", "right_audio_tts": "You have to drink a lot, but you can't drink anything cold."}, {"left": "What have I got?", "right": "Don’t worry. It’s nothing serious. But you have to rest.", "right_audio_tts": "Don't worry. It's nothing serious. But you have to rest."}, {"left": "When can I go to school again?", "right": "I’m not sure. Maybe in a week.", "right_audio_tts": "I'm not sure. Maybe in a week."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'task', replace($blk${"title": "Дополнительное задание — для ЧЕМПИОНОВ", "needs_review": true, "html": "<p>Напиши рассказ (из жизни или выдуманный) о том, как кто-то получил травму или заболел. Можешь обратиться за помощью к словарям.</p><p>Образец — ниже. Напиши свой рассказ здесь или на листочке.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<h3>Образец: план и рассказ про Тома</h3><p><img src=\"@@MEDIA@@sm3/u7/writing_tom_story.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание — ты замечательный ученик!</h3><p>За это лови звёздочку :) Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
