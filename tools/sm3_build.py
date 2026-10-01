#!/usr/bin/env python3
"""Сборка уроков Super Minds 3: блоки → SQL, с проверкой до заливки.

Уроки описываются питоновскими структурами ниже, скрипт собирает из них
миграцию и сам проверяет payload по списку из CLAUDE.md: правильный вариант
указывает на задуманный, нет дублей в вариантах, правые значения match
уникальны, склейка order совпадает с предложением, число пропусков в gaps
совпадает с задуманным, каждая ссылка на картинку есть в media/.

  python3 tools/sm3_build.py --lesson u1_hw1          проверить и показать SQL
  python3 tools/sm3_build.py --lesson u1_hw1 --sql файл.sql
"""
import argparse, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = "@@MEDIA@@"

SUBJECTS = [
    ("English", "английский", "subj_english"),
    ("Maths", "математика", "subj_maths"),
    ("Geography", "география", "subj_geography"),
    ("I.T.", "информационные технологии", "subj_it"),
    ("Music", "музыка", "subj_music"),
    ("Science", "наука", "subj_science"),
    ("Art", "изобразительное искусство", "subj_art"),
    ("P.E.", "физкультура", "subj_pe"),
    ("History", "история", "subj_history"),
]


def img(unit, name):
    return f"{MEDIA}sm3/{unit}/{name}.webp"


def shared(name):
    return f"{MEDIA}shared/{name}.webp"


def quiz_ru_to_en(words, per_question=4):
    """Вопросы «как по-английски».

    Отвлекающие берём по кругу от самого слова, а не первые из списка: иначе
    во всех вопросах стоят одни и те же три варианта, и правильный вычисляется
    исключением, не читая вопроса.
    """
    qs = []
    n = len(words)
    for i, (en, ru, _) in enumerate(words):
        wrong = [words[(i + k) % n][0] for k in range(1, per_question)]
        options = sorted([en] + wrong, key=str.lower)
        qs.append({
            "q": f"Как по-английски «{ru}»?",
            "type": "single",
            "options": [{"text": o} for o in options],
            "correct": [options.index(en)],
        })
    return {"questions": qs}


LESSONS = {
    "u1_hw1": {
        "unit": "u1",
        "unit_title": "Unit 1 · School",
        "unit_sort": 1,
        "lesson_title": "Homework 1",
        "lesson_sort": 0,
        "kind": "homework",
        "blocks": [
            ("text", {"html":
                f'<p><img src="{shared("hello_wave")}" alt="" style="height:200px"></p>'
                "<h2>Привет! 👋</h2>"
                "<p>Сегодня мы повторим названия школьных предметов и дни недели.</p>"
                "<p>Сначала выучим слова, потом разберёмся с расписанием. Поехали!</p>"}),

            ("flashcards", {"cards": [
                {"text": en, "translation": ru, "audio_tts": en, "image": img("u1", f)}
                for en, ru, f in SUBJECTS
            ]}),

            ("match", {"pairs": [
                {"left_image": img("u1", f), "right": en, "right_audio_tts": en}
                for en, ru, f in SUBJECTS
            ]}),

            ("quiz", quiz_ru_to_en(SUBJECTS)),

            ("exact_input", {"items": [
                {"prompt": f"Напиши по-английски: {ru}", "accept": [en, en.lower()], "audio_tts": en}
                for en, ru, f in SUBJECTS
            ]}),

            ("text", {"html":
                "<h3>Расписание на неделю</h3>"
                "<p>Внимательно изучи расписание. Столбцы — это дни недели, слева направо: "
                "понедельник, вторник, среда, четверг, пятница. Поднос с обедом делит день "
                "на уроки <b>до обеда</b> и <b>после обеда</b>.</p>"
                f'<p><img src="{img("u1", "scene_timetable")}" alt="Timetable" style="max-width:100%"></p>'}),

            ("gaps", {
                "title": "Определи, какой день описан, и впиши его название",
                "mode": "type",
                "text":
                    "1. This is what I've got today. P.E., English and Music before lunch. "
                    "I.T. and History after lunch. Today is __Wednesday__.\n"
                    "2. This is what I've got today. Science, Art and English before lunch. "
                    "Maths and Geography after lunch. Today is __Friday__.\n"
                    "3. This is what I've got today. Maths, English and Geography before lunch. "
                    "Music and History after lunch. Today is __Monday__.",
                "gaps_expected": 3,
            }),

            ("order", {
                "words": ["When", "have", "you", "got", "English?", "On", "Mondays."],
                "sentence": "When have you got English? On Mondays.",
                "audio_tts": "When have you got English? On Mondays.",
            }),

            ("speaking", {
                "title": "Расскажи про свой любимый предмет 🎤",
                "html": "<p>Нажми на микрофон и расскажи, какой предмет тебе нравится и когда он у тебя.</p>"
                        "<p><i>Например: I like Art. I've got Art on Tuesdays.</i></p>",
                "needs_review": True,
            }),

            ("text", {"html":
                f'<p><img src="{shared("well_done_trophy")}" alt="" style="height:180px"></p>'
                "<h3>Отличная работа! 🎉</h3><p>До встречи на уроке!</p>"}),
        ],
    },
}


# ---------- проверка ----------

def check(lesson, errors):
    for i, (btype, payload) in enumerate(lesson["blocks"], start=1):
        where = f"блок {i} ({btype})"

        if btype == "quiz":
            for n, q in enumerate(payload["questions"], start=1):
                texts = [o["text"] for o in q["options"]]
                if len(set(texts)) != len(texts):
                    errors.append(f"{where}, вопрос {n}: повторяются варианты")
                for c in q["correct"]:
                    if not 0 <= c < len(texts):
                        errors.append(f"{where}, вопрос {n}: correct вне списка вариантов")
                # правильный вариант должен быть именно английским словом из пары
                ru = re.search(r"«(.+?)»", q["q"])
                if ru:
                    want = next((en for en, r, _ in SUBJECTS if r == ru.group(1)), None)
                    if want and texts[q["correct"][0]] != want:
                        errors.append(f"{where}, вопрос {n}: correct указывает на «{texts[q['correct'][0]]}», "
                                      f"а ждём «{want}»")

        if btype == "match":
            rights = [p["right"] for p in payload["pairs"]]
            if len(set(rights)) != len(rights):
                errors.append(f"{where}: правые значения повторяются — такой блок надо делать quiz")

        if btype == "order":
            glued = " ".join(payload["words"])
            if glued != payload["sentence"]:
                errors.append(f"{where}: склейка слов «{glued}» не совпадает с предложением "
                              f"«{payload['sentence']}»")

        if btype == "gaps":
            found = len(re.findall(r"__[^_]+__", payload["text"]))
            want = payload.get("gaps_expected")
            if want is not None and found != want:
                errors.append(f"{where}: пропусков {found}, а задумано {want}")

        if btype == "exact_input":
            for it in payload["items"]:
                if not it["accept"]:
                    errors.append(f"{where}: пустой список accept")

    # ссылки на картинки
    for i, (btype, payload) in enumerate(lesson["blocks"], start=1):
        for link in re.findall(r"@@MEDIA@@([^\"'\\s)<]+)", json.dumps(payload, ensure_ascii=False)):
            path = os.path.join(ROOT, "media", link)
            if not os.path.exists(path):
                errors.append(f"блок {i} ({btype}): нет файла media/{link}")


# ---------- SQL ----------

def sql_for(key, lesson):
    out = [
        "-- Super Minds 3 · " + lesson["unit_title"] + " · " + lesson["lesson_title"],
        "-- собрано tools/sm3_build.py --lesson " + key,
        "do $mig$",
        "declare",
        "  v_course uuid;",
        "  v_unit   uuid;",
        "  v_lesson uuid;",
        "  v_media  text := 'https://classroom.wowteach.ru/media/';",
        "begin",
        "  select id into v_course from classroom_courses where title = 'Super Minds 3';",
        "",
        "  insert into classroom_units (course_id, title, sort_order)",
        f"  select v_course, '{lesson['unit_title']}', {lesson['unit_sort']}",
        "  where not exists (select 1 from classroom_units",
        f"                    where course_id = v_course and title = '{lesson['unit_title']}');",
        f"  select id into v_unit from classroom_units",
        f"   where course_id = v_course and title = '{lesson['unit_title']}';",
        "",
        "  insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)",
        f"  select v_unit, '{lesson['lesson_title']}', '{lesson['kind']}',",
        f"         {90 if lesson['kind'] == 'test' else 60}, false, {lesson['lesson_sort']}",
        "  where not exists (select 1 from classroom_lessons",
        f"                    where unit_id = v_unit and title = '{lesson['lesson_title']}');",
        f"  select id into v_lesson from classroom_lessons",
        f"   where unit_id = v_unit and title = '{lesson['lesson_title']}';",
        "",
        "  delete from classroom_blocks where lesson_id = v_lesson;",
        "",
        "  insert into classroom_blocks (lesson_id, type, payload, sort_order) values",
    ]
    rows = []
    for n, (btype, payload) in enumerate(lesson["blocks"]):
        clean = {k: v for k, v in payload.items() if k != "gaps_expected"}
        js = json.dumps(clean, ensure_ascii=False)
        rows.append(f"    (v_lesson, '{btype}', replace($blk${js}$blk$, '@@MEDIA@@', v_media)::jsonb, {n})")
    out.append(",\n".join(rows) + ";")
    out += ["end", "$mig$;"]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lesson", required=True)
    ap.add_argument("--sql", help="записать SQL в файл")
    args = ap.parse_args()

    lesson = LESSONS[args.lesson]
    errors = []
    check(lesson, errors)
    if errors:
        print("Проверка не прошла:", file=sys.stderr)
        for e in errors:
            print("  ·", e, file=sys.stderr)
        sys.exit(1)

    print(f"Проверка пройдена: {len(lesson['blocks'])} блоков, "
          f"типы: {', '.join(t for t, _ in lesson['blocks'])}", file=sys.stderr)
    sql = sql_for(args.lesson, lesson)
    if args.sql:
        with open(args.sql, "w", encoding="utf-8") as f:
            f.write(sql + "\n")
        print("SQL записан в", args.sql, file=sys.stderr)
    else:
        print(sql)


if __name__ == "__main__":
    main()
