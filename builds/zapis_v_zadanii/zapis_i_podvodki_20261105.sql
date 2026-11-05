-- Два прохода по домашкам (решение Анны 05.11.2026: «так делай»).
--
-- 1. Запись лежала отдельным блоком перед заданием — семь мест. По правилу от
--    02.11 запись должна быть в самом задании: платформа показывает по одному
--    блоку на экран, и «послушай и ответь» через экран не работает. Звук
--    переезжает в задание, подводка — в «Материал задания», текстовый блок
--    убирается.
-- 2. Текстовый блок, который только объявляет видео («Давай начнём с видео!»,
--    «Молодец! Посмотри видео ещё раз») — шесть мест. По правилу от 04.11
--    инструкция уходит в заголовок самого блока с видео, текст убирается.
--
-- Копия затронутых уроков — classroom_backup_zapis_podvodki_20261105.

do $$
declare
  ids uuid[] := array[
    '33b5871b-e8db-4fd4-8345-a62675ba0f0f','d9c638fc-2298-4987-9d7c-c6a966e1905b',
    '17a18c98-8aa0-48bc-97ec-ed69bbabf928','2105be4b-fb53-4d82-8915-27f24dfa7037',
    '22bbd8fa-6b22-4e67-84b3-43a3f0663d3e','1bc8cead-4629-4d42-aa20-e7e6015504a2',
    '630ee06f-4677-4257-878f-3d4cf7d7f041',
    '25cfbd2e-2e83-4a97-a566-4447f013b1f0','2c2e193f-d67c-467f-88da-c30a5cf592cb',
    '65e0bfdf-3bc1-4ebb-84e1-3ad4fe3b0fa7','8f93ad93-329c-41e4-bae4-1acdc05b64fe',
    'db90593f-50cc-48ef-8abe-38d1de40cdb6','e2d5b177-7e0c-4641-a189-4e1c9cc3e6b2']::uuid[];
  a text;
begin

create table if not exists classroom_backup_zapis_podvodki_20261105 as
  select * from classroom_blocks where lesson_id = any(ids);

-- ---------- 1. запись в задание ----------

-- SM1 Unit 2 ДЗ 4: звук из блока 3 → в квиз «Прочитай историю и ответь на вопросы»;
-- блок 4 был подводкой к тому же квизу.
select payload->>'audio' into a from classroom_blocks where id='9987d17b-f0c3-457a-9d24-c2574b84ad22';
update classroom_blocks set payload = jsonb_set(jsonb_set(payload,'{audio}',to_jsonb(a),true),
       '{title}', to_jsonb('Послушай и прочитай историю, потом ответь на вопросы'::text))
  where id='e8f429a5-07cf-4ab4-8cf7-ff167098e62c';
delete from classroom_blocks where id in ('9987d17b-f0c3-457a-9d24-c2574b84ad22','c059a45c-fc6f-4b7d-b7a1-512f57d4bd05');

-- SM1 Unit 4 ДЗ 4
select payload->>'audio' into a from classroom_blocks where id='7d466c9f-4068-40cb-b298-435e63a58611';
update classroom_blocks t set payload = jsonb_set(jsonb_set(jsonb_set(t.payload,'{audio}',to_jsonb(a),true),
       '{title}', to_jsonb('Послушай историю и выбери продукты, которые в ней были'::text)),
       '{material}', (select to_jsonb(payload->>'html') from classroom_blocks where id='7d466c9f-4068-40cb-b298-435e63a58611'), true)
  where t.id='2c20bd83-3b0d-4c37-b815-9f3662a88dc3';
delete from classroom_blocks where id='7d466c9f-4068-40cb-b298-435e63a58611';

-- SM1 Unit 7 ДЗ 4
select payload->>'audio' into a from classroom_blocks where id='20a84dbd-9d37-41e7-8b72-3a2547da4a50';
update classroom_blocks t set payload = jsonb_set(jsonb_set(t.payload,'{audio}',to_jsonb(a),true),
       '{material}', (select to_jsonb(payload->>'html') from classroom_blocks where id='20a84dbd-9d37-41e7-8b72-3a2547da4a50'), true)
  where t.id='dd04e0c4-d1e1-4841-9ba9-3704f6324dee';
delete from classroom_blocks where id='20a84dbd-9d37-41e7-8b72-3a2547da4a50';

-- SM2 Unit 4 ДЗ 4
select payload->>'audio' into a from classroom_blocks where id='5f72e39c-5401-4fb7-ac27-240dd96a7a20';
update classroom_blocks t set payload = jsonb_set(jsonb_set(jsonb_set(t.payload,'{audio}',to_jsonb(a),true),
       '{title}', to_jsonb('Послушай историю и ответь на вопрос'::text)),
       '{material}', (select to_jsonb(payload->>'html') from classroom_blocks where id='5f72e39c-5401-4fb7-ac27-240dd96a7a20'), true)
  where t.id='54352622-ddd4-4188-b553-6234625acf5c';
delete from classroom_blocks where id='5f72e39c-5401-4fb7-ac27-240dd96a7a20';

-- SM3 Unit 2 ДЗ 4 (у квиза уже есть материал с кадрами истории)
select payload->>'audio' into a from classroom_blocks where id='ff8a74c1-d752-486b-a037-7f2b601f9960';
update classroom_blocks set payload = jsonb_set(jsonb_set(payload,'{audio}',to_jsonb(a),true),
       '{title}', to_jsonb('Послушай и прочитай историю, потом выбери правильный ответ'::text))
  where id='3789f2ed-f597-475c-ad63-26fceeeb9fcc';
delete from classroom_blocks where id='ff8a74c1-d752-486b-a037-7f2b601f9960';

-- SM3 Unit 2 ДЗ 5 (образец к игре)
select payload->>'audio' into a from classroom_blocks where id='827de31d-0716-4716-a9a2-2e417689baa4';
update classroom_blocks set payload = jsonb_set(payload,'{audio}',to_jsonb(a),true)
  where id='d8d630b9-5870-4502-8f84-16aec4e20068';
delete from classroom_blocks where id='827de31d-0716-4716-a9a2-2e417689baa4';

-- SM3 Unit 2 ДЗ 6: образец ответа → в поле sample блока говорения
select payload->>'audio' into a from classroom_blocks where id='1cc39350-a00e-46fa-98b0-b7c297b8fb39';
update classroom_blocks set payload = jsonb_set(payload,'{sample}',to_jsonb(a),true)
  where id='2921049b-4e28-4df0-9ca1-53b1fd40ac6e';
delete from classroom_blocks where id='1cc39350-a00e-46fa-98b0-b7c297b8fb39';

-- ---------- 2. подводки к видео ----------

update classroom_blocks set payload = jsonb_set(payload,'{title}',
  to_jsonb('В комнате у Пенни. Посмотри видео один раз и послушай, что говорят персонажи, потом посмотри ещё раз и повторяй за ними'::text))
  where id='ae179021-a7f1-4d0a-861a-cda0468d67b1';
delete from classroom_blocks where id='c671f1db-4c18-4fa2-80a0-c8ccbe7a242c';

update classroom_blocks set payload = jsonb_set(payload,'{title}',
  to_jsonb('Посмотри видео ещё раз и составь предложения'::text))
  where id='c0e9e651-c095-4b70-8acd-260fa97422a2';
delete from classroom_blocks where id='b0d06d39-dd39-4165-bece-44b55d3b3abe';

update classroom_blocks set payload = jsonb_set(payload,'{title}',
  to_jsonb('Видео: Can you …? Посмотри один раз и послушай, потом посмотри ещё раз и повторяй за персонажами'::text))
  where id='321f203b-b6e0-4c73-86a4-2cae0ced1cd1';
delete from classroom_blocks where id='5c11d350-164f-4998-8de1-fb5715c6f577';

update classroom_blocks set payload = jsonb_set(payload,'{title}',
  to_jsonb('Видео: чем займутся подружки? Как думаешь, что они предложат — listen to music, look for shells или paint a picture?'::text))
  where id='845413dd-c93b-494b-9d3a-9b22f4492a7f';
delete from classroom_blocks where id='8fcb3209-92a9-454e-a3cc-0df18c74bc15';

update classroom_blocks set payload = jsonb_set(payload,'{title}',
  to_jsonb('Посмотри видео один раз и послушай, что говорит голос, потом посмотри ещё раз и повторяй за ним'::text))
  where id='844edba5-1e57-44a2-a1ae-34fc8782c120';
delete from classroom_blocks where id='d18f9fb9-3a8c-4c0c-81e3-8f63b914a75a';

update classroom_blocks set payload = jsonb_set(payload,'{title}',
  to_jsonb('Видео: много разной еды. Попробуй угадать, какие продукты в нём встретятся; потом посмотри ещё раз и повторяй за персонажами'::text))
  where id='d0374ac5-ad88-4675-819e-da456d06395f';
delete from classroom_blocks where id='120c9c93-d061-4ac8-ad0c-1d7bd5889c31';

-- ---------- перенумерация ----------
update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = any(ids);
update classroom_blocks t set sort_order = z.rn - 1
from (select id, row_number() over (partition by lesson_id order by sort_order) rn
        from classroom_blocks where lesson_id = any(ids)) z
where t.id = z.id;

end $$;
