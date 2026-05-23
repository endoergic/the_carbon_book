# Companion Note — LATAM HEFA Bridge Model

*Reads alongside `latam_hefa_model.xlsx`. Built 2026-05-23. Numbers are illustrative placeholders.*

## What the model is for

It answers your original question — *is there stackable revenue to improve a renewable-fuel project's economics, and where?* — by showing the **same physical HEFA plant** under three destinations and then walking the **bridge-to-compliance handoff** over ten years.

## The three destinations (Destination Compare tab)

| | US (RIN+LCFS+45Z) | EU export (ReFuelEU) | Pure VCM bridge |
|---|---|---|---|
| Net margin / gal (placeholder) | ~$2.23 | ~$0.45 | ~$0.57 |
| Clears FID? | **Yes** | No | **Yes** |
| VCM additional? | **No — bankable without it** | n/a | **Yes — VCM is the swing** |

The point is not the specific numbers (swap them) — it's the **pattern**: the destination with the richest compliance stack (US) is exactly where a voluntary credit is *least* defensible, because the project already clears FID without it and the attribute is already claimed by the RIN/LCFS credit. The deregulated bridge is the only place the VCM credit is the decisive, additional dollar. **That is the additionality inversion, shown in numbers.**

## The unit-mismatch lesson (built into the tab on purpose)

Building this surfaced a real trap worth keeping: **RIN and 45Z are quoted per gallon; LCFS and VCM are quoted per tonne CO₂e** — and the SAF *book-and-claim certificate* price (~$1,500–3,500/tCO₂e) is **not** a clean carbon-abatement price at all. It's an aviation-scarcity premium for a different kind of claim.

A HEFA gallon abates only ~0.0085 tCO₂e. Multiply the SAF cert price by that and you get ~$17/gal — *more than the entire fuel plus its whole compliance stack.* That absurd result is the lesson: **the units lie.** Before you ever stack or compare these instruments, convert everything to one unit. The model does this in the mismatch block (RIN ≈ $95/t, LCFS $63/t, VCM proxy $50/t are comparable; the SAF cert at $2,000/t is flagged as non-comparable).

So the model uses a **realistic per-tonne VCM proxy ($50/t default, a blue input)** for the bridge economics, and shows the SAF certificate price separately as reference-only.

## The handoff (Bridge Handoff tab)

The genuinely novel piece. The bridge case earns VCM revenue **only during the bridge window** (default 4 years, until local regulation arrives). When the regime shows up, it **claims the attribute** — VCM revenue stops, and a **stranding haircut** (default 40%) models the value lost in the transition (uncompensated claim, low compliance price, or a coverage gap). After that, the project lives on the post-handoff compliance value.

The discipline: **underwrite the bridge on a finite VCM stream plus the haircut compliance stream that follows — never on VCM revenue continuing forever.** The two yellow drivers to stress are the bridge-window length and the stranding haircut.

## The five inputs that move everything (all yellow on the Inputs tab)

1. Feedstock + opex ($/gal) — the swing cost.
2. LCFS credit price ($/tCO₂e).
3. VCM bridge proxy ($/tCO₂e) — keep this realistic, not the SAF cert headline.
4. Bridge window (years).
5. Stranding haircut (%).

## What to verify before this goes near a real decision

Everything in the honesty flags on the READ ME tab — chiefly that the cost/CI/hurdle figures are generic placeholders, the credit prices move weekly, and the whole bridge case assumes a registry methodology accepts it *and* additionality survives. If the project pencils without the VCM line, the VCM credit is by definition non-additional — the model will tell you so in the verdict row.
