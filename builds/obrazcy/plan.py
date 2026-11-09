# -*- coding: utf-8 -*-
"""Образец ответа не должен выдавать ответ (решение Анны 09.11.2026, «46 б»).

Правило: предложения образца группируются по КОНСТРУКЦИИ (грамматическому
скелету: «it's a X», «i have got X», «there is X in the X»). Все предложения
одной конструкции сводятся к первому; разные конструкции остаются — по одному
предложению каждой, в исходном порядке. Голое перечисление без глагола
(«Teddy bear, lego, robot») режется по запятым и оставляет один пункт.
"""
import json, re, io

SUBJ = {"i","you","he","she","it","we","they","this","that","these","those","there",
        "what","where","who","when","why","how","which","let's","let"}
BE = {"is","are","am","was","were","'s","'re","'m","isn't","aren't","wasn't","weren't"}
MODAL = {"can","can't","cannot","could","will","won't","would","wouldn't","shall","must","should","may"}
DOAUX = {"do","does","did","don't","doesn't","didn't"}
NEG = {"not","n't","don't","doesn't","didn't","can't","isn't","aren't","won't","wouldn't",
       "haven't","hasn't","no","cannot","wasn't","weren't"}
CONTR_BE = {"it's","he's","she's","that's","what's","there's","i'm","you're","we're","they're","who's"}
CONTR_HAVE = {"i've","you've","we've","they've"}

def sig(sentence):
    """Грамматический скелет: кто — какой глагол — отрицание — вопрос."""
    s = sentence.strip().lower()
    vopros = s.rstrip().endswith("?")
    w = re.findall(r"[a-z']+", s)
    if not w:
        return "пусто"
    subj, verb, neg = None, None, False
    for i, x in enumerate(w):
        if x in NEG:
            neg = True
        if subj is None:
            if x in SUBJ:
                subj = x
            elif x in CONTR_BE:
                subj, verb = x.split("'")[0], "be"
            elif x in CONTR_HAVE:
                subj, verb = x.split("'")[0], "have"
        if verb is None:
            if x in BE:
                verb = "be"
            elif x in MODAL:
                verb = "modal"
            elif x in DOAUX:
                verb = "do"
            elif x in ("have","has","had","haven't","hasn't"):
                verb = "have" if (i + 1 < len(w) and w[i+1] == "got") else "глагол"
    if subj is None:
        subj = "имя" if w[0] not in SUBJ else w[0]
    if verb is None:
        # есть ли вообще сказуемое: слово не из служебных после подлежащего
        verb = "глагол" if len(w) > 1 else "нет"
    return "%s|%s|%s|%s" % (subj, verb, "neg" if neg else "+", "?" if vopros else ".")

def split_sentences(text):
    parts = [p.strip() for p in re.split(r"(?<=[.!?])\s+", text.strip()) if p.strip()]
    if len(parts) == 1 and "," in parts[0]:
        body = parts[0].rstrip(".!?")
        chunks = [c.strip() for c in body.split(",") if c.strip()]
        if len(chunks) > 1 and all(len(re.findall(r"[a-zA-Z']+", c)) <= 3 for c in chunks):
            return [c + "." for c in chunks], True
    return parts, False

def shorten(text):
    sents, perechislenie = split_sentences(text)
    if perechislenie:
        # «Teddy bear, lego, robot» — решение Анны: оставляем одно слово/фразу
        return sents[0], len(sents), 1, True
    seen, keep = set(), []
    for s in sents:
        k = sig(s)
        if k in seen:
            continue
        seen.add(k); keep.append(s)
    return " ".join(keep), len(sents), len(keep), perechislenie

if __name__ == "__main__":
    rows = json.load(open("/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/obrazcy.json"))
    plan, bez_teksta = [], []
    import re as _re
    CHTENIE = _re.compile(r"прочита|прочти|повтори за|повторяй", _re.I)
    chtenie = []
    for r in rows:
        t = (r["obr"] or "").strip()
        if not t:
            bez_teksta.append(r); continue
        if CHTENIE.search((r["zag"] or "") + " " + (r["txt"] or "")):
            chtenie.append(r); continue   # «прочитай вслух» — образец это эталон чтения
        new, n_old, n_new, per = shorten(t)
        plan.append(dict(r, novyy=new, bylo_predlozheniy=n_old, stalo=n_new, perechislenie=per,
                         menyaem=(new != t)))
    json.dump(plan, io.open("builds/obrazcy/plan.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(bez_teksta, io.open("builds/obrazcy/bez_teksta.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(chtenie, io.open("builds/obrazcy/chtenie_vsluh.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
    print("«прочитай вслух» — не трогаем:", len(chtenie))
    ch = [p for p in plan if p["menyaem"]]
    from collections import Counter
    print("всего с текстом:", len(plan), "| меняем:", len(ch), "| без текста образца:", len(bez_teksta))
    print(Counter(p["slug"] for p in ch))
