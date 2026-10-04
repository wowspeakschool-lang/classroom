-- Super Minds 3 · Unit 9 · Weather · Homework 6
-- собрано tools/sm3_build.py --lesson u9_hw6
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
  select v_unit, 'Homework 6', 'homework',
         60, false, 5
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 6');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 6';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание!</h2><p>В этом уроке тебя ждёт текст и несколько упражнений.</p><p>В конце урока есть дополнительное задание — по желанию, НО если ты сделаешь его, то будешь чемпионом английского!</p><p>Для начала внимательно прочитай текст ещё раз.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u9/reading_liam_1.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@sm3/u9/reading_liam_2.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'sequence', replace($blk${"title": "Отлично! А теперь прочитай текст ещё раз и расставь предложения в правильном порядке по смыслу", "image": "@@MEDIA@@sm3/u9/scene_storm_window.webp", "items": [{"text": "Liam and his mum and dad went to Florida for a holiday."}, {"text": "Liam woke up because of a noisy thunderstorm."}, {"text": "Liam’s dad switched on the TV."}, {"text": "The man on TV said, ‘There’s going to be rain for fourteen days!’"}, {"text": "Liam didn’t like that. ‘It’s going to be boring!’ he thought."}, {"text": "Liam had a good time inside with his mum and dad."}, {"text": "Liam loved his holiday so much he didn’t want to go home."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Прочитай текст ещё раз и заполни краткое содержание. Вставь слова по смыслу. Не забудь, что текст в прошедшем времени!", "mode": "drag", "text": "Liam was very excited because he was going to Florida for two weeks. ‘It’s going to be __fantastic__!’ he said. ‘We can go for boat rides!’ said Dad. ‘We can relax and have a lot of fun!’ said Mum.\nThey arrived in Florida and the hotel was beautiful. ‘Tomorrow I’m __going__ to swim in the sea!’ he said.\nBut in the middle of the night there was a lot of noise and Liam woke up. He looked outside and saw a big __thunderstorm__.\nDad switched on the TV. ‘There’s going to be a lot of __rain__ in Florida for the next fourteen days,’ said the man on TV. ‘It’s our holiday. We can’t swim or see fish in the rain! It’s going to be __boring__,’ Liam said.\n‘We can have fun in our room. We can read, play games and listen to music,’ said Mum. Two weeks later, their holiday was finished. ‘I __don’t__ want to go home, Mum,’ Liam said. ‘It was a beautiful holiday!’ ‘Let’s play another __game__,’ said Mum. Dad went to get their games box. ‘Hooray!’ shouted Liam."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ для самых больших умников! Послушай краткий пересказ истории — в нём 4 ошибки. С первой я тебе помогу, остальные найди сам", "audio": "", "text": "1. Italy instead of (вместо) Florida.\n2. __a river|a river.__ instead of __the sea|the sea.__\n3. __a thunderstorm|a thunderstorm.__ instead of __a lot of rain|a lot of rain.__\n4. __fantastic|fantastic.__ instead of __boring|boring.__"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_trophy.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание и теперь готов к уроку. Ты — СУПЕР КРУТ!</h3><p>Жду тебя на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6);
end
$mig$;
