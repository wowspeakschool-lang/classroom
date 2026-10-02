-- Super Minds 3 · Unit 2 · Food · Test
-- собрано tools/sm3_build.py --lesson u2_test
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 2 · Food', 2
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 2 · Food');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 2 · Food';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Test', 'test',
         90, false, 7
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Test');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Test';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с картинками", "pairs": [{"left_image": "@@MEDIA@@sm3/u2/food_bread_rolls.webp", "right": "Rolls", "right_audio_tts": "rolls"}, {"left_image": "@@MEDIA@@sm3/u2/food_vegetables.webp", "right": "Vegetables", "right_audio_tts": "vegetables"}, {"left_image": "@@MEDIA@@sm3/u2/food_soup.webp", "right": "Soup", "right_audio_tts": "soup"}, {"left_image": "@@MEDIA@@sm3/u2/food_water.webp", "right": "Water", "right_audio_tts": "water"}, {"left_image": "@@MEDIA@@sm3/u2/food_peas.webp", "right": "Peas", "right_audio_tts": "peas"}, {"left_image": "@@MEDIA@@sm3/u2/food_salad.webp", "right": "Salad", "right_audio_tts": "salad"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'match', replace($blk${"title": "Соедини слова с картинками", "pairs": [{"left_image": "@@MEDIA@@sm3/u2/food_pineapple.webp", "right": "Pineapple", "right_audio_tts": "pineapple"}, {"left_image": "@@MEDIA@@sm3/u2/food_cheese.webp", "right": "Cheese", "right_audio_tts": "cheese"}, {"left_image": "@@MEDIA@@sm3/u2/food_sausages.webp", "right": "Sausages", "right_audio_tts": "sausages"}, {"left_image": "@@MEDIA@@sm3/u2/food_onions.webp", "right": "Onions", "right_audio_tts": "onions"}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: ___ any oranges?", "type": "single", "options": [{"text": "Are there"}, {"text": "Is there"}], "correct": [0]}, {"q": "B: No, ___.", "type": "single", "options": [{"text": "there aren’t"}, {"text": "there isn’t"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: ___ there any water?", "type": "single", "options": [{"text": "Is"}, {"text": "Are"}], "correct": [0]}, {"q": "B: Yes, there ___.", "type": "single", "options": [{"text": "is"}, {"text": "are"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "There are ___ onions on the table.", "type": "single", "options": [{"text": "some"}, {"text": "any"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: Have we got ___ sandwiches?", "type": "single", "options": [{"text": "any"}, {"text": "some"}], "correct": [0]}, {"q": "B: Sorry, we haven’t got ___.", "type": "single", "options": [{"text": "any"}, {"text": "some"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'quiz', replace($blk${"title": "Заполни пропуски — выбери подходящий вариант", "questions": [{"q": "A: ___ any pizza in the fridge?", "type": "single", "options": [{"text": "Is there"}, {"text": "Are there"}], "correct": [0]}, {"q": "B: Yes, ___.", "type": "single", "options": [{"text": "there is"}, {"text": "there are"}], "correct": [0]}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'order', replace($blk${"words": ["Shall", "we", "make", "some", "soup?"], "sentence": "Shall we make some soup?", "audio_tts": "Shall we make some soup?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'order', replace($blk${"words": ["How", "about", "some", "orange", "juice?"], "sentence": "How about some orange juice?", "audio_tts": "How about some orange juice?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8),
    (v_lesson, 'order', replace($blk${"words": ["Can", "I", "have", "some", "cheese", "sandwiches?"], "sentence": "Can I have some cheese sandwiches?", "audio_tts": "Can I have some cheese sandwiches?"}$blk$, '@@MEDIA@@', v_media)::jsonb, 9),
    (v_lesson, 'order', replace($blk${"words": ["We", "haven’t", "got", "any", "pineapple", "juice."], "sentence": "We haven’t got any pineapple juice.", "audio_tts": "We haven't got any pineapple juice."}$blk$, '@@MEDIA@@', v_media)::jsonb, 10),
    (v_lesson, 'order', replace($blk${"words": ["I’d", "like", "some", "lemonade,", "please."], "sentence": "I’d like some lemonade, please.", "audio_tts": "I'd like some lemonade, please."}$blk$, '@@MEDIA@@', v_media)::jsonb, 11),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK · Part 1 🎤", "needs_review": true, "html": "<p>Расскажи о еде, которую ты любишь и не любишь. Запиши свой ответ, нажав на кнопку микрофона.</p><p><i>For example:<br>My favourite food is…<br>I don’t like eating…</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 12),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK · Part 2 🎤", "needs_review": true, "image": "@@MEDIA@@sm3/u2/scene_cafe_menu.webp", "html": "<p>Посмотри на картинку, ознакомься с меню. Затем составь диалог посетителя и официанта и разыграй его. Запиши свой ответ, нажав на кнопку микрофона.</p><p><i>For example:<br>A: Would you like a chicken roll?<br>B: No, thanks. I don’t like chicken.<br>A: Would you like a cheese sandwich?<br>B: Yes, please. I’d love one.</i></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 13);
end
$mig$;
