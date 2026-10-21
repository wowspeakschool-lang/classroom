-- SM2 · юнит 9 и юнит Final Test — блоки на удаление после вычитки.
-- Запускать в Supabase → SQL Editor целиком (через MCP delete зависает).
-- Удаляется 1 блок. После удаления скрипт сам выравнивает нумерацию
-- блоков в задетых уроках.
--
-- Что удаляется:
--   юнит 9 · Homework 1 · блок 3 (как в редакторе) — flashcards «Запомни слова».
--   Это дословная копия блока 2: те же девять фраз, те же девять картинок,
--   отличие только в том, что в блоке 2 карточка переворачивается переводом,
--   а в блоке 3 перевода нет. Рендер карточек одинаковый, то есть ребёнок
--   подряд листает одну и ту же колоду дважды. В выгрузке это были две разные
--   механики («Карточки» и «Запомни»), у нас они совпали.
--   Если колоду без перевода хочется сохранить — не запускайте этот скрипт,
--   порядок блоков от этого не поломается.

begin;

create temporary table udalyaem_sm2_u9 (id uuid) on commit drop;
insert into udalyaem_sm2_u9 (id) values
 ('2189c8ce-169b-4802-88ad-1a19e1f2696c'::uuid);

create temporary table zatronutye_uroki_sm2_u9 on commit drop as
select distinct lesson_id from classroom_blocks where id in (select id from udalyaem_sm2_u9);

delete from classroom_blocks where id in (select id from udalyaem_sm2_u9);

-- нумерация блоков снова подряд с нуля
with novyy as (
  select b.id, row_number() over (partition by b.lesson_id order by b.sort_order) - 1 as n
  from classroom_blocks b
  where b.lesson_id in (select lesson_id from zatronutye_uroki_sm2_u9))
update classroom_blocks b set sort_order = novyy.n + 1000
from novyy where b.id = novyy.id;

update classroom_blocks set sort_order = sort_order - 1000
where lesson_id in (select lesson_id from zatronutye_uroki_sm2_u9) and sort_order >= 1000;

commit;
