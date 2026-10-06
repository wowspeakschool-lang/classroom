-- Go Getter 1 · Unit 8 · Sport and health · Homework 3
-- собрано tools/gg1_build.py --lesson u8_hw3
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
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Добро пожаловать на домашнее задание! Сегодня мы с тобой закрепим знания, полученные на уроке. Мы будем не только задавать мнооого вопросов, но и отвечать на них. В конце тебя будет ждать дополнительное упражнение — для самых смелых и самых сильных учеников 💪</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u8/card_question_words.webp\" alt=\"Вопросительные слова\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'video', replace($blk${"title": "Хэмми расспрашивает Анну о её лучшей подруге… Как думаешь, откуда она? Посмотри видео и проверь себя! Повторяй вопросы и ответы за героями, чтобы хорошенько запомнить правила.", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'match', replace($blk${"title": "Внимательно посмотри видео ещё раз и соедини вопросы и ответы", "pairs": [{"left": "Who is this girl?", "right": "This is Kimmy."}, {"left": "Where does she live?", "right": "In Hong Kong."}, {"left": "Is she a student?", "right": "I'm not sure..."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Нам дали прочитать интервью с одним из друзей Хэмми… Но все вопросы и ответы перепутались! Найди правильный ответ на каждый вопрос", "questions": [{"q": "When is the football game?", "type": "single", "options": [{"text": "It's on Saturday."}, {"text": "It's great."}], "correct": [0]}, {"q": "Where is my mobile phone?", "type": "single", "options": [{"text": "It's from China."}, {"text": "It's on the table."}], "correct": [1]}, {"q": "Whose bike is in front of the house?", "type": "single", "options": [{"text": "It's my mum's bike."}, {"text": "The bike is green."}], "correct": [0]}, {"q": "How many friends have you got?", "type": "single", "options": [{"text": "Five years old."}, {"text": "Five."}], "correct": [1]}, {"q": "What is in your bag?", "type": "single", "options": [{"text": "There's a notebook."}, {"text": "It's next to the desk."}], "correct": [0]}, {"q": "Who is your English teacher?", "type": "single", "options": [{"text": "Mr Evans is here."}, {"text": "It's Mr Evans."}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку (мы уже видели её на уроке) и выбери правильное вопросительное слово. Ответы после вопросов тебе помогут!", "questions": [{"q": "A: ___ is Dug? B: He's in a shopping centre.", "type": "single", "options": [{"text": "Where"}, {"text": "When"}], "correct": [0], "image": "@@MEDIA@@gg1/u8/dug_autograph.webp"}, {"q": "A: ___ is the woman? B: She's Irina Peters.", "type": "single", "options": [{"text": "Whose"}, {"text": "Who"}], "correct": [1]}, {"q": "A: ___ is her sport? B: It's tennis.", "type": "single", "options": [{"text": "What"}, {"text": "Who"}], "correct": [0]}, {"q": "A: ___ does Dug want? B: He wants her autograph.", "type": "single", "options": [{"text": "Why"}, {"text": "What"}], "correct": [1]}, {"q": "A: ___ mobile phones can you see? B: Two.", "type": "single", "options": [{"text": "How many"}, {"text": "When"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'gaps', replace($blk${"title": "А вот это задание уже посложнее… Догадайся сам, какое слово пропущено!", "mode": "type", "text": "1. A: __What__ is your name? B: Marco.\n2. A: __Where__ are you from? B: I'm from Italy, but I live in London now.\n3. A: __How many__ friends have you got in London? B: A lot! Six or seven.\n4. A: __Who__ is your best friend? B: Jacob. He's my classmate. We want to go to a party today.\n5. A: __Whose__ party is it? B: It's my sister's party! It's her birthday!\n6. A: __When|What time__ is the party? B: It's at five o'clock."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'task', replace($blk${"title": "Интервью со звездой ⭐", "needs_review": true, "html": "<p>А это задание — для самых крутых чемпионов! Представь, что у тебя берут интервью 😉 Ответь на вопросы и почувствуй себя звездой!</p><ol><li>What is your name? <i>(name)</i></li><li>How old are you? <i>(number)</i></li><li>Where are you from? <i>(country)</i></li><li>How many friends have you got? <i>(number)</i></li><li>What is your hobby? <i>(hobby)</i></li><li>What is your favourite school subject? <i>(subject)</i></li><li>Who is your best friend? <i>(name)</i></li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'speaking', replace($blk${"title": "Вопросы другу 🎤", "html": "<p>Задай 4 вопроса другу о его жизни (имя, возраст, спорт, день рождения) и ответь на них. Нажми на микрофон.</p><p><i>Пример: What's your favourite sport? Where do you live? When is your birthday? How many brothers and sisters have you got?</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'quiz', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Выбери подходящее вопросительное слово ⭐", "questions": [{"q": "___ is your birthday? — In May.", "type": "single", "options": [{"text": "Whose"}, {"text": "Where"}, {"text": "Who"}, {"text": "When"}], "correct": [3]}, {"q": "___ do you live? — In Moscow.", "type": "single", "options": [{"text": "Where"}, {"text": "Whose"}, {"text": "What"}, {"text": "When"}], "correct": [0]}, {"q": "___ is your hero? — My dad.", "type": "single", "options": [{"text": "Whose"}, {"text": "Who"}, {"text": "When"}, {"text": "Where"}], "correct": [1]}, {"q": "___ sport do you like? — Tennis.", "type": "single", "options": [{"text": "Who"}, {"text": "Whose"}, {"text": "What"}, {"text": "Where"}], "correct": [2]}, {"q": "___ bike is this? — It's Tom's.", "type": "single", "options": [{"text": "What"}, {"text": "Who"}, {"text": "When"}, {"text": "Whose"}], "correct": [3]}, {"q": "___ sisters have you got? — Two.", "type": "single", "options": [{"text": "How many"}, {"text": "What"}, {"text": "When"}, {"text": "Who"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'match', replace($blk${"title": "Соедини вопрос с ответом ⭐", "pairs": [{"left": "Where do you live?", "right": "In London."}, {"left": "Who is your best friend?", "right": "It's Jacob."}, {"left": "What sport do you like?", "right": "I like volleyball."}, {"left": "When is your birthday?", "right": "It's in June."}, {"left": "How many sisters have you got?", "right": "I've got one sister."}, {"left": "Whose bag is this?", "right": "It's my brother's bag."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11);
end
$mig$;
