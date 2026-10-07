# Proofreading Spotlight word lists

Files: /home/user/classroom/tools/spotlight/tsv/grade_N.tsv (tab-separated: grade, module, section, term, pos, translation, note).
The rows were transcribed exactly as printed, including the textbook's own mistakes. The owner wants the mistakes FIXED, not copied.

Read every row of your grade file(s) yourself (in chunks, e.g. 150 rows at a time) and find:
1. Russian spelling errors/typos in translation/note ("пасадочный" → "посадочный", "аннонсировать" → "анонсировать", "вращение обществе" → "вращение в обществе", "потиворечить" → "противоречить", "ракет;ка" → "ракетка").
2. English spelling errors in term ("Sherlock Homes" → "Sherlock Holmes", "hold your noise" → "hold your nose", "(Mp3)" → "(MP3)").
3. Translation that is wrong for the term (e.g. pleasant = "довольный" → "приятный"; "sit an exam" = "готовиться к экзамену" → "сдавать экзамен"; alert = "тревога" when pos is adj → "бдительный"). Fix only clear errors; keep the textbook wording when it is merely unusual.
4. Wrong part of speech label (totally (adj) → adv, main (n) → adj, unsanitary (n) → adj, extremely (adj) → adv, "ph v" → "phr v"). Keep "C n", "U n", "n pl", "phr", "idm" style.
5. Junk: stray characters, double spaces, "( в игре)", broken hyphenation ("чем- либо"), Latin letters inside Russian words or Cyrillic inside English words.
Do NOT change: module/section names, ё vs е, capitalisation style, the meaning chosen by the textbook when it is correct.

Do NOT edit the TSV. Write corrections to /home/user/classroom/tools/spotlight/work/fix_<grade>.tsv with header:
grade	module	section	term	field	old	new	reason
(field = term | pos | translation | note; old must be the exact current value of that field so it can be matched.)
Write with python csv (delimiter '\t'), append as you go. Report the number of corrections per type and the 10 most important ones.
