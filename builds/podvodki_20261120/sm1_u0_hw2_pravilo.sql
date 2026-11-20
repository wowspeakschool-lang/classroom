-- SM1 юнит 0 ДЗ 2: правило «How old are you?» уезжает в «Материал задания»
-- блоков 11 и 12 (где оно и работает), отдельный блок 3 удаляется.
-- Решение Анны 20.11.2026 («165 согласна»).
create table if not exists classroom_backup_sm1_u0hw2_pravilo_20261120 as
select * from classroom_blocks where lesson_id = '9ad9086c-a2c7-4af7-8a01-92119918e456';

update classroom_blocks set payload = jsonb_set(payload, '{material}',
  to_jsonb('<p><b>How old are you?</b> <i>Сколько тебе лет?</i><br><b>I''m seven.</b> <i>Мне семь лет.</i></p>'::text))
where id in ('a4e94fa0-664b-4f65-a943-76df799461dd', 'a33b1788-d992-44fb-a28a-8454daba0cd3');

delete from classroom_blocks where id = '981a80cc-51f7-49ec-9994-2d469c6a88ec';

do $$
declare u uuid := '9ad9086c-a2c7-4af7-8a01-92119918e456'; r record; i int := 0;
begin
  update classroom_blocks set sort_order = -1 - sort_order where lesson_id = u;
  for r in select id from classroom_blocks where lesson_id = u order by sort_order desc loop
    update classroom_blocks set sort_order = i where id = r.id; i := i + 1;
  end loop;
end $$;
