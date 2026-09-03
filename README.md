<div align="center">

# ⚡ Vibe Storm

**The Business-Grade Brainstorm & Intent Contract Engine for Solopreneurs, Founders & Agile Teams**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin%20Compatible-blue)](https://code.claude.com)
[![Cursor](https://img.shields.io/badge/Cursor-Rules%20Ready-purple)](https://cursor.com)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/abm-dungtq/vibe-storm/pulls)
[![Pipeline Standard](https://img.shields.io/badge/Pipeline-Brainstorm%E2%86%92Research%E2%86%92Scout%E2%86%92Plan%E2%86%92Cook-emerald)](https://github.com/abm-dungtq/vibe-storm)

*Turn incomplete commercial intent into a bounded delivery contract and compare viable business approaches before research, planning, or execution — powered by the standard 5-stage agent pipeline.*

[The 5-Stage Pipeline](#-the-5-stage-agent-pipeline) • [The Business Contract](#-the-bounded-business-contract) • [Business Bug Routing](#-business-failure--bug-routing) • [Installation](#-installation-guide) • [Tiếng Việt](#-hướng-dẫn-tiếng-việt)

</div>

---

## 💡 What is Vibe Storm?

In modern business and solopreneurship, projects fail not from lack of effort, but from **vague intent, scope creep, and untested commercial assumptions**.

**Vibe Storm** adapts the battle-tested engineering discipline of `ak:brainstorm` for **all types of Business Requirements** (product launches, revenue campaigns, marketing funnels, content engines, and operational scaling). 

It acts as the **authoritative front-door gate** that establishes a bounded commercial contract before feeding into the standard agent delivery pipeline:

```
[1. BRAINSTORM] ──> [2. RESEARCH] ──> [3. SCOUT] ──> [4. PLAN] ──> [5. COOK]
  Bounded Contract      Market & ICP       Assets & Funnel    Phased Roadmap    Execute Copy,
  & Trade-offs          Deep Dive          Bottlenecks        & Deliverables    Funnel & Launch
```

---

## 📋 The Bounded Business Contract

Every business initiative starts by locking in four mandatory fields:

- **🎯 Outcome:** The measurable commercial end-state (e.g. 50 paying clients, $10k MRR, >=3% funnel conversion).
- **🔒 Constraints:** Budget limits, timeline, unit economics (Max CAC, target margin), compliance, and team bandwidth.
- **🚫 Non-goals:** Nearby distractions, premature scaling, or adjacent offers that this delivery will **NOT** absorb.
- **✅ Acceptance Criteria:** Observable, verifiable commercial evidence proving completion.

---

## 🔍 Business Failure & Bug Routing

When a business initiative underperforms (ad campaign burning budget, conversion rate drop, high churn, outreach ignored), Vibe Storm prevents guessing fixes from symptoms:

1. **Scout the Affected Funnel:** Map the exact drop-off points across the customer journey.
2. **Diagnose and Prove Root Cause:** Pinpoint whether the bottleneck is in the **Offer**, the **Traffic Source**, the **Messaging**, the **Pricing**, or payment friction.
3. **Compare Cause-Aligned Solutions:** Propose targeted interventions only after proving the root cause.

---

## ⚖️ Strategic Option Exploration

When an initiative has real strategic choices, Vibe Storm presents up to three viable approaches:
- Identifies the **load-bearing assumption** each approach depends on most.
- Analyzes the **condition under which it fails first** (worst-case failure condition).
- Recommends the smallest, most capital-efficient path that satisfies the contract.

---

## 🚀 Quick Start

### 1-Line Universal Install

```bash
curl -fsSL https://raw.githubusercontent.com/abm-dungtq/vibe-storm/main/scripts/install.sh | bash
```

### Direct Usage in Any AI Agent (Claude Code, Cursor, Antigravity)

```bash
# Full commercial brainstorm brief
/vibe-storm "AI Ops agency helping dentists automate appointment booking" --full --html

# Diagnose a failing funnel / business bug
/vibe-storm "Ad campaign CTR is 3% but landing page conversion is under 0.5%"

# Formulate a commercial offer & monetization model
/vibe-storm --biz "Productized video editing service for B2B founders"

# Marketing acquisition loops & messaging angles
/vibe-storm --mkt "Notion workspace template for commercial real estate"

# Content strategy & viral video scripts
/vibe-storm --content "1-person AI automation consultancy"

# 48-hour Go-To-Market roadmap
/vibe-storm --sprint "Paid newsletter and community for indie founders"
```

---

## 📦 Cross-Platform Installation Guide

### Claude Code
```bash
git clone https://github.com/abm-dungtq/vibe-storm.git ~/.claude/skills/vibe-storm
```

### Cursor IDE
```bash
mkdir -p .cursor/rules
curl -fsSL https://raw.githubusercontent.com/abm-dungtq/vibe-storm/main/.cursor/rules/vibe-storm.mdc -o .cursor/rules/vibe-storm.mdc
```

### Google Antigravity / Gemini CLI
```bash
mkdir -p ~/.gemini/config/skills/
git clone https://github.com/abm-dungtq/vibe-storm.git ~/.gemini/config/skills/vibe-storm
```

---

## 🇻🇳 Hướng Dẫn Tiếng Việt

**Vibe Storm** là phiên bản chuẩn mực của `ak:brainstorm` dành riêng cho **Yêu cầu Kinh doanh (Business Requirements)**, vận hành chuẩn xác theo chuỗi 5 bước của AgentKit:

$$\mathbf{[Brainstorm]} \longrightarrow \mathbf{[Research]} \longrightarrow \mathbf{[Scout]} \longrightarrow \mathbf{[Plan]} \longrightarrow \mathbf{[Cook]}$$

1. **Hợp đồng Đóng Khung (Bounded Contract):** Mọi yêu cầu kinh doanh bắt buộc phải xác định rõ 4 trường: *Mục tiêu cụ thể (Outcome)*, *Ràng buộc vốn/thời gian (Constraints)*, *Phạm vi từ chối (Non-goals)*, và *Tiêu chí nghiệm thu (Acceptance Criteria)*.
2. **Chẩn đoán Sự cố Kinh doanh (Business Bug Routing):** Khi doanh số tụt dốc, ads lỗ, hoặc conversion kém $\to$ Thám thính phễu $\to$ Chứng minh nguyên nhân gốc rễ (Offer, Traffic, Messaging hay Giá) $\to$ Đưa ra giải pháp trúng đích.
3. **So sánh Phương án Thực tế:** Đưa ra 3 phương án kinh doanh khả thi kèm theo điểm gãy xấu nhất (worst-case failure condition) và giả định sống còn (load-bearing assumption).
4. **Chuyển giao liều lĩnh sang Thực thi:** Chuyển kết quả sang `research` (nghiên cứu đối thủ), `scout` (rà soát tài sản sẵn có), `plan` (lên kế hoạch hành động theo Phase) và `cook` (viết sales copy, dựng phễu, chốt đơn).

---

## 🤝 Contributing & License

Distributed under the **MIT License**. Created by [abm-dungtq](https://github.com/abm-dungtq).
