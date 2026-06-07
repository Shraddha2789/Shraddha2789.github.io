# Sapiens: Deciding What Not to Build

**Company:** Sapiens International Corporation
**Product:** CoreSuite — Enterprise Insurance Platform
**Role:** Senior Product Owner
**Timeline:** October 2024 – Present
**Domain:** Insurtech · Enterprise SaaS · B2B · Policy Servicing

---

## Results at a Glance

| Metric | Result |
|---|---|
| Customer onboarding time reduction | **30%** |
| Transaction abandonment reduction | **25%** |
| Platform adoption increase | **15%** |
| Pre-production quality rate | **95%** |
| Features prioritized across releases | **50+ features, 6 releases** |

---

## Context

Sapiens CoreSuite is an enterprise insurance platform used by tier-1 insurance carriers globally. The product handles critical insurance operations: policy servicing, fund management, digital customer portals, and compliance workflows. The platform serves **500K+ end customers** through Sapiens' insurance carrier clients.

I joined as Senior Product Owner in October 2024. My mandate: define and drive the product roadmap for the next phase of platform evolution, with a specific focus on enabling digital portal integration for enterprise clients.

---

## The Problem

The backlog when I arrived had 50+ features, submitted by multiple clients, with no consistent prioritization methodology. Each client believed their request was the highest priority. Engineering had 6 release slots across the year. The math didn't add up.

The real problem wasn't execution — it was **clarity**:
- Which features created the most value for the most clients?
- Which features were table-stakes for contract retention vs. which were growth enablers?
- Which features were technically risky enough that shipping them in Release 2 instead of Release 1 would significantly reduce delivery risk?

Without answers to these questions, the roadmap was just a queue. And a queue isn't a strategy.

---

## My Role

- Own the product vision and roadmap for CoreSuite's policy servicing and fund management modules
- Lead cross-functional delivery with engineering, QA, architecture, and client success teams (4 teams total)
- Define and maintain prioritization framework for 50+ backlog items
- Drive client discovery — structured interviews with tier-1 insurance clients to validate priorities
- Own API design documentation for digital portal integration layer
- Lead UAT and pre-production quality process

---

## Process

### Building the Prioritization Framework

My first 30 days were spent understanding the backlog, not executing it. I ran:

1. **Client interviews** with 3 tier-1 clients to understand their 12-month digital roadmap and where our platform fit
2. **Engineering architecture review** with the lead architect to understand the technical dependencies between features
3. **Client success analysis** — what were the most common support tickets? What were clients complaining about, vs. what were they asking for? (These are often different.)

From this, I built a prioritization matrix using four factors:
- **Client breadth** — how many clients benefit (score 1–5)?
- **Strategic value** — does this advance platform differentiation or just maintain parity?
- **Technical risk** — does this depend on a complex architectural change that might slip?
- **Revenue linkage** — is this feature tied to a specific contract commitment or renewal?

Features scoring high on client breadth + revenue linkage became Release 1 and 2 priorities. Features high on strategic value but low on client breadth moved to Release 4–6. Features with high technical risk got moved adjacent to releases where engineering capacity allowed for spikes.

### The Hardest Prioritization Call

Release 3 had a conflict between two features:

**Feature A** — A digital self-service portal for policyholders (requested by 2 clients, moderate engineering complexity, but visible to end customers)

**Feature B** — An internal batch processing optimization (requested by 1 client, high engineering complexity, not customer-facing but critical for that client's renewal)

The internal metric said Feature A. The revenue signal said Feature B. I took both to the product steering committee with explicit trade-off framing: "If we do A, we have a better product story but risk this client renewal. If we do B, we protect revenue but delay the portal work that two other clients are waiting for."

Decision: We did Feature B, but I committed to the two clients waiting for Feature A that we'd accelerate it to Release 4 with dedicated capacity. This required me to de-prioritize two smaller feature requests in Release 4 — which required direct client communication to manage expectations.

That client retained. The two de-prioritized features were re-scoped for Release 5.

### Execution

The biggest delivery challenge was pre-production quality. CoreSuite integrates with multiple insurance carrier systems via APIs — and insurance carriers have extremely low tolerance for production defects. A policy processing error at 2am on a Sunday is not a minor bug; it's a compliance incident.

I introduced a **95% pre-production quality gate** — not as a formal metric at first, but as a working standard: every release went through API-level testing (using Postman) with me personally validating integration scenarios before UAT was opened to clients.

This slowed sprints slightly. It also meant we never shipped a P1 defect to a client during the 6 months I've been in the role.

---

## Key Decisions

| Decision | What I chose | Why | Trade-off accepted |
|---|---|---|---|
| Prioritization framework | 4-factor matrix (breadth, strategic, risk, revenue) | Makes trade-offs explicit and defensible | More overhead than gut-feel prioritization |
| Release 3 conflict | Protect renewal (Feature B) | Revenue certainty > roadmap aesthetics | Two clients waited an extra release cycle |
| Pre-production quality gate | 95% before UAT opens | Insurance clients cannot absorb production defects | Slightly longer delivery cycles |
| API design ownership | PO owns API docs, not just engineering | Prevents spec drift; clients expect PO-level technical fluency | More technical work for me as PO |

---

## Outcome

Six months in (current, ongoing):

- Customer onboarding time reduced by **30%** through digital portal integration improvements
- Transaction abandonment reduced by **25%** — driven by UX improvements informed by analytics
- Platform adoption increased by **15%** as new self-service capabilities went live
- **95% pre-production quality rate** — no P1 defects shipped to clients
- 50+ features triaged across 6 releases with clear stakeholder alignment

---

## What I'm Learning

*(This role is ongoing — this section reflects current work.)*

**1. Enterprise clients don't want what they say they want.**
They ask for features. What they actually need is confidence that the platform is moving in the right direction. My job is often to give them that confidence — through communication, prioritization transparency, and consistent delivery — as much as it is to ship a specific feature.

**2. Roadmap predictability is a product.**
For enterprise clients, knowing what's coming and trusting that it will actually ship matters as much as the feature itself. I've invested heavily in making our release communication cadence consistent and clear. This has improved client satisfaction without shipping a single line of code.

**3. Pre-production quality is a growth lever, not just a cost.**
Clients who trust the platform's reliability are more willing to take on new integrations and expand their usage. Every clean release is a trust deposit.

---

*Artifacts: Prioritization framework template · API design documentation (sanitized) · Release communication template*
