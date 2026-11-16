-- Образцы там, где их не было совсем (решение Анны 12.11.2026). Тесты не трогаем.
create table if not exists classroom_backup_obrazcy_net_20261112 as
select * from classroom_blocks where id in ('41c3cb51-20ee-450c-a832-2545039e6cbc'::uuid, 'f7441bce-1eaf-4b11-8d3d-e89198f0fa01'::uuid, '56f37a23-6e0d-4dc1-891b-42448ff5c4cf'::uuid, 'f2bc369a-f1b7-474f-a596-dab054663715'::uuid, '23642479-71af-4c3a-aadb-c63abb32e552'::uuid, '8478e7cc-5581-4590-9d44-0ca07a3969a4'::uuid, 'e1175113-e7b7-407f-b15b-47f650613899'::uuid, '5f7da51e-8b2a-40f3-b9d4-6040866e1b2d'::uuid, '460cdb4a-2f78-4c99-8954-4d431af391e6'::uuid, '408e8e5a-7362-4a31-933f-1b34c48918c9'::uuid, '73666aea-a527-4d73-bd84-0777ef1a6bf6'::uuid, 'ce10a8e2-d829-446d-a560-2bbde8168b8b'::uuid, 'a511cc8c-bffa-49c9-acbe-0b63bef8b842'::uuid, 'f160db63-42b3-4f4b-a306-a93f49933ff5'::uuid, 'f2db20a3-057e-4b5e-b101-48f30ef796d9'::uuid, '9720ec40-0071-4a60-8b11-a2dcdcc0cb32'::uuid, 'f0bb58ca-e8d6-4a8c-bba0-cbb9522a8da3'::uuid, '3a4a3262-5568-439a-bd22-c8d7b22fae0d'::uuid, 'f374f436-bd32-4397-8e8d-80250d38d2df'::uuid, 'b37f3d58-440c-4154-9ae5-a686448f1aa5'::uuid, 'cd8ec437-b7e9-4238-9fb5-34030749b09c'::uuid, 'db524f54-8215-4d91-ba98-45e247e44e38'::uuid, 'd63608d4-2782-4152-9941-65f4649871a5'::uuid, '3ba7e614-865c-4470-ab51-a2d5ea6d7979'::uuid);

update classroom_blocks set payload = jsonb_set(payload,'{html}',
  to_jsonb((payload->>'html') || $t$<p><i>Пример: Can I see your room? — Yes, of course. Come in!</i></p>$t$))
  where id = '41c3cb51-20ee-450c-a832-2545039e6cbc'::uuid;
update classroom_blocks set payload = jsonb_set(payload,'{html}',
  to_jsonb((payload->>'html') || $t$<p><i>Пример: There are five rooms in my house. My favourite room is the kitchen.</i></p>$t$))
  where id = 'f7441bce-1eaf-4b11-8d3d-e89198f0fa01'::uuid;
update classroom_blocks set payload = jsonb_set(payload,'{html}',
  to_jsonb((payload->>'html') || $t$<p><i>Пример: Yes, I have. I've got a cat. No, she hasn't.</i></p>$t$))
  where id = '56f37a23-6e0d-4dc1-891b-42448ff5c4cf'::uuid;
update classroom_blocks set payload = jsonb_set(payload,'{html}',
  to_jsonb((payload->>'html') || $t$<p><i>Пример: Oh no! I'm sorry, Mum.</i></p>$t$))
  where id = 'f2bc369a-f1b7-474f-a596-dab054663715'::uuid;
update classroom_blocks set payload = jsonb_set(payload,'{html}',
  to_jsonb((payload->>'html') || $t$<p><i>Пример: My favourite character is Masha. She's got long brown hair.</i></p>$t$))
  where id = '23642479-71af-4c3a-aadb-c63abb32e552'::uuid;
update classroom_blocks set payload = jsonb_set(payload,'{html}',
  to_jsonb((payload->>'html') || $t$<p><i>Пример: Yes, I do. My cat eats fish. No, they don't.</i></p>$t$))
  where id = '8478e7cc-5581-4590-9d44-0ca07a3969a4'::uuid;
update classroom_blocks set payload = jsonb_set(payload,'{html}',
  to_jsonb((payload->>'html') || $t$<p><i>Пример: thirty-five, twelve…</i></p>$t$))
  where id = 'e1175113-e7b7-407f-b15b-47f650613899'::uuid;
update classroom_blocks set payload = jsonb_set(payload,'{html}',
  to_jsonb((payload->>'html') || $t$<p><i>For example: There is a table. There aren't any chairs.</i></p>$t$))
  where id = '5f7da51e-8b2a-40f3-b9d4-6040866e1b2d'::uuid;
update classroom_blocks set payload = jsonb_set(payload,'{html}',
  to_jsonb((payload->>'html') || $t$<p><i>For example: I'm in the castle. I feel scared.</i></p>$t$))
  where id = '460cdb4a-2f78-4c99-8954-4d431af391e6'::uuid;
update classroom_blocks set payload = jsonb_set(payload,'{html}',
  to_jsonb(regexp_replace(payload->>'html','<i>.*?</i>', $t$<i>There is a cat on the chair. There are two books on the table.</i>$t$)))
  where id = '408e8e5a-7362-4a31-933f-1b34c48918c9'::uuid;
update classroom_blocks set payload = payload
  || jsonb_build_object('sample','')
  || jsonb_build_object('sample_tts', jsonb_build_object('text', $t$Red and blue.$t$, 'voice', 'en_US-amy'))
  where id = '73666aea-a527-4d73-bd84-0777ef1a6bf6'::uuid;
update classroom_blocks set payload = payload
  || jsonb_build_object('sample','')
  || jsonb_build_object('sample_tts', jsonb_build_object('text', $t$Three cars.$t$, 'voice', 'en_US-amy'))
  where id = 'ce10a8e2-d829-446d-a560-2bbde8168b8b'::uuid;
update classroom_blocks set payload = payload
  || jsonb_build_object('sample','')
  || jsonb_build_object('sample_tts', jsonb_build_object('text', $t$Four cats.$t$, 'voice', 'en_US-amy'))
  where id = 'a511cc8c-bffa-49c9-acbe-0b63bef8b842'::uuid;
update classroom_blocks set payload = payload
  || jsonb_build_object('sample','')
  || jsonb_build_object('sample_tts', jsonb_build_object('text', $t$Two dogs.$t$, 'voice', 'en_US-amy'))
  where id = 'f160db63-42b3-4f4b-a306-a93f49933ff5'::uuid;
update classroom_blocks set payload = payload
  || jsonb_build_object('sample','')
  || jsonb_build_object('sample_tts', jsonb_build_object('text', $t$My nose.$t$, 'voice', 'en_US-amy'))
  where id = 'f2db20a3-057e-4b5e-b101-48f30ef796d9'::uuid;
update classroom_blocks set payload = payload
  || jsonb_build_object('sample','')
  || jsonb_build_object('sample_tts', jsonb_build_object('text', $t$How many legs?$t$, 'voice', 'en_US-amy'))
  where id = '9720ec40-0071-4a60-8b11-a2dcdcc0cb32'::uuid;
update classroom_blocks set payload = payload
  || jsonb_build_object('sample','')
  || jsonb_build_object('sample_tts', jsonb_build_object('text', $t$Mum and dad.$t$, 'voice', 'en_US-amy'))
  where id = 'f0bb58ca-e8d6-4a8c-bba0-cbb9522a8da3'::uuid;
update classroom_blocks set payload = payload
  || jsonb_build_object('sample','')
  || jsonb_build_object('sample_tts', jsonb_build_object('text', $t$Mum and dad.$t$, 'voice', 'en_US-amy'))
  where id = '3a4a3262-5568-439a-bd22-c8d7b22fae0d'::uuid;
update classroom_blocks set payload = payload
  || jsonb_build_object('sample','')
  || jsonb_build_object('sample_tts', jsonb_build_object('text', $t$A doctor.$t$, 'voice', 'en_US-amy'))
  where id = 'f374f436-bd32-4397-8e8d-80250d38d2df'::uuid;
update classroom_blocks set payload = payload
  || jsonb_build_object('sample','')
  || jsonb_build_object('sample_tts', jsonb_build_object('text', $t$A doctor.$t$, 'voice', 'en_US-amy'))
  where id = 'b37f3d58-440c-4154-9ae5-a686448f1aa5'::uuid;
update classroom_blocks set payload = payload
  || jsonb_build_object('sample','')
  || jsonb_build_object('sample_tts', jsonb_build_object('text', $t$Swimming.$t$, 'voice', 'en_US-amy'))
  where id = 'cd8ec437-b7e9-4238-9fb5-34030749b09c'::uuid;
update classroom_blocks set payload = payload
  || jsonb_build_object('sample','')
  || jsonb_build_object('sample_tts', jsonb_build_object('text', $t$Swimming.$t$, 'voice', 'en_US-amy'))
  where id = 'db524f54-8215-4d91-ba98-45e247e44e38'::uuid;
update classroom_blocks set payload = payload
  || jsonb_build_object('sample','')
  || jsonb_build_object('sample_tts', jsonb_build_object('text', $t$What's your name?$t$, 'voice', 'en_US-amy'))
  where id = 'd63608d4-2782-4152-9941-65f4649871a5'::uuid;
update classroom_blocks set payload = payload
  || jsonb_build_object('sample','')
  || jsonb_build_object('sample_tts', jsonb_build_object('text', $t$The cat is under the table. The books are on the chair.$t$, 'voice', 'en_US-amy'))
  where id = '3ba7e614-865c-4470-ab51-a2d5ea6d7979'::uuid;
