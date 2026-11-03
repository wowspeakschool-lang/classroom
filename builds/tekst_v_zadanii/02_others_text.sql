-- 03.11.2026. Группа 2А: truefalse -> quiz, материал — текст предыдущего блока.
-- mode: strip  — снять подводку (arg) с html предыдущего блока
--       strip2 — то же, но материал лежит за два блока до задания (GG1 u6 ДЗ 6: рассказ Джен)
--       all    — взять html предыдущего блока целиком
with src(id, mode, arg) as (values
 ('502a35fb-523a-4877-b32d-bbcb475dc7ff'::uuid,'strip',$a$<p><b>Прочитай текст, а потом выбери «Верно» или «Неверно».</b></p>$a$),
 ('aac9ef0d-12e1-4123-90b4-4d7f9d766c1b','strip',$a$<p><b>Давай прочитаем текст про Тима и выполним задания!</b></p>$a$),
 ('096754bd-8921-44a5-85e6-c64498a4448d','strip2',$a$<p><b>Прочитай небольшой текст о том, как Джен обычно проводит выходные. Подумай, похоже ли ваше времяпрепровождение?</b></p>$a$),
 ('7de8692b-d9cf-4a8b-82c8-2fa28bf780dd','strip',$a$<h3>READING</h3><p>Прочитай рассказ Лео о его образе жизни.</p>$a$),
 ('f7af7a9d-76b7-43d1-9d22-b759889c218a','strip',$a$<p>Для начала давай прочитаем текст.</p>$a$),
 ('6ba93386-ec54-4fe1-b524-cee4b8473552','strip',$a$<h3>READING</h3><p>Прочитай текст и выбери «Верно» или «Неверно».</p>$a$),
 ('e6eea8bb-c421-4f21-b833-9c5e87080108','strip',$a$<h3>READING</h3>$a$),
 ('01a2e98b-2662-4941-a1b5-655887431c12','strip',$a$<h3>READING</h3>$a$),
 ('4ad6be3c-cad2-4f53-b17f-fb08f85d733a','strip',$a$<h3>Молодец! А теперь прочитай внимательно текст</h3>$a$),
 ('766cfb8f-b0a9-450c-b3a4-511229cc6357','all',null)
), mat as (
  select s.id, s.mode, s.arg, b.payload p,
    (select pl.payload->>'html' from classroom_blocks pl where pl.lesson_id=b.lesson_id and pl.sort_order=b.sort_order-1) h1,
    (select pl.payload->>'html' from classroom_blocks pl where pl.lesson_id=b.lesson_id and pl.sort_order=b.sort_order-2) h2
  from src s join classroom_blocks b on b.id=s.id
), mat3 as (
  select id, p, case mode when 'all' then h1 when 'strip' then replace(h1,arg,'')
                          when 'strip2' then replace(h2,arg,'') end html
  from mat
), upd as (
  select m.id, jsonb_strip_nulls(jsonb_build_object(
    'title', m.p->'title',
    'skill', m.p->'skill',
    'questions', (select jsonb_agg(jsonb_build_object(
         'q', m.html || '<p><b>' || (st->>'text') || '</b></p>',
         'type','single',
         'options','[{"text":"Верно"},{"text":"Неверно"}]'::jsonb,
         'correct', case when (st->>'correct')::boolean then '[0]'::jsonb else '[1]'::jsonb end
       ) order by ord)
       from jsonb_array_elements(m.p->'statements') with ordinality t(st,ord))
  )) as np
  from mat3 m
)
update classroom_blocks b set type='quiz', payload=u.np from upd u where b.id=u.id;
