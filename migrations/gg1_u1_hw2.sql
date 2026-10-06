-- Go Getter 1 · Unit 1 · Family and friends · Homework 2
-- собрано tools/gg1_build.py --lesson u1_hw2
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 1 · Family and friends', 1
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 1 · Family and friends');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 1 · Family and friends';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>На занятии мы выучили новый глагол: <b>to be</b>. Давай потренируемся и будем использовать его правильно? Приступим!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u1/card_to_be.webp\" alt=\"to be\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку и выбери правильный вариант ответа", "questions": [{"q": "Look! We ___ at a party.", "type": "single", "options": [{"text": "am"}, {"text": "are"}, {"text": "is"}], "correct": [1], "image": "@@MEDIA@@gg1/u1/place_party.webp"}, {"q": "Kate ___ 5 today.", "type": "single", "options": [{"text": "am"}, {"text": "are"}, {"text": "is"}], "correct": [2]}, {"q": "I ___ happy.", "type": "single", "options": [{"text": "am"}, {"text": "are"}, {"text": "is"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку и выбери правильный вариант ответа", "questions": [{"q": "She ___ a teacher.", "type": "single", "options": [{"text": "are"}, {"text": "is"}, {"text": "am"}], "correct": [1], "image": "@@MEDIA@@gg1/u4/english_class.webp"}, {"q": "He ___ a student.", "type": "single", "options": [{"text": "am"}, {"text": "are"}, {"text": "is"}], "correct": [2]}, {"q": "They ___ at school.", "type": "single", "options": [{"text": "are"}, {"text": "am"}, {"text": "is"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски словами am, is или are", "mode": "drag", "text": "Harry: Hi. I am Harry.\nJack: Hi, Harry. I __am__ Jack. You __are__ in class 2 with me. Welcome!\nHarry: Thanks.\nJack: This is Tony. He __is__ my classmate. We are best friends too. Mrs Lee and Mr Brown __are__ my favourite teachers."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'match', replace($blk${"title": "Соедини полную и краткую формы", "pairs": [{"left": "we are", "right": "we're"}, {"left": "Tom is", "right": "Tom's"}, {"left": "I am", "right": "I'm"}, {"left": "he is", "right": "he's"}, {"left": "she is", "right": "she's"}, {"left": "they are", "right": "they're"}, {"left": "you are", "right": "you're"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'speaking', replace($blk${"title": "Мой друг 🎤", "html": "<p>Нажми на микрофон, представься и расскажи о своём друге или подруге. Используй глагол to be (I'm, He's, She's) и местоимения my, your, his, her.</p><p><i>Пример: Hi! I'm Anna. I'm ten. This is my friend. His name's Tom. He's eleven. His mum is Maria.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'quiz', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Выбери правильный вариант ⭐", "questions": [{"q": "I ___ eleven years old.", "type": "single", "options": [{"text": "am"}, {"text": "is"}, {"text": "are"}], "correct": [0]}, {"q": "My granny ___ seventy.", "type": "single", "options": [{"text": "am"}, {"text": "is"}, {"text": "are"}], "correct": [1]}, {"q": "We ___ at school.", "type": "single", "options": [{"text": "is"}, {"text": "am"}, {"text": "are"}], "correct": [2]}, {"q": "You ___ my best friend.", "type": "single", "options": [{"text": "are"}, {"text": "is"}, {"text": "am"}], "correct": [0]}, {"q": "His name ___ Lucas.", "type": "single", "options": [{"text": "am"}, {"text": "is"}, {"text": "are"}], "correct": [1]}, {"q": "My cousins ___ from Spain.", "type": "single", "options": [{"text": "is"}, {"text": "am"}, {"text": "are"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски ⭐", "mode": "drag", "text": "This is my sister. __Her__ name __is__ Lucy. She is eight.\nMy brother and I __are__ at home today.\nTom, is this __your__ bag?\nThis is Ben. __His__ mum is a teacher.\n__My__ name is Anna and I __am__ ten."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>У тебя отлично получилось! 🎉</h3><p>Увидимся на занятии! Bye!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9);
end
$mig$;
