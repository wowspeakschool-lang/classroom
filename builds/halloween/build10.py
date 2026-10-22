import re, json, base64, os
SRC = '/root/.claude/uploads/804eac6d-911f-5112-b4f5-c1e3887b7b56/6c5036b9-halloween_lesson_4-6.html'
music = 'data:audio/mpeg;base64,' + base64.b64encode(open('mus/spook_soft.mp3','rb').read()).decode()  # Spookchosic track, softened
T = open('lesson10.html').read()

A = {}
for f in os.listdir('a10'):
    k, ext = os.path.splitext(f)
    mime = 'image/webp' if ext == '.webp' else 'image/jpeg'
    A[k] = f'data:{mime};base64,' + base64.b64encode(open('a10/' + f, 'rb').read()).decode()

CSS = """body{font-family:'Segoe UI',Arial,sans-serif;background:#f5f0fa;color:#2a1550;padding:24px;max-width:1150px;margin:0 auto;line-height:1.5}
h1{color:#5a2ea8;font-size:26px}.meta,.voc{background:#fff;border-radius:12px;padding:14px 18px;margin:12px 0;box-shadow:0 2px 8px rgba(0,0,0,.08)}.meta b{color:#5a2ea8}
.warn{background:#fff3cd;border:3px solid #e8631a;border-radius:12px;padding:14px 18px;margin:12px 0;font-weight:700;color:#8a3c08;font-size:16px}
table{width:100%;border-collapse:collapse;margin:14px 0;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 10px rgba(0,0,0,.1)}
th{background:#7b4bd6;color:#fff;padding:10px 12px;text-align:left;font-size:14px}td{padding:10px 12px;border-bottom:1px solid #eee;vertical-align:top;font-size:14px}
tr:nth-child(even){background:#faf7fe}.pg{font-weight:700;color:#e8631a;font-size:18px;text-align:center;width:46px}.tl{color:#1a7a3a;font-style:italic;width:22%}.sa{color:#1f5fa8;font-style:italic;width:22%}"""

def plan(beg):
    B = lambda b, c: b if beg else c
    CLUE = " В конце — карточка улики, она попадает в блокнот (слева). Next — дальше."
    rows = [
     ('<b>Начало: площадь и Золотая тыква → газета (3 шага, Next).</b> На экране площадь Spooky Town, на постаменте — Золотая тыква (она мигает). '
      + B('Ученик пробует назвать её; Next / нажатие на тыкву — появляется слово <b>a golden pumpkin</b> и звучит. ', 'Учитель спрашивает, что это и зачем она на площади. Next / нажатие на тыкву — ок. ')
      + 'Next — тыква исчезает (тот же кадр, пустой постамент). Next — вылетает газета ' + B('«WHERE IS THE GOLDEN PUMPKIN?»', '«THIEF STEALS THE GOLDEN PUMPKIN!»') + '. Расскажите историю (см. выше).',
      B('"Look! What\'s this?" "It\'s a golden pumpkin. Repeat!" "Where is the pumpkin now?"', '"What can you see?" "What happened to the pumpkin?" "What does the newspaper say?"'),
      B('"A pumpkin!" "A golden pumpkin!" "I don\'t know!"', '"It\'s a golden pumpkin." "It disappeared! Someone stole it."')),
    ] + ([
     ('<b>Halloween-слова (6 карточек):</b> a witch, a vampire, a mummy, a werewolf, a skeleton, a ghost — это и есть подозреваемые. Сначала только картинки. Ученик пробует назвать, нажатие показывает слово и <b>произносит его</b>. Next открывает следующую карточку. Повторить хором. <br><i>Остальные слова урока у начинающих подписаны прямо на экране</i> (фонарик, стрелки на карте, отличия, правда/ложь, улики на допросе) — заранее их учить не нужно.',
      '"Who is this?" "Is it a witch or a ghost?" "Repeat!"',
      '"A witch!" "A vampire!" "It\'s a ghost!"')] if beg else []) + [
     (B('<b>Подозреваемые.</b> Шесть карточек: портрет и имя. <b>Сначала ученик сам говорит, кто это</b> («She is a witch»), <b>потом нажимаем и проверяем</b> — открывается фраза. Next открывает следующую. ',
        '<b>Подозреваемые.</b> Шесть карточек: портрет и имя. Ученик выбирает, о ком узнать, — нажатие открывает информацию. Next открывает следующую. ')
      + '<b>Вор каждый раз выбирается случайно</b> — заранее его не знает никто.',
      B('"Who is this? Is she a witch?" "Say: She is a…"', '"Tell me about Count Vlad." "What does he look like?" "Who do you think is the thief?"'),
      B('"Wanda. She is a witch." "He is a vampire."', '"He is tall. He has got a black cape. He sleeps all day."')),
     ('<b>Фонарик (3 раунда).</b> Тёмная площадь, предметы спрятаны. Учитель водит фонарик мышкой (фонарик стоит там, где его оставили), ученик говорит, куда светить. Нашли — нажмите на предмет. Последний предмет — часы.' + B(' Рядом с заданием — картинка того, что ищем.', '') + CLUE,
      '"Find the lantern! Left or right? Up or down?"', B('"Left! Up! Here!" "A watch!"', '"Go left… stop! It\'s a watch. It stopped at 9:15!"')),
     ('<b>Свидетель (3 вопроса).</b> Сова Mrs Owl рассказывает, что видела. ' + B('Учитель читает фразу, ученик выбирает картинку. <b>Подписей нет.</b> Перед первым раундом попросите ученика <b>показать руками tall и short</b>, потом выбрать силуэт.', 'Учитель читает рассказ (он на экране), ученик отвечает на вопросы и выбирает ответ.') + ' Нажмите на верный вариант.' + CLUE,
      B('"Show me tall! Show me short!" "Is the thief tall or short?" "What colour is the scarf?" "Where is the thief?"', '"Read the owl\'s story. What time was it? What was the person wearing? Where did they go?"'),
      B('(показывает руками) "Tall!" "Red!" "The park!"', '"It was quarter past nine." "A long black coat." "They went to the park."')),
     ('<b>Шифровка.</b> Записка из символов, внизу — алфавит-ключ. Ученик находит символ в ключе и называет букву, учитель нажимает на символ в записке — появляется буква. ' + B('Послание: I LOVE CANDIES.', 'Послание: SEE YOU AT THE CAFE.') + CLUE,
      '"What letter is this?" "Find the symbol in the key." "What does the note say?"', B('"I… L-O-V-E… I love candies!"', '"S-E-E… See you at the cafe! The thief went to the cafe."')),
     ('<b>Следы.</b> Карта городка. ' + B('Пунктиром мигают следы следующего шага, ученик говорит направление: up / down / left / right.', '<b>Подсказок на карте нет</b>: ученик читает указание справа и говорит направление; следы появляются только после верной стрелки.') + ' Учитель нажимает стрелку — кошка идёт. 5 шагов, в конце — старая башня.' + CLUE,
      B('"Where are the footprints? Up or down?"', '"Read the next step. Where do we go?"'),
      B('"Left!" "Up!" "Right!"', '"Go left to the park." "Turn right and go to the cafe."')),
     ('<b>До и после (6 отличий).</b> Площадь до кражи и после. Ученик называет отличия, учитель нажимает на них (на любой картинке).' + B(' У найденного отличия появляется слово.', '') + CLUE,
      B('"What\'s different?"', '"Compare the pictures. What happened?"'),
      B('"The pumpkin!" "The glasses!" "A cat!" "The lamp!"', '"In the first picture there is a pumpkin. In the second picture there isn\'t." "The bench fell over." "The jar is empty — someone ate the lollipops!"')),
    ] + ([] if beg else [
     ('<b>What happened last night? (5 карточек).</b> Ученик восстанавливает путь вора по порядку — как шли по следам. Нажимаете на карточку, которую называет ученик: верная встаёт в ленту, неверная трясётся («Try again!»). Над ячейками — First, Then, After that, Next, Finally: ученик рассказывает историю целиком.',
      '"What happened first? And then?" "Tell me the whole story."',
      '"First, at 9:15 the thief took the Golden Pumpkin. Then the thief ran to the park. After that… Finally, the thief climbed the old tower."'),
     ('<b>Spot the lie (3 раунда).</b> Трое подозреваемых рассказывают, что видели ночью. Один врёт — его слова не сходятся с уликами. Ученик находит лжеца и объясняет, почему; нажмите на него — штамп LIE! и ответ внизу. Это <b>не</b> про алиби и на поиск вора не влияет. Вывод: «They\'re lying! We need a truth elixir!»',
      '"Who is lying? Why?" "How do you know?"',
      '"Count Vlad is lying. The pumpkin was stolen at 9:15, so he couldn\'t see it at 10 o\'clock."'),
    ]) + [
     ('<b>Правда или ложь (6 утверждений).</b> Проверяем, что запомнили. Ученик отвечает, учитель нажимает TRUE / FALSE: верная кнопка «вдавливается» с ✓, при ошибке — «Try again!». Награда — <b>эликсир правды</b>' + B(' (карточка «Look! The truth elixir!»)', '') + '. <i>Объясните по-русски: кошка нашла волшебный эликсир — кто его выпьет, не сможет соврать. На допросе подозреваемые выпьют его и будут отвечать честно.</i>',
      '"Is it true or false?"', B('"True!" "False! The scarf is red."', '"False. The thief went to the park, not to the cinema."')),
     ('<b>Рентген сумок (все 6 подозреваемых).</b> У каждого своя сумка. Нажмите на сумку — сверху вниз проходит лазер, внутри видны тени предметов. Ученик угадывает предмет, учитель нажимает на тень — предмет проявляется. У двух случайных подозреваемых (но никогда не у вора) в сумке <b>билет в кино на 9:00</b> — это алиби, они получают штамп NOT GUILTY.',
      B('"What\'s in the bag? Is it a key?" "Has she got a ticket?"', '"What can you see in the bag? Where was he at 9:15?"'),
      B('"A key! A phone! A ticket!"', '"It\'s a cinema ticket. He was at the cinema, so he is not guilty."')),
    ] + ([] if beg else [
     ('<b>Prepare your questions.</b> Для каждой улики ученик сам пишет вопрос полностью и нажимает ✓ (или Enter). Регистр и знаки не важны. Неверно — поле трясётся. 💡 — подсказка: слова вопроса вперемешку. Next — подставляет правильный вопрос.',
      '"Write a question for each clue." "Check the word order."',
      '"Where were you at 9:15?" "Did you go to the park?" "Did you go to the cafe?" "Did you climb the tower?" "Did you eat the lollipops?"'),
    ]) + [
     ('<b>Допрос. Решает ученик.</b> Подозреваемые пьют эликсир правды. <b>Сначала нажмите на улику</b> (слева) — появится вопрос. Ученик задаёт его, учитель <b>нажимает на подозреваемого</b> — тот отвечает. Справа — решение по выбранному подозреваемому: <b>NOT GUILTY</b> или <b>THE THIEF!</b> Нажимаете, когда ученик сам скажет и объяснит. Если решение неверное, программа не даст его принять. Передумал — нажмите на подозреваемого со штампом и <b>↩ Undo</b> (снимаются и штампы с рентгена).',
      B('"Choose a clue. Ask Wanda!" "Is she the thief? Yes or no?"', '"Choose a clue. Ask everybody. Who is not guilty? Why?"'),
      B('"Have you got a watch?" — "Yes, I have. / No, I haven\'t." "Wanda — not guilty!"', '"Where were you at 9:15?" — "I was at home." "Did you go to the cafe?" — "No, I didn\'t." "He is not guilty because he didn\'t go to the cafe."')),
     ('<b>Финал.</b> Вор в наручниках у полицейского участка, кошка с Золотой тыквой, «CASE CLOSED!». Сразу выскакивает окно <b>«What\'s your name, detective?»</b> — ученик вписывает имя, ✓ — имя появляется на значке. ✏️ Name — исправить, 💾 Save — скачать картинку. Справа кнопки <b>🏁 Finish</b> (сразу на финальный слайд) и <b>⭐ Extra</b> (дополнительные задания: bucket list, потом настольная игра).',
      B('"Who is the thief?" "What\'s your name, detective?" "Well done!"', '"Who stole the pumpkin? How do you know?"'),
      B('"It\'s Count Vlad!" "My name is…"', '"It\'s Count Vlad because he went to the cafe and he climbed the tower."')),
     ('<b>Бонус (если есть время): Halloween bucket list.</b> Нажатие на карточку — в список, нажатие в списке — убрать. Внизу можно дописать свой пункт. Внизу справа кнопки 🏁 Finish (на финальный слайд) и ⭐ Extra (настольная игра).',
      B('"What do you want to do on Halloween?"', '"What would you like to do this Halloween? Why?"'),
      B('"I want to carve a pumpkin."', '"I\'d like to go to a party because I love costumes."')),
     ('<b>Extra: настольная игра «Spooky Town».</b> Сюда ведёт кнопка ⭐ Extra на странице bucket list. Выберите фишки (1–5 игроков, можно вписать имена) → ▶ Play. Кубик — по очереди (Next тоже бросает). ' + B('На клетках картинки — только 6 слов урока (witch, vampire, mummy, werewolf, skeleton, ghost): «Who is it?» — ученик называет.', 'На клетках «?» — вопрос о Хэллоуине (How do people celebrate Halloween in your country?, What scares you the most?, Tell a short scary story in three sentences.). Ученик отвечает развёрнуто.') + ' ⏩ +2, ⏪ −2, ⭐ — весёлое задание (Make a scary face! / Say BOO! / Fly like a bat!). Кто первым дошёл до башни 🏁 — победил. 🏁 Finish внизу справа — закончить урок в любой момент.',
      B('"Who is it?" "Roll the dice!"', '"Roll the dice!" "Answer the question. Tell us more!" "Why?"'),
      B('"It\'s a witch!" "It\'s a werewolf!"', '"I\'d like to be a vampire because…" "I don\'t believe in ghosts because…"')),
     ('<b>Finish.</b> «Great job, detective! Happy Halloween!» — конфетти, прощаемся.', '"Great job! Happy Halloween! Bye!"', '"Happy Halloween!"'),
    ]
    rows = [(i + 1,) + r for i, r in enumerate(rows)]
    title = 'Halloween 10–12 — ' + B('beginners', 'advanced') + ': «The Golden Pumpkin Mystery»'
    voc = B('<b>Новые слова:</b> witch, vampire, mummy, werewolf, skeleton, ghost. <b>С подсказками на экране:</b> watch, scarf, glasses, boots, candies, ticket, tall, short, park, cafe, church, cinema • Have you got…? Yes, I have / No, I haven\'t • Do you like…? Yes, I do / No, I don\'t • up, down, left, right • colours. <b>Только Present Simple и to be — без прошедшего времени.</b>',
            'Past Simple: Did you…? Yes, I did / No, I didn\'t • was / were, was wearing • Where were you at…? • time: quarter past nine • go past, turn left / right • because')
    h = f'<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8"><title>План урока — {title}</title><style>{CSS}</style></head><body><h1>🔍 План урока: {title}</h1>'
    h += '<div class="meta"><b>Длительность:</b> 40 мин. &nbsp; <b>Мотивация:</b> детектив — ученик ищет улики, получает эликсир правды, допрашивает подозреваемых и находит вора Золотой тыквы. Вор каждый раз случайный.</div>'
    h += '<div class="meta"><b>📖 История (расскажите в начале, по-русски или простыми фразами):</b> В маленьком городке Spooky Town на главной площади стояла <b>Золотая тыква</b> — главное украшение праздника Хэллоуин. Вечером 30 октября, ровно в 9:15, она пропала! Утром 31-го об этом написали все газеты. Полиция не справляется, поэтому зовут лучшего детектива — <b>ученика</b>. Помогает ему кошка-сыщик <b>Inspector Whiskers</b>. Подозреваемых шестеро: ведьма Wanda, вампир Count Vlad, мумия Mumford, оборотень Wolfie, скелет Mr Bones и привидение Boo. За урок детектив соберёт пять улик, найдёт <b>эликсир правды</b> (кто его выпьет, не может соврать), проверит сумки, допросит подозреваемых и найдёт вора. <b>Вор каждый раз выбирается случайно</b> — даже учитель не знает его заранее.</div>'
    h += '<div class="warn">⚠️ ЕСЛИ НЕ ХВАТАЕТ ВРЕМЕНИ — НАЖМИТЕ ЗНАЧОК 🗄 (EVIDENCE ROOM, ВВЕРХУ СПРАВА, РЯДОМ С 📋). ОН ЕСТЬ НА ВСЕХ СТРАНИЦАХ ДО ДОПРОСА. УЧЕНИК НАЖИМАЕТ НА УЛИКИ, КОТОРЫХ У НЕГО ЕЩЁ НЕТ, — И ВЫ СРАЗУ ПЕРЕХОДИТЕ К ДОПРОСУ. СТРЕЛКА ← ВЕРНЁТ НА СТРАНИЦУ, С КОТОРОЙ ВЫ ПРИШЛИ.</div>'
    h += '<table><tr><th>Стр.</th><th>Задание и инструкция</th><th>Teacher\'s language</th><th>Suggested answers / Students\' answers</th></tr>'
    h += ''.join(f'<tr><td class="pg">{a}</td><td>{b}</td><td class="tl">{c}</td><td class="sa">{d}</td></tr>' for a, b, c, d in rows) + '</table>'
    h += f'<div class="voc"><b>🗂️ Лексика и грамматика:</b> {voc}</div>'
    h += '<div class="voc" style="font-size:13px;color:#777"><b>Навигация:</b> ← → — назад / пропустить; Next загорается, когда задание выполнено, а в играх с раундами ведёт к следующему раунду (подсказывает ответ). Кружочки страниц вверху слева кликабельны. 🗄 — склад улик, 📋 — этот план, 🎵 — музыка.</div></body></html>'
    return h

for level, fname, title in [('beg', 'halloween_lesson_10-12_beginners.html', 'Golden Pumpkin Mystery · 10–12 beginners'),
                            ('cont', 'halloween_lesson_10-12_advanced.html', 'Golden Pumpkin Mystery · 10–12 advanced')]:
    t = T.replace('__ASSETS__', json.dumps(A)).replace('__MUSIC__', music).replace('__LEVEL__', level)
    t = t.replace('__PLAN__', json.dumps(__import__('hwplan').add(plan(level == 'beg'), '10b' if level == 'beg' else '10c'))).replace('__TITLE__', title)
    open(fname, 'w').write(t)
    print(fname, len(t))
