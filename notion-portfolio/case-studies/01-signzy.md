# Signzy: From 3 Days to 2 Hours — Reimagining KYC for Tier-1 Banks

**Company:** Signzy Technologies
**Role:** Product Owner — Digital Onboarding Platform
**Timeline:** January 2024 – September 2024
**Domain:** B2B Fintech · Digital Banking · KYC / Identity Verification

---

## Results at a Glance

| Metric | Before | After | Change |
|---|---|---|---|
| Customer onboarding time | ~3 days | <2 hours | **-93%** |
| KYC accuracy | Baseline | +35% improvement | **↑ 35%** |
| Customer acquisition speed | Baseline | 40% faster | **↑ 40%** |
| Revenue growth (platform) | Baseline | +25% | **↑ 25%** |
| Major contract renewals | — | 3 secured | **3 renewals** |

---

## Context

Signzy is a B2B fintech company that builds digital onboarding and identity verification infrastructure for Indian banks. Its clients include tier-1 institutions like **Yes Bank** and **IndusInd Bank** — banks that process hundreds of thousands of new account applications every month.

When I joined as Product Owner, Signzy had a working product but a growing problem: the KYC step in the onboarding funnel was becoming a revenue blocker.

---

## The Problem

> *"Our clients tell us their customers are dropping off at document verification. We're not sure why."*
> — Sales lead, first week

KYC (Know Your Customer) is a regulatory requirement: every Indian bank must verify a new customer's identity before opening an account. The process typically involves document submission, liveness checks (selfie-based verification), and compliance review.

The surface-level complaint: the process took 3 days and had high rejection rates.

**What I found when I dug deeper:**

Through client interviews with bank operations teams and analysis of drop-off data, I mapped the actual failure points:

1. **Document upload step** — 42% of users uploaded low-quality images (poor lighting, cropped edges). The validation happened server-side, hours later. By then, users had given up.
2. **Selfie liveness check** — The model we were using was not trained on the lighting conditions common in tier-2 city environments (high ambient light, low-contrast backgrounds). False rejection rate was high.
3. **No real-time feedback loop** — Users who failed document validation got a generic "submission rejected" email. They didn't know what to fix or how.

The root problem wasn't KYC being slow. It was that **users were failing silently** and we had no mechanism to help them recover.

---

## My Role

I owned the product end-to-end:
- Defined the problem through client discovery (interviews with Yes Bank and IndusInd Bank operations teams)
- Set roadmap priorities for the 9-month engagement
- Wrote specifications and acceptance criteria for engineering
- Managed stakeholder communication with bank clients
- Owned product analytics — built dashboards tracking conversion funnels, KYC pass rates, and rejection categorization
- Ran UAT with QA and client teams before each release

I worked closely with a 6-person engineering team, a data science team (for the AI model improvements), and compliance consultants to ensure every change met RBI guidelines.

---

## Process

### Discovery

I ran two rounds of discovery:

**Round 1 — Internal data:** Pulled 3 months of KYC transaction logs. Mapped the funnel stage-by-stage: where were users dropping, at what rate, and at what time of day. Found that 60%+ of failures happened in the first 10 minutes of the session — the document upload phase. This pointed to a UX problem, not a backend problem.

**Round 2 — Client interviews:** Spent a week talking to bank ops teams at Yes Bank and IndusInd. Their biggest pain wasn't the rejection rate — it was the *support ticket volume*. Each failed KYC generated a support escalation costing ~15 minutes of ops time. At scale, this was a significant cost centre.

**Insight:** The right metric wasn't "time to approve." It was "first-attempt success rate." If users passed on the first try, everything downstream got faster.

### Prioritization

I ran a value vs. effort matrix across 14 potential improvements. Ranked by impact on first-attempt success rate:

| Feature | Impact on Success Rate | Effort | Priority |
|---|---|---|---|
| Real-time document quality feedback | Very High | Medium | **P0** |
| Guided capture UI (frame overlay) | High | Low | **P0** |
| Retrain liveness model on India-specific data | Very High | High | **P1** |
| Real-time rejection with specific error reason | High | Medium | **P1** |
| Automated resubmission reminder flow | Medium | Low | **P2** |

### The Bet I Made

The data science team pushed to retrain the liveness model first — it was the "exciting" problem and the one with the most technical leverage. I pushed back.

**My argument:** Retraining the model would take 8 weeks and carried deployment risk (model updates needed RBI-aligned validation). The guided capture UI and real-time feedback loop could ship in 3 weeks with near-zero compliance risk. And our analysis showed 60% of failures were on document upload, not liveness. We were optimizing the wrong problem.

We shipped guided capture and real-time feedback first. The first-attempt success rate improved by 28% within the first month — without touching the AI model.

The model retrain followed in phase 2, delivering the remaining accuracy gains.

### Execution

- Worked with design to create a mobile-first guided capture experience (frame overlay, lighting indicator, auto-capture when quality threshold met)
- Wrote RBI-compliant specifications for every change (no data retention without consent, audit trails on all verification events)
- Built a rejection categorization taxonomy that ops teams could use to prioritize support queues
- Introduced a product analytics dashboard for clients — bank ops teams could now see their own funnel performance in real-time

---

## Key Decisions

| Decision | What I chose | Why | Alternative rejected |
|---|---|---|---|
| Phase order | UX improvements first, model retrain second | Faster time-to-value, lower risk, addresses the larger failure mode | Model retrain first — high effort, lower coverage of actual failures |
| Feedback granularity | Specific error codes with user-facing explanations | Reduces support tickets, enables user self-service | Generic "rejected" message — faster to build but zero learning for the user |
| Compliance approach | All changes reviewed by compliance consultant before sprint commit | RBI violations = contract loss; better to slow down than ship and scramble | Build first, get compliance sign-off later — too risky for a regulated product |

---

## Outcome

By the time I left Signzy:

- Customer onboarding time had dropped from ~3 days to under 2 hours
- KYC accuracy improved by **35%**
- Customer acquisition time decreased by **40%** (downstream effect of faster, higher-quality KYC)
- The platform contributed to **25% revenue growth** for Signzy — driven by both new client signings and 3 major contract renewals from existing clients
- Client support ticket volume from KYC failures dropped significantly, improving Signzy's NPS with its bank clients

---

## What I Learned

**1. First-attempt success rate is a better north star than average processing time.**
Average processing time masks the bimodal distribution — users who pass fly through; users who fail drag the average down. Optimizing first-attempt success rate fixes both.

**2. In B2B, your user's user is often the one you need to talk to.**
The banks were my direct clients. But the people actually struggling with KYC were their end customers — new account applicants. I had to understand both constituencies to solve the problem correctly.

**3. Compliance constraints can become differentiators.**
I was initially frustrated by how much slower everything moved because of RBI compliance requirements. By the end, I realized that Signzy's ability to ship compliant products reliably *was* the product. Banks couldn't build this themselves. That's why they paid for it.

---

*Artifacts: Product analytics dashboard design · KYC funnel mapping · Feature specification for guided capture UX*
