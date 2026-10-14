-- ============================================================
-- 030. classroom__completion_check: + gaps, truefalse, speaking
--
-- Требует 028 и 029.
--
-- Было: урок считался пройденным, когда сданы блоки типов
--   quiz, exact_input, match, task, embed, order, sort
-- Три новых типа в список не входили — урок закрывался,
-- не дожидаясь ответов на них.
--
-- Сигнатура, права и STABLE не меняются.
-- ============================================================

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
                    'gaps','truefalse','speaking');

  select count(distinct s.block_id) into v_submitted
    from public.classroom_submissions s
    join public.classroom_blocks b on b.id = s.block_id
   where s.enrollment_id = p_enrollment_id
     and b.lesson_id = p_lesson_id
     and b.type in ('quiz','exact_input','match','task','embed','order','sort',
                    'gaps','truefalse','speaking');

  return jsonb_build_object(
    'can_finish', v_submittable > 0 and v_submitted >= v_submittable,
    'submittable', v_submittable,
    'submitted', v_submitted
  );
end
$function$;

-- ---------- Проверка ----------
select 'completion_check знает типы' as проверка,
       (select string_agg(t, ', ' order by t)
          from unnest(array['quiz','exact_input','match','task','embed','order',
                            'sort','gaps','truefalse','speaking']) t
         where position('''' || t || '''' in pg_get_functiondef(p.oid)) > 0) as значение
  from pg_proc p
 where p.proname = 'classroom__completion_check';
