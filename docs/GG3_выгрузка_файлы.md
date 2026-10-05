# Go Getter 3 — тесты, файлы выгрузки в Google Drive

🟥 **В GG3 только тесты, домашек нет.** У каждого урока `kind='test'`,
`pass_threshold = 90`.

Опись снята 05.10.2026 запросом `parentId = '<id папки>'` с
`excludeContentSnippets: true`, по всем страницам `nextPageToken`.

Выгрузка — из **ShkolaApp**, у каждого теста пара `.txt` + `.pdf`. PDF лёгкие,
1.2–1.9 МБ, качаются `download_file_content` целиком.

Папка на общем диске — `Test GG3` `1Q0fOJsYg7LGm0og5mOBixsrsDOQKSw6z`, в ней ещё
одна `Test GG3` — `1RIR_EFGXK4iRimOwvI9slDH365gVHlIX`. Во вложенной — папки
`Unit 1`…`Unit 8` и `Final`, в каждой ровно один тест.

## Сводка

**По тесту на юнит: 8 юнит-тестов + финальный, всего 9.** Unit 0 нет.
Пропусков нет, лишних файлов нет.

| Юнит | id папки | txt | pdf | pdf, МБ |
|---|---|---|---|---|
| Unit 1 | `1aGtPmKa_35gwY0TP6vhc5Rp6xfQ2PShG` | `1BJmsxweM-8LfJFeUaiEjXDrF-O-BOeY1` | `1hwFjw7PUWaITT_IyKZlXi6AH_lCmWQjC` | 1.5 |
| Unit 2 | `1nqAHfarM3g1o8QcDz0slumLPzjka9Eqc` | `1hiFFuKbPTjemO3Xmkr9M-gURDvl2VHAR` | `1Bnp19NggjJEDXImwUEO6i0mfDdbhTsuE` | 1.7 |
| Unit 3 | `13sO55uf1Uk8EOaXnDVREt45V_efl4yIG` | `1kenIktLl9tJhgFH_Cha3jhnJIIpS4MyX` | `1uEj_SCQyxxvK1XpAfXMquZdb342aJfBW` | 1.3 |
| Unit 4 | `1XH4ro_hd9dOmk2ELjFWbYTIy9LNt3pbm` | `1pxVm7HEkLCjXemfH4Sv2w_QjOcOylma2` | `1a_vsogWZmP_FGouwJ7jpMshPiJ0RDUrE` | 1.9 |
| Unit 5 | `1ltFfP1BahK9bDjeycE3Qvkg_xEV7a2RO` | `1ZYBskiZvZvt13KwDWx_e6xqicIitWZjf` | `1Db4n3qQH_KVmV_P828NL4E-jLvYIf9jo` | 1.6 |
| Unit 6 | `1unMxh6KjI9_jILEoJuRD9lvbW7d7IyjZ` | `1zU4H-2w3kkOoakhmaevjpWZje69U2A--` | `1UWMF1Pd1Qs48k8DLSGA-EdzIabhhAZZC` | 1.8 |
| Unit 7 | `1yO6aRizLGt28sKAWw_mxYTR6IVRnKT5m` | `1s6uA127pf4_coxiHoMbLApAikyqik8Vz` | `1citx2nyBSQqP2s6Eo9Sf2v4hpPCBRGxx` | 1.2 |
| Unit 8 | `1wMQEq-xLHHLLDmkAOUMWZGIEAu965lCx` | `1BsFyCtmNWq6Q3KSjU8BxfN_jLKZSyTQ_` | `1rAwyH8H18ruQPgGF1cBxoMCP3QmTIfnG` | 1.2 |
| Final | `1UvFPYQ5Fdcp-FOhmQP4l_NCT0T4-4_It` | `1lqPjdxIQiJbJ3r_oySF302ibEB621yIt` | `1WTCEpnvoIMNVgecqqdPqGflDcNy1eZ4I` | 1.3 |

Имена файлов — `Go Getter 3 Unit N Test` и `Go Getter 3 Final Test`.
