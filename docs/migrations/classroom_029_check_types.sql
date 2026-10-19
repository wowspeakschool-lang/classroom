-- ============================================================
-- 029. CHECK на classroom_blocks.type: + gaps, truefalse, speaking
--
-- Требует 028 (ветки проверки в classroom_submit_block).
-- Без этой миграции блоки трёх новых типов не сохраняются.
--
-- Что делает: снимает существующий CHECK на колонке type
-- и ставит его заново с тремя добавленными значениями.
-- Прежние 10 типов сохранены дословно.
-- Данные не трогаются. Повторный прогон безопасен.
-- ============================================================

-- ---------- 1. Что стоит сейчас ----------
select conname                    as имя_ограничения,
       pg_get_constraintdef(oid)  as было
  from pg_constraint
 where conrelid = 'public.classroom_blocks'::regclass
   and contype  = 'c'
   and pg_get_constraintdef(oid) like '%(type = ANY%';

-- ---------- 2. Замена ----------
do $do$
declare
  v_name text;
begin
  select conname into v_name
    from pg_constraint
   where conrelid = 'public.classroom_blocks'::regclass
     and contype  = 'c'
     and pg_get_constraintdef(oid) like '%(type = ANY%'
   limit 1;

  if v_name is null then
    raise notice 'CHECK на type не найден — снимать нечего';
  else
    execute format('alter table public.classroom_blocks drop constraint %I', v_name);
    raise notice 'Снято ограничение %', v_name;
  end if;

  alter table public.classroom_blocks
    add constraint classroom_blocks_type_check
    check (type = any (array[
      'text','video','quiz','exact_input','match','task','embed',
      'order','sort','flashcards',
      'gaps','truefalse','speaking'
    ]));

  raise notice 'Ограничение поставлено заново, типов: 13';
end
$do$;

-- ---------- 3. Проверка ----------
select 'CHECK на type' as проверка,
       pg_get_constraintdef(oid) as стало
  from pg_constraint
 where conrelid = 'public.classroom_blocks'::regclass
   and conname  = 'classroom_blocks_type_check'

union all
select 'новые типы разрешены',
       case when (select count(*) from unnest(array['gaps','truefalse','speaking']) t
                   where position('''' || t || '''' in
                         (select pg_get_constraintdef(oid) from pg_constraint
                           where conrelid = 'public.classroom_blocks'::regclass
                             and conname  = 'classroom_blocks_type_check')) > 0) = 3
            then 'да, все три' else 'НЕТ' end;
