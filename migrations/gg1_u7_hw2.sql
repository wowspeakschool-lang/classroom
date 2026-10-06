-- Go Getter 1 · Unit 7 · Animals · Homework 2
-- собрано tools/gg1_build.py --lesson u7_hw2
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
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Сегодня мы с тобой закрепим знания, полученные на уроке, и ты без проблем сможешь использовать время Present Simple в отрицательных предложениях. В конце тебя будет ждать дополнительное упражнение — для самых смелых и самых сильных учеников 💪</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u7/card_ps_negative.webp\" alt=\"Present Simple — Negative\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'text', replace($blk${"html": "<p>Посмотри на картинку и попробуй угадать: <b>Does Hammy go to school?</b> Посмотри видео и проверь, угадал ли ты. Повторяй вопросы и ответы за героями, чтобы хорошенько запомнить правила.</p><p><img src=\"@@MEDIA@@gg1/u7/hammy.webp\" alt=\"Hammy\" style=\"height:220px\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'video', replace($blk${"title": "Does Hammy go to school?", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Теперь пришло время практики! Выбери правильный вариант. Смотри на значок перед предложением: ❌ — отрицательное предложение, ✅ — утвердительное", "questions": [{"q": "✅ My puppy ___ TV.", "type": "single", "options": [{"text": "doesn't like"}, {"text": "like"}, {"text": "don't like"}, {"text": "likes"}], "correct": [3]}, {"q": "❌ Cats ___ cupcakes.", "type": "single", "options": [{"text": "don't eat"}, {"text": "eat"}, {"text": "eats"}, {"text": "doesn't eat"}], "correct": [0]}, {"q": "✅ My friend ___ in the garden.", "type": "single", "options": [{"text": "play"}, {"text": "plays"}, {"text": "doesn't play"}, {"text": "don't play"}], "correct": [1]}, {"q": "❌ My sister ___ her room.", "type": "single", "options": [{"text": "tidy"}, {"text": "don't tidy"}, {"text": "doesn't tidy"}, {"text": "tidies"}], "correct": [2]}, {"q": "✅ Joe and Adam ___ after school.", "type": "single", "options": [{"text": "hangs out"}, {"text": "doesn't hang out"}, {"text": "don't hang out"}, {"text": "hang out"}], "correct": [3]}, {"q": "❌ We ___ to school on Sundays.", "type": "single", "options": [{"text": "don't go"}, {"text": "go"}, {"text": "goes"}, {"text": "doesn't go"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "Впиши в пропуски слова, раскрыв скобки. Тебе нужна отрицательная форма. Посмотри, как это сделано в первом предложении", "mode": "type", "text": "1. My pet doesn't like (not like) apples.\n2. I __don't tidy|do not tidy|don’t tidy__ (not tidy) my room every day.\n3. We __don't watch|do not watch|don’t watch__ (not watch) TV before dinner.\n4. My little sister __doesn't go|does not go|doesn’t go__ (not go) to school.\n5. You __don't like|do not like|don’t like__ (not like) pop music.\n6. My cousin __doesn't speak|does not speak|doesn’t speak__ (not speak) French."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'task', replace($blk${"title": "Исправь предложения по таблице ✏️", "needs_review": true, "image": "@@MEDIA@@gg1/u7/table_routines.webp", "html": "<p>Внимательно посмотри на таблицу: в предложениях ниже ошибки! Перепиши их так, чтобы они соответствовали таблице.</p><p><i>Например: Jen, Alex and Dad get up early. — в таблице совсем наоборот! Правильно: Jen, Alex and Dad don't get up early.</i></p><ol><li>Dad gets up early.</li><li>Jen and Alex don't play computer games.</li><li>Mum and Dad play computer games.</li><li>Mum doesn't listen to classical music.</li><li>Jen listens to classical music.</li></ol>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'task', replace($blk${"title": "Задание со звёздочкой ⭐ (дополнительный балл)", "needs_review": true, "html": "<p>Напиши 3 предложения о себе и 3 предложения о своём члене семьи, друге или даже учителе! Что вы обычно НЕ делаете в повседневной жизни?</p><p><i>Посмотри, это мои предложения: I don't get up at 6 o'clock. I don't watch TV in the morning. I don't read a magazine before sleeping. My best friend Anna doesn't get up at 10 o'clock. She doesn't play computer games before school. She doesn't have lunch at 8 o'clock in the evening.</i></p><p>Обрати внимание на вспомогательный глагол, когда я рассказываю о своей подруге ;)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'match', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Соедини утвердительное предложение с отрицательным ⭐", "pairs": [{"left": "I like snakes.", "right": "I don't like snakes."}, {"left": "My brother eats fish.", "right": "My brother doesn't eat fish."}, {"left": "Elephants fly.", "right": "Elephants don't fly."}, {"left": "A kangaroo jumps.", "right": "A kangaroo doesn't jump."}, {"left": "We go to the zoo on Sundays.", "right": "We don't go to the zoo on Sundays."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ⭐", "questions": [{"q": "Monkeys ___ live in the sea.", "type": "single", "options": [{"text": "doesn't"}, {"text": "don't"}], "correct": [1], "image": "@@MEDIA@@gg1/u7/animal_monkey.webp"}, {"q": "A lion ___ eat grass.", "type": "single", "options": [{"text": "doesn't"}, {"text": "don't"}], "correct": [0], "image": "@@MEDIA@@gg1/u7/animal_lion.webp"}, {"q": "Fish ___ walk.", "type": "single", "options": [{"text": "doesn't"}, {"text": "don't"}], "correct": [1], "image": "@@MEDIA@@gg1/u7/animal_fish.webp"}, {"q": "A snake ___ have legs.", "type": "single", "options": [{"text": "doesn't"}, {"text": "don't"}], "correct": [0], "image": "@@MEDIA@@gg1/u7/animal_snake.webp"}, {"q": "Giraffes ___ eat meat.", "type": "single", "options": [{"text": "doesn't"}, {"text": "don't"}], "correct": [1], "image": "@@MEDIA@@gg1/u7/animal_giraffe.webp"}, {"q": "My cat doesn't ___ milk.", "type": "single", "options": [{"text": "like"}, {"text": "likes"}], "correct": [0], "image": "@@MEDIA@@gg1/u7/animal_cat.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ура! Ты справился с домашней работой. Ты молодец! 🎉</h3><p>Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
