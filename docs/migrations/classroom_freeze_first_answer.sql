-- classroom_freeze_first_answer — заморозка урока при ПЕРВОМ ОТВЕТЕ ученика, а не при
-- назначении (решение Анны 15.10.2026). Накатывать после classroom_student_card.
-- Накатана 15.10.2026.
--
-- Пока ученик не начал, правки методиста до него доходят: вычитка домашек идёт
-- параллельно с назначением. Начал отвечать — урок у него заморожен (classroom_submit_block
-- снимает копию при первом ответе, это уже так). Копии, снятые при назначении, у которых
-- нет ни одного ответа, удаляются — ответы и прогресс не трогаются.

-- ── Заморозка при первом ответе ────────────────────────────────────────────

-- назначение и запись на курс больше копию не снимают (триггеры остаются, но ничего не делают)
create or replace function public.classroom__snapshot_on_assign()
returns trigger language plpgsql security definer set search_path = public as $$
begin
  return new;   -- копия снимается при первом ответе (classroom_submit_block)
end $$;

-- прохождение: копия, если ученик уже начал; иначе — живые задания, копию НЕ снимаем
create or replace function public.classroom_run_blocks(p_enrollment_id uuid, p_lesson_id uuid)
returns jsonb language plpgsql stable security definer set search_path = public as $$
begin
  if not public.classroom__can_see_enrollment(p_enrollment_id) then
    raise exception 'Нет доступа к этой работе';
  end if;
  return coalesce(
    (select s.blocks from public.classroom_lesson_snapshots s
      where s.enrollment_id = p_enrollment_id and s.lesson_id = p_lesson_id),
    (select coalesce(jsonb_agg(to_jsonb(b) order by b.sort_order), '[]'::jsonb)
       from public.classroom_blocks b where b.lesson_id = p_lesson_id));
end $$;

-- копии без единого ответа — снять (их сняли при назначении, ученик ещё не начинал)
delete from public.classroom_lesson_snapshots s
 where not exists (select 1 from public.classroom_progress p
                    where p.enrollment_id = s.enrollment_id and p.lesson_id = s.lesson_id)
   and not exists (select 1 from public.classroom_submissions x
                    where x.enrollment_id = s.enrollment_id
                      and x.block_id in (select (e->>'id')::uuid from jsonb_array_elements(s.blocks) e));
