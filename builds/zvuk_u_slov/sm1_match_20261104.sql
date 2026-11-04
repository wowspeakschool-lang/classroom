-- SM1: убираем звук у написанного слова в «Соедини слова с картинками»
-- Решение Анны 04.11.2026: «После написанного слова есть звук. Он не нужен
-- в этой программе. Дети умеют читать».
--
-- Снимаем left_audio/left_audio_tts и right_audio/right_audio_tts только с той
-- стороны пары, где рядом стоит написанное слово. Там, где на стороне нет букв
-- (пусто, «🔊», номер), звук и есть само задание — он остаётся. Запись на уровне
-- блока (payload.audio у «LISTENING. Послушай запись…») не трогаем.

create table if not exists classroom_backup_sm1_match_audio_20261104 as
select b.* from classroom_blocks b
join classroom_lessons l on l.id=b.lesson_id
join classroom_units u on u.id=l.unit_id
join classroom_courses c on c.id=u.course_id
where c.slug='sm1' and b.type='match';

with src as (
  select b.id, pr.ordinality as ord,
         (case when regexp_replace(coalesce(pr.value->>'left',''),'[^a-zA-Zа-яА-ЯёЁ]','','g') <> ''
               then pr.value - 'left_audio' - 'left_audio_tts' else pr.value end) as v1
  from classroom_blocks b
  join classroom_lessons l on l.id=b.lesson_id
  join classroom_units u on u.id=l.unit_id
  join classroom_courses c on c.id=u.course_id,
  lateral jsonb_array_elements(b.payload->'pairs') with ordinality pr
  where c.slug='sm1' and b.type='match'
), src2 as (
  select id, ord,
         (case when regexp_replace(coalesce(v1->>'right',''),'[^a-zA-Zа-яА-ЯёЁ]','','g') <> ''
               then v1 - 'right_audio' - 'right_audio_tts' else v1 end) as v2
  from src
), agg as (
  select id, jsonb_agg(v2 order by ord) as pairs from src2 group by id
)
update classroom_blocks b set payload = jsonb_set(b.payload, '{pairs}', a.pairs)
from agg a
where a.id = b.id and b.payload->'pairs' is distinct from a.pairs;

-- Два задания назывались «послушай слово и найди картинку», хотя слово в них
-- было написано рядом. Со снятым звуком это просто «соедини слово с картинкой».
update classroom_blocks set payload = jsonb_set(payload,'{title}',
  to_jsonb('Соедини имя героя с его картинкой'::text))
where id = '5a18a661-3695-4216-b879-00fd0bf43c35';

update classroom_blocks set payload = jsonb_set(payload,'{title}',
  to_jsonb('Соедини слово с цветом'::text))
where id = '294c3f5b-5833-4302-a166-2f460eeda1c5';
