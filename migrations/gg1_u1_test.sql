-- Go Getter 1 · Unit 1 · Family and friends · Test
-- собрано tools/gg1_build.py --lesson u1_test
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
  select v_unit, 'Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'exact_input', replace($blk${"title": "Впиши слово целиком — недостающие буквы заменены чёрточками", "items": [{"prompt": "m _ t _ e r — мать", "accept": ["mother", "Mother"], "image": "@@MEDIA@@gg1/u1/fam_mother.webp"}, {"prompt": "f _ t _ e r — отец", "accept": ["father", "Father"], "image": "@@MEDIA@@gg1/u1/fam_father.webp"}, {"prompt": "p _ r _ n _ s — родители", "accept": ["parents", "Parents"], "image": "@@MEDIA@@gg1/u1/fam_parents.webp"}, {"prompt": "g _ a _ d _ a _ h _ r — дедушка", "accept": ["grandfather", "Grandfather"], "image": "@@MEDIA@@gg1/u1/fam_grandfather.webp"}, {"prompt": "g _ a _ d _ o _ h _ r — бабушка", "accept": ["grandmother", "Grandmother"], "image": "@@MEDIA@@gg1/u1/fam_grandmother.webp"}, {"prompt": "s _ n — сын", "accept": ["son", "Son"], "image": "@@MEDIA@@gg1/u1/fam_son.webp"}, {"prompt": "d _ u _ h _ e r — дочь", "accept": ["daughter", "Daughter"], "image": "@@MEDIA@@gg1/u1/fam_daughter.webp"}, {"prompt": "a _ n t — тётя", "accept": ["aunt", "Aunt"], "image": "@@MEDIA@@gg1/u1/fam_aunt.webp"}, {"prompt": "u _ c _ e — дядя", "accept": ["uncle", "Uncle"], "image": "@@MEDIA@@gg1/u1/fam_uncle.webp"}, {"prompt": "c _ u _ i n — двоюродный брат / сестра", "accept": ["cousin", "Cousin"], "image": "@@MEDIA@@gg1/u1/fam_cousin.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери пропущенное слово", "questions": [{"q": "A: Who's ___ best friend?", "type": "single", "options": [{"text": "your"}, {"text": "you"}], "correct": [0], "image": "@@MEDIA@@gg1/u1/t1_dog_best_friend.webp"}, {"q": "B: My dog ___ my best friend!", "type": "single", "options": [{"text": "are"}, {"text": "is"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери пропущенное слово", "questions": [{"q": "A: Where ___ your friend?", "type": "single", "options": [{"text": "is"}, {"text": "are"}], "correct": [0], "image": "@@MEDIA@@gg1/u1/t1_friend_home.webp"}, {"q": "B: My friend ___ at home.", "type": "single", "options": [{"text": "are"}, {"text": "is"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери пропущенное слово", "questions": [{"q": "A: Happy Birthday, Anna! Here's ___ present. — B: Thank you.", "type": "single", "options": [{"text": "your"}, {"text": "you"}], "correct": [0], "image": "@@MEDIA@@gg1/u1/t1_birthday.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай и выбери пропущенное слово", "questions": [{"q": "Robin ___ in the garden.", "type": "single", "options": [{"text": "am not"}, {"text": "aren't"}, {"text": "isn't"}], "correct": [2], "image": "@@MEDIA@@gg1/u1/t1_robin_library.webp"}, {"q": "He ___ in the library.", "type": "single", "options": [{"text": "is"}, {"text": "are"}, {"text": "am"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай и выбери пропущенное слово", "questions": [{"q": "My friends ___ from Poland.", "type": "single", "options": [{"text": "isn't"}, {"text": "aren't"}], "correct": [1], "image": "@@MEDIA@@gg1/u1/t1_french_friends.webp"}, {"q": "My friends aren't from ___.", "type": "single", "options": [{"text": "Poland"}, {"text": "Polish"}], "correct": [0]}, {"q": "They ___ French.", "type": "single", "options": [{"text": "is"}, {"text": "are"}, {"text": "am"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["My", "classmates", "aren't", "at", "school."], "sentence": "My classmates aren't at school.", "audio_tts": "My classmates aren't at school.", "image": "@@MEDIA@@gg1/u1/t1_classmates_park.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Our", "neighbours", "are", "on", "holiday."], "sentence": "Our neighbours are on holiday.", "audio_tts": "Our neighbours are on holiday.", "image": "@@MEDIA@@gg1/u1/t1_neighbours_beach.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["My", "dad", "is", "the", "best."], "sentence": "My dad is the best.", "audio_tts": "My dad is the best.", "image": "@@MEDIA@@gg1/u1/t1_super_dad.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Mary's", "family", "is", "from", "London."], "sentence": "Mary's family is from London.", "audio_tts": "Mary's family is from London.", "image": "@@MEDIA@@gg1/u1/place_london.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Tommy", "isn't", "in", "the", "park."], "sentence": "Tommy isn't in the park.", "audio_tts": "Tommy isn't in the park.", "image": "@@MEDIA@@gg1/u1/place_park.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'text', replace($blk${"html": "<h3>READING</h3><p>Прочитай рассказ Марко о его семье и выбери правильный ответ.</p><p><i>Hello! I'm Marco. I'm from Italy. This is my family album. My mother's name is Sofia. She's a teacher. My father's name is Paolo. He's a doctor. My sister is Lucia. She's eight years old. My brother Leo is fourteen. My grandparents live in France. My grandfather is French. My grandmother is Italian. We are on holiday in Spain now. It's our favourite country!</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'quiz', replace($blk${"title": "READING. Выбери правильный ответ", "questions": [{"q": "Where is Marco from?", "type": "single", "options": [{"text": "Spain"}, {"text": "France"}, {"text": "Italy"}], "correct": [2]}, {"q": "Sofia is Marco's…", "type": "single", "options": [{"text": "mother"}, {"text": "sister"}, {"text": "aunt"}], "correct": [0]}, {"q": "What's his father's job?", "type": "single", "options": [{"text": "a father"}, {"text": "a doctor"}, {"text": "a teacher"}], "correct": [1]}, {"q": "How old is Marco's brother?", "type": "single", "options": [{"text": "18"}, {"text": "8"}, {"text": "14"}], "correct": [2]}, {"q": "His grandfather is…", "type": "single", "options": [{"text": "French"}, {"text": "Italian"}, {"text": "British"}], "correct": [0]}, {"q": "Where are they on holiday?", "type": "single", "options": [{"text": "in Italy"}, {"text": "in Spain"}, {"text": "in France"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>LISTENING. Прослушай Эмму и реши: правда или неправда?</b></p><p><img src=\"@@MEDIA@@gg1/u1/t1_emma_park.webp\" alt=\"\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'truefalse', replace($blk${"title": "LISTENING. Правда или неправда?", "statements": [{"text": "Emma is twelve years old.", "correct": false}, {"text": "Emma is from the UK.", "correct": true}, {"text": "Her brother's name is Max.", "correct": true}, {"text": "Max is eleven years old.", "correct": false}, {"text": "Her best friend is from Spain.", "correct": false}, {"text": "They are at the park.", "correct": true}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "html": "<p>Ответь на вопросы. Запиши свой ответ, нажав на кнопку микрофона 🙌</p><ol><li>What's your name?</li><li>Where are you from?</li><li>How old are you?</li><li>What's your mum's name?</li><li>What's your dad's name?</li><li>What's your best friend's name?</li><li>How old is your best friend?</li></ol>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 15);
end
$mig$;
