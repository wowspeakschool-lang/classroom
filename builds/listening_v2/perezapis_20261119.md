# Перезапись аудирований: Rex и pizza (19.11.2026)

Анна прослушала два аудирования SM3 и написала:

> «Rex's favourite gadget — тут как russ. are going to make pizza — пизза. а bike — норм.»

То есть `bike` в юните 9 звучит правильно (пункт закрыт), а два слова надо чинить.

## Что чиним

**`pizza` → `peetsa`.** Подмена уже есть в словаре `docs/ozvuchka_speechkit.md`
(нашли 10.11.2026 на SM1 Unit 4 Test: «пизза» — после «пи» сразу «с», смычки «т»
нет). Беда в датах: записи ниже синтезированы 05–09.11, то есть **до** появления
строки в словаре, поэтому в них слово звучит по-старому. Текст менять не надо —
только применить словарь при синтезе.

**`Rex` → подмена нужна, написание подобрать.** В словаре имя стоит в разделе
«не подменять — распознаватель ошибается, синтез читает верно». Это оказалось
неверно: Анна слышит «russ» своими ушами, а не через распознаватель. Нужны пробы
(`Reks`, `Rekss`, `Recks`, `Reks.`) — выбрать по распознавателю и по спектру
(хвост /ks/ против контрольного `makes`), и дописать выбранное в словарь и в
`tools/speechkit/podmeny.json`.

## Файлы

Ссылки в блоках **пока не переставлены**: все четыре теста опубликованы, и
ссылка на ещё не существующий файл означает тишину у детей. Перестановку сделаю
в чате Classroom, когда файлы окажутся в бакете.

| блок | что сейчас | новое имя | что чиним |
|---|---|---|---|
| SM3 Unit 6 Test, блок 8 | `sm3/sm3_u6_test_b8_v4.mp3` | `sm3_u6_test_b8_v5.mp3` | Rex |
| SM3 Unit 9 Test, блок 7 | `sm3/sm3_u9_test_b7_v4.mp3` | `sm3_u9_test_b7_v5.mp3` | pizza |
| SM3 Unit 8 Test, блок 7 | `sm3/sm3_u8_test_b7_v2.mp3` | `sm3_u8_test_b7_v3.mp3` | pizza (то же слово, запись старая) |
| GG3 Unit 3 Test, блок 8 | `gg2 + gg3/gg3_u3_test_b8_v2.mp3` | `gg3_u3_test_b8_v3.mp3` | pizza (там это ещё и верный вариант ответа) |

Пятый файл — **по желанию Анны**: в GG1 Final Test, блок 8
(`gg1/gg1_final_b7.mp3`) та же собака по имени Rex, два раза. От ключей это имя
не зависит (ответы: eleven · long curly hair · swim · half past seven ·
under the bed · listening to music), поэтому переделываем, только если Анна
скажет. Новое имя тогда — `gg1_final_b7_v2.mp3`, текст — в
`docs/ozvuchka_speechkit.md`, раздел «GG1 · Final Test · блок 9».

Папки в бакете прежние: SM3 — `classroom-media/sm3/`, GG3 — `classroom-media/gg2 + gg3/`.

Тексты не меняются ни словом — берутся из `builds/listening_v2/teksty.py`
(вопросы в базе те же, сверять не надо). Ниже они целиком, чтобы не искать.

---

## SM3 · Unit 6 Test · блок 8 → `sm3_u6_test_b8_v5.mp3`

```
This is a story about Maisie and her brother Rex. Maisie's tablet is bigger than her mobile phone, and her laptop is bigger than the tablet. Her torch is the smallest thing she has got. Maisie's favourite gadget is her laptop. Rex's favourite gadget is his games console, and their father's favourite is his old torch. The torch is cheaper than the electric fan. The laptop is more expensive than the fan, and the tablet is the most expensive thing in the house. In their building the lift is slower than walking upstairs. The electric fan is faster than the old digital radio, and walking upstairs is the fastest way to the second floor.
```

## SM3 · Unit 9 Test · блок 7 → `sm3_u9_test_b7_v5.mp3`

```
This is a story about Liam and his sister Orla. Liam's grandma lives in Scotland. His aunt lives in London, and his uncle lives in Italy. On Monday it is going to be cloudy in Scotland. In London it is going to be sunny, and in Italy it is going to be foggy. On Monday Liam and his grandma are going to make pizza. Orla is going to ride her bike. On Tuesday they are going to watch a film, and on Wednesday they are going to ride their bikes together. Liam is going to take photos of the old castle. Orla is going to take photos of the park, and their grandma is going to take a photo of Liam's new bike.
```

(в этом тексте уже есть `Liam` → `Leeam` и `lives` → `livz` из словаря)

## SM3 · Unit 8 Test · блок 7 → `sm3_u8_test_b7_v3.mp3`

```
This is a story about Tessa and her brother Felix. Last summer Tessa went to Egypt with her family. Her friend Mara went to Spain, and Felix's school group went to China. They stayed in a hotel for two weeks. Mara stayed in Spain for two days only, and Felix's grandparents stayed in China for two months. Tessa didn't go to the museum, because it was closed. Her mother went to the museum a year later, and Felix went to the old market instead. Tessa sent five postcards. Felix sent four, and their mother sent fifteen. Every evening they ate fish and rice. At lunchtime they had pizza and salad, and for breakfast there was always soup and rolls.
```

## GG3 · Unit 3 Test · блок 8 → `gg3_u3_test_b8_v3.mp3`

```
Last summer three friends went on holiday. Daniel went to Italy with his family, Nora went to Spain and Tom went to Scotland. In Italy, Daniel went snorkelling with his father on the first day. His sister didn't go snorkelling — she stayed at the hotel with their mother. In the afternoon it rained, so the family stayed inside and played cards. They didn't go hiking and they didn't go to the beach. On the second day they went on a guided tour of a museum. Daniel's father was excited, but Daniel got bored after an hour. In the evening they ate in a restaurant. Daniel's mother had fish, his sister had soup, and Daniel had pizza. At the airport on the last day Daniel was sad, but his sister was happy, because she doesn't like hot weather.
```

---

**Порядок сдачи прежний** (решение Анны 06.11.2026): сначала готовые mp3
отдельными файлами в чат — Анна слушает; после её «да» файлы идут в бакет.
И до отправки Анне — своя проверка распознавателем, как написано в
`docs/ozvuchka_speechkit.md`.
