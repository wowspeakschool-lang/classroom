# Задача: грамматика Spotlight по классам

Нужно составить ПОЛНЫЙ перечень грамматики (включая Use of English: словообразование,
фразовые глаголы, зависимые предлоги / устойчивые сочетания, а также служебные
грамматические вещи: linkers, relative pronouns, question words, порядок прилагательных и т.д.)
по учебнику(ам) Spotlight, с разбивкой: класс → модуль → урок (1a, 1b...) → тема.

Главное — ОБЪЁМ: что именно дано в этом классе. Примеры, как надо:
- "have got" в 2 кл: только I/you/we/they have got, только утверждение → так и писать.
- "Present Continuous" — если дано только значение "сейчас", писать meanings = "now (действие в момент речи)".
  Если в старших классах значений больше — перечислять ВСЕ значения, которые есть в справочнике/учебнике.
- Формы: + / − / ? / краткие ответы; какие лица; краткие формы; правила орфографии (-ing, -s, -ed) — если даны.
- Сигнальные слова (time expressions), если даны.
- Противопоставления (Present Simple vs Present Continuous и т.п.) — отдельной строкой.

Источники: оглавление (Table of Contents, колонка Grammar / Vocabulary — OCR склеивает колонки,
восстанавливай по смыслу и номерам страниц), Grammar Reference / Грамматический справочник
(главный источник объёма и значений), Word Perfect & Grammar Check, Word List (там видны
фразовые глаголы и предлоги по модулям, а для младших классов — речевые структуры).
OCR текст грязный (кириллица иногда побита) — восстанавливай смысл, не выдумывай.
Если не уверен — пиши в comment "проверить: ...".

## Формат вывода
JSON-массив объектов, записать в файл (путь дан в задании). Поля:
- grade: число (2..11)
- module: строка, "Module 1 · School days" (для 2–4 кл. как в учебнике; Starter — "Starter")
- lesson: "1a" / "Unit 2" / "" если неизвестно
- category: одна из: "Глаголы: времена", "Глаголы: to be / have got / модальные", "Глаголы: другое"
  (инфинитив/герундий, пассив, косв. речь, условные, wish, used to, causative...),
  "Существительные и артикли", "Местоимения", "Прилагательные и наречия", "Числительные",
  "Предлоги", "Предложение и вопросы" (порядок слов, вопросы, there is, imperative, relative clauses,
  linkers, question tags...), "Словообразование", "Фразовые глаголы", "Зависимые предлоги и устойчивые сочетания"
- topic: КАНОНИЧЕСКОЕ английское название темы (см. список ниже; если темы нет в списке — придумай
  короткое в том же стиле). Одинаковая тема в разных классах = одинаковое название, чтобы потом свести.
- scope: объём в этом месте, по-русски, развёрнуто: формы (+/−/?), лица, значения, что именно.
  Для фразовых глаголов: "get: get on with, get over, ..." (глагол + все частицы с значениями кратко).
  Для словообразования: перечислить суффиксы/приставки (-ful, -less, un-...) и что из чего образуется.
  Для предлогов: перечислить сочетания (interested in, good at...).
- example: 1 короткий пример (из учебника, если есть), иначе пусто
- comment: пометки по-русски: что ещё НЕ дано (напр. "вопросов нет", "только he/she has got"),
  связь с другими темами, "впервые" / "повторение из N кл", "проверить: ..." и т.п.
- source: "ToC", "GR", "Word List", "WP&GC" — через запятую

Канонические названия (используй их буквально, когда подходят):
to be (Present) · to be (Past: was/were) · have got · can (ability) · can (permission/request) ·
can/could (ability past) · must/mustn't · have to · should/shouldn't · may/might · need/needn't ·
Modal verbs (deduction) · Present Simple · Present Continuous · Present Simple vs Present Continuous ·
Past Simple · Past Continuous · Past Simple vs Past Continuous · Present Perfect · Present Perfect Continuous ·
Present Perfect vs Past Simple · Past Perfect · Past Perfect Continuous · Future Simple (will) ·
be going to · Future Continuous · Future Perfect · Future Perfect Continuous · Future forms (comparison) ·
used to · would (past habits) · Passive Voice · Causative (have something done) · Reported Speech ·
Conditionals (Type 0) · Conditionals (Type 1) · Conditionals (Type 2) · Conditionals (Type 3) · Mixed Conditionals ·
Wishes (I wish / If only) · Unreal Past (it's time, I'd rather...) · Infinitive / -ing form ·
Stative verbs · Imperative · Let's · There is / There are · There was / There were ·
Plurals (regular) · Plurals (irregular) · Countable / Uncountable nouns · a/an · a/an/some/any ·
Articles (a/an/the/zero) · much/many/a lot of · a few/a little · Quantifiers · Possessive case ('s) ·
Personal pronouns (subject) · Object pronouns · Possessive adjectives · Possessive pronouns ·
Reflexive pronouns · Demonstratives (this/that/these/those) · Indefinite pronouns (some-/any-/no-/every-) ·
Relative pronouns / Relative clauses · Question words · Question tags · Subject/object questions ·
Comparatives & Superlatives · Adjectives (order) · Adjectives -ed/-ing · Adverbs of manner · Adverbs of frequency ·
too / enough · so / such · Prepositions of place · Prepositions of time · Prepositions of movement ·
Cardinal numbers · Ordinal numbers · Linkers · Clauses of purpose · Clauses of result · Clauses of concession ·
Clauses of reason · Time clauses · Emphatic structures · Inversion · Word formation · Phrasal verbs ·
Dependent prepositions · Collocations / Fixed phrases · Determiners (both/either/neither/all/none) · Like (verb vs preposition)

Строку делай на каждую тему в каждом месте, где она вводится или существенно расширяется.
Фразовые глаголы — одна строка на модуль (topic = "Phrasal verbs", scope перечисляет все).
Словообразование — одна строка на модуль. Зависимые предлоги — одна строка на модуль.
Будь исчерпывающим: лучше лишняя строка, чем пропущенная тема.
В конце ответа верни: путь к файлу, число строк, и 5–10 строк о проблемах (неразборчиво, чего нет в источнике).
