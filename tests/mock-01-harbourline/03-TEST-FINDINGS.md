# Test findings: mock call 01 (Harbourline, fictional, BFSI, P+A)

Date: 3 Nov 2026. Tested: the 20-minute card v0.2, W2 post-call v0.1, go/no-go rules (§5.3), the one-pager format.

> **Bias warning:** Claude wrote both the call and the outputs. The customer was realistic (vague in places, an IT
> voice pulling elsewhere, half-commitments) but still cooperative. This proves the **mechanics**, not how real
> customers answer. A real recording is still needed.

## What worked

| Area | Result |
|---|---|
| 20 minutes is enough | Discovery took ~13 min. Ranking against the hypothesis slide got 3 ranked pains + 2 rejected in about 1 minute |
| Hypothesis slide | 3 of 5 hit; the 2 misses were informative (owned by another team / IT) |
| Journey on screen | Produced 9 steps with their terms, roles, systems and 4 break points: enough for an **L3** demo |
| "Size" block | Got all the numbers the value case needs (days, volume, minutes per file, broker share) |
| W2 Brief | Every fact traced to a quote + timestamp; the evidence tags held up |
| One-pager | Fits one page, uses their words, no jargon, forwardable to the COO |
| Gaps → validation moments | Each assumption has a handling route; the demo storyline came straight out of the customer's own insight |

## What broke or was missing → fixed now

| # | Finding | Fix applied |
|---|---|---|
| 1 | **P+A scoring wasn't defined.** P was clearly Green, A clearly Amber; the process had one result per deal | §5.3 + W2: two results. P decides the demo; an Amber A means the AI scene runs on simulated data and no pilot is proposed until A is Green |
| 2 | **Track A couldn't be scored from the card alone.** The AE filled only ★ blocks, and the A-only questions (data, human vs agent) sat in the un-starred Break block | Card: those two questions are ★ for Track A |
| 3 | **"Failed CRM project" + "CRM" as a toxic word** had nowhere to go, but they were the most important positioning insight | Card: a "Risks" line + "Words to avoid". W2: positioning in the Brief |
| 4 | **The ≤5-day target was missed through no fault of ours** (customer month-end → 8 working days) | Metric reworded: demo *offered* within 5 working days |
| 5 | W2 produced an actions table with owners and dates that the spec didn't ask for; it's clearly useful | W2: actions table required |

## Open findings: resolved 3 Nov (Renzo agreed; applied in process v0.4)

| # | Finding | Decision (as applied) |
|---|---|---|
| 6 | **The Green rule is lenient.** P went Green with the economic buyer not engaged, the decision process unknown and a failed-project history. Cheap with reuse, but SC time is still spent | **Tiered gate:** Green (economic buyer named) = full L3 build · Amber = 1-day L2 reference demo · Red = recorded video + questions. An unknown decision process must be asked in the one-pager and at the demo close |
| 7 | **The AI governance pack is needed 2 days after discovery**, and it doesn't exist. In BFSI this blocks the first AI deal | Governance pack lite in Phase 1 (`AI-GOVERNANCE-PACK-LITE-v0.1.md`). In-country hosting confirmed by Renzo; routing, fallback models and AI Studio coverage still to confirm |
| 8 | **Hypotheses should carry an owner** (business vs IT vs another team). H4 and H5 were rejected because they belong to other teams, which wasted a slide slot | Tag each hypothesis with its owner; the slide shows **4 owned by attendees + 1 expansion** (a miss maps the org and a second buyer) |
| 9 | The customer refused a screen share (member data). This is likely the norm in BFSI | Replace the screen share with **"send us one thing"** (a number, report, sanitised screenshot or process doc), the same for all industries |

## Files
- Input: [01-input-transcript.md](01-input-transcript.md)
- Output: [02-W2-output.md](02-W2-output.md)
- Workflow: [../../workflows/W2-Post-Call.md](../../workflows/W2-Post-Call.md)
