---
name: fact-currency-check
description: Verify time-sensitive figures in The Carbon Book against primary sources and update the chapter's "Sources and currency" table and CHANGELOG. Use when checking or refreshing perishable claims — prices, dates, regulatory states, COP outcomes, credit windows.
allowed-tools: Read Grep Glob WebSearch WebFetch Edit Bash(git diff:*)
---

# Fact & currency check for *The Carbon Book*

The book deliberately leans on perishable figures and commits (in `DISCLAIMERS.md`) to sourcing post-2024 facts. This procedure verifies and refreshes them.

## Procedure

1. **Identify perishable claims.** Prices (EUA, CCA, LCFS, credit tiers), regulatory states (rules adopted/stayed/repealed), dated commitments (COP outcomes, NDCs, standard versions), scenario figures, and any credit/program windows. Most are already listed in each chapter's `Sources and currency` table — start there, then scan the body for unlisted ones.
2. **Verify against authoritative sources.** Prefer **primary** sources (the regulator, standard-setter, statute, official decision) over secondary; use reputable secondary (law-firm alerts, IEA/UNEP/World Bank, Carbon Brief) to triangulate. Note publication dates.
3. **Record** value + **as-of date** + source for each.
4. **Reconcile across the whole book.** `grep` the figure/term across all chapters — a number often appears in body, glossary delta, and footer, and sometimes in two chapters (e.g., the 45Z window appeared in Ch7 and Ch12). Fix every instance and make them consistent.
5. **Update** the chapter's `Sources and currency` table (value, as-of, source); correct the body where wrong; add a sourced note where a claim was contested or changed.
6. **Log** substantive corrections in `CHANGELOG.md`.

## Principles
- Cite primary sources; always attach an "as of \<date\>".
- Don't assert a post-cutoff specific without verification; give a range and flag genuinely contested figures.
- A reconciliation isn't done until every cross-reference in the book agrees and the source is cited in the footer.
- Leave commit/push to the maintainer's workflow; report what you changed and the sources used.
