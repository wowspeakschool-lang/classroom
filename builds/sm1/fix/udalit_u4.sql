-- SM1 · юнит 4 «Lunchtime (Food)» · блоки на удаление (запускает Анна в SQL Editor)
-- Копия всех 90 блоков юнита до правок: classroom_backup_sm1_fix_u4_20261021
-- Номера блоков — как в редакторе СЕЙЧАС, после перестановок.
-- Нумерацию sort_order после удаления не чиню — её выровняет координатор.

-- Фоника (решение Анны от 20.10.2026: из SM1 убирается целиком).
-- Все пять домашек уже дозаполнены, объём после удаления не просядет.
delete from classroom_blocks where id = '5e4f7ae2-a4f3-4da0-ba82-14c9052a364a'; -- юнит 4 · ДЗ 4 · блок 3  · match «соедини картинку со словами» — new / screw / cube / flute
delete from classroom_blocks where id = 'f1ba0328-5714-44a3-a36f-3b896beb0530'; -- юнит 4 · ДЗ 5 · блок 3  · quiz «послушай звук» — saw/draw/jaw → straw, how/now/wow → mouse, cloud
delete from classroom_blocks where id = 'd65feea7-0b66-4209-a578-19cf4485f2a4'; -- юнит 4 · ДЗ 6 · блок 3  · sort по звукам |ɪ| heavy/baby, |s| ice/fence, |dʒ| giraffe/orange
delete from classroom_blocks where id = '8c0708ef-f936-4d4c-9cc0-a9562d34a81b'; -- юнит 4 · ДЗ 7 · блок 2  · quiz «выбери слово, в котором есть этот звук» — straw / bone / giraffe
delete from classroom_blocks where id = 'f6b46847-bbac-4442-9e95-2f4abf51873f'; -- юнит 4 · тест · блок 3 · speaking «прочитай вслух» — turtle, crow, rope, cube, cloud, giraffe

-- Дубль внутри ДЗ 5: блок 6 (match «слово ↔ число») и блок 7 (quiz «слово → число»)
-- проверяют одно и то же; на месте блока 7 теперь стоит аудирование «холодильник Тома».
delete from classroom_blocks where id = '6df6d031-eb4f-4b6e-a527-a5ec7e7c3b22'; -- юнит 4 · ДЗ 5 · блок 7 · quiz «слово → цифра», десять вопросов, дубль блока 6
