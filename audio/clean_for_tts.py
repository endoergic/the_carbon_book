#!/usr/bin/env python3
"""
Convert The Carbon Book chapter markdown into TTS-ready plain text.

Strips markdown markup, tables, code blocks, and end-matter (Sources/What's next),
then rewrites domain-specific notation (CO₂, tCO₂e, GtCO₂, currency-prefixed amounts,
em-dashes, etc.) into a form that reads naturally aloud.

Usage:
    python3 clean_for_tts.py                # cleans all CH*.md + APPENDIX_A
    python3 clean_for_tts.py CH09           # just one chapter
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "audio" / "scripts"

# Sections we drop entirely from the audio script — they're reference tables
# that read terribly and aren't part of the narrative.
END_MATTER_HEADINGS = (
    "Sources and currency",
    "What's next",
    "Glossary delta",
)


# ---------------------------------------------------------------------------
# Notation rewrites — order matters. Longest/most-specific patterns first.
# ---------------------------------------------------------------------------

# Mass-of-CO2 units. The unit prefix expansions are tuned for clarity over
# brevity: "gigatonnes of CO2-equivalent" reads better than "GtCO2e."
UNIT_REWRITES: list[tuple[re.Pattern[str], str]] = [
    # Per-tonne pricing: $X/tCO₂e → "X dollars per tonne of CO2-equivalent"
    (re.compile(r"\$(\d[\d,.\-–]*)\s*/\s*tCO[₂2]e"), r"\1 dollars per tonne of CO2-equivalent"),
    (re.compile(r"\$(\d[\d,.\-–]*)\s*/\s*tCO[₂2]"), r"\1 dollars per tonne of CO2"),
    (re.compile(r"€(\d[\d,.\-–]*)\s*/\s*tCO[₂2]e"), r"\1 euros per tonne of CO2-equivalent"),
    (re.compile(r"€(\d[\d,.\-–]*)\s*/\s*tCO[₂2]"), r"\1 euros per tonne of CO2"),
    (re.compile(r"£(\d[\d,.\-–]*)\s*/\s*tCO[₂2]e"), r"\1 pounds per tonne of CO2-equivalent"),
    (re.compile(r"£(\d[\d,.\-–]*)\s*/\s*tCO[₂2]"), r"\1 pounds per tonne of CO2"),
    # Bare per-tonne with no leading currency
    (re.compile(r"/\s*tCO[₂2]e\b"), r" per tonne of CO2-equivalent"),
    (re.compile(r"/\s*tCO[₂2]\b"), r" per tonne of CO2"),
    # Quantities of CO2
    (re.compile(r"\bGtCO[₂2]e\b"), "gigatonnes of CO2-equivalent"),
    (re.compile(r"\bGtCO[₂2]\b"), "gigatonnes of CO2"),
    (re.compile(r"\bMtCO[₂2]e\b"), "megatonnes of CO2-equivalent"),
    (re.compile(r"\bMtCO[₂2]\b"), "megatonnes of CO2"),
    (re.compile(r"\bktCO[₂2]e\b"), "kilotonnes of CO2-equivalent"),
    (re.compile(r"\bktCO[₂2]\b"), "kilotonnes of CO2"),
    (re.compile(r"\btCO[₂2]e\b"), "tonnes of CO2-equivalent"),
    (re.compile(r"\btCO[₂2]\b"), "tonnes of CO2"),
    # Other GHGs
    (re.compile(r"\bCO[₂2]e\b"), "CO2-equivalent"),
    (re.compile(r"\bCO[₂2]\b"), "CO2"),
    (re.compile(r"\bCH[₄4]\b"), "methane"),
    (re.compile(r"\bN[₂2]O\b"), "nitrous oxide"),
    (re.compile(r"\bSF[₆6]\b"), "sulfur hexafluoride"),
    (re.compile(r"\bNF[₃3]\b"), "nitrogen trifluoride"),
    (re.compile(r"\bH[₂2]O\b"), "water"),
    (re.compile(r"\bH[₂2]\b"), "hydrogen"),
    (re.compile(r"\bO[₂2]\b"), "oxygen"),
    (re.compile(r"\bN[₂2]\b"), "nitrogen"),
    # Chemistry
    (re.compile(r"\bCaCO[₃3]\b"), "calcium carbonate"),
    (re.compile(r"\bCaO\b"), "calcium oxide"),
    # Isotope shorthand
    (re.compile(r"δ¹³C"), "delta carbon-13"),
    (re.compile(r"C-14"), "carbon-14"),
    (re.compile(r"C-13"), "carbon-13"),
    (re.compile(r"C-12"), "carbon-12"),
    # Temperature
    (re.compile(r"(\d+(?:\.\d+)?)°C"), r"\1 degrees Celsius"),
    (re.compile(r"(\d+(?:\.\d+)?)°F"), r"\1 degrees Fahrenheit"),
    # Percent
    (re.compile(r"(\d+(?:\.\d+)?)%"), r"\1 percent"),
]

# Currency-prefixed amounts: "$190" → "190 dollars", "€72" → "72 euros".
# Run AFTER UNIT_REWRITES so per-tonne forms claim their dollars first.
# Region-prefixed dollar signs (C$, A$, S$, HK$, NZ$) come first so the plain
# "$" pattern doesn't strip the symbol before we can attach the region.
CURRENCY_REWRITES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bC\$(\d[\d,]*(?:\.\d+)?)"), r"\1 Canadian dollars"),
    (re.compile(r"\bA\$(\d[\d,]*(?:\.\d+)?)"), r"\1 Australian dollars"),
    (re.compile(r"\bS\$(\d[\d,]*(?:\.\d+)?)"), r"\1 Singapore dollars"),
    (re.compile(r"\bHK\$(\d[\d,]*(?:\.\d+)?)"), r"\1 Hong Kong dollars"),
    (re.compile(r"\bNZ\$(\d[\d,]*(?:\.\d+)?)"), r"\1 New Zealand dollars"),
    (re.compile(r"\$(\d[\d,]*(?:\.\d+)?)\s*billion\b", re.I), r"\1 billion dollars"),
    (re.compile(r"\$(\d[\d,]*(?:\.\d+)?)\s*million\b", re.I), r"\1 million dollars"),
    (re.compile(r"\$(\d[\d,]*(?:\.\d+)?)\s*trillion\b", re.I), r"\1 trillion dollars"),
    (re.compile(r"\$(\d[\d,]*(?:\.\d+)?[KMB]?)"), r"\1 dollars"),
    (re.compile(r"€(\d[\d,]*(?:\.\d+)?)"), r"\1 euros"),
    (re.compile(r"£(\d[\d,]*(?:\.\d+)?)"), r"\1 pounds"),
    (re.compile(r"¥(\d[\d,]*(?:\.\d+)?)"), r"\1 yuan"),
]

# Generic symbol → word substitutions applied after structural cleanup.
SYMBOL_REWRITES: list[tuple[str, str]] = [
    ("—", ", "),   # em-dash reads as a pause
    ("–", "-"),    # en-dash reads as a hyphen (number ranges, etc.)
    ("…", "..."),
    ("≈", " approximately "),
    ("≥", " at least "),
    ("≤", " at most "),
    ("×", " times "),
    ("·", " "),
    ("→", " leads to "),
    ("←", " from "),
    ("⇒", " implies "),
    (" ", " "),  # non-breaking space
    ("&", " and "),
    # subscript/superscript digits and isotope marks left in scientific names
    ("¹", "1"), ("²", "2"), ("³", "3"), ("⁴", "4"), ("⁵", "5"),
    ("⁶", "6"), ("⁷", "7"), ("⁸", "8"), ("⁹", "9"), ("⁰", "0"),
    ("₁", "1"), ("₂", "2"), ("₃", "3"), ("₄", "4"), ("₅", "5"),
    ("₆", "6"), ("₇", "7"), ("₈", "8"), ("₉", "9"), ("₀", "0"),
    ("“", '"'), ("”", '"'), ("‘", "'"), ("’", "'"),
]

# Common abbreviations that read poorly. Expand on first appearance is hard;
# we just expand everywhere, since repetition in a long-form audio doesn't hurt.
ABBREVIATION_REWRITES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bCh\.\s*(\d+)"), r"Chapter \1"),
    (re.compile(r"\bChs\.\s*(\d+)"), r"Chapters \1"),
    (re.compile(r"\bp\.\s*(\d+)"), r"page \1"),
    (re.compile(r"\bpp\.\s*(\d+)"), r"pages \1"),
    (re.compile(r"\be\.g\.,?"), "for example,"),
    (re.compile(r"\bi\.e\.,?"), "that is,"),
    (re.compile(r"\bvs\.\s"), "versus "),
    (re.compile(r"\betc\."), "et cetera"),
    (re.compile(r"\bcf\.\s"), "compare "),
    (re.compile(r"\bIPCC\b"), "I.P.C.C."),
    (re.compile(r"\bUNFCCC\b"), "U.N.F.C.C.C."),
    (re.compile(r"\bGHG\b"), "greenhouse gas"),
    (re.compile(r"\bGHGs\b"), "greenhouse gases"),
    (re.compile(r"\bGWP\b"), "global warming potential"),
    (re.compile(r"\bETS\b"), "E.T.S."),
    (re.compile(r"\bEU\b"), "E.U."),
    (re.compile(r"\bUS\b"), "U.S."),
    (re.compile(r"\bUK\b"), "U.K."),
    (re.compile(r"\bCBAM\b"), "C.B.A.M."),
    (re.compile(r"\bCCS\b"), "C.C.S."),
    (re.compile(r"\bCCUS\b"), "C.C.U.S."),
    (re.compile(r"\bCDR\b"), "C.D.R."),
    (re.compile(r"\bDAC\b"), "direct air capture"),
    (re.compile(r"\bBECCS\b"), "BEX"),  # awkward acronym; pronounce as a word
    (re.compile(r"\bSAF\b"), "saff"),
    (re.compile(r"\bVCM\b"), "voluntary carbon market"),
    (re.compile(r"\bSCC\b"), "social cost of carbon"),
    (re.compile(r"\bSBTi\b"), "S.B.T.i."),
    (re.compile(r"\bPCAF\b"), "P-CAF"),
    (re.compile(r"\bLCFS\b"), "L.C.F.S."),
    (re.compile(r"\bRGGI\b"), "Reggie"),  # this is genuinely how it's said
    (re.compile(r"\bCORSIA\b"), "Corsia"),
    (re.compile(r"\bFEOC\b"), "F.E.O.C."),
    (re.compile(r"\bAD/CVD\b"), "A.D. C.V.D."),
    (re.compile(r"\bFID\b"), "F.I.D."),
    (re.compile(r"\bPPA\b"), "P.P.A."),
    (re.compile(r"\bPPAs\b"), "P.P.A.s"),
    (re.compile(r"\bREC\b"), "R.E.C."),
    (re.compile(r"\bRECs\b"), "R.E.C.s"),
    (re.compile(r"\bEPA\b"), "E.P.A."),
    (re.compile(r"\bSEC\b"), "S.E.C."),
    (re.compile(r"\bCARB\b"), "Carb"),
    (re.compile(r"\bSB\s*253\b"), "S.B. 253"),
]


# ---------------------------------------------------------------------------
# Structural cleanup
# ---------------------------------------------------------------------------

def strip_end_matter(text: str) -> str:
    """Drop everything from the first end-matter heading onward."""
    lines = text.splitlines()
    cut = len(lines)
    for i, line in enumerate(lines):
        m = re.match(r"^#+\s+(.+?)\s*$", line)
        if m and any(m.group(1).startswith(h) for h in END_MATTER_HEADINGS):
            cut = i
            break
    return "\n".join(lines[:cut])


def strip_metadata_block(text: str) -> str:
    """Drop the opening Track/Prerequisites/What you should be able to do block.

    These read like a syllabus header, not part of the chapter narrative.
    """
    lines = text.splitlines()
    # Find the first '---' separator that closes the header block.
    for i, line in enumerate(lines):
        if i > 2 and line.strip() == "---":
            return "\n".join(lines[: 1] + lines[i + 1 :])  # keep the H1 title
    return text


def strip_tables(text: str) -> str:
    """Remove markdown tables wholesale.

    Tables don't survive linear reading. The Sources-and-currency footer is
    already gone; anything left tends to be a comparison table that the
    surrounding prose already summarizes in words.
    """
    out: list[str] = []
    in_table = False
    for line in text.splitlines():
        is_table_row = line.lstrip().startswith("|") and line.rstrip().endswith("|")
        if is_table_row:
            in_table = True
            continue
        # The separator line ("|---|---|") also matches above.
        if in_table and not line.strip():
            in_table = False
            out.append("")
            continue
        out.append(line)
    return "\n".join(out)


def strip_code_and_math(text: str) -> str:
    """Remove fenced code blocks and $$...$$ math blocks.

    Inline math ($...$) is NOT generically stripped: the dollar sign is far
    more common as a currency marker in this book than as a math delimiter,
    and the only inline math we'd risk seeing is in chapter 12, which has
    none.
    """
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(
        r"\$\$.*?\$\$",
        "(See the chapter text for the chemical equation.)",
        text,
        flags=re.S,
    )
    text = re.sub(r"`([^`]+)`", r"\1", text)
    return text


def strip_markdown_markup(text: str) -> str:
    """Drop horizontal rules, headings markers, list bullets, blockquotes,
    bold/italic markers — anything that's syntax-only."""

    out: list[str] = []
    for raw in text.splitlines():
        line = raw

        # Horizontal rule
        if re.match(r"^-{3,}\s*$", line.strip()):
            out.append("")
            continue

        # Headings: keep the text, drop the # marks. Add a short blank line so
        # the narrator pauses between sections. Strip any **bold** markers
        # that wrapped the heading text in the source.
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            heading_text = m.group(2)
            heading_text = re.sub(r"\*\*([^*]+)\*\*", r"\1", heading_text)
            heading_text = re.sub(r"(?<!\w)\*([^*]+)\*(?!\w)", r"\1", heading_text)
            out.append("")
            out.append(heading_text + ".")
            out.append("")
            continue

        # Blockquote
        line = re.sub(r"^\s*>\s?", "", line)

        # List bullets
        line = re.sub(r"^\s*[-*+]\s+", "", line)
        line = re.sub(r"^\s*\d+\.\s+", "", line)

        # Bold/italic markers (** and __ and single * / _ around words).
        # Be careful not to eat asterisks inside math; math is already stripped.
        line = re.sub(r"\*\*([^*]+)\*\*", r"\1", line)
        line = re.sub(r"__([^_]+)__", r"\1", line)
        line = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", r"\1", line)
        line = re.sub(r"(?<!\w)_([^_\n]+)_(?!\w)", r"\1", line)

        # Markdown links: [text](url) → text
        line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
        # Footnote refs (uncommon in this book but cheap to handle)
        line = re.sub(r"\[\^[^\]]+\]", "", line)

        out.append(line)
    return "\n".join(out)


def normalize_whitespace(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

_ACRONYM_GLOSS = re.compile(r" \(([A-Z]{2,6}[a-z]?)\)")


def _strip_acronym_glosses(text: str) -> str:
    """Drop parenthetical acronym definitions like "social cost of carbon (SCC)".

    In writing they cue the reader to a shorthand; in audio they read as
    "social cost of carbon S.C.C.", which is just noise once the abbreviation
    is being expanded inline everywhere else.
    """
    return _ACRONYM_GLOSS.sub("", text)


def _collapse_punctuation(text: str) -> str:
    """Clean up artifacts from em-dash → comma substitution and similar."""
    text = re.sub(r",\s*,", ",", text)
    text = re.sub(r"\s+,", ",", text)
    text = re.sub(r"\.{4,}", "...", text)
    return text


def apply_rewrites(text: str) -> str:
    text = _strip_acronym_glosses(text)
    for pattern, repl in UNIT_REWRITES:
        text = pattern.sub(repl, text)
    for pattern, repl in CURRENCY_REWRITES:
        text = pattern.sub(repl, text)
    for pattern, repl in ABBREVIATION_REWRITES:
        text = pattern.sub(repl, text)
    for src, dst in SYMBOL_REWRITES:
        text = text.replace(src, dst)
    text = _collapse_punctuation(text)
    return text


def clean(text: str) -> str:
    text = strip_end_matter(text)
    text = strip_metadata_block(text)
    text = strip_code_and_math(text)
    text = strip_tables(text)
    text = strip_markdown_markup(text)
    text = apply_rewrites(text)
    text = normalize_whitespace(text)
    return text


def chapter_files(arg: str | None) -> list[Path]:
    if arg:
        matches = sorted(REPO.glob(f"{arg}*.md"))
        if not matches:
            print(f"No file matched: {arg}", file=sys.stderr)
            sys.exit(1)
        return matches
    # CH NN _ pattern — avoids picking up CHANGELOG, CONTRIBUTING, etc.
    chapters = sorted(REPO.glob("CH[0-9][0-9]_*.md"))
    appendices = sorted(REPO.glob("APPENDIX_*.md"))
    return chapters + appendices


def main() -> None:
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    files = chapter_files(arg)
    for src in files:
        cleaned = clean(src.read_text(encoding="utf-8"))
        out = OUT_DIR / (src.stem + ".txt")
        out.write_text(cleaned, encoding="utf-8")
        words = len(cleaned.split())
        minutes = words / 150  # ~150 wpm narration
        print(f"{src.name} -> {out.relative_to(REPO)} ({words:,} words, ~{minutes:.0f} min)")


if __name__ == "__main__":
    main()
