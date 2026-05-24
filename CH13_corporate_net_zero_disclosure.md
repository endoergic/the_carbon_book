# Chapter 13 — Corporate Net Zero and the Disclosure Regime

**Track:** Climate Liability → Forward View (B + C)
**Prerequisites:** Chapter 5 (emissions accounting — scopes, the avoided/reduced/removed distinction), Chapter 8 (voluntary carbon markets — credits, integrity, the removal/avoidance split). Helpful: Chapter 7 (compliance markets for contrast).
**What you should be able to do by the end:**
- Distinguish a *net-zero* target from *carbon neutral*, *science-based*, and *Paris-aligned* — and work out which one a given corporate claim actually is.
- Explain what the SBTi Corporate Net-Zero Standard requires (near-term + long-term targets, deep absolute reductions, residual neutralization with removals) and what the V2 revision changes.
- Map the global disclosure architecture: the ISSB (IFRS S1/S2) as the baseline, the EU's CSRD/ESRS, California's SB 253/261, and the collapsed US SEC rule — who must report what, where, and when.
- Explain the transition-plan concept (TPT, GFANZ) and why a target without a plan is not credible.
- Identify the legal exposure around green claims (EU Green Claims and Empowering Consumers directives, the FTC Green Guides, ASA/ACCC actions) and how it interacts with the voluntary market.

---

## Why this chapter exists

Everything in the previous eight chapters — the accounting rules, the policy history, the compliance and voluntary markets — comes to a point inside individual companies. A firm decides what to count, what to disclose, what to promise, and what to buy. That decision is where the abstractions of "Scope 3" and "additionality" and "removal credit" turn into a line in an annual report and, increasingly, a legal obligation.

This chapter is about that decision layer: the **corporate net-zero claim** and the **disclosure regime** that is rapidly forming around it. It is the chapter where the question "what does it actually mean when a company says 'net zero by 2040'?" finally gets a precise answer — and where you learn that the honest answer is "it depends entirely on which framework, if any, the company is actually following."

Two things have changed the landscape decisively in the 2020s. First, a private standard-setter — the **Science Based Targets initiative (SBTi)** — became the de facto arbiter of what counts as a credible corporate climate target, validating targets for thousands of companies. Second, climate disclosure shifted from voluntary to **mandatory** in major jurisdictions, anchored by the new **International Sustainability Standards Board (ISSB)** and the EU's reporting law. As of 2026 this transition is mid-stream, contested, and politically polarized: the EU has just *retrenched* its own rules under competitiveness pressure, the US federal rule has *collapsed*, and California is pressing ahead under litigation. The result is not a single global regime but a fractured map that every multinational has to navigate at once.

I'll organize this in seven parts: the net-zero taxonomy; SBTi as standard-setter; the disclosure architecture and the ISSB baseline; the EU stack and its 2025 retrenchment; the US patchwork; transition plans and financed emissions; and the law of green claims.

---

# Part 1: What "net zero" actually means

## A taxonomy of climate claims

The single most useful thing this chapter can give you is the ability to disambiguate four terms that are routinely used as if they were synonyms. They are not.

**Carbon neutral.** A balance claim: the entity's gross emissions over some period are matched by an equal quantity of offsets (carbon credits retired). It says nothing about whether the entity reduced its own emissions, what *kind* of credits it bought, or whether the claim is consistent with any temperature goal. Historically this was the dominant corporate claim, usually achieved cheaply with avoidance credits (Ch. 8). It is the claim most exposed to the 2022–2024 integrity crisis, and the one regulators are now scrutinizing hardest.

**Net zero.** A *state* in which an entity's residual emissions are balanced by an equal quantity of carbon *removals* — not avoidance — typically reached after deep absolute reductions. The crucial difference from carbon-neutral: net zero requires (a) reducing emissions as far as technically possible first, and (b) neutralizing only the genuinely residual remainder, and (c) doing so with removals durable enough to match the atmospheric lifetime of the emission. Net zero is a destination; carbon-neutral is an annual accounting identity.

**Science-based.** A target whose *trajectory* is consistent with a defined global carbon budget (typically 1.5°C). "Science-based" describes the steepness and endpoint of the reduction pathway, not the use of offsets. A target validated by SBTi is "science-based" in this technical sense.

**Paris-aligned.** The loosest of the four. It usually means "consistent with the goals of the Paris Agreement," but because Paris itself is a bottom-up framework of national pledges (Ch. 6), "Paris-aligned" has no single quantitative definition and is often used as marketing varnish.

The practical skill is reverse-engineering which of these a company actually means. "We are carbon neutral today" almost always means offsets, often low-quality. "We have a net-zero target validated by SBTi for 2040 with interim 2030 targets" is a far stronger claim. "We are committed to a Paris-aligned future" may mean nothing enforceable at all.

## The mitigation hierarchy and the abatement/neutralization split

Underneath the credible version of net zero sits a sequencing rule inherited from environmental policy generally: the **mitigation hierarchy**. In order of priority: *avoid* emissions, *reduce* the ones you can't avoid, and only then *neutralize* the genuinely unavoidable residual.

This maps onto a distinction the disclosure world cares about enormously:

- **Abatement** — cuts to the company's own value-chain emissions (Scopes 1, 2, 3). This is the part that actually changes the physical world inside the firm's boundary.
- **Neutralization** — removing CO₂ from the atmosphere and durably storing it, to balance residual emissions *at the net-zero target year*. Under credible standards this must be **removals**, not avoidance credits, because only removals physically take carbon back out (Ch. 5, Ch. 8).
- **Compensation / "beyond value chain mitigation"** — paying for climate action *outside* the company's own footprint during the transition (e.g., buying avoidance credits while you decarbonize). This is encouraged as additional, but under credible standards it cannot substitute for either abatement or end-state neutralization.

The whole corporate-climate argument of the 2020s turns on these distinctions. A company can buy a million dollars of cheap avoidance credits and call itself carbon-neutral — but that does not count as abatement, does not count as neutralization, and increasingly does not protect it from a greenwashing claim. Understanding *why* requires understanding the institution that drew these lines: SBTi.

## **Stop-and-check 13.A**

1. A consumer-goods company's packaging says "carbon neutral." A competitor's annual report says "net-zero target for 2045, validated, with a 2030 interim target of 50% absolute Scope 1+2 reduction." Which claim tells you more, and what specifically does each leave unspecified?
2. Why does credible net zero insist on *removals* (not avoidance credits) for the residual at the target year? Tie your answer to the permanence argument from Chapter 8.
3. "Paris-aligned" has no single quantitative definition. Is that a flaw in the term, a flaw in the Paris Agreement, or neither?
4. **Socratic prompt:** A company genuinely cannot abate the last 10% of its emissions with current technology. Is "net zero" even the right goal for it, versus a transparent "90% reduction plus durable removal of the rest"? What work is the word "zero" doing?

**Answers**

1. The net-zero claim tells you far more. It specifies a target year (2045), an interim milestone (50% absolute Scope 1+2 reduction by 2030), and that it was independently validated — so you know the trajectory's steepness and that abatement, not offsetting, is doing the work. The "carbon neutral" packaging is an annual balance claim: it says gross emissions were matched by retired offsets but is silent on whether the company reduced anything, what kind of credits it used (avoidance vs. removal), and whether the claim aligns with any temperature goal. Notably, even the stronger claim leaves Scope 3 unstated.

2. Permanence is the crux. A net-zero state must balance a residual emission with a removal durable enough to match that emission's atmospheric lifetime. Avoidance credits do not physically take carbon back out of the air — they at best prevent a future emission elsewhere — so they cannot offset a tonne already emitted. Chapter 8's permanence argument holds that a short-lived or reversible "avoided" tonne cannot be set against a long-lived emitted one without an integrity gap. Only durable removals genuinely neutralize the residual at the target year.

3. Neither, really — it reflects what Paris is. Because the Paris Agreement is a bottom-up framework of nationally determined contributions rather than a single quantified global target, "Paris-aligned" has no fixed numerical meaning to inherit. The looseness is a faithful description of an intentionally flexible treaty, not a defect in either the phrase or the agreement. The problem is purely in usage: the term gets deployed as marketing varnish precisely because its vagueness lets a company imply rigor without committing to a measurable pathway.

4. "Zero" is doing aspirational and rhetorical work that the physics may not support. For a firm with a genuinely unabatable 10%, the honest description is "90% reduction plus durable removal of the residual" — which is exactly what credible net zero means anyway. The word "zero" risks implying the emissions vanished rather than were balanced by removals, and it invites the suspicion that the residual is being neutralized cheaply. The goal is sound; the framing should foreground the abatement percentage and the durability of the removal, so "zero" does not paper over what is actually happening.

---

# Part 2: SBTi — the de facto standard-setter

## What SBTi is

The **Science Based Targets initiative** is a partnership (CDP, the UN Global Compact, World Resources Institute, and WWF) that, since 2015, has developed criteria for corporate emissions targets and validated companies' targets against them. It has no statutory authority. Its power is entirely reputational and market-based: a validated SBTi target became, over the late 2010s and 2020s, the signal that a corporate climate target was serious. Thousands of companies have set or committed to SBTi targets, and many procurement and investor frameworks reference SBTi validation directly.

This is itself a remarkable governance fact: the most consequential definition of "credible corporate net zero" was written not by a regulator but by an NGO coalition — much as the ICVCM and VCMI (Ch. 8) became private quasi-regulators of the voluntary market.

## What the Corporate Net-Zero Standard requires

The **Corporate Net-Zero Standard** (current published version V1.x; V2 in process — see below) requires, in essence:

- **Near-term targets** — typically a 5–10 year horizon, requiring absolute emissions cuts on a 1.5°C-aligned trajectory (historically ~4.2%/year linear, i.e., roughly 42% by 2030 from a recent base year), across Scopes 1, 2, and material Scope 3.
- **Long-term targets** — reducing emissions by roughly **90%** (the deep-decarbonization endpoint) by the net-zero target year, no later than 2050 for the standard pathway.
- **Neutralization of residuals** — the remaining ~10% must be neutralized with carbon removals at the target year.
- **The mitigation hierarchy** — abatement comes first; offsets cannot be counted toward the required reductions.

Two things that surprise newcomers: SBTi targets are mostly about *absolute reductions inside the value chain*, and offsets play almost no role in reaching them. The headline "net zero" is overwhelmingly an abatement commitment, with removals reserved for a small residual.

## Scope 3 — the hard part

For most companies, the overwhelming majority of emissions are **Scope 3** (value-chain emissions — suppliers upstream, product use downstream; Ch. 5). SBTi requires material Scope 3 to be covered, and this is where the framework bites and where companies struggle. A bank's financed emissions, an automaker's tailpipe emissions from sold vehicles, an oil major's emissions from combusted product — these dwarf the company's own operations and are only partly within its control. The tractability of Scope 3 target-setting is the central technical battleground of the V2 revision.

## The 2024 "offset wars"

In April 2024, SBTi's board issued a statement signaling openness to allowing greater use of environmental-attribute certificates (including carbon credits) against **Scope 3** targets. The reaction was immediate and internal: SBTi's own technical staff and many stakeholders objected that this would weaken the abatement-first principle and effectively re-admit offsets through the back door. The episode exposed a genuine fault line — between those who see offsets as a pragmatic bridge for hard-to-abate Scope 3 and those who see any offset allowance as undermining the standard's integrity. It also exposed governance fragility at the institution that had become the market's referee.

## V2 and "Ongoing Emissions Responsibility"

The **Corporate Net-Zero Standard V2** has been through two public consultations (the second closing **12 December 2025**), with the final standard expected in **2026** and mandatory for new targets from **1 January 2028** (companies may keep using V1.3 until end-2027). Its most consequential proposed changes:

- **Ongoing Emissions Responsibility (OER)** — a reframing that encourages (eventually requires, for the largest companies) firms to take responsibility for their emissions *during* the transition, not only at the net-zero endpoint — through carbon credits / beyond-value-chain action — without letting that substitute for abatement. This is the same concept Ch. 8 flagged as bifurcating voluntary demand.
- **Differentiated Scope 3 treatment** — more workable rules for the categories companies genuinely struggle to control, including a shift toward target metrics other than pure absolute tonnage where appropriate.
- **Tiered company treatment** — larger companies and those in higher-income jurisdictions face stricter requirements sooner.
- **Rising removal share** — an increasing fraction of residual neutralization must come from durable removals as the target year approaches, with no avoidance credits eligible for end-state neutralization.

The net effect, if finalized as drafted, is to *strengthen* the abatement-first core while creating a structured, optional role for credits during the transition — and to push corporate demand decisively toward durable removals (Ch. 8, Ch. 11). The unresolved tension: the stricter the standard, the more companies quietly decline to set targets at all.

## **Stop-and-check 13.B**

1. SBTi has no legal authority, yet it became the arbiter of credible corporate net zero. What gave it that power, and what could take it away?
2. For most companies Scope 3 is the majority of emissions and the least controllable. Why does that make Scope 3 simultaneously the most important and the most gameable part of a target?
3. The 2024 "offset wars" pitted "abatement purists" against "pragmatists." Steelman each side in two sentences.
4. **Socratic prompt:** V2's "Ongoing Emissions Responsibility" asks companies to pay for climate action during the transition without counting it toward their reduction target. Is this a meaningful integrity improvement, or does it just re-label the old carbon-neutral purchasing? What would make it credible?

**Answers**

1. SBTi's power is purely reputational and market-based. With no statutory authority, it became the arbiter because a validated SBTi target turned into the trusted signal that a corporate climate commitment was serious — and because investors, procurement frameworks, and corporate peers began referencing that validation directly, giving it network effects. The same forces could take it away: a loss of credibility (the 2024 offset-wars governance crisis showed how fragile that trust is), a competing standard that the market prefers, or mandatory disclosure regimes that supersede a voluntary validator. Its authority lasts only as long as the market keeps treating its stamp as meaningful.

2. Scope 3 is most important because for most firms it is the overwhelming majority of emissions — a bank's financed emissions, an automaker's tailpipe emissions, an oil major's combusted product — so a target excluding it addresses only a sliver of the real footprint. It is most gameable for the same reasons it is hard: the emissions are only partly within the company's control, the data is estimated rather than metered, and boundaries can be drawn to flatter the number. A target that covers everything controllable but omits the uncontrollable majority can look ambitious while leaving the bulk of impact untouched.

3. The purist case: abatement-first is the entire point of a science-based target; admitting credits against Scope 3 reopens the back door to cheap offsets, lets companies buy their way out of genuine value-chain decarbonization, and erodes the standard that gives SBTi its credibility. The pragmatist case: some Scope 3 categories are genuinely intractable on a 1.5°C timeline with today's technology, so a rigid abatement-only rule drives companies to either set no target or quietly miss it — a structured credit allowance keeps them engaged and channels finance to real mitigation in the interim.

4. It is a meaningful improvement only if the structural separation holds in practice. OER differs from old carbon-neutral purchasing in that the spending explicitly does not count toward the reduction target — abatement is still measured and required on its own. That is the integrity feature. The risk is that it collapses back into "pay and claim" if companies foreground the OER spending in their marketing while quietly under-delivering on abatement. Credibility would require: transparent separation of abated tonnes from compensated tonnes, a rising removal share for end-state neutralization, and no permission to advertise OER purchases as progress toward the target.

---

# Part 3: The disclosure architecture and the ISSB baseline

## From voluntary to mandatory

For most of the 2010s, corporate climate disclosure was voluntary and fragmented: companies reported to **CDP** (formerly the Carbon Disclosure Project), adopted the **TCFD** (Task Force on Climate-related Financial Disclosures) recommendations, and chose among a thicket of competing standards (GRI, SASB, etc.). The result was abundant but inconsistent disclosure — hard to compare, easy to cherry-pick.

The late 2020s consolidation has two moves: **convergence** of the voluntary alphabet soup into a single global baseline, and **mandation** of that baseline by individual jurisdictions.

## The TCFD framework — the conceptual backbone

The TCFD (2017) gave the field its durable conceptual structure: disclose climate-related information across four pillars — **governance, strategy, risk management, and metrics & targets** — and, critically, frame climate as a *financial* risk to the business (transition risk, physical risk) rather than purely an environmental externality. TCFD did its job so well that it was **absorbed into the ISSB** in 2023–2024; the task force was disbanded and its monitoring role handed to the IFRS Foundation. When you see "TCFD-aligned," read it as "uses the four-pillar structure now carried forward by the ISSB."

## The ISSB and IFRS S1/S2

The **International Sustainability Standards Board (ISSB)** was created under the IFRS Foundation (the body behind global accounting standards) in 2021 to build a global baseline for sustainability disclosure — the sustainability analogue of international accounting standards. It published its first two standards in June 2023:

- **IFRS S1** — general requirements for disclosure of sustainability-related financial information.
- **IFRS S2** — climate-specific disclosures, building directly on the TCFD four pillars and requiring disclosure of Scope 1, 2, and (where material) Scope 3 emissions, plus transition plans and the financial effects of climate risk.

The ISSB's design philosophy is **single materiality** (sometimes "financial materiality"): it asks what climate information is material *to investors* — i.e., to the enterprise's financial prospects. This is the crucial contrast with the EU's approach (Part 4).

The ISSB itself can't compel anyone; it provides standards that jurisdictions then adopt or reference. By 2025–2026 a substantial and growing list of jurisdictions — across Asia-Pacific, the UK, Canada, Brazil, and others — had committed to adopting or building on IFRS S1/S2, making it the closest thing to a global disclosure lingua franca. The major exceptions: the EU (which built its own, broader regime first) and the US (where the federal effort collapsed).

## The three questions every disclosure regime answers differently

To compare regimes, ask three questions:

1. **Materiality** — single (investor-focused) or double (investor *and* environment/society)?
2. **Scope 3** — required, conditional, or excluded?
3. **Assurance** — must the data be independently audited, and to what level (limited vs. reasonable)?

These three axes explain almost all the divergence between the ISSB baseline, the EU stack, and the US patchwork.

## **Stop-and-check 13.C**

1. TCFD reframed climate from "environmental externality" to "financial risk to the business." Why was that reframing so effective at driving adoption — and what does it leave out?
2. The ISSB uses single (financial) materiality. Give an example of a climate impact that is material to *society* but might not be material to a specific company's *investors*.
3. Why does jurisdictional adoption matter so much for a body (the ISSB) that has no enforcement power of its own?
4. **Socratic prompt:** If you were a finance minister in a mid-sized economy in 2026, would you adopt IFRS S1/S2 wholesale, adapt it, or wait? What's the cost of fragmentation versus the cost of moving early?

**Answers**

1. By framing climate as transition and physical risk to the enterprise's own financial prospects, TCFD moved climate from the CSR/sustainability silo into the language of investors, auditors, and CFOs — people with the authority and incentive to act, and a fiduciary reason to demand the data. That financial framing drove rapid adoption and ultimately absorption into the ISSB. What it leaves out is the other direction of materiality: the company's impact on climate and society, which may be enormous even where it is not financially material to the firm. Single-materiality framing renders those externalities largely invisible.

2. A company whose operations emit substantial methane or whose product drives downstream deforestation may impose large costs on society and the climate that never register as a financial risk to the firm itself — because the harm falls on third parties, is diffuse, or is unlikely to rebound onto the company's cash flows within the horizon investors price. Under single (financial) materiality such an impact can be legitimately omitted; under the EU's double materiality it must be disclosed as impact-material even if it is not financially material.

3. The ISSB writes standards but cannot compel anyone, so its reach depends entirely on jurisdictions choosing to adopt or reference IFRS S1/S2 in their own law. Its value comes from convergence: the more jurisdictions mandate the same baseline, the more comparable global disclosure becomes and the more it functions as a lingua franca. Without adoption it is just a well-designed template. This is why the growing list of adopting jurisdictions across Asia-Pacific, the UK, Canada, and Brazil matters more for the ISSB's influence than the quality of the standards alone.

4. The decisive trade-off is comparability and credibility versus cost and optionality. Adopting wholesale gives instant access to the emerging global baseline, lowers reporting friction for multinationals operating in your market, and signals seriousness to investors — at the cost of flexibility to tailor rules to local capacity. Waiting avoids early compliance costs and lets you watch the EU/US fragmentation settle, but risks being a non-comparable outlier and importing whatever standard your largest trading partners later impose anyway. For a mid-sized economy, adapting IFRS S1/S2 — adopting the core, phasing in Scope 3 and assurance — usually dominates, capturing comparability while managing capacity.

---

# Part 4: The EU stack — and its 2025 retrenchment

## CSRD and ESRS

The EU went furthest, earliest, and broadest. The **Corporate Sustainability Reporting Directive (CSRD)**, adopted 2022, vastly expanded both *who* must report and *what* they must report, replacing the earlier Non-Financial Reporting Directive. Reporting is done against the **European Sustainability Reporting Standards (ESRS)**, of which **ESRS E1** is the climate standard — the most detailed mandatory climate-disclosure standard in the world, covering transition plans, Scope 1/2/3, targets, and the financial effects of climate.

Two features distinguish the EU regime:

- **Double materiality.** Companies must report both how climate affects the business (financial materiality, the ISSB question) *and* how the business affects climate and society (impact materiality). This is a fundamentally broader remit than the ISSB baseline.
- **Breadth and extraterritoriality.** As originally designed, the CSRD would have pulled in tens of thousands of EU companies and many large non-EU companies with significant EU operations.

## The Omnibus retrenchment (2025–2026)

Then the politics turned. Under intense competitiveness pressure — the argument that the reporting burden was hobbling European firms relative to US and Chinese competitors — the European Commission launched a **simplification ("Omnibus")** package in early 2025. The sequence matters and is current as of writing:

- A **"stop-the-clock"** directive (2025) delayed reporting obligations for companies not yet in the first wave.
- A political deal between the Council and Parliament was struck on **9 December 2025**, and the resulting **Amendment Directive (EU) 2026/470** was published **26 February 2026**, entering into force **18 March 2026**.
- The package **sharply raised the scope thresholds**: broadly, EU companies are now in scope at **>1,000 employees and >€450 million net turnover** — dramatically fewer companies than the original CSRD. Non-EU groups come into scope on an EU-turnover test (~€450m) from FY2028 (reporting 2029).
- **Mandatory reporting** under the revised regime applies for financial years starting on or after **1 January 2027**; the largest "wave 1" companies continue reporting under the existing framework for FY2024–2026.
- **ESRS simplification** is underway: EFRAG delivered revised draft standards in late 2025, with the Commission committed to adopting the revised Set 1 ESRS within six months of the Amendment Directive's entry into force (around **September 2026**).

The Omnibus is the single most important corporate-disclosure development of the period, and its lesson is structural: **mandatory climate disclosure is politically reversible.** The EU did not abandon the project — double materiality and ESRS E1 survive — but it materially narrowed it under competitiveness and cost-of-compliance pressure. Anyone modeling the future of disclosure has to price in that the ratchet can loosen, not only tighten.

## **Stop-and-check 13.D**

1. Explain double materiality with a concrete example where the "impact" direction and the "financial" direction give different answers.
2. The 2025 Omnibus raised CSRD thresholds so that far fewer companies report. Is this a defensible simplification or a substantive weakening? Argue both sides.
3. The EU built its own regime (ESRS) rather than adopting the ISSB baseline. What did it gain, and what did global comparability lose?
4. **Socratic prompt:** "Mandatory disclosure is politically reversible." Given the Omnibus, how should an investor who relies on CSRD data adjust their expectations for the next decade?

**Answers**

1. Consider a fertilizer plant near a watercourse. The "impact" direction (impact materiality) asks how the plant's emissions and effluent affect climate and the surrounding ecosystem — potentially large, and reportable under the EU's double-materiality regime regardless of the financial hit to the firm. The "financial" direction asks how climate affects the plant's prospects — perhaps modestly, if regulation is lax and physical risk is distant. The two diverge: a significant societal/environmental impact can coincide with a small financial materiality, so single-materiality (ISSB) reporting would omit what double-materiality (ESRS) requires.

2. Both sides are arguable. Defensible simplification: the original CSRD would have pulled in tens of thousands of firms, many too small to bear over a thousand ESRS data points; raising thresholds to >1,000 employees and >€450m turnover concentrates the burden on companies with the resources to report well and the emissions worth tracking, improving signal-to-noise. Substantive weakening: it removes a large swath of mid-sized companies — and much aggregate emissions and supply-chain coverage — from mandatory disclosure entirely, and the precedent that the regime bends under competitiveness pressure invites further erosion.

3. By building ESRS the EU gained double materiality — disclosure of the company's impact on climate and society, not just climate's financial effect on the company — plus the most detailed mandatory climate standard in the world, tailored to its policy goals and adopted first. What global comparability lost is a common baseline: ESRS diverges from IFRS S1/S2 in materiality concept, breadth, and data points, so a multinational must reconcile two regimes and investors cannot cleanly compare EU filers against ISSB-baseline filers. The EU traded interoperability for ambition and first-mover control.

4. An investor should treat CSRD data as durable in substance but variable in coverage and scope. The Omnibus showed the regime can narrow — fewer reporting companies, simplified data points — so the dataset may thin out, lose comparability across waves, and shift definitions mid-stream. The prudent adjustment: do not assume a fixed reporting universe or stable data fields year over year, build in the possibility of further loosening, lean on the surviving core (double materiality and ESRS E1 persist), and supplement with other sources (ISSB-baseline filings, California data) rather than treating any single mandate as a permanent fixture.

---

# Part 5: The US patchwork

## The SEC climate rule: rise and collapse

The US federal effort is a cautionary tale. The **SEC adopted a climate-disclosure rule on 6 March 2024**, requiring registrants to disclose material climate risks, certain Scope 1 and 2 emissions (for larger filers, where material), and governance — a scaled-back version of its more ambitious 2022 proposal, which had included broad Scope 3 requirements that were dropped after fierce pushback.

The rule was immediately challenged in court and stayed. Then the 2024 election changed the agency's posture entirely. On **27 March 2025**, the SEC voted to **end its defense of the rule**; through 2025 it told the Eighth Circuit it would not defend the rule and signaled it would reconsider it through new rulemaking. As of writing the rule is effectively dead — not formally rescinded in every respect, but unenforced and slated for repeal-by-rulemaking. The practical upshot: **there is no operative federal climate-disclosure mandate in the US.**

This sits inside a broader **federal climate retreat**: the US again initiated withdrawal from the Paris Agreement (executive action January 2025, effective in early 2026), and the **One Big Beautiful Bill Act (OBBBA, signed 4 July 2025)** accelerated the repeal or sunset of most IRA clean-energy tax credits — terminating the residential solar credit (end-2025), sunsetting the 45V hydrogen credit (construction after end-2025), and curtailing the wind/solar 45Y/48E credits, among others. The disclosure-rule collapse is one facet of this larger reversal (developed in Ch. 14).

## California fills the vacuum

With the federal rule gone, **California** became the most consequential US climate-disclosure regulator — exactly the same subnational-resilience pattern seen in compliance markets (Ch. 7). Two 2023 laws:

- **SB 253 (Climate Corporate Data Accountability Act)** — requires large companies (revenue over ~$1B) doing business in California to disclose **Scope 1, 2, and 3** emissions per the GHG Protocol.
- **SB 261 (Climate-Related Financial Risk Act)** — requires companies (revenue over ~$500M) to disclose climate-related financial risk, TCFD-aligned.

The implementation status as of writing is genuinely live and worth stating precisely: **CARB approved implementing regulations on 26 February 2026.** SB 253's first reporting deadline is **10 August 2026** (Scope 1 and 2 first; Scope 3 phasing in later). Litigation (a First Amendment challenge, among other grounds) is ongoing: a court **enjoined enforcement of SB 261 in November 2025** while **declining to enjoin SB 253**, and the **Ninth Circuit heard oral argument on 9 January 2026** without yet ruling. So as of writing, **SB 253 is moving forward** for 2026–27 while **SB 261 is on hold pending the courts** — companies are preparing under uncertainty.

Because so many large US companies "do business in California," SB 253 effectively imposes Scope 1/2/3 disclosure on much of corporate America despite the federal rule's collapse — a striking demonstration of how a single large subnational market can set a de facto national standard.

## **Stop-and-check 13.E**

1. The SEC dropped Scope 3 from its 2024 rule and then abandoned the rule entirely by 2025. Trace the political logic: why was Scope 3 the first casualty, and why did the whole rule then fall?
2. California's SB 253 covers Scope 3; the (dead) federal rule did not. How can a state regulator impose a requirement the federal regulator couldn't sustain?
3. SB 253 is proceeding while SB 261 is enjoined. What does it tell you that the *emissions-data* law survived the first injunction round but the *risk-disclosure* law did not?
4. **Socratic prompt:** A US multinational faces no federal mandate, a California mandate (partly enjoined), and the EU's ESRS. How should it decide what to actually report — to the strictest applicable standard, or jurisdiction-by-jurisdiction? What are the costs of each?

**Answers**

1. Scope 3 was the first casualty because it is the most burdensome, least controllable, and most legally exposed part of the rule — covering value-chain emissions a registrant only estimates, which invited the fiercest pushback from issuers and the strongest litigation-risk concerns, so the SEC dropped it from the 2022 proposal to salvage the rest. The whole rule then fell to a change in political control: after the 2024 election the agency's posture reversed, it stopped defending the rule in court in March 2025, and moved toward repeal-by-rulemaking. The logic is that disclosure mandates rest on shifting executive priorities, so the most contested element goes first and a hostile administration can abandon the remainder entirely.

2. California uses its market-access leverage rather than securities authority. SB 253 applies to large companies "doing business in California" — and because so many large US firms do — so it reaches much of corporate America without needing a federal hook. A state can sustain a Scope 3 requirement the SEC could not partly because it rests on different legal authority (in-state commerce, not federal securities law), faces a different (though still active) litigation posture, and is insulated from the federal political reversal that killed the SEC rule. It is the same subnational-resilience pattern seen when state compliance markets survived federal absence.

3. It suggests the courts found the emissions-data mandate more defensible than the risk-disclosure mandate on the grounds litigated — notably the First Amendment compelled-speech challenge. Reporting measured/estimated emissions per a recognized protocol reads more like objective, factual disclosure, which is harder to attack as compelled opinion; requiring a company to characterize its climate-related financial risks involves more judgment and arguably more compelled expression, making SB 261 the softer target for an injunction. The split is provisional — the Ninth Circuit has not ruled — but it signals that factual data mandates may prove more durable than narrative-risk mandates.

4. The choice is between a single high-water-mark and tailored compliance. Reporting to the strictest applicable standard (effectively ESRS plus SB 253 Scope 3) yields one consistent global dataset, simplifies internal systems, future-proofs against tightening, and avoids the embarrassment of disclosing more in one jurisdiction than another — at the cost of doing expensive, broad reporting even where not legally required, and exposing data that creates litigation and competitive risk. Jurisdiction-by-jurisdiction minimizes cost and exposure but multiplies internal complexity, invites inconsistency that critics can exploit, and must be re-engineered every time a rule shifts. Most large multinationals converge toward the strictest core with jurisdictional add-ons, because the marginal cost of consistency is usually less than the cost of managing divergence.

---

# Part 6: Transition plans and financed emissions

## A target without a plan is not credible

The frontier of credibility has moved from *targets* to **transition plans** — the concrete, costed, year-by-year account of *how* a company will actually hit its target: which capital expenditures, which technology switches, which assumptions about policy and offsets. A 2050 net-zero target with no transition plan is, increasingly, treated as a marketing statement.

The **Transition Plan Taskforce (TPT)** in the UK developed a widely referenced disclosure framework for transition plans (its outputs, like TCFD's, are being folded into the ISSB's work). ESRS E1 requires transition-plan disclosure in the EU. The common thread: a credible plan must show *consistency between the climate target and the business strategy and capital allocation* — not a sustainability report bolted onto an unchanged business model.

## Financed emissions and the net-zero alliances

For financial institutions, the entire game is **financed emissions** — the Scope 3 (Category 15) emissions of the companies and projects they lend to, invest in, or insure. These dwarf a bank's operational footprint by orders of magnitude. The **PCAF (Partnership for Carbon Accounting Financials)** standard (Ch. 5) provides the methodology.

Around 2021, finance organized into net-zero "alliances" under the **Glasgow Financial Alliance for Net Zero (GFANZ)** umbrella — the Net-Zero Banking Alliance, Net-Zero Asset Managers initiative, and others — committing trillions in assets to net-zero alignment. By 2024–2025 these alliances **unraveled significantly**: major US banks and asset managers exited amid antitrust concerns, political pressure (especially anti-ESG campaigns in US states), and the difficulty of reconciling fossil-fuel financing with alliance commitments. GFANZ restructured into a looser advisory body.

The lesson parallels the disclosure story: voluntary collective commitments are fragile under political and commercial pressure. Financed-emissions accounting (PCAF) survives as a technical practice; the high-profile *alliances* built on top of it proved much more reversible than they looked in 2021.

## **Stop-and-check 13.F**

1. Why is a transition plan a stronger signal than a target? What can a plan reveal that a target hides?
2. For a bank, financed emissions are ~99%+ of its footprint and largely outside its direct control. Does that make a bank's net-zero target meaningless, or just hard? What would make it meaningful?
3. The GFANZ alliances unraveled under antitrust and political pressure. Was the alliance model flawed, or just ahead of the politics?
4. **Socratic prompt:** An asset manager says it is "net zero aligned" but continues to hold large fossil-fuel positions, arguing engagement beats divestment. Is that defensible? What evidence would distinguish genuine engagement from a fig leaf?

**Answers**

1. A target states an endpoint; a transition plan shows the costed, year-by-year route — which capex, which technology switches, which assumptions about policy and offsets. A plan can reveal what a bare target hides: whether the climate goal is actually consistent with the company's capital allocation and business strategy, or merely a sustainability statement bolted onto an unchanged business model. A 2050 target with no plan tells you nothing about whether anyone has budgeted the asset retirements and replacements required, so the plan is the stronger signal precisely because it exposes the gap between aspiration and committed spending.

2. It makes a bank's target hard, not meaningless. Financed emissions are real emissions the bank enables through its lending, investing, and insuring, and the PCAF methodology lets them be measured — so the target is about the right thing even if the bank does not directly emit them. What makes it meaningful is influence over the portfolio's trajectory: setting financed-emissions reduction targets, shifting capital toward decarbonizing counterparties, conditioning financing on credible client transition plans, and disclosing progress against an absolute or intensity baseline. Without those levers the target is just an accounting figure; with them it can steer real-world capital.

3. Both readings hold. The model was flawed in that it relied on voluntary collective commitments with weak enforcement, exposing members to antitrust scrutiny for coordinating and to political attack with no legal shield — and it asked institutions to reconcile net-zero pledges with continued fossil financing they were unwilling to abandon. But it was also ahead of the politics: the 2021 enthusiasm assumed a stable pro-climate consensus that the anti-ESG backlash and the broader federal retreat dissolved. The technical practice (PCAF financed-emissions accounting) survived; the high-profile alliances built atop it proved far more reversible, which is the recurring lesson about voluntary collective commitments.

4. It can be defensible, but only with evidence, and the bar is high. Engagement genuinely can beat divestment because selling shares to a less scrupulous owner changes nothing in the real world, whereas an active owner can push management. The distinguishing evidence: specific, time-bound engagement asks tied to the investee's transition plan and capex; a documented escalation ladder (votes against directors, public statements, ultimately divestment) with a track record of using it; and measurable changes in the investee's behavior. A fig leaf looks like vague "constructive dialogue," near-unanimous support for management, no escalation, and fossil positions held with no trajectory or exit condition.

---

# Part 7: The law of green claims

## From reputational risk to legal risk

The final force reshaping corporate climate behavior is **greenwashing law** — the migration of climate claims from the domain of reputation into the domain of enforceable consumer-protection and securities law. This is the mechanism that connects the voluntary-market integrity crisis (Ch. 8) to real corporate consequences.

**The EU.** Two instruments matter. The **Empowering Consumers for the Green Transition Directive** (adopted 2024) bans generic environmental claims ("climate neutral," "eco-friendly") unless substantiated, and specifically targets offset-based neutrality claims. The proposed **Green Claims Directive** would require pre-substantiation and verification of explicit environmental claims — though its passage has itself been contested and delayed amid the same competitiveness backlash that drove the CSRD Omnibus. Together they would make "carbon neutral via offsets" marketing legally hazardous in the EU.

**The US.** The **FTC Green Guides** — guidance on environmental marketing claims — have been under revision, with carbon-offset and "net zero/carbon neutral" claims a focus of the review. Even absent a finalized revision, the FTC and state attorneys general can pursue deceptive-marketing actions, and private greenwashing class actions have proliferated.

**Other jurisdictions.** The UK's **Advertising Standards Authority (ASA)** and **Competition and Markets Authority**, and Australia's **ACCC**, have all taken high-profile actions against carbon-neutral and offset-based claims by airlines, energy companies, and consumer brands.

## The feedback loop into the voluntary market

This legal pressure is, in effect, a **demand-side integrity mechanism** distinct from ICVCM/VCMI/SBTi (Ch. 8). It changes corporate behavior directly: faced with litigation and regulatory risk, many companies have **dropped "carbon neutral" product claims entirely** ("greenhushing" — going quiet rather than risk a claim), shifted from avoidance credits toward removals, and tied any retained claims to validated frameworks. The cheap-offset, loose-claim model that built the legacy voluntary market is being squeezed from two directions at once: integrity bodies on the supply side and consumer-protection law on the demand side.

## **Stop-and-check 13.G**

1. How does greenwashing law function as a "demand-side integrity mechanism" for the voluntary carbon market? Trace the causal chain from an FTC action to a project developer's revenue.
2. "Greenhushing" — companies going silent rather than risk a claim — is a documented response to greenwashing enforcement. Is that a good outcome, a bad one, or both?
3. The same competitiveness backlash that narrowed the CSRD also stalled the EU Green Claims Directive. What does this tell you about the durability of the green-claims crackdown?
4. **Socratic prompt:** Is the right legal target the *claim* (what a company says) or the *conduct* (what it does)? A company could decarbonize aggressively and say nothing, or do little and claim a lot. Which should the law police, and can it do both?

**Answers**

1. The chain runs through demand. Greenwashing law (an FTC deceptive-marketing action, an ASA/ACCC ruling, the EU Empowering Consumers Directive) makes "carbon neutral via offsets" claims legally hazardous. Facing litigation and regulatory risk, companies stop making cheap offset-based neutrality claims and either drop them entirely or shift toward removals and validated frameworks. That reduces demand for the low-quality avoidance credits that built the legacy market — and falling demand cuts the revenue of the project developers who sell them. So a consumer-protection action on the demand side propagates back through corporate purchasing to the supply side, squeezing developers, distinct from the supply-side integrity bodies (ICVCM/VCMI/SBTi).

2. Both. It is good insofar as it ends the era of unsubstantiated, low-quality neutrality claims that misled consumers and propped up weak credits — the law successfully deterred the bad behavior. It is bad insofar as silence also hides genuine progress: a company decarbonizing aggressively but afraid to say so deprives investors, consumers, and policymakers of information, weakens peer pressure and reputational reward for real action, and can chill legitimate communication along with the deceptive kind. Greenhushing is the predictable side-effect of policing claims rather than conduct — it suppresses speech, not just false speech.

3. It signals that the green-claims crackdown rests on the same contested political ground as disclosure and is therefore similarly reversible. The competitiveness backlash that raised CSRD thresholds also stalled the Green Claims Directive, showing that the appetite for new compliance burdens — even consumer-protection ones — recedes under economic pressure. The durable core (the already-adopted Empowering Consumers Directive, existing deceptive-marketing law, private class actions) persists, but the more ambitious pre-substantiation regime is contingent. The lesson mirrors disclosure: the ratchet can loosen, so the crackdown's reach should not be assumed permanent.

4. The law can and arguably should do both, but they are different tools aimed at different harms. Policing the claim is consumer-protection and securities law's natural home — it targets deception, the gap between what is said and what is true, and it is administrable because the claim is concrete and falsifiable. Policing the conduct is the domain of carbon pricing, mandated reductions, and disclosure mandates — it targets the underlying behavior regardless of speech. Relying only on claim-policing produces greenhushing and lets quiet under-performers escape; relying only on conduct-policing lets liars who happen to also act mislead the market. A coherent regime pairs mandatory disclosure (forcing conduct into the open) with claims law (punishing the lie about it).

---

# Closing exercise

Three things to take away:

**1. "Net zero" is not one thing — it is a spectrum from rigorous to meaningless, and the words signal which.** A removal-backed, SBTi-validated, transition-planned net-zero target is a serious commitment; an offset-backed "carbon neutral" sticker is, increasingly, a legal liability. The skill is reading the claim precisely: what's abated, what's neutralized, with what kind of credit, validated by whom.

**2. The disclosure regime is real, mandatory, and fractured.** The ISSB baseline (IFRS S1/S2) is becoming a global lingua franca; the EU built a broader double-materiality regime and then narrowed it under the 2025 Omnibus; the US federal rule collapsed and California stepped into the gap. A multinational in 2026 navigates all of these at once, and must assume the rules can loosen as well as tighten.

**3. Credibility has moved from targets to plans to law.** The frontier is the transition plan (can you show the capex?) and the courtroom (can you defend the claim?). The voluntary market's integrity crisis now has teeth through consumer-protection and securities law — which is reshaping corporate behavior more directly than any voluntary standard.

---

# What this chapter simplified

**1. The mechanics of each standard.** SBTi's sector pathways, the ESRS data points (over a thousand in the original Set 1), and IFRS S2's detailed requirements are each book-length in their own right. I gave the architecture, not the line items.

**2. The Scope 3 measurement problem.** I treated Scope 3 as "hard." The actual difficulty — spend-based vs. activity-based estimation, supplier data quality, double-counting across value chains, the use category for sold products — is the technical heart of corporate accounting and deserves the full Chapter 5 treatment plus more.

**3. The assurance/audit dimension.** I mentioned limited vs. reasonable assurance only in passing. Who audits sustainability data, to what standard, and with what liability is a fast-evolving field (and a major new line of business for the audit firms).

**4. The anti-ESG backlash.** The US state-level anti-ESG movement — laws restricting state pension funds from considering climate, boycott lists, antitrust threats against alliances — is a substantial political force I treated only through its effects (GFANZ unraveling, the federal retreat). It deserves fuller political-economy analysis.

**5. The non-US, non-EU regimes.** The UK SDR, Japan, Singapore, Canada, Brazil, China's evolving disclosure expectations — the global adoption map is richer and more varied than the EU/US contrast I emphasized.

---

# Glossary delta (Chapter 13)

- **Abatement** — Reductions in a company's own value-chain emissions (Scopes 1–3), as opposed to neutralization or compensation outside the boundary.
- **Carbon neutral** — A balance claim matching gross emissions with retired offsets over a period; says nothing about reductions or credit quality. Increasingly a legal-risk claim.
- **CSRD (Corporate Sustainability Reporting Directive)** — EU law mandating sustainability reporting against the ESRS. Scope sharply narrowed by the 2025–2026 Omnibus package (Directive (EU) 2026/470).
- **Double materiality** — The EU principle requiring disclosure of both climate's financial effect on the company *and* the company's impact on climate/society. Contrast: ISSB single (financial) materiality.
- **ESRS E1** — The climate standard within the European Sustainability Reporting Standards; the most detailed mandatory climate-disclosure standard in the world.
- **Financed emissions** — A financial institution's Scope 3 Category 15 emissions from its lending/investing/insuring. Methodology: PCAF.
- **GFANZ (Glasgow Financial Alliance for Net Zero)** — Umbrella for finance-sector net-zero alliances (2021); significantly unraveled 2024–2025 under antitrust and political pressure; restructured into an advisory body.
- **IFRS S1 / S2** — The ISSB's first sustainability and climate disclosure standards (2023); S2 builds on the TCFD four pillars. The emerging global baseline.
- **ISSB (International Sustainability Standards Board)** — IFRS Foundation body building a global disclosure baseline; uses single (financial) materiality.
- **Mitigation hierarchy** — Avoid, then reduce, then neutralize the residual. The sequencing rule underlying credible net zero.
- **Net zero** — A state where residual emissions are balanced by durable *removals* after deep absolute reductions (~90%). A destination, not an annual accounting identity.
- **Neutralization** — Removing and durably storing atmospheric CO₂ to balance residual emissions at the net-zero target year; under credible standards, removals only.
- **OER (Ongoing Emissions Responsibility)** — SBTi V2 concept: take responsibility for emissions during the transition via credits/beyond-value-chain action, without substituting for abatement.
- **SBTi (Science Based Targets initiative)** — NGO-coalition standard-setter that became the de facto arbiter of credible corporate climate targets. Corporate Net-Zero Standard V2 expected 2026, mandatory for new targets from 2028.
- **SB 253 / SB 261** — California climate-disclosure laws (2023): SB 253 (Scope 1/2/3 emissions, first deadline Aug 2026); SB 261 (climate financial risk, enforcement enjoined pending Ninth Circuit ruling). CARB regulations approved Feb 2026.
- **TCFD** — Task Force on Climate-related Financial Disclosures; its four-pillar framework (governance, strategy, risk management, metrics & targets) was absorbed into the ISSB in 2023–2024.
- **TPT (Transition Plan Taskforce)** — UK body whose transition-plan disclosure framework is being folded into the ISSB's work.
- **Transition plan** — A costed, year-by-year account of how a company will achieve its climate target; the frontier of corporate credibility.

---

# Sources and currency

This chapter cites figures and legal states current as of writing (May 2026); each should be re-verified against the primary source and updates tracked in `CHANGELOG.md`:

| Claim | Value/state as stated | As-of | Primary source to verify against |
|---|---|---|---|
| SBTi Corporate Net-Zero Standard V2 | second consultation closed 12 Dec 2025; final expected 2026; mandatory for new targets 1 Jan 2028 | Dec 2025 | sciencebasedtargets.org |
| SBTi near-term / long-term requirement | ~42% by 2030 (near-term); ~90% reduction by net-zero year | V1.x | SBTi Corporate Net-Zero Standard |
| ISSB IFRS S1/S2 | published June 2023; adopted/referenced by a growing list of jurisdictions | 2023–26 | IFRS Foundation |
| CSRD Omnibus | political deal 9 Dec 2025; Directive (EU) 2026/470 published 26 Feb 2026, in force 18 Mar 2026 | Feb 2026 | EUR-Lex; Council of the EU |
| CSRD revised thresholds | >1,000 employees & >€450m turnover; mandatory reporting for FY ≥ 1 Jan 2027 | Feb 2026 | Directive (EU) 2026/470 |
| ESRS revision | revised Set 1 ESRS Delegated Act due ~Sept 2026 | 2025–26 | European Commission; EFRAG |
| SEC climate rule | adopted 6 Mar 2024; SEC ended defense 27 Mar 2025; reconsideration/repeal-by-rulemaking; unenforced | 2025 | SEC.gov press release 2025-58 |
| OBBBA | signed 4 Jul 2025; sunsets/repeals most IRA clean-energy credits (45V end-2025; 45Y/48E curtailed; residential solar end-2025) | Jul 2025 | OBBBA text; IRS |
| US Paris withdrawal | executive action Jan 2025; effective early 2026 | 2025–26 | US State Dept / UNFCCC |
| California SB 253/261 | CARB regulations approved 26 Feb 2026; SB 253 first deadline 10 Aug 2026; SB 261 enforcement enjoined Nov 2025; Ninth Circuit oral argument 9 Jan 2026, no ruling | Mar 2026 | CARB; Ninth Circuit docket |
| EU green-claims law | Empowering Consumers Directive adopted 2024; Green Claims Directive contested/delayed | 2024–26 | EUR-Lex |

---

# What's next

This chapter brought the markets, accounting, and policy of Track B to ground inside the firm. The next chapter zooms back out to the **geopolitical** scale: how the US, EU, China, India, and the major fossil-fuel producers contest and reshape the climate-policy architecture — CBAM and the trade frictions it creates, the "carbon club" idea, China's dominance of the physical-carbon value chain, the petrostate transition question, and the climate-finance cleavage between North and South (the $300B NCQG, the COP30 Belém package).

Chapter 15 then closes the book by looking forward: where current policy actually points for 2030 and 2050, the AI-compute-and-energy collision, the carbon-to-products and removal frontiers, solar geoengineering, and an honest accounting of what works, what doesn't, and what we still don't know.
