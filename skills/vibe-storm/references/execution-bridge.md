# The 5-Stage Business Delivery Pipeline Bridge

How to move a business initiative from initial intent through execution using the `brainstorm -> research -> scout -> plan -> cook` pipeline.

---

## Pipeline Overview

```text
[1. BRAINSTORM] ──> [2. RESEARCH] ──> [3. SCOUT] ──> [4. PLAN] ──> [5. COOK]
  Bounded Contract      Market / ICP      Existing Assets    Phased Roadmap    Execute Copy,
  & Trade-offs          & Competitors     & Funnel State     & Deliverables    Funnel & Launch
```

---

## Stage 1: Brainstorm (`vibe-storm`)
- **Action:** Define Outcome, Constraints, Non-goals, and Acceptance Criteria.
- **Artifact:** Bounded Business Brief (Markdown or `--html`).
- **Trigger:** `/vibe-storm <topic>`

---

## Stage 2: Research
- **Action:** Investigate competitor pricing, market demand, customer objections, and industry benchmarks.
- **Handoff prompt:**
  ```text
  Based on the accepted business contract for [INITIATIVE], conduct deep market research on:
  1. Top 3 competitors, their pricing models, and primary value promises.
  2. The most common buyer objections in this niche.
  3. Industry standard conversion rates and pricing benchmarks.
  ```

---

## Stage 3: Scout
- **Action:** Inspect the business's current assets, traffic sources, email list size, tech stack, and active funnels.
- **Handoff prompt:**
  ```text
  Scout current business assets for [INITIATIVE]:
  1. Audit existing landing pages, conversion rates, and drop-off points.
  2. Inventory reusable assets (case studies, email templates, customer reviews).
  3. Identify integration bottlenecks with payment gateways (Stripe/VietQR/SePay).
  ```

---

## Stage 4: Plan
- **Action:** Structure a multi-phase implementation plan with clear dependencies, deliverables, and rollback/contingency plans.
- **Phases:**
  - *Phase 1:* Offer crafting, pricing structure, and 1-page sales funnel.
  - *Phase 2:* Marketing content production & video scripts.
  - *Phase 3:* Payment gateway & automated onboarding flow.
  - *Phase 4:* Soft launch outreach & first paying customer milestone.

---

## Stage 5: Cook
- **Action:** Systematically execute each deliverable: write high-converting copy, design the sales page, configure payment webhooks, and deploy outreach campaigns.
