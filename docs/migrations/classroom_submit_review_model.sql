-- classroom_submit_review_model — механика сдачи и проверки (HANDOVER 8.1)
--
-- Было: submit_block сразу отдавал ученику процент и «верно/неверно»,
-- а когда сдано всё — сам закрывал урок средним автобаллом.
-- Стало:
--   ученик отвечает вслепую → «Завершить и отправить» (classroom_finish_lesson)
--   → учитель правит вердикты пунктов и оценки блоков (classroom_review_item,
--     classroom_review_block) → выставляет итог (classroom_review_finish)
--     или отдаёт на переделку весь урок / выбранные задания (classroom_retake).
-- Заданная домашка заморожена: при назначении урок копируется ученику
-- (classroom_lesson_snapshots), и правки методиста его не трогают — ни
-- содержимое, ни состав заданий. Проверка идёт по той же копии.
-- Редактор сохраняет урок по номеру задания, а не по месту (classroom_save_lesson),
-- и удаление задания больше не стирает ответы учеников.
-- Порога нет: оценку и переделку решает учитель. Попыток сколько угодно,
-- каждая отправка, проверка и переделка пишется в classroom_progress.history.
--
-- submit_block правится точечно (якоря в живом теле, как в 033/034),
-- остальные функции маленькие и переписаны целиком по живым телам 14.10.2026.


-- ── 0. Заданное не меняется ────────────────────────────────────────────────

-- Ответы и оценки ученика больше не удаляются вместе с заданием:
-- задание живёт в копии урока у ученика, даже если методист убрала его из урока.
alter table public.classroom_submissions drop constraint if exists classroom_submissions_block_id_fkey;
alter table public.classroom_grades      drop constraint if exists classroom_grades_block_id_fkey;

-- Копия урока, какой его задали ученику: строки classroom_blocks в jsonb.
create table if not exists public.classroom_lesson_snapshots (
  enrollment_id uuid not null references public.classroom_enrollments(id) on delete cascade,
  lesson_id     uuid not null references public.classroom_lessons(id) on delete cascade,
  blocks        jsonb not null,
  created_at    timestamptz not null default now(),
  primary key (enrollment_id, lesson_id)
);
alter table public.classroom_lesson_snapshots enable row level security;
do $$
begin
  if not exists (select 1 from pg_policies where tablename = 'classroom_lesson_snapshots'
                  and policyname = 'classroom_lesson_snapshots_read') then
    create policy classroom_lesson_snapshots_read on public.classroom_lesson_snapshots
      for select using (public.classroom__can_see_enrollment(enrollment_id));
  end if;
end $$;

-- Снять копию, если её ещё нет. Возвращает копию.
create or replace function public.classroom__ensure_snapshot(p_enrollment_id uuid, p_lesson_id uuid)
returns jsonb language plpgsql security definer set search_path = public as $$
declare v jsonb;
begin
  insert into public.classroom_lesson_snapshots (enrollment_id, lesson_id, blocks)
  select p_enrollment_id, p_lesson_id,
         coalesce(jsonb_agg(to_jsonb(b) order by b.sort_order), '[]'::jsonb)
    from public.classroom_blocks b where b.lesson_id = p_lesson_id
  on conflict (enrollment_id, lesson_id) do nothing;
  select blocks into v from public.classroom_lesson_snapshots
   where enrollment_id = p_enrollment_id and lesson_id = p_lesson_id;
  return v;
end $$;

-- Задания урока для этого ученика: из копии, если она есть, иначе живые.
create or replace function public.classroom__lesson_blocks(p_enrollment_id uuid, p_lesson_id uuid)
returns setof public.classroom_blocks language sql stable set search_path = public as $$
  select r.*
    from public.classroom_lesson_snapshots s
    cross join lateral jsonb_populate_recordset(null::public.classroom_blocks, s.blocks) r
   where s.enrollment_id = p_enrollment_id and s.lesson_id = p_lesson_id
  union all
  select b.*
    from public.classroom_blocks b
   where b.lesson_id = p_lesson_id
     and not exists (select 1 from public.classroom_lesson_snapshots s
                      where s.enrollment_id = p_enrollment_id and s.lesson_id = p_lesson_id);
$$;

-- Одно задание для этого ученика: из его копии, иначе живое. 0 или 1 строка.
create or replace function public.classroom__enr_block(p_enrollment_id uuid, p_block_id uuid)
returns setof public.classroom_blocks language sql stable set search_path = public as $$
  select r.*
    from public.classroom_lesson_snapshots s
    cross join lateral jsonb_populate_recordset(null::public.classroom_blocks, s.blocks) r
   where s.enrollment_id = p_enrollment_id and r.id = p_block_id
  union all
  select b.* from public.classroom_blocks b
   where b.id = p_block_id
     -- живое задание — только если урок ученику ещё не копировали:
     -- добавленное после назначения к нему не попадает
     and not exists (select 1 from public.classroom_lesson_snapshots s
                      where s.enrollment_id = p_enrollment_id and s.lesson_id = b.lesson_id)
  limit 1;
$$;

-- Копия снимается в момент, когда урок задан ученику (бегунок «Доступ» или
-- «Задать материал»), и когда у ученика появляется запись на курс.
create or replace function public.classroom__snapshot_on_assign()
returns trigger language plpgsql security definer set search_path = public as $$
begin
  if tg_table_name = 'classroom_assignments' then
    if new.status = 'active' and new.target_type = 'student' then
      perform public.classroom__ensure_snapshot(e.id, new.lesson_id)
         from public.classroom_enrollments e
         join public.classroom_units u on u.course_id = e.course_id
         join public.classroom_lessons l on l.unit_id = u.id and l.id = new.lesson_id
        where e.student_id = new.target_id;
    end if;
  else -- classroom_enrollments
    perform public.classroom__ensure_snapshot(new.id, a.lesson_id)
       from public.classroom_assignments a
       join public.classroom_lessons l on l.id = a.lesson_id
       join public.classroom_units u on u.id = l.unit_id and u.course_id = new.course_id
      where a.target_type = 'student' and a.target_id = new.student_id and a.status = 'active';
  end if;
  return new;
end $$;

do $$
begin
  if not exists (select 1 from pg_trigger where tgname = 'classroom_assignments_snapshot') then
    create trigger classroom_assignments_snapshot
      after insert or update of status on public.classroom_assignments
      for each row execute function public.classroom__snapshot_on_assign();
  end if;
  if not exists (select 1 from pg_trigger where tgname = 'classroom_enrollments_snapshot') then
    create trigger classroom_enrollments_snapshot
      after insert on public.classroom_enrollments
      for each row execute function public.classroom__snapshot_on_assign();
  end if;
end $$;

-- Уже заданные уроки: копия с нынешнего состояния.
select public.classroom__ensure_snapshot(e.id, a.lesson_id)
  from public.classroom_assignments a
  join public.classroom_lessons l on l.id = a.lesson_id
  join public.classroom_units u on u.id = l.unit_id
  join public.classroom_enrollments e on e.course_id = u.course_id and e.student_id = a.target_id
 where a.target_type = 'student' and a.status = 'active';

-- Прохождение: задания урока для ученика (из его копии; копия снимается при
-- первом открытии, если урок задан в обход бегунка, например группе).
create or replace function public.classroom_run_blocks(p_enrollment_id uuid, p_lesson_id uuid)
returns jsonb language plpgsql security definer set search_path = public as $$
begin
  if not public.classroom__can_see_enrollment(p_enrollment_id) then
    raise exception 'Нет доступа к этой работе';
  end if;
  return public.classroom__ensure_snapshot(p_enrollment_id, p_lesson_id);
end $$;

-- Сохранение урока в редакторе — по номеру задания, а не по месту.
-- p_blocks: [{id?, type, payload, audience, variant, format}] в нужном порядке.
-- Задание с id обновляется, без id — создаётся, пропавшее из списка — удаляется.
-- Возвращает id всех заданий по порядку (редактор запоминает id новых).
create or replace function public.classroom_save_lesson(p_lesson_id uuid, p_blocks jsonb)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_keep uuid[]; v_item jsonb; v_idx int := 0; v_id uuid; v_out uuid[] := '{}';
begin
  if not public.classroom_is_editor() then
    raise exception 'Сохранять уроки может только методист';
  end if;
  if jsonb_typeof(p_blocks) <> 'array' then raise exception 'p_blocks — не массив'; end if;

  select coalesce(array_agg((x->>'id')::uuid), '{}') into v_keep
    from jsonb_array_elements(p_blocks) x
   where x->>'id' is not null
     and exists (select 1 from public.classroom_blocks b
                  where b.id = (x->>'id')::uuid and b.lesson_id = p_lesson_id);

  delete from public.classroom_blocks
   where lesson_id = p_lesson_id and not (id = any (v_keep));

  -- освободить номера мест, чтобы переставлять без столкновений
  update public.classroom_blocks set sort_order = -1 - sort_order where lesson_id = p_lesson_id;

  for v_item in select * from jsonb_array_elements(p_blocks) loop
    -- id из урока и ещё не занятый (дубль задания в редакторе мог унести чужой id)
    v_id := case when (v_item->>'id')::uuid = any (v_keep)
                  and not ((v_item->>'id')::uuid = any (v_out))
                 then (v_item->>'id')::uuid end;
    if v_id is not null then
      update public.classroom_blocks
         set type = v_item->>'type', payload = coalesce(v_item->'payload', '{}'::jsonb),
             sort_order = v_idx,
             audience = coalesce(v_item->>'audience', 'shared'),
             variant  = coalesce(v_item->>'variant', 'any'),
             format   = coalesce(v_item->>'format', 'any')
       where id = v_id;
    else
      insert into public.classroom_blocks (lesson_id, type, payload, sort_order, audience, variant, format)
      values (p_lesson_id, v_item->>'type', coalesce(v_item->'payload', '{}'::jsonb), v_idx,
              coalesce(v_item->>'audience', 'shared'), coalesce(v_item->>'variant', 'any'),
              coalesce(v_item->>'format', 'any'))
      returning id into v_id;
    end if;
    v_out := v_out || v_id;
    v_idx := v_idx + 1;
  end loop;

  return to_jsonb(v_out);
end $$;

-- ── 1. Колонки ─────────────────────────────────────────────────────────────

alter table public.classroom_progress
  add column if not exists status        text not null default 'in_progress',
  add column if not exists submitted_at  timestamptz,
  add column if not exists reviewed_at   timestamptz,
  add column if not exists reviewed_by   uuid,
  add column if not exists auto_score    integer,
  add column if not exists teacher_score integer,
  add column if not exists teacher_note  text,
  add column if not exists retake_blocks uuid[],
  add column if not exists show_answers  boolean not null default false,
  add column if not exists history       jsonb not null default '[]'::jsonb;

do $$
begin
  if not exists (select 1 from pg_constraint where conname = 'classroom_progress_status_check') then
    alter table public.classroom_progress add constraint classroom_progress_status_check
      check (status in ('in_progress','submitted','reviewed','retake'));
  end if;
  if not exists (select 1 from pg_constraint where conname = 'classroom_progress_teacher_score_check') then
    alter table public.classroom_progress add constraint classroom_progress_teacher_score_check
      check (teacher_score between 0 and 100);
  end if;
end $$;

-- вердикты учителя поверх автоматических: {"2": true} — пункт 3 засчитан
alter table public.classroom_submissions
  add column if not exists overrides     jsonb not null default '{}'::jsonb,
  add column if not exists teacher_score integer;

do $$
begin
  if not exists (select 1 from pg_constraint where conname = 'classroom_submissions_teacher_score_check') then
    alter table public.classroom_submissions add constraint classroom_submissions_teacher_score_check
      check (teacher_score between 0 and 100);
  end if;
end $$;

-- уведомления: CHECK на kind не трогаем — «отправил» и «переделать» идут видом
-- 'info' с payload.event = 'submitted' / 'retake'. (drop constraint через MCP
-- зависает на подтверждении, а отдельный вид фронту не нужен.)

-- ── 2. Помощники ───────────────────────────────────────────────────────────

-- Блок, который ученик обязан сдать. Учительские блоки (audience='teacher') не в счёт.
create or replace function public.classroom__block_counts(b public.classroom_blocks)
returns boolean language sql stable as $$
  select b.type in ('quiz','exact_input','match','task','embed','order','sort',
                    'gaps','truefalse','speaking','sequence','hotspot')
     and coalesce(b.audience, 'shared') in ('shared','student');
$$;

-- Может ли текущий пользователь проверять эту работу (учитель ученика или методист).
create or replace function public.classroom__can_review(p_enrollment_id uuid)
returns boolean language sql stable security definer set search_path = public as $$
  select public.classroom__can_see_enrollment(p_enrollment_id)
     and (public.classroom_is_editor() or public.classroom__current_teacher_id() is not null);
$$;

-- Оценка блока в процентах с учётом учителя:
-- своя оценка учителя → вердикты пунктов (авто, поправленные учителем) →
-- оценки частей task → автобалл. null — оценить нечем (устное без оценки).
create or replace function public.classroom__block_score(
  p_block public.classroom_blocks, p_sub public.classroom_submissions)
returns integer language plpgsql stable set search_path = public as $$
declare
  v_res jsonb; v_ovr jsonb; v_k text; v_v jsonb; v_n int := 0; v_ok int := 0;
begin
  if p_sub.id is null then return null; end if;
  if p_sub.teacher_score is not null then return p_sub.teacher_score; end if;
  v_res := p_sub.answers -> '__results';
  if jsonb_typeof(v_res) = 'object' then
    v_ovr := coalesce(p_sub.overrides, '{}'::jsonb);
    for v_k, v_v in select * from jsonb_each(v_res) loop
      v_n := v_n + 1;
      if coalesce((v_ovr ->> v_k)::boolean, (v_v #>> '{}')::boolean, false) then
        v_ok := v_ok + 1;
      end if;
    end loop;
    if v_n > 0 then return round(v_ok * 100.0 / v_n); end if;
  end if;
  if p_block.type = 'task' then
    return (select round(avg(g.score * 100.0 / nullif(coalesce(g.max_score, 100), 0)))
              from public.classroom_grades g
             where g.enrollment_id = p_sub.enrollment_id and g.block_id = p_block.id);
  end if;
  return p_sub.auto_score;
end $$;

-- Процент за урок: среднее по оценённым блокам, которые ученик обязан сдать.
create or replace function public.classroom__lesson_auto_score(p_enrollment_id uuid, p_lesson_id uuid)
returns integer language sql stable set search_path = public as $$
  select round(avg(public.classroom__block_score(b, s)))::int
    from public.classroom__lesson_blocks(p_enrollment_id, p_lesson_id) b
    join public.classroom_submissions s
      on s.block_id = b.id and s.enrollment_id = p_enrollment_id and s.section_key is null
   where public.classroom__block_counts(b);
$$;

-- ── 3. Выполнено ли задание и можно ли отправлять ─────────────────────────
-- «Сдано» мало: интерфейс отправляет и пустой ответ (тест без отметок,
-- пропуски без слов). Задание выполнено, когда отвечен каждый его пункт.

create or replace function public.classroom__block_complete(
  b public.classroom_blocks, p_answers jsonb)
returns boolean language plpgsql stable set search_path = public as $$
declare
  v_a jsonb := coalesce(p_answers, '{}'::jsonb);
  v_n int; v_i int; v_q jsonb;
begin
  if p_answers is null then return false; end if;   -- ответа нет совсем

  if b.type = 'quiz' then
    v_i := 0;
    for v_q in select * from jsonb_array_elements(coalesce(b.payload->'questions', '[]'::jsonb)) loop
      if coalesce(v_q->>'type', '') <> 'text'
         and coalesce(jsonb_array_length(case when jsonb_typeof(v_a->v_i::text) = 'array'
                                              then v_a->v_i::text end), 0) = 0 then
        return false;
      end if;
      v_i := v_i + 1;
    end loop;
    return true;

  elsif b.type in ('exact_input', 'match', 'gaps', 'truefalse', 'sequence', 'hotspot') then
    v_n := case b.type
      when 'exact_input' then jsonb_array_length(coalesce(b.payload->'items', '[]'::jsonb))
      when 'match'       then jsonb_array_length(coalesce(b.payload->'pairs', '[]'::jsonb))
      when 'gaps'        then jsonb_array_length(public.classroom__gaps_accept(b.payload->>'text'))
      when 'truefalse'   then jsonb_array_length(coalesce(b.payload->'statements', '[]'::jsonb))
      when 'sequence'    then jsonb_array_length(coalesce(b.payload->'items', '[]'::jsonb))
      when 'hotspot'     then jsonb_array_length(coalesce(b.payload->'points', '[]'::jsonb))
    end;
    for v_i in 0 .. coalesce(v_n, 0) - 1 loop
      if not (v_a ? v_i::text) then return false; end if;
      -- в точках пустая строка = ребёнок промахнулся, это ответ (неверный);
      -- в остальных пустое поле = не ответил
      if b.type not in ('hotspot', 'truefalse', 'sequence')
         and btrim(coalesce(v_a->>v_i::text, '')) = '' then
        return false;
      end if;
    end loop;
    return true;

  elsif b.type = 'order' then
    return coalesce(jsonb_array_length(case when jsonb_typeof(v_a->'order') = 'array'
                                            then v_a->'order' end), 0)
         = coalesce(jsonb_array_length(b.payload->'words'), 0);

  elsif b.type = 'sort' then
    select coalesce(sum(jsonb_array_length(coalesce(g->'items', '[]'::jsonb))), 0) into v_n
      from jsonb_array_elements(coalesce(b.payload->'groups', '[]'::jsonb)) g;
    return (select count(*) from jsonb_object_keys(
              case when jsonb_typeof(v_a->'assign') = 'object' then v_a->'assign' else '{}'::jsonb end))
           >= v_n;

  elsif b.type = 'speaking' then
    return btrim(coalesce(v_a->>'audio', '')) <> '';

  elsif b.type = 'task' then
    return btrim(coalesce(v_a->>'text', '')) <> '' or btrim(coalesce(v_a->>'audio', '')) <> '';
  end if;

  return true;   -- embed: «пройдено по факту»
end $$;

-- completion_check: считает выполненные, а не просто сданные задания,
-- и называет невыполненные номерами как в редакторе (sort_order + 1).
-- Учительские блоки не в счёт (HANDOVER 8.5).
create or replace function public.classroom__completion_check(p_enrollment_id uuid, p_lesson_id uuid)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare
  v_submittable int; v_done int; v_left jsonb;
begin
  select count(*),
         count(*) filter (where public.classroom__block_complete(b, s.answers)),
         coalesce(jsonb_agg(jsonb_build_object('block_id', b.id, 'no', b.sort_order + 1)
                            order by b.sort_order)
                  filter (where not public.classroom__block_complete(b, s.answers)), '[]'::jsonb)
    into v_submittable, v_done, v_left
    from public.classroom__lesson_blocks(p_enrollment_id, p_lesson_id) b
    left join public.classroom_submissions s
      on s.block_id = b.id and s.enrollment_id = p_enrollment_id and s.section_key is null
   where public.classroom__block_counts(b);

  return jsonb_build_object(
    'can_finish', v_submittable > 0 and v_done >= v_submittable,
    'submittable', v_submittable,
    'submitted', v_done,
    'incomplete', v_left
  );
end $$;

-- ── 4. submit_block: точечная правка живого тела ───────────────────────────
--  а) отправленную домашку менять нельзя; на переделке — только отданные задания;
--  б) вердикты по пунктам у order (по словам) и sort (по карточкам);
--  в) не закрывать урок и не отдавать ученику процент и вердикты.

do $mig$
declare
  d text; a text; n int; p int;
begin
  d := pg_get_functiondef('public.classroom_submit_block(uuid,uuid,jsonb)'::regprocedure);
  if position('v_prog public.classroom_progress%rowtype' in d) > 0 then
    raise notice 'submit_block уже переделан — пропускаю';
    return;
  end if;

  -- а) задание берётся из копии урока у ученика
  a := '  select * into v_block from public.classroom_blocks where id = p_block_id;';
  n := (length(d) - length(replace(d, a, ''))) / length(a);
  if n <> 1 then raise exception 'submit_block: якорь выборки блока найден % раз', n; end if;
  d := replace(d, a, '  select * into v_block from public.classroom__enr_block(p_enrollment_id, p_block_id);');

  -- а) объявление
  a := 'v_lscore int; v_threshold int;';
  n := (length(d) - length(replace(d, a, ''))) / length(a);
  if n <> 1 then raise exception 'submit_block: якорь объявлений найден % раз', n; end if;
  d := replace(d, a, a || ' v_prog public.classroom_progress%rowtype; v_k int; v_gk int;');

  -- а) замок перед вычислением
  a := '  v_needs_review := public.classroom__block_needs_review(v_block);';
  n := (length(d) - length(replace(d, a, ''))) / length(a);
  if n <> 1 then raise exception 'submit_block: якорь needs_review найден % раз', n; end if;
  d := replace(d, a,
'  -- копия урока снимается при первом ответе, если её ещё нет
  perform public.classroom__ensure_snapshot(p_enrollment_id, v_lesson.id);

  -- домашку после отправки не меняют; на переделке — только отданные задания
  select * into v_prog from public.classroom_progress
   where enrollment_id = p_enrollment_id and lesson_id = v_lesson.id;
  if found then
    if v_prog.status in (''submitted'', ''reviewed'') then
      raise exception ''Домашка уже отправлена — ответы менять нельзя'';
    end if;
    if v_prog.status = ''retake'' and v_prog.retake_blocks is not null
       and not (p_block_id = any (v_prog.retake_blocks)) then
      raise exception ''Это задание учитель уже принял'';
    end if;
  end if;

' || a);

  -- б) вердикты order и sort — перед сохранением
  a := '  v_status := case when v_needs_review then ''pending'' else null end;';
  n := (length(d) - length(replace(d, a, ''))) / length(a);
  if n <> 1 then raise exception 'submit_block: якорь v_status найден % раз', n; end if;
  d := replace(d, a,
'  -- вердикты по пунктам, чтобы учитель мог их поправить
  if v_block.type = ''order'' then
    v_results := ''{}''::jsonb;
    for v_k in 0 .. coalesce(jsonb_array_length(v_block.payload->''words''), 0) - 1 loop
      v_results := v_results || jsonb_build_object(v_k::text,
        public.classroom__norm(p_answers->''order''->>v_k)
          is not distinct from public.classroom__norm(v_block.payload->''words''->>v_k));
    end loop;
  elsif v_block.type = ''sort'' then
    v_results := ''{}''::jsonb; v_gk := 0;
    for v_k in 0 .. coalesce(jsonb_array_length(v_block.payload->''groups''), 0) - 1 loop
      for i in 1 .. coalesce(jsonb_array_length(v_block.payload->''groups''->v_k->''items''), 0) loop
        v_results := v_results || jsonb_build_object(v_gk::text,
          coalesce(p_answers->''assign''->>(v_gk::text) = v_k::text, false));
        v_gk := v_gk + 1;
      end loop;
    end loop;
  end if;

' || a);

  a := 'if v_block.type in (''quiz'',''exact_input'',''match'',''gaps'',''truefalse'',''sequence'',''hotspot'') then';
  n := (length(d) - length(replace(d, a, ''))) / length(a);
  if n <> 1 then raise exception 'submit_block: якорь __results найден % раз', n; end if;
  d := replace(d, a,
    'if v_block.type in (''quiz'',''exact_input'',''match'',''gaps'',''truefalse'',''sequence'',''hotspot'',''order'',''sort'') then');

  -- в) хвост: от completion_check до конца функции
  a := '  v_check := public.classroom__completion_check(p_enrollment_id, v_lesson.id);';
  n := (length(d) - length(replace(d, a, ''))) / length(a);
  if n <> 1 then raise exception 'submit_block: якорь хвоста найден % раз', n; end if;
  p := position(a in d);
  d := substr(d, 1, p - 1) ||
'  -- урок сам не закрывается: его отправляет ученик (classroom_finish_lesson)
  insert into public.classroom_progress (enrollment_id, lesson_id, started_at, status)
  values (p_enrollment_id, v_lesson.id, now(), ''in_progress'')
  on conflict (enrollment_id, lesson_id) do nothing;

  -- ученик отвечает вслепую: ни процента, ни вердиктов
  v_check := public.classroom__completion_check(p_enrollment_id, v_lesson.id);
  return jsonb_build_object(
    ''ok'', true,
    ''needs_review'', v_needs_review,
    ''submittable'', v_check->''submittable'',
    ''submitted'', v_check->''submitted'',
    ''can_finish'', v_check->''can_finish'',
    ''incomplete'', v_check->''incomplete''
  );
end
$function$
';
  execute d;
end $mig$;

-- ── 5. submit_embed: те же правила (embed сейчас только в плане урока) ──────

create or replace function public.classroom_submit_embed(
  p_block_id uuid, p_enrollment_id uuid, p_score integer default null, p_payload jsonb default '{}'::jsonb)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_block     public.classroom_blocks%rowtype;
  v_lesson    public.classroom_lessons%rowtype;
  v_enroll    public.classroom_enrollments%rowtype;
  v_prog      public.classroom_progress%rowtype;
  v_course_id uuid;
  v_needs_review boolean; v_status text; v_store jsonb;
begin
  select * into v_block from public.classroom__enr_block(p_enrollment_id, p_block_id);
  if not found then raise exception 'Блок не найден'; end if;
  if v_block.type <> 'embed' then raise exception 'Блок не типа embed'; end if;
  select * into v_lesson from public.classroom_lessons where id = v_block.lesson_id;
  select * into v_enroll from public.classroom_enrollments where id = p_enrollment_id;
  if not found then raise exception 'Запись (enrollment) не найдена'; end if;
  if not public.classroom__can_see_enrollment(p_enrollment_id) then
    raise exception 'Нет доступа к этой работе';
  end if;
  select c.id into v_course_id
    from public.classroom_units u
    join public.classroom_courses c on c.id = u.course_id
   where u.id = v_lesson.unit_id;
  if v_course_id is distinct from v_enroll.course_id then
    raise exception 'Блок не относится к курсу этой записи';
  end if;
  if p_score is not null and (p_score < 0 or p_score > 100) then
    raise exception 'score должен быть 0..100';
  end if;

  select * into v_prog from public.classroom_progress
   where enrollment_id = p_enrollment_id and lesson_id = v_lesson.id;
  if found then
    if v_prog.status in ('submitted', 'reviewed') then
      raise exception 'Домашка уже отправлена — ответы менять нельзя';
    end if;
    if v_prog.status = 'retake' and v_prog.retake_blocks is not null
       and not (p_block_id = any (v_prog.retake_blocks)) then
      raise exception 'Это задание учитель уже принял';
    end if;
  end if;

  v_needs_review := public.classroom__block_needs_review(v_block);
  v_status := case when v_needs_review then 'pending' else null end;
  v_store := coalesce(p_payload, '{}'::jsonb) || jsonb_build_object('__embed', true);

  insert into public.classroom_submissions
    (enrollment_id, block_id, section_key, answers, auto_score, review_status, submitted_at)
  values (p_enrollment_id, p_block_id, null, v_store, p_score, v_status, now())
  on conflict (enrollment_id, block_id, (coalesce(section_key, ''))) do update
    set answers = excluded.answers, auto_score = excluded.auto_score,
        review_status = excluded.review_status, reviewer_note = null,
        reviewed_at = null, submitted_at = now(),
        overrides = '{}'::jsonb, teacher_score = null;

  insert into public.classroom_progress (enrollment_id, lesson_id, started_at, status)
  values (p_enrollment_id, v_lesson.id, now(), 'in_progress')
  on conflict (enrollment_id, lesson_id) do nothing;

  return jsonb_build_object('ok', true, 'needs_review', v_needs_review);
end $$;

-- ── 6. Ученик: «Завершить и отправить» ─────────────────────────────────────

create or replace function public.classroom_finish_lesson(p_enrollment_id uuid, p_lesson_id uuid)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_check jsonb; v_prog public.classroom_progress%rowtype;
  v_auto int; v_student uuid; v_teacher uuid; v_title text;
begin
  if not public.classroom__can_see_enrollment(p_enrollment_id) then
    raise exception 'Нет доступа к этой работе';
  end if;

  v_check := public.classroom__completion_check(p_enrollment_id, p_lesson_id);
  if not coalesce((v_check->>'can_finish')::boolean, false) then
    raise exception 'Выполнены не все задания. Осталось: %',
      (select string_agg(x->>'no', ', ') from jsonb_array_elements(v_check->'incomplete') x);
  end if;

  select * into v_prog from public.classroom_progress
   where enrollment_id = p_enrollment_id and lesson_id = p_lesson_id for update;
  if found and v_prog.status in ('submitted', 'reviewed') then
    raise exception 'Домашка уже отправлена';
  end if;

  v_auto := public.classroom__lesson_auto_score(p_enrollment_id, p_lesson_id);

  insert into public.classroom_progress
    (enrollment_id, lesson_id, started_at, status, submitted_at, auto_score, history)
  values (p_enrollment_id, p_lesson_id, now(), 'submitted', now(), v_auto,
          jsonb_build_array(jsonb_build_object('event', 'submitted', 'at', now(), 'auto_score', v_auto)))
  on conflict (enrollment_id, lesson_id) do update
    set status = 'submitted', submitted_at = now(), auto_score = v_auto,
        retake_blocks = null,
        history = public.classroom_progress.history
                  || jsonb_build_object('event', 'submitted', 'at', now(), 'auto_score', v_auto);

  -- уведомление учителю: кто задал этот урок, иначе учитель записи
  select e.student_id, e.teacher_id into v_student, v_teacher
    from public.classroom_enrollments e where e.id = p_enrollment_id;
  v_teacher := coalesce((
    select a.assigned_teacher_id from public.classroom_assignments a
     where a.lesson_id = p_lesson_id and a.target_type = 'student' and a.target_id = v_student
       and a.assigned_teacher_id is not null
     order by a.assigned_at desc limit 1), v_teacher);
  select title into v_title from public.classroom_lessons where id = p_lesson_id;
  if v_teacher is not null then
    insert into public.classroom_notifications (recipient_kind, recipient_id, kind, title, payload)
    values ('teacher', v_teacher, 'info', 'Домашка отправлена: ' || coalesce(v_title, ''),
            jsonb_build_object('event', 'submitted', 'lesson_id', p_lesson_id, 'enrollment_id', p_enrollment_id,
                               'student_id', v_student));
  end if;

  -- ученику — только факт отправки
  return jsonb_build_object('ok', true, 'status', 'submitted');
end $$;

-- ── 7. Учитель: вердикт пункта и оценка блока ───────────────────────────────

-- p_verdict = null снимает поправку — пункт снова считается автоматически
create or replace function public.classroom_review_item(
  p_enrollment_id uuid, p_block_id uuid, p_item text, p_verdict boolean)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_block public.classroom_blocks%rowtype; v_sub public.classroom_submissions%rowtype;
  v_status text;
begin
  if not public.classroom__can_review(p_enrollment_id) then
    raise exception 'Проверять может только учитель ученика или методист';
  end if;
  select * into v_block from public.classroom__enr_block(p_enrollment_id, p_block_id);
  if not found then raise exception 'Блок не найден'; end if;
  select status into v_status from public.classroom_progress
   where enrollment_id = p_enrollment_id and lesson_id = v_block.lesson_id;
  if v_status is distinct from 'submitted' and v_status is distinct from 'reviewed' then
    raise exception 'Домашка ещё не отправлена';
  end if;

  update public.classroom_submissions
     set overrides = case when p_verdict is null then overrides - p_item
                          else overrides || jsonb_build_object(p_item, p_verdict) end
   where enrollment_id = p_enrollment_id and block_id = p_block_id and section_key is null
   returning * into v_sub;
  if not found then raise exception 'Ответ на это задание не найден'; end if;
  if not (v_sub.answers->'__results' ? p_item) then
    raise exception 'В задании нет пункта %', p_item;
  end if;

  return jsonb_build_object('ok', true,
    'block_score', public.classroom__block_score(v_block, v_sub),
    'lesson_score', public.classroom__lesson_auto_score(p_enrollment_id, v_block.lesson_id));
end $$;

-- p_score = null снимает оценку учителя — блок снова считается по пунктам
create or replace function public.classroom_review_block(
  p_enrollment_id uuid, p_block_id uuid, p_score integer, p_comment text default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_block public.classroom_blocks%rowtype; v_sub public.classroom_submissions%rowtype;
  v_status text;
begin
  if not public.classroom__can_review(p_enrollment_id) then
    raise exception 'Проверять может только учитель ученика или методист';
  end if;
  if p_score is not null and (p_score < 0 or p_score > 100) then
    raise exception 'Оценка — от 0 до 100';
  end if;
  select * into v_block from public.classroom__enr_block(p_enrollment_id, p_block_id);
  if not found then raise exception 'Блок не найден'; end if;
  select status into v_status from public.classroom_progress
   where enrollment_id = p_enrollment_id and lesson_id = v_block.lesson_id;
  if v_status is distinct from 'submitted' and v_status is distinct from 'reviewed' then
    raise exception 'Домашка ещё не отправлена';
  end if;

  update public.classroom_submissions
     set teacher_score = p_score, reviewer_note = p_comment,
         review_status = null, reviewed_at = now()
   where enrollment_id = p_enrollment_id and block_id = p_block_id and section_key is null
   returning * into v_sub;
  if not found then raise exception 'Ответ на это задание не найден'; end if;

  return jsonb_build_object('ok', true,
    'block_score', public.classroom__block_score(v_block, v_sub),
    'lesson_score', public.classroom__lesson_auto_score(p_enrollment_id, v_block.lesson_id));
end $$;

-- ── 8. Учитель: итог ───────────────────────────────────────────────────────

-- p_score = null — итог равен посчитанному проценту
create or replace function public.classroom_review_finish(
  p_enrollment_id uuid, p_lesson_id uuid, p_score integer default null,
  p_show_answers boolean default false, p_note text default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_prog public.classroom_progress%rowtype; v_auto int; v_final int;
  v_student uuid; v_title text;
begin
  if not public.classroom__can_review(p_enrollment_id) then
    raise exception 'Проверять может только учитель ученика или методист';
  end if;
  if p_score is not null and (p_score < 0 or p_score > 100) then
    raise exception 'Оценка — от 0 до 100';
  end if;
  select * into v_prog from public.classroom_progress
   where enrollment_id = p_enrollment_id and lesson_id = p_lesson_id for update;
  if not found or v_prog.status not in ('submitted', 'reviewed') then
    raise exception 'Домашка ещё не отправлена';
  end if;

  v_auto  := public.classroom__lesson_auto_score(p_enrollment_id, p_lesson_id);
  v_final := coalesce(p_score, v_auto);

  update public.classroom_progress
     set status = 'reviewed', reviewed_at = now(), reviewed_by = public.classroom__my_user_id(),
         auto_score = v_auto, teacher_score = p_score, score = v_final,
         teacher_note = p_note, show_answers = coalesce(p_show_answers, false),
         completed_at = coalesce(completed_at, now()),
         history = history || jsonb_build_object('event', 'reviewed', 'at', now(),
                     'auto_score', v_auto, 'teacher_score', p_score, 'score', v_final)
   where id = v_prog.id;

  update public.classroom_submissions s
     set review_status = null, reviewed_at = coalesce(s.reviewed_at, now())
   where s.enrollment_id = p_enrollment_id
     and s.block_id in (select b.id from public.classroom__lesson_blocks(p_enrollment_id, p_lesson_id) b);

  select student_id into v_student from public.classroom_enrollments where id = p_enrollment_id;
  select title into v_title from public.classroom_lessons where id = p_lesson_id;
  if v_student is not null then
    insert into public.classroom_notifications (recipient_kind, recipient_id, kind, title, payload)
    values ('student', v_student, 'reviewed', 'Домашка проверена: ' || coalesce(v_title, ''),
            jsonb_build_object('event', 'reviewed', 'lesson_id', p_lesson_id, 'enrollment_id', p_enrollment_id,
                               'score', v_final));
  end if;

  return jsonb_build_object('ok', true, 'score', v_final, 'auto_score', v_auto);
end $$;

-- ── 9. Учитель: задать заново ──────────────────────────────────────────────

-- p_blocks пустой или null — весь урок. Старые ответы уходят в history.
create or replace function public.classroom_retake(
  p_enrollment_id uuid, p_lesson_id uuid, p_blocks uuid[] default null, p_note text default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_prog public.classroom_progress%rowtype; v_all boolean; v_blocks uuid[];
  v_old jsonb; v_student uuid; v_title text;
begin
  if not public.classroom__can_review(p_enrollment_id) then
    raise exception 'Проверять может только учитель ученика или методист';
  end if;
  select * into v_prog from public.classroom_progress
   where enrollment_id = p_enrollment_id and lesson_id = p_lesson_id for update;
  if not found or v_prog.status not in ('submitted', 'reviewed') then
    raise exception 'Домашка ещё не отправлена';
  end if;

  v_all := coalesce(cardinality(p_blocks), 0) = 0;
  select coalesce(array_agg(b.id order by b.sort_order), '{}') into v_blocks
    from public.classroom__lesson_blocks(p_enrollment_id, p_lesson_id) b
   where public.classroom__block_counts(b)
     and (v_all or b.id = any (p_blocks));
  if not v_all and cardinality(v_blocks) <> cardinality(p_blocks) then
    raise exception 'Часть выбранных заданий не из этого урока';
  end if;

  select coalesce(jsonb_agg(jsonb_build_object(
           'block_id', s.block_id, 'section_key', s.section_key, 'answers', s.answers,
           'auto_score', s.auto_score, 'overrides', s.overrides, 'teacher_score', s.teacher_score,
           'reviewer_note', s.reviewer_note, 'storage_path', s.storage_path,
           'submitted_at', s.submitted_at)), '[]'::jsonb)
    into v_old
    from public.classroom_submissions s
   where s.enrollment_id = p_enrollment_id and s.block_id = any (v_blocks);

  delete from public.classroom_grades
   where enrollment_id = p_enrollment_id and block_id = any (v_blocks);
  delete from public.classroom_submissions
   where enrollment_id = p_enrollment_id and block_id = any (v_blocks);

  update public.classroom_progress
     set status = 'retake', retake_blocks = case when v_all then null else v_blocks end,
         teacher_note = p_note, score = null, teacher_score = null,
         completed_at = null, show_answers = false,
         history = history || jsonb_build_object('event', 'retake', 'at', now(),
                     'blocks', to_jsonb(v_blocks), 'whole', v_all, 'note', p_note,
                     'score', v_prog.score, 'auto_score', v_prog.auto_score,
                     'submissions', v_old)
   where id = v_prog.id;

  select student_id into v_student from public.classroom_enrollments where id = p_enrollment_id;
  select title into v_title from public.classroom_lessons where id = p_lesson_id;
  if v_student is not null then
    insert into public.classroom_notifications (recipient_kind, recipient_id, kind, title, body, payload)
    values ('student', v_student, 'info', 'Нужно переделать: ' || coalesce(v_title, ''), p_note,
            jsonb_build_object('event', 'retake', 'lesson_id', p_lesson_id, 'enrollment_id', p_enrollment_id,
                               'blocks', to_jsonb(v_blocks)));
  end if;

  return jsonb_build_object('ok', true, 'whole', v_all, 'blocks', to_jsonb(v_blocks));
end $$;

-- ── 10. Сводка домашки: все 15 типов, учитель видит всё, ученик — по правилам ──
-- Ученик до проверки видит только статус. После проверки — оценку и свои ответы;
-- вердикты и верные ответы — только если учитель включил «Показать верные ответы».

create or replace function public.classroom_lesson_grade(p_enrollment_id uuid, p_lesson_id uuid)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare
  v_prog public.classroom_progress%rowtype; v_teacher boolean; v_open boolean;
  v_blocks jsonb; v_check jsonb;
begin
  if not public.classroom__can_see_enrollment(p_enrollment_id) then
    raise exception 'Нет доступа к этой работе';
  end if;
  v_teacher := public.classroom__can_review(p_enrollment_id);
  select * into v_prog from public.classroom_progress
   where enrollment_id = p_enrollment_id and lesson_id = p_lesson_id;
  v_check := public.classroom__completion_check(p_enrollment_id, p_lesson_id);

  if not v_teacher and coalesce(v_prog.status, 'in_progress') <> 'reviewed' then
    return jsonb_build_object(
      'status', coalesce(v_prog.status, 'in_progress'),
      'submitted_at', v_prog.submitted_at,
      'retake_blocks', to_jsonb(v_prog.retake_blocks),
      'teacher_note', case when v_prog.status = 'retake' then v_prog.teacher_note end,
      'submittable', v_check->'submittable', 'submitted', v_check->'submitted',
      'can_finish', v_check->'can_finish', 'incomplete', v_check->'incomplete');
  end if;

  v_open := v_teacher or coalesce(v_prog.show_answers, false);

  select coalesce(jsonb_agg(jsonb_build_object(
           'block_id', b.id, 'type', b.type, 'sort_order', b.sort_order,
           'title', coalesce(b.payload->>'title', ''),
           'needs_review', public.classroom__block_needs_review(b),
           'submitted', s.id is not null,
           'answers', case when s.id is null then null else s.answers - '__results' end,
           'storage_path', s.storage_path,
           'results', case when v_open then s.answers->'__results' end,
           'overrides', case when v_open then s.overrides end,
           'auto_score', case when v_teacher then s.auto_score end,
           'teacher_score', case when v_teacher then s.teacher_score end,
           'score', case when v_open then public.classroom__block_score(b, s) end,
           'comment', s.reviewer_note,
           'review_pending', s.review_status = 'pending',
           'parts', case when v_teacher and b.type = 'task' then (
              select jsonb_agg(jsonb_build_object('section_key', g.section_key, 'score', g.score,
                                                  'max_score', g.max_score, 'comment', g.comment))
                from public.classroom_grades g
               where g.enrollment_id = p_enrollment_id and g.block_id = b.id) end
         ) order by b.sort_order), '[]'::jsonb)
    into v_blocks
    from public.classroom__lesson_blocks(p_enrollment_id, p_lesson_id) b
    left join public.classroom_submissions s
      on s.block_id = b.id and s.enrollment_id = p_enrollment_id and s.section_key is null
   where public.classroom__block_counts(b);

  return jsonb_build_object(
    'status', coalesce(v_prog.status, 'in_progress'),
    'submitted_at', v_prog.submitted_at,
    'reviewed_at', v_prog.reviewed_at,
    'score', v_prog.score,
    'auto_score', case when v_teacher
                       then public.classroom__lesson_auto_score(p_enrollment_id, p_lesson_id) end,
    'teacher_score', case when v_teacher then v_prog.teacher_score end,
    'teacher_note', v_prog.teacher_note,
    'show_answers', coalesce(v_prog.show_answers, false),
    'retake_blocks', to_jsonb(v_prog.retake_blocks),
    'history', case when v_teacher then v_prog.history end,
    'submittable', v_check->'submittable', 'submitted', v_check->'submitted',
    'can_finish', v_check->'can_finish', 'incomplete', v_check->'incomplete',
    'blocks', v_blocks);
end $$;

-- ── 11. Очередь проверки: отправленные домашки целиком, а не блоки task ─────

create or replace function public.classroom_pending_reviews()
returns jsonb language sql stable security definer set search_path = public as $$
  select coalesce(jsonb_agg(jsonb_build_object(
           'enrollment_id', p.enrollment_id, 'student_id', e.student_id,
           'lesson_id', p.lesson_id, 'lesson_title', l.title, 'unit_title', u.title,
           'submitted_at', p.submitted_at, 'auto_score', p.auto_score,
           'attempt', (select count(*) from jsonb_array_elements(p.history) h
                        where h->>'event' = 'submitted')
         ) order by p.submitted_at), '[]'::jsonb)
    from public.classroom_progress p
    join public.classroom_enrollments e on e.id = p.enrollment_id
    join public.classroom_lessons l on l.id = p.lesson_id
    join public.classroom_units u on u.id = l.unit_id
   where p.status = 'submitted'
     and (public.classroom_is_editor()
          or (public.classroom__current_teacher_id() is not null
              and public.classroom__can_see_student(e.student_id)));
$$;

-- ── 12. Карточка ученика: статус домашки ───────────────────────────────────

create or replace function public.classroom_student_lessons(p_student_id uuid, p_course_id uuid)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare
  v_enroll uuid; v_out jsonb; v_teacher boolean;
begin
  if not (public.classroom_is_editor() or public.classroom__can_see_student(p_student_id)) then
    raise exception 'Нет доступа к ученику';
  end if;
  v_teacher := public.classroom_is_editor() or public.classroom__current_teacher_id() is not null;
  select id into v_enroll from public.classroom_enrollments
   where course_id = p_course_id and student_id = p_student_id;
  select coalesce(jsonb_agg(item order by u_sort, l_sort), '[]'::jsonb) into v_out
  from (
    select u.sort_order as u_sort, l.sort_order as l_sort,
      jsonb_build_object(
        'lesson_id', l.id,
        'unit_title', u.title,
        'title', l.title,
        'kind', l.kind,
        'is_published', l.is_published,
        'assigned', a.id is not null,
        'active', coalesce(a.status, '') = 'active',
        'status', a.status,
        'deadline_at', a.deadline_at,
        'hw_status', coalesce(pr.status, case when pr.id is null then null else 'in_progress' end),
        'submitted_at', pr.submitted_at,
        'reviewed_at', pr.reviewed_at,
        'completed', pr.status = 'reviewed',
        'score', case when pr.status = 'reviewed' then pr.score end,
        'auto_score', case when v_teacher then pr.auto_score end,
        'submitted', coalesce(pr.status in ('submitted', 'reviewed'), false),
        'review_pending', coalesce(pr.status = 'submitted', false),
        'retake', coalesce(pr.status = 'retake', false)
      ) as item
    from public.classroom_units u
    join public.classroom_lessons l on l.unit_id = u.id
    left join public.classroom_assignments a
      on a.lesson_id = l.id and a.target_type = 'student' and a.target_id = p_student_id
    left join public.classroom_progress pr
      on pr.enrollment_id = v_enroll and pr.lesson_id = l.id
    where u.course_id = p_course_id
  ) t;
  return jsonb_build_object('enrollment_id', v_enroll, 'lessons', v_out);
end $$;

-- ── 13. Старые функции проверки task: без уведомлений ученику по блоку ──────
-- Ученик получает одно уведомление — из classroom_review_finish.

create or replace function public.classroom_grade_task(
  p_enrollment_id uuid, p_block_id uuid, p_section_key text, p_score integer,
  p_max_score integer default 100, p_comment text default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  v_user uuid := public.classroom__my_user_id();
  v_parts int; v_graded int;
begin
  if not public.classroom__can_review(p_enrollment_id) then
    raise exception 'Проверять может только учитель ученика или методист';
  end if;
  insert into public.classroom_grades
    (enrollment_id, block_id, section_key, score, max_score, comment, graded_by, graded_at)
  values (p_enrollment_id, p_block_id, p_section_key, p_score, coalesce(p_max_score,100), p_comment, v_user, now())
  on conflict (enrollment_id, block_id, section_key) do update
    set score = excluded.score, max_score = excluded.max_score, comment = excluded.comment,
        graded_by = excluded.graded_by, graded_at = now();
  select case when jsonb_typeof(payload->'parts') = 'array' then jsonb_array_length(payload->'parts') else 1 end
    into v_parts from public.classroom__enr_block(p_enrollment_id, p_block_id);
  select count(*) into v_graded from public.classroom_grades
   where enrollment_id = p_enrollment_id and block_id = p_block_id;
  if v_graded >= coalesce(v_parts,1) then
    update public.classroom_submissions set review_status = null, reviewed_at = now()
     where enrollment_id = p_enrollment_id and block_id = p_block_id;
  end if;
  return jsonb_build_object('ok', true, 'block_id', p_block_id,
    'graded_parts', v_graded, 'parts', coalesce(v_parts,1), 'closed', v_graded >= coalesce(v_parts,1));
end $$;

create or replace function public.classroom_finish_review(
  p_enrollment_id uuid, p_block_id uuid, p_note text default null)
returns jsonb language plpgsql security definer set search_path = public as $$
begin
  if not public.classroom__can_review(p_enrollment_id) then
    raise exception 'Проверять может только учитель ученика или методист';
  end if;
  update public.classroom_submissions
     set review_status = null, reviewed_at = now(), reviewer_note = coalesce(p_note, reviewer_note)
   where enrollment_id = p_enrollment_id and block_id = p_block_id;
  if not found then raise exception 'Сдача не найдена'; end if;
  return jsonb_build_object('ok', true);
end $$;
