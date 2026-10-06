-- Go Getter 1 · Unit 0 · Get started! · Test
-- собрано tools/gg1_build.py --lesson u0_test
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 0 · Get started!', 0
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 0 · Get started!');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 0 · Get started!';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Test', 'test',
         90, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'exact_input', replace($blk${"title": "Впиши недостающие буквы", "items": [{"prompt": "b _ _ k", "accept": ["book"], "image": "@@MEDIA@@gg1/u0/obj_book.webp", "audio_tts": "book"}, {"prompt": "p _ n", "accept": ["pen"], "image": "@@MEDIA@@gg1/u0/obj_pen.webp", "audio_tts": "pen"}, {"prompt": "b _ g", "accept": ["bag"], "image": "@@MEDIA@@gg1/u0/obj_bag.webp", "audio_tts": "bag"}, {"prompt": "ch _ _ r", "accept": ["chair"], "image": "@@MEDIA@@gg1/u0/obj_chair.webp", "audio_tts": "chair"}, {"prompt": "r _ d", "accept": ["red"], "image": "@@MEDIA@@gg1/u0/colour_red.svg", "audio_tts": "red"}, {"prompt": "bl _ _", "accept": ["blue"], "image": "@@MEDIA@@gg1/u0/colour_blue.svg", "audio_tts": "blue"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Вставь правильное слово", "questions": [{"q": "1. This is ___ pen.", "type": "single", "options": [{"text": "a"}, {"text": "an"}], "correct": [0]}, {"q": "2. This is ___ orange bag.", "type": "single", "options": [{"text": "a"}, {"text": "an"}], "correct": [1]}, {"q": "3. These are ___.", "type": "single", "options": [{"text": "book"}, {"text": "books"}], "correct": [1]}, {"q": "4. I have a pencil case. This is ___ pencil case.", "type": "single", "options": [{"text": "your"}, {"text": "my"}], "correct": [1]}, {"q": "5. You have a bag. Is this ___ bag?", "type": "single", "options": [{"text": "my"}, {"text": "your"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'order', replace($blk${"words": ["This", "is", "my", "bag."], "sentence": "This is my bag.", "audio_tts": "This is my bag."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"words": ["I", "have", "a", "pen."], "sentence": "I have a pen.", "audio_tts": "I have a pen."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"words": ["These", "are", "my", "books."], "sentence": "These are my books.", "audio_tts": "These are my books."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["Is", "this", "your", "pencil?"], "sentence": "Is this your pencil?", "audio_tts": "Is this your pencil?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["This", "is", "an", "orange", "ruler."], "sentence": "This is an orange ruler.", "audio_tts": "This is an orange ruler."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<h3>READING</h3><p>Прочитай короткие представления.</p><p>Hi! I'm Anna. My pen is red.<br>Hello! My name's Tom. My bag is blue.<br>I'm Olivia. My ruler is yellow.<br>Hello! I'm Daniel. My notebook is green.<br>Hi! My name's Sophie. My pencil case is pink.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'match', replace($blk${"title": "Соедини имя человека с его предметом", "pairs": [{"left": "Anna", "right_image": "@@MEDIA@@gg1/u0/col_red_pen.webp"}, {"left": "Tom", "right_image": "@@MEDIA@@gg1/u0/col_blue_bag.webp"}, {"left": "Olivia", "right_image": "@@MEDIA@@gg1/u0/col_yellow_ruler.webp"}, {"left": "Daniel", "right_image": "@@MEDIA@@gg1/u0/col_green_notebook.webp"}, {"left": "Sophie", "right_image": "@@MEDIA@@gg1/u0/col_pink_pencil_case.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'gaps', replace($blk${"title": "LISTENING. Прослушай учителя на аудио и впиши пропущенное слово (число или цвет)", "mode": "type", "audio": "", "text": "1. Open your book. Page __forty|40__.\n2. Look at picture __twelve|12__.\n3. The new pencil case is __purple__.\n4. There are __twenty|20__ chairs in the classroom.\n5. The teacher's bag is __brown__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING 🎤", "image": "@@MEDIA@@gg1/u0/test_classroom.webp", "html": "<p>Внимательно посмотри на картинку. Нажми на микрофон и ответь на вопросы.</p><ol><li>What can you see?</li><li>What colour is the bag?</li><li>What is on the desks?</li><li>How many books can you see?</li><li>What is your favourite colour?</li></ol>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 10);
end
$mig$;
