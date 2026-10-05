#!/usr/bin/env python3
"""Листы картинок тестов Go Getter 3 — промпты и таблица для нарезки.

Устройство то же, что у tools/gg2_sheets.py (оттуда берутся стиль, сборка
промпта и проверка). Номера листов продолжают нумерацию GG2: Анна присылает
картинки одним потоком, и «Лист 70» не должен значить два разных листа.

В выгрузке GG3 нет ни одной картинки словаря (вместо них плейсхолдеры), и не
выгрузились картинки к SPEAKING TASK 1 — отсюда по два листа слов и одна
сцена на тест.

  python3 tools/gg3_sheets.py            пересобрать docs/GG3_листы_промптов.md
  python3 tools/gg3_sheets.py --check    только проверить
"""
import argparse, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gg2_sheets as base  # noqa: E402

ROOT = base.ROOT

SHEETS = [
    # ---------------- UNIT 1 · chores ----------------
    ("u1", 3, 3, "people", "Домашние дела",
     "Тест Unit 1, блоки 1–2 (12 фраз) — девять с людьми.", [
        ("u1_clear_table", "a boy clearing the table, carrying dirty plates"),
        ("u1_hang_washing", "a girl hanging out the washing on a line"),
        ("u1_iron_tshirt", "a boy ironing a T-shirt"),
        ("u1_take_rubbish", "a girl taking out the rubbish bag to the bin"),
        ("u1_water_plants", "a boy watering the plants with a watering can"),
        ("u1_load_dishwasher", "a girl putting plates into a dishwasher"),
        ("u1_make_bed", "a boy making his bed"),
        ("u1_vacuum_room", "a girl vacuuming her room"),
        ("u1_set_table", "a boy setting the table with plates, knives and forks"),
    ], "Every child is shown full-length, doing the chore clearly."),
    ("u1", 1, 3, "people", "Домашние дела 2",
     "Тест Unit 1, блоки 1–2 — оставшиеся три фразы.", [
        ("u1_feed_dog", "a girl feeding a dog from a bowl"),
        ("u1_empty_dishwasher", "a boy taking clean plates out of a dishwasher"),
        ("u1_put_away_clothes", "a girl putting her clothes away in a wardrobe"),
    ], None),
    ("u1", 1, 1, "people_scene", "Уборка всей семьёй",
     "Тест Unit 1, SPEAKING TASK 1 («The woman is sweeping the floor…»).", [
        ("u1_scene_chores",
         "a family doing chores at home on a Saturday morning: a woman sweeping the floor, a man washing the "
         "dishes, a girl watering the plants, a boy making his bed in the next room, a dog waiting by its empty bowl"),
    ], None),

    # ---------------- UNIT 2 · shopping ----------------
    ("u2", 2, 3, "people_scene", "Покупки: что делают",
     "Тест Unit 2, блоки 1–2.", [
        ("u2_pay_card", "a woman paying by card at a till"),
        ("u2_pay_cash", "a boy paying in cash at a shop counter"),
        ("u2_carry_shopping", "a man carrying heavy shopping bags"),
        ("u2_get_change", "a girl getting her change from a shop assistant"),
        ("u2_queue", "people standing in a queue at a till"),
        ("u2_cashier", "a smiling cashier at a supermarket till"),
    ], None),
    ("u2", 2, 3, "scene", "Покупки: что и где",
     "Тест Unit 2, блоки 1–2. Магазины узнаваемы по витрине, без вывесок.", [
        ("u2_basket", "a shopping basket with groceries"),
        ("u2_list", "a handwritten shopping list on a notepad with a pencil, the lines drawn as plain squiggles"),
        ("u2_trolley", "a shopping trolley"),
        ("u2_greengrocers", "a greengrocer's shop front with boxes of fruit and vegetables outside"),
        ("u2_chemists", "a chemist's shop front with a green cross and medicine in the window"),
        ("u2_department_store", "a big department store with many floors and wide shop windows"),
    ], None),
    ("u2", 1, 1, "people_scene", "У кассы",
     "Тест Unit 2, SPEAKING TASK 1. Перерисовка картинки из выгрузки в общем стиле; вопросы остаются.", [
        ("u2_scene_shop",
         "inside a big supermarket: a cashier scanning shopping at the till, three people standing in a queue, "
         "a full shopping trolley and a shopping basket, shelves with food behind them"),
    ], None),

    # ---------------- UNIT 3 · holidays ----------------
    ("u3", 3, 3, "people_scene", "Каникулы и поездки",
     "Тест Unit 3, блоки 1–2.", [
        ("u3_hiking", "two friends hiking in the mountains with backpacks"),
        ("u3_camping", "a family camping next to a tent"),
        ("u3_boat_trip", "people on a boat trip on a lake"),
        ("u3_local_food", "a boy trying local food at a street food stall abroad"),
        ("u3_cycling", "a girl cycling along a country road"),
        ("u3_explore_city", "two tourists with a map exploring an old city"),
        ("u3_snorkelling", "a girl snorkelling among colourful fish"),
        ("u3_guided_tour", "a guide with a little flag leading a group of tourists"),
        ("u3_beach", "a family going to the beach with towels and a beach ball"),
    ], None),
    ("u3", 1, 3, "people", "Как было в поездке",
     "Тест Unit 3, блок 2.", [
        ("u3_get_tired", "a tired boy sitting on his backpack, wiping his forehead"),
        ("u3_get_lost", "a confused girl holding a map upside down"),
        ("u3_get_bored", "a bored boy yawning"),
    ], None),
    ("u3", 1, 1, "people_scene", "В походе",
     "Тест Unit 3, SPEAKING TASK 1. Вопросы: Where were the people? Did they go hiking or cycling? Did they get tired?", [
        ("u3_scene_trip",
         "a family of four hiking in the mountains on a sunny day: they carry backpacks and water bottles, "
         "the youngest boy looks tired, a lake and pine trees below them"),
    ], None),

    # ---------------- UNIT 4 · gadgets ----------------
    ("u4", 3, 3, "object", "Техника",
     "Тест Unit 4, блоки 1–2.", [
        ("u4_blender", "a kitchen blender"),
        ("u4_microwave", "a microwave oven"),
        ("u4_smart_tv", "a smart TV with app tiles on the screen"),
        ("u4_usb_stick", "a USB stick"),
        ("u4_remote", "a TV remote control"),
        ("u4_hairdryer", "a hairdryer"),
        ("u4_games_console", "a games console with a controller"),
        ("u4_toaster", "a toaster with two slices of toast"),
        ("u4_plug_socket", "an electric plug and a wall socket"),
    ], None),
    ("u4", 2, 2, "people", "Включить, выключить",
     "Тест Unit 4, блоки 1–2.", [
        ("u4_turn_on", "a girl turning on a lamp, the lamp lighting up"),
        ("u4_turn_off", "a boy turning off a TV, the screen going dark"),
        ("u4_plug_in", "a boy plugging a laptop charger into the wall socket"),
        ("u4_unplug", "a girl unplugging a kettle from the wall socket"),
    ], None),
    ("u4", 1, 1, "people_scene", "Фен",
     "Тест Unit 4, SPEAKING TASK 1. Перерисовка картинки из выгрузки; вопросы остаются (What is the girl doing?…).", [
        ("u4_scene_hairdryer",
         "a girl in a bathrobe drying her hair with a hairdryer in a bright bathroom, standing at the mirror, "
         "the hairdryer plugged in near the sink"),
    ], None),

    # ---------------- UNIT 5 · health ----------------
    ("u5", 3, 3, "people", "Болезни",
     "Тест Unit 5, блоки 1–2.", [
        ("u5_sore_throat", "a boy with a sore throat holding his neck"),
        ("u5_blocked_nose", "a girl with a blocked nose, holding a tissue"),
        ("u5_headache", "a boy with a headache holding his head"),
        ("u5_stomachache", "a girl with a stomachache holding her tummy"),
        ("u5_cough", "a boy coughing into his elbow"),
        ("u5_temperature", "a girl with a temperature, a thermometer in her mouth"),
        ("u5_sneeze", "a boy sneezing"),
        ("u5_earache", "a girl with an earache holding her ear"),
        ("u5_toothache", "a boy with a toothache holding his swollen cheek"),
    ], None),
    ("u5", 1, 2, "people", "Болезни 2",
     "Тест Unit 5, блок 2; синяк — финальный тест (по желанию).", [
        ("u5_runny_nose", "a girl with a runny nose"),
        ("u5_bruise", "a boy showing a bruise on his knee"),
    ], None),
    ("u5", 1, 1, "people_scene", "Мальчик заболел",
     "Тест Unit 5, SPEAKING TASK 1 (What's the problem? Does he have a temperature?…).", [
        ("u5_scene_ill",
         "a boy ill in bed with a cold: a thermometer, tissues, a glass of water and medicine on the bedside "
         "table, his mum sitting next to the bed with a cup of tea"),
    ], None),

    # ---------------- UNIT 6 · cooking ----------------
    ("u6", 2, 3, "object", "Посуда",
     "Тест Unit 6, блоки 1–2.", [
        ("u6_bowl", "a mixing bowl"),
        ("u6_fork", "a fork"),
        ("u6_cake_tin", "a round cake tin"),
        ("u6_oven", "an oven"),
        ("u6_pot", "a cooking pot"),
        ("u6_spoon", "a wooden spoon"),
    ], None),
    ("u6", 2, 3, "people", "Готовим",
     "Тест Unit 6, блоки 1–2.", [
        ("u6_bake", "a girl taking a cake out of the oven"),
        ("u6_fry", "a boy frying eggs in a frying pan"),
        ("u6_mix", "a girl mixing batter in a bowl"),
        ("u6_peel", "a boy peeling a potato"),
        ("u6_chop", "a girl chopping carrots on a board"),
        ("u6_slice", "a boy slicing bread"),
    ], None),
    ("u6", 1, 1, "people_scene", "На кухне",
     "Тест Unit 6, SPEAKING TASK 1. Перерисовка картинки из выгрузки; вопросы остаются (What has she done already?…).", [
        ("u6_scene_cooking",
         "a girl cooking in a kitchen: she is chopping carrots on a board; peeled potatoes in a bowl, a pot on "
         "the cooker, a cake tin, spoons and a fork on the table"),
    ], None),

    # ---------------- UNIT 7 · houses ----------------
    ("u7", 2, 2, "scene", "Дома",
     "Тест Unit 7, блоки 1–2.", [
        ("u7_detached", "a detached house standing alone with a garden around it"),
        ("u7_semi_detached", "a semi-detached house: two homes joined together"),
        ("u7_terraced", "a row of terraced houses"),
        ("u7_block_of_flats", "a block of flats"),
    ], None),
    ("u7", 3, 3, "scene", "Части дома",
     "Тест Unit 7, блоки 1–2; домик — финальный тест (по желанию).", [
        ("u7_attic", "an attic under a sloping roof with boxes"),
        ("u7_balcony", "a balcony with flowers"),
        ("u7_lift", "a lift with open doors"),
        ("u7_stairs", "a staircase"),
        ("u7_basement", "a basement with shelves and a washing machine"),
        ("u7_mirror", "a mirror on a wall"),
        ("u7_drawer", "a chest with one drawer pulled open"),
        ("u7_tap", "a kitchen tap with running water"),
        ("u7_cottage", "a small country cottage with a thatched roof"),
    ], None),
    ("u7", 1, 1, "people_scene", "Переезд",
     "Тест Unit 7, SPEAKING TASK 1 (What kind of house is it? Moving in or moving out?).", [
        ("u7_scene_moving",
         "a family moving into a semi-detached house: a removal van in front, a dad and a girl carrying boxes "
         "into the house, a mum carrying a lamp, a boy holding a cat, boxes and a sofa on the lawn"),
    ], None),

    # ---------------- UNIT 8 · future and manners ----------------
    ("u8", 2, 3, "people", "Будущее",
     "Тест Unit 8, блоки 1–2.", [
        ("u8_be_rich", "a young man in a smart suit next to a pile of gold coins and a sports car"),
        ("u8_have_family", "a happy young couple with two little children"),
        ("u8_foreign_language", "a girl learning a foreign language with headphones and a book, flags of different countries above her"),
        ("u8_be_doctor", "a young woman doctor with a stethoscope"),
        ("u8_learn_drive", "a teenager learning to drive a car with an instructor"),
        ("u8_be_famous", "a famous singer on a red carpet with cameras flashing"),
    ], None),
    ("u8", 2, 3, "people", "Вежливость",
     "Тест Unit 8, блоки 1–2.", [
        ("u8_wait_turn", "children waiting their turn in a line at a slide"),
        ("u8_hug", "two friends giving each other a hug"),
        ("u8_shake_hands", "two men shaking hands"),
        ("u8_invite", "a girl giving a party invitation card to her friend"),
        ("u8_call", "a boy calling someone on his phone"),
        ("u8_arrive_on_time", "a girl arriving at school on time, a big clock above the school door"),
    ], None),
    ("u8", 1, 1, "people_scene", "Встреча у школы",
     "Тест Unit 8, SPEAKING TASK 1 (How are the boys greeting each other?…).", [
        ("u8_scene_greeting",
         "two boys of twelve greeting each other in front of a school in the morning: one boy is hugging his "
         "friend, other children shaking hands and waving nearby"),
    ], None),

    # ---------------- FINAL ----------------
    ("final", 1, 1, "people_scene", "Кемпинг",
     "Финальный тест, блок 4 (верно/неверно). Детали задают ответы — не менять.", [
        ("final_scene_camping",
         "a campsite by a lake: two people walking together carrying big backpacks; near the campfire a man "
         "is playing the guitar and a woman next to him is listening and smiling, not singing; two big tents "
         "much bigger than the backpacks; a boy sitting by the lake with a fishing rod, fully dressed"),
    ], None),
]

HEAD = """# Go Getter 3 — ЛИСТЫ ПРОМПТОВ НА КАРТИНКИ (тесты)

Собирается из `tools/gg3_sheets.py` — **правится там**, не здесь.

Номера продолжают листы GG2 (`docs/GG2_листы_промптов.md`). Готовую картинку
присылать в чат с подписью номера листа. Стиль тот же, что у GG2 и GG1.

В выгрузке GG3 нет картинок словаря и картинок к SPEAKING TASK 1 — поэтому
на каждый тест два листа слов и одна сцена. Три сцены из выгрузки (касса,
фен, кухня) перерисовываем в общем стиле, вопросы к ним не меняются.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    errors = base.check(SHEETS)
    if errors:
        for e in errors:
            print("·", e, file=sys.stderr)
        sys.exit(1)
    start = len(base.SHEETS) + 1
    if args.check:
        print(f"листов {len(SHEETS)} (с {start}), картинок {sum(len(s[6]) for s in SHEETS)}, всё сходится")
        return
    doc = os.path.join(ROOT, "docs", "GG3_листы_промптов.md")
    with open(doc, "w", encoding="utf-8") as f:
        f.write(base.render(SHEETS, HEAD, start=start))
    print("записан", os.path.relpath(doc, ROOT))


if __name__ == "__main__":
    main()
