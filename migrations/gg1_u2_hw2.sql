-- Go Getter 1 · Unit 2 · My things · Homework 2
-- собрано tools/gg1_build.py --lesson u2_hw2
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 2 · My things', 2
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 2 · My things');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 2 · My things';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 2', 'homework',
         null, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>На занятии мы выучили много новых слов! Выполни все задания, чтобы запомнить их на все 100!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'flashcards', replace($blk${"cards": [{"text": "big", "translation": "большой", "audio_tts": "big", "image": "@@MEDIA@@gg1/u2/adj_big_small.webp"}, {"text": "small", "translation": "маленький", "audio_tts": "small", "image": "@@MEDIA@@gg1/u2/adj_big_small.webp"}, {"text": "long", "translation": "длинный", "audio_tts": "long", "image": "@@MEDIA@@gg1/u2/adj_long_short.webp"}, {"text": "short", "translation": "короткий", "audio_tts": "short", "image": "@@MEDIA@@gg1/u2/adj_long_short.webp"}, {"text": "new", "translation": "новый", "audio_tts": "new", "image": "@@MEDIA@@gg1/u2/adj_new_old.webp"}, {"text": "old", "translation": "старый", "audio_tts": "old", "image": "@@MEDIA@@gg1/u2/adj_new_old.webp"}, {"text": "cool", "translation": "классный", "audio_tts": "cool", "image": "@@MEDIA@@gg1/u2/adj_cool_boring.webp"}, {"text": "boring", "translation": "скучный", "audio_tts": "boring", "image": "@@MEDIA@@gg1/u2/adj_cool_boring.webp"}, {"text": "too", "translation": "слишком", "audio_tts": "too", "image": "@@MEDIA@@gg1/u2/adj_too_big.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери слово, которое подходит по смыслу", "questions": [{"q": "An elephant is ___.", "type": "single", "options": [{"text": "small"}, {"text": "big"}, {"text": "short"}], "correct": [1]}, {"q": "A mouse is ___.", "type": "single", "options": [{"text": "big"}, {"text": "long"}, {"text": "small"}], "correct": [2]}, {"q": "A giraffe's neck is very ___.", "type": "single", "options": [{"text": "long"}, {"text": "small"}, {"text": "short"}], "correct": [0]}, {"q": "This skirt isn't long. It's ___.", "type": "single", "options": [{"text": "big"}, {"text": "short"}, {"text": "long"}], "correct": [1]}, {"q": "My bike isn't old. It's ___.", "type": "single", "options": [{"text": "boring"}, {"text": "old"}, {"text": "new"}], "correct": [2]}, {"q": "These trainers aren't new. They're ___.", "type": "single", "options": [{"text": "old"}, {"text": "new"}, {"text": "cool"}], "correct": [0]}, {"q": "This film isn't cool. It's ___.", "type": "single", "options": [{"text": "new"}, {"text": "boring"}, {"text": "cool"}], "correct": [1]}, {"q": "Your skateboard isn't boring. It's ___!", "type": "single", "options": [{"text": "short"}, {"text": "boring"}, {"text": "cool"}], "correct": [2]}, {"q": "These jeans are ___ big for me.", "type": "single", "options": [{"text": "too"}, {"text": "new"}, {"text": "big"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с противоположным значением", "pairs": [{"left": "big", "right": "small"}, {"left": "long", "right": "short"}, {"left": "new", "right": "old"}, {"left": "cool", "right": "boring"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски", "mode": "drag", "text": "This jacket is __too__ big for the hanger.\nMy scarf is very __long__.\nThese trainers are __old__ and dirty.\nMy new cap is __cool__!\nThis T-shirt is very __small__.\nThat grey cap is __boring__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<h3>Hello! 👋</h3><p>На занятии мы говорили о предметах, которые находятся далеко или близко. Повторим?</p><p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u2/card_adjectives.webp\" alt=\"Adjectives\" style=\"max-width:100%\"></p><p><img src=\"@@MEDIA@@gg1/u2/card_this_that.webp\" alt=\"this / that / these / those\" style=\"max-width:100%\"></p><p><img src=\"@@MEDIA@@gg1/u2/card_too.webp\" alt=\"too\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'match', replace($blk${"title": "Соедини слово и картинку", "pairs": [{"left": "This", "right_image": "@@MEDIA@@gg1/u2/dem_this.webp"}, {"left": "These", "right_image": "@@MEDIA@@gg1/u2/dem_these.webp"}, {"left": "That", "right_image": "@@MEDIA@@gg1/u2/dem_that.webp"}, {"left": "Those", "right_image": "@@MEDIA@@gg1/u2/dem_those.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'sort', replace($blk${"title": "Какие слова означают, что предмет далеко, а какие — близко?", "groups": [{"name": "Далеко", "items": [{"text": "That"}, {"text": "Those"}]}, {"name": "Близко", "items": [{"text": "This"}, {"text": "These"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'sort', replace($blk${"title": "Какие слова означают, что предмет один, а какие — что их много?", "groups": [{"name": "Один", "items": [{"text": "This"}, {"text": "That"}]}, {"name": "Много", "items": [{"text": "These"}, {"text": "Those"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'speaking', replace($blk${"title": "Моя одежда и чужая 🎤", "html": "<p>Нажми на микрофон и опиши свою и чужую одежду. Используй this / that / these / those и прилагательные (new, old, big, small, cool).</p><p><i>Пример: This is my new T-shirt. It's cool. Those are my old shoes. They're small. These trainers are blue.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'quiz', replace($blk${"title": "Давай теперь поиграем с этими словами! Выбери правильное слово", "questions": [{"q": "___ T-shirt is blue.", "type": "single", "options": [{"text": "That"}, {"text": "Those"}, {"text": "This"}, {"text": "These"}], "correct": [2], "image": "@@MEDIA@@gg1/u2/dem_this.webp"}, {"q": "___ T-shirt is far away.", "type": "single", "options": [{"text": "Those"}, {"text": "These"}, {"text": "This"}, {"text": "That"}], "correct": [3], "image": "@@MEDIA@@gg1/u2/dem_that.webp"}, {"q": "___ T-shirts are new.", "type": "single", "options": [{"text": "These"}, {"text": "That"}, {"text": "Those"}, {"text": "This"}], "correct": [0], "image": "@@MEDIA@@gg1/u2/dem_these.webp"}, {"q": "___ T-shirts are blue.", "type": "single", "options": [{"text": "These"}, {"text": "Those"}, {"text": "That"}, {"text": "This"}], "correct": [1], "image": "@@MEDIA@@gg1/u2/dem_those.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'match', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Соедини начало и конец предложения ⭐", "pairs": [{"left": "An elephant isn't small. It's", "right": "big."}, {"left": "A mouse isn't big. It's", "right": "small."}, {"left": "Rapunzel's hair is very", "right": "long."}, {"left": "My hair isn't long. It's", "right": "short."}, {"left": "My shoes are from the shop today. They're", "right": "new."}, {"left": "This castle is 500 years", "right": "old."}, {"left": "I love this game! It's", "right": "cool."}, {"left": "I don't like this film. It's", "right": "boring."}, {"left": "My dad's T-shirt is", "right": "too big for me."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["These", "jeans", "are", "blue."], "sentence": "These jeans are blue.", "audio_tts": "These jeans are blue."}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["That", "dress", "is", "too", "long."], "sentence": "That dress is too long.", "audio_tts": "That dress is too long."}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке ⭐", "words": ["Those", "trainers", "are", "new!"], "sentence": "Those trainers are new!", "audio_tts": "Those trainers are new!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_jump.webp\" alt=\"\" style=\"height:180px\"></p><h3>У тебя отлично получилось! 🎉</h3><p>Увидимся на занятии! Bye!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 15);
end
$mig$;
