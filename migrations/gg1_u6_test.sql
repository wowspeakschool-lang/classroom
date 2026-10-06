-- Go Getter 1 · Unit 6 · My day · Test
-- собрано tools/gg1_build.py --lesson u6_test
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 6 · My day', 6
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 6 · My day');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 6 · My day';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'exact_input', replace($blk${"title": "Впиши фразу целиком, вставив недостающие буквы", "items": [{"prompt": "g_ t_ sch__l — ходить в школу", "accept": ["go to school", "Go to school"], "image": "@@MEDIA@@gg1/u6/da_go_to_school.webp"}, {"prompt": "h_v_ l_ss_ns — учиться на уроках", "accept": ["have lessons", "Have lessons"], "image": "@@MEDIA@@gg1/u6/da_have_lessons.webp"}, {"prompt": "h_v_ br__kf_st — завтракать", "accept": ["have breakfast", "Have breakfast"], "image": "@@MEDIA@@gg1/u6/da_have_breakfast.webp"}, {"prompt": "h_v_ l_nch — обедать", "accept": ["have lunch", "Have lunch"], "image": "@@MEDIA@@gg1/u6/da_have_lunch.webp"}, {"prompt": "h_v_ d_nn_r — ужинать", "accept": ["have dinner", "Have dinner"], "image": "@@MEDIA@@gg1/u6/da_have_dinner.webp"}, {"prompt": "h_v_ a sh_w_r — принимать душ", "accept": ["have a shower", "Have a shower"], "image": "@@MEDIA@@gg1/u6/da_have_a_shower.webp"}, {"prompt": "d_ my h_m_w_rk — делать домашнее задание", "accept": ["do my homework", "Do my homework"], "image": "@@MEDIA@@gg1/u6/da_do_homework.webp"}, {"prompt": "t_dy my r__m — убираться в комнате", "accept": ["tidy my room", "Tidy my room"], "image": "@@MEDIA@@gg1/u6/da_tidy_my_room.webp"}, {"prompt": "h_ng o_t w_th my fr__nds — тусоваться с друзьями", "accept": ["hang out with my friends", "Hang out with my friends"], "image": "@@MEDIA@@gg1/u6/da_hang_out_with_friends.webp"}, {"prompt": "l_st_n t_ m_s_c — слушать музыку", "accept": ["listen to music", "Listen to music"], "image": "@@MEDIA@@gg1/u6/da_listen_to_music.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай предложение и выбери пропущенное слово", "questions": [{"q": "He ___ up really early at 6 o'clock.", "type": "single", "options": [{"text": "get"}, {"text": "gets"}], "correct": [1], "image": "@@MEDIA@@gg1/u6/boy_wakes_up.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери пропущенные слова", "questions": [{"q": "A: I ___ lunch at home. And you?", "type": "single", "options": [{"text": "have"}, {"text": "has"}], "correct": [0], "image": "@@MEDIA@@gg1/u6/obj_school_canteen.webp"}, {"q": "B: Me too. But my brother ___ at school all day…", "type": "single", "options": [{"text": "are"}, {"text": "is"}], "correct": [1]}, {"q": "B: …and he ___ lunch there.", "type": "single", "options": [{"text": "have"}, {"text": "haves"}, {"text": "has"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай предложение и выбери пропущенное слово", "questions": [{"q": "My friend Alice and I ___ computer games after school.", "type": "single", "options": [{"text": "plays"}, {"text": "play"}], "correct": [1], "image": "@@MEDIA@@gg1/u6/obj_computer_games.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на часы и выбери ответ", "questions": [{"q": "A: What time is it? B: It is ___.", "type": "single", "options": [{"text": "quarter to 2"}, {"text": "quarter past 2"}, {"text": "half past 2"}], "correct": [1], "image": "@@MEDIA@@gg1/u6/clock_0215.svg"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Прочитай диалог и выбери пропущенные слова", "questions": [{"q": "A: What time do you get up? B: I get up at ___. And you?", "type": "single", "options": [{"text": "eight o'clock"}, {"text": "half past seven"}, {"text": "nine o'clock"}], "correct": [0], "image": "@@MEDIA@@gg1/u6/clock_0800.svg"}, {"q": "A: I usually get up at ___.", "type": "single", "options": [{"text": "eight past half"}, {"text": "half past eight"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["He", "usually", "goes", "to", "the gym."], "sentence": "He usually goes to the gym.", "audio_tts": "He usually goes to the gym.", "image": "@@MEDIA@@gg1/u6/obj_gym.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["She", "sometimes", "has", "dinner", "with us."], "sentence": "She sometimes has dinner with us.", "audio_tts": "She sometimes has dinner with us.", "image": "@@MEDIA@@gg1/u6/obj_family_dinner.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["I", "get", "up", "at", "half", "past", "seven."], "sentence": "I get up at half past seven.", "audio_tts": "I get up at half past seven.", "image": "@@MEDIA@@gg1/u6/clock_0730.svg"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["I", "have", "my", "birthday", "in", "September."], "sentence": "I have my birthday in September.", "audio_tts": "I have my birthday in September.", "image": "@@MEDIA@@gg1/u6/birthday_cupcake.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в правильном порядке", "words": ["What", "time", "is", "it", "now?"], "sentence": "What time is it now?", "audio_tts": "What time is it now?", "image": "@@MEDIA@@gg1/u6/pocket_watch.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'text', replace($blk${"html": "<h3>READING</h3><p>Прочитай дневник Джулии.</p><p><b>My weekly schedule</b></p><p><i>On Monday, I always go to school early and have lessons until 3 pm. On Tuesday, I have a piano lesson after school. On Wednesday, I usually hang out with my friends in the park. On Thursday, I do my homework and watch TV. On Friday, I sometimes go to the cinema with my family. On Saturday, I always tidy my room in the morning. On Sunday, I never get up early — I love sleeping!</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'match', replace($blk${"title": "READING. Соедини каждый день недели с тем, что Джулия делает", "pairs": [{"left": "Monday", "right": "have lessons at school"}, {"left": "Tuesday", "right": "have a piano lesson"}, {"left": "Wednesday", "right": "hang out with friends in the park"}, {"left": "Thursday", "right": "do homework and watch TV"}, {"left": "Friday", "right": "go to the cinema with family"}, {"left": "Saturday", "right": "tidy her room"}, {"left": "Sunday", "right": "sleep late"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'text', replace($blk${"audio": "", "html": "<p><b>LISTENING. Прослушай рассказ Алекса о его обычной субботе.</b></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'truefalse', replace($blk${"title": "LISTENING. Правда или неправда?", "statements": [{"text": "Alex usually gets up at eight o'clock.", "correct": false}, {"text": "He always has breakfast with his family.", "correct": true}, {"text": "He does his homework on Sunday.", "correct": false}, {"text": "He plays football with his friends in the park.", "correct": true}, {"text": "They never go to the café.", "correct": false}, {"text": "He has dinner at seven o'clock.", "correct": true}, {"text": "He goes to bed at eleven.", "correct": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 14),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK. PART 1 🎤", "image": "@@MEDIA@@gg1/u6/eric_day_comic.webp", "html": "<p>Посмотри на картинку и опиши, что делает Эрик и его семья.</p><p><i>Пример: Dad cooks breakfast at 7 o'clock.</i></p><p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 15),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK. PART 2 🎤", "html": "<p>Ответь на вопросы:</p><ol><li>What do you do in the morning, afternoon and evening?</li><li>What does your mum / dad do in the morning, afternoon and evening?</li><li>What do you do at the weekend?</li></ol><p>Запиши свой ответ, нажав на кнопку микрофона 🙌</p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 16);
end
$mig$;
