# W3 blind-test output: Demo Design Pack, Harbourline Mutual Bank (FICTIONAL data) · 3 Nov 2026

> Produced by following [W3-Demo-Design.md](../../workflows/W3-Demo-Design.md) v0.1 on [02-W2-output.md](02-W2-output.md).
> Paper exercise: nothing built, no instance touched. Tags: **C** Confirmed · **I** Inferred · **A** Assumed.
> AE: Daniel · SC: Renzo (from the one-pager signature) · Peer reviewer: **not yet named** (see Output 9).

## Step 1: Inputs and colour check

| Input | Status | Note |
|---|---|---|
| W2 Output 1 Brief, 2 score + go/no-go, 4 gaps | ✔ | Brief has no §8b (Great Demo! situation); derived in Step 2 from §2, §4, §7, §8 |
| Go/no-go colour signed by the SC | ✔ | **P = 🟢 Green · A = 🟠 Amber** (W2 Output 2 result) |
| Customer replies to the one-pager checks / the "one thing" | ✘ none yet | All 4 checks are unanswered → treated as validation moments (rule input table). Megan's broker call number not received |
| Core + BFSI pack, catalogue, governance pack | ✔ | |
| Demo date / attendees / length | ✔ | Thu 13 Nov 2026, 10:00–11:00 (60 min). Megan Holt (Head of Lending Ops), Raj Iyer (Enterprise Architect), James (Head of Broker Distribution, requested), Lisa Moretti (COO, "I'll try") |

**Build depth (rule 1):** P Green → **L3** (their terms, $1.2m rule, KPI baselines) **+ simulated L4** for the LOS only, because
"sit around the LOS" is the buying condition (C [04:50–04:59]). A Amber → the AI scene runs on **simulated documents**, and
**no AI pilot is proposed** in the demo. **Budget: 3–4 SC days = 24–32 SC hours** (assuming an 8-hour SC day).

## Step 2: Great Demo! situation

| Element | Value | Tag |
|---|---|---|
| **Critical Business Issue** | Home loan time to decision is too slow to keep brokers: 8–10 days on average (some 3 weeks) while the major banks do 2–3 days for clean deals; share of the main aggregator's volume fell from ~6% to ~4.5% this year | C [08:18–08:58] |
| **Delta** | Lodgement → conditional approval under 5 days ("I'd love three"); assessors off document admin (30–40 min/file); broker share recovered | C (days, minutes) · A (share recovery size) |
| **Critical Date** | **None stated.** Working anchors: the LOS contract is up in ~14 months (≈ Jan 2028), and spring is the volume peak. To ask at the close | I (LOS date from C [04:50]) · A (as the deadline) |

---

## Output 1: Value map

| # | Pain (their words, tag) | KPI from → to (tag) | Required capability (vendor-neutral) | Differentiator | Proof moment | Module / AI task |
|---|---|---|---|---|---|---|
| 1 | "Time to decision. That's the one the board keeps asking about." [02:05] (C, rank 1) | Lodgement → conditional approval: 8–10 days → < 5 (C) | Live view of every application's elapsed time by stage, from data the lending team already captures | **D2** One platform | Scene 0: the COO view shows where the 9 days sit, built from the same files the team works in | M1 / B-M1 |
| 2 | "Half the applications come in incomplete." [02:15] · "expensive people doing admin" [04:00] (C, rank 2; Megan: "might actually be the cause of the first one" [02:53]) | Assessor minutes on documents: 30–40 → ~5–10 per file (C → A) · rounds per file: 2–3 → 1 (C → A) | Automated check of supporting documents against the application, with a drafted request for missing items that a person approves before it is sent, and a record of what was checked and approved, while the loan system stays in place | **D3** AI that acts, governed (+ **D5** fits your landscape) | Scene 1: the agent checks a file in seconds, flags a stale statement, drafts the broker request; the assessor approves; the log shows it | B-M2 + M5 (AI-B1) + B-M9 (LOS stand-in) + B-M10 |
| 1 | (rank 1, decision step) Committee wait above $1.2m (C [04:09]) · queue wait "a day or two" (C [03:33]) | Committee files: wait for a twice-weekly meeting → eligible files decided by the assessor same day (A) · queue 1–2 days → same day (A) | Business users change approval limits and allocation rules themselves, and the next application follows the new rule | **D4** Business owns the rules + **D1** Change at the speed of business | Scene 2: a validation moment turns into a live rule change; the next application routes differently | B-M2 (routing) + M6 live-change kit |
| 3 | "brokers chasing us, yes, that's real" [02:15] (C, rank 3) | Broker status calls: "hundreds a week" (C) → about half (A; number pending from Megan) | Brokers see their application's current stage and outstanding items without phoning | **D2** One platform | Scene 3: the broker's view moves as the assessor works the file, no export, no email | B-M3 |

**Core set check (rule 3):** D1 ✔ (scene 2 + every live change) · D3 ✔ (scene 1) · D2 ✔ (scenes 0, 3) · D5 ✔ (scene 1, simulated LOS feed). P+A needs D2 and D5: both present.

---

## Output 2: Storyline (one page)

**Situation slide (shown first)**
- Brokers go to whoever decides fastest: Harbourline's share is down from ~6% to ~4.5%.
- Today: 8–10 days lodgement → conditional approval. Your goal: under 5.
- Half of files arrive incomplete; your assessors spend 30–40 minutes each on documents.
- Today you'll see: your lending team and an AI assistant working *around* your loan system, not replacing it.

**Scene 0: opening outcome view (the last thing first)**
The COO's turnaround view: average days lodgement → conditional approval by stage, this month vs target (< 5), the share
of files incomplete on arrival, files waiting on brokers, and files waiting for committee. Illustration: the same view
with the target trajectory. "This is the view the board asks about. Let's see how the days come out."

**Scene 1: documents checked in minutes, not days** (pain 2, cause of pain 1)
| Beat | Line |
|---|---|
| Situation | A broker lodgement arrives: half arrive like this one, incomplete. Today an assessor spends 30–40 minutes on it |
| Illustration | The file after the check: documents matched, one stale statement flagged, a drafted request waiting for approval |
| Do it | The agent checks payslips, statements and ID against the application; flags the statement that's too old and the missing one; marks one item "not sure, needs a person"; drafts the broker request; the assessor edits a line and approves; the request goes; the log shows what the agent did and who approved |
| Peel back | Only if asked: where the documents came from (simulated LOS feed, labelled), what the agent is not allowed to do (no credit decisions), where the AI runs (close sheet) |
| Summarise | "30–40 minutes on documents down to around 5–10, and one round with the broker instead of two or three. No credit decision by AI; your assessor approves every request." |

**Scene 2: your rules, changed by your people** (pain 1, decision step)
| Beat | Line |
|---|---|
| Situation | Files above $1.2m wait for the twice-weekly committee; files wait a day or two in the queue |
| Illustration | Two files routed: $1.15m to the assessor, $1.35m to committee |
| Do it | Show the DLA and allocation rules as business settings. Validation moments: "Is $1.2m the same for all home loan types?" and "We assumed oldest complete file first. Is that right?" On a "no", Megan's team's answer is entered live and the next application routes the new way |
| Peel back | Who can change which rule (roles), and the change history |
| Summarise | "Your lending team changes a limit or a queue rule in minutes, without a project, and every file follows it from that moment." |

**Scene 3: brokers know where their deal is** (pain 3)
| Beat | Line |
|---|---|
| Situation | Brokers hear by email at conditional approval and phone in between: "hundreds a week" |
| Illustration | The broker's view of the same file, showing its stage and outstanding items |
| Do it | The assessor moves the scene-1 file on; the broker's view updates; the outstanding-items list matches the approved request; the COO view from scene 0 counts it |
| Peel back | Which broker platform it would connect to (not shown; generic broker portal) |
| Summarise | "Brokers see the stage and what's outstanding without calling; fewer status calls for your lending support team." |

**Timing (60 min)**
| Segment | Min | Clock |
|---|---|---|
| Intros + situation slide | 3 | 10:00–10:03 |
| Scene 0 COO view | 5 | 10:03–10:08 |
| Scene 1 document check (hero) | 16 | 10:08–10:24 (Lisa checkpoint at ~10:18: one-line value summary if she must leave at 20 min) |
| Scene 2 rules live | 10 | 10:24–10:34 |
| Scene 3 broker status | 7 | 10:34–10:41 |
| Buffer for peel-back / live changes | 4 | 10:41–10:45 |
| Close (AE) | 15 | 10:45–11:00 |

---

## Output 3: Build plan

| Scene | Module(s) reused | New in the customer layer | Config level | Buildability | Sign-off needed | SC hours |
|---|---|---|---|---|---|---|
| 0 COO view | M1 / B-M1 (partly exists: Pertamina, SJOG dashboards) | Their KPI names and stages; 6 months of seeded aggregate history inside their ranges | L3 | 🟢 OOTB dashboard | — | 3 |
| 1 Document check | B-M2 (**does not exist yet**, M), M5 / AI-B1 (partly), B-M9 LOS stand-in (partly, Scentia sync), B-M10 AI evidence view (**does not exist**, S) | Document checklist + recency rules as data; drafted-request template in their voice; confirm-then-act step; 3 fictional files with documents | L3 + simulated L4 | 🟠 config with care. **Document reading:** 🔴 if the agent must read real PDF content and that isn't OOTB → fallback: pre-extracted document fields, labelled "document reading simulated" | **SE:** confirm the agent can read the document files on the platform we demo, or approve the fallback | 10 |
| 2 Rules live | B-M2 routing + M6 live-change kit (Scentia `labPackRule`, rules as data) | DLA table ($1.2m, one row), allocation rule (oldest complete first), 2 extra files ($1.15m, $1.35m) | L3 | 🟢 rules as data | — | 4 |
| 3 Broker status | B-M3 (partly: Scentia portals, GOC) | Broker portal user, stage labels in their words, outstanding-items list | L3 | 🟠 portal page + external user | — | 4 |
| All | — | Customer layer below | — | — | — | 3 |
| All | M6 | Rehearse 4 live changes (Output 6) | — | — | — | 2 |
| 1 | — | Agent test set (process §4.1 Gate B, Track A): 10–20 inputs incl. "should refuse" (credit decision request) and "not sure" cases | — | — | — | 2 |
| All | — | Reset script + backup video (Gate B) | — | — | — | 2 |
| **Total** | | | | | | **30 h** vs budget 24–32 h ✔ |

**If over budget:** drop scene 3 to a static portal page (no live update), saving ~2 h. Not needed at 30 h.

**Customer layer**
- **Branding:** Harbourline Mutual Bank name and logo (fictional; placeholder logo).
- **Vocabulary (their term → Creatio term):** lodgement → application/record · Queue → stage · Document check → stage · assessor → user role · DLA → approval limit rule · credit committee → approval group · conditional approval → stage/outcome · broker request / outstanding items → request activity / checklist · LOS → external system (stand-in) · member → contact · *lending workspace and AI assistant* → (product name; **never "CRM"**).
- **Roles and personas:** COO (turnaround view) · Head of Lending Operations (rule owner) · Credit assessor · Credit committee (group) · Broker (portal user) · Head of Broker Distribution (broker view owner). Personas on screen use role titles and fictional staff names; attendees' names are not used as users.
- **Seed data:** 6 months of aggregate history (~900 files/month, ~70% broker / ~30% branch, ~50% incomplete on arrival, average 9 days); 3 live files: **Whitford** $780,000 (hero, stale statement, one missing payslip), **Okafor** $1,150,000 (under DLA), **Lindqvist** $1,350,000 (above DLA); broker **Tom Becker, Becker Home Finance** (fictional); fictional payslips, statements and ID images. No real or customer data.

**Simulated items (labelled "simulated" on screen and later in the Partner Pack)**
1. LOS document store and lodgement feed (B-M9 stand-in).
2. The broker lodgement platform connection (generic broker portal; platform unknown).
3. Document reading, **if** the SE fallback is used.
4. Dashboard history (seeded, illustrative; the stage split of the 9 days is our assumption).
5. All documents and applicants (fictional).

**Reset start state:** Whitford file in *Document check*, agent not yet run, no request drafted · Okafor and Lindqvist in *Queue* · DLA table = one row, $1.2m, all home loans · allocation rule = oldest complete first · checklist without self-employed items · payslip recency 30 days, statements 3 months · broker view of Whitford at *Document check* · COO view showing 9.0 days average. Backup video: full run of scenes 0–3 including one live change.

---

## Output 4: Demo script (DRAFT: for creatio-demo-runbook)

> **DRAFT: for creatio-demo-runbook.** The runbook's approval gate stays with the SC. Business language only; the toolkit decides how to build.

### Use case 0: "Where the 8–10 days go"
- **Flow:** COO opens the turnaround view → sees days by stage against the < 5-day goal → sees most days sit in document check and waiting on brokers → outcome: knows where to act.
- **Pain and value voice:** "Time to decision. That's the one the board keeps asking about." KPI line: "9 days today on average; your goal is under 5." Differentiator: D2 (the view is built from the same files the team works in).
- **Personas:** COO (Lisa's role); Head of Lending Operations.
- **Records / values:** average lodgement → conditional approval **9.0 days** (target line **5**, stretch **3**); stage split Queue 1.5 · Document check incl. waiting on broker 4.5 · Serviceability 1.0 · Credit decision 1.5 · Conditional approval issued 0.5 days (**illustrative, A**); files this month **~900**; incomplete on arrival **~50%**; channel **70% broker / 30% branch**; files waiting for committee; broker share tile "main aggregator: 6.0% → 4.5%".
- **Steps:** The COO opens her turnaround view. She sees the average and the target. She sees most of the days sit in document check and waiting on brokers. She picks the incomplete files waiting on brokers; the Whitford file is one of them.
- **Validation moment:** (soft, no live change) "We've assumed most of the 9 days sit in document checks and waiting on brokers. Does that match what you see?"
- **AI part:** none.
- **Simulated:** history and stage split are seeded and labelled illustrative.

### Use case 1: "Documents checked in minutes, not days"
- **Flow:** broker lodgement arrives from the LOS (simulated) → agent checks the documents → flags stale and missing items → drafts the broker request → assessor approves → request sent → log recorded.
- **Pain and value voice:** "Half the applications come in incomplete." / "expensive people doing admin." KPI line: "30–40 minutes per file on documents down to around 5–10, one round with the broker instead of two or three." Differentiator: D3 (+ D5: the loan system stays where it is).
- **Personas:** Credit assessor; Broker (Tom Becker, Becker Home Finance); Head of Lending Operations (owns the checklist).
- **Records / values:** Whitford application, **$780,000**, PAYG applicants, lodged by broker; documents: 2 payslips (one dated **45 days** before lodgement), bank statements covering **2 of 3 months**, driver licence for both applicants; checklist: payslips within **30 days**, statements covering **3 months**, photo ID per applicant; one payslip with an employer name that doesn't match the application (agent marks "not sure").
- **Steps:**
  1. The Whitford lodgement lands in the assessor's queue from the loan system (labelled simulated feed).
  2. The agent checks the payslips, statements and ID against the application. In seconds it lists: ID ✔ both applicants; payslip older than 30 days; one month of statements missing; employer name differs, "not sure, needs a person".
  3. **Validation moment VM1** (here): "We assumed payslips within 30 days and 3 months of statements. Is that your rule?"
  4. **Validation moment VM2** (here): "Should self-employed applications be in the first phase?"
  5. The agent drafts the request to the broker for the newer payslip and the missing statement month.
  6. The assessor reads it, changes one sentence, and approves. The request goes to the broker by email.
  7. The assessor resolves the "not sure" item herself (trading name vs legal name).
  8. The log shows: what the agent checked, what it flagged, the draft, the assessor's edit and approval, time stamps.
  9. **Validation moment VM3** (here, to Raj): "We've shown documents coming from your loan system like this. How do they leave it today: API, export or email?"
- **AI part:** *Agent alone:* match documents to the application, check recency, list what's missing, draft the request, flag uncertainty. *Person approves:* the broker request; every credit decision. *Data read:* application fields and attached documents (simulated LOS store). *Guardrails shown:* no credit decision (if asked "should we approve?", the agent declines and says it's the assessor's call); "not sure" flag goes to a person; nothing is sent without approval.
- **Simulated:** the LOS feed and document store; document reading if the SE fallback is used; all documents fictional.

### Use case 2: "Your rules, changed by your people"
- **Flow:** two files reach the decision step → routed by the $1.2m limit → Megan's team corrects an assumption → the rule is changed live → the next file routes the new way.
- **Pain and value voice:** "Time to decision" + committee wait above $1.2m. KPI line: "Files your people can decide don't wait for Tuesday's or Thursday's committee." Differentiator: D4 + D1.
- **Personas:** Head of Lending Operations (rule owner); Credit assessor; Credit committee.
- **Records / values:** Okafor **$1,150,000** owner-occupier → assessor; Lindqvist **$1,350,000** → credit committee (meets **twice weekly**); DLA **$1,200,000**, one row, all home loans; allocation rule: oldest complete file first.
- **Steps:**
  1. Both files leave Queue; Okafor goes to the assessor, Lindqvist to committee.
  2. Show the limit and the allocation rule as settings the lending team owns.
  3. **VM4:** "Is the $1.2m limit the same for all home loan types?" If no, Megan's team's answer (e.g. a lower limit for investment loans) is entered as a new row; a new investment file at the new boundary routes to committee.
  4. **VM5:** "We assumed the queue works oldest complete file first. Is that right?" If no (e.g. settlement date or broker priority), the rule is switched; the queue reorders.
  5. The change history shows who changed what, when.
- **AI part:** none (no AI near credit decisions).
- **Simulated:** nothing; values are their rules or validated live.

### Use case 3: "Brokers know where their deal is"
- **Flow:** assessor moves the Whitford file on → broker's view updates with stage and outstanding items → COO view counts it.
- **Pain and value voice:** "brokers chasing us, yes, that's real." KPI line: "Hundreds of status calls a week; brokers see the stage instead." Differentiator: D2.
- **Personas:** Broker (Tom Becker); Head of Broker Distribution (James's role); Credit assessor.
- **Records / values:** Whitford file stages as in the journey (Lodge → Queue → Document check → Serviceability → Credit decision → Conditional approval); outstanding items = the two items from the approved request.
- **Steps:** The broker opens his view: the Whitford deal sits at Document check with two outstanding items, exactly those in the request. He uploads the newer payslip. The assessor sees it, the agent re-checks, one item remains. The broker's view updates. Back on the COO view, the file is counted in "waiting on broker".
- **Validation moment:** (soft) "Today brokers hear from you only by email at conditional approval. Is that right?" (one-pager check 3).
- **AI part:** the re-check reuses scene 1's agent; no new AI.
- **Simulated:** the connection to the brokers' own lodgement platform is not shown; the broker view is a generic broker portal.

---

## Output 5: Config values and evidence

| # | Value | Scene | Value we'll show | Tag | Source |
|---|---|---|---|---|---|
| 1 | KPI name | 0 | Days lodgement → conditional approval | C | Brief §2 [02:05] |
| 2 | Baseline | 0 | 9.0 days avg (8–10; some 3 weeks) | C | [08:18] |
| 3 | Target | 0 | < 5 days; stretch 3 | C | [08:24] |
| 4 | Major banks, clean deals | 0 | 2–3 days | C | [08:24] |
| 5 | Stage names | 0–3 | Lodge · Queue · Document check · Serviceability · Credit decision · Conditional approval | C | Brief §3 |
| 6 | Queue wait | 0 | 1–2 days | C | [03:33] |
| 7 | Volume | 0 | ~900/month, higher in spring | C | [08:32] |
| 8 | Channel mix | 0 | 70% broker / 30% branch | C | [03:20] |
| 9 | Incomplete on arrival | 0, 1 | ~50% | C | [02:15] |
| 10 | Broker share | 0 | 6% → 4.5% | C | [08:58] |
| 11 | Stage split of the 9 days | 0 | 1.5 / 4.5 / 1.0 / 1.5 / 0.5 | **A** | Our assumption from Megan's insight [02:53]; labelled illustrative |
| 12 | Term "member" | all | member | I | Brief §1 (research) |
| 13 | Role: credit assessor | 1, 2 | Credit assessor | C | Brief §3 |
| 14 | Role: Head of Lending Ops | 0–2 | Head of Lending Operations | C | Brief §1 |
| 15 | Role: Head of Broker Distribution | 3 | Head of Broker Distribution | C | Brief §8 |
| 16 | Role: COO | 0 | COO | C | Brief §8 |
| 17 | Documents checked | 1 | Payslips, bank statements, ID | C | [03:33] |
| 18 | Self-employed document | 1 | Tax returns | C | [03:33] |
| 19 | Self-employed in phase 1 | 1 | Not in the checklist at start | **A** | One-pager check 2 → VM2 |
| 20 | Payslip recency | 1 | Within 30 days | **A** | BFSI pack default → VM1 |
| 21 | Statement coverage | 1 | 3 months | **A** | BFSI pack default → VM1 |
| 22 | Agent alone | 1 | Check + list missing + draft | C | [06:08] |
| 23 | Assessor approves request | 1 | Yes, every request | C | [06:08] |
| 24 | No AI credit decisions | 1 | Agent declines | C | [06:08] |
| 25 | AI says when unsure | 1 | "Not sure, needs a person" flag | C | [06:20] |
| 26 | Request channel | 1 | Email to broker | C | [03:47] |
| 27 | Document source | 1 | LOS document store via broker portal | C | [06:28] |
| 28 | How documents leave the LOS | 1 | Simulated feed | **A** | W2 gaps → VM3 |
| 29 | Document format | 1 | PDFs and photos | **A** | One-pager check 4 (folded into VM3) |
| 30 | Minutes per file today | 1 | 30–40 | C | [08:39] |
| 31 | Minutes per file after | 1 | ~5–10 | **A** | W2 (our proposal) |
| 32 | Rounds today | 1 | 2–3 | C | [03:47] |
| 33 | Rounds after | 1 | 1 | **A** | W2 Output 4 |
| 34 | DLA | 2 | $1,200,000 | C | [04:09] |
| 35 | Above DLA | 2 | Credit committee | C | [04:09] |
| 36 | Committee cadence | 2 | Twice weekly | C | [04:09] |
| 37 | DLA same for all home loan types | 2 | One row, all types | **A** | One-pager check 1 → VM4 |
| 38 | Allocation rule | 2 | Oldest complete file first | **A** | W2 gaps → VM5 |
| 39 | Broker hears only by email today | 3 | No in-between status | I | Brief §3 step 6; check 3 |
| 40 | Status calls today | 3 | "Hundreds a week" | C | [08:48] (number pending) |
| 41 | Status calls after | 3 | About half | **A** | Our estimate |
| 42 | Broker-visible stages | 3 | Journey stages 1–6 | I | Brief §3 |
| 43 | Broker platform | 3 | Generic broker portal | **A** | Unknown (W2 gaps) |
| 44 | Data residency | Close | AU, "non-negotiable" | C | [06:47] |

**C + I share = 32 of 44 (73%).** Gate A needs ≥ 60% ✔. All 12 A values are either validation moments (19, 20, 21, 28, 29, 37, 38), said aloud as our estimate in the summary (31, 33, 41), or labelled on screen (11 illustrative, 43 generic).

---

## Output 6: Validation moments and live changes

| # | Scene / step | "We assumed…" (said aloud) | Likely answer | Live change if "no" (≤ 2 min, no-code) | Rehearsed? |
|---|---|---|---|---|---|
| VM1 | 1 / step 3 | "…payslips within 30 days and 3 months of statements. Is that your rule?" | No: e.g. 60 days, or 6 months for some loans | Change the recency values in the checklist rule; re-run the agent on Whitford; the flag changes. **D1 for an agent:** rule changed, agent behaves differently | New for rehearsal (not in the M6 kit list we can see) |
| VM2 | 1 / step 4 | "…self-employed applications aren't in the first phase. Should they be?" | Yes (they mentioned tax returns) | Add "2 years' tax returns + notice of assessment" to the checklist for self-employed; switch a seed file to self-employed; agent asks for them | New for rehearsal |
| VM3 | 1 / step 9 | "…documents can flow from your loan system like this. How do they leave it today?" (to Raj) | Partly / unsure | **No live change** (architecture). Log the answer for partner discovery; show the stand-in label | n/a |
| VM4 | 2 / step 3 | "…the $1.2m limit is the same for all home loan types. Is it?" | No: different for investment or high-LVR | Add a second limit row for the named loan type; route a new file at the boundary to committee | New for rehearsal (pattern: Scentia `labPackRule`) |
| VM5 | 2 / step 4 | "…the queue works oldest complete file first. Is that right?" | No: settlement date or broker priority | Switch the allocation rule; the queue reorders | New for rehearsal |

Soft checks (no live change): stage split of the 9 days (scene 0) · brokers hear only by email (scene 3).

---

## Output 7: Close sheet (AE, last ~15 minutes)

**Summary lines**
- **Scene 0:** "You can see where the 9 days go, against your under-5 goal, from the files your team already works in."
- **Scene 1:** "Documents checked in minutes, not 30–40; one round with the broker, not two or three. Your assessor approves every request; no credit decision by AI."
- **Scene 2:** "Your team changed [the rule they corrected] in under two minutes, and the next file followed it."
- **Scene 3:** "Brokers see the stage and what's outstanding, so fewer of the hundreds of weekly status calls."

**Open qualification questions (phrased as helpful)**
1. **Decision process** (missing): "So we plan the next steps around how you decide: who else needs to see this before a decision, and in what order?"
2. **Paper process** (weak): "Is there a value where procurement runs a tender? If so, we'll shape the proposal to fit it."
3. **Economic buyer** (if Lisa absent): "What would Lisa need to see to back this? Could we take her through the turnaround view for 15 minutes?"
4. **Critical Date** (none stated): "Is there a date this needs to show results by: spring next year, the LOS renewal, a board meeting?"
5. **Competition** (known, Microsoft; maybe Salesforce): "Are you looking at other options for this, for example within your Microsoft estate?"
6. **AI gate**: "What would your risk committee need to see before an AI task touches member files?"

**Mutual action plan draft (anchor: LOS contract renewal ~Jan 2028, I; confirm the real date)**
| # | Step | Owner | Proposed date |
|---|---|---|---|
| 1 | Broker status-call number + one-pager checks back | Megan | Fri 14 Nov |
| 2 | Technical session: document flow out of the LOS, architecture, data residency | Raj + SC | Wk of 17 Nov |
| 3 | AI governance answers (in-region hosting, logging, AI Studio coverage) in writing from Creatio | SC | By 28 Nov (depends on internal asks) |
| 4 | Pre-brief to the CRO's risk committee using the governance pack | Raj, with SC support | Early Dec (their cadence: to ask) |
| 5 | Business case: minutes per file, rounds, status calls, days to decision | AE + Megan | Wk of 24 Nov |
| 6 | Proposal (platform phase 1; AI scene as a follow-on, **no pilot until A is Green**) | AE + SC | Fri 5 Dec |
| 7 | COO review of the Proposal | Lisa, Megan, James | Wk of 8 Dec |
| 8 | Decision / procurement path agreed | Lisa | To ask (unknown) |

**Likely objections (Brief §9)**
| Objection | One-line answer |
|---|---|
| "People will hear 'CRM' and roll their eyes." | "This is a lending workspace and AI assistant around your loan system; you've just seen your team's own stages and rules in it." (Never say CRM) |
| "We did a CRM project five years ago and it failed." | "That's why we start with one outcome, documents and turnaround, in weeks, and your team changes it themselves, as you saw." (D6/D1; proof point: "customers reported a 68% reduction in application development time", Nucleus Research, Apr 2026) |
| "Data has to stay in Australia." | Can say: "We can host the AI model in-country, including Australia." Plus: "the default model runs on Microsoft Azure in the same region as your Creatio site" (public docs). **Don't say** "data never leaves Australia". Offer written confirmation via step 3 |
| "Where does the AI run?" (Raj; rule 9) | As above, and: "Creatio doesn't train models on your data." Certifications: SOC 1, SOC 2, ISO 27001. For anything else (logging, AI Studio specifics): "We'll get you the official answer in writing." |
| "I'm not promising LOS access." | "You don't need to for this: today's demo used a stand-in, clearly labelled. Your loan system stays; we'd work out the document path with you in discovery." (D5) |
| "We're a Microsoft shop." | "We work alongside Microsoft 365 and your existing systems." (D5; don't argue about Microsoft) |
| "Can the AI approve loans?" | "No, and it isn't designed to. It checks and drafts; your assessors decide." |

---

## Output 8: Variants

**Applies here: P+A with Amber A**
- The AI scene (scene 1) runs on **simulated documents and a simulated LOS feed**, labelled on screen.
- **Don't propose a pilot.** Say instead: "When we've worked out with Raj how documents can leave the loan system, and your risk committee has what it needs, we'll propose a measured trial on one task with success measures agreed up front." Upgrade to Green needs: data reachable (VM3 answer + technical session) and no policy blocker (risk committee pre-brief).

**If P drops to Amber before the build** (e.g. Lisa disengages): 1-day L2 reference demo: B-M1, B-M2 and B-M3 with Harbourline's logo, stage names, roles ("assessor", "credit committee", "broker"); no $1.2m rule, no custom checklist; AI scene on the BFSI default checklist. Upgrades back to Green when the AE confirms Lisa's engagement.

**Red:** not applicable.

---

## Output 9: Gate A check

- [x] Every scene traces to a pain in the customer's words (Output 1; quotes with timestamps)
- [x] Every scene names a differentiator; the core set is covered (D1 scene 2 + live changes · D3 scene 1 · D2 scenes 0, 3 · D5 scene 1)
- [x] ≥ 60% of config values are C or I: **32 of 44 (73%)**; the rest are validation moments, stated estimates or labelled
- [~] Every scene uses a named module or pattern with a buildability rating ✔; **one open 🔴 risk** (agent reading real PDF content) needs the SE's confirmation or approval of the labelled fallback **before the build starts**. A no-code replacement is named, so this passes on the rule's wording, but the SE check is still owed
- [x] The demo opens with the outcome (scene 0), not the login screen
- [~] Each pain has a KPI (from → to): ✔ for pains 1 and 2; pain 3's "to" (about half) is our estimate, and the "from" number is still pending from Megan
- [x] SC hours fit the colour's budget: **30 h vs 24–32 h**
- [ ] **Peer check:** reviewer **not named**. The SC must name another SC and get the 15-minute async review before the build

**Result: Gate A NOT yet passed.** Content passes; two items are open: the peer reviewer (not named) and the SE check on document reading.

## Quality check
- [x] No more than 3 scenes plus the opening view
- [x] Nothing shown as real that is simulated (5 simulated items listed and labelled)
- [x] No claim outside the catalogue; AI/data statements only from "can say"
- [x] No real personal data in seed data (fictional applicants, broker and documents)
- [x] The demo script reads as a business story a colleague could present from
