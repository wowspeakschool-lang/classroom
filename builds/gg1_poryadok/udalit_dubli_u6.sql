-- GG1 юнит 6 ДЗ 1: удалить два дубля «соедини картинку и фразу» («159 да», 20.11.2026)
create table if not exists classroom_backup_gg1_u6_dubli_20261120 as
select * from classroom_blocks where lesson_id = 'fed6704a-de12-49a2-8797-63d8234ad561';

delete from classroom_blocks
 where id in ('7c588c08-20a1-4cc4-8b3f-d6d3da5038da','ad8ebbb4-23f5-4c56-919f-74b9673ac0d5');

do $$
declare r record; i int := 0;
begin
  update classroom_blocks set sort_order = -1 - sort_order
   where lesson_id = 'fed6704a-de12-49a2-8797-63d8234ad561';
  for r in select id from classroom_blocks
            where lesson_id = 'fed6704a-de12-49a2-8797-63d8234ad561'
            order by sort_order desc loop
    update classroom_blocks set sort_order = i where id = r.id;
    i := i + 1;
  end loop;
end $$;
