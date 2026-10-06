-- Go Getter 1 · Unit 5 · I can do it · Homework 3
-- собрано tools/gg1_build.py --lesson u5_hw3
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
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Здорово, что ты решил сделать домашнюю работу. Ты большой молодец!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u5/card_can_questions.webp\" alt=\"Can questions & short answers\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'exact_input', replace($blk${"title": "Прочитай предложения и напиши к ним вопросы. Пример: They can swim. → Can they swim?", "items": [{"prompt": "I can draw.", "accept": ["Can you draw?", "Can you draw"]}, {"prompt": "Tom can run fast.", "accept": ["Can Tom run fast?", "Can Tom run fast"]}, {"prompt": "May can sing well.", "accept": ["Can May sing well?", "Can May sing well"]}, {"prompt": "We can help.", "accept": ["Can we help?", "Can we help", "Can you help?", "Can you help"]}, {"prompt": "The cat can climb.", "accept": ["Can the cat climb?", "Can the cat climb"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'task', replace($blk${"title": "Посмотри на картинку и ответь на вопросы", "needs_review": true, "image": "@@MEDIA@@gg1/u5/superdug_beach.webp", "html": "<p><i>Пример: Can Kit and Dug see the boat? — Yes, they can.</i></p><ol><li>Can the boy and girl swim?</li><li>Can their mum swim?</li><li>Can Dug swim?</li><li>Can the small dog help?</li><li>Can Dug help?</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'task', replace($blk${"title": "Напиши вопросы из слов ниже и ответь на них", "needs_review": true, "html": "<p><i>Пример: you / fix a bike? → Can you fix a bike? Yes, I can.</i></p><ol><li>you / play volleyball?</li><li>your mum / speak English?</li><li>your classmates / speak Spanish?</li><li>you / ride a horse?</li><li>your best friend / play the piano?</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "Посмотри на картинки и заполни пропуски нужными словами", "mode": "drag", "image": "@@MEDIA@@gg1/u5/fruits_dance.webp", "text": "1. A: Can you __see__ those red apples?\nB: Yes, I __can__.\nA: Help me, please? I'm too short.\nB: No problem.\n2. A: __Can__ they __dance__?\nB: Yes, they can.\nA: Can the girl play __the piano__ too?\nB: No, she __can't__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'speaking', replace($blk${"title": "Спроси друга 🎤", "html": "<p>Задай 3 вопроса другу про его умения и ответь на них. Нажми на микрофон.</p><p><i>Пример: Can you swim? Yes, I can. Can you sing? No, I can't. Can you ride a horse? No, I can't, but my sister can.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'match', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Выбери подходящий ответ ⭐", "pairs": [{"left": "Can you swim?", "right": "Yes, I can."}, {"left": "Can he fly?", "right": "No, he can't."}, {"left": "Can they cook?", "right": "Yes, they can."}, {"left": "Can she sing?", "right": "No, she can't."}, {"left": "Can it jump?", "right": "Yes, it can."}, {"left": "Can we play football here?", "right": "No, we can't."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["Can", "your", "sister", "ride", "a", "horse?"], "sentence": "Can your sister ride a horse?", "audio_tts": "Can your sister ride a horse?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["What", "can", "your", "dog", "do?"], "sentence": "What can your dog do?", "audio_tts": "What can your dog do?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["Yes,", "she", "can."], "sentence": "Yes, she can.", "audio_tts": "Yes, she can."}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты проделал отличную работу! 🎉</h3><p>Здорово! Молодец!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11);
end
$mig$;
