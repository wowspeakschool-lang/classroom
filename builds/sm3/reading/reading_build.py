#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""Сборка SQL: чтение (reading) и диктант (writing) в тесты SM3, юниты 1-8.

Решение Анны от 03.11.2026, пункт 63. Тексты, вопросы и ключи - teksty.md.
Порядок разделов повторяет тест юнита 0: ... -> READING (текст + верно/неверно)
-> LISTENING -> DICTATION -> SPEAKING.

Запуск:  python3.13 builds/sm3/reading/reading_build.py > builds/sm3/reading/reading.sql
"""

import json
import sys

READ_LEAD = "<p><b>READING.</b> Прочитай текст и ответь, верно или неверно.</p>"
TF_TITLE = "Верно или неверно?"
DICT_TITLE = "DICTATION ✍️ Посмотри на картинку и напиши слово."

UNITS = [
    {
        "unit": 1,
        "theme": "School",
        "text": (
            "Clara is nine years old and she goes to Hill Street School. On Monday she has "
            "Maths, Art and I.T. She loves drawing animals in her Art book. Clara doesn’t like "
            "studying History, but she likes reading about volcanoes in Science. She has to be "
            "on time for school every morning, but she doesn’t have to wear a uniform. After "
            "school Clara likes playing the guitar with her sister."
        ),
        "statements": [
            ("Clara goes to Hill Street School.", True),
            ("On Monday Clara has Maths, Art and I.T.", True),
            ("Clara likes studying History.", False),
            ("Clara has to wear a uniform.", False),
            ("After school Clara likes playing the guitar.", True),
        ],
        "dictation": [
            ("u1/shape_square.webp", ["square", "Square", "a square"]),
            ("u1/shape_circle.webp", ["circle", "Circle", "a circle"]),
            ("u1/shape_triangle.webp", ["triangle", "Triangle", "a triangle"]),
            ("u1/shape_rectangle.webp", ["rectangle", "Rectangle", "a rectangle"]),
            ("u1/shape_hexagon.webp", ["hexagon", "Hexagon", "a hexagon"]),
        ],
    },
    {
        "unit": 2,
        "theme": "Food",
        "text": (
            "Bruno is helping his mum in the kitchen. There are some onions and some peas on "
            "the table. There is some salad in the fridge, but there isn’t any soup. Bruno would "
            "like some apple juice, but there isn’t any at home, so he drinks some water. His "
            "sister says, “Shall we make some sandwiches?” There are five rolls for dinner. "
            "Bruno hasn’t got any chocolate, but he has got a big red apple."
        ),
        "statements": [
            ("There are some onions on the table.", True),
            ("There is some soup in the fridge.", False),
            ("Bruno drinks some water.", True),
            ("Bruno’s sister would like to make a cake.", False),
            ("There are five rolls for dinner.", True),
        ],
        "dictation": [
            ("u2/food_cheese.webp", ["cheese", "Cheese"]),
            ("u2/food_lemonade.webp", ["lemonade", "Lemonade"]),
            ("u2/food_sausages.webp", ["sausages", "Sausages"]),
            ("u2/food_pineapple.webp", ["pineapple", "Pineapple", "a pineapple"]),
            ("u2/food_vegetables.webp", ["vegetables", "Vegetables"]),
        ],
    },
    {
        "unit": 3,
        "theme": "At home",
        "text": (
            "Nadia lives with her mum, her dad and her baby brother. On Tuesday and Friday she "
            "has to dry the dishes after dinner. Her dad cooks and her mum does the shopping on "
            "Sunday. Nadia never sweeps the floor, but she always tidies up her room before bed. "
            "She has dinner at quarter to seven and she reads a book at half past eight. On "
            "Saturday morning Nadia and her dad take the dog for a walk in the park."
        ),
        "statements": [
            ("Nadia has to dry the dishes on Tuesday and Friday.", True),
            ("Nadia’s mum does the shopping on Sunday.", True),
            ("Nadia always sweeps the floor.", False),
            ("Nadia has dinner at quarter to seven.", True),
            ("On Saturday morning Nadia and her dad go to the cinema.", False),
        ],
        "dictation": [
            ("u3/job_vet.webp", ["vet", "Vet", "a vet"]),
            ("u3/job_nurse.webp", ["nurse", "Nurse", "a nurse"]),
            ("u3/job_teacher.webp", ["teacher", "Teacher", "a teacher"]),
            ("u3/job_cleaner.webp", ["cleaner", "Cleaner", "a cleaner"]),
            ("u3/job_firefighter.webp", ["firefighter", "Firefighter", "a firefighter"]),
        ],
    },
    {
        "unit": 4,
        "theme": "In the town",
        "text": (
            "Today is Saturday and Leo’s family is very busy. Leo is going to the sports centre "
            "to play basketball with his cousin. His mum is going to the market square to buy "
            "some fruit. His dad is going to the bus station to meet Grandma. The bus station is "
            "behind the big park, next to the bank. Leo’s sister is at home with the cat. The cat "
            "is under the table, in front of her ball."
        ),
        "statements": [
            ("Leo is going to the sports centre to play basketball.", True),
            ("Leo’s mum is going to the supermarket.", False),
            ("The bus station is behind the big park.", True),
            ("The bus station is next to the bank.", True),
            ("The cat is above the table.", False),
        ],
        "dictation": [
            ("u4/town_funfair.webp", ["funfair", "Funfair", "a funfair"]),
            ("u4/town_car_park.webp", ["car park", "Car park", "a car park", "carpark"]),
            ("u4/tower_lighthouse.webp", ["lighthouse", "Lighthouse", "a lighthouse"]),
            ("u4/tower_skyscraper.webp", ["skyscraper", "Skyscraper", "a skyscraper"]),
            ("u4/tower_clock.webp", ["clock tower", "Clock tower", "a clock tower", "clocktower"]),
        ],
    },
    {
        "unit": 5,
        "theme": "Under the sea",
        "text": (
            "Last Saturday Lara and her class were at the sea museum. There were a lot of old "
            "boats in the first room and there was a big map of the ocean on the wall. Lara’s "
            "favourite room was the dinosaur room, because there was a megalodon tooth in it. "
            "The children were very quiet, so the teacher was happy. There weren’t any books "
            "about the sea in the museum shop. At four o’clock everybody was on the bus."
        ),
        "statements": [
            ("Last Saturday Lara was at the sea museum.", True),
            ("There was a big map of the ocean on the wall.", True),
            ("Lara’s favourite room was the boat room.", False),
            ("The children were very noisy.", False),
            ("At four o’clock everybody was on the bus.", True),
        ],
        "dictation": [
            ("u5/sea_octopus.webp", ["octopus", "Octopus", "an octopus"]),
            ("u5/sea_shark.webp", ["shark", "Shark", "a shark"]),
            ("u5/sea_jellyfish.webp", ["jellyfish", "Jellyfish", "a jellyfish"]),
            ("u5/sea_shell.webp", ["shell", "Shell", "a shell"]),
            ("u5/sea_coral.webp", ["coral", "Coral"]),
        ],
    },
    {
        "unit": 6,
        "theme": "Gadgets",
        "text": (
            "Toby and his dad are in the gadget shop in the town. Toby would like a new games "
            "console, because his old console is slower than his friend’s console. The blue "
            "laptop is two hundred pounds — it is more expensive than the electric fan. The "
            "walkie-talkies are twenty pounds, and they are cheaper than the laptop. Toby’s "
            "favourite gadget is his bike, because it is faster than the bus in the morning."
        ),
        "statements": [
            ("Toby and his dad are in the gadget shop.", True),
            ("Toby’s old console is faster than his friend’s console.", False),
            ("The blue laptop is more expensive than the electric fan.", True),
            ("The walkie-talkies are cheaper than the laptop.", True),
            ("Toby’s favourite gadget is his games console.", False),
        ],
        "dictation": [
            ("u6/gad_tablet.webp", ["tablet", "Tablet", "a tablet"]),
            ("u6/gad_lift.webp", ["lift", "Lift", "a lift"]),
            ("u6/gad_phone.webp", ["mobile phone", "Mobile phone", "a mobile phone", "phone", "Phone"]),
            ("u6/gad_toothbrush.webp", ["toothbrush", "Toothbrush", "electric toothbrush",
                                        "an electric toothbrush", "a toothbrush"]),
            ("u6/gad_torch.webp", ["torch", "Torch", "a torch"]),
        ],
    },
    {
        "unit": 7,
        "theme": "At the doctor’s",
        "text": (
            "Last Saturday Bella played football with her friends in the park. In the evening she "
            "had a stomachache, because she ate a lot of chocolate and drank two glasses of cola. "
            "Her dad cooked some soup, but Bella didn’t eat it. On Sunday morning she felt better. "
            "She watched a film with her brother and wrote a letter to her grandma. On Monday "
            "Bella went to school and played volleyball with her class again."
        ),
        "statements": [
            ("On Saturday Bella played football in the park.", True),
            ("Bella drank two glasses of water.", False),
            ("Bella’s dad cooked some soup.", True),
            ("On Sunday morning Bella felt worse.", False),
            ("On Monday Bella went to school.", True),
        ],
        "dictation": [
            ("u7/ill_cold.webp", ["cold", "Cold", "a cold"]),
            ("u7/med_nurse.webp", ["nurse", "Nurse", "a nurse"]),
            ("u7/med_medicine.webp", ["medicine", "Medicine"]),
            ("u7/ill_headache.webp", ["headache", "Headache", "a headache"]),
            ("u7/ill_toothache.webp", ["toothache", "Toothache", "a toothache"]),
        ],
    },
    {
        "unit": 8,
        "theme": "Countries",
        "text": (
            "Last summer Oscar went to Brazil with his family. They stayed with his uncle in a "
            "small house near the river for ten days. Oscar played football on the beach with his "
            "cousins every morning. One day they went on a boat on the Amazon river and they saw "
            "a lot of birds. Oscar didn’t see any monkeys, but he liked the boat a lot. He sent a "
            "postcard to his teacher."
        ),
        "statements": [
            ("Oscar went to Brazil last summer.", True),
            ("Oscar and his family stayed in a big hotel.", False),
            ("Oscar played football every morning.", True),
            ("Oscar saw a lot of monkeys.", False),
            ("Oscar sent a postcard to his teacher.", True),
        ],
        "dictation": [
            ("u8/country_india.webp", ["India", "india"]),
            ("u8/country_mexico.webp", ["Mexico", "mexico"]),
            ("u8/country_chile.webp", ["Chile", "chile"]),
            ("u8/country_spain.webp", ["Spain", "spain"]),
            ("u8/country_australia.webp", ["Australia", "australia"]),
        ],
    },
]


def j(obj: dict) -> str:
    return json.dumps(obj, ensure_ascii=False)


def unit_data(u: dict) -> dict:
    """Три блока одного юнита в том виде, в каком они лягут в payload."""
    return {
        "unit": u["unit"],
        "text": {"html": READ_LEAD + "<p>" + u["text"] + "</p>"},
        "tf": {
            "title": TF_TITLE,
            "skill": "reading",
            "statements": [{"text": s, "correct": c} for s, c in u["statements"]],
        },
        "dict": {
            "title": DICT_TITLE,
            "skill": "writing",
            "needs_review": False,
            "items": [
                {"prompt": f"{i + 1}.", "image": "@@MEDIA@@sm3/" + path, "accept": acc}
                for i, (path, acc) in enumerate(u["dictation"])
            ],
        },
    }


BODY_HEAD = """do $$
declare
  v_media  text := 'https://classroom.wowteach.ru/media/';
  v_data   jsonb := $json$["""

BODY_TAIL = """]$json$;
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
"""


HEADER = """-- SM3, тесты юнитов 1-8: чтение (skill=reading) и диктант (skill=writing).
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
"""


def main() -> None:
    rows = []
    for u in UNITS:
        rows.append("    " + j(unit_data(u)))
    sys.stdout.write(HEADER + "\n" + BODY_HEAD + "\n" + ",\n".join(rows) + "\n  " + BODY_TAIL)


if __name__ == "__main__":
    main()
