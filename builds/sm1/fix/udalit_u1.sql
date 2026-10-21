-- SM1 · юнит 1 «Unit 1 · My school» — блоки на удаление (вычитка 21.10.2026)
-- Запускать в SQL Editor Supabase (delete через MCP зависает).
-- Копия всех блоков юнита до правок: classroom_backup_sm1_fix_u1_20261021
-- Нумерация блоков — как в редакторе, НА МОМЕНТ ДО общего перенумерования.

delete from classroom_blocks where id = '727b1f7a-cc74-4c1d-9794-690061d80bb8'; -- юнит 1 · ДЗ 1 · блок 4 · фоника: «послушай слово» на pet, net, mum, cup, red, rat
delete from classroom_blocks where id = '983d7c89-02fe-4ebd-86cd-a872501a7144'; -- юнит 1 · ДЗ 2 · блок 3 · фоника: hat, hippo, bed, rabbit, fig, frog
delete from classroom_blocks where id = 'ff83901c-ca47-4c2a-a6ba-01135d5ec5dc'; -- юнит 1 · ДЗ 3 · блок 3 · фоника: doll, bell, jump, jog, van, vet
delete from classroom_blocks where id = '9f8b95c0-f4fb-4e11-830f-8743c2c6ed3e'; -- юнит 1 · ДЗ 4 · блок 3 · фоника: well, west, box, taxi, yell, yes
delete from classroom_blocks where id = 'd88ee1c8-fc40-47bc-868a-ccb8f0757842'; -- юнит 1 · ДЗ 5 · блок 2 · текст с карточкой букв Zz/Qq, другого содержания в блоке нет
delete from classroom_blocks where id = 'eb5e4288-24eb-46b7-b86c-55aec9e34273'; -- юнит 1 · ДЗ 5 · блок 3 · фоника: buzz, zigzag, queen, quest

-- Итого 6 блоков. После удаления заданий остаётся: ДЗ 1 — 15, ДЗ 2 — 9,
-- ДЗ 3 — 8, ДЗ 4 — 8, ДЗ 5 — 9, ДЗ 6 — 13, ДЗ 7 — 21, тест — 12.
