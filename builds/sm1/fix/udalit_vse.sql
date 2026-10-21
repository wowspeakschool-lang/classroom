-- SM1 · все блоки на удаление после вычитки — один скрипт вместо одиннадцати
-- Запускать в Supabase → SQL Editor целиком. Удаляется 59 блоков.
-- Копии всех юнитов до правок: classroom_backup_sm1_fix_u0_20261021 … _u10_20261021.
-- После удаления скрипт сам выравнивает нумерацию блоков в задетых уроках.

begin;

create temporary table udalyaem_sm1 (id uuid) on commit drop;
insert into udalyaem_sm1 (id) values
 ('0c5031ef-6098-4fa9-8424-6d4684e6e6b9'::uuid),
 ('1233a146-7fa4-4cc9-a76e-eded971caecc'::uuid),
 ('19a9c799-fa1f-410d-b576-b30f1b739a73'::uuid),
 ('26049fcb-e245-4fce-9aa0-57780d9b49a5'::uuid),
 ('28b2149b-d63d-4bdd-9961-30dba2e91679'::uuid),
 ('299c259a-9575-4271-8bd5-2dbf065e490d'::uuid),
 ('2abd9de9-0096-44af-91b6-b5664fbd5432'::uuid),
 ('2bbd0908-e12f-4e7e-8d65-691d9bd8bde5'::uuid),
 ('2bee98a6-9ccb-470e-9f39-805c3839e6f1'::uuid),
 ('329d6515-4489-4a2c-9348-97e806f345b5'::uuid),
 ('36aa365e-b364-4699-83ee-2da3e86474a2'::uuid),
 ('4a0e60b8-9dac-4253-b2e0-ac0168774304'::uuid),
 ('51a71093-52c2-42ac-a776-b0b9cc3a96bc'::uuid),
 ('54b38a0b-4323-4181-9db8-31e2123ae745'::uuid),
 ('54f9c9a9-437d-4c3e-81cf-28600764d6b2'::uuid),
 ('56408011-e824-4d08-a6e9-53f31314b98e'::uuid),
 ('5e4f7ae2-a4f3-4da0-ba82-14c9052a364a'::uuid),
 ('63def77f-ca2b-4c8f-a045-71d89aeaef81'::uuid),
 ('6436d0c3-1888-4def-8450-6c7bed525418'::uuid),
 ('66c2e933-c4c3-4216-948d-11a07bf71491'::uuid),
 ('6d322769-b435-4220-9704-1d3a308e16f6'::uuid),
 ('6df6d031-eb4f-4b6e-a527-a5ec7e7c3b22'::uuid),
 ('6ed74b16-2ce7-44e9-9ebd-2fbf2d7ba442'::uuid),
 ('6f4c737a-e95d-4f60-945c-fdbc2a2d9fd6'::uuid),
 ('70534559-df31-4f07-a8d8-a37958aeac20'::uuid),
 ('727b1f7a-cc74-4c1d-9794-690061d80bb8'::uuid),
 ('734b9ca3-4a71-4b5d-9f4a-d4d06884c87e'::uuid),
 ('7451bc62-3f60-4757-81bf-ca2087ccc719'::uuid),
 ('851a19a5-9d79-4c39-aec1-176003f52a6e'::uuid),
 ('86359964-eac5-4fd2-b279-e2a4bb4bfb3c'::uuid),
 ('87990160-7971-4935-968a-fc303151908a'::uuid),
 ('891c24c3-b5d8-4abe-894c-53490fc397f5'::uuid),
 ('89cbeceb-1348-4455-87f3-6156fb1512ea'::uuid),
 ('8c0708ef-f936-4d4c-9cc0-a9562d34a81b'::uuid),
 ('8c52bc7f-ce30-4db8-af4f-3c14af567bd5'::uuid),
 ('8f7c279d-8d2c-44a8-8058-3a500bab6340'::uuid),
 ('903263a1-c286-44c9-876e-ae985db0c408'::uuid),
 ('983d7c89-02fe-4ebd-86cd-a872501a7144'::uuid),
 ('9f8b95c0-f4fb-4e11-830f-8743c2c6ed3e'::uuid),
 ('a1142212-00ab-4876-8a73-192ec3480c40'::uuid),
 ('a2b6bed6-9427-4481-9e29-97dfe4cd3396'::uuid),
 ('ab0f48ca-23af-4c8c-afc9-6620bdbdfd87'::uuid),
 ('ba3e282d-9894-4245-b461-8d7c3692404f'::uuid),
 ('ba5470bb-6905-4aa1-973f-d49c313b0424'::uuid),
 ('ba5e41e6-5c8a-4ffd-b46e-faed4217206e'::uuid),
 ('bd69f418-ef84-4eee-ad7c-c1f6727f4e2e'::uuid),
 ('c6fec3c6-85d1-442b-a4cb-caddd8105406'::uuid),
 ('c9b0ffa2-d747-47e0-8bca-1acf4cb40394'::uuid),
 ('ca74cd17-f866-4d41-b2c9-1d1afd4162a3'::uuid),
 ('d65feea7-0b66-4209-a578-19cf4485f2a4'::uuid),
 ('d88ee1c8-fc40-47bc-868a-ccb8f0757842'::uuid),
 ('de55d72d-a6f8-4240-aa62-21962ead93b5'::uuid),
 ('e893d9a0-d135-415c-bec1-53ada7ef188f'::uuid),
 ('eb5e4288-24eb-46b7-b86c-55aec9e34273'::uuid),
 ('f1ba0328-5714-44a3-a36f-3b896beb0530'::uuid),
 ('f61e4ef1-d518-4fd7-a70c-732ecd62aea4'::uuid),
 ('f6344408-8f6d-48ee-94b1-51267fa95234'::uuid),
 ('f6b46847-bbac-4442-9e95-2f4abf51873f'::uuid),
 ('ff83901c-ca47-4c2a-a6ba-01135d5ec5dc'::uuid);

create temporary table zatronutye_uroki_sm1 on commit drop as
select distinct lesson_id from classroom_blocks where id in (select id from udalyaem_sm1);

delete from classroom_blocks where id in (select id from udalyaem_sm1);

-- нумерация блоков снова подряд с нуля
with novyy as (
  select b.id, row_number() over (partition by b.lesson_id order by b.sort_order) - 1 as n
  from classroom_blocks b
  where b.lesson_id in (select lesson_id from zatronutye_uroki_sm1))
update classroom_blocks b set sort_order = novyy.n + 1000
from novyy where b.id = novyy.id;

update classroom_blocks set sort_order = sort_order - 1000
where lesson_id in (select lesson_id from zatronutye_uroki_sm1) and sort_order >= 1000;

commit;
