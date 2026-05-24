---
name: editorial-review
description: Review a chapter (or the current diff) of The Carbon Book for fit against the book's objective, house-style conformance, balance, and integrity. Use for an editorial pass on a chapter or pending changes.
allowed-tools: Read Grep Glob Bash(git diff:*) Bash(wc:*)
---

# Editorial review of *The Carbon Book*

Read `README.md` and `00_SYLLABUS.md` for the book's objective and the chapter's declared role. Then assess against this rubric. **Review only — propose fixes, don't apply them unless asked.** Lead with a one-line verdict, then prioritized findings, each with a `file:line` reference, what's wrong, and a concrete fix.

## Rubric

1. **Objective fit & role.** Does the chapter serve the book's stated purpose *and* deliver its own "What you should be able to do by the end" objectives? Does it sit correctly in the dependency arc?
2. **Proportionality & balance.** Is any Part disproportionate (>~30% of the chapter)? Is a niche over-weighted relative to the dominant real-world topic? Does the climax/argument land, or does it deflate into detail?
3. **Template completeness.** Present and correct: metadata block (Track, Prerequisites, objectives); `Why this chapter exists`; numbered Parts; every Stop-and-check has an `**Answers**` block; `Closing exercise`; `What this chapter simplified`; `Glossary delta`; `Sources and currency` footer; `What's next` chains correctly.
4. **Voice conformance.** Measured; uses "critique / defense / empirical record" for contested points; honest about uncertainty; no hype or filler.
5. **Cross-reference & prerequisite integrity.** Do `(Ch. X)` references resolve and point to the right place? Are prerequisites declared? Do forward-promises ("developed in Ch. Y") get paid off?
6. **Factual & unit sanity.** Dimensional checks (energy density, $/tCO₂ vs $/tC, per-gallon vs per-tonne); internal consistency (counts, totals, dates); flag every time-sensitive figure that isn't in the `Sources and currency` table for `fact-currency-check`. Consult the `carbon-domain` skill for the distinctions the book commits to.
7. **Cross-chapter de-duplication.** Does material repeat another chapter without intent? Should it be cross-referenced or relocated?
8. **Glossary & CHANGELOG sync.** New terms in `GLOSSARY.md`? Substantive change logged in `CHANGELOG.md`?

## Output
- **Verdict:** one line (ship / fix-then-ship / needs work).
- **Findings:** ordered by severity. For each: `file:line` · issue · suggested fix.
- Separate genuine errors (units, broken refs, factual) from style/balance suggestions.
