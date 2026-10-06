-- Go Getter 1 · Unit 2 · My things · Homework 6
-- собрано tools/gg1_build.py --lesson u2_hw6
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 2 · My things', 2
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 2 · My things');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 2 · My things';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>На занятии ты написал пару предложений про свой любимый предмет. Расскажешь? Но сначала давай вспомним, какие бывают любимые предметы.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'hotspot', replace($blk${"title": "Подпиши названия предметов на картинке", "mode": "label", "image": "@@MEDIA@@gg1/u2/icons_favourite_things.webp", "points": [{"x": 32.0, "y": 26.0, "text": "trainers"}, {"x": 80.0, "y": 26.0, "text": "backpack"}, {"x": 32.0, "y": 58.0, "text": "mountain bike"}, {"x": 80.0, "y": 58.0, "text": "hoodie"}, {"x": 32.0, "y": 91.0, "text": "mobile phone"}, {"x": 80.0, "y": 91.0, "text": "games console"}], "extras": []}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>Послушай, о чём говорят Люк и Роза. Потом выполни задания ниже.</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Какие предметы упоминают Люк и Роза? Отметь все", "questions": [{"q": "Luke and Rosa talk about…", "type": "multiple", "options": [{"text": "hoodie"}, {"text": "mountain bike"}, {"text": "games console"}, {"text": "skateboard"}, {"text": "backpack"}, {"text": "trainers"}, {"text": "mobile phone"}], "correct": [1, 2, 3, 5, 6]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'task', replace($blk${"title": "Послушай аудио ещё раз и допиши предложения", "needs_review": true, "html": "<ol><li>Luke's ______ is new.</li><li>Rosa's favourite colour is ______.</li><li>Luke's trainers are ______.</li><li>Rosa's favourite thing is her ______.</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'speaking', replace($blk${"title": "Моя любимая вещь 🎤", "html": "<p>Теперь твоя очередь! Расскажи о своей любимой вещи. Не забудь ответить на вопросы: What is your name? What is your favourite thing? What is your favourite colour? В качестве образца можешь использовать аудио выше.</p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Спасибо тебе за интересный рассказ! 🎉</h3><p>Увидимся на занятии! Bye!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6);
end
$mig$;
