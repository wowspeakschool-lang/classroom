I've replaced all the human-family pictures in WD2 with Dracosha's dragon family and put in the second batch. The final check passed: none of the 13 old file ids is linked anywhere in the course. Changes went into the database by block id; 123 blocks changed.

Before the edits I saved a copy of all 936 course blocks to the table `classroom_blocks_backup_wd2_family_20261015`.

The control check on every changed block is clean:
- every `correct` points to an existing option;
- single questions have exactly 1 correct answer, multiple have 2 or more;
- no question has two identical options, so no question ended up with the same picture twice;
- the right side of every match is unique;
- no base64;
- every `new/…` link has its file in `media/wow-dragon-2/new/`, and all of them are already committed to main.

**Block numbers.** Numbers below are positions as shown in the editor. `fix/babushka.md` counted `sort_order + 1`, which is one too high in lessons whose blocks start at 1. For example, ДЗ 5 «Найди того же» is block 4 in the editor, not 5. Anna's own numbers (ДЗ 3 б5, ДЗ 7 б4, ДЗ 13 б4) match the editor.

**Family (one-for-one replacement, poses by meaning)**
- **Default rule:**
  - granny → granny_wave; ill granny → granny_armchair
  - sock / sewing / stuffing / teddy → the matching granny poses
  - mother, father, sister, brother, grandpa, ill grandpa → the dragon versions
  - whole family → dragon_family_all
- **Where I used a different picture than the default:**
  - ДЗ 7 · б2: the «the same» card is now pair_same (instead of the family picture).
  - ДЗ 10 · б9 «Granny is coming»: the bare balloon is now granny_balloon, and the «Hooray!» line is granny_wave. I changed only pictures; the spell lines are untouched.
  - ДЗ 11 · б10: granny_wave.
  - ДЗ 14 · б11 «Подбодри бабушку»: granny_bed.
  - ДЗ 15 · б9: «Granny is ill» is granny_bed, «Granny is happy» is granny_dance.
  - ДЗ 17 · б11 «волшебный чай»: granny_tea.
  - ДЗ 21 · б6: kept granny_wave. In that task granny has a ball, so the teddy pose would mislead.
- **All blocks that changed:**
  - ДЗ 5 б2–6, 8–10; ДЗ 6 б4, 5; ДЗ 7 б2–10; ДЗ 8 б4, 5, 9, 11; ДЗ 9 б8, 12; ДЗ 10 б6, 9
  - ДЗ 12 б2, 3, 6, 7, 10; ДЗ 13 б2, 3, 5, 6, 7, 9, 10, 11; ДЗ 14 б5, 11; ДЗ 15 б2, 3, 5, 6, 7, 9
  - ДЗ 18 б2, 5–9; ДЗ 19 б4, 5, 6, 8, 10; ДЗ 20 б2, 3, 6, 9; ДЗ 23 б6, 8; ДЗ 24 б4
  - ДЗ 25 б2, 5; ДЗ 26 б7; ДЗ 29 б6, 9; ДЗ 79 б8; ДЗ 80 б2, 5, 7
- **Wording changed for dragons:**
  - ДЗ 5 · б4: «Найди того же человека» is now «Найди того же героя».
  - ДЗ 7 · б3: «где этот человек» is now «Послушай и выбери комнату».
- **ДЗ 7 · б4 «Они одинаковые?» is back.** Two questions are added at the start of the block: pair_same (answer «They are the same.») and pair_different (answer «They aren't the same.»). Both options sound through `*_tts`.
- scene_family_tree is not used anywhere.

**Second batch**
- ДЗ 3 · б5, question 3: the bat is now bat_tree (small).
- ДЗ 6 · б2: the welcome card is now dragon_welcome. The envelope stays elsewhere, where it means «letter».
- ДЗ 13 · б4: added «Сколько рук у монстра?» with monster_c (three) and monster_b (two); the sound is «two arms» / «three arms».
- ДЗ 34 · б2, б3, б9: dream is now dragon_dream (was the crystal).
- ДЗ 45:
  - б2 (bus card), б6 (sort) and б9 (sequence): the red bus is now dolphin_bus.
  - б7, question 1 «It can bite»: biting_ticket.
- ДЗ 46:
  - б2: new cards sorry and stressed.
  - б3: two new «послушай и выбери» questions, sorry and stressed.
- ДЗ 47:
  - б2: penguin card (penguin_compass).
  - б3: «penguin» question.
  - б8: «It's a penguin.» ✅
- ДЗ 54:
  - б2: science project card.
  - б3: science project question.
  - б9: picture for «Расскажи про проект».
- ДЗ 58 · б2, б4: attach is now dragon_attach (was the plate with glue).
- ДЗ 62:
  - seasick is now dragon_seasick, weak is princess_weak, afraid of heights is unicorn_heights, in б2–б9.
  - б8 is now «Что с Единорогом?» (was «с мальчиком»).
- The same three pictures replaced the old ones in ДЗ 64 б5, ДЗ 67 б2, 3, 4, 7, ДЗ 68 б3, 8, and ДЗ 77 б6.
- ДЗ 64:
  - б2: the keep the balance card is now dragon_balance. Yoga stays in б6 as «do yoga».
  - б3: new «keep the balance» question.
- ДЗ 66:
  - б2, б4: roll a ball is now dragon_roll_ball (was the rolling pin).
  - б3: new «roll a ball» question.
- ДЗ 73:
  - б2: fix card.
  - б7: «fix» question.
- ДЗ 75:
  - б2: the give a present card is now dragon_gives_crystal.
  - б7: «give a present» question.

All new cards and questions have an empty sound field plus `*_tts`, so they need «Озвучить пачкой».

**Записать голосом:** nothing new; I added no letters.

**Not placed, and why**
- **ДЗ 63, 69, 80:** the words seasick, weak and afraid of heights don't appear in any block, so there was nothing to replace. I didn't create new tasks there.
- **ДЗ 45, red bus left in three places:**
  - б3: a wrong option in the «plane» question.
  - б7: an option in «It can swim». A swimming dolphin-bus there would be ambiguous.
  - б8: «It's a plane» ❌.
- **ДЗ 66 · б3:** the rolling pin stays as a wrong option in «plasticine». The ball picture has plasticine on it, so swapping it would be ambiguous.
- **ДЗ 75 · б6 sequence:** the crystal picture stays, because there it means «the crystals».
- **ДЗ 67 · б7** («Комикс про полёт»): this is not a real comic, just our word pictures. I swapped the seasick and afraid pictures there; the text is unchanged.
- **Ill granny for «My legs hurt»** (ДЗ 13 б2, б5, б11; ДЗ 19 б6; ДЗ 20 б9) is now granny_armchair. She holds her head and has a blanket over her legs. It reads as ill, but not as legs hurting; worth a look.
- **ДЗ 80 · б5:** dragon_grandpa_sick also holds one arm, while the phrase is «My arms hurt!». This was already an open point in section 4.
- **`docs/vychitka/wd2/WD2_dorabotat_rukami.md`:** I didn't update section 4 «Картинки ждём». The items above are now done and can be ticked off.