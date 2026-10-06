-- Go Getter 1 · Unit 5 · I can do it · Homework 5
-- собрано tools/gg1_build.py --lesson u5_hw5
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
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Давай приступать к домашней работе!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'gaps', replace($blk${"title": "Посмотри на картинки и заверши предложения", "mode": "type", "image": "@@MEDIA@@gg1/u5/senses_icons.webp", "text": "1. You can see people with your __eyes__.\n2. You can hear music with your __ears__.\n3. You can smell flowers with your __nose__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'gaps', replace($blk${"title": "Прочитай текст и заполни пропуски нужными словами", "mode": "drag", "image": "@@MEDIA@@gg1/u5/sign_language_friends.webp", "text": "Look at these women. They can't __hear__, but they can make words with their __hands__. It's a special sign language. They can use it to speak to their __friends__ and family."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"html": "<p><b>Прочитай текст.</b></p><p><img src=\"@@MEDIA@@gg1/u5/jasmine_sweep.webp\" alt=\"Jasmine and Sweep\" style=\"height:240px\"></p><p><i>Twelve-year-old Jasmine and her best friend are always together. Her best friend isn't a girl or a boy. He's a very special dog, called Sweep. Jasmine is an ordinary girl but she's got a problem – she can't hear. Think about it. She can't hear people, she can't hear music or the TV. She can't even hear cars in the street. It is sometimes very dangerous for her. But Jasmine is OK, because she's got Sweep, and Sweep is her ears! Sweep is a special 'hearing dog'. He can help Jasmine a lot. These days Jasmine can meet all her friends and hang out with them after school. Her parents can relax because Sweep is with her and she's safe.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери лучшее название для текста", "questions": [{"q": "What is the best title for the text?", "type": "single", "options": [{"text": "A dog helps a girl called Jasmine."}, {"text": "A dog called Sweep has got a problem."}, {"text": "A girl called Jasmine helps her pet dog."}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант", "questions": [{"q": "Sweep is ___.", "type": "single", "options": [{"text": "a boy"}, {"text": "a dog"}], "correct": [1]}, {"q": "___ can't hear.", "type": "single", "options": [{"text": "Jasmine"}, {"text": "Sweep"}], "correct": [0]}, {"q": "Jasmine has got ___.", "type": "single", "options": [{"text": "one friend"}, {"text": "lots of friends"}], "correct": [1]}, {"q": "Jasmine ___ visit people.", "type": "single", "options": [{"text": "can"}, {"text": "can't"}], "correct": [0]}, {"q": "Jasmine's mum and dad ___ always with her.", "type": "single", "options": [{"text": "are"}, {"text": "aren't"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'match', replace($blk${"title": "Соедини, чтобы получились предложения", "pairs": [{"left": "Jasmine has", "right": "got a problem."}, {"left": "Sweep is Jasmine's", "right": "ears."}, {"left": "Sweep can", "right": "help Jasmine."}, {"left": "Jasmine's best friend", "right": "is a dog."}, {"left": "Jasmine's parents", "right": "are happy."}, {"left": "Jasmine is safe", "right": "with Sweep."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'speaking', replace($blk${"title": "Какие языки ты знаешь? 🎤", "html": "<p>Нажми на микрофон и расскажи, какие языки ты знаешь и какие хочешь выучить.</p><p><i>Пример: I can speak Polish and English. I can't speak Spanish, but I want to learn it. I think sign language is interesting.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Хорошая работа! 🎉</h3><p>Увидимся на следующем уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
