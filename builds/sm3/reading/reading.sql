-- SM3, тесты юнитов 1-8: чтение (skill=reading) и диктант (skill=writing).
-- Решение Анны от 03.11.2026, пункт 63. Тексты и ключи - builds/sm3/reading/teksty.md.
-- Собрано скриптом builds/sm3/reading/reading_build.py, руками не править.
-- Только insert и update; delete/drop нет. Идемпотентно: залитый юнит пропускается.

-- копия всех блоков восьми тестов до правки
create table if not exists classroom_backup_sm3_reading_20261103 as
select b.*
from classroom_blocks b
join classroom_lessons l on l.id = b.lesson_id
join classroom_units u on u.id = l.unit_id
join classroom_courses c on c.id = u.course_id
where c.slug = 'sm3' and l.kind = 'test' and u.sort_order between 1 and 8;

do $$
declare
  v_media  text := 'https://classroom.wowteach.ru/media/';
  v_data   jsonb := $json$[
    {"unit": 1, "text": {"html": "<p><b>READING.</b> Прочитай текст и ответь, верно или неверно.</p><p>Clara is nine years old and she goes to Hill Street School. On Monday she has Maths, Art and I.T. She loves drawing animals in her Art book. Clara doesn’t like studying History, but she likes reading about volcanoes in Science. She has to be on time for school every morning, but she doesn’t have to wear a uniform. After school Clara likes playing the guitar with her sister.</p>"}, "tf": {"title": "Верно или неверно?", "skill": "reading", "statements": [{"text": "Clara goes to Hill Street School.", "correct": true}, {"text": "On Monday Clara has Maths, Art and I.T.", "correct": true}, {"text": "Clara likes studying History.", "correct": false}, {"text": "Clara has to wear a uniform.", "correct": false}, {"text": "After school Clara likes playing the guitar.", "correct": true}]}, "dict": {"title": "DICTATION ✍️ Посмотри на картинку и напиши слово.", "skill": "writing", "needs_review": false, "items": [{"prompt": "1.", "image": "@@MEDIA@@sm3/u1/shape_square.webp", "accept": ["square", "Square", "a square"]}, {"prompt": "2.", "image": "@@MEDIA@@sm3/u1/shape_circle.webp", "accept": ["circle", "Circle", "a circle"]}, {"prompt": "3.", "image": "@@MEDIA@@sm3/u1/shape_triangle.webp", "accept": ["triangle", "Triangle", "a triangle"]}, {"prompt": "4.", "image": "@@MEDIA@@sm3/u1/shape_rectangle.webp", "accept": ["rectangle", "Rectangle", "a rectangle"]}, {"prompt": "5.", "image": "@@MEDIA@@sm3/u1/shape_hexagon.webp", "accept": ["hexagon", "Hexagon", "a hexagon"]}]}},
    {"unit": 2, "text": {"html": "<p><b>READING.</b> Прочитай текст и ответь, верно или неверно.</p><p>Bruno is helping his mum in the kitchen. There are some onions and some peas on the table. There is some salad in the fridge, but there isn’t any soup. Bruno would like some apple juice, but there isn’t any at home, so he drinks some water. His sister says, “Shall we make some sandwiches?” There are five rolls for dinner. Bruno hasn’t got any chocolate, but he has got a big red apple.</p>"}, "tf": {"title": "Верно или неверно?", "skill": "reading", "statements": [{"text": "There are some onions on the table.", "correct": true}, {"text": "There is some soup in the fridge.", "correct": false}, {"text": "Bruno drinks some water.", "correct": true}, {"text": "Bruno’s sister would like to make a cake.", "correct": false}, {"text": "There are five rolls for dinner.", "correct": true}]}, "dict": {"title": "DICTATION ✍️ Посмотри на картинку и напиши слово.", "skill": "writing", "needs_review": false, "items": [{"prompt": "1.", "image": "@@MEDIA@@sm3/u2/food_cheese.webp", "accept": ["cheese", "Cheese"]}, {"prompt": "2.", "image": "@@MEDIA@@sm3/u2/food_lemonade.webp", "accept": ["lemonade", "Lemonade"]}, {"prompt": "3.", "image": "@@MEDIA@@sm3/u2/food_sausages.webp", "accept": ["sausages", "Sausages"]}, {"prompt": "4.", "image": "@@MEDIA@@sm3/u2/food_pineapple.webp", "accept": ["pineapple", "Pineapple", "a pineapple"]}, {"prompt": "5.", "image": "@@MEDIA@@sm3/u2/food_vegetables.webp", "accept": ["vegetables", "Vegetables"]}]}},
    {"unit": 3, "text": {"html": "<p><b>READING.</b> Прочитай текст и ответь, верно или неверно.</p><p>Nadia lives with her mum, her dad and her baby brother. On Tuesday and Friday she has to dry the dishes after dinner. Her dad cooks and her mum does the shopping on Sunday. Nadia never sweeps the floor, but she always tidies up her room before bed. She has dinner at quarter to seven and she reads a book at half past eight. On Saturday morning Nadia and her dad take the dog for a walk in the park.</p>"}, "tf": {"title": "Верно или неверно?", "skill": "reading", "statements": [{"text": "Nadia has to dry the dishes on Tuesday and Friday.", "correct": true}, {"text": "Nadia’s mum does the shopping on Sunday.", "correct": true}, {"text": "Nadia always sweeps the floor.", "correct": false}, {"text": "Nadia has dinner at quarter to seven.", "correct": true}, {"text": "On Saturday morning Nadia and her dad go to the cinema.", "correct": false}]}, "dict": {"title": "DICTATION ✍️ Посмотри на картинку и напиши слово.", "skill": "writing", "needs_review": false, "items": [{"prompt": "1.", "image": "@@MEDIA@@sm3/u3/job_vet.webp", "accept": ["vet", "Vet", "a vet"]}, {"prompt": "2.", "image": "@@MEDIA@@sm3/u3/job_nurse.webp", "accept": ["nurse", "Nurse", "a nurse"]}, {"prompt": "3.", "image": "@@MEDIA@@sm3/u3/job_teacher.webp", "accept": ["teacher", "Teacher", "a teacher"]}, {"prompt": "4.", "image": "@@MEDIA@@sm3/u3/job_cleaner.webp", "accept": ["cleaner", "Cleaner", "a cleaner"]}, {"prompt": "5.", "image": "@@MEDIA@@sm3/u3/job_firefighter.webp", "accept": ["firefighter", "Firefighter", "a firefighter"]}]}},
    {"unit": 4, "text": {"html": "<p><b>READING.</b> Прочитай текст и ответь, верно или неверно.</p><p>Today is Saturday and Leo’s family is very busy. Leo is going to the sports centre to play basketball with his cousin. His mum is going to the market square to buy some fruit. His dad is going to the bus station to meet Grandma. The bus station is behind the big park, next to the bank. Leo’s sister is at home with the cat. The cat is under the table, in front of her ball.</p>"}, "tf": {"title": "Верно или неверно?", "skill": "reading", "statements": [{"text": "Leo is going to the sports centre to play basketball.", "correct": true}, {"text": "Leo’s mum is going to the supermarket.", "correct": false}, {"text": "The bus station is behind the big park.", "correct": true}, {"text": "The bus station is next to the bank.", "correct": true}, {"text": "The cat is above the table.", "correct": false}]}, "dict": {"title": "DICTATION ✍️ Посмотри на картинку и напиши слово.", "skill": "writing", "needs_review": false, "items": [{"prompt": "1.", "image": "@@MEDIA@@sm3/u4/town_funfair.webp", "accept": ["funfair", "Funfair", "a funfair"]}, {"prompt": "2.", "image": "@@MEDIA@@sm3/u4/town_car_park.webp", "accept": ["car park", "Car park", "a car park", "carpark"]}, {"prompt": "3.", "image": "@@MEDIA@@sm3/u4/tower_lighthouse.webp", "accept": ["lighthouse", "Lighthouse", "a lighthouse"]}, {"prompt": "4.", "image": "@@MEDIA@@sm3/u4/tower_skyscraper.webp", "accept": ["skyscraper", "Skyscraper", "a skyscraper"]}, {"prompt": "5.", "image": "@@MEDIA@@sm3/u4/tower_clock.webp", "accept": ["clock tower", "Clock tower", "a clock tower", "clocktower"]}]}},
    {"unit": 5, "text": {"html": "<p><b>READING.</b> Прочитай текст и ответь, верно или неверно.</p><p>Last Saturday Lara and her class were at the sea museum. There were a lot of old boats in the first room and there was a big map of the ocean on the wall. Lara’s favourite room was the dinosaur room, because there was a megalodon tooth in it. The children were very quiet, so the teacher was happy. There weren’t any books about the sea in the museum shop. At four o’clock everybody was on the bus.</p>"}, "tf": {"title": "Верно или неверно?", "skill": "reading", "statements": [{"text": "Last Saturday Lara was at the sea museum.", "correct": true}, {"text": "There was a big map of the ocean on the wall.", "correct": true}, {"text": "Lara’s favourite room was the boat room.", "correct": false}, {"text": "The children were very noisy.", "correct": false}, {"text": "At four o’clock everybody was on the bus.", "correct": true}]}, "dict": {"title": "DICTATION ✍️ Посмотри на картинку и напиши слово.", "skill": "writing", "needs_review": false, "items": [{"prompt": "1.", "image": "@@MEDIA@@sm3/u5/sea_octopus.webp", "accept": ["octopus", "Octopus", "an octopus"]}, {"prompt": "2.", "image": "@@MEDIA@@sm3/u5/sea_shark.webp", "accept": ["shark", "Shark", "a shark"]}, {"prompt": "3.", "image": "@@MEDIA@@sm3/u5/sea_jellyfish.webp", "accept": ["jellyfish", "Jellyfish", "a jellyfish"]}, {"prompt": "4.", "image": "@@MEDIA@@sm3/u5/sea_shell.webp", "accept": ["shell", "Shell", "a shell"]}, {"prompt": "5.", "image": "@@MEDIA@@sm3/u5/sea_coral.webp", "accept": ["coral", "Coral"]}]}},
    {"unit": 6, "text": {"html": "<p><b>READING.</b> Прочитай текст и ответь, верно или неверно.</p><p>Toby and his dad are in the gadget shop in the town. Toby would like a new games console, because his old console is slower than his friend’s console. The blue laptop is two hundred pounds — it is more expensive than the electric fan. The walkie-talkies are twenty pounds, and they are cheaper than the laptop. Toby’s favourite gadget is his bike, because it is faster than the bus in the morning.</p>"}, "tf": {"title": "Верно или неверно?", "skill": "reading", "statements": [{"text": "Toby and his dad are in the gadget shop.", "correct": true}, {"text": "Toby’s old console is faster than his friend’s console.", "correct": false}, {"text": "The blue laptop is more expensive than the electric fan.", "correct": true}, {"text": "The walkie-talkies are cheaper than the laptop.", "correct": true}, {"text": "Toby’s favourite gadget is his games console.", "correct": false}]}, "dict": {"title": "DICTATION ✍️ Посмотри на картинку и напиши слово.", "skill": "writing", "needs_review": false, "items": [{"prompt": "1.", "image": "@@MEDIA@@sm3/u6/gad_tablet.webp", "accept": ["tablet", "Tablet", "a tablet"]}, {"prompt": "2.", "image": "@@MEDIA@@sm3/u6/gad_lift.webp", "accept": ["lift", "Lift", "a lift"]}, {"prompt": "3.", "image": "@@MEDIA@@sm3/u6/gad_phone.webp", "accept": ["mobile phone", "Mobile phone", "a mobile phone", "phone", "Phone"]}, {"prompt": "4.", "image": "@@MEDIA@@sm3/u6/gad_toothbrush.webp", "accept": ["toothbrush", "Toothbrush", "electric toothbrush", "an electric toothbrush", "a toothbrush"]}, {"prompt": "5.", "image": "@@MEDIA@@sm3/u6/gad_torch.webp", "accept": ["torch", "Torch", "a torch"]}]}},
    {"unit": 7, "text": {"html": "<p><b>READING.</b> Прочитай текст и ответь, верно или неверно.</p><p>Last Saturday Bella played football with her friends in the park. In the evening she had a stomachache, because she ate a lot of chocolate and drank two glasses of cola. Her dad cooked some soup, but Bella didn’t eat it. On Sunday morning she felt better. She watched a film with her brother and wrote a letter to her grandma. On Monday Bella went to school and played volleyball with her class again.</p>"}, "tf": {"title": "Верно или неверно?", "skill": "reading", "statements": [{"text": "On Saturday Bella played football in the park.", "correct": true}, {"text": "Bella drank two glasses of water.", "correct": false}, {"text": "Bella’s dad cooked some soup.", "correct": true}, {"text": "On Sunday morning Bella felt worse.", "correct": false}, {"text": "On Monday Bella went to school.", "correct": true}]}, "dict": {"title": "DICTATION ✍️ Посмотри на картинку и напиши слово.", "skill": "writing", "needs_review": false, "items": [{"prompt": "1.", "image": "@@MEDIA@@sm3/u7/ill_cold.webp", "accept": ["cold", "Cold", "a cold"]}, {"prompt": "2.", "image": "@@MEDIA@@sm3/u7/med_nurse.webp", "accept": ["nurse", "Nurse", "a nurse"]}, {"prompt": "3.", "image": "@@MEDIA@@sm3/u7/med_medicine.webp", "accept": ["medicine", "Medicine"]}, {"prompt": "4.", "image": "@@MEDIA@@sm3/u7/ill_headache.webp", "accept": ["headache", "Headache", "a headache"]}, {"prompt": "5.", "image": "@@MEDIA@@sm3/u7/ill_toothache.webp", "accept": ["toothache", "Toothache", "a toothache"]}]}},
    {"unit": 8, "text": {"html": "<p><b>READING.</b> Прочитай текст и ответь, верно или неверно.</p><p>Last summer Oscar went to Brazil with his family. They stayed with his uncle in a small house near the river for ten days. Oscar played football on the beach with his cousins every morning. One day they went on a boat on the Amazon river and they saw a lot of birds. Oscar didn’t see any monkeys, but he liked the boat a lot. He sent a postcard to his teacher.</p>"}, "tf": {"title": "Верно или неверно?", "skill": "reading", "statements": [{"text": "Oscar went to Brazil last summer.", "correct": true}, {"text": "Oscar and his family stayed in a big hotel.", "correct": false}, {"text": "Oscar played football every morning.", "correct": true}, {"text": "Oscar saw a lot of monkeys.", "correct": false}, {"text": "Oscar sent a postcard to his teacher.", "correct": true}]}, "dict": {"title": "DICTATION ✍️ Посмотри на картинку и напиши слово.", "skill": "writing", "needs_review": false, "items": [{"prompt": "1.", "image": "@@MEDIA@@sm3/u8/country_india.webp", "accept": ["India", "india"]}, {"prompt": "2.", "image": "@@MEDIA@@sm3/u8/country_mexico.webp", "accept": ["Mexico", "mexico"]}, {"prompt": "3.", "image": "@@MEDIA@@sm3/u8/country_chile.webp", "accept": ["Chile", "chile"]}, {"prompt": "4.", "image": "@@MEDIA@@sm3/u8/country_spain.webp", "accept": ["Spain", "spain"]}, {"prompt": "5.", "image": "@@MEDIA@@sm3/u8/country_australia.webp", "accept": ["Australia", "australia"]}]}}
  ]$json$;
  v_rec    jsonb;
  v_unit   int;
  v_lesson uuid;
  v_l      int;
begin
  for v_rec in select * from jsonb_array_elements(v_data) loop
    v_unit := (v_rec->>'unit')::int;

    select l.id into v_lesson
    from classroom_courses c
    join classroom_units u on u.course_id = c.id
    join classroom_lessons l on l.unit_id = u.id
    where c.slug = 'sm3' and u.sort_order = v_unit and l.kind = 'test';

    if v_lesson is null then
      raise exception 'SM3, юнит %: тест не найден', v_unit;
    end if;

    -- идемпотентность: уже залито — юнит пропускаем
    if exists (select 1 from classroom_blocks b
               where b.lesson_id = v_lesson
                 and (coalesce(b.payload->>'title', '') like 'DICTATION%'
                      or coalesce(b.payload->>'html', '') like '%READING.%')) then
      raise notice 'SM3, юнит %: чтение и диктант уже есть, пропускаю', v_unit;
      continue;
    end if;

    -- место вставки: перед блоком аудирования
    select b.sort_order into v_l
    from classroom_blocks b
    where b.lesson_id = v_lesson and b.payload->>'skill' = 'listening'
    order by b.sort_order limit 1;

    if v_l is null then
      raise exception 'SM3, юнит %: блок аудирования не найден', v_unit;
    end if;

    -- хвост сдвигаем в запас (+1000) и раскладываем обратно:
    -- два блока до аудирования (текст и «верно / неверно»), один после (диктант)
    update classroom_blocks set sort_order = sort_order + 1000
      where lesson_id = v_lesson and sort_order >= v_l;
    update classroom_blocks set sort_order = v_l + 2
      where lesson_id = v_lesson and sort_order = v_l + 1000;
    update classroom_blocks set sort_order = sort_order - 1000 + 3
      where lesson_id = v_lesson and sort_order > v_l + 1000;

    insert into classroom_blocks (lesson_id, type, payload, sort_order) values
      (v_lesson, 'text', v_rec->'text', v_l),
      (v_lesson, 'truefalse', v_rec->'tf', v_l + 1),
      (v_lesson, 'exact_input',
        replace((v_rec->'dict')::text, '@@MEDIA@@', v_media)::jsonb, v_l + 3);
  end loop;
end $$;
