# Carbon Markets Glossary

*Running glossary for the carbon textbook project. New terms are added as we cover them.*
*Last updated: 2026-05-23*

---

## Fuel-standard & compliance regimes

**RFS (Renewable Fuel Standard)** — US federal volumetric biofuel mandate. Obligated parties (refiners/importers) must retire enough RINs each year to meet a volume target. Crucially, it is a **step function**: a fuel either clears the lifecycle-reduction threshold for its category or it doesn't, and being *cleaner than the threshold earns nothing extra*.

**RIN (Renewable Identification Number)** — The tradable serial-number credit under the RFS. Attached to a volume of renewable fuel at production, detached at blending. D-codes (D3 cellulosic, D4 biomass-based diesel, D5 advanced, D6 conventional, D7 cellulosic diesel) classify by fuel/feedstock. No counterfactual additionality test — qualification is volumetric.

**LCFS (Low Carbon Fuel Standard)** — Compliance program (California first; now Oregon, Washington, New Mexico, and expanding). Credits a fuel for beating a declining annual **carbon-intensity benchmark**, denominated in tCO2e. Unlike RFS, it is a **continuous (sloped) function**: credits scale with *distance below the benchmark*, so cleaner fuels and ongoing improvements earn proportionally more. Pays for *how clean*, not *how much*.

**REDIII (Renewable Energy Directive III)** — EU framework setting binding renewable transport sub-targets, including an RFNBO (e-fuel) sub-mandate. Transposed into national obligations, so the tradable instrument varies by member state. Largely uses **default CI values by feedstock pathway** (with actual-value/disaggregated-value options), rather than continuous plant-specific re-scoring.

**ReFuelEU Aviation** — EU escalating SAF *blending mandate* on fuel suppliers at EU airports: 2% (2025) rising toward 70% (2050), with a dedicated synthetic/eSAF sub-mandate. A volume-style obligation (closer to RFS logic than LCFS) — it rewards being a qualifying SAF, not continuous operator improvement.

**CORSIA (Carbon Offsetting and Reduction Scheme for International Aviation)** — ICAO scheme for international aviation. Notable as the one major compliance framework where a SAF lifecycle benefit and a VCM-style offset meet in the same place. Phased: pilot 2021–23, first phase 2024–26, second phase 2027–35.

**FuelEU Maritime** — EU regulation (effective 2025) setting declining GHG-intensity targets for energy used by ships calling at EU ports. Until 2033, renewable fuels of non-biological origin (e.g., green ammonia) can count *double* toward a ship's GHG-intensity target — a temporary multiplier incentive.

**EU ETS (Emissions Trading System)** — EU cap-and-trade; now extended to maritime. Tank-to-wake SAF emissions are exempt, which interacts with ReFuelEU to shape SAF demand.

**45Z (Clean Fuel Production Credit)** — US production tax credit for low-CI transport fuels (incl. SAF), effective 2025, in place through 2029. Value *scales with CI* — up to ~$1.00/gal for SAF depending on the emissions profile. Replaced the prior 40B blender-style SAF credit.

**Waste Emissions Charge (WEC)** — US fee on excess methane emissions from large oil & gas facilities. A regulatory "stick" complementing the fuel-credit "carrots."

**CBAM (Carbon Border Adjustment Mechanism)** — EU border tariff on the embedded carbon of certain imports, designed to prevent carbon leakage. Referenced as an analogy for how regulation can follow/capture value once an industry establishes itself.

---

## Fuels & pathways

**SAF (Sustainable Aviation Fuel)** — Lower-lifecycle-emission jet fuel. Cuts lifecycle CO2 ~65–94% vs conventional Jet A-1 depending on pathway/feedstock.

**HEFA (Hydroprocessed Esters and Fatty Acids)** — Dominant commercial SAF/renewable-diesel route, made from fats, oils, and greases (incl. used cooking oil, tallow). Mature; mandates increasingly cap the HEFA share to push newer pathways.

**eSAF / RFNBO (Renewable Fuels of Non-Biological Origin)** — Synthetic e-fuels (power-to-liquid) from renewable electricity + captured CO2 / green hydrogen. ReFuelEU has a dedicated sub-mandate. Typically near-zero CI (clean, but not deeply negative).

**Biomethane / RNG (Renewable Natural Gas)** — Methane captured from sources like dairy manure or landfills and upgraded to pipeline quality. Dairy/landfill pathways can have **deeply negative CI** because capturing methane that would otherwise escape earns a large lifecycle avoided-emissions credit.

**eAmmonia (green ammonia)** — Ammonia produced from green hydrogen; a leading candidate zero-carbon *marine* fuel. Burns without CO2, but production is emissions-intensive unless green. Requires ~3x the volume of marine gas oil for equal energy.

**UCO (Used Cooking Oil)** — Waste feedstock for HEFA. Low CI, but the locus of significant fraud risk in the EU (virgin oil relabeled as UCO to claim the better CI score).

---

## Core carbon-accounting concepts

**Carbon Intensity (CI)** — Lifecycle GHG emissions of a fuel per unit energy (gCO2e/MJ). The metric driving LCFS credit volume. Can be **negative** (e.g., dairy biomethane) when the pathway prevents emissions worse than those it creates.

**Negative CI** — When a fuel's lifecycle score drops below zero because it prevents a large quantity of emissions (e.g., destroying methane that would otherwise have escaped) that outweighs the emissions of producing and burning it. Effectively a counterfactual/avoidance claim embedded inside a fuel score — and it carries the same integrity vulnerabilities (additionality, perverse incentives) as a VCM avoidance credit.

**CI benchmark / ratchet** — The annually declining allowed-CI line in an LCFS-style program. As it drops, credits earned by any fixed-CI fuel shrink over time, and deficits grow for fossil fuels — the engine of long-term credit demand.

**Step function vs. continuous function** — The key structural distinction between regimes. RFS/ReFuelEU = step (pass/fail qualification, no reward for over-performance). LCFS = continuous (reward scales with distance below benchmark). Determines whether continuous operational improvement is monetizable inside the regime.

**Default value vs. actual value** — In REDIII, a fuel can be scored by a published default CI (by feedstock pathway) or by certifying its plant-specific actual value. The *gap between them* is where the "EU white space" question lives.

---

## Voluntary Carbon Market (VCM) integrity

**Additionality** — The test of whether a reduction would have happened *without* the carbon-credit revenue. Not settled case law — it is an administrative judgment by private standard bodies (Verra, Gold Standard) applied by verifiers (VVBs). **The inversion:** the more independent revenue pathways a project has, the *less* additional any single VCM credit is — because some other stream already caused the reduction. Counterintuitively, the most bankable projects are the least additional.

**Financial additionality** — The specific test that a project clears its hurdle rate *only when* credit revenue is included. The cleanest fuel-VCM case: a pre-FID project that doesn't pencil on the compliance stack alone but does once VCM is stacked — assessed at the FID moment.

**Double counting (three distinct failures):**
- **Double issuance** — two credits issued for the same physical tonne.
- **Double claiming** — the same reduction counted toward two goals (e.g., a national compliance obligation *and* a corporate Scope 3 claim).
- **Double monetization** — being paid twice for one environmental good.

**Book-and-claim** — Unbundling a fuel's environmental attribute from its physical molecules so the attribute can be sold/claimed separately. Enables Scope 3 claims and cross-geography value capture (e.g., SAF certificates, SAFc).

**Attribute (environmental attribute)** — The claimable emissions-reduction value of a fuel, separate from the physical fuel. Once a compliance regime "claims" an attribute (via a RIN, an LCFS credit, or a mandate), it is no longer available to sell into the VCM without double-counting.

**VVB (Validation and Verification Body)** — Independent auditor that validates a project's methodology/additionality and verifies its claimed reductions for a registry.

**Permanence / reversal** — Whether a stored/avoided tonne stays out of the atmosphere. Fuel-based reductions pass easily (combustion-displacement doesn't reverse), unlike forestry (fire, harvest). The asymmetry: fuels are permanent-by-nature but additionality-poor; forestry is reversal-prone but sometimes more additional.

**Unit mismatch (per-gallon vs. per-tonne)** — RIN and 45Z are quoted per gallon; LCFS and VCM credits per tCO2e. The SAF book-and-claim *certificate* price (~$1,500–3,500/tCO2e) is **not** a clean carbon-abatement price — it's an aviation-scarcity premium for a different claim. A HEFA gallon abates only ~0.0085 tCO2e, so naively multiplying the SAF cert price by a gallon's abatement implies an absurd ~$17/gal (more than the whole fuel + compliance stack). Always convert all instruments to one unit before comparing or stacking; the SAF cert is reference-only, not stackable against compliance credits.

**Regulatory-closure risk / stranding risk** — The danger that a VCM revenue stream built on a regulatory gap (a deregulated geography, or a methodology blind spot) terminates when regulation arrives or the methodology is revised — the same tonne becomes compliance-claimed, killing the credit. Every fuel-VCM "white space" thesis has a finite half-life because of this.
