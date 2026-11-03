-- Контроль после заливки (03.11.2026). Сверка с копией classroom_backup_tf_v_kviz_vse_20261103:
-- тип quiz, число вопросов = числу прежних пунктов, два варианта «Верно»/«Неверно»,
-- correct = [0]/[1] точно по прежнему boolean, title и skill сохранены,
-- пункт дописан в конец q, материал на месте.
with old as (select id, jsonb_array_length(payload->'statements') n_old, payload->'statements' st,
                    payload->>'skill' sk, payload->>'title' ti
             from classroom_backup_tf_v_kviz_vse_20261103),
nw as (select id, type, payload from classroom_blocks)
select count(*) total,
  count(*) filter (where nw.type='quiz') is_quiz,
  count(*) filter (where jsonb_array_length(nw.payload->'questions') = old.n_old) n_match,
  count(*) filter (where (select bool_and(jsonb_array_length(q->'options')=2
        and q->'options'->0->>'text'='Верно' and q->'options'->1->>'text'='Неверно')
      from jsonb_array_elements(nw.payload->'questions') q)) opts_ok,
  count(*) filter (where (select bool_and((q->'correct') = case when (old.st->(ord::int-1)->>'correct')::boolean
        then '[0]'::jsonb else '[1]'::jsonb end)
      from jsonb_array_elements(nw.payload->'questions') with ordinality t(q,ord))) keys_ok,
  count(*) filter (where coalesce(nw.payload->>'skill','-') = coalesce(old.sk,'-')) skill_ok,
  count(*) filter (where nw.payload->>'title' = old.ti) title_ok,
  count(*) filter (where (select bool_and(q->>'q' like '%<p><b>' || (old.st->(ord::int-1)->>'text') || '</b></p>')
      from jsonb_array_elements(nw.payload->'questions') with ordinality t(q,ord))) stmt_in_q_ok
from old join nw using (id);
-- результат 03.11.2026: 43 / 43 / 43 / 43 / 43 / 43 / 43 / 43
