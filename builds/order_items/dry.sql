-- «Составь предложение» — несколько предложений в одном блоке (payload.items),
-- решение методиста 04.11.2026. Без items всё как раньше.
--  * classroom_submit_block: пункт = предложение целиком; __results {"0": true, …};
--    балл = доля верно собранных предложений;
--  * classroom__block_complete: задание выполнено, когда собраны все предложения;
--  * classroom__mask_block: в тесте без ответов у каждого предложения слова
--    перемешаны и sentence убран.
-- Правка — вставкой перед прежней веткой 'order' в текущем тексте функций, чтобы
-- не перепечатывать их целиком. Проверка: прогнать с p_apply = false (ниже) —
-- откатный блок, сообщает, что нашлось.
do $mig$
declare
  p_apply boolean := false;
  d text; n int; rep text;
  f_sub text; f_cmp text; f_msk text;
begin
  -- 1. проверка ответа
  d := pg_get_functiondef('public.classroom_submit_block'::regproc);
  if position('jsonb_typeof(v_block.payload->''items'') = ''array''' in d) > 0 then raise exception 'уже применено'; end if;
  rep := $r$  elsif v_block.type = 'order' and jsonb_typeof(v_block.payload->'items') = 'array' then
    -- несколько предложений (items, 04.11.2026): пункт = предложение целиком
    declare v_it jsonb; v_n int; v_w int; v_all boolean;
    begin
      for v_it in select * from jsonb_array_elements(v_block.payload->'items') loop
        v_total := v_total + 1;
        v_n := coalesce(jsonb_array_length(v_it->'words'), 0);
        v_all := v_n > 0 and coalesce(jsonb_array_length(case when jsonb_typeof(p_answers->i::text->'order') = 'array'
                                                          then p_answers->i::text->'order' end), 0) = v_n;
        v_w := 0;
        while v_all and v_w < v_n loop
          if public.classroom__norm(p_answers->i::text->'order'->>v_w) is distinct from public.classroom__norm(v_it->'words'->>v_w)
          then v_all := false; end if;
          v_w := v_w + 1;
        end loop;
        if v_all then v_ok := v_ok + 1; end if;
        v_results := v_results || jsonb_build_object(i::text, v_all);
        i := i + 1;
      end loop;
    end;
    v_score := case when v_total > 0 then round(v_ok * 100.0 / v_total) else null end;

$r$;
  n := (select count(*) from regexp_matches(d, '\n  elsif v_block\.type = ''order'' then', 'g'));
  if n <> 1 then raise exception 'submit_block: ветка order найдена % раз', n; end if;
  f_sub := regexp_replace(d, '(\n)(  elsif v_block\.type = ''order'' then)', E'\\1' || replace(rep, '\', '\\') || E'\\2');
  n := (select count(*) from regexp_matches(f_sub, '\n  if v_block\.type = ''order'' then', 'g'));
  if n <> 1 then raise exception 'submit_block: блок вердиктов order найден % раз', n; end if;
  f_sub := regexp_replace(f_sub, '(\n  if v_block\.type = ''order'') then',
                          E'\\1 and jsonb_typeof(v_block.payload->''items'') is distinct from ''array'' then');

  -- 2. «задание выполнено»
  d := pg_get_functiondef('public.classroom__block_complete'::regproc);
  rep := $r$  elsif b.type = 'order' and jsonb_typeof(b.payload->'items') = 'array' then
    -- несколько предложений (items, 04.11.2026): собраны все
    v_i := 0;
    for v_q in select * from jsonb_array_elements(b.payload->'items') loop
      if coalesce(jsonb_array_length(case when jsonb_typeof(v_a->v_i::text->'order') = 'array'
                                          then v_a->v_i::text->'order' end), 0)
         <> coalesce(jsonb_array_length(v_q->'words'), 0) then
        return false;
      end if;
      v_i := v_i + 1;
    end loop;
    return true;

$r$;
  n := (select count(*) from regexp_matches(d, '\n  elsif b\.type = ''order'' then', 'g'));
  if n <> 1 then raise exception 'block_complete: ветка order найдена % раз', n; end if;
  f_cmp := regexp_replace(d, '(\n)(  elsif b\.type = ''order'' then)', E'\\1' || replace(rep, '\', '\\') || E'\\2');

  -- 3. тест без ответов
  d := pg_get_functiondef('public.classroom__mask_block'::regproc);
  rep := $r$  elsif t = 'order' and jsonb_typeof(p->'items') = 'array' then
    -- несколько предложений (items, 04.11.2026): у каждого слова перемешаны, sentence убран
    p := jsonb_set(p, '{items}', coalesce((
      select jsonb_agg((x - 'sentence') || jsonb_build_object('words', coalesce((
               select jsonb_agg(w order by md5(s || ':' || i || ':' || j))
                 from jsonb_array_elements(coalesce(x->'words', '[]'::jsonb)) with ordinality c(w, j)), '[]'::jsonb))
             order by i)
        from jsonb_array_elements(p->'items') with ordinality a(x, i)), '[]'::jsonb));
$r$;
  n := (select count(*) from regexp_matches(d, '\n  elsif t = ''order'' then', 'g'));
  if n <> 1 then raise exception 'mask_block: ветка order найдена % раз', n; end if;
  f_msk := regexp_replace(d, '(\n)(  elsif t = ''order'' then)', E'\\1' || replace(rep, '\', '\\') || E'\\2');

  execute f_sub; execute f_cmp; execute f_msk;


  -- проверка новых веток на выдуманном блоке
  declare r public.classroom_blocks; m jsonb;
  begin
    select * into r from public.classroom_blocks where type = 'order' limit 1;
    r.payload := '{"items":[{"words":["I","like","cats."],"sentence":"I like cats."},{"words":["Go","home."],"sentence":"Go home."}]}'::jsonb;
    if public.classroom__block_complete(r, '{"0":{"order":["I","like","cats."]}}'::jsonb) then raise exception 'complete: одно из двух — не должно быть выполнено'; end if;
    if not public.classroom__block_complete(r, '{"0":{"order":["cats.","I","like"]},"1":{"order":["Go","home."]}}'::jsonb) then raise exception 'complete: оба собраны — должно быть выполнено'; end if;
    r.payload := '{"words":["a","b"],"sentence":"a b"}'::jsonb;
    if not public.classroom__block_complete(r, '{"order":["b","a"]}'::jsonb) then raise exception 'complete: прежний блок сломался'; end if;
    m := public.classroom__mask_block(jsonb_build_object('id','x','type','order','payload','{"items":[{"words":["I","like","cats."],"sentence":"I like cats."}]}'::jsonb), 'seed');
    if m->'payload'->'items'->0 ? 'sentence' or jsonb_array_length(m->'payload'->'items'->0->'words') <> 3 then raise exception 'mask: %', m; end if;
  end;

  if not p_apply then
    raise exception 'ПРОВЕРКА (откат): все три функции собрались; длины % / % / %',
      length(f_sub), length(f_cmp), length(f_msk);
  end if;
end
$mig$;
