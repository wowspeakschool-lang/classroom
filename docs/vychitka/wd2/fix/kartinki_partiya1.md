I've put the first batch of WD2 images into the homeworks and added the new tasks they allow. All changes went into the database by block id. The control check passed on all 22 touched homeworks: `correct` in range, single = 1, multiple ≥ 2, no duplicate options, match right sides unique, no base64. Every `new/…` link points to a file that exists in `media/wow-dragon-2/new/`, and all 76 files there are on `main`. I couldn't open classroom.wowteach.ru from the container because the proxy blocks it, so I haven't confirmed the site actually serves them. New words have an empty sound field with `*_tts`, so they need «Озвучить пачкой».

**Replaced images**
- ДЗ 6 · б2: magic tune is now magic_tune (was the microphone).
- ДЗ 29 · б2, б3, б9: travel permit is now travel_permit.
- ДЗ 34 · б2, б3: the best is now trophy (was the coin).
- ДЗ 39 · б2, б7: for swimming is now swim_ring. Same in ДЗ 80 · б5, where it is a wrong option in a «for hiking» question.
- ДЗ 48 · б2, б3, б4, б8, б9: North/South arrows are now compass_n / compass_s. The б4 title is now «…соедини с картинкой».
- ДЗ 70 · б6 and ДЗ 80 · б9: all four arrows are now compasses (N, S, W, E). West/East used to be the left/right arrows. The correct indices are unchanged.
- ДЗ 57 · б2, б5, б7: the astronaut is now air and the cracked moon is now gravity. In б6 the sort card «air», which showed the Earth, now shows air.
- ДЗ 59 · б4 and ДЗ 60 · б3: the astronaut was a wrong option; it is now air, since spacesuit isn't taught until lesson 67. ДЗ 59 · б4 question 3 now uses the gravity picture.
- ДЗ 67 · б2, б3, б6, б8, б10: the astronaut is now spacesuit.
  - б10: I changed the instruction to «…расскажи про космический костюм», because there is no «космонавт» in the course any more.
  - б5: I paired «gloves» with the gloves picture instead of spacesuit, because a suit for the word «gloves» would confuse.
- ДЗ 74 · б2, б3, б5: the green alien is now shining_spheres.
- Letters now show pictures (the text label is kept):
  - ДЗ 59 · б3: question 2 has F, T, H, S; question 3 has t, s, f, h.
  - ДЗ 67 · б4: question 2 has TH, EA, F, S; question 3 has ea, th, s.
  - ДЗ 75 · б4: question 2 has TH, EA, SH, S; question 3 has sh, s, f.
  - F/f, TH/th, EA/ea, SH/sh are from the new batch; T, H, S, t, s, h are the existing legacy letter images in the same purple style.

**Added**
- ДЗ 4: wafer card in б2, and a «wafer» question in б3.
- ДЗ 25: cards rubber bands, cotton, markers in б2. In б3 they are three more correct options (7 options, correct 0,1,4,5,6).
- ДЗ 26 · б2: magic bow card.
- ДЗ 34: balloon and banana are correct options in б5 (8 options, correct 0,1,2,6,7). Bee is in the «B» group of the б6 sort. All three have a word on the option and no hint sound on the question.
- ДЗ 42 · б6: the small/big sort is now a quiz «Послушай и найди буквы». Question 1 is TH among SH, F, EA; question 2 is th among sh, f, ea. The question sound is empty.
- ДЗ 48: East and West cards in б2, «East» and «West» questions in б3, and pairs «Go East.» / «Go West.» in б4.
- ДЗ 49: napkin and picnic cards in б2, «picnic» and «napkin» questions in б3, napkin in the «Для пикника» group of the б8 sort.
- ДЗ 61 · б4: third pair, rocket_no_engine ↔ «an engine» (existing engine picture d2832581d228).
- ДЗ 66: cards toothpick, plastic knife, plastic board in б2; «plastic knife» and «plastic board» questions in б3; all three in the materials group of the б8 sort.
- ДЗ 71: «There is a book on the table.» added to б3 and as a true/false item in б8 (✅, so the pattern is ✅✅❌✅).
- ДЗ 73: cards clean, dirty, strange signal, space dust in б2; four questions in б7 (clean, dirty, a strange signal, space dust); «It's dirty.» ✅ in б8 (pattern ✅❌❌✅).
- ДЗ 74: sand stones card in б2 and a «sand stones» question in б3.
- ДЗ 80 · б9: question «Give her a red crystal.» with crystal_red, the purple crystal and the crystal cluster.

**Записать голосом**
- ДЗ 42 · б6: question 1 «TH», question 2 «th». This is new and replaces the old «позже» line in section 2.
- Already in the list and still needed: ДЗ 59 · б3 (F, f), ДЗ 67 · б4 (EA, ea), ДЗ 75 · б4 (SH, s). Those questions now show letter pictures; their sound is still empty.

**Not placed, and why**
- Not in this batch, so not touched (some of these files are already in `new/` but weren't in the approved list):
  - ДЗ 3 bat · ДЗ 6 welcome · ДЗ 7 same/different · ДЗ 13 monsters · ДЗ 15 looking
  - ДЗ 31 map/behind · ДЗ 34 dream · ДЗ 45 dolphin bus and biting ticket · ДЗ 46 sorry/stressed · ДЗ 47 penguin
  - ДЗ 54 science project · ДЗ 58 attach · ДЗ 62 seasick/weak/afraid of heights · ДЗ 64 keep the balance · ДЗ 66 roll a ball
  - ДЗ 73 fix · ДЗ 75 give a present
- Granny and family pictures: not touched.
- ДЗ 64 · б7 still shows the astronaut. It's a visual pattern (rocket, astronaut, rocket, ?), the astronaut is drawn into the question picture d0b42c79078e, and no word is spoken. Swapping the answer would break the pattern; it can be redrawn later if needed.
- The up/down arrows stay as wrong options in left/right questions in ДЗ 48 · б7 and ДЗ 53 · б2, б6. There they don't mean North/South, and they weren't on the replacement list.
- The coin b420dfde5b9d stays in ДЗ 29 · б3 and ДЗ 38. There it is just a coin, not «the best».

The «Добавлю, когда придут картинки» and «Записать голосом» sections of `/home/user/classroom/docs/vychitka/wd2/WD2_dorabotat_rukami.md` are not updated yet.