-- Вычитка домашек Halloween, 21.10.2026. Точечные правки, звук остальных мест не трогается.
do $mig$
declare
  l14 uuid := 'a734ca2b-7d73-43e8-9e50-bca2b72607cf';  -- Halloween Homework · 10–12 · continuing
  l16 uuid := 'ee6701d9-7541-41d5-8f20-51930dc76321';  -- Halloween Homework · 13+ · continuing
begin
  -- 10–12 cont: на картинке банка леденцов, а карточка «a lollipop» → «lollipops»; звук очищен под «Озвучить»
  update classroom_blocks set payload = jsonb_set(jsonb_set(jsonb_set(payload,
      '{cards,10,text}', '"lollipops"'), '{cards,10,audio_tts,text}', '"lollipops"'), '{cards,10,audio}', '""')
    where lesson_id = l14 and sort_order = 0 and payload #>> '{cards,10,text}' = 'a lollipop';
  update classroom_blocks set payload = jsonb_set(jsonb_set(jsonb_set(payload,
      '{pairs,4,right}', '"lollipops"'), '{pairs,4,right_audio_tts,text}', '"lollipops"'), '{pairs,4,right_audio}', '""')
    where lesson_id = l14 and sort_order = 2 and payload #>> '{pairs,4,right}' = 'lollipop';
  -- «лишнее» показывает только картинки — заголовок про картинку; варианты lollipop → lollipops
  update classroom_blocks set payload = jsonb_set(replace(payload::text, '"text": "lollipop"', '"text": "lollipops"')::jsonb,
      '{title}', '"Найди лишнюю картинку"')
    where lesson_id = l14 and sort_order = 5 and type = 'quiz';
  -- лесенка: «лишнее» (классификация) раньше «собери слово» и диктанта
  update classroom_blocks set sort_order = sort_order + 100 where lesson_id = l14 and sort_order in (3, 4, 5);
  update classroom_blocks set sort_order = 3 where lesson_id = l14 and sort_order = 105;
  update classroom_blocks set sort_order = 4 where lesson_id = l14 and sort_order = 103;
  update classroom_blocks set sort_order = 5 where lesson_id = l14 and sort_order = 104;
  -- Golden Pumpkin: vampire и werewolf были взаимозаменяемы — добавлены приметы; «footprints of big boots» → «of somebody in big boots»
  update classroom_blocks set payload = jsonb_set(payload, '{text}', to_jsonb(
      'Last night someone stole the Golden Pumpkin! The detectives found a broken __watch__ in the square. It stopped at 9:15. '
   || 'A witness saw a long red __scarf__ in the park. Next to the old tower there were footprints of somebody in big __boots__. '
   || 'Somebody ate all the __lollipops__ at the cafe. Is the thief the __vampire__ in the black cape? Or the hairy __werewolf__? '
   || 'The __mummy__ has got an alibi: a cinema __ticket__ for nine o''clock.'))
    where lesson_id = l14 and type = 'gaps';
  -- 13+ cont, Samhain: a ghost could walk / wore a costume and a mask → ghosts / costumes and masks
  update classroom_blocks set payload = jsonb_set(payload, '{text}', to_jsonb(
      'Long ago in Ireland, people celebrated Samhain at the end of the __harvest__. They made big __bonfires__ on the hills. '
   || 'They believed that __ghosts__ could walk on Earth that night, so they wore __costumes__ and masks. '
   || 'Children carved a scary face into a __turnip__, put a __candle__ inside and made a __lantern__. '
   || 'Later, in America, people used a __pumpkin__ instead.'))
    where lesson_id = l16 and type = 'gaps';
end $mig$;
