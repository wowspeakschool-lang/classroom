-- Go Getter 1 · Unit 7 · Animals · Homework 4
-- собрано tools/gg1_build.py --lesson u7_hw4
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 7 · Animals', 7
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 7 · Animals');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 7 · Animals';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет-привет! 👋</h2><p>Хочу похвалить тебя за твой труд! Ты молодец, что решил сделать домашнюю работу. Вперёд :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u7/card_buying_ticket.webp\" alt=\"Buying a Ticket\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери правильный ответ", "questions": [{"q": "A: Can I help you? B: ___ a ticket to the museum, please?", "type": "single", "options": [{"text": "Would you like"}, {"text": "Can I have"}], "correct": [1]}, {"q": "A: ___ you like a guide?", "type": "single", "options": [{"text": "Would"}, {"text": "Do"}], "correct": [0]}, {"q": "B: No, ___.", "type": "single", "options": [{"text": "please"}, {"text": "thanks"}], "correct": [1]}, {"q": "A: That's £8.50, please. B: Here ___.", "type": "single", "options": [{"text": "you are"}, {"text": "are you"}], "correct": [0]}, {"q": "A: ___ your tickets. B: Thank you.", "type": "single", "options": [{"text": "They're"}, {"text": "Here are"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'sequence', replace($blk${"title": "Поставь предложения в диалоге в правильном порядке", "image": "@@MEDIA@@gg1/u7/scene_cafe_counter.webp", "items": [{"text": "Attendant: Can I help you?"}, {"text": "Customer: Yes. Can I have a sandwich, please?"}, {"text": "Attendant: Yes, OK. Would you like cheese in it?"}, {"text": "Customer: Yes, please."}, {"text": "Attendant: That's £3.25, please."}, {"text": "Customer: Here you are."}, {"text": "Attendant: Thank you. And here's your sandwich."}, {"text": "Customer: Thanks. Have a nice day!"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски в диалоге. Можешь использовать слова из предыдущих упражнений", "mode": "type", "text": "A: Hello. Can __I__ help you?\nB: Hi. Can I __have__ two tickets for the cinema, please?\nA: Sure. Would you __like__ a bag of popcorn?\nB: Yes, please. Good __idea__!\nA: That's £15, __please__.\nB: __Here__ you are.\nA: Here __are__ your tickets and here's the popcorn. Enjoy the film!\nB: __Thanks|Thank you__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'speaking', replace($blk${"title": "В кассе зоопарка 🎤", "image": "@@MEDIA@@gg1/u7/scene_zoo_ticket_office.webp", "html": "<p>Представь, что ты в кассе зоопарка покупаешь билеты для своей семьи. Нажми на микрофон и разыграй диалог.</p><p><i>Пример: Hello! Can I have three tickets to the zoo, please? — That's eighteen pounds fifty. — Here you are. — Thank you. Here are your tickets!</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Спасибо тебе большое за отличную работу! 🎉</h3><p>Увидимся на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6);
end
$mig$;
