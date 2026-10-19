-- Снести копии удалённой чужой «Homework 1» юнита 0 SM0.
-- Копии снимались 19.10.2026 перед удалением урока; сам урок удалён,
-- возвращать нечего — решение Анны от 19.10.
--
-- ЗАПУСКАТЬ В SUPABASE SQL EDITOR: drop через MCP до базы не доходит.

drop table if exists classroom_backup_sm0_u0_hw1_20261019_lesson;
drop table if exists classroom_backup_sm0_u0_hw1_20261019_blocks;
drop table if exists classroom_backup_sm0_u0_hw1_20261019_assign;
drop table if exists classroom_backup_sm0_u0_hw1_20261019_snap;

-- Проверка: запрос должен вернуть пусто.
select table_name from information_schema.tables
 where table_schema = 'public'
   and table_name like 'classroom_backup_sm0_u0_hw1_20261019%';
