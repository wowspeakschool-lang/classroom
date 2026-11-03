-- 03.11.2026. Группа 2Б: truefalse -> quiz, материал — картинка предыдущего блока.
-- mode: img  — все картинки предыдущего блока
--       img2 — картинки двух предыдущих блоков (разворот истории SM3)
with src(id, mode) as (values
 ('5c26a39d-d4a3-4dfe-bc32-53368cd18113'::uuid,'img'),
 ('55e97931-6b23-430d-8b31-8f9b34b926f9','img'),
 ('353222a0-a045-4f3b-8d38-fd96251bb033','img'),
 ('c0a1003b-0545-4d4f-96af-49ae012ba694','img'),
 ('3d78fb65-0793-4dc3-b0ec-5dca4629f070','img'),
 ('051f9d55-b4ef-42fe-bd3d-c9bb6d2cc758','img'),
 ('5aa193b6-ddd6-4551-b4ad-59ebc9f47dde','img'),
 ('0e481c80-e283-42b7-9619-783c2b855321','img'),
 ('f1f9e53a-4737-4e68-8003-145d9192dcf1','img'),
 ('9c9d5273-9141-4214-9305-0f36c614337c','img'),
 ('5a6fbcf5-8cb0-4d25-90c9-c852b138e2a5','img'),
 ('a15e92ee-c5a1-400a-b0b6-915f9224cb2b','img2'),
 ('3b891143-b8ae-4c62-9e2f-f5d780a925b0','img2')
), mat as (
  select s.id, s.mode, b.payload p,
    (select pl.payload->>'html' from classroom_blocks pl where pl.lesson_id=b.lesson_id and pl.sort_order=b.sort_order-1) h1,
    (select pl.payload->>'html' from classroom_blocks pl where pl.lesson_id=b.lesson_id and pl.sort_order=b.sort_order-2) h2
  from src s join classroom_blocks b on b.id=s.id
), mat2 as (
  select m.*,
    (select string_agg('<p><img src="'||g[1]||'" style="max-width:100%"></p>','' order by ord)
       from regexp_matches(m.h1,'<img[^>]*src="([^"]+)"','g') with ordinality t(g,ord)) i1,
    (select string_agg('<p><img src="'||g[1]||'" style="max-width:100%"></p>','' order by ord)
       from regexp_matches(m.h2,'<img[^>]*src="([^"]+)"','g') with ordinality t(g,ord)) i2
  from mat m
), mat3 as (
  select id, p, case mode when 'img' then i1 when 'img2' then i2||i1 end html from mat2
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
