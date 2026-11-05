-- Серии «по предложению на блок» сводятся в одно задание (решение Анны
-- 05.11.2026: «7 Да, сводить, только чтобы ничего не пострадало и там картинки
-- не убрались»). Стало возможно после правки платформы 05.11: у `gaps` работает
-- режим «выбери вариант» и картинка у каждой строки (`line_image`).
-- Копия — classroom_backup_gaps_serii_20261105.

do $$
declare
  v_media text := 'https://classroom.wowteach.ru/media/';
  L1 uuid := '491e5b1d-7932-44c5-906c-5e1c87deda89'; -- SM2 Unit 2 Test, блоки 5–7
  L2 uuid := '200094f1-e6b5-432b-b907-629a2a6d03c8'; -- SM2 Unit 6 ДЗ 3, блоки 10–14
  L3 uuid := 'f8c475be-1c33-46a5-98cc-55762daa2e66'; -- SM2 Unit 6 ДЗ 7, блоки 6–8
  L4 uuid := '37abc0e0-55bf-4136-aabc-f3307cf24fff'; -- SM3 Unit 4 ДЗ 7, блоки 7–11
begin

create table if not exists classroom_backup_gaps_serii_20261105 as
  select * from classroom_blocks where lesson_id in (L1, L2, L3, L4);

-- 1. SM2 Unit 2 Test
update classroom_blocks set payload = replace($j${
  "mode": "choice", "skill": "grammar",
  "title": "Заполни пропуски: выбери подходящий вариант",
  "text": "The bear __doesn't__ like bananas.\nA: Does May __like__ cats?\nB: No, she __doesn't__. She likes dogs.\nA: __Does__ your brother get up at 6 o'clock?\nB: Yes, he __does__, but not at the weekend.",
  "line_image": ["@@MEDIA@@sm2/u2/test_bear.webp", "@@MEDIA@@sm2/u2/test_cat_dog.webp", "", "@@MEDIA@@sm2/u2/test_wakeup.webp", ""],
  "choices": [["don't", "isn't"], ["likes", "liking"], ["don't", "isn't"], ["Do", "Is"], ["do", "is"]]
}$j$, '@@MEDIA@@', v_media)::jsonb
  where lesson_id = L1 and sort_order = 4;
delete from classroom_blocks where lesson_id = L1 and sort_order in (5, 6);

-- 2. SM2 Unit 6 ДЗ 3
update classroom_blocks set payload = replace($j${
  "mode": "choice",
  "title": "Посмотри на картинку и выбери правильное слово",
  "text": "It's __your__ heart.\nIt's __his__ heart.\nIt's __her__ heart.\nIt's __our__ house.\nIt's __their__ house.",
  "line_image": ["@@MEDIA@@sm2/u6/h_your.webp", "@@MEDIA@@sm2/u6/h_his.webp", "@@MEDIA@@sm2/u6/h_her.webp", "@@MEDIA@@sm2/u6/h_our.webp", "@@MEDIA@@sm2/u6/h_their.webp"],
  "choices": [["my", "her"], ["her", "their"], ["his", "our"], ["their", "your"], ["our", "his"]]
}$j$, '@@MEDIA@@', v_media)::jsonb
  where lesson_id = L2 and sort_order = 9;
delete from classroom_blocks where lesson_id = L2 and sort_order between 10 and 13;

-- 3. SM2 Unit 6 ДЗ 7
update classroom_blocks set payload = replace($j${
  "mode": "choice",
  "title": "Посмотри на картинку и выбери правильный ответ на вопрос",
  "text": "Is she sad? __No, she isn't.|No, she isn't__\nIs it a dog? __No, it isn't.|No, it isn't__\nAre we a family? __Yes, we are.|Yes, we are__",
  "line_image": ["@@MEDIA@@sm2/u6/q_tall.webp", "@@MEDIA@@sm2/u6/q_rhino.webp", "@@MEDIA@@sm2/u6/q_family.webp"],
  "choices": [["Yes, she is.", "No, they aren't."], ["Yes, it is.", "No, he isn't."], ["No, we aren't.", "Yes, they are."]]
}$j$, '@@MEDIA@@', v_media)::jsonb
  where lesson_id = L3 and sort_order = 5;
delete from classroom_blocks where lesson_id = L3 and sort_order in (6, 7);

-- 4. SM3 Unit 4 ДЗ 7 — здесь фишки: шестое слово из заголовка (below) не нужно
-- ни в одном предложении, оно и становится лишней фишкой.
update classroom_blocks set payload = replace($j${
  "mode": "drag",
  "title": "Впиши above, near, below, opposite, next to, in front of",
  "text": "The ball is __above__ the table.\nThe bear is __next to__ the ball.\nThe elephant is __in front of__ the chair.\nThe mouse is __near__ the TV.\nThe white cat is __opposite__ the grey cat.",
  "line_image": ["@@MEDIA@@sm3/u4/prep_ball_above_table.webp", "@@MEDIA@@sm3/u4/prep_teddy_next_to_ball.webp", "@@MEDIA@@sm3/u4/prep_elephant_in_front_of_chair.webp", "@@MEDIA@@sm3/u4/prep_mouse_near_tv.webp", "@@MEDIA@@sm3/u4/prep_cats_opposite.webp"],
  "bank": ["above", "next to", "in front of", "near", "opposite", "below", "behind"]
}$j$, '@@MEDIA@@', v_media)::jsonb
  where lesson_id = L4 and sort_order = 6;
delete from classroom_blocks where lesson_id = L4 and sort_order between 7 and 10;

-- перенумерация
update classroom_blocks set sort_order = sort_order + 1000 where lesson_id in (L1, L2, L3, L4);
update classroom_blocks t set sort_order = z.rn - 1
from (select id, row_number() over (partition by lesson_id order by sort_order) rn
      from classroom_blocks where lesson_id in (L1, L2, L3, L4)) z
where t.id = z.id;

end $$;
