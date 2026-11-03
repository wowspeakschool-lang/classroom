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
