-- Go Getter 1 · Unit 4 · Look at me · Test
-- собрано tools/gg1_build.py --lesson u4_test
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
  select v_unit, 'Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'match', replace($blk${"title": "Соедини слова и картинки", "pairs": [{"left": "eyes", "right_image": "@@MEDIA@@gg1/u4/body_eyes.webp"}, {"left": "fingers", "right_image": "@@MEDIA@@gg1/u4/body_fingers.webp"}, {"left": "toes", "right_image": "@@MEDIA@@gg1/u4/body_toes.webp"}, {"left": "spiky", "right_image": "@@MEDIA@@gg1/u4/hair_spiky.webp"}, {"left": "teeth", "right_image": "@@MEDIA@@gg1/u4/body_teeth.webp"}, {"left": "curly", "right_image": "@@MEDIA@@gg1/u4/hair_curly.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'exact_input', replace($blk${"title": "Посмотри на картинку и впиши слово целиком", "items": [{"prompt": "c_ev_r", "accept": ["clever", "Clever"], "image": "@@MEDIA@@gg1/u4/pers_clever.webp"}, {"prompt": "fr_endl_", "accept": ["friendly", "Friendly"], "image": "@@MEDIA@@gg1/u4/pers_friendly.webp"}, {"prompt": "f_n_y", "accept": ["funny", "Funny"], "image": "@@MEDIA@@gg1/u4/pers_funny.webp"}, {"prompt": "hel_ful", "accept": ["helpful", "Helpful"], "image": "@@MEDIA@@gg1/u4/pers_helpful.webp"}, {"prompt": "n_ce", "accept": ["nice", "Nice"], "image": "@@MEDIA@@gg1/u4/pers_nice.webp"}, {"prompt": "sp_rty", "accept": ["sporty", "Sporty"], "image": "@@MEDIA@@gg1/u4/pers_sporty.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалоги и выбери пропущенные слова", "questions": [{"q": "A: ___ your brother got big feet?", "type": "single", "options": [{"text": "Haves"}, {"text": "Has"}, {"text": "Have"}], "correct": [1], "image": "@@MEDIA@@gg1/u4/body_feet.webp"}, {"q": "A: Has your brother got big feet? B: No, he ___.", "type": "single", "options": [{"text": "hasn't"}, {"text": "has"}, {"text": "have"}, {"text": "haven't"}], "correct": [0]}, {"q": "A: ___ they got homework today?", "type": "single", "options": [{"text": "Have"}, {"text": "Has"}, {"text": "Haves"}], "correct": [0], "image": "@@MEDIA@@gg1/u4/homework_diary.webp"}, {"q": "A: Have they got homework today? B: Yes, they ___.", "type": "single", "options": [{"text": "hasn't"}, {"text": "haven't"}, {"text": "have"}, {"text": "has"}], "correct": [2]}, {"q": "Jane ___ a cat, but she has got a rabbit.", "type": "single", "options": [{"text": "haven't got"}, {"text": "hasn't got"}], "correct": [1], "image": "@@MEDIA@@gg1/u4/rabbit.webp"}, {"q": "Jane hasn't got a cat, but she ___ got a rabbit.", "type": "single", "options": [{"text": "has"}, {"text": "haves"}, {"text": "have"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери пропущенное слово", "questions": [{"q": "This is Jane and this is ___ cat.", "type": "single", "options": [{"text": "her"}, {"text": "our"}, {"text": "their"}], "correct": [0]}, {"q": "We have a book. This is ___ book.", "type": "single", "options": [{"text": "her"}, {"text": "our"}, {"text": "their"}], "correct": [1]}, {"q": "They have a car. This is ___ car.", "type": "single", "options": [{"text": "her"}, {"text": "our"}, {"text": "their"}], "correct": [2]}, {"q": "My granny ___ curly hair.", "type": "single", "options": [{"text": "has got"}, {"text": "have got"}, {"text": "haves got"}], "correct": [0], "image": "@@MEDIA@@gg1/u4/granny_curly.webp"}, {"q": "A: ___ you got an English class today?", "type": "single", "options": [{"text": "Haves"}, {"text": "Have"}, {"text": "Has"}], "correct": [1], "image": "@@MEDIA@@gg1/u4/english_class.webp"}, {"q": "A: Have you got an English class today? B: No, but we ___ an Art class.", "type": "single", "options": [{"text": "has got"}, {"text": "got"}, {"text": "have got"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["My", "best friend", "hasn't", "got", "a bike."], "sentence": "My best friend hasn't got a bike.", "audio_tts": "My best friend hasn't got a bike.", "image": "@@MEDIA@@gg1/u4/bike_yellow.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["We've", "got", "a new", "English", "teacher."], "sentence": "We've got a new English teacher.", "audio_tts": "We've got a new English teacher.", "image": "@@MEDIA@@gg1/u4/teacher_board.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["My", "parents", "haven't", "got", "a skateboard."], "sentence": "My parents haven't got a skateboard.", "audio_tts": "My parents haven't got a skateboard."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Juan", "has", "got", "blue", "eyes."], "sentence": "Juan has got blue eyes.", "audio_tts": "Juan has got blue eyes.", "image": "@@MEDIA@@gg1/u4/boy_cap.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["My sisters", "have", "got", "blond", "hair."], "sentence": "My sisters have got blond hair.", "audio_tts": "My sisters have got blond hair.", "image": "@@MEDIA@@gg1/u4/sisters_blond.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'gaps', replace($blk${"title": "READING. Посмотри на картинку, прочитай описание и перетащи правильное слово в каждый пропуск", "mode": "drag", "image": "@@MEDIA@@gg1/u4/tom_lucy_rex.webp", "text": "This is my friend Tom. He's ten years old. Tom has got short, __blond__ hair. He has got big blue __eyes__. He's tall and very __sporty__ — he plays football every day. He's very __friendly__ and helpful. Tom has got a sister. Her name is Lucy. She has got long, __curly__ hair. It's not straight. Lucy is very __clever__ — she likes maths and she can read very well. Tom and Lucy have got a dog. Its name is Rex. Rex has got big ears, a small __nose__ and four white feet. He's a very __funny__ dog!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>LISTENING. Послушай рассказ девочки о её младшей сестре Мие (Mia).</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'quiz', replace($blk${"title": "LISTENING. Выбери правильный ответ", "questions": [{"q": "How old is Mia?", "type": "single", "options": [{"text": "8"}, {"text": "7"}, {"text": "6"}], "correct": [1]}, {"q": "What kind of hair has Mia got?", "type": "single", "options": [{"text": "straight and dark"}, {"text": "wavy and red"}, {"text": "curly and blond"}], "correct": [2]}, {"q": "What colour are her eyes?", "type": "single", "options": [{"text": "green"}, {"text": "blue"}, {"text": "brown"}], "correct": [0]}, {"q": "Mia is…", "type": "single", "options": [{"text": "funny and friendly"}, {"text": "funny and clever"}, {"text": "clever and sporty"}], "correct": [1]}, {"q": "Has Mia got a pet?", "type": "single", "options": [{"text": "Yes, she has a dog."}, {"text": "No, she hasn't."}, {"text": "Yes, she has a goldfish."}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "image": "@@MEDIA@@gg1/u4/monsters_six.webp", "html": "<p>Посмотри на картинку, выбери монстра и опиши его. Запиши свой ответ, нажав на кнопку микрофона 🙌</p><p><i>Пример: My favourite monster has got three eyes. He has got twenty teeth, two legs and two arms.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 12);
end
$mig$;
