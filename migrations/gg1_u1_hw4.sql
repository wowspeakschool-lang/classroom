-- Go Getter 1 · Unit 1 · Family and friends · Homework 4
-- собрано tools/gg1_build.py --lesson u1_hw4
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
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_wave.webp\" alt=\"\" style=\"height:200px\"></p><h2>Hello! 👋</h2><p>На занятии мы учились приветствовать и представлять друг друга по-английски. Повторим?</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'text', replace($blk${"html": "<p>Давай повторим всё, что выучили сегодня на уроке.</p><p><img src=\"@@MEDIA@@gg1/u1/card_introductions.webp\" alt=\"Introductions\" style=\"max-width:100%\"></p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'hotspot', replace($blk${"title": "Заполни диалог: что говорит Джилл? Подпиши облачка", "mode": "label", "image": "@@MEDIA@@gg1/u1/comic_jill_1.webp", "points": [{"x": 54.0, "y": 27.0, "text": "Hi, Mum!"}, {"x": 66.0, "y": 53.0, "text": "This is Amy."}], "extras": ["Sorry, Mum!", "It's OK, Mum!", "I'm Amy.", "Here you are, Amy."]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'hotspot', replace($blk${"title": "Продолжение: что говорят мама Джилл и Эми? Подпиши облачка", "mode": "label", "image": "@@MEDIA@@gg1/u1/comic_jill_2.webp", "points": [{"x": 68.0, "y": 17.0, "text": "Hello, Amy."}, {"x": 65.0, "y": 69.0, "text": "Nice to meet you, Mrs Wilson."}], "extras": ["Thank you, Amy.", "You're Amy.", "Nice to meet you, Jill."]}$blk$, '@@MEDIA@@', v_media)::jsonb, 3),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски", "mode": "drag", "image": "@@MEDIA@@gg1/u1/teens_skatepark.webp", "text": "Thomas: Hi, Stella, __this is__ Frankie. __He's__ my cousin.\nStella: __Hi__, Frankie. Nice __to meet you__.\nFrankie: __Nice__ to meet you too, Stella."}$blk$, '@@MEDIA@@', v_media)::jsonb, 4),
    (v_lesson, 'gaps', replace($blk${"title": "Какие фразы лучше всего подойдут, чтобы получился диалог?", "mode": "drag", "text": "May: __Hi, Auntie Sue.__\nAuntie Sue: Oh, hello, May!\nMay: And this is Nancy. __She's my best friend at school.__\nAuntie Sue: Hello, Nancy. __Nice to meet you.__\nNancy: Hello, Mrs Smith. __Nice to meet you too.__"}$blk$, '@@MEDIA@@', v_media)::jsonb, 5),
    (v_lesson, 'speaking', replace($blk${"title": "Знакомство 🎤", "html": "<p>Представь, что ты знакомишь своего друга с мамой. Нажми на микрофон и разыграй знакомство.</p><p><i>Пример: Hi, Mum! This is my friend Tom. He's my classmate. — Nice to meet you, Mrs Brown!</i></p>", "needs_review": true}$blk$, '@@MEDIA@@', v_media)::jsonb, 6),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_clap.webp\" alt=\"\" style=\"height:180px\"></p><h3>У тебя отлично получилось! 🎉</h3><p>Увидимся на занятии! Bye!</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 7);
end
$mig$;
