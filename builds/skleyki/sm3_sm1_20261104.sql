-- Склеенные домашки: убираем шов «вторая часть» и выстраиваем лесенку сложности
-- (решения Анны 20.10.2026 «задания идут по возрастанию сложности» и
--  03.11.2026 «один план урока — одна домашка»).
--
-- SM3, ДЗ 1 юнитов 3, 6, 7, 8, 9 — у всех пяти одинаковая склейка: после
-- «напиши слово по картинке» стоял экран «А теперь — вторая, вторая часть»,
-- а за ним шли задания легче предыдущих. Шов убран, «напиши слово» (самое
-- трудное) переставлено после «соедини» и «впиши пропуск».
-- SM1 Unit 9 ДЗ 6 — тот же шов «Переходим ко второй части», порядок там
-- уже правильный, поэтому только шов и подводка внутри задания 10.
--
-- Удаляются 7 блоков: шесть швов и текст с образцом в SM3 u3 (образец
-- переехал внутрь самого задания, в payload.material).

create table if not exists classroom_backup_skleyki_20261104 as
select * from classroom_blocks where lesson_id in (
  select lesson_id from classroom_blocks where id in (
    '32705c8f-bcc7-4902-980f-1a1d7b50014f',
    '5b57c164-88f8-4524-abc5-892151cd8524',
    '0be38b98-52d6-4397-b32e-d175b645a34d',
    '394f2e86-46a3-40a6-be53-4f1f4907ffd8',
    '45462107-4d76-4424-b487-bd5b3f0cb867',
    '66821aef-66d5-4f9a-abdd-19a22b73fb28'));

-- 1. SM3 u3 ДЗ 1 — образец «Write about you» внутри задания, без подводки
--    «ты справился с основными заданиями».
update classroom_blocks set payload =
  jsonb_set(jsonb_set(payload, '{material}',
    to_jsonb($t$<p><b>Write about you.</b></p><p><i>I like taking the dog for a walk. I don’t like tidying up.</i></p>$t$::text)),
    '{html}',
    to_jsonb($t$<p>Что ты любишь и не любишь делать по дому? Ориентируйся на образец.</p><p>Не забудь рассказать свой текст на уроке :)</p>$t$::text))
where id = 'cc74d87c-f38d-43eb-b76a-2c06df2a23a2';

-- 2. SM1 u9 ДЗ 6 блок 10 — подводка «ты справился с большей частью задания»
--    в заголовке задания.
update classroom_blocks set payload = jsonb_set(payload, '{title}',
  to_jsonb($t$Прочитай о местах, которые я очень люблю, и заполни пропуски$t$::text))
where id = 'b6668f7e-c021-45eb-8e47-245183bc6d30';

-- 3. Удаляем швы.
delete from classroom_blocks where id in (
  '32705c8f-bcc7-4902-980f-1a1d7b50014f',  -- SM3 u3  «Это вторая часть домашней работы»
  'd3b6d284-f103-4b89-9b6e-5507b3544588',  -- SM3 u3  образец (переехал в задание)
  '5b57c164-88f8-4524-abc5-892151cd8524',  -- SM3 u6  «А теперь — вторая, вторая часть»
  '0be38b98-52d6-4397-b32e-d175b645a34d',  -- SM3 u7  то же
  '394f2e86-46a3-40a6-be53-4f1f4907ffd8',  -- SM3 u8  «Добро пожаловать в вторую часть»
  '45462107-4d76-4424-b487-bd5b3f0cb867',  -- SM3 u9  «А теперь — вторая, вторая часть»
  '66821aef-66d5-4f9a-abdd-19a22b73fb28'); -- SM1 u9 ДЗ 6 «Переходим ко второй части»

-- 4. Новый порядок. Сначала уводим номера за 1000, чтобы не спорить
--    с уникальным ключом (lesson_id, sort_order), потом расставляем.
do $$
declare
  v_order jsonb := $j$[
    ["a5508c95-938a-4289-94c8-8999eb71e3ac", 0],
    ["f6ace5d0-4805-44da-ae5f-591749d652cf", 1],
    ["8fbf0bc8-0358-4683-ba07-03197b85e6e4", 2],
    ["57e000bd-a61a-4fc5-9e48-3efda87c08e4", 3],
    ["d15aa12e-3e72-4d58-8bb5-c166e6ea658b", 4],
    ["ddce010e-667d-4d49-8455-34ec7eb30df7", 5],
    ["cc74d87c-f38d-43eb-b76a-2c06df2a23a2", 6],
    ["68a4c447-4b49-4d53-8e05-25303e606ee0", 7],

    ["a54e668a-d6e8-4148-988d-e97b84584f6f", 0],
    ["7abd382b-3ca8-465c-ae29-21ceaa044e54", 1],
    ["6f97b24d-aef8-4c21-8c38-373df6276250", 2],
    ["cf4ff094-a919-47ac-b1f3-28b4e6cb0062", 3],
    ["2f07aac9-cde9-4b5e-a866-c71cda07235e", 4],
    ["767a381f-e86b-4555-be3e-e76835eae699", 5],
    ["29778220-954a-46e9-b2f0-842d96bf70c6", 6],

    ["52fbe7c5-0f8e-4855-a301-eff7fd6447bb", 0],
    ["9822d3c2-00fd-4f91-bd68-f40957d6f8d9", 1],
    ["a6c43321-a11a-49f1-b06b-3551c55df4a9", 2],
    ["716f1454-bbdb-4b7f-b565-57226cbd1609", 3],
    ["5467285b-01eb-4d52-bfc4-c05606992ac6", 4],
    ["a6f0259f-b320-42c1-99e3-f800a6d2be1a", 5],
    ["329db879-d69c-479f-b7f3-df6115018790", 6],

    ["8bbacf31-5ede-445e-b6b4-3193c784d6b3", 0],
    ["4ca9c073-8b36-4415-a6d4-10670e2794b0", 1],
    ["bd219a90-7822-4eaf-beb9-daf924bba26f", 2],
    ["adae5409-e6bb-4ac8-89e8-e76775404df5", 3],
    ["97487a9f-2c7a-408f-aaf4-27dd3f20fd27", 4],
    ["6d5a0363-c912-407b-b980-bb1f1f880c4b", 5],
    ["9b222d1f-feb5-4e46-b457-bc7945ef9595", 6],

    ["0fc3d949-c3c0-4641-b6fb-cfa74d5ffced", 0],
    ["67012ef2-a60f-454c-a845-48e078ca9766", 1],
    ["d170708d-6e48-424c-8a62-418d8b02f254", 2],
    ["8c49d6d9-60d9-469b-9529-e34c0739e915", 3],
    ["2e201ad7-3c3d-48fe-b5d4-e7577ac5ba0a", 4],
    ["d79ce1a4-03d6-450e-ac7c-9f1216aa10cd", 5],
    ["8dd05c45-c636-42ef-af6f-0de611795a57", 6],

    ["17c8e473-5e26-4afd-b3d7-d1ff85743ea4", 0],
    ["b8c18729-b5c7-43c1-bd85-bab6be8c2842", 1],
    ["0aeb2615-71ec-4103-962a-079dace3a9a7", 2],
    ["658b8f06-c3e8-4d1d-b268-fd89fa481b7c", 3],
    ["56a7e7e8-2996-4bb1-96bd-6e3cdd8cbbee", 4],
    ["b3995fa0-9cf4-436f-adf3-b8f315da6254", 5],
    ["42b2359d-8f61-475c-8e01-1ec34b6097c9", 6],
    ["c7e4c2b2-843c-47d1-862c-83cedb1ca261", 7],
    ["b6668f7e-c021-45eb-8e47-245183bc6d30", 8],
    ["2b0f66b2-406c-4a65-83c8-730b65f2cef7", 9],
    ["2565789f-cae2-4c98-832b-01d1f2c0c734", 10],
    ["fdc01c01-d110-462d-af6a-3e822b38b778", 11]
  ]$j$::jsonb;
  v_ids uuid[];
  v_rec jsonb;
begin
  select array_agg((x->>0)::uuid) into v_ids from jsonb_array_elements(v_order) x;

  update classroom_blocks set sort_order = sort_order + 1000
  where lesson_id in (select distinct lesson_id from classroom_blocks where id = any(v_ids));

  for v_rec in select x from jsonb_array_elements(v_order) x loop
    update classroom_blocks set sort_order = (v_rec->>1)::int
    where id = (v_rec->>0)::uuid;
  end loop;

  if exists (select 1 from classroom_blocks
             where lesson_id in (select distinct lesson_id from classroom_blocks where id = any(v_ids))
               and sort_order >= 1000) then
    raise exception 'остались блоки с номером за 1000 — список неполный';
  end if;
end $$;
