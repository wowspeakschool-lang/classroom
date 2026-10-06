-- Go Getter 1 · Unit 8 · Sport and health · Homework 7
-- собрано tools/gg1_build.py --lesson u8_hw7
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Go Getter 1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 8 · Sport and health', 8
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 8 · Sport and health');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 8 · Sport and health';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 7', 'homework',
         60, false, 6
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 7');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 7';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>Сегодня мы закрепим знания, полученные в этом месяце. На следующем занятии тебя ждёт тест, и сегодня мы будем к нему готовиться вместе. В конце тебя будет ждать дополнительное упражнение — для самых смелых и самых сильных учеников 💪</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "В первом задании тебе нужно проявить смекалку! Посмотри на слова и выбери одно лишнее", "questions": [{"q": "table tennis / taekwondo / tennis / badminton", "type": "single", "options": [{"text": "tennis"}, {"text": "taekwondo"}, {"text": "table tennis"}, {"text": "badminton"}], "correct": [1]}, {"q": "sailing / windsurfing / swimming / ice-skating", "type": "single", "options": [{"text": "windsurfing"}, {"text": "sailing"}, {"text": "ice-skating"}, {"text": "swimming"}], "correct": [2]}, {"q": "spring / January / winter / summer", "type": "single", "options": [{"text": "spring"}, {"text": "summer"}, {"text": "winter"}, {"text": "January"}], "correct": [3]}, {"q": "hot / warm / autumn / sunny", "type": "single", "options": [{"text": "autumn"}, {"text": "warm"}, {"text": "sunny"}, {"text": "hot"}], "correct": [0]}, {"q": "snowy / cold / windy / early", "type": "single", "options": [{"text": "cold"}, {"text": "early"}, {"text": "windy"}, {"text": "snowy"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'gaps', replace($blk${"title": "Повторим вопросительные слова и местоимения! Воспользуйся табличками, чтобы заполнить пропуски", "mode": "type", "image": "@@MEDIA@@gg1/u8/tables_question_pronouns.webp", "text": "1. A: __Where__ are you? Are you at school?\n2. A: __How__ many cookies are there? B: Six.\n3. Your parents are nice. I like __them__.\n4. Where's Emma? I can't see __her__.\n5. Look at that picture! Do you like __it__?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'exact_input', replace($blk${"title": "Все предложения рассыпались, слова потеряли окончания, а вспомогательные глаголы сбежали! Напиши предложения правильно. Образец: Jack / hate / play / tennis → Jack hates playing tennis. Обрати внимание на окончание -ing — как думаешь, почему?", "items": [{"prompt": "my sister / not like / roller skate", "accept": ["My sister doesn't like roller skating.", "My sister doesn't like roller skating", "My sister does not like roller skating.", "My sister does not like roller skating"]}, {"prompt": "you / like / swim?", "accept": ["Do you like swimming?", "Do you like swimming"]}, {"prompt": "I / love / sing", "accept": ["I love singing.", "I love singing"]}, {"prompt": "we / not like / get up / early", "accept": ["We don't like getting up early.", "We don't like getting up early", "We do not like getting up early.", "We do not like getting up early"]}, {"prompt": "your friends / like / eat / pizza?", "accept": ["Do your friends like eating pizza?", "Do your friends like eating pizza"]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'task', replace($blk${"title": "Мой образ жизни ✍️", "needs_review": true, "html": "<p>Давай вспомним Лукаса и как он рассказывал о себе. Напиши такой же небольшой текст, только уже О СЕБЕ!</p><p><b>My lifestyle!</b></p><p><i><b>Sleep.</b> I go to bed at half past nine on school days and I get up at eight o'clock. I love sleeping!</i></p><p><i><b>Food.</b> My favourite food is pizza. Mum and Dad don't like pizza. Yes, really! They like fruit and vegetables. I drink a lot of water.</i></p><p><i><b>Sports and friends.</b> I'm not very sporty but I like watching football on TV. I love music and I play the guitar every day after school from 5 to 6. I often hang out with Jen, Alex and Lian too!</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'exact_input', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Собери слово из букв ⭐", "items": [{"prompt": "E K C Y O H", "accept": ["hockey", "Hockey"], "image": "@@MEDIA@@gg1/u8/sport_hockey.webp", "audio_tts": "hockey"}, {"prompt": "T I N E N S", "accept": ["tennis", "Tennis"], "image": "@@MEDIA@@gg1/u8/sport_tennis.webp", "audio_tts": "tennis"}, {"prompt": "S G N K I I", "accept": ["skiing", "Skiing"], "image": "@@MEDIA@@gg1/u8/sport_skiing.webp", "audio_tts": "skiing"}, {"prompt": "N S G L I I A", "accept": ["sailing", "Sailing"], "image": "@@MEDIA@@gg1/u8/sport_sailing.webp", "audio_tts": "sailing"}, {"prompt": "C C Y G L I N", "accept": ["cycling", "Cycling"], "image": "@@MEDIA@@gg1/u8/sport_cycling.webp", "audio_tts": "cycling"}, {"prompt": "L L B O A L E L V Y", "accept": ["volleyball", "Volleyball"], "image": "@@MEDIA@@gg1/u8/sport_volleyball.webp", "audio_tts": "volleyball"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски ⭐", "mode": "drag", "text": "1. My dad loves __cooking__ pizza.\n2. We don't like __getting__ up early.\n3. Does your sister __like__ swimming?\n4. Tom __hates__ cleaning his room.\n5. Kate is my friend. I like __her__ a lot.\n6. These are my cats. I love __them__!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'gaps', replace($blk${"title": "Выбери правильное вопросительное слово ⭐", "mode": "drag", "text": "1. __Where__ do you live? — In Paris.\n2. __Who__ is your sports hero? — Irina Peters.\n3. __When__ is the game? — It's on Tuesday.\n4. __Whose__ phone is it? — It's Irina's phone.\n5. __What__ have you got there? — Her autograph!\n6. __How many__ photos have you got? — Eighty."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/good_luck_clover.webp\" alt=\"\" style=\"height:180px\"></p><h3>У тебя отлично получилось! 🎉</h3><p>Уверена, ты справишься с тестом на все сто! Удачи!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8);
end
$mig$;
