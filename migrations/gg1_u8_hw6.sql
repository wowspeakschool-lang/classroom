-- Go Getter 1 · Unit 8 · Sport and health · Homework 6
-- собрано tools/gg1_build.py --lesson u8_hw6
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 8 · Sport and health', 8
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 8 · Sport and health');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 8 · Sport and health';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Добро пожаловать на домашнее задание! Сегодня мы с тобой закрепим знания, полученные на уроке. Как ты помнишь, мы слушали рассказы ребят о том, какой образ жизни они ведут. Сегодня ты тоже будешь слушать и выполнять задания, но уже самостоятельно!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'match', replace($blk${"title": "Первое задание — очень лёгкое! Соедини картинки со словами 😉", "pairs": [{"left_image": "@@MEDIA@@gg1/u8/life_fruit_vegetables.webp", "right": "food", "right_audio_tts": "food"}, {"left_image": "@@MEDIA@@gg1/u8/life_sleep.webp", "right": "sleep", "right_audio_tts": "sleep"}, {"left_image": "@@MEDIA@@gg1/u8/life_do_exercise.webp", "right": "exercise", "right_audio_tts": "exercise"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>Пришло время серьёзной работы! Послушай, как Том отвечает на вопросы о своём образе жизни.</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'match', replace($blk${"title": "Соедини номера вопросов из аудио с темами", "pairs": [{"left": "Question 1", "right": "Food"}, {"left": "Question 2", "right": "Exercise"}, {"left": "Question 3", "right": "Sleep"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Послушай Тома ещё раз и впиши в предложения недостающие слова", "mode": "type", "audio": "", "text": "Question 1: Tom's favourite food is __chips__. He eats a lot of __fruit__ and vegetables. He drinks a lot of __water__.\nQuestion 2: He likes __cycling__. He always __walks__ to school. He sometimes goes __swimming__.\nQuestion 3: He goes to bed at __9.30|9:30|half past nine|half past 9__. He goes to sleep at __ten o'clock|10 o'clock|10.00|10:00|ten|10__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "Побудь в роли учителя! В квадратных скобках — ошибки. Впиши в окошко правильное слово или поменяй порядок слов. Первое исправление уже сделано: Andy [like] likes pizza", "mode": "type", "text": "Andy [like] likes pizza but he [don't] __doesn't__ eat it very often. He [has always] __always has__ lunch at school. He often eats sandwiches.\nHe likes [read] __reading__ but he doesn't [likes] __like__ sport very much. His favourite sport [are] __is__ swimming. He has swimming lessons on Fridays.\nAndy goes to bed [in] __at__ nine because he likes [sleep] __sleeping__. He doesn't get up early."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'task', replace($blk${"title": "Рассказ о Мэй ✍️", "needs_review": true, "html": "<p>Напиши небольшой рассказ о Мэй по примеру рассказа Энди, который ты прочитал(а) выше! Воспользуйся табличкой — там есть вся нужная тебе информация о Мэй. Не забудь разделить рассказ на три абзаца: еда, спорт, подъём и отход ко сну!</p><p><img src=\"@@MEDIA@@gg1/u8/may_table.webp\" alt=\"May\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_jump.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7);
end
$mig$;
