-- Go Getter 1 · Unit 5 · I can do it · Test
-- собрано tools/gg1_build.py --lesson u5_test
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 5 · I can do it', 5
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 5 · I can do it');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 5 · I can do it';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'match', replace($blk${"title": "Соедини слова и картинки", "pairs": [{"left": "cook", "right_image": "@@MEDIA@@gg1/u5/verb_cook.webp"}, {"left": "swim", "right_image": "@@MEDIA@@gg1/u5/verb_swim.webp"}, {"left": "fly", "right_image": "@@MEDIA@@gg1/u5/verb_fly.webp"}, {"left": "write", "right_image": "@@MEDIA@@gg1/u5/verb_write.webp"}, {"left": "sing", "right_image": "@@MEDIA@@gg1/u5/verb_sing.webp"}, {"left": "read", "right_image": "@@MEDIA@@gg1/u5/verb_read.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'exact_input', replace($blk${"title": "Посмотри на картинку и впиши сочетание целиком", "items": [{"prompt": "pl_y the p_ano", "accept": ["play the piano", "Play the piano"], "image": "@@MEDIA@@gg1/u5/coll_play_piano.webp"}, {"prompt": "r_d_ the h_rse", "accept": ["ride the horse", "Ride the horse"], "image": "@@MEDIA@@gg1/u5/coll_ride_horse.webp"}, {"prompt": "m_ke c_pcakes", "accept": ["make cupcakes", "Make cupcakes"], "image": "@@MEDIA@@gg1/u5/coll_make_cupcakes.webp"}, {"prompt": "pl_y footb_ll", "accept": ["play football", "Play football"], "image": "@@MEDIA@@gg1/u5/coll_play_football.webp"}, {"prompt": "r_d_ a bike", "accept": ["ride a bike", "Ride a bike"], "image": "@@MEDIA@@gg1/u5/coll_ride_bike.webp"}, {"prompt": "m_ke a p_ster", "accept": ["make a poster", "Make a poster"], "image": "@@MEDIA@@gg1/u5/coll_make_poster.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери пропущенное слово", "questions": [{"q": "A: ___ you make a poster? B: No, I can't.", "type": "single", "options": [{"text": "Can"}, {"text": "Cans"}, {"text": "Is"}], "correct": [0], "image": "@@MEDIA@@gg1/u5/coll_make_poster.webp"}, {"q": "A: Can you make a poster? B: No, I ___.", "type": "single", "options": [{"text": "don't"}, {"text": "can't"}, {"text": "can"}], "correct": [1]}, {"q": "A: What ___ you and your brother do? B: We can play the guitar.", "type": "single", "options": [{"text": "is"}, {"text": "cans"}, {"text": "can"}], "correct": [2], "image": "@@MEDIA@@gg1/u5/obj_guitar.webp"}, {"q": "A: What can you and your brother do? B: We ___ play the guitar.", "type": "single", "options": [{"text": "can"}, {"text": "are"}, {"text": "have"}], "correct": [0]}, {"q": "Joanna ___ draw, but she can't write yet.", "type": "single", "options": [{"text": "cans"}, {"text": "can"}, {"text": "do"}], "correct": [1], "image": "@@MEDIA@@gg1/u5/obj_crayons_drawing.webp"}, {"q": "Joanna can draw, but she ___ write yet.", "type": "single", "options": [{"text": "cans"}, {"text": "haven't"}, {"text": "can't"}], "correct": [2]}, {"q": "His aunt ___ ride a horse. She's old.", "type": "single", "options": [{"text": "can't"}, {"text": "can"}, {"text": "don't"}], "correct": [0], "image": "@@MEDIA@@gg1/u5/coll_ride_horse.webp"}, {"q": "A: ___ you cook well? B: Yes, I can.", "type": "single", "options": [{"text": "Has"}, {"text": "Can"}, {"text": "Does"}], "correct": [1], "image": "@@MEDIA@@gg1/u5/obj_mixing_bowl.webp"}, {"q": "A: Can you cook well? B: Yes, I ___.", "type": "single", "options": [{"text": "can't"}, {"text": "have"}, {"text": "can"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Can", "your brother", "fix", "that", "computer?"], "sentence": "Can your brother fix that computer?", "audio_tts": "Can your brother fix that computer?", "image": "@@MEDIA@@gg1/u5/obj_broken_laptop.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Can", "Betty's dog", "run", "fast?"], "sentence": "Can Betty's dog run fast?", "audio_tts": "Can Betty's dog run fast?", "image": "@@MEDIA@@gg1/u5/animal_beagle_puppy.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Max and", "his friends", "can't", "speak", "French."], "sentence": "Max and his friends can't speak French.", "audio_tts": "Max and his friends can't speak French.", "image": "@@MEDIA@@gg1/u5/obj_french_flag.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["The students", "can't", "read", "difficult", "words."], "sentence": "The students can't read difficult words.", "audio_tts": "The students can't read difficult words.", "image": "@@MEDIA@@gg1/u5/obj_book_stack.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["What", "can", "your", "hamster", "do?"], "sentence": "What can your hamster do?", "audio_tts": "What can your hamster do?", "image": "@@MEDIA@@gg1/u5/animal_hamster.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'gaps', replace($blk${"title": "READING. Прочитай рекламу спортивного клуба и впиши пропущенный глагол. Используй слова из списка", "mode": "drag", "text": "1. You can __swim__ in the swimming pool every Monday.\n2. You can __ride__ a bike in the park on Tuesday.\n3. You can __climb__ on the climbing wall on Wednesday.\n4. On Thursday, you can sing and __dance__ in the music room.\n5. On Friday, you can __draw__ and paint pictures of the city."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>LISTENING. Прослушай рассказ Джека о себе и своей сестре Лили.</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'sort', replace($blk${"title": "LISTENING. Перетащи каждое умение в нужный столбик", "groups": [{"name": "Jack can", "items": [{"text": "ride a bike"}, {"text": "swim"}, {"text": "dive"}, {"text": "play football"}]}, {"name": "Lily can", "items": [{"text": "sing"}, {"text": "play the piano"}, {"text": "draw"}, {"text": "ride a horse"}]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "html": "<p>Ответь на вопросы. Запиши свой ответ, нажав на кнопку микрофона 🙌</p><ol><li>Can you swim?</li><li>Can you cook well?</li><li>What can your best friend do?</li><li>Can your brother play the piano?</li><li>Can your father skateboard?</li><li>Can your teacher fix the computer?</li><li>What can kangaroos do?</li><li>Can penguins fly?</li><li>Can your mother drive a car?</li><li>Can your grandpa climb?</li><li>Can you ride a bike?</li><li>Can your classmates speak English?</li></ol>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 11);
end
$mig$;
