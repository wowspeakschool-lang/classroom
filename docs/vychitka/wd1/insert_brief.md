# Вставка новых картинок в Wow Dragon 1 — бриф агенту

Курс `wow-dragon-1`, проект Supabase `vtcxghsqymwkyiogpndf`, `mcp__Supabase__execute_sql`.
Уроки: `classroom_lessons.title = 'Homework N'`. Номер блока «бN» = номер в
редакторе = `row_number() over (order by sort_order)`.
Резервная копия: `classroom_blocks_backup_wd1_vychitka_20261014` (до правок).

Новые картинки (все одобрены Анной, лежат на сайте):
`https://classroom.wowteach.ru/media/wow-dragon-1/new/<имя>.webp`, файлы —
`/home/user/classroom/media/wow-dragon-1/new/`. Открой нужные файлы (Read),
чтобы видеть, что на них.

## Правила
- Меняешь **только ссылки на картинки** (`image`, `left_image`, `img`, `src` —
  поле смотри в текущем payload). Тексты, звук, `correct`, порядок — не трогать.
  Исключение: если картинка сделана под новое задание («новый блок» ниже) и
  подходящего блока нет — опиши в ответе, не создавай блок.
- Перед правкой прочитай payload по `id`; правка — по `id`, точечно через
  `jsonb_set`, а не перезаписью целиком:
  `update classroom_blocks set payload = jsonb_set(payload, '{questions,0,options,2,image}', to_jsonb('https://…'::text)) where id='…';`
- В строках SQL нельзя `;` (MCP зависает) — у нас его и не будет.
- Если на месте, указанном в списке, нет картинки, которую надо заменить
  (номер сдвинулся), найди это место в уроке по смыслу (слово/фраза в тексте или
  звуке). Не нашёл — в ответ, не гадай.
- Старая картинка годилась бы и так? Всё равно ставь новую: это решение Анны.
- После урока проверь: `select payload::text like '%/new/%'` по изменённым id и
  что все ссылки `/new/<имя>.webp` соответствуют файлам.
- Не трогать уроки вне своего диапазона. Файлы не писать — ответ текстом.

## Что куда (из отчётов «Нужна картинка»)
ДЗ 1–26:
- ДЗ 5 (по желанию): friends → `dragon_friends`
- ДЗ 7: Дракоша hungry → `dragon_hungry` (где в ДЗ 7 есть hungry)
- ДЗ 8: clap your hands → `dragon_clap`
- ДЗ 9 б6: cut out (сейчас ножницы) → `dragon_cut_out`
- ДЗ 14 б2, б3, б5, б6, б8, б9 и ДЗ 18 б2: bad cat / dog / dinosaur →
  `bad_cat`, `bad_dog`, `bad_dinosaur`; ДЗ 25 б4 в.3 bad dog (`f06a7f41eddc…`
  → `bad_dog`); ДЗ 26 б6 в.6 bad cat (`680772c3fab1…` → `bad_cat`). Вообще
  везде в ДЗ 1–26, где стоят эти старые bad-картинки, — заменить.
- ДЗ 26 б3: игрушки в количествах — `dolls_2`, `robots_3`, `cars_2`, `cars_3`,
  `planes_3`, `dinosaurs_2`, `teddy_bears_2`, `teddy_bears_3` — туда, где
  вариант называет это количество, а картинка не та / кружок / одна штука.
- ДЗ 26 б7: цвета — `dog_black`, `dog_brown`, `dog_white`, `cat_red`,
  `cat_orange`, `cat_grey`, `ice_cream_blue`, `ice_cream_pink`,
  `ice_cream_white` вместо кружков.
- ДЗ 26 б6: «The dragon is big» → `dragon_big`

ДЗ 28–53:
- ДЗ 28 б2, б6 в.2, б8: learn → `dragon_learn`
- ДЗ 31 б2, ДЗ 33 б9 в.2, ДЗ 34 б7 в.3 и б10: «I don't have» → `dragon_dont_have`
- ДЗ 32: строчные b, d, q → `lc_b`, `lc_d`, `lc_q` везде, где сейчас строчные
  нарисованы уменьшенными заглавными (и в ДЗ 40, если там те же картинки
  строчных). `lc_u` — строчная u: где в курсе строчная u нарисована криво/как
  заглавная (ищи по курсу, ДЗ 28–53 и сообщи, если такое место в 55–80).
- ДЗ 35 б5, б6: colour → `dragon_colour`
- ДЗ 38 б8: funny → `dragon_funny`; ДЗ 45 и ДЗ 53 б9: funny / friendly →
  `dragon_funny`, `dragon_friendly`
- ДЗ 44 б2, б4, б7; ДЗ 52 б9; ДЗ 53 б9: be on time → `dragon_on_time`
- ДЗ 53 б6: `circles_pink_2`, `squares_orange_3`, `triangles_white_5`

ДЗ 55–80:
- ДЗ 55 б2: find → `dragon_find` (сейчас фонарик)
- ДЗ 63 б2: We need → `dragon_we_need`
- ДЗ 66 б2: help → `dragon_help`
- ДЗ 71 б2 (б3, б5): competition → `scene_competition`
- ДЗ 75 б5, б6: строчная s → `lc_s` (и везде в 55–80, где строчная s как заглавная)
- ДЗ 75 б2–б3: hooray (сейчас та же картинка, что win) → `dragon_hooray`
- строчная u (если есть в 55–80, напр. ДЗ 59, 67, 79, 80) → `lc_u`

## Ответ
По каждому ДЗ: блок · что было → что стало (имя файла). Отдельно: «не нашёл
место» и «новый блок не создан».
