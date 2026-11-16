-- SM2: два блока «Соедини слово и перевод» — дубль задания «картинка ↔ слово»
-- в той же домашке на том же наборе слов (правило Анны от 22.10.2026).
--   Unit 0 ДЗ 1 блок 6 (10 слов класса)  — дубль блока 5
--   Unit 2 ДЗ 1 блок 6 (9 животных)      — дубль блока 5
-- Копия блоков: classroom_backup_sm2_perevod_20261111
-- Запуск: только через net.http_get с Pages (delete через MCP зависает).

delete from classroom_blocks
where id in ('74ccf606-611f-4448-b371-26218c5b5c2d',
             '45e479bd-893d-4f03-8843-83e0a866cc2c');

-- перенумерация обоих уроков без дырок
with les as (
  select l.id from classroom_courses c
  join classroom_units u on u.course_id = c.id
  join classroom_lessons l on l.unit_id = u.id
  where c.slug = 'sm2' and l.title = 'Homework 1' and u.sort_order in (0, 2))
update classroom_blocks b set sort_order = -1 - b.sort_order
where b.lesson_id in (select id from les);

with les as (
  select l.id from classroom_courses c
  join classroom_units u on u.course_id = c.id
  join classroom_lessons l on l.unit_id = u.id
  where c.slug = 'sm2' and l.title = 'Homework 1' and u.sort_order in (0, 2)),
nu as (
  select b.id, row_number() over (partition by b.lesson_id order by b.sort_order desc) - 1 as n
  from classroom_blocks b where b.lesson_id in (select id from les))
update classroom_blocks b set sort_order = nu.n from nu where nu.id = b.id;
