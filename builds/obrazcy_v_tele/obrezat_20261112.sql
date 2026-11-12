-- Обрезка примеров в теле заданий speaking, правило Анны 09.11.2026 (решение 12.11: «остальное делаем»)
create table if not exists classroom_backup_obrazcy_v_tele_20261112 as
select * from classroom_blocks where id in ('9d3661b6-a4ac-479b-bd96-411d5b4c42c4'::uuid, '0c64ae84-5440-4f52-8f2e-2dd1692c5f37'::uuid, 'acdc892a-5b21-4df0-bdae-71c7b52b1a8c'::uuid, 'e4218501-6757-426f-9cde-d0e4a6ab5b1f'::uuid, '1faa48b3-8741-44ef-b5f3-813e4f210ec6'::uuid, '5f22898a-21e9-4cdc-aff8-049f9f7ef86b'::uuid, 'c76d6c57-eeb3-4b76-a7dd-503d52ec5b71'::uuid, '86500ffa-8382-4696-b8f0-7369e85982f4'::uuid, 'ee5bb9f4-886e-4b18-8067-bc4b4ec188eb'::uuid, '455e5f39-fb2f-453e-856c-ae21069ecc63'::uuid, 'bca92013-1cbc-40cb-9099-64fe24d81d55'::uuid, 'ce2149bb-2c9b-43a0-a39d-471c0216637f'::uuid, 'a954d2e6-e9cf-44da-b2c5-3d848ea75440'::uuid, 'f31dec0f-099c-4f6e-bc7b-b40a276ab00a'::uuid, 'beef99e5-33f6-4c9d-8504-4e5bb594184b'::uuid, '51750a50-9331-4313-9f79-1b1ffa0db58e'::uuid, '992f7e3b-a3be-4820-a6e6-33c7f2e309cc'::uuid, '47e448b2-5e41-4d67-9fb9-238f6ff37228'::uuid, '394d22bf-5391-465f-8812-6fc1848e90fa'::uuid, 'a6eda555-ad6a-4eea-868a-98353dd1cb22'::uuid, '55f2f6da-50b0-4b0b-866f-e82f102908cd'::uuid, '637f8844-96fc-431b-8bb0-027f2231f378'::uuid, '0a151532-8206-4eb0-9329-57cbdd7c8ea6'::uuid, '6c8eb33f-80b1-4b0e-a78f-11c971588e58'::uuid, '5004d19d-4490-4db0-bdfa-cafa5ac5c26e'::uuid, 'b2669261-7dd1-4745-80b4-8e802d8cb97a'::uuid, '1df60c28-86c7-4947-a273-f3604940a98d'::uuid, '886c6c18-1b4e-4525-975f-1a7d24a0d090'::uuid, '1e124301-f8e0-4cb1-954c-c5412061339c'::uuid, 'bbbc87a9-d9f0-4daf-b8a3-18329ac1f13b'::uuid, 'fd78cd1a-fc0a-4189-82b1-0f9720ee19dc'::uuid, '7cfee9c1-e88a-45b6-a75a-e4b69932ce83'::uuid, 'a9925e08-a84b-4e42-994f-16a9bbb35d05'::uuid, 'd6aa9e52-ac1d-47bf-8224-d0b4d741feb4'::uuid, '1c4a4a95-a6c5-4f0f-9968-2b4e3deac62b'::uuid, '4bdbaa8f-dc6d-4c7b-8867-a9bd7dc430dd'::uuid);

update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: The bananas are yellow.</i>$t$)))
  where id = '9d3661b6-a4ac-479b-bd96-411d5b4c42c4'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: This is my family: my mum…</i>$t$)))
  where id = '0c64ae84-5440-4f52-8f2e-2dd1692c5f37'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: Hi! I'm Anna. This is my friend. His name's Tom. He's eleven.</i>$t$)))
  where id = 'acdc892a-5b21-4df0-bdae-71c7b52b1a8c'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: I'm Polish. I'm not British. My cousins are Italian.</i>$t$)))
  where id = 'e4218501-6757-426f-9cde-d0e4a6ab5b1f'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: Hi, Mum! This is my friend Tom. — Nice to meet you!</i>$t$)))
  where id = '1faa48b3-8741-44ef-b5f3-813e4f210ec6'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: My mum is at home. My friends are in the park.</i>$t$)))
  where id = '5f22898a-21e9-4cdc-aff8-049f9f7ef86b'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: Hi! I'm Anna. This is my family: my mum, my dad and my brother. We're in the park today.</i>$t$)))
  where id = 'c76d6c57-eeb3-4b76-a7dd-503d52ec5b71'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: I've got a blue T-shirt and black jeans.</i>$t$)))
  where id = '86500ffa-8382-4696-b8f0-7369e85982f4'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: This is my new T-shirt. Those are my old shoes.</i>$t$)))
  where id = 'ee5bb9f4-886e-4b18-8067-bc4b4ec188eb'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: Is this jacket new? — Yes, it is. Are these shoes too big? — No, they aren't.</i>$t$)))
  where id = '455e5f39-fb2f-453e-856c-ae21069ecc63'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: This is my favourite top. It's blue with red squares. I love it!</i>$t$)))
  where id = 'bca92013-1cbc-40cb-9099-64fe24d81d55'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: I want a big house with a garden. In my bedroom there is a big bed.</i>$t$)))
  where id = 'ce2149bb-2c9b-43a0-a39d-471c0216637f'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: I've got two books and a pencil case.</i>$t$)))
  where id = 'beef99e5-33f6-4c9d-8504-4e5bb594184b'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: run, swim…</i>$t$)))
  where id = '51750a50-9331-4313-9f79-1b1ffa0db58e'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: Can you swim? — Yes, I can. Can you sing? — No, I can't.</i>$t$)))
  where id = '992f7e3b-a3be-4820-a6e6-33c7f2e309cc'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: I can speak Polish. I can't speak Spanish, but I want to learn it.</i>$t$)))
  where id = '47e448b2-5e41-4d67-9fb9-238f6ff37228'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: In January I go skiing.</i>$t$)))
  where id = 'a6eda555-ad6a-4eea-868a-98353dd1cb22'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: On weekdays I always go to school.</i>$t$)))
  where id = '55f2f6da-50b0-4b0b-866f-e82f102908cd'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: Hello! Can I have three tickets, please? — That's eighteen pounds fifty. — Here you are.</i>$t$)))
  where id = '637f8844-96fc-431b-8bb0-027f2231f378'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: What's your favourite sport? Where do you live? How many brothers and sisters have you got?</i>$t$)))
  where id = '6c8eb33f-80b1-4b0e-a78f-11c971588e58'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Пример: Today it's warm and sunny. My favourite season is summer. I love it!</i>$t$)))
  where id = '5004d19d-4490-4db0-bdfa-cafa5ac5c26e'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>I have a costume — I'm a vampire. I eat mummy hot dogs.</i>$t$)))
  where id = '1df60c28-86c7-4947-a273-f3604940a98d'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>On Halloween I wear a costume. This year I'm a vampire! My friends and I carve a pumpkin.</i>$t$)))
  where id = '886c6c18-1b4e-4525-975f-1a7d24a0d090'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>Например: I go to school.</i>$t$)))
  where id = '1e124301-f8e0-4cb1-954c-c5412061339c'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>For example:<br>My bedroom is upstairs.<br>We haven’t got a cellar.</i>$t$)))
  where id = 'fd78cd1a-fc0a-4189-82b1-0f9720ee19dc'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>For example:<br>I’m good at swimming.<br>I’m not good at painting.</i>$t$)))
  where id = '7cfee9c1-e88a-45b6-a75a-e4b69932ce83'::uuid;
update classroom_blocks set payload = jsonb_set(payload, '{html}',
  to_jsonb(regexp_replace(payload->>'html', '<i>.*?</i>', $t$<i>For example:<br>This is my mum’s sister. She’s my aunt.</i>$t$)))
  where id = 'a9925e08-a84b-4e42-994f-16a9bbb35d05'::uuid;
