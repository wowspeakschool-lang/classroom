-- SM1 · удаление блоков по решениям Анны от 20.10.2026
-- Запускать в Supabase → SQL Editor: через MCP delete не проходит.
--
-- Что удаляется (55 блоков):
--   фоника — 21            буквы и буквосочетания, задания на них
--   текстовый повтор — 12  «Сегодня мы повторим…» там, где уже есть карточки
--   рекламный баннер — 18  «Информация для родителей», 3 бесплатных урока
--   дубль после расклейки — 4  лишние «соедини цифру/цвет и слово» в юните 0
--
-- Копия всех этих блоков уже сделана: classroom_backup_sm1_fonika_20261020
-- (столбец prichina говорит, за что блок попал в список). Вернуть блок можно
-- оттуда — payload, тип и прежний sort_order сохранены.

begin;

-- 1. запомнить уроки, которых коснётся удаление
create temporary table zatronutye_uroki on commit drop as
select distinct lesson_id from classroom_backup_sm1_fonika_20261020;

-- 2. удалить блоки
delete from classroom_blocks
where id in (select id from classroom_backup_sm1_fonika_20261020);

-- 3. убрать дыры в нумерации: sort_order снова подряд с нуля
with novyy as (
  select b.id, row_number() over (partition by b.lesson_id order by b.sort_order) - 1 as n
  from classroom_blocks b
  where b.lesson_id in (select lesson_id from zatronutye_uroki))
update classroom_blocks b set sort_order = novyy.n + 1000
from novyy where b.id = novyy.id;

update classroom_blocks set sort_order = sort_order - 1000
where lesson_id in (select lesson_id from zatronutye_uroki) and sort_order >= 1000;

commit;

-- 4. проверка: дыр в нумерации нет, удалённых блоков в курсе не осталось
select
  (select count(*) from classroom_blocks b
     where b.id in (select id from classroom_backup_sm1_fonika_20261020)) as ostalos_udalyaemyh,
  (select count(*) from (
      select b.lesson_id, count(*) as n, min(b.sort_order) as mn, max(b.sort_order) as mx
      from classroom_courses c
      join classroom_units u on u.course_id = c.id
      join classroom_lessons l on l.unit_id = u.id
      join classroom_blocks b on b.lesson_id = l.id
      where c.slug = 'sm1' group by b.lesson_id) t
    where t.mn <> 0 or t.mx <> t.n - 1) as urokov_s_dyroy;
