#!/usr/bin/env python3
"""Сборка уроков Super Minds 1: блоки → SQL, с проверкой до заливки.

Копия tools/sm3_build.py, но уроки лежат не здесь, а по юнитам в
tools/sm1/uN.py — в каждом словарь LESSONS. Так юниты можно собирать
параллельно, не толкаясь в одном файле. Общие помощники (img, shared,
quiz_ru_to_en) — здесь, юнит берёт их через `from sm1_build import *`.

Ключи уроков: u5_hw4 … u9_hw7, u1_test … u9_test, final_test.

  python3 tools/sm1_build.py --list                     все уроки и число блоков
  python3 tools/sm1_build.py --lesson u6_hw1            проверить и показать SQL
  python3 tools/sm1_build.py --lesson u6_hw1 --chunks <lesson_id> --per-chunk 7
  python3 tools/sm1_build.py --check-all                проверить всё
"""
import argparse, glob, importlib.util, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = "@@MEDIA@@"
MEDIA_URL = "https://classroom.wowteach.ru/media/"


def img(unit, name):
    return f"{MEDIA}sm1/{unit}/{name}.webp"


def shared(name):
    return f"{MEDIA}shared/{name}.webp"


def quiz_ru_to_en(words, per_question=4):
    """Вопросы «как по-английски». words — список (en, ru, файл).

    Отвлекающие берём по кругу от самого слова, а не первые из списка: иначе
    во всех вопросах стоят одни и те же три варианта.
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


def load_lessons():
    """Собирает LESSONS из tools/sm1/*.py. Повтор ключа — ошибка."""
    sys.modules.setdefault("sm1_build", sys.modules[__name__])
    out = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "tools", "sm1", "*.py"))):
        name = os.path.splitext(os.path.basename(path))[0]
        if name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f"sm1_{name}", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for k, v in getattr(mod, "LESSONS", {}).items():
            if k in out:
                sys.exit(f"урок {k} описан дважды ({path})")
            out[k] = v
    return out


# ---------- проверка ----------

def check(lesson, errors):
    for i, (btype, payload) in enumerate(lesson["blocks"], start=1):
        where = f"блок {i} ({btype})"

        if btype == "quiz":
            for n, q in enumerate(payload["questions"], start=1):
                # вариант бывает картинкой, а не текстом — сравниваем по тому,
                # что в нём есть, иначе проверка на дубли падает на картинках
                texts = [o.get("text", o.get("image", "")) for o in q["options"]]
                if len(set(texts)) != len(texts):
                    errors.append(f"{where}, вопрос {n}: повторяются варианты")
                for c in q["correct"]:
                    if not 0 <= c < len(texts):
                        errors.append(f"{where}, вопрос {n}: correct вне списка вариантов")

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
        for link in re.findall(r"@@MEDIA@@([^\"'\s)<\\]+)", json.dumps(payload, ensure_ascii=False)):
            path = os.path.join(ROOT, "media", link)
            if not os.path.exists(path):
                errors.append(f"блок {i} ({btype}): нет файла media/{link}")


# ---------- SQL ----------

def sql_for(key, lesson):
    out = [
        "-- Super Minds 1 · " + lesson["unit_title"] + " · " + lesson["lesson_title"],
        "-- собрано tools/sm1_build.py --lesson " + key,
        "do $mig$",
        "declare",
        "  v_course uuid;",
        "  v_unit   uuid;",
        "  v_lesson uuid;",
        "  v_media  text := 'https://classroom.wowteach.ru/media/';",
        "begin",
        "  select id into v_course from classroom_courses where slug = 'sm1';",
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
    ap.add_argument("--lesson")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--check-all", action="store_true")
    ap.add_argument("--sql", help="записать SQL в файл")
    ap.add_argument("--chunks", metavar="LESSON_ID",
                    help="печатать вставки блоков кусками, готовыми для "
                         "execute_sql (длинный do-блок отваливается по таймауту)")
    ap.add_argument("--per-chunk", type=int, default=3)
    args = ap.parse_args()

    LESSONS = load_lessons()
    if args.list or args.check_all:
        bad = 0
        for k, l in LESSONS.items():
            errors = []
            check(l, errors)
            bad += bool(errors)
            print(f"{k:12} {l['unit_title']:28} {l['lesson_title']:14} "
                  f"{len(l['blocks']):3} бл.  {'ОШИБКИ: ' + '; '.join(errors) if errors else 'ok'}")
        sys.exit(1 if bad and args.check_all else 0)

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
    if args.chunks:
        rows = []
        for n, (btype, payload) in enumerate(lesson["blocks"]):
            clean = {k: v for k, v in payload.items() if k != "gaps_expected"}
            js = json.dumps(clean, ensure_ascii=False)
            rows.append(f"('{args.chunks}', '{btype}', replace($blk${js}$blk$, "
                        f"'@@MEDIA@@', '{MEDIA_URL}')::jsonb, {n})")
        for i in range(0, len(rows), args.per_chunk):
            print("-- кусок", i // args.per_chunk + 1)
            print("insert into classroom_blocks (lesson_id, type, payload, sort_order) values")
            print(",\n".join(rows[i:i + args.per_chunk]))
            print("returning sort_order, type;\n")
        return

    sql = sql_for(args.lesson, lesson)
    if args.sql:
        with open(args.sql, "w", encoding="utf-8") as f:
            f.write(sql + "\n")
        print("SQL записан в", args.sql, file=sys.stderr)
    else:
        print(sql)


if __name__ == "__main__":
    main()
