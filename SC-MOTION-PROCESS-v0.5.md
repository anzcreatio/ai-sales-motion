# APAC presales motion: target process v0.5 (sign-off candidate)

Status: **sign-off candidate.** All documents and workflows exist in draft; nothing is built in Creatio. See
[SIGN-OFF-PACK-v0.5.md](SIGN-OFF-PACK-v0.5.md) for what needs approving and [PILOT-GUIDE.md](PILOT-GUIDE.md) for how to run a deal. Owner: Renzo. Pilot: the local APAC team (BDRs, 8 AEs, 3 SCs).
Last updated 3 Nov 2026. Version history in §15.

---

## 0. Decisions so far

| # | Decision | Source |
|---|---|---|
| 1 | We define our own differentiators | Renzo, 2 Nov |
| 2 | **SC + Claude build by default.** SEs are a shared pool and an escalation path, not a step | Renzo, 2 Nov |
| 3 | Industries: **BFSI, Manufacturing, General industry**. The motion must be ready for all three | Renzo, 3 Nov (replaces "Banking first") |
| 4 | Two pre-contract documents: a customer **Solution Proposal** (sales) and a **Partner Handover Pack** (enough for the partner to run its own discovery, never a full spec) | Renzo, 2 Nov |
| 5 | Pilot locally first | Renzo, 2 Nov |
| 6 | Process before tooling: nothing is built in Creatio until this process is agreed | Renzo, 2 Nov |
| 7 | **Hypothesis-led.** Customers rarely give artefacts or detail. Our research, industry packs and AI form the hypothesis; the customer confirms or corrects it | Renzo, 2 Nov |
| 8 | **Discovery = one 30-min call (max 45), ≤20 min of real discovery.** Minimise customer calls | Renzo, 2–3 Nov |
| 9 | Call 2 is a **configured** demo (their language, roles, stages), not just hypothesis validation | Renzo, 2 Nov |
| 10 | AEs are weak at qualifying, so qualification is woven into discovery and **scored by AI**, with an SC go/no-go | Renzo, 2 Nov |
| 11 | Templates are **generic**; industry content plugs in via Industry Packs | Renzo, 2–3 Nov |
| 12 | BDRs earn the meeting with a short card and **park** discovery. One forked card covers **CRM vs AI Studio** | Renzo, 3 Nov |
| 13 | One Discovery Brief is the single source. Every later document is generated from it | proposed, not challenged |
| 14 | **AI Studio is bundled with every Business Studio licence** (since 1 May 2026; AI use bought as credit packages) and can still be sold standalone if necessary. The P / A track describes the **buyer's interest**, not the licence | Renzo, 3 Nov (revised) |
| 15 | **The Sales Director sponsors the go/no-go gate** | Renzo, 3 Nov |
| 16 | **Simplified flow for the current team maturity** (§4.0): BDR identifies CRM / Business Studio / AI Studio and asks the 6 questions (recorded) → SC + Claude turn the transcript into a playback slide, a solution-hypothesis slide and a ≤ half-day light configuration ([FM workflow](workflows/FM-First-Meeting-Prep.md)) → first SC meeting shows all three. Guardrails: research behind the hypothesis; "you told us" vs "we think" kept apart; config only for confirmed pains; booking rule still applies | Renzo + team, 6 Nov |

## 1. Purpose and success measures

**Purpose:** win more deals, faster, by having every BDR, AE and SC run the same AI-powered motion. It turns a short
conversation into a demo of the customer's own problem solved in Creatio, then into a proposal and a partner
handover, without extra calls and without depending on who is in the room.

| Measure | Target (to baseline in the pilot) |
|---|---|
| **Win rate** | Up. This is the real goal; the rest are means |
| Discovery → demo **offered** (our side; the customer's calendar may push the actual date) | ≤5 working days |
| Customer meetings before the proposal | ≤2 (discovery + demo) |
| Demo scenes with pain + KPI + differentiator | 100% |
| Deals demoed that passed go/no-go | 100% |
| Partner re-asks the basics after handover | ~0 |

## 2. Principles

1. **Pain before product.** No demo scene without a named customer pain, a KPI and a differentiator.
2. **Homework before the customer's time.** We arrive with a hypothesis; the customer corrects it.
3. **Every touchpoint shows a differentiator**, from the first discovery slide onwards.
4. **One source, many outputs.** Brief → runbook → Proposal → Partner Pack. Claude generates; the SC curates.
5. **Assemble, don't build.** Demos come from Core + Industry modules; per-deal work is the customer layer.
6. **Qualified before we invest.** No task, no demo.
7. **Only propose what is safe to build** with approved patterns, and say honestly what is assumed.
8. **Light enough for 3 SCs.** Gates are checklists, not meetings.

## 3. Solution architecture: four layers

| Layer | What it is | Industry-specific? |
|---|---|---|
| **1 Motion** | Stages, gates, cards, AI workflows, one-pager, scorecard | No. One for all |
| **2 Assets** | **Core pack** (= General industry) + **Industry Packs** (BFSI, Manufacturing) + differentiator catalogue + approved build-pattern catalogue + master sandbox modules | Packs only |
| **3 AI layer** | Packaged Claude workflows that turn each input into a standard output (§10) | No |
| **4 People** | Roles, pack ownership, weekly deal review on scorecards, monthly asset harvest (§11) | No |

---

## 4. The motion

### 4.0 Simplified flow (current, decision 16)
| Step | Who | Output |
|---|---|---|
| 1 BDR call | BDR | Identify CRM / Business Studio / AI Studio (or a mix); ask the 6 questions in order; record it ([call sheet](TEMPLATE-BDR-Card-and-Handoff-v0.4.md)). An SC who joins goes one layer deeper on each |
| 2 Prep | SC + Claude ([FM](workflows/FM-First-Meeting-Prep.md)) | Transcript → playback slide + solution-hypothesis slide (Creatio template) + light-config brief + meeting plan |
| 3 Light config | SC (demo toolkit) | ≤ half a day: their name, terms, stages, 1–2 example records, one prepared live change; only for confirmed pains |
| 4 First SC meeting | AE + SC | Playback ("did we get this right?") → hypothesis → the first take in Creatio → change it live → closing question ("could this fix [their top pain]?"): yes with a named person and date → commercials; want more → solution summary slide, they pick what to see next |

The full motion below (W1–W5) stays as the reference and for later stages (W3 for a deeper demo, W5 for the Proposal and Partner Pack).

```
 BDR call ─► Prep ─► Discovery ─► Go/No-go ─► "What we heard" ─► Design + build ─► Value demo ─► Proposal ─► Partner handover
 (BDR)     (AI+SC)  (30-min call)  (SC gate)      (AE sends)         (SC+AI)        (1 meeting)    (≤48 h)    (pre-contract)
  Day -n   Day 0-1    Day 1        Day 1-2         Day 2              Day 2-6         ~Day 7         Day 9     when the deal firms
```

**Customer time before the proposal: the BDR call + 2 meetings (30 min discovery + the demo).**

| # | Stage | Owner | Customer time | What happens | Output | Gate |
|---|---|---|---|---|---|---|
| 0 | **BDR call** | BDR | Cold call | 5-question forked card (CRM / AI Studio). Captures the trigger in their words, then parks discovery. Books the joint discovery | Handoff form (mandatory to book) | Booking threshold |
| 1 | **Prep** | AI, checked by the SC | none | Account research + matching Industry Pack (or Core) → hypotheses, journey picture, KPI ranges, the 3 things to learn | **Pre-call pack** + pre-filled 20-minute card | *No pack, no call* |
| 2 | **Discovery** | AE runs the meeting; SC leads discovery | **30 min** | 1 hypothesis slide; they pick and rank; "Where does it break?"; size it; why now / who signs; book the demo. **No Hello Deck** | Recording or 20-minute card notes | — |
| 3 | **Go / no-go** | AI scores; SC decides | none | Discovery Brief with evidence tags; qualification score with evidence quotes and red flags | Green / Amber / Red | **Go/no-go** |
| 4 | **"What we heard"** | AI drafts; AE sends ≤24 h | ~5 min async | 1 page: their journey + pain points, the outcome we'll show, 3–5 yes/no checks, agenda + attendees. **No product screens.** Forwardable | Corrections; the champion sells the demo internally | — |
| 5 | **Design + build** | SC + AI (SE if escalated) | none | Value map → runbook with validation moments → stand from Core + Industry modules + customer layer → readiness check, click path, backup video | Ready stand | **A, B** |
| 6 | **Value demo** | SC presents; AE runs the meeting | 1 meeting | Opens on their KPI outcome; scene per pain (pain → proof → value); 3–5 validation moments; live change on correction; **mutual action plan** | Confirmed value case | — |
| 7 | **Solution Proposal** | AI drafts; SC curates | none | ≤48 h after the demo, from the Brief + demo recording | Customer proposal | — |
| 8 | **Partner Handover Pack** | AI drafts; SC curates | none | Scope as sold, conceptual solution, reference demo, demo-only items, **assumption register = the partner's discovery agenda** | Partner pack + walkthrough | **C** |

### 4.1 Two tracks: Platform (CRM / no-code) and AI Studio

**One motion, two tracks.** The 9 stages, the gates and the evidence tags are the same. What changes per track is
the discovery focus, the qualification bar, the assets we build from, how we prove the demo works, and what goes
into the Proposal and the Partner Pack. **AI Studio is bundled with every Business Studio licence** (since 1 May 2026), and
can be sold standalone, often alongside an existing CRM (Salesforce, Dynamics) or ERP. So the track describes what
the buyer came for, not what they license.

The BDR tags each lead at Stage 0. The SC confirms the track at go/no-go.

| Track | When | Default |
|---|---|---|
| **P: Platform** (CRM / no-code apps) | They want to replace or build: CRM, service, onboarding, portals, workflow | Every P demo includes **one AI scene** (D3): AI Studio is part of what they'd license. Every P Proposal sizes **AI credits** |
| **A: AI Studio** | They want AI to do a task, usually on top of systems they keep | Show the agent acting **on a platform** with governance (D3 + D5), never a chatbot in isolation |
| **P+A: Both** | Platform need + a named AI task | Run as **P**, with the AI task as the hero scene |

#### Stage by stage

| Stage | P: Platform | A: AI Studio |
|---|---|---|
| **0 BDR** | CRM branch: area · current system · users | AI branch: **task to automate** · where the work happens · AI policy/owner · existing AI tools |
| Booking threshold | Interest area + trigger + a business person attending | **A named task** + a business owner. "Exploring AI" → nurture or an AI ideas workshop |
| **1 Prep** | Industry Pack → pain hypotheses + journey picture | **AI use-case library** → 5 task hypotheses for their industry + a task picture (trigger → inputs → decisions → actions → systems) |
| **2 Discovery** ("Break" block) | "Walk me through where this goes wrong" (journey) | "Walk me through the task": how often, how long each, what decisions, which systems, what goes wrong, who checks it |
| Discovery "Size" block | KPI range for the journey | **Volume × time per task**, error/rework rate, customer wait time |
| Extra questions | — | "What would the agent be allowed to do on its own, and what needs a human?" · "Where does the data live, and can we reach it?" · "Who owns AI risk here?" |
| **3 Go/no-go** | Standard (§5.3) | **Stricter, all four needed:** named task · business owner · data reachable · no policy blocker. Missing any → Red, or Amber with an AI ideas workshop (AI Studio-only deals; P+A follows §5.3) |
| **4 One-pager** | Journey + pain points + outcome | Task picture + what the agent will do vs what a human approves + outcome (e.g. "minutes per task from 20 to 2") |
| **5 Design + build** | Core + Industry modules + customer layer; config levels L1–L4 | **Agent patterns** + AI master sandbox; their task, their tone, their policy; simulated connection to their named systems (L4 is usually needed) |
| Proof before demo (Gate B) | Click-path readiness after reset | Click-path readiness **plus an agent test set**: 10–20 realistic inputs incl. edge cases and "should refuse" cases, all passing |
| **6 Value demo** | Opens on the KPI; scene per pain; live no-code change | Opens on the KPI; **the agent does their task end to end** (chat or voice) → asks a human to confirm → the action lands in the system → the audit trail; live change = a business user changes a rule or instruction and the agent behaves differently |
| **7 Proposal** | Phased roadmap | **A measured pilot** (one task, 4–8 weeks, success KPIs and exit criteria agreed up front) + scale-out roadmap + **AI governance section** (data, security, human control, audit) |
| **8 Partner Pack** | Objects, processes, pages, integrations | **Agent specification**: purpose, skills, tools/processes it calls, data access, guardrails, human checkpoints, the test set, prompt notes. Integration points to their systems |
| Value maths | Journey KPI from → to | Volume × time saved × cost + quality (errors, wait time, deflection) |
| Strongest differentiators | D1 no-code speed · D2 one platform · D4 business owns the rules | D3 AI that acts, governed · D5 fits your landscape · D1 (change the agent without code) |
| Likely competitors | Salesforce, Dynamics, local CRMs | Microsoft Copilot Studio, Salesforce Agentforce, ServiceNow, point AI vendors, in-house builds *(to verify with research)* |
| SE escalation | Custom UI, real integrations | **Voice agents**, real integrations, new agent patterns |

#### Track risks to manage

| Risk | Track | Control |
|---|---|---|
| "AI tourism": interest with no task, owner or budget | A | Stricter go/no-go; AI ideas workshop only for target accounts |
| Pilots that never convert | A | Pilot exit criteria and the commercial next step agreed **before** the pilot starts |
| Security/compliance blocks the deal late (especially BFSI) | A | AI governance pack sent after discovery, not after the demo; ask "who owns AI risk?" in discovery |
| Feature comparison against the incumbent CRM | P | Lead with their pain and KPI; show D1/D4 live; one AI scene to lift the conversation |
| Platform deals with no AI story look dated | P | One AI scene in every P demo |

**AI ideas workshop (optional, target accounts only):** 45 min; we bring 5 use cases from the AI use-case library
for their industry, and they pick one. It turns "we're exploring AI" into a named task, then rejoins the motion at Stage 2.

---

## 5. Stage detail

### 5.0 BDR call
- Card, parking lines and handoff form: [TEMPLATE-BDR-Card-and-Handoff-v0.4.md](TEMPLATE-BDR-Card-and-Handoff-v0.4.md). Cold outreach opens with three pains (customer picture → CRM · systems can't keep up → no-code · AI past the pilot → AI agents) and the customer picks one; raised hands open with "What prompted it?". Then six questions for everyone. One-page sheet; the call is recorded and W1 extracts the handoff from the transcript.
- The BDR **does not** discover, pitch, demo, price or answer technical questions. When they hear a pain, they write down one
  sentence in the customer's words and park it.
- **Booking threshold** (light; BDRs are not gatekeepers): interest area + trigger + at least one business-side
  attendee (AI Studio: a named task). IT-only and "send me info" leads go to nurture.
- **Meetings we generate ourselves** (no BDR): the AE or SC fills the same handoff form with the signal instead of a
  trigger; W1 runs its Outbound branch. The booking threshold then becomes the goal of the call: if it isn't met, the
  next step is nurture or an AI ideas workshop, not a demo.
- The BDR books the **joint AE + SC discovery** directly. The AE gets the same handoff form, so there is no separate
  AE handoff step (to confirm, §14).

### 5.1 Prep (AI pre-call pack): [W1-Pre-Call.md](workflows/W1-Pre-Call.md)
**Who runs it:** the AE or the SC, once the discovery is booked (once per booked discovery, not per lead).
Input: the handoff form (+ BDR recording if one exists). Claude produces:
1. Account research: strategy, annual report, news, regulator items, tech stack, job ads.
2. 5 pain hypotheses from the Industry Pack, ranked for this account: **4 owned by the people attending + 1
   deliberate "expansion" hypothesis** owned by another team (a miss there is still useful: it maps the org and a
   possible second buyer). Every hypothesis in the pack carries its usual owner (business function, IT, another team).
3. One journey picture for the most likely pain.
4. KPI ranges to probe.
5. The 3 things we must learn.
6. The **20-minute card pre-filled** (Part A) and the one-slide "What we see at organisations like you".

**The SC always checks it** (about 10 minutes), whoever ran it: the test run produced one wrong number that only a check caught. **No pack, no call.**

### 5.2 Discovery: the standard 30-minute call (≤20 min of discovery)

| Min | Block | Lead | Anchor question (said word for word) | Captures |
|---|---|---|---|---|
| 0–2 | Set-up | AE | "OK if we record so we don't miss anything?" | Consent |
| 2–6 | **Pick** | SC | "Here's what we see at organisations like yours. Which are true for you, and which hurts most?" | Ranked pains, their words |
| 6–13 | **Break** | SC | "Walk me through where this goes wrong. Where does it get stuck?" (journey on screen) · AI Studio: "Walk me through the task" | Steps, roles, bottleneck, their terms |
| 13–17 | **Size** | AE | "Roughly how long or how many today: closer to X, Y or Z?" · "What happens if nothing changes in 12 months?" | KPI range, consequence |
| 17–20 | **Who and why now** | AE | "Why now?" · "Who'd sign off a fix?" · "Who else wants this fixed?" | Why now, economic buyer, champion |
| close | **Commit** | AE | "Let's show you this working on your process. Who should be there, and when?" | Demo date, attendees, scenario |

The rest of the 30 minutes covers intros and the one-slide pitch.

**What 20 minutes can deliver:** 1–2 ranked pains, where *one* journey breaks, 1–2 KPI ranges, 3 qualification
signals, demo agreed. **It can't deliver** a full process, rules for several journeys, a full value case or full
MEDDPICC. Those gaps move to the one-pager, the demo's validation moments and the demo close.

**Live notes:** the 20-minute card, one page, generic, forked by track: [TEMPLATE-Discovery-Card-v0.2.md](TEMPLATE-Discovery-Card-v0.2.md).
The earlier 2-page notes template is archived; its extra fields now come from Claude's Brief output.

### 5.3 Go / no-go (qualification scorecard)
Claude scores the call (transcript or notes) on MEDDPICC + why now + commitments, with **evidence quotes** and
**red flags**. Commitments weigh most: demo booked in the call, economic buyer/influencer attending, champion
forwards the one-pager, **they'll send us one thing** (a number, report, sanitised screenshot or process document;
same for every industry).

**Build depth follows the score** (SC effort scales with deal quality):

| Result | Rule | What we build | SC effort |
|---|---|---|---|
| **Green** | Ranked pain with a consequence + why now + **economic buyer named** + demo booked with a business owner | Full **L3** demo: their terms, rules, numbers (L4 where integration is a buying criterion) | 3–4 days |
| **Amber** | Pain clear, but the economic buyer isn't named, or no why now | **L2 reference demo**: Core/Industry modules with their logo and terms, no custom rules. Upgrades to Green if the AE closes the gaps before the build | ~1 day |
| **Red** | No pain above "nice to have", IT-only, already chose a vendor, or refused the demo date/attendees | No live demo. Send the [Red follow-up email](templates/TEMPLATE-Red-Followup-Email-v0.1.md): a 4–6 min industry video ([library](modules/VIDEO-LIBRARY-PLAN-v0.1.md)) + the 2–3 missing questions; a reply re-runs W2 | ~1 hour (AE) |

If the **decision process is unknown** (any colour), it must be asked in the one-pager and again at the demo close.

**The SC signs the go/no-go; the Sales Director sponsors the gate** and settles disputes with AEs.

**P+A deals get two results.** The P result decides whether we demo. If A is Amber, the AI scene is still shown
(on simulated data), but no AI pilot is proposed until A is Green (task + owner + data reachable + no policy blocker).

The remaining qualification (decision process, paper process, competition) is asked in the one-pager and at the demo close.

### 5.4 "What we heard" one-pager
Within 24 h. Content: their journey with their pain points marked (their words) · the outcome we'll show
("approval from ~10 days to ~3") · 3–5 yes/no checks (our assumed rules/defaults) · demo agenda + who should
attend · 1–2 open qualification questions. **No product screens**, to keep the wow for the room. It is designed to be
forwarded internally by the champion.

### 5.5 Design + build
- **Design: [W3](workflows/W3-Demo-Design.md)** (SC, Claude Code) produces the Demo Design Pack: value map (pain → KPI →
  required capability → differentiator → proof moment → module), storyline, build plan with SC hours, the **demo script**,
  decision values with evidence tags, 3–5 **validation moments** with rehearsed live changes, and the close sheet.
- **Runbook and build:** the demo script goes to the toolkit's `creatio-demo-runbook` (the runbook the SC approves),
  then `creatio-demo-build` (W4).
- **Configuration levels.** Target L2–L3 for every deal; L4 where integration is a buying criterion.

  | Level | What the customer sees |
  |---|---|
  | L1 | Branded reference process |
  | **L2** | Their language, roles, stages |
  | **L3** | Their rules, thresholds, KPI baselines |
  | L4 | Simulated sync with their named systems |

- **Assembly:** Core modules + Industry module + customer layer (brand, terms, seed data, thin package). SE only
  for escalation items (§11).

### 5.6 Value demo
Follows **Great Demo!**: do the last thing first (open on their outcome and the Critical Business Issue). Each scene runs
situation (their pain and CBI) → illustration of the result → do it (the proof moment) → peel back the layers only as
far as they ask → summarise the value + metric. 3–5 planned "We assumed X, is that right?" moments; a correction triggers a **live no-code change**
(D1). The AE closes with the remaining qualification questions and a **mutual action plan** (steps, owners, dates to
decision).

### 5.7 Solution Proposal and 5.8 Partner Handover Pack
Templates: [Solution Proposal](templates/TEMPLATE-Solution-Proposal-v0.1.md) (Shipley 4-box summary, Command of the
Message structure, Great Demo! CBI/Delta/Critical Date, Forrester TEI-style conservative value case, mutual action plan) ·
[Partner Handover Pack](templates/TEMPLATE-Partner-Handover-Pack-v0.1.md) (deal context, commercial constraints,
commitments made in the sale, conceptual solution outline, assumptions register, discovery agenda by review area).
Both are generated together by [W5](workflows/W5-Close.md) from the Brief updated after the demo, so they can't contradict
each other; W5 runs the Gate C consistency check.

---

## 6. Gates (checklists, not meetings)

**Go / no-go** (after discovery): see §5.3.

**Gate A: design (before any build)**
- [ ] Every scene traces to a pain, in the customer's words
- [ ] Every scene names a differentiator; the **core set** appears at least once: **D1 + D3**, plus **D2** (Track P) or **D5** (Track A); P+A shows both; **manufacturing demos always show D5** ([catalogue](DIFFERENTIATOR-CATALOGUE-v0.1.md))
- [ ] ≥60% of the scenario's **decision values** (rules, thresholds, limits, routing, document requirements, what the AI may do alone) are Confirmed or Inferred; the rest are validation moments, logged checks or labelled pack defaults ([W3](workflows/W3-Demo-Design.md) rule 6)
- [ ] Every scene uses an **approved build pattern** (until the pattern catalogue exists: a named Core/Industry module) with a buildability rating (green OOTB / amber config + caution / red code or integration, which needs an SE or partner sign-off)
- [ ] The demo opens with the outcome, not the login screen
- [ ] Each pain has a KPI (from → to), even if it's a range
- [ ] Peer check by another SC: 15 min, async, on the runbook

**Gate B: proven**
- [ ] Every scene passes readiness on the stand after a reset
- [ ] Reset works and is documented
- [ ] Backup video exists

**Gate C: handover**
- [ ] The Partner Pack marks every item *demo* / *assumed* / *unknown*
- [ ] Open questions for partner discovery are listed per area
- [ ] No contradiction with the Proposal the customer saw

## 7. Evidence tags (used in every document)

| Tag | Meaning | In the Proposal | In the Partner Pack |
|---|---|---|---|
| **Confirmed** | The customer said it (quote, timestamp) | Stated as fact | Baseline |
| **Inferred** | From research about this customer | "We understand…" | Verify |
| **Assumed** | Industry Pack default | Listed as an assumption | **A discovery item** |

## 8. Documents and templates

| Document | Audience | Produced by | Status |
|---|---|---|---|
| [BDR call sheet](TEMPLATE-BDR-Card-and-Handoff-v0.4.md) · [Word, one page](TEMPLATE-BDR-Call-Sheet-v0.4.docx) (one page: cold and raised-hand openers, 6 questions, booking rule; transcript replaces the form) | BDR, AE | BDR / AE | Draft v0.4 · not yet used on a call |
| Pre-call pack (research, 4+1 hypotheses, slide, card Part A) | AE, SC | [W1](workflows/W1-Pre-Call.md) | Draft v0.4 (extracts the handoff from the BDR transcript) · blind-tested on a real bank; used on 2 live deals |
| [Discovery slides](templates/TEMPLATE-Discovery-Slides-v0.1.pptx): slide 1 hypotheses (W1 Output 8), slide 2 journey or task with likely breaks (Output 4); talk track in the notes · [worked example](tests/w1-test-01-great-southern-bank/04-discovery-slides-example.pptx) | Customer (on screen) | AE pastes from W1 | Draft v0.1 · Creatio template |
| [20-minute discovery card](TEMPLATE-Discovery-Card-v0.2.md) (forked P / A) | AE, SC | AE (live notes) | Draft v0.2 · mock-tested |
| SC summary · Discovery Brief (evidence only) · qualification score + go/no-go · "What we heard" one-pager · gaps list | Internal / customer | [W2](workflows/W2-Post-Call.md) | Draft v0.2 · mock-tested; re-tested on 2 live calls (Suntory, PRC) |
| Demo Design Pack: value map, storyline, build plan, demo script (input to the toolkit's runbook), validation moments, close sheet with a mutual action plan draft, Gate A | Internal / AE | [W3](workflows/W3-Demo-Design.md) | Draft v0.2 · mock-tested (predicted both live changes; missed one adoption objection, now covered) |
| [Solution Proposal](templates/TEMPLATE-Solution-Proposal-v0.1.md) | Customer | [W5](workflows/W5-Close.md) | Draft v0.1 · mock-tested |
| [Partner Handover Pack](templates/TEMPLATE-Partner-Handover-Pack-v0.1.md) | Partner | W5 | Draft v0.1 · mock-tested |
| [AI governance pack lite](AI-GOVERNANCE-PACK-LITE-v0.1.md) | Internal | SC | Draft; official answers pending (9 internal asks) |
| [On-prem sizing rules v0.1](apac-sc-motion/knowledge/SIZING-RULES-v0.1.json) + skill [`sc-sizing`](apac-sc-motion/skills/sc-sizing/SKILL.md): calculator fetched live, rules R1–R31 (Academy + infra team), recommended + reduced option per environment, storage plan; customer `NN-sizing.docx`/`.xlsx` worded as pending infra review, `NN-sizing-internal.md` | Customer (after infra review) / internal | SC; infra review Sergey Sinienok | v0.1 · tested on 2 infra-reviewed cases |
| [Confidential terms v0.1](apac-sc-motion/standards/CONFIDENTIAL-TERMS-v0.1.md): a customer's confidential terms stay in the deal folder, generic labels everywhere shared, `confidential.py` scan · [As-built template v0.1](apac-sc-motion/knowledge/TEMPLATE-As-Built-v0.1.md) for existing customers (`sc-guide` mode D) | Internal | SC + Claude | v0.1 (16 Nov 2026, plugin 0.24.0) |
| [Channels and integrations playbook v0.1](apac-sc-motion/knowledge/CHANNELS-AND-INTEGRATIONS-PLAYBOOK-v0.1.md): what is native vs Marketplace vs simulated for integrations, chat channels (WhatsApp, Messenger, Instagram, Telegram, SMS, web chat), social comments and WhatsApp/SMS from campaigns; recipes, demo routes, pre-demo checklist, lead times. From Academy 8.3 + v10, 18 Nov 2026; not yet proven on a stand | Internal | SC + Claude (W3, `sc-demo-plan`) | v0.1 (18 Nov 2026), documentation only |
| [Delivery Assurance](apac-sc-motion/knowledge/DELIVERY-ASSURANCE-v0.2.md): framework, 3 packages + Freedom, when to raise it for partner delivery risk, where it shows up with customers, can say / don't say. No prices in any output | **Internal only** | SC + AE (owner Alex Klochkov) | v0.2 (16 Nov 2026); currency open |
| [M6 live-change kit](modules/M6-LIVE-CHANGE-KIT-v0.1.md): 4 change tiers, demo rules object, 21-entry catalogue (Core, BFSI, Manufacturing), presenter protocol | SC | Pack owners | Design v0.1 · harvested from Scentia; T1/T2 times not yet measured |
| [Demo video library plan](modules/VIDEO-LIBRARY-PLAN-v0.1.md) (4 industry videos, scene clips, backup videos; toolkit-recorded) · [Red follow-up email](templates/TEMPLATE-Red-Followup-Email-v0.1.md) (drafted by W2) | Customer (Red/Amber) | Pack owners · AE | Plan v0.1 · videos need built modules; interim = public Creatio videos; hosting tool to decide |
| **Learning loop (pilot) = [LEARNING-LOOP-v0.1](apac-sc-motion/standards/LEARNING-LOOP-v0.1.md) + skill [`sc-ready`](apac-sc-motion/skills/sc-ready/SKILL.md)** (18 Nov 2026): call it first (SC's 3 lines before Claude's, in FM and demo plan), 💡 Learn points (max 2, by impact), readiness check before a meeting (quiz first, crib after). Private log on the SC's PC | SC only | SC + Claude | v0.1 · pilot, Renzo only, 2 weeks (to 2 Dec) |
| **FM v0.7 = plugin skill [`sc-first-meeting`](apac-sc-motion/skills/sc-first-meeting/SKILL.md)** (since 11 Nov 2026): transcript → standard deck + light-config brief (Business Studio, then AI) + meeting plan. Superseded: [FM v0.2](workflows/FM-First-Meeting-Prep.md) and its [3-slide builder](templates/_build/build_first_meeting_slides.py) | SC (customer sees the deck) | SC + Claude | v0.7 (18 Nov: step 1b call it first, pilot) · v0.6 (13 Nov: agenda with today's goal = the closing question; meeting card) · v0.5 (13 Nov: asks introduction or detailed demo first) · v0.4 (12 Nov: website + customer documents as inputs) · Phase 0; used on H&G, Suntory, Telkomsel as v0.2 |
| **[Document standard v0.1](apac-sc-motion/standards/DOC-STANDARD-v0.1.md)** + doc kit (`standards/doc-kit/creatio_doc.py`) | SC, customer | SC + Claude | v0.1 (18 Nov: every Word document in the Creatio look, PDF through Word) |
| **[Deck standard v0.6](apac-sc-motion/standards/DECK-STANDARD-v0.6.md)** + builder skill [`sc-deck`](apac-sc-motion/skills/sc-deck/SKILL.md) (`deck.json` per deal → deck; corporate slides from SharePoint `Slide-library`) | SC, customer | SC + Claude | v0.6 (18 Nov: eight visual slide types in the creatio.com style) · v0.5 (16 Nov: no title kickers, card agenda, owners and minutes in the notes) · v0.4 (13 Nov: agenda "Today's goal" = closing question, builder checks) · v0.1 · rebuilt H&G, Suntory, Telkomsel decks from `deck.json` |
| [Plugin repo `apac-sc-motion`](apac-sc-motion/README.md): skills, standards, templates, knowledge copies, library, lessons. **Its `knowledge/` copies of the packs, catalogue and governance pack are what SCs use; change them there** | All SCs | Renzo | v0.1.0 · local git, host to decide |
| [Shared Claude project setup kit](CLAUDE-PROJECT-SETUP-v0.1.md): instructions to paste, 11 knowledge files, per-deal use, test | Renzo, AEs, SCs | Renzo | Draft v0.1 · not yet built (3 blockers in §0) |
| Track A extras: agent specification (in the Partner Pack §4.6) · agent test-set template · AI pilot section (Proposal §8) | Customer / partner | W5 / SC | Partly in templates; test-set template not written |

## 9. Shared libraries

### 9.1 Core + Industry Packs
**Files:** [packs/INDUSTRY-PACK-TEMPLATE-v0.1.md](packs/INDUSTRY-PACK-TEMPLATE-v0.1.md) (10 sections, used by every pack) · [packs/CORE-PACK-v0.1.md](packs/CORE-PACK-v0.1.md) · overlays [packs/BFSI-PACK-v0.1.md](packs/BFSI-PACK-v0.1.md) and [packs/MANUFACTURING-PACK-v0.1.md](packs/MANUFACTURING-PACK-v0.1.md) (all drafts, 3 Nov 2026; research in `research/`). **Manufacturing rule (approved by Renzo, 3 Nov 2026):** D5 is shown in every manufacturing demo (P or A), and an incumbent CRM is assumed to stay. The template's 10 sections supersede the 8 listed below.

Core = General industry; BFSI (banking + lending first; wealth note; insurance later) and Manufacturing (use cases +
coexistence, not CRM) are overlays. Each SC owns one pack and harvests it after every deal. Only real deals count as
hypothesis hits.

### 9.2 Differentiator catalogue

Maintained in [DIFFERENTIATOR-CATALOGUE-v0.1.md](DIFFERENTIATOR-CATALOGUE-v0.1.md): D1–D7 with verified proof points,
competitor facts and a "don't use" list. **Core set (approved):** D1 + D3 in every demo, plus D2 (Platform) or D5 (AI
Studio); manufacturing demos always show D5.

### 9.3 Approved build-pattern catalogue (new)
Proven OOTB/no-code patterns, each with a buildability rating, build notes and **partner handover notes**. Gate A
only accepts scenes built from catalogue patterns, which is what makes proposals safe to build and hand over.
It covers both tracks: platform patterns (pages, processes, rules, portals) and **agent patterns** (§9.4).

### 9.4 AI Studio track assets (new)

| Asset | Content | Owner |
|---|---|---|
| **AI use-case library** | Per industry (Core, BFSI, Manufacturing): 5–10 tasks · what the agent does vs the human · systems touched · value maths · proof moment | SC pack owners (one section in each pack) |
| **Agent pattern catalogue** | Proven agent shapes, e.g. intake + triage, document check, prepare-and-confirm, customer self-service (chat/voice), internal copilot on records. Each with tools/processes, guardrails, buildability rating, handover notes | SC + SE |
| **AI master sandbox** | Reusable agents + tools + a simulated "their CRM/ERP" connection (Salesforce-like, SAP-like) to prove coexistence | SC + SE |
| **AI governance pack** | Standard answers: data handling and residency, model use, human control, audit trail, security. BFSI version first | SC (with Creatio security/legal input) |
| **Agent test-set template** | 10–20 inputs per agent incl. edge and refusal cases; used at Gate B and handed to the partner | SC |

## 10. AI layer: standard workflows

| # | Workflow | Input | Output | Used by |
|---|---|---|---|---|
| W1 | **Pre-call** ([v0.4](workflows/W1-Pre-Call.md)) | BDR call transcript (or a short AE/SC handoff) | Research, hypotheses, journey picture, pre-filled card, one slide | SC / AE |
| FM | **First-meeting prep** ([v0.2](workflows/FM-First-Meeting-Prep.md)) · **current default** | BDR or partner call transcript | Playback + hypothesis slides, light-config brief, meeting plan | SC |
| W2 | **Post-call** ([v0.2](workflows/W2-Post-Call.md)) | Transcript or card notes | SC summary, Brief (evidence only), qualification score, one-pager, gaps list; length follows the evidence | SC / AE |
| W3 | **Design** ([v0.2](workflows/W3-Demo-Design.md)) | W2 outputs + one-pager replies | Demo Design Pack: summary, value map, storyline, build plan, demo script for `creatio-demo-runbook`, decision values, validation moments, close sheet, Gate A | SC |
| W4 | **Build** | Runbook | Stand, readiness, click path, video (existing demo toolkit) | SC |
| W5 | **Close** ([v0.2](workflows/W5-Close.md)) | Brief (updated after the demo) + demo outcome notes + build log | Proposal + Partner Pack + Gate C check | SC |

**Interfaces:** AEs and BDRs won't use Claude Code. W1 and W2 run in a **shared Claude project** (templates and
instructions loaded; paste in, get out). SCs use Claude Code for W3–W5.

## 11. Roles

| Role | Owns |
|---|---|
| **BDR** | Cold call, forked card, handoff form, booking the joint discovery |
| **AE** | Running W1 once the discovery is booked (or the SC does), running the meetings, qualification questions, sending the one-pager, the mutual action plan |
| **SC** | Checking every W1 pack before the call, discovery questions, go/no-go, design and demo, curating AI outputs, **one pack each** (Core/General, BFSI, Manufacturing) |
| **AI (Claude)** | Research, hypotheses, Brief, scoring, all drafts, build and checks |
| **SE** (escalation only) | Custom UI (Angular), AI Studio voice/telephony, real integration prototypes, new reusable modules. The request is the runbook scene + Brief extract; no briefing call |

**Cadence:** weekly deal review on scorecards (30 min) · monthly asset harvest into the packs.

## 12. Frameworks borrowed (verified 3 Nov 2026: [research](research/proposal-handover-frameworks-2026-11-03.md))

| Framework | Owner / origin | Correct terms | Used for |
|---|---|---|---|
| **Command of the Message** | Force Management | Before Scenario · Negative Consequences · Positive Business Outcomes (PBOs) · Required Capabilities · Metrics · Differentiators · Proof Points. The **Mantra** is a spoken recap that grows over the deal, not a document section. ("After scenario" is secondary-source wording; avoid it) | Brief and Proposal structure; "What we heard" = their practice of restating at each meeting |
| **MEDDPICC** | PTC, 1996 (Dick Dunkel, Jack Napoli, under John McMahon); PC added later | Metrics · Economic buyer · Decision criteria · Decision process · Paper process · **Implicate** the pain · Champion (needs power, influence, credibility) · Competition (incl. **do nothing** and **build in-house**) | Qualification scorecard. "Why now" and "commitments" are **our additions**, labelled as such |
| **Great Demo!** | Peter Cohan (Second Derivative) | Do the Last Thing First · Situation Slide: **Critical Business Issue** (a goal at risk), **Delta** (value), **Critical Date** · per section: Situation Slide → Illustration → Do It → Peel Back the Layers → Summarise | Demo structure; CBI / Delta / Critical Date captured in the Brief |
| **Tell-Show-Tell** | Bob Riefstahl, Demo2Win! (not Great Demo!) | Tell → Show → Tell | Scene wrap only *after* discovery (Cohan warns it becomes a feature tour without it) |
| **Shipley 4-box executive summary** | Shipley Associates | Hot buttons in their priority, credited to them → each as a heading: benefit → solution → proof → one next step | Proposal executive summary and body |
| **Forrester TEI** | Forrester | Benefits · Costs (new spend only) · Flexibility · Risk; risk-adjusted and unadjusted; 3 years; reader uses own numbers | Proposal value case |
| **Mutual action plan** | General practice | Steps, owners, dates to decision and go-live | Demo close and Proposal |
| **Conceptual solution outline** (not "solution blueprint") | SI practice (Microsoft Solution Blueprint Review, SAP Activate fit-to-standard) | The implementer builds the blueprint after its own workshops | Partner Handover Pack: presales gives the outline and open questions |

## 13. Rollout

| Phase | Status | What |
|---|---|---|
| **1 Design** (process, templates, workflows, packs, catalogue) | ✔ Drafted 2–3 Nov 2026; tested on 1 mock deal + 1 real-bank pre-call | Everything in §8 (W3 added 3 Nov) |
| **2 Sign-off** | **Now** | Renzo + Sales Director approve the decisions in the sign-off pack |
| **3 Pilot readiness** (1–2 weeks) | After sign-off | Shared Claude project with W1/W2 loaded · 1-hour AE/SC briefing on the pilot guide · pack owners named · baseline metrics from the last 10 deals · governance asks sent |
| **4 Pilot** (6 weeks) | | 3 SCs, the next 4–6 new opportunities across industries. Build only what each demo needs, starting with harvested modules (M4 case/SLA, M6 live-change kit) |
| **5 Review → v1.0** | Week 6 | Metrics vs baseline; template and pack fixes; decide W3, the master sandbox build and wider rollout |

**Pilot metrics** (vs a baseline from recent deals): discovery → demo offered (days) · customer meetings before the
Proposal · % of discoveries that got a pre-call pack · go/no-go distribution · % demos showing the core set · SC hours
per deal · SE hours used · demo → next-stage conversion · partner feedback on the Handover Pack · W1/W2 token use.

## 14. Open questions

| # | Question | Owner | Blocks |
|---|---|---|---|
| 1 | Recording: consent convention and tool (Teams, Gong, other)? | Renzo / Sales Director | W2 quality |
| 2 | Does the BDR book the joint discovery directly, with no separate AE handoff step? | Sales Director | Stage 0 |
| 3 | Which note tool do AEs use (OneNote, Word, Creatio)? | AEs | Card format |
| 4 | Where do deal artefacts live: SharePoint/Teams now, Creatio later? | Renzo | Pilot setup |
| 5 | Is the AI ideas workshop worth SC time, and for which accounts? | Renzo | Track A |
| 6 | Official AI governance answers (9 internal asks) | Creatio security / AI Studio product | BFSI AI deals |
| 7 | Official price book (plans, products, AI credit packages) | Sales ops | Every value case |
| 8 | Referenceable APAC bank / manufacturer customers | Creatio APAC marketing | Proof points |
| 9 | A real discovery recording to test W2 | Renzo | Validation |
| 10 | W1 token use on the shared Claude project now that AEs run it | Pilot | Scale |
| 11 | **Experiment E1: "first take" pre-read.** Should W1 offer an optional pre-read for meetings that slip or are at risk? It's the hypothesis slide + journey (Outputs 8 + 4) as one page, sent before discovery with "which is most true?" and an optional test of their enquiry response. First run: SAHE (`deals/southern-academy-of-higher-education/04–05`), pre-read only (test enquiry dropped). **Pass if:** he replies or picks one, the call happens, and Pick/Break go deeper than usual. **Fail if:** he answers by email and the call slips or gets shallower. Decide after 2–3 deals; not for every deal | Renzo | W1 Output (optional) |

## 15. Changes

### After v0.5: live-deal updates
- **19 Nov 2026: build rules v0.7** (plugin 0.35.0; Renzo, from Creatio's internal Confluence). `BUILD-RULES-v0.6` renamed to `-v0.7`, new §6 configuration quality: shared-stand change discipline, new data bindings for new data, source-only C#, handler `next` + `scopes`, bulk processes in the background, delegated credentials for demo AI agents, Designer dependency gap, one business rule per field, CSP, process prompts, data model, metadata and NCD naming, two prompts per custom component; load R&D's instructions MCP on VPN. Toolkit notes rule 9. Log §4 item 153.
- **18 Nov 2026: build rules v0.6** (plugin 0.32.6; Renzo, after the BPD Bali map build). `BUILD-RULES-v0.5` renamed to `-v0.6`, new §5: custom components start on the UI kit (vendored kit-data / kit-write / tokens); by build end the deal folder holds component source, README, page bodies, seed scripts and a handover note (`approval_pack.py report` lists gaps); headless checks when the browser pane is signed out; clio traps; web map = custom component (register L-001). Toolkit notes block rules 5–8. Log §4 item 144.
- **18 Nov 2026: channels and integrations playbook v0.1** (Renzo: our weak spots are showing integrations, chat channels, social comments and WhatsApp in campaigns). New `apac-sc-motion/knowledge/CHANNELS-AND-INTEGRATIONS-PLAYBOOK-v0.1.md` from Academy 8.3/v10 + Marketplace. Key facts: no WhatsApp/SMS/process element in the campaign canvas (route B = Modify data → process → Send chat message); comments and Google reviews not native (simulated Meta webhook → case); v10 moves channels to Customer Communication Hub. Not yet rehearsed on a stand. Log §4 item 143.
- **18 Nov 2026: every Word document in the Creatio look** (plugin 0.32.3; Renzo). New `apac-sc-motion/standards/DOC-STANDARD-v0.1.md` and doc kit (`standards/doc-kit/creatio_doc.py`): logo, orange cover band, Montserrat headings, navy tables, estimates shaded, status in the footer, PDF through Word, every page checked. Applies to all Word output, customer and internal. `sc-workshop` playback uses it now; `sc-sizing` in 0.33.0. From the Agrobank sizing.
- **18 Nov 2026: learning loop pilot** (plugin 0.32.0). Renzo: Claude makes us faster but we must not become blindly dependent. New `standards/LEARNING-LOOP-v0.1.md`, skill `sc-ready` (readiness check: quiz first, crib after, verdict), FM v0.7 + `sc-demo-plan` step 1b "call it first" (quotes first for SCs who weren't on the call), CHAT-FORMAT v0.2 (💡 Learn, 7th mark), chat stage `Ready`, desk brief suggests `sc-ready` the day before a meeting. Behind `"pilot"` in `~/.apac-sc-motion.json`: Renzo only, review 2 Dec. Log §4 item 133.
- **18 Nov 2026: on-prem hardware sizing** (plugin 0.30.0, published). New skill `sc-sizing` + `knowledge/SIZING-RULES-v0.1.json`: Creatio calculator as the base, adjusted only by sourced rules from Academy and Sergey Sinienok's guidance (Jan–Oct 2026 emails); every output a recommendation pending infra review. Log §4 item 130.
- **18 Nov 2026: deck standard v0.6, eight visual slide types** (plugin 0.28.0, not published). `statement`, `landscape`, `compare`, `band`, `milestones`, `hero_screen`, `photo_cards`, `quote`, in the creatio.com style. `DECK-STANDARD-v0.5` renamed to `-v0.6` and references updated. Test deck `apac-sc-motion/tests/deck/visual-types/`. Log §4 item 128.
- **17 Nov 2026: no "SC check required" warning lines** (plugin 0.27.0; Renzo). Claude adds the line to nothing it generates (docs, emails, decks and notes, HTML, scripts); CLAUDE.md, W0, W2, the AE project kit, `DECK-STANDARD-v0.5` and every plugin skill and script updated, and the line stripped from existing deal files, test fixtures and the Slide-library. The SC still reviews everything before a customer sees it. Log §4 item 126.
- **17 Nov 2026: customer self-install guides** (plugin 0.26.0). `sc-customer-academy` F0 links to new Windows and Mac install guides (`modules/F0-install-windows.md`, `F0-install-mac.md`): one prompt in Claude Code installs .NET, clio and Creatio's public toolkit; the customer connects their sandbox with their own password in their own terminal. Replaces the Academy setup wizard (404). Not yet tested on a clean machine. Log §4 item 125.
- **16 Nov 2026: existing customers, confidential terms, who owns what** (plugin 0.24.0, published). New
  `apac-sc-motion/standards/CONFIDENTIAL-TERMS-v0.1.md` (+ `confidential.py`: generic labels in everything shared,
  scan before writing); `sc-guide` mode D, the existing-customer path, with `knowledge/TEMPLATE-As-Built-v0.1.md`;
  `deal_dates.py event`; roadmap `owner` line (DECK-STANDARD v0.5 row). From EDB. Log §4 item 115.
- **16 Nov 2026: build on top of master stands** (plugin 0.23.0). `DEMO-BAR-v0.3` §6c and `BUILD-RULES-v0.5`: complementary
  use cases are built on top of a neutral master stand (register `apac-sc-motion/library/stands.json`), one customer
  layer at a time, so masters grow into one coherent solution. Log §4 item 109.
- **16 Nov 2026: Delivery Assurance knowledge (internal), v0.2.** `apac-sc-motion/knowledge/DELIVERY-ASSURANCE-v0.2.md`
  from the Jan 2026 deck (owner Alex Klochkov): framework, packages, partner-risk signals → package, where it shows up
  with customers, can say / don't say. **No prices in any output**; indicative prices to the SC in chat only, flagged.
  Hooks in `sc-first-meeting`, `sc-deck`, `sc-workshop`, `sc-meeting-review`, `sc-rfp`, W5 rule 10. Log §4 items 108, 110.
- **16 Nov 2026: DECK-STANDARD v0.5** (plugin 0.21.0). From the Navalo deck as presented: no caps label above titles, agenda as numbered cards with a solid goal panel, no minutes or owners on the agenda or next-steps slides (in the notes instead). Owners off the slide is a 2-deal pattern (Suntory, Navalo). Log §4 item 98.
- **12 Nov 2026: token efficiency, no quality change (plugin v0.16.1).** `CONTEXT-HANDOVER.md` cut from ~27k to ~3k
  tokens; the history moved verbatim to `CONTEXT-HANDOVER-LOG.md`, read on demand. This process doc is read only when
  a task changes the motion or needs §8. Deck checks: every slide on the first build, then only changed slides unless
  the change can touch them all.
- **12 Nov 2026: Claude tells each SC about updates (plugin v0.16.0).** A plugin startup hook
  (`hooks/whats_new.py`) compares the installed version with the one published on SharePoint, gives the update command
  when they're behind, and shows the changelog once after an update (tracked as `seen_version` in
  `~/.apac-sc-motion.json`). The Monday release message stays as a backup until it's proven for Willy and Ferdhi.
- **12 Nov 2026: release discipline (plugin v0.15.2).** Every plugin release needs a `CHANGELOG.md` entry
  (`publish.ps1` refuses without one) and is tagged `v<version>` in git. Each Monday at 8 am a Claude scheduled task
  on Renzo's PC (`sc-release-message`) drafts a Teams-ready message from last week's entries into SharePoint
  `Plugin/release-messages/<date>.md`; Renzo posts it. Draft only, never sent automatically.
- **14 Nov 2026: SC desk and privacy per SC (plugin 0.20.0, unpublished).** New skill `sc-desk`: commitments
  ledger per deal, stall checks, daily brief (8 am scheduled task per SC), Friday desk view, load check; a task desk,
  not a CRM. `standards/FEEDBACK-LOOP-v0.2.md`: feedback about the skills and Claude stays global; the SC's performance
  (coaching, meeting self-ratings, training results) stays on their own PC, shared only by their choice ("for you,
  not about you"); no per-person scores anywhere; desk briefs private; Friday team page totals only.
  Source: Renzo, 14 Nov (log §4 items 101, 102, 105).
- **13 Nov 2026: plugin 0.18.0 published.** FM v0.6 + DECK-STANDARD v0.4: every demo deck opens with an agenda whose
  "Today's goal" is the closing question, word for word; "not yet" pins down the next step; the builder checks it.
  New `standards/FEEDBACK-LOOP-v0.1.md` (feedback as you go in every skill, patterns not people on Fridays), new
  skill `sc-lessons` with shared registers (product limits, discovery questions; live straight away when they only
  make us more careful), requirements library seed + meeting card ("tell us what we need"), "where we win" strip on
  build plans, richer SC click path (teaches the demo, logins, two-user screenshots, meeting-card tab), our-idea steps
  stay without an answer. Source: Renzo, team walkthrough 13 Nov (log §4 items 70-79).
- **13 Nov 2026: FM v0.5, demo depth first (plugin 0.17.0).** `sc-first-meeting` and `sc-guide` ask the
  SC whether the customer expects an introduction to Creatio or a detailed demo on their pains. Introduction = light
  config as before. Detailed = best-practice pains from the pack (tag I), a success-criteria email for the customer to
  rank them, and a Full demo plan through `sc-demo-plan`. Source: Renzo (bookings sometimes set a higher bar than an
  intro, and customers expect us to know best practice).
- **12 Nov 2026: deal folders carry the creator's initials (plugin v0.15.1).** New deal folders are named
  `<account>-<sc>` (`rh` Renzo, `wn` Willy, `fa` Ferdhi), initials stored once in `~/.apac-sc-motion.json` by
  `sc-setup`. Deal folder only, one folder per account (reuse any existing suffix), never renamed on handover; folders
  made before today keep their names. Rule lives in `sc-setup`; applied in `sc-first-meeting`, `sc-guide`, `sc-rfp`,
  `sc-workshop` and W0.
- **12 Nov 2026: build plan before any build (plugin v0.15.0).** The SC approves `NN-build-plan.html` (wireframe per
  demo step, the customer's verified quote or a sourced "our idea" blind spot, minutes, differentiator, reuse, their
  criteria against our demo, hours) before any stand write. Source: Renzo stopped the Navalo build to add it.
- **12 Nov 2026: FM v0.4 (plugin v0.14.1).** `sc-first-meeting` asks for the company website (required, but research
  continues if it's missing) and anything the customer has sent; customer documents that arrive later outrank the call
  and trigger a rework of the hypothesis. Source: Navalo deal (Renzo's suggestion; the overview email reshaped the deck).
- **11 Nov 2026: first weekly lessons digest (W46), all three proposals applied (plugin v0.7.0).** Demo bar v0.2: Full and
  Proof demos on a clean stand; rehearse on the presenting device, network and login. Core pack v0.2 (plugin copy):
  J4 field visit, J5 project selling. The plugin's `knowledge/` packs are now ahead of `packs/` in this workspace.
- **11 Nov 2026: Phase 0 of the team rollout.** Plugin repo `apac-sc-motion` (v0.1.0) created: `sc-setup`,
  `sc-first-meeting` (FM v0.3), `sc-deck` + `DECK-STANDARD-v0.3`. FM now produces the whole presented deck (cover,
  current understanding, hypothesis, one component slide per part with Business Studio first and AI second, summary,
  next steps), not 3 slides, because every presented deck grew to 10–23 slides. Light-config brief split into Business
  Studio then AI. Deals moved to the SharePoint site (`deals/` is a link). Lessons: `apac-sc-motion/lessons/2026-11-11-presented-decks.md`.
- **5 Nov 2026: Experiment E1 logged (§14 #11), no process change yet.** SAHE's first meeting slipped, so we're sending
  a "first take" pre-read (hypotheses + journey as one page, plus an offer to test their enquiry response) before
  discovery. In the room it feeds Pick, Break and Size; corrected, it becomes the "What we heard" one-pager (§5.4) and
  the demo's opening journey. It goes into W1 as an optional output only if it passes on 2–3 deals.
- **5 Nov 2026: W2 v0.2.** The first real run (Suntory intro call) produced ~250 lines from ~10 minutes of discovery,
  with Assumed items reading like findings. W2 now: puts a ≤15-line SC summary first; names the call type (Discovery /
  Intro / Partial) and runs a Short mode for thin calls; drops empty rows and sections; keeps Assumed items out of the
  Brief and out of the one-pager's findings (quick checks only); writes "from → to" only with their number; lists our
  side's unverified claims; caps length. Demo scene suggestions moved to W3 (step 3 and rule 4 updated). §8 and §10 now
  show W1 v0.3 and W2 v0.2. Blind-tested on Suntory (Amber/Amber, 975 words vs ~3,300 in v0.1) and PRC (Red), then
  tightened: claims get their own table outside the word cap; Short cap 800 words; commitments, promises and positioning
  corrections can't be cut; tie-breaks for Amber vs Red and for a "named task"; Red email carries promised items and
  respects the customer's reconnect timing ([findings](tests/w2-v0.2-TEST-FINDINGS.md)).

### v0.5 (3 Nov 2026): sign-off candidate
- 9 Nov: **FM v0.2**: third slide, "Your solution at a glance" (numbered parts, shown / not yet shown, no question on it), and a spoken closing question: "could this fix [their top pain]?", then "is it worth working out what it would take and cost, and who needs to be part of that?". "Want to know more" brings up the summary slide.
- 9 Nov: **BDR call sheet v0.4**, after reading it against the Suntory intro call: question 6 (AI) asked of everyone, so a specific job named there adds the AI track; question 4 drops "this year"; question 5 asks who runs it and who signs off (matches the booking rule's "who owns it"); question 2 asks what has to stay; role asked at the start; sizing follow-up (FM needs a KPI); "can it do X?" captures the idea; never name other customers or quote their numbers; AEs use the same six before any slides. FM and W1 updated.
- 6 Nov: **simplified flow adopted** (decision 16, §4.0) with the team: 6 BDR questions → FM workflow (playback + hypothesis slides, light config) → first SC meeting. New: `workflows/FM-First-Meeting-Prep.md`, `templates/_build/build_first_meeting_slides.py`.
- 5 Nov (later): **BDR call sheet v0.3**: one page; the recorded call's transcript replaces the handoff form (W1 step 0 extracts it); pick-specific follow-ups and track add-ons removed.
- 5 Nov: **BDR / AE call card v0.2**: three-pain cold opener (the pick sets the track), raised-hand opener, five core questions for every call, No-code as a third track, booking rule = pain in their words + owner attending + timeframe. W1 inputs updated to match.
- Added after the pack: **demo video library plan + Red follow-up email** (W2 drafts it for Red deals); **M6 live-change kit** design (validation moments answered by rule values or rows; process changes are set pieces only; D1 proof moment corrected to measured times); **W3 demo design v0.2** (blind-tested on the Harbourline mock; Gate A now counts decision values only, accepts module IDs until the pattern catalogue exists); the shared Claude project setup kit and the discovery slides template (§8); W1 Outputs 4 and 8 point to the slides.
- Consolidated: documents table reflects what exists and how it was tested; packs and catalogue sections point to their files;
  rollout restated as design ✔ → sign-off → pilot readiness → pilot → v1.0; open questions get owners.
- Proposal + Partner Pack templates and W5 (v0.2) added; frameworks verified and corrected (§12).
- AI Studio bundled with Business Studio (decision 14 revised); manufacturing D5 rule; core set approved.
- New: [SIGN-OFF-PACK-v0.5.md](SIGN-OFF-PACK-v0.5.md), [PILOT-GUIDE.md](PILOT-GUIDE.md).

### v0.4 (3 Nov 2026), after mock call 01 (`tests/mock-01-harbourline/`)
- **Tiered go/no-go:** build depth follows the score (Green = full L3 · Amber = 1-day L2 reference demo · Red =
  recorded video + questions). Green needs the economic buyer **named**. An unknown decision process must be asked.
- P+A deals get two results; an Amber A means the AI scene runs on simulated data and no pilot is proposed.
- Hypothesis slide = 4 owned by the attendees + 1 expansion; every pack hypothesis carries its usual owner.
- The "show us your screen" commitment is replaced by "send us one thing", for all industries.
- The card captures risks (a previous failed project) and words to avoid; the A-only questions are must-fill for Track A.
- The demo target is now "offered within 5 working days".
- AI governance pack lite moves to Phase 1. In-country LLM hosting confirmed by Renzo (AU, ID); routing, fallback models and AI Studio coverage still to confirm.

### v0.3 (3 Nov 2026)
- Two tracks in one motion: **P: Platform (CRM / no-code)**, **A: AI Studio**, and **P+A**, with a stage-by-stage
  table (§4.1). AI Studio is sold separately from CRM, standalone if necessary.
- Track A: a stricter go/no-go (task, owner, data, no policy blocker), an agent test set at Gate B, a measured pilot in the
  Proposal, an agent specification in the Partner Pack, AI value maths.
- Every Platform demo includes one AI scene.
- New assets: AI use-case library, agent pattern catalogue, AI master sandbox, AI governance pack, agent test-set template (§9.4).
- The Sales Director sponsors the go/no-go gate.

### v0.2 (3 Nov 2026), changes from v0.1

- Hypothesis-led discovery; one 30-min call with ≤20 min discovery; the Hello Deck replaced by one hypothesis slide.
- New Stage 0 (BDR) with a forked CRM / AI Studio card; opportunity-type variants across the motion.
- New go/no-go gate with AI-scored qualification; the "What we heard" one-pager replaces a second discovery call.
- Configuration levels L1–L4 (target L2–L3); validation moments and a live change in the demo; mutual action plan.
- Evidence tags (Confirmed / Inferred / Assumed) carried through every document.
- Core + Industry Packs for BFSI, Manufacturing and General industry; SC pack ownership; approved build-pattern catalogue.
- AI layer defined as 5 standard workflows; a shared Claude project for AEs and BDRs.
- Rollout re-phased (front end first).
