-- GG1 Unit 1 Test: аудирование было собрано как чтение (замечание Анны 05.11.2026).
-- Запись лежала отдельным блоком «Прочитай» перед заданием, поэтому платформа
-- показывала её как материал для чтения, а у самого задания звука не было.
-- Правило от 02.11.2026: запись — в самом задании. Картинка в задании уже есть
-- (payload.material), так что текстовый блок после переноса звука лишний.

do $$
declare L uuid := 'bb8d9c5c-f3c0-4551-9bfe-a7a1e029f83e';
begin
  select l.id into L from classroom_lessons l
    join classroom_units u on u.id = l.unit_id
    join classroom_courses c on c.id = u.course_id
   where c.slug = 'gg1' and u.sort_order = 1 and l.kind = 'test';

  create table if not exists classroom_backup_gg1_u1_listening_20261105 as
    select * from classroom_blocks where lesson_id = L;

  update classroom_blocks set payload = jsonb_set(payload, '{audio}',
         to_jsonb('https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg1/gg1_u1_test_b14.mp3'::text), true)
   where id = 'f2700e68-4d87-46a9-94ea-1245f4faedf9';

  delete from classroom_blocks where id = '66d05574-8d9e-42d8-9b1f-a7107d744534';

  update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = L;
  update classroom_blocks t set sort_order = z.rn - 1
    from (select id, row_number() over (order by sort_order) rn
            from classroom_blocks where lesson_id = L) z
   where t.id = z.id;
end $$;
