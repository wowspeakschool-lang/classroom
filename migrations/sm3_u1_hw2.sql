-- Super Minds 3 · Unit 1 · School · Homework 2
-- собрано tools/sm3_build.py --lesson u1_hw2
do $mig$
declare
  v_course uuid;
  v_unit   uuid;
  v_lesson uuid;
  v_media  text := 'https://classroom.wowteach.ru/media/';
begin
  select id into v_course from classroom_courses where title = 'Super Minds 3';

  insert into classroom_units (course_id, title, sort_order)
  select v_course, 'Unit 1 · School', 1
  where not exists (select 1 from classroom_units
                    where course_id = v_course and title = 'Unit 1 · School');
  select id into v_unit from classroom_units
   where course_id = v_course and title = 'Unit 1 · School';

  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
  select v_unit, 'Homework 2', 'homework',
         60, false, 1
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 2');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 2';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_book.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! 👋</h2><p>Сегодня ты будешь много работать с предложениями: впишешь пропущенные слова и расставишь слова по порядку, чтобы получились верные фразы.</p><p>Удачи!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'gaps', replace($blk${"title": "Сара и Адам рассказывают о себе. Перетащи слова в пропуски", "mode": "drag", "text": "Adam:\nI love __reading__ books in English.\nI'm good at __writing__ stories, hey!\nI love __learning__ about lots of things.\nWe learn at school all __day__.\n\nSarah:\nI love __working__ on paper.\nI think Art's just __great__!\nI really like my __teachers__.\nThat's why I'm never __late__!"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'order', replace($blk${"words": ["I", "like", "speaking", "English.", "I'm", "good", "at", "it."], "sentence": "I like speaking English. I'm good at it.", "audio_tts": "I like speaking English. I'm good at it."}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'order', replace($blk${"words": ["I", "don't", "like", "learning", "Maths."], "sentence": "I don't like learning Maths.", "audio_tts": "I don't like learning Maths."}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'order', replace($blk${"words": ["I", "love", "studying", "history.", "I", "love", "my", "teacher", "too."], "sentence": "I love studying history. I love my teacher too.", "audio_tts": "I love studying history. I love my teacher too."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_star.webp\" alt=\"\" style=\"height:180px\"></p><h3>Отлично! Домашнее задание готово 🌟</h3><p>Ты молодец, встретимся на следующем уроке :)</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5);
end
$mig$;
