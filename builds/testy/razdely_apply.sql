-- Разделы заданий в тестах юнитов: payload.skill = grammar | vocabulary |
-- speaking | listening | reading | writing (шесть разделов трекера прогресса).
-- Решение Анны 23.10.2026: проставляем мы, методист проверяет по razdely_spisok.md.
-- Решения записаны компактно (курс юнит: номер_блока_как_в_редакторе + код),
-- ключ — курс + юнит + номер блока (в юните ровно один тест), без UUID.
-- Идемпотентно: повторный запуск ничего не меняет. Не запускать до «да».

-- 1. Копия затрагиваемых блоков (RLS включён).
create table if not exists classroom_backup_test_skill_20261023 as
with src(t) as (values ($d$
gg1 0: 2V 3G 4-8G 10R 11L 12S
gg1 1: 2V 3-7G 8-12G 14R 16L 17S
gg1 2: 2V 3-7G 8-12G 14R 16L 17S
gg1 3: 2V 3V 4G 5-9G 11R 13L 14S
gg1 4: 2V 3V 4G 5G 6-10G 11R 13L 14S
gg1 5: 2V 3V 4G 5-9G 10R 12L 13S
gg1 6: 2V 3G 4G 5G 6V 7V? 8-12G 14R 16L 17S 18S
gg1 7: 2V 3-7G 8-12G 14R 16L 17S
gg1 8: 2V 3-7G 8-12G 14R 15L 16S 17S
gg1 9: 3L 5L 7L 9R? 10R? 11-15W? 16W? 17S
gg2 0: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 1: 2V 3G 4G 5-9G 11R 12L 13S 14S
gg2 2: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 3: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 4: 2V 3G 4G 5-9G 11R 12L 13S 14S
gg2 5: 2V 3G 4G 5-9G 11R 12L 13S 14S
gg2 6: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 7: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 8: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 9: 2W 3V 4G 6R 8L 9S 10S
gg3 0: 2V 3V 4V 5V 6G 7G 8V 9G 10G? 11G 12-15G 16V 18R 20L 21W 22S
gg3 1: 2V 3W? 4V 5G 6-10G 12R 14L 15W 16S 17S
gg3 2: 2V 3W? 4V 5G 6-10G 12R 14L 15W 16S 17S
gg3 3: 2V 3W? 4G 5-9G 11R 13L 14W 15S 16S
gg3 4: 2V 3W? 4V 5G 6-10G 12R 14L 15W 16S 17S
gg3 5: 2V 3W? 4V 5V 6G 7-10G 12R 14L 15W 16S 17S
gg3 6: 2V 3W? 4V 5G 6-10G 12R 14L 15W 16S 17S
gg3 7: 2V 3W? 4V 5V 6G 7-11G 13R 15L 16W 17S 18S
gg3 8: 2V 3W? 4V 5G 6-10G 12R 14L 15W 16S 17S
gg3 9: 4L 6R 7W? 8V? 9G 10G? 11W 13S
sm0 0: 2R? 3R? 4R? 5R? 6L 7W? 8W? 9V 10V 11R 12R? 13S
sm0 1: 2R? 3W? 4W? 5R? 6V 7L 8S 9L 10S 11S
sm0 2: 2W? 3W? 4R 5R? 6R? 7R? 8R? 9R? 10V 11V 12S 13S
sm0 3: 2W? 3W? 4W? 5W? 6R? 7R? 8V 9L 10S 11S
sm0 4: 2W? 3W? 4W? 5W? 6R? 7R? 8R? 9V 10V? 11V 12L 13S 14S
sm0 5: 2W? 3W? 4W? 5W? 6R? 7R 8V 9V 10V 11V 12L 13L 14S 15S 16S
sm1 0: 2L? 3V 4V 5L 6G 7S
sm1 1: 1W 2S? 4L 6L 7V 8G 9-13G 14S
sm1 2: 1V 3L 5R 6G 7-11G 12W 13S? 14S
sm1 3: 1V 2W 3S? 4G 5-9G 10R 12L 13S
sm1 4: 1W 2V 3G 4-8G 9V 10V? 12R 13L 14S
sm1 5: 1W 2V 3G 4-8G 10R 12L 13S
sm1 6: 1W 2G 3-7G 8R 10L 11S
sm1 7: 1W 2V 3G 4G 5-9G 11L 13R 14S 15S
sm1 8: 1W 2V 3G 4-8G 10R 12L 13S
sm1 9: 1W 2V 3V? 4G? 5-9G 11L 13R 14S 15S
sm1 10: 2L 4L 6R 8R 9W? 10S 11S 12S
sm2 0: 2V 4G 6R 9L 10S
sm2 1: 3V 5G 7-11G 13R 16L 17S
sm2 2: 3V 5-9G 11-15G 17R 20L 21S
sm2 3: 2W? 3V 4G 6-10G 11R 13L 14S
sm2 4: 2W? 3V 4G 5-9G 11R 13L 14S 15S
sm2 5: 2W? 3V 4V? 5G 6-10G 11R 13L 14S
sm2 6: 2V 3V 4G 5-9G 11R 14L 15S
sm2 7: 2V 3V 4V? 5G 6-10G 12R 15L 16S 17S
sm2 8: 2V 3V 4V 5G 6-10G 12R 15L 16S
sm2 9: 2V 3G? 4G 5-9G 11R 13L 14S
sm2 10: 4L 5L 7W? 8V 9G 10V? 11-15G 17R 18S 19W
sm3 0: 2L 3V? 4G 5-8G 9G 11V 12R? 13R? 15R 17L 18W 19S
sm3 1: 1V 2-6G 7-11G 12S
sm3 2: 1V 2V 3-7G 8-12G 13S 14S
sm3 3: 1V 2V 3G 4G 5V? 6V? 7G 8-12G 13S
sm3 4: 1V 2-4G 5G? 6G 7G 8-12G 13S 14S
sm3 5: 1V 2-7G 8-12G 13S
sm3 6: 1V 2V 3-7G 8-12G 13S 14S
sm3 7: 1V 2-6G 7-11G 12S
sm3 8: 1V 2-6G 7-11G 12S
sm3 9: 1V 2V? 3V? 4-7G 8-12G 13S 14S
sm3 10: 4L 5L 7L 9V? 10R? 12R
$d$)),
lines as (
  select split_part(split_part(l, ':', 1), ' ', 1) as slug,
         split_part(split_part(l, ':', 1), ' ', 2)::int as unit,
         trim(split_part(l, ':', 2)) as rest
  from src, regexp_split_to_table(t, E'\n') l where l ~ '^[a-z0-9]+ [0-9]+:'),
toks as (
  select slug, unit, regexp_match(tok, '^([0-9]+)(?:-([0-9]+))?([GVSLRW])([?])?$') as m
  from lines, regexp_split_to_table(rest, '\s+') tok),
dec as (
  select slug, unit, n as block_no,
         case m[3] when 'G' then 'grammar' when 'V' then 'vocabulary' when 'S' then 'speaking'
                   when 'L' then 'listening' when 'R' then 'reading' else 'writing' end as skill,
         m[4] is not null as guess
  from toks, generate_series(m[1]::int, coalesce(m[2], m[1])::int) n),
blk as (
  select c.slug, u.sort_order as unit, l.title as test_title, b.sort_order + 1 as block_no, b.id, b.type,
         coalesce(b.payload->>'title', '') as title
  from classroom_courses c join classroom_units u on u.course_id = c.id
  join classroom_lessons l on l.unit_id = u.id join classroom_blocks b on b.lesson_id = l.id
  where l.kind = 'test' and c.slug in ('gg1','gg2','gg3','sm0','sm1','sm2','sm3'))
select x.* from classroom_blocks x where x.id in (select b.id from blk b join dec d using (slug, unit, block_no));
alter table classroom_backup_test_skill_20261023 enable row level security;

-- 2. Проставить раздел.
with src(t) as (values ($d$
gg1 0: 2V 3G 4-8G 10R 11L 12S
gg1 1: 2V 3-7G 8-12G 14R 16L 17S
gg1 2: 2V 3-7G 8-12G 14R 16L 17S
gg1 3: 2V 3V 4G 5-9G 11R 13L 14S
gg1 4: 2V 3V 4G 5G 6-10G 11R 13L 14S
gg1 5: 2V 3V 4G 5-9G 10R 12L 13S
gg1 6: 2V 3G 4G 5G 6V 7V? 8-12G 14R 16L 17S 18S
gg1 7: 2V 3-7G 8-12G 14R 16L 17S
gg1 8: 2V 3-7G 8-12G 14R 15L 16S 17S
gg1 9: 3L 5L 7L 9R? 10R? 11-15W? 16W? 17S
gg2 0: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 1: 2V 3G 4G 5-9G 11R 12L 13S 14S
gg2 2: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 3: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 4: 2V 3G 4G 5-9G 11R 12L 13S 14S
gg2 5: 2V 3G 4G 5-9G 11R 12L 13S 14S
gg2 6: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 7: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 8: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 9: 2W 3V 4G 6R 8L 9S 10S
gg3 0: 2V 3V 4V 5V 6G 7G 8V 9G 10G? 11G 12-15G 16V 18R 20L 21W 22S
gg3 1: 2V 3W? 4V 5G 6-10G 12R 14L 15W 16S 17S
gg3 2: 2V 3W? 4V 5G 6-10G 12R 14L 15W 16S 17S
gg3 3: 2V 3W? 4G 5-9G 11R 13L 14W 15S 16S
gg3 4: 2V 3W? 4V 5G 6-10G 12R 14L 15W 16S 17S
gg3 5: 2V 3W? 4V 5V 6G 7-10G 12R 14L 15W 16S 17S
gg3 6: 2V 3W? 4V 5G 6-10G 12R 14L 15W 16S 17S
gg3 7: 2V 3W? 4V 5V 6G 7-11G 13R 15L 16W 17S 18S
gg3 8: 2V 3W? 4V 5G 6-10G 12R 14L 15W 16S 17S
gg3 9: 4L 6R 7W? 8V? 9G 10G? 11W 13S
sm0 0: 2R? 3R? 4R? 5R? 6L 7W? 8W? 9V 10V 11R 12R? 13S
sm0 1: 2R? 3W? 4W? 5R? 6V 7L 8S 9L 10S 11S
sm0 2: 2W? 3W? 4R 5R? 6R? 7R? 8R? 9R? 10V 11V 12S 13S
sm0 3: 2W? 3W? 4W? 5W? 6R? 7R? 8V 9L 10S 11S
sm0 4: 2W? 3W? 4W? 5W? 6R? 7R? 8R? 9V 10V? 11V 12L 13S 14S
sm0 5: 2W? 3W? 4W? 5W? 6R? 7R 8V 9V 10V 11V 12L 13L 14S 15S 16S
sm1 0: 2L? 3V 4V 5L 6G 7S
sm1 1: 1W 2S? 4L 6L 7V 8G 9-13G 14S
sm1 2: 1V 3L 5R 6G 7-11G 12W 13S? 14S
sm1 3: 1V 2W 3S? 4G 5-9G 10R 12L 13S
sm1 4: 1W 2V 3G 4-8G 9V 10V? 12R 13L 14S
sm1 5: 1W 2V 3G 4-8G 10R 12L 13S
sm1 6: 1W 2G 3-7G 8R 10L 11S
sm1 7: 1W 2V 3G 4G 5-9G 11L 13R 14S 15S
sm1 8: 1W 2V 3G 4-8G 10R 12L 13S
sm1 9: 1W 2V 3V? 4G? 5-9G 11L 13R 14S 15S
sm1 10: 2L 4L 6R 8R 9W? 10S 11S 12S
sm2 0: 2V 4G 6R 9L 10S
sm2 1: 3V 5G 7-11G 13R 16L 17S
sm2 2: 3V 5-9G 11-15G 17R 20L 21S
sm2 3: 2W? 3V 4G 6-10G 11R 13L 14S
sm2 4: 2W? 3V 4G 5-9G 11R 13L 14S 15S
sm2 5: 2W? 3V 4V? 5G 6-10G 11R 13L 14S
sm2 6: 2V 3V 4G 5-9G 11R 14L 15S
sm2 7: 2V 3V 4V? 5G 6-10G 12R 15L 16S 17S
sm2 8: 2V 3V 4V 5G 6-10G 12R 15L 16S
sm2 9: 2V 3G? 4G 5-9G 11R 13L 14S
sm2 10: 4L 5L 7W? 8V 9G 10V? 11-15G 17R 18S 19W
sm3 0: 2L 3V? 4G 5-8G 9G 11V 12R? 13R? 15R 17L 18W 19S
sm3 1: 1V 2-6G 7-11G 12S
sm3 2: 1V 2V 3-7G 8-12G 13S 14S
sm3 3: 1V 2V 3G 4G 5V? 6V? 7G 8-12G 13S
sm3 4: 1V 2-4G 5G? 6G 7G 8-12G 13S 14S
sm3 5: 1V 2-7G 8-12G 13S
sm3 6: 1V 2V 3-7G 8-12G 13S 14S
sm3 7: 1V 2-6G 7-11G 12S
sm3 8: 1V 2-6G 7-11G 12S
sm3 9: 1V 2V? 3V? 4-7G 8-12G 13S 14S
sm3 10: 4L 5L 7L 9V? 10R? 12R
$d$)),
lines as (
  select split_part(split_part(l, ':', 1), ' ', 1) as slug,
         split_part(split_part(l, ':', 1), ' ', 2)::int as unit,
         trim(split_part(l, ':', 2)) as rest
  from src, regexp_split_to_table(t, E'\n') l where l ~ '^[a-z0-9]+ [0-9]+:'),
toks as (
  select slug, unit, regexp_match(tok, '^([0-9]+)(?:-([0-9]+))?([GVSLRW])([?])?$') as m
  from lines, regexp_split_to_table(rest, '\s+') tok),
dec as (
  select slug, unit, n as block_no,
         case m[3] when 'G' then 'grammar' when 'V' then 'vocabulary' when 'S' then 'speaking'
                   when 'L' then 'listening' when 'R' then 'reading' else 'writing' end as skill,
         m[4] is not null as guess
  from toks, generate_series(m[1]::int, coalesce(m[2], m[1])::int) n),
blk as (
  select c.slug, u.sort_order as unit, l.title as test_title, b.sort_order + 1 as block_no, b.id, b.type,
         coalesce(b.payload->>'title', '') as title
  from classroom_courses c join classroom_units u on u.course_id = c.id
  join classroom_lessons l on l.unit_id = u.id join classroom_blocks b on b.lesson_id = l.id
  where l.kind = 'test' and c.slug in ('gg1','gg2','gg3','sm0','sm1','sm2','sm3'))
update classroom_blocks x set payload = x.payload || jsonb_build_object('skill', d.skill)
from blk b join dec d using (slug, unit, block_no)
where x.id = b.id and x.payload->>'skill' is distinct from d.skill;

-- 3. Проверка: сколько блоков с разделом по курсам.
with src(t) as (values ($d$
gg1 0: 2V 3G 4-8G 10R 11L 12S
gg1 1: 2V 3-7G 8-12G 14R 16L 17S
gg1 2: 2V 3-7G 8-12G 14R 16L 17S
gg1 3: 2V 3V 4G 5-9G 11R 13L 14S
gg1 4: 2V 3V 4G 5G 6-10G 11R 13L 14S
gg1 5: 2V 3V 4G 5-9G 10R 12L 13S
gg1 6: 2V 3G 4G 5G 6V 7V? 8-12G 14R 16L 17S 18S
gg1 7: 2V 3-7G 8-12G 14R 16L 17S
gg1 8: 2V 3-7G 8-12G 14R 15L 16S 17S
gg1 9: 3L 5L 7L 9R? 10R? 11-15W? 16W? 17S
gg2 0: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 1: 2V 3G 4G 5-9G 11R 12L 13S 14S
gg2 2: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 3: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 4: 2V 3G 4G 5-9G 11R 12L 13S 14S
gg2 5: 2V 3G 4G 5-9G 11R 12L 13S 14S
gg2 6: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 7: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 8: 2V 3G 4G 5-9G 11R 13L 14S 15S
gg2 9: 2W 3V 4G 6R 8L 9S 10S
gg3 0: 2V 3V 4V 5V 6G 7G 8V 9G 10G? 11G 12-15G 16V 18R 20L 21W 22S
gg3 1: 2V 3W? 4V 5G 6-10G 12R 14L 15W 16S 17S
gg3 2: 2V 3W? 4V 5G 6-10G 12R 14L 15W 16S 17S
gg3 3: 2V 3W? 4G 5-9G 11R 13L 14W 15S 16S
gg3 4: 2V 3W? 4V 5G 6-10G 12R 14L 15W 16S 17S
gg3 5: 2V 3W? 4V 5V 6G 7-10G 12R 14L 15W 16S 17S
gg3 6: 2V 3W? 4V 5G 6-10G 12R 14L 15W 16S 17S
gg3 7: 2V 3W? 4V 5V 6G 7-11G 13R 15L 16W 17S 18S
gg3 8: 2V 3W? 4V 5G 6-10G 12R 14L 15W 16S 17S
gg3 9: 4L 6R 7W? 8V? 9G 10G? 11W 13S
sm0 0: 2R? 3R? 4R? 5R? 6L 7W? 8W? 9V 10V 11R 12R? 13S
sm0 1: 2R? 3W? 4W? 5R? 6V 7L 8S 9L 10S 11S
sm0 2: 2W? 3W? 4R 5R? 6R? 7R? 8R? 9R? 10V 11V 12S 13S
sm0 3: 2W? 3W? 4W? 5W? 6R? 7R? 8V 9L 10S 11S
sm0 4: 2W? 3W? 4W? 5W? 6R? 7R? 8R? 9V 10V? 11V 12L 13S 14S
sm0 5: 2W? 3W? 4W? 5W? 6R? 7R 8V 9V 10V 11V 12L 13L 14S 15S 16S
sm1 0: 2L? 3V 4V 5L 6G 7S
sm1 1: 1W 2S? 4L 6L 7V 8G 9-13G 14S
sm1 2: 1V 3L 5R 6G 7-11G 12W 13S? 14S
sm1 3: 1V 2W 3S? 4G 5-9G 10R 12L 13S
sm1 4: 1W 2V 3G 4-8G 9V 10V? 12R 13L 14S
sm1 5: 1W 2V 3G 4-8G 10R 12L 13S
sm1 6: 1W 2G 3-7G 8R 10L 11S
sm1 7: 1W 2V 3G 4G 5-9G 11L 13R 14S 15S
sm1 8: 1W 2V 3G 4-8G 10R 12L 13S
sm1 9: 1W 2V 3V? 4G? 5-9G 11L 13R 14S 15S
sm1 10: 2L 4L 6R 8R 9W? 10S 11S 12S
sm2 0: 2V 4G 6R 9L 10S
sm2 1: 3V 5G 7-11G 13R 16L 17S
sm2 2: 3V 5-9G 11-15G 17R 20L 21S
sm2 3: 2W? 3V 4G 6-10G 11R 13L 14S
sm2 4: 2W? 3V 4G 5-9G 11R 13L 14S 15S
sm2 5: 2W? 3V 4V? 5G 6-10G 11R 13L 14S
sm2 6: 2V 3V 4G 5-9G 11R 14L 15S
sm2 7: 2V 3V 4V? 5G 6-10G 12R 15L 16S 17S
sm2 8: 2V 3V 4V 5G 6-10G 12R 15L 16S
sm2 9: 2V 3G? 4G 5-9G 11R 13L 14S
sm2 10: 4L 5L 7W? 8V 9G 10V? 11-15G 17R 18S 19W
sm3 0: 2L 3V? 4G 5-8G 9G 11V 12R? 13R? 15R 17L 18W 19S
sm3 1: 1V 2-6G 7-11G 12S
sm3 2: 1V 2V 3-7G 8-12G 13S 14S
sm3 3: 1V 2V 3G 4G 5V? 6V? 7G 8-12G 13S
sm3 4: 1V 2-4G 5G? 6G 7G 8-12G 13S 14S
sm3 5: 1V 2-7G 8-12G 13S
sm3 6: 1V 2V 3-7G 8-12G 13S 14S
sm3 7: 1V 2-6G 7-11G 12S
sm3 8: 1V 2-6G 7-11G 12S
sm3 9: 1V 2V? 3V? 4-7G 8-12G 13S 14S
sm3 10: 4L 5L 7L 9V? 10R? 12R
$d$)),
lines as (
  select split_part(split_part(l, ':', 1), ' ', 1) as slug,
         split_part(split_part(l, ':', 1), ' ', 2)::int as unit,
         trim(split_part(l, ':', 2)) as rest
  from src, regexp_split_to_table(t, E'\n') l where l ~ '^[a-z0-9]+ [0-9]+:'),
toks as (
  select slug, unit, regexp_match(tok, '^([0-9]+)(?:-([0-9]+))?([GVSLRW])([?])?$') as m
  from lines, regexp_split_to_table(rest, '\s+') tok),
dec as (
  select slug, unit, n as block_no,
         case m[3] when 'G' then 'grammar' when 'V' then 'vocabulary' when 'S' then 'speaking'
                   when 'L' then 'listening' when 'R' then 'reading' else 'writing' end as skill,
         m[4] is not null as guess
  from toks, generate_series(m[1]::int, coalesce(m[2], m[1])::int) n),
blk as (
  select c.slug, u.sort_order as unit, l.title as test_title, b.sort_order + 1 as block_no, b.id, b.type,
         coalesce(b.payload->>'title', '') as title
  from classroom_courses c join classroom_units u on u.course_id = c.id
  join classroom_lessons l on l.unit_id = u.id join classroom_blocks b on b.lesson_id = l.id
  where l.kind = 'test' and c.slug in ('gg1','gg2','gg3','sm0','sm1','sm2','sm3'))
select b.slug, x.payload->>'skill' as skill, count(*)
from blk b join classroom_blocks x on x.id = b.id
where b.type not in ('text','video','flashcards','embed')
group by 1, 2 order by 1, 2;
