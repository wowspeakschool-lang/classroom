-- 03.11.2026. Группа 3: два особых случая.
-- 1) GG1 Unit 1 Test, блок 16 (LISTENING). Запись лежала в текстовом блоке 15 —
--    на экране задания её не было слышно. Переносим запись в каждый вопрос
--    (questions[i].audio), картинку Эммы — в материал.
with mat as (
  select b.id, b.payload p,
    $m$<p><img src="https://classroom.wowteach.ru/media/gg1/u1/t1_emma_park.webp" alt="Emma" style="max-width:100%"></p>$m$ as html,
    'https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_u1_test_b14.mp3' as aud
  from classroom_blocks b where b.id = 'f2700e68-4d87-46a9-94ea-1245f4faedf9'
), upd as (
  select m.id, jsonb_strip_nulls(jsonb_build_object(
    'title', m.p->'title',
    'skill', m.p->'skill',
    'questions', (select jsonb_agg(jsonb_build_object(
         'q', m.html || '<p><b>' || (st->>'text') || '</b></p>',
         'type','single',
         'audio', to_jsonb(m.aud),
         'options','[{"text":"Верно"},{"text":"Неверно"}]'::jsonb,
         'correct', case when (st->>'correct')::boolean then '[0]'::jsonb else '[1]'::jsonb end
       ) order by ord)
       from jsonb_array_elements(m.p->'statements') with ordinality t(st,ord))
  )) as np
  from mat m
)
update classroom_blocks b set type='quiz', payload=u.np from upd u where b.id=u.id;

-- 2) SM1 Final Test, блок 4. В текстовом блоке лежал лист из пяти нумерованных
--    картинок, каждое утверждение — про свою картинку. В квизе каждый вопрос
--    получает только свою картинку.
update classroom_blocks set type='quiz', payload = jsonb_build_object(
  'title', 'Посмотри на картинку и прочитай предложение. Верно или неверно?',
  'skill', 'reading',
  'questions', jsonb_build_array(
    jsonb_build_object('q', $q$<p><img src="https://classroom.wowteach.ru/media/sm1/ft/ft_eraser.webp" alt="" style="max-width:220px;border-radius:10px"></p><p><b>It's a ruler.</b></p>$q$,
      'type','single','options','[{"text":"Верно"},{"text":"Неверно"}]'::jsonb,'correct','[1]'::jsonb),
    jsonb_build_object('q', $q$<p><img src="https://classroom.wowteach.ru/media/sm1/ft/ft_spider.webp" alt="" style="max-width:220px;border-radius:10px"></p><p><b>It's a spider.</b></p>$q$,
      'type','single','options','[{"text":"Верно"},{"text":"Неверно"}]'::jsonb,'correct','[0]'::jsonb),
    jsonb_build_object('q', $q$<p><img src="https://classroom.wowteach.ru/media/sm1/ft/ft_bike.webp" alt="" style="max-width:220px;border-radius:10px"></p><p><b>It's a bike.</b></p>$q$,
      'type','single','options','[{"text":"Верно"},{"text":"Неверно"}]'::jsonb,'correct','[0]'::jsonb),
    jsonb_build_object('q', $q$<p><img src="https://classroom.wowteach.ru/media/sm1/ft/ft_arm.webp" alt="" style="max-width:220px;border-radius:10px"></p><p><b>It's a leg.</b></p>$q$,
      'type','single','options','[{"text":"Верно"},{"text":"Неверно"}]'::jsonb,'correct','[1]'::jsonb),
    jsonb_build_object('q', $q$<p><img src="https://classroom.wowteach.ru/media/sm1/u4/food_chicken.webp" alt="" style="max-width:220px;border-radius:10px"></p><p><b>It's a chicken.</b></p>$q$,
      'type','single','options','[{"text":"Верно"},{"text":"Неверно"}]'::jsonb,'correct','[0]'::jsonb)
  ))
where id = '7b047858-cfb5-49f3-a134-ecb22e79a14e';
