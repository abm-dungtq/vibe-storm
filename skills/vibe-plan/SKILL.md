---
name: vibe-plan
description: "Structure comprehensive, phased business execution plans for product launches, marketing campaigns, and revenue initiatives. Creates files-first roadmaps (plan.md + phase-NN-*.md) with commercial verification criteria, risk scorecards, and visual HTML dashboards."
user-invocable: true
when_to_use: "Use when a business initiative, marketing campaign, or product launch requires structured phases, milestones, risk mitigation, and commercial execution plans."
category: utilities
keywords: [plan, business-plan, roadmap, phases, milestones, gtm, launch, execution]
license: MIT
argument-hint: "[business task or brief] [--fast] [--html] [--advice] [--ultra] [--yagni]"
metadata:
  author: abm-dungtq
  version: "3.0.0"
  workflow:
    follows: [vibe-storm, vibe-research, vibe-scout]
    precedes: [vibe-cook]
---

# Vibe Plan (Business Execution Roadmapping)

Structure clear, phased commercial roadmaps through intent validation, market research synthesis, and asset audits.

Principles: **files-first | phased milestones | commercial verification criteria | risk-aware execution**

## Files-First Planning Architecture

Every business plan is stored as durable, hand-editable Markdown files under `plans/<timestamp>-<slug>/`:
```text
plans/260904-launch-ai-ops/
├── plan.md                          # Master commercial plan & executive overview
├── phase-01-offer-and-positioning.md
├── phase-02-marketing-assets-and-content.md
├── phase-03-funnel-and-checkout.md
└── phase-04-launch-and-acquisition.md
```

## Canonical Phase File Template

Every phase file follows this schema:

```markdown
---
phase: 1
title: "Grand Slam Offer & Pricing Strategy"
status: pending       # pending | in-progress | completed
priority: P1          # P1 | P2 | P3
effort: "1d"          # e.g. "4h", "1d", "3d"
dependencies: []      # phase numbers this blocks on
target_kpi: "5 pre-orders or $1,000 deposits"
---

# Phase 1: Grand Slam Offer & Pricing Strategy

## 1. Phase Objective
[Concrete commercial outcome this phase achieves]

## 2. Deliverables & Tangible Assets
- [ ] Asset 1: [e.g. 1-Page Offer Document with Risk Reversal]
- [ ] Asset 2: [e.g. Pricing Table with 3 Tiers]
- [ ] Asset 3: [e.g. FAQ addressing top 5 buying objections]

## 3. Commercial Verification Plan
Observable evidence required before marking phase completed:
- [ ] Verification 1: [e.g. 20 target prospects reviewed the offer sheet]
- [ ] Verification 2: [e.g. At least 3 prospects confirmed intent to purchase]

## 4. Risks & Contingency Fallback
- **Risk:** [What if prospects reject the price anchor?]
- **Fallback:** [Pre-defined pivot or bonus stack adjustment]
```

## Standard 4-Phase Business Roadmap

Unless customized by the user, commercial initiatives default to a 4-phase rollout:

1. **Phase 1: Offer & Positioning (Days 1-2)**
   - The Wedge, value proposition, Grand Slam Offer stack, and pricing tiers.
2. **Phase 2: Marketing Assets & Content (Days 3-4)**
   - 4 content pillars that sell, viral video scripts, social proof case studies, and email sequences.
3. **Phase 3: Sales Funnel & Checkout (Days 5-6)**
   - 1-page sales page, mobile payment integration (Stripe, VietQR, SePay), and automated delivery workflow.
4. **Phase 4: Launch & Customer Acquisition (Days 7-8)**
   - Outbound outreach to 50 targeted prospects, announcement to network, and securing the first paying clients.

## HTML Output Mode (`--html`)

When `--html` is passed, generate an interactive, self-contained `plan.html` visual dashboard with:
- Phased Gantt/Timeline view.
- Live progress checklist.
- Risk matrix and KPI tracker.

## Downstream Pipeline Handoff

Pass the generated `plan.md` and phase files directly to **`vibe-cook`** for phase-by-phase execution:
```text
Plan ready at ./plans/<timestamp>-<slug>/plan.md. To execute, run /vibe-cook ./plans/<timestamp>-<slug>/plan.md
```
## Composable Modes

- `--advice`: Runs under adversarial advisory supervision to validate timeline feasibility, resource allocation, and break-even milestones before locking phases.
- `--ultra`: Runs a 5-perspective plan evaluation (growth hacker, unit economist, ops lead, copy chief, skeptic) to catch failure modes early.
- `--yagni`: Strips secondary deliverables and phases that do not directly generate first cash flow.

## References

Load canonical phase schemas and quality checklists when structuring plans:
- Master plan and phase file templates: `references/phase-templates.md`
