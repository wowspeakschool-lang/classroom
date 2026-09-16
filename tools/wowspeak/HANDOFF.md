# HANDOFF — WOW Speak Speaking-Club deck builder

You build **PowerPoint speaking-club lesson decks** in the WOW Speak style for **Anna**,
founder/director of **WowSpeak** (online English school for Russian-speaking kids).
Anna writes mostly in **Russian**, fast pace, wants concise replies.

Read `REGLAMENT_ADDENDUM.md` together with this file — it is the newer document and it wins
wherever the two disagree. In short, what changed: **WordWall is gone** (games live inside the
.pptx), **icons are generated here** through the OpenAI API, and **every request to Anna goes
on the first line marked 🟥**.

## 0. The toolkit

| File | What it is |
|---|---|
| `wowspeak_builder.py` | the deck builder. `build(cfg, out_path)` |
| `wowspeak_games.py` | the in-deck games. **Required** — without it nothing builds |
| `wowspeak_cropping.py` | icon sheets: `gen_sheet` → `whiten` → `crop_grid_auto` → `preview` |
| `wowspeak_qa.py` | QA: `python3 wowspeak_qa.py final/*.pptx` |
| `run_example.py` | a full worked example: one theme × 4 versions. Copy it for a new theme |
| `WORD_BANK.md` | every word used so far. Scan before picking new vocabulary |
| `REGLAMENT_ADDENDUM.md` | the rules that changed, including the 10 game rules |

Deps: `pip install python-pptx Pillow numpy --break-system-packages`.
Save decks with `prs.save(path)` (the builder does) and hand the files straight into the chat.

## 1. The four versions (always make all 4 per theme)
- **10-12 Beginners** (A1) — icon vocab
- **10-12 Advanced** (~B1) — definition-card vocab
- **13+ Beginners** (A1-A2) — icon vocab
- **13+ Advanced** (~B1) — definition-card vocab

Beginners = basic, very supported. Advanced = a real conversation club.
For 13+ Beginners keep Beginner language but pick teen-relevant items (the two Beginners
usually share ~4 words + 2 teen-swapped).

**Filename format (exact):** `Speaking Clubs [age+level] [full theme name].pptx`
e.g. `Speaking Clubs 10-12 Beginners What autumn smells like.pptx`

## 2. The staged WORKFLOW (per theme) — follow in order, WAIT at each ⏸
- **STEP 1** — propose the vocabulary for all 4 versions **+** English video-search queries.
  ⏸ wait for approval. Ask for the video link on the first line, marked 🟥.
- **STEP 2** — generate the icon sheet(s) with `gen_sheet` (only the two Beginners levels need
  icons; Advanced uses definition cards). One sheet per age group, ≤10 icons, no labels.
- **STEP 3** — `whiten` → `crop_grid_auto` → `preview` montage → ⏸ **WAIT for "ок".**
  Do NOT build decks before approval. This preview step is mandatory.
- **STEP 4** — build all 4 decks (icons + video link + games), run `wowspeak_qa.py`, deliver
  the files in the chat. **No WordWall columns any more** — the games are in the deck.

Use GPT economically: **`quality='medium'` by default** (a quarter of the price; on a ~4 cm
lesson tile the difference against `high` is barely visible), **one sheet for the whole theme**
covering every version's words, reuse the crops across all four decks, and fix a crooked icon
by cropping again - re-generating one icon costs nearly as much as a whole sheet. Go to `high`
only when a medium sheet genuinely comes out wrong.

## 3. THE DECK FORMAT
`build(cfg, out)` renders, in lesson order:

| Slide | Beginners | Advanced |
|---|---|---|
| Title | theme + subtitle + emoji row | same |
| Teacher notes | dark slide; slide numbers filled in automatically | same |
| Mood check | 5 emoji mood cards | same |
| Lead-in | ~6 simple discussion Qs | ~6 open/evaluative Qs |
| **New Words** | 6 icon cards **(the only slide with captions)** | 6 word + definition cards |
| Talk with the words | rotating mini-activity + support frame | reusable "Useful language for discussion" |
| **Games (N slides)** | picture quiz, one round per word + "what's missing" | word quiz (definition → word) + board |
| | *on quiz and board slides a stray click is swallowed by an invisible catcher; the small "→" bottom-left is the way on* | |
| Video | embedded file or a gold link button + 2-3 discussion Qs | same |
| Main speaking | sentence frames | rotating format (Debate / Ranking / Discuss & Pitch / Role-play / Would-you-rather / Diamond-9) |
| Thank you | | |
| *(end of file)* | service screens: Correct / Try again / board questions | same |

`cfg['games']` is a list of specs, each `{'type': 'quiz'|'missing'|'reveal'|'board', ...}`:
```python
'games':[{'type':'quiz','bg':'FFF7D4'},          # a round per word, from cfg['vocab']
         {'type':'missing','bg':'D4F5E6'},       # Beginners: cards really disappear
         {'type':'board','bg':'D4ECFF','questions':[...]}]   # Advanced: number → question
```
`{'type':'missing'}` builds one slide per step by default; `'anim':True` builds the single
animated slide instead (`<p:timing>`, disappear on click) — same thing on screen, but the
animated one can only be verified in real PowerPoint.

Quiz mode is picked from the level: Beginners get pictures ("Which one is "rain"?"),
Advanced gets words ("Which word means: "…"?"). Override with `'mode':'picture'|'word'`.
The games obey the 10 rules in `REGLAMENT_ADDENDUM.md §4` — read them before touching
`wowspeak_games.py`.

## 4. DESIGN SYSTEM (baked into wowspeak_builder.py)
- Canvas 12192000 × 6858000 EMU (13.33 × 7.5 in, 16:9).
- Palette: HOTPINK `E91E8C`, GOLD `FFD700`, INK `3A2E55`, TEAL `1E9E7A`, RED `D32F2F`,
  DARK `2C2040`. Pastel backgrounds: pink `FFE4F0`, blue `D4ECFF`, yellow `FFF7D4`,
  lavender `EDE4FA`, mint `D4F5E6`, peach `FFE6D0`. Game cards come from `pal(bg, i)`,
  never from `PASTELS` (rule 8).
- Fonts: **Trebuchet MS** (titles), **Calibri** (body).
- Furniture: pastel corner blobs, rounded white cards with a soft shadow, a white pill title
  band on light slides / gold text on dark slides, `WOW Speak 💜/💛` bottom-right.
- Emojis render fine in PowerPoint; LibreOffice previews some in B/W — that's fine.
- No theme emoji is hard-coded: title and farewell read `cfg['emoji']`.

## 5. cfg schema for build(cfg, out)
```
level          'beg' | 'adv'
theme          full theme name (str)
emoji          [title_left, title_mid, title_right, [6 deco emojis]]
title_bg       pastel hex for the title slide
subtitle       'Speaking Club · 10-12 Beginners'
mood_q         one-line question on the mood slide
moods          [(emoji,label) x5]
lead_in        [(question, emoji) x ~6]
vocab_title    band text on the New Words slide
vocab          beg: [(word,'icons_dir/word.png') x6]   adv: [(word, definition) x6]
games          [ {type:'quiz'|'missing'|'reveal'|'board', ...}, ... ]
video_url      link for the button  (video_file / video_poster embed a local file instead)
video_qs       [(question, emoji) x2-3]
# Beginners only:
mini           {title, frame, items:[(text,emoji)...]}
speak_title, frame_hint, frames [str x ~5]
# Advanced only:
disc           {headline, statement, options:[...], tasks:[...]}
bye            thank-you subtitle
notes          [{label,text,[url],[tail],[red]} ...]   {GAMES}/{VIDEO}/{SPEAKING}/{SERVICE}
               inside label or text are replaced with the real slide numbers
```

## 6. QA checklist (every build)
- `python3 wowspeak_qa.py final/*.pptx` — double round-trip, links, dead picture-on-button,
  card-colour-equals-background, feedback screens at the end, no_click_advance on quiz/board.
- Visual: `apt-get install -y libreoffice-impress` (it is often missing), then
  `soffice --headless --convert-to pdf file.pptx --outdir pdf` and PyMuPDF to look at the
  New Words slide, a quiz round and the main-speaking slide.
- **Animations never play in a PDF.** The games themselves are checked in real PowerPoint,
  in slideshow mode (F5) — that part is Anna's side.

## 7. Accumulated rules / preferences (don't relearn)
- Requests and questions to Anna: **first line, marked 🟥**, messages short.
- Video: insert the link Anna provides. No link → offer 2-3 candidates (title + channel) and
  say honestly if YouTube pages were unreachable and the titles come from search results only.
  Never download a video; a local file she sends gets embedded.
- No baked-in captions in generated icon sheets; captions only on New Words.
- Advanced abstract words → definition cards, not icons.
- **Repeated words are fine.** What must not happen is two lessons on the same subject with
  nearly the same word list (two "clothes" lessons). One clothing item surfacing inside another
  theme is not a problem. Use `WORD_BANK.md` to spot a repeated *topic*, not a repeated word.
  (Anna's topic catalog `РК_каталог_тем.xlsx` has topic names only.)
- Show previews as **files** — Anna cannot see the assistant's own view-tool images.
- Files that came pre-named with "wow" keep that base; otherwise `Speaking Clubs …`.

## 8. Where the work stands
Next theme in the queue: **"What autumn smells like" 🍂** (STEP 1 proposal was sent, waiting
for Anna's approval of the words and a video link). Proposed sets:
- 10-12 Beginners (icons): rain · pumpkin spice · wood (bonfire) · leaves · coffee · candle
- 10-12 Advanced (defs): smell · scent · damp · nostalgic · remind · fresh
- 13+ Beginners (icons): rain · pumpkin spice · coffee · leaves · candle · cinnamon
- 13+ Advanced (defs): scent · aroma · damp · earthy · nostalgic · remind

Approved by Anna, with `pumpkin spice` shortened to **`pumpkin`** on both Beginners decks.
Video (all four decks): <https://youtu.be/cj6RmvPGqlI>.
Icons: one sheet for the whole theme, cropped into `icons/smell/` — awaiting the preview "ок".
