#!/usr/bin/env python3
"""
Synthesize cleaned chapter scripts to MP3 using Microsoft's Edge-TTS voices.

Edge-TTS is free, no API key, uses Microsoft's neural voices — markedly
better than offline `say`/`pyttsx3`, without ElevenLabs' character cap.

Usage:
    python3 synthesize.py                   # all chapters, default voice
    python3 synthesize.py CH09              # one chapter
    python3 synthesize.py --voice en-US-AndrewMultilingualNeural
    python3 synthesize.py --rate -10%       # slow down 10 percent
    python3 synthesize.py --list-voices     # show common voice options

Setup (once):
    pip install edge-tts
"""
from __future__ import annotations

import argparse
import asyncio
import shutil
import sys
from pathlib import Path

try:
    import edge_tts
except ImportError:
    sys.stderr.write(
        "edge-tts is not installed. Install it with:\n"
        "    python3 -m pip install edge-tts\n"
    )
    sys.exit(1)

REPO = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO / "audio" / "scripts"
MP3_DIR = REPO / "audio" / "mp3"

# A handful of voices I've found pleasant for long-form non-fiction. There are
# hundreds more — run with --list-voices to see them.
SUGGESTED_VOICES = {
    "andrew": "en-US-AndrewMultilingualNeural",   # warm male US, default
    "aria":   "en-US-AriaNeural",                 # measured female US
    "guy":    "en-US-GuyNeural",                  # crisp male US
    "ryan":   "en-GB-RyanNeural",                 # male UK
    "sonia":  "en-GB-SoniaNeural",                # female UK
}
DEFAULT_VOICE = SUGGESTED_VOICES["andrew"]


async def synth_one(text: str, out_path: Path, voice: str, rate: str) -> None:
    tmp_path = out_path.with_suffix(".tmp.mp3")
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
    await communicate.save(str(tmp_path))
    shutil.move(str(tmp_path), str(out_path))


def chapter_scripts(arg: str | None) -> list[Path]:
    if not SCRIPTS_DIR.exists():
        sys.stderr.write(
            f"No scripts found in {SCRIPTS_DIR}. Run clean_for_tts.py first.\n"
        )
        sys.exit(1)
    if arg:
        matches = sorted(SCRIPTS_DIR.glob(f"{arg}*.txt"))
        if not matches:
            sys.stderr.write(f"No script matched: {arg}\n")
            sys.exit(1)
        return matches
    return sorted(SCRIPTS_DIR.glob("*.txt"))


async def list_voices() -> None:
    voices = await edge_tts.list_voices()
    english = [v for v in voices if v["Locale"].startswith("en-")]
    english.sort(key=lambda v: (v["Locale"], v["ShortName"]))
    for v in english:
        print(f"{v['ShortName']:<45}  {v['Gender']:<6}  {v['Locale']}")


async def main_async(args: argparse.Namespace) -> None:
    if args.list_voices:
        await list_voices()
        return

    MP3_DIR.mkdir(parents=True, exist_ok=True)
    voice = SUGGESTED_VOICES.get(args.voice, args.voice) or DEFAULT_VOICE

    scripts = chapter_scripts(args.chapter)
    for script in scripts:
        out = MP3_DIR / (script.stem + ".mp3")
        if out.exists() and not args.force:
            print(f"skip {out.name} (already exists; --force to overwrite)")
            continue
        text = script.read_text(encoding="utf-8")
        if not text.strip():
            print(f"skip {script.name} (empty)")
            continue
        print(f"synth {script.name} -> {out.relative_to(REPO)} ({len(text):,} chars)")
        await synth_one(text, out, voice, args.rate)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chapter", nargs="?", help="e.g. CH09 (default: all)")
    parser.add_argument(
        "--voice",
        default=DEFAULT_VOICE,
        help=(
            "Edge-TTS short name or one of: "
            + ", ".join(SUGGESTED_VOICES)
        ),
    )
    parser.add_argument(
        "--rate",
        default="+0%",
        help="Playback rate, e.g. -10%% slower, +15%% faster",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-synthesize even if the MP3 already exists",
    )
    parser.add_argument(
        "--list-voices",
        action="store_true",
        help="Print all en-* voices and exit",
    )
    args = parser.parse_args()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
