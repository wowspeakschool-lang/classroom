-- Материал задания внутрь задания: проход по блокам всех типов, 04.11.2026
-- Меняется только ключ payload.material. Источник — html предыдущего материального блока того же урока.

create table if not exists classroom_backup_material_vse_20261104 as
select * from classroom_blocks where id in (
  '83e36c75-7cce-4208-a7d5-61a2e73e688c',
  '72147651-f8a2-485b-b0e9-faceef2331a2',
  'e5b100e9-5ba1-4a0a-95df-0bb417129b3a',
  '75941764-06dc-4b3d-b15d-9189e1761ca8',
  '4e7d7a54-216f-4d77-b3ea-dae3c3aef111',
  '9512dab5-16d5-495a-a6fd-9ec9791246a6',
  '25c1d87f-81ba-4090-86f5-9f0c1c84ff91',
  '2a225617-4397-4573-a166-8c639fa31c8f',
  '6b9f33fb-6b5f-46b3-9fb7-8761e4fb8f37',
  'c981593f-4421-4786-8954-f4889168701c',
  '5b011750-3470-44fd-ac7b-ec52a2b0f93c',
  'ae4f387e-be5d-470a-92c8-a75ce48fabd6',
  '3e9af7db-23e3-455c-bd21-ea06f9c4670c',
  '48820217-74df-404e-9916-b783629bbcce',
  'a83c243d-00d8-4925-9bd1-3570502c00ab',
  'f45ef035-de71-4a0a-b016-cc7f7c454a00',
  'b4ebed26-1e41-4354-b58e-d51f3794788e',
  'e2d9c05e-0e1a-4f83-990e-3b6bdab773a8',
  '763ffeca-debb-49ab-ba36-91db1baa7ac4',
  '73b235c2-2929-4568-b9da-ac50b3b6bc5e',
  'b10a2f62-c87e-4ffd-9b2b-c438d9968f11',
  '3d96483e-7d64-46a1-b07e-b78c1fb7fe6a',
  '83b61db1-3ed6-490b-b6fc-1aa8400b3356',
  '079b71d9-0e35-4a02-a5e9-f1207c5e6116',
  '62cb3b52-3221-4d6a-bd6b-0bbbd55f9e01',
  '15a3c65b-69be-4950-a221-401c3cda1616',
  '37df47ff-8c54-4113-9484-c5d439a84339',
  '7e8161a3-d9a5-4683-9502-9c77d6070f7e',
  'fc48cb79-485d-415f-ad85-a2019ba86631',
  'd4eaaafe-1c48-49e4-a00b-43fce3464b66',
  '5b2a0ce8-9a4a-4571-a0a6-36be3290abe9',
  '1130e78b-8e19-4faf-ab0a-3f8a4b706787',
  '11ee89a2-5560-4d56-96cf-07a9dcdcf503',
  '7c2731b2-1f36-43b1-90a9-f4bc4e17c6ae',
  '0a304a86-28c2-4e41-ac62-5ef3547f235e',
  'ee08da8a-26bb-4eeb-bd73-6dceca2398c6',
  '16c8f1b7-10b9-4d1a-b36f-88ee3f1e4c59',
  '066732ac-7787-439f-95b1-d06d5ab27b3e',
  '7e52ce3c-4ce1-4331-a18c-103ac27c67cf',
  '5bcbf8c6-4bd9-4402-8ccd-6f7a42b09499',
  '76f10c10-704a-4d98-908c-e77fe7ea0129',
  'c694f0ac-e801-40ea-8220-5f693e189d95',
  '79f9b851-9632-4931-b11c-bebe4b58eee8',
  '0ce8d4e2-7c6c-40ba-9af5-f71fd3863628',
  '3e65a820-cf6c-4592-80a6-68cc204b0a51',
  'e669c60b-aedb-4367-877a-b7afdcff3789',
  '65e1e464-2291-4507-abd4-073da1902a56',
  '966b9b5e-619a-4070-a374-0a19246ae8a3',
  '906e9e59-f5ed-4758-b593-953919a23b2c',
  'f4192ceb-2b46-47ec-8e96-c8f9aa6ef9b5',
  'b7cdf11c-be9b-4498-b268-07aeb8730979',
  '268806a8-c65b-46fa-936f-2adb7fc01e4b',
  '0cc6c5ef-fd87-4160-b8ab-5aea16c20faf',
  '494edef8-9a59-4a01-aabb-9c1cb958b393',
  '667d8af1-2f6f-498f-b3b2-dd8d0140d94e',
  'f34865cf-07ae-47e2-9d5b-70b7767d56b9',
  '7120c566-0a48-4620-927d-855e790c77bc',
  'f38a3f74-3748-4c06-b6b2-3903dffe7598',
  '38f1ebf6-c76f-4ec2-9a04-4ffb113d6926',
  'dbc88a75-1900-4732-b2a4-e0b0e7932e17',
  'e6f41458-7d55-4742-9673-7b8e082306bb',
  'd2ca34df-59e6-46fc-a6f2-fe27228a73f8',
  '33019a89-806e-4fa8-b142-362ad4924a96',
  'a13ae889-e24f-434e-8964-efa1ae3290ab',
  '80a393b9-8866-4ce6-b285-da46053b2cf0',
  'a83c2522-5b32-45f6-b9d4-2e0207637fb7',
  'a3657565-1ac4-401d-bd32-8928fc59943c',
  '093d02a5-bbb4-4008-8fb0-47a18395b923',
  '6e32e32f-9db8-466e-a447-02c7613a1f38',
  'a838a51c-61e8-4774-b48c-64e0554f44b4',
  'bf5b266c-3479-43de-88c8-4f2dbcc2a938',
  'fc74792c-94bd-431a-9b9e-fd04a22a9598',
  '4a858f82-9fef-44eb-989a-b71cd11e56ca',
  '466ec59b-4fad-4bae-911c-11f5686cffb1',
  '63558b2f-0840-4cc5-97d8-364a64610046',
  '093d20fc-0107-4523-a1f1-9fe440e239c0',
  '027118c9-9638-498f-8e88-85d9e7b441f2',
  'd1343e7e-7f0c-4f27-a59d-8f5de7595034',
  'b4faa2f2-c629-4267-b94a-1485d43fab26',
  '4ed33fbe-5b1f-4abe-83d8-1106df7614d1',
  '342680e2-2d7a-4a2f-85fb-8bc20246178c',
  'b664a53e-26a3-4b70-a508-740cf874b396',
  '80f4851c-943d-4082-8413-dc5f03a98261',
  '24f27c0d-8b25-40ff-a843-ae0c5a93036f',
  '397ca59e-666a-4e51-a5f7-67afb734c9e2',
  '7a252517-d82d-4e7d-b65b-53c15e38a846',
  'd5ca59fc-a90c-44a7-9e34-bd979b4ade18',
  'd17712e1-4be3-443e-ba2f-293829a55f2e',
  '75d05057-a871-4c49-a521-caaec91ce437',
  'cea4eecd-2a4d-4fa6-9277-8cb6e3242a3f',
  'fe0e7473-7ed2-4103-a720-2fcd0226ec8d',
  'd216ade7-f6ea-449e-b1ce-68ff596337ea',
  'fc316941-dd5c-4f42-bb05-48d0aff8781b',
  'efb8de58-a9b6-4145-9370-6205e07a707b',
  'ad483430-1d1b-46db-948b-06e4ab73fb18',
  '2d425371-9d29-4c6b-a669-7ab2430f8c55',
  '0af5f0b2-f90b-4d12-9447-382cf16cea59',
  'b986ef9d-a3d9-4ae3-8863-6db158897bcd',
  '2f8c2e26-0aaa-4081-9e8b-1103014f73e9',
  'e8890603-de98-4a67-8902-743345587467',
  'ce891d77-b6b9-4963-9d53-48fe2b78d7e5',
  'afb8dbdb-745f-467a-bcb4-ee17a467f541',
  '703f5bbf-018c-4f94-a573-b0149e2b4b8f',
  '40c68cf3-7156-455f-874e-19b223c49aff',
  '60b1ee92-37c0-4f1d-a985-ce48ab03d146',
  'c4b15d41-798c-4f57-9174-ca98c74021e2',
  'd6b54ac9-1371-478c-8d3d-6dbc587ccaab',
  'cc74d87c-f38d-43eb-b76a-2c06df2a23a2',
  '2b6bfc09-5b4d-4ad2-b1c7-bd02cd97cb8b',
  '7c325f6f-9692-4c59-a196-280b4fc7678e',
  '6cec72b1-00f7-49f7-8863-e302ceac26fd',
  'fc909a22-25bc-4aa0-8aad-66d9d5677a82',
  'ceb28a38-597e-45bf-9ab7-f3c5a7532817',
  'e698b30b-be13-4c96-8e8b-1f0c564e00ba',
  'd9c5ad96-2a25-4ef0-999e-f4d8916e669e',
  '0a28f90b-4549-4c99-8ac4-bdf2083c01ad',
  'e2699347-1a80-4c87-84bc-df878d10a1fd',
  '11c88d89-f3a7-4ce0-9791-381a079d1249',
  '707637f6-bac3-49dc-978a-b2a6007d9991',
  '024aa1a1-23f7-45bb-b8ee-5e6595af9bfb',
  '2a4184cd-5aa8-46c6-a5be-b20c8ddb2d95',
  '38e54ced-2eb7-46b4-be72-f76f0d9e437a',
  '51f34c7a-1338-48a9-90da-5629db5af77a',
  '7a90b07d-c1f5-4735-b54d-31927cdcc758',
  '7d8e9ac9-79f0-4c9f-9c57-92478a13c86a',
  '12cecc0a-1122-479e-92cc-633b344c9419',
  'b36294ae-fad1-4e1a-a95b-3b5dfad4eadb',
  'a2dbf67c-3244-4dcb-a8d4-3ab0d435a4af',
  '7bf73e40-9845-42fc-9217-3657a654f159',
  '1f0b700e-1869-45de-a3b9-b223bc93a8a0'
);

-- gg1 u0 · Homework 2 · блок 6 (match) <- блок [5]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (4))))
  where t.id = '83e36c75-7cce-4208-a7d5-61a2e73e688c' and not (t.payload ? 'material');

-- gg1 u0 · Unit 0 Test · блок 10 (match) <- блок [9]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (8))))
  where t.id = '72147651-f8a2-485b-b0e9-faceef2331a2' and not (t.payload ? 'material');

-- gg1 u1 · Homework 5 · блок 6 (gaps) <- блок [4]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (3))))
  where t.id = 'e5b100e9-5ba1-4a0a-95df-0bb417129b3a' and not (t.payload ? 'material');

-- gg1 u1 · Homework 6 · блок 5 (quiz) <- блок [4]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (3))))
  where t.id = '75941764-06dc-4b3d-b15d-9189e1761ca8' and not (t.payload ? 'material');

-- gg1 u1 · Unit 1 Test · блок 14 (quiz) <- блок [13]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (12))))
  where t.id = '4e7d7a54-216f-4d77-b3ea-dae3c3aef111' and not (t.payload ? 'material');

-- gg1 u2 · Homework 4 · блок 9 (gaps) <- блок [8]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (7))))
  where t.id = '9512dab5-16d5-495a-a6fd-9ec9791246a6' and not (t.payload ? 'material');

-- gg1 u2 · Homework 5 · блок 7 (quiz) <- блок [6]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (5))))
  where t.id = '25c1d87f-81ba-4090-86f5-9f0c1c84ff91' and not (t.payload ? 'material');

-- gg1 u2 · Homework 6 · блок 6 (quiz) <- блок [5]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (4))))
  where t.id = '2a225617-4397-4573-a166-8c639fa31c8f' and not (t.payload ? 'material');

-- gg1 u3 · Unit 3 Test · блок 11 (truefalse) <- блок [10]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (9))))
  where t.id = '6b9f33fb-6b5f-46b3-9fb7-8761e4fb8f37' and not (t.payload ? 'material');

-- gg1 u4 · Homework 5 · блок 9 (sort) <- блок [7]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (6))))
  where t.id = 'c981593f-4421-4786-8954-f4889168701c' and not (t.payload ? 'material');

-- gg1 u4 · Homework 5 · блок 10 (gaps) <- блок [7]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (6))))
  where t.id = '5b011750-3470-44fd-ac7b-ec52a2b0f93c' and not (t.payload ? 'material');

-- gg1 u4 · Homework 6 · блок 9 (task) <- блок [8]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (7))))
  where t.id = 'ae4f387e-be5d-470a-92c8-a75ce48fabd6' and not (t.payload ? 'material');

-- gg1 u5 · Homework 5 · блок 5 (quiz) <- блок [4]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (3))))
  where t.id = '3e9af7db-23e3-455c-bd21-ea06f9c4670c' and not (t.payload ? 'material');

-- gg1 u5 · Homework 5 · блок 6 (quiz) <- блок [4]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (3))))
  where t.id = '48820217-74df-404e-9916-b783629bbcce' and not (t.payload ? 'material');

-- gg1 u5 · Homework 5 · блок 7 (match) <- блок [4]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (3))))
  where t.id = 'a83c243d-00d8-4925-9bd1-3570502c00ab' and not (t.payload ? 'material');

-- gg1 u6 · Homework 5 · блок 5 (truefalse) <- блок [3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (2))))
  where t.id = 'f45ef035-de71-4a0a-b016-cc7f7c454a00' and not (t.payload ? 'material');

-- gg1 u6 · Homework 5 · блок 6 (quiz) <- блок [3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (2))))
  where t.id = 'b4ebed26-1e41-4354-b58e-d51f3794788e' and not (t.payload ? 'material');

-- gg1 u6 · Homework 5 · блок 7 (gaps) <- блок [3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (2))))
  where t.id = 'e2d9c05e-0e1a-4f83-990e-3b6bdab773a8' and not (t.payload ? 'material');

-- gg1 u6 · Homework 6 · блок 10 (task) <- блоки [4, 5]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (3,4))))
  where t.id = '763ffeca-debb-49ab-ba36-91db1baa7ac4' and not (t.payload ? 'material');

-- gg1 u7 · Homework 5 · блок 9 (quiz) <- блок [8]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (7))))
  where t.id = '73b235c2-2929-4568-b9da-ac50b3b6bc5e' and not (t.payload ? 'material');

-- gg1 u7 · Homework 5 · блок 10 (task) <- блок [8]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (7))))
  where t.id = 'b10a2f62-c87e-4ffd-9b2b-c438d9968f11' and not (t.payload ? 'material');

-- gg1 u7 · Homework 6 · блок 6 (quiz) <- блок [5]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (4))))
  where t.id = '3d96483e-7d64-46a1-b07e-b78c1fb7fe6a' and not (t.payload ? 'material');

-- gg1 u7 · Unit 7 Test · блок 14 (quiz) <- блок [13]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (12))))
  where t.id = '83b61db1-3ed6-490b-b6fc-1aa8400b3356' and not (t.payload ? 'material');

-- gg1 u8 · Homework 5 · блок 4 (quiz) <- блок [3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (2))))
  where t.id = '079b71d9-0e35-4a02-a5e9-f1207c5e6116' and not (t.payload ? 'material');

-- gg1 u8 · Homework 5 · блок 5 (gaps) <- блок [3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (2))))
  where t.id = '62cb3b52-3221-4d6a-bd6b-0bbbd55f9e01' and not (t.payload ? 'material');

-- gg2 u0 · Unit 0 Test · блок 11 (quiz) <- блок [10]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (9))))
  where t.id = '15a3c65b-69be-4950-a221-401c3cda1616' and not (t.payload ? 'material');

-- gg2 u1 · Homework 1 · блок 12 (quiz) <- блок [11]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (10))))
  where t.id = '37df47ff-8c54-4113-9484-c5d439a84339' and not (t.payload ? 'material');

-- gg2 u1 · Homework 5 · блок 8 (quiz) <- блок [6]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (5))))
  where t.id = '7e8161a3-d9a5-4683-9502-9c77d6070f7e' and not (t.payload ? 'material');

-- gg2 u1 · Homework 5 · блок 9 (task) <- блок [6]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (5))))
  where t.id = 'fc48cb79-485d-415f-ad85-a2019ba86631' and not (t.payload ? 'material');

-- gg2 u1 · Unit 1 Test · блок 11 (quiz) <- блок [10]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (9))))
  where t.id = 'd4eaaafe-1c48-49e4-a00b-43fce3464b66' and not (t.payload ? 'material');

-- gg2 u2 · Homework 5 · блок 5 (sort) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = '5b2a0ce8-9a4a-4571-a0a6-36be3290abe9' and not (t.payload ? 'material');

-- gg2 u3 · Homework 5 · блок 3 (speaking) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = '1130e78b-8e19-4faf-ab0a-3f8a4b706787' and not (t.payload ? 'material');

-- gg2 u3 · Homework 5 · блок 5 (task) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = '11ee89a2-5560-4d56-96cf-07a9dcdcf503' and not (t.payload ? 'material');

-- gg2 u3 · Homework 5 · блок 9 (task) <- блок [8]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (7))))
  where t.id = '7c2731b2-1f36-43b1-90a9-f4bc4e17c6ae' and not (t.payload ? 'material');

-- gg2 u3 · Homework 5 · блок 10 (task) <- блок [8]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (7))))
  where t.id = '0a304a86-28c2-4e41-ac62-5ef3547f235e' and not (t.payload ? 'material');

-- gg2 u3 · Unit 3 Test · блок 11 (quiz) <- блок [10]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (9))))
  where t.id = 'ee08da8a-26bb-4eeb-bd73-6dceca2398c6' and not (t.payload ? 'material');

-- gg2 u4 · Homework 5 · блок 15 (gaps) <- блок [14]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (13))))
  where t.id = '16c8f1b7-10b9-4d1a-b36f-88ee3f1e4c59' and not (t.payload ? 'material');

-- gg2 u4 · Homework 6 · блок 3 (quiz) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = '066732ac-7787-439f-95b1-d06d5ab27b3e' and not (t.payload ? 'material');

-- gg2 u4 · Homework 6 · блок 4 (gaps) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = '7e52ce3c-4ce1-4331-a18c-103ac27c67cf' and not (t.payload ? 'material');

-- gg2 u4 · Homework 6 · блок 6 (task) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = '5bcbf8c6-4bd9-4402-8ccd-6f7a42b09499' and not (t.payload ? 'material');

-- gg2 u4 · Unit 4 Test · блок 11 (gaps) <- блок [10]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (9))))
  where t.id = '76f10c10-704a-4d98-908c-e77fe7ea0129' and not (t.payload ? 'material');

-- gg2 u5 · Homework 6 · блок 4 (quiz) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = 'c694f0ac-e801-40ea-8220-5f693e189d95' and not (t.payload ? 'material');

-- gg2 u5 · Homework 6 · блок 5 (sort) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = '79f9b851-9632-4931-b11c-bebe4b58eee8' and not (t.payload ? 'material');

-- gg2 u5 · Homework 6 · блок 6 (gaps) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = '0ce8d4e2-7c6c-40ba-9af5-f71fd3863628' and not (t.payload ? 'material');

-- gg2 u5 · Unit 5 Test · блок 11 (quiz) <- блок [10]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (9))))
  where t.id = '3e65a820-cf6c-4592-80a6-68cc204b0a51' and not (t.payload ? 'material');

-- gg2 u6 · Homework 5 · блок 9 (gaps) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = 'e669c60b-aedb-4367-877a-b7afdcff3789' and not (t.payload ? 'material');

-- gg2 u6 · Homework 6 · блок 3 (quiz) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = '65e1e464-2291-4507-abd4-073da1902a56' and not (t.payload ? 'material');

-- gg2 u6 · Homework 6 · блок 4 (quiz) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = '966b9b5e-619a-4070-a374-0a19246ae8a3' and not (t.payload ? 'material');

-- gg2 u6 · Homework 6 · блок 5 (truefalse) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = '906e9e59-f5ed-4758-b593-953919a23b2c' and not (t.payload ? 'material');

-- gg2 u6 · Homework 6 · блок 6 (sort) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = 'f4192ceb-2b46-47ec-8e96-c8f9aa6ef9b5' and not (t.payload ? 'material');

-- gg2 u6 · Homework 6 · блок 7 (gaps) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = 'b7cdf11c-be9b-4498-b268-07aeb8730979' and not (t.payload ? 'material');

-- gg2 u6 · Unit 6 Test · блок 11 (quiz) <- блок [10]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (9))))
  where t.id = '268806a8-c65b-46fa-936f-2adb7fc01e4b' and not (t.payload ? 'material');

-- gg2 u7 · Homework 3 · блок 4 (truefalse) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = '0cc6c5ef-fd87-4160-b8ab-5aea16c20faf' and not (t.payload ? 'material');

-- gg2 u7 · Homework 5 · блок 10 (gaps) <- блок [9]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (8))))
  where t.id = '494edef8-9a59-4a01-aabb-9c1cb958b393' and not (t.payload ? 'material');

-- gg2 u7 · Homework 6 · блок 5 (sort) <- блок [3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (2))))
  where t.id = '667d8af1-2f6f-498f-b3b2-dd8d0140d94e' and not (t.payload ? 'material');

-- gg2 u7 · Homework 6 · блок 8 (gaps) <- блок [3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (2))))
  where t.id = 'f34865cf-07ae-47e2-9d5b-70b7767d56b9' and not (t.payload ? 'material');

-- gg2 u7 · Homework 6 · блок 10 (task) <- блок [3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (2))))
  where t.id = '7120c566-0a48-4620-927d-855e790c77bc' and not (t.payload ? 'material');

-- gg2 u8 · Homework 6 · блок 6 (sort) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = 'f38a3f74-3748-4c06-b6b2-3903dffe7598' and not (t.payload ? 'material');

-- gg2 u8 · Homework 6 · блок 7 (gaps) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = '38f1ebf6-c76f-4ec2-9a04-4ffb113d6926' and not (t.payload ? 'material');

-- gg2 u8 · Unit 8 Test · блок 11 (gaps) <- блок [10]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (9))))
  where t.id = 'dbc88a75-1900-4732-b2a4-e0b0e7932e17' and not (t.payload ? 'material');

-- gg2 u9 · Final Test · блок 6 (quiz) <- блок [5]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (4))))
  where t.id = 'e6f41458-7d55-4742-9673-7b8e082306bb' and not (t.payload ? 'material');

-- sm1 u3 · Homework 5 · блок 6 (quiz) <- блок [5]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (4))))
  where t.id = 'd2ca34df-59e6-46fc-a6f2-fe27228a73f8' and not (t.payload ? 'material');

-- sm1 u4 · Homework 3 · блок 13 (speaking) <- блок [3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (2))))
  where t.id = '33019a89-806e-4fa8-b142-362ad4924a96' and not (t.payload ? 'material');

-- sm1 u4 · Homework 3 · блок 14 (speaking) <- блок [3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (2))))
  where t.id = 'a13ae889-e24f-434e-8964-efa1ae3290ab' and not (t.payload ? 'material');

-- sm1 u4 · Homework 5 · блок 14 (truefalse) <- блок [13]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (12))))
  where t.id = '80a393b9-8866-4ce6-b285-da46053b2cf0' and not (t.payload ? 'material');

-- sm1 u4 · Unit 4 Test · блок 12 (truefalse) <- блок [11]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (10))))
  where t.id = 'a83c2522-5b32-45f6-b9d4-2e0207637fb7' and not (t.payload ? 'material');

-- sm1 u5 · Unit 5 Test · блок 10 (match) <- блок [9]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (8))))
  where t.id = 'a3657565-1ac4-401d-bd32-8928fc59943c' and not (t.payload ? 'material');

-- sm1 u6 · Homework 4 · блок 10 (truefalse) <- блок [6]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (5))))
  where t.id = '093d02a5-bbb4-4008-8fb0-47a18395b923' and not (t.payload ? 'material');

-- sm1 u6 · Homework 4 · блок 11 (quiz) <- блок [6]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (5))))
  where t.id = '6e32e32f-9db8-466e-a447-02c7613a1f38' and not (t.payload ? 'material');

-- sm1 u6 · Homework 4 · блок 12 (speaking) <- блок [6]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (5))))
  where t.id = 'a838a51c-61e8-4774-b48c-64e0554f44b4' and not (t.payload ? 'material');

-- sm1 u7 · Homework 4 · блок 6 (sequence) <- блок [5]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (4))))
  where t.id = 'bf5b266c-3479-43de-88c8-4f2dbcc2a938' and not (t.payload ? 'material');

-- sm1 u7 · Homework 4 · блок 7 (quiz) <- блок [5]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (4))))
  where t.id = 'fc74792c-94bd-431a-9b9e-fd04a22a9598' and not (t.payload ? 'material');

-- sm1 u7 · Unit 7 Test · блок 12 (quiz) <- блок [11]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (10))))
  where t.id = '4a858f82-9fef-44eb-989a-b71cd11e56ca' and not (t.payload ? 'material');

-- sm1 u8 · Homework 5 · блок 12 (match) <- блок [10]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (9))))
  where t.id = '466ec59b-4fad-4bae-911c-11f5686cffb1' and not (t.payload ? 'material');

-- sm1 u8 · Homework 5 · блок 13 (gaps) <- блок [10]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (9))))
  where t.id = '63558b2f-0840-4cc5-97d8-364a64610046' and not (t.payload ? 'material');

-- sm1 u8 · Unit 8 Test · блок 10 (quiz) <- блок [9]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (8))))
  where t.id = '093d20fc-0107-4523-a1f1-9fe440e239c0' and not (t.payload ? 'material');

-- sm1 u9 · Homework 5 · блок 12 (quiz) <- блок [11]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (10))))
  where t.id = '027118c9-9638-498f-8e88-85d9e7b441f2' and not (t.payload ? 'material');

-- sm1 u9 · Unit 9 Test · блок 12 (gaps) <- блок [11]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (10))))
  where t.id = 'd1343e7e-7f0c-4f27-a59d-8f5de7595034' and not (t.payload ? 'material');

-- sm2 u0 · Unit 0 Test · блок 6 (truefalse) <- блок [5]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (4))))
  where t.id = 'b4faa2f2-c629-4267-b94a-1485d43fab26' and not (t.payload ? 'material');

-- sm2 u1 · Homework 2 · блок 18 (speaking) <- блок [17]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (16))))
  where t.id = '4ed33fbe-5b1f-4abe-83d8-1106df7614d1' and not (t.payload ? 'material');

-- sm2 u1 · Homework 4 · блок 11 (speaking) <- блок [5]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (4))))
  where t.id = '342680e2-2d7a-4a2f-85fb-8bc20246178c' and not (t.payload ? 'material');

-- sm2 u1 · Homework 5 · блок 10 (quiz) <- блок [9]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (8))))
  where t.id = 'b664a53e-26a3-4b70-a508-740cf874b396' and not (t.payload ? 'material');

-- sm2 u1 · Unit 1 Test · блок 13 (match) <- блок [12]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (11))))
  where t.id = '80f4851c-943d-4082-8413-dc5f03a98261' and not (t.payload ? 'material');

-- sm2 u2 · Homework 4 · блок 7 (quiz) <- блок [6]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (5))))
  where t.id = '24f27c0d-8b25-40ff-a843-ae0c5a93036f' and not (t.payload ? 'material');

-- sm2 u2 · Homework 4 · блок 12 (truefalse) <- блок [6]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (5))))
  where t.id = '397ca59e-666a-4e51-a5f7-67afb734c9e2' and not (t.payload ? 'material');

-- sm2 u2 · Unit 2 Test · блок 17 (quiz) <- блок [16]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (15))))
  where t.id = '7a252517-d82d-4e7d-b65b-53c15e38a846' and not (t.payload ? 'material');

-- sm2 u3 · Homework 4 · блок 12 (speaking) <- блок [4]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (3))))
  where t.id = 'd5ca59fc-a90c-44a7-9e34-bd979b4ade18' and not (t.payload ? 'material');

-- sm2 u3 · Homework 5 · блок 7 (task) <- блок [3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (2))))
  where t.id = 'd17712e1-4be3-443e-ba2f-293829a55f2e' and not (t.payload ? 'material');

-- sm2 u4 · Homework 4 · блок 7 (match) <- блок [5]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (4))))
  where t.id = '75d05057-a871-4c49-a521-caaec91ce437' and not (t.payload ? 'material');

-- sm2 u4 · Homework 4 · блок 8 (truefalse) <- блок [5]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (4))))
  where t.id = 'cea4eecd-2a4d-4fa6-9277-8cb6e3242a3f' and not (t.payload ? 'material');

-- sm2 u4 · Homework 4 · блок 12 (speaking) <- блок [5]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (4))))
  where t.id = 'fe0e7473-7ed2-4103-a720-2fcd0226ec8d' and not (t.payload ? 'material');

-- sm2 u4 · Homework 5 · блок 8 (quiz) <- блок [6]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (5))))
  where t.id = 'd216ade7-f6ea-449e-b1ce-68ff596337ea' and not (t.payload ? 'material');

-- sm2 u5 · Homework 4 · блок 6 (quiz) <- блок [5]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (4))))
  where t.id = 'fc316941-dd5c-4f42-bb05-48d0aff8781b' and not (t.payload ? 'material');

-- sm2 u5 · Homework 4 · блок 7 (match) <- блок [5]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (4))))
  where t.id = 'efb8de58-a9b6-4145-9370-6205e07a707b' and not (t.payload ? 'material');

-- sm2 u6 · Homework 4 · блок 6 (truefalse) <- блок [4]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (3))))
  where t.id = 'ad483430-1d1b-46db-948b-06e4ab73fb18' and not (t.payload ? 'material');

-- sm2 u6 · Homework 4 · блок 8 (gaps) <- блок [4]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (3))))
  where t.id = '2d425371-9d29-4c6b-a669-7ab2430f8c55' and not (t.payload ? 'material');

-- sm2 u6 · Unit 6 Test · блок 11 (quiz) <- блок [10]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (9))))
  where t.id = '0af5f0b2-f90b-4d12-9447-382cf16cea59' and not (t.payload ? 'material');

-- sm2 u7 · Homework 4 · блок 5 (quiz) <- блок [4]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (3))))
  where t.id = 'b986ef9d-a3d9-4ae3-8863-6db158897bcd' and not (t.payload ? 'material');

-- sm2 u7 · Homework 4 · блок 6 (match) <- блок [4]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (3))))
  where t.id = '2f8c2e26-0aaa-4081-9e8b-1103014f73e9' and not (t.payload ? 'material');

-- sm2 u7 · Homework 4 · блок 7 (truefalse) <- блок [4]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (3))))
  where t.id = 'e8890603-de98-4a67-8902-743345587467' and not (t.payload ? 'material');

-- sm2 u7 · Homework 5 · блок 4 (truefalse) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = 'ce891d77-b6b9-4963-9d53-48fe2b78d7e5' and not (t.payload ? 'material');

-- sm2 u7 · Homework 5 · блок 5 (gaps) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = 'afb8dbdb-745f-467a-bcb4-ee17a467f541' and not (t.payload ? 'material');

-- sm2 u8 · Homework 4 · блок 5 (truefalse) <- блок [3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (2))))
  where t.id = '703f5bbf-018c-4f94-a573-b0149e2b4b8f' and not (t.payload ? 'material');

-- sm2 u8 · Homework 4 · блок 10 (speaking) <- блок [3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (2))))
  where t.id = '40c68cf3-7156-455f-874e-19b223c49aff' and not (t.payload ? 'material');

-- sm2 u9 · Homework 5 · блок 5 (exact_input) <- блок [4]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (3))))
  where t.id = '60b1ee92-37c0-4f1d-a985-ce48ab03d146' and not (t.payload ? 'material');

-- sm3 u1 · Homework 6 · блок 3 (gaps) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = 'c4b15d41-798c-4f57-9174-ca98c74021e2' and not (t.payload ? 'material');

-- sm3 u1 · Homework 6 · блок 4 (truefalse) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = 'd6b54ac9-1371-478c-8d3d-6dbc587ccaab' and not (t.payload ? 'material');

-- sm3 u3 · Homework 1 · блок 9 (task) <- блок [8]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (7))))
  where t.id = 'cc74d87c-f38d-43eb-b76a-2c06df2a23a2' and not (t.payload ? 'material');

-- sm3 u3 · Homework 7 · блок 8 (task) <- блок [7]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (6))))
  where t.id = '2b6bfc09-5b4d-4ad2-b1c7-bd02cd97cb8b' and not (t.payload ? 'material');

-- sm3 u4 · Homework 7 · блок 5 (task) <- блок [4]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (3))))
  where t.id = '7c325f6f-9692-4c59-a196-280b4fc7678e' and not (t.payload ? 'material');

-- sm3 u5 · Homework 8 · блок 3 (quiz) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = '6cec72b1-00f7-49f7-8863-e302ceac26fd' and not (t.payload ? 'material');

-- sm3 u5 · Homework 8 · блок 4 (quiz) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = 'fc909a22-25bc-4aa0-8aad-66d9d5677a82' and not (t.payload ? 'material');

-- sm3 u5 · Homework 8 · блок 5 (quiz) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = 'ceb28a38-597e-45bf-9ab7-f3c5a7532817' and not (t.payload ? 'material');

-- sm3 u5 · Homework 8 · блок 6 (quiz) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = 'e698b30b-be13-4c96-8e8b-1f0c564e00ba' and not (t.payload ? 'material');

-- sm3 u5 · Homework 8 · блок 7 (quiz) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = 'd9c5ad96-2a25-4ef0-999e-f4d8916e669e' and not (t.payload ? 'material');

-- sm3 u7 · Homework 6 · блок 4 (sequence) <- блоки [2, 3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1,2))))
  where t.id = '0a28f90b-4549-4c99-8ac4-bdf2083c01ad' and not (t.payload ? 'material');

-- sm3 u7 · Homework 6 · блок 5 (gaps) <- блоки [2, 3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1,2))))
  where t.id = 'e2699347-1a80-4c87-84bc-df878d10a1fd' and not (t.payload ? 'material');

-- sm3 u7 · Homework 6 · блок 6 (gaps) <- блоки [2, 3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1,2))))
  where t.id = '11c88d89-f3a7-4ce0-9791-381a079d1249' and not (t.payload ? 'material');

-- sm3 u8 · Homework 5 · блок 7 (quiz) <- блок [6]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (5))))
  where t.id = '707637f6-bac3-49dc-978a-b2a6007d9991' and not (t.payload ? 'material');

-- sm3 u8 · Homework 6 · блок 3 (gaps) <- блок [2]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1))))
  where t.id = '024aa1a1-23f7-45bb-b8ee-5e6595af9bfb' and not (t.payload ? 'material');

-- sm3 u9 · Homework 6 · блок 4 (sequence) <- блоки [2, 3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1,2))))
  where t.id = '2a4184cd-5aa8-46c6-a5be-b20c8ddb2d95' and not (t.payload ? 'material');

-- sm3 u9 · Homework 6 · блок 5 (gaps) <- блоки [2, 3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1,2))))
  where t.id = '38e54ced-2eb7-46b4-be72-f76f0d9e437a' and not (t.payload ? 'material');

-- sm3 u9 · Homework 6 · блок 6 (gaps) <- блоки [2, 3]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (1,2))))
  where t.id = '51f34c7a-1338-48a9-90da-5629db5af77a' and not (t.payload ? 'material');

-- sm3 u10 · Final Test · блок 10 (gaps) <- блок [9]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (8))))
  where t.id = '7a90b07d-c1f5-4735-b54d-31927cdcc758' and not (t.payload ? 'material');

-- wow-dragon-2 u100 · Homework 18 · блок 11 (sequence) <- блок [10]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (9))))
  where t.id = '7d8e9ac9-79f0-4c9f-9c57-92478a13c86a' and not (t.payload ? 'material');

-- wow-dragon-2 u200 · Homework 42 · блок 8 (sequence) <- блок [7]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (6))))
  where t.id = '12cecc0a-1122-479e-92cc-633b344c9419' and not (t.payload ? 'material');

-- wow-dragon-2 u300 · Homework 59 · блок 9 (sequence) <- блок [8]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (7))))
  where t.id = 'b36294ae-fad1-4e1a-a95b-3b5dfad4eadb' and not (t.payload ? 'material');

-- wow-dragon-2 u300 · Homework 75 · блок 8 (sequence) <- блок [6]
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb((
  select string_agg(s.payload->>'html', '' order by s.sort_order) from classroom_blocks s
  where s.lesson_id = t.lesson_id and s.sort_order in (5))))
  where t.id = 'a2dbf67c-3244-4dcb-a8d4-3ab0d435a4af' and not (t.payload ? 'material');

-- sm2 u2 · Homework 5 · блок 6 (quiz) <- блоки текст о зебре (собран из блоков 4 и 5)
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb($mat$<p><img src="https://classroom.wowteach.ru/media/sm2/u2/zebra_drawing.webp" alt="" style="height:220px"></p><p style="text-align:center"><b>a zebra</b></p><p>I've got four legs, two ears, two eyes and lots of black and white stripes. I come from Africa, but now I live in a zoo. I like carrots and grass. I don't like bananas. I drink water. I've got lots of friends here. My best friend is Charlie. He's a monkey.</p>$mat$::text))
  where t.id = '7bf73e40-9845-42fc-9217-3657a654f159' and not (t.payload ? 'material');

-- sm2 u2 · Homework 5 · блок 7 (truefalse) <- блоки текст о зебре (собран из блоков 4 и 5)
update classroom_blocks t set payload = jsonb_set(t.payload, '{material}', to_jsonb($mat$<p><img src="https://classroom.wowteach.ru/media/sm2/u2/zebra_drawing.webp" alt="" style="height:220px"></p><p style="text-align:center"><b>a zebra</b></p><p>I've got four legs, two ears, two eyes and lots of black and white stripes. I come from Africa, but now I live in a zoo. I like carrots and grass. I don't like bananas. I drink water. I've got lots of friends here. My best friend is Charlie. He's a monkey.</p>$mat$::text))
  where t.id = '1f0b700e-1869-45de-a3b9-b223bc93a8a0' and not (t.payload ? 'material');
