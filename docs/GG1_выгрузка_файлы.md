# Go Getter 1 — файлы выгрузки в Google Drive

Чтобы не искать заново: поиск по Drive стоит дорого. После перезаливки
05.10.2026 у **каждого** задания, как в SM3, два файла: `.pdf` и `.txt` того же
имени. В `.txt` — только текст, картинки — в PDF (pymupdf, см. CLAUDE.md).

Опись снята 05.10.2026 запросом `parentId = '<id папки>'` с
`excludeContentSnippets: true`. ⚠️ Ответ приходит страницами по 4–15 файлов,
**сколько бы ни стояло в `pageSize`** — идти по `nextPageToken`, пока он не
пропадёт, иначе половина юнита не видна. Подпапок внутри юнитов нет.

⚠️ **Методист перезалила всю выгрузку GG1 сжатой 05.10.2026.** Все id папок и
файлов поменялись; id из первой заливки (папка `1n5SD_jhJuy4QwL7RefvpsRAKK86EppSy`,
PDF по 22–35 МБ) **устарели — не использовать**.

PDF теперь весят **0.8–5.5 МБ**. `download_file_content` надёжно
отдаёт файлы примерно до 4 МБ. Больше 4 МБ — 8 файлов: семь тестов юнитов и одна домашка —
Unit 1 Test (5.5), Unit 2 Test (4.6), Unit 3 Test (4.6), Unit 4 Test (4.9), Unit 5 Test (4.4), Unit 6 Test (5.5), Unit 6 Homework 3 (4.1), Unit 7 Test (5.1).
С ними сначала пробовать скачивание; если не пройдёт — текст брать из `.txt`,
а картинки искать другим путём.

Выгрузка — из **ShkolaApp**, не «Взнания». Текстовый слой хороший: задания,
слова «Составь предложение», пары, пропуски читаются. **У игр Wordwall в конце
текста есть ссылки** `wordwall.net/resource/…?wwmethod=embed` — в отличие от SM3.
Чего в тексте нет: какой вариант «Верно / неверно» отмечен и сами картинки.

Путь: папка `GG1` (`1DtJHjm7rmvF33PqSyAvxtYypPx1csC3p`) → в ней вложенная
папка `GG1` (`1LKnRolbg1BsNWPWdd9wDeDCt8YhzbkWo`), больше в верхней ничего нет.
Во вложенной — папки `Unit 0`…`Unit 8` и файлы финального теста, отдельной
папки у него нет.

| Юнит | id папки |
|---|---|
| Unit 0 | `1TGPiKTU5FjfrjFP5NfhHPUeEAuVepFtx` |
| Unit 1 | `15Rkikcs_hqM8RGQtYlWsFbVEnPASZ5qv` |
| Unit 2 | `1k2SFmoRzDkopY9PDrdO_voGNNX1nozFE` |
| Unit 3 | `1Q1DbYaDYNGxw8fDlYNRQ9LkeLXVbQg00` |
| Unit 4 | `1EYGemU7hmq-680ruA1EPKt-glNevpXz2` |
| Unit 5 | `18W_Rnve8uYppzwRouuzdo_XD9tnOoRTM` |
| Unit 6 | `1P2npm2Z12q-dUgNvzeqSg9QjDXNhpJi6` |
| Unit 7 | `1k7PkgumIUawHajjvV7Q-WSo2IAu3WOPg` |
| Unit 8 | `1nThPMetLmxmljo4LDaT-0wiWLsVtcPFK` |

Размер — в МБ (10⁶ байт) для PDF и в КБ (10³ байт) для `.txt`.

## Unit 0 — папка `1TGPiKTU5FjfrjFP5NfhHPUeEAuVepFtx`

| Файл | pdf | МБ | txt | КБ |
|---|---|---|---|---|
| Homework 1 | `1MIq-XVS5jt7vpwUI-plawe924LfGLvG_` | 1.9 | `1lMJMoVlqKMcCJU8sJsUVT8Yt000QgEe2` | 13.6 |
| Homework 2 (1) | `1A2yTqoaMmCK27n0nIvuUQVnRiwXUdlGI` | 0.8 | `1UdTok3M2Z5ICnnSE8m7Kw3dwHVAP5v72` | 3.7 |
| Homework 2 (2) | `1Ons049_pGIOQRcZHiLhDifPilB1zZo6O` | 1.8 | `1qhBTxjlSvnTNZ1kVlOiB0RtZjXJInBte` | 11.3 |
| Homework 3 (1) | `14NLFjCTh_hDuXswA88yOjJz-x79K3Doe` | 0.8 | `1XWtkMBB7Z3OP0WS4SKYCZNg70CQM2Yet` | 4.1 |
| Homework 3 (2) | `1groy7CFRZZ5dWF7gXi6h1uIgng0ATnQn` | 2.2 | `1KzojE5QQ2wdCmX07j0HUoDOieE0z7PqI` | 15.7 |
| Test | `1lri__GeQ-d7bVhDmhJ1VL8wyWdT-rN_w` | 1.8 | `128gig7WeG6ryU9guSEbRL72_TW78YtRd` | 12.9 |

Файлов 12 (6 pdf + 6 txt). Пропусков в нумерации нет, тест на месте. Домашек **три**: «Homework 2» и «Homework 3» разложены на два файла — каждая один урок. Нумерация идёт подряд 1–3 и на этом кончается; что юнит вводный и домашек в нём просто меньше — предположение, содержимое не открывалось.

## Unit 1 — папка `15Rkikcs_hqM8RGQtYlWsFbVEnPASZ5qv`

| Файл | pdf | МБ | txt | КБ |
|---|---|---|---|---|
| Homework 1 (1) | `1SfnXUi9igB-vIRl_OkPnCCP32iSDMaDh` | 0.8 | `1k7ba36A6Rrz3HHh4_FKB0I2vvWslHYAE` | 4.1 |
| Homework 1 (2) | `1NkCaQiIe6JQbx9fyLFDtBoCh4s4Ojwpa` | 2.3 | `1dJBX1dtuznduZO5ACqqrGlWX9D2Os0Jv` | 10.7 |
| Homework 2 | `1FwkaVhX1q1ZQTac6LCnBgHoD9ZJu2qcH` | 1.8 | `1rattfUhHfhuUgMvq2-azy478QRzukj6v` | 11.8 |
| Homework 3 | `1ciehn7XMnGzq5T1t7SPCbg8Z5b5lmUqz` | 2.7 | `10I-ZeKKqhSe7nDD_HKOaBEwWn1P70IF0` | 17.5 |
| Homework 4 | `171f9Qs063VS38BaEcmaCg3DPFfMYpnkU` | 2.7 | `1lRFRzfo7Nty_t5n6woxB66Ne_WijpB52` | 10.8 |
| Homework 5 | `1mlvWt-YKH0_nh0bllFWMCy9yC0qX01kr` | 1.7 | `19DH5mvGcNQpVP7Vgsenp6vw9voWrodTB` | 9.2 |
| Homework 6 | `1TuhwN5YY0qBlbAG3SNiVyqoQE16miRD5` | 2.5 | `1yLcsI5hWRqn4lKGtduLKNtc3lmsH51jK` | 8.7 |
| Homework 7 | `1oMeEPfvQFHfJ3s9PzHv-wWnRtMppGPfS` | 2.7 | `1AnGk4hp1r2VbkPs4Mt3s1rt94674J0Tj` | 19.8 |
| Test | `1ZmhP3NkHM2KW1EUEqSHJDah5MGqGzSpk` | 5.5 | `19oYtT_wEnlugCi8qB52Z9T7_SEOgOE71` | 19.5 |

Файлов 18 (9 pdf + 9 txt). Пропусков в нумерации нет, тест на месте. Домашек **семь**, «Homework 1» разложена на два файла — это один урок. Тест больше 4 МБ.

## Unit 2 — папка `1k2SFmoRzDkopY9PDrdO_voGNNX1nozFE`

| Файл | pdf | МБ | txt | КБ |
|---|---|---|---|---|
| Homework 1 (1) | `1_bKZnwBDO4O4JqG_JBX3hW_8PzDzZaqn` | 0.8 | `10b7KkJ_LKZkFtWWSbLaKz2cQRgz-oBDQ` | 3.9 |
| Homework 1 (2) | `14dsUXOCO4EFt6Qg48k9LsR2G41eUH0e0` | 1.8 | `1WvK3fDhxtW1NsxbPG9dao8nXv71p5kAv` | 11.9 |
| Homework 2 (1) | `1nmqqnhYN6KGNoZUj_IaEssyW8RAPDDoP` | 0.8 | `1ngmCuKVN44SPt02q7CHCRNTP7-P5vXDL` | 3.5 |
| Homework 2 (2) | `1hYr0p_k9HlmOuvX7hYtkCprNwBRMSQTW` | 1.6 | `1qefa2Q5L6-osjAgEQSK3ZIcqQ-z4Hh2j` | 11.0 |
| Homework 3 | `12tPrrbmEiiwFFkIh38PuNchQ_fSlffoz` | 1.9 | `1ZVNAMN5vazg8rrAxVbQzVFLJCRYlU-01` | 12.5 |
| Homework 4 | `16po5vIdX-7qPP7aZj4V_FSZplOwQNckl` | 3.2 | `1pgXQBcQg_onv_PTiZ3yA2-GCKwYwNtOr` | 11.6 |
| Homework 5 | `1fWgeRj7DW58oM3kvwq4OZqR4wtXswoca` | 1.3 | `168ATEztbM6asvrZflAvTNFaopydJq-7C` | 5.7 |
| Homework 6 | `1LQ61pFjpDJ8yROfGUywpGAwez-hS9Iwq` | 1.6 | `1loRrAqJX56pKDyn4ITnMtuMygaHaiIA-` | 9.9 |
| Homework 7 | `1Y0wU4EZjHaCQj6UczoZ6fhFM-LBfcrdR` | 2.0 | `1bbDOrrES3wa4dqMPfF_H-5qdIVVw79fI` | 13.0 |
| Test | `1eOZI3vdUD184WpXYo5z8ID5UGeo2h38f` | 4.6 | `1oAdHCK8otVIQTs14_W5HwMD1MBu6k0TH` | 23.5 |

Файлов 20 (10 pdf + 10 txt). Пропусков в нумерации нет, тест на месте. Домашек **семь**, «Homework 1» и «Homework 2» разложены на два файла — каждая один урок. Мусорного `.DS_Store`, который лежал здесь в первой заливке, больше нет. Тест больше 4 МБ.

## Unit 3 — папка `1Q1DbYaDYNGxw8fDlYNRQ9LkeLXVbQg00`

| Файл | pdf | МБ | txt | КБ |
|---|---|---|---|---|
| Homework 1 (1) | `1ZEtkqkGQaFG_5fAgTZTkcYCbx2qtr_U5` | 0.8 | `1AaM_QYuM5hy91or0pf4RBrl0pCspqI5j` | 3.4 |
| Homework 1 (2) | `1dgWdO-Ak0lsbImvxhYrOXoKGwBbSKQVC` | 0.8 | `1nEu4W8jEl1I3WkE519K5PTv1c6USPcxt` | 3.4 |
| Homework 1 (3) | `1uXRUHftIP2mLNwTjdO_aE3bi438CxRpL` | 2.1 | `1bew5jhUfUt84U3l28w4iEpEYFhxBGlBO` | 12.7 |
| Homework 2 (1) | `1aeSwErHd-c3f3VvkiyC6bkKqsUMRK6ju` | 1.4 | `17i1gzhyQoKbIFesQOUDs2xT7GfEeGzlb` | 9.1 |
| Homework 2 (2) | `12o7_2FZwoSCZQSrN_sGIgVn_5jIZOu-i` | 1.6 | `1t_9IqQFdVke_hGkHRDIRyoLUNkjLxdzb` | 9.9 |
| Homework 3 (1) | `1eQk6S2ZRWMBi8q0bB-xh4DXjMY3jKY98` | 1.8 | `17-IO8YEL0lBrA_BaY1r-rmWw_E3dcyZs` | 10.9 |
| Homework 3 (2) | `1_DcjdVRLBfpV4FhAcb_eka_mKPwBn0vK` | 2.1 | `1sMMwkPfTkPs7zw01KqqA20mSZ8gAIXWJ` | 13.0 |
| Homework 4 | `1NqyGX5kTjuuEzXInh8vVh1p8pMqt4mfp` | 1.9 | `1CdwKHnA7AKqKba7TvXkEDeOynV-_cvzr` | 10.5 |
| Homework 5 (1) | `1Tbq4w3pVU2xjxLbZoStqhOn4K-anjP66` | 0.8 | `140NCuQNkI4n63pkzdnApjYHzdzqfi93b` | 3.2 |
| Homework 5 (2) | `1fsT9lpOiLCnZVXgj_He_mtOFyKkAakVF` | 1.9 | `12AzmsbvPbbM1QyMgvvSHyRihmuo18efd` | 11.0 |
| Homework 6 | `1ynCK9VAxQLoXTPM404sifms6nIZ11i8j` | 1.8 | `18jisKOuSxUnKT0lIrkEPqhG9ZSD16WPQ` | 8.9 |
| Homework 7 | `141iJ_5bfhw_Wp1vF0SNM5l2Prwn_M58u` | 2.1 | `1aa0DfAqM25Y-wk38co8r3V_P4fiuri2h` | 13.4 |
| Test | `1ROtoEMAO2Iq1ztpxTsCvq6I6qrmyrvbc` | 4.6 | `1HZKjp2VRThD6XSQ7hdNu8ijumIH2DT4_` | 24.6 |

Файлов 26 (13 pdf + 13 txt). Пропусков в нумерации нет, тест на месте. Домашек **семь**. ⚠️ «Homework 1» разложена на **три** файла — (1), (2), (3); в SM3 такого не было. «Homework 2», «Homework 3» и «Homework 5» — на два. Каждая — один урок, блоки подряд. Тест больше 4 МБ.

## Unit 4 — папка `1EYGemU7hmq-680ruA1EPKt-glNevpXz2`

| Файл | pdf | МБ | txt | КБ |
|---|---|---|---|---|
| Homework 1 (1) | `1Tk6mtVep0NCyvz1uM6sAWqILqS-9cdxC` | 0.8 | `1uRKW6dzScCVzj6KcnDWqOI3G7z8bMUOb` | 3.4 |
| Homework 1 (2) | `1E1yiqvJo7mhRHFFihu8zERsLS8JYfymI` | 0.8 | `14XzP_1vXg_e2cXVgLBWMFhI-XZgcauVW` | 3.5 |
| Homework 1 (3) | `161zv1yueOLsWbUVMAZXCSR9MVm7JfgSv` | 2.6 | `16aiYDKXJaowNLQVUnEsC3df9IVyiupCj` | 15.7 |
| Homework 2 (1) | `1Q3_cDoXqQXaeV2Fu-8GSs9ZI7nxg5Of8` | 0.8 | `1soBJirjwbXcsrHsc2ljpHaa3UT0xQ_S9` | 3.4 |
| Homework 2 (2) | `1ktbyojDCA7B-D8-JyKc4Kc0Rp_FqnE2G` | 2.0 | `1VmiHWKd1utC8HG1QhPIFA6Y5Fa8tbJXP` | 15.1 |
| Homework 3 | `1qrxWht3_WdpyUC5ajVxEzDj5MPYCH1ax` | 2.7 | `1l9jf9Or2WtL5dwkv8_Rtu49G-bruGQHu` | 15.9 |
| Homework 4 | `1k4xN-15Mp0mDdqW_I3cDy3Ww00-pV1xj` | 2.2 | `1v01ysu5AivbzJBTZ_luAh0SlrOLw7y1E` | 15.2 |
| Homework 5 | `1h2Yl_8jeQ38Oy8b7o86R_GD1z5IqSPoR` | 1.5 | `1CLR9FMMDADFcMFuiKuGtMPgjZPgA3caB` | 10.8 |
| Homework 6 | `1NeED7gBdRasz37QrvoX4PlEg9sJv1NY2` | 1.8 | `1x6HI2YTuCRiIPBGmNC_h9kEix0lqbVPH` | 11.4 |
| Homework 7 | `1QG6yDzo6geLWMYziGLmKzqxt86sun2A5` | 2.1 | `1ydbcF_c9UPeqJNbpRtNPk0JQ7hSRmzSm` | 12.3 |
| Test | `1aWBGKNlg6xgb5wlU5X6spvVfz_xYp7mn` | 4.9 | `1fLcOH1ThFqkcirY8jgIFJM3-Lm8i8-2X` | 29.6 |

Файлов 22 (11 pdf + 11 txt). Пропусков в нумерации нет, тест на месте. Домашек **семь**. ⚠️ «Homework 1» разложена на **три** файла — (1), (2), (3). «Homework 2» — на два. Каждая — один урок. Тест больше 4 МБ.

## Unit 5 — папка `18W_Rnve8uYppzwRouuzdo_XD9tnOoRTM`

| Файл | pdf | МБ | txt | КБ |
|---|---|---|---|---|
| Homework 1 (1) | `1RUxkedq3XEdUPBwglJ9HkulcUvavLkSv` | 0.8 | `1U5oUu1R_EJegccSsS-j0V1qhYPmuEJnp` | 3.8 |
| Homework 1 (2) | `1k43UDitCXl2r3Nh-eJaatC34EtbP8qRj` | 2.2 | `1PEMgavd3TXnhs9gFKcqyEGUxW-mezph7` | 10.1 |
| Homework 2 | `11gte7a878AkM7ti_tfj6_jV6hlzYz0el` | 1.6 | `1yJmAdUUglesivIxTkWHa0xlE9HgGjPYt` | 13.5 |
| Homework 3 | `1KkHMTd_4rODlK46x1TWkJcGDBmvMtnpF` | 3.2 | `1nQcJPEjZkP7UY2s-8te-Q6F7LdK6GCn9` | 11.3 |
| Homework 4 | `1CA1mzavh_rtZb2ZEsFxle8rfh6BGm6ER` | 2.2 | `1gEcRjKNTaLOf5SyRnF_LpPCvzCtfpg5n` | 8.9 |
| Homework 5 | `1d_1bk17ug_ym7kgQWXnchC_FCGfCT3Gj` | 2.1 | `1bC9dcN9Be2A7HEFWotokt8pRp90XtYCH` | 11.0 |
| Homework 6 | `1ZWyWpfxlqQe-EkCvoL-jrzPh-OOk98dT` | 3.0 | `14D-wv1Ludxp_DNhSFpVWPcE-ZcY01e6x` | 10.0 |
| Homework 7 | `1824sXwtG1ruGkPW9rj9YE9cmx0Z4Dtzp` | 1.9 | `1ocIF7-JpYVUh2F3J0WWf2c9CCdbZezBf` | 10.4 |
| Test | `1qiAnqpm32BYbiY7dbh3ytYXo6YJYWVm2` | 4.4 | `1g78ZO5MqKjOszAWbZZ_2Y3iA2Kqodwy2` | 24.5 |

Файлов 18 (9 pdf + 9 txt). Пропусков в нумерации нет, тест на месте. Домашек **семь**, «Homework 1» разложена на два файла — это один урок. Тест больше 4 МБ.

## Unit 6 — папка `1P2npm2Z12q-dUgNvzeqSg9QjDXNhpJi6`

| Файл | pdf | МБ | txt | КБ |
|---|---|---|---|---|
| Homework 1 (1) | `1P7CsNegPRs12-bI2WvdVpyAOXUK4qOLD` | 0.8 | `1PcYWbavW_95aqW6JAzVEwZ9rfG330mw4` | 4.4 |
| Homework 1 (2) | `1AYkQ2rb7s8X6tMAyKuB5GC8raos51UDr` | 1.6 | `1oCBnFOqT5XUETjjmAitBkgzcX7abBSKw` | 9.2 |
| Homework 2 | `1gy5JfiCWg-8KbU5zq5dj0MxGZVRI3wPN` | 2.7 | `1Mw4GtKxcMGbe9VrxZNnkBaQ-NIipf7DF` | 14.8 |
| Homework 3 | `1R5GQL4uWTZsiC2c8_UJQwKfW-5VzQGBL` | 4.1 | `1C-ArnxthRCbhB_NepCBWsoKHi7-1SVa5` | 17.2 |
| Homework 4 | `154Ujj7xn_0ehG-fE4eB7RCxjmQ6TTx8k` | 1.9 | `1EBw1n1DYjr3Vf0_uSGwgJOuyNkdUnbI7` | 12.4 |
| Homework 5 | `1_54XlL7e0vLJsiGGgXBtHBoMtsIO471-` | 1.9 | `1ombe6drxupIgjGWAkDHRPZKWZHYS2xE8` | 14.3 |
| Homework 6 | `1kugbzel8Int0EirDOEVmkb3FKqjEN7l-` | 1.9 | `1fKT6QuKyTBYCAITYGzTkmTM3qln7Qhsm` | 11.2 |
| Homework 7 | `1xosxf6PAVy4GwfN-PXRb5KcJVY9z63CW` | 2.7 | `1Rg2XpxdXwEdO4NMgXj5HFnIm_gFv7IKF` | 18.5 |
| Test | `1V1W1MvvQOc0Lc6cHz1l48W43leo-xDG6` | 5.5 | `10a77ltPXbr9-gmM14bXQR490LjXgF3aa` | 19.3 |

Файлов 18 (9 pdf + 9 txt). Пропусков в нумерации нет, тест на месте. Домашек **семь**, «Homework 1» разложена на два файла — это один урок. Тест больше 4 МБ.

## Unit 7 — папка `1k7PkgumIUawHajjvV7Q-WSo2IAu3WOPg`

| Файл | pdf | МБ | txt | КБ |
|---|---|---|---|---|
| Homework 1 (1) | `1BI9mvqqcKx_yfqNbHu1W9mc-i61qovCa` | 0.8 | `1Ta4aSoTAPoczQbPyCi2MbDY9f7UqtWUs` | 4.5 |
| Homework 1 (2) | `1AFDlc3jbNu-7pQHKdfLDmSjjXcmUzTWI` | 1.5 | `1Uyncb2wjEiI2EG7gJFZRzkJg0lpcD4So` | 8.4 |
| Homework 2 | `1ad-PFe8RY6Ox9BRYUyvivzoN2t8iiPw5` | 2.1 | `1C083LWytIkcYv4QIGV0Tte3_5qfAL35W` | 15.2 |
| Homework 3 | `1GATlftfCunhfuE0Pabi0bMHZR3waXux0` | 3.3 | `1LjXNMpOqrBOFKZSH8zW2m-bpn98Ve9CR` | 16.9 |
| Homework 4 | `1ObRz9rxlYGozsBxVnp3JzylrZVGf09bt` | 2.3 | `1PjJN4QSr4Xb3dW11TIH1KIzxr95vk4Em` | 10.4 |
| Homework 5 (1) | `1izTNH9iwMVebIXfoSQplZhIkSUSXEaFE` | 0.8 | `1-vE-suaYAIl4SBT-QIkWAYZIb4J6SNwg` | 3.1 |
| Homework 5 (2) | `1fZ48jTrPzOlT9e0eRcBaNK79nkqZXrOc` | 3.1 | `1aO_V4lOTtyN3GR7mtjrk8Qbmwu_PlJkt` | 13.3 |
| Homework 6 | `1y4qLZmUd3V4HyBdHKwNH2QCv8XgpE5lU` | 2.1 | `11ECV2QpFn5BDGsh6rwkOb3A9WuFsIPnY` | 13.0 |
| Homework 7 | `12fD0til6yFN3XfQGxNFYpod49rGLz4NK` | 1.5 | `18uknfrpwwA_Xrx2TEQbauW7QN3ERL21O` | 10.3 |
| Test | `12ix54BLdPaKstDl0DIz7OiFQOKE8vzzR` | 5.1 | `1xpbR0MO2iv0e8bKetF2WKq4z6AieyWQ6` | 23.1 |

Файлов 20 (10 pdf + 10 txt). Пропусков в нумерации нет, тест на месте. Домашек **семь**, «Homework 1» и «Homework 5» разложены на два файла — каждая один урок. Тест больше 4 МБ.

## Unit 8 — папка `1nThPMetLmxmljo4LDaT-0wiWLsVtcPFK`

| Файл | pdf | МБ | txt | КБ |
|---|---|---|---|---|
| Homework 1 (1) | `1wE9v4V8Ms3hzanDOJsWVHnrR8tWOEPdc` | 0.8 | `1K2NuA28A8kudmP2MDYGYoHjPv8Z1LZZx` | 4.0 |
| Homework 1 (2) | `1O82Dc-G_IfkZfcVzDKrbCSDUfARAVUFl` | 2.7 | `16MV1oWERsq7k1hzZHXFZlrdboDwnw0i7` | 18.0 |
| Homework 2 | `1E2c71N4ednbJKC26iQkT229i6jY3zqau` | 2.4 | `1reumZ2YYNDHbjS0iysmV7inEgBMu8R_3` | 20.0 |
| Homework 3 | `1gxgr9_WdGk2vTOMnxFWJp_HFFUDwpH0G` | 2.1 | `1w0m1TOnGYweTKLieOibAz07VseQ3tP5F` | 18.3 |
| Homework 4 | `1QEA0AmvB2mtikEmt1fBPkj5PLGL1yKp1` | 2.4 | `1WzagAbk6Hhh9c85nDqrlJA1NSimZ_Q_0` | 15.1 |
| Homework 5 | `198m_MX7Os8IYBAs8ZHN1dhPEcXfaZx7m` | 1.9 | `1GWccM9GdrsLPcgqksZ56SF93xKbLpWQE` | 11.7 |
| Homework 6 | `1G5i_nMBcTqfbqLi8R0QLh8Uyz8c6T4z1` | 1.6 | `1x5TZYhxlWmEaYUoljR8lS45RVQAkV_1Y` | 11.6 |
| Homework 7 | `1tHdjA2L5EDB6AEthsoMH0dk-9UBzM79f` | 1.8 | `1pm7ETbOKbI9DX6_7Tj373-NeO00Ypq9i` | 13.3 |
| Test | `17F6a_uyfbmDG9QTnhWDCFZQ9ubDJF-vm` | 1.9 | `1BnlAuqUXPBV64N7dDj6wdQ0o1N9sJXGk` | 19.7 |

Файлов 18 (9 pdf + 9 txt). Пропусков в нумерации нет, тест на месте. Домашек **семь**, «Homework 1» разложена на два файла — это один урок. Тест называется иначе, чем в других юнитах: `GG1 Unit 8 Test`, а не `Go Getter 1 Unit 8 Test`.

## Final Test — во вложенной папке GG1

| Файл | pdf | МБ | txt | КБ |
|---|---|---|---|---|
| Go Getter 1 Final Test | `1jQdOqph9szCvtJf1gHh_NmPaFp-xIc5c` | 3.2 | `1AuyesYZ_MsOPYD8iFhzQd0zAxS67y7VY` | 26.8 |

Отдельной папки нет — файлы лежат рядом с папками юнитов. Скачивается коннектором
(меньше 4 МБ). Заливать, как у SM3, отдельным юнитом `Final Test`.

## Итого

* PDF — **87**, `.txt` — **87** (9 юнитов + финальный тест), у каждого PDF есть
  `.txt` того же имени. Прочего нет — `.DS_Store` из Unit 2 после перезаливки пропал.
* Состав файлов тот же, что в первой заливке: ни одно задание не пропало и не добавилось.
* Уроков-домашек — 3 (Unit 0) + 7 × 8 = **59**, тестов юнитов — 9, плюс финальный.
* Пропусков в нумерации нет ни в одном юните.
* Домашек на три файла — две: Unit 3 HW1 и Unit 4 HW1.
* Все PDF вместе — 185 МБ (было около 2.1 ГБ), `.txt` — 1052 КБ.
* Самый большой файл — Unit 6 Test, 5.5 МБ; самый маленький — Unit 7 Homework 5 (1), 0.75 МБ.
  Больше 4 МБ — 8 файлов: тесты Unit 1–7 и Unit 6 Homework 3 (см. выше).
