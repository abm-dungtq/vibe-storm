# Business Phase Templates & Deliverable Checklists

Detailed templates for structuring business phases with `vibe-plan`.

---

## 1. Master Plan Template (`plan.md`)

```markdown
# Commercial Execution Plan: [Project Name]

## Executive Summary
- **Business Model:** [Productized Service / Digital Asset / Micro-SaaS / E-com / AI Agency]
- **Target Audience (ICP):** [Specific target customer]
- **Target Revenue KPI:** [$X MRR / $Y launch sales in Z days]
- **Launch Deadline:** [Target launch date]

## Phase Overview & Dependency Matrix
| Phase | Title | Priority | Effort | Dependencies | Target KPI |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Grand Slam Offer & Positioning | P1 | 1d | None | 5 pre-orders |
| Phase 2 | Marketing Assets & Content Sprint | P2 | 2d | Phase 1 | 10 high-intent leads |
| Phase 3 | Funnel & Checkout Automation | P1 | 1d | Phase 1 | Checkout test passed |
| Phase 4 | Customer Acquisition & First Dollar | P1 | 2d | Phase 2, 3 | First paying customer |

## Risk Scorecard & Contingency Plans
- **Top Commercial Risk:** [e.g. CAC too high]
- **Mitigation:** [Switch from paid ads to 1-on-1 direct outbound]
```

---

## 2. Phase Quality Criteria

A phase plan is ready for `vibe-cook` only when:
1. Every deliverable is a tangible file (e.g. `copy/sales-page.md`, `funnel/checkout.ts`, `emails/sequence.md`).
2. Every phase has an observable, falsifiable verification test.
3. Dependencies are acyclic and explicitly declared.
