# Audio pipeline

Two scripts that turn the book into a folder of MP3s you can drop into any
podcast app. The narration uses Microsoft's neural voices via `edge-tts` —
free, no API key, and noticeably better than offline TTS.

```
audio/
├── clean_for_tts.py    # CH*.md → audio/scripts/CH*.txt
├── synthesize.py       # audio/scripts/CH*.txt → audio/mp3/CH*.mp3
├── scripts/            # cleaned text, one .txt per chapter
└── mp3/                # synthesized audio, one .mp3 per chapter
```

## One-time setup

```sh
python3 -m venv audio/.venv
audio/.venv/bin/pip install edge-tts
```

## Generate the audiobook

```sh
# 1. clean all chapters (fast, pure Python)
python3 audio/clean_for_tts.py

# 2. synthesize all chapters to MP3
audio/.venv/bin/python audio/synthesize.py
```

The full book is ~17 hours of audio. Each chapter is its own MP3 (~50-90 min).
Synthesis is roughly real-time on a single connection — plan on the full
run taking the better part of a day. Re-runs skip chapters whose MP3
already exists; pass `--force` to overwrite.

## Useful flags

```sh
# just one chapter
audio/.venv/bin/python audio/synthesize.py CH09

# pick a different voice (see --list-voices for everything available)
audio/.venv/bin/python audio/synthesize.py --voice aria
audio/.venv/bin/python audio/synthesize.py --voice en-GB-RyanNeural

# slow it down or speed it up
audio/.venv/bin/python audio/synthesize.py --rate -10%
audio/.venv/bin/python audio/synthesize.py --rate +15%

# re-synthesize a chapter you don't like
audio/.venv/bin/python audio/synthesize.py CH09 --force --voice guy

# show every English voice edge-tts can use
audio/.venv/bin/python audio/synthesize.py --list-voices
```

## What the cleaner does

The chapters are dense markdown with tables, unicode notation (CO₂, tCO₂e,
GtCO₂), currency-prefixed numbers (`$190/tCO₂e`), em-dashes, and abbreviations
that read terribly aloud. `clean_for_tts.py` rewrites them:

- `$72/tCO₂e` → "72 dollars per tonne of CO2-equivalent"
- `GtCO₂` → "gigatonnes of CO2"
- `Ch. 7` → "Chapter 7"
- `i.e.,` → "that is,"
- `1.5°C` → "1.5 degrees Celsius"
- `CCUS`, `CBAM`, `IPCC`, ... → spelled-out letters
- em-dashes → commas (the narrator pauses on commas)
- Tables, fenced code, and the end-of-chapter "Sources and currency" /
  "What's next" / "Glossary delta" sections are dropped entirely — they're
  reference data that doesn't survive linear listening.

The cleaned scripts live in `audio/scripts/` and are checked-in plain text —
useful both as the synthesis input and as a readable transcript.

## Notes

- Edge-TTS rate-limits aggressively if you slam it. The driver synthesizes
  chapters serially for that reason; don't parallelize.
- If a chapter sounds wrong somewhere, edit the `.txt` in `audio/scripts/`
  directly and re-run with `--force`. The cleaner is deterministic — running
  it again will overwrite your edits — so do final touch-ups after the last
  cleaner run.
- For the one LaTeX equation in Chapter 12 (the cement calcination reaction),
  the cleaner replaces it with "(See the chapter text for the chemical
  equation.)". The narrator can't read `$$\text{CaCO}_3...$$` usefully.
