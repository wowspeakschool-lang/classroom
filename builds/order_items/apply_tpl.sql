-- Серии order → одно задание с items (решение методиста 04.11.2026). Собирается build.py.
-- Первый блок серии получает title + items (skill и material остаются его), остальные удаляются.
-- Копия всех блоков затронутых уроков — classroom_backup_order_series_20261104.
do $do$
declare
  p jsonb := $plan$@@PLAN@@$plan$::jsonb;
  e jsonb; n_ser int := 0; n_del int := 0; d text; k uuid; miss int;
begin
  create table classroom_backup_order_series_20261104 as
    select * from classroom_blocks where lesson_id in (
      select lesson_id from classroom_blocks where id in (select (x->>'k')::uuid from jsonb_array_elements(p) x));
  alter table classroom_backup_order_series_20261104 enable row level security;

  for e in select * from jsonb_array_elements(p) loop
    k := (e->>'k')::uuid;
    -- серия должна быть целой: первый и все остальные блоки на месте и типа order
    select count(*) into miss from (select (e->>'k') id union all select jsonb_array_elements_text(e->'d')) z
      where not exists (select 1 from classroom_blocks b where b.id = z.id::uuid and b.type = 'order' and not (b.payload ? 'items'));
    if miss > 0 then raise exception 'серия % изменилась с выгрузки (% блоков нет)', k, miss; end if;
    update classroom_blocks
       set payload = (payload - 'words' - 'sentence' - 'image' - 'audio' - 'audio_tts' - 'prompt')
                     || jsonb_build_object('title', e->>'t', 'items', e->'i')
     where id = k;
    for d in select jsonb_array_elements_text(e->'d') loop
      delete from classroom_blocks where id = d::uuid;
      n_del := n_del + 1;
    end loop;
    n_ser := n_ser + 1;
  end loop;

  update classroom_blocks set sort_order = sort_order + 100000
   where lesson_id in (select distinct lesson_id from classroom_backup_order_series_20261104);
  update classroom_blocks b set sort_order = r.rn - 1
    from (select id, row_number() over (partition by lesson_id order by sort_order) rn from classroom_blocks
           where lesson_id in (select distinct lesson_id from classroom_backup_order_series_20261104)) r
   where b.id = r.id;

  raise notice 'серий %, убрано блоков %', n_ser, n_del;
end
$do$;
