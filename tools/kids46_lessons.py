#!/usr/bin/env python3
"""Содержание лид-магнита 4–6: слова, задания, реплики.

Здесь только содержание. Картинки, вёрстка и сборка — в build_kids46.py.

Вещь на экране описывается парой `(предмет, цвет)`, картинка берётся по
ключу `предмет_цвет`. Что при этом звучит, решает поле `say`:

    color     green
    item      a top
    combo     a green top
    sentence  I have a green top

Одна пара — разные задания, поэтому и уроки, и файл озвучки собираются из
одного списка. Номера дорожек скрипт раздаёт сам по порядку.
"""

COLORS = ["green", "blue", "yellow"]
COLOR_RU = {"green": "зелёный", "blue": "синий", "yellow": "жёлтый"}

OBJS = ["ball", "car", "flower", "cup", "fish"]
ITEMS = ["top", "jeans", "shoes"]

ITEM_EN = {"top": "a top", "jeans": "jeans", "shoes": "shoes"}
ITEM_BARE = {"top": "top", "jeans": "jeans", "shoes": "shoes"}
# «a green top», но «green jeans» — артикля у множественного числа нет
COMBO_EN = {"top": "a {c} top", "jeans": "{c} jeans", "shoes": "{c} shoes"}

VOICES = {"firefly": "Искорка", "bunny": "Зайчик",
          "hedgehog": "Ёжик", "fox": "Лисёнок"}
FRIENDS = ["bunny", "hedgehog", "fox"]


def combo(item, color):
    return COMBO_EN[item].format(c=color)


def sentence(item, color):
    return "I have " + combo(item, color)


# ────────────────────────────────────────────────────────────── уроки ──
#
# Типы заданий:
#   word       слушай и повторяй одно слово
#   findall    нажми на все предметы названного цвета (float — шарики летят)
#   sort       разложи по корзинам
#   order      нажми цвета в названном порядке
#   name       назови сам: сначала говорит ребёнок, потом звучит эталон
#   collect    положи в чемодан / купи в магазине / отправь в стирку
#   catch      поймай вещь, пока она не уехала
#   pick       выбери из двух-четырёх
#   truefalse  верно или нет: слышим одно, видим другое
#   fingers    рука с пальцами: знакомство и три дрилла
#   vocab      словарик в конце урока: картинка и озвучка, без слов
#
# token: True — после задания даётся камушек. Наград меньше, чем заданий:
# иначе дорожка достраивается до острова задолго до конца урока.

L1 = {
    "id": 1, "title": "Солнечная Полянка", "island": "meadow",
    "token": "stone",
    "token_lines": [
        ("Молодец! Вот тебе волшебный камушек. Смотри — он лёг в воду.", "радостно"),
        ("И ещё камушек! Дорожка растёт.", "весело"),
        ("Третий! Уже половина пути.", "подбадривающе"),
        ("Четвёртый. Ещё чуть-чуть.", "нетерпеливо"),
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
        {"t": "findall", "color": "green",
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
        {"t": "sort", "colors": ["green", "blue"],
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

        {"t": "vocab", "say": "color",
         "things": [("ball", "green"), ("car", "blue"), ("cup", "yellow")],
         "text": "Вот всё, что ты сегодня выучил. Нажимай на картинки и слушай.",
         "tone": "спокойно, с гордостью"},
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
        ("Пятое! Совсем немного осталось.", "нетерпеливо"),
        ("Последнее! Мостик до Драконьего Острова готов. Прыгаем!",
         "торжественно, зовём за собой"),
    ],
    "screens": [
        {"t": "story", "pic": "clouds",
         "text": "Мы на Облачном Острове! Тут всё мягкое, как подушки. "
                 "Ой… впереди пропасть, а мостика нет.",
         "tone": "восхищённо, потом озадаченно"},
        {"t": "story", "solo": True,
         "text": "Сначала вспомним цвета — все три. А потом научимся новому!",
         "tone": "бодро, по-деловому"},

        # ── разминка: все три цвета, играми, которых не было в первом уроке ──
        {"t": "pick", "say": "color",
         "rounds": [
             {"target": ("flower", "green"),
              "others": [("flower", "blue"), ("flower", "yellow")]},
             {"target": ("car", "yellow"),
              "others": [("car", "green"), ("car", "blue")]},
             {"target": ("fish", "blue"),
              "others": [("fish", "yellow"), ("fish", "green")]},
         ],
         "text": "Слушай цвет и показывай.", "tone": "спокойно"},
        {"t": "catch", "token": True, "say": "color",
         "rounds": [
             {"target": ("ball", "yellow"),
              "others": [("ball", "green"), ("ball", "blue")]},
             {"target": ("cup", "green"),
              "others": [("cup", "blue"), ("cup", "yellow")]},
             {"target": ("car", "blue"),
              "others": [("car", "yellow"), ("car", "green")]},
         ],
         "text": "Предметы поехали! Поймай тот, цвет которого я назову.",
         "tone": "азартно"},
        {"t": "truefalse", "say": "color",
         "rounds": [
             {"thing": ("flower", "green"), "claim": ("flower", "green")},
             {"thing": ("fish", "blue"), "claim": ("fish", "yellow")},
             {"thing": ("cup", "yellow"), "claim": ("cup", "yellow")},
             {"thing": ("ball", "green"), "claim": ("ball", "blue")},
         ],
         "text": "Я буду называть цвет. Угадала — палец вверх, "
                 "не угадала — палец вниз.",
         "tone": "по-игровому, с хитринкой"},

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
        {"t": "collect", "token": True, "target": "shelf", "say": "item", "who": "fox",
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

        # ── слияние: цвет вместе с одеждой ──
        {"t": "collect", "target": "suitcase", "say": "combo",
         "rounds": [
             {"target": ("top", "green"), "others": [("top", "blue"), ("top", "yellow")]},
             {"target": ("jeans", "yellow"), "others": [("jeans", "green"), ("jeans", "blue")]},
             {"target": ("shoes", "blue"), "others": [("shoes", "yellow"), ("shoes", "green")]},
         ],
         "text": "Теперь я назову и цвет, и вещь. Слушай внимательно!",
         "tone": "подзадориваем"},
        {"t": "truefalse", "token": True, "say": "combo",
         "rounds": [
             {"thing": ("top", "green"), "claim": ("top", "green")},
             {"thing": ("jeans", "blue"), "claim": ("jeans", "yellow")},
             {"thing": ("shoes", "yellow"), "claim": ("shoes", "yellow")},
             {"thing": ("top", "blue"), "claim": ("jeans", "blue")},
         ],
         "text": "И снова: угадала я или нет?",
         "tone": "с хитринкой"},
        {"t": "pick", "say": "combo",
         "rounds": [
             {"target": ("jeans", "green"),
              "others": [("jeans", "blue"), ("top", "green"), ("shoes", "green")]},
             {"target": ("top", "yellow"),
              "others": [("top", "green"), ("jeans", "yellow"), ("shoes", "yellow")]},
             {"target": ("shoes", "blue"),
              "others": [("shoes", "green"), ("jeans", "blue"), ("top", "blue")]},
         ],
         "text": "Теперь вещей много. Слушай и показывай.",
         "tone": "спокойно"},
        {"t": "name", "token": True, "say": "combo",
         "rounds": [("top", "blue"), ("jeans", "green"), ("shoes", "yellow")],
         "text": "А теперь ты. Назови и цвет, и вещь!",
         "tone": "ждём ответа"},

        {"t": "vocab", "say": "combo",
         "things": [("top", "green"), ("jeans", "blue"), ("shoes", "yellow")],
         "text": "Вот что ты выучил сегодня. Нажимай и слушай.",
         "tone": "спокойно, с гордостью"},
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
        {"t": "order",
         "rounds": [["blue", "green"], ["yellow", "blue", "green"]],
         "text": "Слушай и нажимай кляксы по порядку.",
         "tone": "загадочно"},
        {"t": "catch", "say": "item",
         "rounds": [
             {"target": ("shoes", "green"), "others": [("top", "blue"), ("jeans", "yellow")]},
             {"target": ("jeans", "blue"), "others": [("shoes", "yellow"), ("top", "green")]},
         ],
         "text": "Вещи поехали! Поймай ту, которую я назову.",
         "tone": "азартно"},
        {"t": "truefalse", "say": "combo",
         "rounds": [
             {"thing": ("jeans", "green"), "claim": ("jeans", "green")},
             {"thing": ("top", "yellow"), "claim": ("top", "blue")},
             {"thing": ("shoes", "blue"), "claim": ("shoes", "blue")},
         ],
         "text": "Угадала я или нет?", "tone": "с хитринкой"},

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
         "things": [("top", "green"), ("top", "blue"), ("top", "yellow"),
                    ("jeans", "yellow"), ("shoes", "yellow")],
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
        {"t": "name", "say": "sentence", "example": True,
         "rounds": [("top", "yellow"), ("jeans", "green"), ("shoes", "blue")],
         "text": "А теперь ты расскажи! Что у тебя есть? Если забыл — нажми "
                 "«послушать пример».",
         "tone": "ждём ответа, подбадривающе"},

        {"t": "vocab", "say": "sentence",
         "things": [("top", "green"), ("jeans", "blue"), ("shoes", "yellow")],
         "text": "Вот твои фразы. Нажимай и слушай.",
         "tone": "спокойно, с гордостью"},

        # ── сюжет ──
        {"t": "story", "pic": "cave_closed",
         "text": "Ой, смотри! Следы ведут к пещере. А вход завален камнем. "
                 "Одному не сдвинуть… Хорошо, что с нами друзья!",
         "tone": "загадочно, потом с усилием"},
        {"t": "story", "pic": "push", "btn": "Помочь!",
         "text": "Раз, два, взяли! Толкаем все вместе!",
         "tone": "с натугой, весело"},
        {"t": "story", "pic": "cave_egg",
         "text": "Получилось! Как темно… Подожди, я посвечу. Смотри — гнёздышко, "
                 "а в нём яйцо!",
         "tone": "радость, потом тише, потом изумление"},
        {"t": "story", "pic": "egg",
         "text": "Интересно, кто же там внутри? Неужели дракончик? "
                 "Узнаем на первом уроке!",
         "tone": "тайна, предвкушение"},
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
ASK_REPEAT = ("Теперь твоя очередь! Покажи ладошку, говори и следи за пальчиками.",
              "мягко приглашаем, с улыбкой")
FINALE = ("Ты прошёл всю дорогу до праздника и теперь умеешь рассказывать о себе "
          "по-английски! А кто в яйце — узнаешь на первом уроке.",
          "торжественно, тепло")


# ──────────────────────────────── английские дорожки ──

def english_tracks():
    """Слова, сочетания, фразы и отдельные слова для дриллов по пальцам."""
    tracks, index = [], {}

    def add(text):
        if text not in index:
            index[text] = "EN-%02d" % (len(tracks) + 1)
            tracks.append((index[text], text))
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
    # отдельные слова: на них по очереди показывает стрелка на пальцах
    for w in ["I", "have", "a"] + [ITEM_BARE[i] for i in ITEMS]:
        add(w)
    return tracks, index
