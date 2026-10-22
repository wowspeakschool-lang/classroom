-- Задания на перевод — блоки на удаление
-- Собрано 22.10.2026 по решению Анны («Пары „слово ↔ перевод“ — то же самое
-- задание, его тоже не делаем»; «если рядом в той же домашке уже есть задание
-- на том же наборе слов, переделка даст дубль — тогда блок удаляем»).
-- Образец — builds/sm2/fix/udalit_vse.sql.
--
-- Запускать целиком в Supabase → SQL Editor: через MCP `delete` зависает.
-- Скрипт идемпотентен, повторный запуск ничего не сломает.
--
-- ЧТО УДАЛЯЕТСЯ (1 блок)
--
-- SM1 · юнит 5 · Homework 7 · блок 10 — `gaps` в режиме «впиши»,
--   «Впиши нужный день недели»:
--     1. I play football on __Mondays__. (пн)
--     2. I go swimming on __Wednesdays__. (ср)   … и так пять пунктов.
--   Английское предложение не определяет день вообще: ответ целиком задаёт
--   русское сокращение в скобках. То есть это «переведи пн → Mondays»,
--   а не работа с языком.
--   Переделывать не во что: у дней недели картинки не бывает, а писать день
--   ребёнок в этой же домашке уже учится — блок 8 «Составь слово из букв:
--   d · a · y · M · o · n» даёт ровно тот же навык на том же наборе слов.
--   Дни недели в ДЗ 7 закрыты ещё двумя заданиями: блок 4 (`sequence` —
--   расставь дни по порядку) и блок 9 (`gaps` drag — «On __Mondays__ I go
--   __swimming__»). Поэтому блок снимаем.
--   После удаления в ДЗ 7 остаётся 12 блоков (9 заданий) — выше ориентира в 8.
--
-- Копия удаляемого блока лежит в classroom_backup_perevod_20261022.

begin;

create temporary table udalyaem_perevod (id uuid) on commit drop;
insert into udalyaem_perevod (id) values
  ('8b8966fd-d798-4f86-bf4b-7af2158e4d76'::uuid);   -- SM1 u5 ДЗ 7, блок 10

create temporary table zatronutye_uroki_perevod on commit drop as
select distinct lesson_id from classroom_blocks where id in (select id from udalyaem_perevod);

delete from classroom_blocks where id in (select id from udalyaem_perevod);

-- перенумерация затронутых уроков: сначала в «безопасную» зону, потом обратно,
-- чтобы не нарушить уникальный ключ (lesson_id, sort_order)
with novyy as (
  select b.id, row_number() over (partition by b.lesson_id order by b.sort_order) - 1 as n
  from classroom_blocks b
  where b.lesson_id in (select lesson_id from zatronutye_uroki_perevod))
update classroom_blocks b set sort_order = novyy.n + 1000
from novyy where b.id = novyy.id;

update classroom_blocks set sort_order = sort_order - 1000
where lesson_id in (select lesson_id from zatronutye_uroki_perevod) and sort_order >= 1000;

commit;

-- Проверка после запуска: обе цифры должны быть 0.
select
  (select count(*) from classroom_blocks
    where id = '8b8966fd-d798-4f86-bf4b-7af2158e4d76') as ostalos_udalyaemyh,
  (select count(*) from (
     select l.id from classroom_courses c
     join classroom_units u on u.course_id = c.id
     join classroom_lessons l on l.unit_id = u.id
     join classroom_blocks b on b.lesson_id = l.id
     where c.slug = 'sm1'
     group by l.id
     having max(b.sort_order) <> count(*) - 1 or min(b.sort_order) <> 0) z) as urokov_s_dyroy;
