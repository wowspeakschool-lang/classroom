-- ============================================================
-- 032. Новый тип блока: sequence — «Расставь по порядку»
--
-- Правильный порядок = порядок элементов в payload.items.
-- Ученику список показывается перемешанным, ответ приходит как
-- {"позиция": исходный_индекс}: {"0":2, "1":0, "2":1}
--
-- Эта часть только разрешает тип и учитывает его при закрытии урока.
-- Подсчёт баллов добавим отдельно (см. запрос в конце файла).
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
      'sequence'
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
                    'gaps','truefalse','speaking','sequence');

  select count(distinct s.block_id) into v_submitted
    from public.classroom_submissions s
    join public.classroom_blocks b on b.id = s.block_id
   where s.enrollment_id = p_enrollment_id
     and b.lesson_id = p_lesson_id
     and b.type in ('quiz','exact_input','match','task','embed','order','sort',
                    'gaps','truefalse','speaking','sequence');

  return jsonb_build_object(
    'can_finish', v_submittable > 0 and v_submitted >= v_submittable,
    'submittable', v_submittable,
    'submitted', v_submitted
  );
end
$function$;

-- ---------- 3. Проверка ----------
select 'тип sequence разрешён' as проверка,
       case when pg_get_constraintdef(oid) like '%sequence%' then 'да' else 'НЕТ' end as значение
  from pg_constraint
 where conrelid = 'public.classroom_blocks'::regclass
   and conname  = 'classroom_blocks_type_check'
union all
select 'completion_check знает sequence',
       case when position('sequence' in pg_get_functiondef(oid)) > 0 then 'да' else 'НЕТ' end
  from pg_proc where proname = 'classroom__completion_check';

-- ============================================================
-- ДАЛЬШЕ НУЖНО ТЕЛО classroom_submit_block — пришли выдачу:
--
-- SELECT unnest(string_to_array(pg_get_functiondef(oid), E'\n')) AS строка
-- FROM pg_proc WHERE proname = 'classroom_submit_block';
--
-- По ней добавлю ветку подсчёта в 033. Вслепую переписывать
-- не буду: функцию уже пересобирали целиком в 028.
-- ============================================================
