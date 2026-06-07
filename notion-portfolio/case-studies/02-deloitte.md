# Deloitte: Which GenAI Feature Do You Build First?

**Company:** Deloitte Digital
**Product:** TruServe — AI-Powered Contact Center Platform
**Role:** Product Consultant — Enterprise Solutions & Digital Transformation
**Timeline:** November 2021 – January 2024
**Domain:** Enterprise SaaS · GenAI · Healthcare · Fortune 500

---

## Results at a Glance

| Metric | Result |
|---|---|
| Operational efficiency gain | **60%** |
| Agent handle time reduction | **35%** |
| Program delivery | **$10M · 20% ahead of schedule** |
| GenAI features shipped | **10+** |
| Client satisfaction | Fortune 500 (Apple Inc., HCSC) |

---

## Context

TruServe is Deloitte's Salesforce-based platform for enterprise contact center management. It sits at the core of how large companies handle customer service — routing tickets, managing agent workflows, generating post-call documentation, and integrating with CRM systems.

In 2022–2023, as GPT-3 and then GPT-4 became viable for enterprise deployment, Deloitte had an opportunity and a challenge: **every client wanted "GenAI in their contact center," but no one could agree on what that actually meant or where to start.**

I was part of the team that figured it out — first at the product level (what to build and in what order) and then during a $10M implementation program at Health Care Service Corporation (HCSC), one of the largest US health insurers.

---

## The Problem

HCSC's contact center ran ~1 million customer interactions per year across 2,000+ agents. Their stated goal: "use AI to improve agent efficiency."

That's not a product brief. That's a category.

When I sat down with HCSC's operations leaders, I ran a structured discovery exercise: we mapped 180+ agent tasks across three business units (individual plans, employer benefits, provider relations) and scored each task on two dimensions:
- **Automation potential** — could AI reliably do this or assist with it?
- **Business impact** — what's the cost or consequence of this task being slow or error-prone?

What we found:

| Task category | Automation potential | Business impact | Volume |
|---|---|---|---|
| Post-call documentation | High | Medium | Very High |
| Smart email drafting | High | High | High |
| Real-time agent guidance (next best action) | Medium | Very High | High |
| Supervisor escalation routing | Medium | High | Medium |
| Sentiment analysis / QA flagging | High | Medium | Medium |

The highest-leverage targets were post-call documentation and smart email drafting — not the "exciting" real-time agent assist that leadership kept asking about.

---

## My Role

On TruServe product:
- Identified GenAI use cases through client workshops and internal product research
- Defined product requirements for 10+ AI automation features
- Worked with Deloitte's data science team to translate use cases into technical specifications
- Prioritized features across three client implementations

On the HCSC $10M program:
- Managed cross-functional delivery (100+ person team across Deloitte, HCSC IT, and vendor partners)
- Owned stakeholder communication with HCSC C-suite and operations leadership
- Ran product reviews, sprint ceremonies, and release planning
- Managed scope, timeline, and budget escalations

---

## Process

### The Prioritization Framework

GenAI feature prioritization is tricky because excitement and risk are often correlated: the features everyone wants to see (real-time agent assist, autonomous resolution) are also the highest-risk to get wrong.

I introduced a **risk-adjusted value framework**:

For each proposed feature:
1. What is the upside if it works well?
2. What is the downside if it gets it wrong? (In healthcare, wrong information = compliance liability)
3. How much training data / prompt engineering does it need to be reliable?
4. Can we measure whether it's actually working?

Applying this framework:

**Smart email drafting → P0**
High upside (saves 8–12 minutes per email), minimal downside (agent reviews before sending), requires little training data, easy to measure (email quality scores, time-to-send).

**Real-time agent guidance → P2 (not P0)**
Very high upside but high downside risk: if the guidance is wrong during a live call, the agent follows bad advice and the customer gets bad service. Needs extensive training data from HCSC's specific workflows. Not measurable until deployed. Too much risk to deploy early.

This was a hard conversation with HCSC stakeholders, who had been sold on the "real-time AI assistant" vision. My argument: *let's earn the right to do the high-risk feature by proving we can nail the low-risk ones first.*

They agreed. We shipped smart email drafting in sprint 4. It hit a 78% acceptance rate (agents accepted the AI draft without significant edits 78% of the time). That number became our proof point for expanding the program.

### Delivery

The $10M program ran 18 months. Key challenges:

**Challenge 1: Scope creep from AI excitement**
Every month, new GPT capabilities were announced. HCSC stakeholders kept adding "can we also do X?" to the backlog. I implemented a strict change control process: any scope addition had to go through a 3-step evaluation (impact on timeline, impact on budget, impact on integration complexity) before it could be added. This prevented three significant scope expansions that would have delayed delivery.

**Challenge 2: Change management > technology**
The hardest part of shipping GenAI features was not the technology — it was adoption. Agents were skeptical. They'd seen automation promises before and had experienced suggestions that were wrong or tone-deaf. We built an "AI confidence score" into the UI — agents could see how confident the model was in a given suggestion — and designed an easy override flow. This increased adoption by ~30% compared to our baseline assumption.

**Challenge 3: Cross-org alignment at HCSC**
HCSC's IT, Legal, Operations, and Business teams all had different definitions of "done." We ran monthly joint reviews with all four functions. Slow? Yes. Did it prevent a compliance-related launch delay that would have cost 6 weeks? Also yes.

---

## Key Decisions

| Decision | What I chose | Why | Alternative |
|---|---|---|---|
| Feature sequencing | Low-risk, high-visibility features first | Build trust before deploying high-stakes AI | Flagship features first — risky, harder to measure |
| Real-time guidance timing | Deferred to Phase 2 | Not enough training data; downside risk too high | Ship in Phase 1 — stakeholders wanted it, but data wasn't there |
| Adoption design | AI confidence scores + easy override | Skeptical agents adopt when they feel in control, not replaced | Clean AI output without override — faster to build, worse adoption |
| Scope control | Formal change control process | Prevents timeline slippage, protects delivery credibility | Accommodate all requests — faster short-term, catastrophic long-term |

---

## Outcome

By program completion:

- **60% operational efficiency improvement** across HCSC's contact center operations
- **35% reduction in average handle time** per agent
- **$10M program delivered 20% ahead of original schedule** — a significant achievement for an enterprise transformation of this scale
- 10+ GenAI features shipped, including smart email drafting, automated post-call documentation, QA sentiment flagging, and escalation routing
- Program became an internal Deloitte case study for GenAI transformation methodology

Separately, the TruServe product roadmap work I contributed to was used in pitches to Fortune 500 clients including Apple Inc.

---

## What I Learned

**1. "AI" is not a product requirement. A job-to-be-done is.**
Every stakeholder wanted AI. Nobody could tell me what problem they wanted it to solve. My job was to translate the category excitement into specific, measurable tasks that AI could actually do reliably.

**2. In regulated industries, the cost of being wrong is asymmetric.**
In healthcare, an AI system that's right 90% of the time but wrong 10% in dangerous ways is worse than a system that does nothing. This shaped every feature prioritization decision I made.

**3. Adoption is a product problem, not a training problem.**
The most technically impressive feature we shipped had the lowest adoption until we redesigned the UX to make agents feel in control. Feature quality ≠ adoption. You have to design for the skeptic, not the enthusiast.

**4. Delivery credibility is earned early.**
The reason we could expand scope in Phase 2 (adding higher-risk, higher-value features) is because Phase 1 shipped on time and on budget. Delivery credibility is currency in enterprise programs. Spend it carefully.

---

*Artifacts: GenAI feature prioritization framework · TruServe product requirements (sanitized) · HCSC program structure*
