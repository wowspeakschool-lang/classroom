-- Подводки внутрь заданий (решение Анны 20.11.2026). Блоки удаляются, уроки перенумеровываются.
create table if not exists classroom_backup_podvodki_20261120 as
select b.* from classroom_blocks b where b.lesson_id in (
  '02318779-4bc2-41c6-8e83-5b29f345063d'::uuid,
  '071c7454-bdd3-4f25-9c91-82f70c82e2e9'::uuid,
  '0ea0cd06-957c-41b3-8898-115071addb07'::uuid,
  '0fcc69fc-2b29-4598-888d-85cd9462b171'::uuid,
  '11e3a724-a913-4674-b995-9cc5b5730766'::uuid,
  '13f3a27a-4935-45e3-bdc9-732182f85e90'::uuid,
  '3be806f6-8407-4b49-bf62-c7e4f451475c'::uuid,
  '3d99f3c7-a8ce-43f8-bff1-1332816b6191'::uuid,
  '3f573a3d-ab85-46d5-9e9d-af23fd256710'::uuid,
  '4895aef2-0d9a-41fe-8cb9-c9cd45d0ce92'::uuid,
  '4bba3feb-e27c-4855-add7-150b185e28e2'::uuid,
  '4cf4c755-dd7e-4892-b62b-a7bbbae90542'::uuid,
  '4d349ca7-4b58-48e8-824a-fcde5e710f54'::uuid,
  '5137fe5f-1e13-4b8c-bb8d-bef30e98eb15'::uuid,
  '5a94763b-71b5-4165-b17f-8d4942a95b01'::uuid,
  '5ca65a4e-cdb3-41a5-948b-10e63200781f'::uuid,
  '5ef4f0f4-df0d-4861-979e-4b07b8ad12dc'::uuid,
  '6097a083-2eea-4166-8751-a5771b0f1bfb'::uuid,
  '71133446-3777-4dbd-a5a2-1ba78fe82fe9'::uuid,
  '72022c46-2535-4739-96c8-114e0acecf6d'::uuid,
  '733dc304-b3d8-4436-8f16-5ca67f5eff42'::uuid,
  '7693a293-54d5-4063-8645-b63c54bfee88'::uuid,
  '7a60cb85-9509-4982-9db5-c9b4f7a1d98e'::uuid,
  '83fd09f0-a2a0-4745-9777-5ea73b3323b4'::uuid,
  '8a5af72a-34a2-4ce7-9702-eeaf1b9b6109'::uuid,
  '8e5529ec-dd1b-482c-9f88-d3de63beb68d'::uuid,
  '93638f0e-8ef2-4aad-b8a6-5251bffee9d1'::uuid,
  '93ce371e-4b95-41e6-83bd-096fdc9dd66c'::uuid,
  '9c298871-50b1-4392-b74a-e436e93e54a9'::uuid,
  'a3baf17a-9b4a-4405-85e8-0d647997ea09'::uuid,
  'a69261e4-c07e-4f84-baf6-52c0564302c5'::uuid,
  'acecb9d6-a741-416f-b895-c6819bf923fd'::uuid,
  'b34421bf-19d0-4098-989f-1c4dc259a384'::uuid,
  'b586c4d4-f4a6-44e0-959b-49d62e90b9f5'::uuid,
  'c844f0ab-00a9-4175-b9ff-b71a45fc4cc0'::uuid,
  'd34ed37d-06de-4343-b38f-437ce18aa9eb'::uuid,
  'd7074b31-2c22-41b2-bf17-5bc1f9ed3493'::uuid,
  'd8fbeb71-a2ef-4bfd-a0d9-eb73dae5d5e0'::uuid,
  'e98283ea-253d-49a4-a9e2-abff23cffe04'::uuid,
  'f88cf616-d2dd-48a9-a486-0dc0d6909fbd'::uuid
);

update classroom_blocks set payload = jsonb_set(payload,'{title}',to_jsonb('Составь вопросы. Не забудь вопросительный знак в конце'::text)) where id='4f1ca1ab-9f00-4fda-b15f-9e2bcf74ff44';
update classroom_blocks set payload = jsonb_set(payload,'{material}',to_jsonb($m$<p>Наречие стоит перед обычным глаголом и после <b>am</b>, <b>is</b>, <b>are</b>.</p>$m$::text)) where id='28d9fc4d-1235-4bb6-8ae9-5c1ea0369eeb';
update classroom_blocks set payload = jsonb_set(payload,'{material}',to_jsonb($m$<p>Вопрос начинается с <b>Do</b> или <b>Does</b>, а в конце стоит знак вопроса.</p>$m$::text)) where id='7ca47a58-0a67-43f2-aaa0-1e6c1aebfeed';
update classroom_blocks set payload = jsonb_set(payload,'{title}',to_jsonb('Составь вопросы про животных'::text)) where id='60c558ef-168a-4868-8224-0b312c2f53f4';
update classroom_blocks set payload = jsonb_set(payload,'{material}',to_jsonb($m$<p>После <b>love</b>, <b>like</b> и <b>hate</b> глагол получает окончание <b>-ing</b>.</p>$m$::text)) where id='9011327a-e572-40bb-a6fd-78ecd8062054';
update classroom_blocks set payload = jsonb_set(payload,'{material}',to_jsonb($m$<p><b>How many</b> — если предмет можно посчитать.</p><p><b>How much</b> — если посчитать нельзя.</p>$m$::text)) where id='56d0d186-cd09-423d-94af-7c34494a4678';
update classroom_blocks set payload = jsonb_set(payload,'{title}',to_jsonb('Посмотри на картинку и напиши, какие эмоции у героев · 1'::text)) where id='5f08b705-7099-4ba8-bf97-1438c2b8a1fa';
update classroom_blocks set payload = jsonb_set(payload,'{material}',to_jsonb($m$<p>При сравнении двух предметов ставим <b>than</b> — «чем».</p>$m$::text)) where id='daaa6fe4-7a1f-486b-b5cb-6e19113ad7bf';
update classroom_blocks set payload = jsonb_set(payload,'{material}',to_jsonb($m$<p>Нарисуй три картины, будто их нарисовали три разных персонажа — Карла, Рокко и Большой Эл.</p>$m$::text)) where id='65452bfd-ac5c-4d0b-aab2-48b09fa3b8d3';
update classroom_blocks set payload = jsonb_set(payload,'{material}',to_jsonb($m$<p>Нарисуй двух знакомых тебе людей, одно здание (можно достопримечательность) и один предмет.</p>$m$::text)) where id='8eaaa2ed-f278-4613-bf24-e64b643afc1a';
update classroom_blocks set payload = jsonb_set(payload,'{material}',to_jsonb($m$<p><b>LOOK! Prices 💷</b></p><p>£10.50 = <b>ten pounds fifty</b><br>£7.25 = <b>seven pounds twenty-five</b><br>£0.50 = <b>fifty pence</b></p>$m$::text)) where id='5e0bc597-bcca-4dd3-ad3a-119346957905';
update classroom_blocks set payload = jsonb_set(payload,'{material}',to_jsonb($m$<p>О планах говорим с <b>be going to</b>. В вопросе сначала вопросительное слово, потом <b>am / is / are</b>:</p><p><b>What are you going to do?</b><br><b>Where are you going to go?</b><br><b>Who is going to come?</b></p>$m$::text)) where id='6336f334-4f4d-44a4-abe5-0f6102fa972a';
update classroom_blocks set payload = jsonb_set(payload,'{title}',to_jsonb('Составь вопросы'::text)) where id='0b766758-f8c1-45ea-859d-802eebbc7ab0';
update classroom_blocks set payload = jsonb_set(payload,'{material}',to_jsonb($m$<p><b>Look at me!</b> <i>Посмотри на меня!</i><br><b>My turn. Look!</b> <i>Моя очередь. Смотри!</i><br><b>Listen to me.</b> <i>Послушай меня.</i><br><b>I speak to animals.</b> <i>Я говорю с животными.</i><br><b>I'm four.</b> <i>Мне четыре года.</i></p>$m$::text)) where id='c6897eee-6edb-46bb-91ea-7aa76961824b';
update classroom_blocks set payload = jsonb_set(payload,'{title}',to_jsonb('Посмотри на картинку и напиши слово'::text)) where id='76232d8f-fff5-4801-995b-de8245f48700';
update classroom_blocks set payload = jsonb_set(payload,'{material}',to_jsonb($m$<p>В вопросах порядок слов меняется: <b>has</b> уходит вперёд.</p>$m$::text)) where id='b7364570-4413-46c0-b488-39fb7a09d1ae';
update classroom_blocks set payload = jsonb_set(payload,'{material}',to_jsonb($m$<p>Нарисуй карту своего города и подпиши названия мест. Покажи рисунок учителю на уроке.</p>$m$::text)) where id='cfe09dc2-92c9-47bd-84b5-074d237197ac';
update classroom_blocks set payload = jsonb_set(payload,'{material}',to_jsonb($m$<p><b>There is</b> — когда предмет один: <i>There is a bed in my room.</i></p><p><b>There are</b> — когда предметов много: <i>There are two windows in my room.</i></p>$m$::text)) where id='a3b0549b-ee83-44cd-9834-66f3b78eb64e';
update classroom_blocks set payload = jsonb_set(payload,'{title}',to_jsonb('Составь вопросы'::text)) where id='b3075dfb-468d-4b43-a682-59fc165ea14c';

delete from classroom_blocks where id in (
  'c18e91ee-cc7c-4952-b908-207f7b999032'::uuid,
  'bddf7873-856b-4e82-8c89-cd11df5d2945'::uuid,
  '9f850c13-c0ea-40cd-b1bb-dc53a2899215'::uuid,
  '06f00e3e-4ce1-4f00-bfcd-d5acc90b9bcf'::uuid,
  'd8c1bb1a-15cc-4277-80b0-55374a4b6709'::uuid,
  'b8e4c414-10f0-4f77-b6c2-f0703afebd51'::uuid,
  '5d429c17-503b-488a-b5be-982c86c34671'::uuid,
  'a4d3ed28-a313-40c9-94a9-169282beaa23'::uuid,
  '2973a872-4661-4379-9608-8ff085e48f5b'::uuid,
  '4666209f-11ce-4d77-9d8a-9845b49acfc8'::uuid,
  '65b75ed5-445d-4558-ad72-fd36456b7d1f'::uuid,
  '7d09d006-c958-4411-849c-2d35dff6670f'::uuid,
  'bd82cd9a-e86a-4917-8dee-fd61135c34bb'::uuid,
  '9bf785b6-dd9f-43a4-b478-9b6c26bcb5c2'::uuid,
  '326ff644-f5c0-43cd-9bce-4bd6a1173eb4'::uuid,
  'e4fa4678-d5cb-42b7-aecc-c78ca1493e45'::uuid,
  'f1bd2155-80fa-4b1f-ae66-03cc9278455b'::uuid,
  '1127addb-2845-4cac-865d-11ef36a44da1'::uuid,
  'a72a14b3-4b17-481c-90f3-4df833ce62e0'::uuid,
  '4960ebcb-4f98-4c43-97ad-9b5c6177b423'::uuid,
  'dd37aaf8-1dcc-46cf-93dd-e739d3a9dcf5'::uuid,
  '39e4b9b5-339f-46e1-8705-aa4b4b890465'::uuid,
  '7463721f-d6d0-4bde-b197-a812610dc8de'::uuid,
  '364e8713-26e4-4ad8-8126-c1e5e72dbc79'::uuid,
  'b3a645c6-bbb2-4547-85fa-65b86c6c1a5e'::uuid,
  'f1bd5537-2c4a-4ba1-b34f-ab80803ff55f'::uuid,
  '299d74c4-75b3-48eb-99cc-f75c3539d408'::uuid,
  '41e6c699-2775-4480-9067-02b09f92ad61'::uuid,
  '6624973b-7d28-4701-89a3-1550e265e668'::uuid,
  '23e030dc-16ce-47d3-a645-c204514fb9ef'::uuid,
  '862bb846-02de-4310-b8da-e2c559cc0e09'::uuid,
  '26808bb4-d39d-482b-9586-2e4773f9dfaf'::uuid,
  'a62e02c4-9eea-435a-b4ce-66d2accc06ad'::uuid,
  '1dcf714b-007f-424d-9685-8b635a2e15d1'::uuid,
  '43b83132-0296-4ded-88e6-92e52ac3ae65'::uuid,
  '34091e71-062a-4752-8494-5501361aa4ac'::uuid,
  '4e60b898-66c9-416a-82b2-49d3748f41d9'::uuid,
  'a15b1b7f-9140-4fd3-8700-0b3131cbe91f'::uuid,
  '52d2587f-ebc8-4abc-8206-5a24b40a05ad'::uuid,
  'a4b5e007-212e-4998-9b09-4a005188d6b4'::uuid,
  '722c1543-3b18-497f-9390-b56b0c5abcfa'::uuid,
  '987e61f0-54f0-430c-a263-ee4d68009021'::uuid,
  '069b6ade-3895-4570-adec-a5dfbe3fe360'::uuid,
  '06ee5c14-b22d-4130-bcdf-3231b171442e'::uuid,
  '25cefe04-962b-47d4-8191-24c0d804a42c'::uuid,
  '772ea6fc-d797-4c70-824c-42830a9d7ec3'::uuid
);

do $$
declare u uuid; r record; i int;
begin
  foreach u in array array[
    '02318779-4bc2-41c6-8e83-5b29f345063d'::uuid,
    '071c7454-bdd3-4f25-9c91-82f70c82e2e9'::uuid,
    '0ea0cd06-957c-41b3-8898-115071addb07'::uuid,
    '0fcc69fc-2b29-4598-888d-85cd9462b171'::uuid,
    '11e3a724-a913-4674-b995-9cc5b5730766'::uuid,
    '13f3a27a-4935-45e3-bdc9-732182f85e90'::uuid,
    '3be806f6-8407-4b49-bf62-c7e4f451475c'::uuid,
    '3d99f3c7-a8ce-43f8-bff1-1332816b6191'::uuid,
    '3f573a3d-ab85-46d5-9e9d-af23fd256710'::uuid,
    '4895aef2-0d9a-41fe-8cb9-c9cd45d0ce92'::uuid,
    '4bba3feb-e27c-4855-add7-150b185e28e2'::uuid,
    '4cf4c755-dd7e-4892-b62b-a7bbbae90542'::uuid,
    '4d349ca7-4b58-48e8-824a-fcde5e710f54'::uuid,
    '5137fe5f-1e13-4b8c-bb8d-bef30e98eb15'::uuid,
    '5a94763b-71b5-4165-b17f-8d4942a95b01'::uuid,
    '5ca65a4e-cdb3-41a5-948b-10e63200781f'::uuid,
    '5ef4f0f4-df0d-4861-979e-4b07b8ad12dc'::uuid,
    '6097a083-2eea-4166-8751-a5771b0f1bfb'::uuid,
    '71133446-3777-4dbd-a5a2-1ba78fe82fe9'::uuid,
    '72022c46-2535-4739-96c8-114e0acecf6d'::uuid,
    '733dc304-b3d8-4436-8f16-5ca67f5eff42'::uuid,
    '7693a293-54d5-4063-8645-b63c54bfee88'::uuid,
    '7a60cb85-9509-4982-9db5-c9b4f7a1d98e'::uuid,
    '83fd09f0-a2a0-4745-9777-5ea73b3323b4'::uuid,
    '8a5af72a-34a2-4ce7-9702-eeaf1b9b6109'::uuid,
    '8e5529ec-dd1b-482c-9f88-d3de63beb68d'::uuid,
    '93638f0e-8ef2-4aad-b8a6-5251bffee9d1'::uuid,
    '93ce371e-4b95-41e6-83bd-096fdc9dd66c'::uuid,
    '9c298871-50b1-4392-b74a-e436e93e54a9'::uuid,
    'a3baf17a-9b4a-4405-85e8-0d647997ea09'::uuid,
    'a69261e4-c07e-4f84-baf6-52c0564302c5'::uuid,
    'acecb9d6-a741-416f-b895-c6819bf923fd'::uuid,
    'b34421bf-19d0-4098-989f-1c4dc259a384'::uuid,
    'b586c4d4-f4a6-44e0-959b-49d62e90b9f5'::uuid,
    'c844f0ab-00a9-4175-b9ff-b71a45fc4cc0'::uuid,
    'd34ed37d-06de-4343-b38f-437ce18aa9eb'::uuid,
    'd7074b31-2c22-41b2-bf17-5bc1f9ed3493'::uuid,
    'd8fbeb71-a2ef-4bfd-a0d9-eb73dae5d5e0'::uuid,
    'e98283ea-253d-49a4-a9e2-abff23cffe04'::uuid,
    'f88cf616-d2dd-48a9-a486-0dc0d6909fbd'::uuid
  ] loop
    update classroom_blocks set sort_order = -1 - sort_order where lesson_id = u;
    i := 0;
    for r in select id from classroom_blocks where lesson_id = u order by sort_order desc loop
      update classroom_blocks set sort_order = i where id = r.id;
      i := i + 1;
    end loop;
  end loop;
end $$;
