-- Super Minds 3 · Unit 1 · School · Homework 7
-- собрано tools/sm3_build.py --lesson u1_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 1 · School', 1
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 1 · School');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 1 · School';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет!</h2><p>Сегодня ты будешь много работать с геометрическими фигурами, а потом составишь интервью и ответишь на вопросы.</p><p>Задания самые разные и очень интересные — удачи :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'exact_input', replace($blk${"items": [{"image": "@@MEDIA@@sm3/u1/shape_pentagon.webp", "prompt": "1. Напиши название фигуры", "accept": ["pentagon", "Pentagon", "a pentagon"], "audio_tts": "pentagon"}, {"image": "@@MEDIA@@sm3/u1/shape_hexagon.webp", "prompt": "2. Напиши название фигуры", "accept": ["hexagon", "Hexagon", "a hexagon"], "audio_tts": "hexagon"}, {"image": "@@MEDIA@@sm3/u1/shape_triangle.webp", "prompt": "3. Напиши название фигуры", "accept": ["triangle", "Triangle", "a triangle"], "audio_tts": "triangle"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"title": "Соедини каждую иллюстрацию с названием объекта, который на ней изображён", "pairs": [{"left_image": "@@MEDIA@@sm3/u1/shapepic_cat.webp", "right": "cat", "right_audio_tts": "cat"}, {"left_image": "@@MEDIA@@sm3/u1/shapepic_person.webp", "right": "person", "right_audio_tts": "person"}, {"left_image": "@@MEDIA@@sm3/u1/shapepic_boat.webp", "right": "boat", "right_audio_tts": "boat"}, {"left_image": "@@MEDIA@@sm3/u1/shapepic_snake.webp", "right": "snake", "right_audio_tts": "snake"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'match', replace($blk${"title": "У каждой фигуры свой цвет. Соедини фигуру с её названием", "pairs": [{"left_image": "@@MEDIA@@sm3/u1/shape_square.webp", "right": "blue square", "right_audio_tts": "a blue square"}, {"left_image": "@@MEDIA@@sm3/u1/shape_circle.webp", "right": "green circle", "right_audio_tts": "a green circle"}, {"left_image": "@@MEDIA@@sm3/u1/shape_pentagon.webp", "right": "yellow pentagon", "right_audio_tts": "a yellow pentagon"}, {"left_image": "@@MEDIA@@sm3/u1/shape_triangle.webp", "right": "red triangle", "right_audio_tts": "a red triangle"}, {"left_image": "@@MEDIA@@sm3/u1/shape_rectangle.webp", "right": "orange rectangle", "right_audio_tts": "an orange rectangle"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Find the hexagon.", "type": "single", "options": [{"image": "@@MEDIA@@sm3/u1/shape_pentagon.webp"}, {"image": "@@MEDIA@@sm3/u1/shape_hexagon.webp"}, {"image": "@@MEDIA@@sm3/u1/shape_square.webp"}, {"image": "@@MEDIA@@sm3/u1/shape_circle.webp"}], "correct": [1]}, {"q": "Find the rectangle.", "type": "single", "options": [{"image": "@@MEDIA@@sm3/u1/shape_triangle.webp"}, {"image": "@@MEDIA@@sm3/u1/shape_circle.webp"}, {"image": "@@MEDIA@@sm3/u1/shape_rectangle.webp"}, {"image": "@@MEDIA@@sm3/u1/shape_hexagon.webp"}], "correct": [2]}, {"q": "Find the circle.", "type": "single", "options": [{"image": "@@MEDIA@@sm3/u1/shape_circle.webp"}, {"image": "@@MEDIA@@sm3/u1/shape_square.webp"}, {"image": "@@MEDIA@@sm3/u1/shape_pentagon.webp"}, {"image": "@@MEDIA@@sm3/u1/shape_triangle.webp"}], "correct": [0]}, {"q": "Find the square.", "type": "single", "options": [{"image": "@@MEDIA@@sm3/u1/shape_rectangle.webp"}, {"image": "@@MEDIA@@sm3/u1/shape_hexagon.webp"}, {"image": "@@MEDIA@@sm3/u1/shape_triangle.webp"}, {"image": "@@MEDIA@@sm3/u1/shape_square.webp"}], "correct": [3]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'match', replace($blk${"title": "Составь интервью: соедини вопросы с ответами", "pairs": [{"left": "What’s your favourite subject, Kate?", "right": "Science. I love it."}, {"left": "What do you like about it?", "right": "We do fun activities in the Science, and I love doing them."}, {"left": "How many Science lessons do you have a week?", "right": "Three, but I’d like to have it every day."}, {"left": "Have you got Science today?", "right": "Let me think. It’s Wednesday. Yes, I’ve got Science after Maths."}, {"left": "Do lots of students like Science?", "right": "No, not many children like it. They think it’s difficult."}, {"left": "What’s the favourite subject in your class?", "right": "For most of my classmates it’s English. They love it."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'truefalse', replace($blk${"title": "Верно или неверно?", "statements": [{"text": "Kate’s favourite subject is Chemistry.", "answer": false}, {"text": "On Wednesdays she has Science.", "answer": true}, {"text": "She has three Science lessons every week.", "answer": true}, {"text": "Kate’s classmates love Science.", "answer": false}, {"text": "Kate tells that Science lessons are boring.", "answer": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "What is Kate’s favourite subject?", "type": "single", "options": [{"text": "English"}, {"text": "Maths"}, {"text": "Science"}, {"text": "History"}], "correct": [2]}, {"q": "How many Science lessons has Kate got a week?", "type": "single", "options": [{"text": "one"}, {"text": "three"}, {"text": "five"}, {"text": "every day"}], "correct": [1]}, {"q": "Which lesson comes before Science on Wednesday?", "type": "single", "options": [{"text": "Art"}, {"text": "Music"}, {"text": "Maths"}, {"text": "P.E."}], "correct": [2]}, {"q": "What is the favourite subject in Kate’s class?", "type": "single", "options": [{"text": "Science"}, {"text": "English"}, {"text": "Geography"}, {"text": "I.T."}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты справился со всеми заданиями, поздравляю!</h3><p>Теперь можешь смело отдыхать :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
