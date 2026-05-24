# Appendix A — Fuel-Standard Compliance Operations and the Fuel–VCM Boundary

**Companion to:** Chapter 7 Part 8 (fuel-standard compliance regimes) and Chapter 8 Part 8 (fuel-based credits and the additionality inversion).
**What this appendix is:** The two markets chapters establish the *concepts* — the step-function vs. continuous-function distinction, the additionality inversion, attribute claiming, and the three structural types of voluntary white space. This appendix collects the *operational* detail a renewable-fuel project developer or analyst needs to act on those concepts: how carbon-intensity (CI) optimization translates into credit revenue, when plant-specific certification pays for itself, how to route product across markets, how any producer in the world can access California's LCFS, how the LCFS design is diffusing internationally, and how a voluntary market can actively help bring a future compliance regime into being.

It is deliberately housed outside the chapter narrative because its register is practitioner/advisory rather than pedagogical, and because keeping it in one place avoids the duplication that arises when the same CARB-registration walkthrough appears in two chapters. Read Ch. 7 Part 8 and Ch. 8 Part 8 first; come here when you need the mechanics.

> **Prerequisite concepts (from the chapters):** step function vs. continuous function (Ch. 7 Part 8); the additionality inversion, attribute claiming, double counting, and the three white-space types — geographic gap, boundary gap, pre-FID financial swing (Ch. 8 Part 8).

---

## A.1 Carbon intensity as a continuous lever

LCFS-style systems reward every increment of CI improvement, not just threshold crossing. This creates a quantifiable ROI framework for capital and operational decisions — the practical consequence of the "continuous function" design from Ch. 7.

**A worked LCFS value.** Take a CI of 20 gCO₂e/MJ (roughly what well-optimized US HEFA SAF achieves with waste feedstocks and renewable process energy). The gap below California's current SAF benchmark (~86.6 gCO₂e/MJ as of 2025, per CARB Title 17 §95484) is roughly 66.6 gCO₂e/MJ. SAF carries roughly **43 GJ of energy per tonne** (~0.13 GJ per gallon). The LCFS credit value is the CI gap × energy × credit price:

- **Per GJ:** 66.6 gCO₂e/MJ × 1,000 MJ/GJ ÷ 1,000,000 g/t × $63/tCO₂e = **$4.20 per GJ** of fuel. (Credit price: ~$63/tCO₂e Q1 2026; ~$66/tCO₂e week of May 11–17, 2026 per CARB weekly report — use current CARB data.)
- **Per tonne of SAF:** $4.20/GJ × 43 GJ/t ≈ **$181 per tonne**.
- **Per gallon:** $4.20/GJ × 0.13 GJ/gal ≈ **$0.55 per gallon**, purely from LCFS.

The same gallon earns a 45Z credit of ~$0.90–1.00/gal at that CI level. The RIN, if the fuel qualifies under D4 (biomass-based diesel) or D7 (cellulosic diesel), adds another $0.40–1.50/gal depending on current D-code pricing. (Always convert instruments to a common per-tonne basis before adding them — see Ch. 8 Part 8, "The unit mismatch trap.")

Three variables determine how much LCFS value a gallon captures:

**1. Feedstock CI.** Feedstock choice is the largest single CI driver. Approximate lifecycle starting-point CIs for common inputs (before process optimization):

| Feedstock | Approximate CI (gCO₂e/MJ) |
|---|---|
| Used cooking oil (UCO) | 15–25 |
| Tallow / animal fats | 20–35 |
| Canola / rapeseed | 55–75 |
| Soy oil | 55–80 |
| Palm oil | 40–80 (varies widely with land-use accounting) |
| Corn stover | 10–35 |
| Dedicated energy crops | 30–60 |

UCO and animal fats sit at the top of the CI hierarchy because they carry no feedstock-production allocation in lifecycle accounting — they are waste streams. The premium attached to low-CI feedstocks reflects this: UCO commands a significant market premium over virgin oils in the SAF and biodiesel sectors, and that premium is partly a proxy for LCFS credit capture.

**2. Process energy.** Process energy — heat, steam, hydrogen — is the second-largest CI driver and the most tractable through investment. Switching from fossil natural gas to renewable natural gas (RNG) for process heat can reduce plant CI by 10–20 gCO₂e/MJ. Green hydrogen replacing fossil hydrogen in hydroprocessing cuts CI by 15–30 gCO₂e/MJ. The question is always cost per incremental CI point: at what credit price does the capital investment pay back?

**3. Upstream Scope 3 improvements.** Some LCFS methodologies allow crediting of upstream changes — certified sustainable feedstock supply chains, methane-leak reduction at feedstock production. These are harder to verify and the CI credit is smaller, but they can matter at the margin for producers already near the compliance-grade threshold.

---

## A.2 Actual-value certification: when it pays

Every major regime — California LCFS, Oregon CFP, Canadian Clean Fuel Regulation, REDIII — publishes default CI values by feedstock-pathway combination. A HEFA producer using UCO has a published default CI it can use without certification. The question is whether investing in plant-specific actual-value certification (CA LCFS calls this a "Tier 2" or full Lifecycle Analysis registration) is worth the cost.

The calculation is straightforward:

- **Registration cost:** ~$50,000–200,000 one-time, plus $20,000–50,000/year in ongoing monitoring, data management, and verification fees.
- **CI uplift:** if the plant's actual CI is 10 gCO₂e/MJ below the published default (common for optimized plants), and the plant produces 50,000 tonnes of SAF per year:

  50,000 t × 43,000 MJ/t × 10 gCO₂e/MJ ÷ 1,000,000 g/t × $63/tCO₂e ≈ **$1.35 million per year** in additional LCFS credit value (≈ 21,500 tCO₂e × $63). (At the May 2026 spot of ~$66/tCO₂e the figure is ~$1.42 million; use current CARB weekly price.)

At those numbers, the one-time registration cost is recovered within roughly **two to three months** of the additional credit revenue even at the top of the cost range; ongoing verification fees are a small fraction of annual uplift. Volume and CI uplift determine whether the investment makes sense; for large producers with meaningfully better-than-default performance, actual-value certification is almost always the right call.

---

## A.3 Market routing: California full stack vs. federal vs. EU

A US producer selling into multiple markets faces a routing decision: which market for which tonne of physical product captures the most compliance revenue?

| Routing | Instruments accessible | Approx. combined value range ($/gal SAF at CI ~20 g/MJ) |
|---|---|---|
| California | LCFS + RIN (if eligible) + 45Z | $2.50–3.50 |
| Oregon / Washington | CFP/CFS + RIN + 45Z | $1.80–2.80 |
| Federal only (no LCFS) | RIN + 45Z | $1.30–2.00 |
| EU | ReFuelEU compliance + REDIII RFNBO premium | €1.00–2.50/gal (€0.30–0.90 REDIII premium; €0.70–1.60 SAF mandate scarcity) |
| Canada | CFR credit + potential provincial programs | CAD $1.50–2.50/gal |

California dominates for producers that can access it. The binding constraint is physical logistics: the closer a producer is to the California fuel market, the lower the transport differential to route volume there rather than to commodity markets. This is why several Latin American UCO-HEFA projects specifically target California as the first export market — not just because of SAF demand but because the LCFS + 45Z stack provides materially better economics than any other accessible market.

---

## A.4 LCFS geographic reach: any producer, anywhere

A widespread misunderstanding — even among carbon-market professionals — is that LCFS is a California program and therefore only applies to fuel producers operating in or near California. This is incorrect in a way that has material commercial consequences, and it is the operational basis for the "apparent vs. true geographic gap" distinction in Ch. 8 Part 8.

**Any fuel producer in the world can access California LCFS credits**, provided they register a compliant CI pathway with CARB and the fuel is physically delivered into the California transport fuel supply. The geographic constraint is on *delivery*, not on *production*. A Brazilian UCO-HEFA producer, a Canadian canola-biodiesel plant, or a European eSAF facility can all earn LCFS credits if they export into California.

### The CARB pathway registration process

Registration is a defined administrative process, not an arbitrary barrier:

1. **Identify applicable pathway and methodology.** CARB maintains the CA-GREET lifecycle model. Most feedstock-technology combinations have a designated methodology; novel pathways may require a provisional application.
2. **Compile plant-specific inventory data.** Typically 12 months of verified operational data: feedstock sourcing records, energy consumption, process flows, any biogas utilization, transportation distances to the California delivery point.
3. **Engage a third-party CA-accredited LCA specialist.** CARB requires a certified third-party verifier to review the application. This is not a VCM verifier — it is a CARB-accredited engineer, typically affiliated with a specialized consultancy.
4. **Submit application to CARB.** CARB reviews for completeness, may issue comment letters, and issues a formal CI score. For well-documented applications on established pathways, approval typically takes 6–18 months.
5. **Execute Fuel Pathway Registration Agreement.** A legal agreement binding the producer to annual re-verification and allowing CARB to audit records.
6. **Maintain annual verification and reporting.** Ongoing verified annual reports; CI is re-confirmed or adjusted annually.

**Costs:** one-time registration (LCA consultant, legal, application fee) ~$50,000–200,000 depending on pathway complexity and whether data-collection infrastructure already exists; ongoing ~$20,000–50,000/year. At California credit prices, a producer shipping as little as 5,000–10,000 tonnes/year of SAF typically recovers registration costs within the first credit cycle.

### Cascade to other programs

Registration cascades. Oregon's Clean Fuels Program and Washington's Clean Fuel Standard both accept CARB-registered pathways with simplified re-registration. New Mexico's pilot follows similar logic. Canada's Clean Fuel Regulation has a separate registration requirement but follows substantially similar (CA-GREET-compatible) LCA methodology, so plants that have assembled the CARB data package face reduced marginal effort. **A single investment in CARB pathway registration can unlock access to four or five distinct North American compliance programs.**

### Who has done it

The international producer base in the CARB registry is substantial:

- **Brazilian ethanol producers** (sugarcane) — the sugarcane lifecycle score in CA-GREET is materially lower than the corn-ethanol default, giving Brazilian exporters an LCFS advantage on volume imported into California. Several large mills have held registrations for over a decade.
- **Canadian canola-biodiesel producers** — canola-based FAME biodiesel scores well below the diesel benchmark; Canadian producers registered to access California credits and have been a consistent supply source.
- **European and Australian tallow/UCO-HEFA SAF producers** — as the SAF supply chain matured, low-CI European producers registered California pathways to access the LCFS premium on top of EU mandate compliance value; some hold simultaneous CARB and REDIII actual-value certifications.
- **Singapore and South Korean refiners** producing HEFA from waste feedstocks have begun CARB registration as part of California SAF supply agreements.

### Apparent vs. true geographic gap

This is the operational core of the Ch. 8 white-space analysis. Producers must distinguish:

- **Apparent geographic gap:** the producer *could* register a CARB pathway (6–18 months, ~$50–200k one-time) and access LCFS, but hasn't yet — because of information barriers, upfront cost, or lack of California commercial relationships. This gap can be closed by the producer and **should not be underwritten as permanent VCM white space.**
- **True geographic gap:** the producer genuinely cannot access any compliance regime because (a) the fuel type has no applicable CARB or equivalent methodology, (b) volume is too small to justify registration economics (typically under ~2,000 tonnes/year of SAF), or (c) physical delivery into any compliance jurisdiction is not commercially viable given logistics.

Category (a) is shrinking as CA-GREET expands coverage. Category (b) affects small producers. Category (c) is a real constraint for landlocked or remote projects. The practical takeaway: before declaring a project VCM-eligible on geographic-gap grounds, verify the producer *cannot* access LCFS — not just that they *haven't yet*.

---

## A.5 The LCFS family beyond California

California's LCFS is not a one-off. It has become the template for a growing family of CI-based fuel standards. Understanding where the family reaches and where it is expanding is essential for multi-year compliance-revenue strategy.

### North American state expansion

- **Oregon Clean Fuels Program (CFP, 2016):** modeled closely on California's; initially gasoline/diesel substitutes, now includes SAF. Accepts CARB-registered pathways with simplified re-registration.
- **Washington Clean Fuel Standard (CFS, 2023):** CI-benchmark-plus-ratchet structure under HB 1091; CARB pathway cascade applies. A smaller fuel market than California's, but an industrial and maritime fuel base that is particularly relevant for RNG and potentially marine-fuel credits.
- **New Mexico (2023 pilot):** in rulemaking; if finalized, likely to follow the Oregon/Washington model of CARB pathway acceptance.
- **British Columbia (2010, expanded):** the Renewable and Low Carbon Fuel Requirements Regulation (RLCFR) predates California's LCFS in some respects; CI-based, revised multiple times. Canadian producers often hold both CARB and RLCFR registrations.

The expansion pattern is consistent: states with strong climate-policy infrastructure and significant ground-transport fuel markets adopt LCFS-type instruments as complements to cap-and-trade or carbon taxes, not substitutes.

### Canada: a national-scale CI fuel standard

Canada's **Clean Fuel Regulation (CFR)** came into force July 1, 2023 — the first national-scale fuel standard with a CI-based credit-generation mechanism in North America. It requires annual per-unit reductions in lifecycle CI for liquid fossil fuels, with credits generated by producers of qualifying low-CI fuels. Credits are denominated in tCO₂e (like LCFS, unlike RINs). The methodology tracks CA-GREET structure closely, and CARB data packages are substantially transferable. The CFR market is earlier and smaller than California's, but at national scale (Canada's liquid-fuel market is roughly 15% of the US market) it is a meaningful incremental revenue stream.

### The EU: step-function mandates with an actual-value CI layer

The EU has not adopted an LCFS equivalent — REDIII, ReFuelEU Aviation, and FuelEU Maritime are volume-mandate (step-function) structures. But REDIII contains an actual-value certification mechanism that creates a *partial* CI-based reward layer within the mandate system. Actual-value certification demonstrating GHG savings against the fossil comparator unlocks eligibility: REDIII Article 29 sets minimum thresholds of ≥50% for installations operational before October 2015, ≥60% for those starting from October 2015, and ≥65% for installations starting from January 1, 2021 — these apply to transport biofuels and bioliquids. (The 70%/80% thresholds cited in some secondary sources apply to electricity and heat from solid biomass, not to transport fuels.) Producers certifying savings substantially above the applicable floor — in the 80%+ range — distinguish themselves in tenders and offtake negotiations even within the volume-mandate structure; this premium is commercially meaningful but should not be cited as a statutory REDIII threshold. The practical effect: the actual-value premium manifests as offtake pricing power rather than a continuous per-gram credit stream — airlines and SAF buyers subject to ReFuelEU pay a premium for well-documented low-CI SAF because it provides compliance buffer and reputational credibility. (This is the "boundary gap" of Ch. 8 Part 8: the room left between default values and what the methodology can actually score.)

### Beyond North America and Europe

- **Singapore SAF Framework (2026):** the Civil Aviation Authority of Singapore (CAAS) enacted a SAF levy effective April 1, 2026, for flights departing from October 1, 2026, targeting a 1% SAF blend at Changi and Seletar airports, scaling to 3–5% by 2030. Given Singapore's position as Asia-Pacific's largest jet-fuel hub, this is the first significant Asia-Pacific blending mandate; CI-intensity thresholds rewarding actual-value certification are expected in subsequent rulemaking.
- **Japan SAF ambitions:** Japan has set a 10%-by-2030 SAF target and is engaging with lifecycle CI frameworks; METI's SAF supply-chain work overlaps with ICAO/CORSIA methodology.

### What makes LCFS logic portable

Not every jurisdiction can implement an LCFS. The enabling conditions:

1. **A liquid-fuel market large enough to sustain credit trading.** California's ~18–20 billion gallons/year of liquid transport fuel (approximately 13.4 Bgal gasoline in 2024 plus diesel and other fuels, per CEC/CARB data) provides the depth for a two-sided market; small jurisdictions face thin markets and price volatility.
2. **Regulatory capacity to administer lifecycle assessment.** CARB's CA-GREET infrastructure, enforcement apparatus, and LCA staff are not trivial institutional investments.
3. **A pre-existing low-carbon fuel supply capable of generating credits immediately.** Without early credit supply, the market has no price signal. California benefited from an existing ethanol and biodiesel sector.
4. **Political economy that tolerates per-unit price signals on transport fuels.** LCFS costs pass through to fuel marketers and ultimately consumers — politically sensitive where fuel prices are managed.

Where these conditions hold, LCFS logic is portable; where they don't, volume mandates (step-function) are more politically tractable even if less efficient. The trajectory for the family is upward: Canada's national CFR, Washington's adoption in 2023, and Singapore's 2026 SAF levy suggest the CI-based continuous-improvement model is gradually winning the design competition where political conditions permit.

---

## A.6 A producer's compliance-capture decision matrix

For a given operational improvement, which compliance regimes can claim the resulting CI reduction, and where does voluntary-credit white space remain? "✓" means the regime's methodology can score and reward the improvement; "✗" means it cannot; "△" means partial credit.

| Improvement type | RFS | LCFS (CA/OR/WA) | 45Z | REDIII / ReFuelEU | Canada CFR | VCM potential |
|---|---|---|---|---|---|---|
| **Feedstock switch to UCO/tallow** | △ (qualifies D4/D5) | ✓ (full CI score) | ✓ (CI-scaled) | ✓ (Annex IX Part A) | ✓ | Low — fully captured by compliance |
| **Feedstock switch to energy crops (canola, soy)** | ✓ (D4/D5) | △ (better than fossil but not negative) | △ | ✓ | △ | Low — compliance captures most value |
| **Renewable electricity for process energy** | ✗ (not scored) | ✓ (full CI reduction credited) | ✓ | △ (actual-value pathway required) | ✓ | Low in CA/LCFS; possible EU boundary-gap |
| **Green hydrogen replacing fossil H₂ (HEFA)** | ✗ | ✓ | ✓ | △ (actual-value; RFNBO multiplier if certified) | △ | Low in LCFS; EU boundary-gap for uncertified plants |
| **Process efficiency / heat integration** | ✗ | ✓ (if CI change is material enough for re-verification) | ✓ | △ (actual-value only) | ✓ | EU boundary-gap only; LCFS captures it |
| **Upstream Scope 3 (feedstock supply-chain methane)** | ✗ | △ (certain methodologies only) | ✗ | ✗ | △ | Possible white space if LCFS methodology has no field for it |
| **Novel fuel type — no existing pathway methodology** | ✗ | ✗ (pending new methodology) | △ (eligible if meets CI threshold) | ✗ | ✗ | Genuine white space until methodology is established |
| **Production in non-LCFS, non-EU, non-CFR geography** | ✗ | ✗ (unless CARB pathway registered) | ✗ (US-only) | ✗ (EU market access required) | ✗ (Canada market) | True geographic gap while delivery into compliance markets is non-commercial |

**Reading this table:** the LCFS is the most comprehensive CI-capture instrument — it can score renewable electricity, green hydrogen, and process-efficiency changes that other regimes miss. This is why LCFS maximizes compliance revenue *and* minimizes VCM white space simultaneously. REDIII's actual-value pathway is second-broadest but operationally harder to access. RFS and 45Z are narrowest: volume-and-threshold instruments that don't score most plant-level CI improvements at all.

The genuine VCM white spaces reduce to three: **novel fuel pathways** with no established methodology yet (e.g., green methanol at non-EU ports, agricultural-residue fuels in developing markets, certain pyrolysis-oil HEFA); **upstream Scope 3** where no methodology covers the improvement; and the **true geographic gap**. Everything else is either captured by compliance already or is an apparent gap that can be closed by registration.

---

## A.7 VCMs as a bridge *toward* regulation

The chapter analysis frames voluntary markets as operating within the gaps left by compliance regimes. There is a stronger version: voluntary markets can actively *create the conditions* for compliance regimes to form. The bridge works in both directions — not only across a regulatory gap, but toward a regulatory future the project itself helps bring about. This is not hypothetical; there are documented mechanisms and concrete cases.

### Five mechanisms by which VCMs catalyze compliance markets

1. **Proof of concept.** VCM projects generate evidence that an abatement is technically feasible and economically achievable at scale, reducing the policy risk of building a future standard around it. A biochar project producing 5,000 t of credits/year demonstrates to an agriculture ministry that the abatement is measurable, verifiable, and real.
2. **MRV infrastructure.** Building a Verra or Gold Standard project requires monitoring, reporting, and verification systems — sensor networks, data protocols, third-party auditors. These are the exact prerequisites for a future compliance market and are transferable.
3. **Industry constituency.** VCM projects create producers and buyers with a commercial interest in a future compliance market (better pricing, lower buyer uncertainty, longer-duration revenue). A cluster of LATAM HEFA producers earning VCM revenue has an incentive to lobby for domestic fuel standards.
4. **Supply base.** Compliance markets need supply on Day 1. VCM-funded projects build supply before the mandate exists. ReFuelEU's escalating SAF mandate would have almost no credible supply base if the VCM-and-early-procurement market hadn't funded the first generation of SAF plants between 2018 and 2024.
5. **Price discovery.** Voluntary markets generate observable price data — what buyers actually pay for verified reductions — which feeds the economic modeling regulators use to set benchmarks, credit prices, and penalty levels.

### Concrete bridge-toward-regulation cases

- **Chile HEFA → SAF mandate.** LATAM HEFA projects serving VCM buyers and spot exports, funded partly through voluntary airline offtake, create the operating capacity and documented supply chain that make a Chilean SAF mandate politically plausible.
- **US Midwest RNG → state LCFS programs.** California LCFS created a deep dairy-RNG credit market in the early 2010s; the operational experience and MRV infrastructure built for CARB reporting became the template Oregon, Washington, and Canada used. Expansion didn't require building new MRV from scratch.
- **UK SAF mandate supply base.** When the UK SAF mandate was announced, industry and government advisors pointed to voluntary procurement deals and airline SAF programs as evidence of demand depth that made the mandate viable.
- **Canada CFR — transition from CARB pathways.** Many Canadian producers registered CARB pathways in 2015–2020 for California revenue; when the CFR launched in 2023, they had already done the LCA registration and CI documentation the CFR required.
- **Brazil/Colombia biomethane informing domestic fuel standards.** Early Verra/Gold Standard methane-avoidance projects built continuous methane-flow measurement and biogas-composition tracking that now underpin Brazil's RenovaBio/Renovacombustíveis pathways and Colombia's biomethane/hydrogen pathway development.

### Requirements and limits

For the bridge-toward-regulation frame to be a sound strategy rather than a rationalization:

1. **Credible regulatory trajectory.** Genuine evidence of political momentum — NDC commitments requiring sector action, active consultations, peer-jurisdiction precedent. "Regulation is possible someday" is not sufficient.
2. **MRV infrastructure that transfers.** The project must be built to standards likely compatible with the eventual compliance regime. A bespoke methodology that can't convert is a dead end, not a bridge. CARB-compatible LCA methodology is explicitly a transferable MRV investment.
3. **Transparent stranding-risk disclosure.** The voluntary revenue stream will terminate when compliance arrives — possibly at administered rather than market prices. Build the model in two phases: (1) VCM-funded construction and early operation; (2) compliance-funded operation at lower per-unit margin but higher volume certainty.
4. **No double-claiming at the transition.** When the compliance regime claims the attribute, the VCM stream must be retired. The transition is an attribute-accounting event.

The frame does not rescue projects with weak near-term additionality. A project that isn't additional under VCM rules doesn't become additional because there *might* be a future compliance market. The near-term integrity tests still apply — the bridge argument operates in addition to them, not instead of them.

---

# Sources and currency

This appendix cites figures that are current as of writing (May 2026) and will move. The following are the most time-sensitive claims; each should be re-verified against the primary source before being relied upon, and updates tracked via `CHANGELOG.md`:

| Claim | Value as stated | As-of | Primary source to verify against |
|---|---|---|---|
| LCFS credit price (A.1, A.2) | ~$63/tCO₂e (Q1 2026 average); ~$66/tCO₂e (week of May 11–17, 2026) | May 2026 | CARB Weekly LCFS Credit Transfer Activity Reports (ww2.arb.ca.gov) |
| LCFS SAF / alternative jet fuel CI benchmark (A.1) | 86.64 gCO₂e/MJ in 2025; declining annually (80.36 by 2030+) | 2025 | California Code of Regulations Title 17 §95484 Table 3 |
| LCFS diesel benchmark (context for Ch.7 line ~541) | 81.70 gCO₂e/MJ effective July 1, 2025 (down from 86.64) | July 2025 | CARB LCFS 2024 amendments; Cal. Code Regs. Tit. 17 §95484 |
| LCFS price cap | $268.90/tCO₂e (June 2025 – May 2026); new cap published April 6, 2026 | 2025–26 | CARB LCFS Credit Clearance Market notices |
| 45Z credit value (A.1) | Up to $1.00/gal for SAF (reduced from $1.75 by OBBBA, Public Law 119-21, July 2025) | 2025–2029 window | IRC §45Z as amended; IRS / Treasury proposed regulations Feb 2026 |
| RIN price range D4/D7 (A.1) | $0.40–1.50/gal cited as range; D4 spot ~$0.77 (Q1 2025) rising to ~$1.10–1.11 (late 2025/2026) | Q1 2025 – early 2026 | EPA RIN trades and price information; OPIS/Stillwater D-code price reports |
| D3 vs. D7 D-code definitions (A.1) | D3 = cellulosic biofuel (broader; includes ethanol, RNG); D7 = cellulosic diesel specifically | Current | EPA RFS program: 40 CFR Part 80 |
| CARB pathway approval timeline (A.4) | 6–18 months for established pathways | Current practice | CARB LCFS program — Fuel Pathway Registration process |
| CARB pathway registration cost (A.4) | ~$50,000–200,000 one-time; ~$20,000–50,000/yr ongoing | Current practitioner range | CARB LCFS practitioner guidance; law-firm alerts (Sidley, Weaver, etc.) — no CARB-published fixed fee |
| Washington CFS enactment (A.5) | HB 1091 signed May 2021; operative January 1, 2023; tightened by HB 1409 (signed May 17, 2025) | 2021 / 2025 | Washington Dept. of Ecology; HB 1091; HB 1409 |
| Canada CFR in force date (A.5) | July 1, 2023 | 2023 | Canada.ca — Clean Fuel Regulations |
| Canada liquid fuel market size vs. US (A.5) | "~15% of the US market" — approximate, unverified against published primary data; treat as illustrative order-of-magnitude | — | Verify against EIA / NRCan annual fuel statistics before citing |
| Singapore SAF mandate (A.5) | SAF levy effective April 1, 2026; flights departing from October 1, 2026; 1% blend target for 2026, scaling to 3–5% by 2030 | March 2026 | Civil Aviation Authority of Singapore (CAAS) announcement March 2026 |
| Japan SAF "10%-by-2030" target (A.5) | 10% SAF use by Japanese airlines by 2030 | Feb 2023 Cabinet decision | Japan GX Basic Policy (Feb 2023); MLIT Roadmap for Decarbonization of Aviation (Dec 2021) |
| California annual liquid transport fuel volume (A.5) | ~18–20 billion gallons/year (≈13.4 Bgal gasoline in 2024 + diesel + other) | 2024 | California Energy Commission; California Dept. of Tax and Fee Administration |
| REDIII GHG-savings thresholds for transport biofuels (A.5) | ≥50% (pre-Oct 2015 plants); ≥60% (from Oct 2015); ≥65% (from Jan 1, 2021) — these apply to biofuels/bioliquids for transport | Oct 2023 (REDIII in force) | REDIII Article 29; EUR-Lex CELEX:32023L2413 |
| REDIII "80–85%" superior-performance range (A.5) | Illustrative commercial premium range; NOT a statutory threshold — the 70%/80% statutory thresholds apply to electricity/heat from solid biomass, not transport biofuels | — | REDIII Article 29; distinguish from Article 29(1) transport biofuel thresholds vs. Article 29(3) biomass-for-energy thresholds |
| A.3 routing table $/gal ranges | California $2.50–3.50; OR/WA $1.80–2.80; Federal $1.30–2.00; EU €1.00–2.50; Canada CAD $1.50–2.50 | ~2025–26 | Derived from individual instrument prices above; verify each component as underlying prices move |
