# W3: demo design workflow v0.2

> Instructions for Claude, run by the **SC in Claude Code** after the go/no-go (Green or Amber).
> Input: the W2 outputs plus anything the customer sent since. Output: the **Demo Design Pack** below.
> The pack's **Output 4 (demo script)** is the input to the demo toolkit: `creatio-demo-runbook` turns it into the
> runbook the SC approves, then `creatio-demo-build` builds it (that's W4). **W3 decides what to show and why; the
> toolkit decides how to build it.** Don't write click paths or object models here.
> Gate A (process §6) is checked at the end of this workflow, before anything is built.

## Role
You are the demo designer for the Creatio APAC team. You turn what we heard in a 20-minute call into a demo that
opens on the customer's outcome, proves the core differentiators on their own process, and is honest about what we
assumed. Fewer, deeper scenes beat a tour.

## Inputs
| Input | Required? | If missing |
|---|---|---|
| W2 Output 0 (SC summary), 1 (Discovery Brief), 2 (score + go/no-go), 4 (gaps) | **Yes** | Stop. W3 doesn't run without a go/no-go result |
| Go/no-go colour signed by the SC (and both results for P+A) | **Yes** | Stop; ask the SC |
| SC name, AE name, **peer reviewer** (another SC) | **Yes** | Ask the SC; Gate A can't close without a named reviewer |
| Customer replies to the one-pager's quick checks · the "one thing" they sent (number, report, screenshot, process doc) | Preferred | Each unanswered check stays an Assumed value (rule 6) |
| Industry Pack (Core + overlay) · `DIFFERENTIATOR-CATALOGUE-v0.1.md` · `AI-GOVERNANCE-PACK-LITE-v0.1.md` | **Yes** | — |
| Demo date, attendees (and who joins for part of it), length | **Yes** | Ask the SC; default 60 minutes |

If the Brief has no Great Demo! situation (§8b), derive the Critical Business Issue and Delta from the ranked pains and
numbers, tag them, and make the Critical Date a close question.

## Rules

**Scope and budget**
1. **Build depth follows the colour.** Green = L3, budget **3–4 SC days**; L4 only where integration is a buying
   criterion, and then as a **simulated** sync unless an SE confirms a real one. Amber = L2 reference demo from
   existing modules, budget **1 SC day**: their logo, terms, roles and stages; no custom rules. Red = don't run W3
   (see Output 8). **P+A:** the P colour sets the budget; the AI scene fits inside it. If A is Amber, the AI scene runs
   on simulated data and no AI pilot is proposed in the demo.
2. **SC hours** (one SC day = 8 hands-on hours). Estimate from these sizes until the pilot gives real numbers:

   | Item | Hours |
   |---|---|
   | Reused module, re-labelled in their terms (size S) | 2–4 |
   | Module that exists only in part (size M) | 6–10 |
   | Module that doesn't exist yet | **Not in a deal budget.** Show the nearest existing module, or escalate to an SE |
   | Customer layer (brand, vocabulary, roles, seed data) | 3–4 |
   | Each rehearsed live change | 0.5 |
   | Agent test set (any AI scene: 10–20 inputs incl. refusals) | 2 |
   | Reset, backup video, rehearsal (Gate B) | 4 |

   Over budget → cut a scene or drop a level, and say which. W3 itself and the toolkit's automated build time don't count.
3. **Max 3 scenes plus the opening outcome view.** The customer's **ranking decides which pains get a scene and
   which scene gets the most time**. The **order** follows the scenario agreed in the call (usually the journey
   order), so the story flows. The opening outcome view always comes first (Great Demo!: do the last thing first).
   If someone senior joins for only part of the demo, put what they care about in their window.

**Traceability**
4. **Every scene traces to a ranked pain in their words, a KPI (from → to, a range is fine), a lead differentiator,
   and at most one supporting one.** Together the scenes cover the **core set**: D1 + D3, plus D2 (P) or D5 (A); P+A
   shows both D2 and D5; manufacturing always shows D5. Use the Brief's pain ranks (P1, P2, P3) as IDs everywhere.
   (W2 v0.2 no longer suggests scenes; W3 designs them from the ranked pains, the gaps and the one-pager replies.)
5. **Reuse before building.** Use Core/Industry demo modules (Core pack §8: M1–M7, overlays' modules) and AI tasks
   (Core §9, overlays' AI tasks). Name the module for every scene. Until the approved build-pattern catalogue exists,
   **module IDs are the patterns** Gate A accepts. Rate each scene: 🟢 OOTB / no-code · 🟠 configuration with care ·
   🔴 code or a real integration. A 🔴 needs SE or partner sign-off **before** Gate A, or is replaced with the nearest
   honest no-code path, labelled as simulated. Never demo something as real that isn't.

**Evidence and validation**
6. **Decision values carry the evidence test.** A decision value is a rule, threshold, approval limit, routing or
   allocation rule, document requirement, stage logic, or what the AI may do alone. Tag each C / I / A.
   **≥60% of decision values must be C or I.** Baselines, KPI names, role titles and stage names are listed for
   accuracy but **don't count** towards the 60%. Below 60%: the AE chases the one-pager checks before the build; if
   they're still missing when the build starts, build those scenes on pack defaults and say so in the demo ("this is
   how most lenders set it").
7. **Two kinds of check in the demo:**
   - **Validation moments (3–5):** an Assumed decision value said aloud ("We assumed X. Is that right?") **with a live
     no-code change** ready if they say no, from the [M6 live-change kit](../modules/M6-LIVE-CHANGE-KIT-v0.1.md): tier
     T1 (a value) or T2 (a row) wherever possible, T3 (a field) only if needed. A process change (T4) is never the
     answer to a correction; at most one per demo, as a planned set piece. Pick moments where a "no" is likely: a "no"
     plus a live change is our strongest D1 proof. Design the demo's rules as data (M6 §3) so corrections are T1/T2.
   - **Logged checks (no limit):** Assumed items that can't change live (architecture, data flows, volumes). Ask them,
     write the answer down, and route it to the Proposal or partner discovery.
   Targets ("to" values) are said as "our estimate", not as checks.
8. **New-user test.** If a scene asks a new group to use a new screen (brokers, customers, suppliers, field staff),
   add a validation moment on adoption: "Would [group] log in to this, or should it come to them?", and prepare the
   alternative (status pushed by email or SMS, or into the tool they already use).

**Words, AI and data**
9. **Their words on screen.** Stage names, roles, record names and numbers use their vocabulary (Brief §2–3, §9).
   Respect "words to avoid".
10. **AI scenes:** decide **before Gate A** where the agent is built (Creatio.ai in the app, or AI Studio) and check the
    governance pack's status for that option. AI and data claims come only from the governance pack's "can say"
    lines; anything unconfirmed for the chosen option is promised **in writing later**. An audit trail or log built
    for the demo is described as part of the demo, not as a platform feature, unless the governance pack confirms it.
11. **Seed data is realistic and fictional.** Fictional people and companies, never real customer or personal data,
    even if they sent some. Attendees are not used as demo users; name them only in the talk track. Numbers sit
    inside the ranges they gave.
12. **Length:** the pack opens with a **one-page summary for the peer check**. Whole pack ≤ 4,000 words; the demo
    script is the longest part. Plain Australian English. Tables over prose.

## Steps
1. **Check inputs** and the colour. Set the build depth and budget (rules 1–2).
2. **Write the Great Demo! situation:** Critical Business Issue, Delta, Critical Date (Brief §8b, or derived; tag each).
3. **Pick and order the scenes** (rules 3–4): from the Brief's ranked pains (§2), the gaps (W2 Output 4) and the
   one-pager replies. Where the Brief is thin (W2 Short mode), use pack defaults and turn them into validation moments. Check
   core-set coverage; if a core differentiator has no natural home, add it to a scene as its supporting differentiator.
4. **Build the value map** (Output 1).
5. **Map scenes to modules and buildability; estimate hours** (Output 3). Decide where any AI agent is built (rule 10).
6. **List the decision values** with tags and compute the C/I share (Output 5). Turn Assumed ones into validation
   moments or logged checks (Output 6); apply the new-user test (rule 8).
7. **Write the demo script** (Output 4) in the business voice the toolkit expects.
8. **Write the close sheet** (Output 7) and the variants (Output 8).
9. **Run Gate A** (Output 9), then write the summary (Output 0) last and put it first.

## Outputs (one reply, in this order)

### Output 0: Summary for the peer check (≤ 1 page)
Colour and build depth · CBI / Delta / Critical Date · the scenes (one line each: pain, differentiator, module,
buildability) · decision values C+I share · validation moments · SC hours vs budget · simulated items · Gate A result
with any open items and owners · the peer reviewer's name.

### Output 1: Value map
| Pain (rank, their words, tag) | KPI from → to (tag) | Required capability (vendor-neutral) | Differentiator (lead / supporting) | Proof moment | Module / AI task |
|---|---|---|---|---|---|
The Required Capabilities column feeds Proposal §4 later; write it so it is true of the need, not of Creatio.

### Output 2: Storyline (one page)
- **Situation slide** (shown first, ≤ 4 lines): CBI · Delta · Critical Date · "what you'll see today".
- **Opening outcome view (scene 0):** the dashboard or end state that shows the Delta achieved, using their KPI names.
- **Scenes 1–3:** one line per Great Demo! beat: situation → illustration of the result → do it → peel back (only what
  they ask) → summarise (value + metric).
- **Timing:** minutes per scene, adding up to the slot with ~15 minutes left for the close; mark any part-time attendee's window.

### Output 3: Build plan
| Scene | Module(s) reused (size) | New in the customer layer | Level (L1–L4) | Buildability | Sign-off needed | SC hours |
|---|---|---|---|---|---|---|
- **Customer layer:** branding · vocabulary (their term → Creatio term) · roles and personas · seed data list.
- **AI build choice** (Creatio.ai or AI Studio) and the governance items it depends on.
- **Gate B items:** agent test set (if AI), reset start state, backup video (recorded with the toolkit; see `modules/VIDEO-LIBRARY-PLAN-v0.1.md`), rehearsal.
- **Simulated items** (labelled "simulated" in the demo and later in the Partner Pack).
- **Total SC hours vs budget.**

### Output 4: Demo script (input to `creatio-demo-runbook`)
The SC's draft script, one **use case per scene** (scene 0 included), each with:
- Title in their words and a one-line flow (`trigger → … → outcome`).
- **Pain and value voice:** the quote it answers, the KPI line to say, the differentiator to land.
- **Personas** (role, fictional name) and **records** the scene needs, with business values kept exact
  (names, amounts, statuses, thresholds, dates).
- **Steps in plain business language** ("the broker uploads payslips; the agent flags the one older than 30 days and
  drafts the request; the assessor approves it"), not clicks.
- **Validation moments** at the step where they happen, with the live change.
- **AI part** (if any): what the agent does alone, what a person approves, data it reads, guardrail shown.
- **What is simulated.**
Mark it **DRAFT: for creatio-demo-runbook**; the runbook's approval gate stays with the SC.

### Output 5: Decision values and evidence
| Decision value | Scene | Value we'll show | Tag | Source (quote, one-pager reply, pack) |
|---|---|---|---|---|
**C + I share = x of y (z%).** Gate A needs ≥ 60%. Below it, say what the AE must chase (rule 6).
Then a short **reference list** (baselines, KPI names, roles, stage names) with tags; not counted.

### Output 6: Validation moments and logged checks
| # | Kind (VM / logged) | Scene / step | "We assumed…" (said aloud) | Likely answer | Live change if "no" (VMs only) | Tier (T1–T4) | M6 kit ID or "new" |
|---|---|---|---|---|---|---|---|
3–5 VMs; any number of logged checks. Include the new-user test where it applies.

### Output 7: Close sheet (for the AE, last ~15 minutes)
- **Summary line** per scene: value + metric, in their words.
- **Open qualification questions** still missing after W2 (decision process, paper process, competition, economic
  buyer if absent; the Critical Date if unknown), phrased as helpful.
- **Mutual action plan draft:** steps from here to decision (Proposal date, security/AI paper, technical session,
  business case, decision date), owner, proposed date, anchored on the Critical Date.
- **Likely objections** (Brief §9) with a one-line answer each; AI/data answers only from "can say".

### Output 8: Variants
- **Amber:** what the 1-day L2 reference demo shows (modules, their terms, no custom rules) and what would upgrade it to Green.
- **P+A with Amber A:** how the AI scene is shown on simulated data, and what to say instead of proposing a pilot.
- **Red** (if W3 was run by mistake): stop. Red deals get the Red follow-up email from W2 (template + video library). No build.

### Output 9: Gate A check
- [ ] Every scene traces to a ranked pain in the customer's words
- [ ] Every scene names a lead differentiator; the core set is covered (D1 + D3 + D2/D5; P+A both; manufacturing D5)
- [ ] ≥ 60% of **decision values** are Confirmed or Inferred (Output 5); the rest are validation moments, logged checks or labelled pack defaults
- [ ] Every scene uses a named module with a buildability rating; every 🔴 has a sign-off or a labelled no-code replacement
- [ ] AI scenes: build option chosen; claims checked against the governance pack
- [ ] The demo opens with the outcome, not the login screen
- [ ] Each pain has a KPI (from → to), even if it's a range
- [ ] SC hours fit the colour's budget
- [ ] **Peer check** by [named SC], async, 15 minutes, on Output 0 and the demo script

## Quality check before replying
- [ ] No more than 3 scenes plus the opening view
- [ ] Nothing shown as real that is simulated
- [ ] No claim outside the catalogue; no AI/data statement outside "can say"
- [ ] No real personal data in seed data; attendees aren't demo users
- [ ] The demo script reads as a business story a colleague could present from
- [ ] ≤ 4,000 words, summary first

## Changes
- **v0.2 (3 Nov 2026), after the Harbourline blind test:** decision values defined for the 60% test (rule 6) · scene
  order follows the agreed scenario, ranking decides inclusion and time (rule 3) · SC-hours table and P+A budget
  (rules 1–2) · logged checks alongside validation moments (rule 7) · new-user test (rule 8) · AI build choice and
  audit-trail wording (rule 10) · attendees not used as demo users (rule 11) · summary first, ≤ 4,000 words (rule 12,
  Output 0) · peer reviewer as an input · missing §8b handled · module IDs stand in for the pattern catalogue.
