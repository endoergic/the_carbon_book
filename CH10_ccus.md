# Chapter 10 — Carbon Capture, Utilization, and Storage (CCUS)

**Track:** Foundations & Physical Carbon (A) extended into the policy/technology forward view.
**Prerequisites:** Chapter 3 (CO₂ molecule value chain — pipelines, hubs, the merchant CO₂ market). Helpful: Chapter 4 (fossil fuel context), Chapter 8 (CDR purchases via voluntary credits).
**What you should be able to do by the end:**
- Identify the four core technology categories: **post-combustion**, **pre-combustion**, **oxy-fuel combustion**, and **direct capture** (covered more deeply in Ch. 11), and the contexts each is best suited for.
- Walk through a CCUS project value chain: capture → compression → transport → injection → monitoring → verification.
- State current global operational CCUS capacity (~50 Mt/yr in 2025), the project pipeline (~430 Mt/yr by 2030 if all announced projects come online), and the gap to NZE pathway requirements (~1,000–1,300 Mt/yr needed by 2030; ~6,000 Mt/yr by 2050).
- Identify the major operational CCUS projects: Petrobras Santos Basin Pre-Salt (Brazil, ~10.6 Mt/yr nameplate — the world's largest), Sleipner & Snøhvit (Norway), Quest (Canada), Boundary Dam (Saskatchewan), Gorgon (Australia), Northern Lights Phase 1 (Norway, operational 2025), Stratos DAC (Texas, Phase 1 operations from 2026), Brevik Cement (Norway).
- Explain why ~60% of operational CCUS capacity is at natural gas processing — and why this matters for assessing whether CCUS deployment is on track.
- Articulate the integrity questions specific to CCUS: monitoring, leakage, displacement of investment from direct decarbonization, EOR vs. dedicated storage.
- Explain the post-OBBBA 45Q dynamics and how subsidies are shaping the project pipeline.

---

## Why this chapter exists

Chapters 1–9 have built up the analytical and policy context. CCUS is where the rubber meets the road for the heavy-industry and fossil-fuel-dependent parts of the economy. Many sectors — steel, cement, refining, chemicals, ammonia, hydrogen, possibly some power — have no plausible path to deep decarbonization without some form of carbon capture. CCUS is either *the technology that lets these sectors decarbonize* or *the technology that lets these sectors continue to operate while delaying real decarbonization*. Which framing applies depends substantially on how it's deployed.

The 2025–2030 period will be substantially determinative. We're at the end of a long phase where CCUS was mostly a promise; we're entering a phase where it's either scaling to climate-relevant volumes or proving structurally limited. The current pipeline (~430 Mt/yr capacity by 2030 if all announced projects come online) would represent ~9× the 2025 operational capacity but still falls short of the ~1,000 Mt/yr that the IEA's Net Zero Emissions (NZE) by 2050 scenario suggests is needed by 2030.

This chapter focuses on **point-source CCUS** — capturing CO₂ from industrial and power facilities. Chapter 11 covers **direct air capture and broader CDR** — capturing CO₂ from the atmosphere directly. The distinction is fundamental: point-source CCUS reduces emissions at the source; CDR removes CO₂ from the atmosphere. Both are "carbon capture" but they answer different climate questions.

I'll organize this in seven parts: the technology stack; the project value chain; current state and the gap to NZE; the major operational projects; the economic and policy drivers (45Q, EU funding, China's deployment); the substantive critiques of CCUS; and the path forward 2026–2030.

---

# Part 1: The technology stack

Carbon capture is not a single technology — it's a family of technologies suited to different contexts. The four main categories:

## Post-combustion capture

**What it is:** Capture of CO₂ from flue gas after combustion. The most generic and widely-applicable approach.

**How it works:** Flue gas (which contains roughly 5–15% CO₂ by volume in power plants, 20–30% in cement plants, even higher in some industrial processes) passes through an absorber where CO₂ is selectively captured by a solvent (typically amine-based, like monoethanolamine — MEA — or proprietary solvents like Mitsubishi's KS-1 or Aker Carbon Capture's S26). The CO₂-rich solvent is then heated in a stripper to release pure CO₂, regenerating the solvent for reuse.

**Where it's used:**
- **Coal-fired power plants** (rare — Boundary Dam in Saskatchewan is the only commercial example for a long-running facility)
- **Natural gas-fired power plants** (rare; UK's Net Zero Teesside Power FID in 2024 is among the first)
- **Cement plants** (Brevik in Norway operational 2025; others in pipeline)
- **Steel mills, refineries, chemical plants**
- **Pulp and paper, biomass-fired power (BECCS)**

**Energy and cost:** Post-combustion capture is energy-intensive (typically requires 2.5–4 GJ of heat per tCO₂ captured, plus electricity for compression). Capture costs typically $40–120/tCO₂ depending on flue gas CO₂ concentration and project specifics; costs are higher for dilute streams (power plants) and lower for concentrated streams (cement, some chemicals).

**Strengths:** Retrofittable to existing facilities. Mature commercial technology. Multiple operational projects.

**Weaknesses:** Energy penalty (a power plant with post-combustion CCS produces ~10–25% less net electricity per unit of fuel). Solvent degradation. Capture rates typically 85–95%, not 100%.

## Pre-combustion capture

**What it is:** Capture of CO₂ before combustion, typically by converting a hydrocarbon fuel to hydrogen plus CO₂, then capturing the CO₂.

**How it works:** Natural gas (or other hydrocarbons) is reacted with steam (steam methane reforming) or partial-oxidation processes to produce a syngas (CO + H₂). Water-gas shift reaction converts the CO to CO₂. The CO₂ is separated (usually with physical solvents like Selexol or Rectisol, which work better at higher CO₂ partial pressures than amines). The remaining hydrogen is used as fuel.

**Where it's used:**
- **Hydrogen production** (the largest current pre-combustion capture application — Quest in Canada, Air Products' Port Arthur in Texas, several others)
- **Ammonia and fertilizer production**
- **Integrated gasification combined cycle (IGCC)** power plants — rare in operation; some projects in pipeline.

**Strengths:** Higher CO₂ partial pressure makes separation easier and lower-cost. Produces hydrogen as a useful product, enabling broader applications. Mature in hydrogen and ammonia contexts.

**Weaknesses:** Less retrofittable; typically requires new-build facilities. Most relevant in contexts where hydrogen is itself the product (limited scope vs. post-combustion's broader applicability).

## Oxy-fuel combustion

**What it is:** Burning fuel in pure oxygen (rather than air), producing a flue gas that's nearly pure CO₂ and water.

**How it works:** Air separation unit produces pure O₂. Fuel is combusted in this oxygen-rich environment (with some recycled flue gas to moderate temperatures). The resulting flue gas is nearly all CO₂ and H₂O. Water is condensed; CO₂ is captured at near-100% concentration with minimal separation effort.

**Where it's used:**
- **Cement plants** (some pilot and demonstration projects)
- **Steel mills**
- **Power generation** (limited commercial deployment)

**Strengths:** Very high CO₂ purity in flue gas simplifies capture. Theoretically higher capture rates (95%+).

**Weaknesses:** Air separation is energy-intensive (~200 kWh per tonne of O₂). Net energy penalty often similar to or higher than post-combustion. Less mature commercially.

## Direct air capture (DAC) and broader CDR

Covered in detail in Chapter 11. Briefly: **DAC** captures CO₂ from ambient air (about 425 ppm — three orders of magnitude lower than industrial flue gases), making it much harder than point-source capture. **BECCS** combines biomass combustion (which uses recently atmospheric carbon) with carbon capture, producing net-negative emissions. Both are "removal" technologies in the carbon-accounting sense, distinct from emission reductions at point sources.

## Comparing technologies

| Technology | CO₂ source concentration | Maturity | Best applications |
|---|---|---|---|
| Post-combustion | 3–30% | Commercial | Retrofits, broad applicability |
| Pre-combustion | 30–60% | Commercial in H₂/NH₃ | Hydrogen, ammonia, IGCC |
| Oxy-fuel | ~100% in flue gas | Demonstration | Cement, steel, future power |
| DAC | 0.04% (425 ppm) | Early commercial | Net-negative emissions |

The technology choice for a specific project depends on the source's CO₂ concentration, the available infrastructure, the economic context, and the climate goal (emission reduction vs. removal).

---

# Part 2: The CCUS project value chain

A CCUS project has six main steps:

## 1. Capture

The capture facility separates CO₂ from the source stream. Capture rates typically 85–95% for post-combustion, higher for pre-combustion and oxy-fuel. Energy input typically electricity plus thermal energy (the latter often steam at 100–150°C).

Capture costs vary enormously by application:
- **Natural gas processing:** $15–25/tCO₂ (the easy case — CO₂ is already separated for fuel-spec reasons)
- **Hydrogen production:** $25–45/tCO₂
- **Ammonia production:** $25–45/tCO₂
- **Cement:** $60–120/tCO₂
- **Steel:** $70–130/tCO₂
- **Coal power:** $60–130/tCO₂
- **Gas power:** $80–150/tCO₂
- **Direct air capture (Ch. 11):** $400–1,000+/tCO₂

The 10× cost range across capture applications is essential context. The "cheap CCS" projects (gas processing, hydrogen, ammonia) have been the bulk of operational capacity for two decades. The "expensive CCS" projects (power, cement, DAC) are what's required for climate-meaningful decarbonization but are far less mature.

## 2. Compression and dehydration

Captured CO₂ at atmospheric pressure is too voluminous to transport economically. Compression to supercritical state (above 73.8 bar and 31°C) reduces volume by ~600× and is required for pipeline transport. Water is also removed because wet CO₂ corrodes pipelines.

Compression typically adds $5–15/tCO₂ in capital and operating cost depending on project scale and energy availability.

## 3. Transport

CO₂ is transported from capture facilities to storage sites. The major modes:

**Pipelines** — by far the dominant mode for large-volume CCUS. Approximately 8,000 km of CO₂ pipelines operational globally (most in the US, for legacy EOR uses; see Ch. 3). New pipelines being constructed include Summit Carbon Solutions' Iowa-Nebraska-Wyoming system (Ch. 3), various EU systems (the Pathways network in Alberta, Porthos-Aramis in the Netherlands), and others.

**Ships** — used for cross-border CO₂ transport, especially in Europe. The Northern Lights project uses CO₂ ships to bring CO₂ from emitters across northern Europe to the Norwegian storage site. The shipping infrastructure is new but growing rapidly.

**Trucks and rail** — used for small-scale projects or where pipeline infrastructure doesn't exist. Higher per-ton costs.

Transport costs: $5–15/tCO₂ for pipeline at distance; $10–30/tCO₂ for shipping; $30+/tCO₂ for trucks or rail.

## 4. Injection and storage

CO₂ is injected into geological formations for permanent storage. The main types:

**Saline aquifers** — porous rock formations containing brine water (not usable for drinking or agriculture). The largest theoretical storage capacity globally. Used by Sleipner (since 1996), Snøhvit, Quest, Gorgon, and Northern Lights.

**Depleted oil and gas reservoirs** — formations that previously held hydrocarbons; now serve as storage. Australia's Moomba project (2024 operational) uses depleted gas fields.

**Enhanced oil recovery (EOR)** — injection of CO₂ into operating oil fields to increase oil production. Has been the dominant CCUS use historically (~70% of operational CCUS capacity in the US is EOR-coupled). EOR raises a fundamental question: does it count as climate action? See Part 6.

**Mineralization** — reaction of CO₂ with reactive rocks (basalt, peridotite) to form stable carbonate minerals. Iceland's Carbfix project uses this approach. Very high permanence (geological timescales) but limited geographic suitability.

Storage costs: $5–15/tCO₂ for saline aquifers; can be negative for EOR (the oil revenue offsets costs); higher for mineralization.

## 5. Monitoring, reporting, verification (MRV)

Stored CO₂ must be monitored to confirm it stays put. Standard MRV includes:
- **Reservoir pressure and temperature** tracking
- **Wellhead leak detection**
- **Seismic monitoring** for unusual movement
- **Atmospheric and groundwater monitoring** for surface leakage
- **Periodic 3D/4D seismic surveys** to confirm CO₂ plume behavior

Major regulatory regimes (EU Storage Directive, EPA UIC Class VI in the US, similar regimes in Canada, Australia, Norway, UK) set MRV requirements. The typical commitment: monitoring for the project's operational period plus a defined post-closure period (often 50+ years), after which liability transfers to a public authority.

## 6. Post-closure stewardship

After injection ends, the storage site must be permanently sealed and monitored for as long as required. Long-term stewardship costs are typically built into project economics. The legal framework for post-closure liability is one of the more contested governance issues in CCUS — some jurisdictions transfer liability to the state after a defined period; others keep it with the operator indefinitely.

## **Stop-and-check 10.A**

1. The cost range for CCUS spans from $15/tCO₂ (gas processing) to $1,000+/tCO₂ (DAC). The 50 Mt/yr operational capacity has been heavily concentrated at the low-cost end. What does this say about whether operational CCUS represents climate-meaningful decarbonization?
2. Post-combustion capture is the most retrofittable approach but has the highest energy penalty. Oxy-fuel has lower energy penalty but is harder to retrofit. For a 40-year-old coal power plant in 2030, which would you recommend, and why?
3. CO₂ pipelines and shipping infrastructure are essential for large-scale CCUS but cost roughly the same per ton-mile as oil pipelines (Ch. 3). Why has CO₂ pipeline build-out been so slow relative to the apparent climate need?
4. **Socratic prompt:** If the Norwegian state suddenly transferred 100% of post-closure liability for Sleipner's stored CO₂ to the project operator (Equinor), what would happen? What does this hypothetical tell you about the importance of post-closure liability frameworks?

**Answers**

1. It tells us that operational capacity is a misleading proxy for climate progress. The ~50 Mt/yr is overwhelmingly the cheap "low-hanging fruit" — gas processing at $15–25/tCO₂, where CO₂ was already being separated for fuel-spec reasons — which has been picked for two decades. The climate-meaningful applications (power, cement, steel, DAC) sit at the $60–1,000+/tCO₂ end and remain barely deployed. So most operational CCUS represents the easy, marginal-emissions cases rather than the hard decarbonization the climate problem actually requires.

2. For a 40-year-old coal plant, the better question is often whether to capture at all rather than which method. But forced to choose, post-combustion is the realistic option: it is retrofittable to existing equipment, while oxy-fuel's lower energy penalty is largely theoretical and requires near-rebuilds (a new air separation unit and combustion redesign) that rarely pencil out on an aging asset with limited remaining life. The decisive variable is remaining useful life — a plant near retirement usually favors closure over either capture route.

3. CO₂ pipelines face problems oil pipelines do not: there is no pre-existing revenue stream (the CO₂ has negative value absent subsidy or carbon price), so build-out depends on coordinating capture demand, transport, and storage simultaneously — the bankability and infrastructure-mismatch problems. Add a 20–30 year payback needing policy certainty that most regimes do not provide, plus public opposition and permitting friction, and the per-ton-mile cost similarity to oil is beside the point. The economics and coordination, not the engineering, are the bottleneck.

4. Equinor would likely have declined to build Sleipner, or demanded far higher returns, because open-ended liability for CO₂ that must remain stored for millennia is effectively unquantifiable and uninsurable. No commercial operator can carry thousand-year risk on its balance sheet. The hypothetical shows that the standard framework — operator liability during operations plus a defined post-closure window (often 50+ years), then transfer to a public authority — is not a giveaway but a precondition for any private CCUS investment to occur at all.

---

# Part 3: Current state and the gap

## Operational capacity

As of Q1 2025 (IEA CCUS Projects Database), there is approximately **50 Mt/yr of operational CO₂ capture capacity globally**, slightly up from 47.4 Mt/yr a year earlier. The number of operational facilities has grown to ~79 across 9 industries.

The breakdown of where this capacity is captured:

**~60% at natural gas processing facilities** — including Sleipner (Norway, since 1996), Snøhvit (Norway, since 2008), and many US/Canadian gas-processing-CCS projects. These facilities had to separate CO₂ from natural gas anyway (to meet pipeline-spec gas requirements); CCS just captures and stores that already-separated CO₂.

**~15% at hydrogen and ammonia plants** — Quest (Canada), Air Products Port Arthur (US), various Middle East and Chinese projects.

**~10% at other industrial sources (gas processing/EOR and chemicals)** — including the Petrobras Santos Basin Pre-Salt project (Brazil, ~10.6 Mt/yr nameplate — the world's single largest CCS facility, capturing CO₂ from the pre-salt gas-processing and EOR process; 2024 actual reinjection was ~14.2 Mt). [Note: Petrobras is a gas-processing/EOR project, not a fertilizer or chemical plant. At ~10.6–14 Mt/yr it substantially exceeds a 10% share of 50 Mt/yr; the percentage breakdown here is approximate.]

**~5% at coal power** — primarily Boundary Dam (Saskatchewan, since 2014) and small-scale projects in China.

**~5% at iron and steel** — primarily Abu Dhabi's Al Reyadah project.

**~5% at other industrial sources** — cement (just coming online with Brevik in 2025), refining, biomass.

The 60% concentration at gas processing is significant. Gas-processing CCS is the lowest-cost form of carbon capture ($15–25/tCO₂) because the CO₂ separation work is being done anyway. **This is the "low-hanging fruit" that has been picked for decades**. The harder applications — power, cement, steel — have been much slower to deploy.

## Pipeline of projects

Looking at the announced project pipeline through 2030 (IEA database):

- **~430 Mt/yr of capture capacity** could become operational by 2030 if all announced projects proceed on schedule.
- **~670 Mt/yr of storage capacity** could be available by 2030 (storage capacity often greater than capture capacity in clustered hub configurations).
- **628 projects** in various stages of the pipeline globally (up ~60% since 2023).
- **247 projects** at FEED (Front-End Engineering Design) stage, more than double 2023 levels.
- **~$6.4 billion in CCUS investment** in 2024 (tripled since 2022).

Geographic concentration is striking, though the picture depends on which denominator you use:
- **~80% of the announced new-project pipeline** (by capture capacity) is in North America and Europe — the IRA/45Q and EU/UK floors are pulling the growth.
- By contrast, China and the Middle East hold a larger share of *operational* capacity (~25%) than of that forward pipeline, because the early CCS stock skewed toward their EOR and gas-processing projects.
- Most of Africa, South Asia, and Latin America have minimal CCUS pipeline on either lens.

## The gap to net zero pathways

The IEA's Net Zero Emissions (NZE) by 2050 scenario suggests required CCUS capacity:
- **~1,024 Mt/yr by 2030** (more than 20× current levels).
- **~6,040 Mt/yr by 2050** (more than 120× current levels).

The current pipeline (~430 Mt/yr by 2030 if all announced projects materialize) falls short of NZE by roughly a factor of 2.5×. And not all announced projects materialize — historical experience suggests perhaps 50–70% of announced projects reach operation, so the realistic 2030 operational capacity may be ~250–350 Mt/yr.

The 2030 gap is:
- **Required:** ~1,000 Mt/yr
- **Pipeline:** ~430 Mt/yr (announced projects)
- **Plausible realization:** ~250–350 Mt/yr

This is a gap of approximately 3–4× between what's likely and what's needed.

## Why the gap exists

The persistent under-deployment of CCUS relative to scenarios has several causes:

**1. CCUS economics depend on policy support.** Most CCUS applications outside gas processing aren't economic without subsidies or carbon prices. The 45Q tax credit in the US, the EU's ETS plus Innovation Fund, the UK's CCS contracts-for-difference framework — these are the primary drivers. Where policy support is weaker, deployment is slower.

**2. Infrastructure mismatch.** Capture facilities need access to CO₂ transport and storage infrastructure. Most regions don't have this. Building shared "hub" infrastructure (multiple capture facilities → shared pipelines/ships → shared storage) requires coordination that's difficult to achieve.

**3. The bankability problem.** CCUS projects require 20–30 year payback periods to generate returns, depending on carbon price and revenue stability. Most carbon-pricing regimes don't offer that policy certainty. The UK has addressed this with contracts-for-difference (CCS-CfD); the US relies on the 45Q tax credit (with the OBBBA changes — see Part 5).

**4. The "build CCS or shut the plant" decision.** For aging coal and industrial facilities, the CCS investment must compete with simply retiring the plant and replacing with renewables or low-carbon alternatives. Often the latter is more economic. CCS economics are most favorable for assets that have remaining useful life and where alternatives are weak (cement, steel, certain heavy industry).

**5. Political controversy.** CCS has been politically contested — critics argue it's a fossil-fuel lifeline; supporters argue it's essential for hard-to-abate sectors. The fossil-fuel-lifeline critique has limited CCS political support in some jurisdictions (EU member states have been mixed; US support is fluctuating with administrations).

## What's changing

Several factors are accelerating deployment:

**1. Cost improvements.** Capture costs are declining as the technology matures. Brevik (Norway cement, operational 2025) achieved costs in the $80–100/tCO₂ range — competitive with current carbon prices in EU.

**2. Hub-based development.** Northern Lights, Porthos-Aramis, the East Coast Cluster (UK), Pathways (Canada), and similar hubs are shared-infrastructure plays that pool capture demand across emitters and unlock storage access.

**3. Cross-border CO₂ transport.** Northern Lights receives CO₂ from emitters in the Netherlands, Belgium, Germany, Ireland, France, and Sweden. The international CO₂ transport infrastructure has shifted from concept to operations in 2025.

**4. CBAM-driven exposure.** Steel, cement, and aluminum exporters to the EU face CBAM costs that make capture investment more attractive. The 2026 CBAM enforcement is driving project FIDs in Turkey, India, and other CBAM-exposed exporters.

**5. Supportive policy in some major markets.** US 45Q increases (post-OBBBA), UK CCS-CfD allocations, EU Innovation Fund, Canada's Investment Tax Credit, China's pilot programs — all are mobilizing capital toward CCUS.

The 2026–2030 period will substantially determine whether CCUS scales toward NZE pathway requirements or stays at the 250–350 Mt/yr level despite the announced pipeline.

## **Stop-and-check 10.B**

1. About 60% of operational CCUS capacity is at gas processing — the cheapest application, where the CO₂ was already being separated for fuel-spec reasons. Why does that one fact mean "50 Mt/yr operational" overstates climate progress?
2. Realistic 2030 capacity (~250–350 Mt/yr) is roughly 3–4× below NZE's ~1,000 Mt/yr. Of the structural reasons the gap persists (economics, infrastructure mismatch, bankability, the build-vs-retire choice, politics), which is the binding constraint — and how does it connect to the CCS-financing pattern from Ch. 3?
3. For an aging coal plant, a CCS retrofit competes with simply *retiring* the plant and replacing it with renewables. When does CCS win that contest, and when does retirement win?
4. **Socratic prompt:** The announced pipeline is ~430 Mt/yr, but historically only 50–70% of announced CCS projects reach operation. You're stress-testing a national climate plan that *assumes its announced CCS pipeline delivers in full*. What would you demand to see before trusting that number?

**Answers**

1. Because the 60% at gas processing isn't doing the hard climate work — it's capturing CO₂ that was already being stripped out to meet pipeline-spec gas requirements, so the marginal cost and the marginal abatement are both small. It's the cheapest tonne ($15–25/tCO₂), it's been picked for two decades, and it tells you almost nothing about whether capture can scale in the sectors that matter (power, cement, steel), which sit at $60–1,000+/tCO₂ and remain barely deployed. So "50 Mt/yr operational" measures how much low-hanging fruit exists, not how much climate-meaningful decarbonization CCS is delivering — the headline capacity is real but unrepresentative.

2. Bankability is the binding constraint, and it's the same problem as the graphite plants and CCS hubs in earlier chapters: CCUS projects need 20–30-year paybacks, but most carbon-pricing regimes don't offer revenue certainty over that horizon, so projects can't reach FID. Economics (most applications uneconomic without support), infrastructure mismatch (no transport/storage nearby), and the build-vs-retire choice all feed into it, but they reduce to "no contracted, durable revenue stream, no financing." It's exactly the Ch. 3 pattern — policy has to manufacture a revenue floor (UK CCS-CfD, Norway's Longship, 45Q's transferable credit) before private capital will build. Where that floor is absent or short (the US 45Q's 12-year window vs. the UK CfD's 25 years), deployment stalls.

3. CCS wins where the asset has substantial remaining useful life *and* there is no cheaper low-carbon alternative — which is rarely true for coal power (renewables plus storage now usually beat coal-plus-CCS) and much truer for cement and steel, where process emissions can't be electrified away. Retirement wins when the plant is old, alternatives are cheaper, and the CCS retrofit would lock in decades more fossil operation just to capture part of the stream. For a 40-year-old coal plant specifically, retirement-and-replace usually dominates; the CCS-retrofit case is strongest for younger assets in genuinely hard-to-abate sectors.

4. I'd demand evidence that each project has crossed the gates that separate an announcement from a build: a final investment decision (not just FEED), a contracted revenue floor (CfD, long-term offtake, or monetizable credits sufficient for the payback), secured transport-and-storage access (a permitted Class VI well or hub agreement, not a hoped-for one), and resolved permitting/community status. I'd haircut the headline by the historical 30–50% attrition, apply heavier discounts to projects lacking FID and revenue certainty, and treat first-of-a-kind cost estimates skeptically. A plan that books the full 430 Mt/yr is assuming away exactly the bankability and execution risk the deployment record says is the main event — so the burden of proof is on each tonne having a financed, sited, FID'd home, not an announcement.

---

# Part 4: The major operational and FID-stage projects

## Petrobras Santos Basin Pre-Salt (Brazil, ~10.6 Mt/yr)

The world's single largest CCS project by capacity. Captures CO₂ from natural gas associated with oil production in Brazil's offshore Pre-Salt fields. The CO₂ is re-injected for EOR. Operational since 2013.

**Significance:** Demonstrates that very large-scale CO₂ separation and re-injection is technically feasible. However, the project is heavily oriented toward enhanced oil recovery — the CO₂ is being used to extract more oil, raising the question of whether net CO₂ removal occurs. (Treated more in Part 6.)

## Sleipner (Norway, ~1 Mt/yr) — the original

Began operation **September 15, 1996** — the world's first commercial CCS project at scale. Captures CO₂ from Sleipner gas field processing (the natural gas is high in CO₂; separation was needed for pipeline-spec gas; storage was added because Norway's carbon tax made venting expensive). Stores in saline aquifer (Utsira formation) 800 m below sea bed.

**Significance:** Three decades of operational data. Demonstrates the long-term viability of saline aquifer storage. Has been continuously monitored with no detectable leakage. The proof-of-concept for the entire CCUS industry.

## Snøhvit (Norway, ~700 ktCO₂/yr)

Companion project to Sleipner. Operational since 2008. Same fundamental approach: gas processing CO₂ separated and stored in saline aquifer. However, the project encountered a significant injectivity problem: CO₂ injected into the Tubåen Formation caused rapid pressure build-up (~943 psi over initial reservoir pressure) due to a small isolated channel and faulted reservoir geometry. Injection into the Tubåen was halted in April 2011 and switched to the overlying Stø Formation, where injection has proceeded successfully. No surface leakage has been detected, but the episode is the canonical example of why detailed reservoir characterization is essential — and why "no detectable leakage" should not be conflated with "operated without incident."

## Quest (Canada, ~1 Mt/yr)

Operational since 2015 in Alberta. Captures CO₂ from Shell's Scotford hydrogen production facility (which serves the bitumen upgrading operations). Stores in deep saline aquifer. The first commercial CCS facility serving heavy oil processing.

**Significance:** Demonstrates pre-combustion capture and saline aquifer storage at industrial scale. One of the few CCS projects with substantial publicly-available operational data.

## Boundary Dam (Saskatchewan, Canada, ~1 Mt/yr at design)

Operational since 2014. The world's first commercial-scale CCS on a coal-fired power plant (110 MW capacity post-retrofit). Post-combustion capture at SaskPower's Boundary Dam Unit 3.

**Significance:** Proves coal-CCS is technically possible but financially difficult. Boundary Dam has had operational issues including periods well below design capture rate. As of September 2025, the project had captured a cumulative ~7.1 Mt CO₂ since 2014 (SaskPower disclosures), having recovered from earlier underperformance and approximately meeting its design capture trajectory — though annual capture (~700–790 ktCO₂/yr) remains below the ~1 Mt/yr design rate.

## Gorgon (Australia, ~3.4 Mt/yr at design)

Chevron's Gorgon LNG facility on Barrow Island, Western Australia. CCS injects CO₂ from gas processing into a saline aquifer beneath the island. Operational since 2019. Design capacity ~3.4 Mt/yr.

**Significance:** Important for demonstrating gas-processing CCS in non-Norwegian contexts. However, the project has struggled with operational performance — has consistently run below design capacity due to technical issues. Cumulative CO₂ injected through 2024 was ~10.5 Mt vs. design ~17 Mt. A reminder that CCS is not yet a fully-mature plug-and-play technology.

## Northern Lights Phase 1 (Norway, 1.5 Mt/yr operational; Phase 2 to 5 Mt/yr by 2028)

The breakthrough project for the European CCS landscape. Commercial operations began **August 25, 2025**. Receives CO₂ via ship from emitters across northern Europe (Heidelberg Materials' Brevik cement plant in Norway; Yara's ammonia facility in the Netherlands; ENBW Energie Baden-Württemberg's emissions in Germany; others). Stores 2,600 m below seabed in the Aurora storage site.

**Significance:** First commercial cross-border CO₂ shipping operation. First operational hub model (multiple emitters, shared infrastructure). The template for the European CCS sector. Phase 2 expansion (FID March 2025) brings storage capacity to 5+ Mt/yr by 2028. Backed by €131 million in EU funding.

## Brevik Cement (Norway, 400 kt/yr)

Heidelberg Materials' Brevik plant captures 50% of its CO₂ emissions starting 2025 — the **world's first commercial CCS at a cement plant**. CO₂ goes to Northern Lights via ship. Post-combustion capture using amine technology.

**Significance:** Proves cement CCS is commercially possible. Cement emissions are roughly 8% of global CO₂; if Brevik's approach can be replicated, the cement sector becomes addressable. The capture cost is in the $80–100/tCO₂ range.

## Moomba CCS (Australia, 1.7 Mt/yr)

Santos's Moomba project in South Australia. Operational October 2024. Reuses existing oil and gas processing infrastructure and depleted gas reservoirs. Achieves capture costs under $30/tCO₂ — one of the lowest in the world due to reuse of existing infrastructure.

**Significance:** Demonstrates that integrated brownfield CCS can be cost-competitive. The "easy retrofit" model.

## Stratos DAC (Texas, USA, 500 ktCO₂/yr at full capacity)

Occidental Petroleum's 1PointFive subsidiary brought the world's largest direct air capture facility online in 2025. Located in the Permian Basin. CO₂ captured and stored geologically (with some EOR use).

**Significance:** Brings DAC to commercial-relevant scale (500 kt/yr is roughly 100× the previous largest DAC facility). Provides a template for the next decade's DAC scaling. Heavily reliant on 45Q tax credits and voluntary credit purchases (Microsoft and others have purchased Stratos credits at premium prices).

## Net Zero Teesside Power (UK, FID 2024)

UK's first commercial gas-power CCS facility. Reached FID in 2024 with capture capacity of 2 Mt/yr. Operational target 2027–2028. UK's CCS Cluster Sequencing program supports it with contracts-for-difference revenue.

**Significance:** First commercial CCS on a gas-fired power plant. Tests whether CCS on gas can be cost-effective at scale.

## ExxonMobil Baytown Blue Hydrogen (USA, paused November 2025)

Covered in Chapter 3: ExxonMobil's blue hydrogen and CCS hub at Baytown, Texas was paused in November 2025 due to economic and policy challenges. The pause is a notable setback — Baytown was supposed to be one of the largest US CCUS projects and a foundation for the Gulf Coast carbon-transport hub.

## Indonesia Tangguh LNG (FID 2024)

ExxonMobil and BP's Tangguh LNG expansion in West Papua, Indonesia. CCS reached FID in 2024 with capture capacity of ~25 Mt/yr (very large — gas processing-derived). One of the largest CCS project FIDs ever, illustrating that the technology can be deployed at very large scale in the gas processing context.

## **Stop-and-check 10.C**

1. Sleipner has been operating since 1996 — almost 30 years. Why hasn't the Sleipner model been replicated more widely outside of gas processing?
2. Petrobras Santos Basin captures ~10.6 Mt/yr (nameplate; 2024 actual ~14.2 Mt) — the world's largest CCS project. But the CO₂ is used for EOR. Does this count as climate action? (Return to this in Part 6.)
3. Northern Lights' commercial start in August 2025 is widely described as a turning point. What about it is structurally different from prior CCS projects?
4. **Socratic prompt:** If you had to advise the US Department of Energy on which CCUS project type to prioritize for federal support, would you choose (a) more big gas-processing CCS, (b) cement CCS, (c) steel CCS, (d) coal power CCS, or (e) DAC? Defend a single choice.

**Answers**

1. The Sleipner model works because gas processing already separates CO₂ to meet pipeline-spec gas requirements, so capture is nearly free and storage is the only added step — and Norway's carbon tax made venting more expensive than storing. Outside gas processing, capture must do the full, energy-intensive separation work from dilute flue gas, costs jump three- to ten-fold, and the climate-meaningful applications lack both the cheap concentrated stream and the policy pressure Norway's tax provided. The model didn't replicate because its core advantage — pre-separated CO₂ plus a punitive venting cost — is specific to gas processing.

2. By the chapter's own framing, this is genuinely contested. Petrobras re-injects the CO₂ for enhanced oil recovery, so the injected CO₂ extracts additional oil that is then burned. Whether it counts as climate action turns on the marginal-oil counterfactual: if EOR substitutes for equivalent oil that would have been produced anyway while keeping CO₂ that would otherwise be vented underground, it is modestly climate-positive; if it enables incremental oil production that wouldn't have happened, the downstream combustion emissions can offset or exceed the injected ton. The answer depends on the counterfactual, not the technology.

3. Northern Lights is the first operational hub-and-spoke model and the first commercial cross-border CO₂ shipping operation. Prior projects were single-emitter, vertically integrated stores (a gas plant disposing of its own CO₂). Northern Lights instead provides shared transport-and-storage as a service, receiving CO₂ by ship from many emitters across several countries (Brevik cement, Yara ammonia, German power). This decouples capture from storage, lets emitters without local geology participate, and pools demand to make the infrastructure bankable — a structural shift from project-by-project CCS.

4. A defensible single choice is cement CCS. Cement's process emissions (CO₂ released from limestone calcination) cannot be eliminated by electrification or fuel-switching, so capture is the only deep-decarbonization route — unlike coal power, where renewables plus storage are cheaper and CCS mainly delays retirement. Cement also has a higher flue-gas CO₂ concentration than power, lowering capture cost, and Brevik already proves commercial feasibility at $80–100/tCO₂. The decisive criterion is prioritizing sectors with no alternative and a demonstrated, replicable template; DAC is defensible too but far costlier and earlier-stage.

---

# Part 5: Economic and policy drivers

## 45Q (US)

The Section 45Q tax credit is the dominant CCUS policy in the US and one of the largest CCUS subsidies globally.

**History:**
- **2008:** Original 45Q enacted with modest credit values ($10/tCO₂ for EOR-coupled, $20/tCO₂ for dedicated storage). Limited uptake.
- **2018:** Bipartisan Budget Act expanded 45Q substantially. Credit values rose to $35/tCO₂ for EOR-coupled, $50/tCO₂ for dedicated storage. Direct pay and transferability added.
- **2022:** Inflation Reduction Act (IRA) further expanded. Values raised to $60/tCO₂ for EOR-coupled (with bonus provisions), $85/tCO₂ for dedicated storage (with bonus provisions), $180/tCO₂ for DAC with storage, $130/tCO₂ for DAC with EOR. Direct pay made permanent. Substantial bonus credits for prevailing wage and domestic content.
- **2025 OBBBA (One Big Beautiful Bill Act, July 2025):** Set EOR-coupled and dedicated-storage credits to the *same level* of $85/tCO₂. Maintained DAC values. Phased out certain bonus credits. Effect: makes EOR economically equivalent to dedicated storage from a 45Q perspective, removing the climate-policy preference for actual sequestration vs. EOR.

The 45Q changes have substantial implications:
- **More projects financially viable.** Higher credits enable projects that wouldn't pencil out at lower subsidies.
- **EOR economically equivalent to storage** under OBBBA. Climate critics argue this is regressive (rewards continued oil production); industry argues it incentivizes more capture regardless of disposition.
- **DAC heavily subsidized.** $180/tCO₂ for DAC with permanent storage makes DAC the most-supported climate technology in US policy. Approximately the same level as the SCC under the Biden estimate.

**Current status (mid-2026):** 45Q is the operational US CCUS subsidy. The Trump administration's broader stance on climate has not (yet) led to direct attacks on 45Q, partly because it's bipartisan (Sen. Capito, Sen. Whitehouse, others have supported expansions) and has strong industry constituency.

## EU Innovation Fund and Hydrogen Bank

The EU's funding mechanisms for CCUS are several:

- **Innovation Fund:** Approximately €38 billion through 2030 from ETS revenues, supporting innovative low-carbon technologies including CCUS. Multiple CCUS project awards in 2022–2025.
- **Hydrogen Bank:** Specific support for renewable hydrogen production, with separate window for "fossil + CCS" (blue hydrogen) under restrictive conditions.
- **Project of Common Interest (PCI) status:** Streamlines permitting and provides funding access for cross-border CO₂ networks.
- **State aid approvals:** Member states like Norway, UK (technically outside EU), Netherlands, Denmark have provided substantial national support.

The EU's CCUS support emphasizes hub-based infrastructure development and cross-border CO₂ networks. Northern Lights, Porthos, Aramis, Acorn, and the East Coast Cluster are all beneficiaries.

## UK CCS-CfD

The UK has developed one of the most sophisticated CCUS support frameworks. The CCS Contracts for Difference (CCS-CfD) provides revenue stability for emitters investing in capture, with the government covering the difference between the carbon price and a strike price set by competitive auction.

**Status:** First Track 1 allocation completed 2023, supporting four projects (East Coast Cluster, HyNet North West). Second Track 1 allocation in 2024. Track 2 allocations planned. The framework is designed to provide ~25-year revenue certainty.

## Canada and Norway

**Canada's CCUS Investment Tax Credit** (announced 2022, in force 2023): 50% of capital cost for direct CO₂ capture (60% for DAC), 37.5% for transport and storage. Combined with provincial supports (Alberta's TIER credits, Saskatchewan's similar programs), provides substantial subsidy.

**Norway's CO₂ tax** has been a major driver of Sleipner and Snøhvit. Currently NOK 952/tCO₂ (~$95), rising to NOK 2,000/tCO₂ (~$220) by 2030. Combined with the carbon-storage exemption, this creates strong CCS economics. **Longship** is the Norwegian government's flagship CCS funding program supporting Northern Lights and Brevik.

## China's deployment

China's CCS deployment has been less subsidized but driven by:
- **State-owned enterprise mandates** in oil and gas (CNPC, Sinopec, CNOOC).
- **Industrial demonstration programs** at key facilities (Qilu-Shengli, Sinopec Zhongyuan).
- **Carbon market integration** — China's national ETS could create demand for CCS over time.
- **Strategic positioning** — China is investing in CCS expertise as part of broader industrial policy positioning.

Chinese CCS capacity is harder to track in international databases but is growing rapidly. Estimates suggest ~5 Mt/yr operational in China by end of 2024, with substantial expansion planned.

## **Stop-and-check 10.D**

1. The OBBBA equalized 45Q values between EOR-coupled and dedicated storage at $85/tCO₂. From a climate-policy perspective, is this a win or loss? Make the case both ways.
2. The UK's CCS-CfD provides 25-year revenue certainty. The US 45Q is a 12-year credit (per project). How does this difference affect project financing decisions?
3. China's CCS deployment is happening without major subsidy — driven by state-owned enterprise mandates and industrial demonstration. What does this say about deployment models outside the US-EU framework?
4. **Socratic prompt:** If you were designing CCUS policy from scratch in a hypothetical major economy in 2026, what would you prioritize — a strong subsidy like 45Q, a price-stabilization mechanism like CCS-CfD, or something else? Defend your choice.

**Answers**

1. Both cases are legitimate. The "loss" case: by paying EOR-coupled and dedicated storage identically at $85/tCO₂, OBBBA removes the policy preference for permanent sequestration over CO₂ that extracts more oil whose combustion emits further — rewarding continued oil production and blurring the climate distinction. The "win" case: industry argues the equalization simply incentivizes more capture regardless of disposition, pulling additional CO₂ out of stacks that would otherwise be vented, and higher credits make more projects bankable. The disagreement reduces to whether you trust the EOR marginal-oil counterfactual.

2. The UK's ~25-year CCS-CfD certainty directly addresses the bankability problem: CCUS projects need 20–30 year payback periods, and lenders price long-tenor debt on revenue stability. A 12-year 45Q credit covers only part of the asset's life, leaving post-credit revenue dependent on uncertain carbon prices, which raises the cost of capital and shortens financeable debt. The CfD's longer horizon supports cheaper, higher-leverage project finance; 45Q tends to favor equity-heavy structures or sponsors who can monetize the credit quickly via transferability.

3. It shows the subsidy-led US-EU model is not the only viable deployment pathway. China is mobilizing CCS through state-owned-enterprise mandates (CNPC, Sinopec, CNOOC), industrial demonstration programs, and strategic industrial positioning rather than per-ton credits. In economies with strong state direction over heavy industry, deployment can be commanded rather than priced. The implication is that the "policy support is essential" lesson is about needing *some* forcing mechanism — tax credit, price stabilization, or mandate — not specifically a Western-style subsidy.

4. A defensible answer prioritizes a price-stabilization mechanism like CCS-CfD, because the binding constraint identified in this chapter is bankability — projects need ~25-year revenue certainty that volatile carbon prices and time-limited credits don't deliver. A CfD targets that directly while letting competitive auctions discover the true cost. The decisive variables are the maturity of your carbon market (a credible price for the CfD to reference) and fiscal capacity. Absent a functioning carbon price, a 45Q-style subsidy or a mandate may be the only feasible starting point.

---

# Part 6: The substantive critiques

CCUS is one of the most politically contested climate technologies. The critiques fall into several categories.

## Critique 1: CCUS is a fossil-fuel lifeline

The deepest concern: CCUS allows continued fossil fuel use under the pretense of decarbonization, when the climate goal should be reducing fossil fuel use to near zero.

**The argument:** The IEA NZE scenario shows fossil fuel use falling sharply by 2050 even with CCUS deployment. CCUS at 6 Gt/yr by 2050 (~15% of current CO₂ emissions) addresses residual emissions in hard-to-abate sectors but doesn't enable continued large-scale fossil fuel use. Where CCUS is deployed to "decarbonize" continued fossil fuel use (especially in power generation, where renewables are cheaper), it competes for capital with cleaner alternatives.

**The defense:** For sectors where alternatives don't yet exist (cement process emissions, steel from blast furnaces, ammonia, refining, some chemicals), CCUS is the only available decarbonization route. Rejecting CCUS for these sectors effectively requires either (a) shutting them down, or (b) continued unmitigated emissions. The "lifeline" framing is misapplied when CCUS targets sectors with no alternative.

**Where the critique lands:** Most strongly in power generation (where renewables generally are cheaper and CCUS is delaying retirement). Less strongly in heavy industry where CCUS may be genuinely necessary.

## Critique 2: EOR doesn't count as climate action

Approximately 70% of historical US CCUS capacity is enhanced oil recovery — CO₂ injected to extract more oil. The oil is then burned, producing more CO₂.

**The argument:** A ton of CO₂ injected for EOR is associated with extraction and combustion of additional oil whose downstream CO₂ emissions can exceed the injected ton. Various lifecycle analyses suggest EOR-coupled CCS is at best net-neutral and possibly net-positive in emissions, depending on the marginal-oil counterfactual.

**The defense:** EOR-coupled CCS keeps CO₂ underground that would otherwise be vented. If the alternative is unmitigated CO₂ + oil extraction, EOR-coupled CCS is climatically better. The marginal-oil counterfactual is critical — if EOR substitutes for cheaper but worse oil sources, the net climate effect may be small.

**Where the critique lands:** EOR-coupled CCS is climate-positive if you accept the marginal-oil counterfactual where the alternative is unmitigated venting plus equivalent oil production from other sources. It's climate-neutral or negative if EOR enables incremental oil production that wouldn't have happened otherwise. The 2025 OBBBA's equalization of 45Q values between EOR and dedicated storage removed the policy preference for the cleaner option — a substantively concerning shift.

## Critique 3: CCUS competes for capital with direct decarbonization

A dollar spent on CCUS is a dollar not spent on renewables, EVs, building efficiency, or other direct-decarbonization measures. The question: is the marginal CCUS dollar yielding more emissions reductions than the marginal direct-decarbonization dollar?

**The argument:** Renewable energy now costs less than fossil-plus-CCUS in most contexts. Battery storage is becoming cost-competitive with fossil-plus-CCUS for firming. The capital costs of CCUS at scale would be enormous (trillions of dollars by 2050 under NZE scenarios). That capital is potentially more impactful elsewhere.

**The defense:** The marginal CCUS dollar matters most in sectors where direct decarbonization is hardest. Renewables don't address cement process emissions or steel blast furnaces. The "competing for capital" framing assumes a fixed total capital pool, but actually climate finance is dramatically under-supplied relative to need — both sources can grow.

**Where the critique lands:** Most strongly when CCUS is deployed in sectors where alternatives exist and are cheaper (power generation primarily). Less strongly in sectors without alternatives.

## Critique 4: Monitoring and verification are insufficient

For CCUS to provide climate benefit, the stored CO₂ must stay stored. Current MRV requirements are 50–100 year monitoring periods, but CO₂ in saline aquifers is supposed to be stored for thousands of years.

**The argument:** No technology can monitor CO₂ for 1,000+ years. Long-term liability gets transferred to public authorities who may not maintain monitoring rigor. Reservoir behavior over geological timescales is not fully understood.

**The defense:** Multi-decade operational data (Sleipner 30+ years, Snøhvit 16+ years) shows no detectable leakage. Reservoir engineering is well-developed (oil and gas industry has 100+ years of subsurface experience). The long-tail risk of leakage is small but not zero, and is comparable to other geological storage (nuclear waste, natural gas, etc.).

**Where the critique lands:** A genuinely valid concern that requires ongoing attention. The risk is real but probably overstated by critics relative to comparable risks elsewhere.

## Critique 5: The cost curve isn't bending fast enough

CCUS costs have declined modestly over the past decade but not at the pace renewables have declined. The expected scale economies and "learning by doing" haven't materialized as strongly as supporters claimed.

**The argument:** Solar costs fell 90% since 2010. Wind fell 50%. Batteries fell 80%. CCUS costs have fallen perhaps 20–30%. The cost-decline trajectory doesn't suggest CCUS will become cheap enough to deploy at climate-relevant scale.

**The defense:** Most CCUS deployment to date has been first-of-a-kind projects, where costs are inflated. Scale economies and standardization haven't been achieved. Hub-based deployment, standardized capture technologies, and improved monitoring should drive costs down meaningfully.

**Where the critique lands:** A reasonable observation that costs may not fall as needed for full NZE deployment. CCUS at $80–100/tCO₂ is competitive with current EU ETS prices; CCUS at $200/tCO₂ is not. Whether cost curves achieve the former level broadly is genuinely uncertain.

## A balanced reading

The substantive critiques of CCUS aren't easily dismissed, but neither do they justify rejecting CCUS entirely. The current 50 Mt/yr operational capacity is mostly low-cost gas-processing CCS that's been operating cleanly for decades. The pipeline is mostly first-of-a-kind projects in cement, steel, hydrogen, and DAC where the climate case is strongest. The 2026–2030 deployments will substantially clarify which CCUS applications work and which don't.

The likely outcome: **CCUS deployment expands meaningfully but falls short of NZE scenarios.** Some sectors (cement, steel, ammonia, blue hydrogen, possibly some power) will use CCUS. Other sectors (most power generation, transportation, buildings) will not. The 2030 operational capacity will likely be in the 200–400 Mt/yr range — below NZE requirements but well above current levels, and concentrated in sectors where direct decarbonization is hardest.

The honest reading: CCUS is **a necessary component of comprehensive decarbonization but not a complete one**. It works alongside renewables, electrification, efficiency, and (for the hardest emissions) direct air capture, in a multi-tool portfolio.

## **Stop-and-check 10.E**

1. The "fossil-fuel lifeline" critique lands hardest in one sector and weakest in another. Which, and why does the *sector* — not the technology — determine whether the critique is fair?
2. EOR-coupled CCS: walk through the marginal-oil counterfactual that decides whether it's climate-positive, neutral, or negative. Why did OBBBA's 45Q equalization make the climate concern worse?
3. "CCUS competes for capital with direct decarbonization." When is that a strong objection, and when does it dissolve?
4. **Socratic prompt:** Each of the five critiques is framed as "where it lands" rather than "true or false." Synthesize: give the one-sentence honest verdict on CCUS that all five critiques *together* support — and the one-sentence rebuttal a thoughtful proponent would offer.

**Answers**

1. It lands hardest in **power generation** and weakest in **heavy industry** (cement, steel, ammonia). In power, renewables-plus-storage are now generally cheaper than fossil-plus-CCS, so CCS there mostly prolongs fossil assets that have a cheaper clean substitute — the lifeline critique is fair. In cement and steel, the emissions are partly *process* emissions (calcination, blast-furnace chemistry) with no electrification path, so capture is the only deep-decarbonization route and "lifeline" is misapplied. The technology is identical in both; what changes is whether a cheaper alternative exists. So the critique is really a claim about *substitutability in the sector*, not about CCS itself — which is why "is CCS a lifeline?" has no sector-independent answer.

2. The injected CO₂ extracts additional oil that is later burned, so the climate verdict turns on what that oil displaces. If the EOR barrel substitutes one-for-one for a barrel that would have been produced anyway (from a dirtier source), and the injected CO₂ would otherwise have been vented, then EOR-coupled CCS is modestly climate-positive — net CO₂ goes underground that otherwise wouldn't. If instead the cheap EOR barrel is *incremental* — oil produced that wouldn't have been, at a price that expands consumption — its combustion emissions can equal or exceed the injected tonne, making the system neutral-to-negative. OBBBA made it worse by paying EOR-coupled and dedicated storage the *same* $85/tCO₂, erasing the prior policy preference for permanent sequestration and removing the incentive to choose the cleaner disposition — so the subsidy now rewards the EOR pathway equally regardless of the counterfactual.

3. It's strong wherever a cheaper direct-decarbonization substitute exists for the same emissions — again, mainly power, where a dollar into renewables abates more than a dollar into coal-plus-CCS, so CCS capital is genuinely lower-leverage. It dissolves in two situations: where no substitute exists (cement process CO₂ — the renewables dollar can't touch it, so the comparison is false), and to the extent the "fixed capital pool" premise is wrong (climate finance is under-supplied relative to need, so the two can grow together rather than trading off). The objection is really "is this the highest-leverage use of the marginal dollar *for these emissions*?" — decisive in substitutable sectors, moot in non-substitutable ones.

4. **Honest verdict the five critiques jointly support:** CCUS is a genuinely necessary tool for a narrow set of hard-to-abate, no-substitute emissions, but it has been oversold as a general decarbonization solution, is too easily steered (by EOR economics and fossil interests) toward prolonging fossil use rather than abating the residual, and won't reach the volumes scenarios assume. **The proponent's one-sentence rebuttal:** none of that argues against deploying CCUS where it *is* the only option — the critiques are arguments for *targeting* it at cement, steel, chemicals, and durable storage and disciplining the EOR/power misuses, not for rejecting the one technology those sectors actually need. *(Both sentences describe the same balanced position from opposite ends: deploy it, but only where it's the right tool, and guard against the misuses the critiques identify.)*

---

# Part 7: The path forward 2026–2030

The next five years will substantially determine CCUS's role in the broader climate landscape. Several inflection points:

## Major projects to watch

**Net Zero Teesside Power (UK, 2027–2028).** First gas-power CCS at scale. Tests whether the technology and economics work for power generation.

**East Coast Cluster (UK, 2027).** UK's largest CCS hub. Multiple industrial emitters with shared infrastructure.

**Porthos and Aramis (Netherlands, 2027–2029).** EU's largest planned CCS storage. Tests cross-border European CO₂ infrastructure at scale.

**Tangguh LNG (Indonesia, 2027–2028).** Reaches operation. Demonstrates very-large-scale CCS in LNG context.

**Stratos Phase 2 (USA, 2027–2028).** Scales DAC further. Tests whether DAC can move from kilotonnes to megatonnes of removal capacity.

**Northern Lights Phase 2 (Norway, 2028).** 5 Mt/yr capacity. Confirms scaled hub-and-spoke model.

**Various Chinese projects.** Several megatonne-scale projects in development. Tests Chinese deployment model at scale.

## Policy battlegrounds

**45Q in the US (2025–2026).** The OBBBA changes are recent. Whether they hold (or are reversed by future Congresses) is a major variable.

**EU 2026 ETS reform.** The integration of CDR into the ETS — and the implications for CCS — is being negotiated.

**CBAM expansion.** If CBAM extends to additional sectors and remains durable, the demand for CCUS in CBAM-exposed industries grows.

**Article 6 operationalization.** The interaction of voluntary credit purchases with national NDCs will shape global CCS finance.

## The 2030 outlook

The plausible 2030 outcomes:

**Optimistic case:** CCUS operational capacity reaches 400–500 Mt/yr by 2030. Hub-based deployment in Europe and the US becomes the model. Cement and steel CCS are operational at multiple facilities. DAC reaches 5–10 Mt/yr. Costs have come down. The trajectory toward NZE 2050 looks achievable.

**Central case:** CCUS operational capacity reaches 250–350 Mt/yr by 2030. About half the announced pipeline materializes. The Norwegian/UK/EU hub model proves successful but expensive. US deployment is significant but mostly EOR-coupled. Power-sector CCUS remains marginal. The trajectory falls short of NZE but is sustained at modest scale.

**Pessimistic case:** CCUS operational capacity reaches 150–250 Mt/yr by 2030. Several large projects fail or are cancelled (ExxonMobil Baytown is the harbinger). Cost reductions don't materialize. Political opposition (from both climate hawks and fossil fuel allies) erodes funding. The technology persists but at much smaller scale than scenarios envisioned.

The actual outcome depends on policy, project execution, technology cost trajectory, and the broader climate-policy political environment. The 2025–2026 period (with major project FIDs, US policy shifts, the EU 2026 reform) is more consequential than any prior CCUS period.

## **Stop-and-check 10.F**

1. The "central case" 2030 outcome has CCUS deploying at 250–350 Mt/yr — significant absolute scale but far below NZE requirements. What does this imply about how 1.5°C-compatible pathways need to be structured?
2. The hub-and-spoke model (Northern Lights, Porthos, East Coast Cluster) bundles capture from multiple emitters with shared transport and storage. What's the advantage over project-by-project CCS?
3. The Trump administration has not so far attacked 45Q despite broader climate skepticism. What does this say about the political coalition supporting CCUS?
4. **Socratic prompt:** If you were a climate-focused VC in 2026, which CCUS investment opportunities would you find most attractive — equity in capture-technology companies, infrastructure equity in hubs, project finance for individual capture projects, or advance market commitments for high-quality credits? Defend your choice.

**Answers**

1. It implies that 1.5°C-compatible pathways cannot lean on CCUS as a primary lever during this decade. If CCUS realistically reaches only 250–350 Mt/yr against the ~1,000 Mt/yr NZE need by 2030, the bulk of near-term abatement must come from direct decarbonization — renewables, electrification, efficiency — with CCUS reserved for the hard-to-abate residual. Pathways should treat CCUS as a targeted tool for sectors with no alternative (cement, steel, some chemicals) rather than a license to sustain fossil use, and should not bank on capture volumes the deployment record does not support.

2. Hub-and-spoke pools capture demand from multiple emitters across shared transport and storage, which solves the coordination and infrastructure-mismatch problems that stall standalone projects. A single emitter often cannot justify building dedicated pipeline or storage; bundling several spreads the large fixed costs of transport and the storage site across many tonnes, lowering per-ton cost and unlocking storage access for emitters without local geology. It also concentrates the regulatory, MRV, and liability burden in one professionalized operator rather than replicating it project by project.

3. It suggests the CCUS coalition is bipartisan and constituency-driven rather than ideological. 45Q has sponsors across the aisle (Capito, Whitehouse) and a strong industry base — oil, gas, and heavy industry — that benefits regardless of climate framing, partly because the EOR pathway aligns with fossil interests. So even an administration hostile to climate policy broadly leaves 45Q intact: it functions as industrial and energy-sector support, not just climate policy, which insulates it politically in a way that, say, renewable mandates are not.

4. A defensible choice is infrastructure equity in hubs. Transport-and-storage hubs are the chapter's identified breakthrough and behave like regulated utility assets: long-lived, with contracted throughput from multiple emitters and often public or CfD-backed revenue, which diversifies away single-project execution risk. Capture-technology equity offers higher upside but binary outcomes; individual project finance concentrates execution and policy risk; AMCs suit buyers, not investors. The decisive variables are your risk tolerance and time horizon — a VC seeking durable, de-risked cash flows favors hubs; one seeking venture-scale returns favors capture-tech equity.

---

# Closing exercise

Three things to take away:

**1. CCUS deployment has been slower than scenarios envisioned but is accelerating.** Operational capacity 50 Mt/yr in 2025; announced pipeline ~430 Mt/yr by 2030 (with realistic realization ~250–350 Mt/yr). The gap to NZE 2030 requirements (~1,000 Mt/yr) is large. Most operational capacity is at low-cost gas-processing facilities; the climate-meaningful deployment in cement, steel, and DAC is just beginning.

**2. Hub-based infrastructure is the breakthrough.** Northern Lights, the East Coast Cluster, Porthos, Pathways, Stratos. These shared-infrastructure projects pool demand, unlock storage access, and reduce per-ton costs. The 2025 commercial start of Northern Lights is the most important institutional moment in CCUS history.

**3. CCUS is necessary but not sufficient.** For some sectors (cement, steel, certain chemicals, certain refineries, possibly some power) it's essential. For other sectors (most power, transportation, buildings) it's likely the wrong tool. The next decade will sort which applications work and which don't.

The chapters that follow build on CCUS:
- Chapter 11 dives deeper into direct air capture and the full CDR portfolio.
- Chapter 12 covers hard-to-abate sectors where CCUS is most necessary.
- Chapter 13 covers how corporates use CCUS purchases in net-zero claims.

---

# What this chapter simplified

**1. The deep chemistry of capture solvents.** Amine chemistry, solvent degradation, regeneration energy requirements, novel solvents (Allam-Fetvedt cycle, calcium looping, etc.) — these are technical literatures I covered only at the surface. For project-level analysis, the solvent choice and regeneration approach matter enormously.

**2. The storage geology.** I described saline aquifers and depleted reservoirs briefly. The actual reservoir engineering — caprock integrity assessment, plume migration modeling, induced seismicity, well construction standards — is substantial subsurface engineering work that doesn't translate easily to summary form.

**3. The China story.** Chinese CCUS deployment is less well-documented in English-language databases than Western projects. Estimates of capacity and project status carry more uncertainty than I conveyed. The strategic dimensions (China as future CCS technology exporter) deserve more space than I gave them.

**4. The regulatory framework detail.** EPA UIC Class VI rules, EU Storage Directive, Canada's regulatory framework, Norway's framework — each has substantial substantive content that affects project economics and risk allocation. I summarized this; the underlying detail matters for project developers and investors.

**5. The 45Q project finance mechanics.** 45Q's interaction with project finance (tax equity, transfer markets, direct pay) is itself a substantial sub-literature. The simplest version: $85/tCO₂ tax credit for sequestered CO₂, monetizable through direct pay or transferability under IRA. The actual mechanics involve substantial financial structuring.

**6. The international politics of CCUS standards.** What counts as "permanent storage"? What MRV requirements are sufficient? These have substantial implications for credit issuance, Article 6 compatibility, and project economics. I touched on these without deep coverage.

---

# Glossary delta (Chapter 10)

- **Amine** — Class of chemicals (monoethanolamine MEA, methyldiethanolamine MDEA, proprietary blends) used as solvents in post-combustion CCUS to selectively bind CO₂.
- **BECCS (Bioenergy with Carbon Capture and Storage)** — Burning biomass and capturing the resulting CO₂. Treated as net-negative emissions because biomass carbon was recently atmospheric. Covered in Ch. 11.
- **Boundary Dam** — Saskatchewan coal-fired power plant with post-combustion CCS, operational since 2014. World's first commercial coal-power CCS.
- **Brevik Cement** — Heidelberg Materials' cement plant in Norway with CCS operational 2025; world's first commercial cement CCS.
- **CCS-CfD (Carbon Capture and Storage Contracts for Difference)** — UK policy providing revenue certainty to CCUS projects via difference between strike price and carbon price.
- **Class VI well (UIC)** — EPA's Underground Injection Control regulation category specifically for CO₂ geological sequestration wells in the US.
- **Direct pay** — IRA provision allowing certain entities to receive 45Q tax credit value as direct cash payment rather than tax offset.
- **East Coast Cluster** — UK's largest planned CCS hub, on the north-east coast of England.
- **EOR (Enhanced Oil Recovery)** — Use of CO₂ to extract additional oil from operating fields. Most CCUS capacity historically.
- **FEED (Front-End Engineering Design)** — Project development stage where engineering design is fully developed; precedes FID.
- **FID (Final Investment Decision)** — Project development stage where capital commitment is made. The decisive moment.
- **Gorgon** — Chevron's Australian LNG project with CCS, operational since 2019.
- **Hub-and-spoke model** — Shared CCS infrastructure linking multiple capture facilities to common transport and storage. Northern Lights, East Coast Cluster, Porthos are examples.
- **Innovation Fund (EU)** — EU funding mechanism for innovative low-carbon technologies; ~€38 billion through 2030 from ETS revenues.
- **Longship** — Norwegian government's flagship CCS funding program supporting Northern Lights and Brevik.
- **Moomba CCS** — Australian project at Santos's Moomba gas processing facility; operational October 2024. ~$30/tCO₂ cost — among the lowest globally.
- **MRV (Monitoring, Reporting, Verification)** — The processes for confirming stored CO₂ stays stored. Critical for credit issuance and regulatory compliance.
- **Northern Lights** — Norwegian CCS hub; cross-border CO₂ shipping. Phase 1 operational August 2025 (1.5 Mt/yr); Phase 2 expansion to 5 Mt/yr by 2028.
- **NZE (Net Zero Emissions) scenario** — IEA's normative scenario consistent with 1.5°C; suggests CCUS at ~1,000 Mt/yr by 2030 and ~6,000 Mt/yr by 2050.
- **Oxy-fuel combustion** — Burning fuel in pure oxygen rather than air, producing flue gas that's nearly pure CO₂.
- **Petrobras Santos Basin Pre-Salt** — Brazil's CCS-EOR project; world's largest operational CCS facility (~10.6 Mt/yr).
- **Post-combustion capture** — CCUS approach capturing CO₂ from flue gas after combustion. Most widely-applicable approach.
- **Pre-combustion capture** — CCUS approach capturing CO₂ before combustion, typically by converting fuel to hydrogen plus CO₂.
- **Quest** — Shell's Canadian CCS project at Scotford hydrogen production facility; operational since 2015.
- **Saline aquifer** — Porous rock formation containing brine water (not usable for drinking). The dominant CCUS storage type for new projects.
- **Sleipner** — Norway's CCS pioneer; operational since 1996. The world's first commercial CCS project.
- **Snøhvit** — Companion Norwegian project to Sleipner, operational since 2008.
- **Stratos** — Occidental's DAC facility in Texas; Phase 1 operations from 2026 (ramping). World's largest direct air capture facility (500 ktCO₂/yr design).
- **Tangguh** — Indonesia LNG facility with CCS reaching FID 2024; one of the largest CCS FIDs ever.
- **TIER (Technology Innovation and Emissions Reduction) regulation** — Alberta's carbon-pricing system for large industrial emitters; includes credits for CCUS.

---

# Sources and currency

This chapter cites figures that are current as of writing (May 2026) and will move. The most time-sensitive claims, to be re-verified against primary sources and tracked via `CHANGELOG.md`:

| Claim | Value as stated | As-of | Primary source to verify against |
|---|---|---|---|
| Global operational CCUS capacity | ~50 Mt/yr (up from 47.4 Mt/yr) | Q1 2025 | IEA CCUS Projects Database 2025 |
| Number of operational facilities / industries | ~79 facilities across 9 industries | Q1 2025 | IEA CCUS Projects Database 2025 |
| Project pipeline capture capacity by 2030 | ~430 Mt/yr (if all announced projects proceed) | Q1 2025 | IEA CCUS Projects Database 2025 |
| Storage capacity by 2030 | ~670 Mt/yr | Q1 2025 | IEA CCUS Projects Database 2025 |
| Projects in global pipeline | 628 projects (+60% since 2023) | Q1 2025 | IEA CCUS Projects Database 2025 |
| Projects at FEED stage | 247 (more than double 2023 levels) | Q1 2025 | IEA CCUS Projects Database 2025 |
| CCUS investment 2024 | ~$6.4 billion (tripled since 2022) | 2024 | IEA CCUS Projects Database 2025 |
| NZE CCUS requirement 2030 | ~1,024 Mt/yr | 2021/2023 NZE | IEA Net Zero Roadmap (2021 NZE; 2023 update revises to ~1,000 Mt/yr) |
| NZE CCUS requirement 2050 | ~6,040 Mt/yr | 2021/2023 NZE | IEA Net Zero Roadmap (2023 update: >6 Gt/yr) |
| Boundary Dam cumulative capture | ~7.1 Mt cumulative since 2014 (annual ~700–790 ktCO₂/yr, below ~1 Mt/yr design) | Sept 2025 | SaskPower disclosures |
| Gorgon cumulative injection vs. design | ~10.5 Mt through 2024 vs. ~17 Mt design | 2024 | IEEFA / Chevron Australia disclosures; Rigzone Nov 2024 |
| Petrobras Santos Basin capacity | ~10.6 Mt/yr (design/nameplate; 2024 actual ~14.2 Mt) | 2024 | Petrobras operator disclosures; gasworld; Offshore Energy |
| Norway CO2 tax current rate | NOK 952/tCO₂ (~$95) | 2023 (mineral oil general rate) — NOTE: 2025 petroleum-sector rate is NOK 944/tCO₂; verify before re-print | Norskpetroleum.no; Norwegian Tax Administration |
| Norway CO2 tax 2030 target | NOK 2,000/tCO₂ (~$220) | 2020-prices basis; NOK 2,400 in 2025 prices | Norwegian Government Prop. 1 LS (2024–2025) |
| China operational CCUS capacity | ~5 Mt/yr | end-2024 | IEA CCUS Projects Database 2025 (Chinese data carries higher uncertainty) |
| Northern Lights EU funding | €131 million | 2024 | European Commission / Connecting Europe Facility; norlights.com |

---

# What's next

CCUS is the technology platform; CDR is the next frontier. Chapter 11 picks up where this chapter leaves off:

- **Direct air capture (DAC)** at scale.
- **BECCS** in detail.
- **Enhanced rock weathering** (peridotite mineralization, basalt mineralization).
- **Ocean-based CDR** — alkalinity enhancement, OAE, blue carbon.
- **Biochar and biomass burial**.
- **The 1.5°C-compatible gigaton-scale removal challenge.**

Chapter 12 then covers the hard-to-abate sectors (steel, cement, aviation, shipping, chemicals) where these technologies have to deploy.

