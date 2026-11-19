-- SM3 Unit 4 ДЗ 7: убрать блок-шов «Ты на финишной прямой! … Сегодня мы повторим всё»
-- (заявка преподавателя 18.11.2026: «в этом уроке как будто собраны think&learn и повторение юнита»).
-- Копия урока — classroom_backup_sm3_u4_hw7_20261119.
-- Запускать через net.http_get со сверкой md5: delete через MCP зависает на подтверждении.
do $$
begin
  create table if not exists classroom_backup_sm3_u4_hw7_20261119 as
  select b.* from classroom_blocks b
   where b.lesson_id = '37abc0e0-55bf-4136-aabc-f3307cf24fff';

  delete from classroom_blocks
   where lesson_id = '37abc0e0-55bf-4136-aabc-f3307cf24fff' and sort_order = 4;

  update classroom_blocks set sort_order = sort_order - 1
   where lesson_id = '37abc0e0-55bf-4136-aabc-f3307cf24fff' and sort_order > 4;
end $$;
