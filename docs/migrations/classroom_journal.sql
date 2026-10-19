-- classroom_journal — журнал методиста (HANDOVER 8.4, макет docs/makety/zhurnal_v2.html)
-- и перевод старых устных заданий в «Запись голоса».
-- Накатывать после classroom_no_mic. Ничего не удаляет.

-- 1. Журнал: всё заданное ученикам (домашки и тесты) со статусом сдачи.
--    Только методист. Интерфейс сам сводит это в таблицу по юниту
--    или в сводку по ученикам («Все программы»).
create or replace function public.classroom_journal()
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare v_out jsonb;
begin
  if not public.classroom_is_editor() then raise exception 'Журнал — только для методиста'; end if;
  select coalesce(jsonb_agg(jsonb_build_object(
           'student_id', a.target_id, 'student', s.name,
           'teacher_id', t.id, 'teacher', t.name,
           'course_id', c.id, 'course_slug', c.slug, 'course_title', c.title,
           'unit_id', u.id, 'unit_no', u.sort_order, 'unit_title', u.title,
           'lesson_id', l.id, 'lesson_title', l.title, 'lesson_sort', l.sort_order, 'kind', l.kind,
           'enrollment_id', e.id,
           'assigned_at', a.assigned_at, 'deadline_at', a.deadline_at,
           'status', pr.status,
           'score', case when pr.status = 'reviewed' then pr.score end,
           'submitted_at', pr.submitted_at, 'reviewed_at', pr.reviewed_at,
           'first_submitted_at', case when pr.submitted_at is not null then public.classroom__first_submitted(pr) end,
           'retake_deadline_at', case when pr.status = 'retake' then pr.retake_deadline_at end,
           'progress', case when e.id is not null and pr.status in ('in_progress', 'retake')
                            then public.classroom__completion_check(e.id, l.id) end
         )), '[]'::jsonb)
    into v_out
    from public.classroom_assignments a
    join public.classroom_lessons l on l.id = a.lesson_id and coalesce(l.kind, 'homework') in ('homework', 'test')
    join public.classroom_units u on u.id = l.unit_id
    join public.classroom_courses c on c.id = u.course_id
    left join public.students s on s.id = a.target_id
    left join public.classroom_enrollments e on e.course_id = c.id and e.student_id = a.target_id
    left join public.classroom_progress pr on pr.enrollment_id = e.id and pr.lesson_id = l.id
    left join public.teachers t on t.id = coalesce(a.assigned_teacher_id, e.teacher_id)
   where a.target_type = 'student' and a.status = 'active';
  return v_out;
end $$;

-- 2. Старые устные задания («Открытый вопрос» с ответом голосом) → «Запись голоса».
--    У них появятся «не работает микрофон — написать текстом» и обычная проверка.
--    Звук задания (audio) остаётся и показывается кнопкой «Послушать».
--    Ученикам, которые уже начали такие домашки, ничего не меняется — у них копия.
update public.classroom_blocks
   set type = 'speaking', payload = payload - 'answer_kind'
 where type = 'task' and payload->>'answer_kind' = 'audio';
