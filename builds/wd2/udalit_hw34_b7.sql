-- Wow Dragon 2, ДЗ 34, блок 7 «Посмотри на ряд. Какая буква следующая?»
-- Решение Анны от 23.10.2026: задание убираем.
-- Причина: это задание не на букву, а на размер — в ряду три одинаковых B
-- разной величины, и два варианта ответа из трёх тоже B, различаются только
-- размером. В курсе про буквы оно выбивается.
--
-- Копия блока уже лежит в classroom_backup_wd2_20261023.
-- Запускать в SQL Editor: delete через MCP не проходит.

begin;

select count(*) as kopiya_est from classroom_backup_wd2_20261023
where id = '485aa22f-e432-47d7-918a-93af774c514a';

delete from classroom_blocks
where id = '485aa22f-e432-47d7-918a-93af774c514a';

-- проверка: блока нет, в уроке осталось 13 блоков
select count(*) as ostalos_udalyaemyh from classroom_blocks
where id = '485aa22f-e432-47d7-918a-93af774c514a';

select count(*) as blokov_v_dz34 from classroom_blocks
where lesson_id = '7b4622b7-baf6-42b9-b7b8-c20882ad9fb6';

commit;
