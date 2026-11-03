# -*- coding: utf-8 -*-
"""GG2 юниты 1-2: перенумерация блоков и правки payload (вычитка 03.11.2026)."""
import json, sys

LID = {
 'u1hw1': '852fc4ee-b710-458f-8957-3a446e9dc234',
 'u1hw2': '829ba270-7377-43f0-b5ad-093441ba6b07',
 'u1hw3': 'ed03a12f-2fd8-4e50-96a6-e889f97107e5',
 'u1hw4': '851d9b90-f06b-46e5-8fd5-96cec97d6d69',
 'u1hw5': '3894f232-5143-4498-aa0c-c575e0760cc1',
 'u1hw6': '17a7a056-ec35-467b-8b6d-031c50fe937a',
 'u1hw7': '5c0e4d0a-b796-409e-a120-c1e6267d130b',
 'u2hw1': 'abf66c3b-2936-433e-adbf-e516a4552c8b',
 'u2hw2': '0c683af2-bcf7-4b35-9a5a-ca9b82ed81d6',
 'u2hw3': 'd8fbeb71-a2ef-4bfd-a0d9-eb73dae5d5e0',
 'u2hw4': 'edb04172-9975-4411-bda8-74f5592a7a13',
 'u2hw5': 'ccb8ec26-8db1-4014-ba1e-500fc48b8624',
 'u2hw6': '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f',
 'u2hw7': '4d349ca7-4b58-48e8-824a-fcde5e710f54',
}
NEW = {  # новые блоки, которые добавляет gg2_u12_new.sql: их sort_order заняты
 'u1hw2': [4,5,8,9], 'u1hw4': [7,8,9], 'u1hw5': [4], 'u1hw6': [6,8],
 'u2hw3': [5,6,7,8], 'u2hw4': [3,5], 'u2hw5': [5,6], 'u2hw6': [7,8], 'u2hw7': [3],
}
# old -> new
MOVE = {
 'u1hw1': {0:0,1:1,3:2,2:3,9:4,4:5,5:6,6:7,7:8,8:9,10:10,11:11,12:12,13:13},
 'u1hw2': {0:0,1:1,2:2,3:3,4:6,5:7,6:10},
 'u1hw4': {0:0,1:1,2:2,3:3,6:4,4:5,5:6,7:10,8:11},
 'u1hw5': {0:0,1:1,2:2,3:3,4:5,5:6,6:7,7:8,8:9},
 'u1hw6': {0:0,1:1,2:2,3:3,4:4,5:5,6:7,7:9,8:10},
 'u2hw1': {0:0,1:1,5:2,2:3,3:4,4:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12},
 'u2hw3': {0:0,1:1,4:2,2:3,3:4,5:9},
 'u2hw4': {0:0,1:1,2:2,3:6,4:4,5:7,6:8},
 'u2hw5': {0:0,1:1,2:2,3:3,4:4,5:7,6:8},
 'u2hw6': {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:9,8:10},
 'u2hw7': {0:0,1:1,2:2,3:4,4:5,5:6,6:7,7:8,8:9},
}
# блоков в уроке сейчас
CNT = {'u1hw1':14,'u1hw2':7,'u1hw3':12,'u1hw4':9,'u1hw5':9,'u1hw6':9,'u1hw7':12,
       'u2hw1':13,'u2hw2':16,'u2hw3':6,'u2hw4':7,'u2hw5':7,'u2hw6':9,'u2hw7':9}

err = []
for k, mp in MOVE.items():
    if sorted(mp.keys()) != list(range(CNT[k])): err.append(f'{k}: в карте не все старые sort_order')
    if len(set(mp.values())) != len(mp): err.append(f'{k}: дубли новых sort_order')
    final = sorted(list(mp.values()) + NEW.get(k, []))
    if final != list(range(len(final))): err.append(f'{k}: итоговая нумерация с дырой: {final}')
for k, ns in NEW.items():
    if k in MOVE and set(ns) & set(MOVE[k].values()): err.append(f'{k}: новый блок налезает на старый')
    if k not in MOVE:
        final = sorted(list(range(CNT[k])) + ns)
        if final != list(range(len(final))): err.append(f'{k}: итоговая нумерация с дырой: {final}')
if err:
    print('ОШИБКИ:'); [print(' -', e) for e in err]; sys.exit(1)
print('карты перенумерации проверены')

AUD = 'https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg2%20%2B%20gg3/gg2_u2_hw6_b2.mp3'
IMG = 'https://classroom.wowteach.ru/media/'

def q(s):  # литерал json-строки для jsonb_set
    return "'" + json.dumps(s, ensure_ascii=False).replace("'", "''") + "'"
def jq(o):
    return "'" + json.dumps(o, ensure_ascii=False).replace("'", "''") + "'"

E = []  # (lesson_key, new_sort_order, expr) — expr применяется к payload
def ed(k, so, expr): E.append((k, so, expr))

# ── U1 HW1
ed('u1hw1', 8, f"jsonb_set(jsonb_set(payload,'{{title}}',{q('Посмотри на картинку и напиши слово по-английски')}),'{{items,1,prompt}}',{q('')})")
ed('u1hw1', 9, f"""jsonb_set(payload,'{{html}}',{q('<p><img src="'+IMG+'shared/hello_rocket.webp" alt="" style="height:200px"></p><h3>Время почитать 📖</h3><p>Ты выучил и школьные предметы, и школьные принадлежности — молодец! Осталось совсем немного.</p>')})""")
ed('u1hw1', 10, f"""jsonb_set(payload,'{{html}}',{q("<h3>Karen и её расписание</h3><p>Прочитай, что рассказывает Karen, и отметь её любимые школьные предметы.</p><blockquote><p>My name is Karen. I'm 11 years old. My favourite subjects are P.E. and Computer Studies. I have P.E. on Monday and Wednesday and Computer Studies on Friday.</p></blockquote>")})""")
ed('u1hw1', 12, f"""jsonb_set(jsonb_set(payload,'{{title}}',{q('Мои любимые предметы ✍️')}),'{{html}}',{q('<p>А вот и последнее задание. Прочитай ещё раз текст о Karen и письменно перечисли свои любимые школьные предметы.</p><p><i>Например: My favourite subjects are English and Art.</i></p>')})""")

# ── U1 HW3
ed('u1hw3', 0, f"""jsonb_set(payload,'{{html}}',{q('<p><img src="'+IMG+'shared/hello_wave.webp" alt="" style="height:200px"></p><h2>Добро пожаловать в домашку! 👋</h2><p>В этом уроке тебя ждёт интересное видео и классные задания!</p>')})""")
ed('u1hw3', 4, f"""jsonb_set(jsonb_set(payload,'{{title}}',{q('Посмотри видео ещё раз и выбери только верные утверждения')}),'{{questions,0,q}}',{q('')})""")
ed('u1hw3', 10, f"""jsonb_set(jsonb_set(payload,'{{title}}',{q('Ответь на вопросы ✍️')}),'{{html}}',{q('<p>Осталось последнее задание.</p><p>В таблице отмечено, чем любят и не любят заниматься Carla (кошка) и Rocco (енот). Письменно ответь на вопросы из предыдущего упражнения (например: <i>Yes, she does. / No, he doesn\'t.</i>).</p><p><img src="'+IMG+'gg2/u1/book_carla_rocco_table.webp" alt="" style="height:220px"></p><ol><li>Does Carla paint pictures?</li><li>Does Rocco paint pictures?</li><li>Do Rocco and Carla like music?</li><li>Do Rocco and Carla play football?</li><li>Does Rocco play chess?</li><li>Does Carla play chess?</li></ol>')})""")

# ── U1 HW5: картинка подсказывала ответ
ed('u1hw5', 6, "jsonb_set(payload,'{questions,0}', (payload->'questions'->0) - 'image')")

# ── U1 HW7
ed('u1hw7', 5, f"""jsonb_set(payload,'{{html}}',{q('<h3>Теперь соберём предложения 📝</h3><p>Молодец! Ты выполнил бóльшую часть заданий. Дальше — четыре задания, в каждом нужно собрать предложение из слов.</p>')})""")
ed('u1hw7', 10, f"""jsonb_set(jsonb_set(payload,'{{title}}',{q('Составь вопросы ✍️')}),'{{html}}',{q('<p>Это последнее задание. Вспомни вопросы, которые мы учили несколько уроков назад. Обычно я задаю вопрос, а ты отвечаешь. А сейчас наоборот: я напишу ответы, а ты составь и запиши к ним вопросы.</p><p><i>Например: ответ «I\'m eleven». Вопрос к нему — «How old are you?»</i></p><ol><li>I\'m Paul.</li><li>P-A-U-L.</li><li>22 North Street, Oldtown.</li><li>It\'s 02465 438967.</li><li>It\'s paulharris@mymail.com.</li></ol>')})""")

# ── U2 HW1
ed('u2hw1', 0, f"""jsonb_set(payload,'{{html}}',{q('<p><img src="'+IMG+'shared/hello_wave.webp" alt="" style="height:200px"></p><h2>Привет! 👋</h2><p>Надеюсь, ты перекусил перед домашним заданием, так как сегодня нас с тобой ждут вкусняшки 😋</p><p>Выполни все задания, чтобы выучить слова на 100%!</p>')})""")
ed('u2hw1', 6, f"""jsonb_set(payload,'{{html}}',{q('<p><img src="'+IMG+'shared/hello_rocket.webp" alt="" style="height:200px"></p><h3>Теперь слова в предложениях 🚀</h3><p>Ты уже узнаёшь продукты на картинках и на слух. Теперь поставим эти слова в предложения.</p>')})""")
ed('u2hw1', 9, "jsonb_set(jsonb_set(payload,'{title}'," + q('Прочитай рассказ Макса и выбери подходящий вариант для каждого пропуска') + "),'{questions,0}'," + jq({
   "q": "Hi! I have breakfast at 7 a.m. I usually have ___ and milk.", "type": "single",
   "correct": [0], "options": [{"text": "cereal"}, {"text": "chips"}]}) + "::jsonb)")
ed('u2hw1', 10, "jsonb_set(jsonb_set(payload,'{title}'," + q('Вспомни рассказ Макса. Что Макс ест на завтрак, обед и ужин?') + "),'{groups}'," + jq([
   {"name": "breakfast", "items": [{"text": "cereal"}, {"text": "milk"}]},
   {"name": "lunch", "items": [{"text": "pasta"}, {"text": "tuna"}]},
   {"name": "dinner", "items": [{"text": "chicken"}]}]) + "::jsonb)")

# ── U2 HW2
ed('u2hw2', 3, "jsonb_set(jsonb_set(payload,'{title}'," + q('Посмотри на картинку и напиши слово по-английски') +
   "),'{items}', (select jsonb_agg(jsonb_set(it,'{prompt}','\"\"') order by ord) from jsonb_array_elements(payload->'items') with ordinality t(it,ord)))")
ed('u2hw2', 4, f"""jsonb_set(payload,'{{html}}',{q('<p><img src="'+IMG+'shared/hello_wave.webp" alt="" style="height:200px"></p><h3>Новое правило 💪</h3><p>Слова ты уже знаешь — теперь разберёмся с исчисляемыми и неисчисляемыми существительными. После этих заданий ты будешь легко их различать.</p>')})""")
ed('u2hw2', 10, f"""jsonb_set(payload,'{{title}}',{q('Прочитай рецепт Ани и выбери правильный вариант для каждого пропуска')})""")
ed('u2hw2', 11, f"""jsonb_set(jsonb_set(payload,'{{title}}',{q('А теперь потренируемся составлять вопросы. Выбери правильный вариант')}),'{{questions,0,q}}',{q('___ there ___ sugar?')})""")
ed('u2hw2', 14, f"""jsonb_set(jsonb_set(payload,'{{title}}',{q('Диалог о списке продуктов ✍️')}),'{{html}}',{q('<p>А это последнее задание. Составь и запиши диалог о списке продуктов. Можешь взять диалог из предыдущего упражнения в качестве примера. Удачи, ты обязательно справишься!</p><p><i>Shopping list: apples, carrots, chicken, cheese, curry sauce, doughnuts</i></p>')})""")

# ── U2 HW3
ed('u2hw3', 0, f"""jsonb_set(payload,'{{html}}',{q('<p><img src="'+IMG+'shared/hello_highfive.webp" alt="" style="height:200px"></p><h2>Привет! 👋</h2><p>В этом уроке мы научимся считать неисчисляемые продукты и спрашивать, сколько чего есть: <b>How much</b> и <b>How many</b>. Как это возможно? Давай начнём — и узнаешь!</p><p>У тебя всё получится. Удачи! ❤️</p>')})""")

# ── U2 HW4
ed('u2hw4', 7, f"""jsonb_set(jsonb_set(payload,'{{title}}',{q('Свой диалог в кафе ✍️')}),'{{html}}',{q('<p>Осталось последнее задание. Твоя задача — составить и записать диалог. Используй диалог из предыдущих упражнений как пример.</p>')})""")

# ── U2 HW5
ed('u2hw5', 3, f"""jsonb_set(payload,'{{title}}',{q('Прочитай текст о Сьюзи и ответь на вопросы')})""")

# ── U2 HW6: запись — внутрь заданий, а не текстом перед ними
ed('u2hw6', 1, "payload - 'audio'")
ed('u2hw6', 2, "jsonb_set(jsonb_set(jsonb_set(payload,'{title}'," + q('Прослушай аудио и выбери, что Пенни будет на завтрак. Верных ответов несколько') +
   "),'{questions,0,q}'," + q('What would Penny like for breakfast?') + "),'{questions,0,audio}'," + q(AUD) + ")")
ed('u2hw6', 3, "jsonb_set(jsonb_set(jsonb_set(payload,'{title}'," + q('Прослушай аудио ещё раз и выбери правильный вариант') +
   "),'{questions,0,q}'," + q('Penny has P.E. ___.') + "),'{questions,0,audio}'," + q(AUD) + ")")
ed('u2hw6', 4, "jsonb_set(payload,'{audio}'," + q(AUD) + ")")
ed('u2hw6', 6, f"""jsonb_set(payload,'{{title}}',{q('Прочитай письмо Стива и выбери because или so для каждого пропуска')})""")

# ── U2 HW7
ed('u2hw7', 0, f"""jsonb_set(payload,'{{html}}',{q('<p><img src="'+IMG+'shared/hello_wave.webp" alt="" style="height:200px"></p><h2>Привет! 👋</h2><p>Рада, что ты заглянул в домашку! Сегодня мы с тобой выполним несколько полезных упражнений, которые помогут тебе закрепить полученные знания. Let\'s go!</p>')})""")
ed('u2hw7', 8, f"""jsonb_set(jsonb_set(payload,'{{title}}',{q('Рецепт любимого завтрака ✍️')}),'{{html}}',{q('<p>А это последнее задание. Напиши рецепт своего любимого завтрака. Можешь использовать рецепт тостов из предыдущего задания как пример.</p>')})""")

# ═══ SQL ═══
out = ['-- GG2 юниты 1-2: перенумерация и правки payload (вычитка 03.11.2026)', 'begin;', '',
       '-- 1. перенумерация: сдвиг в запас, потом на место']
for k, mp in MOVE.items():
    out.append(f"update classroom_blocks set sort_order = sort_order + 1000 where lesson_id = '{LID[k]}';")
    for old, new in sorted(mp.items(), key=lambda x: x[1]):
        out.append(f"update classroom_blocks set sort_order = {new} where lesson_id = '{LID[k]}' and sort_order = {old + 1000};")
    out.append('')
out.append('-- 2. правки payload (по НОВЫМ номерам)')
for k, so, expr in E:
    out.append(f"update classroom_blocks set payload = {expr}, updated_at = now()\n  where lesson_id = '{LID[k]}' and sort_order = {so};")
out += ['', 'commit;']
path = '/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/gg2_u12_fix.sql'
open(path, 'w').write('\n'.join(out) + '\n')
print('SQL:', path, len('\n'.join(out)), 'байт; правок payload:', len(E))
