# Go Getter 1 — файлы выгрузки в Google Drive

Чтобы не искать заново: поиск по Drive стоит дорого. В отличие от SM3, в выгрузке
GG1 **только PDF — файлов `.txt` нет ни в одном юните**. Текст заданий придётся
снимать с самого PDF (текстовый слой через `read_file_content` или pymupdf),
картинки — оттуда же.

Опись снята 05.10.2026 запросом `parentId = '<id папки>'` с
`excludeContentSnippets: true`. ⚠️ Ответ приходит страницами по 4–8 файлов,
**сколько бы ни стояло в `pageSize`** — идти по `nextPageToken`, пока он не
пропадёт, иначе половина юнита не видна. Подпапок внутри юнитов нет.

⚠️ **PDF тяжёлые: 22–35 МБ**, кроме трёх тестов (Unit 7, Unit 8, Final Test).
Через `download_file_content` такие не скачиваются — предел коннектора 10 МБ,
а на SM3 сервер Drive падал уже на 10 МБ («message too large»). План: текстовый
слой через `read_file_content`, картинки — искать другой путь.

Выгрузка — из **ShkolaApp**, не «Взнания». Текстовый слой хороший: задания,
слова «Составь предложение», пары, пропуски читаются. **У игр Wordwall в конце
текста есть ссылки** `wordwall.net/resource/…?wwmethod=embed` — в отличие от SM3.
Чего в тексте нет: какой вариант «Верно / неверно» отмечен и сами картинки.

Папка GG1 целиком — `parentId = '1n5SD_jhJuy4QwL7RefvpsRAKK86EppSy'` (в ней
папки `Unit 0`…`Unit 8` и файл финального теста, отдельной папки у него нет).

| Юнит | id папки |
|---|---|
| Unit 0 | `1aWqaqe7cLhep35PwpjCu0yY3B_2nLcqm` |
| Unit 1 | `1e-ztD5CHTgGCLmEdQFKCqRhobs01QrvB` |
| Unit 2 | `1CKJNXjjaPpA4FbXF0HillESvZbftLO-E` |
| Unit 3 | `1XNFlph2wBYg6FV2YnKin5VqiK3_W_WJg` |
| Unit 4 | `171osxdB1ook1uTXpvX8yXKmHzxar-B-d` |
| Unit 5 | `1zTWKdeiGixSGVlRTy6pWRSZEtURqcgtR` |
| Unit 6 | `1_qd1J3C4c7mMsaXt-bVcgG6rdbErI9Sr` |
| Unit 7 | `1wTRU4fT2KGfciBWDx3WH2800asr91YqK` |
| Unit 8 | `1pbQSK9YdIBJN_80Ub7GfdvaVtqbo9nHP` |

Тип у всех файлов ниже — `application/pdf`, размер в МБ (10⁶ байт).

## Unit 0 — папка `1aWqaqe7cLhep35PwpjCu0yY3B_2nLcqm`

| Файл | pdf | МБ |
|---|---|---|
| Homework 1 | `150WpDU7g-yuxEbI57P4jPnvjYSwiJUvW` | 24.1 |
| Homework 2 (1) | `1V0QG1kEkpre_9Geh7koy6o9_IKppaP5g` | 22.8 |
| Homework 2 (2) | `12Jh-um2gw93XqlG7Oy3_yL6GHpEmEeHv` | 31.9 |
| Homework 3 (1) | `1AjFA4BW3iVjUUo5Us9xDv1iSpAur7ifc` | 22.8 |
| Homework 3 (2) | `1VTKdLrdTwMI5mbQ_dUURHBXzv8I_iG6J` | 24.6 |
| Test | `1yj6XAL1x6FbmY64DHBnm9lY2EYEyjn_T` | 25.0 |

Файлов 6. Пропусков в нумерации нет, тест на месте. Домашек **три**: «Homework 2» и «Homework 3» разложены на два файла — каждая один урок. Нумерация идёт подряд 1–3 и на этом кончается; что юнит вводный и домашек в нём просто меньше — предположение, содержимое не открывалось.

## Unit 1 — папка `1e-ztD5CHTgGCLmEdQFKCqRhobs01QrvB`

| Файл | pdf | МБ |
|---|---|---|
| Homework 1 (1) | `1psugH3d8vT14NMUlN84RxJHDVG47kied` | 22.8 |
| Homework 1 (2) | `18aYS8nGBlKeII4yHggPxNm_r1sTGqPVF` | 26.9 |
| Homework 2 | `10Hijred6YSY2PZGvSfXyBQnOkrZwnVnr` | 24.2 |
| Homework 3 | `18vJZgB_WX1tydmiUlMn5hdyKiZl5CQED` | 25.2 |
| Homework 4 | `1rrKI-NvjuYvn621eovUoXOVvgVWdLD-2` | 25.8 |
| Homework 5 | `1tkC4EEj-W7bePbYifB2ECs91BNfNh3Sd` | 23.7 |
| Homework 6 | `1yirB_ZdWD7kF3LaKYQ6K9VMY7wSAgxcw` | 25.9 |
| Homework 7 | `1U77w-N9gpm4fXJ4SXhxsOHULw97wNsrs` | 28.1 |
| Test | `1dPEUmEuUND5yhGbWuqPAKJ4T4JayYLzo` | 27.7 |

Файлов 9. Пропусков в нумерации нет, тест на месте. Домашек **семь**, «Homework 1» разложена на два файла — это один урок.

## Unit 2 — папка `1CKJNXjjaPpA4FbXF0HillESvZbftLO-E`

| Файл | pdf | МБ |
|---|---|---|
| Homework 1 (1) | `1S7wes-utrDoJNcZS02RiuSW32yvLLUtV` | 22.8 |
| Homework 1 (2) | `1ldzoUyxcuTCcT-JHh3HU5Xw0vahjbZTY` | 24.1 |
| Homework 2 (1) | `1WUozHVQgRqmqKEEN12FWvjFrmC--rcsr` | 22.8 |
| Homework 2 (2) | `1UVMNQ7SLXVaQcgvgnc08ACIFkmym_UkG` | 24.4 |
| Homework 3 | `1Eku2vDhVlGkAusfh4vTm1ESi9FleAkmS` | 24.3 |
| Homework 4 | `1R6aI1UzL8IuLiEmy1p8lJA-zdRSu6QEY` | 25.4 |
| Homework 5 | `1woKGhCBtYGcRTLMLBsNoRft91qvWEGu-` | 25.2 |
| Homework 6 | `1_oDspRcftPBpAsCmE0qFWXwG9Vp_I9ta` | 23.7 |
| Homework 7 | `1_tT7Q4TDpI3kehNFd27s_csg1wExfdT-` | 25.1 |
| Test | `1-aYpaGW80VjbLkGAVYg8iCesU-M9QON5` | 27.3 |

Файлов 10 (+ `.DS_Store`). Пропусков в нумерации нет, тест на месте. Домашек **семь**, «Homework 1» и «Homework 2» разложены на два файла — каждая один урок.

⚠️ В папке лежит ещё мусорный `.DS_Store` (`1UA_u2VnDw_Ys4M0g5SShHKkoLmB8Fskw`, 6 КБ, `application/octet-stream`) — служебный файл macOS, к выгрузке отношения не имеет.

## Unit 3 — папка `1XNFlph2wBYg6FV2YnKin5VqiK3_W_WJg`

| Файл | pdf | МБ |
|---|---|---|
| Homework 1 (1) | `1LctSeGB-djiBIANr2VKZI3OiClTfmJVz` | 22.8 |
| Homework 1 (2) | `1Ls-Fcl5mvZCgb4mfjcJYvdA9BRyp-Lmr` | 22.8 |
| Homework 1 (3) | `1vBbONRfTSXJC52V4agHwpoAxOWdonxbR` | 24.9 |
| Homework 2 (1) | `1C-zhY8Hs_GoLeGEYbmVyz_VjHHTORUFs` | 23.7 |
| Homework 2 (2) | `1sHG3C_Owfe3q1tddaUc_30PHd9VvK_Op` | 25.4 |
| Homework 3 (1) | `1JjYBjlssOI-r6IysRJcMMVZ45v7b6fwJ` | 24.3 |
| Homework 3 (2) | `1DchOccuGPuGi4wKyccXpDWnt-fUlCBZH` | 24.5 |
| Homework 4 | `1U6Wck3PtRZzrkoV83fTuNyH3iJn9Olzp` | 24.6 |
| Homework 5 (1) | `1hku4vvbUphZXjgYCI0iRg5_TFLbOjnnl` | 22.8 |
| Homework 5 (2) | `1-_hpQfGPuehfH3-ovHQQsibu2-BfJPr9` | 24.6 |
| Homework 6 | `130FypVNegOT-pOsvRICwMAmEY9LZOg4d` | 23.8 |
| Homework 7 | `1xI75nuNfUD1j4D5PfsjsnQ1bXoEnwUp7` | 25.3 |
| Test | `11TfuQTvIvNCS5L2q4P7pU9c4CS_02pEe` | 28.0 |

Файлов 13. Пропусков в нумерации нет, тест на месте. Домашек **семь**. ⚠️ «Homework 1» разложена на **три** файла — (1), (2), (3); в SM3 такого не было. «Homework 2», «Homework 3» и «Homework 5» — на два. Каждая — один урок, блоки подряд.

## Unit 4 — папка `171osxdB1ook1uTXpvX8yXKmHzxar-B-d`

| Файл | pdf | МБ |
|---|---|---|
| Homework 1 (1) | `1Xej1qp3BX8tU112ojF5MlvyIswMOkehA` | 22.8 |
| Homework 1 (2) | `1PQGBR5m96H7KeVGT_TQ-XzEoxtW6fRrL` | 22.8 |
| Homework 1 (3) | `1wdltB-Krdyc5rU13Qr1gHXP13u6X5q1S` | 24.8 |
| Homework 2 (1) | `1ctAz7csL0q5zIH2vHzz66belygdrGOI0` | 22.8 |
| Homework 2 (2) | `1PhGgaPwPtvi5PK91o12l1VUXQryUMXd3` | 24.4 |
| Homework 3 | `1Xt4fndeunBdRwLR445-29ORuG4UryPDf` | 25.3 |
| Homework 4 | `1o4iD2186xW4d4fg7LQ8zr5ANNnH2h65y` | 26.7 |
| Homework 5 | `1mSP_5fZRrEMdsSXEn7yn64qTuRnxCQoB` | 27.1 |
| Homework 6 | `1UIW_Md7gV0CYUCEo4k2K_H8CG8o7GnKz` | 25.1 |
| Homework 7 | `1h42yv6UdyuA5gc79lZACXaWfsdWsztA6` | 29.7 |
| Test | `1GKiFGl8iyIYu5asJggj6YBMs6blajbSg` | 34.1 |

Файлов 11. Пропусков в нумерации нет, тест на месте. Домашек **семь**. ⚠️ «Homework 1» разложена на **три** файла — (1), (2), (3). «Homework 2» — на два. Каждая — один урок.

## Unit 5 — папка `1zTWKdeiGixSGVlRTy6pWRSZEtURqcgtR`

| Файл | pdf | МБ |
|---|---|---|
| Homework 1 (1) | `1Gm8S_u3FAPCxxxl051sTvJOkUyAIVAJr` | 22.8 |
| Homework 1 (2) | `1fZKIRp2N9XoUtlLlcf-3B7zR5-chjVRq` | 24.4 |
| Homework 2 | `19Ea5UUk83RnHJcPl9-BtDODUArvctF7Q` | 24.7 |
| Homework 3 | `1hG2lkAiTKWCBel93J2VoTGb_y3hqBQal` | 25.4 |
| Homework 4 | `1OYsfh4CzkaYK3ooPvXsgLZneCC7jCP7Y` | 24.3 |
| Homework 5 | `1YFL3_hhHVhG9zUSq--IayYT8_vF4o4bb` | 25.7 |
| Homework 6 | `17iAGEAnb4WyjZdXzLAqWlwzjF4iE9Isq` | 25.0 |
| Homework 7 | `1104toTOiOOnVNE2qNiw6YadGgvEihz7v` | 24.1 |
| Test | `1IzY7U0LhZ5O3lWA8ysbYK4tADUtTWji9` | 34.6 |

Файлов 9. Пропусков в нумерации нет, тест на месте. Домашек **семь**, «Homework 1» разложена на два файла — это один урок.

## Unit 6 — папка `1_qd1J3C4c7mMsaXt-bVcgG6rdbErI9Sr`

| Файл | pdf | МБ |
|---|---|---|
| Homework 1 (1) | `1pPecyqmQQ-AHTv2RYglV6-TUYHFas89I` | 22.8 |
| Homework 1 (2) | `1NeceAvQhcRwaRdMvho2XQbkxch_6c828` | 25.6 |
| Homework 2 | `1-WrIsRGQBAQX68jRsX4Hf_hV2f_6UIiw` | 24.8 |
| Homework 3 | `1ZnyNVcjMpey3vG0dzgEwJf9zzHEogO0E` | 27.3 |
| Homework 4 | `1Tdy0VwucOZydsp4kI7IEN1YjfjSd9Zqz` | 24.7 |
| Homework 5 | `1j71qDZf4EDh9JajVXWMzSdEjz2gr7rqx` | 32.1 |
| Homework 6 | `1D-L7ROwRshQUwnMCc-iOIEtLcmMMGNnI` | 24.3 |
| Homework 7 | `1WsG6CTD9pzhF2o-95Q1GZtb8inbJFNaZ` | 25.6 |
| Test | `1cHTFJXaCbwrgUN1S7iXWcmZGqrksCxTe` | 27.8 |

Файлов 9. Пропусков в нумерации нет, тест на месте. Домашек **семь**, «Homework 1» разложена на два файла — это один урок.

## Unit 7 — папка `1wTRU4fT2KGfciBWDx3WH2800asr91YqK`

| Файл | pdf | МБ |
|---|---|---|
| Homework 1 (1) | `13-xyT3W3N79LlxAMruxniA6gG6rVqoHT` | 22.8 |
| Homework 1 (2) | `1_aIcqiGYdvA1zvwd3eUlMY00UYj6poLY` | 27.9 |
| Homework 2 | `1YQnxo8BA0rbQE7mvopHW6Q2lXgaHBWtF` | 25.3 |
| Homework 3 | `1QkDF8iEMpumSChXQQIPLT09U5oZiaiqK` | 26.5 |
| Homework 4 | `16tYrQFifFetYUjw17HcsU8ry2vau86rs` | 24.4 |
| Homework 5 (1) | `1d1giiDZNPY5CnifmSZlz0mqP0n-28kH4` | 22.8 |
| Homework 5 (2) | `1lMTN8_BZYAkSO6i7YR6lHx-dalkuhomu` | 25.3 |
| Homework 6 | `1bJ-KRmW0jn7UyWW88z0HYGXYo4xTa0PY` | 24.2 |
| Homework 7 | `1ZtNoIVtpP0yCc5IHYd2I84PoSOPPjkOi` | 23.7 |
| Test | `10aSg853-Cl6i5ffL2M2aWTsZKaYVfaP2` | 5.3 |

Файлов 10. Пропусков в нумерации нет, тест на месте. Домашек **семь**, «Homework 1» и «Homework 5» разложены на два файла — каждая один урок. Тест заметно легче остальных (5.3 МБ) — скачивается коннектором.

## Unit 8 — папка `1pbQSK9YdIBJN_80Ub7GfdvaVtqbo9nHP`

| Файл | pdf | МБ |
|---|---|---|
| Homework 1 (1) | `1A-NO7kSuT3ecgln2QmMBqHbS4pRRd-xb` | 22.8 |
| Homework 1 (2) | `1W2R22MYiizvDKl4UcFRWkKeJ1f1sQcvr` | 24.9 |
| Homework 2 | `17FNEvxuh7Akub0d_CuLFvwlpY3unl3Tx` | 26.1 |
| Homework 3 | `1SXjpgzAi2GcxRudOqeX9T-oAQe532YWj` | 27.5 |
| Homework 4 | `1syJ-nq0KEp-IDcKx6UYyNjOiD4CBBAGC` | 31.8 |
| Homework 5 | `1bJqkYZHQULLt2ysMYeLcZlr0QDdjE4QT` | 28.8 |
| Homework 6 | `1L4l4aj8FjJDt-ili0zbWwOA10LABF9T5` | 25.5 |
| Homework 7 | `1xX8jHggfH2idwzrHlnfsqYupGVcBzmxZ` | 26.7 |
| Test | `11IoCU9Z3CgUH_YKOdNUHHPonQld-bNEi` | 2.1 |

Файлов 9. Пропусков в нумерации нет, тест на месте. Домашек **семь**, «Homework 1» разложена на два файла — это один урок. Тест называется иначе, чем в других юнитах: `GG1 Unit 8 Test.pdf`, а не `Go Getter 1 Unit 8 Test.pdf`; весит 2.1 МБ — скачивается коннектором.

## Final Test — в корне папки GG1

| Файл | pdf | МБ |
|---|---|---|
| Go Getter 1 Final Test | `1oE2mdOhoAB-eyA9_Ztp3RTQIb4xP1Ryh` | 3.5 |

Отдельной папки нет — файл лежит рядом с папками юнитов. Скачивается коннектором
(меньше 10 МБ). Заливать, как у SM3, отдельным юнитом `Final Test`.

## Итого

* PDF — **87** (9 юнитов + финальный тест), `.txt` — **ни одного**, прочее —
  только `.DS_Store` в Unit 2.
* Уроков-домашек — 3 (Unit 0) + 7 × 8 = **59**, тестов юнитов — 9, плюс финальный.
* Пропусков в нумерации нет ни в одном юните.
* Домашек на три файла — две: Unit 3 HW1 и Unit 4 HW1.
* Самый большой файл — Unit 5 Test, 34.6 МБ. Меньше 10 МБ только
  тесты Unit 7 (5.3), Unit 8 (2.1) и финальный (3.5).
