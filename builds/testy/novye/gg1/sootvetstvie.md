# Промпты 1–10 (Go Getter 1, юниты 0–3) — что из какого листа нарезано

Листы Анны лежат на Диске в папке «тесты Pic» (`1XHXpMI-3I0MwRIlVygXzzduhvl5tKwF3`),
имена — случайные UUID. Нарезано `tools/cut_auto.py`, webp качество 90.
Файлы здесь — **превью**, в `media/` кладём после «да» Анны.

| промпт | UUID листа | размер листа | кусков | файлы | ляжет в |
|---|---|---|---|---|---|
| 1 | `81a36c79-86f0-49e6-ad2a-21fa234e5521.png` | 1536×1024 | 6 | obj_book, obj_pen, obj_bag, obj_chair, obj_clock, obj_ruler | `media/gg1/u0/` |
| 2 | `e5177a41-d1de-4e35-a07b-a79a10ebd520.png` | 1536×1024 | 6 | col_red_pen, col_blue_bag, col_yellow_ruler, col_green_notebook, col_pink_pencil_case, colour_red | `media/gg1/u0/` |
| 3 | `21bfd83d-30ef-4b4e-a1bb-d2e784504a25.png` | 1536×1024 | 1 | test_classroom | `media/gg1/u0/` |
| 4 | `cf67a31c-8522-4db1-a09f-e531beaff608.png` | 2172×724 | 5 | clothes_tshirt, clothes_skirt, clothes_dress, clothes_jeans, clothes_coat | `media/gg1/u2/` |
| 5 | `f96b9dd2-4877-4822-b120-c5432065a26b.png` | 1672×941 | 5 | clothes_jumper, clothes_shoes, clothes_top, clothes_shirt, clothes_trousers | `media/gg1/u2/` |
| 6 | `a0e6d864-6064-468c-84d2-460ed4839396.png` | 1536×1024 | 6 | clothes_jacket + пять про запас (`zapas/`) | `media/gg1/u2/` |
| 7 | `c9a7681a-825b-48ec-bef8-792642259153.png` | 1536×1024 | 5 | near_trainers, near_tracksuit, far_hoodie, far_cap, far_boots | `media/gg1/u2/` |
| 8 | `e8a28141-45fe-4554-821a-ce66907e2e0a.png` | 2172×724 | 3 | pencils_heart, boot_black, cinema | `media/gg1/u2/` |
| 9 | `811c7a00-731b-4d5b-a3ab-3e23722f76de.png` | 1536×1024 | 1 | kevin_birthday | `media/gg1/u2/` |
| 10 | `e0870211-fff1-41fb-a1d3-cc1abf5a761e.png` | 1536×1024 | 6 | furn_wardrobe, furn_bath, part_window, furn_carpet, photo_lamp, photo_armchair | `media/gg1/u3/` |

Контактные листы: `kontakt_gg1_u0.png`, `kontakt_gg1_u2.png`,
`kontakt_gg1_u3.png`, `kontakt_gg1_u2_zapas.png`.

## 🟥 Что требует решения Анны

1. **`colour_red` в базе — `.svg`, а новый кусок — `.webp`.** Остальные 38 имён
   совпали с базой один в один, это единственное исключение. Поставить новый
   файл можно только вместе с правкой пяти блоков
   (GG1 Unit 0: ДЗ 2 блоки 2, 3, 4, 7 и Unit 0 Test блок 2) — то есть правка
   заденет и домашки, не только тест. Либо меняем ссылки на `.webp`, либо
   оставляем старый svg.
2. **Лист промпта 5 сгенерирован узким (1672×941 на пять вещей в ряд).**
   Куски вышли 254–411 px по большей стороне вместо 600–800: clothes_top
   254×320, clothes_trousers 261×387, clothes_shoes 311×266, clothes_jumper
   385×335, clothes_shirt 411×348. Не растягиваем. Прежние файлы были того же
   порядка (189–359 px), так что хуже не стало, но если нужен запас по
   качеству — перегенерировать лист промпта 5 пошире.
3. **`photo_lamp` стал мельче прежнего** (было 512×512, стало 393×474) —
   лист промпта 10 с шестью предметами. Стиль при этом теперь общий с
   остальной мебелью.
4. **У `near_trainers` на кроссовках генератор нарисовал «галочку» Nike**,
   хотя в промпте стояло «no brand marks». Если смущает — перегенерировать
   лист промпта 7.

## Запас (`u2/zapas/`)

Из листа промпта 6, кроме `clothes_jacket`, нарезаны пять вещей про запас:
`zapas_cap`, `zapas_hoodie`, `zapas_tracksuit`, `zapas_trainers`,
`zapas_boots`. В базе таких имён нет — это те же предметы, что внутри сцен
промпта 7, на случай если Анна решит оставить формат «предмет + стрелка».
Пока никуда не кладутся.
