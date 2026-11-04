-- Разделители перед серией «Составь предложение», которая стала одним заданием
-- Решение Анны 04.11.2026 («134 согласна»): у тех, что обещают серию, обещание
-- убрать, с правилом — оставить, остальные — удалить.
--
-- Переписывание (10 блоков) уже применено из чата. Здесь остаётся удаление
-- 40 блоков и перенумерация затронутых уроков: через MCP удаление зависает на
-- подтверждении, поэтому запускать в SQL Editor.
--
-- Копия всех блоков 49 уроков — classroom_backup_razdeliteli_20261104 (590 строк).

delete from classroom_blocks where id in (
  'dc37363a-9084-40f9-aec9-ef82a2b5784d','5bd678cc-00c8-4430-b6ae-c79cc2a47ac7','4ef1fb1d-d23a-4888-9f3f-1274399339ac',
  'd6a19ad3-bb70-461f-96e9-fb859265b9e7','7dba1f6e-2d08-4f01-9240-db2ec2829ac2','fcad0549-0452-4b4a-9306-1b913c4f5f79',
  'b85edc1b-270b-4cc2-a88d-07c333f73db2','c3acd056-5108-4255-9331-038a4656f4e4','017b59c7-1806-446d-9f65-697cfaa26517',
  '233a7ba4-639a-4e68-9153-efe9ac1aead9','aaf77424-7462-4a99-aee5-1b01effcdf99','4a7a51b2-1266-4393-94a4-e529a7744db4',
  '87bc7080-febf-4fd2-8ab2-027ce84a698b','f75a9261-9b24-4a35-ab71-fd80bc5f20a5','6f7190d4-2f51-427f-914d-a8fa97c2f6e4',
  '9803c881-e86c-46c4-8e8e-8660971cfab5','c806279a-ba15-481f-995e-ad3673cc9080','3a069790-7d24-47e2-af7b-7b4421d055a5',
  '57c52562-bd9b-467a-95f1-0e3ac6c4f076','22236cf3-656d-4948-8ba5-23fa2425877f','0008a00a-8000-49db-a52f-6d5375d0407d',
  'bca202a2-d763-4952-a515-b5a522513f30','93966576-4340-406c-a807-6b57bca2280d','0f87c439-a3b8-4690-a37b-5bda60ae762e',
  '5cec3cc8-0b61-41fb-a154-48622f6774f7','db03d236-eeed-451f-b582-dce7d8ca0ce2','f6abc476-0cbe-47bf-95b6-08f240a0ca0a',
  'd1281c3b-3432-4795-9e1d-d42eb63b3a70','ca67ee35-a226-4485-8717-b41c680826f3','f41a3683-6712-4f98-9170-200bc3770ed4',
  '909a406c-5dd8-4208-afc0-c65c9af6e571','2f91845a-575a-4180-a7e6-a4dfc373ebfa','b5eb1ca4-6591-4eb3-a7a9-daf4cb8bb946',
  '74d0d214-228b-4338-828f-662245c12503','ad078053-5af2-4e6e-a744-d0d5a26cbbdf','1b92f7b7-d3f2-458c-be90-3caa6b24ab41',
  '7af8bfc9-3de4-44ee-abaa-aebb236a3a3a','feeb2dec-7072-4e05-8867-4591550d1cd1','e1f6715f-ff7c-4deb-83d5-5bad5278e7f5',
  'f4584ae5-bf99-46b4-b9ab-b2ed8f5f8840');

-- Перенумерация: номера уводим за 1000, потом расставляем подряд с нуля.
do $$
declare v_les uuid[];
begin
  select array_agg(distinct lesson_id) into v_les from classroom_backup_razdeliteli_20261104;

  update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = any(v_les);

  with ord as (
    select id, row_number() over (partition by lesson_id order by sort_order) - 1 as n
    from classroom_blocks where lesson_id = any(v_les)
  )
  update classroom_blocks b set sort_order = o.n from ord o where o.id = b.id;

  if exists (select 1 from classroom_blocks where lesson_id = any(v_les) and sort_order >= 1000) then
    raise exception 'перенумерация не завершена';
  end if;
end $$;
