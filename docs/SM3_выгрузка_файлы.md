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

## Unit 4 — папка `18ryKOtfb9FFAufOxtCoqF2ZfMRezqN69`

| Файл | txt | pdf |
|---|---|---|
| Homework 1 | `1J30eCxTgmKS78Z5Bg1pZUX7wVL4JsdnA` | `1s8R4KIVdAuKAKjl1_5AskZlhNHRJO2ce` |
| Homework 2 | `1Ac49uux_FZ8LBR3nFMsk8xGd8vjBtKqJ` | `1GnWYA0g9w_yx4jKFR3YBklf_CFtq7sCd` |
| Homework 3 | `1jdmxz_5mIuX2rBbRWTCgeI3HY-T6nnrO` | `1W5Nbi8sUgLXMfSSetPN8R93Bs9hW8I_Z` |
| Homework 4 | `1A5BjmZp1WV7NtGgClO5mtYG6aA3K4Gdw` | `1rZQQ7oZgePA9JpQiurMMDpQXFP_fNcO8` |
| Homework 5 | `1kUKFmJ3_COUAhyPjii-5Db_R2djjw7jc` | `1w9ixn2VC1UkW48GWSOd9YkQVi7Ic4Ywv` |
| Homework 6 | `1ZT1gFwM18r4efBulIsgO8O6ECM3b-VK0` | `1i3Le8bBP9VF6ijVoMfbCqoGH6eYJGSFX` |
| Homework 7 (1) | `1DJtGtraKXCe3ebF_E-hBWd4FQo5V0joC` | `1i0bVBA3Gv49VvIvFgspsVSFvSvXh6KhD` |
| Homework 7 (2) | `1_r50kv9sPXI5cxfSJRrU-aUYXkU7XECJ` | `17BKYJ5YWwHPGJ5-Qg1f99jAIvg3hl1yi` |
| Test | `1UuR4On0ybV_qY_UmGIMHBVoaJ7PQ8s2r` | `1NZnACkpr01uoxe-eQ6P4zfe2HyqV5nau` |

## Unit 5 — папка `1SQ5g-yNDrL6y6np6rSwup6SKsCju0lbQ`

| Файл | txt | pdf |
|---|---|---|
| Homework 1 | `1e-OHNt8_47j_CJd6vB0TKH0B8C7RwsfM` | `1hWaaHPbwEooyIa0nnUzZG88T2rtuSDa1` |
| Homework 2 (1) | `1Jh4gHJV6xgg3UvLRkWqVfZDYBCw7sMXD` | `1s-EI2ogsT0CumuXK0VUzYEAjzdKma8Yn` |
| Homework 2 (2) | `1qqVP1oqCb982Jx0GxHVEAeX9SKt3zwTG` | `1TW7dpKIq1BwLyeGWiSDMOd00rxKUYU5J` |
| Homework 3 | `1Yz_rqu5vrS_LUOIQgEQ328G58W7A68ah` | `1l4eS-XhmPv85QHacN8aXfailr_Cvm7qV` |
| Homework 4 | `1IH2j8fr8Wc-Rf4be1bOUrg0uCPoXPzX6` | `1akWMbi6gkihPpD2iCA-Gxi_typ8K4uPf` |
| Homework 5 | `1gnQ7xryBtZh4Q14qKIfxzkrri_q80_vk` | `1VWNFMUnthpVfuDaHYVtbNKAcz2OQwoCj` |
| Homework 6 | `19WNaY0ZsXDSVgkSpNd8G90v0dfvG7_D1` | `1ZaJoO478FMJCzUkYbATrg_tCjYdnuOts` |
| Homework 7 | `1T0CT5x8P2-YbBJHZGDTvCyPOaanG_3dr` | `1EHZpkjO8CmVU7NTgwIEJHr5TYmJYX9zO` |
| Homework 8 | `1BZSqhyc2zCOZDW-k6d0ygauy6OU4AziK` | `1HdEXAijlHy0sZTeLEg_JzXBhVT5lejE4` |
| Test | `1Iax_SIpthbr5MGXJkR7ZTipxe92_OdKZ` | `1ZZeS_9ISmsb1FvK94rPVhbOIEwp5BA3c` |

В Unit 5 домашек **восемь**, а «Homework 2» разложена на два файла — это
один урок.

## Unit 6 — папка `1mINuJdaEmlo-nHZ7Y2F3SvAqQf2ClFet`

| Файл | txt | pdf |
|---|---|---|
| Homework 1 (1) | `18x2A-xc2BJugAuTVKKe6gqNkqOcc0rO0` | `1Vn0Vi12v6o4q-s0alkJWCQyGt3j-RUw_` |
| Homework 1 (2) | `1qxfdjuj4tFCJqb2IoB73KoF-xyqOTO7w` | `12DcSxjOPWfKTZdHmWvmvjkA1RuSQ-XIb` |
| Homework 2 | `1SstfWInRXP9EIwFNv7LDx8wu8uLC0bHS` | `1TCfRJMLrYbyNhKAjbfsmlq7rZTVnt86Y` |
| Homework 3 | `1Wnj-7iqKOvILkt9ZeRYMMxMwoxrUWYMN` | `1DPI6An_yFQQv9nSxcUs3BUKA4X9sSnsM` |
| Homework 4 | `1U_vGQYi_R5_Sgeo6OszveCOfXN9SQ7q8` | `1-tG40dWV7H3mlBAX3c3JoFjnT05VGxGs` |
| Homework 5 | `1HvkJEbR17SBHj9KDr4sf2lhzGEHdg6rb` | `12FruUMk-LCPDeZwvTOEYzum11x-oxyM3` |
| Homework 6 | `1PFuU8nvrHMdA9lXaO2mn3nvaBCcJNH4x` | `1N4B4eRezI5htHk5Df6g9GSj8zsneocZ7` |
| Homework 7 | `1XD_PfZLTS-7nuW1w5lsMHUgk1zZl9Iqs` | `1TMt1UTxH8TdbvZ3JMsL77L_VditU0KQU` |
| Homework 8 | `1RZAmJEFhzxFiBawB9NUVBXoLMfrCaS8X` | `1AcVC7ExsKvwLPurJtT-RMBkJFjO2_8up` |
| Test | `1HmJ7ChZ5h-x5yZVLMCGbnZxmKpUtP8ok` | `12tiBHHh8mpsYTGTr4pkKC1Rvaj2aCJgm` |

Домашек **восемь**, «Homework 1» разложена на два файла — это один урок.
