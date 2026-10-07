-- Super Minds 1 · Unit 8 · My body · Homework 5
-- собрано tools/sm1_build.py --lesson u8_hw5
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm1';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 8 · My body', 8
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 8 · My body');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 8 · My body';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Добро пожаловать в домашнее задание! 👋</h2><p>Сегодня тебя ждут много интересных историй и задания к ним! Внимательно читай инструкцию к каждому заданию!</p><p>В конце тебя ждёт дополнительное задание! Его делать необязательно, но если ты его выполнишь, то будешь супер мега крутым учеником!</p><p>Let's go!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Начнём с практики!</p><p>Внимательно посмотри на картинку. Прочитай вопрос и ответь: <b>Yes, he/she/it can</b> или <b>No, he/she/it can't</b>!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Can she skip?", "type": "single", "options": [{"text": "Yes, she can."}, {"text": "No, she can't."}], "correct": [1], "image": "@@MEDIA@@sm1/u8/she_cant_skip.webp"}, {"q": "Can he touch his toes?", "type": "single", "options": [{"text": "No, he can't."}, {"text": "Yes, he can."}], "correct": [1], "image": "@@MEDIA@@sm1/u8/he_touch_toes.webp"}, {"q": "Can she dance?", "type": "single", "options": [{"text": "Yes, she can."}, {"text": "No, she can't."}], "correct": [0], "image": "@@MEDIA@@sm1/u8/ab_cat_dance.webp"}, {"q": "Can he ride his bike?", "type": "single", "options": [{"text": "No, he can't."}, {"text": "Yes, he can."}], "correct": [0], "image": "@@MEDIA@@sm1/u8/ab_bear_cant_ride_bike.webp"}, {"q": "Can this dog swim?", "type": "single", "options": [{"text": "No, it can't."}, {"text": "Yes, it can."}], "correct": [1], "image": "@@MEDIA@@sm1/u8/ab_dog_swim.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"html": "<p>Ура! Ты справился с первым заданием! А теперь перейдём к следующему…</p><p>Посмотри внимательно на картинку и расставь слова в правильном порядке.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"words": ["He", "can", "stand", "on", "one", "leg."], "sentence": "He can stand on one leg.", "audio_tts": "He can stand on one leg.", "image": "@@MEDIA@@sm1/u8/ab_stand_one_leg.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["He", "can", "swim."], "sentence": "He can swim.", "audio_tts": "He can swim.", "image": "@@MEDIA@@sm1/u8/ab_dog_swim.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["She", "can't", "ride", "a", "horse."], "sentence": "She can't ride a horse.", "audio_tts": "She can't ride a horse.", "image": "@@MEDIA@@sm1/u8/she_cant_ride_horse.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["He", "can't", "play", "tennis."], "sentence": "He can't play tennis.", "audio_tts": "He can't play tennis.", "image": "@@MEDIA@@sm1/u8/he_cant_play_tennis.webp"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p>Ты такой молодец! Ты выполнил уже два задания. А сейчас тебя ждут интересные истории.</p><p>Ребята подготовили для тебя рассказ о своих питомцах. Как думаешь, какие у них домашние животные? Прочитай текст вслух и проверь себя.</p><p><img src=\"@@MEDIA@@sm1/u8/pet_forum.webp\" alt=\"Pet forum\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'truefalse', replace($blk${"title": "Отлично! Тебе понравились истории? Прочитай текст ещё раз и ответь: верно или неверно?", "statements": [{"text": "Patch can swim.", "correct": true}, {"text": "Jazzy is a horse.", "correct": true}, {"text": "Jazzy can't skip.", "correct": false}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'speaking', replace($blk${"title": "Мой питомец 🎤", "html": "<p>Послушай, как я описала своего домашнего животного! Тебе понравился мой дружок?</p><p>Настала твоя очередь! Нарисуй своего питомца, опиши его и покажи рисунок на уроке.</p><p><b>Пример:</b> I have got a dog. His name is Tabby. He can swim and he can play football.</p>", "sample": "", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'gaps', replace($blk${"title": "Ты выполнил все задания из основной части! А это дополнительное задание — для настоящих чемпионов! Впиши слова can или can't.", "mode": "type", "text": "Bob is a cat. He __can__ run and jump and he __can__ sing!\nHarry's cat __can't__ sing.\nPatch is a dog. He __can__ swim and he __can__ play football.\nJazzy is a horse. She __can't__ sing. She __can__ skip."}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'match', replace($blk${"title": "Соедини описание с именем питомца", "pairs": [{"left": "He's black with one white foot. He can sing!", "right": "Bob", "right_audio_tts": "Bob"}, {"left": "He can swim and he can play football.", "right": "Patch", "right_audio_tts": "Patch"}, {"left": "She's a big black horse. She can skip.", "right": "Jazzy", "right_audio_tts": "Jazzy"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Поздравляю! Ты завершил домашнее задание! Молодец!</h3><p>За прохождение домашнего задания держи ещё одну дополнительную ⭐. Жду тебя на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 13);
end
$mig$;
