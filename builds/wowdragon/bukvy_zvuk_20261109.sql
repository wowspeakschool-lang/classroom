-- Wow Dragon: записи букв голосом Анны расставлены по блокам (09.11.2026).
-- Девять файлов в classroom-media/wowdragon: P U D B T S G H TH; Анна записала ЗВУК буквы.
-- Там, где вопрос называл букву («Найди букву P»), возвращено слушание.
-- Копия затронутых блоков — classroom_backup_wd_bukvy_zvuk_20261109.

do $$
declare base text := 'https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/wowdragon/'; r record;
begin
  for r in select * from (values
    ('49faa740-37a0-468c-a074-1df1e3429f9d','{cards,0,audio}','wd1_P.mp3'),
    ('49faa740-37a0-468c-a074-1df1e3429f9d','{cards,1,audio}','wd1_P.mp3'),
    ('69747f75-56c5-44ec-a1d0-f951a63e907a','{questions,0,audio}','wd1_P.mp3'),
    ('ab601dfa-3007-4585-a74e-fc2de34db421','{cards,0,audio}','wd1_U.mp3'),
    ('ab601dfa-3007-4585-a74e-fc2de34db421','{cards,1,audio}','wd1_U.mp3'),
    ('b35acbf0-2bb9-4bde-bfca-13e2a8192991','{questions,0,audio}','wd1_U.mp3'),
    ('b35acbf0-2bb9-4bde-bfca-13e2a8192991','{questions,1,audio}','wd1_U.mp3'),
    ('e486082a-14dd-4df7-9c21-9b17f8e559d0','{pairs,0,right_audio}','wd1_U.mp3'),
    ('e486082a-14dd-4df7-9c21-9b17f8e559d0','{pairs,1,right_audio}','wd1_P.mp3'),
    ('80aa6124-6781-4372-923d-565361d22be1','{cards,5,audio}','wd1_D.mp3'),
    ('0696ff46-ac31-47af-88f7-45742b2f6211','{questions,0,audio}','wd1_P.mp3'),
    ('0696ff46-ac31-47af-88f7-45742b2f6211','{questions,1,audio}','wd1_U.mp3'),
    ('0696ff46-ac31-47af-88f7-45742b2f6211','{questions,2,audio}','wd1_D.mp3'),
    ('0f703ae9-e1be-4c15-a4b0-83ee381823aa','{cards,0,audio}','wd1_B.mp3'),
    ('8f489c51-acee-445e-9149-4b293b333ee3','{questions,0,audio}','wd1_B.mp3'),
    ('8f489c51-acee-445e-9149-4b293b333ee3','{questions,1,audio}','wd1_D.mp3'),
    ('8f489c51-acee-445e-9149-4b293b333ee3','{questions,2,audio}','wd1_P.mp3'),
    ('8f489c51-acee-445e-9149-4b293b333ee3','{questions,3,audio}','wd1_U.mp3'),
    ('72cf9a64-2792-4ab0-a43e-5302d087f667','{pairs,0,right_audio}','wd1_B.mp3'),
    ('72cf9a64-2792-4ab0-a43e-5302d087f667','{pairs,1,right_audio}','wd1_D.mp3'),
    ('72cf9a64-2792-4ab0-a43e-5302d087f667','{pairs,2,right_audio}','wd1_P.mp3'),
    ('72cf9a64-2792-4ab0-a43e-5302d087f667','{pairs,3,right_audio}','wd1_U.mp3'),
    ('e810ff23-588b-4b58-84e9-e71bae60a687','{cards,0,audio}','wd1_T.mp3'),
    ('bdd44c7d-decc-4b56-a34b-d1806b7a371f','{questions,0,audio}','wd1_T.mp3'),
    ('dbf9db37-7125-4be1-8f75-a2b63c2d383b','{pairs,0,right_audio}','wd1_T.mp3'),
    ('dbf9db37-7125-4be1-8f75-a2b63c2d383b','{pairs,1,right_audio}','wd1_B.mp3'),
    ('dbf9db37-7125-4be1-8f75-a2b63c2d383b','{pairs,2,right_audio}','wd1_D.mp3'),
    ('e908c78b-265e-4c08-b7e2-0e26c1ec4c59','{cards,3,audio}','wd1_S.mp3'),
    ('119e5cdb-a7be-4ab4-b236-350c4e3f6674','{questions,0,audio}','wd1_S.mp3'),
    ('24bba960-bdb9-479a-bf75-00d05c717919','{questions,0,audio}','wd2_H.mp3'),
    ('0de84d29-d2dc-4051-85d8-a37896679adf','{questions,0,audio}','wd2_G.mp3'),
    ('77152016-05ad-4392-bc9d-c33e5ffa9064','{questions,0,audio}','wd2_G.mp3'),
    ('77152016-05ad-4392-bc9d-c33e5ffa9064','{questions,1,audio}','wd2_H.mp3'),
    ('f62edc02-e790-4106-8392-cb3b9602b6b7','{questions,0,audio}','wd1_T.mp3'),
    ('f62edc02-e790-4106-8392-cb3b9602b6b7','{questions,1,audio}','wd2_G.mp3'),
    ('f62edc02-e790-4106-8392-cb3b9602b6b7','{questions,2,audio}','wd2_H.mp3'),
    ('066872df-60f4-42fc-b5e9-db2f01d11353','{questions,0,audio}','wd2_G.mp3'),
    ('066872df-60f4-42fc-b5e9-db2f01d11353','{questions,1,audio}','wd2_H.mp3'),
    ('066872df-60f4-42fc-b5e9-db2f01d11353','{questions,2,audio}','wd1_T.mp3'),
    ('7427afc8-6f85-4903-9685-3aa7fe65ed0c','{questions,0,audio}','wd2_TH.mp3'),
    ('ef58f6b2-8adb-4534-a10b-63c4f1fdec4e','{questions,2,audio}','wd1_S.mp3'),
    ('857d906f-99d1-46ec-9114-4214d111b944','{questions,0,audio}','wd1_D.mp3'),
    ('857d906f-99d1-46ec-9114-4214d111b944','{questions,1,audio}','wd1_D.mp3'),
    ('404cc72f-60b5-4113-9e0a-cefb1960dbd8','{cards,2,audio}','wd1_B.mp3')
  ) as t(bid, path, f) loop
    update classroom_blocks set payload = jsonb_set(payload, r.path::text[], to_jsonb(base || r.f))
    where id = r.bid::uuid;
  end loop;

  for r in select * from (values
    ('69747f75-56c5-44ec-a1d0-f951a63e907a','{questions,0,q}','Послушай и найди большую букву.'),
    ('b35acbf0-2bb9-4bde-bfca-13e2a8192991','{questions,0,q}','Послушай и найди большую букву.'),
    ('b35acbf0-2bb9-4bde-bfca-13e2a8192991','{questions,1,q}','Послушай и найди маленькую букву.'),
    ('0696ff46-ac31-47af-88f7-45742b2f6211','{questions,0,q}','Послушай и найди букву.'),
    ('0696ff46-ac31-47af-88f7-45742b2f6211','{questions,1,q}','Послушай и найди букву.'),
    ('0696ff46-ac31-47af-88f7-45742b2f6211','{questions,2,q}','Послушай и найди букву.'),
    ('8f489c51-acee-445e-9149-4b293b333ee3','{questions,0,q}','Послушай и найди букву.'),
    ('8f489c51-acee-445e-9149-4b293b333ee3','{questions,1,q}','Послушай и найди букву.'),
    ('8f489c51-acee-445e-9149-4b293b333ee3','{questions,2,q}','Послушай и найди букву.'),
    ('8f489c51-acee-445e-9149-4b293b333ee3','{questions,3,q}','Послушай и найди букву.'),
    ('24bba960-bdb9-479a-bf75-00d05c717919','{questions,0,q}','Послушай и найди букву.'),
    ('0de84d29-d2dc-4051-85d8-a37896679adf','{questions,0,q}','Послушай и найди букву.'),
    ('77152016-05ad-4392-bc9d-c33e5ffa9064','{questions,0,q}','Послушай и найди букву.'),
    ('77152016-05ad-4392-bc9d-c33e5ffa9064','{questions,1,q}','Послушай и найди букву.'),
    ('f62edc02-e790-4106-8392-cb3b9602b6b7','{questions,0,q}','Послушай и найди букву.'),
    ('f62edc02-e790-4106-8392-cb3b9602b6b7','{questions,1,q}','Послушай и найди букву.'),
    ('f62edc02-e790-4106-8392-cb3b9602b6b7','{questions,2,q}','Послушай и найди букву.'),
    ('066872df-60f4-42fc-b5e9-db2f01d11353','{questions,0,q}','Послушай и найди букву.'),
    ('066872df-60f4-42fc-b5e9-db2f01d11353','{questions,1,q}','Послушай и найди букву.'),
    ('066872df-60f4-42fc-b5e9-db2f01d11353','{questions,2,q}','Послушай и найди букву.'),
    ('7427afc8-6f85-4903-9685-3aa7fe65ed0c','{questions,0,q}','Послушай и найди буквы.')
  ) as t(bid, path, f) loop
    update classroom_blocks set payload = jsonb_set(payload, r.path::text[], to_jsonb(r.f))
    where id = r.bid::uuid;
  end loop;
end $$;

-- WD1 Homework 32, блок 7 («Это буква P?»): три вопроса получают звук и честный текст
update classroom_blocks set payload =
  jsonb_set(jsonb_set(jsonb_set(jsonb_set(jsonb_set(jsonb_set(payload,
    '{questions,0,audio}', to_jsonb('https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/wowdragon/wd1_P.mp3'::text)),
    '{questions,1,audio}', to_jsonb('https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/wowdragon/wd1_P.mp3'::text)),
    '{questions,2,audio}', to_jsonb('https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/wowdragon/wd1_P.mp3'::text)),
    '{questions,0,q}', '"Послушай звук и посмотри на букву. Это она?"'::jsonb),
    '{questions,1,q}', '"Послушай звук и посмотри на букву. Это она?"'::jsonb),
    '{questions,2,q}', '"Послушай звук и посмотри на букву. Это она?"'::jsonb)
where id = '5482f1b6-223b-4cee-a096-56851766ba49';

-- WD2 Homework 75, блок 4, вопрос 2: записи SH нет — текст не обещает звук
update classroom_blocks set payload = jsonb_set(payload, '{questions,1,q}', '"Найди буквы SH."'::jsonb)
where id = 'ef58f6b2-8adb-4534-a10b-63c4f1fdec4e';
