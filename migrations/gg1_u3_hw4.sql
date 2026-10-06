-- Go Getter 1 · Unit 3 · My home · Homework 4
-- собрано tools/gg1_build.py --lesson u3_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 3 · My home', 3
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 3 · My home');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 3 · My home';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>Как здорово, что ты решился взяться за домашнюю работу. Поехали!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u3/card_guest_phrases.webp\" alt=\"Принимаем гостя\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"title": "Соедини картинку и подходящую фразу", "pairs": [{"left_image": "@@MEDIA@@gg1/u3/phrase_come_in.webp", "right": "Hello, please, come in."}, {"left_image": "@@MEDIA@@gg1/u3/phrase_sandwich.webp", "right": "Would you like a sandwich?"}, {"left_image": "@@MEDIA@@gg1/u3/room_bathroom.webp", "right": "Where is the bathroom?"}, {"left_image": "@@MEDIA@@gg1/u3/phrase_upstairs.webp", "right": "It's upstairs."}, {"left_image": "@@MEDIA@@gg1/u3/phrase_shoes.webp", "right": "Where are my shoes?"}, {"left_image": "@@MEDIA@@gg1/u3/phrase_here_you_are.webp", "right": "Here you are."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'sequence', replace($blk${"title": "Представь, что ты говоришь со своим другом. Расставь предложения по порядку!", "items": [{"text": "Hello, please, come in!"}, {"text": "Hello, thank you!"}, {"text": "Where is the bathroom? I need to wash my hands."}, {"text": "It's upstairs, next to the bedroom."}, {"text": "Let me show you."}, {"text": "Come to the living room after that."}, {"text": "Would you like some tea or coffee?"}, {"text": "Yes, please!"}, {"text": "OK, let's go upstairs!"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "А теперь давай потренируемся! Вставь пропущенные слова в диалог", "mode": "drag", "image": "@@MEDIA@@gg1/u3/kids_at_door.webp", "text": "A: Hello! Please, __come in__.\nB: Thank __you__!\nA: Would you __like__ a cup of __tea__?\nB: Yes, __please__, yummy!\nA: Where's the __bedroom__?\nB: __Let__ me __show__ you!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'speaking', replace($blk${"title": "Небольшой challenge ⭐", "image": "@@MEDIA@@gg1/u3/phrase_come_in.webp", "html": "<p>Узнай у преподавателя значение слова challenge! Получишь звёздочку, если справишься.</p><p>Представь, что ты пришёл в новый дом к своему другу и очень хочешь посмотреть его комнату. Составь диалог между вами и запиши его.</p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты — молодец! Со всем отлично справился! 🎉</h3><p>До скорой встречи!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6);
end
$mig$;
