# Transcribing Spotlight Word List crops to TSV

Crops: /home/user/classroom/tools/spotlight/crops/<grade>/NNN_p<page><L|R><a|b>.png.
Read strictly in NNN order (= reading order: left column top, left bottom, right top, right bottom, next page).
Open each image with the Read tool and read it yourself. Do not use OCR.

TSV, UTF-8, tab-separated, header:
grade	module	section	term	pos	translation	note
- module: module heading as printed ("Module 1", "Starter Unit"...). Blocks outside modules (name lists, Spotlight on Russia, etc.) → use the block heading as module.
- section: lesson/sub-heading as printed ("1a", "1a Family Members", "Culture Corner 1", "English in Use 1", "Across the Curriculum ...", "Going Green 2", "Spotlight on Exams"). Sub-blocks like "Phrasal verbs", "Phrases", "Words often confused", "Phrasals & Phrases" inside a lesson → section "<lesson> <sub-block>", e.g. "1a Phrasal verbs".
- term: English word/phrase exactly as printed, WITHOUT the /transcription/.
- pos: part of speech printed in brackets, without brackets (n, v, adj, adv, phr, phr v, C n, U n ...), else empty.
- translation: Russian translation exactly as printed; join wrapped lines with a space. No trailing "|" or other junk.
- note: italic remark if any, else empty.
Skip page numbers, "Word List" headers, WLnn labels, watermarks, Irregular Verbs tables, grammar-terms lists, Appendices.
An entry wrapping onto the next line/crop continues the same row; a heading at the bottom of a crop applies to the next crop.
Normalise curly apostrophes to '.

Write with python csv (delimiter '\t', lineterminator '\n'), appending after every crop so nothing is lost.
Use ONLY your own helper script and state file, inside /home/user/classroom/tools/spotlight/work/<your job name>/ — never the shared scratchpad, never other jobs' files.
When done report: rows written, (module, section) list with counts, doubtful entries.
