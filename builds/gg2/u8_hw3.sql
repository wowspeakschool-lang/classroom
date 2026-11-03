-- Go Getter 2, Unit 8, Homework 3 — пересборка под план урока.
-- Дата: 03.11.2026. Миграция: classroom_gg2_u8_hw3_po_planu_20261103
--
-- ПРИЧИНА. 03.11 домашки GG2 развели по планам уроков (24 → 28). ДЗ 3 юнита 8
-- была собрана нами с нуля на тему «порядковые числительные и даты», потому что
-- в выгрузке «Взнания» домашки к третьему плану не было. Решение Анны:
-- «нужно чтобы соответствовало планам уроков».
--
-- Планы на Google Диске: общий диск 0AFvsQ32rh1KuUk9PVA →
-- «GG2 remastered» (1yus3lx7-pSjjL9S2_4CB4WzVMPnjXW2Q) → Unit 8 →
-- Lesson 1…Lesson 8, в каждой папке «Lesson N.docx».
--
-- Unit 8 Lesson 1 (Having fun): лексика событий, p.94-95 + ex.7-10 —
--   «I say cardinal – you say ordinal», «Write the dates», Megan’s pinboard,
--   «Write your diary». То есть ПОРЯДКОВЫЕ ЧИСЛИТЕЛЬНЫЕ И ДАТЫ — это Lesson 1,
--   материал ДЗ 1, а не ДЗ 3.
-- Unit 8 Lesson 3 (Having fun): «Revision of grammar / Revision of vocabulary /
--   Practice using grammar + additional grammar». Lead-in — видео «Past Simple
--   in Conversation», study focus — wordwall «gg2 u6 past simple», study
--   practice — p.97 ex.7 «ask and answer the questions» и ex.9 «Listen and
--   match the names», activation — p.97 ex.8 «ask and answer about your plans»
--   и ex.10 «Imagine your perfect weekend. In pairs, talk about your plans».
--
-- Отсюда тема ДЗ 3: повторение Past Simple + вопросы и ответы о планах
-- с be going to, в конце — рассказ об идеальных выходных.
--
-- Старые блоки копируются в classroom_backup_gg2_u8_hw3_20261103.
-- is_published не трогаем; pass_threshold у урока остаётся null.
-- Картинки — только ссылками, через плейсхолдер @@MEDIA@@.
-- Звук: пустой audio + audio_tts рядом (нажимает методист, «Озвучить пачкой»).
-- У блоков order звука нет — в GG2 он подсказывает ответ.
--
-- 13 блоков, из них 8 заданий. Лесенка сложности:
--   тема A (повторяемая, раньше) Past Simple: quiz (узнавание) → gaps (письмо);
--   тема B be going to: match (узнавание) → sort (классификация) →
--   order ×2 (сборка с опорой) → gaps (письмо) → task (говорение/письмо).

do $$
declare
  v_media  text := 'https://classroom.wowteach.ru/media/';
  v_lesson uuid;
begin

  select l.id into v_lesson
  from classroom_courses c
  join classroom_units   u on u.course_id = c.id
  join classroom_lessons l on l.unit_id   = u.id
  where c.slug = 'gg2' and u.sort_order = 8 and l.title = 'Homework 3';

  if v_lesson is null then
    raise exception 'GG2 Unit 8 Homework 3 не найдена';
  end if;

  -- 1. копия старых блоков
  if not exists (select 1 from pg_tables
                 where schemaname = 'public'
                   and tablename  = 'classroom_backup_gg2_u8_hw3_20261103') then
    create table classroom_backup_gg2_u8_hw3_20261103 as
      select * from classroom_blocks where lesson_id = v_lesson;
  end if;

  -- 2. чистим урок
  delete from classroom_blocks where lesson_id = v_lesson;

  -- 3. новые блоки
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values

  -- 1. приветствие
  (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_highfive.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>Сегодня мы повторим две вещи: как рассказать о том, что уже было, и как рассказать о своих планах. А в конце ты расскажешь о своих идеальных выходных.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),

  -- 2. подводка к Past Simple
  (v_lesson, 'text', $blk${"html": "<h3>Сначала вспомним прошлое 🕰</h3><p>Когда мы говорим о том, что уже случилось, глагол меняется:</p><p><b>play → played</b>, <b>go → went</b>, <b>have → had</b>, <b>eat → ate</b>, <b>meet → met</b>, <b>get → got</b>, <b>be → was / were</b></p>"}$blk$::jsonb, 1),

  -- 3. задание 1 — Past Simple, узнавание
  (v_lesson, 'quiz', $blk${"title": "Прочитай предложение и выбери правильную форму глагола", "questions": [
    {"q": "Last Saturday we ___ to a football match.", "type": "single", "correct": [0], "options": [{"text": "went"}, {"text": "go"}, {"text": "are going"}]},
    {"q": "Tom ___ a big birthday party last week.", "type": "single", "correct": [1], "options": [{"text": "has"}, {"text": "had"}, {"text": "have"}]},
    {"q": "They ___ pizza at the picnic yesterday.", "type": "single", "correct": [2], "options": [{"text": "eat"}, {"text": "eating"}, {"text": "ate"}]},
    {"q": "I ___ my friends at the bowling last Friday.", "type": "single", "correct": [0], "options": [{"text": "met"}, {"text": "meet"}, {"text": "meets"}]},
    {"q": "She ___ a lovely present for her birthday.", "type": "single", "correct": [1], "options": [{"text": "get"}, {"text": "got"}, {"text": "gets"}]}
  ]}$blk$::jsonb, 2),

  -- 4. задание 2 — Past Simple, воспроизведение
  (v_lesson, 'gaps', $blk${"mode": "type", "title": "Впиши глагол в прошедшем времени", "text": "Last weekend __was__ (be) great! On Saturday I __went__ (go) to a concert with my dad. On Sunday we __had__ (have) a picnic in the park. We __played__ (play) football and I __ate__ (eat) three sandwiches!"}$blk$::jsonb, 3),

  -- 5. подводка к be going to
  (v_lesson, 'text', $blk${"html": "<h3>А теперь — планы 🗓</h3><p>О планах мы говорим с <b>be going to</b>. В вопросе сначала идёт вопросительное слово, потом <b>am / is / are</b>:</p><p><b>What are you going to do?</b><br><b>Where are you going to go?</b><br><b>Who is going to come?</b></p>"}$blk$::jsonb, 4),

  -- 6. задание 3 — вопрос ↔ ответ, узнавание
  (v_lesson, 'match', $blk${"title": "Соедини вопросы с ответами", "pairs": [
    {"left": "What are you going to do on Saturday?", "right": "I'm going to have a barbecue with my family.", "right_audio": "", "right_audio_tts": {"text": "I'm going to have a barbecue with my family.", "voice": "en_US-amy"}},
    {"left": "Where are you going to have your party?", "right": "At the restaurant near the park.", "right_audio": "", "right_audio_tts": {"text": "At the restaurant near the park.", "voice": "en_US-amy"}},
    {"left": "When are you going to buy the tickets?", "right": "On Friday morning.", "right_audio": "", "right_audio_tts": {"text": "On Friday morning.", "voice": "en_US-amy"}},
    {"left": "Who are you going to invite?", "right": "All my friends from school.", "right_audio": "", "right_audio_tts": {"text": "All my friends from school.", "voice": "en_US-amy"}},
    {"left": "Are you going to wear a costume?", "right": "Yes, I am. I've got a dragon costume!", "right_audio": "", "right_audio_tts": {"text": "Yes, I am. I've got a dragon costume!", "voice": "en_US-amy"}},
    {"left": "Is Megan going to sing at the show?", "right": "No, she isn't. She's going to dance.", "right_audio": "", "right_audio_tts": {"text": "No, she isn't. She's going to dance.", "voice": "en_US-amy"}}
  ]}$blk$::jsonb, 5),

  -- 7. задание 4 — классификация: прошлое или планы
  (v_lesson, 'sort', $blk${"title": "Распредели предложения: что уже было, а что только в планах", "groups": [
    {"name": "Last weekend 🕰", "items": [{"text": "We went to the cinema."}, {"text": "I had a big chocolate cake."}, {"text": "They played football in the park."}]},
    {"name": "Next weekend 🗓", "items": [{"text": "We are going to have a barbecue."}, {"text": "I am going to buy a present."}, {"text": "She is going to sing at the concert."}]}
  ]}$blk$::jsonb, 6),

  -- 8. разделитель перед серией «собери вопрос»
  (v_lesson, 'text', $blk${"html": "<p>Отлично! Теперь соберём вопросы 📝</p>"}$blk$::jsonb, 7),

  -- 9. задание 5 — сборка вопроса с опорой
  (v_lesson, 'order', replace($blk${"title": "Собери вопрос из слов", "image": "@@MEDIA@@gg2/u8/beach_holiday.webp", "words": ["Where", "are", "you", "going", "to", "go", "at", "the", "weekend?"], "sentence": "Where are you going to go at the weekend?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),

  -- 10. задание 6 — сборка вопроса с опорой
  (v_lesson, 'order', replace($blk${"title": "Собери вопрос из слов", "image": "@@MEDIA@@gg2/u8/picnic.webp", "words": ["Are", "you", "going", "to", "have", "a", "picnic", "on", "Sunday?"], "sentence": "Are you going to have a picnic on Sunday?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),

  -- 11. задание 7 — воспроизведение формы без опоры
  (v_lesson, 'gaps', $blk${"mode": "type", "title": "Впиши am, is или are", "text": "Next Saturday my sister __is__ going to have a party. We __are__ going to make a big cake. I __am__ going to buy balloons and flowers. My cousin Jack __is__ going to bring his guitar. What __are__ you going to do next Saturday?"}$blk$::jsonb, 10),

  -- 12. задание 8 — творческое, p.97 ex.10 «Imagine your perfect weekend»
  (v_lesson, 'task', $blk${"title": "Мои идеальные выходные ✍️", "needs_review": true, "html": "<p>Представь свои идеальные выходные. Напиши 4–5 предложений о том, что ты собираешься делать: куда пойдёшь, с кем и чем будете заниматься. Используй <b>be going to</b>.</p><p>Образец:</p><p><i>On Saturday I am going to go to the cinema with my friends. We are going to eat popcorn. On Sunday I am going to have a picnic with my family.</i></p>"}$blk$::jsonb, 11),

  -- 13. прощание
  (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Молодец! 🎉</h3><p>Ты повторил прошедшее время и научился спрашивать о планах. Увидимся на занятии!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12);

  raise notice 'GG2 U8 HW3: блоков стало %',
    (select count(*) from classroom_blocks where lesson_id = v_lesson);

end $$;
