# Pilot guide: how we run a deal (APAC presales motion v0.5)

**For:** BDRs, AEs, SCs in the 6-week pilot. **Read time:** 5 minutes. Full detail: [SC-MOTION-PROCESS-v0.5.md](SC-MOTION-PROCESS-v0.5.md).

**The idea in one line:** we do our homework before the customer speaks, use one 30-minute call to confirm and sharpen
it, and come back with their problem solved in Creatio. **Two customer meetings before the Proposal.**

> **Simplified flow (6 Nov 2026, process §4.0):** BDR asks the 6 questions (recorded) → SC + Claude run
> [FM](workflows/FM-First-Meeting-Prep.md) on the transcript (playback + hypothesis slides, ≤ half-day light config) → first SC
> meeting. Steps 2–5 below are replaced by that for now; steps 6–9 apply to later stages.

## The 9 steps

| # | Step | Who | What you do | Tool / file | Rule |
|---|---|---|---|---|---|
| 1 | **BDR call** | BDR | Record it. Cold: three-pain opener, they pick one · raised hand: "What prompted it?". Then the 6 questions. Book a 30-min session with AE + SC only if: pain in their words + owner + timeframe | [One-page call sheet](TEMPLATE-BDR-Card-and-Handoff-v0.4.md) ([Word](TEMPLATE-BDR-Call-Sheet-v0.4.docx)) | **No recording (or 3-line note), no booking** |
| 2 | **Pre-call pack** | AE or SC | Paste the handoff into the shared Claude project → research, 5 hypotheses, slide, pre-filled card | [W1](workflows/W1-Pre-Call.md) in the [shared Claude project](CLAUDE-PROJECT-SETUP-v0.1.md); paste Outputs 8 and 4 into the [discovery slides](templates/TEMPLATE-Discovery-Slides-v0.1.pptx) | **No pack, no call.** The SC checks it (10 min) |
| 3 | **Discovery** (30 min) | AE runs, SC leads discovery | Record (ask first) · the hypothesis slide: "which are true, which hurts most?" · "where does it break?" · size it · why now, who signs · book the demo with the right people. **No Hello Deck** | [20-minute card](TEMPLATE-Discovery-Card-v0.2.md): fill the ★ blocks only | Write their exact words |
| 4 | **Go / no-go** | Claude scores, SC decides | Paste the card + transcript → Brief, score, one-pager | [W2](workflows/W2-Post-Call.md) | 🟢 full demo · 🟠 1-day reference demo · 🔴 [Red email](templates/TEMPLATE-Red-Followup-Email-v0.1.md): video + 2–3 questions (AE sends ≤24 h; a reply re-runs W2). **The Sales Director backs the gate** |
| 5 | **"What we heard"** | AE sends within 24 h | One page: their journey, the outcome we'll show, yes/no checks, attendees | W2 output | No product screens |
| 6 | **Build the demo** | SC + Claude | Design first (W3: scenes, validation moments, close sheet; a peer SC checks it), then build from its demo script with the demo toolkit; record a backup video | [W3](workflows/W3-Demo-Design.md) + packs + catalogue | Must show **D1 + D3 + D2 or D5** (manufacturing: always D5) |
| 7 | **Value demo** | SC presents, AE runs | Open on their outcome · scene per pain · "we assumed X, is that right?" · change it live when they correct us · close with a mutual action plan | Runbook | Economic buyer in the room if at all possible |
| 8 | **Proposal** | Claude drafts, SC finalises | Within 48 h (or the agreed date) | [W5](workflows/W5-Close.md) + [template](templates/TEMPLATE-Solution-Proposal-v0.1.md) | Conservative value case; AI credits always costed |
| 9 | **Partner Handover Pack** | Claude drafts, SC finalises | Same source as the Proposal; walkthrough with the partner | W5 + [template](templates/TEMPLATE-Partner-Handover-Pack-v0.1.md) | Partner confirms it can deliver every commitment |

## Five things never to do
1. Run a discovery without a checked pre-call pack.
2. Demo a 🔴 deal live.
3. Say anything about AI and data beyond the "can say" list in the [governance pack](AI-GOVERNANCE-PACK-LITE-v0.1.md) (e.g. never "your data never leaves Australia" yet).
4. Use a claim from the catalogue's "don't use" list (e.g. "37% lower TCO than Salesforce", "10x faster", "AI is free").
5. Knock a competitor by name.

## What to log for the pilot (per deal)
Dates of BDR call, discovery, demo offered, demo held, Proposal sent · number of customer meetings · go/no-go colour ·
SC hours · SE hours · outcome. The SC adds what was confirmed or missed to the industry pack's harvest log.

## Where to get help
SC pack owners: Core/General · BFSI · Manufacturing (names to be confirmed at sign-off). Renzo owns the process.
