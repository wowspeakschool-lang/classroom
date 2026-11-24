-- GG2 Unit 5 · Homework 8 — повторение юнита перед тестом (черновик, is_published = false)
do $$
declare
  v_unit uuid;
  v_les  uuid;
  v_m    text := 'https://classroom.wowteach.ru/media/gg2/u5/';
  v_s    text := 'https://classroom.wowteach.ru/media/shared/gg/';
  v_a    text := 'https://api.wowteach.ru/storage/v1/object/public/classroom-media/uploads/';
begin
  select u.id into v_unit
  from classroom_courses c join classroom_units u on u.course_id = c.id
  where c.slug = 'gg2' and u.sort_order = 5;

  -- тест уезжает на 8-е место, ДЗ 8 встаёт перед ним
  update classroom_lessons set sort_order = 8 where unit_id = v_unit and title = 'Unit 5 Test';

  insert into classroom_lessons (unit_id, title, kind, sort_order, is_published)
  values (v_unit, 'Homework 8', 'homework', 7, false)
  returning id into v_les;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values

  (v_les, 'text', jsonb_build_object('html',
    '<p><img src="' || v_s || 'hello_highfive.webp" alt="" style="height:200px"></p>' ||
    '<h2>Привет! 👋</h2><p>Это последнее задание юнита: повторим всё про город, прошлое и дорогу — ' ||
    'и ты готов к тесту. Поехали!</p>'), 0),

  (v_les, 'match', jsonb_build_object(
    'title', 'Послушай слово и соедини его с картинкой',
    'pairs', jsonb_build_array(
      jsonb_build_object('left','🔊','left_audio', v_a || '1794584320128_tts_1794584320128.mp3',
        'left_audio_tts', jsonb_build_object('text','cafe.','voice','en_GB-alba'),
        'right','café','right_image', v_m || 'cafe.webp'),
      jsonb_build_object('left','🔊','left_audio', v_a || '1794584322539_tts_1794584322539.mp3',
        'left_audio_tts', jsonb_build_object('text','cinema.','voice','en_GB-alba'),
        'right','cinema','right_image', v_m || 'cinema.webp'),
      jsonb_build_object('left','🔊','left_audio', v_a || '1794584324943_tts_1794584324943.mp3',
        'left_audio_tts', jsonb_build_object('text','hotel.','voice','en_GB-alba'),
        'right','hotel','right_image', v_m || 'hotel.webp'),
      jsonb_build_object('left','🔊','left_audio', v_a || '1794584327315_tts_1794584327315.mp3',
        'left_audio_tts', jsonb_build_object('text','hospital.','voice','en_GB-alba'),
        'right','hospital','right_image', v_m || 'hospital.webp'),
      jsonb_build_object('left','🔊','left_audio', v_a || '1794584331668_tts_1794584331668.mp3',
        'left_audio_tts', jsonb_build_object('text','park.','voice','en_GB-alba'),
        'right','park','right_image', v_m || 'park.webp'),
      jsonb_build_object('left','🔊','left_audio', v_a || '1795547711326_tts_1795547711326.mp3',
        'left_audio_tts', jsonb_build_object('text','museum.','voice','en_US-amy'),
        'right','museum','right_image', v_m || 'museum.webp'))), 1),

  (v_les, 'quiz', jsonb_build_object(
    'title', 'Посмотри на картинку и выбери, что на ней изображено',
    'questions', jsonb_build_array(
      jsonb_build_object('q','What is it?','type','single','image', v_m || 'bank.webp','correct', jsonb_build_array(0),
        'options', jsonb_build_array(jsonb_build_object('text','bank'), jsonb_build_object('text','hotel'), jsonb_build_object('text','library'))),
      jsonb_build_object('q','What is it?','type','single','image', v_m || 'library.webp','correct', jsonb_build_array(2),
        'options', jsonb_build_array(jsonb_build_object('text','museum'), jsonb_build_object('text','theatre'), jsonb_build_object('text','library'))),
      jsonb_build_object('q','What is it?','type','single','image', v_m || 'theatre.webp','correct', jsonb_build_array(1),
        'options', jsonb_build_array(jsonb_build_object('text','cinema'), jsonb_build_object('text','theatre'), jsonb_build_object('text','hotel'))),
      jsonb_build_object('q','What is it?','type','single','image', v_m || 'supermarket.webp','correct', jsonb_build_array(0),
        'options', jsonb_build_array(jsonb_build_object('text','supermarket'), jsonb_build_object('text','shop'), jsonb_build_object('text','café'))),
      jsonb_build_object('q','What is it?','type','single','image', v_m || 'restaurant.webp','correct', jsonb_build_array(2),
        'options', jsonb_build_array(jsonb_build_object('text','supermarket'), jsonb_build_object('text','café'), jsonb_build_object('text','restaurant'))),
      jsonb_build_object('q','What is it?','type','single','image', v_m || 'train_station.webp','correct', jsonb_build_array(1),
        'options', jsonb_build_array(jsonb_build_object('text','sports centre'), jsonb_build_object('text','train station'), jsonb_build_object('text','police station'))))), 2),

  (v_les, 'sort', jsonb_build_object(
    'title', 'Распредели предложения: это про прошлое или про сейчас?',
    'groups', jsonb_build_array(
      jsonb_build_object('name','⏪ Прошлое', 'items', jsonb_build_array(
        jsonb_build_object('text','There was an old cinema here.'),
        jsonb_build_object('text','The streets were quiet.'),
        jsonb_build_object('text','There weren''t any cafés in 1990.'),
        jsonb_build_object('text','My school was small.'))),
      jsonb_build_object('name','▶️ Сейчас', 'items', jsonb_build_array(
        jsonb_build_object('text','There is a new sports centre.'),
        jsonb_build_object('text','The streets are busy.'),
        jsonb_build_object('text','There are three cafés in my street.'),
        jsonb_build_object('text','My school is big.'))))), 3),

  (v_les, 'gaps', jsonb_build_object(
    'title', 'Впиши was, wasn''t, were или weren''t',
    'mode', 'drag',
    'bank', jsonb_build_array('was','wasn''t','were','weren''t','was','were'),
    'text', '1. Last summer we __were__ in London. It was great!' || chr(10) ||
            '2. The museum __wasn''t__ boring. It was really interesting.' || chr(10) ||
            '3. There __was__ a small park behind our hotel.' || chr(10) ||
            '4. The streets __weren''t__ quiet. They were very busy.' || chr(10) ||
            '5. My friends __were__ at the stadium yesterday.' || chr(10) ||
            '6. I __was__ at home last Saturday.'), 4),

  (v_les, 'order', jsonb_build_object(
    'title', 'Составь предложения и вопросы',
    'items', jsonb_build_array(
      jsonb_build_object('words', jsonb_build_array('Was','there','a','cinema','in','your','town?'),
        'sentence','Was there a cinema in your town?'),
      jsonb_build_object('words', jsonb_build_array('There','weren''t','any','shops','in','this','street.'),
        'sentence','There weren''t any shops in this street.'),
      jsonb_build_object('words', jsonb_build_array('Where','were','you','last','Saturday?'),
        'sentence','Where were you last Saturday?'),
      jsonb_build_object('words', jsonb_build_array('The','hotel','was','opposite','the','train','station.'),
        'sentence','The hotel was opposite the train station.'))), 5),

  (v_les, 'gaps', jsonb_build_object(
    'title', 'Допиши короткие ответы',
    'mode', 'type',
    'text', '1. Was the museum interesting? — No, it __wasn''t__.' || chr(10) ||
            '2. Were you at the stadium yesterday? — Yes, I __was__.' || chr(10) ||
            '3. Was there a hotel near the park? — Yes, there __was__.' || chr(10) ||
            '4. Were the streets busy? — No, they __weren''t__.' || chr(10) ||
            '5. Were there any cafés in 1990? — No, there __weren''t__.'), 6),

  (v_les, 'gaps', jsonb_build_object(
    'title', 'Прохожий спрашивает дорогу. Вставь пропущенные слова',
    'mode', 'drag',
    'bank', jsonb_build_array('Excuse','get','straight','turn','opposite','far'),
    'text', 'A: __Excuse__ me. How can I __get__ to the hospital?' || chr(10) ||
            'B: Go __straight__ on and __turn__ left at the bank. The hospital is __opposite__ the park.' || chr(10) ||
            'A: Is it __far__?' || chr(10) ||
            'B: No, it''s five minutes from here.'), 7),

  (v_les, 'quiz', jsonb_build_object(
    'title', 'Прочитай рассказ Тома о его городе. Верно или неверно?',
    'material', '<p><b>My town</b></p><p>Ten years ago my town was small and quiet. There was one café and there ' ||
       'weren''t any cinemas. There was an old stadium near the river. Now my town is big and busy. There are ' ||
       'three cinemas, two sports centres and a new stadium. The museum is still here, but now it is more ' ||
       'interesting: there are films and games inside.</p>',
    'questions', jsonb_build_array(
      jsonb_build_object('q','Ten years ago the town was big.','type','single','correct', jsonb_build_array(1),
        'options', jsonb_build_array(jsonb_build_object('text','Верно'), jsonb_build_object('text','Неверно'))),
      jsonb_build_object('q','There weren''t any cinemas ten years ago.','type','single','correct', jsonb_build_array(0),
        'options', jsonb_build_array(jsonb_build_object('text','Верно'), jsonb_build_object('text','Неверно'))),
      jsonb_build_object('q','The stadium near the river was new.','type','single','correct', jsonb_build_array(1),
        'options', jsonb_build_array(jsonb_build_object('text','Верно'), jsonb_build_object('text','Неверно'))),
      jsonb_build_object('q','Now there are three cinemas in the town.','type','single','correct', jsonb_build_array(0),
        'options', jsonb_build_array(jsonb_build_object('text','Верно'), jsonb_build_object('text','Неверно'))),
      jsonb_build_object('q','The museum is more interesting now.','type','single','correct', jsonb_build_array(0),
        'options', jsonb_build_array(jsonb_build_object('text','Верно'), jsonb_build_object('text','Неверно'))))), 8),

  (v_les, 'speaking', jsonb_build_object(
    'title', 'SPEAKING 🎤 Расскажи вслух и запиши ответ',
    'html', '<p>Расскажи, каким твой город (или твоя улица) был раньше и какой он сейчас. Скажи 4–5 предложений: ' ||
            'используй <b>was / were</b>, <b>there was / there were</b> и слова <b>busy, quiet, old, new, big, small</b>.</p>' ||
            '<p><i>Например: Ten years ago our school was small. There weren''t any computers.</i></p>',
    'needs_review', true), 9),

  (v_les, 'text', jsonb_build_object('html',
    '<p><img src="' || v_s || 'bye_star.webp" alt="" style="height:180px"></p>' ||
    '<h3>Отличная работа!</h3><p>Весь юнит повторён — теперь тест тебе точно по плечу. Увидимся на занятии 😎</p>'), 10);
end $$;
