-- SM2 · юниты 0, 1, 2 — блоки на удаление после вычитки (решение 3а: текстовый
-- «Давай повторим всё, что выучили на уроке» не нужен там, где есть карточки).
-- Запускать в Supabase → SQL Editor целиком. Удаляются 4 текстовых блока.
-- После удаления скрипт сам выравнивает нумерацию блоков в задетых уроках.
--
-- Что удаляем (номер блока — как в редакторе, на 22.10.2026, после перестановки):
--   Unit 0 · Homework 1 · блок 4 — «Давай повторим…» + карточка лексики card_vocab_objects
--   Unit 0 · Homework 5 · блок 3 — «Давай повторим…» + карточки фраз card_keyphrases_1/2
--   Unit 1 · Homework 1 · блок 4 — «Давай повторим…» + карточка лексики card_vocab_routine
--   Unit 2 · Homework 1 · блок 4 — «Вот все слова урока…» + карточка card_vocab_animals
-- В каждом из этих уроков те же слова уже даны блоком flashcards, который теперь
-- стоит вторым блоком.

begin;

create temporary table udalyaem_sm2_u0_u2 (id uuid) on commit drop;
insert into udalyaem_sm2_u0_u2 (id) values
 ('4ce977fe-dca5-46b7-8c8a-026cdb99cff7'::uuid),  -- u0 ДЗ 1
 ('da5af1cc-39c0-4362-aeb7-d7f7012abfe7'::uuid),  -- u0 ДЗ 5
 ('53dfd7aa-3e1c-43b4-9d97-d3b3849e8400'::uuid),  -- u1 ДЗ 1
 ('55d09121-aaa1-4b84-9c1b-ec65f8021153'::uuid);  -- u2 ДЗ 1

create temporary table zatronutye_uroki_sm2 on commit drop as
select distinct lesson_id from classroom_blocks where id in (select id from udalyaem_sm2_u0_u2);

delete from classroom_blocks where id in (select id from udalyaem_sm2_u0_u2);

-- нумерация блоков снова подряд с нуля
with novyy as (
  select b.id, row_number() over (partition by b.lesson_id order by b.sort_order) - 1 as n
  from classroom_blocks b
  where b.lesson_id in (select lesson_id from zatronutye_uroki_sm2))
update classroom_blocks b set sort_order = novyy.n + 1000
from novyy where b.id = novyy.id;

update classroom_blocks set sort_order = sort_order - 1000
where lesson_id in (select lesson_id from zatronutye_uroki_sm2) and sort_order >= 1000;

commit;
