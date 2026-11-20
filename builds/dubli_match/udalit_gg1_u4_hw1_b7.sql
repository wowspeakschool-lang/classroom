-- GG1 юнит 4 ДЗ 1: третье задание на те же части лица (блок 7) удаляется.
-- Блок 5 остался «картинка ↔ слово», блок 6 стал «послушай и соедини».
-- Решение Анны 20.11.2026 («179 да»).
create table if not exists classroom_backup_gg1_u4hw1_dubl_20261120 as
select * from classroom_blocks where id = 'e8c2bea1-e4ac-465e-97a0-4e3a18d946ee';

delete from classroom_blocks where id = 'e8c2bea1-e4ac-465e-97a0-4e3a18d946ee';

do $$
declare u uuid := '11bfee5d-28bd-42b8-841d-139834270d2f'; r record; i int := 0;
begin
  update classroom_blocks set sort_order = -1 - sort_order where lesson_id = u;
  for r in select id from classroom_blocks where lesson_id = u order by sort_order desc loop
    update classroom_blocks set sort_order = i where id = r.id; i := i + 1;
  end loop;
end $$;
