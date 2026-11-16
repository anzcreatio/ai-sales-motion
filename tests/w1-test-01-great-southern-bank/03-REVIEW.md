# W1 test 01: review (3 Nov 2026)

Blind run: a fresh agent followed W1 v0.1 as written. Inputs: [00-input-handoff.md](00-input-handoff.md) (real bank,
invented BDR call). Output: [01-W1-output.md](01-W1-output.md). Agent notes: [02-run-notes.md](02-run-notes.md).

## Verdict: good enough to take into a real call, after a 10-minute SC check

| Check (W1 quality list) | Result |
|---|---|
| Every research claim sourced and dated | ✔ mostly; undated and older sources flagged |
| Hypotheses 4 + 1, owners, one restating the trigger | ✔ (H1 restates the trigger) |
| Slide reads as industry observations | ✔ |
| People: public professional information only | ✔ titles; role holders flagged "check it's the same person" |
| Readable in 10 minutes | ✘ 10–12 min (links inside tables) |

## What made it valuable (things an SC wouldn't find in 10 minutes)
1. **The incumbent and its AI roadmap**: the contact centre runs on a contact-centre platform delivered by a telco
   partner, with call-note summarising on its roadmap. That reshapes H2 and the whole competitor angle (coexist, don't replace).
2. **A contradiction to probe**: public data says calls are answered fast; the BDR quote says customers wait too long.
   The pack says probe it (peaks? hardship queues? cost, not wait?) rather than assert it.
3. **Hidden stakeholders**: the bank is building its own first AI agents, so the data & AI lead is both the AI-risk
   owner and a likely "we'll build it ourselves" competitor. The pack says to get them in the room.
4. **Vocabulary and positioning**: the bank says "customers", not "members"; avoid "CRM" and "chatbot".

## Errors found (spot check by Claude)
| # | Error | Impact | Fix in W1 v0.2 |
|---|---|---|---|
| 1 | "~280 seats" in the snapshot. The vendor case study says about 100 agents and 280 licences | A wrong number in front of the customer kills credibility | Rule 1: keep numbers in their exact unit |
| 2 | Slide H4 "Boards want AI that is useful, controlled and explainable" is a truism: everyone agrees, we learn nothing | One of five slide slots wasted | Rule 5: every hypothesis must be something they could say "no" to |
| 3 | KPI benchmarks rely on weak vendor blogs | Low, flagged | Rule 1: prefer "our estimate" over a weak source |

## W1 changes applied (v0.1 → v0.2)
Undated/older/weak sources flagged · numbers kept in exact units · combined tags allowed · attendee naming rule ·
4 + 1 can sit mostly with the business owner · hypotheses must be falsifiable · sources as footnotes ·
customer's own vocabulary · confirm the right company first (ABN/country) · ask what the incumbent already promises ·
check public data against the BDR pain quote · "Not invited" rows allowed · opportunity type → track mapping.

## Cost and practicality
- One run: ~5 minutes, ~12 searches + 13 page fetches, roughly 120k tokens in total. Fine for SCs; for 8 AEs on
  shared Claude project limits, **W1 should be run by the SC, or once per booked discovery, not per lead**.
- 5 of 13 fetches were blocked (the bank's own investor PDF, exec page). Expect that, and keep the SC check.

## Still untested
- A real deal where we know the truth (hit rate of the hypotheses).
- An Industry Pack-fed run (no packs exist yet; the hypotheses here were built from general knowledge + research).
