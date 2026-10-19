-- ============================================================
-- 034. Новый тип блока: hotspot — «Точки на картинке»
--
-- payload: { title, image, mode:'label'|'find',
--            points:[{x,y,text}], extras:[текст, ...] }
-- Координаты в процентах. Правильная подпись к точке i — points[i].text.
-- Ответ приходит как {"0":"dog","1":"cat"}.
--
-- Ветка подсчёта вставляется в classroom_submit_block точечно,
-- как в 033: функция не переписывается.
--
-- Требует 033.
-- ============================================================

-- ---------- 1. Разрешить тип ----------
do $do$
declare v_name text;
begin
  select conname into v_name
    from pg_constraint
   where conrelid = 'public.classroom_blocks'::regclass
     and contype = 'c'
     and pg_get_constraintdef(oid) like '%(type = ANY%'
   limit 1;
  if v_name is not null then
    execute format('alter table public.classroom_blocks drop constraint %I', v_name);
  end if;
  alter table public.classroom_blocks
    add constraint classroom_blocks_type_check
    check (type = any (array[
      'text','video','quiz','exact_input','match','task','embed',
      'order','sort','flashcards','gaps','truefalse','speaking',
      'sequence','hotspot'
    ]));
end
$do$;

-- ---------- 2. Учитывать при закрытии урока ----------
CREATE OR REPLACE FUNCTION public.classroom__completion_check(
    p_enrollment_id uuid, p_lesson_id uuid)
RETURNS jsonb
LANGUAGE plpgsql
STABLE SECURITY DEFINER
SET search_path TO 'public'
AS $function$
declare
  v_submittable int;
  v_submitted   int;
begin
  select count(*) into v_submittable
    from public.classroom_blocks b
   where b.lesson_id = p_lesson_id
     and b.type in ('quiz','exact_input','match','task','embed','order','sort',
                    'gaps','truefalse','speaking','sequence','hotspot');

  select count(distinct s.block_id) into v_submitted
    from public.classroom_submissions s
    join public.classroom_blocks b on b.id = s.block_id
   where s.enrollment_id = p_enrollment_id
     and b.lesson_id = p_lesson_id
     and b.type in ('quiz','exact_input','match','task','embed','order','sort',
                    'gaps','truefalse','speaking','sequence','hotspot');

  return jsonb_build_object(
    'can_finish', v_submittable > 0 and v_submitted >= v_submittable,
    'submittable', v_submittable,
    'submitted', v_submitted
  );
end
$function$;

-- ---------- 3. Подсчёт баллов: вставка ветки ----------
do $do$
declare
  v_def    text;
  v_anchor text := '  elsif v_block.type = ''sort'' then';
  v_branch text;
  v_old    text := 'in (''quiz'',''exact_input'',''match'',''gaps'',''truefalse'',''sequence'')';
  v_new    text := 'in (''quiz'',''exact_input'',''match'',''gaps'',''truefalse'',''sequence'',''hotspot'')';
begin
  select pg_get_functiondef(oid) into v_def
    from pg_proc where proname = 'classroom_submit_block';
  if v_def is null then raise exception 'Функция classroom_submit_block не найдена'; end if;

  if position('''hotspot''' in v_def) > 0 then
    raise notice 'Ветка hotspot уже есть — ничего не меняю';
    return;
  end if;
  if position('''sequence''' in v_def) = 0 then
    raise exception 'Сначала нужна миграция 033';
  end if;
  if (length(v_def) - length(replace(v_def, v_anchor, ''))) / length(v_anchor) <> 1 then
    raise exception 'Якорь ветки sort найден не один раз — вставка отменена';
  end if;
  if (length(v_def) - length(replace(v_def, v_old, ''))) / length(v_old) <> 1 then
    raise exception 'Список типов для __results найден не один раз — вставка отменена';
  end if;

  v_branch :=
'  -- НОВОЕ: точки на картинке. Верная подпись к точке i — points[i].text
  elsif v_block.type = ''hotspot'' then
    declare
      v_np int; v_pi int := 0; v_want text; v_got text;
    begin
      v_np := coalesce(jsonb_array_length(v_block.payload->''points''), 0);
      v_total := 0; v_ok := 0;
      while v_pi < v_np loop
        v_total := v_total + 1;
        v_want := v_block.payload->''points''->v_pi->>''text'';
        v_got  := p_answers ->> v_pi::text;
        v_match := (v_got is not null and v_got <> ''''
                    and public.classroom__norm(v_got)
                        is not distinct from public.classroom__norm(v_want));
        if v_match then v_ok := v_ok + 1; end if;
        v_results := v_results || jsonb_build_object(v_pi::text, v_match);
        v_pi := v_pi + 1;
      end loop;
      v_score := case when v_total > 0 then round(v_ok * 100.0 / v_total) else null end;
    end;

';

  v_def := replace(v_def, v_anchor, v_branch || v_anchor);
  v_def := replace(v_def, v_old, v_new);
  execute v_def;
  raise notice 'Ветка hotspot вставлена';
end
$do$;

-- ---------- 4. Проверка ----------
select 'тип hotspot разрешён' as проверка,
       case when pg_get_constraintdef(oid) like '%hotspot%' then 'да' else 'НЕТ' end as значение
  from pg_constraint
 where conrelid = 'public.classroom_blocks'::regclass
   and conname  = 'classroom_blocks_type_check'
union all
select 'submit_block знает hotspot',
       case when position('''hotspot''' in pg_get_functiondef(oid)) > 0 then 'да' else 'НЕТ' end
  from pg_proc where proname = 'classroom_submit_block'
union all
select 'completion_check знает hotspot',
       case when position('hotspot' in pg_get_functiondef(oid)) > 0 then 'да' else 'НЕТ' end
  from pg_proc where proname = 'classroom__completion_check';
