# Super Minds 3 — файлы выгрузки в Google Drive

Чтобы не искать заново: поиск по Drive стоит дорого, а `search_files` не умеет
`in parents`. У каждой домашки два файла одного имени — `.txt` (только текст) и
`.pdf` (в нём картинки заданий, достаются `tools/sm3_pdf_frames.py`).

Поиск, который работает: `fullText contains 'SM3 Unit 2 Homework 4'`.

## Unit 1 — папка `11n9OUJMZNylYTw74P4QJJk6cruf4JFKV` ✅ залит

| Файл | txt |
|---|---|
| Homework 1 (1) · словарь | `178hOyC3IK8Qjknk2SvEdANsUBejrYsy-` |
| Homework 1 (2) | `17x_mVPjZHTXFJE0IQaUozs6aHw494Hsa` |
| Homework 2 | `1k9g5MA2r8M5EjgSQxCgzzJ_8LpG9znEW` |
| Homework 3 | `1IoS0-TAvyIPnZUbMM9QFOx7z-6YT15xt` |
| Homework 4 | `16AjS9QKGZ8UNiwELAPchmNScd76xmhmZ` |
| Homework 5 | `1NFE-L6_jNB3TS3TtBmfZxRUrcmjE1Xdm` |
| Homework 6 | `1co0_YVGoaIDTCwAkVD2YExN88KPTWZxK` |
| Homework 7 (1) | `1YH4olyXhVmcYUB2ZLkDgQkwbVN3exIpq` |
| Homework 7 (2) | `1kzDfHWgliHulcqnLf8rWpQRbjMMmgK1l` |
| Test | `1JlLOeWomzD4HV70Uw1vLsU9alTPVr0a0` |

PDF, из которых взяты картинки: Homework 3 `12_FtdN0ZIyafQtH0Sf_QZ2-KsHvDzbqQ`,
Homework 4 `1GSocFgnMcf3XW_wHm1X_mXRR850HL2vP`,
Homework 5 `1iOYzTL0mcZWU1mH9hh46rHG_BSfvjD_y`,
Homework 6 `1X0GDg6o-GzIU0dlFCPbkUK1QTv4ro6C2`.

## Unit 2 — папка `1_GoOaodMZcLU7Lax3PABDykuVBw8RK9K`

| Файл | txt | pdf |
|---|---|---|
| Homework 1 (1) · словарь | `1rQhzgi58jgE2lP2nRR_K1yS974X519TU` | |
| Homework 1 (2) | `1Z7slVIbF7NPCW8hPWme5g7ifGhsfecs7` | |
| Homework 2 (1) | `1q-Z4Ot6CW2eKJaBlpCwLdY1EdiL5Vtz_` | `1lraoHVDa_2TzCTYoYKPoiqwn71w1rlPo` |
| Homework 2 (2) | `1Cq-IUPCvIDhzZZRymU4DDI1Lmyq_dARi` | |
| Homework 3 | `1YTZiW9bSIr7BLeaYb_BraMWbPzBCmLEb` | |
| Homework 4 | `1A-mrWo-DhtAN_Gr7We-GONCxz0GXCN9c` | `1N_0iHdaYMMberiLNcL2EIHGS-2Rm6LIL` |
| Homework 5 | `1QWJzrjcjWwRCVNjbVAerfEnE3U0odc45` | `1SDu2Zqln8HYz6AtGwfsAhC3uSoavR6jf` |
| Homework 6 | `1IKX2kB-WVSSLu7BnYXfBnIC1Pvm66eTz` | `1c42cj7AQT8jgk-HEnSKvAg7LxPBNEo0i` |
| Homework 7 | `10bCb9xcwCdw9BXCEKucLzieuY4Dp7IaO` | `11nMEf720mrPUlK1iwl7DXKbt_vEdHWSa` |
| Test | `1n2UkVe9HfNSe7Dz_Iu85yQoru1guIQ4t` | `1jSknYsBD1U-7jM43Geh30LOcHL_oCZLt` |

Остальные PDF Unit 2: Homework 1 (1) `1qqEkKTb0Irz0LmZuQTClKn5rrLc-gxfG`,
Homework 1 (2) `10KelPFPOV_o-ODoZBBASan3IU0XxEZH0`,
Homework 2 (2) `1X77Twe5fQZL8X6C6kC1Q6YQqEpKx1Q3d`,
Homework 3 `13taPLa_A8bQPLktY_WuFlL1ikqz1mNth`.

## Как искать файлы остальных юнитов

`parentId` в `search_files` **работает** (раньше я считал, что нет). Весь юнит
одним запросом, с `excludeContentSnippets: true` и `pageSize: 60`, ответ в двух
страницах — `nextPageToken` обязателен, иначе половина файлов не видна:

```
parentId = '<id папки юнита>'
```

Папка SM3 целиком — `parentId = '1i0n65ZsCIE7O5kKzx8kF19IvdwNWrCye'` (в ней
папки `Unit 1`…`Unit 9`, `Final Test` и учебник `SB.pdf`, 182 МБ — через
коннектор не скачивается, предел 10 МБ).

| Юнит | id папки |
|---|---|
| Unit 1 | `11n9OUJMZNylYTw74P4QJJk6cruf4JFKV` |
| Unit 2 | `1_GoOaodMZcLU7Lax3PABDykuVBw8RK9K` |
| Unit 3 | `19w2ygZLlyq4eZd6A8J6oUxW36ZoAUFc8` |
| Unit 4 | `18ryKOtfb9FFAufOxtCoqF2ZfMRezqN69` |
| Unit 5 | `1SQ5g-yNDrL6y6np6rSwup6SKsCju0lbQ` |
| Unit 6 | `1mINuJdaEmlo-nHZ7Y2F3SvAqQf2ClFet` |
| Unit 7 | `14de98KcGvlhB08-2Pzu7X0Y7uw-eDTUp` |
| Unit 8 | `19PXVjf3Vkst9l9a9tcEBXxZYP1Lj6YnO` |
| Unit 9 | `1w1Xs41E-PKy1_NL1xa_72TBoUMGntPXD` |
| Final Test | `1REKAMJPUXek1tKnQ7jY_UraULwv9igPp` |

## Unit 3 — папка `19w2ygZLlyq4eZd6A8J6oUxW36ZoAUFc8`

| Файл | txt | pdf |
|---|---|---|
| Homework 1 (1) | `1eP0oiLP8bUd4qNoHDhADUnfqKzLgvSmM` | `1BfQBVS8mIgykYhRkTMbFqX9GGvbDuKFa` |
| Homework 1 (2) | `1w3qZSg4g8dyRPnF0ugc5Xd9cT_-otBcs` | `1E3Y7fnpS91VWR_s13C1OV0KG-MafTkNC` |
| Homework 2 | `1dAd4uSK78zEblht7PbtBpP7SVo0aVzQ3` | `1wRT1N2msWhDSKQe5BLoweDv6hStC_4mE` |
| Homework 3 | `1B3xuSbpp0f_8KamK_83qWUwOIf0mpEn6` | `1Z0s2vMGfMolgUKKh6daQF4u-tNaGnO4W` |
| Homework 4 (1) | `1k0hTaeRPFLfjJE3iFHHQI00F63ck_GLS` | `10gdVMy2Pq0f72dfae07FjQi36Hmcy6Lh` |
| Homework 4 (2) | `1hZpb7MqoyoZZ8DMD6RqbmtFdpnGi-t-H` | `1Z2GFSwAuaKl501D2nb9KE0JITR1WUn7A` |
| Homework 5 | `1eeRrFgCqU2CC5yuuX-nsc-7dtETTY_U2` | `1-I_BD2uaTcU42vLqS82y6i43FmOSJQiU` |
| Homework 6 | `15dBF-86diN1brSSR85KZ4nGBIe-rAtTZ` | `1dcnhZgcGqDNnRXsIdHuuVYD6VPjxlN1d` |
| Homework 7 (1) | `1GoBER6CfVsx039Yux4bJOCPid5Gk3S6G` | `1L4vLuGqbDnPePwN07vVxhVn-o1LY4afK` |
| Homework 7 (2) | `1R3HH_SK_4D4w-nPnSc0sklDO2VAWA76Z` | `1FJwz4fOfld7evwLMEqlIWvlby8PS8hIX` |
| Test | `1f3D2EyLGNhu8SDxEStrU6tf8f34j87mh` | `1sSJ2Lyo0UvyaCSqzNedalCQodhU_ponK` |

Пары «(1)» и «(2)» — это **одна** домашка, залитая одним уроком.
