-- Go Getter 1 · Unit 7 · Animals · Homework 5
-- собрано tools/gg1_build.py --lesson u7_hw5
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
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_headphones.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Время для домашнего задания! Сначала выучим новые слова — какими бывают животные. Let's go!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'flashcards', replace($blk${"cards": [{"text": "cute", "translation": "милый", "audio_tts": "cute", "image": "@@MEDIA@@gg1/u7/adj_cute.webp"}, {"text": "dangerous", "translation": "опасный", "audio_tts": "dangerous", "image": "@@MEDIA@@gg1/u7/adj_dangerous.webp"}, {"text": "fast", "translation": "быстрый", "audio_tts": "fast", "image": "@@MEDIA@@gg1/u7/adj_fast.webp"}, {"text": "slow", "translation": "медленный", "audio_tts": "slow", "image": "@@MEDIA@@gg1/u7/adj_slow.webp"}, {"text": "strong", "translation": "сильный", "audio_tts": "strong", "image": "@@MEDIA@@gg1/u7/adj_strong.webp"}, {"text": "ugly", "translation": "уродливый", "audio_tts": "ugly", "image": "@@MEDIA@@gg1/u7/adj_ugly.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Как по-английски «милый»?", "type": "single", "options": [{"text": "dangerous"}, {"text": "cute"}, {"text": "slow"}, {"text": "fast"}], "correct": [1]}, {"q": "Как по-английски «опасный»?", "type": "single", "options": [{"text": "slow"}, {"text": "dangerous"}, {"text": "fast"}, {"text": "strong"}], "correct": [1]}, {"q": "Как по-английски «быстрый»?", "type": "single", "options": [{"text": "fast"}, {"text": "strong"}, {"text": "slow"}, {"text": "ugly"}], "correct": [0]}, {"q": "Как по-английски «медленный»?", "type": "single", "options": [{"text": "cute"}, {"text": "ugly"}, {"text": "strong"}, {"text": "slow"}], "correct": [3]}, {"q": "Как по-английски «сильный»?", "type": "single", "options": [{"text": "dangerous"}, {"text": "cute"}, {"text": "ugly"}, {"text": "strong"}], "correct": [3]}, {"q": "Как по-английски «уродливый»?", "type": "single", "options": [{"text": "fast"}, {"text": "cute"}, {"text": "ugly"}, {"text": "dangerous"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'match', replace($blk${"title": "Соедини картинку и слово", "pairs": [{"left_image": "@@MEDIA@@gg1/u7/adj_cute.webp", "right": "cute", "right_audio_tts": "cute"}, {"left_image": "@@MEDIA@@gg1/u7/adj_dangerous.webp", "right": "dangerous", "right_audio_tts": "dangerous"}, {"left_image": "@@MEDIA@@gg1/u7/adj_fast.webp", "right": "fast", "right_audio_tts": "fast"}, {"left_image": "@@MEDIA@@gg1/u7/adj_slow.webp", "right": "slow", "right_audio_tts": "slow"}, {"left_image": "@@MEDIA@@gg1/u7/adj_strong.webp", "right": "strong", "right_audio_tts": "strong"}, {"left_image": "@@MEDIA@@gg1/u7/adj_ugly.webp", "right": "ugly", "right_audio_tts": "ugly"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<h3>Вторая часть домашнего задания 👋</h3><p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u7/card_adjectives.webp\" alt=\"Adjectives\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку и выбери, верно утверждение или нет", "questions": [{"q": "It's fast.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0], "image": "@@MEDIA@@gg1/u7/animal_cat.webp"}, {"q": "It's strong.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [1], "image": "@@MEDIA@@gg1/u7/animal_fish.webp"}, {"q": "It's dangerous.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0], "image": "@@MEDIA@@gg1/u7/animal_lion.webp"}, {"q": "It's cute.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [1], "image": "@@MEDIA@@gg1/u7/animal_spider.webp"}, {"q": "It's ugly.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0], "image": "@@MEDIA@@gg1/u7/adj_ugly.webp"}, {"q": "It's slow.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [1], "image": "@@MEDIA@@gg1/u7/animal_tiger.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'quiz', replace($blk${"title": "Какие слова описывают акул лучше всего? Отметь их", "questions": [{"q": "Sharks are… / Sharks have got…", "type": "multiple", "image": "@@MEDIA@@gg1/u7/adj_dangerous.webp", "options": [{"text": "dangerous"}, {"text": "cute face"}, {"text": "fast"}, {"text": "strong"}, {"text": "big ears"}, {"text": "lots of teeth"}, {"text": "long body"}], "correct": [0, 2, 3, 5, 6]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p><b>Прочитай текст и выполни задания ниже.</b></p><p><img src=\"@@MEDIA@@gg1/u7/scene_shark.webp\" alt=\"Sharks\" style=\"height:240px\"></p><h3>All about sharks</h3><p><b>Are all sharks dangerous to people?</b><br><i>No, they aren't. Most sharks are not dangerous to us, but we are very dangerous to sharks! Why? Sharks don't often eat people, but in some countries people eat sharks.</i></p><p><b>So, what do sharks usually eat?</b><br><i>They eat fish and other sea animals. They sometimes eat other sharks.</i></p><p><b>Are they clever? What can they do?</b><br><i>Sharks are strong and they are fast swimmers. They can see and smell under water very well.</i></p><p><b>Can they hear?</b><br><i>Good question. It's amazing. They haven't got ears like ours, but they can hear fish from hundreds of kilometres away!</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай текст и выбери правильные варианты ответов", "questions": [{"q": "Sharks aren't ___ dangerous to people.", "type": "single", "options": [{"text": "sometimes"}, {"text": "often"}], "correct": [1]}, {"q": "People ___ a problem for sharks.", "type": "single", "options": [{"text": "are"}, {"text": "aren't"}], "correct": [0]}, {"q": "Sharks don't often eat ___.", "type": "single", "options": [{"text": "sea animals"}, {"text": "other sharks"}], "correct": [1]}, {"q": "They ___ very good eyes.", "type": "single", "options": [{"text": "have got"}, {"text": "haven't got"}], "correct": [0]}, {"q": "They ___ hear very well.", "type": "single", "options": [{"text": "can't"}, {"text": "can"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'task', replace($blk${"title": "Прочитай текст ещё раз и ответь на вопросы", "needs_review": true, "html": "<ol><li>What do sharks usually eat?</li><li>Do they often eat people?</li><li>Can they smell well?</li><li>What can they hear?</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_jump.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа! Спасибо тебе большое! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
