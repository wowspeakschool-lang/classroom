#!/usr/bin/env python3
"""Содержание лид-магнита 4–6: слова, задания, реплики.

Здесь только содержание. Картинки, вёрстка и сборка — в build_kids46.py.

Вещь на экране описывается парой `(предмет, цвет)`, картинка берётся по
ключу `предмет_цвет`. Что при этом звучит, решает поле `say`:

    color     green
    item      a top
    combo     a green top
    sentence  I have a green top

Одна пара — четыре разных задания, поэтому и уроки, и файл озвучки
собираются из одного списка.

Номера дорожек (RU-01, EN-01 …) раздаёт скрипт по порядку: держать их
руками в двух местах — верный способ получить рассинхрон.
"""

COLORS = ["green", "blue", "yellow"]
COLOR_RU = {"green": "зелёный", "blue": "синий", "yellow": "жёлтый"}

# предметы для урока цветов и одежда
OBJS = ["ball", "car", "flower", "cup", "fish"]
ITEMS = ["top", "jeans", "shoes"]

ITEM_EN = {"top": "a top", "jeans": "jeans", "shoes": "shoes"}
# «a green top», но «green jeans» — артикля у множественного числа нет
COMBO_EN = {"top": "a {c} top", "jeans": "{c} jeans", "shoes": "{c} shoes"}

VOICES = {"firefly": "Искорка", "bunny": "Зайчик",
          "hedgehog": "Ёжик", "fox": "Лисёнок"}
FRIENDS = ["bunny", "hedgehog", "fox"]

# четыре фразы, которые дриллим
DRILL = [("top", "green"), ("top", "blue"), ("jeans", "blue"), ("shoes", "yellow")]


def sentence(item, color):
    return "I have " + COMBO_EN[item].format(c=color)


def combo(item, color):
    return COMBO_EN[item].format(c=color)


# ────────────────────────────────────────────────────────────── уроки ──
#
# Типы заданий:
#   word      слушай и повторяй одно слово
#   findall   нажми на все предметы названного цвета (float — шарики летят)
#   sort      разложи по корзинам
#   order     нажми цвета в названном порядке
#   name      назови сам: сначала говорит ребёнок, потом звучит эталон
#   collect   послушай и положи в чемодан / купи в магазине / отправь в стирку
#   catch     поймай вещь, пока она не уехала
#   pick      выбери из двух-четырёх
#   fingers   рука с пальцами: знакомство и три дрилла
#
# token: True — после задания даётся камушек, облачко или прибегает друг.

L1 = {
    "id": 1, "title": "Солнечная Полянка", "island": "meadow",
    "token": "stone",
    "token_lines": [
        ("Молодец! Вот тебе волшебный камушек. Смотри — он лёг в воду.", "радостно"),
        ("И ещё камушек! Дорожка растёт.", "весело"),
        ("Третий! Уже половина пути.", "подбадривающе"),
        ("Четвёртый. Смотри, как блестит.", "любуемся"),
        ("Пятый! Ещё чуть-чуть.", "нетерпеливо"),
        ("Шестой! Совсем немного осталось.", "весело"),
        ("Последний камушек! Дорожка до Облачного Острова готова. Идём!",
         "торжественно, зовём за собой"),
    ],
    "screens": [
        {"t": "story", "solo": True, "btn": "Полетели!",
         "text": "Привет! Я светлячок Искорка. Смотри, что мне принесли — "
                 "приглашение! Нас зовут на праздник на Драконий Остров. Полетели!",
         "tone": "знакомство, радостно, с приглашением"},
        {"t": "story", "pic": "meadow",
         "text": "Мы на Солнечной Полянке! Тут всё разноцветное. Давай выучим "
                 "цвета по-английски.",
         "tone": "восхищённо"},

        {"t": "word", "say": "color", "thing": ("ball", "green"),
         "text": "Смотри, мячик зелёный. А теперь послушай, как этот цвет "
                 "звучит по-английски. И повтори за мной!",
         "tone": "показываем, приглашаем слушать"},
        {"t": "findall", "token": True, "color": "green",
         "pool": [("ball", "green"), ("car", "blue"), ("flower", "green"),
                  ("cup", "yellow"), ("fish", "green"), ("car", "yellow")],
         "text": "Послушай цвет и нажми на все предметы этого цвета.",
         "tone": "с интересом"},

        {"t": "word", "say": "color", "thing": ("car", "blue"),
         "text": "А машинка синяя. Послушай, как называется этот цвет. Повтори!",
         "tone": "показываем"},
        {"t": "findall", "token": True, "float": True, "color": "blue",
         "pool": [("balloon", "blue"), ("balloon", "green"), ("balloon", "blue"),
                  ("balloon", "green"), ("balloon", "blue")],
         "text": "Послушай цвет и лопни все шарики этого цвета!",
         "tone": "весело, азартно"},
        {"t": "sort", "token": True, "colors": ["green", "blue"],
         "rounds": [("cup", "green"), ("fish", "blue"), ("flower", "blue"),
                    ("ball", "green")],
         "text": "Разложи по корзинам. Нажми на предмет — услышишь его цвет.",
         "tone": "деловито, спокойно"},

        {"t": "word", "say": "color", "thing": ("cup", "yellow"),
         "text": "А чашка жёлтая. Послушай и повтори за мной.",
         "tone": "показываем"},
        {"t": "findall", "token": True, "color": "yellow",
         "pool": [("cup", "yellow"), ("ball", "green"), ("fish", "yellow"),
                  ("car", "blue"), ("flower", "yellow"), ("ball", "blue")],
         "text": "Снова послушай цвет и нажми на все такие предметы.",
         "tone": "с интересом"},
        {"t": "sort", "token": True, "colors": COLORS,
         "rounds": [("car", "yellow"), ("ball", "blue"), ("flower", "green"),
                    ("fish", "yellow"), ("cup", "blue")],
         "text": "А теперь корзины три. Разложи всё по цветам.",
         "tone": "деловито"},
        {"t": "order", "token": True,
         "rounds": [["green", "blue"], ["yellow", "green"],
                    ["blue", "yellow", "green"]],
         "text": "Слушай и нажимай кляксы в том же порядке.",
         "tone": "загадочно, медленно"},
        {"t": "name", "token": True, "say": "color",
         "rounds": [("fish", "green"), ("car", "yellow"), ("cup", "blue")],
         "text": "А теперь ты назови сам. Какого цвета?",
         "tone": "с интересом, ждём ответа"},
    ],
}

L2 = {
    "id": 2, "title": "Облачный Остров", "island": "clouds",
    "token": "cloudlet",
    "token_lines": [
        ("Молодец! Вот тебе облачко. Оно село прямо над пропастью.", "радостно"),
        ("Ещё облачко! Мостик начинается.", "весело"),
        ("Третье. Уже можно шагнуть.", "подбадривающе"),
        ("Четвёртое, мягкое, как подушка.", "нежно"),
        ("Пятое!", "весело"),
        ("Шестое. Мостик уже длинный.", "любуемся"),
        ("Седьмое!", "весело"),
        ("Восьмое. Ещё одно — и пойдём.", "нетерпеливо"),
        ("Последнее! Мостик до Драконьего Острова готов. Прыгаем!",
         "торжественно, зовём за собой"),
    ],
    "screens": [
        {"t": "story", "pic": "clouds",
         "text": "Мы на Облачном Острове! Тут всё мягкое, как подушки. "
                 "Ой… впереди пропасть, а мостика нет.",
         "tone": "восхищённо, потом озадаченно"},
        {"t": "story", "solo": True,
         "text": "Давай сначала вспомним цвета. А потом научимся новому!",
         "tone": "бодро, по-деловому"},

        # ── разминка: только цвета ──
        {"t": "findall", "token": True, "float": True, "color": "yellow",
         "pool": [("balloon", "yellow"), ("balloon", "blue"), ("balloon", "yellow"),
                  ("balloon", "green"), ("balloon", "yellow")],
         "text": "Послушай цвет и лопни все шарики этого цвета!",
         "tone": "весело"},
        {"t": "findall", "token": True, "color": "green",
         "pool": [("flower", "green"), ("cup", "blue"), ("ball", "green"),
                  ("fish", "yellow"), ("car", "green"), ("cup", "yellow")],
         "text": "А теперь послушай другой цвет и найди все такие предметы.",
         "tone": "спокойно"},
        {"t": "name", "token": True, "say": "color",
         "rounds": [("ball", "blue"), ("flower", "yellow")],
         "text": "Назови сам: какого цвета?",
         "tone": "ждём ответа"},

        # ── новое, по накопительной ──
        {"t": "word", "say": "item", "thing": ("top", "green"),
         "text": "А это кофточка. Послушай, как она называется по-английски, "
                 "и повтори за мной.",
         "tone": "показываем, приглашаем слушать"},
        {"t": "collect", "token": True, "target": "suitcase", "say": "item",
         "rounds": [
             {"target": ("top", "green"), "others": [("ball", "blue"), ("cup", "yellow")]},
             {"target": ("top", "blue"), "others": [("fish", "green"), ("car", "yellow")]},
             {"target": ("top", "yellow"), "others": [("flower", "blue"), ("ball", "green")]},
         ],
         "text": "Собираем чемодан на праздник! Послушай и положи нужную вещь.",
         "tone": "по-деловому, весело"},

        {"t": "word", "say": "item", "thing": ("jeans", "blue"),
         "text": "А это джинсы. Послушай и повтори за мной.",
         "tone": "показываем"},
        {"t": "collect", "token": True, "target": "shelf", "say": "item",
         "who": "fox",
         "rounds": [
             {"target": ("jeans", "blue"), "others": [("top", "green")]},
             {"target": ("top", "yellow"), "others": [("jeans", "green")]},
             {"target": ("jeans", "yellow"), "others": [("top", "blue")]},
         ],
         "text": "Лисёнок пришёл в магазин. Послушай, что он хочет купить.",
         "tone": "с интересом"},

        {"t": "word", "say": "item", "thing": ("shoes", "yellow"),
         "text": "А это ботинки. Послушай и повтори за мной.",
         "tone": "показываем"},
        {"t": "collect", "token": True, "target": "machine", "say": "item",
         "rounds": [
             {"target": ("shoes", "green"), "others": [("top", "blue"), ("jeans", "yellow")]},
             {"target": ("jeans", "green"), "others": [("shoes", "blue"), ("top", "yellow")]},
             {"target": ("top", "blue"), "others": [("shoes", "yellow"), ("jeans", "blue")]},
         ],
         "text": "Ой, вещи запачкались! Послушай и отправь нужную в стирку.",
         "tone": "озабоченно, потом весело"},
        {"t": "catch", "token": True, "say": "item",
         "rounds": [
             {"target": ("shoes", "blue"), "others": [("top", "green"), ("jeans", "yellow")]},
             {"target": ("top", "green"), "others": [("jeans", "blue"), ("shoes", "yellow")]},
             {"target": ("jeans", "yellow"), "others": [("shoes", "green"), ("top", "blue")]},
         ],
         "text": "Вещи поехали! Поймай ту, которую я назову.",
         "tone": "азартно, быстро"},

        # ── слияние: цвет вместе с одеждой ──
        {"t": "collect", "token": True, "target": "suitcase", "say": "combo",
         "rounds": [
             {"target": ("top", "green"), "others": [("top", "blue"), ("top", "yellow")]},
             {"target": ("jeans", "yellow"), "others": [("jeans", "green"), ("jeans", "blue")]},
             {"target": ("shoes", "blue"), "others": [("shoes", "yellow"), ("top", "blue")]},
         ],
         "text": "Теперь труднее: я назову и цвет, и вещь. Слушай внимательно!",
         "tone": "подзадориваем"},
        {"t": "name", "token": True, "say": "combo",
         "rounds": [("top", "blue"), ("jeans", "green"), ("shoes", "yellow")],
         "text": "А теперь ты. Назови и цвет, и вещь!",
         "tone": "ждём ответа"},
    ],
}

L3 = {
    "id": 3, "title": "Драконий Остров", "island": "dragon",
    "token": "friend",
    "token_lines": [
        ("Слышишь? Это зайчик! Он услышал, как ты говоришь, и прибежал.",
         "обрадованно, с удивлением"),
        ("А вот и ёжик! Он тоже с нами.", "весело"),
        ("И лисёнок прибежал! Теперь мы все вместе.", "торжествующе"),
    ],
    "screens": [
        {"t": "story", "pic": "dragon",
         "text": "Мы на Драконьем Острове! Вот и праздник: флажки, фонарики… "
                 "А где же все? Никого нет. Как странно.",
         "tone": "радость, потом недоумение"},
        {"t": "story", "solo": True,
         "text": "Давай вспомним всё, что знаем. А потом научимся рассказывать "
                 "о себе — на празднике это пригодится!",
         "tone": "заговорщицки"},

        # ── разминка ──
        {"t": "findall", "float": True, "color": "blue",
         "pool": [("balloon", "blue"), ("balloon", "yellow"), ("balloon", "blue"),
                  ("balloon", "green"), ("balloon", "blue")],
         "text": "Послушай цвет и лопни все шарики этого цвета!",
         "tone": "весело"},
        {"t": "collect", "target": "shelf", "say": "item", "who": "bunny",
         "rounds": [
             {"target": ("shoes", "green"), "others": [("top", "blue")]},
             {"target": ("jeans", "yellow"), "others": [("shoes", "blue")]},
         ],
         "text": "Зайчик зашёл в магазин. Что он хочет?",
         "tone": "с интересом"},
        {"t": "pick", "say": "combo",
         "rounds": [
             {"target": ("jeans", "green"),
              "others": [("jeans", "blue"), ("top", "green"), ("shoes", "green")]},
             {"target": ("top", "yellow"),
              "others": [("top", "green"), ("jeans", "yellow"), ("shoes", "yellow")]},
         ],
         "text": "А теперь и цвет, и вещь. Покажи, что я назову.",
         "tone": "спокойно"},

        # ── новое: фраза ──
        {"t": "fingers", "mode": "full", "thing": ("top", "green"),
         "text": "Смотри: у меня есть зелёная кофточка. Сейчас я скажу это "
                 "по-английски. Пять слов — пять пальчиков!",
         "tone": "показываем, приглашаем слушать"},
        {"t": "fingers", "mode": "chain", "token": True, "thing": ("top", "green"),
         "text": "Давай соберём фразу по кусочкам. Повторяй за мной!",
         "tone": "по-игровому, бодро"},
        {"t": "fingers", "mode": "back", "token": True, "thing": ("jeans", "blue"),
         "text": "А теперь наоборот — с конца. Так даже легче!",
         "tone": "заговорщицки"},
        {"t": "fingers", "mode": "swap", "token": True,
         "things": DRILL,
         "text": "Теперь я меняю одно слово, а ты говоришь новую фразу.",
         "tone": "с вызовом, весело"},

        {"t": "pick", "say": "sentence",
         "rounds": [
             {"target": ("top", "green"),
              "others": [("jeans", "green"), ("top", "blue")]},
             {"target": ("shoes", "yellow"),
              "others": [("shoes", "green"), ("jeans", "yellow")]},
             {"target": ("jeans", "blue"),
              "others": [("top", "blue"), ("shoes", "blue")]},
         ],
         "text": "Слушай, кто что говорит, и показывай.",
         "tone": "спокойно"},
        {"t": "name", "say": "sentence",
         "rounds": [("top", "yellow"), ("jeans", "green"), ("shoes", "blue")],
         "text": "А теперь ты расскажи! Что у тебя есть?",
         "tone": "ждём ответа"},

        # ── сюжет ──
        {"t": "story", "pic": "cave_closed",
         "text": "Ой, смотри! Следы ведут к пещере. А вход завален камнем. "
                 "Одному не сдвинуть… Хорошо, что с нами друзья!",
         "tone": "загадочно, потом с усилием"},
        {"t": "story", "pic": "push", "btn": "Помочь!",
         "text": "Раз, два, взяли! Толкаем все вместе!",
         "tone": "с натугой, весело"},
        {"t": "story", "pic": "cave_open",
         "text": "Получилось! Как темно… Подожди, я посвечу. Смотри — гнёздышко!",
         "tone": "радость, потом тише"},
        {"t": "story", "pic": "egg",
         "text": "А в нём яйцо! Интересно, кто же там внутри? Неужели дракончик? "
                 "Узнаем на первом уроке!",
         "tone": "изумление, тайна, предвкушение"},
    ],
}

LESSONS = [L1, L2, L3]

PRAISE = [
    ("Молодец!", "живо"),
    ("Правильно!", "радостно"),
    ("Верно! Умница!", "тепло"),
    ("Получилось!", "с восторгом"),
    ("Ух ты, как здорово!", "восхищённо"),
]
RETRY = [
    ("Ой, не то. Попробуй ещё разок.", "спокойно, без тени упрёка"),
    ("Почти! Давай ещё раз.", "подбадривающе"),
]
ASK_REPEAT = ("А теперь скажи сам, целиком.", "мягко приглашаем")


# ──────────────────────────────── английские дорожки ──

def english_tracks():
    """Все английские записи: слова, сочетания, фразы и куски для дриллов."""
    tracks = []                      # (ключ, текст)
    index = {}                       # текст → ключ

    def add(text):
        if text not in index:
            key = "EN-%02d" % (len(tracks) + 1)
            index[text] = key
            tracks.append((key, text))
        return index[text]

    for c in COLORS:
        add(c)
    for it in ITEMS:
        add(ITEM_EN[it])
    for it in ITEMS:
        for c in COLORS:
            add(combo(it, c))
    for it in ITEMS:
        for c in COLORS:
            add(sentence(it, c))
    add("I")
    add("I have")
    return tracks, index
