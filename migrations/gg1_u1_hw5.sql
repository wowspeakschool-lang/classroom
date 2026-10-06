-- Go Getter 1 · Unit 1 · Family and friends · Homework 5
-- собрано tools/gg1_build.py --lesson u1_hw5
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
  select v_unit, 'Homework 5', 'homework',
         60, false, 4
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 5');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 5';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_rocket.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет-привет! 👋</h2><p>Готов к новому домашнему заданию? Вперёд!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p><b>Прочитай, что ребята рассказывают о себе 😃</b></p><p><b>Silvia:</b> Hi. My name's Silvia. I'm 12 and I'm British. My brother is 9. My dad is Spanish. Ellie is my aunt — she's Spanish too. Bea is my friend. Sweep is a dog. He's our dog!</p><p><b>Nick:</b> Hello! I'm Nick. I'm British. I'm at a party today — it's my cousin's birthday. My mum and dad are at the party too.</p><p><b>Bea:</b> Hi! I'm Bea. My mother is Italian and my father is British. We aren't at school today. My granny and my grandad are in the park and my sister and my mother are in the garden.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"title": "Прочитай тексты ещё раз и соедини части предложений", "pairs": [{"left": "Hi. My name's", "right": "Silvia."}, {"left": "I'm", "right": "12."}, {"left": "My brother is", "right": "9."}, {"left": "Ellie is", "right": "my aunt."}, {"left": "Bea is", "right": "my friend."}, {"left": "Sweep is", "right": "a dog."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски словами British, Italian или Spanish", "mode": "drag", "text": "1. Silvia is __British__.\n2. Nick is __British__.\n3. Silvia's dad is __Spanish__.\n4. Aunt Ellie is __Spanish__.\n5. Bea's mother is __Italian__.\n6. Bea's father is __British__."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'exact_input', replace($blk${"title": "Догадайся, какое слово пропущено, и впиши его целиком", "items": [{"prompt": "I'm at a p… today.", "accept": ["party"], "image": "@@MEDIA@@gg1/u1/place_party.webp", "audio_tts": "I'm at a party today."}, {"prompt": "We aren't at s… today.", "accept": ["school"], "image": "@@MEDIA@@gg1/u1/place_school.webp", "audio_tts": "We aren't at school today."}, {"prompt": "My sister and my mother are in the g….", "accept": ["garden"], "image": "@@MEDIA@@gg1/u1/place_garden.webp", "audio_tts": "My sister and my mother are in the garden."}, {"prompt": "My granny and my grandad are in the p….", "accept": ["park"], "image": "@@MEDIA@@gg1/u1/place_park.webp", "audio_tts": "My granny and my grandad are in the park."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'speaking', replace($blk${"title": "Где сейчас твоя семья? 🎤", "html": "<p>Нажми на микрофон и расскажи, где сейчас члены твоей семьи и друзья.</p><p><i>Пример: My mum is at home. My dad is at school. My brother is in the park. My friends are on holiday.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_smiley.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отличная работа! 🎉</h3><p>Ещё увидимся!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 6);
end
$mig$;
