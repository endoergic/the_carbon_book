# Chapter 8 — Voluntary Carbon Markets

**Track:** Climate Liability (B)
**Prerequisites:** Chapter 5 (avoided/reduced/removed distinction), Chapter 6 (CDM as VCM ancestor), Chapter 7 (compliance markets for contrast).
**What you should be able to do by the end:**
- Explain the difference between voluntary and compliance carbon markets, including who buys credits, who issues them, and what claims credits enable.
- Identify the major voluntary carbon market standards (Verra/VCS, Gold Standard, ART/TREES, ACR, CAR, Isometric, Puro.earth, Plan Vivo) and what each is known for.
- Walk through the project-credit lifecycle: methodology, project design, validation, monitoring, verification, registry issuance, retirement.
- Articulate the four core integrity concerns: additionality, baseline, permanence, leakage — and how each fails in real projects.
- Tell the story of the 2022–2024 voluntary market crisis: the Guardian/Die Zeit/SourceMaterial investigation, REDD+ baseline collapse, supply-side reforms (ICVCM Core Carbon Principles), and demand-side reforms (VCMI Claims Code, SBTi V2's removal requirements).
- Distinguish between project categories (NBS vs. engineered removal vs. avoidance vs. cookstove), why prices differ enormously across them, and what each is most useful for.
- Read current voluntary market price tiers and explain why a "carbon credit" can cost anywhere from $1 to $1,500+/tCO₂e.
- Discuss the ongoing tension between scaling the market (more credits, more capital flow to projects) and improving quality (higher standards, fewer credits at higher prices) — and the reform proposals that try to do both.

---

## Why this chapter exists

The voluntary carbon market (VCM) is the most controversial part of the carbon-policy landscape. It's small in absolute terms — total VCM transactions in 2024 were roughly **$1.5–2 billion**, less than 1% of the EU ETS's annual revenue — but it punches above its weight in public attention, corporate climate strategy, and regulatory scrutiny. Most major climate-skeptical journalism over the past three years has been about VCM failures. Most major corporate net-zero scandals have involved VCM credits. The integrity questions in the VCM are the integrity questions everyone is talking about.

This is also the area where the most fundamental analytical questions live. **Can offsets work at all?** Can a market mechanism substitute reductions in one place for reductions somewhere else without introducing systematic gaming? Can projects designed to "avoid" deforestation actually demonstrate they did so? Can baselines (counterfactual emissions scenarios) be verified well enough to prevent manipulation? These questions aren't fully resolved — and they probably won't be, in the sense that some kinds of offsets seem more verifiable than others, and the policy community is in the middle of working out which are which.

This chapter takes a position: the voluntary market has had real and serious integrity problems, and the 2022–2024 reform movement is a genuine effort to address them. The reforms are partial and ongoing; whether they will produce a credibly high-integrity market or whether the structural problems are too deep is genuinely undetermined as of mid-2026.

I'll organize this in eight parts: VCM fundamentals and how it differs from compliance markets; the project lifecycle and the four core integrity concerns; the major standards and what each specializes in; the 2022–2024 crisis; the supply-side reform (ICVCM and Core Carbon Principles); the demand-side reform (VCMI Claims Code, SBTi V2, ISSB rules); the current state of prices, demand, and the unresolved questions; and fuel-based credits and the additionality inversion.

---

# Part 1: What the voluntary carbon market is

## The basic transaction

A **carbon credit** is a tradable instrument representing one ton of CO₂-equivalent reduced, avoided, or removed from the atmosphere by a specific project. Credits are issued by **standards** (Verra, Gold Standard, etc.) after a project has been validated, implemented, monitored, and verified. They live in **registries** until they are **retired** — permanently canceled — by a buyer who claims the credit's climate benefit.

The voluntary market exists because some entities want to make climate claims (carbon neutral, climate positive, etc.) and offsets are one way to "balance" residual emissions. Unlike compliance markets, **no one is legally required to buy or retire voluntary credits**. The market operates entirely on private demand from corporates, foundations, individuals, and (increasingly) governments using credits to meet Paris NDC obligations.

The typical transaction:
1. A project developer identifies a project that will reduce or remove emissions (e.g., conserve a forest, install methane-capture equipment, build a direct air capture facility).
2. The developer designs the project according to a **methodology** approved by one of the standards. The methodology specifies how emissions will be measured, what counts as the baseline, what verification is required, and how credits will be calculated.
3. The project is **validated** by an accredited third-party validation/verification body (VVB).
4. The project is implemented and emissions/removals are **monitored** over the crediting period.
5. The VVB **verifies** the monitoring data and issues a verification report.
6. The standard **issues** credits equal to the verified tons.
7. Credits are traded (via brokers, exchanges, direct sale) until they reach a buyer who **retires** them.
8. The retiring buyer makes a claim — "we have offset X tons" — supported by the retirement record.

The integrity of this entire chain depends on the methodology, the validation, the monitoring, and the verification. When any of these fails, the credits don't represent real climate benefit even though they exist in the registry.

## How VCM differs from compliance markets

| Feature | Compliance Market | Voluntary Market |
|---|---|---|
| Who's required to participate | Covered entities by law | Nobody |
| What's traded | Allowances (right to emit) | Credits (verified reductions/removals) |
| Cap on total credits | Yes (the cap) | No (more projects → more credits) |
| Price discovery | Market within cap | Project-by-project plus market |
| Geographic scope | Jurisdictional | Global |
| Quality of underlying units | Backed by sovereign authority + cap | Backed by standard's methodology + verification |
| Typical price (2025–26) | €70–80 (EU), ~$30 (CA), RGGI ~$13 auction / volatile secondary | $1–1,500+ (depending on type) |

The voluntary market's enormous price range — three orders of magnitude — is the most visible sign that the credits sold under the "carbon credit" label are not homogeneous. A $3 REDD+ credit and a $1,200 DAC credit are both called "1 tCO₂e," but they represent very different physical activities, durabilities, and risk profiles.

## Two markets in one

A useful frame: the voluntary market is really *two* markets operating under shared institutional infrastructure.

**Market A — the "compliance-like" segment** consists of large corporate buyers (Microsoft, Stripe, Google, Salesforce, financial institutions, oil and gas majors) buying credits in significant volume to support net-zero claims. This segment has been the driver of recent price segmentation: buyers in this segment increasingly want high-integrity, durable removal credits at substantial premiums.

**Market B — the "legacy" segment** consists of smaller corporate buyers buying credits for "carbon neutral" claims at low prices — often $3–10/tCO₂e for nature-based avoidance credits. This segment has been the source of most integrity scandals. Many large companies have exited this segment over 2023–2025 as the integrity controversies hit.

The 2022–2024 crisis is primarily a Market B crisis. The reform movement (ICVCM, VCMI, SBTi V2) is trying to shrink Market B and grow Market A.

## **Stop-and-check 8.A**

1. Compliance markets have a cap; the voluntary market does not. Walk through what that single structural difference does to how credits are *priced* and how supply is *constrained*.
2. A "$3 REDD+ credit" and a "$1,200 DAC credit" are both labelled "1 tCO₂e." In what sense is calling them the same unit the conceptual error at the root of most VCM integrity failures?
3. No one is legally required to buy voluntary credits. Given that, what actually creates demand — and why does that make VCM demand more fragile than compliance demand?
4. **Socratic prompt:** The chapter frames the VCM as "two markets in one" — a high-integrity removal segment (Market A) and a legacy avoidance segment (Market B) sharing one infrastructure and one label. Is sharing the "carbon credit" label across both a feature (liquidity, common rails) or a bug (it lets low-integrity credits borrow the credibility of high-integrity ones)?

**Answers**

1. In a compliance market the cap fixes total supply: allowances are scarce by law, and the price is the market clearing that fixed quantity against demand. The voluntary market has no cap — supply is whatever projects get developed and verified — so more demand calls forth more credits rather than bidding up a fixed stock. That means price is set project-by-project (cost of the underlying activity plus a quality premium) rather than by system-wide scarcity, and it removes the floor that a binding cap provides. Without a cap, low-cost project types (cheap avoidance) can flood supply and crater prices, which is exactly what happened to nature-based credits in 2022–2024.

2. Because the label asserts equivalence the physical activities don't have. A DAC credit removes a tonne and stores it for millennia; a $3 REDD+ credit claims a tonne *avoided* against an unobservable counterfactual baseline, with reversal and leakage risk. Treating them as one fungible unit lets a buyer "neutralize" a fossil emission (centuries of atmospheric impact) with a cheap, non-durable, possibly non-additional avoidance credit — a swap that doesn't hold up physically. The three-orders-of-magnitude price range is the market admitting the units aren't the same; the integrity failures come from pretending, for accounting and marketing purposes, that they are.

3. Demand comes almost entirely from *voluntary* corporate climate claims (carbon-neutral and net-zero marketing), plus emerging sovereign Article 6 and CORSIA buying. Because the corporate portion rests on reputational choices rather than legal obligation, it evaporates the moment the reputational calculus flips — which is precisely what happened when the 2023 investigations made "carbon neutral via cheap offsets" a liability rather than an asset, and major buyers exited. Compliance demand is anchored by a legal surrender obligation that doesn't disappear when the news cycle turns; voluntary demand is anchored only by the value of the claim, so it is far more sensitive to scandal, scrutiny, and disclosure rules.

4. It is genuinely both, and the tension is the chapter's through-line. The shared label and infrastructure (registries, methodologies, VVBs, exchanges) give the market liquidity, common standards, and a path for high-integrity supply to scale on existing rails — a real feature. But the same shared label lets a low-integrity avoidance credit present itself as the same "1 tCO₂e" as a durable removal, borrowing the credibility of the good end of the market to sell the weak end — the bug that produced the crisis. The reform architecture (ICVCM labeling, SBTi restricting which credit types neutralize residuals) is essentially an attempt to *keep the shared rails while unbundling the label* — to let buyers tell the two markets apart without forcing them onto entirely separate infrastructure. Whether a single label can carry that much discrimination is the open question.

---

# Part 2: The project lifecycle and the four integrity concerns

To understand how VCM credits go wrong, you have to understand how they're supposed to work.

## The methodology

Every credit-issuing project follows a **methodology** — a standardized document specifying:
- What kind of activity qualifies (e.g., afforestation on previously-deforested land).
- What constitutes the **baseline** (the counterfactual emissions scenario without the project).
- How **additionality** is demonstrated (the project wouldn't have happened without carbon revenue).
- How emissions/removals are **measured and monitored**.
- How **leakage** (emissions displacement to other locations) is accounted for.
- How **permanence** (durability of the storage) is assessed and what buffers/reversal protections are required.
- How credits are **calculated** from monitoring data.

Standards have catalogs of methodologies covering many project types: REDD+ (avoided deforestation), ARR (afforestation/reforestation/revegetation), improved forest management (IFM), grassland management, blue carbon (coastal ecosystems), agricultural soil carbon, biochar, direct air capture, enhanced rock weathering, BECCS, biomass burial, methane capture from landfills, methane capture from cookstoves, fuel switching, renewable energy (now largely deprecated), waste handling, etc.

The methodology is the technical heart of the credit. A weak methodology produces credits that don't represent real climate benefit, even if all the project's monitoring is done correctly. A strong methodology produces credits that survive third-party scrutiny.

## The four integrity concerns

Four conceptual integrity tests have to be passed for a credit to represent real climate benefit:

### 1. Additionality

**Definition:** Would the project's emissions reductions have happened anyway, in the absence of carbon revenue?

A project that would have been built regardless (a wind farm in a market where wind is already economic, a forest protection that would have happened under existing law) is **not additional**. Issuing credits for non-additional activities just rewards what would have happened anyway — no climate benefit is created.

**Why it's hard:** Additionality is inherently counterfactual. You can't observe what would have happened. Standards try to demonstrate additionality through several tests: financial additionality (was the project economic without credit revenue?), regulatory additionality (was it required by law?), barrier analysis (were there non-financial barriers carbon finance helped overcome?), common-practice analysis (is this type of project unusual in this jurisdiction?).

**Where it fails:** Renewable energy credits in markets where renewables are cost-competitive. Forest protection projects in legally-protected areas. Methane capture at landfills where capture is required or economic on its own. The CDM had widely-documented additionality failures (Ch. 6); the VCM has inherited and extended these.

### 2. Baseline

**Definition:** What would emissions have been without the project? This is the counterfactual against which reductions/removals are measured.

For a REDD+ project: how much deforestation would have occurred on this land if the project didn't exist? The credits issued equal the difference between this counterfactual and observed deforestation.

**Why it's hard:** Baselines are projections, not observations. Different baseline methodologies produce very different numbers — often by factors of 2–10×. Project developers have strong incentives to overstate baselines (more deforestation projected → more credits issued). The verification community has incentives to defer to project developers' methodological choices.

**Where it fails:** Spectacularly in REDD+. The 2023 Guardian/Die Zeit/SourceMaterial investigation (based on three peer-reviewed studies by West et al. 2020/2023 and others) found that 94% of audited Verra REDD+ credits had baselines that overstated deforestation by an average of ~400% — sometimes much more. Some projects' baselines projected catastrophic deforestation that had no historical or geographic precedent.

### 3. Permanence

**Definition:** Will the emissions reduction/removal stay reduced/removed? For how long?

Burning fossil fuels releases CO₂ that affects the atmosphere for centuries to millennia. To genuinely "neutralize" such an emission, you need durable storage at a similar timescale. A forest that gets re-burned in a wildfire ten years later has not durably stored carbon.

**Why it's hard:** Forests, soils, and biological systems can lose stored carbon to wildfires, pests, droughts, land-use change, and policy reversal. Geological storage (DAC, BECCS) is more durable but is much more expensive and limited in scale. Most standards use **buffer pools** — reserved credits held back from issuance to compensate for reversals — but the buffer pool sizes are based on historical experience that may not predict future reversal rates as climate changes.

**Where it fails:** Wildfire-driven reversal in California IFM projects (especially 2020–2024). Conversion of REDD+ lands after project conclusion. Soil-carbon projects with poor tillage maintenance. The basic question of whether 100-year buffer arrangements are adequate when projects are claiming benefits supposed to neutralize emissions affecting the atmosphere for 1,000+ years.

### 4. Leakage

**Definition:** Did the project's emission reductions get displaced elsewhere? If a REDD+ project saves 1,000 hectares of forest but the deforestation pressure simply moves to a neighboring 1,000 hectares, the net climate benefit is zero or negative.

**Why it's hard:** Leakage can happen at multiple scales — local (next county), regional, national, international. Standards typically apply discount factors to claimed reductions to account for leakage, but the appropriate discount rate is genuinely uncertain. A national-scale REDD+ program might leak internationally (deforestation pressure moves to a different country); a project-scale REDD+ project might leak nationally.

**Where it fails:** Project-scale REDD+ has been credibly accused of substantial leakage. Some studies estimate effective leakage rates of 50–80% — meaning a project that "avoided" 1,000 tCO₂ of deforestation only avoided 200–500 tCO₂ on net. The jurisdictional REDD+ approach (ART/TREES) was developed partly to address this problem by working at the national/sub-national scale.

## How the four failures combine

A project can fail one, two, three, or all four tests. The 2022–2024 REDD+ crisis involved widespread failures of additionality (projects in low-deforestation areas), baseline (overstated by 4×+ on average), permanence (forest loss post-issuance), and leakage (regional displacement). It's the convergence of all four problems that produced the headline finding that "90% of REDD+ credits are worthless."

Other project types fail differently:
- **Renewable energy credits:** Primarily additionality failures (the project would have been built anyway).
- **HFC destruction:** Largely additional and durable (the gas is destroyed), but historically had perverse incentives (CDM era).
- **DAC and engineered removals:** Strong on permanence and additionality (without revenue, these projects don't exist); weaker on baseline (what's the counterfactual for a removal? Generally zero, which is straightforward).
- **Biochar:** Strong on additionality and durability (centuries); weaker on baseline (what would the feedstock have done without biochar conversion?).
- **Improved forest management:** Mixed on all four.

The "carbon credit" label hides enormous variation in which tests projects pass.

## **Stop-and-check 8.B**

1. Why is additionality "inherently counterfactual" — and what does this imply about how well any verification system can prove additionality?
2. The 2023 Guardian investigation found that REDD+ baselines on average overstated deforestation by 400%. If baselines were tighter, would the credits be smaller or more credible? What's the trade-off?
3. Permanence: a forest stores 100 tCO₂ for 50 years then burns. How does this compare climatically to never having stored the 100 tCO₂?
4. **Socratic prompt:** If you had to pick one of the four integrity tests as the most consequential, which would you pick and why? Make a case.

**Answers**

1. Additionality is counterfactual because it asks what would have happened without carbon revenue — a scenario that, by definition, did not occur and cannot be observed. You only ever see the world in which the project was built; the alternative world is a construction. Standards substitute proxies — financial, regulatory, barrier, and common-practice tests — but each is an inference, not a measurement, and each is open to dispute. The implication is that no verification system can prove additionality; it can only build a more or less plausible case. That irreducible uncertainty is why additionality failures (renewables that were already economic, forests already protected by law) recur across both the CDM and the VCM.

2. Tighter baselines would make the credits both smaller and more credible — fewer tons would be issued, but each issued ton would more honestly reflect avoided deforestation. The trade-off is between volume and integrity: project developers earn from the gap between projected and observed deforestation, so a conservative baseline cuts issuance and revenue, weakening the financial incentive to develop projects at all. The 400% average overstatement shows how far the prior baselines had drifted toward volume over honesty. Tightening corrects the integrity problem but shrinks the market and the financing flowing to genuine conservation — which is the core tension between scaling the market and improving its quality.

3. Storing 100 tCO₂ for 50 years and then releasing it is climatically much better than never storing it, but it is not equivalent to a permanent removal. For those 50 years the carbon was out of the atmosphere, delaying warming and its compounding damages; that delay has real value. But once the forest burns, the 100 tCO₂ returns, and the original fossil emission it was meant to "neutralize" affects the atmosphere for centuries to millennia. So temporary storage buys time, not cancellation. Treating a 50-year store as if it offsets a multi-century emission — the way many "carbon neutral" claims did — overstates the benefit; the timescales do not match.

4. A defensible pick is the baseline, because it is the quantity that determines how many credits exist, and the 2022–2024 crisis showed it failing most spectacularly — REDD+ baselines overstated deforestation by ~400% on average, manufacturing tons that never corresponded to real avoidance. A baseline error multiplies directly into issued volume regardless of how well the other tests are passed. One could equally argue for additionality, since a non-additional project produces zero real benefit no matter how tight its baseline, or for permanence, since a reversed removal undoes the entire claim. The strongest case names the test whose failure most directly inflates issuance at scale: in the historical record, that has been the baseline.

---

# Part 3: The major standards

The voluntary carbon market has multiple competing standards. Each has its specialty, methodology catalog, and integrity reputation.

## Verra (Verified Carbon Standard, VCS)

**Founded:** 2005, originally as the "Voluntary Carbon Standard." Now the largest VCM standard by far.

**Scope:** All project types. Largest catalog of methodologies.

**Market share:** ~70% of voluntary credits issued historically. Approximately 1 billion credits issued cumulatively.

**Reputation:** Largest, most institutionally embedded, but most exposed to integrity controversies. The 2023 Guardian investigation centered on Verra REDD+ credits. Verra's response — strongly contesting the methodology critiques, then ultimately revising its REDD+ approach — has been controversial.

**Major methodology changes 2023–2025:**
- **VM0048** (consolidated REDD+ methodology) — replaces VM0006, VM0007, VM0009, VM0010, VM0015, VM0037, with stricter baseline rules using jurisdictional baseline frameworks.
- **VM0047** (ARR methodology) — first ARR methodology to receive CCP label (December 2024).
- **JNR Framework v4.1** — jurisdictional REDD+ framework allowing project-level activities to nest within national/sub-national baselines.

**ICVCM status (mid-2026):** CCP-Eligible (May 2024). Some VCS methodologies have received CCP-approved label; others under review.

## Gold Standard

**Founded:** 2003, by WWF and other NGOs. Originally focused on CDM project quality.

**Scope:** All project types, with particular strength in cookstoves, renewable energy (historically), water benefits, and community-focused projects.

**Reputation:** Generally considered higher-integrity than Verra historically. Stronger NGO governance. Smaller scale.

**ICVCM status:** CCP-Eligible (May 2024). Several Gold Standard methodologies have received CCP approval.

## ART (Architecture for REDD+ Transactions)

**Founded:** 2018 by Winrock International.

**Scope:** Jurisdictional REDD+ only. Operates the TREES methodology (REDD+ Environmental Excellence Standard).

**Distinctive feature:** Jurisdictional approach — entire countries or sub-national regions can register baselines, with credits issued for emissions below the jurisdictional baseline. Eliminates project-scale leakage. Allows alignment with Paris Article 6.

**Reputation:** High integrity, with strict eligibility (only countries/jurisdictions can register, with substantial governance requirements). Smaller volume than project-scale REDD+.

**ICVCM status:** CCP-Eligible (May 2024).

## ACR (American Carbon Registry)

**Founded:** 1996 (the original VCM registry, predating Verra). Operated by Winrock International.

**Scope:** US-focused, with particular strength in industrial gas destruction (HFCs, methane), agricultural soil carbon, and improved forest management.

**Reputation:** Strong US institutional integration. Approved as compliance offset registry for California Cap-and-Invest.

**ICVCM status:** CCP-Eligible (early 2024).

## CAR (Climate Action Reserve)

**Founded:** 2001 (California-based).

**Scope:** US and Mexico-focused, with particular strength in methane projects (landfills, manure, coal mines).

**Reputation:** Strong technical methodology development, especially in methane. Approved as compliance offset registry for California Cap-and-Invest.

**ICVCM status:** CCP-Eligible (early 2024).

## Isometric

**Founded:** 2022.

**Scope:** Carbon dioxide removal (CDR) only — engineered and high-durability removals (DAC, BECCS, biochar, enhanced rock weathering, ocean alkalinity, mineralization, etc.).

**Distinctive feature:** Designed specifically for engineered removals at high durability standards (1,000+ year storage). Open-source science approach. Strict additionality and verification requirements.

**Reputation:** New, but high-integrity by design. Backed by Stripe, Shopify, and other large CDR buyers.

**ICVCM status:** CCP-Eligible (December 2024).

## Puro.earth

**Founded:** 2019, originally by Fortum (Finnish utility). Now majority-owned by Nasdaq.

**Scope:** Net-CO₂-removal only. Methodologies for biochar, enhanced rock weathering, geologically-stored BECCS, ocean-based CDR, mineralization, woody biomass carbon storage.

**Reputation:** Pioneer in engineered removals. Smaller scale but growing fast.

**ICVCM status:** Under assessment.

## Plan Vivo

**Founded:** 1994 (the original community-focused carbon standard).

**Scope:** Smallholder forestry, agroforestry, ecosystem-based projects with strong community benefits emphasis.

**Reputation:** Smallest of the major standards but strongest community-focus.

## CORSIA-eligible standards

The **Carbon Offsetting and Reduction Scheme for International Aviation (CORSIA)** — ICAO's compliance scheme for international airline emissions — accepts credits from approved standards. ICAO's Technical Advisory Body has approved a subset of standards' methodologies for CORSIA eligibility. This creates a compliance demand stream that operates alongside voluntary demand.

## The CCP-Eligible programs

The **Integrity Council for the Voluntary Carbon Market (ICVCM)** announced in 2024 that six carbon-crediting programs met its **Core Carbon Principles (CCPs)** integrity benchmark: ACR, ART, CAR, Gold Standard, Verra/VCS, and Isometric. These programs together represent ~98% of VCM market share. Puro.earth and others remain under assessment.

CCP-Eligibility is the first stage. The ICVCM then assesses individual methodologies — some methodologies from CCP-Eligible programs get CCP-Approved status, others don't. As of October 2025, approximately 51 million credits had been issued under CCP-Approved methodologies (representing ~4% of 2024 market volume), with hundreds of millions more expected.

## **Stop-and-check 8.C**

1. Multiple standards (Verra, Gold Standard, ACR, CAR, ART, Isometric, Puro.earth, Plan Vivo) compete for the same project developers. In a market where the *standard* is paid (indirectly) by the projects it certifies, what's the structural risk — and what does it have in common with credit-rating agencies before 2008?
2. ICVCM sits *above* the standards as a "standard for standards." Why was a meta-layer needed — why couldn't competition among the existing standards produce high integrity on its own?
3. Verra holds ~70% market share and was the focus of the 2023 REDD+ investigation, while newer entrants (Isometric, Puro.earth) are removal-only and "high-integrity by design." Why might a smaller, narrower, newer standard be structurally better-positioned on integrity than the dominant incumbent?
4. **Socratic prompt:** ICVCM's CCP label is itself voluntary and has no enforcement power — it works only if buyers prefer labeled credits. Is a privately-run "standard for standards" with no statutory authority a credible long-term fix for VCM integrity, or a placeholder until real financial regulators (SEC, ESMA) step in?

**Answers**

1. The structural risk is issuer-pays conflict of interest: a standard competing for the developers whose projects (and fees) sustain it has an incentive to keep methodologies generous, because a developer can take its volume to a laxer competitor. That is precisely the dynamic that corrupted credit-rating agencies before 2008 — issuers shopped for the agency that would rate their structured products AAA, and the agencies, paid by issuers, obliged. In carbon markets the "rating" is the methodology's leniency on baselines and additionality, and a race-to-the-bottom among issuer-paid standards is the natural failure mode. It is a major reason the 2022–2024 crisis concentrated in the largest, most developer-facing standard.

2. Because competition among issuer-paid standards pushes toward leniency, not rigor — the opposite of what integrity requires. If buyers can't easily tell a strict standard from a lax one (and pre-crisis they mostly couldn't, since every credit said "1 tCO₂e"), then the cheaper, easier-to-certify credit wins on price, rewarding the laxest standard. A meta-layer (ICVCM) was needed to create a quality signal *above* the competing standards — a common benchmark (the CCPs) that lets buyers distinguish integrity, so that demand can reward rigor instead of leniency. It's an attempt to convert a race-to-the-bottom into a race-to-the-CCP-label by giving the quality difference a name buyers can price.

3. Several structural reasons. A removal-only standard sidesteps the hardest integrity problem in the market — the unobservable avoidance counterfactual — because removals have a near-zero, easily-defined baseline and physically-measurable storage. A newer standard carries no legacy book of weak credits to defend, so it has no incentive to rationalize past methodologies (Verra had to defend a billion issued credits). And a smaller, narrower scope lets it hold a single high bar rather than maintain a sprawling catalog across every project type. Incumbency in this market is partly a liability: scale brings a legacy portfolio, developer relationships, and reputational stakes that all pull against tightening.

4. There's a real case it's a credible long-term fix *and* a real case it's a placeholder, and the honest answer hinges on whether buyer demand for integrity persists. The case for durability: the VCM is voluntary by nature, so a buyer-driven quality signal is the native enforcement mechanism — if premium buyers (Microsoft, Frontier, sovereign Article 6 purchasers) keep paying up for CCP-labeled and durable credits, a private meta-standard backed by disclosure rules (IFRS S2) can discipline the market without statute. The case for placeholder: a body with no subpoena power, funded within the ecosystem it polices, depending on voluntary demand that evaporates in a downturn, looks fragile — and the December 2024 internal dissent over REDD+ approvals showed it can be captured or split. The likely trajectory is hybrid: ICVCM-style labeling becomes the technical substrate that statutory regulators (and Article 6 governance) eventually lean on, much as accounting standards bodies feed securities regulation. Private standard-setting and public enforcement converge rather than one replacing the other.

---

# Part 4: The 2022–2024 crisis

The voluntary carbon market had been growing rapidly through 2020–2022 as corporate net-zero commitments multiplied. Market volume grew from ~100 MtCO₂e/yr issued in 2017 to ~250 MtCO₂e/yr in 2022. The market was projected to reach $10–50 billion by 2030.

Then it cratered.

## The Guardian/Die Zeit/SourceMaterial investigation (January 2023)

In January 2023, three news organizations published a joint investigation — the result of nine months of work — concluding that **more than 90% of rainforest carbon offsets** issued by Verra (the largest VCM standard) were "worthless." The investigation drew on three peer-reviewed academic studies:

- **West et al. (2020)** — "Overstated carbon emission reductions from voluntary REDD+ projects in the Brazilian Amazon."
- **Guizar-Coutiño et al. (Cambridge, 2022)** — Examined REDD+ project effectiveness using synthetic control methods.
- **West et al. (2023)** — Systematic synthetic control analysis of 27 REDD+ projects.

The headline findings: REDD+ project baselines on average overstated avoided deforestation by ~400%. Only 8 of the 29 projects examined across the combined investigations showed clear evidence of reduced deforestation. The credits being sold (and retired by buyers like Gucci, Shell, easyJet, Salesforce, Disney, and BHP) didn't represent the climate benefits they claimed.

Verra responded with a strong technical rebuttal disputing the studies' methodology — challenging the synthetic-control approaches used, the matching criteria, the underlying data quality, the lack of peer review of the journalistic claims, and the misrepresentation of one of the cited Cambridge studies (which actually had cautiously positive findings about REDD+).

The academic debate continued. A 2023 rebuttal paper (Mitchard et al.) argued that the West et al. methodology had serious problems and that proper corrections would increase the credible-credit fraction by ~62%. The substantive question — what fraction of REDD+ credits really represent climate benefit — remains contested. The consensus position in 2025–2026 is that **the average integrity is much lower than was claimed by issuers, but better than 0–10%**. Probably 30–50% of legacy REDD+ credits represent some real climate benefit, with wide variation across projects.

## The market reaction

Whatever the precise truth about REDD+ integrity, the market reaction was severe:

- **Nature-based credit prices collapsed.** N-GEO (Nature-based Global Emissions Offset) futures fell from $15+/tCO₂e in mid-2022 to under $1/tCO₂e by mid-2024. The price decline reflected both supply (continued issuance) and collapsing demand.
- **Corporate buyers pulled back.** Major buyers (Shell, Gucci, Disney, Salesforce, others) stopped purchasing nature-based credits or distanced themselves from prior purchases. Some quietly removed "carbon neutral" claims from products.
- **Net-zero pledges restructured.** SBTi tightened its rules on use of offsets in net-zero claims. Corporate climate strategies shifted from "buy credits to offset" toward "invest in direct emissions reduction with high-quality removals for residuals."
- **Voluntary market issuance growth stalled.** 2024 issuance was approximately flat with 2022 levels, breaking the prior growth trajectory.

## Other 2023–2024 controversies

The REDD+ crisis was the most prominent, but several other controversies hit in parallel:

**The cookstove crisis (2023–2024).** Multiple academic studies (notably Gill-Wiehl et al. 2024, Berkeley) found that cookstove credits — projects distributing efficient stoves in developing countries, generating credits from reduced firewood emissions — had been over-credited by 5–10× on average. The methodologies systematically overstated baseline firewood use and understated fuel-switching behavior. Verra and Gold Standard issued substantial methodology revisions in 2024–2025.

**Wildfire reversals.** A series of major wildfires in California IFM projects (most prominently the 2020 Lionshead Fire affecting Warm Springs forest projects, and 2023 wildfires affecting Massachusetts and California IFM projects) tested buffer pool mechanisms. The buffer pools generally held — meaning replacement credits were issued from reserves — but the reversal rate was uncomfortably close to buffer adequacy thresholds.

**Renewable energy credits being phased out.** ICVCM ruled in late 2024 that legacy renewable energy methodologies do not meet CCP standards. New renewable-energy methodologies focused on contexts where renewables are genuinely additional (e.g., emerging markets) are being developed. The shift effectively removed a major historical category of credit issuance.

**The Cambodia REDD+ situation.** A major REDD+ project (Southern Cardamom REDD+ in Cambodia) was suspended by Verra in mid-2023 amid documented community-rights violations and credible claims that project guards had committed abuses against indigenous communities. The case raised broader questions about whether community-rights safeguards in REDD+ are adequately enforced.

## The reform response

The 2022–2024 crisis catalyzed a reform movement that has been working through 2023–2026. There are two parallel tracks:

**Supply-side reform** — improving the quality of credits issued. Led by **ICVCM**.

**Demand-side reform** — improving the quality of claims buyers can make based on credits. Led by **VCMI** and **SBTi**.

These run in parallel and are designed to be complementary.

## **Stop-and-check 8.D**

1. The Guardian investigation said "more than 90%" of REDD+ credits were worthless. The academic debate suggests the overstated fraction is probably more like 50–70% (i.e., ~30–50% represent real benefit). Is this a meaningful distinction? Does it change how a corporate buyer should treat their existing credit portfolio?
2. The cookstove crisis involved methodologies that systematically overstated baselines. How does this kind of methodological failure differ from the REDD+ case?
3. The 2024 ICVCM rejection of legacy renewable-energy methodologies effectively removed a major historical category of credits from CCP eligibility. What does this say about the legitimacy of the credits that were sold under those methodologies historically?
4. **Socratic prompt:** A company bought 1 million tCO₂e of nature-based credits from Verra projects between 2018–2022. The credits were retired and the company made "carbon neutral" claims at the time. In 2026, the company learns that those credits were likely 30–50% of the climate benefit claimed. What should the company do — disclose, retroactively buy additional credits, change its current strategy, all of the above, or none?

**Answers**

1. The distinction matters less for the headline than for the response. Whether the overstated fraction is 90% or ~50–70% (i.e., ~30–50% real benefit), the operative conclusion is the same: a large share of REDD+ credits did not deliver the claimed benefit, so a portfolio built on them is substantially overstated and any "carbon neutral" claim resting on them is unsupported. Where the distinction does matter is in the remedy and the framing: 30–50% real benefit means the credits were not pure fiction, so a buyer should treat the portfolio as partially valid and discount it rather than write it to zero, and policymakers should reform rather than abolish REDD+. The precise number guides how much to discount and how to fix the methodology, not whether there is a problem.

2. The cookstove failure was a quantification-and-baseline error of a different kind. REDD+ baselines projected a counterfactual deforestation rate that was systematically inflated; cookstove methodologies systematically mis-measured inputs — overstating how much firewood households would have burned and understating fuel-switching behavior — over-crediting by 5–10×. The REDD+ problem was the counterfactual scenario; the cookstove problem was the measurement parameters feeding the credit calculation. Both produce inflated issuance, but the REDD+ case is harder because the counterfactual is irreducibly unobservable, whereas the cookstove parameters can in principle be measured better, which is why methodology revisions in 2024–2025 could address them more directly.

3. It implies those legacy credits were sold under standards that, in hindsight, did not meet a defensible integrity bar — most were non-additional, because renewables were already cost-competitive in many of the markets where the projects were credited. The buyers who retired them and claimed offsets were, in many cases, paying for reductions that would have happened anyway. The retroactive rejection does not automatically void every historical credit, but it signals that the category's legitimacy was weak, and it shifts reputational and disclosure risk onto firms that relied on it. New renewable-energy methodologies survive only by targeting genuinely additional contexts (e.g., emerging markets), which underscores that the old, broad category lacked that discipline.

4. The most defensible course is "all of the above," sequenced. The company should disclose — accurately restating that its past "carbon neutral" claims rested on credits now understood to deliver only 30–50% of the claimed benefit, since continued silence invites greenwashing and litigation risk under emerging disclosure regimes. It should change its current strategy first: prioritize direct decarbonization and shift residual purchases toward high-integrity, durable removals, as SBTi V2 pushes. Retroactively buying additional credits to "true up" the past is more contestable — it can look like genuine remediation or like buying absolution — and is defensible only if paired with honest disclosure and a credible forward strategy. The decisive variables are legal exposure, the credibility cost of restating versus staying quiet, and whether the firm's forward plan reduces its reliance on contested credits.

---

# Part 5: ICVCM and Core Carbon Principles (supply-side reform)

The **Integrity Council for the Voluntary Carbon Market (ICVCM)** is an independent governance body launched in 2021 (following the work of the **Taskforce on Scaling Voluntary Carbon Markets** under Mark Carney). ICVCM is the supply-side equivalent of a financial regulator: it sets quality benchmarks that credits and standards must meet to receive the **Core Carbon Principles (CCP) label**.

## The Core Carbon Principles

The CCPs are 10 principles for high-integrity carbon credits, organized in three sections:

**Governance:**
1. **Effective governance** — the carbon-crediting program has effective program governance.
2. **Tracking** — the program operates a registry to uniquely identify credits.
3. **Transparency** — the program provides comprehensive, transparent information.
4. **Robust independent third-party validation and verification** — by accredited verifiers.

**Emissions impact:**
5. **Additionality** — credits represent emissions reductions or removals that are additional.
6. **Permanence** — credits represent emissions reductions or removals that are permanent, or appropriately address reversal risk.
7. **Robust quantification** — emissions reductions or removals are robustly quantified.
8. **No double counting** — credits are not double-counted or double-claimed.

**Sustainable development:**
9. **Sustainable development benefits and safeguards** — credits contribute to sustainable development and avoid negative impacts.
10. **Contribution toward net zero transition** — credits help to scale up activities consistent with net zero pathways.

The CCPs are not themselves a methodology — they're a benchmark against which methodologies and programs are assessed.

## The assessment process

ICVCM assesses both **programs** (the standards) and **methodologies** (the specific project-type rules within programs).

**Programs (CCP-Eligibility):**
- Six programs approved as CCP-Eligible: ACR, ART, CAR, Gold Standard, Verra/VCS, Isometric.
- Others under assessment: Puro.earth, Social Carbon, possibly others.
- CCP-Eligibility means the program's governance meets CCP standards. It does NOT mean all credits from the program are high-integrity.

**Methodologies (CCP-Approved):**
- ICVCM is reviewing methodologies one at a time, in multi-stakeholder working groups (MSWGs).
- As of late 2025: approximately 36 methodologies approved across the six eligible programs.
- Credits issued under CCP-Approved methodologies receive the **CCP label**.
- As of October 2025: ~51 million credits had been issued using CCP-approved methodologies, representing ~4% of 2024 market volume.

The methodology assessment is contentious. In December 2024, the ICVCM approved three REDD+ methodologies (Verra's VM0048, ART's TREES v2, Verra's JNR Framework v4.1). The decision was protested by some Expert Panel members and Subject Matter Experts in a public December 10, 2024 statement, arguing the approved methodologies did not actually meet several CCP requirements. The dispute reflects deeper questions about whether REDD+ at any methodology level can pass the integrity tests.

## The CCP price premium

CCP-labeled credits trade at substantial premiums to non-labeled credits. According to ClearBlue Markets and Calyx Global data, CCP-labeled credits had price premiums of 30–60% in 2025. By Q3 2025, the premium for "Tier 1" CCP-eligible credits over "Tier 3" credits averaged 47% in the ClearBlue–Calyx index.

The price segmentation creates a market signal: project developers face stronger incentives to design projects to CCP standards; buyers face incentives to prefer CCP-labeled credits for their climate claims.

## Whether the reform is working

The ICVCM/CCP framework is the most ambitious supply-side reform attempt in VCM history. Whether it's working depends on what success means:

- **Catalyzing price differentiation:** Working. CCP-labeled credits command substantial premiums.
- **Catalyzing methodology improvement:** Partly working. Major methodology revisions (VM0048, the new ARR methodology, the renewable-energy methodology rejections) reflect CCP pressure.
- **Reducing low-integrity credit volume:** Limited progress. Low-integrity legacy credits continue to be issued and retired in large volumes outside the CCP framework.
- **Building durable institutional trust:** Mixed. The December 2024 internal dissent over REDD+ approvals undermined the framework's credibility in the eyes of some critics.

The ICVCM's institutional position is uncomfortable: it's voluntary, has no enforcement power, and depends on demand-side pressure (buyers preferring CCP-labeled credits) to drive supply-side change. That demand-side pressure is itself dependent on the VCMI and SBTi framework decisions in 2026–2027.

## **Stop-and-check 8.E**

1. CCP-labeled credits trade at a 30–60% premium. Trace the causal chain by which a *labeling* scheme with no enforcement power nonetheless changes what projects developers choose to build.
2. ICVCM approved three REDD+ methodologies in December 2024 over the public dissent of some of its own expert panel. What does that internal split tell you about whether REDD+ *avoidance* can clear a rigorous integrity bar at all?
3. The chapter grades ICVCM's progress at "reducing low-integrity credit volume" as limited — weak legacy credits keep being issued and retired outside the CCP framework. Why can a supply-side label not stop that on its own?
4. **Socratic prompt:** Only ~4% of 2024 market volume carries the CCP label after several years of work. Is a reform that has labeled 4% of the market succeeding slowly or failing? What evidence would distinguish the two?

**Answers**

1. The chain runs through price and finance. The label creates a visible quality tier; quality-sensitive buyers (facing disclosure rules and reputational risk) pay a premium for it; that premium raises the realized price and bankability of label-eligible projects relative to non-eligible ones; so developers, choosing what to build and which methodology to use, steer toward CCP-compliant designs to capture the premium and the easier financing. No enforcement is required — the label changes relative project economics, and developers follow the money. It's the same mechanism by which any voluntary certification (organic, Fair Trade, LEED) shifts production without legal compulsion: it works as long as buyers keep paying for the label.

2. It tells you the integrity community itself is not convinced REDD+ avoidance can pass, even with the revised jurisdictional methodologies. The dissent wasn't about a peripheral detail — expert-panel members publicly argued the approved methodologies still failed core CCP requirements, which is a remarkable thing for a body's own experts to say about its flagship decision. That signals the problem may be structural rather than methodological: avoidance rests on an unobservable counterfactual baseline, and no amount of methodology revision fully removes that. The split suggests REDD+ integrity is contested at the deepest level, and that approving it was partly a market-pragmatic decision (REDD+ is too large to exclude) rather than a purely technical one.

3. Because a supply-side label only governs which credits *can* claim a quality tier — it cannot stop other credits from being issued and sold. As long as some buyers will purchase cheap non-labeled avoidance credits for low-cost "carbon neutral" claims, standards will keep issuing them and the legacy volume persists. Killing that volume requires the *demand* side to refuse it — buyers, regulators, and claim-frameworks declining to recognize non-labeled credits. That's exactly why supply-side reform (ICVCM) is explicitly paired with demand-side reform (VCMI, SBTi, ISSB disclosure): the label raises the ceiling for good credits but only demand-side discipline can lower the floor for bad ones.

4. The 4% number alone is ambiguous; what distinguishes slow success from failure is the *trajectory and the price signal*, not the level. Success looks like: the labeled share growing each year, the CCP premium persisting or widening (showing buyers value the distinction), methodology approvals expanding the eligible pool, and non-labeled volume shrinking. Failure looks like: the share stalling, the premium collapsing (buyers stop caring), approvals gridlocked by disputes like the REDD+ dissent, and cheap non-labeled credits continuing to clear at volume. The 47% Tier-1 premium and the methodology pipeline are early evidence for the optimistic reading; the persistence of large non-labeled retirement and the internal dissent are evidence for the pessimistic one. You judge a young certification by its derivative, not its level — but if the share is still ~4% several years on, the derivative had better be clearly positive.

---

# Part 6: VCMI, SBTi, and demand-side reform

The supply-side reforms (ICVCM) are mirrored by demand-side reforms specifying when buyers can credibly claim climate benefits from voluntary credits.

## VCMI Claims Code of Practice

The **Voluntary Carbon Markets Integrity Initiative (VCMI)** is a multi-stakeholder governance body focused on the demand side. Launched in 2021 alongside ICVCM, VCMI develops the **Claims Code of Practice** — guidance on what corporate climate claims are credible based on voluntary credit use.

The Claims Code establishes a tier structure:

- **Silver tier** — Companies meeting basic requirements (publicly disclosed inventory, transition plan, year-over-year reduction performance, validated SBTi targets) can use offsets up to a specified threshold and make tier-specific claims.
- **Gold tier** — Higher requirements; correspondingly stronger claims permitted.
- **Platinum tier** — Highest requirements; strongest claims.

Claims must be tied to validated SBTi targets and supported by purchase of CCP-labeled credits. The Claims Code is voluntary and operates by reputational pressure.

The 2024 release of Version 1 of the Claims Code triggered substantial corporate buyer response. Several major buyers (Salesforce, Microsoft, others) have begun structuring their VCM portfolios to qualify for higher tiers.

## SBTi V2 and the role of credits in net-zero

The Science Based Targets initiative's **Corporate Net-Zero Standard Version 2 (CNZS V2)** — second consultation closed December 2025, final standard expected in 2026 and mandatory for new near-term targets from 1 January 2028 (see Ch. 13 for the authoritative timeline) — substantially changes how corporate net-zero pledges can use voluntary credits.

Key V2 provisions (Ch. 5 covered this in more detail):
- **"Ongoing Emissions Responsibility (OER)"** replaces the previous "Beyond Value Chain Mitigation" (BVCM) framework. Companies are encouraged (voluntary until 2035, mandatory thereafter for Category A companies) to take responsibility for their emissions during the transition period through carbon credits.
- **Two tiers of recognition** — "Recognized" and "Leadership" — for companies engaging with OER.
- **Mandatory removal purchasing post-2035** at a percentage of ongoing emissions that rises to 100% by net-zero target year.
- **Increasing share of long-lived removals** in the residual-neutralization mix.
- **No avoidance credits** for residual emissions at net-zero target year — only removals.

SBTi V2 effectively bifurcates voluntary credit demand:
- **High-quality removal credits** (DAC, BECCS, biochar at the durable end, possibly ARR with strong permanence) become increasingly important for residual neutralization.
- **Avoidance credits** become recognized for the OER framework as "support for climate action" but cannot substitute for direct decarbonization or residual-neutralization removals.

This is a substantial demand-side restructuring. The market is now bifurcated by credit type more than by quality alone:
- **Removal credits** at high prices (DAC ~$500–1,500/tCO₂e, biochar ~$80–200/tCO₂e, biomass burial ~$150–250/tCO₂e, BECCS ~$150–300/tCO₂e, etc.) — the SBTi-eligible-for-neutralization category.
- **Avoidance credits** at low prices ($1–10/tCO₂e for legacy projects; $5–20/tCO₂e for CCP-labeled) — useful for OER claims but not residual neutralization.

## ISSB and disclosure regimes

The supply-side and demand-side reforms operate alongside emerging regulatory pressure on disclosure. **IFRS S2** (Ch. 5) requires companies to disclose Scope 1, 2, 3 emissions plus any use of carbon credits, including:
- Type and quality of credits used.
- Whether credits are tied to net-zero claims.
- Whether claims are validated under any framework.

This disclosure requirement makes credit quality publicly visible in audited financial reports. Combined with shareholder pressure and litigation risk, this is producing material constraints on corporate use of low-quality credits.

The combination of ICVCM + VCMI + SBTi V2 + ISSB represents the most comprehensive reform of VCM governance ever attempted. Whether it's adequate to transform the market is the central open question.

## **Stop-and-check 8.F**

1. ICVCM reforms the supply side (credit quality); VCMI/SBTi reform the demand side (what claims you can make). Why does neither work without the other?
2. SBTi V2 lets avoidance credits support "Ongoing Emissions Responsibility" but bars them from neutralizing residual emissions at the net-zero target year — only removals qualify. Trace how that one rule reshapes demand across the credit-type spectrum.
3. The VCMI Claims Code and SBTi target validation operate by reputational pressure, not law. What gives reputational pressure real teeth in this market, and what could remove the teeth?
4. **Socratic prompt:** Supply-side and demand-side reforms are designed to be "complementary" — each makes the other matter. But both are voluntary, and each depends on the other to have force. Is this a virtuous circle (quality supply and discerning demand reinforcing each other) or a fragile loop that unwinds if either side loses momentum?

**Answers**

1. Supply-side reform creates the *ability* to tell good credits from bad (the CCP label); demand-side reform creates the *motive* to care. A quality label with no buyers who insist on it just sits there — developers won't pay to meet a bar no purchaser rewards. Conversely, a demand-side rule that says "only high-integrity removals neutralize residuals" is meaningless if there's no agreed, verifiable definition of "high-integrity" for buyers to point to. ICVCM supplies the definition and VCMI/SBTi supply the obligation to use it; the label is the noun and the claims code is the verb. Each is inert alone, which is why the reform was deliberately built as two interlocking tracks.

2. The rule splits the demand curve in two. Removals (DAC, BECCS, biochar, durable ARR) become the only instrument that can do the high-value job — neutralizing residual emissions in a net-zero claim — so demand and price for durable removals rise and a forward scarcity builds (hence advance-purchase coalitions like Frontier). Avoidance credits are demoted to a supporting role ("support for climate action" under OER) that is recognized but cannot back the headline net-zero claim, capping their value and pushing their price down. The single accounting rule thus does what years of integrity argument couldn't: it reprices the entire spectrum by *use case*, making a durable removal and a cheap avoidance credit non-substitutable even though both are "1 tCO₂e." (This is the demand-side expression of Ch. 5's avoided/removed distinction.)

3. The teeth come from three reinforcing sources: mandatory disclosure (IFRS S2 forces credit type and quality into audited reports, so claims are visible and comparable), litigation and regulatory risk (greenwashing actions by the FTC, ESMA, ASA, ACCC turn a loose claim into legal exposure), and the concentration of demand among large, reputation-sensitive buyers who can be named. What removes the teeth: a political/regulatory rollback that weakens disclosure or greenwashing enforcement, an economic downturn that makes buyers prioritize cost over credibility, or fragmentation where enough buyers accept weaker claims that the reputational penalty for low integrity disappears. Reputational pressure has force only while non-compliance is *visible* and *costly*; remove either and it evaporates.

4. It is genuinely both, and which one it is depends on momentum that is not guaranteed. The virtuous-circle reading: discerning demand (SBTi/VCMI) pays premiums for labeled, durable credits (ICVCM), which finances better projects, which deepens high-integrity supply, which makes it easier for more buyers to commit — a flywheel, with disclosure rules as the ratchet that stops backsliding. The fragile-loop reading: every node is voluntary and mutually dependent, so a stall anywhere propagates — if buyers retreat (downturn, political cover to stop bothering), the CCP premium collapses, developers stop pursuing the label, supply quality stalls, and the demand-side rules lose the supply they presuppose. The honest assessment is that the system is a flywheel that hasn't yet built enough mass to be self-sustaining: it is being held in motion by a relatively small set of committed buyers and a still-fragile set of voluntary institutions, and its durability through a political or economic shock (the Trump-era skepticism, a recession) is the unresolved question the chapter keeps returning to. Mandatory disclosure is the most likely candidate for the "ratchet" that would make the circle robust rather than fragile — which is why the reform's fate is tied to the disclosure regimes of Ch. 5 and Ch. 13.

---

# Part 7: Current state and the unresolved questions

## Market structure 2025–2026

The voluntary carbon market in 2025–2026 has several distinct segments:

**By credit type:**
- **Engineered removals** (DAC, BECCS, biomass burial, mineralization): ~$150–1,500/tCO₂e. Small volumes (~100 ktCO₂e/yr issued, growing). Stripe and the Frontier coalition are major buyers.
- **Nature-based removals** (ARR, soil carbon, biochar, blue carbon): ~$20–150/tCO₂e. Moderate volumes.
- **REDD+ avoidance** (jurisdictional ART/TREES): ~$10–25/tCO₂e for CCP-labeled.
- **REDD+ avoidance** (project-scale legacy): ~$2–8/tCO₂e for non-CCP-labeled, less for older vintages.
- **Methane projects** (landfill, mine, manure): ~$15–40/tCO₂e for CCP-labeled.
- **Cookstoves**: ~$5–20/tCO₂e for CCP-labeled.
- **Industrial gases** (HFC destruction, N₂O abatement): ~$3–15/tCO₂e.
- **Renewable energy** (legacy, mostly retired or pre-2020): under $1/tCO₂e generally; new CCP-eligible methodologies in emerging markets ~$15–30/tCO₂e.
- **CORSIA-eligible Phase 1**: ~$15–25/tCO₂e (ICE futures).

**By buyer profile:**
- **Compliance-adjacent corporates** (Microsoft, Stripe, Salesforce, large financial institutions): increasingly focused on high-quality removals plus jurisdictional REDD+ for OER.
- **Legacy corporates buying for "carbon neutral" claims**: declining segment, mostly purchasing low-cost avoidance credits, increasingly facing reputational and disclosure pressure.
- **Government buyers** (Singapore, Switzerland, US international purchases under Article 6.2 agreements): emerging segment for CCP-labeled credits.

**By region:**
- **Latin America and Africa** remain the largest credit origin regions (forestry-heavy).
- **Asia** is growing (cookstoves, methane, biomass).
- **North America and Europe** are smaller credit origins but larger buyers.

## What's unresolved

Several substantive questions remain open as of mid-2026:

**1. Can REDD+ avoidance be made credibly high-integrity?**

The 2022–2024 crisis raised this as a fundamental question. Jurisdictional approaches (ART/TREES) and the new Verra methodologies (VM0048, JNR) are answers in principle, but the empirical record is too short to know if they produce credits that survive future scrutiny. The December 2024 internal ICVCM dissent over REDD+ approval suggests the question is not settled within the integrity community itself.

**2. Will CDR scale at the prices and volumes needed?**

The IPCC scenarios for 1.5°C require CDR scale of 5–10 GtCO₂/yr by mid-century. Current CDR volumes are <1 MtCO₂/yr — three to four orders of magnitude smaller. The voluntary market is currently providing the primary financing for early-stage CDR development (Stripe's Frontier coalition has $1B+ committed; advance purchase agreements are scaling). Whether this scales to gigaton volumes at affordable costs is genuinely uncertain.

**3. How do voluntary credits interact with Article 6?**

The **Paris Agreement's Article 6** creates international carbon trading mechanisms — Article 6.2 (cooperative approaches between countries) and Article 6.4 (a new UNFCCC-supervised mechanism). The relationship between Article 6 credits and voluntary credits is being worked out. **Singapore, Switzerland, Norway, Sweden, Korea** and others are buying Article 6.2 credits to count toward their NDCs. The market structure (compliance demand from sovereign buyers in parallel with voluntary corporate demand) creates competition for high-quality supply and is gradually merging the markets.

The **Coalition to Grow Carbon Markets** is a recent (2025) initiative pushing for harmonization across voluntary, Article 6, and CORSIA markets.

**4. Can scale be reconciled with quality?**

The basic tension: more credits at lower quality (the historical pattern) vs. fewer credits at higher quality (the ICVCM direction). High-quality CDR at $500/tCO₂e cannot fund gigaton-scale removals affordably; low-quality avoidance at $3/tCO₂e doesn't represent real climate benefit. The market is currently bifurcating into these two segments, with the volume in low-quality declining and high-quality scaling slowly.

**5. Is the institutional reform durable?**

ICVCM, VCMI, SBTi V2 — all are voluntary governance bodies dependent on continued buyer engagement and methodology investment. The Trump administration's general skepticism of international climate governance creates political risk. The corporate reform momentum is real but could be reversed by economic downturn or regulatory backlash.

The 2026–2027 period will substantially determine whether the post-crisis voluntary market becomes a credibly high-integrity mechanism or fragments into competing tiers with permanent quality concerns.

## **Stop-and-check 8.G**

1. The voluntary market is bifurcating into "removal credits" (premium-priced, scarce) and "avoidance credits" (discounted, abundant). Is this bifurcation a sign of healthy market discrimination or a sign that the avoidance category has structural problems?
2. CDR at $500–1,500/tCO₂e can scale within current carbon-pricing margins for some sectors but not all. Where does this leave the gigaton-scale CDR that 1.5°C pathways assume?
3. Article 6 creates compliance-style demand for credits at the sovereign level. How does this change the structure of the voluntary market, given that some of the same credit types will be used for both NDC compliance and voluntary claims?
4. **Socratic prompt:** If you were CEO of a company committed to net-zero by 2040, with current emissions of 1 MtCO₂e/yr and the SBTi V2 framework about to become mandatory, how would you structure your VCM strategy? What types of credits, at what prices, for what claims?

**Answers**

1. It is both healthy discrimination and a symptom of structural problems, and the two are the same fact seen from different angles. The bifurcation is healthy in that the market is finally pricing real differences: removal credits carry durable, physically removed carbon and survive the additionality and permanence tests, so buyers pay premiums for them, while avoidance credits — which depend on contested counterfactual baselines — are discounted. That price gap is the market correctly distinguishing units that used to be treated as fungible. But it also reflects that the avoidance category has deeper, possibly irreducible problems: its value rests on unobservable baselines and is vulnerable to leakage and reversal. So the discounting is rational discrimination precisely because the structural problems are real; the two framings are not in conflict.

2. It leaves the gigaton-scale CDR assumption in tension with affordability. Engineered removals at $500–1,500/tCO₂e can be absorbed by sectors with high carbon-cost margins or by deep-pocketed buyers (Stripe, Frontier), but cannot finance the 5–10 GtCO₂/yr that 1.5°C pathways assume — current CDR volumes are three to four orders of magnitude below that, and gigaton volumes at those prices would cost trillions. The implied requirement is steep cost declines through scale and learning, plus far larger and more durable demand (likely compliance-driven and sovereign, not just voluntary). Whether costs fall fast enough is genuinely uncertain; until they do, the pathways' CDR assumption outruns what the market can affordably deliver.

3. Article 6 adds sovereign, compliance-style demand alongside voluntary corporate demand, and because both can draw on the same high-quality credit types, it intensifies competition for limited high-integrity supply and tends to merge the two markets. Countries like Singapore, Switzerland, Norway, Sweden, and Korea buying Article 6.2 credits toward their NDCs raises the floor under premium credits and pulls supply toward CCP-grade, durable units. It also sharpens double-counting discipline: a credit used for a sovereign NDC cannot also back a corporate voluntary claim, forcing "corresponding adjustments" and clearer attribution. The net effect is a structurally tighter, more contested market for quality supply, gradually fusing voluntary and compliance demand rather than keeping them separate.

4. With a 2040 net-zero target and mandatory SBTi V2 approaching, the strategy should put direct decarbonization first and use the VCM in two distinct lanes. During the transition, engage avoidance and jurisdictional credits for the Ongoing Emissions Responsibility framework — recognized as "support for climate action" but not as residual neutralization — preferring CCP-labeled, jurisdictional REDD+ (ART/TREES) over cheap legacy project-scale credits to manage reputational and disclosure risk, at perhaps $10–25/tCO₂e. Simultaneously, build a forward book of durable removals (DAC, BECCS, biochar, durable ARR) via advance-purchase agreements, accepting $80–1,500/tCO₂e, since V2 requires an increasing share of long-lived removals and only removals for residuals at the target year. Claims should be tied to validated SBTi targets and supported by CCP-labeled credits to qualify under the VCMI Claims Code. The decisive variables are the firm's residual-emissions profile, its tolerance for high removal prices now versus scarcity later, and its disclosure exposure under IFRS S2.

---

# Part 8: Fuel-based credits and the additionality inversion

Chapter 7 Part 8 covered the architecture of fuel-standard compliance regimes — RFS, LCFS, 45Z, REDIII, ReFuelEU, FuelEU Maritime. This part brings those regimes into the VCM integrity framework by asking: can you add a voluntary carbon credit on top of compliance revenue from a fuel standard?

The answer governs most practical VCM work done by renewable-fuel project developers. And the answer is almost always no — for a reason that is counterintuitive until you see it clearly. The most commercially successful fuel projects, precisely *because* they are successful, cannot support defensible voluntary credits. This is the **additionality inversion**.

## The additionality inversion

Additionality requires that a reduction would not have happened without the carbon-credit revenue. This means the project must depend on the credit revenue to be viable.

Fuel-standard compliance regimes create independent revenue for emissions reduction without requiring an additionality test — they pay for performance against a statutory baseline. The more generous the compliance revenue, the more self-sufficient the project is. A US HEFA SAF producer earning a full stack of RIN + LCFS + 45Z revenue can finance the project on compliance revenue alone. This is financially good news for the project — and fatal news for additionality.

**The inversion:** the richer the compliance stack, the less defensible any voluntary credit on top. The project that most needs a voluntary credit — because compliance revenue is thin or absent — is the project in a deregulated geography with no compliance market at all.

This is counterintuitive. Most people assume that where the project economics are best, the environmental benefit is greatest and the market opportunity is richest. But additionality isn't measuring benefit — it's measuring counterfactual dependence. Counterfactual dependence is highest where the project is hardest to finance without the credit.

**The resulting principle:** fuel-standard compliance revenue and VCM revenue are not stackable on the same tonne. One or the other causes the reduction; both cannot.

## Two additional complications: attribute claiming and double counting

Even where additionality might survive, two further tests must pass.

**Attribute claiming:** When a fuel earns a compliance credit (a RIN, an LCFS credit, a 45Z credit), the compliance regime has "claimed" the emissions-reduction attribute of that gallon. The attribute is attached to the compliance instrument. Selling a voluntary credit on the same attribute is **double claiming** — the same reduction counted toward two different goals. This is one of the three distinct forms of double counting:
- **Double issuance** — two credits issued for the same physical tonne.
- **Double claiming** — the same reduction counted toward two goals (e.g., a compliance obligation *and* a corporate Scope 3 claim).
- **Double monetization** — being paid twice for the same environmental good.

**Double counting across compliance regimes:** Some fuel projects serve multiple markets. HEFA produced in Latin America and exported to Europe for ReFuelEU compliance has its attribute claimed by the EU compliance obligation. If that attribute was also used to generate a voluntary credit, or sold into a US RIN market, the attribute has been counted twice. Book-and-claim mechanisms address physical separation but attribute accounting must be separate and traceable.

## Where white space actually exists: three structural types

Despite the additionality inversion, three structural situations allow a defensible voluntary credit in fuel markets.

**1. Geographic gap — no compliance regime claims the attribute.** A project in a jurisdiction with no active fuel-standard regime earns no compliance revenue. If the project wouldn't exist without voluntary credit revenue, additionality is genuine. A HEFA plant in Brazil, financed because VCM pre-purchase revenue makes it viable, where no domestic compliance market exists, is the cleanest fuel-VCM case available. The white space is finite — it closes when local regulation arrives and the compliance regime claims the attribute — but it is genuine while it exists.

The critical caveat: the geographic gap is narrower than it first appears, because **any fuel producer in the world can access California's LCFS** by registering a CARB-approved CI pathway and delivering fuel into California — the constraint is on *delivery*, not production. So a project must distinguish an **apparent** geographic gap (the producer *could* register a CARB pathway and access LCFS but hasn't yet — a gap the producer can close, which should not be underwritten as permanent VCM white space) from a **true** geographic gap (the producer genuinely cannot reach any compliance regime, because no applicable methodology exists, volume is too small to justify registration, or delivery into a compliance market is not commercially viable). The practical takeaway: before declaring a project VCM-eligible on geographic-gap grounds, verify the producer *cannot* access LCFS — not merely that they *haven't yet*. The CARB registration mechanics, costs, and the international producer base that has already done it are in **Appendix A**.

**2. Boundary gap — the regime's accounting methodology cannot score a real improvement.** REDIII relies primarily on default CI values by feedstock pathway. Some real plant-level improvements fall outside what the methodology can score. The decisive screen: *can the operator move their certified CI score by reporting this improvement through the actual-value certification pathway?*
- **Yes** → compliance captures it → **not** VCM-eligible.
- **No, the methodology has no field for it** → candidate white space — subject to all four integrity tests.

The boundary-gap case requires deep familiarity with the specific methodology's blind spots. Its half-life is finite: methodology revisions close gaps.

**3. Pre-FID financial swing — the project doesn't clear its hurdle rate on compliance alone.** A project close to viability but not quite clearing FID without an additional revenue stream has genuine additionality if the voluntary credit is demonstrably the decisive, contracted dollar at FID. The requirement: make the VCM offtake load-bearing in the specific FID analysis — a signed pre-purchase in the financing case the credit committee approves, documented so that the bank's credit-committee memo and the verifier's additionality file are the same document. Risk: rising compliance prices post-FID can retroactively undermine the additionality claim.

## The four worked cases

### HEFA in North America and Latin America

**NAM:** The full compliance stack (RIN + LCFS + 45Z) is so rich that US HEFA projects are bankable on compliance alone. The attribute is claimed the moment the fuel is produced. A voluntary credit on top is double-claiming an already-claimed attribute. The most commercially attractive cell in the fuel-VCM space is a trap.

**LATAM:** Little or no domestic compliance value. The genuine bridge window. A LATAM HEFA project financed because VCM revenue makes it viable, with no domestic compliance regime, is the cleanest fuel-VCM case available. The window is finite — it closes when the molecules reach a compliance market or local regulation arrives. Underwrite the bridge on a **finite** VCM revenue period followed by an explicit handoff to compliance revenue, with a "stranding haircut" modeled for the transition (government may claim the attribute without compensating the project, or at a low administered price).

### eSAF in the EU

ReFuelEU rewards volume and qualification, not continuous improvement. REDIII's default-value structure means real plant-level CI gains the methodology cannot score are left unclaimed. The boundary-gap white space lives here — not in the existence of the eSAF plant (the mandate owns that) but in the specific improvement delta that falls outside both the default value and the actual-value certification pathway. The edge is knowing the methodology's blind spots better than the regulator's table does; the edge has a half-life.

### Biomethane in North America and the EU

**NAM:** Dairy and landfill biomethane can have deeply negative CI (often around −250 gCO₂e/MJ) because capturing methane that would otherwise escape earns a large avoided-emissions credit. This is captured in full by LCFS. A voluntary credit on top is both non-additional and reputationally problematic.

The biomethane case illustrates an important structural point: negative-CI performance in a fuel score is a **counterfactual avoidance claim embedded inside a lifecycle score** — structurally identical to a REDD+ avoidance credit, with the same additionality and baseline vulnerabilities. The LCFS's deep negative-CI credits are the fuel-market equivalent of the avoided-deforestation problem from Parts 2–4 of this chapter: the claim is real, but it is entirely captured by the compliance regime. No white space remains.

**EU:** Same boundary-gap logic as eSAF — only the improvement delta the certified CI score cannot capture is a candidate.

### eAmmonia for marine applications

Green ammonia is a leading candidate zero-carbon marine fuel. FuelEU Maritime's 2× RFNBO multiplier creates powerful incentives for EU-port shipping. But the compliance regime is immature: IMO's global mechanism is in formation, bunkering standards are 2026–27, and commercial engines are recent.

For a green-ammonia project serving non-EU routes, there is currently no mature compliance buyer — which creates a bridge window structurally similar to the LATAM HEFA case. The additionality story competes with heavy direct subsidies, and the stranding risk is acute: when the IMO mechanism and FuelEU coverage arrive, the compliance regime claims the attribute and the voluntary stream ends.

## White-space ranking for voluntary credits

This table ranks fuel-market contexts by VCM white-space quality — which is inversely correlated with compliance economics:

| Rank | Where | Type | Why | Half-life |
|---|---|---|---|---|
| 1 | Deregulated geographies (LATAM, parts of SEA/Africa) | Geographic / bridge | No regime claims the attribute; VCM is the financing that makes it additional | Finite — closes when local regulation arrives |
| 2 | EU eSAF / biomethane improvement delta | Boundary gap | REDIII default values can't score continuous operator CI gains | Shrinking — methodology revisions close cracks |
| 3 | Pre-FID marginal projects (any geography) | Financial-additionality swing | Project doesn't pencil on compliance alone; contracted VCM is the decisive dollar at FID | Compliance-price risk — rising premiums retroactively challenge additionality |
| 4 | Marine eAmmonia, non-EU routes | Immature-regime bridge | No mature compliance buyer yet | Acute stranding risk; competes with direct subsidies |
| — | NAM HEFA / NAM biomethane / EU mandate-covered SAF | **None** | Compliance stack causes the reduction and claims the attribute | Not applicable — these are double-counting traps |

The headline: the single best VCM white space is the deregulated-geography bridge, and the most defensible structural play in regulated markets is the EU improvement delta — precisely because the EU rewards volume rather than continuous improvement, which leaves a narrow but real unclaimed gap. California's LCFS, by being the most granular and continuous CI market in the world, leaves almost no VCM white space — its granularity is exactly what closes the gap.

## The unit mismatch trap

A recurrent error in fuel-VCM analysis: comparing instruments denominated in different units without converting first.
- RINs and 45Z are quoted **per gallon**.
- LCFS credits and VCM credits are quoted **per tCO₂e**.
- SAF book-and-claim certificates are quoted per tCO₂e at approximately $1,500–3,500/tCO₂e.

A HEFA gallon abates approximately 0.0085 tCO₂e. Multiplying the SAF certificate price ($2,000/tCO₂e) by a gallon's abatement implies roughly $17/gallon — more than the fuel itself plus its entire compliance stack. This absurd result is the signal: the SAF certificate price is not a carbon-abatement price. It is an aviation-scarcity premium for a specific compliance claim under ReFuelEU and CORSIA — an instrument for airlines seeking to meet blending obligations, not a stackable revenue line for the HEFA plant itself.

Always convert all instruments to a common per-tonne basis before comparing or stacking. At that basis: a D4 RIN at $0.85 ≈ $100/tCO₂e, an LCFS credit at $63/tCO₂e, a VCM proxy at $40–60/tCO₂e — these are comparable. The SAF cert at $2,000/tCO₂e is flagged as a non-comparable instrument for a different kind of claim.

## Permanence/additionality asymmetry: bridging back to the chapter's integrity framework

Fuel-based reductions have a different integrity profile than the forestry projects that dominate much of the VCM integrity debate.

**Fuel reductions are permanent by nature.** When a gallon of fossil jet fuel is displaced by SAF, the combustion-displacement is irreversible — the CO₂ that would have been emitted stays in the ground. The permanence problem that plagues forestry projects (fire, land-use change, policy reversal) does not apply.

**Fuel reductions are additionality-poor in practice.** Precisely because compliance regimes pay well for fuel decarbonization, most fuel-market emissions reductions are caused by compliance revenue, not by voluntary credit revenue. The additionality test fails in most commercially significant fuel cases.

**Forestry is the mirror image.** Nature-based projects struggle with permanence (reversal risk) but sometimes pass additionality (a forest protection project in a high-deforestation-risk jurisdiction really might require the credit revenue). Different failure modes, same four-test framework from Part 2.

This asymmetry is one reason the voluntary carbon market contains so little fuel-offset volume: the most permanent reductions (fuel displacement) are mostly non-additional in practice, while the most additional projects (early-stage conservation) have permanence problems. The VCM is not well-suited to either end of the fuel world — only to the narrow bridge-window cases described above.

---

## Operational depth: see Appendix A

Two further pieces of this analysis are operational rather than conceptual, and are collected in **Appendix A (Fuel-Standard Compliance Operations and the Fuel–VCM Boundary)** alongside the Chapter 7 material they depend on:

- **A producer's compliance-capture decision matrix** — for each category of operational improvement (feedstock switch, renewable process energy, green hydrogen, efficiency, upstream Scope 3, novel pathways, out-of-jurisdiction production), which regimes can score it and where genuine VCM white space survives. The short version: the white space reduces to novel fuel pathways with no methodology yet, certain upstream Scope 3 improvements, and the *true* geographic gap.
- **VCMs as a bridge *toward* regulation** — the stronger claim that a voluntary market can help bring a future compliance regime into being (through proof of concept, MRV infrastructure, industry constituency, supply base, and price discovery), with documented cases (US Midwest RNG → state LCFS programs, Canada CFR absorbing CARB-registered pathways, Brazil/Colombia biomethane informing domestic standards) and the conditions under which the bridge strategy is sound rather than a rationalization.

The headline carries forward without the detail: the single best VCM white space in fuel markets is the deregulated-geography bridge, and the most defensible play in a regulated market is the EU improvement delta — precisely because the EU rewards volume rather than continuous improvement. California's LCFS, by being the most granular continuous-CI market in the world, leaves almost no white space at all.

## **Stop-and-check 8.H**

1. The additionality inversion says the richest compliance stack produces the weakest VCM white space. A critic says this is just a definitional trick — if the reduction happens, why do we care which revenue stream caused it? What's the substantive answer?
2. A LATAM HEFA developer plans to earn VCM revenue for four years, then transition to compliance revenue when local regulation arrives. Is this a defensible strategy? What does it require to be credible, and what can go wrong?
3. REDIII's default-value methodology creates a "boundary gap." What would REDIII have to look like for this gap to close entirely? Is a gap-closing methodology revision a sign of policy improvement or of white-space destruction?
4. A fuel developer in Colombia says their project falls in the "geographic gap" because Colombia has no domestic fuel standard. A due-diligence analyst pushes back. What questions should the analyst ask, and under what circumstances would the analyst conclude the gap is apparent rather than true?
5. The "VCMs as bridge toward regulation" argument has a dark version: a project that deliberately avoids seeking CARB registration in order to preserve its VCM revenue stream. Is this a realistic concern? How would a buyer or standard detect it, and what would it mean for project credibility?
6. **Socratic prompt:** A HEFA plant in South Africa earns VCM credits for two years under a bridge strategy. In year three, South Africa announces a new LCFS-equivalent and says it will grandfather the existing VCM credit stream for two more years, then claim the attribute. Does this stranding risk change how the project should have been financed from the start? What would you have done differently?

**Answers**

1. The substantive answer is that additionality is not measuring whether the reduction happened — it is measuring whether the voluntary credit caused it. If a rich compliance stack already finances the project, then the compliance revenue caused the reduction and the credit added nothing real; selling a voluntary credit on top means a buyer pays for a reduction that would have occurred anyway, and the buyer's offset claim is false. The reduction is genuine, but its causation is already "spoken for." Allowing a non-additional voluntary credit lets a buyer believe they have neutralized an emission when no incremental abatement was financed — which is exactly the integrity failure the whole framework exists to prevent. The critic's "the reduction happened" misses that offsets are a causal claim, not a performance claim.

2. It is defensible only under specific conditions, and it carries real risks. To be credible, the bridge must be underwritten as a finite VCM revenue period with an explicit, planned handoff to compliance revenue, and the additionality case must hold for the years it claims credits — the project must genuinely depend on VCM revenue while no compliance regime claims the attribute. What can go wrong: local regulation may arrive earlier or later than modeled; when it arrives the government may claim the attribute without compensating the project or at a low administered price (the "stranding haircut"); and if compliance prices turn out rich, the retrospective additionality of the bridge years can be challenged. A credible structure models the stranding transition explicitly rather than assuming a smooth handoff.

3. The gap would close entirely if REDIII scored every real plant-level CI improvement — if its accounting could capture, through an accessible actual-value certification pathway, any reduction an operator actually achieves, leaving nothing the methodology cannot see. As long as default values by feedstock pathway blunt plant-specific gains, some genuine improvements remain unscored and therefore potentially VCM-eligible. A gap-closing revision is a sign of policy improvement: the compliance regime is now rewarding more of the real abatement, which is the better outcome for the climate. From the VCM developer's seat it is white-space destruction, but that is the point — the white space existed only because the regulator's accounting was incomplete, so closing it means the policy got better, not that value was unfairly taken.

4. The analyst should ask whether the gap is apparent or true. Key questions: Could the producer register a CARB-approved CI pathway and deliver into California's LCFS? Could they reach any other compliance market (US RINs, Canada's CFR, a forthcoming domestic standard)? Is volume large enough to justify registration, and is delivery into a compliance market commercially viable? Does an applicable methodology exist for their fuel? If the producer *could* access LCFS or another regime but simply *hasn't yet*, the gap is apparent — closeable by the producer — and should not be underwritten as permanent VCM white space. The analyst concludes the gap is true only if the producer genuinely cannot reach any compliance regime: no applicable methodology, volume too small to justify registration, or delivery not commercially viable.

5. It is a realistic concern: a project could rationally preserve a VCM revenue stream by declining to register a CARB pathway it could otherwise obtain, since registration would let the compliance regime claim the attribute and end the voluntary stream. This is the dark version of the "bridge toward regulation" argument. A buyer or standard would detect it by testing the apparent-versus-true geographic gap — asking whether registration is feasible (methodology exists, volume sufficient, delivery viable) and whether the producer has deliberately avoided an accessible compliance route. If a producer is forgoing accessible compliance revenue specifically to keep selling credits, the additionality claim is a manufactured artifact of that choice, not a genuine counterfactual dependence — which destroys the credit's credibility and should disqualify it.

6. Yes — the stranding risk should have shaped the financing from the outset, and the example shows why. Knowing that a compliance regime can arrive at any time and claim the attribute (here, after a two-year grandfather), the project should never have been financed as though VCM revenue were permanent. I would have underwritten only a finite VCM revenue window with an explicit handoff to compliance revenue, modeled a "stranding haircut" for the transition (assuming the attribute may be claimed without compensation or at a low administered price), and sized debt and return expectations to the bridge years rather than to a perpetual voluntary stream. The decisive variables are how soon local regulation might plausibly arrive, the grandfathering terms, and whether the project pencils on the post-handoff compliance economics alone.

---

# Closing exercise

Three things to take away:

**1. The voluntary market's integrity is genuinely contested.** The 2022–2024 crisis revealed that a substantial fraction of legacy credits — especially in REDD+ — did not represent the climate benefits claimed. The reform movement is real and substantive (ICVCM, VCMI, SBTi V2, ISSB rules) but the reforms are partial, ongoing, and contested. Anyone reading current VCM debates should understand both the integrity critique and the reform response.

**2. Carbon credits are not a commodity in the conventional sense.** A $3 REDD+ credit and a $1,200 DAC credit are both called "1 tCO₂e," but they represent different physical activities, different durabilities, and different verification rigor. Treating them as interchangeable units is the conceptual mistake at the heart of many integrity failures.

**3. The market's future depends on whether scale can be reconciled with quality.** The current trajectory has high-quality credits growing slowly and low-quality credits being progressively delegitimized. Whether this produces a credible high-integrity market at scale, or a small-and-credible market alongside a larger-and-discredited one, will be determined in 2026–2028 by ICVCM, SBTi V2, Article 6 operationalization, and corporate buyer behavior.

---

# What this chapter simplified

**1. The detail of methodology mechanics.** I described methodologies broadly. The actual methodologies are 50–200 page technical documents covering measurement protocols, monitoring requirements, calculation formulas, reversal provisions, etc. Methodology details are where most integrity failures actually live. For any specific project category, the relevant methodology document is the authoritative source.

**2. The treatment of co-benefits.** I focused on carbon-integrity questions. Many VCM projects also claim biodiversity, community-development, water-quality, and other co-benefits. These co-benefits are themselves controversial — sometimes overstated, sometimes underestimated, sometimes traded off against carbon ambition. The Plan Vivo standard and Gold Standard's co-benefit framework attempt to address this. I didn't give it adequate space.

**3. The CORSIA story.** CORSIA — the international aviation compliance scheme — is a major source of credit demand and a hybrid voluntary/compliance market. CORSIA Phase 1 (pilot) ran 2021–2023; Phase 2 (mandatory for participants) is 2024–2026; Phase 3 (broader mandatory) is 2027 onwards. CORSIA-eligible credits trade at premiums to non-eligible voluntary credits. I gave brief coverage; deeper treatment in Chapter 12.

**4. The Article 6 detail.** The Article 6 mechanism is enormously consequential for VCM evolution but the operational rules are still being implemented. I gave introductory coverage. The next few COPs will substantially clarify Article 6, and the voluntary market structure will adjust accordingly.

**5. The legal and reputational risks for buyers.** Corporate buyers of low-quality credits are facing increasing litigation risk (greenwashing class actions, consumer protection claims) and regulatory risk (FTC, ESMA, ASA, ACCC investigations of carbon-neutral claims). I gave brief coverage. The litigation/regulatory landscape is moving fast and is itself an integrity-reform mechanism distinct from ICVCM/VCMI/SBTi.

---

# Glossary delta (Chapter 8)

- **Additionality** — The integrity test asking whether a project's emissions reductions would have happened anyway in the absence of carbon revenue.
- **ACR (American Carbon Registry)** — VCM standard, founded 1996; US-focused; CCP-Eligible.
- **ART (Architecture for REDD+ Transactions)** — Jurisdictional REDD+ standard; operates TREES methodology; CCP-Eligible.
- **Baseline** — The counterfactual emissions scenario against which project reductions are measured. The 2022–2024 REDD+ crisis was primarily a baseline-integrity problem.
- **Buffer pool** — Reserve credits held back from issuance to compensate for potential reversal of carbon storage. All major nature-based standards maintain buffer pools.
- **CAR (Climate Action Reserve)** — VCM standard, founded 2001; US/Mexico-focused; CCP-Eligible.
- **CCP (Core Carbon Principles)** — Ten principles for high-integrity carbon credits established by ICVCM. Programs and methodologies meeting CCP standards can carry the CCP label.
- **Coalition to Grow Carbon Markets** — 2025 multi-stakeholder initiative pushing harmonization across voluntary, Article 6, and CORSIA markets.
- **CORSIA (Carbon Offsetting and Reduction Scheme for International Aviation)** — ICAO scheme for international airline emissions; a *hybrid* mechanism (it accepts voluntary-market credits to meet a compliance obligation). Phase 1: 2021–2023 (pilot); Phase 2: 2024–2026 (mandatory for participants); Phase 3: 2027+.
- **CORSIA-eligible** — Standards and methodologies approved by ICAO's Technical Advisory Body for use in CORSIA. Credits trade at premium to non-eligible credits.
- **Frontier coalition** — Stripe-led group of buyers committing advance purchases of high-quality CDR. Approximately $1B+ committed by 2025.
- **Gold Standard** — VCM standard, founded 2003 by WWF; community-focused; CCP-Eligible.
- **ICVCM (Integrity Council for the Voluntary Carbon Market)** — Independent governance body established 2021; sets supply-side quality standards via the Core Carbon Principles.
- **IFM (Improved Forest Management)** — Project type covering forest management changes that increase carbon storage or reduce emissions vs. baseline practices.
- **Isometric** — VCM standard, founded 2022; CDR-only; CCP-Eligible (December 2024).
- **Jurisdictional REDD+** — REDD+ approach at national or sub-national scale rather than project scale. Addresses leakage and aligns with Article 6. ART/TREES is the primary standard.
- **Leakage** — Displacement of emissions to areas outside the project boundary. One of the four integrity tests.
- **N-GEO (Nature-based Global Emissions Offset)** — Standardized futures contract for nature-based avoidance credits. Reference price for nature-based market.
- **Permanence** — Durability of emissions reduction or removal. One of the four integrity tests.
- **Plan Vivo** — VCM standard, founded 1994; smallholder forestry/agroforestry focus.
- **Puro.earth** — VCM standard, founded 2019; CDR-only; Nasdaq-majority-owned.
- **REDD+** — Reducing Emissions from Deforestation and forest Degradation (plus conservation, sustainable forest management, carbon stock enhancement). UNFCCC framework that the VCM has built upon.
- **Removal credit** — Carbon credit representing emissions physically removed from the atmosphere (vs. emissions avoided).
- **Reversal** — Loss of stored carbon back to the atmosphere. Wildfires, land-use change, policy reversal, soil degradation are major reversal causes.
- **Retirement** — Permanent cancellation of a carbon credit from a registry, allowing the retiring buyer to claim the credit's benefit.
- **TREES (REDD+ Environmental Excellence Standard)** — ART's jurisdictional REDD+ methodology. v2.0 was CCP-approved in December 2024.
- **VCMI (Voluntary Carbon Markets Integrity Initiative)** — Demand-side governance body; develops the Claims Code of Practice.
- **VCS (Verified Carbon Standard)** — Verra's main standard. Largest VCM standard globally. CCP-Eligible.
- **Verra** — VCM standard organization, founded 2005. Operates VCS, JNR, and Plastic Standard. Largest by issuance.
- **VVB (Validation/Verification Body)** — Accredited third-party that validates project designs and verifies monitoring data.

### Fuel-VCM additions (Ch. 8 Part 8)

- **Additionality inversion** — The richer the compliance revenue stack, the weaker the case for a voluntary credit on top. Maximum commercial viability implies minimum additionality.
- **Attribute (environmental attribute)** — The claimable emissions-reduction value of a fuel. Once a compliance regime claims it (via a RIN, LCFS credit, or mandate), it cannot also be sold as a voluntary credit without double-claiming.
- **Book-and-claim** — Mechanism for separating a fuel's environmental attribute from its physical molecules, enabling cross-geography voluntary claims and Scope 3 accounting.
- **Double counting — three distinct failures** — (1) Double issuance: two credits for the same tonne. (2) Double claiming: the same reduction toward two goals. (3) Double monetization: paid twice for the same environmental good.
- **Financial additionality** — A project clears its hurdle only when credit revenue is included; documented at the FID moment.
- **Negative CI** — A fuel CI score below zero; structurally a counterfactual avoidance claim embedded in a lifecycle score, with the same integrity vulnerabilities as VCM avoidance credits.
- **Regulatory-closure risk / stranding risk** — A VCM revenue stream built on a regulatory gap terminates when regulation arrives and claims the attribute.
- **Unit mismatch (per-gallon vs. per-tonne)** — RIN and 45Z are per gallon; LCFS and VCM are per tCO₂e. SAF certificate price (~$1,500–3,500/tCO₂e) is a scarcity premium, not a stackable abatement price. Always convert to one unit before comparing.

---

# Sources and currency

This chapter cites figures that are current as of writing (May 2026) and will move. The most time-sensitive claims, to be re-verified against primary sources and tracked via `CHANGELOG.md`:

| Claim | Value as stated | As-of | Primary source to verify against |
|---|---|---|---|
| Total VCM transaction value | ~$1.5–2 billion | 2024 | Ecosystem Marketplace / MSCI Carbon Markets |
| N-GEO nature-based price collapse | >$15 (mid-2022) → <$1/tCO₂e (mid-2024) | mid-2024 | CME/ICE N-GEO futures |
| CCP-approved issuance | ~51M credits; ~4% of 2024 volume | Oct 2025 | ICVCM |
| CCP price premium | 30–60%; ~47% Tier 1 vs Tier 3 | Q3 2025 | ClearBlue Markets / Calyx Global |
| CCP-eligible programs | six programs; ~98% of market share | May 2024 | ICVCM |
| SBTi Corporate Net-Zero Standard V2 | second consultation; final expected mid–late 2026 | Nov 2025 | SBTi |
| REDD+ integrity range | ~30–50% of legacy credits represent real benefit (vs. "90% worthless" headline) | 2025–26 consensus | West et al. 2020/2023; Guizar-Coutiño et al. 2022; Mitchard et al. 2023 |
| Removal price tiers | DAC ~$500–1,500; biochar ~$80–200; BECCS ~$150–300/tCO₂e | 2025–26 | CDR.fyi / Frontier disclosures |
| Frontier coalition commitments | $1B+ | 2025 | Frontier |

---

# What's next

This completes the markets pair (compliance + voluntary). Two natural next moves:

- **Chapter 9 (Carbon Pricing)** — broader treatment of how carbon gets priced across instruments: carbon taxes, internal corporate prices, social cost of carbon, carbon-tariffs, border adjustments, the economics of carbon pricing.
- **Chapter 10 (CCUS)** — the carbon capture, utilization, and storage technology landscape: post-combustion, pre-combustion, oxy-fuel, direct air capture, the economics, the project landscape, the major commercial CCUS projects (mostly EOR), the new wave of dedicated geological storage.

Or jump to whatever you want to read.

