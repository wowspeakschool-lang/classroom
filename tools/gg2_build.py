#!/usr/bin/env python3
"""Сборка уроков Go Getter 2 (и тестов Go Getter 3): блоки → SQL, с проверкой до заливки.

Каркас — tools/sm3_build.py (проверки те же); свои здесь только курс, модули
уроков и выдача SQL для заливки через execute_sql. Уроки лежат в модулях по
юнитам: tools/gg2_u0.py … tools/gg2_u8.py, tools/gg2_final.py — в каждом
словарь LESSONS. GG3 собирается этим же кодом: tools/gg3_build.py.

Блок урока — кортеж (тип, payload) или (тип, payload, {"todo": [...]}).
todo — строки для файла «доработать руками»: (вид, текст), где вид —
video · audio · game · check · other. Номер блока в файле считается сам
(как в редакторе, с 1), поэтому вставка блока не сдвигает подписи.

  python3 tools/gg2_build.py --list                     все уроки и проверка
  python3 tools/gg2_build.py --lesson u1_hw1            проверить, показать SQL-миграцию
  python3 tools/gg2_build.py --lesson u1_hw1 --sql      записать migrations/gg2_u1_hw1.sql
  python3 tools/gg2_build.py --lesson u1_hw1 --setup    SQL: завести юнит и урок, вернуть id урока
  python3 tools/gg2_build.py --lesson u1_hw1 --clear ID SQL: стереть блоки урока (DELETE в CTE)
  python3 tools/gg2_build.py --lesson u1_hw1 --chunks ID  вставки блоков кусками по 3
  python3 tools/gg2_build.py --lesson u1_hw1 --verify ID  контрольный select после заливки
  python3 tools/gg2_build.py --todo                     строки «доработать руками» по всем урокам
"""
import argparse, importlib, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = "@@MEDIA@@"
MEDIA_URL = "https://classroom.wowteach.ru/media/"

COURSE = {"slug": "gg2", "title": "Go Getter 2",
          "modules": ["gg2_u0", "gg2_u1", "gg2_u2", "gg2_u3", "gg2_u4",
                      "gg2_u5", "gg2_u6", "gg2_u7", "gg2_u8", "gg2_final"]}

BLOCK_TYPES = {"text", "video", "quiz", "exact_input", "match", "task", "embed", "order",
               "sort", "flashcards", "gaps", "truefalse", "speaking", "sequence", "hotspot"}


# ---------- помощники для модулей уроков ----------

def img(unit, name, course="gg2"):
    """Картинка юнита: media/<курс>/<юнит>/<имя>.webp."""
    return f"{MEDIA}{course}/{unit}/{name}.webp"


def shared(name):
    return f"{MEDIA}shared/{name}.webp"


def todo(block, *items):
    """Пометить блок строками для «доработать руками»: todo(("video", {...}), ("video", "что за видео"))."""
    btype, payload = block[0], block[1]
    return (btype, payload, {"todo": list(items)})


def video(title, todo_text):
    """Пустой видеоблок — файла в выгрузке нет, ссылку пришлёт методист."""
    return todo(("video", {"title": title, "url": "", "provider": "file"}), ("video", todo_text))


# ---------- загрузка уроков ----------

def load(course=COURSE):
    lessons = {}
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    for mod in course["modules"]:
        try:
            m = importlib.import_module(mod)
        except ModuleNotFoundError as e:
            if e.name == mod:
                continue
            raise
        for k, v in m.LESSONS.items():
            if k in lessons:
                raise SystemExit(f"урок {k} описан дважды")
            lessons[k] = v
    return lessons


def blocks_of(lesson):
    """[(тип, payload, todo-список)] без служебного третьего элемента."""
    out = []
    for b in lesson["blocks"]:
        meta = b[2] if len(b) > 2 else {}
        out.append((b[0], b[1], meta.get("todo", [])))
    return out


# ---------- проверка ----------

def check(lesson, errors):
    kind = lesson.get("kind")
    if kind not in ("homework", "test"):
        errors.append(f"kind = {kind!r}, ждём homework или test")
    for i, (btype, payload, _) in enumerate(blocks_of(lesson), start=1):
        where = f"блок {i} ({btype})"
        if btype not in BLOCK_TYPES:
            errors.append(f"{where}: неизвестный тип блока")
            continue

        if btype == "quiz":
            for n, q in enumerate(payload["questions"], start=1):
                texts = [o.get("text", o.get("image", "")) if isinstance(o, dict) else o for o in q["options"]]
                if len(set(texts)) != len(texts):
                    errors.append(f"{where}, вопрос {n}: повторяются варианты")
                if not q.get("correct"):
                    errors.append(f"{where}, вопрос {n}: не указан correct")
                for c in q.get("correct", []):
                    if not 0 <= c < len(texts):
                        errors.append(f"{where}, вопрос {n}: correct вне списка вариантов")
                if q.get("type") not in ("single", "multiple"):
                    errors.append(f"{where}, вопрос {n}: type должен быть single или multiple")

        if btype == "match":
            rights = [p.get("right", p.get("right_image")) for p in payload["pairs"]]
            if len(set(rights)) != len(rights):
                errors.append(f"{where}: правые значения повторяются — такой блок надо делать quiz")

        if btype == "order":
            glued = " ".join(payload["words"])
            if glued != payload["sentence"]:
                errors.append(f"{where}: склейка слов «{glued}» не совпадает с предложением «{payload['sentence']}»")

        if btype == "gaps":
            found = len(re.findall(r"__[^_]+__", payload["text"]))
            want = payload.get("gaps_expected")
            if want is not None and found != want:
                errors.append(f"{where}: пропусков {found}, а задумано {want}")
            if found == 0:
                errors.append(f"{where}: нет ни одного пропуска __слово__")

        if btype == "exact_input":
            for it in payload["items"]:
                if not it.get("accept"):
                    errors.append(f"{where}: пустой список accept")

        if btype == "truefalse":
            for s in payload["statements"]:
                if not isinstance(s.get("correct"), bool):
                    errors.append(f"{where}: у утверждения «{s.get('text','')[:40]}» correct не true/false")

        if btype == "video":
            if payload.get("url") and payload.get("provider") not in ("file", "youtube"):
                errors.append(f"{where}: provider должен быть file или youtube")

    for i, (btype, payload, _) in enumerate(blocks_of(lesson), start=1):
        dump = json.dumps(payload, ensure_ascii=False)
        for link in re.findall(r"@@MEDIA@@([^\"'\s)<\\]+)", dump):
            if not os.path.exists(os.path.join(ROOT, "media", link)):
                errors.append(f"блок {i} ({btype}): нет файла media/{link}")
        if "base64," in dump:
            errors.append(f"блок {i} ({btype}): base64 в payload — только ссылки")


# ---------- SQL ----------

def q(s):
    return s.replace("'", "''")


def payload_json(payload):
    clean = {k: v for k, v in payload.items() if k != "gaps_expected"}
    return json.dumps(clean, ensure_ascii=False)


def setup_sql(lesson, course=COURSE):
    ut, lt = q(lesson["unit_title"]), q(lesson["lesson_title"])
    kind = lesson["kind"]
    thr = 90 if kind == "test" else 60
    return f"""insert into classroom_units (course_id, title, sort_order)
select c.id, '{ut}', {lesson['unit_sort']} from classroom_courses c
where c.slug = '{course['slug']}'
  and not exists (select 1 from classroom_units u where u.course_id = c.id and u.title = '{ut}');
insert into classroom_lessons (unit_id, title, kind, pass_threshold, is_published, sort_order)
select u.id, '{lt}', '{kind}', {thr}, false, {lesson['lesson_sort']}
from classroom_units u join classroom_courses c on c.id = u.course_id
where c.slug = '{course['slug']}' and u.title = '{ut}'
  and not exists (select 1 from classroom_lessons l where l.unit_id = u.id and l.title = '{lt}');
update classroom_lessons l set kind = '{kind}', pass_threshold = {thr}, sort_order = {lesson['lesson_sort']}
from classroom_units u join classroom_courses c on c.id = u.course_id
where l.unit_id = u.id and c.slug = '{course['slug']}' and u.title = '{ut}' and l.title = '{lt}';
select l.id, l.kind, l.pass_threshold, l.is_published from classroom_lessons l
join classroom_units u on u.id = l.unit_id join classroom_courses c on c.id = u.course_id
where c.slug = '{course['slug']}' and u.title = '{ut}' and l.title = '{lt}';"""


def clear_sql(lesson_id):
    return (f"with d as (delete from classroom_blocks where lesson_id = '{lesson_id}' returning sort_order)\n"
            f"select count(*) as deleted from d;")


def chunks_sql(lesson, lesson_id, per_chunk=3):
    rows = []
    for n, (btype, payload, _) in enumerate(blocks_of(lesson)):
        rows.append(f"('{lesson_id}', '{btype}', replace($blk${payload_json(payload)}$blk$, "
                    f"'@@MEDIA@@', '{MEDIA_URL}')::jsonb, {n})")
    out = []
    for i in range(0, len(rows), per_chunk):
        out.append(f"-- кусок {i // per_chunk + 1}\n"
                   "insert into classroom_blocks (lesson_id, type, payload, sort_order) values\n"
                   + ",\n".join(rows[i:i + per_chunk]) + "\nreturning sort_order, type;")
    return out


def verify_sql(lesson_id):
    return (f"select count(*) as blocks, string_agg(type, ',' order by sort_order) as types,\n"
            f"       count(*) filter (where payload::text like '%@@MEDIA@@%') as unreplaced_media,\n"
            f"       max(sort_order) as last_sort\n"
            f"from classroom_blocks where lesson_id = '{lesson_id}';")


def migration_sql(key, lesson, course=COURSE):
    out = [f"-- {course['title']} · {lesson['unit_title']} · {lesson['lesson_title']}",
           f"-- собрано tools/{course['slug']}_build.py --lesson {key}",
           "-- заливалось через execute_sql кусками (--setup, --clear, --chunks); этот файл — исходник",
           setup_sql(lesson, course), "",
           "-- затем: delete блоков урока (CTE) и вставка:"]
    out += chunks_sql(lesson, "<lesson_id>", per_chunk=1000)
    return "\n".join(out) + "\n"


def todo_md(lessons, course=COURSE):
    lines = []
    for key, lesson in lessons.items():
        for i, (btype, payload, items) in enumerate(blocks_of(lesson), start=1):
            for kind, text in items:
                lines.append((lesson["unit_sort"], lesson["lesson_sort"], key, lesson["unit_title"],
                              lesson["lesson_title"], i, kind, text))
    lines.sort()
    out = ["| юнит | урок | блок | что | имя файла |", "|---|---|---|---|---|"]
    for us, ls, key, ut, lt, i, kind, text in lines:
        unit = key.split("_")[0]
        les = key.split("_", 1)[1] if "_" in key else key
        fname = f"{course['slug']}_{unit}_{les}_b{i}" if unit != "final" else f"{course['slug']}_final_b{i}"
        lines_kind = {"video": "🎬 видео", "audio": "🔊 аудио", "game": "🎲 игра", "check": "👀 проверить",
                      "other": "📝"}.get(kind, kind)
        out.append(f"| {ut} | {lt} | {i} | {lines_kind}: {text} | `{fname}` |")
    return "\n".join(out)


def main(course=COURSE):
    ap = argparse.ArgumentParser()
    ap.add_argument("--lesson")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--sql", action="store_true", help=f"записать migrations/{course['slug']}_<урок>.sql")
    ap.add_argument("--setup", action="store_true")
    ap.add_argument("--clear", metavar="LESSON_ID")
    ap.add_argument("--chunks", metavar="LESSON_ID")
    ap.add_argument("--per-chunk", type=int, default=3)
    ap.add_argument("--verify", metavar="LESSON_ID")
    ap.add_argument("--todo", action="store_true")
    args = ap.parse_args()

    lessons = load(course)
    if args.todo:
        print(todo_md(lessons, course))
        return
    if args.list:
        bad = 0
        for key, lesson in sorted(lessons.items(), key=lambda kv: (kv[1]["unit_sort"], kv[1]["lesson_sort"])):
            errors = []
            check(lesson, errors)
            bad += bool(errors)
            print(f"{key:12} {lesson['unit_title']:28} {lesson['lesson_title']:14} {lesson['kind']:8} "
                  f"{len(lesson['blocks']):3} бл.  {'OK' if not errors else 'ОШИБКИ: ' + str(len(errors))}")
            for e in errors:
                print("     ·", e)
        sys.exit(1 if bad else 0)

    lesson = lessons[args.lesson]
    errors = []
    check(lesson, errors)
    if errors:
        print("Проверка не прошла:", file=sys.stderr)
        for e in errors:
            print("  ·", e, file=sys.stderr)
        sys.exit(1)
    print(f"Проверка пройдена: {len(lesson['blocks'])} блоков", file=sys.stderr)

    if args.setup:
        print(setup_sql(lesson, course))
    elif args.clear:
        print(clear_sql(args.clear))
    elif args.chunks:
        print("\n\n".join(chunks_sql(lesson, args.chunks, args.per_chunk)))
    elif args.verify:
        print(verify_sql(args.verify))
    elif args.sql:
        path = os.path.join(ROOT, "migrations", f"{course['slug']}_{args.lesson}.sql")
        with open(path, "w", encoding="utf-8") as f:
            f.write(migration_sql(args.lesson, lesson, course))
        print("записан", os.path.relpath(path, ROOT), file=sys.stderr)
    else:
        print(migration_sql(args.lesson, lesson, course))


if __name__ == "__main__":
    main()
