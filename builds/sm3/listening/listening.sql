-- SM3, тесты юнитов 1–8: добавляем аудирование (LISTENING)
-- Решение Анны от 03.11.2026: «в тестах Super Minds 3 юнитов 1–8 нужно добавить
-- аудирование» — сейчас его там нет совсем, оно есть только в тесте юнита 0
-- (блок 16) и в финальном тесте.
--
-- Что делаем: в каждый тест юнитов 1–8 (classroom_lessons.kind = 'test',
-- курс slug = 'sm3') вставляем ОДИН блок quiz с пятью вопросами по рассказу.
--   * payload.audio = '' — пусто, ссылку впишем после записи;
--   * audio_tts НЕ ставим ни в блоке, ни в вопросах: «Озвучить пачкой» затёрло бы
--     место под запись (решение Анны от 18.10.2026). Аудирование начитывает
--     Yandex SpeechKit из отдельной сессии (решение от 20.10.2026);
--   * payload.skill = 'listening' — раздел трекера прогресса у каждого задания
--     теста (решение Анны от 23.10.2026);
--   * текста рассказа на экране нет — отдельного текстового блока не делаем;
--   * рассказ в третьем лице, без диалогов (решение Анны от 20.10.2026):
--     английский голос в синтезе один.
-- Текст рассказов и ключи — builds/sm3/listening/teksty.md.
--
-- Блок встаёт перед SPEAKING TASK — на то же место в структуре, что в тесте
-- юнита 0 (там он после чтения, перед диктантом и говорением; в тестах 1–8
-- чтения и диктанта нет). Остальные блоки сдвигаются на +1 через запас +1000,
-- чтобы не задеть уникальный ключ (lesson_id, sort_order).
--
-- Только insert и update. is_published и pass_threshold не трогаем.

do $mig$
declare
  v_lesson uuid;
  r record;
begin
  for r in
    select * from (values
      (1, 11, $blk${ "audio": "", "skill": "listening", "title": "LISTENING 🎧 Послушай рассказ про Майло и выбери правильный ответ. Можно послушать два раза", "questions": [ { "q": "What is Milo’s favourite subject?", "type": "single", "correct": [ 0 ], "options": [ { "text": "Geography" }, { "text": "Science" }, { "text": "Maths" } ] }, { "q": "Which subject does Milo NOT like?", "type": "single", "correct": [ 0 ], "options": [ { "text": "Maths" }, { "text": "Art" }, { "text": "Geography" } ] }, { "q": "What does Milo have to wear to school?", "type": "single", "correct": [ 0 ], "options": [ { "text": "a uniform" }, { "text": "a hat" }, { "text": "trainers" } ] }, { "q": "What does Milo hate doing?", "type": "single", "correct": [ 0 ], "options": [ { "text": "singing" }, { "text": "dancing" }, { "text": "swimming" } ] }, { "q": "How many books has Milo got in his school bag?", "type": "single", "correct": [ 0 ], "options": [ { "text": "nine" }, { "text": "five" }, { "text": "nineteen" } ] } ] }$blk$::jsonb),
      (2, 12, $blk${ "audio": "", "skill": "listening", "title": "LISTENING 🎧 Послушай рассказ про Фрею и выбери правильный ответ. Можно послушать два раза", "questions": [ { "q": "Are there any sausages in the basket?", "type": "single", "correct": [ 0 ], "options": [ { "text": "No, there aren’t." }, { "text": "Yes, there are." }, { "text": "Yes, there is." } ] }, { "q": "How many apples has Freya got?", "type": "single", "correct": [ 0 ], "options": [ { "text": "six" }, { "text": "seven" }, { "text": "sixteen" } ] }, { "q": "What is there in the salad?", "type": "single", "correct": [ 0 ], "options": [ { "text": "onions and peas" }, { "text": "cheese and rolls" }, { "text": "soup and water" } ] }, { "q": "What would Freya’s brother like?", "type": "single", "correct": [ 0 ], "options": [ { "text": "some lemonade" }, { "text": "some water" }, { "text": "some soup" } ] }, { "q": "What is there for dinner?", "type": "single", "correct": [ 0 ], "options": [ { "text": "some soup" }, { "text": "some salad" }, { "text": "some rolls" } ] } ] }$blk$::jsonb),
      (3, 12, $blk${ "audio": "", "skill": "listening", "title": "LISTENING 🎧 Послушай рассказ про Хьюго и выбери правильный ответ. Можно послушать два раза", "questions": [ { "q": "What time does Hugo get up?", "type": "single", "correct": [ 0 ], "options": [ { "text": "at half past seven" }, { "text": "at quarter past seven" }, { "text": "at half past nine" } ] }, { "q": "What does Hugo always do before school?", "type": "single", "correct": [ 0 ], "options": [ { "text": "He takes the dog for a walk." }, { "text": "He does the shopping." }, { "text": "He washes up." } ] }, { "q": "What doesn’t Hugo like doing?", "type": "single", "correct": [ 0 ], "options": [ { "text": "washing up" }, { "text": "sweeping the floor" }, { "text": "tidying up his room" } ] }, { "q": "When does Hugo do the shopping?", "type": "single", "correct": [ 0 ], "options": [ { "text": "on Saturday" }, { "text": "on Monday" }, { "text": "on Wednesday" } ] }, { "q": "What time does Hugo go to bed?", "type": "single", "correct": [ 0 ], "options": [ { "text": "at quarter past nine" }, { "text": "at quarter to nine" }, { "text": "at half past nine" } ] } ] }$blk$::jsonb),
      (4, 12, $blk${ "audio": "", "skill": "listening", "title": "LISTENING 🎧 Послушай рассказ про Грету и выбери правильный ответ. Можно послушать два раза", "questions": [ { "q": "What is opposite Greta’s house?", "type": "single", "correct": [ 0 ], "options": [ { "text": "the library" }, { "text": "the bank" }, { "text": "the tower" } ] }, { "q": "Where is the tower?", "type": "single", "correct": [ 0 ], "options": [ { "text": "near the market square" }, { "text": "opposite the library" }, { "text": "between two trees" } ] }, { "q": "Why is Greta going to the library on Monday?", "type": "single", "correct": [ 0 ], "options": [ { "text": "to borrow a book" }, { "text": "to go swimming" }, { "text": "to buy some apples" } ] }, { "q": "Where is the bank?", "type": "single", "correct": [ 0 ], "options": [ { "text": "between the supermarket and the car park" }, { "text": "near the bus station" }, { "text": "opposite the tower" } ] }, { "q": "Where is Greta going on Saturday?", "type": "single", "correct": [ 0 ], "options": [ { "text": "to the sports centre" }, { "text": "to the library" }, { "text": "to the market square" } ] } ] }$blk$::jsonb),
      (5, 12, $blk${ "audio": "", "skill": "listening", "title": "LISTENING 🎧 Послушай рассказ про Отиса и выбери правильный ответ. Можно послушать два раза", "questions": [ { "q": "Where was Otis yesterday?", "type": "single", "correct": [ 0 ], "options": [ { "text": "at the beach" }, { "text": "in the park" }, { "text": "at school" } ] }, { "q": "How many dolphins were there near the boat?", "type": "single", "correct": [ 0 ], "options": [ { "text": "two" }, { "text": "three" }, { "text": "twelve" } ] }, { "q": "Were there any jellyfish?", "type": "single", "correct": [ 0 ], "options": [ { "text": "No, there weren’t." }, { "text": "Yes, there were." }, { "text": "Yes, there was." } ] }, { "q": "What was in Otis’s bucket?", "type": "single", "correct": [ 0 ], "options": [ { "text": "a starfish and a seahorse" }, { "text": "a turtle and a seal" }, { "text": "a dolphin and a shell" } ] }, { "q": "Where was Otis at six o’clock?", "type": "single", "correct": [ 0 ], "options": [ { "text": "in the café" }, { "text": "in the sea" }, { "text": "in a boat" } ] } ] }$blk$::jsonb),
      (6, 12, $blk${ "audio": "", "skill": "listening", "title": "LISTENING 🎧 Послушай рассказ про Мейзи и выбери правильный ответ. Можно послушать два раза", "questions": [ { "q": "Is Maisie’s tablet bigger than her mobile phone?", "type": "single", "correct": [ 0 ], "options": [ { "text": "Yes, it is." }, { "text": "No, it isn’t." }, { "text": "Yes, it does." } ] }, { "q": "What is bigger than the tablet?", "type": "single", "correct": [ 0 ], "options": [ { "text": "the laptop" }, { "text": "the mobile phone" }, { "text": "the torch" } ] }, { "q": "What is Maisie’s favourite gadget?", "type": "single", "correct": [ 0 ], "options": [ { "text": "her laptop" }, { "text": "her games console" }, { "text": "her torch" } ] }, { "q": "Which gadget is cheaper than the electric fan?", "type": "single", "correct": [ 0 ], "options": [ { "text": "the torch" }, { "text": "the laptop" }, { "text": "the tablet" } ] }, { "q": "What is slower than the stairs?", "type": "single", "correct": [ 0 ], "options": [ { "text": "the lift" }, { "text": "the electric fan" }, { "text": "the digital radio" } ] } ] }$blk$::jsonb),
      (7, 11, $blk${ "audio": "", "skill": "listening", "title": "LISTENING 🎧 Послушай рассказ про Руфуса и выбери правильный ответ. Можно послушать два раза", "questions": [ { "q": "What did Rufus have on Monday?", "type": "single", "correct": [ 0 ], "options": [ { "text": "a headache and a cough" }, { "text": "a stomachache" }, { "text": "an earache" } ] }, { "q": "Who phoned the doctor?", "type": "single", "correct": [ 0 ], "options": [ { "text": "his mum" }, { "text": "his sister" }, { "text": "the nurse" } ] }, { "q": "What did Rufus do on Tuesday?", "type": "single", "correct": [ 0 ], "options": [ { "text": "He watched TV." }, { "text": "He went to school." }, { "text": "He played football." } ] }, { "q": "Who cooked some soup for Rufus?", "type": "single", "correct": [ 0 ], "options": [ { "text": "his sister" }, { "text": "his mum" }, { "text": "the doctor" } ] }, { "q": "When did Rufus go to school again?", "type": "single", "correct": [ 0 ], "options": [ { "text": "on Thursday" }, { "text": "on Tuesday" }, { "text": "on Wednesday" } ] } ] }$blk$::jsonb),
      (8, 11, $blk${ "audio": "", "skill": "listening", "title": "LISTENING 🎧 Послушай рассказ про Тессу и выбери правильный ответ. Можно послушать два раза", "questions": [ { "q": "Where did Tessa go last summer?", "type": "single", "correct": [ 0 ], "options": [ { "text": "to Egypt" }, { "text": "to Spain" }, { "text": "to China" } ] }, { "q": "How long did they stay in the hotel?", "type": "single", "correct": [ 0 ], "options": [ { "text": "two weeks" }, { "text": "two days" }, { "text": "two months" } ] }, { "q": "Did Tessa go to the museum?", "type": "single", "correct": [ 0 ], "options": [ { "text": "No, she didn’t." }, { "text": "Yes, she did." }, { "text": "No, she wasn’t." } ] }, { "q": "How many postcards did Tessa send?", "type": "single", "correct": [ 0 ], "options": [ { "text": "five" }, { "text": "four" }, { "text": "fifteen" } ] }, { "q": "What did they eat every evening?", "type": "single", "correct": [ 0 ], "options": [ { "text": "fish and rice" }, { "text": "pizza and salad" }, { "text": "soup and rolls" } ] } ] }$blk$::jsonb)
    ) as t(unit_sort, ins_sort, payload)
  loop
    select l.id into v_lesson
    from classroom_courses c
    join classroom_units u on u.course_id = c.id
    join classroom_lessons l on l.unit_id = u.id
    where c.slug = 'sm3' and u.sort_order = r.unit_sort and l.kind = 'test';

    if v_lesson is null then
      raise exception 'SM3: тест юнита % не найден', r.unit_sort;
    end if;

    -- в тесте уже есть аудирование? тогда ничего не делаем (идемпотентность)
    if exists (select 1 from classroom_blocks b
               where b.lesson_id = v_lesson
                 and b.payload->>'title' like 'LISTENING%') then
      raise notice 'SM3 юнит %: аудирование уже есть, пропускаем', r.unit_sort;
      continue;
    end if;

    -- 1) отодвигаем хвост теста (SPEAKING TASK и всё после) с запасом +1000
    update classroom_blocks
       set sort_order = sort_order + 1000
     where lesson_id = v_lesson and sort_order >= r.ins_sort;

    -- 2) ставим аудирование на освободившееся место
    insert into classroom_blocks (lesson_id, type, payload, sort_order)
    values (v_lesson, 'quiz', r.payload, r.ins_sort);

    -- 3) возвращаем хвост, сдвинутым ровно на +1
    update classroom_blocks
       set sort_order = sort_order - 999
     where lesson_id = v_lesson and sort_order >= 1000;
  end loop;
end
$mig$;
