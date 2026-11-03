-- 03.11.2026. Текст — внутрь задания: truefalse -> quiz.
-- Группа 1: тесты GG3 u0-u8 и SM3 u0-u8, где перед блоком лежит
-- <p><b>READING.</b> Прочитай текст…</p><p>рассказ</p>.
-- Материал (рассказ) переносится в q каждого вопроса, подводка снимается.
with src(id) as (values
 ('ced08bcf-85f3-4c7c-9ed0-3a85e0114e11'::uuid),('6e44501e-d654-4a4e-88db-6775f5b6a179'),
 ('dbe68e07-9a67-4916-8da5-2a6e9a788369'),('a43dab25-c406-4019-bae3-128a52b18b13'),
 ('581bb760-610f-4b23-8e6c-e91fb8287f28'),('a310c0e7-44a4-4f23-ba14-fc7b8393ba74'),
 ('38008c25-67ce-4ba0-935b-9878c53e4694'),('539274b6-f3ef-4b54-8d1f-114d0a2f0c41'),
 ('6e319bc9-b066-443a-8eca-063c6061be64'),('61d99ef5-7821-40c8-89c8-6cc6168df876'),
 ('de2f04d3-587d-423b-9ce4-9554dc097275'),('a4345c43-e148-49e2-af1f-03f42a915704'),
 ('ba806d84-16bf-4924-b145-d29c73fda7d4'),('812079de-cf7a-40a2-8670-27ef5d984775'),
 ('af27aa01-4697-479d-81cb-5006d10aff17'),('291f905c-f62c-4b73-b738-b4cb69975022'),
 ('066151ac-3f2c-419e-a2ee-ed9464222125'),('d836a256-3204-48c7-8c77-2744591e3310')
), mat as (
  select s.id, b.payload p,
    regexp_replace((select pl.payload->>'html' from classroom_blocks pl
                    where pl.lesson_id=b.lesson_id and pl.sort_order=b.sort_order-1),
      '^<p>\s*<b>READING\.</b>[^<]*</p>','') as html
  from src s join classroom_blocks b on b.id=s.id
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
  from mat m
)
update classroom_blocks b set type='quiz', payload=u.np from upd u where b.id=u.id;
