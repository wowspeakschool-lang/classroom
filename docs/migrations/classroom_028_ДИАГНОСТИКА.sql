-- ============================================================
-- Classroom: сверка состояния базы с журналом миграций
-- Только SELECT. Ничего не меняет.
-- Прогнать целиком одним куском — вернёт одну таблицу.
-- ============================================================

select 'CHECK на classroom_blocks.type' as проверка,
       pg_get_constraintdef(oid)        as значение
  from pg_constraint
 where conrelid = 'public.classroom_blocks'::regclass
   and contype  = 'c'

union all
select 'submit_block знает типы',
       coalesce((select string_agg(t, ', ' order by t)
                   from unnest(array['quiz','exact_input','match','order',
                                     'sort','gaps','truefalse','speaking']) t
                  where position('''' || t || '''' in pg_get_functiondef(p.oid)) > 0),
                '— функция пустая')
  from pg_proc p
 where p.proname = 'classroom_submit_block'

union all
select 'completion_check знает типы',
       coalesce((select string_agg(t, ', ' order by t)
                   from unnest(array['quiz','exact_input','match','order',
                                     'sort','gaps','truefalse','speaking','task']) t
                  where position('''' || t || '''' in pg_get_functiondef(p.oid)) > 0),
                '— функция пустая')
  from pg_proc p
 where p.proname = 'classroom__completion_check'

union all
select 'needs_review знает speaking',
       case when position('speaking' in pg_get_functiondef(oid)) > 0
            then 'да' else 'НЕТ — записи не пойдут на проверку' end
  from pg_proc
 where proname = 'classroom__block_needs_review'

union all
select 'функция classroom__gaps_accept',
       case when count(*) > 0 then 'есть' else 'НЕТ — gaps не проверяется' end
  from pg_proc
 where proname = 'classroom__gaps_accept'

union all
select 'типы блоков, реально лежащие в базе',
       coalesce(string_agg(distinct type, ', '), '—')
  from public.classroom_blocks

union all
select 'блоков новых типов в базе',
       coalesce(count(*)::text, '0')
  from public.classroom_blocks
 where type in ('gaps','truefalse','speaking');
