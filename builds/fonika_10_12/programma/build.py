# Программа курса «Reading Club 10+» (фоника 10–12) → HTML → PDF (Playwright)
import re, sys, os, subprocess, json
OUT = os.path.dirname(os.path.abspath(__file__))

# ---------- шифр (pigpen) ----------
def glyph(ch, size=34, stroke="#1f2a44"):
    ch = ch.lower(); s = size; m = 4; a, b = m, s - m
    L = []
    def ln(x1, y1, x2, y2): L.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
    grid = "abcdefghi"; grid2 = "jklmnopqr"; x1 = "stuv"; x2 = "wxyz"
    dot = False
    if ch in grid or ch in grid2:
        if ch in grid2: dot = True; ch = grid[grid2.index(ch)]
        r, c = divmod(grid.index(ch), 3)
        top = r > 0; bot = r < 2; left = c > 0; right = c < 2
        if top: ln(a, a, b, a)
        if bot: ln(a, b, b, b)
        if left: ln(a, a, a, b)
        if right: ln(b, a, b, b)
    else:
        if ch in x2: dot = True; ch = x1[x2.index(ch)]
        cx = cy = s / 2
        if ch == "s": ln(a, a, cx, cy); ln(cx, cy, b, a)      # открыт вверх
        if ch == "t": ln(a, a, cx, cy); ln(cx, cy, a, b)      # открыт влево
        if ch == "u": ln(b, a, cx, cy); ln(cx, cy, b, b)      # открыт вправо
        if ch == "v": ln(a, b, cx, cy); ln(cx, cy, b, b)      # открыт вниз
    d = f'<circle cx="{s/2}" cy="{s/2 if ch not in "stuv" else (s*0.7 if ch=="s" else s*0.3 if ch=="v" else s/2)}" r="2.6" fill="{stroke}"/>' if dot else ""
    if dot and ch in "tu": d = f'<circle cx="{s*0.3 if ch=="t" else s*0.7}" cy="{s/2}" r="2.6" fill="{stroke}"/>'
    return f'<svg width="{s}" height="{s}" viewBox="0 0 {s} {s}" stroke="{stroke}" stroke-width="2.6" stroke-linecap="round" fill="none">{"".join(L)}{d}</svg>'

def key(letters, closed=""):
    cells = []
    for ch in letters:
        cells.append(f'<div class="k"><div>{glyph(ch)}</div><b>{ch}</b></div>')
    for ch in closed:
        cells.append('<div class="k off"><div class="q">?</div><b>&nbsp;</b></div>')
    return '<div class="key">' + "".join(cells) + "</div>"

def coded(text):
    out = []
    for w in text.split(" "):
        g = "".join(glyph(c, 26) if c.isalpha() else f'<span class="p">{c}</span>' for c in w)
        out.append(f'<span class="w">{g}</span>')
    return '<div class="coded">' + "".join(out) + "</div>"

# ---------- программа ----------
M1 = [
 # № , новые звуки, слова, слова-исключения, сообщение, сюжет
 (1, "s a t p i", "sat, tap, pit, tip, pat", "I", "I sat. Tap it.",
  "Sam и Dan находят на шкафчике записку из странных значков. Приходит сообщение от «Агента X»: прочитать её могут только те, кто знает код."),
 (2, "n m d o g", "man, dog, dig, pond, map", "the", "Sam and Dan: dig in the pit!",
  "Надпись на стене школьного двора — теперь ребята могут прочитать свои имена."),
 (3, "c k e u r", "cat, kid, pen, sun, red", "said, are, you", "Run! Get the red cup.",
  "Записка под красной кружкой в столовой."),
 (4, "h b f l j", "hat, bus, fun, leg, jam", "is, he, she, to", "Get on the big red bus. Sit at the top.",
  "Подсказка на автобусной остановке."),
 (5, "v w x y z qu", "van, wet, box, yes, zip, quiz", "was, my, go, no", "Zip up the box. It is in the van.",
  "Коробка в фургоне доставки — ключ собран почти целиком."),
 (6, "Алфавит: имена букв, порядок, гласные a e i o u", "Sam: S-A-M, TV, PE, DJ", "—", "From A to Z.",
  "«Мастер-ключ»: все 26 символов открыты. У каждой буквы есть звук и имя."),
 (7, "«Волшебная e»: a_e i_e o_e u_e — одно правило", "tape, pine, hope, cube, bike", "have, one", "Hide the code at nine. Take the bike.",
  "«Хитрость немой буквы»: символ e в конце гаснет и заставляет гласную сказать своё имя."),
 (8, "sh · ch · th", "ship, fish, chip, much, thin, this", "do, some, come", "Shh! Chat at the chip shop. Then run!",
  "«Двойные коды»: два знакомых символа, склеенные вместе, звучат по-новому."),
 (9, "ee · oo · ar", "tree, moon, book, car, park", "your, who", "Meet at the park at noon. Look at the green car.",
  "Встреча в парке — ребята близко к разгадке."),
 (10, "Повторение · итоговый текст · итоговый тест", "", "", "You did it! Come to the club!",
  "Финал: «Агент X» — девушка из старших классов, которая ведёт тайный клуб дешифровщиков. Сертификат."),
]
M2 = [
 (11, "ee · ea", "see, tree, sea, read", "Сезон 2: у одноклассницы пропал телефон. Первая подсказка — на экране."),
 (12, "ai · ay", "rain, train, play, day", "Ждём на вокзале под дождём."),
 (13, "oa · ow (snow)", "boat, road, snow, slow", "Лодка у реки."),
 (14, "igh · y (fly)", "light, night, my, try", "Ночной фонарь: почему он мигает?"),
 (15, "oo · oo (moon / book)", "food, moon, book, look", "Комната с книгами."),
 (16, "ar · or", "car, park, fork, sport", "Спортивная площадка, тёмный угол."),
 (17, "ur · er · ir", "burn, her, girl, first", "Девочка в фиолетовой футболке."),
 (18, "ow · ou · oi · oy", "now, out, coin, boy", "Мальчик с монетой — дело почти раскрыто."),
 (19, "Повторение · -ing / -ed · итоговый тест", "", "Дело закрыто, сертификат дешифровщика."),
]

# ---------- проверка декодируемости сообщений ----------
learned = set(); tricky = set(); bad = []
extra = {1: set(), 6: set(), 10: set()}
for n, snd, _, tw, msg, _ in M1:
    if n <= 5: learned |= set(snd.replace("qu", "q u").split())
    tricky |= {t.strip() for t in tw.split(",") if t.strip() not in ("—", "")}
    for w in re.findall(r"[A-Za-z]+", msg):
        lw = w.lower()
        if lw in {t.lower() for t in tricky} or lw == "i": continue
        if n >= 6: continue
        if not set(lw) <= learned: bad.append((n, w))
print("недекодируемые слова в сообщениях:", bad or "нет")

STRUCT = [
 ("1", "Mission briefing", "Пришло сообщение символами, часть ключа — «?»", "1", ""),
 ("2", "Code review", "Символ → буква → звук; слова-исключения прошлых уроков", "2", "+3 · слова на время, личный рекорд"),
 ("3", "HW check", "1–2 слова, где были ошибки в ДЗ", "1", ""),
 ("4", "New code", "«This is c. Sound /k/.» + слово-якорь с картинкой", "4", ""),
 ("5", "Hear it", "Устно: первый звук слова, деление на звуки, звук → буква", "2", ""),
 ("6", "Write it", "Буква со стрелками → 3 раза в тетради → списать 2 слова", "3", "+2 · списать ещё 3 слова"),
 ("7", "Blending", "Звуковые кнопки: звуки → слово; картинка — после прочтения", "4", "+3 · «Настоящее слово или фейк?»"),
 ("8", "Word building", "Собрать слово из букв-магнитов по картинке", "2", ""),
 ("9", "Tricky words", "Слова-исключения урока: запоминаем целиком", "2", ""),
 ("10", "Dictation", "4 слова на слух — в тетради", "3", "+2 · фраза на слух"),
 ("11", "Decode the message", "Фразы обычными буквами → сообщение символами → чтение → 2 вопроса", "5", ""),
 ("12", "Mission complete", "Счётчик слов, что умею, ДЗ, монетки", "1", ""),
]

def m1rows():
    r = []
    for n, snd, words, tw, msg, plot in M1:
        r.append(f'<tr><td class="n">{n}</td><td><b class="snd">{snd}</b><div class="mut">{words}</div></td>'
                 f'<td>{tw}</td><td><div class="msg">{msg}</div><div class="mut">{plot}</div></td></tr>')
    return "".join(r)
def m2rows():
    return "".join(f'<tr><td class="n">{n}</td><td><b class="snd">{s}</b><div class="mut">{w}</div></td><td class="mut">{p}</td></tr>' for n, s, w, p in M2)
def strows():
    return "".join(f'<tr><td class="n">{a}</td><td><b>{b}</b></td><td>{c}</td><td class="c">{d}</td><td class="mut">{e}</td></tr>' for a, b, c, d, e in STRUCT)

CSS = """
@page{size:A4;margin:14mm 14mm 16mm}
*{box-sizing:border-box} body{font-family:Inter,sans-serif;color:#1f2a44;font-size:10.2pt;line-height:1.42;margin:0}
h1{font-family:'Inter Display',Inter;font-size:30pt;line-height:1.05;margin:0 0 6px;letter-spacing:-.5px}
h2{font-family:'Inter Display',Inter;font-size:15pt;margin:20px 0 8px;color:#1f2a44;break-after:avoid}
h3{font-size:11pt;margin:14px 0 6px;break-after:avoid}
p{margin:0 0 7px} .mut{color:#6a7389;font-size:9pt} .lead{font-size:11.5pt;color:#38425c}
.cover{background:#1f2a44;color:#fff;border-radius:14px;padding:26px 26px 22px;margin-bottom:16px}
.cover .tag{color:#ffcf5c;font-weight:700;letter-spacing:1.5px;font-size:9pt;text-transform:uppercase}
.cover p{color:#d7dcea}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:10px 0}
.card{background:#f3f5fa;border-radius:10px;padding:9px 11px} .card b{display:block;font-size:12.5pt;color:#1f2a44} .card span{color:#6a7389;font-size:8.6pt}
table{width:100%;border-collapse:collapse;margin:6px 0 4px;break-inside:auto} tr{break-inside:avoid}
th{font-size:8.4pt;text-transform:uppercase;letter-spacing:.6px;color:#6a7389;text-align:left;padding:6px 7px;border-bottom:2px solid #1f2a44}
td{padding:5px 7px;border-bottom:1px solid #e1e5ee;vertical-align:top}
td.n{font-weight:700;color:#e0663e;width:26px;font-size:11pt} td.c{text-align:center;font-weight:700}
.snd{font-size:10.5pt} .msg{font-family:'DejaVu Sans Mono',monospace;font-size:9pt;background:#fff6dc;border-radius:6px;padding:3px 7px;display:inline-block;margin-bottom:3px}
.key{display:flex;flex-wrap:wrap;gap:5px;margin:8px 0}
.k{border:1.5px solid #c9d0de;border-radius:8px;padding:4px 4px 2px;text-align:center;width:44px;background:#fff}
.k b{font-size:11pt} .k.off{background:#eef0f5;border-style:dashed} .q{height:34px;line-height:34px;font-size:16pt;color:#9aa3b8}
.coded{display:flex;flex-wrap:wrap;gap:12px;background:#f3f5fa;border-radius:10px;padding:10px 12px;margin:6px 0}
.coded .w{display:inline-flex;gap:2px;align-items:center} .coded .p{font-size:14pt;font-weight:700;margin-left:1px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.box{border:1.5px solid #e1e5ee;border-radius:10px;padding:10px 12px;margin:6px 0}
.box.warm{background:#fff6dc;border-color:#f1dca0}
ul{margin:4px 0 6px;padding-left:18px} li{margin:2px 0}
.pb{break-before:page}
.foot{margin-top:14px;color:#9aa3b8;font-size:8pt}
"""

sample_msg = "Run! Get the red cup."
html = f"""<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>Reading Club 10+ — программа курса</title><style>{CSS}</style></head><body>

<div class="cover">
 <div class="tag">WowSpeak · курс чтения · 10–12 лет</div>
 <h1>Reading Club 10+</h1>
 <p style="font-size:12.5pt;color:#fff;margin-bottom:8px">Учимся читать по-английски, взламывая код</p>
 <p>Программа курса фоники для учеников 10–12 лет, которые не читают или читают с большим трудом.</p>
</div>

<div class="grid">
 <div class="card"><b>10 уроков</b><span>буквы, алфавит, «волшебная e», основные сочетания</span></div>
 <div class="card"><b>30 / 40 мин</b><span>один план, в режиме 40 — дополнительные экраны</span></div>
 <div class="card"><b>онлайн</b><span>интерактивный урок на платформе + домашка</span></div>
 <div class="card"><b>≈ 140 слов</b><span>читает ученик к концу курса</span></div>
</div>

<h2>Для кого и зачем</h2>
<p>Ученикам 10–12 лет, которые два–четыре года учили английский в школе, но не научились читать. Названия букв они обычно знают («эй, би, си»), а сложить звуки в слово не могут. Прежний курс чтения им не подходил: картинки с монстриками слишком детские, буквы шли по алфавиту по пять за урок, ch, sh и th — все в одном уроке, а на само чтение времени почти не оставалось.</p>
<p><b>Цель:</b> ученик читает короткие слова и простые тексты сам, по звукам, а не угадывает. После курса он идёт в обычную группу Go Getter; остальные написания (ai, oa, igh и другие) встречает там.</p>

<h2>На чём стоит курс</h2>
<ul>
 <li><b>Систематическая фоника.</b> Звуки идут не по алфавиту, а группами, из которых сразу складываются слова: s a t p i → sat, tap, pit. Порядок — как в Jolly Phonics и Genki Phonics.</li>
 <li><b>Больше чтения, меньше знакомства с буквой.</b> На новые звуки — не больше пяти минут урока. Остальное — слышать звуки, писать, читать слова, фразы и текст.</li>
 <li><b>Каждый урок кончается текстом</b> только из пройденных звуков и выученных слов-исключений — ученик читает его сам, без угадывания.</li>
 <li><b>Письмо — лесенкой:</b> написать букву → списать слово → собрать из букв-магнитов → диктант.</li>
 <li><b>Подача по возрасту:</b> герои — подростки, тексты — записки, переписка, объявления. Картинки — полуреалистичный 3D, как в Go Getter.</li>
 <li><b>Для русскоязычных отдельно:</b> h ≠ х, w, th, краткие a и e, буквы, похожие на русские (p, c, x, y, H, B).</li>
</ul>

<h2 class="pb">История и шифр</h2>
<p class="lead">Чтение по-английски — это и есть расшифровка (decoding). Поэтому ученик не «учит буквы, как малыш», а взламывает код.</p>
<p><b>Герои:</b> Sam (Саманта) и Dan, 11–12 лет. Их имена ученик прочитает уже на уроке 2. В городе кто-то оставляет записки, написанные значками. Каждый урок открывает новые символы шифра — и приходит новое сообщение, которое теперь можно прочитать. В конце курса выясняется, кто такой «Агент X», и ребят приглашают в тайный клуб дешифровщиков.</p>

<h3>Как выглядит шифр</h3>
<p>У каждой буквы свой символ. Внизу экрана — ключ: открытые символы подписаны, закрытые — «?». Пример: урок 3, пройдены s a t p i n m d o g, открываются c k e u r.</p>
{key("satpinmdogckeur", "bfhjlqvwxyz")}
<p>Сообщение урока 3 символами — ученик расшифровывает его по ключу, а потом читает обычными буквами:</p>
{coded(sample_msg)}
<p class="mut">Ответ: «{sample_msg}». Символы на этом листе — эскиз (по мотивам старинного шифра pigpen); финальные нарисуем одним стилем.</p>

<div class="two">
 <div class="box"><b>Сочетания (урок 8)</b><br>Не новые символы, а склейка двух уже открытых: символ s + символ h, сцепленные вместе, — один звук /ʃ/. Ученик видит, что sh — две знакомые буквы, которые вместе звучат по-новому.</div>
 <div class="box"><b>«Волшебная e» (урок 7)</b><br>Символ e в конце слова «гаснет» — молчит, а от него стрелка к гласной: «скажи своё имя». tap → tape, pin → pine.</div>
</div>
<p class="mut">Шифра в уроке одно короткое сообщение: расшифровка тренирует узнавание букв, а читает ученик обычными буквами.</p>

<h2>Мотивация</h2>
<ul>
 <li><b>Счётчик слов</b> в конце урока: «теперь ты можешь прочитать 140 слов» — видимый рост своего умения.</li>
 <li><b>Личный рекорд</b> скорости чтения — соревнование только с собой.</li>
 <li><b>Ранг агента:</b> новичок → агент → старший агент → дешифровщик; сертификат в конце курса.</li>
 <li><b>Монетки платформы</b> — как во всех курсах школы.</li>
 <li>Учитель по-русски объясняет, зачем это: школьный английский станет легче.</li>
</ul>

<h2 class="pb">Как устроен урок</h2>
<p>Один скелет на все уроки, кроме первого; задания и игры внутри меняются. В режиме 40 минут добавляются экраны, помеченные «+». Кнопка <b>⭐ Extra</b> — «If time»: 2–3 игры в запас.</p>
<table><thead><tr><th>№</th><th>этап</th><th>что происходит</th><th>30 мин</th><th>40 мин — добавляется</th></tr></thead>
<tbody>{strows()}<tr><td></td><td><b>Итого</b></td><td></td><td class="c">30</td><td class="mut">+10</td></tr></tbody></table>
<div class="box warm"><b>If time — игры, меняются от урока к уроку</b> (в каждом уроке минимум две интересные, а не «выбери вариант»): «Скоростной дешифратор» — слово мелькает на 2 секунды; «Взломщик» — слово символами на время; «Поймай звук» — нажми, когда услышишь звук; «Сортировка на слух»; «Буквы-магниты» — собери слово; «Найди слово» в сетке букв.</div>
<p><b>Урок 1 отличается:</b> повторять ещё нечего, брифинг длиннее (кто такой Агент X, что такое шифр и ключ), сообщение совсем короткое. <b>Ученику к каждому уроку нужны тетрадь и ручка</b> — сообщаем заранее.</p>
<p><b>Буквы и звуки.</b> На карточке — одной строкой: «This is <b>c</b>. Sound /k/.» Имя буквы не прячем (со школы его знают), но и не разбираем — разница «имя / звук» объясняется на уроке 6. У каждой буквы одно слово-якорь с картинкой (cat, kid, egg, up, red); остальные слова — материал для чтения, их значение показывает картинка после прочтения.</p>

<h2 class="pb">10 уроков · буквы, алфавит, «волшебная e», основные сочетания</h2>
<p class="mut">Слова-исключения читаются не по правилам (said, you) — их запоминаем целиком. Сообщение — текст, который ученик расшифровывает в конце урока.</p>
<table><thead><tr><th>№</th><th>звуки · примеры</th><th>слова-исключения</th><th>сообщение · сюжет</th></tr></thead><tbody>{m1rows()}</tbody></table>


<h2>Чего в курсе нет — и почему</h2>
<ul>
 <li><b>ck, ff, ll, ss</b> — читаются как одна буква, ученик справляется и без отдельного урока.</li>
 <li><b>Долгие гласные другими написаниями</b> — ai/ay, ea, oa/ow, igh/y, or, ur/er/ir, ow/ou, oi/oy — и редкие: ear, air, ure, ph, wh, wr, le, ew, aw, ie, мягкие <b>c</b> и <b>g</b>. Курс даёт основу: буквы, «волшебную e» и главные сочетания; остальное ученик встречает в Go Getter.</li>
 <li>Из 56 слов-исключений берём около 30 самых частых.</li>
</ul>

<h2>Входная проверка</h2>
<p>5–10 минут, интерактивным экраном: звуки 10 букв · 6 коротких слов · 4 выдуманных слова (dut, pim — читает ли по звукам или угадывает) · 4 слова с сочетаниями и «волшебной e» · слова-исключения. По результату — с какого урока начинать: 1 или 6–7; кто читает всё — курс не нужен, сразу в Go Getter. <span class="mut">Где проводить — до курса (на вводном уроке) или в начале урока 1 — решаем.</span></p>

<h2>Что получает школа</h2>
<ul>
 <li>10 интерактивных уроков на платформе (30 и 40 минут, If time) и план учителя к каждому;</li>
 <li>домашка к каждому уроку (6–8 заданий), итоговый тест;</li>
 <li>история с героями и картинками в одном стиле, сертификат дешифровщика.</li>
</ul>
<p class="foot">WowSpeak · Reading Club 10+ · программа курса · черновик для согласования</p>
</body></html>"""
open(os.path.join(OUT, "programma.html"), "w").write(html)
print("ok")
