---
name: carbon-book-chapter
description: Draft or revise a chapter of The Carbon Book in house style. Use when writing a new chapter, restructuring an existing one, or making chapter content conform to the book's template, voice, and conventions.
allowed-tools: Read Grep Glob Edit Write
---

# Drafting a chapter of *The Carbon Book*

You are writing for a **professional in an adjacent field** (climate, energy, finance, policy, tech) who wants comprehensive depth without an undergraduate ramp. Pedagogy is Socratic and conversational. Read `00_SYLLABUS.md` and `README.md` first for the chapter's place in the arc and its prerequisites.

## Length & balance
- Match the neighbors: the drafted chapters run ~6,000–9,000 words (the syllabus's 12–15k is aspirational). Don't pad.
- **Proportionality matters.** No single sub-topic should dominate. If a Part exceeds ~30% of the chapter, it's probably an appendix in disguise (see how the fuel-standard material was moved to `APPENDIX_A_*`).

## The template (in this order)
1. `# Chapter N — Title`
2. A bold metadata block: `**Track:**` (A Foundations/Physical · B Climate Liability · C Forward View), `**Prerequisites:**` (name chapters + why), `**What you should be able to do by the end:**` (4–6 capability bullets).
3. `---`
4. `## Why this chapter exists` — motivate it; state how it's organized.
5. Numbered `# Part N: ...` sections with `##`/`###` subsections.
6. `## **Stop-and-check N.X**` blocks (one per Part, ~3–4 questions; the **last is `**Socratic prompt:**`**). **Each block is immediately followed by an `**Answers**` block** (book-wide convention — see the format below).
7. `# Closing exercise` — three numbered takeaways.
8. `# What this chapter simplified` — honest list of what you compressed/omitted.
9. `# Glossary delta (Chapter N)` — new terms defined; cross-reference (don't duplicate) terms defined earlier.
10. `# Sources and currency` — a table of the time-sensitive claims (see below).
11. `# What's next` — chain to the following chapter(s).

## Stop-and-check answer format (match exactly)
```
4. **Socratic prompt:** <question>

**Answers**

1. <one substantive paragraph, ~50–110 words, grounded in the chapter>

2. ...

4. <models the trade-off and names the decisive variables — not a single "right" answer>
```

## Voice
- Measured and explanatory. For contested topics use the **"the critique / the defense / the empirical record"** structure.
- Honest about uncertainty: distinguish *what works, what doesn't, what we don't know*.
- Every sentence should inform. No hype, no "great question," no filler.

## Conventions
- Cross-reference other chapters as `(Ch. X)`; declare prerequisites explicitly.
- **Unit discipline** (consult the `carbon-domain` skill): tCO₂ vs tCO₂e vs tC; state GWP horizon; $/tCO₂ vs $/tC; gCO₂e/MJ; per-gallon vs per-tonne.
- Apply the framing question to every claim: *which carbon, measured how, against what baseline, by whom, how durable?*

## Perishable facts — keep them quarantined
- **Do not hardcode 2025+ figures (prices, regulatory states, COP outcomes, credit windows) into prose without sourcing.** Put each in the `Sources and currency` table: `| Claim | Value as stated | As-of | Primary source to verify against |`.
- Verify any time-sensitive figure with the **`fact-currency-check`** skill or the **`carbon-researcher`** subagent before asserting it. When in doubt, give a range and flag it.

## After drafting
- Add the chapter's new terms to `GLOSSARY.md` and a bullet to `CHANGELOG.md`.
- Run the **`editorial-review`** skill on the draft before considering it done.
- Commit following the repo's contribution workflow.
