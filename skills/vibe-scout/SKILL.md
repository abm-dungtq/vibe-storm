---
name: vibe-scout
description: "Audit existing business assets, customer funnels, and conversion bottlenecks. Rapidly inspects landing pages, email lists, traffic analytics, customer journey drop-offs, and reusable commercial materials before planning or execution."
user-invocable: true
when_to_use: "Use to audit existing business assets, inspect conversion funnels, identify marketing bottlenecks, or map current customer touchpoints before planning."
category: utilities
keywords: [scout, funnel, audit, assets, conversion, dropoff, analytics, bottlenecks]
license: MIT
argument-hint: "[funnel URL, business asset, or problem] [--ultra]"
metadata:
  author: abm-dungtq
  version: "1.0.0"
  workflow:
    follows: [vibe-storm, vibe-research]
    precedes: [vibe-plan]
---

# Vibe Scout (Funnel & Asset Audit)

Rapidly audit current business reality, existing marketing funnels, customer touchpoints, and reusable commercial assets before planning or launching.

Principles: **facts over vanity metrics | pinpoint the single biggest leak | inventory what is reusable | token-efficient reporting**

## When to Use

- Before planning a new marketing campaign or product launch.
- When an existing sales funnel is underperforming and you need to find the exact leak.
- To inventory existing customer lists, social followings, testimonials, and marketing collateral.
- When inheriting or taking over an existing business project.

## 5-Step Scouting Workflow

### 1. Identify Audit Scope
- Parse the business URL, product repository, marketing accounts, or analytics state.
- Identify the target customer journey to trace.

### 2. Map the Full Customer Journey
Trace the exact path prospects take from initial discovery to paying customer:
```text
[Discovery / Traffic] ──> [Landing Page / Offer] ──> [Checkout / Payment] ──> [Onboarding & Retention]
```

### 3. Pinpoint Conversion Bottlenecks
Compare current metrics against commercial benchmarks:
- **Traffic to Lead/Click:** Benchmark >= 2.0% (If below: Hook/Creative failure).
- **Lead to Sales Page View:** Benchmark >= 30% (If below: Bridge/Email failure).
- **Sales Page to Cart/Checkout:** Benchmark >= 3.0% (If below: Offer/Proof failure).
- **Checkout to Paid Order:** Benchmark >= 60% (If below: Payment/Friction failure).

### 4. Inventory Reusable Commercial Assets
Catalog all existing leverage points that reduce future effort:
- **Audience Assets:** Email subscribers, social followers, community members.
- **Proof Assets:** Customer testimonials, video reviews, client case studies, founder credentials.
- **Content Assets:** Top-performing blog posts, viral video clips, slide decks.
- **Tech & Payment Assets:** Active Stripe accounts, custom domains, pre-configured email templates.

### 5. Generate Business Scout Report
Persist the findings in `reports/scout-{topic-slug}.md` using this canonical structure:

```markdown
# Business Scout Report: [Topic / Funnel]

## 1. Executive Summary & Core Bottleneck
[2-paragraph summary: What works, what is broken, and the #1 single bottleneck to fix]

## 2. Customer Journey Health Map
| Stage | Current Metric | Benchmark | Health Status | Primary Leak |
| :--- | :--- | :--- | :--- | :--- |
| Traffic -> Click | [e.g. 0.8%] | 2.0% | 🔴 CRITICAL | Creative hook is generic |
| Click -> Lead | [e.g. 15%] | 20% | 🟡 WARNING | Opt-in headline lacks urgency |
| Lead -> Sale | [e.g. 4.2%] | 3.0% | 🟢 HEALTHY | Offer converts well |

## 3. Reusable Commercial Asset Inventory
- **Audience:** [Lists, accounts, communities]
- **Social Proof:** [Testimonials, case studies]
- **Collateral:** [Templates, past copy, media assets]

## 4. Immediate High-ROI Interventions
1. [Highest leverage fix: e.g. Add 1-click VietQR/SePay to reduce checkout friction]
2. [Second leverage fix: e.g. Retarget un-converted leads with case study video]
```

## Downstream Pipeline Handoff

Pass the audited bottleneck and reusable asset inventory directly to **`vibe-plan`** to build the remediation roadmap.
