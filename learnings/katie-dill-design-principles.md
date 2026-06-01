# Design Principles from Katie Dill (Head of Design, Stripe)

Source: Katie Dill's masterclass on the Stripe homepage redesign.

---

## 1. Website as Manifesto

Every screen must express a named company value — technical excellence, reliability, trust. Design choices are never neutral; typography, color, and motion are direct expressions of who you are.

**Rules:**
- Before designing any screen, name the value it must express.
- Show, don't tell. Use visual structure (bento layouts, motion, density) to communicate scale and capability — not text walls.
- Ask: "If someone read nothing on this page, what would they *feel* about us?"

---

## 2. Lean-Back Browsing

Users browse in a low-commitment, exploratory mode. Do not force them out of that state to get information.

**Rules:**
- Use modals for deeper detail, not new pages. Keep users in context.
- Apply progressive disclosure: show the minimum needed to orient, reveal depth only on demand.
- Respect cognitive budget. Every extra element costs attention — spend it deliberately.

---

## 3. The 7/10 Trap

AI reaches a "good enough" baseline fast. That's the starting point, not the finish line.

**Rules:**
- Use AI to accelerate to baseline (structure, copy, imagery, prototypes). Then stop and craft.
- Every AI-generated element requires intentional human curation before it ships.
- Ask: "What makes this feel *ours* and not generic?" If the answer is nothing, it's not done.
- The time AI saves is a budget for craft, not a reason to ship faster.

---

## 4. Fight Mediocrity

There is a constant gravitational pull toward "good enough." Small slides compound into product-wide erosion.

**Rules:**
- Name every compromise before accepting it. "We're shipping this even though X is weak because Y."
- Details compound. A blurry icon and a misaligned label and a vague CTA = a product that feels amateur.
- If a detail bothers you, fix it or explicitly decide not to. Ignoring it is not neutral.

---

## 5. MVQP — Minimum Viable Quality Product

Ship to learn, not to avoid judgment. But define the quality floor before you build.

**Rules:**
- Before starting, write down what "acceptable quality" looks like for this specific thing.
- Ship when you've cleared that floor, even if you haven't cleared your ideal.
- After shipping, treat user behavior as the real test — not internal approval.
- Do not let "we'll fix it later" substitute for having no quality floor at all.

---

## 6. Walk the Store

Everyone — designers, engineers, PMs — should regularly use the product end-to-end as a real user would.

**Rules:**
- Schedule recurring first-hand product testing. Make it a team ritual, not a QA phase.
- Look for dead ends: places users get stuck, confused, or abandoned.
- Look for seams: places where two product areas meet awkwardly because two teams didn't coordinate.
- The goal is coherence. Parts that work individually can still fail together.

---

## Pre-Ship Checklist (for any web experience)

Run this before shipping any screen, page, or interaction:

- [ ] **Manifesto check** — What value does this screen express? Is it visible without reading?
- [ ] **Lean-back check** — Does this respect browsing mode? Is progressive disclosure in place?
- [ ] **7/10 check** — Has every AI-generated element been curated by a human with taste?
- [ ] **Mediocrity check** — Are all compromises named? Are any details silently accepted as "fine"?
- [ ] **MVQP check** — Is the quality floor defined? Has it been cleared?
- [ ] **Walk the store** — Has someone used this as a real user, end-to-end, today?
