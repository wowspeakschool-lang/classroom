# -*- coding: utf-8 -*-
"""Озвучка лид-магнита WowSpeak 4-6 через Yandex SpeechKit.

Файл собран скриптом, руками его править не нужно — кроме таблицы ГОЛОСА
ниже и двух строк с ключом.

Как пользоваться — в инструкции WowSpeak_озвучка_яндекс.md. Коротко:

    python ozvuchka.py obrazcy    записать по образцу на каждый голос
    python ozvuchka.py            записать все реплики
    python ozvuchka.py RU-05      переписать одну реплику заново
"""

# ─────────────────────────────── сюда вставить свои две строки ──

KEY = ""        # API-ключ сервисного аккаунта, начинается на AQVN
FOLDER = ""     # идентификатор каталога, начинается на b1g

# ──────────────────────────────────────────── голоса героев ──
#
# Слева — герой, справа — голос Яндекса и роль. Послушайте образцы
# (python ozvuchka.py obrazcy) и замените имя голоса, если не понравился.
# Роль можно убрать, написав None вместо "good".

VOICES = {
    "firefly": ["alena", "good"],
    "bunny": ["jane", "good"],
    "hedgehog": ["ermil", "good"],
    "fox": ["zahar", "good"],
    "en": ["john", None],
    "en_slow": ["john", None],
}

# Кого прогонять в режиме obrazcy. Неизвестное сервису имя просто
# пропускается с пометкой — так и видно, какие голоса есть на самом деле.
SAMPLES = ["alena", "jane", "omazh", "dasha", "julia", "lera", "masha", "marina", "filipp", "ermil", "zahar", "alexander", "kirill", "anton", "madi_ru", "zorro", "ermolaev"]

SPEED = "0.95"        # чуть медленнее обычного: слушает четырёхлетка
SLOW = "0.7"          # английское слово «по слогам»

# ───────────────────────────────────────────── сами реплики ──

TRACKS = [
    ["RU-01", "Привет! Я светлячок Искорка. Смотри, что мне принесли — приглашение! Нас зовут на праздник на Драконий Остров. Полетели!", "firefly"],
    ["RU-02", "Смотри, куда нам надо — вон он, Драконий Остров, дальний. Только дороги туда нет. Ничего, мы её построим!", "firefly"],
    ["RU-03", "Начнём с Солнечной Полянки. Нажми на первый остров, чтобы начать путешествие!", "firefly"],
    ["RU-04", "Мы на Солнечной Полянке! Тут всё разноцветное. Давай выучим цвета по-английски.", "firefly"],
    ["RU-05", "Смотри, мячик зелёный. А теперь послушай, как этот цвет звучит по-английски. И повтори за мной!", "firefly"],
    ["RU-06", "Послушай цвет и нажми на все предметы этого цвета.", "firefly"],
    ["RU-07", "А машинка синяя. Послушай, как называется этот цвет. Повтори!", "firefly"],
    ["RU-08", "Послушай цвет и лопни все шарики этого цвета!", "firefly"],
    ["RU-09", "Молодец! Вот тебе волшебный камушек. Смотри — он лёг в воду.", "firefly"],
    ["RU-10", "Разложим всё по корзинам. Нажми на корзинку нужного цвета, а нажмёшь на предмет — услышишь его цвет.", "firefly"],
    ["RU-11", "А чашка жёлтая. Послушай и повтори за мной.", "firefly"],
    ["RU-12", "Снова послушай цвет и нажми на все такие предметы.", "firefly"],
    ["RU-13", "И ещё камушек! Дорожка растёт.", "firefly"],
    ["RU-14", "А теперь корзины три. Снова нажимай на корзинку нужного цвета.", "firefly"],
    ["RU-15", "Третий! Уже половина пути.", "firefly"],
    ["RU-16", "Слушай и нажимай кляксы в том же порядке.", "firefly"],
    ["RU-17", "Четвёртый. Ещё чуть-чуть.", "firefly"],
    ["RU-18", "А теперь ты назови сам. Какого цвета?", "firefly"],
    ["RU-19", "Последний камушек! Дорожка до Облачного Острова готова. Идём!", "firefly"],
    ["RU-20", "Вот всё, что ты сегодня выучил. Нажимай на картинки и слушай.", "firefly"],
    ["RU-21", "Мы на Облачном Острове! Тут всё мягкое, как подушки. Ой… впереди пропасть, а мостика нет.", "firefly"],
    ["RU-22", "Сначала вспомним цвета — все три. А потом научимся новому!", "firefly"],
    ["RU-23", "Слушай цвет и показывай.", "firefly"],
    ["RU-24", "Предметы поехали! Поймай тот, цвет которого я назову.", "firefly"],
    ["RU-25", "Молодец! Вот тебе облачко. Оно село прямо над пропастью.", "firefly"],
    ["RU-26", "Я буду называть цвет. Угадала — палец вверх, не угадала — палец вниз.", "firefly"],
    ["RU-27", "А это кофточка. Послушай, как она называется по-английски, и повтори за мной.", "firefly"],
    ["RU-28", "Собираем чемодан на праздник! Послушай и положи нужную вещь.", "firefly"],
    ["RU-29", "Ещё облачко! Мостик начинается.", "firefly"],
    ["RU-30", "А это джинсы. Послушай и повтори за мной.", "firefly"],
    ["RU-31", "Лисёнок пришёл в магазин. Послушай, что он хочет купить.", "firefly"],
    ["RU-32", "Третье. Уже можно шагнуть.", "firefly"],
    ["RU-33", "А это ботинки. Послушай и повтори за мной.", "firefly"],
    ["RU-34", "Ой, вещи запачкались! Послушай и отправь нужную в стирку.", "firefly"],
    ["RU-35", "Четвёртое, мягкое, как подушка.", "firefly"],
    ["RU-36", "Теперь я назову и цвет, и вещь. Слушай внимательно!", "firefly"],
    ["RU-37", "И снова: угадала я или нет?", "firefly"],
    ["RU-38", "Пятое! Совсем немного осталось.", "firefly"],
    ["RU-39", "Теперь вещей много. Слушай и показывай.", "firefly"],
    ["RU-40", "А теперь ты. Назови и цвет, и вещь!", "firefly"],
    ["RU-41", "Последнее! Мостик до Драконьего Острова готов. Прыгаем!", "firefly"],
    ["RU-42", "Вот что ты выучил сегодня. Нажимай и слушай.", "firefly"],
    ["RU-43", "Мы на Драконьем Острове! Вот и праздник: флажки, фонарики… А где же все? Никого нет. Как странно.", "firefly"],
    ["RU-44", "Давай вспомним всё, что знаем. А потом научимся рассказывать о себе — на празднике это пригодится!", "firefly"],
    ["RU-45", "Вещи выложены. Смотри внимательно — сейчас облачко наплывёт, и одной вещи не станет. Найди, какой!", "firefly"],
    ["RU-46", "Вещи выцвели! Послушай и нажми кляксу нужного цвета — вещь снова станет цветной.", "firefly"],
    ["RU-47", "Смотри: у меня есть зелёная кофточка. Сейчас я скажу это по-английски. Пять слов — пять пальчиков!", "firefly"],
    ["RU-48", "Давай соберём фразу по кусочкам. Повторяй за мной!", "firefly"],
    ["RU-49", "Слышишь? Это зайчик! Он услышал, как ты говоришь, и прибежал.", "firefly"],
    ["RU-50", "А теперь наоборот — с конца. Так даже легче!", "firefly"],
    ["RU-51", "А вот и ёжик! Он тоже с нами.", "firefly"],
    ["RU-52", "Теперь я называю вещь, а ты говоришь про неё целым предложением. Сколько слов — столько и пальчиков. Сказал — нажми «проверить себя».", "firefly"],
    ["RU-53", "И лисёнок прибежал! Теперь мы все вместе.", "firefly"],
    ["RU-54", "Слушай, кто что говорит, и показывай.", "firefly"],
    ["RU-55", "А теперь ты расскажи! Что у тебя есть? Если забыл — нажми «послушать пример».", "firefly"],
    ["RU-56", "Вот твои фразы. Нажимай и слушай.", "firefly"],
    ["RU-57", "Ой, смотри! Следы — и с коготками! Чьи же они? Ведут прямо к пещере. А вход завален камнем. Одному не сдвинуть… Хорошо, что с нами друзья!", "firefly"],
    ["RU-58", "Раз, два, взяли! Толкаем все вместе!", "firefly"],
    ["RU-59", "Получилось! Как темно… Подожди, я посвечу. Смотри — гнёздышко, а в нём яйцо!", "firefly"],
    ["RU-60", "Интересно, кто же там внутри? Неужели дракончик? Мы обязательно узнаем — в следующем приключении. Я буду тебя ждать!", "firefly"],
    ["RU-61", "Молодец!", "firefly"],
    ["RU-62", "Правильно!", "firefly"],
    ["RU-63", "Верно! Умница!", "firefly"],
    ["RU-64", "Получилось!", "firefly"],
    ["RU-65", "Ух ты, как здорово!", "firefly"],
    ["RU-66", "Ой, не то. Попробуй ещё разок.", "firefly"],
    ["RU-67", "Почти! Давай ещё раз.", "firefly"],
    ["RU-68", "Теперь твоя очередь! Покажи ладошку, говори и следи за пальчиками.", "firefly"],
    ["RU-69", "Ты прошёл всю дорогу до праздника и теперь умеешь рассказывать о себе по-английски! А кто вылупится из яйца — узнаем в следующем приключении.", "firefly"],
    ["RU-70", "Дорожка готова! Нажми на Облачный Остров — полетели дальше.", "firefly"],
    ["RU-71", "Мостик готов! Нажми на Драконий Остров — там нас ждёт праздник.", "firefly"],
    ["RU-72", "Ты прошёл всю дорогу до праздника! Можно заглянуть на любой остров ещё раз.", "firefly"],
    ["RU-73", "Нажми на остров, чтобы продолжить путешествие.", "firefly"],
    ["EN-01", "green", "en"],
    ["EN-01-slow", "green", "en_slow"],
    ["EN-02", "blue", "en"],
    ["EN-02-slow", "blue", "en_slow"],
    ["EN-03", "yellow", "en"],
    ["EN-03-slow", "yellow", "en_slow"],
    ["EN-04", "a top", "en"],
    ["EN-04-slow", "a top", "en_slow"],
    ["EN-05", "jeans", "en"],
    ["EN-05-slow", "jeans", "en_slow"],
    ["EN-06", "shoes", "en"],
    ["EN-06-slow", "shoes", "en_slow"],
    ["EN-07", "a green top", "en"],
    ["EN-07-slow", "a green top", "en_slow"],
    ["EN-08", "a blue top", "en"],
    ["EN-08-slow", "a blue top", "en_slow"],
    ["EN-09", "a yellow top", "en"],
    ["EN-09-slow", "a yellow top", "en_slow"],
    ["EN-10", "green jeans", "en"],
    ["EN-10-slow", "green jeans", "en_slow"],
    ["EN-11", "blue jeans", "en"],
    ["EN-11-slow", "blue jeans", "en_slow"],
    ["EN-12", "yellow jeans", "en"],
    ["EN-12-slow", "yellow jeans", "en_slow"],
    ["EN-13", "green shoes", "en"],
    ["EN-13-slow", "green shoes", "en_slow"],
    ["EN-14", "blue shoes", "en"],
    ["EN-14-slow", "blue shoes", "en_slow"],
    ["EN-15", "yellow shoes", "en"],
    ["EN-15-slow", "yellow shoes", "en_slow"],
    ["EN-16", "I have a green top", "en"],
    ["EN-17", "I have a blue top", "en"],
    ["EN-18", "I have a yellow top", "en"],
    ["EN-19", "I have green jeans", "en"],
    ["EN-20", "I have blue jeans", "en"],
    ["EN-21", "I have yellow jeans", "en"],
    ["EN-22", "I have green shoes", "en"],
    ["EN-23", "I have blue shoes", "en"],
    ["EN-24", "I have yellow shoes", "en"],
    ["EN-25", "I", "en"],
    ["EN-25-slow", "I", "en_slow"],
    ["EN-26", "have", "en"],
    ["EN-26-slow", "have", "en_slow"],
    ["EN-27", "a", "en"],
    ["EN-27-slow", "a", "en_slow"],
    ["EN-28", "top", "en"],
    ["EN-28-slow", "top", "en_slow"],
]

# ─────────────────────────────────────────────────── работа ──

import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

URL = "https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "audio-4-6")

try:                                   # чтобы русские буквы печатались в cmd
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def synth(text, who, voice=None, emotion=None):
    if voice is None:
        voice, emotion = VOICES[who]
    english = who.startswith("en")
    form = {"text": text, "voice": voice, "format": "mp3",
            "lang": "en-US" if english else "ru-RU",
            "speed": SLOW if who == "en_slow" else SPEED,
            "folderId": FOLDER}
    if emotion:
        form["emotion"] = emotion
    req = urllib.request.Request(
        URL, data=urllib.parse.urlencode(form).encode(),
        headers={"Authorization": "Api-Key " + KEY})
    try:
        return urllib.request.urlopen(req, timeout=120).read()
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        # Роль есть не у каждого голоса, и отказ из-за неё выглядит как
        # отказ вообще. Пробуем ещё раз без роли, прежде чем сдаться.
        if e.code == 400 and emotion and "emotion" in body.lower():
            return synth(text, who, voice, None)
        raise RuntimeError("%s %s" % (e.code, body[:300]))


def check_keys():
    if not KEY or not FOLDER:
        stop("Не вписаны KEY и FOLDER в начале файла — без них сервис не "
             "поймёт, кто к нему пришёл.")


def stop(msg):
    print("\n" + msg)
    try:
        input("\nНажмите Enter, чтобы закрыть окно.")
    except Exception:
        pass
    sys.exit(1)


def main():
    args = sys.argv[1:]
    check_keys()

    if args and args[0] in ("obrazcy", "samples"):
        line = "Смотри! Мы на Драконьем Острове. Ой… а где же все?"
        out = os.path.join(HERE, "obrazcy")
        os.makedirs(out, exist_ok=True)
        for v in SAMPLES:
            try:
                data = synth(line, "firefly", v, "good")
            except RuntimeError as e:
                print("  %-12s — нет такого голоса (%s)" % (v, str(e)[:60]))
                continue
            with open(os.path.join(out, v + ".mp3"), "wb") as f:
                f.write(data)
            print("  %-12s — записан" % v)
        print("\nОбразцы лежат в папке obrazcy рядом с этим файлом.")
        print("Послушайте и, если нужно, поменяйте имена в таблице VOICES.")
        return

    only = set(a for a in args if a.startswith(("RU-", "EN-")))
    os.makedirs(OUT, exist_ok=True)
    done = skipped = 0
    for key, text, who in TRACKS:
        path = os.path.join(OUT, key + ".mp3")
        if os.path.exists(path) and (not only or key not in only):
            skipped += 1
            continue
        for attempt in range(4):
            try:
                data = synth(text, who)
                break
            except RuntimeError as e:
                msg = str(e)
                if msg.startswith("429") and attempt < 3:
                    time.sleep(2 * (attempt + 1))
                    continue
                if msg.startswith("401") or msg.startswith("403"):
                    stop("Сервис не принял ключ (%s).\nПроверьте KEY и FOLDER "
                         "и что сервисному аккаунту выдана роль "
                         "ai.speechkit-tts.user." % msg[:40])
                stop("Дорожка %s не записалась: %s" % (key, msg[:300]))
        with open(path, "wb") as f:
            f.write(data)
        done += 1
        print("  %-12s %s" % (key, text[:58]))
        time.sleep(0.2)

    print("\nЗаписано %d, уже было %d. Файлы в папке audio-4-6." % (done, skipped))
    print("Положите эту папку в Google Drive и напишите мне.")
    try:
        input("\nНажмите Enter, чтобы закрыть окно.")
    except Exception:
        pass


if __name__ == "__main__":
    main()
