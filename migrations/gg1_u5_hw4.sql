-- Go Getter 1 · Unit 5 · I can do it · Homework 4
-- собрано tools/gg1_build.py --lesson u5_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 5 · I can do it', 5
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 5 · I can do it');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 5 · I can do it';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Привет-привет! Самое время приступить к домашней работе!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u5/card_suggestions.webp\" alt=\"Making suggestions\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"title": "Соедини части предложений", "pairs": [{"left": "Let's play", "right": "football after school."}, {"left": "We can watch", "right": "my new DVD."}, {"left": "Let's go", "right": "to the park."}, {"left": "We can make", "right": "chocolate cupcakes."}, {"left": "Let's ride", "right": "our bikes."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Заверши предложения нужными словами", "mode": "drag", "text": "1. Let's do __that__! 😊\n2. It's not a __good__ idea. ☹️\n3. Great __idea__! 😊\n4. I'm not __sure__. 😐"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'sequence', replace($blk${"title": "Расположи предложения в нужном порядке, чтобы получился диалог", "items": [{"text": "Hi! Let's play in the garden."}, {"text": "No, not the garden again. We can go to the park."}, {"text": "Yes, the park's a great idea. We can play football."}, {"text": "I'm not sure about football."}, {"text": "Why not?"}, {"text": "We haven't got a ball."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'task', replace($blk${"title": "Напиши небольшие диалоги по картинкам", "needs_review": true, "image": "@@MEDIA@@gg1/u5/suggestion_scenes.webp", "html": "<p>A предлагает (We can… / Let's…), B отвечает — смайлик подсказывает как: 😊 соглашается, 😐 сомневается, ☹️ отказывается.</p><ol><li>A: play a game / B: 😊<br><i>Пример: A: We can play a game! B: Great idea!</i></li><li>A: watch that / B: 😐</li><li>A: go there / B: ☹️</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6);
end
$mig$;
