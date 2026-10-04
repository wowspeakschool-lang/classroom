-- Super Minds 3 · Unit 3 · At home · Test
-- собрано tools/sm3_build.py --lesson u3_test
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 3 · At home', 3
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 3 · At home');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 3 · At home';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с картинками", "pairs": [{"left_image": "@@MEDIA@@sm3/u3/chore_tidy_up.webp", "right": "Tidy up", "right_audio_tts": "tidy up"}, {"left_image": "@@MEDIA@@sm3/u3/chore_walk_dog.webp", "right": "Take the dog for a walk", "right_audio_tts": "take the dog for a walk"}, {"left_image": "@@MEDIA@@sm3/u3/chore_do_shopping.webp", "right": "Do the shopping", "right_audio_tts": "do the shopping"}, {"left_image": "@@MEDIA@@sm3/u3/chore_wash_up.webp", "right": "Wash up", "right_audio_tts": "wash up"}, {"left_image": "@@MEDIA@@sm3/u3/chore_sweep.webp", "right": "Sweep", "right_audio_tts": "sweep"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'gaps', replace($blk${"title": "Посмотри на картинку и заполни пропуски ⬇", "mode": "drag", "image": "@@MEDIA@@sm3/u3/scene_day_times.webp", "text": "1. I __take the dog for a walk__ at quarter past seven.\n2. I __do homework__ at six o’clock.\n3. I go to bed at __half past ten__.\n4. I clean my room at __half past eight__.\n5. I play with my friends at __eleven o’clock__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: I think you like ___ up your room.", "type": "single", "options": [{"text": "tidying"}, {"text": "tidy"}, {"text": "wash"}], "correct": [0]}, {"q": "B: No, I ___ like it.", "type": "single", "options": [{"text": "don’t"}, {"text": "do"}, {"text": "does"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: I like ___ the dog for a walk. B: Me too.", "type": "single", "options": [{"text": "taking"}, {"text": "take"}, {"text": "walk"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: What time do you go to bed? B: At ___ past eleven.", "type": "single", "options": [{"text": "half"}, {"text": "quarter"}], "correct": [0]}, {"q": "B: At half past ___.", "type": "single", "options": [{"text": "11"}, {"text": "10"}, {"text": "12"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "I have breakfast at quarter ___ eight.", "type": "single", "options": [{"text": "to"}, {"text": "half"}, {"text": "past"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "I ___ sweep the floor at the weekend. I like it a lot!", "type": "single", "options": [{"text": "always"}, {"text": "never"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["Do", "you", "like", "doing", "shopping?"], "sentence": "Do you like doing shopping?", "audio_tts": "Do you like doing shopping?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"words": ["I", "don’t", "like", "washing", "up."], "sentence": "I don’t like washing up.", "audio_tts": "I don't like washing up."}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"words": ["My mum", "and", "I", "cook", "dinner", "at", "half", "past", "six."], "sentence": "My mum and I cook dinner at half past six.", "audio_tts": "My mum and I cook dinner at half past six."}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"words": ["I", "sometimes", "tidy", "up", "my", "room."], "sentence": "I sometimes tidy up my room.", "audio_tts": "I sometimes tidy up my room."}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'order', replace($blk${"words": ["Do", "you", "always", "wash", "your", "clothes?"], "sentence": "Do you always wash your clothes?", "audio_tts": "Do you always wash your clothes?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "needs_review": true, "html": "<p>Расскажи о распорядке своего дня (5–7 предложений). Запиши свой ответ, нажав на кнопку микрофона.</p><p><i>For example: I take my dog for a walk at 8 o’clock.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12);
end
$mig$;
