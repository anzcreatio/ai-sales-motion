# W5: close workflow v0.2 (Solution Proposal + Partner Handover Pack)

> Instructions for Claude, run by the SC in Claude Code after the value demo. Two documents from one source, so they
> never contradict each other. Proposal within 48 h of the demo, or by the date agreed with the customer if later; Partner Pack when the deal firms (or with the Proposal
> if the partner is already chosen).

## Inputs
| Input | Required? | If missing |
|---|---|---|
| Discovery Brief (W2 output), updated after the demo | **Yes** | Stop |
| Demo outcome notes: recording/transcript, or the SC's notes on reactions, corrections, live changes made, new pains, objections, agreed next steps | **Yes** | Stop: the Proposal must reflect what happened in the demo |
| Demo runbook + build log (stand, packages, what's simulated) | Yes for the Partner Pack | Partner Pack §4–5 marked "to complete" |
| Industry Pack (Core + overlay), differentiator catalogue, AI governance pack lite | Yes | — |
| Official price book (plan, products, AI credit packages) | For §7 costs | Use "[price from price book]" placeholders; never invent prices. Headline the risk-adjusted benefits "before costs" |
| Value per unit (loaded hourly cost per role, margin per deal) | For §7 benefits | Use the Industry Pack's default rates, tagged Assumed, and list them for the SC to replace |
| Partner effort band (estimation skills) | Optional | Partner Pack §9 marked "to estimate" |
| Plan durations (pilot weeks, time to first live outcome) | Optional | Use Industry Pack defaults, labelled "proposed; partner to confirm" in **both** documents |

## Rules
1. **Update the Brief from the demo first.** Upgrade what the customer confirmed (A → C and I → C), add corrections and
   new pains, and record which hot buttons got the strongest reaction. Both documents are built from this updated Brief.
2. **One source, two audiences.** Every promise in the Proposal appears in the Partner Pack's "Commitments made in the
   sale". Every assumption in the Proposal appears in the Partner Pack's assumptions register.
3. Follow each template's own writing rules (`templates/TEMPLATE-Solution-Proposal-v0.1.md`,
   `templates/TEMPLATE-Partner-Handover-Pack-v0.1.md`).
4. **Value case:** conservative. Risk-adjust each benefit by its evidence tag (−10% / −25% / −50%); **when a benefit mixes
   tags, use its least certain input's tag**; headline the risk-adjusted figure; never count flexibility; costs include AI credits.
5. **What counts as a promise:** any statement of what the solution will do, deliver, or by when (including plan
   durations and AI behaviour). Each one goes into Partner Pack §3.
6. **Words to avoid win.** If a catalogue proof point contains a word this deal avoids (e.g. an analyst title with "CRM"),
   use a different proof point or the demo itself, and tell the SC.
7. **Length:** ~500 words per page. Proposal body ≤ 5,000 words; Partner Pack ≤ 5,000 words before appendices (move
   the full assumptions register to an appendix if needed, keeping the top 10 in §6).
8. **Claims:** only from the differentiator catalogue and governance pack, attributed as they say.
9. Customer-facing text has no internal jargon (no MEDDPICC, Gate, evidence tag, D-IDs, track letters).
10. **Delivery Assurance** (16 Nov 2026): when the deal shows partner delivery risk (new partner, custom or integration
    lines, core-system integrations, a customer burned before), propose Creatio Delivery Assurance in the Proposal's
    delivery approach and list the planned reviews in the Partner Pack. Package and price come only from the AE.
    Internal reference and "can say" lines: `apac-sc-motion/knowledge/DELIVERY-ASSURANCE-v0.1.md`.

## Steps
1. Update the Brief from the demo outcome notes (Rule 1). List the changes.
2. Pick the hot buttons: **include** the 2–4 pains with the strongest reaction (in discovery or the demo), and **order** them
   by the customer's own ranking.
3. Pick the differentiators: the core set (D1 + D3, plus D2 for P, D5 for A; **P+A and manufacturing include D5**; P+A
   adds D2 too when one platform was a hot button), max 4. Proof points from the catalogue; **where the catalogue has
   none, "what you saw in the demo" is the proof**, and the gap is reported to the catalogue owner.
4. Build the value case (benefits from the Brief's numbers, costs from the price book or placeholders).
5. Draft the Proposal.
6. Draft the Partner Handover Pack.
7. **Consistency check (Gate C):** run the checklist below and fix any failure before replying. Items that depend on missing
   inputs (prices, effort band, build log) are reported as **pending**, not failed.
8. Reply with (or write to files, if asked): the change list from step 1, both documents, the Gate C result, and a list of anything the SC must fill in
   or check (prices, effort band, unverified claims).

## Gate C consistency check
- [ ] Every Proposal promise is in Partner Pack §3 "Commitments made in the sale"
- [ ] Every Proposal assumption (§10) is in Partner Pack §6, with a validation route
- [ ] Every Partner Pack item has an evidence tag; every built item has a demo status; simulated items are listed
- [ ] No Proposal statement contradicts the Partner Pack (scope, phases, AI behaviour, integrations)
- [ ] AI statements match the governance pack's "can say" list
- [ ] Costs include licences, AI credits and the partner band; the headline value is risk-adjusted
- [ ] No claim from the catalogue's "don't use" list; no competitor named negatively
