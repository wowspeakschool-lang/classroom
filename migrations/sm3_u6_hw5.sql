-- Super Minds 3 · Unit 6 · Gadgets · Homework 5
-- собрано tools/sm3_build.py --lesson u6_hw5
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
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>В этом уроке тебя ждут текст и упражнения к нему, а ещё крутое интерактивное видео. Выполни все задания, если хочешь выучить тему на все 100!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<h3>Пришло время вспомнить текст, который мы читали на уроке!</h3><p>Прежде чем читать, ответь на вопрос: <b>Why are Horax and Zelda scared?</b></p><p>Прочитай историю и проверь себя — правильно ли ты угадал?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u6/story_caves_1.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u6/story_caves_2.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай историю ещё раз и выбери правильный вариант", "questions": [{"q": "In picture 1, what does Ben mean when he says ‘Somewhere down there …’?", "type": "single", "options": [{"text": "A place below a tree"}, {"text": "A place under a stone"}, {"text": "A place in the caves"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ответа", "questions": [{"q": "In picture 3, why does Ben say ‘The torch was a good idea.’?", "type": "single", "options": [{"text": "Because he’s scared of the dark."}, {"text": "Because it’s dark in the cave."}, {"text": "Because a torch is his favourite gadget."}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ответа", "questions": [{"q": "In picture 6, how does Lucy know Horax and Zelda are coming?", "type": "single", "options": [{"text": "Buster sees them."}, {"text": "She sees them."}, {"text": "Ben tells her."}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ответа", "questions": [{"q": "Who makes the scary noise?", "type": "single", "options": [{"text": "Horax and Zelda."}, {"text": "Buster."}, {"text": "Ben."}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ответа", "questions": [{"q": "Buster is ___ dog in the world!", "type": "single", "options": [{"text": "clever"}, {"text": "cleverer"}, {"text": "the cleverest"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ответа", "questions": [{"q": "What is the next letter?", "type": "single", "options": [{"text": "F"}, {"text": "E"}, {"text": "T"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'match', replace($blk${"title": "Ты отлично справляешься! Соедини героя и фразу, которую он произнёс", "pairs": [{"left": "Ben", "right": "The torch was a good idea!", "right_audio_tts": "The torch was a good idea!"}, {"left": "Lucy", "right": "Have you got a walkie-talkie and a torch?", "right_audio_tts": "Have you got a walkie-talkie and a torch?"}, {"left": "Zelda", "right": "Let’s run!", "right_audio_tts": "Let's run!"}, {"left": "Horax", "right": "Where are those kids?", "right_audio_tts": "Where are those kids?"}, {"left": "Buster", "right": "Grrrrrrr!"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Не забудь про интерактивное видео</h3><p>Учитель прикрепил его в твоём личном кабинете. Это по желанию, НО если посмотришь — будешь нереально крут!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11);
end
$mig$;
