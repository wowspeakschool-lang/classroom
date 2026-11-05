# -*- coding: utf-8 -*-
import json, io, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import teksty

BIDS = {(c, u): b for c, u, b in json.load(io.open(sys.argv[1], encoding='utf-8'))}
CHISLA_BID = "d5115f02-08d0-4c15-93be-a2b1571e9b00"
BASE = "https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/"
FOLDER = {"gg3": "gg2%20%2B%20gg3/", "sm3": "sm3/"}

def q(s): return "'" + s.replace("'", "''") + "'"

out = ["-- Аудирования GG3 и SM3: новые тексты и вопросы (решение Анны 05.11.2026)",
       "-- В каждом рассказе 2-3 человека, все варианты ответа звучат в записи.",
       "-- Копия блоков — classroom_backup_listening_v2_20261105", ""]
spisok = []
for (course, unit), v in sorted(teksty.NARRATIONS.items()):
    url = BASE + FOLDER[course] + v['file']
    qs = [{"q": qt, "options": [{"text": o} for o in opts], "correct": [0]} for qt, opts in v['questions']]
    patch = {"title": v['title'], "questions": qs, "audio": url, "skill": "listening"}
    out.append("-- %s unit %s, блок %s — %s" % (course, unit, v['block'], v['file']))
    out.append("update classroom_blocks set payload = payload || %s::jsonb where id = '%s';"
               % (q(json.dumps(patch, ensure_ascii=False)), BIDS[(course, unit)]))
    spisok.append((course, unit, v['block'], v['file'], v['text']))

out.append("-- sm3 unit 0, блок 9 — числа, звука не было вовсе")
out.append("update classroom_blocks set payload = payload || %s::jsonb where id = '%s';"
           % (q(json.dumps({"audio": BASE + FOLDER['sm3'] + teksty.CHISLA['file'],
                            "skill": "listening"}, ensure_ascii=False)), CHISLA_BID))
io.open('builds/listening_v2/listening_v2_20261105.sql', 'w', encoding='utf-8').write("\n".join(out) + "\n")

m = ["# Озвучка: новые аудирования тестов Go Getter 3 и Super Minds 3",
     "",
     "Тексты переписаны 05.11.2026. В каждом рассказе два-три человека, и **все три",
     "варианта ответа звучат в записи** — прежние были слишком лёгкими: один герой,",
     "каждый факт назван один раз, неверные варианты в записи не звучали вовсе.",
     "Старые записи этих блоков больше не подходят: вопросы другие.",
     "",
     "**Как делать.** Yandex SpeechKit, английский голос, одна дорожка на текст,",
     "пауза около секунды между предложениями, перед «Number N» — около двух.",
     "",
     "**Словарь подмен обязателен** — `docs/ozvuchka_speechkit.md`: headache → head ake,",
     "stomachache → stomak ake, toothache → tooth ache, earache → ear ake, cough → coff,",
     "TV → tee vee, café → caffay, library → lybrary, bowl → bowle, Liam → Leeam.",
     "Подмена делается **только в тексте для синтеза**, сам текст в репозитории не меняем.",
     "",
     "**Куда класть.** Бакет `classroom-media`: GG3 — папка `gg2 + gg3`, SM3 — папка `sm3`.",
     "Имя файла — ровно как указано ниже. Ссылки в блоки уже вписаны: как файл появится",
     "под этим именем, запись заиграет сама, в базе больше ничего делать не нужно.",
     "",
     "Всего 20 файлов: 9 — Go Getter 3, 10 — Super Minds 3, плюс один с числами.",
     ""]
for course, unit, block, fname, text in spisok:
    m += ["---", "", "## %s · Unit %s Test · блок %s" % (course.upper(), unit, block), "",
          "Файл: `%s`" % fname, "", "```", text, "```", ""]
m += ["---", "", "## SM3 · Unit 0 Test · блок 9 — числа", "",
      "У этого блока звука не было вообще: задание «послушай и выбери число»,",
      "а слушать нечего. Ответы: 24, 39, 52, 76, 100.", "",
      "Файл: `%s`" % teksty.CHISLA['file'], "", "```", teksty.CHISLA['text'], "```", ""]
io.open('builds/listening_v2/dlya_chata_ozvuchki.md', 'w', encoding='utf-8').write("\n".join(m) + "\n")
print("блоков:", len(spisok) + 1)
