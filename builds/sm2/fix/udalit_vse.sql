-- SM2 — удаление лишних блоков, один скрипт на весь курс
-- Собран 22.10.2026 из builds/sm2/fix/udalit_u6_u8.sql и udalit_u9_final.sql.
-- Файлы udalit_u0_u2.sql и udalit_u3_u5.sql пустые: там удалять не понадобилось.
--
-- Что удаляется (8 блоков):
--   юнит 6 ДЗ 1 — match «слово ↔ перевод» и осиротевшая подводка к нему
--   юнит 7 ДЗ 1 — то же
--   юнит 8 ДЗ 1 — match «слово ↔ перевод»
--   юнит 9 ДЗ 1 — вторая колода карточек, дословный дубль первой
--
-- Скрипт идемпотентен: повторный запуск ничего не сломает.
-- Запускать в SQL Editor целиком, одним куском.

begin;

create temporary table udalyaem_sm2 (id uuid) on commit drop;
insert into udalyaem_sm2 (id) values
  ('a035f500-9d33-470b-95c3-44257fce9acf'::uuid),
  ('7af7746a-7703-4242-bce2-ec146d6fa314'::uuid),
  ('a0ff5cce-20ab-4a9b-9bba-1c5211adfed7'::uuid),
  ('bcf726de-aaa0-4ce7-8d6c-d360dd87bc64'::uuid),
  ('8e2378de-ce67-4125-9ffc-6f4d06fec2c8'::uuid),
  ('d313a139-c82d-4a8b-92ff-d568f182655c'::uuid),
  ('86d83f77-bc2f-47ae-9269-48a1670d7da2'::uuid),
  ('2189c8ce-169b-4802-88ad-1a19e1f2696c'::uuid);

create temporary table zatronutye_uroki_sm2 on commit drop as
select distinct lesson_id from classroom_blocks where id in (select id from udalyaem_sm2);

delete from classroom_blocks where id in (select id from udalyaem_sm2);

with novyy as (
  select b.id, row_number() over (partition by b.lesson_id order by b.sort_order) - 1 as n
  from classroom_blocks b
  where b.lesson_id in (select lesson_id from zatronutye_uroki_sm2))
update classroom_blocks b set sort_order = novyy.n + 1000
from novyy where b.id = novyy.id;

update classroom_blocks set sort_order = sort_order - 1000
where lesson_id in (select lesson_id from zatronutye_uroki_sm2) and sort_order >= 1000;

commit;

-- Проверка после запуска: обе цифры должны быть 0.
select
  (select count(*) from classroom_blocks where id in (
     'a035f500-9d33-470b-95c3-44257fce9acf',
     '7af7746a-7703-4242-bce2-ec146d6fa314',
     'a0ff5cce-20ab-4a9b-9bba-1c5211adfed7',
     'bcf726de-aaa0-4ce7-8d6c-d360dd87bc64',
     '8e2378de-ce67-4125-9ffc-6f4d06fec2c8',
     'd313a139-c82d-4a8b-92ff-d568f182655c',
     '86d83f77-bc2f-47ae-9269-48a1670d7da2',
     '2189c8ce-169b-4802-88ad-1a19e1f2696c')) as ostalos_udalyaemyh,
  (select count(*) from (
     select l.id from classroom_courses c
     join classroom_units u on u.course_id = c.id
     join classroom_lessons l on l.unit_id = u.id
     join classroom_blocks b on b.lesson_id = l.id
     where c.slug = 'sm2'
     group by l.id
     having max(b.sort_order) <> count(*) - 1 or min(b.sort_order) <> 0) z) as urokov_s_dyroy;
