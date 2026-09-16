# WOW Speak — speaking-club deck toolkit

Build 4 PowerPoint decks per theme (10-12 / 13+ × Beginners / Advanced) with the vocabulary
game built **inside** the .pptx — no WordWall, no internet, no accounts.

```bash
pip install python-pptx Pillow numpy --break-system-packages
python3 run_example.py final          # 4 decks into ./final
python3 wowspeak_qa.py final/*.pptx   # QA
```

Read `HANDOFF.md` first, then `REGLAMENT_ADDENDUM.md` — the 10 game rules there are not
suggestions, every one of them is a bug that already shipped once.

| File | What it is |
|---|---|
| `wowspeak_builder.py` | the deck builder: `build(cfg, out_path)` |
| `wowspeak_games.py` | the in-deck games (quiz / what's missing / reveal / board) |
| `wowspeak_cropping.py` | icon sheets: `gen_sheet` → `whiten` → `crop_grid_auto` → `preview` |
| `wowspeak_qa.py` | round-trip, links, dead buttons, colour clashes, slide order |
| `run_example.py` | worked example — copy it for a new theme |
| `HANDOFF.md` / `REGLAMENT_ADDENDUM.md` / `WORD_BANK.md` | the docs |
