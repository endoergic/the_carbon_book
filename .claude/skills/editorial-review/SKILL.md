---
name: editorial-review
description: Review a chapter (or the current diff) of The Carbon Book for fit against the book's objective, house-style conformance, balance, and integrity. Use for an editorial pass on a chapter or pending changes.
allowed-tools: Read Grep Glob Bash(git diff:*) Bash(wc:*)
---

# Editorial review of *The Carbon Book*

Read `README.md` and `00_SYLLABUS.md` for the book's objective and the chapter's declared role. Then assess against this rubric. **Review only — propose fixes, don't apply them unless asked.** Lead with a one-line verdict, then prioritized findings, each with a `file:line` reference, what's wrong, and a concrete fix.

## Rubric

1. **Objective fit & role.** Does the chapter serve the book's stated purpose *and* deliver its own "What you should be able to do by the end" objectives? Does it sit correctly in the dependency arc?
2. **Proportionality, coverage balance & accessibility.** *Do a coverage census first* — estimate each Part's word-share and depth, then check: (a) is any Part disproportionate (>~30% of the chapter), or a niche over-weighted relative to the dominant real-world topic? — **but exempt a deliberate applied-learning capstone** (an end-of-chapter worked-examples section that exercises the chapter's framework against real cases): depth there is justified by the applied-learning payoff, not author momentum, and several pages is acceptable so long as it's framed as applied practice rather than new theory; (b) does the **depth gradient track importance, or just author momentum** — are thin sections starved while strong ones over-fatten? (depth should track how much a sub-topic matters, not how much the author had to say); (c) does **every major sub-topic/Part have its own Stop-and-check**? Its absence makes a section second-class and is a balance defect, not a nicety; (d) **persona accessibility** — for each reader-persona the chapter's subject implies (e.g. a refinery-markets expert, a steel practitioner, a project-finance reader), is there an on-ramp that lets them translate the material to their own world, *and* is the treatment accurate enough that a domain expert wouldn't dismiss it as stuck on the wrong nuance or skipping the obvious bridge?; (e) where the chapter has a geopolitics or market-structure dimension, is it covered evenly, or concentrated on one case while comparably-important ones are skipped? Does the climax/argument land, or deflate into detail?
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
