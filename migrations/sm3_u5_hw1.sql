-- Super Minds 3 · Unit 5 · Under the sea · Homework 1
-- собрано tools/sm3_build.py --lesson u5_hw1
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 5 · Under the sea', 5
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 5 · Under the sea');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 5 · Under the sea';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 1', 'homework',
         60, false, 0
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 1');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 1';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! Сегодня мы ныряем под воду 🌊</h2><p>Выучим слова про море и его обитателей. Поехали!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'flashcards', replace($blk${"cards": [{"text": "seal", "translation": "тюлень", "audio_tts": "seal", "image": "@@MEDIA@@sm3/u5/sea_seal.webp"}, {"text": "dolphin", "translation": "дельфин", "audio_tts": "dolphin", "image": "@@MEDIA@@sm3/u5/sea_dolphin.webp"}, {"text": "anchor", "translation": "якорь", "audio_tts": "anchor", "image": "@@MEDIA@@sm3/u5/sea_anchor.webp"}, {"text": "turtle", "translation": "черепаха", "audio_tts": "turtle", "image": "@@MEDIA@@sm3/u5/sea_turtle.webp"}, {"text": "shell", "translation": "ракушка", "audio_tts": "shell", "image": "@@MEDIA@@sm3/u5/sea_shell.webp"}, {"text": "octopus", "translation": "осьминог", "audio_tts": "octopus", "image": "@@MEDIA@@sm3/u5/sea_octopus.webp"}, {"text": "seahorse", "translation": "морской конёк", "audio_tts": "seahorse", "image": "@@MEDIA@@sm3/u5/sea_seahorse.webp"}, {"text": "starfish", "translation": "морская звезда", "audio_tts": "starfish", "image": "@@MEDIA@@sm3/u5/sea_starfish.webp"}, {"text": "jellyfish", "translation": "медуза", "audio_tts": "jellyfish", "image": "@@MEDIA@@sm3/u5/sea_jellyfish.webp"}, {"text": "to dive", "translation": "нырять", "audio_tts": "to dive", "image": "@@MEDIA@@sm3/u5/sea_diving_gear.webp"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"questions": [{"q": "Как по-английски «тюлень»?", "type": "single", "options": [{"text": "anchor"}, {"text": "dolphin"}, {"text": "seal"}, {"text": "turtle"}], "correct": [2]}, {"q": "Как по-английски «дельфин»?", "type": "single", "options": [{"text": "anchor"}, {"text": "dolphin"}, {"text": "shell"}, {"text": "turtle"}], "correct": [1]}, {"q": "Как по-английски «якорь»?", "type": "single", "options": [{"text": "anchor"}, {"text": "octopus"}, {"text": "shell"}, {"text": "turtle"}], "correct": [0]}, {"q": "Как по-английски «черепаха»?", "type": "single", "options": [{"text": "octopus"}, {"text": "seahorse"}, {"text": "shell"}, {"text": "turtle"}], "correct": [3]}, {"q": "Как по-английски «ракушка»?", "type": "single", "options": [{"text": "octopus"}, {"text": "seahorse"}, {"text": "shell"}, {"text": "starfish"}], "correct": [2]}, {"q": "Как по-английски «осьминог»?", "type": "single", "options": [{"text": "jellyfish"}, {"text": "octopus"}, {"text": "seahorse"}, {"text": "starfish"}], "correct": [1]}, {"q": "Как по-английски «морской конёк»?", "type": "single", "options": [{"text": "jellyfish"}, {"text": "seahorse"}, {"text": "starfish"}, {"text": "to dive"}], "correct": [1]}, {"q": "Как по-английски «морская звезда»?", "type": "single", "options": [{"text": "jellyfish"}, {"text": "seal"}, {"text": "starfish"}, {"text": "to dive"}], "correct": [2]}, {"q": "Как по-английски «медуза»?", "type": "single", "options": [{"text": "dolphin"}, {"text": "jellyfish"}, {"text": "seal"}, {"text": "to dive"}], "correct": [1]}, {"q": "Как по-английски «нырять»?", "type": "single", "options": [{"text": "anchor"}, {"text": "dolphin"}, {"text": "seal"}, {"text": "to dive"}], "correct": [3]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'exact_input', replace($blk${"items": [{"image": "@@MEDIA@@sm3/u5/sea_seal.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["seal", "Seal"], "audio_tts": "seal"}, {"image": "@@MEDIA@@sm3/u5/sea_dolphin.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["dolphin", "Dolphin"], "audio_tts": "dolphin"}, {"image": "@@MEDIA@@sm3/u5/sea_anchor.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["anchor", "Anchor"], "audio_tts": "anchor"}, {"image": "@@MEDIA@@sm3/u5/sea_turtle.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["turtle", "Turtle"], "audio_tts": "turtle"}, {"image": "@@MEDIA@@sm3/u5/sea_shell.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["shell", "Shell"], "audio_tts": "shell"}, {"image": "@@MEDIA@@sm3/u5/sea_octopus.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["octopus", "Octopus"], "audio_tts": "octopus"}, {"image": "@@MEDIA@@sm3/u5/sea_seahorse.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["seahorse", "Seahorse"], "audio_tts": "seahorse"}, {"image": "@@MEDIA@@sm3/u5/sea_starfish.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["starfish", "Starfish"], "audio_tts": "starfish"}, {"image": "@@MEDIA@@sm3/u5/sea_jellyfish.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["jellyfish", "Jellyfish"], "audio_tts": "jellyfish"}, {"image": "@@MEDIA@@sm3/u5/sea_diving_gear.webp", "prompt": "Посмотри на картинку и напиши слово", "accept": ["to dive", "To dive", "dive", "Dive"], "audio_tts": "to dive"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отлично! Слова выучены.</h3><p>Увидимся на уроке!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4);
end
$mig$;
