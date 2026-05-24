# Chapter 3 — The CO₂ Molecule Value Chain

**Track:** Foundations & Physical Carbon (A), with forward links to Tracks B and C
**Prerequisites:** Chapter 1 (carbon chemistry, the cycle).
**Helpful prior:** Chapter 2 (the parallel commodity-carbon framing).
**What you should be able to do by the end:**
- Distinguish the *capture-and-storage* value chain (where the goal is to remove CO₂ from the atmosphere/emissions) from the *merchant CO₂* value chain (where CO₂ is a useful industrial gas with established markets), and name three places where they collide.
- Sketch the CO₂ molecule's path from a major industrial point source (cement plant, ethanol fermenter, gas processing facility) through compression/liquefaction, midstream transport (pipeline, truck, ship), to one of four destinations: storage, EOR, merchant sale, or product conversion.
- Explain why the existing US CO₂ infrastructure (~5,000 miles of pipeline, ~70 Mt/yr of CO₂-EOR) emerged from oil-field development, not climate policy, and why that legacy shapes the current politics.
- State, with specifics, what changed about US CCS economics in 2022 (IRA's expansion of 45Q) and again in 2025 (OBBBA's parity between sequestration and EOR), and why the second change is a structurally different signal than the first.
- Articulate why the Satartia, Mississippi pipeline rupture (Feb 2020) is the canonical case study for CO₂ pipeline safety policy, and what PHMSA proposed in January 2025 in response.
- Identify the three or four CCS hub projects most likely to define the 2025–2030 CCS landscape — North Sea (Northern Lights, Porthos, Aramis), US Gulf Coast (Houston Ship Channel, ExxonMobil), Alberta (ACTL/Pathways), and the Midwest ethanol corridor — and their distinctive characteristics.

---

## Why this chapter exists, separately from Chapter 10

Most carbon curricula collapse "what we do with CO₂" into a single CCUS chapter. That obscures two distinct things.

The first is the **physical value chain of the CO₂ molecule** — how it moves through space and over time, from wherever it's generated to wherever it ends up. That's an infrastructure story (pipelines, pumps, ships, tanks, wells) with mostly engineering and permitting questions, and it has *existed for decades* because CO₂ has industrial uses long predating any climate motivation.

The second is the **technology and policy of capturing CO₂ for climate purposes** — the actual capture step at a source or from ambient air, the policy frameworks (45Q, EU funding, UK Track-1/2 clusters) that make capture economic, and the regulatory regime for permanent storage (Class VI wells, MMV requirements). That's a climate-policy story.

Chapter 3 covers the first; Chapter 10 covers the second. They overlap — most of the actually-built CCS projects use the same kind of midstream infrastructure as the legacy CO₂-EOR network — but treating them separately lets us see something important: the *molecule* value chain is mature, while the *climate-motivated capture-and-store* value chain is still nascent and being built on top of (and sometimes in tension with) the legacy infrastructure.

You'll also see in this chapter why one of the things you specifically asked about — **the Baytown-type project** — sits at the interface. ExxonMobil's Baytown low-carbon hydrogen project (paused in November 2025) was simultaneously a hydrogen play, a CCS play, an industrial-gas play, and a Gulf Coast pipeline-network play. None of those framings alone captures what was being built.

---

# Part 1: Where CO₂ comes from — sources, ranked by what matters

Whether you're capturing CO₂ for storage, capturing it for sale, or just trying to understand industrial gas flows, sources matter — but not in the way emissions inventories rank them. A power plant emitting 5 Mt of CO₂ per year and an ammonia plant emitting 0.5 Mt are both "sources" in a GHG inventory. But from the perspective of *capturing* the CO₂, they're radically different problems with radically different costs.

Three things determine how attractive a source is for CO₂ capture:

**1. Concentration.** Power plant flue gas is ~4–15% CO₂ by volume; the rest is mostly nitrogen plus water vapor, oxygen, NOx, SOx. Ammonia plant tail gas is ~99% CO₂. The thermodynamic minimum work to separate CO₂ from a mixture scales steeply with how dilute it is, and the real engineering costs scale even more steeply. So concentrated streams are much cheaper to capture from than dilute ones.

**2. Pressure.** A stream already at elevated pressure (a gas-processing plant separating CO₂ out at 30 bar) doesn't need to spend much extra energy on compression. Atmospheric-pressure flue gas needs to be compressed to ~100+ bar for transport in supercritical phase, which is a major operating cost.

**3. Purity.** CO₂ for food and beverage use needs to be very pure — typically <50 ppm of various contaminants. CO₂ for EOR can tolerate more impurities. CO₂ for permanent storage is somewhere in between, depending on the operator's specs. A source whose CO₂ stream is already nearly pure (ethanol fermentation: pure CO₂ + trace ethanol vapor) is structurally cheaper to clean up than a source with lots of impurities (power plant flue gas: SO₂, NOx, mercury, particulates).

These three factors are why the "cost per ton captured" varies by an order of magnitude across sources. Here's the rough cost stack (LCOA — *levelized cost of avoided* or *captured* — figures are approximate, in 2024 dollars):

- **Natural gas processing** ($15–25/tCO₂): CO₂ is *already* being separated to meet pipeline gas spec. The capture cost is just adding compression. Almost trivial.
- **Ammonia production** ($25–50/tCO₂): The Haber-Bosch front-end produces a nearly-pure CO₂ stream from steam methane reforming. Easy capture.
- **Ethanol fermentation** ($25–50/tCO₂): Fermentation produces a nearly-pure CO₂ stream as fermentation byproduct. Most ethanol plants vent it today, but capturing it is mechanically simple. This is what most of the proposed Midwest CCS pipelines are built around.
- **Hydrogen production (SMR with capture)** ($50–80/tCO₂): Steam methane reforming produces a CO₂ stream that's easier to separate if captured at the shift converter, harder if captured at the boiler exhaust. "Blue hydrogen" is built on this.
- **Cement** ($60–120/tCO₂): Cement is a hard case. Roughly 60% of cement's CO₂ comes from process emissions (calcium carbonate decomposition, CaCO₃ → CaO + CO₂) — which is *unavoidable* by switching fuels. The flue gas has a moderate CO₂ concentration (~20–25%) but contains dust, sulfur, and other impurities. Northern Lights' first customer (Heidelberg Materials' Brevik cement plant) was the world's first cement CCS at scale.
- **Steel (BF-BOF)** ($60–110/tCO₂): Multiple gas streams (coke oven gas, blast furnace top gas, BOF gas) with different concentrations and contaminants. Capture economically only at full-system scale.
- **Power generation (post-combustion)** ($60–100/tCO₂ for coal, $90–140 for gas): Dilute streams, large volumes, hard. Boundary Dam (Saskatchewan, coal) and Petra Nova (Texas, coal — shut down 2020) are the demonstration cases.
- **Direct Air Capture (DAC)** ($400–1,000+/tCO₂ today): Capturing from atmospheric concentration (~425 ppm = ~0.04%) is the hardest because the dilution is extreme. We cover DAC in Chapter 11.

This cost ordering — gas processing → ammonia/ethanol → hydrogen → cement → steel → power → DAC — is the **order in which CCS is being built**, in roughly that sequence. The cheap-to-capture sources go first; the dilute-stream applications wait.

## Where the CO₂ actually comes from today (US example)

Of the ~5,000 miles of US CO₂ pipeline currently operating, the source breakdown is approximately:

- **Natural sources** — naturally-occurring CO₂ from underground reservoirs like Bravo Dome (New Mexico), McElmo Dome (Colorado), Sheep Mountain (Colorado), Jackson Dome (Mississippi). These domes are CO₂ "fields" in the same geological sense as oil fields. The CO₂ is mined and piped to oil fields for EOR. **This is a substantial fraction of historical US CO₂-EOR volume** — over half by some estimates — and it's not even arguably climate-positive. Pumping naturally-sequestered CO₂ out of the ground to inject it into oil fields adds net atmospheric CO₂ regardless of how much oil is produced.
- **Gas processing plants** — particularly LaBarge, Wyoming (ExxonMobil's Shute Creek), the largest single anthropogenic CO₂ source in the world for EOR. ~7 Mt/yr captured.
- **Ammonia and methanol plants** — Coffeyville Resources (Kansas), various Gulf Coast facilities.
- **Ethanol plants** — Archer Daniels Midland's Decatur, Illinois plant has been doing this longest.
- **Coal gasification** — formerly the Great Plains Synfuels Plant (Beulah, ND) supplied CO₂ via the largest CO₂ pipeline in North America to Weyburn in Saskatchewan; that pipeline shut down in 2021 when the synfuels economics deteriorated.

Outside the US, the global merchant CO₂ market (food, beverage, industrial) is supplied largely from ammonia plants and ethanol plants — wherever the byproduct CO₂ stream is cheap to clean up and there's local demand. This is why merchant CO₂ supply tightens whenever ammonia or ethanol plants go offline; we'll see this in Part 4.

## **Stop-and-check 3.A**

1. A flue gas stream is 12% CO₂; an ammonia plant tail gas is 99% CO₂. The thermodynamic work of separation scales roughly with the negative log of CO₂ mole fraction. Approximately how much more *thermodynamic minimum* work does the 12% stream require per ton of CO₂ captured? (Real engineering cost is much higher than thermodynamic minimum, but the ratio is indicative.)
2. Why is natural CO₂ extraction from underground domes (e.g., Bravo Dome) for EOR *not* climate-positive — and arguably net-emitting? What's the right counterfactual, and where does the naïve mass balance go wrong?
3. Cement is unusual because most of its CO₂ comes from process chemistry rather than fuel combustion. Why does this make cement decarbonization different from, say, decarbonizing a coal power plant?
4. **Socratic prompt:** If you were building a CCS portfolio today and you had to rank sources by economic attractiveness, you'd start with gas processing and ammonia. But these are also the sources that *already* capture CO₂ — they're not net-new mitigation, they're getting paid for what they were doing anyway. Is paying 45Q credits for these "additional" or just rent-seeking? How would you tell the difference? (This is the **additionality** question that will dominate Chapter 8.)

**Answers**

1. The thermodynamic minimum work scales as −R·T·ln(y), where y is the mole fraction of CO₂ in the gas. For 12% CO₂: −ln(0.12) ≈ 2.12. For 99% CO₂: −ln(0.99) ≈ 0.01. The ratio is about 200×. In practice, real engineering costs diverge from thermodynamic minimums due to mass transfer, solvent regeneration, and infrastructure — but the ratio is directionally correct and explains why ammonia/gas processing capture costs ($15–25/tCO₂) are roughly 10–20× lower than point-source combustion capture ($60–120/tCO₂).

2. The answer hinges on the counterfactual, and the naïve mass balance picks the wrong one. The dome CO₂ was already *permanently and safely sequestered* underground, so the correct baseline is "leave it there." Mine it and inject it into an oil reservoir and, in the best case where every ton stays put, you've merely moved sequestered carbon from one geological store to another — zero climate benefit, and not a removal. But it's worse than neutral, for two reasons: (a) extraction, processing, and EOR operations vent a fraction, and oil reservoirs aren't engineered for permanence the way dedicated storage is, so some CO₂ that would otherwise have stayed buried forever reaches the atmosphere; and (b) the whole purpose is to recover additional oil, which is then burned. So against the proper "leave it sequestered" baseline, mining dome CO₂ for EOR is net-emitting — exactly why the body calls it "not even arguably climate-positive." The seductive "-1 extracted + 1 re-injected = 0" balance is the trap: it treats the molecule as if it had been in the atmosphere to begin with, ignoring that it started in permanent storage and that the operation exists to produce more fossil carbon.

3. Cement's ~60% of CO₂ comes from calcination — CaCO₃ → CaO + CO₂ — which is a *chemical reaction*, not combustion. You can't avoid it by switching to renewable energy. Decarbonizing a coal power plant is primarily about the fuel: switch to gas, switch to renewables, add CCS to the flue gas. Cement requires CCS at the calcination step regardless of fuel choice, or a chemical substitute for clinker (SCMs, alternative binders), or a completely different chemistry (Sublime Systems' electrochemical approach, calcium looping). This makes cement structurally harder to decarbonize than power generation.

4. The additionality test is: would the CO₂ separation have happened anyway without the 45Q credit? For gas processing, the answer is yes — operators must remove CO₂ to meet pipeline specifications; the capture happens regardless. If 45Q pays for capturing CO₂ that would have been captured anyway (just vented rather than stored), the credit is not funding new climate action; it's funding infrastructure for storage. That's not necessarily rent-seeking — dedicated storage is genuinely incremental — but the *mitigation* (CO₂ removal from the atmosphere) only occurs in the storage step, not the capture step. Rent-seeking vs. legitimate subsidy depends on whether the storage would have happened at all without the credit (likely not) versus whether the capture would have happened at all without the credit (likely yes, but vented).

---

# Part 2: The midstream — getting CO₂ from there to here

Once you have CO₂, the question is how to move it. There are three options: pipeline, truck, and ship. They serve different distance/volume regimes.

## Pipelines

Pipelines are the workhorse of the existing US CO₂ economy and the assumed solution for most large-scale future CCS. The US currently operates **~5,000 miles of CO₂ pipeline**, the densest CO₂ pipeline network in the world. By comparison, the US has ~2.6 million miles of natural gas pipeline — so CO₂ infrastructure is about 0.2% the size of the gas network. PHMSA estimates that the CO₂ pipeline mileage could expand by **roughly 10× by 2050** under aggressive CCS scenarios.

Most existing CO₂ pipelines are in three regions:

- **Permian Basin (Texas / New Mexico)** — Dense network connecting Bravo Dome, Sheep Mountain, and the Shute Creek (LaBarge) sources to Permian oil fields for EOR. Operated primarily by Kinder Morgan, ExxonMobil (formerly Denbury), Occidental, and a handful of others.
- **Mississippi / Gulf Coast** — Denbury's network (acquired by ExxonMobil for $4.9B in 2023) connecting Jackson Dome and several anthropogenic sources to oilfields and, increasingly, to proposed storage sites along the Gulf. ~925 miles. This is the network through which Satartia's rupture occurred.
- **Wyoming / Western Plains** — Shute Creek hub, connecting to oil fields and increasingly to ethanol-corridor capture projects.

CO₂ in pipelines is usually transported in **supercritical phase** — above its critical point of 31°C and 74 bar, where it behaves as a dense fluid that's neither liquid nor gas. Supercritical CO₂ is denser than gas (so more mass moves per unit volume of pipe) and behaves more like a liquid (so single-phase flow is easier to manage). Operating pressures in CO₂ pipelines are typically 100–150 bar — comparable to natural gas pipelines but with very different physics because of supercritical-phase behavior.

**Pipeline construction cost** for CO₂ is comparable to natural gas pipelines, on the order of **$1–4 million per mile** for typical onshore terrain, more for difficult terrain or larger diameters. Summit Carbon Solutions' Midwest project was originally estimated at ~$5.5 billion for ~2,000 miles — about $2.75M/mile. The new Iowa-to-Wyoming route is reportedly ~200 miles shorter.

## CO₂ pipeline safety: the Satartia case

CO₂ pipelines have a long safety record, but the Satartia, Mississippi event on **February 22, 2020** changed the politics.

A 24-inch Denbury Gulf Coast Pipelines CO₂ line ruptured during heavy rains. The line was carrying supercritical-phase CO₂. When it failed, **the CO₂ depressurized and formed a dense, low-lying cloud** that flowed downhill toward the small community of Satartia (population ~30). Because CO₂ is heavier than air, it displaced oxygen in low-lying areas; because the gas is invisible and largely odorless, residents had no warning.

**More than 45 people were hospitalized.** Vehicles entering the cloud stalled because internal combustion engines need oxygen to run. Emergency responders arrived without knowing they were entering a CO₂ release; some were exposed before they could evacuate. The town was evacuated. There were no fatalities, but several people experienced severe hypoxia and lingering health effects.

The PHMSA failure investigation, completed in 2022, found that the rupture was caused by **soil movement** (a landslide triggered by heavy rains saturating the soil over the pipeline route), exacerbated by **operator failures** including inadequate consideration of geohazards in route selection, insufficient leak detection, and slow emergency notification of local responders.

The PHMSA failure-investigation report and Dan Zegart's subsequent longform investigation ("The Gassing of Satartia," *HuffPost*) brought the incident to national attention and made CO₂ pipeline safety a permitting issue everywhere subsequent projects have been proposed. Iowa, South Dakota, North Dakota, Nebraska, Minnesota, Illinois, Louisiana — every state with a pending CO₂ pipeline application now treats Satartia as a touchstone for what could go wrong.

## The PHMSA rulemaking

On **January 10, 2025** — in the closing days of the Biden administration — PHMSA issued a **Notice of Proposed Rulemaking (NPRM)** to update CO₂ pipeline safety regulations under 49 CFR Part 195. Key proposed changes:

- **Bringing gas-phase and liquid-phase CO₂ pipelines under Part 195** for the first time (previously only supercritical-phase CO₂ was regulated).
- **Mandatory vapor dispersion analysis** for CO₂ pipelines, considering terrain and weather conditions, or use of a simplified 2-mile "could-affect" distance.
- **Leak detection systems** for all CO₂ pipelines, with additional monitoring for supercritical/liquid lines.
- **Fixed vapor detection and alarms** at specific facilities.
- **Operator training and equipment provided to local emergency responders** along pipeline routes.
- **Updated reporting requirements**, integrity-management programs, and route-selection criteria for geohazards.

The NPRM was a direct response to Satartia. Its status as of writing: **the comment period followed publication in the Federal Register, but the Trump administration that took office in January 2025 has not yet finalized the rule, and CCS-industry stakeholders (Carbon Capture Coalition, Global CCS Institute) have lobbied for various modifications.** Whether the rule is finalized as proposed, weakened, or shelved is a live question that materially affects the cost and timeline of every proposed CO₂ pipeline in the US. *If you're reading this and want the current status, search PHMSA-2022-0125 docket.*

## Trucking and shipping

For smaller volumes or shorter distances — typically less than ~1,000 km and ~1 Mt/yr — pipelines don't pencil out and CO₂ is moved by **trucks** (cryogenic tanker, carrying liquefied CO₂ at about -25°C and 20 bar) or **rail** (similar tankers). This is how the merchant CO₂ market mostly works today: industrial gas companies receive CO₂ from a source plant, liquefy it, store it, and truck it to beverage distributors, food processors, welding-supply distributors, etc. A typical CO₂ tanker truck carries ~20 tons.

For longer distances or where pipelines are infeasible — particularly **across water** — **ships** are the alternative. CO₂ shipping is mature for the small specialty market (food-grade CO₂ moves by ship internationally for decades) but is now scaling up for industrial CCS purposes. Northern Lights' Phase 1 operations rely on **dedicated CO₂ carrier ships** that pick up CO₂ from coastal capture sites (Heidelberg cement plant in Brevik, Norway; Hafslund Celsio's waste-to-energy plant in Oslo) and deliver it to the Øygarden terminal for pipeline-and-injection.

Northern Lights commissioned two purpose-built **7,500 m³ LCO₂ carriers** (the *Northern Pioneer* and *Northern Pathfinder*) in 2024–2025. These ships transport liquefied CO₂ at ~7 bar and ~-50°C — different operating conditions than long-distance pipeline transport. Shipping costs are higher per ton-km than pipeline at full pipeline utilization but lower than building a pipeline for a smaller throughput, especially across water where pipelines are very expensive.

The ship-based model is structurally important for European CCS because Europe lacks the dense onshore CO₂ pipeline network of the US Gulf, and many of the best storage sites (depleted North Sea oil and gas reservoirs) are offshore. **The Northern Lights architecture — ship-collected CO₂ from distributed sources, single offshore storage hub — may become the European template.** Similar models are being developed for Porthos (Netherlands), Aramis (Netherlands), and Acorn (UK).

## **Stop-and-check 3.B**

1. Supercritical CO₂ is denser than gaseous CO₂ but less dense than liquid CO₂. Why is supercritical phase the preferred state for long-distance pipeline transport, but liquid phase the preferred state for trucking and shipping?
2. The Satartia rupture happened because of soil movement, not equipment failure or operator error in the pipeline-operation sense. Why does this make CO₂ pipeline siting different from natural gas pipeline siting?
3. Compare the European ship-based CCS architecture (Northern Lights) with the US pipeline-based architecture (Gulf Coast). What are the structural advantages and disadvantages of each? Where will each scale better?
4. **Socratic prompt:** PHMSA's NPRM applies to *any* CO₂ pipeline regardless of motivation — climate CCS, EOR, merchant supply. Should it? Are there arguments for different safety standards based on what the CO₂ is being used for?

**Answers**

1. Supercritical CO₂ behaves like a dense fluid (high density, single phase) — enabling high mass throughput per unit of pipe diameter and avoiding the two-phase flow complications that make liquid pipelines technically demanding at small scales. For trucking and shipping, liquefied CO₂ (−25°C, ~20 bar) is preferred because: (a) liquefaction is more practical at small volumes than compressing to supercritical conditions; (b) liquid density is similar to supercritical; and (c) cryogenic tanker technology is well-established and widely available. Pipeline supercritical is cost-optimal at large throughput; trucking/shipping liquid is cost-optimal at small throughput.

2. Natural gas pipeline ruptures release a flammable/explosive gas that dissipates rapidly. CO₂ is heavier than air and hugs the ground; it displaces oxygen silently and invisibly. Satartia showed that geohazards (soil movement, flooding) that trigger rupture can coincide with atmospheric conditions (valley topography, calm wind) that concentrate the plume near populated areas. Natural gas pipeline siting has learned from decades of flammable-gas accidents; CO₂ pipeline siting requires its own body of standards specifically for asphyxiation hazard in low-lying terrain. The hazard profile is different enough that it can't simply be copied from gas-pipeline practice.

3. US pipeline-based architecture advantages: low per-ton-mile cost at large scale; leverages existing Permian EOR infrastructure; connects many inland industrial sources to Gulf Coast storage. Disadvantages: permitting and right-of-way acquisition is politically intense; requires large upfront investment; only viable for high-volume, fixed-route flows. European ship-based architecture advantages: flexible — can collect from any coastal emitter; no onshore pipeline permitting; scalable incrementally. Disadvantages: higher per-ton cost than pipeline at large scale; requires liquefaction at source and regasification at storage terminus; CO₂ shipping infrastructure still developing. Pipeline scales better where the industrial landscape is dense and routes are fixed; ships scale better where sources are dispersed, volumes are uncertain, or the geography is archipelagic/coastal.

4. The substantive argument for same standards is that CO₂ physics is the same regardless of motivation: a CO₂ pipeline rupture creates the same asphyxiation hazard whether the CO₂ was captured for climate CCS, EOR, or beverage supply. Safety standards should follow the hazard, not the motivation. The counter-argument — that climate CCS should face lighter standards to avoid slowing deployment — would be ethically indefensible if applied to, say, flammable pipelines. The appropriate policy response is to speed up permitting processes, not to weaken safety standards.

---

# Part 3: The hubs — where the future is being built

CCS at scale doesn't work as one-project-at-a-time individual capture-pipeline-storage chains. The economics demand **hubs**: clusters of multiple capture sources sharing midstream and storage infrastructure. This is the model being built simultaneously in five major regions.

## The North Sea: Northern Lights (Norway), Porthos & Aramis (Netherlands), Acorn (UK)

**Northern Lights (Norway).** Operational since August 2025 — the world's first open-access (third-party) CO₂ transport and storage facility. The joint venture is equally owned by Equinor, Shell, and TotalEnergies. Phase 1 capacity: **1.5 Mt CO₂/year**. The first injection occurred August 25, 2025, with CO₂ shipped from Heidelberg Materials' Brevik cement plant. Storage is in the **Aurora reservoir, 2,600 meters below the seabed** off Øygarden in western Norway.

Phase 2 reached FID in March 2025 — investing NOK 7.5 billion (~$700 million) to expand capacity to **at least 5 Mt/year by 2028**. Phase 1 capacity is already fully booked by five industrial customers: Heidelberg Materials (Norway), Hafslund Celsio (Oslo waste-to-energy), Yara (Netherlands ammonia), Ørsted (Denmark biomass power), Stockholm Exergi (Sweden biomass power). The Norwegian government is covering ~80% of Phase 1 costs through the Longship program — a critical fact, because it makes Northern Lights *not* a market-rate test of CCS economics but a government-subsidized demonstrator.

**Porthos (Netherlands).** ~2.5 Mt/year planned, storing CO₂ from Rotterdam-area industries in depleted North Sea gas reservoirs. Reached FID in October 2023, currently in construction, first injection now expected second half 2027 (delayed from original 2026 target due to supply-chain and first-of-kind complexity).

**Aramis (Netherlands).** Larger and later than Porthos — targeting 22 Mt/year of capacity in the long run, with the first phase ~5 Mt/year. Partners include Shell, TotalEnergies, EBN, Gasunie. FID was originally targeted for 2024 but slipped; the project remains in late-stage development.

**Acorn (UK).** Scotland-based, intended to repurpose existing North Sea gas infrastructure for CO₂. Approved in October 2023 as part of the UK's Track-1 CCUS cluster sequencing. First injection planned ~2027.

The North Sea is geologically well-suited to CO₂ storage — well-characterized depleted reservoirs, decades of subsurface engineering experience from oil and gas, and existing offshore infrastructure that can be partly repurposed. The political backing is strong (Norwegian and UK governments have made CCS a strategic priority). The North Sea cluster may end up storing 30–50 Mt/yr by the early 2030s — a substantial fraction of total global CCS deployment.

## The US Gulf Coast: Houston, Baytown, and the Denbury legacy

The US Gulf Coast is the world's largest concentration of industrial CO₂ sources — refineries, petrochemicals, ammonia, hydrogen, cement, gas processing. It's also home to the world's largest existing CO₂ pipeline network (the Denbury system, acquired by ExxonMobil in 2023). And it has excellent subsurface storage potential in saline formations along the Gulf.

**ExxonMobil and Baytown.** ExxonMobil announced in 2022 a major Baytown low-carbon hydrogen project: producing up to **1 billion cubic feet/day of "blue hydrogen"** from natural gas with **>98% CO₂ capture** (~7 Mt CO₂/yr captured) for storage in nearby saline formations and EOR sites. The hydrogen would supply ExxonMobil's own olefins plant (cutting integrated complex emissions ~30%) and external customers.

In **November 2025**, ExxonMobil CEO Darren Woods announced the Baytown blue-hydrogen project was being **paused** due to weak customer demand and changes to the §45V clean hydrogen tax credit under OBBBA. This was a major signal: the most-resourced energy major's flagship low-carbon hydrogen project, in the most-resourced infrastructure region, with the most generous federal subsidies in history, couldn't find paying customers.

However, the broader **Houston Ship Channel CCS Alliance** continues. ExxonMobil has separately committed to provide third-party CO₂ transport and storage services for ~6.7 Mt/year of CO₂ from non-ExxonMobil emitters — independent of the hydrogen project. The carbon capture infrastructure exists (or is being built) regardless of whether the hydrogen plant gets built. Other Houston Ship Channel emitters — refineries, petrochemicals, ammonia plants — are signing offtake agreements with ExxonMobil's CCS services.

**Other Gulf Coast hubs:**
- **Stratos (Occidental)** — Permian Basin DAC facility (1st phase 500,000 t/yr capture from atmosphere, commercial operation 2025), built by Occidental's 1PointFive subsidiary, captured CO₂ stored locally.
- **Talos Energy and Carbonvert** — partnered with Louisiana's Carbon Hub on saline storage.
- **Air Products / Eastman Cyclyx / various** — multiple Gulf Coast CCS proposals at various FID stages.

The Gulf Coast model is **brownfield development** — leveraging existing pipeline networks, existing industrial sources, existing subsurface expertise. Distinct from Northern Lights (greenfield, ship-based) and from Midwest (greenfield, pipeline-based, ethanol-focused).

## Alberta: Pathways and ACTL

Alberta has been doing CO₂-EOR for decades and currently operates the **Alberta Carbon Trunk Line (ACTL)** — a ~240 km pipeline taking CO₂ from a fertilizer plant (Nutrien) and a refinery (Sturgeon/North West) to Enhance Energy's EOR operations. ~1.6 Mt/yr capacity, operational since 2020.

The big proposed project is the **Pathways Alliance** — a consortium of six oil sands operators (Suncor, Cenovus, Imperial, ConocoPhillips, MEG Energy, Canadian Natural) targeting CCS for oil sands emissions. Headline number: ~10 Mt CO₂/yr captured from oil sands facilities, transported via a new ~400 km pipeline to a planned saline storage hub in northeastern Alberta. Total project cost estimated at ~$16 billion.

Pathways has been **slow**. The consortium had been waiting on federal and provincial regulatory and financial commitments through 2023–2024, with the project in a "ready when policy allows" holding pattern. The change of Canadian federal government in 2025 has shifted the policy framework; the project's FID timing remains uncertain.

The Pathways project is also politically loaded in a way Northern Lights isn't — it's CCS *on* oil sands extraction, which critics argue is using carbon capture to extend the life of one of the most carbon-intensive oil production processes in the world. The Pathways defenders argue that oil sands operate regardless of CCS and capturing their emissions is strictly additional to the baseline. Both arguments have merit. This is a Chapter 10 debate.

## The US Midwest: Summit and the ethanol corridor

The Midwest US story is unusual because it's not anchored to fossil fuels. It's anchored to **corn-ethanol fermentation CO₂** — a stream that's nearly pure CO₂ as a fermentation byproduct, currently vented at every US ethanol plant. The economics: capturing this CO₂ is mechanically simple and earns 45Q credits; the catch is that you have to *transport* it to a storage site, and the Midwest doesn't have one nearby.

**Summit Carbon Solutions** — the largest proposed Midwest CCS project, originally planned as a 5-state, ~2,000 mile pipeline collecting CO₂ from ~57 ethanol plants in Iowa, Minnesota, South Dakota, North Dakota, and Nebraska, delivering it to a saline storage site in North Dakota.

Summit's story has been a master class in how CCS projects can fall apart even with strong economics:

- **June 2024.** Iowa Utilities Commission issues a conditional permit, contingent on Summit obtaining permits in North and South Dakota.
- **2024–2025.** South Dakota's Public Utilities Commission denies Summit's permit application twice, after intense landowner opposition.
- **March 2025.** South Dakota enacts a state law (HB 1052) **prohibiting the use of eminent domain for CO₂ pipelines**. This breaks Summit's ability to assemble contiguous rights-of-way through the state.
- **2025.** A North Dakota judge revokes Summit's underground storage permit, citing inadequate review.
- **September 2025.** Summit files a petition with the IUC to amend its Iowa permit to remove the requirement for Dakota approvals.
- **July 4, 2025.** The OBBBA is signed into law, enacting **45Q parity between sequestration and EOR** — meaning Summit can earn the same credit value piping CO₂ to oil-recovery sites as to dedicated storage.
- **May 2026.** Summit announces a **fundamental project pivot**: a new westward route from Iowa through Nebraska to a **sequestration site in Wyoming**, plus stated interest in EOR uses. The original North Dakota storage destination is no longer the primary plan. The pipeline shrinks by ~200 miles and ~400 landowners are removed from the affected route. Summit also scrubs "climate change" references from its website and reframes the project as supporting "America's long-term goal of energy dominance."

The Summit story is the canonical case study of CCS pipeline politics: **strong economics, weak property-rights coalition, regulatory cascade failures, and a project that survives by transforming its identity in response to political signals**. Whether the new Nebraska-to-Wyoming route survives the next round of property-rights pushback is the question of the next 12–18 months.

**Navigator CO2 Ventures**, a competing Midwest CO₂ pipeline proposal targeting ethanol plants in five states, **cancelled its project in October 2023** after similar regulatory and landowner resistance. Navigator's cancellation was the first major casualty of the post-IRA CCS rush. Summit's transformation may be the second.

## Comparison

| Hub | Architecture | Capacity (planned) | Status | Key challenge |
|---|---|---|---|---|
| Northern Lights | Ship-collected, single offshore storage | 1.5 Mt/yr (Phase 1, fully booked); 5+ Mt/yr (Phase 2, 2028) | Phase 1 operational since Aug 2025 | Cost — heavily subsidized by Norwegian government |
| Porthos | Pipeline from Rotterdam to North Sea | 2.5 Mt/yr | Construction, first injection ~H2 2027 (slipped) | EU funding, industrial customer offtake |
| Aramis | Larger Dutch project | Up to 22 Mt/yr long-term | Pre-FID | Customer commitments, financing |
| Acorn | UK Scotland cluster | TBD, multi-Mt/yr | Approved Track-1, ~2027 injection | Cost competitiveness |
| Gulf Coast (ExxonMobil/Houston) | Pipeline, brownfield infrastructure | ~6.7 Mt/yr third-party + 7.5 Mt/yr Baytown (paused) | Phased buildout | Customer demand, 45V uncertainty |
| Alberta Pathways | Pipeline, oil sands facilities → saline storage | ~10 Mt/yr | Pre-FID, political holding pattern | Federal/provincial policy alignment |
| Midwest (Summit) | Pipeline collecting ethanol CO₂ | ~8 Mt/yr originally | Rerouted May 2026, contested | Property rights, route certainty |

The honest read on this table: **of all the projects listed, only Northern Lights Phase 1 is actually operating**, and Northern Lights is a heavily subsidized demonstrator rather than a market-rate solution. The rest are in various states of construction, regulatory limbo, or political restructuring. The 2025–2027 period will be when the others either come online (or don't), and when we'll learn whether the IRA/OBBBA-era CCS push translates to physical infrastructure.

## How a CCS project actually gets financed

To see *why* most of that table is stuck pre-FID or on government life support, you have to look at how a CCS project assembles its revenue — because the problem is the same one the non-Chinese graphite plants faced in Chapter 2: a high-capital-cost asset that cannot reach a final investment decision (FID) without a *contracted, bankable revenue floor*. A capture plant and its storage well are billion-dollar commitments with decades of operating life — the same irreversible-capital-under-demand-uncertainty bet as the steel reline in Chapter 2 — and a lender will not fund them against a hoped-for spot price.

A CCS project has up to three revenue streams, and the financing turns on how bankable each one is:

1. **The 45Q tax credit** — $85/t for point-source storage, $180/t for DAC, paid for **12 years** after start-up. But a tax credit is only worth its face value to someone with enough tax liability to absorb it, and most project developers (or the single-purpose entities that own the asset) don't have it. The IRA's decisive move was to make 45Q **transferable** — the developer can *sell* the credit for cash to a third party with tax appetite — and available as **direct pay** for some entities. That is what turned 45Q from a tax attribute into something a lender can underwrite against. Two features still haunt it: the credit runs **12 years while the storage liability runs decades**, and it carries **recapture risk** — if the stored CO₂ leaks back out within the recapture window, the IRS can claw the credit back, which lenders price as a hazard.
2. **A carbon price or compliance value** — the EU ETS for European emitters, a voluntary-market buyer elsewhere. But as Northern Lights shows, an ETS price around €75/t doesn't cover a ~$150–300/t all-in CCS cost, so this rarely closes the gap on its own.
3. **The molecule's own value** — EOR payments or a merchant CO₂ sale (Part 4). This is exactly why OBBBA's parity provision matters so much: by raising EOR's 45Q value to full parity, it lets a project stack EOR revenue *on top of* the $85 credit — often the increment that finally tips a project to FID, and the reason the destination tilts toward oil.

For the cheap-to-capture sources (gas processing, ammonia, ethanol) near existing pipelines, stacking 45Q + EOR can pencil — which is why the Gulf/Permian projects are the ones moving. For the dilute, expensive sources that matter most for climate (cement, steel, power), none of the three streams is bankable at today's prices. So those projects only happen where a government *manufactures the missing revenue floor*: Norway's **Longship** program covering ~80% of Northern Lights, the UK's **CCS contracts-for-difference** (the state pays the difference between a fixed strike price and the prevailing ETS), the EU **Innovation Fund**. This is the identical pattern to the graphite bankability problem in Chapter 2 — *policy manufacturing a price floor so private capital will finance the build-out* — and you will meet it a third time in CDR procurement (Ch. 11) and a fourth in SAF mandates (Ch. 12, Appendix A). Hold the pattern; it is one of the load-bearing ideas of this book. For the dilute-capture projects to follow without subsidy, either the cost curve bends or the floor stays.

## **Stop-and-check 3.C**

1. Why is the Gulf Coast a structurally favored CCS region compared to, say, the Midwest? List three reasons that aren't just "more emissions."
2. Northern Lights is heavily subsidized (~80% of Phase 1 cost paid by Norwegian government). Does this make it a successful demonstration of CCS, or a successful demonstration of *subsidized* CCS? What's the difference, and why does it matter?
3. Summit pivoted from "climate solution" framing to "energy dominance" framing in 2025. Was this just opportunistic marketing, or does it reflect a real change in what the project will do? (Hint: think about what 45Q parity for EOR actually means for Summit's business.)
4. **Socratic prompt:** If you were a policymaker trying to maximize the climate benefit of US CCS deployment in 2026–2030, where would you focus federal support? Defend a specific allocation across (a) gas processing / ammonia retrofits, (b) cement and steel point sources, (c) ethanol corridor capture, (d) DAC, (e) midstream infrastructure (pipelines and storage hubs). What's your reasoning?

**Answers**

1. Gulf Coast structural advantages (beyond raw emissions volume): (1) Existing 5,000-mile CO₂ pipeline network and EOR infrastructure — marginal cost of connecting new sources to storage is low; (2) Deep saline aquifer storage capacity, well-characterized from decades of oil and gas subsurface work; (3) Deepwater and offshore storage potential — the Gulf of Mexico offers enormous storage capacity without onshore permitting complications; (4) Industrial port access enabling CO₂ export or import for cross-border CCS.

2. Northern Lights demonstrates *technical* and *operational* viability at 1.5 Mt/yr. The 80% subsidy tells you it doesn't work at current market prices — the $150–300/tCO₂ all-in cost isn't justified by EU ETS prices of €75/tCO₂e plus any voluntary market revenue. The difference matters for policy conclusions: it suggests CCS infrastructure requires government investment at initial scale (like other infrastructure, not unlike roads), not that the technology is mature enough to be self-sustaining. The useful question is whether the next generation of projects can achieve 40–50% subsidy, and then 20%, as costs decline.

3. Summit's framing shift reflects a real business shift. OBBBA equalized 45Q values for EOR and dedicated storage at $85/tCO₂. That means Summit can route CO₂ to EOR operators and earn the same credit as dedicated storage — while receiving EOR operator payments on top of 45Q. The business case has actually improved, but the climate case is weaker because EOR CO₂ helps produce more oil. The framing change isn't just political opportunism; it accurately reflects that the project's economics now partially depend on oil production.

4. The climate-optimal allocation: heaviest weight on (e) midstream infrastructure, because it's the rate-limiting constraint for all CCS types — without hubs, no individual source can connect to storage economically. Second priority: (b) cement and steel, because these face no cost-competitive renewable alternative and CBAM creates urgency for EU-facing producers. Third: (c) ethanol corridor, as CO₂ is already separated and Midwest hub density provides future optionality. Lower priority for (a) gas processing, where additionality of federal support is lower because capture often occurs anyway. Minimal marginal federal dollars to (d) DAC, which already receives $180/tCO₂ under 45Q and has concentrated corporate demand.

---

# Part 4: The merchant CO₂ market — the part nobody in climate talks about

We've spent most of this chapter on the climate-motivated CO₂ value chain. But there's a much older, much more mature CO₂ economy that climate people generally don't know exists: **the merchant CO₂ market**.

## What it is

Merchant CO₂ is industrial-grade CO₂ sold as a commodity for productive uses. The market is approximately **$13 billion globally in 2024**, projected to grow to ~$21 billion by 2029, moving on the order of **~230 Mt of CO₂ per year** worldwide — a throughput that, by raw volume, dwarfs both US CO₂-EOR (~70 Mt/yr) and global geological storage (~50 Mt/yr). Hold that comparison lightly, though: as Stop-and-check 3.D presses, almost none of this CO₂ is *stored* — it is used and re-released — so the volume measures market size, not climate mitigation. Industrial gas companies (the same firms that sell oxygen and nitrogen) source CO₂ from byproduct streams at industrial plants, purify it to food/beverage/industrial spec, liquefy it, and distribute it to thousands of end customers.

Three companies — **Air Liquide, Linde, Air Products** — collectively hold ~82% of the global merchant CO₂ market. Below them are regional players: Messer, Nippon Sanso (Taiyo Nippon), Yara (large CO₂ producer in Europe via ammonia), Praxair (now part of Linde), Gulf Cryo, BOC, and many smaller distributors.

## Where the CO₂ comes from

For merchant CO₂, the source matters because of purity requirements. The economically attractive sources are:

- **Ammonia plants** — Largest single source globally. Ammonia synthesis produces CO₂ as a near-pure stream from the SMR/shift section. Most large ammonia plants in the US, Trinidad, Saudi Arabia, Russia, and elsewhere have CO₂-recovery units selling to industrial gas companies.
- **Ethanol fermentation** — Major US merchant CO₂ source, especially in the Midwest. The 2022 US merchant CO₂ shortage was driven partly by ethanol plant maintenance turnarounds reducing CO₂ supply.
- **Hydrogen production** — Increasingly relevant as the hydrogen economy scales; SMR hydrogen plants are major CO₂ co-producers.
- **Natural gas processing** — Where the gas stream has high CO₂ content, the separated CO₂ can be sold.
- **Captured CO₂ from CCS** — A new and growing source; Linde's Freeport, Texas plant captures CO₂ from MEGlobal's ethylene glycol facility and sells it as merchant CO₂ with ISCC PLUS sustainability certification.

## Where the CO₂ goes

End uses are diverse but concentrated:

- **Food and beverage carbonation** (~25–30% of merchant volume, the single largest application): Beer, soda, carbonated water. Beverages are the visible end use that everyone has interacted with.
- **Food preservation and processing**: Modified-atmosphere packaging (MAP) of meat, dairy, and produce extends shelf life. CO₂ is used to chill and freeze (dry ice, snow). Coffee decaffeination uses supercritical CO₂ as a solvent.
- **Welding shield gas**: CO₂ or CO₂-blend shield gases protect arc welding from atmospheric oxygen contamination. Industrial application.
- **Greenhouse CO₂ enrichment**: Greenhouses (especially Dutch tomato and cucumber operations) inject CO₂ to accelerate plant growth, often using captured CO₂ from local cogeneration or ethanol plants. A surprisingly large application — single Dutch greenhouses consume hundreds of tons per year.
- **Water treatment** (pH adjustment for municipal and industrial water): Replaces sulfuric acid in many applications.
- **EOR** (the giant one in the US): ~70 Mt/yr in the US alone. Mostly supplied by pipeline from natural CO₂ domes and a few large anthropogenic sources, not by the industrial-gas merchant system.
- **Firefighting**: CO₂-based extinguishers for specific fire classes (electrical, flammable liquid).
- **Other industrial**: Pulp and paper, casting and foundry, chemicals manufacturing, supercritical fluid extraction.

## The 2022 shortage and structural fragility

In summer 2022, the US experienced a significant **merchant CO₂ shortage**. The cause was a confluence: maintenance turnarounds at major ammonia and ethanol plants, plus a contamination event at the Jackson Dome (Mississippi) natural CO₂ source. Beverage producers, breweries, dry-ice suppliers, and food packagers experienced supply disruptions. Some breweries reportedly had to cut production.

This event exposed something structural: **the US merchant CO₂ market is highly dependent on a small number of large sources, with limited geographic diversification.** When one or two go offline simultaneously, the whole system tightens. The fragility was unfamiliar to most beverage and food companies, who had treated CO₂ as a reliable utility commodity.

Lessons from 2022:
- **CO₂ supply contracts now matter strategically** to anyone who consumes serious volumes. Several major beverage companies have signed long-term offtake agreements with new CO₂ sources, including some from CCS projects.
- **Some breweries have invested in fermentation CO₂ recovery on-site**, capturing the CO₂ they produce themselves rather than buying it from the merchant market. This is a small but growing trend.
- **The merchant CO₂ market is now a meaningful potential buyer for CCS-captured CO₂** — particularly for projects in the right location and with the right purity. This is one of the convergence points between the merchant value chain and the climate-CCS value chain.

## The convergence

The legacy merchant CO₂ market and the new climate-CCS value chain are *colliding* in ways most market participants didn't anticipate three years ago:

- **Merchant-grade CCS supply.** CCS projects that produce food-grade pure CO₂ (e.g., Linde's Freeport facility, ethanol-corridor capture projects with appropriate purification) can sell to the merchant market for $80–150/ton — comparable to or higher than the $85/ton 45Q credit. Some projects can stack revenues: claim 45Q for sequestration *or* sell as merchant CO₂. (You can't do both for the same molecule under current rules, but project economics may favor one or the other depending on local market.)
- **DAC for premium markets.** Direct air capture produces extremely pure CO₂ that can command premium prices in specialty industrial markets (semiconductor processing, supercritical CO₂ extraction, niche food applications). 1PointFive has signaled interest in DAC CO₂ sales as a near-term revenue source while the storage-credit market matures.
- **CO₂-to-products.** Several companies are using merchant-grade CO₂ as feedstock for chemicals, polymers, e-fuels, and building materials, with the climate value depending on whether the source CO₂ is biogenic, atmospheric (DAC), or fossil. We'll come back to this in Part 5.

The honest framing: **the merchant CO₂ market is the most mature destination for captured CO₂ that exists, and it's drawing in CCS supply as the latter becomes available.** Whether that's a climate-positive use or just shuffling CO₂ atoms around for industrial purposes depends on the whole-system accounting, and the accounting frameworks are still catching up.

## **Stop-and-check 3.D**

1. The merchant CO₂ market moves ~230 Mt/yr — far more than EOR or geological storage by volume. Why is volume a misleading way to think about its climate relevance?
2. The 2022 US shortage showed merchant supply leans on a handful of large ammonia and ethanol sources. As those sources add CCS capture, does that make the merchant market *more* or *less* fragile?
3. A brewery buys captured CO₂ from a CCS project to carbonate its beer. Is that "carbon storage"? Trace the molecule.
4. **Socratic prompt:** A project sells its captured CO₂ to a brewery instead of storing it, but still wants to claim a climate benefit. What's the honest accounting — and who, if anyone, gets to claim the "avoided" or "removed" ton?

**Answers**

1. Because almost none of merchant CO₂ is *stored* — it is used and then re-released. The CO₂ in a soda is vented the moment you open and drink it; welding gas, greenhouse enrichment, and dry ice nearly all return to the atmosphere within days to months. So 230 Mt/yr of throughput is a *flow*, not a sink. Its climate relevance isn't the volume it moves but (a) where the CO₂ originates (fossil byproduct vs. biogenic vs. atmospheric) and (b) whether using captured CO₂ displaces a fossil-sourced molecule. Volume measures the size of the market, not the size of any mitigation.

2. It cuts both ways, but the net is probably *more* resilient. Adding capture and purification at the big ammonia and ethanol sources gives them a second revenue stream (45Q or merchant sales) that makes the recovery unit worth running and maintaining rather than venting — which stabilizes supply — and the CCS push is bringing new purified sources online (Linde's Freeport plant, ethanol-corridor projects). But the concentration risk remains: if supply is still anchored to a few mega-sources, a coincident outage still tightens the market. What reduces fragility is geographic diversification, not capture per se.

3. No — it is the opposite of storage. Trace it: the project captures a ton that would otherwise be vented or stored, sells it to the brewery, the brewery dissolves it in beer, and within weeks a customer opens the can and the CO₂ returns to the atmosphere. The net atmospheric effect is roughly zero relative to venting (you delayed the release by the supply-chain time) and *worse* than storage (which would have kept it underground). The only climate case is a *substitution* one — if this CO₂ displaces CO₂ the brewery would otherwise have bought from a fossil source, you have avoided that fossil molecule. But you have not removed or stored anything. Merchant use is not sequestration.

4. The honest accounting splits the molecule's journey into *capture* and *fate*, and only the fate determines the climate claim. Selling to a brewery is a use, not storage, so no removal or durable-storage credit is warranted; at most there is an *avoided*-emissions claim, and only if the captured CO₂ genuinely displaces a fossil-sourced merchant molecule. Even then, that avoided ton belongs to whoever's emissions would otherwise have risen (the displaced fossil supplier's customer), not to the CCS project, which merely changed where its own molecule went. The trap is double-counting: the project can't book a storage benefit (there is none) and the buyer can't book a removal. This is exactly the avoided/reduced/removed discipline of Ch. 5 applied to one molecule — and it's why 45Q pays for *storage*, not for a merchant sale.

---

# Part 5: CO₂ as feedstock — turning the molecule into products

The frontier of the CO₂ molecule value chain is converting CO₂ into something *other than* storage, EOR, or merchant gas. This is "CCU" — Carbon Capture and *Utilization* — distinguished from CCS (storage) by what happens to the captured CO₂.

The thermodynamics are unkind. CO₂ is a low-energy molecule; turning it back into anything useful (fuels, chemicals, materials) requires substantial energy input, typically from electricity or hydrogen. The carbon footprint of the product depends entirely on whether that input energy is itself low-carbon. CCU with fossil-electricity input is climatically worse than not doing it. CCU with renewable-electricity or green-hydrogen input *might* be climate-positive depending on the alternatives.

The categories of CCU, ranked by current scale:

## Mineralization (concrete and aggregates)

The most mature CCU application, scaling fastest. CO₂ is reacted with calcium-containing materials to form calcium carbonate (CaCO₃), which is a stable solid that locks the CO₂ in mineral form essentially indefinitely.

Two business models exist:

- **CO₂-cured concrete** (CarbonCure). Inject CO₂ into wet concrete during mixing; the CO₂ reacts with calcium hydroxide in the cement paste to form calcium carbonate inside the concrete matrix. Modest CO₂ utilization per ton of concrete (~10–20 kg CO₂/m³) but applied at concrete-industry scale, which is enormous. CarbonCure is in thousands of concrete plants globally.
- **Mineralized aggregates** (Solidia, Heirloom-Carbonbuilt partnerships, Mineral Carbonation International). Use CO₂ to mineralize industrial wastes (steel slag, mining tailings, fly ash) or natural materials (peridotite, basalt) into building aggregate or supplementary cementitious materials. Higher CO₂ uptake per ton of product (50–200+ kg CO₂/ton), niche commercial-scale today.

Mineralization is permanent (>1000-year storage) and counts as both CCU and CCS in most frameworks. It scales bounded by the construction industry's appetite for these materials.

## E-fuels and methanol

Combining CO₂ with hydrogen produces methanol (CH₃OH), which can then be upgraded to gasoline, jet, or diesel via established processes (Fischer-Tropsch, methanol-to-olefins, methanol-to-gasoline). The whole pathway requires substantial hydrogen input — about 0.19 tons of H₂ per ton of methanol (CO₂ + 3H₂ → CH₃OH + H₂O), which at current electrolyzer efficiency takes on the order of 10–11 MWh of electricity per ton of methanol.

E-fuels are climatically meaningful only if the hydrogen is green (renewable-powered electrolysis) and the CO₂ is biogenic or atmospheric (not fossil). Even with both inputs green, e-fuels are typically 3–10× the cost of fossil-fuel alternatives. Their realistic near-term market is sustainable aviation fuel (SAF) and shipping fuel, where electrification isn't viable.

Major players: HIF Global (Chile, Texas), Infinium (US), Sunfire (Germany), Twelve (US — focused on chemicals rather than fuels but similar technology).

## Polymers and chemicals

CO₂ can be used as a feedstock for polyols (used in polyurethane foams), polycarbonates, and various organic chemicals. Covestro and Econic have commercial polyurethane products with ~20% CO₂ feedstock content. Aramco/Saudi Basic has CO₂-based polyols. Twelve (US) makes various petrochemical molecules from CO₂.

The CO₂-feedstock chemicals market is small (a few hundred kt/yr globally) but high-value and growing. The climate value depends on counterfactuals — if the alternative feedstock is petroleum, CO₂ substitution displaces some fossil carbon.

## Carbon-to-products (the speculative frontier)

The longer reach: producing synthetic graphite from CO₂ (early R&D), carbon black from CO₂ (early commercial — see methane pyrolysis in Ch. 2), even diamond from CO₂ (academic only). These are the most exotic applications but, if they work, link the climate-CO₂ value chain back to the commodity-carbon markets of Chapter 2 in a way that closes the loop.

LanzaTech (NASDAQ: LNZA after 2023 SPAC IPO) is the most-developed player using CO₂ and CO from industrial off-gases as fermentation feedstock for ethanol and chemicals. Its commercial operations are mostly steel-mill off-gas based rather than pure CO₂, but it's the closest thing to scaled biological CO₂ utilization.

## The honest assessment

Of total global CO₂ emissions (~38 GtCO₂/yr), the total *theoretical* market for CCU at all current and reasonably-projected applications is somewhere in the range of **0.5–2 Gt/yr by 2050** — i.e., a few percent of emissions. CCU is not a primary climate solution. It's a secondary contributor that helps decarbonize specific products (aviation fuel, chemicals, concrete) where direct electrification or alternatives don't work.

The reason climate people sometimes oversell CCU is that it sounds attractive — "turn the problem into the solution!" — but the thermodynamics and the scale don't match the rhetoric. *Most* captured CO₂ is going to need to go into geological storage for permanent isolation. CCU helps at the margin in specific applications. It does not replace the need for CCS.

## **Stop-and-check 3.E**

1. CCU products range from mineralized concrete (locks CO₂ for >1,000 years) to e-fuels (re-released on combustion within weeks). Why does that durability spread make "CCU" almost useless as a single category for climate accounting?
2. Turning CO₂ back into a fuel or chemical costs energy. Under what condition is CCU climate-positive, and under what condition is it climate-*negative*?
3. E-fuels cost 3–10× fossil fuels even with green inputs. Why might they be the right answer for aviation and shipping but the wrong answer for ground transport?
4. **Socratic prompt:** Should CCU earn carbon-removal credits? Make the case that mineralized concrete should and e-fuels shouldn't — then name the exact variable that separates them.

**Answers**

1. Because the climate value of "using" CO₂ depends entirely on how long the carbon stays out of the atmosphere, and CCU products span the whole permanence spectrum. Mineralization (CaCO₃ in concrete or aggregate) is geologically stable — effectively permanent, indistinguishable in outcome from CCS. An e-fuel re-releases its CO₂ the instant it's burned, days to months later — not storage at all, only (possibly) a fossil-fuel substitution. Lumping these under one acronym invites the error of treating an e-fuel as if it sequesters carbon. For accounting you must ask the durability question (Ch. 11's permanence tiers) of each *product*, never of "CCU" as a class.

2. CCU is climate-positive only when (a) the energy input — electricity or hydrogen — is genuinely low-carbon, and (b) the product displaces a more carbon-intensive incumbent (and, for any *storage* claim, the carbon stays locked up). Because CO₂ is a low-energy molecule, converting it always costs energy; if that energy is fossil-fired, the conversion releases more CO₂ than it consumes and CCU is climate-*negative* — you'd have done better not to bother. The decisive variable is the carbon intensity of the energy, which is why a CCU claim is only ever as clean as the grid or hydrogen behind it.

3. Aviation and shipping have no near-term electrification path — batteries are too heavy for long-haul flight and ships need energy-dense liquid fuel — so a drop-in e-fuel (or SAF) may be the *only* decarbonization option, and a 3–10× premium is tolerable on a small slice of total energy. Ground transport has a cheaper, more efficient alternative: direct electrification, which uses the clean electricity straight rather than eating the round-trip losses of electricity → hydrogen → e-fuel → combustion. Spending scarce green electrons on e-fuels for cars when a battery would do is thermodynamically wasteful. Match the expensive molecule to the use that has no substitute.

4. Mineralized concrete should: the carbon is fixed as a stable carbonate for >1,000 years, so if the source CO₂ is atmospheric or biogenic it's a genuine removal with durable storage — the same outcome as CCS. E-fuels shouldn't: the carbon is re-released on combustion within weeks, so there is no storage and at most an avoided-emissions (substitution) claim, not a removal. The variable that separates them is **durability/permanence** — how long the carbon is isolated from the atmosphere — which is exactly the axis Ch. 11 uses to tier removals. A credit system blind to durability would pay the same for both and reward the one that does nothing for the atmosphere.

## **Stop-and-check 3.F (whole chapter)**

1. The CO₂ molecule value chain has four primary destinations: storage, EOR, merchant sale, and product conversion. Rank these by current scale (Mt/yr). Now rank them by expected scale in 2040. What changes between the rankings?
2. A captured CO₂ molecule going to storage earns $85/ton 45Q (post-OBBBA). A captured CO₂ molecule sold to the merchant market earns ~$80–150/ton at current prices. Why would any project pursue storage rather than sale? What's the project-economic difference?
3. The 2022 US merchant CO₂ shortage exposed structural fragility in a market most climate analysts didn't know existed. What does this say about how well-integrated the "carbon as molecule" framing is into climate analysis?
4. **Socratic prompt:** Imagine you're CEO of a major industrial gas company in 2026. The merchant CO₂ market is your bread and butter. CCS projects are starting to come online that will produce CO₂ at competitive prices to your existing supply chain. Are these new sources a threat (eating your margins) or an opportunity (expanding the market) — and how should you respond strategically?

**Answers**

1. By current scale (global, by volume): Merchant CO₂ (~230 Mt/yr) > EOR (~70 Mt/yr, mostly US) > Geological storage (~50 Mt/yr) ≫ Product conversion (<10 Mt/yr, mostly niche). But note the scale ranking inverts the *mitigation* ranking — most merchant CO₂ and all EOR-extracted oil re-enter the atmosphere, while only geological storage (and durable mineralization within product conversion) actually isolates carbon. By 2040 expected scale: Geological storage likely dominates (IEA NZE: 1,000+ Mt/yr by 2030, 6,000 Mt/yr by 2050); Merchant CO₂ grows only moderately (food/industrial demand is slow-growing); EOR potentially constrained by the oil transition; Product conversion grows if e-fuels and mineralization scale. The key change between rankings: storage goes from smallest to largest, because it's the only destination policy is actively trying to scale for climate reasons.

2. A captured CO₂ molecule going to storage earns $85/ton 45Q (OBBBA parity). A molecule sold to merchant market earns $80–150/ton at current prices — comparable to 45Q on revenue. The project-economic difference: merchant sales require co-location with purification, liquefaction, and distribution infrastructure, plus ongoing buyer relationships. Storage requires long-term geological liability management and Class VI well permitting, which is slow and costly. The merchant sale earns similar revenue without the liability burden, which is why companies with merchant market access often prefer it. But merchant market volume is limited (~230 Mt/yr globally); once that's supplied, additional captured CO₂ must go to storage.

3. The merchant CO₂ market's near-total invisibility in climate analysis reflects the broader problem: "carbon" in climate discourse means CO₂ as an emission or as a policy abstraction, while CO₂ as an industrial molecule with a mature value chain is treated as a separate subject entirely. The 2022 US shortage (triggered by disruptions at ammonia plants that were the main CO₂ source) harmed food-and-beverage supply chains and hospitals — systems that most climate analysts had no awareness were CO₂-dependent. Better integration of "CO₂ as molecule" and "CO₂ as emission" framing is an analytical gap with real-world consequences.

4. CCS-derived CO₂ is both threat and opportunity. Threat: new large-volume, low-cost point-source CO₂ could undercut existing supply margins if it enters the merchant market. Opportunity: (1) You can acquire or contract CCS-source CO₂ as cheaper feedstock, reducing your production costs; (2) As the industrial gas company with purification, liquefaction, and distribution infrastructure, you're the logical operator for merchant CO₂ from CCS projects — positioning yourself as the midstream intermediary. The strategic response: partner with or acquire CCS project operators to integrate CCS-sourced CO₂ into your existing network; don't fight the new supply, own it.

---

# Closing exercise

Three things to take away:

**1. The molecule value chain is older and bigger than climate people realize.** The US has had 5,000 miles of CO₂ pipeline and a 70 Mt/yr EOR industry for decades. The global merchant CO₂ market is $13 billion. None of this was originally about climate. The CCS push of 2022 onward is building *on top of* this existing infrastructure and politics, not from scratch. Understanding the legacy is essential to understanding the dynamics.

**2. Storage vs. EOR vs. utilization is now a single policy choice.** OBBBA's July 2025 parity provision made EOR and sequestration earn the same 45Q credit. From a project-economic perspective, that means CCS developers can route CO₂ wherever's most economically attractive — and EOR will often win on the basis of nearby pipeline and existing infrastructure. Whether that's a good climate policy is contested. Summit's 2025–2026 pivot from "climate" framing to "energy dominance" framing is in part a response to this policy change.

**3. The next 24 months are decisive.** Northern Lights Phase 2 (FID March 2025, online 2028), Porthos first injection (~H2 2027, slipped from 2026), Acorn first injection (~2027), Pathways FID decision, Summit reroute approval, Baytown CCS without hydrogen, PHMSA final rule — all of these will resolve in the 2025–2028 window. By the end of 2027 we'll know whether the CCS hub model is becoming reality at meaningful scale or whether it's stuck in permitting-and-financing limbo. The current snapshot (May 2026) is genuinely an in-between moment.

---

# What this chapter simplified

**1. The cost-of-capture stack is more nuanced than presented.** I gave you $/tCO₂ ranges by source type. In reality, capture cost depends on plant size, location, electricity prices, capture technology choice, and whether you're calculating LCOC (cost per ton captured) vs. LCOA (cost per ton avoided, which accounts for the parasitic energy of the capture system itself). For any specific project, the actual cost is project-specific.

**2. Pipeline phase behavior was treated lightly.** Supercritical CO₂ transport has rich engineering questions — what happens at the pseudo-critical point, how to manage two-phase regions during depressurization, what impurities (especially water — leads to carbonic acid corrosion — and hydrogen sulfide — accelerates stress corrosion cracking) do to pipeline integrity. Any actual pipeline engineer reading this chapter would find Part 2 superficial. That's intentional for a curriculum overview, but it's a real gap if you ever need to assess a specific pipeline project.

**3. The PHMSA NPRM is current as of May 2026 but the politics may have shifted.** What I described is the proposed rule as of January 2025. The Trump administration's PHMSA may modify, weaken, or shelve it. Check the docket (PHMSA-2022-0125) before relying on the current status.

**4. Capacity numbers for proposed hubs are operator-stated.** Northern Lights Phase 2's "5+ Mt/yr by 2028" is the company's number. Aramis's "up to 22 Mt/yr" is the project sponsor's number. In CCS especially, between project announcements, FID, and actual operation, capacity numbers tend to drift downward. The actually-delivered capacities of these projects in 2030 may be substantially below the announced figures.

**5. The merchant CO₂ market sizes I cited are mostly from market-research firms.** Like the Chapter 2 commodity numbers, these have the methodology-disagreement problem. The $13 billion figure is in the middle of the cited range; serious users should triangulate against industrial gas company financial reports.

---

# Glossary delta (Chapter 3)

- **45Q tax credit** — Section 45Q of the US Internal Revenue Code, providing a per-ton tax credit for CO₂ captured and either sequestered or used. Created 2008, expanded by FUTURE Act (2018) and Inflation Reduction Act (2022), modified by OBBBA (2025) to provide parity between sequestration and EOR. Current values: $85/tCO₂ for point-source sequestration, $180/tCO₂ for DAC sequestration, with EOR/utilization now matching post-OBBBA (was previously discounted). Paid for **12 years** after a facility starts up. The IRA made the credit **transferable** (sellable for cash to a third party with tax liability) and available as **direct pay** for some entities — the features that made 45Q financeable. Subject to **recapture** (see below).
- **Contract for difference (CfD, CCS)** — A subsidy mechanism in which the government pays a project the difference between a fixed strike price and the prevailing carbon price (e.g. the EU ETS), guaranteeing a revenue floor. Used by the UK to make CCS bankable; analogous to renewable-energy CfDs.
- **ACTL (Alberta Carbon Trunk Line)** — Operating Canadian CO₂ pipeline (~240 km), connecting a Nutrien fertilizer plant and Sturgeon refinery to Enhance Energy's EOR operations. ~1.6 Mt/yr capacity, operational since 2020.
- **Aramis** — Proposed Dutch CCS hub, targeting up to 22 Mt/yr long-term capacity. Partners include Shell, TotalEnergies, EBN, Gasunie. Pre-FID as of 2026.
- **Acorn** — UK Track-1 CCUS cluster in Scotland, approved October 2023. Repurposes existing North Sea gas infrastructure for CO₂ storage.
- **CCU (Carbon Capture and Utilization)** — Capturing CO₂ for use in products (fuels, chemicals, materials, mineralization) rather than permanent storage. Distinct from CCS.
- **CCUS** — Umbrella term covering both CCS (storage) and CCU (utilization).
- **CO₂-EOR (Enhanced Oil Recovery)** — Injection of CO₂ into oil reservoirs to mobilize remaining oil. ~70 Mt CO₂/yr injected in the US; the largest historical use of large-scale CO₂ infrastructure.
- **Class VI well** — US EPA-regulated well class specifically for permanent CO₂ storage. Distinct from Class II (EOR injection) and Class I (industrial waste). Class VI permitting has historically been slow at EPA; some states (LA, ND, WY) have obtained primacy to permit Class VI wells themselves.
- **Critical point (CO₂)** — The thermodynamic state above which CO₂ exists as a supercritical fluid: 31.1°C and 73.8 bar.
- **Denbury / Denbury Gulf Coast Pipelines** — Historically the largest US CO₂ pipeline network operator. Acquired by ExxonMobil in 2023 for $4.9 billion. Operator at the time of the 2020 Satartia rupture.
- **EOR (Enhanced Oil Recovery)** — General term for techniques to extract additional oil from a reservoir beyond primary and secondary recovery. CO₂-EOR is one approach; others use steam, polymers, or surfactants.
- **LCOA (Levelized Cost of CO₂ Avoided)** — Cost per ton of net CO₂ avoided by a capture project, accounting for the parasitic emissions associated with capture itself. Higher than LCOC.
- **LCOC (Levelized Cost of CO₂ Captured)** — Cost per ton of CO₂ captured by a project, before accounting for the parasitic emissions of the capture system.
- **Longship** — The Norwegian government's full-chain CCS program that funds ~80% of Northern Lights Phase 1. The archetypal government-as-revenue-floor CCS subsidy.
- **MMV (Measurement, Monitoring, and Verification)** — The framework for confirming permanent storage of injected CO₂. Class VI wells require detailed MMV plans for 50-year post-injection periods.
- **Northern Lights** — World's first open-access (third-party) CO₂ transport and storage facility, operational since August 2025. JV of Equinor, Shell, TotalEnergies. Phase 1: 1.5 Mt/yr; Phase 2: 5+ Mt/yr by 2028.
- **OBBBA (One Big Beautiful Bill Act, July 2025)** — US reconciliation legislation that, among other changes, established 45Q parity between sequestration and EOR/utilization (both now earn $85/tCO₂ for point source, $180/tCO₂ for DAC) and introduced Foreign Entity of Concern restrictions to 45Q.
- **Pathways Alliance** — Consortium of six Canadian oil sands operators proposing ~10 Mt/yr CCS for oil sands emissions. Pre-FID as of 2026.
- **Pipeline phase (CO₂)** — Refers to the thermodynamic state of CO₂ in transport: supercritical (above critical point), liquid (below critical, high pressure), or gas (low pressure). Different phases have different operating, safety, and rupture-behavior characteristics.
- **PHMSA (Pipeline and Hazardous Materials Safety Administration)** — US Department of Transportation agency responsible for regulating pipeline safety. Issued the January 2025 NPRM updating CO₂ pipeline safety regulations.
- **Porthos** — Dutch CCS hub project, Rotterdam-area industrial sources storing in depleted North Sea gas reservoirs. ~2.5 Mt/yr, first injection now expected second half 2027 (slipped from original 2026 target).
- **Recapture (45Q)** — IRS provision allowing the 45Q credit to be clawed back if stored CO₂ leaks out within a defined recapture window. Priced by lenders as a project risk because the storage liability outlasts the 12-year credit period.
- **Saline aquifer / saline formation** — Deep underground geological formation containing saltwater, suitable for CO₂ storage. Large potential storage capacity globally; the favored target for most large-scale CCS projects.
- **Satartia, Mississippi (Feb 22, 2020)** — Town near the rupture of a Denbury CO₂ pipeline. >45 hospitalizations; no fatalities. The defining CO₂ pipeline safety incident in US history; basis for PHMSA's January 2025 NPRM.
- **Shute Creek / LaBarge** — ExxonMobil's gas processing facility in Wyoming, the largest single anthropogenic CO₂ source for EOR in the world (~7 Mt/yr captured).
- **Summit Carbon Solutions** — Largest proposed Midwest CO₂ pipeline project, originally a ~2,000 mile, 5-state network collecting ethanol fermentation CO₂ for North Dakota storage. Substantially restructured in 2025–2026 due to property-rights opposition.
- **Supercritical CO₂** — CO₂ above its critical point (31.1°C, 73.8 bar). Dense, single-phase fluid; the typical state for long-distance pipeline transport.

---

# Sources and currency

This chapter cites figures that are current as of writing (May 2026) and will move. The following are the most time-sensitive claims; each should be re-verified against the primary source before being relied upon, and updates tracked via `CHANGELOG.md`:

| Claim | Value as stated | As-of | Primary source to verify against |
|---|---|---|---|
| 45Q point-source sequestration credit | $85/tCO₂ | July 4, 2025 (OBBBA enactment) | IRC §45Q as amended by OBBBA (P.L. 119-21); Jackson Walker law-firm alert |
| 45Q DAC sequestration credit | $180/tCO₂ | July 4, 2025 (OBBBA enactment) | IRC §45Q as amended by OBBBA (P.L. 119-21) |
| OBBBA EOR–sequestration parity (EOR raised from $60 → $85 point-source; $130 → $180 DAC) | EOR now at parity with sequestration | July 4, 2025 | IRC §45Q as amended; Payne Institute analysis; Pipeline Fighters Hub |
| Northern Lights Phase 1 operational | First injection August 25, 2025 | Aug 25, 2025 | Equinor press release; TotalEnergies press release; norlights.com |
| Northern Lights Phase 1 capacity | 1.5 Mt/yr, fully booked | Aug 2025 | Equinor / norlights.com |
| Northern Lights Phase 2 FID | March 27, 2025 | Mar 27, 2025 | Equinor press release 20250327 |
| Northern Lights Phase 2 investment | NOK 7.5 billion (~$700M) | Mar 27, 2025 | Equinor press release 20250327; Rigzone |
| Northern Lights Phase 2 capacity / timeline | ≥5 Mt/yr by H2 2028 | Mar 27, 2025 | Equinor press release 20250327 |
| ExxonMobil Baytown blue-hydrogen project paused | November 2025 | Nov 2025 | PGJ Online; H2 View; Canary Media; Enverus |
| Summit Carbon reroute announced | May 13–15, 2026 | May 2026 | summitcarbonsolutions.com; North Dakota Monitor; Agriculture of America |
| Summit route change: Iowa → Nebraska → Wyoming; ~200 miles shorter; ~400 landowners removed | May 2026 | May 2026 | summitcarbonsolutions.com; DakotaFreePress |
| South Dakota HB 1052 (eminent domain ban for CO₂ pipelines) | Signed March 6, 2025 | Mar 6, 2025 | SD Legislature; SDPB; Pipeline Fighters Hub |
| North Dakota judge voids Summit CO₂ storage permit | Second ruling March 10, 2026 (first ruling Dec 2025) | Mar 10, 2026 | North Dakota Monitor; Ethanol Producer Magazine |
| PHMSA NPRM on CO₂ pipeline safety | Issued Jan 10, 2025; Federal Register pub. Jan 15, 2025; unfinalized as of May 2026 | Jan 2025 | PHMSA docket PHMSA-2022-0125 at regulations.gov; DOT press release |
| Global merchant CO₂ market size | ~$13B (2024) → ~$21B (2029) | 2024/2029 projection | Business Research Company / GlobeNewswire (Nov 2025); triangulate against industrial gas company reports |
| Top-three merchant CO₂ market share (Air Liquide, Linde, Air Products) | ~82% (81.89% in 2023 data) | 2023 (latest available) | Business Research Company / GlobeNewswire (Nov 2025) |
| US CO₂ pipeline mileage | ~5,000 miles | circa 2024 | PHMSA pipeline mileage reports; IEA |
| US CO₂-EOR volume | ~70 Mt/yr | circa 2023–24 | EIA / NETL CO₂-EOR studies |
| Global merchant CO₂ volume (answer-key anchor) | ~230 Mt/yr | circa 2024 | Market-research consensus; triangulate against industrial-gas company disclosures — this figure appears only in answer keys; add to Part 4 body if confirmed |
| Shute Creek / LaBarge CO₂ capture rate | ~7 Mt/yr | circa 2022–24 | IEEFA; MIT Sequestration database; EPA Subpart RR reporting |
| ExxonMobil / Denbury acquisition price | $4.9 billion | Nov 2023 (close) | ExxonMobil press release July 13, 2023; SEC Form 8-K |
| Porthos first injection | H2 2027 (slipped from original 2026) | Apr 2026 | VEMW (Dutch industry association); porthosco2.nl |
| Acorn (UK) first injection | ~2027 | Oct 2023 approval | DESNZ Track-1 cluster sequencing decision |
| Aramis long-term capacity / status | Up to 22 Mt/yr; pre-FID | 2026 | Port of Rotterdam; Shell CCS Globe; Gasunie |
| Alberta Pathways capacity / cost | ~10 Mt/yr; ~$16B | 2024 | Pathways Alliance press materials; Canadian government filings |

> **OBBBA date note:** Line 216 of this chapter previously stated "November 2025" as the date OBBBA enacted 45Q parity — this was a drafting error. OBBBA (P.L. 119-21) was signed July 4, 2025. The November 2025 date has been corrected to "July 4, 2025" in the Summit timeline. The Closing section (line ~382) correctly states "OBBBA's July 2025 parity provision" and the Glossary delta correctly states "OBBBA (One Big Beautiful Bill Act, July 2025)" — these are consistent and correct.

> **Porthos delay note:** Porthos first injection has slipped from the original end-2026 target to second half 2027, confirmed by VEMW (April 2026). All four occurrences in this chapter (body, hub comparison table, Closing section, Glossary delta) have been updated.

> **North Dakota permit timeline note:** The chapter's Summit timeline entry "2025. A North Dakota judge revokes Summit's underground storage permit" captures the first ruling (Dec 2025, constitutional invalidity finding) but not the second ruling (March 10, 2026, permit formally voided). The entry is technically accurate as written but incomplete; the body text at line ~214 may warrant a date refinement to "Dec 2025–Mar 2026" for precision.

> **Answer-key contradiction note (resolved May 2026):** The whole-chapter Stop-and-check Answer 1 previously ranked "EOR (~70 Mt/yr US) ≥ Merchant CO₂ (~230 Mt/yr globally, dwarfing EOR by volume)," which was self-contradictory. Fixed in the depth pass: the ranking now reads Merchant CO₂ (~230 Mt/yr) > EOR (~70 Mt/yr) > Geological storage (~50 Mt/yr) ≫ Product conversion, with an explicit note that the *scale* ranking inverts the *mitigation* ranking. The ~230 Mt/yr merchant figure has also been added to the Part 4 body (previously it appeared only in answer keys). The figure remains market-research-derived; triangulate against industrial-gas company disclosures before relying on it.

---

# What's next

You've now seen the full physical foundation: how the carbon problem arises (Ch. 1), the commodity-carbon-materials economy that runs parallel to the climate story (Ch. 2), and the CO₂-molecule infrastructure that bridges them (Ch. 3). With these three chapters, you have the entire physical picture.

The natural next move is **Chapter 4 (Fossil Fuels)**, which closes out the physical-foundation track by treating the carbon stock we're currently mobilizing — coal, oil, gas — as its own value chain with its own dynamics. After that, the curriculum bridges into **Chapter 5 (Emissions Accounting)**, which is the rosetta stone for everything in Tracks B and C.

Or you can skip directly into the markets — Chapter 5 then 7 (compliance markets) or 8 (voluntary markets) — and we'll cover fossil fuels later when needed. Your call.

