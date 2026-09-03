# Vibe Ideation Frameworks & Formulas

Operational formulas, evaluation rubrics, and copyable prompt templates used by `vibe-storm`.

---

## 1. Business Engine Frameworks (`--biz`)

### The Wedge Formula
$$\\text{Wedge Viability} = \\frac{\\text{Urgency of Pain} \\times \\text{Willingness to Pay}}{\\text{Time to First Value}}$$

- **Target Wedge Size:** Solves 1 micro-task in under 60 seconds (e.g., "Clean noisy podcast audio in 1 click", not "Complete audio production suite").
- **Pricing Anchor:** Anchor against manual labor or expensive agency retainers (\$500/mo freelancer -> \$29/mo AI tool).
- **Anti-Scope Guardrails:** No team workspaces, no enterprise SSO, no custom role permissions in MVP.

### Day-1 Smoke Test Protocols
1. **Loom Concierge:** Record a 90-second video demo using mockups, DM 20 target users on X/LinkedIn: *"I built a prototype solving X. Want early access for \$19?"*
2. **The Fake Door / Pre-order:** Simple landing page with Stripe Checkout in test mode or \$1 deposit. If <3% convert, pivot angle.

---

## 2. Marketing Engine Frameworks (`--mkt`)

### The Hook-Offer-Angle Matrix

| Angle Type | Hook Formula | Example |
| :--- | :--- | :--- |
| **Pain-Driven** | "How much time did you waste doing [X] this week?" | "Stop spending 4 hours editing podcast filler words manually." |
| **Dream-Driven** | "Go from [Raw Input] to [Polished Result] in 30 seconds." | "Turn your raw zoom recording into studio-mastered audio before your coffee cools down." |
| **Contrarian** | "Why top creators stopped using [Expensive Tool]." | "Why spending \$2,000 on soundproofing is obsolete in the AI era." |

### Engineering as Marketing (Free Mini-Tools)
- Identify a sub-feature that can run client-side or with low API cost.
- Offer it 100% free with no signup required, watermarked, or with an upgrade banner.

---

## 3. Content Engine Frameworks (`--content`)

### The Hook-Retain-Reward Script Formula (Short-Form)
1. **Hook (0-3s):** Visual movement + Contrarian/Shock statement (No "Hey guys, today I am going to...").
2. **Retain (3-15s):** Agitate the status quo. Show the painful traditional workflow.
3. **Reward (15-45s):** Demonstrate the 10x shortcut. Reveal the exact mechanism.
4. **CTA (45-60s):** Low-friction action: *"Comment 'AUDIO' and I will DM you the tool link."*

### 1 Insight -> 4 Formats Multiplier
```text
[Core Insight]
  ├──> X/Twitter Thread: 1 Hook tweet + 5 value tweets + 1 CTA
  ├──> LinkedIn Post: 1 Contrarian opening line + 3 bullet takeaways + visual diagram
  ├──> TikTok / Reel: 45s Hook-Retain-Reward talking head with B-roll demo
  └──> Visual Carousel: 5 slides breakdown (Problem -> Old Way -> New Way -> Steps -> Summary)
```

---

## 4. Rollout Engine Frameworks (`--sprint`)

### 48-Hour AI-Native Sprint Schedule

```
Hour 00 - 04 | Specification & Visual Mockup (v0 / Stitch / Claude)
Hour 04 - 12 | Core Functional Pipeline (API route + Backend processing)
Hour 12 - 24 | Frontend UI & Happy Path Polish (Cursor / Claude Code)
Hour 24 - 32 | Landing Page, Copywriting & Responsive Design
Hour 32 - 40 | Payment & Auth Integration (Stripe / SePay / Better-Auth)
Hour 40 - 48 | Soft Launch: Deploy (Vercel/Fly), post to 3 communities, collect feedback
```
