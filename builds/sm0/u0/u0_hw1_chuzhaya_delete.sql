-- SM0 · юнит 0 · удалить чужую «Homework 1» (sort_order 1, 17 блоков)
--
-- Это дословная копия Homework 4 юнита 1 (буквы f/u, «I've got a dog!»,
-- «How many?»), попавшая в юнит 0. Решение Анны от 19.10: удалить.
-- На её место уже встала восстановленная ДЗ 1 (sort_order 0).
--
-- ЗАПУСКАТЬ В SUPABASE SQL EDITOR: delete через MCP до базы не доходит.
--
-- Копии на случай отката уже сняты 19.10 (таблицы с префиксом
-- classroom_backup_sm0_u0_hw1_20261019_): lesson, blocks, assign, snap.
--
-- Вместе с уроком пропадут:
--   17 блоков,
--   5 выдач ученикам (2 active со сроком 31.07.2026, 3 paused),
--   1 замороженная копия от 15.10.2026 (ученик открыл урок; сохранённых
--   ответов в classroom_progress по этому уроку нет).

begin;

delete from classroom_lesson_snapshots
 where lesson_id = '0dc3e405-1e22-4c8d-8dd3-8e2ba704da6a';

delete from classroom_assignments
 where lesson_id = '0dc3e405-1e22-4c8d-8dd3-8e2ba704da6a';

delete from classroom_blocks
 where lesson_id = '0dc3e405-1e22-4c8d-8dd3-8e2ba704da6a';

delete from classroom_lessons
 where id = '0dc3e405-1e22-4c8d-8dd3-8e2ba704da6a';

commit;

-- Проверка: в юните 0 курса sm0 должна остаться одна «Homework 1» (sort_order 0).
select l.sort_order, l.title, l.kind, l.is_published,
       (select count(*) from classroom_blocks b where b.lesson_id = l.id) as blocks
from classroom_courses c
join classroom_units u on u.course_id = c.id and u.sort_order = 0
join classroom_lessons l on l.unit_id = u.id
where c.slug = 'sm0'
order by l.sort_order;
