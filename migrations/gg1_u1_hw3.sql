-- Go Getter 1 · Unit 1 · Family and friends · Homework 3
-- собрано tools/gg1_build.py --lesson u1_hw3
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
  select v_unit, 'Homework 3', 'homework',
         60, false, 2
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 3');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 3';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>На занятии мы узнали много нового! Повторим?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u1/card_to_be_negative.webp\" alt=\"to be: отрицательная форма\" style=\"max-width:100%\"></p><p><img src=\"@@MEDIA@@gg1/u1/card_countries.webp\" alt=\"Countries & Nationalities\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в предложении в правильном порядке", "words": ["My", "friends", "aren't", "at home."], "sentence": "My friends aren't at home.", "audio_tts": "My friends aren't at home."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в предложении в правильном порядке", "words": ["You", "aren't", "right."], "sentence": "You aren't right.", "audio_tts": "You aren't right."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в предложении в правильном порядке", "words": ["I'm", "not", "a superhero."], "sentence": "I'm not a superhero.", "audio_tts": "I'm not a superhero."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в предложении в правильном порядке", "words": ["Ben", "isn't", "my", "friend."], "sentence": "Ben isn't my friend.", "audio_tts": "Ben isn't my friend."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в предложении в правильном порядке", "words": ["She", "isn't", "my", "aunt."], "sentence": "She isn't my aunt.", "audio_tts": "She isn't my aunt."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"title": "Расставь слова в предложении в правильном порядке", "words": ["They", "aren't", "my", "cousins."], "sentence": "They aren't my cousins.", "audio_tts": "They aren't my cousins."}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку и скажи: верно или неверно", "questions": [{"q": "He's a teacher.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [1], "image": "@@MEDIA@@gg1/u1/tf_boy_backpack.webp"}, {"q": "He isn't ready for school.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0]}, {"q": "She isn't eleven.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0], "image": "@@MEDIA@@gg1/u1/tf_girl_ten.webp"}, {"q": "She's at school.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [1]}, {"q": "They aren't happy.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [0], "image": "@@MEDIA@@gg1/u1/tf_boys_bench.webp"}, {"q": "They're at home.", "type": "single", "options": [{"text": "Верно"}, {"text": "Неверно"}], "correct": [1]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'match', replace($blk${"title": "Соедини название страны и национальность", "pairs": [{"left": "Poland", "left_image": "@@MEDIA@@gg1/u1/flag_poland.svg", "right": "Polish", "right_audio_tts": "Polish"}, {"left": "France", "left_image": "@@MEDIA@@gg1/u1/flag_france.svg", "right": "French", "right_audio_tts": "French"}, {"left": "the UK", "left_image": "@@MEDIA@@gg1/u1/flag_uk.svg", "right": "British", "right_audio_tts": "British"}, {"left": "Spain", "left_image": "@@MEDIA@@gg1/u1/flag_spain.svg", "right": "Spanish", "right_audio_tts": "Spanish"}, {"left": "Italy", "left_image": "@@MEDIA@@gg1/u1/flag_italy.svg", "right": "Italian", "right_audio_tts": "Italian"}, {"left": "China", "left_image": "@@MEDIA@@gg1/u1/flag_china.svg", "right": "Chinese", "right_audio_tts": "Chinese"}, {"left": "the USA", "left_image": "@@MEDIA@@gg1/u1/flag_usa.svg", "right": "American", "right_audio_tts": "American"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски словами my, your, his или her", "mode": "drag", "text": "Hanna: This is __my__ brother. __His__ name is Alex. The present is for Granny. __Her__ name is Sophie.\nAlex: This is __your__ present, Granny."}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'speaking', replace($blk${"title": "Откуда вы? 🎤", "html": "<p>Нажми на микрофон и расскажи, откуда ты и твоя семья.</p><p><i>Пример: I'm Polish. I'm not British. My granny is Spanish, she isn't French. My cousins are Italian.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'match', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Чей это флаг? Соедини флаг и страну ⭐", "pairs": [{"left_image": "@@MEDIA@@gg1/u1/flag_poland.svg", "right": "Poland", "right_audio_tts": "Poland"}, {"left_image": "@@MEDIA@@gg1/u1/flag_france.svg", "right": "France", "right_audio_tts": "France"}, {"left_image": "@@MEDIA@@gg1/u1/flag_uk.svg", "right": "the UK", "right_audio_tts": "the UK"}, {"left_image": "@@MEDIA@@gg1/u1/flag_spain.svg", "right": "Spain", "right_audio_tts": "Spain"}, {"left_image": "@@MEDIA@@gg1/u1/flag_italy.svg", "right": "Italy", "right_audio_tts": "Italy"}, {"left_image": "@@MEDIA@@gg1/u1/flag_china.svg", "right": "China", "right_audio_tts": "China"}, {"left_image": "@@MEDIA@@gg1/u1/flag_usa.svg", "right": "the USA", "right_audio_tts": "the USA"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'quiz', replace($blk${"title": "Выбери правильный вариант ⭐", "questions": [{"q": "She ___ British. She's Spanish.", "type": "single", "options": [{"text": "isn't"}, {"text": "am not"}, {"text": "aren't"}], "correct": [0]}, {"q": "I ___ twelve. I'm ten.", "type": "single", "options": [{"text": "isn't"}, {"text": "am not"}, {"text": "aren't"}], "correct": [1]}, {"q": "We ___ from France.", "type": "single", "options": [{"text": "am not"}, {"text": "isn't"}, {"text": "aren't"}], "correct": [2]}, {"q": "My brother ___ at home.", "type": "single", "options": [{"text": "isn't"}, {"text": "aren't"}, {"text": "am not"}], "correct": [0]}, {"q": "They ___ my cousins.", "type": "single", "options": [{"text": "am not"}, {"text": "aren't"}, {"text": "isn't"}], "correct": [1]}, {"q": "It ___ my bag.", "type": "single", "options": [{"text": "aren't"}, {"text": "am not"}, {"text": "isn't"}], "correct": [2]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 13),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_jump.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа! 🎉</h3><p>Увидимся на занятии! Bye!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 14);
end
$mig$;
