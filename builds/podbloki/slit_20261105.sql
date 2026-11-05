-- Одинаковые задания подряд сводятся в одно (решение Анны 05.11.2026: «делаем
-- как лучше и логичнее»). Там, где платформа умеет подпункты, блоки слиты;
-- где не умеет (speaking, sequence) — заголовкам проставлена нумерация серии
-- отдельной правкой (classroom_backup_serii_zagolovki_20261105).
--
-- Слияния здесь:
--   gg1 Unit 7 ДЗ 1   — два match «Соедини картинку и слово» → один
--   gg2 Unit 2 ДЗ 1   — три match «Соедини картинку со словом» → один
--   sm3 Unit 2 Test   — два match «Соедини слова с картинками» → один
--   sm2 Unit 3 ДЗ 2   — два order «Составь предложения» → один (8 пунктов)
--   sm3 Unit 3 ДЗ 2   — шесть task «сколько времени» → один с шестью часами
--
-- Копия затронутых уроков — classroom_backup_podbloki_slit_20261105.

do $$
declare
  v_media text := 'https://classroom.wowteach.ru/media/';
  Lgg1 uuid := 'f06dbd79-1825-48aa-9d7e-579549288df5';
  Lgg2 uuid := 'abf66c3b-2936-433e-adbf-e516a4552c8b';
  Lsm3t uuid := 'e03c6b59-c239-49d7-8b2f-92922bdfe114';
  Lsm2 uuid := 'b586c4d4-f4a6-44e0-959b-49d62e90b9f5';
  Lsm3 uuid := '5c042a0d-48c7-4e20-ab7a-a2c91fd67d50';
begin

create table if not exists classroom_backup_podbloki_slit_20261105 as
  select * from classroom_blocks where lesson_id in (Lgg1, Lgg2, Lsm3t, Lsm2, Lsm3);

-- 1. gg1 Unit 7 ДЗ 1: match sort 4 + sort 5
update classroom_blocks a set payload = jsonb_set(a.payload, '{pairs}',
       (a.payload->'pairs') || (select b.payload->'pairs' from classroom_blocks b where b.lesson_id = Lgg1 and b.sort_order = 5))
  where a.lesson_id = Lgg1 and a.sort_order = 4;
delete from classroom_blocks where lesson_id = Lgg1 and sort_order = 5;

-- 2. gg2 Unit 2 ДЗ 1: match sort 3 + 4 + 5
update classroom_blocks a set payload = jsonb_set(a.payload, '{pairs}',
       (a.payload->'pairs')
       || (select b.payload->'pairs' from classroom_blocks b where b.lesson_id = Lgg2 and b.sort_order = 4)
       || (select b.payload->'pairs' from classroom_blocks b where b.lesson_id = Lgg2 and b.sort_order = 5))
  where a.lesson_id = Lgg2 and a.sort_order = 3;
delete from classroom_blocks where lesson_id = Lgg2 and sort_order in (4, 5);

-- 3. sm3 Unit 2 Test: match sort 1 + sort 3 (после правки порядка они разъехались)
update classroom_blocks a set payload = jsonb_set(a.payload, '{pairs}',
       (a.payload->'pairs') || (select b.payload->'pairs' from classroom_blocks b where b.lesson_id = Lsm3t and b.sort_order = 3))
  where a.lesson_id = Lsm3t and a.sort_order = 1;
delete from classroom_blocks where lesson_id = Lsm3t and sort_order = 3;

-- 4. sm2 Unit 3 ДЗ 2: order sort 8 + sort 9.
-- У пунктов второго блока картинок не было, а правило — «либо у всех, либо ни
-- у одного»: cinema и park берём готовые, zoo меняем на swimming pool (есть
-- картинка, цель задания — hasn't got — сохраняется).
update classroom_blocks a set payload = jsonb_set(a.payload, '{items}',
       (a.payload->'items') || replace($j$[
         {"image": "@@MEDIA@@sm2/u3/p_cinema.webp",
          "words": ["Has","your","town","got","a","cinema?"], "sentence": "Has your town got a cinema?"},
         {"image": "@@MEDIA@@sm2/u3/p_park.webp",
          "words": ["Our","town","has","got","a","big","park."], "sentence": "Our town has got a big park."},
         {"image": "@@MEDIA@@sm2/u3/p_swimming_pool.webp",
          "words": ["My","town","hasn't","got","a","swimming pool."], "sentence": "My town hasn't got a swimming pool."}
       ]$j$, '@@MEDIA@@', v_media)::jsonb)
  where a.lesson_id = Lsm2 and a.sort_order = 8;
delete from classroom_blocks where lesson_id = Lsm2 and sort_order = 9;

-- 5. sm3 Unit 3 ДЗ 2: шесть task «сколько времени» → один
update classroom_blocks a set payload = replace($j${
  "skill": "writing",
  "title": "Посмотри на картинки и напиши, сколько времени",
  "html": "<p>Напиши по-английски, сколько времени на каждых часах. По строке на картинку: сначала 1, потом 2 и так далее.</p><p><b>1.</b> <img src=\"@@MEDIA@@sm3/u3/digital_two_fifteen.svg\" alt=\"\" style=\"height:110px\"> &nbsp; <b>2.</b> <img src=\"@@MEDIA@@sm3/u3/digital_eleven_oclock.svg\" alt=\"\" style=\"height:110px\"> &nbsp; <b>3.</b> <img src=\"@@MEDIA@@sm3/u3/digital_twelve_forty_five.svg\" alt=\"\" style=\"height:110px\"></p><p><b>4.</b> <img src=\"@@MEDIA@@sm3/u3/digital_nine_thirty.svg\" alt=\"\" style=\"height:110px\"> &nbsp; <b>5.</b> <img src=\"@@MEDIA@@sm3/u3/digital_five_forty_five.svg\" alt=\"\" style=\"height:110px\"> &nbsp; <b>6.</b> <img src=\"@@MEDIA@@sm3/u3/digital_eight_oclock.svg\" alt=\"\" style=\"height:110px\"></p>"
}$j$, '@@MEDIA@@', v_media)::jsonb
  where a.lesson_id = Lsm3 and a.sort_order = 3;
delete from classroom_blocks where lesson_id = Lsm3 and sort_order between 4 and 8;

-- перенумерация пяти уроков без дырок
update classroom_blocks set sort_order = sort_order + 1000
  where lesson_id in (Lgg1, Lgg2, Lsm3t, Lsm2, Lsm3);
update classroom_blocks t set sort_order = z.rn - 1
from (select id, row_number() over (partition by lesson_id order by sort_order) rn
      from classroom_blocks where lesson_id in (Lgg1, Lgg2, Lsm3t, Lsm2, Lsm3)) z
where t.id = z.id;

end $$;
