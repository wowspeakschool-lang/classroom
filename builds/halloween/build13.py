import re, json, base64, os
SRC = '/root/.claude/uploads/804eac6d-911f-5112-b4f5-c1e3887b7b56/6c5036b9-halloween_lesson_4-6.html'
music = 'data:audio/mpeg;base64,' + base64.b64encode(open('mus/spook_soft.mp3','rb').read()).decode()  # Spookchosic track, softened
T = open('lesson13.html').read()
A = {}
for f in os.listdir('a13'):
    k, ext = os.path.splitext(f)
    mime = 'image/webp' if ext == '.webp' else 'image/jpeg'
    A[k] = f'data:{mime};base64,' + base64.b64encode(open('a13/' + f, 'rb').read()).decode()
BUB = json.load(open('jack_bubbles.json'))
CSS = """body{font-family:'Segoe UI',Arial,sans-serif;background:#f6efe2;color:#2a1a10;padding:24px;max-width:1150px;margin:0 auto;line-height:1.5}
h1{color:#8a3c08;font-size:26px}.meta,.voc{background:#fff;border-radius:12px;padding:14px 18px;margin:12px 0;box-shadow:0 2px 8px rgba(0,0,0,.08)}.meta b{color:#8a3c08}
.warn{background:#fff3cd;border:3px solid #c0392b;border-radius:12px;padding:14px 18px;margin:12px 0;font-weight:700;color:#7a1f12;font-size:16px}
table{width:100%;border-collapse:collapse;margin:14px 0;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 10px rgba(0,0,0,.1)}
th{background:#6e3510;color:#fff;padding:10px 12px;text-align:left;font-size:14px}td{padding:10px 12px;border-bottom:1px solid #eee;vertical-align:top;font-size:14px}
tr:nth-child(even){background:#fbf6ec}.pron{width:auto;min-width:420px;box-shadow:none;margin:10px 0 0}.pron td{padding:5px 14px;font-size:15px}.pg{font-weight:700;color:#c0392b;font-size:18px;text-align:center;width:46px}.tl{color:#1a7a3a;font-style:italic;width:22%}.sa{color:#1f5fa8;font-style:italic;width:22%}"""

def plan(beg):
    B = lambda b, c: b if beg else c
    DIG = ' За задание — <b>цифра кода</b> (появляется в панели CODE слева). <b>Ученик записывает её в тетрадь.</b>'
    rows = [
     ('<b>Lead-in.</b> Улица в ночь Хэллоуина. Вопрос <b>What\'s the topic?</b> — ученик угадывает, Next открывает ответ «Halloween». Дальше учитель <b>сам задаёт 1–2 вопроса</b> (на экране их нет).',
      B('"What\'s the topic?" "Do you like Halloween?" "Do you carve a pumpkin?"', '"What\'s the topic?" "What symbols of Halloween do you know?" "Do people celebrate Halloween in your country?"'),
      B('"Halloween!" "Yes, I do. / No, I don\'t."', '"Halloween!" "Pumpkins, ghosts, bats, witches…" "Not really, but some young people have parties."')),
     ('<b>Слова (' + B('6', '8') + ').</b> Сначала картинка: ученик пробует назвать, нажатие показывает слово и <b>произносит</b>. Next открывает следующую.',
      '"What\'s this?" "Repeat!"', B('"A pumpkin! A turnip! A bonfire…"', '"A lantern. The harvest…"')),
     ('<b>Zoom in (' + B('5', '6') + ' раундов).</b> Картинка сильно увеличена и медленно отдаляется. Ученик называет слово как можно раньше; нажатие на картинку / Next — слово появляется на экране (без озвучки: произносит ученик). В конце — <b>половинка ключа</b>.',
      '"What is it? Guess!" "Quick!"', '"Is it a candle?" "It\'s a bonfire!"'),
     ('<b>Missing letters (' + B('5', '6') + ' слов).</b> Картинка и слово, в котором пропущены ' + B('3', '3–4') + ' буквы. Ученик называет буквы, учитель нажимает их на клавиатуре. Слева медленно проявляется и растёт <b>призрак</b> (' + B('24', '18') + ' сек.), каждая неверная буква его приближает. Успели — призрак исчезает; не успели — «BOO!», недостающие буквы появляются красным. Next — подсказка.' + ' В конце — <b>вторая половинка ключа</b>.',
      '"Which letters are missing? Spell the word."', B('"U, M, K — pumpkin!"', '"B-O-N-F-I-R-E."')),
     ('<b>Особняк.</b> Две половинки ключа (за Zoom in и Missing letters) уже соединились в панели KEY. Нажмите на дверь (или Next) — ключ летит в замок, дверь со скрипом открывается.',
      B('"Look! A big house. It\'s a mansion. Let\'s go in!"', '"What can you see? Would you go inside?"'), B('"Yes!"', '"It looks scary but I\'d go in."')),
     ('<b>Холл: фонарик.</b> Темно. Учитель водит фонарик мышкой — фонарик стоит там, где его оставили (без мыши Next сам подводит его к следующему предмету), ученик говорит, куда светить, и называет найденные предметы — учитель нажимает. Нашли всё — зажигается свет, на экране распахнутая входная дверь… и она <b>захлопывается</b>. Записка: ' + B('«You can\'t go out! Find the code. Every room has one number.»', '«The door is locked. To escape, find the 5-digit code. Each room hides one digit.»') + ' Дальше 5 комнат = 5 цифр. <b>Попросите ученика приготовить тетрадь или листок: каждую полученную цифру он записывает.</b>',
      '"Where shall I shine the torch? Left or right?" "What\'s that?"', B('"Left! A candle!"', '"Go up… stop! It\'s an old lantern."')),
     ('<b>Библиотека: Samhain.</b> Текст, где выученные слова заменены картинками: ученик читает вслух и вместо картинки называет слово (нажатие на картинку показывает слово). Потом — <b>True / False</b> (6); текст остаётся на экране, ученик ищет ответ в нём. ' + B('Текст из коротких простых предложений.', 'Past Simple, passive (were lit), used to.') + DIG,
      '"Read the text, please." "Is it true or false?"', B('"Samhain is a Celtic festival — true!"', '"False — bonfires were lit at the end of the harvest, not to celebrate the summer."')),
     ('<b>Кухня: комикс «Samhain night».</b> Ирландия, давным-давно: Нора и её брат Лиам готовятся к Самайну — фонарь из репы, костёр, призрак, маски. 6 кадров, в каждом два облачка. ' + B('В каждом кадре одна реплика уже вписана; ученик выбирает вторую из 6 фраз справа и нажимает на пустое облачко.', 'Ученик вписывает все 12 реплик (сначала фразы к кадрам 1–3, потом к 4–6): выбирает фразу справа и нажимает на облачко. Потом <b>пересказывает историю</b>: First… Then… In the end…') + ' Неверно — кадр трясётся. В конце — карточка о фонарях из репы.' + DIG,
      B('"Who is this? What does she say?" "Read the dialogue in roles."', '"Who says this? Why do they wear masks? Retell the story."'), B('"Mum: Make a lantern!"', '"First, Nora carved a turnip… In the end the ghost ran away from the lantern."')),
     (B('<b>Бальный зал: guising.</b> Короткий текст с картинками-словами, потом 6 костюмов: ученик говорит «I want to be a…», учитель нажимает.',
        '<b>Бальный зал: откуда традиции.</b> Соедините традицию и её происхождение (нажать слева, потом справа). Потом обсуждение: «What would you dress up as and why?» — 6 костюмов для опоры.') + DIG,
      B('"What do you want to be?"', '"Where does trick-or-treating come from?" "What would you dress up as? Why?"'), B('"I want to be a vampire!"', '"I\'d dress up as a pirate because…"')),
     ('<b>Подвал: Myth or fact? (6).</b> Утверждение с картинкой, кнопки MYTH / FACT. После верного ответа — короткое объяснение. Среди фактов — самая тяжёлая тыква в мире: 1 247 кг (рекорд Гиннесса, 2023).' + B(' Утверждения короткие, в Present Simple.', '') + DIG,
      '"Myth or fact? Why do you think so?"', B('"Fact!"', '"It\'s a myth — the first lanterns were turnips."')),
     ('<b>Чердак: Halloween goes to America.</b> ' + B('5', '6') + ' карточек без дат. Ученик говорит, что было раньше, учитель нажимает на карточку — она встаёт в первую свободную ячейку (нажатие на карточку в ячейке возвращает её). Когда все разложены — <b>✓ Check</b>: на всех карточках появляются даты, верные остаются на месте (зелёные), неверные возвращаются вниз — ученик раскладывает их заново, уже по датам.' + DIG,
      '"What happened first? And then? Now look at the dates."', B('"The Celts celebrate Samhain. Then…"', '"In the 1840s Irish families moved to America and brought Halloween with them."')),
     ('<b>Дверь.</b> Ученик называет код по своим записям в тетради (сверить можно с панелью CODE), учитель вводит его на замке. Неверно — замок трясётся. Next вводит код сам.',
      '"What\'s the code?"', '"Seven, two, nine, four, one!"'),
     ('<b>Escaped!</b> Дверь открывается на праздник. Окно «What\'s your name?» → ' + B('карточка <b>«Well done! Great job, [имя]! You found the code. You are free!»</b>', '<b>сертификат</b> «This is to certify that [имя] escaped from Samhain Mansion on Halloween night»') + ', 💾 Save — скачать картинкой. Внизу <b>🏁 Finish</b> (финальный слайд) и <b>⭐ Extra</b> (доп. задания).',
      '"Congratulations! You escaped!"', '"Yay!"'),
     ('<b>Extra 1: Halloween bucket list.</b> Нажатие на карточку — в список, в списке — убрать, внизу свой пункт.',
      B('"What do you want to do on Halloween?"', '"Imagine your perfect Halloween night. What would you do?"'), B('"I want to carve a pumpkin."', '"I\'d like to visit a haunted house because…"')),
     ('<b>Extra 2: настольная игра.</b> Фишки (1–5 игроков, можно вписать имена) → ▶ Play. Кубик по очереди. ' + B('На клетках картинки — только 6 слов урока (pumpkin, turnip, bonfire, costume, ghost, candle): «What is it?» — ученик называет.', 'На клетках «?» — вопросы о Хэллоуине, отвечать развёрнуто.') + ' ⏩ +2, ⏪ −2, ⭐ весёлые задания. Первый у дверей особняка — победил.',
      B('"What is it?"', '"Answer the question. Why?"'), B('"It\'s a lantern."', '"I don\'t believe in ghosts because…"')),
     ('<b>Finish.</b> «Well done! Happy Halloween!»', '"Happy Halloween! Bye!"', '"Happy Halloween!"'),
    ]
    rows = [(i + 1,) + r for i, r in enumerate(rows)]
    title = 'Halloween 13+ — ' + B('beginners', 'advanced') + ': «Samhain Mansion»'
    h = f'<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8"><title>План урока — {title}</title><style>{CSS}</style></head><body><h1>🗝 План урока: {title}</h1>'
    h += '<div class="meta"><b>Длительность:</b> 40 мин. &nbsp; <b>Мотивация:</b> escape room — ученик собирает ключ от особняка, попадает внутрь, дверь захлопывается; в каждой из 5 комнат он узнаёт кусок истории Хэллоуина и получает цифру кода. Код каждый урок новый.</div>'
    h += '<div class="meta"><b>📖 История для учителя:</b> Хэллоуин начался больше 2000 лет назад с кельтского праздника <b>Samhain</b> — конец урожая и начало зимы; верили, что граница между миром живых и мёртвых в эту ночь тонкая, жгли костры и наряжались, чтобы духи не узнали. Позже Церковь сделала 1 ноября Днём всех святых (All Hallows\' Day), вечер накануне — <b>All Hallows\' Eve → Halloween</b>. Легенда о <b>Скупом Джеке</b> объясняет фонарь jack-o\'-lantern: в Ирландии и Шотландии их резали из <b>репы</b>, в Америке — из тыквы. Дети ходили по домам в масках, пели и читали стихи за угощение (<b>guising</b>) — отсюда trick-or-treat. В 1840-х ирландские переселенцы привезли праздник в Америку; слова «trick or treat» впервые напечатаны в Канаде (Альберта) в 1927 г. Сегодня американцы тратят на Хэллоуин около 13,1 млрд $ (прогноз NRF на 2025 г.). Факты сверены с источниками (Tourism Ireland, Smithsonian, Guinness, NRF).</div>'
    PRON = [('Samhain', '/ˈsaʊɪn/'), ('Halloween', '/ˌhæləʊˈiːn/'), ("All Hallows' Eve", '/ˌɔːl ˈhæləʊz ˈiːv/'), ("All Saints' Day", '/ˌɔːl ˈseɪnts deɪ/'),
            ('Celts', '/kelts/'), ('Celtic', '/ˈkeltɪk/'), ('harvest', '/ˈhɑːvɪst/'), ('costume', '/ˈkɒstjuːm/'), ('guising', '/ˈɡaɪzɪŋ/'),
            ('mansion', '/ˈmænʃn/'), ('spirits', '/ˈspɪrɪts/'), ('haunted', '/ˈhɔːntɪd/'), ('vampire', '/ˈvæmpaɪə/'), ('pirate', '/ˈpaɪrət/'),
            ('myth', '/mɪθ/'), ('centuries', '/ˈsentʃəriz/'), ('recognise', '/ˈrekəɡnaɪz/'), ('Guinness', '/ˈɡɪnɪs/'), ('carve', '/kɑːv/'), ('carving', '/ˈkɑːvɪŋ/')]
    h += '<div class="meta"><b>🗣 Произношение.</b> Перед уроком убедитесь, что правильно произносите эти слова (британская транскрипция):<table class="pron">' + ''.join('<tr>' + ''.join(f'<td><b>{w}</b></td><td>{t}</td>' for w, t in PRON[i:i + 2]) + '</tr>' for i in range(0, len(PRON), 2)) + '</table></div>'
    h += '<div class="warn">⚠️ ЕСЛИ НЕ ХВАТАЕТ ВРЕМЕНИ — НАЖМИТЕ ЗНАЧОК 🗝 (CODE ROOM, ВВЕРХУ СПРАВА, РЯДОМ С 📋). ОН ЕСТЬ НА ВСЕХ СТРАНИЦАХ ДО ДВЕРИ. ЗА КАЖДУЮ НЕДОСТАЮЩУЮ ЦИФРУ УЧЕНИК ОТВЕЧАЕТ НА ОДИН БЫСТРЫЙ ВОПРОС (ВЫБОР ИЗ ТРЁХ), ПОТОМ — СРАЗУ К ДВЕРИ. СТРЕЛКА ← ВЕРНЁТ ТУДА, ОТКУДА ВЫ ПРИШЛИ.</div>'
    h += '<table><tr><th>Стр.</th><th>Задание и инструкция</th><th>Teacher\'s language</th><th>Suggested answers / Students\' answers</th></tr>'
    h += ''.join(f'<tr><td class="pg">{a}</td><td>{b}</td><td class="tl">{c}</td><td class="sa">{d}</td></tr>' for a, b, c, d in rows) + '</table>'
    voc = B('pumpkin, turnip, bonfire, costume, ghost, candle • Do you…? Yes, I do / No, I don\'t • I want to be a… • Present Simple, to be, there is / are',
            'pumpkin, turnip, bonfire, costume, ghost, candle, lantern, harvest • Past Simple, Past Continuous, used to, passive (were lit, was shortened) • I\'d dress up as… because… • myth / fact')
    h += f'<div class="voc"><b>🗂️ Лексика и грамматика:</b> {voc}</div>'
    h += '<div class="voc" style="font-size:13px;color:#777"><b>Навигация:</b> ← → — назад / пропустить; Next ведёт к следующему раунду (подсказывает ответ), когда задание выполнено — к следующей странице. Кружочки вверху слева кликабельны. 🗝 — Code room, 📋 — этот план, 🎵 — музыка.</div></body></html>'
    return h

for level, fname, title in [('beg', 'halloween_lesson_13plus_beginners.html', 'Samhain Mansion · 13+ beginners'),
                            ('cont', 'halloween_lesson_13plus_advanced.html', 'Samhain Mansion · 13+ advanced')]:
    t = T.replace('__ASSETS__', json.dumps(A)).replace('__MUSIC__', music).replace('__LEVEL__', level).replace('__BUBBLES__', json.dumps(BUB))
    t = t.replace('__PLAN__', json.dumps(__import__('hwplan').add(plan(level == 'beg'), '13b' if level == 'beg' else '13c'))).replace('__TITLE__', title)
    open(fname, 'w').write(t)
    print(fname, len(t))
