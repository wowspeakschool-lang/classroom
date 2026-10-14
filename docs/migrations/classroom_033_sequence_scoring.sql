-- ============================================================
-- 033. Подсчёт баллов для типа sequence
--
-- Функция classroom_submit_block не переписывается целиком:
-- миграция берёт её текущее определение из базы, вставляет одну
-- новую ветку перед веткой 'sort' и выполняет результат.
-- Все существующие ветки остаются ровно такими, как сейчас.
--
-- Если якорь не найден или найден дважды — миграция падает
-- и ничего не меняет.
--
-- Требует 032.
-- ============================================================

-- ---------- 1. Что сейчас ----------
select 'submit_block знает sequence' as проверка,
       case when position('''sequence''' in pg_get_functiondef(oid)) > 0
            then 'да — миграция уже применена' else 'нет' end as значение
  from pg_proc where proname = 'classroom_submit_block';

-- ---------- 2. Вставка ветки ----------
do $do$
declare
  v_def    text;
  v_anchor text := '  elsif v_block.type = ''sort'' then';
  v_branch text;
  v_old    text := 'in (''quiz'',''exact_input'',''match'',''gaps'',''truefalse'')';
  v_new    text := 'in (''quiz'',''exact_input'',''match'',''gaps'',''truefalse'',''sequence'')';
begin
  select pg_get_functiondef(oid) into v_def
    from pg_proc where proname = 'classroom_submit_block';
  if v_def is null then
    raise exception 'Функция classroom_submit_block не найдена';
  end if;

  if position('''sequence''' in v_def) > 0 then
    raise notice 'Ветка sequence уже есть — ничего не меняю';
    return;
  end if;

  -- Якорь должен встречаться ровно один раз
  if (length(v_def) - length(replace(v_def, v_anchor, ''))) / length(v_anchor) <> 1 then
    raise exception 'Якорь ветки sort найден не один раз — вставка отменена';
  end if;
  if (length(v_def) - length(replace(v_def, v_old, ''))) / length(v_old) <> 1 then
    raise exception 'Список типов для __results найден не один раз — вставка отменена';
  end if;

  -- Позиция k верна, если в ней лежит элемент с номером k.
  -- Ответ приходит как {"0":2,"1":0,...}: позиция -> исходный индекс.
  v_branch :=
'  -- НОВОЕ: расставь по порядку. Верный порядок = порядок items в payload.
  elsif v_block.type = ''sequence'' then
    declare
      v_n int; v_pos int := 0; v_val text;
    begin
      v_n := coalesce(jsonb_array_length(v_block.payload->''items''), 0);
      v_total := 0; v_ok := 0;
      while v_pos < v_n loop
        v_total := v_total + 1;
        v_val := p_answers ->> v_pos::text;
        v_match := (v_val is not null and v_val = v_pos::text);
        if v_match then v_ok := v_ok + 1; end if;
        v_results := v_results || jsonb_build_object(v_pos::text, v_match);
        v_pos := v_pos + 1;
      end loop;
      v_score := case when v_total > 0 then round(v_ok * 100.0 / v_total) else null end;
    end;

';

  v_def := replace(v_def, v_anchor, v_branch || v_anchor);
  v_def := replace(v_def, v_old, v_new);

  execute v_def;
  raise notice 'Ветка sequence вставлена';
end
$do$;

-- ---------- 3. Проверка ----------
select 'submit_block знает типы' as проверка,
       (select string_agg(t, ', ' order by t)
          from unnest(array['quiz','exact_input','match','order','sort',
                            'gaps','truefalse','speaking','sequence']) t
         where position('''' || t || '''' in pg_get_functiondef(p.oid)) > 0) as значение
  from pg_proc p where p.proname = 'classroom_submit_block'
union all
select 'разбор ответов пишется для sequence',
       case when pg_get_functiondef(oid) like '%''truefalse'',''sequence''%'
            then 'да' else 'НЕТ' end
  from pg_proc where proname = 'classroom_submit_block';
