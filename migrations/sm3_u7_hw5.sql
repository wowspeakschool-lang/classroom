-- Super Minds 3 · Unit 7 · At the doctor’s · Homework 5
-- собрано tools/sm3_build.py --lesson u7_hw5
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
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет, добро пожаловать в домашнее задание!</h2><p>Сегодня мы прочитаем историю и выполним упражнения. А в конце тебя ждёт дополнительное задание — по желанию, но ты будешь МЕГА крут, когда справишься с ним!</p><p>Для начала вспомни: каким был номер палаты, в которой лежал дедушка Бена?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u7/story_hospital_1.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u7/story_hospital_2.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'match', replace($blk${"title": "Прочти ещё раз и сопоставь две части предложения по смыслу", "pairs": [{"left": "Ben got", "right": "a text message.", "right_audio_tts": "a text message"}, {"left": "It said, ‘Go to the hospital,’", "right": "but it was a trick.", "right_audio_tts": "but it was a trick"}, {"left": "They found Horax", "right": "and not Ben’s grandfather there!", "right_audio_tts": "and not Ben's grandfather there"}, {"left": "Horax wanted", "right": "the book and the letters.", "right_audio_tts": "the book and the letters"}, {"left": "At that moment", "right": "the doctor came in.", "right_audio_tts": "the doctor came in"}, {"left": "Lucy and Ben said, ‘Bye, bye,’", "right": "and went out of the room.", "right_audio_tts": "and went out of the room"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'truefalse', replace($blk${"title": "Выбери True (правда) или False (неправда)", "statements": [{"text": "The doctor took Ben and Lucy to room 209.", "correct": true}, {"text": "Horax wanted the book from the children.", "correct": true}, {"text": "Lucy gave Horax the book.", "correct": false}, {"text": "The doctor thought Horax was Ben’s grandfather.", "correct": true}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'task', replace($blk${"title": "Дополнительное задание — перепиши предложения в прошедшем времени", "needs_review": true, "html": "<p>Как в примере (пункт 1). В предыдущих заданиях есть подсказки — пролистай наверх.</p><p>1. Lucy and Ben / go / hospital — <i>Lucy and Ben went to the hospital.</i><br>2. They / go / room 209<br>3. They / find / Horax, not / Ben / grandfather<br>4. It / be / trick<br>5. Horax / want / book and letters<br>6. At that moment / doctor / arrive<br>7. Ben / Lucy / say goodbye / and / go / out / room</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отлично, ты справился со всеми заданиями!</h3><p>Держи за это кубок победителя. Жду тебя на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6);
end
$mig$;
