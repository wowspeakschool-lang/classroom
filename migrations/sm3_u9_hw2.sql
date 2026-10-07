-- Super Minds 3 · Unit 9 · Weather · Homework 2
-- собрано tools/sm3_build.py --lesson u9_hw2
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 9 · Weather', 9
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 9 · Weather');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 9 · Weather';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>Выполни все задания, если хочешь выучить тему на все 100! В конце есть дополнительное задание — по желанию, НО если сделаешь его, будешь нереально крут.</p><p>Для начала посмотри видео и всё повтори.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'video', replace($blk${"title": "Видео: going to — планы и погода", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'order', replace($blk${"words": ["On", "Saturday,", "we", "are", "going", "to make", "sandwiches", "and", "go", "to the park."], "sentence": "On Saturday, we are going to make sandwiches and go to the park.", "audio_tts": "On Saturday, we are going to make sandwiches and go to the park."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"words": ["The weather", "is", "going", "to", "be", "sunny", "and", "warm."], "sentence": "The weather is going to be sunny and warm.", "audio_tts": "The weather is going to be sunny and warm."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'truefalse', replace($blk${"title": "Посмотри на прогноз погоды и отметь, какие предложения верные (true), а какие неверные (false)", "image": "@@MEDIA@@sm3/u9/weather_week_board.webp", "statements": [{"text": "On Monday it’s going to be sunny.", "correct": false}, {"text": "On Tuesday it isn’t going to be rainy.", "correct": true}, {"text": "On Wednesday it’s going to be sunny.", "correct": false}, {"text": "On Thursday it’s going to be foggy.", "correct": false}, {"text": "On Friday it’s going to be cloudy.", "correct": true}, {"text": "On Saturday it’s going to be sunny.", "correct": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'match', replace($blk${"title": "Послушай запись и соедини дни недели с занятиями", "pairs": [{"left": "Monday", "right_image": "@@MEDIA@@sm3/u9/plan_sleep.webp", "right": "sleep"}, {"left": "Tuesday", "right_image": "@@MEDIA@@sm3/u9/plan_watch_tv.webp", "right": "watch TV"}, {"left": "Wednesday", "right_image": "@@MEDIA@@sm3/u9/plan_cook.webp", "right": "cook food"}, {"left": "Thursday", "right_image": "@@MEDIA@@sm3/u9/plan_tennis.webp", "right": "play tennis"}, {"left": "Friday", "right_image": "@@MEDIA@@sm3/u9/plan_kite.webp", "right": "fly a kite"}, {"left": "Sunday", "right_image": "@@MEDIA@@sm3/u9/plan_ride_horse.webp", "right": "ride a horse"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'video', replace($blk${"title": "Аудио к заданию «дни недели и занятия»", "url": "", "provider": ""}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'gaps', replace($blk${"title": "Посмотри на картинки и дни недели из прошлого задания и заполни пропуски. Первое предложение — образец", "text": "1. On Monday I’m going to sleep.\n2. On Tuesday I’m going to __watch TV|watch tv__.\n3. On Wednesday I’m going to __cook food__.\n4. On Thursday I’m going to __play tennis__.\n5. On Friday I’m going to __fly a kite__.\n6. On Sunday I’m going to __ride a horse__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'task', replace($blk${"title": "Дополнительное задание — напиши о своих планах на неделю", "needs_review": true, "html": "<p>3–4 предложения о том, что ты собираешься делать.</p><p><i>Например: On Saturday I’m going to do my homework.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание — ты МЕГА КРУТ!</h3><p>Жду тебя на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9);
end
$mig$;
