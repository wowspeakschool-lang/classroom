-- Go Getter 1 · Unit 7 · Animals · Test
-- собрано tools/gg1_build.py --lesson u7_test
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
  select v_unit, 'Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'exact_input', replace($blk${"title": "Впиши слово целиком: некоторые буквы пропущены", "items": [{"prompt": "b _ r d", "accept": ["bird", "Bird"], "image": "@@MEDIA@@gg1/u7/animal_bird.webp"}, {"prompt": "b _ t _ e _ f _ y", "accept": ["butterfly", "Butterfly"], "image": "@@MEDIA@@gg1/u7/animal_butterfly.webp"}, {"prompt": "c _ o _ o _ i _ e", "accept": ["crocodile", "Crocodile"], "image": "@@MEDIA@@gg1/u7/animal_crocodile.webp"}, {"prompt": "e _ e _ h _ n t", "accept": ["elephant", "Elephant"], "image": "@@MEDIA@@gg1/u7/animal_elephant.webp"}, {"prompt": "f _ y", "accept": ["fly", "Fly"], "image": "@@MEDIA@@gg1/u7/animal_fly.webp"}, {"prompt": "g _ r _ f _ e", "accept": ["giraffe", "Giraffe"], "image": "@@MEDIA@@gg1/u7/animal_giraffe.webp"}, {"prompt": "m _ n _ e y", "accept": ["monkey", "Monkey"], "image": "@@MEDIA@@gg1/u7/animal_monkey.webp"}, {"prompt": "s _ a _ e", "accept": ["snake", "Snake"], "image": "@@MEDIA@@gg1/u7/animal_snake.webp"}, {"prompt": "s _ i _ e r", "accept": ["spider", "Spider"], "image": "@@MEDIA@@gg1/u7/animal_spider.webp"}, {"prompt": "w _ a _ e", "accept": ["whale", "Whale"], "image": "@@MEDIA@@gg1/u7/animal_whale.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай предложение и выбери пропущенное слово", "questions": [{"q": "He ___ to school at the weekend.", "type": "single", "options": [{"text": "don't go"}, {"text": "doesn't go"}], "correct": [1], "image": "@@MEDIA@@gg1/u7/school_walk.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери пропущенное слово", "questions": [{"q": "A: I ___ do my homework at the weekend. And you?", "type": "single", "options": [{"text": "don't"}, {"text": "doesn't"}], "correct": [0]}, {"q": "B: I ___ my homework on Saturday, but I don't do it on Sunday.", "type": "single", "options": [{"text": "does"}, {"text": "do"}], "correct": [1]}, {"q": "B: I do my homework on Saturday, but I ___ it on Sunday.", "type": "single", "options": [{"text": "don't do"}, {"text": "doesn't do"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай предложение и выбери пропущенное слово", "questions": [{"q": "My friend Alice and I ___ play computer games after school, we play football.", "type": "single", "options": [{"text": "doesn't"}, {"text": "don't"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери пропущенное слово", "questions": [{"q": "A: ___ she play the piano?", "type": "single", "options": [{"text": "Does"}, {"text": "Do"}], "correct": [0], "image": "@@MEDIA@@gg1/u7/piano.webp"}, {"q": "A: Does she ___ the piano?", "type": "single", "options": [{"text": "plays"}, {"text": "play"}], "correct": [1]}, {"q": "B: No, she ___.", "type": "single", "options": [{"text": "doesn't"}, {"text": "don't"}], "correct": [0]}, {"q": "B: She ___ the guitar instead.", "type": "single", "options": [{"text": "play"}, {"text": "plays"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери пропущенное слово", "questions": [{"q": "A: What ___ your brother do to relax?", "type": "single", "options": [{"text": "does"}, {"text": "do"}], "correct": [0]}, {"q": "A: What does your brother ___ to relax?", "type": "single", "options": [{"text": "dos"}, {"text": "do"}, {"text": "does"}], "correct": [1]}, {"q": "B: He ___ to music. And you?", "type": "single", "options": [{"text": "listenes"}, {"text": "listen"}, {"text": "listens"}], "correct": [2]}, {"q": "A: I usually ___ swimming.", "type": "single", "options": [{"text": "go"}, {"text": "gos"}, {"text": "goes"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["He", "doesn't", "play", "computer", "games", "on", "weekdays."], "sentence": "He doesn't play computer games on weekdays.", "audio_tts": "He doesn't play computer games on weekdays."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["I", "don't", "have", "lunch", "at", "school."], "sentence": "I don't have lunch at school.", "audio_tts": "I don't have lunch at school."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Do", "you", "play", "the", "guitar?"], "sentence": "Do you play the guitar?", "audio_tts": "Do you play the guitar?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["Does", "she", "do", "any", "sport?"], "sentence": "Does she do any sport?", "audio_tts": "Does she do any sport?", "image": "@@MEDIA@@gg1/u7/sport_balls.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["What", "does", "she", "have", "for", "dinner?"], "sentence": "What does she have for dinner?", "audio_tts": "What does she have for dinner?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'text', replace($blk${"html": "<h3>READING</h3><p>Прочитай письмо Мии подруге и выбери правильные ответы.</p><p><img src=\"@@MEDIA@@gg1/u7/animal_rabbit.webp\" alt=\"Coco\" style=\"height:200px\"></p><p><i>Hi Olivia,<br>How are you? I'm fine. I have great news! We have a new pet. It's a small rabbit and her name is Coco. She is white and grey and she is very cute. Coco doesn't eat meat or fish. She eats leaves and vegetables. She drinks about one litre of water in a week. Every day my brother walks Coco in the garden — she loves it! I wanted a cat too, but we don't have one because my mum doesn't like cats.<br>Write soon!<br>Mia</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'quiz', replace($blk${"title": "READING. Выбери правильный ответ", "questions": [{"q": "What animal is Coco?", "type": "single", "options": [{"text": "a hamster"}, {"text": "a cat"}, {"text": "a rabbit"}], "correct": [2]}, {"q": "What colour is Coco?", "type": "single", "options": [{"text": "white and grey"}, {"text": "brown and white"}, {"text": "grey and black"}], "correct": [0]}, {"q": "What does Coco eat?", "type": "single", "options": [{"text": "fish"}, {"text": "leaves and vegetables"}, {"text": "meat"}], "correct": [1]}, {"q": "How much water does Coco drink in a week?", "type": "single", "options": [{"text": "5 litres"}, {"text": "2 litres"}, {"text": "1 litre"}], "correct": [2]}, {"q": "Who walks Coco in the garden?", "type": "single", "options": [{"text": "her brother"}, {"text": "her mum"}, {"text": "Mia"}], "correct": [0]}, {"q": "Why doesn't Mia's family have a cat?", "type": "single", "options": [{"text": "Cats are dangerous."}, {"text": "Her mum doesn't like cats."}, {"text": "Mia doesn't like cats."}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>LISTENING. Прослушай объявление в Лондонском зоопарке.</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'gaps', replace($blk${"title": "LISTENING. Перетащи пропущенные числа и слова", "mode": "drag", "text": "1. Adult ticket: £__18.50__.\n2. Child ticket: £__9.30__.\n3. The zoo opens at __10__ am.\n4. There are over __700__ animals in the zoo.\n5. The café is next to the __giraffes__.\n6. There is a big __elephant__ family in the zoo.\n7. A guide costs £__4.20__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "html": "<p>Представь, что ты собираешься брать интервью у своего друга. Составь 3 вопроса для интервью. Запиши свой ответ, нажав на кнопку микрофона 🙌</p><p><i>Пример: Do you listen to music? What sport do you like?</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 15);
end
$mig$;
