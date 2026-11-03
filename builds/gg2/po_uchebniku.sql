-- Go Getter 2 — девять домашек приведены к материалу учебника (решение Анны 03.11.2026:
-- «по планам идём»). Страницы: 17, 18, 29, 41, 65, 66, 78, 89, 90.
-- Копия затронутых блоков — classroom_backup_gg2_po_uchebniku_20261103 (107 строк).
-- Меняется только материал (текст/образец письма) и привязанные к нему задания.
-- Аудирования не трогаем: скриптов записей на страницах нет.

-- ============================================================
-- Unit 1 · Homework 5 — чтение: Boarding School (p.17, 1.5)
-- было: свой текст про Стива и спортшколу
-- ============================================================
do $do$
declare
  v_lesson uuid := '3894f232-5143-4498-aa0c-c575e0760cc1';
  v_text text := $t$<h3>Boarding School — What’s it really like?</h3>
<p>In films, boarding schools are exciting places, often with magic or monsters. But what is a real British boarding school like? Thirteen-year-old Laura Henderson describes a typical day at her school.</p>
<p>“We wake up at 6.30 in the morning and have breakfast in the school canteen. At 8.00, the bell rings for assembly in the hall. The great thing about boarding school is that we’re never late for school!</p>
<p>Lessons start at 9.00 and finish at 3.30. My favourite lesson is Science because we often do experiments. In the afternoon, we sometimes go to the library to read, or we do P.E. in the gym. In the evening, I often play badminton or go to a cookery class.</p>
<p>I go to a boarding school because my parents live in France. Do I miss them? Yes, but I’ve got some good friends here.</p>
<p>And no, we don’t have any magic or monsters!”</p>
<p><i>boarding school — a school where students live as well as study</i></p>$t$;
  v_q jsonb := '[]'::jsonb;
  r record;
begin
  update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = v_lesson;
  delete from classroom_blocks where lesson_id = v_lesson and sort_order in (1005,1006,1007,1008);
  update classroom_blocks set sort_order = 0 where lesson_id = v_lesson and sort_order = 1000;
  update classroom_blocks set sort_order = 1 where lesson_id = v_lesson and sort_order = 1001;
  update classroom_blocks set sort_order = 2 where lesson_id = v_lesson and sort_order = 1002;
  update classroom_blocks set sort_order = 3 where lesson_id = v_lesson and sort_order = 1003;
  update classroom_blocks set sort_order = 4 where lesson_id = v_lesson and sort_order = 1004;
  update classroom_blocks set sort_order = 9 where lesson_id = v_lesson and sort_order = 1009;

  -- 5. материал
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', jsonb_build_object('html',
      $h$<h3>Время почитать 📖</h3><p>Лора учится в школе-пансионе: там ученики не только учатся, но и живут. Прежде чем читать, подумай: чем такой день отличается от твоего?</p>$h$ || v_text), 5);

  -- 6. верно / неверно по тексту (текст внутри каждого вопроса — платформа показывает по блоку на экран)
  for r in select * from (values
      ('Laura is thirteen years old.', 0),
      ('She has breakfast at home.', 1),
      ('Lessons finish at 3.30.', 0),
      ('Her favourite lesson is Maths.', 1),
      ('In the evening she often plays badminton.', 0),
      ('Laura doesn’t miss her parents.', 1)
    ) as t(st, cr) loop
    v_q := v_q || jsonb_build_object(
      'q', v_text || '<p><b>' || r.st || '</b></p>',
      'type', 'single', 'correct', jsonb_build_array(r.cr),
      'options', jsonb_build_array(jsonb_build_object('text','Верно'), jsonb_build_object('text','Неверно')));
  end loop;
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'quiz', jsonb_build_object(
      'title', 'Прочитай текст ещё раз. Это верно или неверно?', 'questions', v_q), 6);

  -- 7. Exam Spot: выбери лучший ответ
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'quiz', jsonb_build_object(
      'title', 'Это вопросы к Лоре. Выбери ответ, который ей подходит',
      'questions', jsonb_build_array(
        jsonb_build_object('q','What do you do at the weekend, Laura?','type','single','correct',jsonb_build_array(1),
          'options', jsonb_build_array(jsonb_build_object('text','Yes, I do.'), jsonb_build_object('text','I usually go sailing.'), jsonb_build_object('text','No, I don’t have lessons at the weekend.'))),
        jsonb_build_object('q','Where do you have breakfast?','type','single','correct',jsonb_build_array(2),
          'options', jsonb_build_array(jsonb_build_object('text','Every morning.'), jsonb_build_object('text','I have toast and cereal.'), jsonb_build_object('text','In the canteen.'))),
        jsonb_build_object('q','Who is your best friend?','type','single','correct',jsonb_build_array(1),
          'options', jsonb_build_array(jsonb_build_object('text','She’s very well, thank you.'), jsonb_build_object('text','Her name is Ruby.'), jsonb_build_object('text','She’s fourteen.')))
      )), 7);

  -- 8. письменные ответы
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'task', jsonb_build_object(
      'title', 'Последнее задание ✍️',
      'needs_review', true,
      'html', $h$<p>Молодец! Прочитай текст ещё раз и письменно ответь на вопросы:</p><ol><li>What type of school does Laura go to?</li><li>What time does she wake up?</li><li>What is her favourite lesson?</li><li>When does she play badminton?</li><li>Does Laura miss her parents?</li></ol>$h$), 8);
end $do$;

-- ============================================================
-- Unit 1 · Homework 6 — образец письма: блог Дейзи «My favourite day» (p.18, 1.6)
-- было: рассказ Лили. Аудирование (четверо детей) не трогаем — скрипта на странице нет.
-- ============================================================
do $do$
declare
  v_lesson uuid := '17a7a056-ec35-467b-8b6d-031c50fe937a';
begin
  delete from classroom_blocks where lesson_id = v_lesson and sort_order in (5,7,9);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', jsonb_build_object('html',
      $h$<h3>Молодец! 👏</h3><p>Ты справился с большей частью заданий. А какой твой любимый день недели? Давай почитаем блог Дейзи — она написала о своём любимом дне для школьного сайта.</p>$h$), 5);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'gaps', jsonb_build_object(
      'title', 'Прочитай блог Дейзи и перетащи слова в пропуски',
      'mode', 'drag',
      'image', 'https://classroom.wowteach.ru/media/gg2/u1/walk_to_school.webp',
      'text', $t$My __favourite__ day
On my favourite day I get up __at__ 7 a.m. and listen to __music__. I meet my __friends__ at 8.15 and we walk to school. We often talk about our plans for the weekend.
Lessons start at 9 a.m., with Music, then __Art__ – my favourite subjects! At __lunchtime__, I sometimes play table tennis.
__In__ the afternoon, I usually go __skateboarding__ in the park with my friends. In the __evening__, we often watch music videos!
Guess what my favourite day is. Yes, it’s __Friday__!$t$), 7);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'task', jsonb_build_object(
      'title', 'Мой любимый день ✍️',
      'needs_review', true,
      'html', $h$<p>Ура, это последнее задание! Напиши о своём любимом дне недели. Возьми за образец блог Дейзи и не забудь про <b>at</b>, <b>in</b>, <b>on</b>.</p><p><i>My favourite weekday is … In the morning, I … On … I have … lessons. I do … In the afternoon/evening, I …</i></p>$h$), 9);
end $do$;

-- Unit 1 · Homework 6 — порядок: подводка к блогу должна стоять прямо перед блогом
update classroom_blocks set sort_order=1005 where lesson_id='17a7a056-ec35-467b-8b6d-031c50fe937a' and sort_order=5;
update classroom_blocks set sort_order=5    where lesson_id='17a7a056-ec35-467b-8b6d-031c50fe937a' and sort_order=6;
update classroom_blocks set sort_order=6    where lesson_id='17a7a056-ec35-467b-8b6d-031c50fe937a' and sort_order=1005;

-- ============================================================
-- Unit 2 · Homework 5 — чтение: The pancake (p.29, 2.5)
-- было: «Susie's favourite meals» и задания по нему
-- ============================================================
do $do$
declare
  v_lesson uuid := 'ccb8ec26-8db1-4014-ba1e-500fc48b8624';
  v_p1 text := $t$<p><b>1</b> Pancakes are popular all over the world, and different countries use different ingredients. They are often sweet and usually round. In France, pancakes come with chocolate. In Asia, they have fish on top. But in the UK, we have pancakes with lemons and sugar.</p>$t$;
  v_p2 text := $t$<p><b>2</b> Every year there is a day when people in the UK eat a lot of pancakes. It’s called Pancake Day and it’s always on a Tuesday, in February or March. We use 52 million eggs on this day – that’s a lot!</p>$t$;
  v_p3 text := $t$<p><b>3</b> People do lots of things with pancakes. In the UK, there are pancake competitions. People run with pancakes and throw them into the air. In the USA, pancake art is very popular. People make pictures of their favourite celebrity, like Jennifer Lawrence!</p>$t$;
  v_p4 text := $t$<p><b>4</b> It’s easy to make pancakes: you need milk, water, flour and eggs. Cook the ingredients in a pan, then throw the pancakes in the air! Good luck!</p>$t$;
  v_text text;
  v_head jsonb := '[]'::jsonb;
  v_q jsonb := '[]'::jsonb;
  v_opts jsonb := jsonb_build_array(
    jsonb_build_object('text','A The perfect pancake'),
    jsonb_build_object('text','B Let’s have fun!'),
    jsonb_build_object('text','C A special day'),
    jsonb_build_object('text','D A popular food'));
  r record;
begin
  v_text := '<h3>The pancake</h3>' || v_p1 || v_p2 || v_p3 || v_p4;

  update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = v_lesson;
  delete from classroom_blocks where lesson_id = v_lesson and sort_order in (1001,1002,1003,1004,1006);
  update classroom_blocks set sort_order = 0 where lesson_id = v_lesson and sort_order = 1000;
  update classroom_blocks set sort_order = 5 where lesson_id = v_lesson and sort_order = 1005;
  update classroom_blocks set sort_order = 7 where lesson_id = v_lesson and sort_order = 1007;
  update classroom_blocks set sort_order = 8 where lesson_id = v_lesson and sort_order = 1008;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', jsonb_build_object('html',
      $h$<h3>Время почитать 📖</h3><p>Блинчики едят во всём мире, и в каждой стране — по-своему. Прочитай текст и узнай, что такое Pancake Day.</p><p><img src="https://classroom.wowteach.ru/media/gg2/u2/pancakes.webp" alt="Pancakes" style="max-width:100%;max-height:320px"></p>$h$ || v_text), 1);

  for r in select * from (values (1,3),(2,2),(3,1),(4,0)) as t(np, cr) loop
    v_head := v_head || jsonb_build_object(
      'q', (case r.np when 1 then v_p1 when 2 then v_p2 when 3 then v_p3 else v_p4 end)
           || '<p><b>Какой заголовок подходит этому абзацу?</b></p>',
      'type','single','correct', jsonb_build_array(r.cr), 'options', v_opts);
  end loop;
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'quiz', jsonb_build_object(
      'title','Подбери заголовок к каждому абзацу текста','questions', v_head), 2);

  for r in select * from (values
      ('Which country has pancakes with chocolate?', 1, 'Asia', 'France', 'the UK'),
      ('Where can you eat pancakes with fish on top?', 1, 'In France', 'In Asia', 'In the USA'),
      ('When is Pancake Day?', 1, 'On a Sunday, in May', 'On a Tuesday, in February or March', 'On a Friday, in January'),
      ('How many eggs do people in the UK use on Pancake Day?', 2, '15 million', '52 thousand', '52 million'),
      ('Which pancake activity is popular in the USA?', 1, 'pancake competitions', 'pancake art', 'pancake football'),
      ('What ingredients do you need to make pancakes?', 0, 'milk, water, flour and eggs', 'fish, lemons and sugar', 'chocolate, cheese and water')
    ) as t(qq, cr, o1, o2, o3) loop
    v_q := v_q || jsonb_build_object(
      'q', v_text || '<p><b>' || r.qq || '</b></p>',
      'type','single','correct', jsonb_build_array(r.cr),
      'options', jsonb_build_array(jsonb_build_object('text',r.o1), jsonb_build_object('text',r.o2), jsonb_build_object('text',r.o3)));
  end loop;
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'quiz', jsonb_build_object(
      'title','Прочитай текст ещё раз и ответь на вопросы','questions', v_q), 3);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'sort', jsonb_build_object(
      'title','Распредели по странам: где что бывает с блинчиками',
      'groups', jsonb_build_array(
        jsonb_build_object('name','France','items', jsonb_build_array(jsonb_build_object('text','pancakes with chocolate'))),
        jsonb_build_object('name','Asia','items', jsonb_build_array(jsonb_build_object('text','pancakes with fish on top'))),
        jsonb_build_object('name','the UK','items', jsonb_build_array(
          jsonb_build_object('text','pancakes with lemons and sugar'),
          jsonb_build_object('text','Pancake Day'),
          jsonb_build_object('text','pancake competitions'))),
        jsonb_build_object('name','the USA','items', jsonb_build_array(
          jsonb_build_object('text','pancake art'),
          jsonb_build_object('text','pictures of famous people'))))), 4);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'gaps', jsonb_build_object(
      'title','Впиши some или any',
      'mode','type',
      'text', $t$1. In France there’s __some|Some__ chocolate on pancakes.
2. Is there __any|Any__ fish on pancakes in the UK? No, there isn’t.
3. People in the UK use __some|Some__ eggs on Pancake Day — 52 million!
4. There aren’t __any|Any__ pancake competitions in my town.
5. You need __some__ milk, water, flour and eggs to make pancakes.$t$), 6);
end $do$;

-- ============================================================
-- Unit 3 · Homework 5 — чтение: Space Adventure USA, интервью с Заком (p.41, 3.5)
-- было: интервью Tech Ted ↔ Dave. Дневник Пенни (блоки 7–10) не трогаем — это
-- отдельный вопрос сверки (материал p.44, skills revision урока 7).
-- ============================================================
do $do$
declare
  v_lesson uuid := '03f5b521-e392-41c0-b9c4-016f578d548f';
  v_text text := $t$<h3>Space Adventure USA</h3>
<p>Are you interested in Space travel? Then read Zoom Magazine’s interview with Space Cadet, Zak Cohen. 14-year-old Zak is at The Space Adventure Summer Camp in Orlando.</p>
<p><b>Hi, Zak. So, do you like it here?</b><br>Yes, the camp is great. We learn a lot about space and we do lots of activities! Look, here are some photos of what we can do at the camp.</p>
<p><b>What are you doing in this photo?</b><br>I’m sitting in a special chair and I’m flying into space. Well, not really. I’m in a simulator – it’s like a big computer game!</p>
<p><b>Are you enjoying it?</b><br>Yes, I am. It’s a bit difficult – because I’m not good at computer games! But I’m having fun!</p>
<p><b>Cool! What about space walking? Is there a simulator for that?</b><br>Yes, there is, but I’m scared of it. I don’t want to be sick!</p>
<p><b>What other things can you do at the camp?</b><br>We can make small rockets – they’re great! And we can meet real astronauts too. I’m excited about that.</p>
<p><b>And what about aliens?</b><br>Aliens? You’re joking! There aren’t any aliens in Space Adventure!</p>$t$;
  v_q jsonb := '[]'::jsonb;
  r record;
begin
  update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = v_lesson;
  delete from classroom_blocks where lesson_id = v_lesson and sort_order in (1001,1003,1004,1005,1006);
  update classroom_blocks set sort_order = 0  where lesson_id = v_lesson and sort_order = 1000;
  update classroom_blocks set sort_order = 2  where lesson_id = v_lesson and sort_order = 1002;
  update classroom_blocks set sort_order = 6  where lesson_id = v_lesson and sort_order = 1007;
  update classroom_blocks set sort_order = 7  where lesson_id = v_lesson and sort_order = 1008;
  update classroom_blocks set sort_order = 8  where lesson_id = v_lesson and sort_order = 1009;
  update classroom_blocks set sort_order = 9  where lesson_id = v_lesson and sort_order = 1010;
  update classroom_blocks set sort_order = 10 where lesson_id = v_lesson and sort_order = 1011;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', jsonb_build_object('html',
      $h$<h3>Время почитать 📖</h3><p>Журнал Zoom взял интервью у Зака — он проводит лето в космическом лагере в Орландо. Прочитай интервью, а потом запиши своё чтение.</p>$h$ || v_text), 1);

  for r in select * from (values
      ('Zak is fourteen years old.', 0),
      ('In the photo Zak is flying into space in a real rocket.', 1),
      ('Zak is good at computer games.', 1),
      ('Zak is scared of the space walking simulator.', 0),
      ('Zak can meet real astronauts at the camp.', 0),
      ('There are aliens at Space Adventure.', 1)
    ) as t(st, cr) loop
    v_q := v_q || jsonb_build_object(
      'q', v_text || '<p><b>' || r.st || '</b></p>',
      'type','single','correct', jsonb_build_array(r.cr),
      'options', jsonb_build_array(jsonb_build_object('text','Верно'), jsonb_build_object('text','Неверно')));
  end loop;
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'quiz', jsonb_build_object(
      'title','Прочитай интервью ещё раз. Это верно или неверно?','questions', v_q), 3);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'task', jsonb_build_object(
      'title','Ответь на вопросы ✍️','needs_review', true,
      'html', $h$<p>Великолепно! А теперь прочитай интервью ещё раз и письменно ответь на вопросы.</p><ol><li>Is Zak enjoying Space Camp?</li><li>What is he doing in the photo?</li><li>Is he good at computer games?</li><li>Why is he scared of the space walk?</li><li>What things can he make at the camp?</li><li>Who can he meet at the camp?</li></ol>$h$), 4);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'gaps', jsonb_build_object(
      'title','Прилагательные с предлогами. Перетащи предлог в пропуск, а потом ответь на вопросы вслух',
      'mode','drag',
      'text', $t$1. Are you interested __in__ space?
2. Are you good __at__ taking selfies?
3. Are you excited __about__ the holidays?
4. Are you scared __of__ spiders?
5. Are you worried __about__ your exams?
6. Are you bad __at__ computer games?$t$), 5);
end $do$;

-- ============================================================
-- Unit 5 · Homework 6 — чтение: Hollywood then and now (p.65, 5.5)
-- было: текст про Лондон в 1965 году
-- ============================================================
do $do$
declare
  v_lesson uuid := '5aeb7a18-2dc3-4035-a0aa-1f4cfcc1dc9d';
  v_text text := $t$<h3>Hollywood then and now</h3>
<p>Hollywood is famous for its film studios and for big, exciting films such as <i>Star Wars</i>, <i>Titanic</i> and <i>The Avengers</i>. A lot of people live there too. But it was very different in the past.</p>
<p>In 1900, Hollywood was a small village near Los Angeles. There was a post office, a hotel, two shops – and 500 people. In 1911 there was also a police station and a little film studio. The film industry was new, and films were very popular. A year later, in 1912, there were fifteen studios in the town! Hollywood wasn’t a quiet little town any more. It was full of actors, and there were restaurants and cinemas.</p>
<p>Today, Hollywood is part of Los Angeles. There are busy shopping centres, modern hotels and theatres. Millions of tourists visit Hollywood every year, and many go to Universal Studios. It’s a large theme park and a real film studio. Hollywood is very different from the small village of the past!</p>$t$;
  v_q jsonb := '[]'::jsonb;
  r record;
begin
  update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = v_lesson;
  delete from classroom_blocks where lesson_id = v_lesson and sort_order in (1001,1002,1003,1004,1005);
  update classroom_blocks set sort_order = 0 where lesson_id = v_lesson and sort_order = 1000;
  update classroom_blocks set sort_order = 6 where lesson_id = v_lesson and sort_order = 1006;
  update classroom_blocks set sort_order = 7 where lesson_id = v_lesson and sort_order = 1007;
  update classroom_blocks set sort_order = 8 where lesson_id = v_lesson and sort_order = 1008;
  update classroom_blocks set sort_order = 9 where lesson_id = v_lesson and sort_order = 1009;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', jsonb_build_object('html',
      $h$<h3>Время почитать 📖</h3><p>Голливуд знают во всём мире. А сто лет назад это была крошечная деревня. Прочитай текст и посмотри, как он менялся.</p>$h$ || v_text), 1);

  for r in select * from (values
      ('In 1900 there were 500 people in Hollywood.', 0),
      ('There wasn’t a post office in Hollywood in 1900.', 1),
      ('Films were very popular in 1911.', 0),
      ('There were fifty film studios in 1912.', 1),
      ('Universal Studios is a big cinema.', 1),
      ('Today Hollywood is part of Los Angeles.', 0)
    ) as t(st, cr) loop
    v_q := v_q || jsonb_build_object(
      'q', v_text || '<p><b>' || r.st || '</b></p>',
      'type','single','correct', jsonb_build_array(r.cr),
      'options', jsonb_build_array(jsonb_build_object('text','Верно'), jsonb_build_object('text','Неверно')));
  end loop;
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'quiz', jsonb_build_object(
      'title','Прочитай текст ещё раз. Это верно или неверно?','questions', v_q), 2);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'quiz', jsonb_build_object(
      'title','Прекрасно! Прочитай предложения и выбери правильный вариант',
      'questions', jsonb_build_array(
        jsonb_build_object('q','In 1900 Hollywood was a small ___ near Los Angeles.','type','single','correct',jsonb_build_array(1),
          'options', jsonb_build_array(jsonb_build_object('text','city'), jsonb_build_object('text','village'))),
        jsonb_build_object('q','In 1911 there was also a ___ and a little film studio.','type','single','correct',jsonb_build_array(0),
          'options', jsonb_build_array(jsonb_build_object('text','police station'), jsonb_build_object('text','train station'))),
        jsonb_build_object('q','In 1912 there were ___ studios in the town.','type','single','correct',jsonb_build_array(1),
          'options', jsonb_build_array(jsonb_build_object('text','fifty'), jsonb_build_object('text','fifteen'))),
        jsonb_build_object('q','Hollywood was full of ___.','type','single','correct',jsonb_build_array(0),
          'options', jsonb_build_array(jsonb_build_object('text','actors'), jsonb_build_object('text','farmers'))),
        jsonb_build_object('q','Today there are busy ___, modern hotels and theatres.','type','single','correct',jsonb_build_array(1),
          'options', jsonb_build_array(jsonb_build_object('text','swimming pools'), jsonb_build_object('text','shopping centres'))),
        jsonb_build_object('q','Universal Studios is a theme park and a real ___.','type','single','correct',jsonb_build_array(0),
          'options', jsonb_build_array(jsonb_build_object('text','film studio'), jsonb_build_object('text','post office')))
      )), 3);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'sort', jsonb_build_object(
      'title','Распредели по годам: что было в Голливуде и когда',
      'groups', jsonb_build_array(
        jsonb_build_object('name','Hollywood in 1900','items', jsonb_build_array(
          jsonb_build_object('text','a post office'), jsonb_build_object('text','a hotel'),
          jsonb_build_object('text','two shops'), jsonb_build_object('text','500 people'))),
        jsonb_build_object('name','Hollywood in 1911','items', jsonb_build_array(
          jsonb_build_object('text','a police station'), jsonb_build_object('text','a little film studio'))),
        jsonb_build_object('name','Hollywood in 1912','items', jsonb_build_array(
          jsonb_build_object('text','fifteen film studios'), jsonb_build_object('text','restaurants and cinemas'))),
        jsonb_build_object('name','Hollywood today','items', jsonb_build_array(
          jsonb_build_object('text','busy shopping centres'), jsonb_build_object('text','modern hotels and theatres'),
          jsonb_build_object('text','Universal Studios'))))), 4);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'gaps', jsonb_build_object(
      'title','Ещё раз прочитай текст и ответь на вопросы коротким ответом. Первый — пример',
      'mode','type',
      'text', $t$1. Was Hollywood a small village in 1900? Yes, it was.
2. Was there a post office in Hollywood in 1900? __Yes, there was|Yes, there was.|Yes there was|Yes there was.__
3. Were films popular in 1911? __Yes, they were|Yes, they were.|Yes they were|Yes they were.__
4. Were there fifty film studios in 1912? __No, there weren’t|No, there weren’t.|No there weren’t|No there weren’t.|No, there weren't|No, there weren't.|No there weren't|No there weren't.__
5. Is Hollywood part of Los Angeles today? __Yes, it is|Yes, it is.|Yes it is|Yes it is.__$t$), 5);
end $do$;

-- ============================================================
-- Unit 5 · Homework 7 — образец письма: «My town» Керри про Портри (p.66, 5.6)
-- было: шаблон про Алису из Овертауна. Аудирование (Эми и бабушка) не трогаем —
-- скрипта на странице нет, в базе остаётся запись Джимми с мамой.
-- ============================================================
do $do$
declare
  v_lesson uuid := '1f10f6db-68d3-4661-a081-73c89da2500d';
  v_text text := $t$<h3>My town</h3>
<p>Hi, my name’s Kerry and I live in Portree. It’s a village on the Isle of Skye in Scotland.</p>
<p>In the past Portree was a small fishing village and there weren’t many shops. There was a post office and bank, but there wasn’t a supermarket or a sports centre. It was a very quiet town.</p>
<p>Today Portree is different. There’s a big, modern supermarket and a new swimming pool. There’s a cinema too (my favourite place 🙂)! In the summer it’s very busy. Tourists visit the island, so Portree has restaurants and hotels. People also swim in the sea! Portree is a lovely place to live.</p>$t$;
  v_q jsonb := '[]'::jsonb;
  r record;
begin
  update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = v_lesson;
  delete from classroom_blocks where lesson_id = v_lesson and sort_order = 1007;
  update classroom_blocks set sort_order = 0 where lesson_id = v_lesson and sort_order = 1000;
  update classroom_blocks set sort_order = 1 where lesson_id = v_lesson and sort_order = 1001;
  update classroom_blocks set sort_order = 2 where lesson_id = v_lesson and sort_order = 1002;
  update classroom_blocks set sort_order = 3 where lesson_id = v_lesson and sort_order = 1003;
  update classroom_blocks set sort_order = 4 where lesson_id = v_lesson and sort_order = 1004;
  update classroom_blocks set sort_order = 5 where lesson_id = v_lesson and sort_order = 1005;
  update classroom_blocks set sort_order = 6 where lesson_id = v_lesson and sort_order = 1006;
  update classroom_blocks set sort_order = 9 where lesson_id = v_lesson and sort_order = 1008;

  for r in select * from (values
      ('Where does Kerry live?', 0, 'In Portree, on the Isle of Skye', 'In Edinburgh', 'In London'),
      ('What was Portree in the past?', 1, 'a big city', 'a small fishing village', 'a busy tourist town'),
      ('Which is Kerry’s favourite place in town?', 2, 'the swimming pool', 'the supermarket', 'the cinema'),
      ('Why is Portree very busy in the summer?', 1, 'People work in the shops.', 'Tourists visit the island.', 'There is a music festival.')
    ) as t(qq, cr, o1, o2, o3) loop
    v_q := v_q || jsonb_build_object(
      'q', v_text || '<p><b>' || r.qq || '</b></p>',
      'type','single','correct', jsonb_build_array(r.cr),
      'options', jsonb_build_array(jsonb_build_object('text',r.o1), jsonb_build_object('text',r.o2), jsonb_build_object('text',r.o3)));
  end loop;
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'quiz', jsonb_build_object(
      'title','Прочитай рассказ Керри о её городе и ответь на вопросы','questions', v_q), 7);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'task', jsonb_build_object(
      'title','Напиши о своём городе ✍️','needs_review', true,
      'html', $h$<p>А теперь напиши о своём городе или посёлке: каким он был раньше и какой он сейчас. Не забудь про прилагательные — <b>big, small, busy, quiet, modern, old, clean, dirty, interesting, boring</b>.</p><p>Вот образец — рассказ Керри:</p>$h$ || v_text ||
      $h2$<p><i>I’m … and I live in …<br>In the past my town/village was …<br>There were …, but there wasn’t …<br>Today my town/village is different. There is … and there are …</i></p>$h2$), 8);
end $do$;

-- ============================================================
-- Unit 6 · Homework 7 — образец письма: «A Great Day Out» by Matt (p.78, 6.6)
-- было: рассказ Элены о выходных. Аудирование (Меган) не трогаем — скрипта
-- на странице нет, в базе остаётся рассказ Ника.
-- ============================================================
do $do$
declare
  v_lesson uuid := 'f0e0740a-9f28-41d7-85c9-080c9d2cfbf5';
  v_text text := $t$<h3>A Great Day Out</h3><p><i>by Matt</i></p>
<p>Last Saturday, I went to London with my family. First, we visited Madame Tussaud’s. That was really cool. All my favourite actors and singers were there. I took a selfie with Usain Bolt!</p>
<p>Then, we went to the London Aquarium. We walked under the water and we watched the sharks. My brother was scared, but I wasn’t.</p>
<p>After that, we went to a Mexican restaurant. We ate tacos and drank milkshakes.</p>
<p>We arrived home at midnight. We were tired, but happy!</p>$t$;
begin
  update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = v_lesson;
  delete from classroom_blocks where lesson_id = v_lesson and sort_order in (1004,1005);
  update classroom_blocks set sort_order = 0  where lesson_id = v_lesson and sort_order = 1000;
  update classroom_blocks set sort_order = 1  where lesson_id = v_lesson and sort_order = 1001;
  update classroom_blocks set sort_order = 2  where lesson_id = v_lesson and sort_order = 1002;
  update classroom_blocks set sort_order = 3  where lesson_id = v_lesson and sort_order = 1003;
  update classroom_blocks set sort_order = 7  where lesson_id = v_lesson and sort_order = 1006;
  update classroom_blocks set sort_order = 8  where lesson_id = v_lesson and sort_order = 1007;
  update classroom_blocks set sort_order = 9  where lesson_id = v_lesson and sort_order = 1008;
  update classroom_blocks set sort_order = 10 where lesson_id = v_lesson and sort_order = 1009;
  update classroom_blocks set sort_order = 11 where lesson_id = v_lesson and sort_order = 1010;
  update classroom_blocks set sort_order = 12 where lesson_id = v_lesson and sort_order = 1011;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'gaps', jsonb_build_object(
      'title','Прочитай рассказ Мэтта о его отличном дне и впиши глаголы в прошедшем времени. Смотри пример: go → went',
      'mode','type',
      'text', $t$A Great Day Out by Matt
Last Saturday, I went (go) to London with my family. First, we __visited__ (visit) Madame Tussaud’s. That __was__ (be) really cool. All my favourite actors and singers __were__ (be) there. I __took__ (take) a selfie with Usain Bolt!
Then, we __went__ (go) to the London Aquarium. We __walked__ (walk) under the water and we __watched__ (watch) the sharks. My brother __was__ (be) scared, but I wasn’t.
After that, we went (go) to a Mexican restaurant. We __ate__ (eat) tacos and __drank__ (drink) milkshakes.
We __arrived__ (arrive) home at midnight. We __were__ (be) tired, but happy!$t$), 4);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'quiz', jsonb_build_object(
      'title','Прочитай рассказ Мэтта ещё раз и ответь на вопрос',
      'questions', jsonb_build_array(jsonb_build_object(
        'q', v_text || '<p><b>What three places did he go to?</b></p>',
        'type','single','correct', jsonb_build_array(0),
        'options', jsonb_build_array(
          jsonb_build_object('text','Madame Tussaud’s, the London Aquarium and a Mexican restaurant'),
          jsonb_build_object('text','Madame Tussaud’s, the zoo and an Italian restaurant'),
          jsonb_build_object('text','the London Eye, the London Aquarium and a café'))))), 5);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'task', jsonb_build_object(
      'title','Напиши свой рассказ ✍️','needs_review', true,
      'html', $h$<p>Супер, ты отлично справляешься! Теперь напиши небольшой рассказ о своих прошлых выходных или о каком-то памятном и интересном для тебя дне ;)</p><p>Возьми за образец рассказ Мэтта и используй слова <b>First, Then, After that</b>. Рассказ должен быть в прошедшем времени — проверяй, в какой форме ты пишешь глаголы.</p><p><i><b>First</b>, we visited Madame Tussaud’s.<br><b>Then</b>, we went to the London Aquarium.<br><b>After that</b>, we went to a Mexican restaurant.</i></p>$h$), 6);
end $do$;

-- ============================================================
-- Unit 7 · Homework 6 — чтение: Antarctic Adventure, Льюис Кларк (p.89, 7.5)
-- было: текст про Эдмунда Хиллари и Эверест
-- ============================================================
do $do$
declare
  v_lesson uuid := '6097a083-2eea-4166-8751-a5771b0f1bfb';
  v_text text := $t$<h3>Antarctic Adventure</h3>
<p>On 1 December 2014, 16-year-old Lewis Clarke got on a plane. Nineteen hours later he arrived in Antarctica. Lewis didn’t go there with his parents. He went there with an explorer, Carl Alvey. Lewis was on a Polar expedition – he wanted to be the youngest person to go to the South Pole!</p>
<p>The journey was difficult and dangerous. Lewis travelled 700 miles and skied for eight hours every day. His backpack was heavy – inside there was a tent, clothes, food, a torch and a camera. He also had his schoolwork!</p>
<p>After 48 days, Lewis arrived at the South Pole. He was happy, and he phoned his parents. Then he had his favourite meal – spaghetti bolognese!</p>
<p>Lewis was the youngest person to go to the South Pole, but it wasn’t his first world record. When he was twelve, he swam the English Channel with five other schoolchildren. Is Lewis cool – or just crazy?</p>$t$;
  v_q jsonb := '[]'::jsonb;
  r record;
begin
  update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = v_lesson;
  delete from classroom_blocks where lesson_id = v_lesson
    and sort_order in (1001,1002,1003,1004,1005,1006,1007,1008,1009);
  update classroom_blocks set sort_order = 0  where lesson_id = v_lesson and sort_order = 1000;
  update classroom_blocks set sort_order = 10 where lesson_id = v_lesson and sort_order = 1010;

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', jsonb_build_object('html',
      $h$<p>Любишь ли ты путешествовать? А ты смог бы отправиться туда, где только снег и лёд? Сегодня мы прочитаем историю Льюиса Кларка. Как думаешь, сколько ему было лет, когда он дошёл до Южного полюса?</p>$h$), 1);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', jsonb_build_object('html', $h$<h3>Время почитать 📖</h3>$h$ || v_text), 2);

  for r in select * from (values
      ('Lewis Clarke went to Antarctica by plane.', 0),
      ('Lewis went to Antarctica with his parents.', 1),
      ('The journey was easy.', 1),
      ('Lewis had his schoolwork in his backpack.', 0),
      ('There were three people in Lewis’s team.', 2),
      ('Lewis swam the English Channel alone.', 1)
    ) as t(st, cr) loop
    v_q := v_q || jsonb_build_object(
      'q', v_text || '<p><b>' || r.st || '</b></p>',
      'type','single','correct', jsonb_build_array(r.cr),
      'options', jsonb_build_array(
        jsonb_build_object('text','True'), jsonb_build_object('text','False'), jsonb_build_object('text','Not stated')));
  end loop;
  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'quiz', jsonb_build_object(
      'title','Прочитай текст ещё раз. Для каждого предложения выбери: True (правда), False (неправда) или Not stated (по тексту этого не узнать)',
      'questions', v_q), 3);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'sort', jsonb_build_object(
      'title','Распредели: что Льюис взял с собой в рюкзак, а чего у него там не было',
      'groups', jsonb_build_array(
        jsonb_build_object('name','In Lewis’s backpack','items', jsonb_build_array(
          jsonb_build_object('text','a tent'), jsonb_build_object('text','clothes'),
          jsonb_build_object('text','food'), jsonb_build_object('text','a torch'),
          jsonb_build_object('text','a camera'), jsonb_build_object('text','his schoolwork'))),
        jsonb_build_object('name','Not in his backpack','items', jsonb_build_array(
          jsonb_build_object('text','a bike'), jsonb_build_object('text','a guitar'),
          jsonb_build_object('text','a TV'))))), 4);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'match', jsonb_build_object(
      'title','Соедини слово из текста с его объяснением',
      'pairs', jsonb_build_array(
        jsonb_build_object('left','explorer','right','a person who travels to new places'),
        jsonb_build_object('left','expedition','right','a long journey with a special aim'),
        jsonb_build_object('left','record','right','the best result in the world'),
        jsonb_build_object('left','dangerous','right','not safe'),
        jsonb_build_object('left','heavy','right','difficult to carry'),
        jsonb_build_object('left','tent','right','you sleep in it when you travel'))), 5);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'sequence', jsonb_build_object(
      'title','Расставь события истории по порядку',
      'items', jsonb_build_array(
        jsonb_build_object('text','On 1 December 2014, Lewis Clarke got on a plane.'),
        jsonb_build_object('text','Nineteen hours later he arrived in Antarctica.'),
        jsonb_build_object('text','Lewis travelled 700 miles and skied for eight hours every day.'),
        jsonb_build_object('text','After 48 days, he arrived at the South Pole.'),
        jsonb_build_object('text','He phoned his parents and had spaghetti bolognese.'))), 6);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'gaps', jsonb_build_object(
      'title','Прочитай текст ещё раз и перетащи слова в пропуски',
      'mode','drag',
      'text', $t$1. Lewis was the youngest person to go to the __South Pole__.
2. He went to Antarctica with an __explorer__.
3. He skied for __eight hours__ every day.
4. The journey took __48 days__.
5. At the South Pole, Lewis phoned his parents and ate __spaghetti bolognese__.
6. He swam the English Channel when he was __twelve__.$t$), 7);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'gaps', jsonb_build_object(
      'title','А теперь те же слова — в новых предложениях. Перетащи слово в пропуск',
      'mode','drag',
      'text', $t$1. The __expedition__ to Antarctica was six months long.
2. Polar bears are __dangerous__ animals when they are hungry.
3. Christopher Columbus was a famous __explorer__.
4. Wow! Five metres in long jump! Mark, this is a school __record__!
5. My schoolbag is very __heavy__ today because I’ve got my P.E. kit.$t$), 8);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'task', jsonb_build_object(
      'title','Ответь на вопросы ✍️','needs_review', true,
      'html', $h$<p>Молодец! Осталось последнее задание. Прочитай текст ещё раз и письменно ответь на вопросы:</p><ol><li>When did Lewis get on the plane?</li><li>Who did he go to Antarctica with?</li><li>How many miles did he travel?</li><li>How long did the journey take?</li><li>What did he eat at the South Pole?</li><li>What was his first world record?</li></ol>$h$), 9);
end $do$;

-- ============================================================
-- Unit 7 · Homework 7 — образец письма: открытка Лили с Тенерифе (p.90, 7.6)
-- было: открытка Терри для Джоша. Аудирование (дети и чемоданы) не трогаем —
-- скрипта на странице нет, в базе остаётся разговор Пенни и Дэвида.
-- ============================================================
do $do$
declare
  v_lesson uuid := 'bc13d30c-8887-43b9-aa20-2e4a57e2a244';
begin
  delete from classroom_blocks where lesson_id = v_lesson and sort_order in (6,7);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'text', jsonb_build_object('html',
      $h$<p>Отлично! Теперь напишем открытку. Для начала прочитай открытку, которую Лили отправила подруге с Тенерифе, и заполни пропуски.</p>$h$), 6);

  insert into classroom_blocks (lesson_id, type, payload, sort_order) values
    (v_lesson, 'gaps', jsonb_build_object(
      'title','Перетащи фразы в пропуски',
      'mode','drag',
      'text', $t$__Hi__ Caitlin,
__We’re having a lovely time in__ Tenerife. It’s sunny here and the people are really friendly. We’re staying in a hotel. It isn’t near the beach. We go to the beach by bus.
__Yesterday we went__ sightseeing and I bought some souvenirs. Then we ate at a restaurant. We had paella and it was great!
Today we’re on the beach and I’m reading my Percy Jackson book. The beach is busy and it’s hot! Luckily, I can swim in the sea!
__See you soon!__
Lily$t$), 7);
end $do$;
