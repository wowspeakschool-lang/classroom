# -*- coding: utf-8 -*-
"""Новые блоки для домашек GG2 юнитов 1-2 + проверка payload до заливки."""
import json, os, sys, re

MEDIA_ROOT = '/home/user/classroom/media'
MEDIA = '@@MEDIA@@'

L = {
  ('u1','hw2'): '829ba270-7377-43f0-b5ad-093441ba6b07',
  ('u1','hw4'): '851d9b90-f06b-46e5-8fd5-96cec97d6d69',
  ('u1','hw5'): '3894f232-5143-4498-aa0c-c575e0760cc1',
  ('u1','hw6'): '17a7a056-ec35-467b-8b6d-031c50fe937a',
  ('u2','hw3'): 'd8fbeb71-a2ef-4bfd-a0d9-eb73dae5d5e0',
  ('u2','hw4'): 'edb04172-9975-4411-bda8-74f5592a7a13',
  ('u2','hw5'): 'ccb8ec26-8db1-4014-ba1e-500fc48b8624',
  ('u2','hw6'): '52eaf7a4-b1a7-4a23-9f36-0b9e599a940f',
  ('u2','hw7'): '4d349ca7-4b58-48e8-824a-fcde5e710f54',
}

AUD_U2HW6 = 'https://vtcxghsqymwkyiogpndf.supabase.co/storage/v1/object/public/classroom-media/gg2%20%2B%20gg3/gg2_u2_hw6_b2.mp3'

B = []  # (lesson_key, sort_order, type, payload)
def add(key, so, typ, payload): B.append((key, so, typ, payload))

# ─────────── U1 HW2: Present Simple + наречия частотности (плана Lesson 2) ───────────
add(('u1','hw2'), 4, 'quiz', {
 "title": "Как часто это бывает? Прочитай предложение и выбери подходящее наречие",
 "questions": [
  {"q": "Sam goes to school from Monday to Friday. He ___ goes to school on Sunday.", "type": "single",
   "correct": [0], "options": [{"text": "never"}, {"text": "always"}, {"text": "usually"}]},
  {"q": "I have breakfast every morning. I ___ have breakfast.", "type": "single",
   "correct": [1], "options": [{"text": "never"}, {"text": "always"}, {"text": "sometimes"}]},
  {"q": "Kate plays tennis on most days. She ___ plays tennis.", "type": "single",
   "correct": [1], "options": [{"text": "never"}, {"text": "usually"}, {"text": "sometimes"}]},
  {"q": "Tom eats pizza two or three times a year. He ___ eats pizza.", "type": "single",
   "correct": [2], "options": [{"text": "often"}, {"text": "always"}, {"text": "sometimes"}]},
  {"q": "We have P.E. on Monday, Tuesday and Thursday. We ___ have P.E.", "type": "single",
   "correct": [1], "options": [{"text": "never"}, {"text": "often"}, {"text": "always"}]},
 ]})

add(('u1','hw2'), 5, 'sort', {
 "title": "Распредели формы глагола: какие подходят к I / we / they, а какие — к he / she / it",
 "groups": [
  {"name": "I / we / they", "items": [{"text": "play"}, {"text": "go"}, {"text": "like"}, {"text": "watch"}, {"text": "tidy"}]},
  {"name": "he / she / it", "items": [{"text": "plays"}, {"text": "goes"}, {"text": "likes"}, {"text": "watches"}, {"text": "tidies"}]},
 ]})

add(('u1','hw2'), 8, 'gaps', {
 "mode": "choice",
 "title": "Выбери наречие, которое подходит по смыслу",
 "text": ("1. Lessons start at 8.30. We __always__ start at 8.30.\n"
          "2. I like vegetables but I __never__ eat fish.\n"
          "3. My dad works at home, so he is __usually__ at home in the afternoon.\n"
          "4. We go to the cinema two or three times a year. We __sometimes__ go to the cinema.\n"
          "5. Anna does karate on Monday, Wednesday and Friday. She __often__ does karate."),
 "choices": [["never", "sometimes"], ["always", "often"], ["never", "sometimes"], ["always", "often"], ["never", "always"]],
})

add(('u1','hw2'), 9, 'task', {
 "title": "Расскажи о своём дне ✍️",
 "html": ("<p>Напиши три предложения о своём дне. Используй <b>always</b>, <b>usually</b>, "
          "<b>often</b>, <b>sometimes</b> или <b>never</b>.</p>"
          "<p><i>Например: I always get up at 7 o'clock. I sometimes play football after school.</i></p>"),
 "needs_review": True})

# ─────────── U1 HW4: do / play (плана Lesson 4) ───────────
add(('u1','hw4'), 7, 'text', {
 "html": ("<h3>do или play? 🏀</h3><p>С одними занятиями мы говорим <b>do</b>, с другими — <b>play</b>. "
          "Давай потренируемся.</p>")})

add(('u1','hw4'), 8, 'sort', {
 "title": "Распредели занятия: с какими говорим do, а с какими — play",
 "groups": [
  {"name": "do", "items": [{"text": "ballet"}, {"text": "karate"}, {"text": "pottery"}]},
  {"name": "play", "items": [{"text": "basketball"}, {"text": "chess"}, {"text": "football"}, {"text": "tennis"}]},
 ]})

add(('u1','hw4'), 9, 'gaps', {
 "mode": "choice",
 "title": "Выбери do или play в правильной форме",
 "text": ("1. I __play__ chess with my grandfather.\n"
          "2. My sister __does__ ballet on Mondays.\n"
          "3. We __play__ basketball at school.\n"
          "4. Max __does__ karate after school.\n"
          "5. Do you __play__ football in your free time?\n"
          "6. They __do__ pottery in Art."),
 "choices": [["do", "does"], ["do", "play"], ["do", "does"], ["do", "plays"], ["do", "does"], ["does", "play"]],
})

# ─────────── U1 HW5: места в школе (плана Lesson 5) ───────────
add(('u1','hw5'), 4, 'gaps', {
 "mode": "drag",
 "title": "Перетащи названия школьных мест в пропуски",
 "text": ("1. We have lunch in the __canteen__.\n"
          "2. We play football on the __playground__.\n"
          "3. We do P.E. in the __gym__.\n"
          "4. We read books in the __library__.\n"
          "5. We use laptops in the __computer room__.\n"
          "6. The teachers have coffee in the __staff room__."),
})

# ─────────── U1 HW6: дни недели + at / in / on (плана Lesson 6) ───────────
add(('u1','hw6'), 6, 'sequence', {
 "title": "Расставь дни недели по порядку — от Monday до Sunday",
 "items": [{"text": "Monday"}, {"text": "Tuesday"}, {"text": "Wednesday"}, {"text": "Thursday"},
           {"text": "Friday"}, {"text": "Saturday"}, {"text": "Sunday"}]})

add(('u1','hw6'), 8, 'gaps', {
 "mode": "choice",
 "title": "Выбери at, in или on",
 "text": ("1. I get up __at__ 7.30.\n"
          "2. We have Music __on__ Tuesday.\n"
          "3. __In__ the morning I have breakfast.\n"
          "4. Lessons finish __at__ 3 o'clock.\n"
          "5. I do ballet __in__ the evening.\n"
          "6. We play basketball __on__ Friday."),
 "choices": [["in", "on"], ["at", "in"], ["At", "On"], ["in", "on"], ["at", "on"], ["at", "in"]],
})

# ─────────── U2 HW3: how much / how many (плана Lesson 3) ───────────
add(('u2','hw3'), 5, 'text', {
 "html": ("<h3>How much или How many? 🤔</h3>"
          "<p>Если предмет можно посчитать, спрашиваем <b>How many</b>: <i>How many apples are there?</i></p>"
          "<p>Если посчитать нельзя, спрашиваем <b>How much</b>: <i>How much milk is there?</i></p>")})

add(('u2','hw3'), 6, 'sort', {
 "title": "Распредели слова: с какими спросим How many, а с какими — How much",
 "groups": [
  {"name": "How many", "items": [{"text": "apples"}, {"text": "eggs"}, {"text": "bananas"}, {"text": "biscuits"}, {"text": "sandwiches"}]},
  {"name": "How much", "items": [{"text": "milk"}, {"text": "sugar"}, {"text": "water"}, {"text": "bread"}, {"text": "cheese"}]},
 ]})

add(('u2','hw3'), 7, 'gaps', {
 "mode": "type",
 "title": "Впиши в пропуски How much или How many",
 "text": ("1. __How many|how many__ eggs are there in the fridge?\n"
          "2. __How much|how much__ bread do we need?\n"
          "3. __How many|how many__ apples would you like?\n"
          "4. __How much|how much__ cheese is there on the pizza?\n"
          "5. __How many|how many__ biscuits are there in the packet?"),
})

add(('u2','hw3'), 8, 'task', {
 "title": "Спроси сам ✍️",
 "image": MEDIA + "gg2/u2/scene_breakfast.webp",
 "html": ("<p>Посмотри на картинку и напиши четыре вопроса: два с <b>How many</b> и два с <b>How much</b>.</p>"
          "<p><i>Например: How many eggs are there? How much milk is there?</i></p>"),
 "needs_review": True})

# ─────────── U2 HW4: заказ в кафе + ёмкости (плана Lesson 4) ───────────
add(('u2','hw4'), 3, 'quiz', {
 "title": "Ты в кафе. Выбери подходящую реплику",
 "questions": [
  {"q": "Waitress: What would you like? — Guest: ___", "type": "single", "correct": [0],
   "options": [{"text": "I'd like a ham sandwich, please."}, {"text": "Great, thanks."}, {"text": "Anything else?"}]},
  {"q": "Waitress: Would you like anything to drink? — Guest: ___", "type": "single", "correct": [1],
   "options": [{"text": "Yes, I'm hungry."}, {"text": "Can I have a lemonade, please?"}, {"text": "No, thanks. I'd like a salad."}]},
  {"q": "Guest: Can I have some chips, please? — Waitress: ___", "type": "single", "correct": [0],
   "options": [{"text": "Yes, of course. Anything else?"}, {"text": "I'd like a hot dog."}, {"text": "How much is it?"}]},
  {"q": "Waitress: Anything else? — Guest: ___", "type": "single", "correct": [1],
   "options": [{"text": "What would you like?"}, {"text": "No, thanks. That's all."}, {"text": "Great, thanks."}]},
 ]})

add(('u2','hw4'), 5, 'gaps', {
 "mode": "drag",
 "title": "Перетащи в пропуски названия ёмкостей",
 "text": ("Waiter: What would you like?\n"
          "Kate: Can I have a __bottle__ of water, please?\n"
          "Waiter: Anything else?\n"
          "Kate: Yes. A __packet__ of biscuits and a __bar__ of chocolate, please.\n"
          "Waiter: Would you like anything to drink?\n"
          "Kate: A __can__ of cola and a __carton__ of juice, please.\n"
          "Waiter: Great, thanks."),
})

# ─────────── U2 HW5: рецепт блинчиков + some / any (плана Lesson 5) ───────────
add(('u2','hw5'), 5, 'sequence', {
 "title": "Это рецепт блинчиков. Расставь шаги по порядку",
 "items": [{"text": "Put some flour in a bowl."},
           {"text": "Add two eggs and some milk."},
           {"text": "Mix the flour, the eggs and the milk."},
           {"text": "Cook the pancakes in some butter."},
           {"text": "Put some strawberries and sugar on the pancakes."},
           {"text": "Eat the pancakes!"}]})

add(('u2','hw5'), 6, 'gaps', {
 "mode": "type",
 "title": "Впиши some или any",
 "text": ("1. There's __some|Some__ fish in the fridge at Susie's house.\n"
          "2. There isn't __any|Any__ chicken at Susie's house.\n"
          "3. Is there __any|Any__ rice at her aunt's house?\n"
          "4. Susie has __some|Some__ sausages for an English breakfast.\n"
          "5. We haven't got __any|Any__ tomatoes."),
})

# ─────────── U2 HW6: so / because (плана Lesson 6) ───────────
add(('u2','hw6'), 7, 'order', {
 "title": "Собери предложение с because",
 "words": ["I", "like", "pancakes", "because", "they", "are", "sweet."],
 "sentence": "I like pancakes because they are sweet."})

add(('u2','hw6'), 8, 'order', {
 "title": "Собери предложение с so",
 "words": ["I'm", "hungry", "so", "I", "want", "a", "sandwich."],
 "sentence": "I'm hungry so I want a sandwich."})

# ─────────── U2 HW7: разделитель перед серией из четырёх gaps ───────────
add(('u2','hw7'), 3, 'text', {
 "html": ("<h3>Теперь заполним пропуски 📝</h3>"
          "<p>Дальше тебя ждут четыре задания с пропусками. Читай внимательно и вписывай подходящие слова.</p>")})

# ═══════════════════════ проверка ═══════════════════════
err = []
def gapcount(t): return len(re.findall(r'__[^_]+__', t))

for key, so, typ, p in B:
    tag = f"{key[0]} {key[1]} #{so} {typ}"
    if typ == 'quiz':
        if not p.get('title'): err.append(tag + ': нет title')
        for qi, q in enumerate(p['questions']):
            opts = [o.get('text', o.get('image')) for o in q['options']]
            if len(set(opts)) != len(opts): err.append(f"{tag} q{qi+1}: дубли вариантов")
            for c in q['correct']:
                if not (0 <= c < len(opts)): err.append(f"{tag} q{qi+1}: correct вне диапазона")
            if not q.get('q'): err.append(f"{tag} q{qi+1}: пустой q")
            if re.search(r'[А-Яа-я]', q['q']): err.append(f"{tag} q{qi+1}: русский текст в q")
    elif typ == 'sort':
        if not p.get('title'): err.append(tag + ': нет title')
        names = [g['name'] for g in p['groups']]
        if len(set(names)) != len(names): err.append(tag + ': дубли групп')
        items = [i.get('text') for g in p['groups'] for i in g['items']]
        if len(set(items)) != len(items): err.append(tag + ': дубли элементов')
        if not items: err.append(tag + ': нет элементов')
    elif typ == 'gaps':
        if not p.get('title'): err.append(tag + ': нет title')
        n = gapcount(p['text'])
        if n == 0: err.append(tag + ': нет пропусков')
        if p['mode'] == 'drag' and n < 2: err.append(tag + ': drag при одном пропуске')
        if p['mode'] == 'choice':
            ch = p.get('choices') or []
            if len(ch) != n: err.append(f"{tag}: choices {len(ch)} != пропусков {n}")
            for gi, x in enumerate(re.findall(r'__([^_]+)__', p['text'])):
                right = x.split('|')[0].strip()
                if right in (ch[gi] if gi < len(ch) else []):
                    err.append(f"{tag} пропуск {gi+1}: верный ответ дублируется в choices")
                if not (ch[gi] if gi < len(ch) else []):
                    err.append(f"{tag} пропуск {gi+1}: нет дистракторов")
        if p['mode'] == 'drag':
            chips = [x.split('|')[0].strip() for x in re.findall(r'__([^_]+)__', p['text'])]
            if len(set(chips)) < 2: err.append(tag + ': все фишки одинаковые')
    elif typ == 'sequence':
        if not p.get('title'): err.append(tag + ': нет title')
        its = [i['text'] for i in p['items']]
        if len(set(its)) != len(its): err.append(tag + ': дубли строк')
    elif typ == 'order':
        if ' '.join(p['words']) != p['sentence']:
            err.append(tag + ': words не склеиваются в sentence')
        if 'audio' in p or 'audio_tts' in p: err.append(tag + ': звук в order вне SM0')
    elif typ == 'task':
        if not p.get('html'): err.append(tag + ': нет html')
        if not p.get('needs_review'): err.append(tag + ': нет needs_review')
    elif typ == 'text':
        if not p.get('html'): err.append(tag + ': нет html')
    # картинки
    for m in re.findall(r'@@MEDIA@@([A-Za-z0-9_./-]+)', json.dumps(p, ensure_ascii=False)):
        if not os.path.isfile(os.path.join(MEDIA_ROOT, m)): err.append(f"{tag}: нет файла media/{m}")
    if 'base64' in json.dumps(p): err.append(tag + ': base64 в payload')

if err:
    print("ОШИБКИ:")
    for e in err: print(' -', e)
    sys.exit(1)
print(f"проверка пройдена: {len(B)} новых блоков, ошибок нет")

# ═══════════════════════ SQL ═══════════════════════
out = ["-- GG2 юниты 1-2: новые блоки домашек (вычитка 03.11.2026)",
       "do $$", "declare v_media text := 'https://classroom.wowteach.ru/media/';", "begin"]
for key, so, typ, p in B:
    js = json.dumps(p, ensure_ascii=False).replace('$blk$', '')
    out.append(f"""  insert into classroom_blocks (lesson_id, type, payload, sort_order)
  values ('{L[key]}', '{typ}', replace($blk${js}$blk$, '@@MEDIA@@', v_media)::jsonb, {so})
  on conflict (lesson_id, sort_order) do update set payload = excluded.payload, type = excluded.type;""")
out += ["end $$;"]
path = '/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/gg2_u12_new.sql'
open(path, 'w').write('\n'.join(out) + '\n')
print('SQL:', path, len('\n'.join(out)), 'байт')
