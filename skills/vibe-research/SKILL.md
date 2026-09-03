---
name: vibe-research
description: "Conduct deep commercial and market research for business initiatives, product launches, and growth campaigns. Reverse-engineers competitor offers, pricing benchmarks, customer objections, and industry demand before planning or building."
user-invocable: true
when_to_use: "Use when evaluating a market, analyzing competitor offers, researching pricing models, or validating customer demand before planning."
category: utilities
keywords: [research, competitor, market, pricing, icp, customer, analysis, validation]
license: MIT
argument-hint: "[market or competitor topic] [--ultra] [--yagni]"
metadata:
  author: abm-dungtq
  version: "3.0.0"
  workflow:
    follows: [vibe-storm]
    precedes: [vibe-scout, vibe-plan]
---

# Vibe Research (Business & Market Intelligence)

Conduct rigorous, evidence-grounded commercial research without fluff or academic theory. Understand competitors, customer objections, and pricing structures before planning or building.

Principles: **evidence over assumptions | brutal honesty on competitor moats | max 5 search passes | actionable synthesis**

## 4-Phase Research Methodology

### Phase 1: Commercial Scope Definition
Clearly define the boundaries of the research:
- **Target Market & Niche:** Specific industry, customer persona (ICP), and geography.
- **Core Hypotheses to Test:** Pricing tolerance, willingness to pay, and unmet customer pains.
- **Boundaries:** What is inside versus outside this market inquiry.

### Phase 2: Systematic Market Intelligence
Employ a focused, evidence-based research strategy (strictly maximum 5 search iterations):
1. **Competitor Offer Reverse-Engineering:** Identify the top 3 direct and 2 indirect players. Analyze their pricing tiers, core promises, and positioning.
2. **Customer Pain & Objection Discovery:** Search customer reviews, Reddit/forums, and social communities for recurring complaints about existing solutions.
3. **Pricing Benchmarks:** Uncover prevailing industry pricing models (flat fee, monthly retainer, tiered SaaS, per-transaction).
4. **Distribution & Acquisition Footprint:** Identify how market leaders acquire customers (SEO, organic video, paid ads, outbound).

### Phase 3: Commercial Synthesis & Value Gap
Synthesize raw findings into strategic insights:
- **The Value Gap:** Where are competitors over-charging or failing to deliver?
- **The Wedge Opportunity:** What single high-friction task can be solved 10x faster or cheaper?
- **Unit Economics Viability:** Are estimated customer acquisition costs (CAC) compatible with expected pricing?

### Phase 4: Business Research Report Generation
Persist the findings in `reports/research-{topic-slug}.md` using this canonical structure:

```markdown
# Business Research Report: [Topic]

## 1. Executive Summary
[Concise 2-paragraph synthesis of market feasibility, competitor landscape, and recommended wedge]

## 2. Competitor Teardown
| Competitor | Pricing Model | Core Promise | Critical Weakness / Customer Complaints |
| :--- | :--- | :--- | :--- |

## 3. Customer Objections & Buying Triggers
- Top 3 reasons customers refuse to buy existing solutions
- The #1 breakthrough feature or promise that drives conversion

## 4. Value Gap & Wedge Opportunity
[Detailed analysis of the market gap and how our offer exploits it]

## 5. Pricing & Unit Economics Recommendation
- Recommended price anchor vs competitor alternatives
- Gross margin & break-even assumptions

## 6. Unresolved Market Risks & Next Steps
[Open questions passed to vibe-scout or vibe-plan]
```

## Downstream Pipeline Handoff

Pass verified market findings, competitor benchmarks, and pricing recommendations directly into:
- **`vibe-scout`**: To audit existing internal assets against market findings.
- **`vibe-plan`**: To build the phased execution roadmap based on the validated wedge.
## References

Load operational frameworks when conducting deep market intelligence:
- Competitor teardown models & objection queries: `references/research-frameworks.md`
