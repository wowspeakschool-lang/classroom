-- SM1 Unit 4 Test: удалить замороженную копию урока у ученика, который тест
-- ещё проходит и до блока 9 (аудирование) не дошёл. Решение Анны 10.11.2026
-- («25 удалить их копии», «27 оставить прежний» — сдавшему копию оставляем).
-- Копия обеих копий — classroom_backup_sm1_u4_snap_20261110.
delete from classroom_lesson_snapshots
where lesson_id = 'a2af7e4a-ddf0-41ec-a3b5-db9f918a29b2'
  and enrollment_id = '1946c95a-d1a7-484e-8756-2fab43c2f468';
