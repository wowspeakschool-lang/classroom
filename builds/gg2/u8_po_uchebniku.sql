-- Go Getter 2, Unit 8 — приведение домашек к плану урока (по развороту 94–95 и с. 101)
-- 03.11.2026
--   ДЗ 1 (lesson 72754fc3…): убраны блоки 11–13 (текст про Анну, юнит 3),
--        возвращены порядковые числительные и даты из копии прежней ДЗ 3,
--        добавлена отработка по доске объявлений Меган (с. 94–95).
--   ДЗ 6 (lesson 946314de…): текст «Running for fun!» заменён на
--        «Sleepovers with a Difference» (с. 101), задания переписаны под него.
-- is_published не трогаем. Картинки — только ссылками.

-- ============================================================
-- 0. БЭКАП
-- ============================================================
create table if not exists classroom_backup_gg2_u8_po_uchebniku_20261103 as
select * from classroom_blocks
where lesson_id in ('72754fc3-1be7-4950-952d-b09eeb9747bc',
                    '946314de-7862-462c-a67c-08e32ccb6088');

-- ============================================================
-- 1. ДЗ 1 — classroom_gg2_u8_hw1_po_planu_20261103
-- ============================================================
do $mig$
declare
  v_lesson uuid := '72754fc3-1be7-4950-952d-b09eeb9747bc';
  v_media  text := 'https://classroom.wowteach.ru/media/';
  v_opt2   jsonb;
begin
  -- 1.1 убрать блоки 11–13 (sort_order 10,11,12): текст про Анну, gaps по нему и «Увлечения моей семьи»
  delete from classroom_blocks where lesson_id = v_lesson and sort_order in (10,11,12);

  -- 1.2 прощание (блок 14, sort_order 13) временно уводим, чтобы освободить места
  update classroom_blocks set sort_order = 1013
   where lesson_id = v_lesson and sort_order = 13;

  -- 1.3 приветствие обещает ровно то, что в домашке есть
  update classroom_blocks
     set payload = jsonb_build_object('html',
           replace($h$<p><img src='@@MEDIA@@shared/hello_wave.webp' alt='' style='height:200px'></p><h2>Привет! 👋</h2><p>Надеюсь, ты любишь праздники! Сегодня мы выучим слова о событиях, прочитаем афиши и приглашения с доски объявлений Меган, а ещё научимся называть даты по-английски 📅</p><p>Выполни все задания, чтобы запомнить всё на 100%!</p>$h$,
                   '@@MEDIA@@', v_media))
   where lesson_id = v_lesson and sort_order = 0;

  -- 1.4 доска объявлений Меган (с. 94): подводка + чтение афиш
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
  (v_lesson, 'text', jsonb_build_object('html',
     $h$<h3>Доска объявлений Меган 📌</h3><p>У Меган на стене висят приглашения, афиши и билет. Прочитай каждое объявление и реши, что это за событие.</p>$h$), 10);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
  (v_lesson, 'quiz', jsonb_build_object(
    'title', 'Прочитай объявление с доски Меган и выбери, что это за событие',
    'needs_review', false,
    'questions', jsonb_build_array(
      jsonb_build_object('q',
        $h$<p style='background:#d8f1f4;border-radius:12px;padding:14px 16px;text-align:center'>Please come to<br><b style='font-size:20px;color:#e8a400'>DANNY'S PARTY</b><br>On Saturday 11th June at 5 p.m.<br>Wear a funny costume! 🎩</p>$h$,
        'type','single','correct', jsonb_build_array(1),
        'options', jsonb_build_array(jsonb_build_object('text','a picnic'), jsonb_build_object('text','a fancy dress party'), jsonb_build_object('text','a football match'))),
      jsonb_build_object('q',
        $h$<p style='background:#ffe680;border-radius:12px;padding:14px 16px;text-align:center'><b>HARTWELL SCHOOL</b><br><b style='font-size:20px;color:#d6336c'>STARS OF TOMORROW</b> ⭐<br>Thursday 2nd June at 2 p.m.<br>Can you sing or play an instrument?<br>Can you dance or tell funny stories?<br><b>Great Prizes!</b><br>Contact: Mrs Harris</p>$h$,
        'type','single','correct', jsonb_build_array(0),
        'options', jsonb_build_array(jsonb_build_object('text','a talent competition'), jsonb_build_object('text','a barbecue'), jsonb_build_object('text','a sleepover'))),
      jsonb_build_object('q',
        $h$<p style='background:#f8d7da;border-radius:12px;padding:14px 16px;text-align:center'>Hartwell School Drama Club<br><b>PRESENTS</b><br><b style='font-size:20px;color:#b02a37'>Romeo &amp; Juliet</b><br>17th June, 7.00 p.m.<br>In the School Hall<br><b>TICKETS: £5.00</b></p>$h$,
        'type','single','correct', jsonb_build_array(2),
        'options', jsonb_build_array(jsonb_build_object('text','a concert'), jsonb_build_object('text','a dance show'), jsonb_build_object('text','a play'))),
      jsonb_build_object('q',
        $h$<p style='background:#dfe3f7;border-radius:12px;padding:14px 16px;text-align:center'><b style='font-size:20px;color:#d6336c'>Pyjama party</b> 🐱<br>To: Megan<br>When: 28th May<br>Where: My house!<br>From: Hannah<br><b>Don't forget your pyjamas and a sleeping bag!</b></p>$h$,
        'type','single','correct', jsonb_build_array(1),
        'options', jsonb_build_array(jsonb_build_object('text','a birthday party'), jsonb_build_object('text','a sleepover'), jsonb_build_object('text','a talent competition'))),
      jsonb_build_object('q',
        $h$<p style='background:#e7f0ff;border-radius:12px;padding:14px 16px;text-align:center'><b>RIVER DANCE CLUB</b><br>presents <b style='font-size:20px;color:#1f6feb'>STREET DANCE!</b><br>Friday 30th September<br>From 5–7 p.m.<br>At the River Centre</p>$h$,
        'type','single','correct', jsonb_build_array(0),
        'options', jsonb_build_array(jsonb_build_object('text','a dance show'), jsonb_build_object('text','a play'), jsonb_build_object('text','a picnic'))),
      jsonb_build_object('q',
        $h$<p style='background:#e8f7f5;border-radius:12px;padding:14px 16px;text-align:center'>🎟 <b style='font-size:20px'>THE ACTION</b> 🎸🥁<br>Date: Saturday 1st October<br>Stadium: Olympic Arena<br>Doors open: 17.00<br>Seat: G116 · Price: £25.00</p>$h$,
        'type','single','correct', jsonb_build_array(2),
        'options', jsonb_build_array(jsonb_build_object('text','a barbecue'), jsonb_build_object('text','a sleepover'), jsonb_build_object('text','a concert')))
    )), 11);

  -- 1.5 числа и даты — из копии прежней ДЗ 3 (classroom_backup_gg2_u8_hw3_20261103)
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  select v_lesson, type, payload, 12 from classroom_backup_gg2_u8_hw3_20261103 where sort_order = 1;  -- текст «Числа и даты 📅»
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  select v_lesson, type, payload, 13 from classroom_backup_gg2_u8_hw3_20261103 where sort_order = 2;  -- карточки порядковых числительных
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  select v_lesson, type, payload, 14 from classroom_backup_gg2_u8_hw3_20261103 where sort_order = 3;  -- 1st ↔ the first
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  select v_lesson, type, payload, 15 from classroom_backup_gg2_u8_hw3_20261103 where sort_order = 4;  -- как читается дата

  -- 1.6 даты событий с доски Меган (с. 94–95, упр. 9)
  v_opt2 := jsonb_build_array(
    jsonb_build_object('left','28th May',      'right','the sleepover',          'right_audio','', 'right_audio_tts', jsonb_build_object('text','the sleepover','voice','en_US-amy')),
    jsonb_build_object('left','2nd June',      'right','the talent competition', 'right_audio','', 'right_audio_tts', jsonb_build_object('text','the talent competition','voice','en_US-amy')),
    jsonb_build_object('left','11th June',     'right','the fancy dress party',  'right_audio','', 'right_audio_tts', jsonb_build_object('text','the fancy dress party','voice','en_US-amy')),
    jsonb_build_object('left','17th June',     'right','the play',               'right_audio','', 'right_audio_tts', jsonb_build_object('text','the play','voice','en_US-amy')),
    jsonb_build_object('left','30th September','right','the dance show',         'right_audio','', 'right_audio_tts', jsonb_build_object('text','the dance show','voice','en_US-amy')),
    jsonb_build_object('left','1st October',   'right','the concert',            'right_audio','', 'right_audio_tts', jsonb_build_object('text','the concert','voice','en_US-amy')));
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
  (v_lesson, 'match', jsonb_build_object(
    'title', 'Посмотри на даты событий с доски Меган и соедини дату с событием',
    'pairs', v_opt2), 16);

  -- 1.7 предложения с датами
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  select v_lesson, type, payload, 17 from classroom_backup_gg2_u8_hw3_20261103 where sort_order = 5;  -- «Теперь соберём предложения 📝»
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  select v_lesson, type, payload, 18 from classroom_backup_gg2_u8_hw3_20261103 where sort_order = 6;  -- My birthday is on the fifth of June.

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
  (v_lesson, 'order', jsonb_build_object(
    'title', 'Собери предложение из слов',
    'words', jsonb_build_array('The','sleepover','is','on','the','twenty-eighth','of','May.'),
    'sentence', 'The sleepover is on the twenty-eighth of May.'), 19);

  -- 1.8 напиши дату словами (с. 95, упр. 8)
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
  (v_lesson, 'gaps', jsonb_build_object(
    'mode', 'type',
    'title', 'Напиши дату словами. Образец: 1 May — the first of May',
    'text', $h$1. 3 October — __the third of October__
2. 14 May — __the fourteenth of May__
3. 9 June — __the ninth of June__
4. 25 April — __the twenty-fifth of April__
5. 12 March — __the twelfth of March__
6. 30 August — __the thirtieth of August__$h$), 20);

  -- 1.9 письменное задание
  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  select v_lesson, type, payload, 21 from classroom_backup_gg2_u8_hw3_20261103 where sort_order = 10;  -- «Когда твои праздники? ✍️»

  -- 1.10 прощание — последним
  update classroom_blocks set sort_order = 22
   where lesson_id = v_lesson and sort_order = 1013;
end
$mig$;

-- ============================================================
-- 2. ДЗ 6 — classroom_gg2_u8_hw6_sleepovers_20261103
-- ============================================================
do $mig$
declare
  v_lesson uuid := '946314de-7862-462c-a67c-08e32ccb6088';
  v_media  text := 'https://classroom.wowteach.ru/media/';
  v_art    text;   -- текст статьи без картинок — он же внутри заданий
  v_full   text;   -- текст статьи с картинками — отдельный блок-материал
  v_tf     jsonb := '[]'::jsonb;
  v_yn     jsonb;
  r        record;
begin
  v_art := $h$<h3>Sleepovers with a Difference</h3><p><b>Do you like going to sleepovers at friends' houses? Then why not try one of our "Sleepovers with a Difference"?</b></p><p><b>1 Sleep with dinosaurs!</b></p><ul><li><b>Where is it?</b> The Natural History Museum, London</li><li><b>Who can go?</b> Children aged 7–11</li><li><b>What can you do?</b> You can learn about dinosaurs, explore the museum at night, and sleep next to a diplodocus! In the morning, you can visit the museum shop.</li></ul><p><b>2 Sleep with sharks!</b></p><ul><li><b>Where is it?</b> The National Marine Aquarium, Plymouth</li><li><b>Who can go?</b> Children aged 5–15</li><li><b>What can you do?</b> You can have a tour of the aquarium and see amazing underwater creatures. Later, you can watch a movie and sleep next to the sharks!</li></ul><p><b>3 Sleep with an Egyptian mummy!</b></p><ul><li><b>Where is it?</b> The British Museum, London</li><li><b>Who can go?</b> Children aged 8–15</li><li><b>What can you do?</b> You can make an Egyptian boat, learn about the pyramids, and sleep on the floor of one of the oldest museums in the world. In the morning, you can have breakfast in the museum café.</li></ul><p><b>So what are you waiting for? Pack your sleeping bag, toothbrush and torch, and get ready for a night of adventure!</b></p>$h$;

  v_full := replace(replace(replace(v_art,
      '<p><b>1 Sleep with dinosaurs!</b></p>',
      $h$<p style='text-align:center'><img src='@@MEDIA@@gg2/u8/sleepover_girls.webp' alt='' style='max-width:320px;width:100%;border-radius:12px'></p><p><b>1 Sleep with dinosaurs!</b></p>$h$),
      '<p><b>3 Sleep with an Egyptian mummy!</b></p>',
      $h$<p style='text-align:center'><img src='@@MEDIA@@gg2/u8/sleep_floor.webp' alt='' style='max-width:320px;width:100%;border-radius:12px'></p><p><b>3 Sleep with an Egyptian mummy!</b></p>$h$),
      'get ready for a night of adventure!</b></p>',
      $h$get ready for a night of adventure!</b></p><p style='text-align:center'><img src='@@MEDIA@@gg2/u8/sleepover.webp' alt='' style='max-width:320px;width:100%;border-radius:12px'></p>$h$);
  v_full := replace(v_full, '@@MEDIA@@', v_media);

  -- 2.1 старый текст «Running for fun!» и все задания к нему
  delete from classroom_blocks where lesson_id = v_lesson and sort_order between 1 and 9;
  update classroom_blocks set sort_order = 1010 where lesson_id = v_lesson and sort_order = 10;

  -- 2.2 приветствие
  update classroom_blocks
     set payload = jsonb_build_object('html',
           replace($h$<p><img src='@@MEDIA@@shared/hello_headphones.webp' alt='' style='height:200px'></p><h2>Hello! 👋</h2><p>Сегодня мы почитаем про необычные ночёвки: рядом с динозавром, рядом с акулами и рядом с египетской мумией 🦖🦈</p><p>Прочитай текст и выполни задания. Готов начать?</p>$h$,
                   '@@MEDIA@@', v_media))
   where lesson_id = v_lesson and sort_order = 0;

  -- 2.3 текст-материал
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
  (v_lesson, 'text', jsonb_build_object('html',
     $h$<p>Прочитай текст внимательно — дальше будут задания по нему.</p>$h$ || v_full), 1);

  -- 2.4 место ↔ что там можно делать
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
  (v_lesson, 'match', jsonb_build_object(
    'title', 'Прочитай текст ещё раз и соедини место с тем, что там можно делать',
    'pairs', jsonb_build_array(
      jsonb_build_object('left','The Natural History Museum, London',    'right','sleep next to a diplodocus'),
      jsonb_build_object('left','The National Marine Aquarium, Plymouth','right','watch a movie and sleep next to the sharks'),
      jsonb_build_object('left','The British Museum, London',            'right','make an Egyptian boat and learn about the pyramids'))), 2);

  -- 2.5 верно / неверно — текст несёт каждый вопрос (truefalse на платформе материал не показывает)
  for r in select * from (values
      ('The Natural History Museum is in America.', 1),
      ('You can walk around the museum at night.',  0),
      ('At the Aquarium, you can see a film.',      0),
      ('You can''t go if you''re fifteen.',         1),
      ('The British Museum is a new museum.',       1),
      ('You sleep in a bed.',                       1)
    ) as t(st, c)
  loop
    v_tf := v_tf || jsonb_build_object(
      'q', v_art || '<p><b>' || r.st || '</b></p>',
      'type', 'single',
      'correct', jsonb_build_array(r.c),
      'options', jsonb_build_array(jsonb_build_object('text','Верно'), jsonb_build_object('text','Неверно')));
  end loop;
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
  (v_lesson, 'quiz', jsonb_build_object(
    'title', 'Прочитай предложение и ответь: верно или неверно?',
    'needs_review', false,
    'questions', v_tf), 3);

  -- 2.6 вопросы по тексту
  v_yn := jsonb_build_array(
    jsonb_build_object('q', v_art || '<p><b>Where can you sleep next to a diplodocus?</b></p>', 'type','single','correct',jsonb_build_array(0),
      'options', jsonb_build_array(jsonb_build_object('text','The Natural History Museum'), jsonb_build_object('text','The National Marine Aquarium'), jsonb_build_object('text','The British Museum'))),
    jsonb_build_object('q', v_art || '<p><b>Who can go to the sleepover at the aquarium?</b></p>', 'type','single','correct',jsonb_build_array(1),
      'options', jsonb_build_array(jsonb_build_object('text','children aged 7–11'), jsonb_build_object('text','children aged 5–15'), jsonb_build_object('text','children aged 8–15'))),
    jsonb_build_object('q', v_art || '<p><b>What can you do in the morning at the Natural History Museum?</b></p>', 'type','single','correct',jsonb_build_array(0),
      'options', jsonb_build_array(jsonb_build_object('text','visit the museum shop'), jsonb_build_object('text','have breakfast in the café'), jsonb_build_object('text','watch a movie'))),
    jsonb_build_object('q', v_art || '<p><b>Where can you make an Egyptian boat?</b></p>', 'type','single','correct',jsonb_build_array(1),
      'options', jsonb_build_array(jsonb_build_object('text','at the aquarium'), jsonb_build_object('text','at the British Museum'), jsonb_build_object('text','at the Natural History Museum'))),
    jsonb_build_object('q', v_art || '<p><b>What can you see at the National Marine Aquarium?</b></p>', 'type','single','correct',jsonb_build_array(0),
      'options', jsonb_build_array(jsonb_build_object('text','amazing underwater creatures'), jsonb_build_object('text','the pyramids'), jsonb_build_object('text','a diplodocus'))),
    jsonb_build_object('q', v_art || '<p><b>What do you need to pack?</b></p>', 'type','single','correct',jsonb_build_array(0),
      'options', jsonb_build_array(jsonb_build_object('text','a sleeping bag, a toothbrush and a torch'), jsonb_build_object('text','a costume and a hat'), jsonb_build_object('text','a camera and a book'))));
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
  (v_lesson, 'quiz', jsonb_build_object(
    'title', 'Ответь на вопросы по тексту',
    'needs_review', false,
    'questions', v_yn), 4);

  -- 2.7 распредели по трём ночёвкам
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
  (v_lesson, 'sort', jsonb_build_object(
    'title', 'Распредели: что к какой ночёвке относится',
    'groups', jsonb_build_array(
      jsonb_build_object('name','Sleep with dinosaurs!', 'items', jsonb_build_array(
        jsonb_build_object('text','The Natural History Museum'), jsonb_build_object('text','children aged 7–11'), jsonb_build_object('text','visit the museum shop'))),
      jsonb_build_object('name','Sleep with sharks!', 'items', jsonb_build_array(
        jsonb_build_object('text','The National Marine Aquarium'), jsonb_build_object('text','children aged 5–15'), jsonb_build_object('text','watch a movie'))),
      jsonb_build_object('name','Sleep with an Egyptian mummy!', 'items', jsonb_build_array(
        jsonb_build_object('text','The British Museum'), jsonb_build_object('text','children aged 8–15'), jsonb_build_object('text','make an Egyptian boat'))))), 5);

  -- 2.8 расскажи про ночёвку с акулами
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
  (v_lesson, 'gaps', jsonb_build_object(
    'mode', 'drag',
    'title', 'Перетащи слова в пропуски — расскажи про ночёвку с акулами',
    'text', $h$The Sleep with sharks! night is at the National Marine __Aquarium__ in __Plymouth__. __Children__ aged 5–15 can go. You can have a __tour__ of the aquarium and see amazing underwater __creatures__. Later, you can watch a __movie__ and sleep next to the __sharks__!$h$), 6);

  -- 2.9 Exam Spot: вопросы Эммы
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
  (v_lesson, 'gaps', jsonb_build_object(
    'mode', 'type',
    'title', 'Прочитай диалог и впиши вопросы Эммы',
    'text', $h$Emma: What did you do last weekend?
Sylvia: I went to a sleepover at the Science Museum.
Emma: __Was it good|was it good__?
Sylvia: Yes, it was really good. We did some experiments and watched a film. Next weekend I'm going to visit my cousins.
Emma: __Where do they live|where do they live__?
Sylvia: They live in Edinburgh.$h$), 7);

  -- 2.10 письменное задание
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
  (v_lesson, 'task', jsonb_build_object(
    'title', 'Какая ночёвка тебе нравится? ✍️',
    'needs_review', true,
    'html', $h$<p>Would you like to go on one of these sleepovers? Which one? Why?</p><p>Напиши 3–4 предложения по-английски.</p><p><i>Например: I'd like to sleep with the sharks. I like underwater creatures and I want to watch a movie at the aquarium.</i></p><p>Не забудь прочитать свой текст учителю на уроке!</p>$h$), 8);

  -- 2.11 прощание — последним
  update classroom_blocks set sort_order = 9
   where lesson_id = v_lesson and sort_order = 1010;
end
$mig$;
