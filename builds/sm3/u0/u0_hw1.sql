-- SM3 · Unit 0 · Homework 1 — к уроку Lesson 1
-- Собрано скриптом builds/sm3/u0/build.py. Не заливать, пока не назовут,
-- куда переехала платформа. Проверка:
--   python3.13 tools/val.py builds/sm3/u0 sm3/u0

do $$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where slug = 'sm3';
  if v_course is null then raise exception 'курс sm3 не найден'; end if;

  select id into v_unit from classroom_units where course_id = v_course and sort_order = 0;
  if v_unit is null then
    insert into classroom_units (course_id, title, sort_order)
    values (v_course, 'Unit 0 · Meet The Explorers', 0)
    returning id into v_unit;
  end if;

  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and sort_order = 0;
  if v_lesson is null then
    insert into classroom_lessons (unit_id, title, kind, sort_order, pass_threshold, is_published)
    values (v_unit, 'Homework 1', 'homework', 0, 60, false)
    returning id into v_lesson;
  else
    update classroom_lessons
       set title = 'Homework 1', kind = 'homework', pass_threshold = 60
     where id = v_lesson;
  end if;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p>Привет! 👋 В этой домашке повторим числа от 21 до 100 и новые слова: <b>upstairs</b>, <b>downstairs</b>, <b>cellar</b>.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'quiz', replace($blk${"title": "Посмотри на картинку и выбери правильный вариант.", "questions": [{"q": "Where is the cat?", "type": "single", "correct": [0], "image": "@@MEDIA@@sm3/u0/house_upstairs.webp", "options": [{"text": "Upstairs."}, {"text": "Downstairs."}, {"text": "In the cellar."}]}, {"q": "Where is the cat?", "type": "single", "correct": [1], "image": "@@MEDIA@@sm3/u0/house_downstairs.webp", "options": [{"text": "Upstairs."}, {"text": "Downstairs."}, {"text": "In the cellar."}]}, {"q": "Where is the cat?", "type": "single", "correct": [2], "image": "@@MEDIA@@sm3/u0/house_cellar.webp", "options": [{"text": "Upstairs."}, {"text": "Downstairs."}, {"text": "In the cellar."}]}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'quiz', replace($blk${"title": "Послушай и выбери число.", "questions": [{"q": "", "type": "single", "correct": [0], "options": [{"text": "34"}, {"text": "43"}, {"text": "14"}], "audio": "", "audio_tts": "thirty-four"}, {"q": "", "type": "single", "correct": [1], "options": [{"text": "17"}, {"text": "70"}, {"text": "77"}], "audio": "", "audio_tts": "seventy"}, {"q": "", "type": "single", "correct": [0], "options": [{"text": "58"}, {"text": "85"}, {"text": "55"}], "audio": "", "audio_tts": "fifty-eight"}, {"q": "", "type": "single", "correct": [0], "options": [{"text": "61"}, {"text": "16"}, {"text": "66"}], "audio": "", "audio_tts": "sixty-one"}, {"q": "", "type": "single", "correct": [0], "options": [{"text": "99"}, {"text": "79"}, {"text": "19"}], "audio": "", "audio_tts": "ninety-nine"}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'exact_input', replace($blk${"title": "Прочитай число словами и впиши его цифрами.", "items": [{"prompt": "1. forty-two", "accept": ["42"]}, {"prompt": "2. sixty-three", "accept": ["63"]}, {"prompt": "3. eighty-seven", "accept": ["87"]}, {"prompt": "4. one hundred", "accept": ["100"]}], "needs_review": false}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Вставь пропущенные слова: upstairs · downstairs · cellar.", "text": "My bedroom is __upstairs__.\nThe kitchen is __downstairs__, next to the front door.\nThe old boxes are in the __cellar__.", "mode": "type"}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'order', replace($blk${"words": ["My", "bedroom", "is", "upstairs."], "sentence": "My bedroom is upstairs.", "audio": "", "audio_tts": "My bedroom is upstairs."}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'order', replace($blk${"words": ["The", "cellar", "is", "under", "the house."], "sentence": "The cellar is under the house.", "audio": "", "audio_tts": "The cellar is under the house."}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'speaking', replace($blk${"title": "SPEAKING TASK 🎤", "html": "<p>Расскажи про свой дом или квартиру, 4–5 предложений. Нажми на микрофон и запиши ответ.</p><p><i>For example:<br>My bedroom is upstairs.<br>The kitchen is downstairs.<br>We haven’t got a cellar.</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 7),
    (v_lesson, 'text', replace($blk${"html": "<p>Молодец! 🌟 Теперь ты знаешь, где upstairs, где downstairs и что такое cellar, и считаешь до ста.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 8)
  on conflict (lesson_id, sort_order) do update
    set type = excluded.type, payload = excluded.payload;

  raise notice 'Homework 1: % блоков', 9;
end $$;
