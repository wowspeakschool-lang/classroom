# «Озвучить пачкой» теряет блоки в конце списка

Нашлось 10.11.2026. Анна нажала «Озвучить пачкой» по всем курсам, кнопка
отчиталась «все 7260 помеченных уже озвучены», а в базе осталось **12
помеченных мест без звука** — и все они в девяти уроках, чьи `lesson_id`
начинаются на `f`, то есть в самом хвосте порядка по `id`.

## Где

`src/features/hwReview/editor/api.ts`, функция `ttsScan`:

```ts
for (let i = 0; i < lessonIds.length; i += 100) {
  const { data, error } = await sb.from('classroom_blocks')
    .select('id, payload')
    .in('lesson_id', lessonIds.slice(i, i + 100))
  ...
}
```

У запроса нет ни `.limit()`, ни `.range()`, ни постраничного обхода, поэтому
действует серверный предел PostgREST на число строк в ответе (у проекта он
1000). Сотня уроков — это больше тысячи блоков: в базе 593 урока и 6275
блоков, в среднем 10,6 блока на урок, то есть примерно **1060 блоков на
порцию**. Всё, что выше тысячи, молча отбрасывается.

Из-за этого ломаются сразу две вещи:

1. блоки из хвоста порции не попадают в `items` — их не озвучивают;
2. счётчик `done` считается по тем же полученным строкам, поэтому кнопка
   говорит «всё озвучено»: потерянных пометок она не видела.

Порядок строк без `order` в PostgREST не определён, но на практике идёт по
индексу первичного ключа, поэтому отбрасывается хвост по `id` — ровно те
девять уроков на `f`.

## Что сделать

Обойти выборку постранично, пока страница приходит полной:

```ts
for (let i = 0; i < lessonIds.length; i += 100) {
  const ids = lessonIds.slice(i, i + 100)
  const SIZE = 1000
  for (let from = 0; ; from += SIZE) {
    const { data, error } = await sb.from('classroom_blocks')
      .select('id, payload')
      .in('lesson_id', ids)
      .order('id')
      .range(from, from + SIZE - 1)
    if (error) throw error
    const rows = (data ?? []) as { id: string; payload: Payload | null }[]
    for (const b of rows) { /* как было */ }
    if (rows.length < SIZE) break
  }
}
```

`.order('id')` здесь обязателен: без устойчивого порядка страницы могут
пересечься или пропустить строки.

Проверка после правки: нажать «Озвучить пачкой» по всем курсам и убедиться,
что запрос ниже возвращает ноль.

```sql
with recursive obj(bid, val) as (
  select b.id, b.payload from classroom_blocks b where b.payload::text like '%_tts%'
  union all
  select o.bid, e.value from obj o
    cross join lateral (
      select value from jsonb_each(o.val) where jsonb_typeof(o.val)='object'
      union all
      select value from jsonb_array_elements(o.val) where jsonb_typeof(o.val)='array'
    ) e
  where jsonb_typeof(o.val) in ('object','array')
)
select count(*)
from obj o
cross join lateral jsonb_object_keys(o.val) k(key)
where jsonb_typeof(o.val)='object' and k.key like '%\_tts'
  and coalesce(o.val->>left(k.key, length(k.key)-4), '') = '';
```

## Пока не исправлено

Обход со стороны контента: выбирать на «Медиа» не все курсы сразу, а по
одному курсу (или по юниту) — тогда порция остаётся меньше тысячи блоков и
ничего не теряется. Второй путь — открыть урок в редакторе и нажать там
«🔊 Озвучить (N)»: он читает блоки одного урока и под предел не попадает.

## Что осталось озвучить на 10.11.2026

| курс | урок | блоки |
|---|---|---|
| Super Minds 1 | юнит 1, ДЗ 3 | 12 |
| Super Minds 2 | юнит 6, ДЗ 7 | 14 |
| Super Minds 2 | юнит 7, ДЗ 6 | 8 |
| Wow Dragon 1 | ДЗ 7 | 11 |
| Wow Dragon 1 | ДЗ 78 | 11 |
| Wow Dragon 2 | ДЗ 1 | 10, 11 |
| Wow Dragon 2 | ДЗ 40 | 10, 11 |
| Wow Dragon 2 | ДЗ 47 | 9, 10 |
| Wow Dragon 2 | ДЗ 67 | 13 |
