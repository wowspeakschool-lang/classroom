#!/usr/bin/env python3
"""Сборка уроков Go Getter 1: блоки → SQL, с проверкой до заливки.

Копия tools/sm3_build.py для GG1 (общий сборщик не дорабатываем — курсы живут
отдельно). Уроки описываются питоновскими структурами ниже, скрипт собирает из
них миграцию и сам проверяет payload по списку из CLAUDE.md: правильный
вариант указывает на задуманный, нет дублей в вариантах, правые значения match
уникальны, склейка order совпадает с предложением, число пропусков в gaps
совпадает с задуманным, каждая ссылка на картинку есть в media/.

  python3 tools/gg1_build.py --list                   все уроки и что не готово
  python3 tools/gg1_build.py --lesson u0_hw1          проверить и показать SQL
  python3 tools/gg1_build.py --lesson u0_hw1 --sql migrations/gg1_u0_hw1.sql
  python3 tools/gg1_build.py --lesson u0_hw1 --chunks <lesson_id> --per-chunk 7
  python3 tools/gg1_build.py --unit u2 --insert       вставки всех уроков юнита
  python3 tools/gg1_build.py --unit u2 --check        сверка всего юнита одной строкой
                                                      (id уроков — tools/gg1_ids.json)

Выгрузка — ShkolaApp (docs/GG1_выгрузка_файлы.md). Игры Wordwall пересобраны
штатными блоками: в заголовке у таких блоков нет пометки, она стоит в
комментарии «СОСТАВ МОЙ» и строкой в docs/GG1_доработать_руками.md.
"""
import argparse, importlib, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gg1_lib import ROOT, MEDIA_URL, COURSE, VOCAB  # noqa: E402

# Уроки — по модулю на юнит; порядок здесь = порядок в --list.
UNIT_MODULES = ["gg1_u0", "gg1_u1", "gg1_u2", "gg1_u3", "gg1_u4",
                "gg1_u5", "gg1_u6", "gg1_u7", "gg1_u8", "gg1_final"]
LESSONS = {}
for _m in UNIT_MODULES:
    try:
        LESSONS.update(importlib.import_module(_m).LESSONS)
    except ModuleNotFoundError as e:
        if e.name != _m:
            raise


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
                # правильный вариант должен быть именно английским словом из пары
                ru = re.search(r"«(.+?)»", q["q"])
                if ru:
                    want = next((en for en, r, _ in VOCAB if r == ru.group(1)), None)
                    if want and texts[q["correct"][0]] != want:
                        errors.append(f"{where}, вопрос {n}: correct указывает на «{texts[q['correct'][0]]}», "
                                      f"а ждём «{want}»")

        if btype == "match":
            rights = [p.get("right", p.get("right_image")) for p in payload["pairs"]]
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
        for link in re.findall(r"@@MEDIA@@([^\"'\\\s)<]+)", json.dumps(payload, ensure_ascii=False)):
            path = os.path.join(ROOT, "media", link)
            if not os.path.exists(path):
                errors.append(f"блок {i} ({btype}): нет файла media/{link}")


# ---------- SQL ----------

def sql_for(key, lesson):
    out = [
        f"-- {COURSE} · " + lesson["unit_title"] + " · " + lesson["lesson_title"],
        "-- собрано tools/gg1_build.py --lesson " + key,
        "do $mig$",
        "declare",
        "  v_course uuid;",
        "  v_unit   uuid;",
        "  v_lesson uuid;",
        "  v_media  text := 'https://classroom.wowteach.ru/media/';",
        "begin",
        f"  select id into v_course from classroom_courses where title = '{COURSE}';",
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


def jsonb_text(v):
    """Текст jsonb так, как его печатает Postgres (payload::text): ключи по длине,
    потом по байтам, разделители «, » и «: »."""
    if isinstance(v, dict):
        keys = sorted(v, key=lambda k: (len(k.encode()), k.encode()))
        return "{" + ", ".join(json.dumps(k, ensure_ascii=False) + ": " + jsonb_text(v[k]) for k in keys) + "}"
    if isinstance(v, list):
        return "[" + ", ".join(jsonb_text(x) for x in v) + "]"
    return json.dumps(v, ensure_ascii=False)


def digests(lesson):
    """md5 каждого блока в том виде, в каком он ляжет в базу."""
    import hashlib
    out = []
    for n, (btype, payload) in enumerate(lesson["blocks"]):
        clean = {k: v for k, v in payload.items() if k != "gaps_expected"}
        clean = json.loads(json.dumps(clean, ensure_ascii=False).replace("@@MEDIA@@", MEDIA_URL))
        out.append((n, btype, hashlib.md5(jsonb_text(clean).encode()).hexdigest()))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lesson")
    ap.add_argument("--list", action="store_true", help="все уроки и что в них не готово")
    ap.add_argument("--sql", help="записать SQL в файл")
    ap.add_argument("--chunks", metavar="LESSON_ID",
                    help="печатать вставки блоков кусками, готовыми для execute_sql "
                         "(длинный do-блок отваливается по таймауту)")
    ap.add_argument("--per-chunk", type=int, default=3)
    ap.add_argument("--verify", metavar="LESSON_ID",
                    help="запрос для сверки залитого урока: md5 каждого блока в базе "
                         "против собранного здесь; одна строка: ok или BAD <sort_order> на каждый блок")
    ap.add_argument("--unit", help="все уроки юнита (u2): с --insert — вставки, с --check — сверка")
    ap.add_argument("--insert", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    if args.unit:
        ids = json.load(open(os.path.join(ROOT, "tools", "gg1_ids.json")))
        keys = [k for k in LESSONS if k.startswith(args.unit + "_")]
        for k in keys:
            errors = []
            check(LESSONS[k], errors)
            if errors:
                sys.exit(f"{k}: проверка не прошла: {errors}")
            if k not in ids:
                sys.exit(f"{k}: нет id в tools/gg1_ids.json")
        if args.insert:
            # по уроку на запрос: так запрос короче лимита и падение видно по уроку
            for k in keys:
                print(f"-- {k}")
                print("insert into classroom_blocks (lesson_id, type, payload, sort_order) values")
                print(",\n".join(
                    f"('{ids[k]}', '{t}', replace($blk$"
                    + json.dumps({a: b for a, b in p.items() if a != "gaps_expected"}, ensure_ascii=False)
                    + f"$blk$, '@@MEDIA@@', '{MEDIA_URL}')::jsonb, {n})"
                    for n, (t, p) in enumerate(LESSONS[k]["blocks"])))
                print("returning sort_order;\n")
        if args.check:
            rows = ",".join(f"('{ids[k]}',{n},'{t}','{h}')" for k in keys for n, t, h in digests(LESSONS[k]))
            lids = ",".join(f"'{ids[k]}'" for k in keys)
            print(f"with want(lid,so,t,m) as (values {rows}),\n"
                  "have as (select lesson_id::text lid, sort_order so, type t, md5(payload::text) m "
                  f"from classroom_blocks where lesson_id::text in ({lids}))\n"
                  "select count(*) total, count(*) filter (where w.m = h.m and w.t = h.t) ok, "
                  "string_agg(coalesce(w.lid, h.lid) || ':' || coalesce(w.so, h.so), ' ') "
                  "filter (where w.m is distinct from h.m or w.t is distinct from h.t) bad, "
                  "(select count(*) from classroom_blocks where payload::text like '%@@MEDIA@@%') leftover "
                  "from want w full join have h using (lid, so);")
        return

    if args.list:
        for key, lesson in LESSONS.items():
            errors = []
            check(lesson, errors)
            state = "готов" if not errors else f"{len(errors)} замечаний"
            print(f"{key:<10} {lesson['unit_title']} · {lesson['lesson_title']:<11} "
                  f"{len(lesson['blocks']):>2} блоков · {state}")
            for e in errors:
                print("     ·", e)
        return
    if not args.lesson:
        ap.error("нужен --lesson или --list")

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
    if args.verify:
        rows = ", ".join(f"({n}, '{t}', '{h}')" for n, t, h in digests(lesson))
        print(f"with want(sort_order, type, md5) as (values {rows}),\n"
              f"have as (select sort_order, type, md5(payload::text) md5 from classroom_blocks "
              f"where lesson_id = '{args.verify}')\n"
              "select count(*) blocks, string_agg(case when w.md5 = h.md5 and w.type = h.type "
              "then 'ok' else 'BAD ' || coalesce(w.sort_order, h.sort_order) end, ' ' "
              "order by coalesce(w.sort_order, h.sort_order)) result "
              "from want w full join have h using (sort_order);")
        return
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

