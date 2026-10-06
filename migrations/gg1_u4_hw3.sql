-- Go Getter 1 · Unit 4 · Look at me · Homework 3
-- собрано tools/gg1_build.py --lesson u4_hw3
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 4 · Look at me', 4
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 4 · Look at me');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 4 · Look at me';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hey there! 👋</h2><p>Привет, дорогой друг! Сегодня мы продолжим увлекательное путешествие в мир английского языка и будем вместе упражняться в новой теме! Удачи!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u4/card_have_got_questions.webp\" alt=\"have got: вопросы\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'hotspot', replace($blk${"title": "Давай вспомним слова, которые учили! Подпиши части тела на картинке", "mode": "label", "image": "@@MEDIA@@gg1/u4/girl_jumping.webp", "points": [{"x": 44.3, "y": 31.7, "text": "nose"}, {"x": 41.4, "y": 14.7, "text": "blond hair"}, {"x": 54.3, "y": 34.0, "text": "mouth"}, {"x": 66.9, "y": 32.6, "text": "ear"}, {"x": 34.7, "y": 85.2, "text": "leg"}, {"x": 64.9, "y": 76.2, "text": "foot"}, {"x": 5.6, "y": 25.4, "text": "finger"}, {"x": 47.0, "y": 41.5, "text": "neck"}], "extras": []}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Какой ты молодец! Лови награду! 🏅</h3><p>И приступим к кое-чему новенькому 😉</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'video', replace($blk${"title": "Посмотри видео и запомни, как мы задаём вопросы с have got", "url": "", "provider": "youtube"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'match', replace($blk${"title": "Давай найдём ответы на вопросы. Соедини половинки", "pairs": [{"left": "Have you got a brother?", "right": "No, I haven't. But I've got a sister."}, {"left": "Has she got an interesting book?", "right": "Yes, she has. It's about Harry Potter."}, {"left": "Has your mother got a car?", "right": "No, she hasn't. She usually takes a taxi."}, {"left": "Has Mrs Smith got a beautiful garden?", "right": "Yes, she has. There are lots of different flowers."}, {"left": "Has your friend got a skateboard?", "right": "Yes, he has. He loves it."}, {"left": "Has your family got a big house?", "right": "No, we haven't. We live in a small flat near the station."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><b>Посмотри на картинку. Это монстры Зог (Zog) и Боб (Bob). Зог высокий, Боб круглый.</b></p><p><img src=\"@@MEDIA@@gg1/u4/scene_two_monsters.webp\" alt=\"Zog and Bob\" style=\"height:300px\"></p><p><i>Пример: Has Zog got three legs? — No, he hasn't.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на Зога и Боба и выбери правильный ответ", "questions": [{"q": "Have Zog and Bob got green skin?", "type": "single", "options": [{"text": "No, they haven't."}, {"text": "Yes, they have."}], "correct": [1]}, {"q": "Has Zog got a long neck?", "type": "single", "options": [{"text": "Yes, he has."}, {"text": "No, he hasn't."}], "correct": [0]}, {"q": "Has Bob got long hair?", "type": "single", "options": [{"text": "Yes, he has."}, {"text": "No, he hasn't."}], "correct": [1]}, {"q": "Have they got big eyes?", "type": "single", "options": [{"text": "Yes, they have."}, {"text": "No, they haven't."}], "correct": [0]}, {"q": "Has Bob got a big mouth?", "type": "single", "options": [{"text": "No, he hasn't."}, {"text": "Yes, he has."}], "correct": [1]}, {"q": "Has Zog got short legs?", "type": "single", "options": [{"text": "No, he hasn't."}, {"text": "Yes, he has."}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова по порядку, чтобы получились вопросы", "words": ["Has", "Zog", "got", "a", "long", "neck?"], "sentence": "Has Zog got a long neck?", "audio_tts": "Has Zog got a long neck?", "image": "@@MEDIA@@gg1/u4/scene_two_monsters.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова по порядку, чтобы получились вопросы", "words": ["Has", "Bob", "got", "a", "big", "head?"], "sentence": "Has Bob got a big head?", "audio_tts": "Has Bob got a big head?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова по порядку, чтобы получились вопросы", "words": ["Have", "they", "got", "big", "eyes?"], "sentence": "Have they got big eyes?", "audio_tts": "Have they got big eyes?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова по порядку, чтобы получились вопросы", "words": ["Have", "they", "got", "green", "skin?"], "sentence": "Have they got green skin?", "audio_tts": "Have they got green skin?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'speaking', replace($blk${"title": "Ответь на вопросы 🎤", "html": "<p>Мы тобой гордимся! Давай выполним ещё одно задание. Нажми на микрофон и ответь на вопросы:</p><ol><li>Have you got a pet? Which one?</li><li>Has your mother got dark hair?</li><li>Has your father got a car?</li><li>Have you got any brothers or sisters?</li><li>Has your friend got an interesting book?</li></ol>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'quiz', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Выбери правильный вариант ⭐", "questions": [{"q": "___ you got a sister?", "type": "single", "options": [{"text": "Have"}, {"text": "Has"}], "correct": [0]}, {"q": "___ your dad got a car?", "type": "single", "options": [{"text": "Have"}, {"text": "Has"}], "correct": [1]}, {"q": "Has she got blue eyes? — Yes, she ___.", "type": "single", "options": [{"text": "have"}, {"text": "is"}, {"text": "has"}], "correct": [2]}, {"q": "Have they got a dog? — No, they ___.", "type": "single", "options": [{"text": "haven't"}, {"text": "aren't"}, {"text": "hasn't"}], "correct": [0]}, {"q": "___ it got a long tail?", "type": "single", "options": [{"text": "Has"}, {"text": "Have"}], "correct": [0]}, {"q": "Have you got curly hair? — No, I ___.", "type": "single", "options": [{"text": "hasn't"}, {"text": "don't"}, {"text": "haven't"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильное слово ⭐", "questions": [{"q": "I've got a cat. ___ cat is black.", "type": "single", "options": [{"text": "Its"}, {"text": "My"}, {"text": "Your"}], "correct": [1]}, {"q": "You've got a new bike. ___ bike is cool.", "type": "single", "options": [{"text": "Their"}, {"text": "Our"}, {"text": "Your"}], "correct": [2]}, {"q": "He's got a sister. ___ sister is ten.", "type": "single", "options": [{"text": "His"}, {"text": "Her"}, {"text": "Its"}], "correct": [0]}, {"q": "She's got a dog. ___ dog is funny.", "type": "single", "options": [{"text": "Our"}, {"text": "Her"}, {"text": "His"}], "correct": [1]}, {"q": "The dog has got big ears. ___ ears are brown.", "type": "single", "options": [{"text": "Our"}, {"text": "Their"}, {"text": "Its"}], "correct": [2]}, {"q": "We've got a house. ___ house is big.", "type": "single", "options": [{"text": "Our"}, {"text": "Their"}, {"text": "Your"}], "correct": [0]}, {"q": "They've got a car. ___ car is red.", "type": "single", "options": [{"text": "Its"}, {"text": "Their"}, {"text": "Our"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>Спасибо тебе за твою усердную работу! 🎉</h3><p>До новых встреч! Bye!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 15);
end
$mig$;
