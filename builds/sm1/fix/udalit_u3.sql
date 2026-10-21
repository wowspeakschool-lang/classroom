-- SM1 · юнит 3 «My pets» · блоки на удаление (запускает Анна в SQL Editor)
-- Копия всех 93 блоков юнита до правок: classroom_backup_sm1_fix_u3_20261021
-- Нумерацию sort_order после удаления не чиню — её выровняет координатор.

-- Фоника (решение Анны от 20.10.2026: из SM1 убирается целиком)
delete from classroom_blocks where id = '54b38a0b-4323-4181-9db8-31e2123ae745'; -- юнит 3 · ДЗ 2 · блок 3 · quiz «послушай звук» на A_E и Yy (cake/snake/spy/fly)
delete from classroom_blocks where id = '86359964-eac5-4fd2-b279-e2a4bb4bfb3c'; -- юнит 3 · ДЗ 5 · блок 3 · quiz на OI и EAR (coin/hear/oil/near), к тому же по два варианта ответа
delete from classroom_blocks where id = '8c52bc7f-ce30-4db8-af4f-3c14af567bd5'; -- юнит 3 · ДЗ 6 · блок 3 · sort «er или air» (hair/chair/sister/brother)
delete from classroom_blocks where id = 'ca74cd17-f866-4d41-b2c9-1d1afd4162a3'; -- юнит 3 · ДЗ 7 · блок 17 · order «Составь слово: chair», пятый фоничный, замены ему не нашлось; стоит последним, пока не удалён

-- ДЗ 1 перегружена: девять «Собери слово» на девять слов подряд.
-- Остаются пять коротких (rat, frog, dog, cat, duck); длинные четыре слова
-- ребёнок пишет целиком в блоке 17 и собирает заново в ДЗ 7.
delete from classroom_blocks where id = '2abd9de9-0096-44af-91b6-b5664fbd5432'; -- юнит 3 · ДЗ 1 · блок 7  · order «Собери слово: слон»
delete from classroom_blocks where id = '54f9c9a9-437d-4c3e-81cf-28600764d6b2'; -- юнит 3 · ДЗ 1 · блок 9  · order «Собери слово: ящерица»
delete from classroom_blocks where id = '19a9c799-fa1f-410d-b576-b30f1b739a73'; -- юнит 3 · ДЗ 1 · блок 11 · order «Собери слово: паук»
delete from classroom_blocks where id = '26049fcb-e245-4fce-9aa0-57780d9b49a5'; -- юнит 3 · ДЗ 1 · блок 15 · order «Собери слово: осел»
