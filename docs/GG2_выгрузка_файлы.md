# Go Getter 2 — файлы выгрузки в Google Drive

Чтобы не искать заново: поиск по Drive стоит дорого. Опись снята 05.10.2026
запросом `parentId = '<id папки>'` с `excludeContentSnippets: true`.
⚠️ Ответ приходит страницами по 4–8 файлов, сколько бы ни стояло в `pageSize`, —
идти по `nextPageToken`, пока он не пропадёт.

Выгрузка — из **ShkolaApp**, как у GG1, но **у каждого файла есть пара `.txt` + `.pdf`**,
как у SM3. `.txt` даёт текст, `.pdf` — картинки и отметки верных ответов.
PDF лёгкие, от 0.3 до 6.9 МБ, тяжелее 4 МБ всего четыре файла.
Подпапок внутри юнитов нет.

Папка на общем диске — `GG2` `1JLkwfmzW4kJPTNUwm0rGSeVDVWXk1PI2`, в ней ещё одна
`GG2` — `1oGajObRStbbMjI2BK8TP48Gwo4UWXShI`. Во вложенной лежат папки
`Unit 0`…`Unit 8` и файлы финального теста (отдельной папки у него нет).

| Юнит | id папки |
|---|---|
| Unit 0 | `1J8IGB7gYcQPl-KPDlJ3obxdwDpsmSBDo` |
| Unit 1 | `1_VkFI3cmv9obPQra96t5B4KouQst6oMN` |
| Unit 2 | `13L5RMgp-w4AhNnno_V9lq785kvBTVcNv` |
| Unit 3 | `1zcSYne8JZgkufYRjqFJH-tNJCgl3jJDP` |
| Unit 4 | `1_wgy3Wbgs4WmHM2FbYdXszvBqMXruLLb` |
| Unit 5 | `1y5--EFvkGBjRwxR0K1_pJyOPpA4e9bMQ` |
| Unit 6 | `1u67bYSawIiCbOJmkmryN4WrDmPP-SZdd` |
| Unit 7 | `1kCTcKVNCHEPdwXJ5Q94PUDwgRt_S_Ilb` |
| Unit 8 | `1rIGMextg1UU3JXuQhjfwIyzxH9yQRI4m` |

## Сводка

| Юнит | Домашек | Тест | Замечания |
|---|---|---|---|
| Unit 0 | 0 | ✅ | только тест |
| Unit 1 | 7 | ✅ | |
| Unit 2 | 7 | ✅ | ⚠️ у Homework 3 только часть (1) |
| Unit 3 | 7 | ✅ | |
| Unit 4 | 7 | ✅ | |
| Unit 5 | 6 | ✅ | Homework 7 нет |
| Unit 6 | 6 | ✅ | Homework 7 нет |
| Unit 7 | 6 | ✅ прислан | в Drive вместо теста — копия теста Unit 8; настоящий — `docs/GG2_Unit_7_Test.pdf` |
| Unit 8 | 6 | ✅ | |
| Final Test | — | ✅ | в корне курса |

Итого 52 домашки (76 пар txt+pdf), 9 юнит-тестов и финальный тест — 174 файла в Drive и тест Unit 7 в репозитории.
«Homework N (1)/(2)/(3)» — один урок, разложенный на несколько файлов.

## Unit 0 — папка `1J8IGB7gYcQPl-KPDlJ3obxdwDpsmSBDo`

| Файл | txt | pdf | pdf, МБ |
|---|---|---|---|
| Test | `1Z_H5UqeMGyhGLRCLnihjjZY6EGg4g1CE` | `1_kpFwFLfr-P6Wc6a2-GZK2y9deUEHZEY` | 2.7 |

Файлов 2. **Домашек нет совсем — только тест.** Юнит вводный, `sort_order` юнитов начинаем с 0.

## Unit 1 — папка `1_VkFI3cmv9obPQra96t5B4KouQst6oMN`

| Файл | txt | pdf | pdf, МБ |
|---|---|---|---|
| Homework 1 (1) | `1g3pOJ2RUFNkDUW-Ua80VYP78pKVi5N6W` | `1Cww99iAt_3K1gr5OhdpokM_Y-kgkETq6` | 0.8 |
| Homework 1 (2) | `1zyuIwNjG3NlofwCMnZ6NtTquiI_79Zi7` | `1WxJIRuuWoqPF8l6ytMmJilmzo_Lm98Kz` | 0.8 |
| Homework 1 (3) | `1SYeus9zHxgYiQdpd9VlxxlQheAbJR3VY` | `1RLHi05E7zrRthhWlEiQ-3Zc9EbVaS7lV` | 2.1 |
| Homework 2 | `1LUcaVrBqIFS6EJO5xSiOP3uhkVHM89i_` | `1RgpT3WKkUl6YGB-wTwP2JAVqP5to5iIl` | 1.6 |
| Homework 3 | `1NkVRB_YxOmIcKUFIasvtV_xaCF4evcXe` | `1IG6Y-Ovh-7bAXCE25bnt4I5CdXbE9DEd` | 2.6 |
| Homework 4 | `1hDieTVTKr4pArUebQhhiL9DBkLOJFOIQ` | `1g4fOz9gib_rO7J2T3SyXO4zWW5NVBSCa` | 2.5 |
| Homework 5 (1) | `1Hdv9K8rfKOww_Yrsdab1mFwksm51xv8d` | `10FWGl7GEAWuMd2W--7AHfSvXlAWUslHd` | 0.8 |
| Homework 5 (2) | `1TP23-YF_Hd8xRSIjcbNe6hEeVPWBeEDR` | `1aGV3zS_xcqrDLX-s9CrjSa0jQk-O36rg` | 3.8 |
| Homework 6 | `1cDTPaKwegV4l2CItnneLWsxffv40SbUI` | `1Nx92iImVR2wG7cK4XjOR1upsYfOF2eZI` | 4.9 |
| Homework 7 | `1TvBp0OcmuOOxAql4xPNpctV6WwX_dX7U` | `1jVtQnvA4fBhiFVXcIEBZgHOBEJVAJwVw` | 3.3 |
| Test | `1Ep80LARqYQVkFIE8tQ1QRt-cRo9dDKY1` | `1HPAXjua5Ipw8Nr9l8jgokxlmjQO3u-bK` | 2.2 |

Файлов 22. Домашек **семь**: Homework 1 разложена на три файла, Homework 5 — на два; каждая один урок. Тест на месте.

## Unit 2 — папка `13L5RMgp-w4AhNnno_V9lq785kvBTVcNv`

| Файл | txt | pdf | pdf, МБ |
|---|---|---|---|
| Homework 1 (1) | `1VCmEHL_r9fDAEesek4T6ijwWxjqDZHsE` | `1kyW5FkfWvT1tuyxIUDmU9gtZ9vMaqjGk` | 0.8 |
| Homework 1 (2) | `1vpj9G4ABZo5hwtG0p7H6IvYykWaeFSdU` | `1O3dC2NhohKGpPQIM1_oHWmBIhi4qB3eC` | 1.8 |
| Homework 2 (1) | `1Gxg_blzbOed8McZTTZx2z3j5ZWXapcUD` | `1gTuSY6tK3o_FUyfkIienQvYWW_cOdrDb` | 0.8 |
| Homework 2 (2) | `1qEQ5ZDGLRxIBfNiW0NMoBnFKbYjXCou5` | `15cyyHdjHnX8H5gFDmDsJ6HayFmtS8aBQ` | 3.3 |
| Homework 3 (1) | `1WE6QQPfaxiWGH9nimgSJrWe2QkeymGjA` | `1C69VmDfL4JFVUJg-XOTcaFxURNqJn0bT` | 0.8 |
| Homework 4 | `12cLmmU9hIB7vwziZoCMcD6IzrEmMAJvv` | `1gQIimFwAiDI9VFbHuSzLgUbPX3N5fd5X` | 2.0 |
| Homework 5 | `15yhQ-DExouEey8ZkqSLKcPzx2NP5dgHy` | `1rUaXbwYL-CJAuN_Ja_dOhW29g22uWDpO` | 2.2 |
| Homework 6 | `1AmeFbCjqivQmcQezgMZnzetP6Tyyo4LV` | `1pUT_SpEke9HQXZQXmzTvZ2bL4Fz4pYq7` | 2.0 |
| Homework 7 | `1j68wqhO8kfuH4xBumJWY9LrY67anmr02` | `1k2UTg_pNoruEwpaeEJnw2KMWSUtEU_i9` | 2.5 |
| Test | `13jBmFrRUCuU7ezinNVr5mrkmH-DGH6IV` | `1Pfh1APMJzdblbYJJjZRyA5b3GlGwXTY_` | 2.1 |

Файлов 20. Домашек семь, Homework 1 и 2 — по два файла. ⚠️ **У Homework 3 есть только часть (1)**, маленькая (0.8 МБ, txt 4 КБ — как у прочих «(1)»). Части (2) в папке нет, хотя у соседних домашек с такой же короткой «(1)» она есть. Анна подтвердила: прислано всё как есть, домашку переносим из одной части. Тест на месте.

## Unit 3 — папка `1zcSYne8JZgkufYRjqFJH-tNJCgl3jJDP`

| Файл | txt | pdf | pdf, МБ |
|---|---|---|---|
| Homework 1 (1) | `1EJRa30uXUeEhEpiKabS3sUpBLI7EoTTO` | `16KlnfzMu32Jz8taN8158XxnpkT3jhL8e` | 0.8 |
| Homework 1 (2) | `1OWZgq38CrDjuvy99hngEZIItHiuumkVB` | `18_ZFWxrWrN_IY3vkvYVRcVwFL74F6rdf` | 0.8 |
| Homework 1 (3) | `1dWt9e4IBNQAmdOcVRY0GWAHagRbS622X` | `1PekVmYw60rprKnbLJEm9uCwOovvf9CMj` | 2.0 |
| Homework 2 | `18cezQ41yEOi_AZl6RwlqLySQ2QIgmwhY` | `1qRuIIt6wqz1AQGnprBJxKge89KlmnVBK` | 3.4 |
| Homework 3 | `1LGiFKaq3gXmNvwhTwwlMel9jyWirBo3M` | `11Eq1qU2dSM5Hnd32eChHBsHASijr5L-H` | 4.3 |
| Homework 4 | `1YK4FDXO0avJJ7Mo6mUCpUfjRuOE-4iXR` | `1oubDJ0locI0eYwLsIamgOinX6tCPyN93` | 2.9 |
| Homework 5 (1) | `1irfhBySNvXIHcdBQImRJy_vL7xuVlDvS` | `17VA_g29rhDoNTp9yNVPu4mLXXF5ztgHk` | 2.6 |
| Homework 5 (2) | `1iMmyH9B9iTqZbzyxRUtRgwieBFUuxrKV` | `1XRMy5OcHwNya3FPkioonPvnDbAeSaog9` | 1.5 |
| Homework 6 | `1Z8Zpvm3eackjpvl1AE_CnMyaO7GfxmpL` | `1GzFDw_QSVnqnbckkQgWrNndUie7uGoC_` | 2.8 |
| Homework 7 | `1W8ETaHX8HSxLQMgl2ctHMariGWUAaOE4` | `1qtadZXe7o8jB3KB_NbA10HUXVfIlUqTh` | 3.5 |
| Test | `19gL4HryvEzrudcBhkD_fOYJ7cR2V_qJd` | `1o9RijXa74SW7-e8t4J4R1RA6q2sH7mds` | 2.4 |

Файлов 22. Домашек семь: Homework 1 — три файла, Homework 5 — два. Тест на месте.

## Unit 4 — папка `1_wgy3Wbgs4WmHM2FbYdXszvBqMXruLLb`

| Файл | txt | pdf | pdf, МБ |
|---|---|---|---|
| Homework 1 (1) | `1tsueT8G0E8EpFiWf0fukbaPaO25whZjQ` | `1XDe6FRStROWU9gfnR3MGbrdDnSl_ykDc` | 0.3 |
| Homework 1 (2) | `13jXP5Zygk_245TvwlLzTDtbMKTykFEwS` | `1axF5Zpbdb8zqjAXYdgU_oOKFAEaVYFgj` | 2.5 |
| Homework 2 (1) | `13iltd4OkSFeHghncOis1HE27IiaC0eai` | `15COfmTz-0F6X1KKC_F_zYhi80I5MAaXw` | 0.8 |
| Homework 2 (2) | `1Ih9HgX_dXmWJi2DTXBxAL-8PYG6iYI7o` | `1tLHBkdVbcljZ68a7_KPdMziVFq2ZFTBr` | 3.7 |
| Homework 3 (1) | `1IvTiy_ReRQb-qVik9VFeHqwWPFMjl7-G` | `1Jd5gHaWAXAsJ3GlBKOhXAo6vubzmgAs5` | 0.8 |
| Homework 3 (2) | `1R5lmOtAzyV0aDSE8De1MJbDWhR8_Ol8V` | `16G0lQHdXJ5DfMJJQaHJMksiNk6TxJMAi` | 2.5 |
| Homework 4 | `1d-RVny0tBkx1VJ1UKT0rElongAXRGrD2` | `1pH-6cWaY5sgunGCrvEUGom_lzbhdukZg` | 2.9 |
| Homework 5 | `1V2nGCrzih4fYqXgmKDmy6yxk5Jghjb99` | `1S0da8S0Qc0YUSi7s_eDUFlzgykEROp6I` | 2.2 |
| Homework 6 | `17Dm6paO-jFpPv9NT56_yX0str8aLowA1` | `1pRHxCSrHfBByL52VbU9m5zWZ5TKxqqmr` | 3.4 |
| Homework 7 (1) | `1sMVyqObazrwHmRNDZfnsrFP3LHiuCLtV` | `168QYg5MztxZ0FCPBGvxzb5DEhHsfh038` | 6.9 |
| Homework 7 (2) | `1xUj9cRKncWt7qlidSNINh81aqrsR4SD7` | `1VmUU-i703a0KlG5b3jhtCUrsKRRBHeQF` | 3.0 |
| Test | `1Xr8mvyPiVUyKk8xf3cBC6bH5qlGPf7rh` | `1nTWzKM8U-weUL3tKiYlBuJkcl-VONUnj` | 2.6 |

Файлов 24. Домашек семь: Homework 1, 2, 3 и 7 — по два файла. Тест на месте.

## Unit 5 — папка `1y5--EFvkGBjRwxR0K1_pJyOPpA4e9bMQ`

| Файл | txt | pdf | pdf, МБ |
|---|---|---|---|
| Homework 1 (1) | `1AO4Oqs9qtWUKniE8QKfhFhBpyr2hI0Tp` | `1SB_D7J6LCfcdDqnIVqcg8Ou0MXreLNFh` | 0.8 |
| Homework 1 (2) | `1J6UYaPW1l1rIQPzKyvoFl1Ep5H7SAjQi` | `1FO9WcyypUo3UC64I8cmDKcxY4H-DyVqk` | 2.4 |
| Homework 2 (1) | `1s0rDm-LKbR5YUDl0Zy__1FzfMVm9qwxg` | `1C9TeONvppYG6LyA3_lO4qfdKyS_2phHD` | 1.3 |
| Homework 2 (2) | `1Yk_pdB5tNAH2n27BdglR95KjjTzqOO_d` | `1Gs14_JkYd8TQwpKM7KHqLrm3qOZ3uG4K` | 2.3 |
| Homework 3 | `1Sxz3KBrZxXXenk6KJLeQpRmjitB47BpC` | `175N6dw3B5DQpgpZy3HJ8e-81ekxCk8ew` | 1.9 |
| Homework 4 | `1NPYvXGM_F6YcVALXC_WBgBvbaYQgw6Md` | `1lVmuRQb5g6X0JzaYP1oVHmjvaGHGkJgA` | 2.4 |
| Homework 5 | `15UT6bI3UxCoxXMwbPcbL_Ak5GWVb4QFJ` | `1wVicmirv0coa04Jy9eeMXGn64N6cVfYl` | 1.2 |
| Homework 6 | `1KSHDuA7G_NEPYhCCnrHKVnORtarZQfcj` | `1VxzOY1EJYHim8OHxSKNeRng35T3RE3VW` | 1.4 |
| Test | `1tzgbcu1KhS8-IEiRi5JufSA7zgYsK1rN` | `1XhN7kpP1G2lc8oec5aCrEvVO0iUQ7kjb` | 2.1 |

Файлов 18. Домашек **шесть** (Homework 7 нет): Homework 1 и 2 — по два файла. Тест на месте.

## Unit 6 — папка `1u67bYSawIiCbOJmkmryN4WrDmPP-SZdd`

| Файл | txt | pdf | pdf, МБ |
|---|---|---|---|
| Homework 1 (1) | `1Q7tQjsbL0K0FiZsRuKpKDRKQhD6sjBbw` | `1wb0gvw7VLcHDqa4keM8iMob2dMPbl-SW` | 0.8 |
| Homework 1 (2) | `1OWnvYd_-FMyEMaHlWby-yLYzRuycBRZr` | `1K2gejFZCaD3hgepeOlqA6xNUlHJzvwMo` | 2.5 |
| Homework 2 (1) | `1L0GS4htGrniqZNDIVvEf7LcTQNahcV0H` | `1iWfPUky4yQz4NcB39PcAeTlKn-KZKHVH` | 1.6 |
| Homework 2 (2) | `1oqwJzn4dj397FdlqJSNYDrGVAvcNkQuj` | `1L4AlgJ6aEBE2oE1uv_JV3N-IiyGUx3ej` | 1.5 |
| Homework 3 | `1571UXNFX_znewNe99sux6mwIp846WUf4` | `1ASWHbdSrjwALxwoMKEWcXP_htSbZAvh4` | 1.7 |
| Homework 4 | `1v4_nF4pxxBwBgDqkyhHoTlNgil6fJXFW` | `1nwknYeTbN5fm4fMGHgAaI-GBZD9BQaS9` | 2.4 |
| Homework 5 | `16Szrs_5KRPPpezrSCFK8EfKCYBb0ySPK` | `17MsgjrmVI1L9AOLpwRzyD__94n80ImFY` | 2.4 |
| Homework 6 (1) | `15tfRQuSOdM0NZBnfTRJ2WWeofVeE-Ek2` | `1bNnowPpmMbcImz5WY23xZB2jVAzUvrH-` | 1.1 |
| Homework 6 (2) | `1EgFmc-RZkrraHEhKxjHzP5kFoC_tEfkK` | `1fOeOSDLpKHWwX2Sl98FB5-CJEUweLAUi` | 1.6 |
| Test | `1q0a9ASIf3-SamnfMfXasG3ZvRvi95csu` | `1LlkYtXP0BufUNZwdKenm_JktbiIJ3F9U` | 2.5 |

Файлов 20. Домашек **шесть**: Homework 1, 2 и 6 — по два файла. У Homework 1 (1) и Homework 3 в имени `unit` со строчной — те же файлы, искать по `title contains` с учётом этого. Тест на месте.

## Unit 7 — папка `1kCTcKVNCHEPdwXJ5Q94PUDwgRt_S_Ilb`

| Файл | txt | pdf | pdf, МБ |
|---|---|---|---|
| Homework 1 (1) | `1umC0mYmSXJgZlNQXnUOJ26RcXNOnEVoc` | `1rzXGn02b1FN6zNeSSN8_-dhcwiFC4YSA` | 0.8 |
| Homework 1 (2) | `1GmiGFkFBy8r4rQSxk7e1oG5aZQsC0pye` | `15H1wdvvta5VMfduiDHEzRc0XQbr0skwI` | 0.7 |
| Homework 1 (3) | `1Eao20yzPMslnBVNmo3jE8J787tmuUtMf` | `1SLDE3uMtdeG7IDWhtgw50zez2oeLdtQP` | 2.0 |
| Homework 2 | `1F4d5WJS12Mm1jKsZCxa_5jF_8miC57zu` | `1HSiDDHp4v3vhKsqLDYNqk26q7C7aGwgS` | 4.1 |
| Homework 3 | `1SVJdYBaVd6-G0pGAoICxQUOwHOl3ya1u` | `1GYayuowIYXki7G6VJSiPSrAAgVGO7Kok` | 3.5 |
| Homework 4 | `1Lm-u2FZgMkAqrrxdW5t19r55oFnqprgV` | `1U_NJRW3esnuy6bvoX77EppE3dPwAG7N2` | 2.8 |
| Homework 5 | `1Q5esviKA3aIySZHfDorrfn3MdS_eeGYU` | `1T10ozoBUDDEXbG8ycAggiwLRIbSs2pB5` | 2.4 |
| Homework 6 (1) | `1F_VGSTTnegOcP-Paxb2qottG9hoIjoiB` | `1WEyLedFDw2JgcNLLDO8CUblSPtAmE-yI` | 3.0 |
| Homework 6 (2) | `1lYnYRQ7BPhRip3ReFK4xlgXYrOo8yZc0` | `1VxSKXOzEmwyw29sFq9nisPPzKUXXiJgE` | 3.2 |
| Final ⚠️ копия Unit 8 Test | `1-dMjtdmJ2teqF1EyLlaJxMVJiBOjT6if` | `1HmD7wF8VnJZbuaQhsu90W5bzIZdaBp69` | 2.1 |
| Test | `1U0p_q1IKnTaWvcDKlGwqLgGUIQ1Pacj2` | `1k-v45yzrdY-diV2PWYMjvF9V4567_FHU` | 2.6 |

Файлов 22. Домашек **шесть**: Homework 1 — три файла, Homework 6 — два. 🟥 **Своего теста нет.** Файл `GG2 Unit 7 Final` — байт в байт копия `GG2 Unit 8 Test` (размер совпадает до байта, в txt заголовок «Go Getter 2 Unit 8 Test»). Похоже, при выгрузке теста Unit 7 скачался тест Unit 8.
**Настоящий тест Unit 7 Анна прислала в чат 05.10.2026** — лежит в репозитории
`docs/GG2_Unit_7_Test.pdf` (23 стр., 2.5 МБ, только PDF, без `.txt`). На Диске его нет.

## Unit 8 — папка `1rIGMextg1UU3JXuQhjfwIyzxH9yQRI4m`

| Файл | txt | pdf | pdf, МБ |
|---|---|---|---|
| Homework 1 (1) | `1IE2BIeP8FoeMHmQWYmOqmdwb9wD4ze42` | `15_gfJ6fs45RaCQSaDgEpzdOTA-xYvj62` | 0.8 |
| Homework 1 (2) | `1JAwc-0JszxCTSmfOU0k-4hK4tcHzzMXj` | `1iq4GVeKOb4ANsEvOxYqIfVx_VcDdqpp3` | 0.8 |
| Homework 1 (3) | `1om9GoP3pZKyst0iPocSr4rRPs4AEwzAf` | `1ZuMdI15xL10DoWVPrAwC4p9Z3XgseuRl` | 2.4 |
| Homework 2 (1) | `1EmqKC4JWXlr4oUg6dFmHTo5URPC-V737` | `1L3Jc6f33zf1OGpLUUURnZc1uWrOQUj_T` | 3.2 |
| Homework 2 (2) | `1Bni8Dt_2YlM87vjSbJUfIQwNfeEvbopG` | `1wlqBJlPtfHv1_U3k0j1l5Jbnh8J9879B` | 0.8 |
| Homework 3 | `1DrWxSEF3Sv8K7bP1WxuG8zNlwrk4zmUL` | `1sxWNgGOBnhv_qcsjn_k5h5fBiOIddY-P` | 2.9 |
| Homework 4 | `1mPvm_F7we4Ei_oA_p06YAY-OAIUuWIw7` | `12FeX7kyNxKP_aUhHrgYwwZv6KE84MhYR` | 3.0 |
| Homework 5 | `1d4XpB8ioSAat3AQ-wk_4HGpBJRgDPTbC` | `1W0OqJdrvmSWvNeLcR8eImgf3tn-_PwLs` | 2.1 |
| Homework 6 (1) | `10nJPlMAf1k7GkfIrEFs7eHs0nftF8tej` | `1UspIYeHHDxF9xJC_1Hxp7mkAWk2KL14n` | 1.8 |
| Homework 6 (2) | `1_DvqhlpTcmX-8EegEZrf-ZXNoGdRTc7J` | `1EJDlu38qgw7PkCpthZYNu_Jt_leWTU0x` | 1.8 |
| Test | `11MNxfVPSp9qgo4VLVR41EFjmRH5HaVpS` | `1m1YUTxx0KRvPhDQ3NNA2d7Rlz5fANFyt` | 2.1 |

Файлов 22. Домашек **шесть**: Homework 1 — три файла, Homework 2 и 6 — по два. Тест на месте. Имя файла `GG2 Unit 8 Test`, а не `Go Getter 2 Unit 8 Test`, как у остальных.

## Final Test — в корне папки курса

| Файл | txt | pdf | pdf, МБ |
|---|---|---|---|
| Final Test | `1MqHG_U_UCuyB0qfJVnK9v5cnni5sWIQl` | `1emQyoUVCozTmfcb0bpsFkSm65UCBT5sn` | 3.2 |

Отдельным юнитом `Final Test` с одним уроком `Final Test`, как в SM2/SM3.
