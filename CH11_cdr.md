# Chapter 11 — Carbon Dioxide Removal (CDR)

**Track:** Forward View (C).
**Prerequisites:** Chapter 10 (CCUS — point-source capture and storage infrastructure). Helpful: Chapter 1 (the carbon cycle), Chapter 8 (voluntary markets and the bifurcation between avoidance and removal credits).
**What you should be able to do by the end:**
- Distinguish **carbon dioxide removal (CDR)** from **point-source carbon capture (CCS/CCUS)** — both are "carbon capture" but they answer different climate questions.
- Distinguish **conventional CDR** (afforestation, soil carbon, blue carbon) from **novel CDR** (DAC, BECCS, enhanced rock weathering, ocean alkalinity enhancement, biochar, biomass burial, mineralization).
- Walk through the major CDR technology categories: DAC (solid sorbent vs. liquid solvent vs. electrochemical), BECCS (bioenergy + CCS), enhanced rock weathering, ocean-based CDR, biochar, biomass burial, mineralization.
- State current CDR deployment (~2 GtCO₂/yr globally, ~99.9% from conventional CDR; novel CDR delivered ~1,200 tonnes through 2023 H1 of 2025 from DAC specifically; ~600 ktCO₂/yr operational DAC capacity entering 2026 with Stratos ramp-up).
- Articulate the gigaton gap: IPCC 1.5°C-compatible scenarios require **5–10 GtCO₂/yr of novel CDR by mid-century** — three to four orders of magnitude above current capacity.
- Explain what advance market commitments (AMCs) are and why Frontier ($1B+) is the most consequential mechanism for early-stage CDR financing.
- Identify the major operational and FID-stage projects: Climeworks Mammoth (Iceland, 36 ktCO₂/yr), 1PointFive Stratos (Texas, 500 ktCO₂/yr at full capacity), Heirloom-Climeworks Project Cypress, Stockholm Exergi BECCS (Sweden), Drax UK (proposed BECCS), Carbfix (Iceland mineralization), various biochar and biomass-burial deployments.
- Articulate the substantive critiques of CDR: moral hazard, energy and land demands, monitoring and permanence questions, the cost trajectory, and the relationship to direct decarbonization.

---

## Why this chapter exists

Chapters 1–10 have largely been about reducing emissions — preventing CO₂ from entering the atmosphere in the first place. This chapter is about the other half of the climate problem: **removing CO₂ that's already there, or that will be emitted by hard-to-eliminate sources.**

The climate science makes the case unavoidable. The atmosphere now holds approximately **425.7 ppm CO₂** (2025) — up from 280 ppm pre-industrial. Every plausible 1.5°C-compatible pathway involves not just stopping new emissions but actively removing CO₂ from the atmosphere at gigaton scale. The IPCC AR6 scenarios require **5–10 GtCO₂/yr of CDR by 2050**, with some scenarios going as high as 20 GtCO₂/yr. Current novel-CDR capacity is in the kilotonne range — three to four orders of magnitude below required scale.

This chapter therefore sits at the most uncertain frontier of the curriculum. The technologies covered are real, deployed (some of them at meaningful scale), and improving rapidly. They are also far below the scale climate scenarios assume, far more expensive than market-rate decarbonization, and the subject of intense debate about whether they should be relied on at all. Whether CDR can scale from kilotonnes to gigatonnes in the next 25 years is one of the most consequential open questions in climate policy.

I'll organize this in seven parts: the CDR concept and how it differs from CCS; the conventional CDR baseline (and why we don't usually talk about it as climate technology); direct air capture in depth; BECCS in depth; the broader removal portfolio (enhanced weathering, ocean CDR, biochar, biomass burial); the demand side (corporate buyers, Frontier, sovereign purchases, ETS integration); and the substantive critiques and the path forward.

---

# Part 1: The CDR concept

## What CDR is and isn't

A **carbon dioxide removal (CDR)** technology takes CO₂ out of the atmosphere and stores it durably — durable enough that on policy-relevant timescales (decades to millennia), the carbon stays out of the atmosphere.

CDR is **distinct from point-source capture** (Ch. 10) in a fundamental way: point-source capture intercepts CO₂ at the smokestack before it reaches the atmosphere. The CO₂ was already going to be emitted; the capture prevents the emission. CDR removes CO₂ that's already in the atmosphere (or, in the case of BECCS, that just came from the atmosphere via biomass growth before being released by combustion and re-captured).

The accounting distinction matters for net-zero claims:
- **Point-source capture** = avoiding an emission. Counts against the source's gross emissions.
- **CDR** = removing past or atmospheric emissions. Generates a "negative" emission that can offset elsewhere or push net emissions below zero.

A facility with **only** point-source capture is at best zero-emissions. A facility with **CDR** can have negative net emissions — putting more CO₂ in the ground than it puts in the air.

## Why CDR is necessary

The case for CDR rests on three observations:

**1. Residual emissions.** Some emissions can't be eliminated at acceptable cost in any timeframe. Cement process emissions (from limestone calcination — see Ch. 12) are chemically unavoidable. Methane and N₂O from agriculture are partially intractable. Long-haul aviation, certain industrial heat. The "residual" emissions that have to be neutralized rather than eliminated are estimated at 2–5 GtCO₂e/yr in net-zero economies.

**2. Past emissions.** Even at net-zero emissions, the existing atmospheric CO₂ overhang (over 280 ppm baseline) will keep warming the planet for centuries. To stabilize temperatures at lower levels — or to recover from temporary overshoot of 1.5°C — atmospheric CO₂ must be drawn down. This is "net-negative emissions" territory, requiring substantial CDR.

**3. Overshoot scenarios.** Most 1.5°C-compatible scenarios in IPCC AR6 involve some temperature overshoot (going above 1.5°C and then coming back down). Coming back down requires net-negative emissions, which requires large-scale CDR for several decades.

These three uses are different. Use #1 ("offsetting residual emissions") requires CDR at roughly the scale of residual emissions — 2–5 GtCO₂/yr globally. Uses #2 and #3 (drawing down past emissions or recovering from overshoot) require much larger scales — potentially 10–20 GtCO₂/yr for several decades.

## Conventional vs. novel CDR

CDR splits into two distinct categories that share an accounting label but operate very differently:

**Conventional CDR** uses natural systems to absorb and store CO₂:
- **Afforestation/reforestation** — planting trees on land that wasn't recently forested
- **Soil carbon sequestration** — agricultural practices that increase soil organic carbon
- **Wetland and peatland restoration** — restoring degraded ecosystems
- **Blue carbon** — coastal ecosystems (mangroves, seagrass, salt marshes) that store carbon

Conventional CDR is **the bulk of all current CDR**. The IPCC and the State of Carbon Dioxide Removal report (2024) estimate ~2 GtCO₂/yr of CDR globally — almost all from afforestation/reforestation and soil carbon.

**Novel CDR** uses engineered or accelerated processes:
- **Direct Air Capture (DAC)** — chemical capture of CO₂ from ambient air, then storage
- **Bioenergy with Carbon Capture and Storage (BECCS)** — burning biomass and capturing the CO₂
- **Enhanced rock weathering** — accelerating natural rock-CO₂ reactions
- **Ocean alkalinity enhancement** — adding alkalinity to the ocean to absorb more atmospheric CO₂
- **Biochar** — pyrolyzing biomass to produce stable carbon for soil application
- **Biomass burial** — storing biomass in conditions that prevent decomposition
- **Mineralization** — reacting CO₂ with reactive rocks to form stable carbonates

Novel CDR delivered approximately **1,200 tonnes** of removals (DAC specifically) through H1 2025 — five orders of magnitude smaller than conventional CDR. The novel-CDR pipeline is what's growing rapidly.

The conceptual difference: conventional CDR is bio-based and uses living systems; novel CDR is technology-based and uses physical-chemical processes. Conventional CDR is older, cheaper, and at scale; novel CDR is newer, more expensive, but more permanent and verifiable in many cases.

## Why this chapter focuses on novel CDR

Conventional CDR is important but largely already happening through existing policy frameworks (forestry incentives, agricultural soil-carbon programs, REDD+, agroforestry initiatives). It's covered in Chapter 8's discussion of voluntary forestry credits. The integrity questions about conventional CDR — what counts as additional, what about permanence under wildfire risk, what about leakage — are real and unresolved.

Novel CDR is the new frontier. It's where most current investment is going. It's what's likely to scale meaningfully over 2025–2050 (whereas conventional CDR is land-constrained — there's a finite amount of plausible afforestation land globally). And it's where the substantive scaling challenge lives.

This chapter focuses on novel CDR while acknowledging that comprehensive CDR strategy involves both categories.

---

# Part 2: Direct Air Capture (DAC) in depth

DAC is the most prominent novel CDR technology — the one that gets headline attention, attracts the most capital, and represents the conceptual "pure" form of atmospheric removal.

## The technical challenge

DAC captures CO₂ from ambient air, which contains approximately **425 ppm (0.04%) CO₂**. By comparison:
- Power plant flue gas: 3–15% CO₂
- Cement plant flue gas: 20–30% CO₂

Air is **three to four orders of magnitude more dilute** in CO₂ than point-source flue gases. The dilution drives the cost: separating something rare from a vast volume of air requires moving a lot of air, contacting it with a lot of sorbent, and using a lot of energy.

The theoretical minimum work to separate CO₂ from air is approximately **20 kJ/mol** (the entropic cost of "concentrating" CO₂ from 425 ppm to pure form). The actual energy use of current DAC systems is **8–10× this thermodynamic minimum** — typically 5–10 GJ per ton CO₂, including thermal energy for sorbent regeneration plus electricity for fans and compression.

The thermodynamic minimum gives a floor on how cheap DAC can get; current cost trajectories are closing the gap but still some distance away.

## DAC technologies

The DAC industry has converged on two major technology classes plus a smaller emerging category.

### Solid sorbent DAC (S-DAC)

**How it works:** Air is drawn through containers filled with solid sorbent — typically an amine-functionalized polymer. CO₂ chemically binds to the sorbent. When the sorbent is saturated, it's heated to ~100°C to release pure CO₂, and the cycle repeats.

**Energy:** Lower-temperature heat (80–120°C) means S-DAC can use lower-grade energy sources (geothermal in Iceland; future industrial waste heat).

**Modularity:** S-DAC is inherently modular — many small contactor units operating in parallel. Easier to scale from kilotonne to megatonne by building more units.

**Examples:** Climeworks (Switzerland-Iceland) is the dominant S-DAC company. Their Orca plant (operational 2021, 4 ktCO₂/yr) and Mammoth plant (operational May 2024, 36 ktCO₂/yr) are the largest S-DAC facilities globally. Other S-DAC developers include Phlair (formerly Carbon Engineering's solid-sorbent spinoff), AspiraDAC, and Sustaera.

### Liquid solvent DAC (L-DAC)

**How it works:** Air contacts a strongly alkaline aqueous solution (typically potassium hydroxide, KOH). CO₂ reacts with the solution, forming dissolved carbonates. The CO₂-rich solution is processed through a series of chemical reactions (calcium hydroxide → calcium carbonate → calcination at ~900°C → pure CO₂ + calcium oxide).

**Energy:** High-temperature heat (~900°C) means L-DAC needs high-temperature thermal energy — historically from natural gas, now increasingly from electric high-temperature processes.

**Scale efficiency:** L-DAC achieves scale through fewer, larger units. Capital intensity per unit capacity is lower at large scale than S-DAC, but minimum economic scale is larger.

**Examples:** **1PointFive's Stratos** in Ector County, Texas — operational from late 2025 with phased ramp-up to **500 ktCO₂/yr by mid-2026**. Designed by Carbon Engineering (acquired by Occidental). Powered by a dedicated 145 MW solar facility. The first commercial-scale L-DAC. Other L-DAC developers include Mission Zero Technologies.

### Electrochemical and emerging DAC approaches

Several developers are pursuing alternatives that use electricity (rather than thermal energy) as the primary energy input:

- **Verdox** — electrochemical sorbent regeneration; potentially much lower energy use.
- **Mission Zero** — electrochemical aqueous capture.
- **Heirloom** — mineralization-based DAC. Spreads calcium hydroxide on outdoor trays; the alkaline material absorbs atmospheric CO₂ to form limestone. Then heated to release CO₂ and regenerate calcium hydroxide. Uses electric kilns; potentially lower energy than other approaches.
- **44.01** — peridotite mineralization-based; binds CO₂ permanently in rock.

These approaches are at smaller scale than S-DAC and L-DAC but represent significant technology diversification. The mature DAC industry in 2030 will probably have multiple competing technology classes rather than a single dominant approach.

## Current state and trajectory

**Operational DAC capacity entering 2026:**
- Climeworks Mammoth (Iceland): 36 ktCO₂/yr (S-DAC)
- 1PointFive Stratos (Texas, ramping): up to 500 ktCO₂/yr design capacity (L-DAC)
- Heirloom first commercial facility (California): kilotonne-scale (mineralization-based)
- Various smaller pilots and demonstration facilities globally

**Total operational DAC capacity, early 2026:** approximately 60–80 ktCO₂/yr fully operational, with Stratos still ramping. If Stratos achieves design capacity by mid-2026, total operational DAC capacity will approach 570 ktCO₂/yr — an 8.7× single-year increase.

**Pipeline through 2030:** 30+ DAC facilities announced for post-2025 operation; cumulative announced capacity in low megatonnes/yr by 2030. Significant geographic concentration in the US, Europe, and Iceland.

**DOE DAC Hubs:** The US DOE announced $1.2 billion in hub funding in August 2023:
- **South Texas DAC Hub** (1PointFive/Occidental-led)
- **Project Cypress** (Louisiana, Climeworks + Heirloom-led)

Both targeting 1 MtCO₂/yr capacity once fully built. Construction underway; operational ~2027–2028.

**Climeworks' Kenya project:** Climeworks announced in 2024 plans for an African DAC facility targeting 1 MtCO₂/yr by 2028. The Kenya project would use the country's geothermal resources for low-cost heat — the same model as Iceland.

## Costs and the cost trajectory

DAC is the most expensive form of CDR currently deployed:

- **Current operational costs** (best-case for established players like Climeworks): $400–800/tCO₂
- **Stratos target** at full capacity: ~$300–500/tCO₂
- **Climeworks 2030 target**: $250–350/tCO₂
- **Long-term targets** (industry projection, IEA NZE): $100–200/tCO₂ by 2050

For comparison, EU ETS allowances trade at €70–75/tCO₂ in 2026; nature-based avoidance credits trade at $5–25/tCO₂. DAC is currently 5–50× more expensive than alternative carbon-pricing options for the same accounting outcome.

The cost trajectory is favorable but uncertain. Historical analogues — wind costs fell 50% in 15 years, solar fell 90% in 15 years, batteries fell 80% — suggest DAC could decline substantially. But DAC's thermodynamic minimum (~$30–80/tCO₂ at very large scale and cheap energy) is higher than zero, so the bottom-end target is structural rather than aspirational.

The 45Q tax credit in the US — **$180/tCO₂ for DAC with geological storage**, **$130/tCO₂ for DAC with EOR** — is calibrated near the high end of current costs. For US-located projects, 45Q substantially covers the cost-to-revenue gap.

## **Stop-and-check 11.A**

1. DAC must capture CO₂ from air at 425 ppm — three orders of magnitude more dilute than point-source flue gases. Why hasn't this killed DAC commercially? What features make it economically viable despite the dilution?
2. The Mammoth plant has been operating in Iceland since May 2024 at 36 ktCO₂/yr. Total cumulative DAC delivery through mid-2025 was about 1,200 tonnes (across all suppliers). Why is delivery so much smaller than installed capacity?
3. Stratos's design capacity is 500 ktCO₂/yr — nearly 14× the size of Mammoth. The technology jump (S-DAC → L-DAC) is large. What's the risk if Stratos underperforms?
4. **Socratic prompt:** If you were Microsoft's chief sustainability officer in 2026, deciding whether to commit to a 10-year DAC purchase agreement at $500/tCO₂, what would you weigh in deciding yes or no?

---

# Part 3: BECCS in depth

Bioenergy with Carbon Capture and Storage (BECCS) is the second major novel-CDR category. It's also the most controversial.

## The conceptual structure

BECCS combines two technologies:
1. **Bioenergy** — burning biomass (wood, agricultural residues, dedicated energy crops, biogas) to produce heat, electricity, or fuel.
2. **CCS** — capturing the CO₂ produced by combustion and storing it geologically.

The carbon accounting:
- The biomass took CO₂ from the atmosphere (during photosynthesis).
- Burning the biomass releases the CO₂ back to the atmosphere.
- Capturing and storing that CO₂ means the carbon ends up in the ground rather than in the atmosphere.
- Net result: CO₂ has moved from atmosphere → biomass → geological storage.

If the biomass was sustainably produced (the harvested biomass is regrown, maintaining stable forest stocks), then BECCS delivers **net-negative emissions**.

The "if" is doing a lot of work. We'll return to this in the integrity discussion below.

## Where BECCS operates

BECCS can be applied wherever biomass is being burned at scale:

**Pulp and paper mills.** Black liquor is a byproduct of paper production; it's burned for energy. Capture from black liquor combustion is a leading near-term BECCS application. Stockholm Exergi's Värtaverket CHP plant in Sweden is the leading commercial example (FID 2024 for 800 ktCO₂/yr capture).

**Biomass-fired power plants.** Drax in the UK is the most prominent example (proposed 8 MtCO₂/yr BECCS). The 2025 status: the project has been in development since 2018, with various policy uncertainties; current status is FID-pending under the UK CCS-CfD framework.

**Bioethanol plants.** Ethanol production releases concentrated CO₂ that's easy to capture. Several ethanol+CCS projects in the US (mostly oriented toward EOR rather than dedicated storage; Summit Carbon Solutions covered in Ch. 3 is an EOR-coupled approach).

**Biogas processing.** Anaerobic digestion of agricultural waste produces biogas (mostly methane and CO₂). The CO₂ stream is highly concentrated and easy to capture.

**Dedicated BECCS facilities.** New facilities built specifically to burn biomass and capture CO₂. Largely conceptual in 2025–2026; no commercial-scale dedicated BECCS plants operational.

## Current state

BECCS is more mature than DAC in some ways and less in others:

**Mature:** The technology is straightforward — BECCS = biomass combustion + standard CCS. The major BECCS-relevant components (combustion, amine capture, geological storage) are all commercial.

**Less mature:** Commercial deployment is just starting. The Stockholm Exergi project reached FID in 2024. Drax UK is pending FID under CCS-CfD allocation. Most ethanol+CCS in the US uses EOR rather than dedicated storage, which is not climatically equivalent.

**Scale potential:** BECCS could potentially scale to hundreds of MtCO₂/yr by 2030–2035 if the policy framework, biomass supply chains, and CCS infrastructure align.

**Current operational capacity:** Approximately 1–2 MtCO₂/yr of dedicated BECCS capacity globally as of early 2026. Mostly at ethanol facilities (some of which are EOR-coupled and don't count cleanly).

## The biomass question

The deepest BECCS controversy concerns biomass sustainability. The carbon accounting assumes the biomass came from sustainable sources — newly-grown trees that are being regrown, not virgin forest being converted to bioenergy.

The reality is mixed:

- **Wood pellets for Drax** have been linked to clear-cutting in the US Southeast and Estonia. Critics argue these aren't "sustainable" in any meaningful sense; defenders argue they use forest residues and waste wood, which would otherwise decompose.
- **Energy crops on dedicated land** require land that could grow food. The food-vs-fuel debate (active for biofuels) applies to BECCS as well.
- **Agricultural residues** (crop stems, husks) are abundant but typically support soil health if left in place. Removing residues for energy can degrade soils.
- **Black liquor and process residues** are genuinely unproblematic — they're already being burned, and capturing the CO₂ adds CDR without changing the biomass supply chain.

The substantive question: what fraction of potential BECCS volume is genuinely net-negative when full lifecycle effects (land conversion, forest depletion, soil degradation, transport emissions) are accounted for?

The honest answer is: a substantial fraction, but not all, and not at unlimited scale. Conservative estimates suggest sustainable BECCS could deliver 1–3 GtCO₂/yr by 2050. Optimistic estimates go higher (5+ GtCO₂/yr); pessimistic ones lower (< 1 GtCO₂/yr).

## The IPCC's reliance on BECCS

A critical observation: **IPCC scenarios consistent with 1.5°C have historically relied heavily on BECCS for negative emissions**. Many AR5 and AR6 scenarios assume 5–15 GtCO₂/yr of BECCS by 2050. This is much larger than realistic sustainable potential.

The IPCC scenarios using BECCS at scale have been substantively criticized for relying on a technology that may not scale sustainably. More recent scenarios diversify CDR across DAC, enhanced weathering, and other novel approaches — but BECCS remains a significant component.

The implication: if BECCS doesn't scale to the levels IPCC scenarios assume, the negative emissions have to come from somewhere else. DAC is the obvious alternative but is 5–10× more expensive per ton.

---

# Part 4: The broader removal portfolio

Beyond DAC and BECCS, several other novel CDR approaches are at various stages of development.

## Enhanced rock weathering (ERW)

**How it works:** Crushed silicate rocks (basalt, peridotite, olivine) react slowly with atmospheric CO₂ to form stable carbonate minerals. The natural weathering rate is slow (geological timescales), but crushing the rock to fine particles greatly accelerates the reaction.

**Application:** Spread crushed silicate rock on agricultural land. The rock dust serves multiple purposes — neutralizing acidic soils (improving crop yields), releasing nutrients (improving soil fertility), and pulling CO₂ from the atmosphere (CDR).

**Permanence:** Excellent. Once CO₂ is bound in carbonate minerals, it's stored on geological timescales.

**Scale potential:** Large — silicate rocks are abundant and agricultural land is widespread. Estimates of plausible scale: 1–5 GtCO₂/yr by 2050.

**Current deployment:** UNDO, Lithos, Eion, Cascade, and various other companies are at early commercial stages. Cumulative deliveries through 2025: hundreds of thousands of tonnes (significantly more than DAC, less than biochar). The Frontier coalition has purchased meaningfully from ERW providers.

**Verification challenges:** Confirming that crushed rock is actually weathering and capturing CO₂ requires extensive monitoring. The Isometric and Puro.earth standards have developed methodologies; verification remains complex and expensive.

## Ocean alkalinity enhancement (OAE)

**How it works:** Adding alkaline materials (typically olivine, basalt, or hydrated lime) to seawater increases ocean alkalinity, allowing the ocean to absorb more atmospheric CO₂.

**Theoretical basis:** Solid. The ocean already absorbs ~25% of human CO₂ emissions (Ch. 1). Increased alkalinity would increase that absorption rate.

**Practical challenges:** OAE is highly experimental. The marine biogeochemistry is complex; potential side effects (pH changes, mineral precipitation, effects on marine biology) are still being researched.

**Current deployment:** Several startups (Planetary Technologies, Vesta, Climaford, Gigablue, Ebb Carbon) are conducting pilot-scale experiments. No commercial deployment yet.

**Outlook:** Major potential scale (theoretically up to 10+ GtCO₂/yr); major uncertainty about feasibility, side effects, and verifiability. The IPCC has noted OAE as "promising but not yet proven."

## Biochar

**How it works:** Biomass is pyrolyzed (heated in low-oxygen conditions) to produce a stable charcoal-like material called biochar. Applied to soils, biochar can persist for centuries to millennia, sequestering the embedded carbon while improving soil properties.

**Permanence:** Generally good — 100–1,000 year residence times depending on biochar quality, soil conditions, and management.

**Scale potential:** Constrained by biomass feedstock availability. Realistic estimates: 0.5–2 GtCO₂/yr by 2050.

**Current deployment:** Biochar is the largest current source of "engineered" CDR delivery globally. Multiple operational projects; thousands to tens of thousands of tonnes delivered annually. The Puro.earth standard has the most-developed biochar methodology.

**Co-benefits:** Improved soil fertility (in some applications), water retention, reduced fertilizer needs. The agricultural-utility plus CDR value proposition makes biochar attractive in agricultural contexts.

## Biomass burial

**How it works:** Biomass (woody waste, agricultural residues) is buried in conditions that prevent decomposition — deep geological burial, dry conditions, anoxic environments. The carbon stays sequestered for centuries.

**Permanence:** Very good with proper burial conditions.

**Scale potential:** Constrained by feedstock and burial infrastructure. Estimates: 0.5–3 GtCO₂/yr.

**Current deployment:** Graphyte, Vaulted Deep, and several other startups are scaling biomass burial operations. Cumulative deliveries growing rapidly.

**Distinguishing from landfilling:** Biomass burial is engineered for permanent sequestration; landfilling is waste management. The distinction matters for accounting.

## Mineralization

**How it works:** Reaction of CO₂ with reactive minerals (calcium silicates, magnesium silicates, peridotite) to form stable carbonates.

**Subcategories:**
- **In-situ mineralization** — injecting CO₂ into reactive subsurface formations. Carbfix in Iceland is the leading example, dissolving CO₂ in water and injecting into basaltic formations.
- **Ex-situ mineralization** — bringing reactive rocks above ground and reacting them with CO₂.
- **Industrial waste mineralization** — using mining waste, steel slag, fly ash as reactive substrates.

**Permanence:** Excellent — geological timescales.

**Scale potential:** Geographically constrained — depends on reactive rock availability. Iceland's basaltic geology is ideal; many other regions have less suitable resources.

**Current deployment:** Carbfix has been operating commercially since 2014. 44.01 in Oman is scaling. Heirloom uses mineralization within its DAC process. Several other companies at pilot or early commercial stages.

## Conventional CDR at scale

Worth one more note on conventional CDR. **Afforestation and reforestation** can plausibly scale to 0.5–2 GtCO₂/yr by 2050. **Improved forest management** could add another 0.5–1.5 GtCO₂/yr. **Soil carbon sequestration** could add 1–3 GtCO₂/yr, though with significant permanence questions. **Wetland and peatland restoration** could add 0.5–1 GtCO₂/yr.

Total conventional CDR potential: roughly 3–7 GtCO₂/yr by 2050 — significant but constrained by land availability and competing uses.

## **Stop-and-check 11.B**

1. Looking at the realistic 2050 scale potentials: DAC (5–10+ GtCO₂/yr potential), BECCS (1–5), enhanced weathering (1–5), biochar (0.5–2), ocean alkalinity (uncertain), mineralization (1–3), conventional CDR (3–7). What does the portfolio approach imply about climate strategy?
2. Biochar and enhanced weathering have substantial co-benefits (soil improvement). DAC has no inherent co-benefits beyond CDR. Does this matter for which technologies deserve priority?
3. The IPCC has historically relied heavily on BECCS in 1.5°C scenarios. If BECCS scales below expectations, what alternatives are most credible?
4. **Socratic prompt:** If you had $1 billion to invest in CDR by 2030, would you concentrate it in one technology category or diversify across several? Defend your strategy.

---

# Part 5: The demand side — buyers, AMCs, and policy support

## Corporate buyers

The voluntary corporate market is currently the primary funder of novel CDR. As of mid-2025, total CDR purchases (across all novel technologies) reached approximately:

- **Microsoft:** ~18 million tCO₂ across multiple suppliers — by far the largest single buyer. Roughly 80% of total durable CDR purchases globally.
- **Airbus:** ~400,000 tCO₂ (largely DAC).
- **Frontier coalition** (Stripe, Alphabet, Shopify, Meta, McKinsey): $1B+ committed, distributed across multiple suppliers.
- **JP Morgan Chase:** $200M+ committed across multiple providers.
- **Amazon:** 250,000 tCO₂ committed to 1PointFive over 10 years.
- **Shopify:** ~$50M+ committed across multiple providers.
- **Various others:** SwissRe, Boston Consulting Group, Equinor, others contributing.

The buyer concentration is striking. Microsoft alone accounts for the majority of demand. This is good for early-stage scaling (concentrated demand creates revenue certainty) but a vulnerability (demand collapse if Microsoft's strategy shifts).

## Frontier and advance market commitments

**Frontier** is the most important institutional innovation in CDR financing. Launched in April 2022 by Stripe, Alphabet, Shopify, Meta, McKinsey, and now joined by additional partners. Frontier operates as an **advance market commitment (AMC)** for permanent carbon removal:

- **The commitment:** $1 billion+ in pre-purchase commitments through 2030, distributed across multiple CDR providers and technologies.
- **The mechanism:** Frontier signs forward contracts with CDR providers at specified prices, providing revenue certainty before the providers have proven scale.
- **The selection:** Frontier evaluates providers across multiple dimensions (durability, additionality, scalability, co-benefits) and distributes purchases across promising approaches.
- **The signal:** The aggregated commitment from major buyers signals to the broader market that there's durable demand for high-quality CDR, encouraging entrepreneurial entry and investment.

Frontier has now made purchases across 12+ suppliers, including DAC providers (Climeworks, 1PointFive, Heirloom), BECCS, biochar, enhanced weathering, mineralization, and biomass burial.

The model has spawned analogous initiatives:
- **NextGen** (S&P Global subsidiary): purchasing CDR for corporate buyers.
- **Symbiosis Coalition:** ~$500M committed for various removal types.
- **Various other corporate buyer aggregators.**

The AMC approach is widely seen as the most consequential innovation in early-stage CDR financing.

## Policy support

Beyond corporate demand, public policy is increasingly supporting CDR:

**United States:**
- **45Q tax credit:** $180/tCO₂ for DAC with geological storage, $130/tCO₂ for DAC with EOR (post-OBBBA).
- **DOE DAC Hubs:** $1.2 billion initial funding for two hubs (South Texas, Project Cypress).
- **45V Hydrogen tax credit:** Indirectly supports CDR through blue hydrogen with CCS.
- **CRP (Carbon Removal Procurement):** Federal procurement commitments under various programs.

**European Union:**
- **Carbon Removals Certification Framework (CRCF):** Formalized December 2024. Establishes EU-wide standards for CDR certification. Enables CDR credits to participate in EU policy frameworks.
- **Innovation Fund:** ~€38 billion through 2030 supports CCUS and CDR.
- **Potential ETS integration:** The 2026 EU ETS reform may integrate CDR into compliance markets, creating direct demand from regulated entities. This would be a major demand-side expansion.

**United Kingdom:**
- **CCS-CfD framework:** Provides revenue certainty for CCS, including for BECCS projects.
- **Engineered Removals Business Model:** Specific support framework for novel CDR.

**Canada:**
- **CCUS Investment Tax Credit:** 60% capital cost coverage for DAC; 50% for other carbon capture.

**Singapore, Switzerland, Japan, Korea:**
- Various sovereign purchase programs under Article 6.2 of the Paris Agreement, providing demand for CDR credits including from international suppliers.

**Sovereign and corporate demand combined is what's driving the early-stage CDR scaling.** The 2026–2030 period will substantially clarify whether this demand is durable and growing, or whether it plateaus.

## CDR in net-zero accounting

A critical demand driver: **SBTi V2** (Ch. 5, Ch. 8) requires increasing use of removal credits for residual neutralization at net-zero. Companies committing to net-zero with SBTi must:
- Reduce gross emissions to near zero
- Neutralize residual emissions with high-quality removal credits
- Increase the durability and quality of removal credits over time, with mandatory shifts toward long-lived removals (DAC, mineralization, biomass burial) by net-zero target year

If SBTi V2 is broadly adopted (final version expected mid-late 2026), it creates substantial implicit demand for durable CDR over 2030–2050. The 4,000+ companies with SBTi-validated net-zero targets would collectively require ~1+ GtCO₂/yr of removal credits by their net-zero target years (mostly 2040–2050).

This is one of the largest demand-side reform mechanisms in the climate-policy landscape. Whether SBTi V2 is implemented as currently drafted will substantially shape CDR scaling.

---

# Part 6: Substantive critiques of CDR

CDR is among the most controversial parts of the climate-policy debate. The critiques are substantive and deserve fair treatment.

## Critique 1: Moral hazard

The deepest concern: CDR enables continued emissions by promising future removal of what's being emitted now. If CDR is going to scale to gigaton levels, why decarbonize the economy at the costs of doing so today?

**The argument:** Reliance on CDR substitutes for present-day mitigation. Every climate strategy that "balances" residual emissions with future removals depends on the future removals materializing. If they don't, the strategy fails — but the emissions have already happened. This is the inverse of insurance: rather than paying now to prevent future harm, you're betting on future technology to undo present harm.

**The defense:** Realistic 1.5°C-compatible pathways require both deep mitigation AND CDR — not either/or. The IPCC scenarios assume both. CDR isn't a substitute for mitigation; it's a complement for unavoidable residuals. Treating CDR as an excuse to delay mitigation is misuse, not a feature of the technology.

**Where it lands:** The critique applies most strongly to corporations and governments that use CDR as a substitute for emissions reductions. It applies less to CDR investment that targets genuinely residual emissions or that aims to draw down past emissions. The distinction is policy-design dependent: SBTi V2's structure (mandatory deep reduction first, removals only for residuals) is one approach to limit moral hazard.

## Critique 2: Energy and resource demands

DAC and BECCS at scale require enormous resources.

**DAC at gigaton scale:**
- ~5–10 GJ thermal + electricity per tCO₂.
- 10 GtCO₂/yr DAC requires ~50–100 EJ/yr energy — roughly 10–20% of current global energy consumption.
- This much energy must be zero-carbon for DAC to be net-negative. It can't compete with electrification for clean electricity without scaling clean electricity dramatically.

**BECCS at scale:**
- 5 GtCO₂/yr BECCS would require approximately 5 GtCO₂/yr of biomass capture — roughly 0.5–1 GtC of biomass annually.
- Land requirements: hundreds of millions of hectares of dedicated bioenergy crops, plus management of forest residues and waste streams.
- Water requirements: substantial irrigation in many contexts.

**The argument:** The scale of CDR envisioned in 1.5°C scenarios requires resource allocation that competes with food, water, biodiversity, and other land uses. The "free lunch" framing of CDR understates these trade-offs.

**The defense:** Resource demands can be met through diversification (multiple CDR pathways), efficiency improvements (DAC energy intensity falling), and competition-avoidance (using marginal/degraded land, agricultural residues, waste streams). The trade-offs are real but manageable with thoughtful deployment.

**Where it lands:** Genuine constraints. Gigaton-scale CDR isn't free; it requires real resources that must be allocated thoughtfully.

## Critique 3: Permanence and verification

Stored CO₂ needs to stay stored. The various CDR pathways have different permanence profiles:

- **Geological storage** (DAC, BECCS): centuries to millennia.
- **Mineralization**: geological timescales.
- **Biochar**: 100–1,000+ years depending on conditions.
- **Soil carbon, forestry**: decades to centuries, with reversal risk.

Verification is harder for biological storage than for geological storage. A buried tree might be intact in 100 years, or might not.

**The argument:** Conventional CDR with shorter permanence isn't equivalent to durable storage. Treating them as fungible understates the climate impact.

**The defense:** The same critique applies to compliance accounting generally. As long as durability and verification methods are transparent, buyers can make informed choices.

**Where it lands:** Genuine concern that requires careful methodology. Different durabilities should be priced differently and used differently. SBTi V2 explicitly differentiates by durability for this reason.

## Critique 4: The cost curve

CDR is expensive. DAC at $400–800/tCO₂ today, $250–350 targeted by 2030. Conventional CDR at $5–50/tCO₂ but with quality questions. The cost gap to carbon-pricing instruments is large.

**The argument:** $200/tCO₂ DAC funding 1 GtCO₂/yr requires $200 billion annually. Scaling to 10 GtCO₂/yr requires $2 trillion annually. These are extraordinary commitments for what amounts to climate insurance.

**The defense:** Costs decline with scale. Solar fell 90%; wind fell 50%; batteries fell 80%. Even partial cost declines would substantially improve CDR economics. The investment isn't avoidance-coupled — it's complement to mitigation, not substitute.

**Where it lands:** Real concern that CDR may not scale at affordable costs. The cost trajectory is favorable but not guaranteed.

## Critique 5: The geographic concentration of buyers

80%+ of novel CDR demand comes from a handful of US-based tech companies (Microsoft, Stripe, Google, Meta, etc.). This concentration is a double-edged feature:

**Strength:** Concentrated demand creates revenue certainty for early-stage providers.

**Weakness:** Demand is vulnerable to changes in any single company's strategy. Microsoft's commitment depends on Microsoft's continued strategy. A reversal would collapse much of the demand pool.

**The argument:** Real CDR scale-up requires diversified demand — government procurement, regulated industry, more corporate buyers globally. Current concentration is unsustainable.

**The defense:** Concentrated demand is a feature of early-stage markets generally. Diversification will follow scale. EU CRCF and other policy frameworks will broaden demand.

**Where it lands:** Genuine fragility. The 2026–2030 period will test whether demand diversifies.

## A synthesis

The substantive critiques don't add up to a case for rejecting CDR — they add up to a case for being careful about how CDR is deployed and what it's used to justify. The honest reading: **CDR is necessary for any realistic 1.5°C-compatible pathway**, but it's not a substitute for direct mitigation, its scaling is uncertain, and it requires careful policy design to avoid moral hazard.

---

# Part 7: The path forward 2026–2050

The next 25 years will substantially determine CDR's role in climate strategy.

## Scaling trajectory

Three plausible 2050 outcomes:

**Optimistic case:** Novel CDR scales to 5–8 GtCO₂/yr by 2050. DAC at $150–250/tCO₂; BECCS contributing 1–3 GtCO₂/yr from sustainable biomass; enhanced weathering at 1–2 GtCO₂/yr; biochar at 0.5–1 GtCO₂/yr; combined ocean and mineralization at 0.5–1 GtCO₂/yr. Combined with 5–7 GtCO₂/yr of conventional CDR, total CDR reaches 10–15 GtCO₂/yr — sufficient to enable 1.5°C-compatible pathways with substantial overshoot recovery.

**Central case:** Novel CDR scales to 2–4 GtCO₂/yr by 2050. DAC at $300–500/tCO₂; BECCS at 1–2 GtCO₂/yr (constrained by biomass questions); enhanced weathering at modest scale; biochar contributing meaningfully. Conventional CDR at 4–6 GtCO₂/yr. Combined CDR reaches 6–10 GtCO₂/yr — sufficient for residual neutralization in 1.5–2°C overshoot scenarios but not for substantial overshoot recovery.

**Pessimistic case:** Novel CDR scales to 0.5–1.5 GtCO₂/yr by 2050. DAC remains expensive ($500+/tCO₂); BECCS constrained by sustainability questions; enhanced weathering hits geological constraints; conventional CDR plateaus due to land competition. Combined CDR reaches 3–5 GtCO₂/yr — insufficient for substantial residual neutralization, requiring greater emissions reductions or accepting larger overshoot.

The pessimistic case isn't a worst-case — it's substantially what current trends extrapolated forward would produce. The optimistic case requires substantial policy support, demand-side reform, technology cost declines, and resolution of biomass-sustainability questions.

## Decision points 2026–2030

Several near-term decisions will substantially shape the trajectory:

**The 2026 EU CRCF implementation.** How CDR credits integrate into European policy frameworks. If permanent removals enter the EU ETS as compliance units, demand expands substantially.

**The 2026–2027 SBTi V2 finalization.** What proportion of net-zero claims must come from removals; what durability standards apply; whether the framework is widely adopted.

**The 45Q durability post-OBBBA.** Whether US tax credits at current levels persist or are reduced/eliminated under future administrations.

**Frontier and AMC scaling.** Whether the advance-purchase model scales to $5–10 billion annually or stays in the current $1–2 billion range.

**Article 6 operationalization.** Whether sovereign demand for CDR credits emerges at scale, expanding the buyer pool beyond corporates.

**Major DAC project performance.** Whether Stratos, Project Cypress, the South Texas DAC Hub, Mammoth, and Kenya project deliver on capacity and cost targets.

## **Stop-and-check 11.C**

1. The "central case" 2050 CDR scenario has novel CDR at 2–4 GtCO₂/yr. The IPCC's 1.5°C scenarios assume 5–10 GtCO₂/yr. The gap implies either greater emissions reductions or larger overshoot. Which path is more credible?
2. SBTi V2 mandates increasing removal-credit use over time. If 4,000 SBTi-validated companies all demand removal credits, total demand could reach 1+ GtCO₂/yr by 2050 — orders of magnitude larger than current. Is this realistic?
3. The Frontier model has been described as the most important institutional innovation in early-stage CDR. Why hasn't it been replicated more widely — for renewable energy, batteries, or other clean technologies?
4. **Socratic prompt:** Imagine you're a junior climate-policy advisor in 2026, asked to write a one-page memo on whether the EU should integrate CDR into the ETS. What's the case for, the case against, and what would you recommend?

---

# Closing exercise

Three things to take away:

**1. CDR is structurally necessary but currently far below scale.** Every 1.5°C-compatible pathway requires CDR; current novel-CDR capacity is in the kilotonne range while 2050 requirements are in the multi-gigaton range. The scaling challenge is enormous.

**2. The portfolio approach is more realistic than concentrating on any single technology.** DAC, BECCS, enhanced weathering, biochar, biomass burial, mineralization, and conventional CDR all have roles. None alone can deliver the scale needed at affordable cost.

**3. CDR is necessary but not sufficient.** It works alongside deep mitigation, not as a substitute. The moral-hazard concern is real but addressable through policy design (mandatory deep mitigation first; CDR only for residuals). The 2026–2030 period will substantially determine whether CDR scaling matches climate-scenario assumptions.

The next two chapters look at where the residual emissions actually live (Ch. 12: hard-to-abate sectors) and how corporates structure climate strategies that integrate everything we've covered (Ch. 13: net zero and disclosure).

---

# What this chapter simplified

**1. The atmospheric carbon budget mechanics.** The relationship between CDR scale and temperature outcomes depends on the specific carbon-cycle response, which I treated lightly. The actual modeling involves complex feedbacks (ocean uptake, terrestrial sinks, methane decay, aerosol effects) that affect how much CDR is needed for a given temperature target.

**2. The detail of each CDR technology's lifecycle accounting.** Each pathway has substantial lifecycle accounting nuance — energy sources, supply-chain emissions, indirect land-use change, and so on. I gave summary treatment; detailed comparisons require detailed lifecycle analyses.

**3. Methodologies for verification.** Each CDR pathway has different verification challenges. DAC + geological storage: relatively straightforward (CO₂ flow meters, geological monitoring). Enhanced weathering: complex (depends on long-term reaction kinetics, soil chemistry, water flow). Biochar: depends on biochar quality assessment and soil application accounting. The methodology literature is technical and substantial.

**4. The geographic specificity of CDR.** Different regions have different CDR profiles. Iceland (geothermal + basalt = DAC + mineralization); the Permian Basin (geological storage + EOR opportunity); Brazil (biomass + soil carbon); Australia (enhanced weathering with abundant olivine). I gave brief mention; the geographic specifics matter enormously for project economics.

**5. The integration with hard-to-abate sectors.** CDR's primary near-term economic case is in sectors where mitigation is hard (Chapter 12). The pairing of cement-with-DAC, steel-with-BECCS-residuals, aviation-with-direct-DAC-offsets is where the policy and economics intersect. I'll cover the receiving sectors in Ch. 12.

---

# Glossary delta (Chapter 11)

- **AMC (Advance Market Commitment)** — Pre-purchase commitments by aggregated buyers that provide revenue certainty for early-stage suppliers. Frontier is the leading CDR AMC.
- **BECCS (Bioenergy with Carbon Capture and Storage)** — Burning biomass and capturing the resulting CO₂. Treated as net-negative emissions when biomass is sustainably sourced.
- **Biochar** — Charcoal-like material produced by pyrolyzing biomass; applied to soils for carbon sequestration plus soil benefits.
- **Biomass burial** — Storing biomass under conditions that prevent decomposition.
- **Carbfix** — Iceland-based mineralization CDR; injects dissolved CO₂ into basaltic formations.
- **Climeworks** — Swiss DAC company. Operates Orca (4 ktCO₂/yr, 2021) and Mammoth (36 ktCO₂/yr, 2024) in Iceland; planning Project Cypress (Louisiana) and Kenya project.
- **CRCF (Carbon Removals Certification Framework)** — EU framework for CDR certification. Formalized December 2024.
- **DAC (Direct Air Capture)** — Capture of CO₂ from ambient air through chemical processes.
- **DAC Hubs** — US DOE program; $1.2 billion to two hubs (South Texas, Project Cypress) plus additional rounds.
- **Drax** — UK biomass power plant; proposed BECCS at 8 MtCO₂/yr.
- **Enhanced Rock Weathering (ERW)** — Spreading crushed silicate rocks (basalt, olivine) on land to accelerate natural CO₂-rock reactions.
- **Frontier** — Stripe-led AMC for CDR; $1B+ committed through 2030 across multiple suppliers.
- **Heirloom** — US mineralization-based DAC company. Uses calcium hydroxide on outdoor trays.
- **L-DAC (Liquid solvent DAC)** — DAC using alkaline aqueous solution and high-temperature regeneration. Stratos technology.
- **Mammoth** — Climeworks' Iceland DAC facility. 36 ktCO₂/yr design capacity; operational May 2024.
- **Mineralization** — Reaction of CO₂ with reactive rocks to form stable carbonate minerals.
- **Moral hazard** — In CDR context: the concern that CDR availability reduces incentive for direct mitigation.
- **Ocean Alkalinity Enhancement (OAE)** — Adding alkaline materials to seawater to increase ocean CO₂ uptake.
- **1PointFive** — Occidental Petroleum subsidiary operating Stratos DAC facility and South Texas DAC Hub.
- **Orca** — Climeworks' first commercial DAC facility (Iceland, 4 ktCO₂/yr, 2021).
- **Permanence** — Duration of CO₂ storage. DAC + geological: centuries-millennia. Forestry: decades-centuries.
- **Project Cypress** — Climeworks-Heirloom DOE DAC Hub in Louisiana; 1 MtCO₂/yr target.
- **S-DAC (Solid sorbent DAC)** — DAC using solid sorbent and lower-temperature regeneration. Climeworks technology.
- **Stockholm Exergi** — Swedish utility; BECCS at Värtaverket CHP plant; FID 2024 for 800 ktCO₂/yr.
- **Stratos** — 1PointFive's L-DAC facility in Texas; 500 ktCO₂/yr design capacity; ramping in 2025–2026.
- **Vaulted Deep** — US biomass burial CDR company.
- **Verra-style verification** — Refers to the lifecycle of project methodology, validation, monitoring, verification, and credit issuance (covered in Ch. 8). Applies to CDR projects under voluntary market frameworks.

---

# What's next

CDR addresses the residuals; the remaining emissions live in **hard-to-abate sectors**. Chapter 12 covers steel, cement, chemicals, aviation, and shipping — the industrial backbone where deep decarbonization is hardest and where most residual emissions accumulate.

Chapter 13 then covers how corporates structure net-zero strategies that integrate everything: emissions reductions, residual neutralization, removal purchases, disclosure, and target validation.

