#!/usr/bin/env python3
"""Заменяет награды курса на волшебные предметы (решение Анны от 16.09.2026).

Было: кристалл, палочка, меч, медаль, корона, дракон — шесть трофеев без
назначения. Меч вдобавок спорил с каноном: злодея в истории нет.

Стало пять предметов, каждый нужен в дороге и выдаётся до того, как понадобится:
  звёздочка  (начало У1, светит весь урок)    a star
  бутылочка  (конец У1, для дороги в У2)      a bottle
  сапоги     (конец У2, донесут в У3)         boots
  колокольчик(конец У3, им будят Дракона в У4) a bell
  корона     (конец У4, подарок Дракона)      a crown

Дракон остаётся героем финала, но в рюкзак не кладётся: в рюкзак кладут вещи.
"""
import base64, io, os, re
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS = os.path.join(ROOT, "lessons", "wowspeak-mini")
ITEMS_DIR = os.path.join(ROOT, "assets", "items")
NEW_ITEMS = ["star", "bottle", "boots", "bell"]
OLD_ITEMS = ["crystal", "wand", "sword", "medal"]

RU = {"star": "звёздочка", "bottle": "бутылочка", "boots": "сапоги-скороходы",
      "bell": "колокольчик", "crown": "корона"}
EN = {"star": "a star", "bottle": "a bottle", "boots": "boots",
      "bell": "a bell", "crown": "a crown"}


def item_uri(name):
    im = Image.open(os.path.join(ITEMS_DIR, name + ".png")).convert("RGBA")
    b = im.getbbox() or (0, 0, im.width, im.height)
    im = im.crop(b)
    side = max(im.size)
    sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    sq.paste(im, ((side - im.width) // 2, (side - im.height) // 2))
    sq = sq.resize((320, 320), Image.LANCZOS)
    buf = io.BytesIO()
    sq.save(buf, "WEBP", quality=88, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()


def screen_span(s, sid):
    """Границы объекта экрана с данным id в тексте урока."""
    m = re.search(r'id:\s*"%s"' % re.escape(sid), s)
    assert m, "экран %s не найден" % sid
    start = s.rfind("{", 0, m.start())
    depth, i = 0, start
    while i < len(s):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return start, i + 1
        i += 1
    raise AssertionError("не закрыт объект экрана " + sid)


def set_fields(s, sid, **fields):
    a, b = screen_span(s, sid)
    obj = s[a:b]
    for key, val in fields.items():
        literal = val if isinstance(val, str) and val.startswith("[") else '"%s"' % val
        pat = re.compile(r'(\b%s\s*:\s*)(\[[^\]]*\]|"(?:[^"\\]|\\.)*")' % re.escape(key))
        if pat.search(obj):
            obj = pat.sub(lambda m: m.group(1) + literal, obj, count=1)
        else:  # поля нет — дописываем сразу после id
            obj = re.sub(r'(id:\s*"[^"]+",)', r'\1 %s: %s,' % (key, literal), obj, count=1)
    return s[:a] + obj + s[b:]


PLAN = {
 1: {
  "1-1": dict(speech="Привет! Я Хранительница Слов, и я очень рада тебя видеть. Сегодня мы "
                     "вместе выучим несколько новых английских слов и поиграем. Поехали!"),
  "1-2": dict(speech="Смотри — это твой рюкзак. В нём будут волшебные вещи, которые помогут "
                     "тебе в пути по Волшебной стране. Первую я дам прямо сейчас."),
  "1-3": dict(speech="Держи звёздочку — «a star». Она светит и подсказывает, куда какая вещь. "
                     "Произнеси: «a star». Сегодня она нам очень пригодится!",
              pic="star", emoji="⭐", en="a star", ru="звёздочка", autoPlayEN="a star"),
  "7-1": dict(speech="Ты выучил 7 новых английских слов! Держи волшебную бутылочку — "
                     "«a bottle». Вода в ней никогда не кончается, а дорога до Острова "
                     "Зеркал длинная.",
              pic="bottle", emoji="🍶", en="a bottle", ru="бутылочка", autoPlayEN="a bottle"),
 },
 2: {
  "1-2": dict(earned='["star","bottle"]', filledSlots="2",
              speech="Смотри, вот твой рюкзак. В нём уже две волшебные вещи — звёздочка "
                     "и бутылочка. Сегодня добудешь третью!"),
  "7-1": dict(speech="Молодец! Держи сапоги-скороходы — «boots». В них ты быстро доберёшься "
                     "до Острова Друзей.",
              pic="boots", emoji="👢", en="boots", ru="сапоги-скороходы", autoPlayEN="boots"),
  "7-2": dict(earned='["star","bottle","boots"]',
              speech="Смотри — в рюкзаке уже три волшебные вещи! Ты отлично поработал сегодня."),
 },
 3: {
  "1-2": dict(earned='["star","bottle","boots"]',
              speech="Смотри, у тебя уже три волшебные вещи — звёздочка, бутылочка и сапоги. "
                     "Сегодня добудешь четвёртую! А сначала — вспомним прошлый урок."),
  "7-1": dict(speech="Бен и Мия дарят тебе колокольчик — «a bell». Он ещё пригодится: "
                     "у Замка спит Дракон, и разбудить его можно только звоном.",
              pic="bell", emoji="🔔", en="a bell", ru="колокольчик", autoPlayEN="a bell"),
  "7-2": dict(earned='["star","bottle","boots","bell"]',
              speech="Смотри — в рюкзаке уже четыре волшебные вещи! Ты отлично поработал сегодня."),
 },
 4: {
  "1-2": dict(earned='["star","bottle","boots","bell"]',
              speech="Смотри, у тебя уже четыре волшебные вещи — звёздочка, бутылочка, сапоги "
                     "и колокольчик. Сегодня получишь последнюю! А сначала — вспомним всё, "
                     "что ты выучил."),
  "3-1": dict(speech="Позвони в колокольчик! Слышишь? Дракон просыпается — «a dragon». "
                     "Он огромный, добрый и очень рад тебе.",
              pic="dragon", emoji="🐉", en="a dragon", ru="дракон", autoPlayEN="a dragon"),
  "3-2": dict(earned='["star","bottle","boots","bell"]',
              speech="Дракон проснулся, и праздник вот-вот начнётся! Осталась одна вещь — "
                     "её подарит тебе сам Дракон. А сейчас — твой проект."),
  "7-1": dict(speech="Дракон дарит тебе корону — «a crown»! Ты прошёл всю Волшебную страну "
                     "и заслужил её.",
              pic="crown", emoji="👑", en="a crown", ru="корона", autoPlayEN="a crown"),
  "7-2": dict(earned='["star","bottle","boots","bell","crown"]',
              speech="Смотри — все пять волшебных вещей собраны, рюкзак полон! И ты прошёл "
                     "4 урока из 4. Ты молодец!"),
 },
}

PROJECT_ACH_NEW = ('const PROJECT_ACH = [\n'
                   + "".join('  { id:"%s", en:"%s", ru:"%s" },\n' % (k, EN[k], RU[k])
                             for k in ["star", "bottle", "boots", "bell", "crown"])
                   + '];')


def patch(n):
    path = os.path.join(LESSONS, "lesson-%d.html" % n)
    s = open(path, encoding="utf-8").read()

    # 1. картинки предметов в IMG
    need = [k for k in NEW_ITEMS if '%s:' % k not in s or ('"%s"' % k) in str(PLAN[n])]
    anchor = re.search(r'(\b(?:IMG|ASSETS)\s*=\s*\{)', s) or re.search(r'(\bbackpack\s*:\s*")', s)
    assert anchor, "не найден объект картинок"
    inject = "".join('\n  %s: "%s",' % (k, item_uri(k)) for k in NEW_ITEMS
                     if not re.search(r'\b%s\s*:\s*"data:' % k, s))
    if inject:
        pos = s.index("{", anchor.start()) + 1
        s = s[:pos] + inject + s[pos:]

    # 2. экраны наград и рюкзака
    for sid, fields in PLAN[n].items():
        s = set_fields(s, sid, **fields)

    # 3. таблица «эмодзи -> картинка»: в Уроке 1 награда подбирается по эмодзи,
    #    а не по полю pic, поэтому без этой правки карточка осталась бы пустой
    emoji_map = re.search(r'EMOJI_KEY = \{[^}]*\}', s)
    assert emoji_map, "EMOJI_KEY не найден"
    s = (s[:emoji_map.start()]
         + 'EMOJI_KEY = { "⭐": "star", "🍶": "bottle", "👢": "boots", "🔔": "bell", '
           '"👑": "crown", "🐉": "dragon", "🎒": "backpack", "🏬": "shop" }'
         + s[emoji_map.end():])

    # 4. звук завершения урока подбирался по мечу и палочке; теперь финальные
    #    награды другие — бутылочка, сапоги, колокольчик и корона
    s, cnt = re.subn(r'if \(s\.emoji === "🪄"(?:\s*\|\|\s*s\.pic === "[a-z]+")*\)',
                     'if (["🍶", "👢", "🔔", "👑"].indexOf(s.emoji) >= 0)', s)
    assert cnt == 1, "условие звука завершения не найдено (%d)" % cnt

    # 5. шесть слотов рюкзака -> пять
    s, cnt = re.subn(r'for \(let i = 0; i < 6; i\+\+\)', 'for (let i = 0; i < 5; i++)', s)
    assert cnt >= 1, "не найден рисовальщик слотов рюкзака"

    # 6. список наград для финального проекта (только Урок 4)
    if n == 4:
        old = re.search(r'const PROJECT_ACH = \[.*?\];', s, re.S)
        assert old, "PROJECT_ACH не найден"
        s = s[:old.start()] + PROJECT_ACH_NEW + s[old.end():]

    # 7. старые награды больше не должны упоминаться
    # Удаляем только внутри объекта с картинками. Раньше чистка висячих запятых
    # шла по всему файлу и задевала посторонний код.
    a = s.index("{", anchor.start())
    depth, i = 0, a
    while i < len(s):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                break
        i += 1
    block = s[a:i + 1]
    for key in OLD_ITEMS:
        # запятая может стоять и до, и после записи (последняя в объекте — без неё)
        block = re.sub(r',?\s*\b%s\s*:\s*"data:image[^"]+"' % key, '', block)
    block = re.sub(r'\{\s*,', '{', block)
    block = re.sub(r',(\s*)\}', r'\1}', block)
    s = s[:a] + block + s[i + 1:]
    leftovers = {k: len(re.findall(r'\b%s\b' % k, s)) for k in OLD_ITEMS}
    assert not any(leftovers.values()), "остались ссылки на старые награды: %s" % leftovers

    open(path, "w", encoding="utf-8").write(s)
    return "готово (%.1f МБ)" % (os.path.getsize(path) / 1048576)


if __name__ == "__main__":
    for n in (1, 2, 3, 4):
        print("Урок %d: %s" % (n, patch(n)))
