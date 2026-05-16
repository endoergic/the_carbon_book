# Chapter 5 — Emissions Accounting: The Rosetta Stone

**Track:** Climate Liability (B)
**Prerequisites:** Chapter 1 (CO₂e, GWP, GHG basket). Helpful but not required: Chapters 2–4.
**What you should be able to do by the end:**
- Define Scope 1, 2, and 3 emissions and identify which scope a given emission source belongs to, including for ambiguous cases (leased assets, electricity, embedded supply chain).
- Distinguish the two Scope 2 reporting methods (location-based and market-based) and explain what each is for.
- Walk through the GHG Protocol's organizational boundary approaches (equity share, financial control, operational control) and explain when they give different answers.
- Define and distinguish *avoided*, *reduced*, and *removed* emissions, and identify which can legitimately be netted against a company's emissions inventory.
- Explain financed emissions, PCAF, and the *33% facilitated emissions* weighting convention.
- Read a corporate climate disclosure (Scope 1/2/3 numbers, target framing, methodology footnotes) and identify the three or four places where the disclosure could be misleading without technically being wrong.
- State the current status of major accounting standards: GHG Protocol revisions (mid-2026 draft, ~2027 final), PCAF 3rd edition (Dec 2025), ISSB IFRS S1/S2 (21+ jurisdictions adopting), SBTi CNZS V2 (final 2026), and how they relate to one another.

---

## Why this chapter exists

The chapters so far have established the physical carbon problem (Ch. 1), the materials commodity economy (Ch. 2), the CO₂ infrastructure economy (Ch. 3), and the fossil fuel value chain (Ch. 4). Everything to come — carbon markets, climate policy, corporate net-zero claims, climate finance, disclosure regulation — runs on a single piece of plumbing: **how emissions are counted**.

Emissions accounting is the rosetta stone. When someone says "we cut emissions 40%" or "our portfolio is aligned to 1.5°C" or "the bank financed $300M of emissions" or "the offset retired 1,000 tCO₂e," those claims are only as meaningful as the accounting underneath them. The accounting choices shape the markets, the regulations, the incentives, and ultimately the climate outcomes.

This chapter is the most technical of the curriculum so far, and also the most important for reading anything else. Once you have a working model of Scope 1/2/3, control vs. equity share, location-based vs. market-based, financed vs. facilitated, avoided vs. reduced vs. removed — you can read any climate disclosure, any net-zero pledge, any market integrity controversy, and locate the substantive question fast. Without it, you're at the mercy of the framing.

I'll be more terms-and-definitions heavy here than elsewhere because the precision matters. I'll also flag the contested edges: emissions accounting has more genuine analytical controversy embedded in it than most non-specialists realize, and the ongoing GHG Protocol and SBTi revisions are touching all of them.

---

# Part 1: The basic architecture — Scope 1, 2, 3

## Where the scopes come from

The architecture of corporate GHG accounting was set by the **Greenhouse Gas Protocol Corporate Accounting and Reporting Standard**, first published in 2001 and revised in 2004. The GHG Protocol is a joint initiative of the **World Resources Institute (WRI)** and the **World Business Council for Sustainable Development (WBCSD)**, originally founded in 1997. The Corporate Standard introduced the three-scope structure that has dominated corporate emissions accounting ever since.

The framing was elegant and has held up remarkably well: divide a company's emissions into three layers based on *control* and *causation*:

**Scope 1 — Direct emissions.** Emissions from sources the company *owns or operationally controls*. The flames coming out of the company's smokestacks. Trucks the company owns. The natural gas the company burns in its boilers. Fugitive methane from the company's gas pipelines. If a company sold all its assets to someone else, Scope 1 emissions would move with them.

**Scope 2 — Energy indirect emissions.** Emissions from the *generation of electricity, heat, steam, or cooling that the company purchases*. A data center buying grid electricity has Scope 2 emissions equal to the emissions from the power plant supplying that electricity (or some allocation thereof). The company didn't burn the fuel; the power plant did. But because the company's demand caused the power plant to burn the fuel, the emissions are attributed to the buyer.

**Scope 3 — Other indirect emissions.** Everything else in the value chain. This is the catch-all and by far the largest category for most non-utility companies. The emissions of the company's suppliers (upstream Scope 3). The emissions caused by the use of the company's products (downstream Scope 3). The emissions of employees commuting and travelling. The emissions of waste disposal. The emissions of financial investments. Scope 3 is divided into **15 categories** under the GHG Protocol's Corporate Value Chain (Scope 3) Accounting and Reporting Standard, published in 2011 — and a 16th category is being added in the current revision (more on this below).

## The point of the three-scope structure

The reason the GHG Protocol drew the lines this way: it wanted a system where *every emission gets counted somewhere, but no single emission gets double-counted* across companies.

A coal-fired power plant's emissions are the power company's Scope 1. The same emissions, attributed by electricity sold, are the customers' Scope 2. The fuel burned in the plant was upstream Scope 3 for the power company (Category 3: Fuel- and energy-related activities) and downstream Scope 3 for the coal mining company (Category 11: Use of sold products). If you summed all the world's corporate inventories, the same physical CO₂ molecule would appear several times — but at different positions in different companies' inventories.

This is intentional. The GHG Protocol calls the three scopes a **"complementary framework"**: it's not arithmetic, it's a *system of accountability*. A coal company can't say "we don't emit; our customers do" — that's exactly what downstream Scope 3 captures. An electricity buyer can't say "we don't emit; the power plant does" — that's Scope 2. The framework lets each company see the emissions it influences and creates pressure points for action up and down the value chain.

The corollary: you cannot **add up corporate Scope 1+2+3 emissions across companies and get to the global total**. That math doesn't work. National emissions inventories (which feed into IPCC reports and UNFCCC submissions) are constructed completely differently — they're territorial, attributing emissions to where the activity physically occurred, with no Scope 2 or 3.

## What goes in Scope 1

Scope 1 covers four categories under the GHG Protocol:

- **Stationary combustion.** Fuel burned in facilities owned or controlled by the company: boilers, furnaces, generators, kilns. The output is CO₂ plus smaller amounts of CH₄ and N₂O.
- **Mobile combustion.** Fuel burned in company-owned vehicles, ships, aircraft, equipment. Same gases.
- **Process emissions.** GHGs released by chemical or physical processes other than fuel combustion. Cement (CO₂ from calcining limestone), ammonia (CO₂ from H₂ production via steam methane reforming), aluminum (PFCs from anode effects in smelting), refrigerants (HFCs from leaks).
- **Fugitive emissions.** Unintentional releases. Methane from natural gas pipelines and compressor stations. Refrigerant leaks from cooling systems. SF₆ leaks from electrical equipment.

Scope 1 is usually the easiest scope to measure, because the company directly controls the activity. It's also the scope where third-party verification is most rigorous — assurance providers can inspect facilities, audit fuel purchase records, and verify combustion emission factors.

For most companies in most sectors, **Scope 1 is a small fraction of total emissions**. The exceptions: heavy industry (steel, cement, chemicals, refining), upstream oil and gas, electric utilities, freight transport, agriculture. For these sectors, Scope 1 is the dominant emission category.

## What goes in Scope 2

Scope 2 covers emissions from purchased energy:
- **Electricity** (the dominant component for most companies).
- **Heat or steam** (district heating, industrial steam from a third party).
- **Cooling** (chilled water from a district cooling system).

The accounting question is non-trivial: when a company plugs into a grid, what emissions should be attributed to its consumption? The grid is a mix of generation sources, the mix varies by time of day and season, and the same electricity could in principle have come from many sources. The GHG Protocol's 2015 **Scope 2 Guidance** introduced two methods that must both be reported (a "dual reporting" requirement):

**Location-based method.** Uses an average emission factor for the grid in the geographic location where the electricity was consumed. A facility in West Virginia (coal-heavy grid) has higher Scope 2 than the same load in Norway (hydro-dominated grid) — *regardless* of what the buyer claims to have procured. This method captures physical reality.

**Market-based method.** Uses emission factors that reflect the company's contractual instruments for electricity supply: RECs (renewable energy certificates), PPAs (power purchase agreements), green tariffs, on-site generation. If a company buys renewable energy contractually, those contracts "claim" the clean attributes and the company's market-based Scope 2 is reduced.

Both methods have to be reported because they answer different questions:
- Location-based: *what physical emissions resulted from this consumption?*
- Market-based: *what is the company doing to drive clean electricity through procurement?*

The market-based method has been the subject of ongoing controversy. The criticism: a company can buy cheap unbundled RECs from a wind project that would have been built anyway, retire them against its Scope 2, and claim "100% renewable" without changing actual electricity flows. This is the **"REC washing"** critique. The defense: REC markets create demand signals that incentivize new renewable build over time, even if the marginal-impact mechanism is weaker than direct procurement.

The GHG Protocol is currently revising the Scope 2 Guidance — a public consultation ran from October 2025 through January 2026. Proposed changes include moving from annual to **hourly matching** (24/7 carbon-free energy), tightening **geographic** boundaries on RECs to match physical grid realities, and creating a hierarchy of emission factors that prefers more granular data. If adopted, this would substantially raise the bar for "100% renewable" claims. Final revised Scope 2 Guidance is expected in 2027.

The Emissions First Partnership (a group including Amazon and Meta) has separately proposed an alternative framework that would emphasize the *carbon impact* of electricity procurement rather than the megawatt-hour matching framework. This is in active tension with the 24/7 matching approach, and the GHG Protocol revisions will resolve which framework dominates for the next decade.

## What goes in Scope 3

Scope 3 is divided into 15 categories under the 2011 Standard:

**Upstream Scope 3** (emissions in the supply chain before the company touches the product):
1. **Purchased goods and services** — the embodied emissions of everything the company buys.
2. **Capital goods** — embodied emissions of long-lived assets (factories, vehicles, IT infrastructure).
3. **Fuel- and energy-related activities** — upstream emissions of the fuels and electricity the company buys (extraction, transport, refining — but excluding the actual combustion, which is in the company's Scope 1 or 2).
4. **Upstream transportation and distribution** — third-party logistics moving goods *into* the company.
5. **Waste generated in operations** — disposal of company waste.
6. **Business travel** — employee business travel on third-party transport.
7. **Employee commuting** — employees going to and from work.
8. **Upstream leased assets** — emissions from leased assets not counted in Scope 1 or 2.

**Downstream Scope 3** (emissions after the company sells the product):
9. **Downstream transportation and distribution** — third-party logistics moving goods *to* customers.
10. **Processing of sold products** — emissions when customers further process intermediate goods.
11. **Use of sold products** — emissions from customers using the product (the big one for fuel producers, automakers, appliance makers).
12. **End-of-life treatment of sold products** — disposal or recycling of products at end of life.
13. **Downstream leased assets** — emissions from assets the company leases to others.
14. **Franchises** — emissions of franchisees not counted in Scope 1 or 2.
15. **Investments** — emissions of the company's equity, debt, and project investments (the big one for financial institutions).

**A 16th category is being added** in the current revision (Phase 1 progress update, March 2026): **Other value chain activities not captured in categories 1–15**. This is meant to capture things like *facilitated emissions* (capital-markets underwriting by banks), licensing of intellectual property, and other emissions sources that don't cleanly fit the original 15. PCAF Parts A, B, and C are the calculation methodology referenced by Category 16 for the financial-sector activities.

For most non-financial companies, **Categories 1 (purchased goods) and 11 (use of sold products) dominate Scope 3 — often together representing 60–80% of total Scope 3.** For a software company, business travel and purchased services might be larger. For an oil major, Category 11 (when customers burn the fuel) is typically 80%+ of total emissions. For a bank, Category 15 (financed emissions) is over 99% of total.

## **Stop-and-check 5.A**

1. A company owns a refinery that burns natural gas to produce gasoline. The gasoline is sold to motorists who burn it in cars. Categorize each of these emissions sources by scope:
   - The natural gas burned at the refinery
   - The electricity the refinery buys from the grid
   - The methane released from the refinery's faulty valves
   - The emissions when motorists burn the gasoline
   - The emissions from the trucks that delivered the crude oil to the refinery
2. Why does the GHG Protocol require dual reporting (location- and market-based) for Scope 2? What questions do the two methods answer?
3. A company shows large reductions in Scope 2 emissions year-over-year because they bought unbundled RECs from a wind farm that was already operating. What's the integrity issue here, and what would a more rigorous accounting approach require?
4. **Socratic prompt:** ExxonMobil's Scope 1+2 emissions are about 120 MtCO₂e/yr. Its Scope 3 Category 11 emissions are about 570 MtCO₂e/yr. If ExxonMobil commits to "net zero by 2050" but only specifies Scope 1+2, what fraction of its actual climate impact is the commitment addressing? What should you ask the company before treating its commitment as credible?

---

# Part 2: Organizational boundaries — who owns what

Before you can count any of a company's emissions, you have to define *which entities count as part of the company*. A corporation with subsidiaries, joint ventures, leased facilities, and minority equity stakes faces a real boundary question. The GHG Protocol offers three approaches:

**Equity share approach.** Account for emissions in proportion to the company's *ownership interest* in each entity. A 60% stake in a joint venture gets 60% of the JV's emissions. This approach aligns with how financial accounting often treats partial ownership. Used in some sectors (especially oil and gas) where joint ventures are common.

**Financial control approach.** Account for 100% of emissions from any entity where the company has *financial control* — the power to direct financial and operational policies. This typically matches financial consolidation: if the entity rolls up in your audited financials, you take 100% of its emissions.

**Operational control approach.** Account for 100% of emissions from any entity where the company has *operational control* — the power to introduce and implement operating policies. The most common choice in practice, because it aligns with the practical question of "what can the company actually influence?"

These three approaches give different answers for the same set of facts. Consider an oil major with a 30% stake in a refinery joint venture where it has operational control. Under equity share: 30% of the refinery's emissions. Under financial control: 0% (the company doesn't financially consolidate it). Under operational control: 100% (the company operates the facility).

Companies must declare which approach they use and apply it consistently. Changes in approach require restatement of base-year inventories. The GHG Protocol's current revision is considering whether to **limit options** for organizational boundary setting to improve comparability across companies. The expected direction: greater standardization on a subset of approaches (likely operational control plus, for some sectors, equity share), with stricter documentation requirements for whichever is chosen.

## Why this is genuinely contested

The boundary choice has substantive emissions implications. Consider a private-equity sponsor that holds majority stakes in 50 portfolio companies. Under operational control: probably zero Scope 1 emissions (the sponsor doesn't operate any portfolio company day-to-day). Under equity share: substantial emissions reflecting the sponsor's ownership stake in each portfolio company. Under financial control: probably zero again (most PE structures don't financially consolidate portfolio companies in the sponsor's accounts).

Critics argue that "operational control" lets financial-control-only owners escape responsibility for emissions they could in principle influence as owners. Defenders argue that emissions accounting is meant to capture *what an entity can actually change* — and financial owners typically have less direct influence on day-to-day operations than operators.

Either way, the choice of boundary approach is the single biggest leverage point in a corporate emissions inventory, and it should be one of the first things you check when reading a disclosure.

---

# Part 3: Inventories vs. targets vs. claims

A common source of confusion: emissions accounting produces three distinct artifacts, which serve different purposes and have different rules.

## The inventory

A corporate emissions inventory is a *backward-looking measurement* of emissions during a reporting period (typically a calendar year). It says: *during 2024, this company emitted X MtCO₂e across these scopes and categories.* An inventory is meant to be a faithful reflection of what happened.

The GHG Protocol Corporate Standard sets five principles for inventory preparation: **relevance, completeness, consistency, transparency, accuracy** — with relevance and completeness being the most contested in practice. Relevance asks whether the inventory captures emissions that genuinely reflect the company's activities; completeness asks whether the inventory excludes material sources that should have been included.

Inventories are subject to **assurance** — independent third-party verification. The level of assurance varies: **limited assurance** is a moderate-confidence opinion based on review procedures; **reasonable assurance** is a high-confidence opinion based on more rigorous audit-style procedures. Most jurisdictions that mandate climate disclosure require limited assurance initially, often transitioning to reasonable assurance over a phased timeline (typically 3–5 years).

## The target

A *target* is a *forward-looking commitment* to achieve a certain emissions outcome by a certain date. Targets can be:

- **Absolute** (reduce total emissions by X% from a base year) — the cleanest and most demanding form.
- **Intensity** (reduce emissions per unit of output or revenue) — allows total emissions to grow if output grows faster. SBTi requires intensity targets to be supplemented by absolute alignment.
- **Carbon-neutral or net-zero** by a specified date — implies residual emissions are offset or removed.
- **Aligned to a specific temperature pathway** (1.5°C, well-below-2°C) — under SBTi or similar frameworks.

A common slip: companies report inventories *and* set targets, but the two don't always use the same accounting basis. A company might report its 2024 inventory using operational control, then set a target using equity share — or vice versa. The 2025 GHG Protocol revisions are pushing toward requiring consistency between inventory and target accounting bases, with explicit justification when they differ.

## The claim

A *claim* is a *public communication* about emissions or climate action. "We are carbon neutral." "Our products have a 30% lower carbon footprint." "We've cut emissions in half." Claims can be based on inventories and targets, but the relationship is often loose — and this is where greenwashing concerns concentrate.

The SBTi V2 draft (November 2025) takes a markedly different approach to claims than V1: it specifies categories of claims that companies can make based on different types of validated targets, with **standardized language** required for each. The goal is to prevent the gap between what a company has technically achieved and what its marketing implies.

## Why this matters

The inventory tells you what happened. The target tells you what the company plans. The claim tells you what the company says. These three should be tightly coupled, but in practice they're often loose — and the looseness is where misleading-but-technically-true communication lives. When you read a climate disclosure:

- *What is the inventory?* (Scopes, methodology, assurance level)
- *What is the target?* (Absolute or intensity, base year, scope coverage, alignment claim)
- *What is the claim?* (And does it accurately reflect what the inventory and target show?)

Inconsistency among these three is the single most common pattern of corporate greenwashing.

---

# Part 4: Financed emissions — the bank problem

For financial institutions, **Scope 3 Category 15 (Investments)** isn't just a category — it's essentially the entire emissions footprint. A bank's Scope 1 (its branches, its corporate jets) and Scope 2 (the electricity in its branches) are typically less than 1% of its total emissions. **The other 99%+ comes from financed emissions: the emissions of the companies and projects the bank lends to, invests in, or insures.**

This is the famous "**99% rule**" for financial institutions. Wherever a bank's emissions go — up, down, sideways — what's actually happening is driven by changes in its portfolio composition, not by its own operations. The narrative shift in climate finance over the past five years has been the recognition that *banks' real emissions are in their balance sheets*, not their buildings.

## PCAF — the methodology

The **Partnership for Carbon Accounting Financials (PCAF)** is an industry-led initiative founded in 2015 in the Netherlands that has become the global standard-setter for financial-sector emissions accounting. PCAF's **Global GHG Accounting and Reporting Standard for the Financial Industry** is now in its **3rd edition (December 2025)** and is the reference methodology cited by GHG Protocol Scope 3 Category 15.

The standard divides financial-sector emissions into three parts:

- **Part A — Financed Emissions.** Emissions associated with lending and investment activities. The original PCAF standard; methodologies for ten asset classes.
- **Part B — Facilitated Emissions.** Emissions associated with capital-markets activities (underwriting bond and equity issuances). Introduced in 2023.
- **Part C — Insurance-Associated Emissions.** Emissions associated with re/insurance underwriting. Methodologies expanded in December 2025 to cover treaty reinsurance and project insurance.

PCAF uses an **attribution factor**: for each financial relationship, what fraction of the borrower/investee's emissions belongs to the financial institution? Typical formulas:

- **For lending and equity:** attribution = outstanding loan or equity / total enterprise value (or in some cases total debt + equity)
- **For project finance:** attribution = financial institution's share of the project financing
- **For mortgages:** attribution based on outstanding loan / property value
- **For motor vehicle loans:** attribution based on loan share of vehicle value

The result: a financial institution can report, for each financial product, *its portion of the financed entity's emissions*. Summing across the portfolio gives the institution's financed emissions inventory.

## The 33% facilitated emissions weighting

Banks' capital-markets activities (underwriting bond issues, IPOs, secondary offerings) create exposure to the same emissions as direct lending, but the bank doesn't hold the asset on its balance sheet. PCAF treats these as a separate category — **facilitated emissions** — and applies a **33% weighting** to acknowledge that capital-markets activities involve less ongoing exposure than direct financing.

This 33% number is a compromise that nobody is fully happy with. Critics argue it understates the climate impact of underwriting fossil-fuel bond issuances (the bank facilitated the financing that enabled emissions). The industry argues that even 33% overstates a bank's responsibility for emissions it didn't hold on balance sheet. The number reflects political negotiation more than science, and it will probably be revisited in future PCAF revisions.

## The December 2025 PCAF update

PCAF released its 3rd edition in December 2025 with several substantive changes:

- **Four new asset class methodologies:** use-of-proceeds structures (green bonds and similar), securitizations and structured products, sub-sovereign debt, and optional reporting for undrawn loan commitments under IFRS S1/S2.
- **Two new insurance methodologies:** treaty reinsurance and project insurance (all-risk policies for construction).
- **Inventory fluctuation guidance** — new reporting recommendations to address year-over-year volatility from market price movements, since PCAF attribution factors are denominated in enterprise value.
- **Supplemental guidance on avoided and forward-looking emissions** — for separate (not netted) reporting of financed avoided emissions.

This is now the operational reference for any financial institution's Scope 3 Category 15 reporting. The forthcoming **GHG Protocol Scope 3 revision** explicitly references PCAF for the new Category 16 (other value chain activities) — the first time the GHG Protocol has named-checked a third-party standard in its own standard text.

## The volatility problem

A subtle issue with PCAF: because the attribution factor uses enterprise value (EV) as a denominator, a bank's financed emissions can swing dramatically based on changes in *equity prices*, not just changes in underlying physical emissions. A bank holding equity in an oil company will see its attributed emissions *rise* if the oil company's share price falls (smaller denominator), even though the physical emissions of the oil company didn't change.

This **inventory fluctuation** issue is mathematically annoying and politically inconvenient — banks reporting rising financed emissions in a down-market year look bad without having done anything wrong. The December 2025 PCAF update introduced new reporting recommendations (fluctuation analysis, inflation adjustment) to address this, but doesn't solve the underlying issue. The deeper question — whether enterprise-value attribution is the right approach at all, or whether it should be replaced with a different denominator — is unresolved.

## **Stop-and-check 5.B**

1. A US bank has $100B in loans to oil and gas companies. Under PCAF, what determines the bank's financed emissions from these loans — and what data does the bank need from the oil/gas companies?
2. The 33% weighting on facilitated emissions is described as "a compromise nobody is fully happy with." What's the substantive question this is trying to answer, and what are the arguments for a higher or lower weighting?
3. If a bank's stock-financed emissions go up because equity prices fell (without any change in underlying physical emissions), is the bank's climate performance worse, better, or unchanged? What does this say about whether PCAF is measuring the right thing?
4. **Socratic prompt:** A bank announces it will reduce financed emissions by 50% by 2030. List four different ways it could achieve this on paper without actually reducing the climate impact of its lending.

---

# Part 5: Avoided, reduced, and removed — the three things that aren't the same

One of the most common sources of misleading climate claims is the conflation of three different concepts: **avoided emissions**, **reduced emissions**, and **removed emissions**. Each is real, each has a legitimate use case, but they answer different questions and cannot substitute for each other in net-zero accounting.

## Reduced emissions

*Reduced emissions* = the difference between what the company's emissions are now and what they were in a previous period.

A factory that emitted 100 ktCO₂ in 2020 and emits 80 ktCO₂ in 2024 has *reduced* emissions by 20 ktCO₂/yr. The reduction is measured against a *base year* — typically a year the company designates as the baseline for tracking progress.

Reduced emissions are the most rigorous form of climate progress. The company is genuinely emitting less. The atmospheric stock is genuinely growing more slowly than it otherwise would. This is what climate policy is actually trying to achieve.

The integrity question: was the base year well-chosen? If a company picks a base year that happened to be a peak emissions year (post-COVID recovery, for example), it can show big reductions without much underlying improvement. SBTi and the GHG Protocol both require base-year selection to be representative and stable, with rebaselining when structural changes occur. The current GHG Protocol revisions are tightening rules around base-year recalculation.

## Avoided emissions

*Avoided emissions* = the difference between actual emissions and what emissions *would have been* under some counterfactual scenario.

A wind farm that generates 1 TWh of electricity "avoids" the CO₂ that would have been emitted if that 1 TWh had come from a fossil fuel source. The avoidance is *counterfactual* — it depends on what you compare against. Different baselines give different avoided-emissions numbers. The "natural gas comparison" gives a smaller number than the "coal comparison."

Avoided emissions are useful for *project-level* climate impact assessment: "this project, compared to a credible counterfactual, displaces X tCO₂ of emissions." They're how carbon credit projects (Ch. 8) measure their climate benefit. They're how green investments are evaluated.

But avoided emissions **cannot be subtracted from a company's emissions inventory**. The GHG Protocol is unambiguous about this: avoided emissions are reported *separately* from inventory emissions, never netted. A company that sells wind turbines can report large *avoided* emissions from its products (downstream Scope 3, in some sense), but those avoidance numbers don't reduce its own Scope 1, 2, or 3 inventory.

PCAF's December 2025 update added explicit guidance on this: financial institutions can report "financed avoided emissions" as a forward-looking metric, but only separately from financed emissions. Never netted. Never substituted.

This rule is broken constantly in corporate marketing. "Our products avoided 100 MtCO₂" is not the same as "We emitted 100 MtCO₂ less." The first is a counterfactual comparison; the second is an actual change. Many companies present the first as if it were the second, which is misleading.

## Removed emissions

*Removed emissions* = emissions that were physically taken out of the atmosphere through a removal action.

A direct air capture (DAC) facility removes CO₂ from the atmosphere and stores it geologically. A reforestation project pulls CO₂ from the atmosphere into biomass and (sometimes) soil. A BECCS facility captures combustion CO₂ from biomass and stores it geologically. These are all *removals*.

Removals can legitimately be netted against gross emissions to compute *net* emissions. A company emitting 1,000 ktCO₂/yr and purchasing 200 ktCO₂/yr of permanent removals has net emissions of 800 ktCO₂/yr. The math works because removal is the physical inverse of emission — same molecule, opposite direction.

But there are three subtleties:

**1. Permanence matters.** Removing CO₂ from the atmosphere and storing it for 100 years (a forest that might burn) is not the same as storing it for 10,000+ years (geological sequestration). SBTi's V2 draft is increasingly pushing for *durable* removals to match the durability of the emissions being neutralized. Fossil emissions release CO₂ that will affect the atmosphere for thousands of years; only similarly-durable removals should be used to neutralize them.

**2. Quality matters.** Some removal projects (especially nature-based projects) have had integrity problems — overstating baseline emissions, double-counting credits, claims that didn't reflect physical reality. The voluntary carbon market scandals of 2022–2023 (Ch. 8) hit removal credits especially hard.

**3. Order of operations matters.** SBTi V2 (and most rigorous net-zero frameworks) require companies to *first* reduce gross emissions through direct action, *then* use removals only to neutralize residuals. Buying lots of removal credits while continuing to emit at high levels is the textbook greenwashing pattern.

## The hierarchy

The cleanest way to think about these three:

| Type | Counts toward inventory reduction? | Best use |
|---|---|---|
| Reduced | Yes — directly | Tracking actual progress |
| Avoided | No — separate disclosure only | Counterfactual project analysis |
| Removed | Yes — can be netted against gross emissions | Neutralizing residual emissions in net-zero claims |

When you read a corporate climate claim, ask: *which of these is the company actually doing?* "Carbon neutral" claims often mix the three. "Net zero" claims should be using reduced + removed, never avoided. Net-zero credibility hinges on the order: deep reductions first, then removals for residuals, with no avoidance-substitution in the inventory math.

---

# Part 6: The current state of the standards — who runs what, who's revising what

This is the live status of the major standards as of mid-2026, because corporate emissions accounting is in a period of unusually active revision.

## GHG Protocol

The Greenhouse Gas Protocol is the foundational reference: the **Corporate Accounting and Reporting Standard (2004)**, the **Corporate Value Chain (Scope 3) Standard (2011)**, the **Scope 2 Guidance (2015)**, and the **Project Accounting Protocol (2005)**. It is co-owned by WRI and WBCSD and managed by a Steering Committee, Independent Standards Board, and Technical Working Groups.

The Protocol has not been substantively updated since 2011 (Scope 3) and 2015 (Scope 2). A comprehensive revision is underway:

- **Public consultation period:** completed 2022–2023.
- **Technical Working Groups:** began work September 2024; 42 meetings on Scope 3, 37 on Corporate Standard through end of 2025.
- **ISO partnership:** announced September 2025. ISO will harmonize its 14064 series with GHG Protocol revisions; ISO technical staff joined GHG Protocol TWGs in Q1 2026.
- **Phase 1 Progress Updates:** Corporate Standard published December 2025; Scope 3 published March 2026.
- **Public consultation on draft standards:** expected mid-2026.
- **Final revised standards:** expected late 2027.
- **Transition period:** likely a 2–3 year phase-in after final publication.

Substantive proposed changes:
- **Scope 3 95% coverage rule.** Required Scope 3 emissions must cover at least 95% of categories 1–15; exclusions must be quantified, disclosed, and justified.
- **New Category 16** — other value chain activities. Includes facilitated emissions for banks, licensing, and other previously-uncategorized exposures. References PCAF for financial-sector methodologies.
- **Stricter data quality tiering.** Companies must disaggregate reported emissions by data type (e.g., supplier-specific vs. industry-average) to enable comparison.
- **Tightened Scope 2 rules** — moving toward hourly matching, geographic granularity, hierarchy of emission factors.
- **Boundary setting harmonization** — fewer options for organizational boundary choice.

## ISSB (IFRS S1 and S2)

The **International Sustainability Standards Board (ISSB)** was created by the IFRS Foundation in November 2021 to develop a global baseline of sustainability disclosure standards. ISSB issued its first two standards in **June 2023**:

- **IFRS S1 — General Requirements for Disclosure of Sustainability-related Financial Information.** Covers governance, strategy, risk management, and metrics & targets across all material sustainability topics.
- **IFRS S2 — Climate-related Disclosures.** Specific requirements for climate disclosure, including Scope 1, 2, 3 GHG emissions reporting and scenario analysis.

IFRS S2 effectively replaces the TCFD recommendations as the global framework for climate disclosure. It uses the GHG Protocol as the basis for emissions accounting requirements.

**Adoption status (January 2026):**
- **21+ jurisdictions** have adopted IFRS S1/S2 on a mandatory or voluntary basis. Adopters include Brazil, Canada, Mexico, Chile, Qatar, Singapore, Hong Kong, Japan, Malaysia, Australia, New Zealand, Turkey, Thailand, Nigeria, Kenya, and others.
- **An additional 16+ jurisdictions** are in process. China issued a climate standard based on IFRS S2 in December 2025 (without a mandatory timeline yet).
- **The European Union** is following its own ESRS framework (European Sustainability Reporting Standards) but maintaining interoperability with IFRS S2.
- **The United States:** the SEC's federal climate disclosure rule was withdrawn in 2025 after sustained litigation. There is no federal mandate. **California's SB 253** (Climate Corporate Data Accountability Act) became effective January 2026, requiring large companies doing business in California to report Scope 1, 2, and (by 2027) Scope 3 emissions. California's framework references the GHG Protocol and is broadly compatible with IFRS S2.

In December 2025, the ISSB issued **targeted amendments to IFRS S2** to address implementation challenges, particularly around GWP values (jurisdictional relief allowing different IPCC assessment-cycle values) and reducing duplicative reporting where local frameworks already cover GHG disclosure.

The ISSB is not itself an emissions-accounting standard — it's a *disclosure* standard that references the GHG Protocol for emissions calculation. But its global adoption means that GHG Protocol changes will increasingly cascade into mandatory disclosure regimes worldwide.

## SBTi (Corporate Net-Zero Standard)

The **Science Based Targets initiative** is a partnership between CDP, WWF, the UN Global Compact, and the World Resources Institute, founded in 2015. SBTi develops target-setting standards: how a company aligns its emissions targets with the Paris Agreement.

SBTi's flagship is the **Corporate Net-Zero Standard (CNZS)**, originally published October 2021, currently at Version 1.3.

**Version 2 status:**
- **First consultation draft:** March 2025.
- **Second consultation draft:** November 2025 (more substantive, with technical annexes).
- **Public consultation:** ran through December 12, 2025.
- **Final V2:** expected mid-to-late 2026.
- **Mandatory adoption** for new target submissions: January 1, 2028.
- **V1.3** remains valid for existing targets and new targets through December 31, 2027.

Substantive proposed changes in V2:
- **Two company categories.** "Category A" (large- and medium-sized companies in high-income countries) faces stricter requirements; "Category B" (smaller companies, or in lower-income countries) faces more flexibility.
- **Scope-specific target setting.** Separate target requirements for Scope 1, 2, and each Scope 3 category, rather than aggregate scope targets.
- **Ongoing Emissions Responsibility (OER).** Replaces "Beyond Value Chain Mitigation" (BVCM). Companies are encouraged (initially voluntary; mandatory from 2035) to take responsibility for emissions during their net-zero transition through carbon credits — with explicit tiers of recognition.
- **Removal requirements.** By 2035, an increasing share of long-lived removals required. By net-zero target year, all residual emissions must be neutralized by removals (not avoidance credits).
- **Climate Transition Plans** mandatory for Category A companies, with publication within 12 months of validation.
- **Third-party assurance** mandatory for Category A.
- **Cyclical target validation** every five years (proposed in some drafts).

The OER replacement of BVCM is the biggest substantive shift. Under V1.3, BVCM was voluntary and loosely-defined ("companies should support climate action beyond their value chain"). Under V2, OER is a structured framework with explicit tiers and timelines.

## PCAF

Covered in Part 4. Current edition: **3rd edition, December 2025**. The de facto Scope 3 Category 15 calculation reference, now formally cited by GHG Protocol in the new Category 16 framework.

## ISO 14064 / 14067 / 14068

The **ISO 14060 series** is the international standardization body's framework for GHG accounting and verification. Notable standards:

- **ISO 14064-1** (organization-level emissions inventories) — broadly aligned with GHG Protocol.
- **ISO 14064-2** (project-level emissions reductions) — paralleling GHG Protocol Project Accounting Protocol.
- **ISO 14064-3** (verification) — defines assurance procedures.
- **ISO 14067** (product carbon footprints) — for individual products.
- **ISO 14068** (carbon neutrality) — published November 2023, defines what a "carbon neutrality" claim requires. Stricter than many corporate self-declared carbon neutrality claims.

A new **ISO 14060 (Net Zero Aligned Organizations)** standard is in development and expected to launch at COP30 in November 2025. Combined with the ISO-GHG Protocol harmonization announced September 2025, this should reduce the proliferation of competing net-zero frameworks over the next several years.

## The big picture

The standards landscape is in unusually active flux, but the direction of travel is convergent:

- **GHG Protocol revisions** tighten methodology and expand scope coverage.
- **ISSB IFRS S2** provides the disclosure baseline now adopted in 20+ jurisdictions.
- **PCAF** is the operational reference for financial-sector emissions, now formally embedded in GHG Protocol.
- **SBTi V2** raises the target-setting bar with scope-specific targets, mandatory transition plans, and structured OER.
- **ISO 14060 series** is being aligned with GHG Protocol; ISO 14068 codifies stricter "carbon neutrality" requirements.

The 2027–2028 transition will be substantial. Most current corporate net-zero pledges and emissions inventories will need revision to meet the post-revision standards. Companies that built reporting systems on the 2011 Scope 3 Standard or the 2015 Scope 2 Guidance will face significant rework.

## **Stop-and-check 5.C**

1. The GHG Protocol revisions are introducing a 95% Scope 3 coverage requirement. What does this rule out, and why is it significant?
2. The SBTi V2 draft replaces "Beyond Value Chain Mitigation" with "Ongoing Emissions Responsibility." What's substantively different about OER, and why does the change matter?
3. The US has withdrawn its federal climate disclosure rule, but California has implemented SB 253 effective January 2026. What does this say about the durability of climate disclosure regimes in the absence of federal coordination?
4. **Socratic prompt:** A company has invested heavily in building reporting systems aligned to the current (2011/2015) GHG Protocol standards. With the 2027 revisions coming, should it pause the buildout, accelerate it, or restructure it now in anticipation of the new standards? Which choice carries which risks?

---

# Part 7: Reading a corporate climate disclosure — a worked example

To pull this all together, let's walk through how to read a corporate climate disclosure with informed skepticism. I'll describe a generic pattern rather than name a specific company — the patterns are widely applicable.

## What you typically find

A typical corporate climate disclosure (in the company's annual report, 10-K, or standalone sustainability report) includes:

1. **Headline narrative** — "Our climate strategy is aligned to 1.5°C," "We are committed to net zero by 2050," etc.
2. **Scope 1, 2, 3 emissions** — usually a table with year-over-year comparison.
3. **Scope 2 dual reporting** — location-based and market-based.
4. **Scope 3 breakdown** — by some subset of the 15 categories.
5. **Target progress** — performance against previously-stated targets.
6. **Methodology footnotes** — accounting choices, boundaries, base year, GWP vintage.
7. **Assurance statement** — auditor's opinion, including scope and confidence level.

## What to actually look for

Working through the disclosure:

**Step 1: What's the organizational boundary?**
Operational control? Financial control? Equity share? Has it changed? If the company restructured (acquired/divested entities), did it restate prior-year numbers?

**Step 2: What's the Scope 3 coverage?**
How many of the 15 categories are reported? For a non-financial company, expect Categories 1 (purchased goods) and 11 (use of sold products) to be the dominant ones. If either is missing or implausibly small, that's a red flag.

**Step 3: What's the Scope 2 methodology breakdown?**
Are location- and market-based both reported? Is the "market-based" reduction credible? Look for the renewable-energy procurement mechanism — direct PPAs and on-site generation are stronger than unbundled RECs.

**Step 4: What's the target methodology?**
Absolute or intensity? Base year? Coverage (Scope 1 only? 1+2? 1+2+3?). Aligned to a temperature target via what framework (SBTi-validated? Self-declared?). How does target accounting relate to inventory accounting?

**Step 5: What's the claim language?**
"Net zero" vs. "carbon neutral" vs. "climate positive" vs. "net negative." Each implies different things. "Net zero" implies emissions reduction + removal of residuals. "Carbon neutral" historically includes avoidance offsets, which under newer standards is being constrained. "Climate positive" is largely a marketing term without standardized definition.

**Step 6: What's the offset/removal strategy?**
If the company is using carbon credits, what type? Avoidance (renewables, REDD+, methane abatement)? Removal (DAC, BECCS, reforestation)? Durability? Vintage? Issuance standard (Verra, Gold Standard, Puro.earth)? Quality matters enormously; many credits issued in the 2018–2022 window have integrity problems (Ch. 8).

**Step 7: What's the assurance level?**
Limited assurance means the auditor did review-level procedures and didn't find anything wrong. Reasonable assurance means audit-level procedures and a stronger opinion. Many companies start with limited assurance and only Scope 1+2 — Scope 3 coverage and reasonable assurance come later, if at all.

## The most common misleading patterns

In corporate climate disclosure, the four patterns to watch for:

**1. Scope 3 truncation.** Reporting Scope 1+2 in detail, mentioning Scope 3 only briefly or partially. For most companies, Scope 3 is 60–90% of total emissions. A disclosure that under-covers Scope 3 may technically comply with current standards but materially understates climate impact.

**2. Market-based Scope 2 via unbundled RECs.** Showing dramatic Scope 2 reductions from purchasing low-quality RECs that don't correspond to additional renewable generation. Defensible under current standards, but the 2025–2026 GHG Protocol revisions are tightening this.

**3. Avoidance credits netted against gross emissions.** Treating avoided emissions as if they reduce inventory emissions. Specifically prohibited under GHG Protocol, but common in carbon-neutral claims.

**4. Inconsistent boundaries.** Reporting inventory on operational control while setting targets on equity share, or vice versa. Each individually may be defensible, but the combination obscures comparability.

You don't need to be an accountant to spot these. The patterns are predictable, and once you recognize them, you can read any corporate disclosure with much more critical sophistication.

## **Stop-and-check 5.D**

1. A company's Scope 1+2 reported emissions are 500 ktCO₂e. Its Scope 3 reported emissions are 200 ktCO₂e. The company is a consumer products manufacturer. What's likely wrong with this disclosure?
2. A company's market-based Scope 2 is 50 ktCO₂e while its location-based Scope 2 is 800 ktCO₂e. What does this tell you about the company's renewable-energy procurement, and what would you want to ask?
3. A company claims "we achieved carbon neutrality in 2024 through a combination of operational improvements and high-quality offsets." What questions would you ask to assess the credibility of this claim?
4. **Socratic prompt:** If you had to design a corporate climate disclosure regime from scratch, knowing the patterns of misleading disclosure that have emerged, what three features would you require? Defend each.

---

# Closing exercise

I want you to attempt three things:

**1. Categorize from memory.** For each of the following emissions sources, identify the scope:
- A bakery's natural gas oven
- A bakery's grid electricity
- The wheat the bakery buys from a farm
- The disposal of the bakery's used cooking oil
- The emissions from customers driving to the bakery
- The emissions of a bond issuance the bakery's parent company underwrites (if the parent is a bank)

**2. Three-paragraph explanation.** Without notes, explain (a) why Scope 3 is the largest category for most companies, (b) why the choice of market-based vs. location-based Scope 2 matters, and (c) why "avoided emissions" cannot be netted against an inventory.

**3. Honest uncertainty.** What are the three or four areas where you'd want to dig into the underlying standards rather than trust this summary? My candidates: (1) the proposed Scope 3 95% coverage rule and how exclusions are quantified, (2) PCAF's enterprise-value attribution and the inventory-fluctuation problem, (3) the GHG Protocol Scope 2 revision and the 24/7 vs. annual matching debate, (4) the SBTi V2 OER framework and how "ongoing emissions" interact with net-zero claims. Pick any of these and read primary sources.

---

# What this chapter simplified

**1. "Scope 1+2+3 covers everything."** Not quite. The scopes have boundary disputes, especially around indirect emissions that fall in multiple categories. Category 3 (Fuel- and energy-related activities) overlaps with Category 11 (Use of sold products) for fuel producers. Category 1 (Purchased goods) overlaps with Category 2 (Capital goods) for some procurement patterns. The 95% rule helps, but the underlying overlap-and-gap problems are real.

**2. "PCAF is the standard for financial institutions."** PCAF is the most widely-used, but it's not the only one. Some specialized methodologies (NZIA for insurance, for instance) coexist. The PCAF-GHG Protocol formal alignment in 2025–2026 should reduce fragmentation, but local variants persist.

**3. "Standards are converging."** The big-picture story is convergence (GHG Protocol-ISO partnership, PCAF as the financial reference, ISSB as the disclosure baseline). But within each standard family, ongoing revisions are creating substantive divergence in the short term: SBTi V1.3 vs. V2, GHG Protocol 2011 vs. 2027, PCAF 2nd vs. 3rd edition. The 2025–2028 period is a discontinuity, not a smooth transition.

**4. "GWP values are fixed."** GWP-100 values shift across IPCC assessment cycles. CH₄ GWP was 25 (AR4), 28 (AR5), 30 (AR6, fossil origin). Regulatory regimes use different vintages — the EU ETS used AR4 until recently, US EPA uses a mix. The 2025 ISSB amendments to IFRS S2 explicitly allow jurisdictional relief on GWP vintages. Numbers can shift by 5–20% just from GWP vintage choices.

**5. "Scope 3 is straightforward in principle."** It's nightmarishly complex in practice. Category 1 (purchased goods) requires emissions data from thousands of suppliers, most of whom don't have inventories themselves. Category 11 (use of sold products) requires assumptions about how customers will use products over their lifetime. The proposed 95% coverage rule is aggressive given the data infrastructure that currently exists.

---

# Glossary delta (Chapter 5)

- **Assurance (limited / reasonable)** — Independent third-party verification of an emissions disclosure. Limited assurance is review-level; reasonable assurance is audit-level.
- **Attribution factor (PCAF)** — The fraction of a borrower/investee's emissions assigned to a financial institution. Usually outstanding loan or equity divided by enterprise value.
- **Avoided emissions** — Counterfactual: difference between actual emissions and what emissions would have been under a stated baseline scenario. Reported separately from inventories, never netted.
- **Beyond Value Chain Mitigation (BVCM)** — Voluntary climate action a company takes outside its value chain (e.g., funding reforestation). Being replaced in SBTi V2 by Ongoing Emissions Responsibility (OER).
- **Category 15 (Investments)** — Scope 3 category covering emissions of a company's investments. Dominant for financial institutions (>99% of total emissions).
- **Category 16** — New Scope 3 category being added in GHG Protocol revision. Covers other value chain activities including facilitated emissions, licensing, and IP-related emissions.
- **Climate Transition Plan** — A company's published plan for transitioning its operations and value chain consistent with its climate targets. Mandatory under SBTi V2 for Category A companies and increasingly required under regulatory disclosure regimes.
- **Corporate Standard (2004)** — The GHG Protocol Corporate Accounting and Reporting Standard, foundational reference for corporate emissions accounting.
- **Equity share approach** — Organizational boundary approach that accounts for emissions in proportion to ownership stake.
- **Facilitated emissions** — Emissions associated with a financial institution's capital-markets activities (bond/equity underwriting), as distinct from direct lending. Weighted at 33% under PCAF.
- **Financed emissions** — Emissions associated with a financial institution's lending and investment activities (Scope 3 Category 15).
- **Financial control approach** — Organizational boundary approach that accounts for 100% of emissions from entities the company financially controls.
- **GHG Protocol** — Greenhouse Gas Protocol; co-managed by World Resources Institute (WRI) and World Business Council for Sustainable Development (WBCSD). Foundational emissions accounting standards body.
- **IFRS S1 / S2** — International Sustainability Standards Board's first two standards (June 2023). S1 covers general sustainability disclosure; S2 covers climate. Adopted in 21+ jurisdictions as of January 2026.
- **ISO 14060 series** — International Organization for Standardization's GHG accounting and verification standards. 14064 (organizations and projects), 14067 (products), 14068 (carbon neutrality).
- **ISSB** — International Sustainability Standards Board, created by IFRS Foundation in 2021. Issues IFRS S1 and S2.
- **Location-based Scope 2** — Scope 2 reporting using grid-average emission factors for the location of consumption. Reflects physical reality.
- **Market-based Scope 2** — Scope 2 reporting using contractual instruments (RECs, PPAs, green tariffs). Reflects company procurement choices.
- **Operational control approach** — Organizational boundary approach that accounts for 100% of emissions from entities the company operationally controls.
- **PCAF** — Partnership for Carbon Accounting Financials, founded 2015. Industry-led standard-setter for financial-sector emissions. 3rd edition published December 2025.
- **PCAF Parts A, B, C** — Financed Emissions (Part A), Facilitated Emissions (Part B), Insurance-Associated Emissions (Part C).
- **Ongoing Emissions Responsibility (OER)** — SBTi V2 framework replacing BVCM. Companies take structured responsibility for emissions during transition, with explicit tiers and post-2035 mandatory requirements.
- **PPA (Power Purchase Agreement)** — Contract for procurement of electricity from a specific generator, often used to claim renewable energy under market-based Scope 2.
- **REC (Renewable Energy Certificate)** — Tradeable instrument representing the environmental attributes of 1 MWh of renewable electricity. Unbundled RECs (separated from physical electricity) are increasingly controversial.
- **Reduced emissions** — Actual emissions in current period minus actual emissions in base year. The cleanest form of climate progress.
- **Removed emissions** — CO₂ physically taken out of the atmosphere through removal action (DAC, BECCS, reforestation, etc.). Can be netted against gross emissions when permanent and high-quality.
- **SBTi (Science Based Targets initiative)** — Joint initiative of CDP, WWF, UN Global Compact, WRI, founded 2015. Develops corporate target-setting standards. Corporate Net-Zero Standard (CNZS) is flagship.
- **Scope 1 / Scope 2 / Scope 3** — The three-tier emissions structure of the GHG Protocol Corporate Standard. Scope 1: direct emissions. Scope 2: purchased energy. Scope 3: other value chain.
- **Scope 3 Standard (2011)** — GHG Protocol Corporate Value Chain (Scope 3) Accounting and Reporting Standard. Defines 15 categories of value chain emissions.
- **Scope 2 Guidance (2015)** — GHG Protocol guidance introducing location-based vs. market-based dual reporting.
- **TCFD (Task Force on Climate-related Financial Disclosures)** — 2017 framework for climate-related financial disclosure. Effectively replaced by IFRS S2 in 2023.
- **WBCSD** — World Business Council for Sustainable Development, co-manages GHG Protocol with WRI.
- **WRI** — World Resources Institute, co-manages GHG Protocol with WBCSD.

---

# What's next

The accounting plumbing is now in place. The next chapters use it:

- **Chapter 6 (Carbon Policy History 1988–2015)** — how international and national climate policy developed and what shaped the institutional landscape that emissions accounting now operates within.
- **Chapter 7 (Compliance Carbon Markets)** — emissions trading systems (EU ETS, California, RGGI, China, UK). Where emissions are priced.
- **Chapter 8 (Voluntary Carbon Markets)** — the offset markets. Where Reduced, Avoided, and Removed emissions are bought and sold, and where most market integrity controversies live.
- **Chapter 13 (Corporate Net Zero and Disclosure)** — a deeper dive on how corporate climate strategy is actually structured under all the standards above.

