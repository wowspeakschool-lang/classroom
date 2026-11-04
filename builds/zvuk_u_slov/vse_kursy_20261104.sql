-- Звук у написанного слова — убираем везде, кроме SM0 и Wow Dragon
-- Решение Анны 04.11.2026: «131 убираем везде, кроме SM0 и WowDragon».
--
-- Правило одно: звук снимается с того места, где слово уже написано.
-- В match — со стороны пары с буквами; сторона без букв («🔊», номер, пусто)
-- это настоящее аудирование, её не трогаем. В quiz — с варианта, у которого
-- есть текст, и с вопроса, в котором написано английское слово или фраза;
-- вопрос с одной русской инструкцией («Послушай и выбери») звук сохраняет.
-- Запись на уровне блока (payload.audio) не трогаем нигде.

create table if not exists classroom_backup_zvuk_u_slov_20261104 as
select b.* from classroom_blocks b
join classroom_lessons l on l.id=b.lesson_id
join classroom_units u on u.id=l.unit_id
join classroom_courses c on c.id=u.course_id
where c.slug not in ('sm0','wow-dragon-1','wow-dragon-2')
  and b.type in ('match','quiz');

-- match
with src as (
  select b.id, pr.ordinality as ord,
         (case when regexp_replace(coalesce(pr.value->>'left',''),'[^a-zA-Zа-яА-ЯёЁ]','','g') <> ''
               then pr.value - 'left_audio' - 'left_audio_tts' else pr.value end) as v1
  from classroom_blocks b
  join classroom_lessons l on l.id=b.lesson_id
  join classroom_units u on u.id=l.unit_id
  join classroom_courses c on c.id=u.course_id,
  lateral jsonb_array_elements(b.payload->'pairs') with ordinality pr
  where c.slug not in ('sm0','wow-dragon-1','wow-dragon-2') and b.type='match'
), src2 as (
  select id, ord,
         (case when regexp_replace(coalesce(v1->>'right',''),'[^a-zA-Zа-яА-ЯёЁ]','','g') <> ''
               then v1 - 'right_audio' - 'right_audio_tts' else v1 end) as v2
  from src
), agg as (select id, jsonb_agg(v2 order by ord) as pairs from src2 group by id)
update classroom_blocks b set payload = jsonb_set(b.payload, '{pairs}', a.pairs)
from agg a where a.id = b.id and b.payload->'pairs' is distinct from a.pairs;

-- quiz
with q as (
  select b.id, qq.ordinality as qo, qq.value as qv
  from classroom_blocks b
  join classroom_lessons l on l.id=b.lesson_id
  join classroom_units u on u.id=l.unit_id
  join classroom_courses c on c.id=u.course_id,
  lateral jsonb_array_elements(b.payload->'questions') with ordinality qq
  where c.slug not in ('sm0','wow-dragon-1','wow-dragon-2') and b.type='quiz'
), opts as (
  select q.id, q.qo, jsonb_agg(
      case when regexp_replace(coalesce(o.value->>'text',''),'[^a-zA-Zа-яА-ЯёЁ]','','g') <> ''
           then o.value - 'audio' - 'audio_tts' else o.value end order by o.ordinality) as options
  from q, lateral jsonb_array_elements(q.qv->'options') with ordinality o
  group by q.id, q.qo
), qfix as (
  select q.id, q.qo,
    (case when regexp_replace(coalesce(q.qv->>'q',''),'[^a-zA-Z]','','g') <> ''
          then q.qv - 'audio' - 'audio_tts' else q.qv end)
    || (case when opts.options is not null then jsonb_build_object('options', opts.options) else '{}'::jsonb end) as v
  from q left join opts on opts.id = q.id and opts.qo = q.qo
), agg as (select id, jsonb_agg(v order by qo) as questions from qfix group by id)
update classroom_blocks b set payload = jsonb_set(b.payload, '{questions}', a.questions)
from agg a where a.id = b.id and b.payload->'questions' is distinct from a.questions;

-- Диктанты тестов SM1 (решение от 18.10: диктант — картинка, а не звук).
create table if not exists classroom_backup_diktant_zvuk_20261104 as
select * from classroom_blocks where id in
 ('e81c2be8-55b0-44d3-bae3-cf17e1b8792f','669dd1e7-8854-444d-848f-3d835b5259a8','9c42967b-9c11-43ed-8654-05ca452dafcf');

with it as (
  select b.id, x.ordinality as ord, (x.value - 'audio' - 'audio_tts') as v
  from classroom_blocks b, lateral jsonb_array_elements(b.payload->'items') with ordinality x
  where b.id in ('e81c2be8-55b0-44d3-bae3-cf17e1b8792f','669dd1e7-8854-444d-848f-3d835b5259a8','9c42967b-9c11-43ed-8654-05ca452dafcf')
), agg as (select id, jsonb_agg(v order by ord) as items from it group by id)
update classroom_blocks b set payload = jsonb_set(b.payload,'{items}', a.items)
from agg a where a.id=b.id;
