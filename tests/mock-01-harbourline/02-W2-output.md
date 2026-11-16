# W2 output: Harbourline Mutual Bank (FICTIONAL test)

> Produced by following [W2-Post-Call.md](../../workflows/W2-Post-Call.md) on [01-input-transcript.md](01-input-transcript.md).
> Inputs: transcript ✔ (recorded) · card ✔ (★ blocks only) · Part A ✔. Confidence: **good** for pains, journey and numbers; **low** for the decision process.
> Tags: **C** Confirmed (quote + time) · **I** Inferred · **A** Assumed.

---

## Output 1: Discovery Brief

### 1. Snapshot
| Field | Value |
|---|---|
| Account | Harbourline Mutual Bank, customer-owned bank, AU, ~180k members (I, research) |
| Pack / track | BFSI · **P+A** (C: platform "sit around" the LOS + an AI document-check task) |
| Attendees | Megan Holt, Head of Lending Operations: business owner, likely champion · Raj Iyer, Enterprise Architect: IT, influencer, cautious |
| Call | Recorded, 31 min, ~13 min of discovery |

### 2. Ranked pains
| Rank | Pain | Their words | Consequence | KPI | Tag |
|---|---|---|---|---|---|
| 1 | Slow time to decision on home loans | "Time to decision. That's the one the board keeps asking about." [02:05] | Losing broker share: "dropped from about 6 percent to 4 and a half percent of our main aggregator's volume" [08:58] | Days lodgement → conditional approval | C |
| 2 | Incomplete applications + manual document checks | "Half the applications come in incomplete." [02:15] · "expensive people doing admin" [04:00] | Waits + 2–3 rounds of back-and-forth; "might actually be the cause of the first one" [02:53] | Minutes per file on documents; rounds per file | C |
| 3 | Brokers chasing status | "brokers chasing us, yes, that's real" [02:15] | Lending support load ("hundreds of calls a week") [08:48] | Status calls per week | C |
| ✘ | Hardship / complaints | "sits with the member service team… They're fine." [02:34] | — | — | C (not a pain) |
| ? | Single member view | "an IT priority… data platform project" [02:40] | — | — | C (out of scope; owned by IT) |

### 3. Journey as described (home loan, front half)
| # | Step (their term) | Who | System | Breaks here? | Tag |
|---|---|---|---|---|---|
| 1 | Lodge (broker portal ~70%, branch ~30%) | Broker / branch | Broker portal → LOS | — | C [03:20] |
| 2 | Queue | — | LOS | **Wait "a day or two"** | C [03:33] |
| 3 | Document check (payslips, statements, ID, tax returns for self-employed) | Credit assessor | LOS doc store + email | **Incomplete → email broker → wait; 2–3 rounds** | C [03:33–03:47] |
| 4 | Serviceability | Assessor | LOS + a spreadsheet "because they don't trust it" | **Duplicate work** | C [04:09] |
| 5 | Credit decision | Assessor ≤ $1.2m (DLA); credit committee above | LOS; committee meets twice a week | **Committee wait above $1.2m** | C [04:09] |
| 6 | Conditional approval to the broker | — | Email from the LOS | No status in between → broker calls | C [04:31] / I |
| 7–9 | Valuation (outsourced) → formal approval → settlement | — | — | "mostly fine" | C [04:31] |

### 4. Numbers
| Measure | Today | Target | Tag |
|---|---|---|---|
| Lodgement → conditional approval | 8–10 days avg; some 3 weeks | < 5 days ("I'd love three"); big four 2–3 days for clean deals | C [08:18–08:24] |
| Applications | ~900/month, higher in spring | — | C [08:32] |
| Assessor time on documents | 30–40 min/file, more for self-employed | — (we propose ~5–10) | C [08:39] / A for target |
| Incomplete on arrival | "Half" | — | C [02:15] |
| Broker status calls | "hundreds a week" (Megan to get the number) | — | C [08:48] |
| Broker share, main aggregator | ~6% → ~4.5% this year | Recover | C [08:58] |

### 5. Rules and approvals
- DLA: assessor approves up to **$1.2m**; above that, **credit committee, twice weekly** (C [04:09]).
- Assessor must approve AI-drafted broker requests "at least at first" (C [06:08]).
- No AI credit decisions (C [06:08]). AI must say when it's unsure (C [06:20]).

### 6. AI (Track A element)
| Item | Value | Tag |
|---|---|---|
| Task | Document check: match payslip/statement/ID to the application, check recency, list what's missing, draft the broker request | C [05:50] |
| Agent alone | Check + draft | C [06:08] |
| Human | Approves the broker request; all credit decisions | C [06:08] |
| Data location | LOS document store (via the broker portal) + email follow-ups | C [06:28] |
| Data reachable? | LOS API "limited… I'm not promising anything" | C [06:35]: **weak** |
| Policy / owner | AI policy in draft; risk committee (chaired by the CRO) approves anything touching members or decisions | C [06:47–07:02] |
| Constraints | Data must stay in Australia, "non-negotiable"; Copilot already rolled out internally | C [06:47] |

### 7. Landscape
| System | Role | Must integrate? | Tag |
|---|---|---|---|
| LOS (vendor product, heavily customised, contract up in ~14 months) | Origination, doc store, serviceability, conditional approval emails | **Yes**: "we'd want something to sit around it" | C [04:50–04:59] |
| Broker portal | Lodgement | Yes (I) | C / I |
| Microsoft 365 + Copilot | Internal productivity | Likely (I) | C [06:47] |
| Data platform project (IT) | Single member view | No, out of scope | C [02:40] |

### 8. People and decision
| Item | Detail | Tag |
|---|---|---|
| Economic buyer | **Lisa Moretti, COO** (new; "made turnaround time her thing"); board above a threshold | C [10:08–10:17] |
| Champion | Megan (acting as one) · **James, Head of Broker Distribution** ("probably more than me"), not yet met | C [10:26] |
| Decision process | Unknown. A past CRM project "failed… took two years and nobody used it" | C [10:34] |
| Paper process | Tender via procurement above a threshold; number unknown | C [11:00] |
| Competition | Microsoft ("we're a Microsoft shop"); possibly Salesforce (digital team meeting) | C [10:50] |
| Why now | Broker share drop + new COO focus | C [10:08] |
| Risk gate | CRO-chaired risk committee for AI | C [07:02] |

### 9. Concerns and objections
- "People will hear 'CRM' and roll their eyes." [10:42]: **don't position this as a CRM.**
- "We did a CRM project about five years ago and it failed." [10:34]
- "Data has to stay in Australia, that's non-negotiable." [06:47]
- LOS access: "I'm not promising anything there." [06:35]

### 10. What got a reaction
- Documents as the *cause* of slow decisions (Megan's own insight [02:53]). Use it as the demo's storyline.
- "Expensive people doing admin" [04:00]. This is the value line.

### 11. Agreed next step
- **Demo:** Thu 13 Nov, 10:00. Scenario (Daniel's words, accepted): broker lodges → AI checks the documents and drafts the missing-docs request → assessor approves → time to decision on a dashboard.
- **Attendees:** Megan, Raj, **James** (requested), **Lisa** ("I'll try, I can't promise").
- **We promised:** a one-page summary before the invite; Megan forwards it to Lisa and James. **Megan promised:** the broker call volume.

---

## Output 2: Qualification score and go/no-go

| Criterion | Evidence | Strength |
|---|---|---|
| Pain + consequence | Broker share 6% → 4.5% [08:58] | **Strong** |
| Why now | Share drop + new COO [10:08] | **Strong** |
| KPI range | 8–10 days → < 5; 900/month; 30–40 min/file | **Strong** |
| Economic buyer | Named (COO), not engaged; attendance "I'll try" | Weak |
| Champion | Megan active; James possibly stronger, not met | Weak–medium |
| Decision process | Unknown; failed CRM history | **Missing** |
| Paper process | Tender above an unknown threshold | Weak |
| Competition | Microsoft; maybe Salesforce | Medium (known) |
| Commitments | Demo booked ✔ · senior attendee ✘ (pending) · will forward ✔ · screen ✘ (member data) | Medium |
| **Track A:** named task | Document check [05:50] | ✔ Strong |
| **Track A:** business owner | Megan | ✔ Strong |
| **Track A:** data reachable | LOS API limited, not promised | ✘ **Weak** |
| **Track A:** no policy blocker | Policy in draft; risk committee approval; AU residency | ⚠ **Not a blocker yet, but a gate** |

### Result
| Part | Result | Reason |
|---|---|---|
| **P: Platform** ("lending workspace around the LOS") | 🟢 **Green** | Ranked pain with consequence + why now + demo booked with the business owner |
| **A: AI document check** | 🟠 **Amber** | Task and owner are clear; data access is unproven and the risk committee is a gate. Demo it (it's the hero scene), but on simulated documents, and don't promise a pilot until the two items below are closed |

**Red flags:** none from the list. **Risk noted:** "failed CRM" scar tissue (not on the red-flag list; see test findings).

### Actions before the demo
| # | Action | Owner | By |
|---|---|---|---|
| 1 | Get Lisa (COO) to the first 20 min, via the one-pager + a short note from Daniel to Megan | AE | Fri 7 Nov |
| 2 | Confirm James attends; he's the likely real champion | AE | Fri 7 Nov |
| 3 | Ask Raj: how can documents leave the LOS today (API, export, the email path)? | SC | Before the demo |
| 4 | Send the **AI governance pack** (AU data residency, human approval, audit) so Raj can pre-brief the CRO | SC | Wed 5 Nov |
| 5 | Ask the tender threshold + the decision steps (in the one-pager) | AE | — |

---

## Output 3: "What we heard" one-pager (ready to send)

**Subject:** Harbourline lending: what we heard, and what we'll show you on 13 Nov

Hi Megan,

Thanks for the time today with Raj. Below is a one-page summary of what we heard, and what we'll show you on
Thursday 13 November. It would be great if you could forward it to Lisa and James. Could you also check the quick
questions at the bottom? A yes or no is plenty.

Daniel and Renzo

---

**What you told us**
- Home loan **time to decision is the board's top concern**: 8–10 days on average, sometimes 3 weeks, while the major banks do 2–3 days for clean deals.
- **Half of applications arrive incomplete**, so assessors spend 30–40 minutes per file on documents and go back to brokers two or three times. As you put it, documents may be the real cause of the delay.
- **Brokers send deals to whoever is fastest**, and Harbourline's share of your main aggregator's volume has dropped from about 6% to 4.5% this year.

**Where it breaks today**
Lodge → **wait in queue (1–2 days)** → **document check + requests to the broker (2–3 rounds)** → serviceability (**LOS + spreadsheet**) → decision (**credit committee twice weekly above $1.2m**) → conditional approval → valuation → settlement

**What we'll show you on 13 November**
Your lending team working *around* your current loan system, not replacing it:
1. **Where the time goes:** a live view of time to conditional approval, from today's 8–10 days towards your under-5-day goal.
2. **Documents checked in minutes, not days:** an AI assistant checks the payslips, statements and ID against the application and drafts the request for what's missing. Your assessor approves it before it goes to the broker. No credit decisions are made by AI.
3. **Brokers know where their deal is** without calling you.

**Quick checks (yes / no)**
1. Is the $1.2m limit the same for all home loan types?
2. Should self-employed applications be included in the first phase?
3. Do brokers only hear from you by email today (no status updates in between)?
4. Do documents arrive as PDFs or photos (no paper)?

**Proposed demo:** Thursday 13 November, 10:00–11:00
Suggested attendees: Megan, Raj, **James** (broker experience) and **Lisa** (we'll show the turnaround view in the first 20 minutes, if she can only join briefly).

**Two questions to help us prepare**
- When a decision like this is made at Harbourline, what are the steps, and is there a value threshold where procurement runs a tender?
- Could you share the weekly number of broker status calls you mentioned?

---

## Output 4: Gaps and validation moments

| Assumed / weak item | Demo depends on it? | Handling |
|---|---|---|
| How documents leave the LOS (API, export, email) | Yes (AI scene) | Simulated doc intake in the demo + **validation moment**: "We've assumed documents can flow from the LOS like this. Raj, is that realistic?" → partner discovery |
| Serviceability spreadsheet logic | No | Out of the demo; partner discovery |
| Queue / allocation rules | Yes (scene 1) | Assumed rule: oldest + complete first. **Validation moment** |
| Which broker portal / aggregator | Yes (scene 3) | Generic "broker portal" in the demo; one-pager check 3 |
| Self-employed in scope | Partly | One-pager check 2 |
| Risk committee requirements | Yes (for a pilot) | AI governance pack; show the audit trail and human approval in the demo |
| Credit committee: same rule for all loan types | Yes (scene 2 rule) | One-pager check 1 |

**Config level achievable:** **L3** (their terms: assessors, DLA, LOS, credit committee; their $1.2m rule; their KPI
baselines) **+ simulated L4** (an LOS document store stand-in), because "sit around the LOS" is the buying condition.

**Suggested scenes** (open on the outcome):

| # | Scene | Pain | Proof moment | Differentiator | KPI line |
|---|---|---|---|---|---|
| 0 | COO turnaround view (opening) | H1 | Time-to-decision dashboard by stage: where the 8–10 days go | D2 | 8–10 days → < 5 |
| 1 | AI document check → missing-docs request → assessor approves → broker notified | H3 (cause of H1) | Agent checks a file in seconds, flags a stale statement, drafts the request; the assessor approves; audit trail shown | **D3** (+ D5: works beside the LOS) | 30–40 min/file → ~5–10; rounds 2–3 → 1 |
| 2 | Business changes the rule live | H1 | Megan's team changes the DLA threshold or a document rule; the next application routes differently | **D4 / D1** | Committee wait avoided on eligible files |
| 3 | Broker status without a phone call | H2 | Broker portal view updates as the file moves | D2 | Status calls: "hundreds a week" → down |

**Positioning note:** never say "CRM" in this deal. Call it a *lending workspace and AI assistant around your LOS*.
