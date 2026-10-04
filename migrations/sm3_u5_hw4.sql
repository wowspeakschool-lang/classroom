-- Super Minds 3 · Unit 5 · Under the sea · Homework 4
-- собрано tools/sm3_build.py --lesson u5_hw4
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
  select v_unit, 'Homework 4', 'homework',
         60, false, 3
  where not exists (select 1 from classroom_lessons
                    where unit_id = v_unit and title = 'Homework 4');
  select id into v_lesson from classroom_lessons
   where unit_id = v_unit and title = 'Homework 4';

  delete from classroom_blocks where lesson_id = v_lesson;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/hello_laptop.webp\" alt=\"\" style=\"height:200px\"></p><h2>Привет! Какой ты молодец, что делаешь домашнюю работу :)</h2><p>Сегодня потренируем was, were, wasn’t и weren’t.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 0),
    (v_lesson, 'gaps', replace($blk${"title": "Заполни пропуски с помощью was, were, wasn’t или weren’t", "text": "1. «Where __was__ Anne yesterday?» — «She __was__ at the park with her friends.»\n2. «__Was__ Ed at school last week?» — «No, he __wasn’t__. He __was__ at home because he was sick.»\n3. «__Were__ my keys on the table?» — «No, they __weren’t__.»\n4. «__Was__ Sylvia at the birthday party?» — «Yes, she __was__. She was very happy.»\n5. «__Were__ your friends on the beach?» — «No, they __weren’t__. It was too cold.»\n6. «Where __were__ Joe and Bill on Saturday afternoon?» — «I think they were at the cinema.»"}$blk$, '@@MEDIA@@', v_media)::jsonb, 1),
    (v_lesson, 'match', replace($blk${"title": "Найди ответы на вопросы", "pairs": [{"left": "Was Jack at the swimming pool?", "right": "No, he wasn’t. It wasn’t open.", "right_audio_tts": "No, he wasn't. It wasn't open."}, {"left": "Were your brother and sister on the beach at the weekend?", "right": "Yes, they were. They were in the sea too.", "right_audio_tts": "Yes, they were. They were in the sea too."}, {"left": "Where were you on Sunday, Louise?", "right": "I was at home all day. I was tired.", "right_audio_tts": "I was at home all day. I was tired."}, {"left": "Were your grandparents in the garden, Liz?", "right": "No, they weren’t. It was too hot to do gardening.", "right_audio_tts": "No, they weren't. It was too hot to do gardening."}, {"left": "Were there seahorses and starfish in the sea?", "right": "Yes, there were! Lots of them. They were beautiful!", "right_audio_tts": "Yes, there were! Lots of them. They were beautiful!"}, {"left": "Was there a clock on the tower in the square?", "right": "Yes, there was. A very old one.", "right_audio_tts": "Yes, there was. A very old one."}]}$blk$, '@@MEDIA@@', v_media)::jsonb, 2),
    (v_lesson, 'text', replace($blk${"html": "<p><img src=\"@@MEDIA@@shared/well_done_medal.webp\" alt=\"\" style=\"height:180px\"></p><h3>Ты большой молодец!</h3><p>Спасибо за твои старания! Увидимся на уроке.</p>"}$blk$, '@@MEDIA@@', v_media)::jsonb, 3);
end
$mig$;
