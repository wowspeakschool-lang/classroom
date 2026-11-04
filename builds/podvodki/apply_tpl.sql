-- Подводки внутрь задания (решение Анны 04.11.2026, «38 да»). Собирается builds/podvodki/build.py.
-- merge: блок-подводка убирается, у заданий новый заголовок; material: html блока → payload.material
-- заданий (первые абзацы-инструкции по-русски срезаются); dup: блок убирается (текст уже в material).
-- Копия всех блоков затронутых уроков — classroom_backup_podvodki_20261104.
do $do$
declare
  p jsonb := $plan$@@PLAN@@$plan$::jsonb;
  e jsonb; g jsonb; h text; mat text; orig text; m text[]; inner_ text; plain text; lat int; let int;
  n_del int := 0; n_mat int := 0; n_tit int := 0; n_skip int := 0; fid text; fh text;
begin
  create table classroom_backup_podvodki_20261104 as
    select * from classroom_blocks where lesson_id in (
      select lesson_id from classroom_blocks where id in (select (x->>'t')::uuid from jsonb_array_elements(p) x));
  alter table classroom_backup_podvodki_20261104 enable row level security;

  for e in select * from jsonb_array_elements(p) loop
    select payload->>'html' into h from classroom_blocks where id = (e->>'t')::uuid and type = 'text';
    -- блок уже снял другой чат (04.11.2026: «вторая часть» в SM1/SM3) — пропускаем вместе с заданиями
    if h is null then n_skip := n_skip + 1; continue; end if;

    if e->>'a' = 'material' then
      mat := coalesce(e->>'mh', h);
      if e->>'mh' is null and (e->>'s')::boolean then
        orig := mat;
        loop
          m := regexp_match(mat, '<p\y[^>]*>((?:(?!</p>).)*)</p>');
          exit when m is null;
          inner_ := m[1];
          plain := regexp_replace(inner_, '<[^>]+>', '', 'g');
          lat := length(regexp_replace(plain, '[^A-Za-z]', '', 'g'));
          let := length(regexp_replace(plain, '[^A-Za-zА-Яа-яЁё]', '', 'g'));
          exit when inner_ ~* '<img' or plain !~ '[А-Яа-яЁё]' or lat > 0.3 * let;
          mat := regexp_replace(mat, '<p\y[^>]*>(?:(?!</p>).)*</p>\s*', '');
        end loop;
        if regexp_replace(regexp_replace(mat, '<(?!img)[^>]+>', '', 'g'), '\s', '', 'g') = '' then mat := orig; end if;
      end if;
      if e ? 'mf' then
        for fid in select jsonb_array_elements_text(e->'mf') loop
          select payload->>'html' into fh from classroom_blocks where id = fid::uuid;
          if fh is null then raise exception 'нет блока для material_from_ids %', fid; end if;
          mat := fh || E'\n' || mat;
        end loop;
      end if;
      for g in select * from jsonb_array_elements(e->'g') loop
        update classroom_blocks set payload = payload || jsonb_build_object('material', mat)
         where id = (g->>'id')::uuid and not (payload ? 'material');
        if found then n_mat := n_mat + 1; end if;
      end loop;
    end if;

    for g in select * from jsonb_array_elements(e->'g') loop
      if coalesce(g->>'nt', '') <> '' then
        update classroom_blocks set payload = payload || jsonb_build_object('title', g->>'nt')
         where id = (g->>'id')::uuid and coalesce(payload->>'title', '') <> g->>'nt';
        if found then n_tit := n_tit + 1; end if;
      end if;
    end loop;

    delete from classroom_blocks where id = (e->>'t')::uuid;
    n_del := n_del + 1;
  end loop;

  -- сомкнуть нумерацию затронутых уроков (через сдвиг — из-за уникальности (lesson_id, sort_order))
  update classroom_blocks set sort_order = sort_order + 100000
   where lesson_id in (select distinct lesson_id from classroom_backup_podvodki_20261104);
  update classroom_blocks b set sort_order = r.rn - 1
    from (select id, row_number() over (partition by lesson_id order by sort_order) rn from classroom_blocks
           where lesson_id in (select distinct lesson_id from classroom_backup_podvodki_20261104)) r
   where b.id = r.id;

  raise notice 'убрано блоков %, material %, заголовков %, пропущено (уже сняты) %', n_del, n_mat, n_tit, n_skip;
end
$do$;
