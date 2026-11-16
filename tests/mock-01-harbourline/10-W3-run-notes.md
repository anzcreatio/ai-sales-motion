# W3 blind-test run notes: Harbourline (FICTIONAL) · 3 Nov 2026

> Run of [W3-Demo-Design.md](../../workflows/W3-Demo-Design.md) v0.1 on [02-W2-output.md](02-W2-output.md), output in
> [09-W3-design-pack.md](09-W3-design-pack.md). Files 01 and 04–08 were not opened. 03-TEST-FINDINGS was not opened either.
> Paper exercise; no instance or toolkit touched.

## 1. Headline
- **Scenes:** 0 COO turnaround view · 1 AI document check (hero) · 2 DLA + queue rules changed live · 3 broker status.
- **C + I share:** 32 of 44 (73%). Honest, but see §4.1: on rules and thresholds only it is 9 of 16 (56%) and would fail.
- **Gate A:** **not passed.** Content passes; open items are the peer reviewer (no name available) and an SE check on whether the agent can really read PDF documents.
- **SC hours:** 30 h vs 24–32 h budget (assuming an 8-hour day; the hours are guesses, see §2.6).
- **Length:** design pack **5,711 words**. Too long for "a peer reviews it in 15 minutes" (Gate A).

## 2. Ambiguities and the judgement calls I made

| # | Where | Ambiguity | What I chose |
|---|---|---|---|
| 2.1 | Rule 2 vs Step 3 vs W2's agreed scenario | Rule 2 says scene order follows the customer's pain ranking. Ranked pain 1 (time to decision) is already answered by scene 0, and the scene most directly on it (DLA rule) is the weakest-evidenced. Megan's own insight says documents (rank 2) *cause* rank 1, and the scenario agreed in the call runs lodge → doc check → approve → dashboard | Journey order: docs (rank 2) → rules (rank 1, decision step) → broker status (rank 3). This breaks rule 2 literally. The workflow should say whether "ranking" or "journey/agreed scenario" wins |
| 2.2 | W2 Output 4 pain IDs | Suggested scenes use "H1/H2/H3" with H3 = documents and H2 = broker status, but the Brief ranks documents 2nd and brokers 3rd. W3 Step 3 says re-rank by the customer's ranking | Used the Brief's ranking. W2 and W3 should share one pain-ID scheme |
| 2.3 | Rule 1, P+A budget | Budget is stated per colour, but P+A has two colours (Green P, Amber A). Is the AI scene in the 3–4 day Green budget, or does Amber A add/limit anything? | One budget: Green P, 3–4 days; AI scene inside it on simulated data |
| 2.4 | "SC days" vs "SC hours" | Budget is in days, Output 3 asks for hours; no day length defined | 8 h/day → 24–32 h |
| 2.5 | What SC hours include | Does the toolkit's automated build count? W3 design time? Runbook approval? Gate B prep (reset, video, agent test set)? | Counted SC hands-on time for build supervision + customer layer + rehearsal + test set + reset/video; excluded W3 itself |
| 2.6 | Hours estimation | Packs give module sizes (S/M) but no hours per size, so every hours figure is a guess, and "fits the budget" can be made true by choice of numbers | Guessed (S ≈ 3 h, M ≈ 4–10 h). A size → hours table is needed |
| 2.7 | L3 vs L4 for Green | Rule 1: "L4 only where integration is a buying criterion". W2 says "sit around the LOS" is the buying condition, but LOS access is unproven and A is Amber | L3 + **simulated** L4 (LOS stand-in only). Unclear whether "simulated L4" is a real level or a contradiction |
| 2.8 | What counts as a "config value" (rule 6, Output 5) | No definition. Stage names, KPI baselines and role titles are easy Cs that inflate the share; rules/thresholds are where the As live. Process §6 says "config fields", workflow says "config values" | Counted everything that appears on screen as a value (44). Reported the rules-only share in §4.1 |
| 2.9 | Rule 7: a live change for each VM | W2's most important validation moment ("how do documents leave the LOS?") is an architecture question with no ≤2-min no-code change | Kept it as VM3 with "no live change"; it's still one of the 5. Workflow should allow "logged for discovery" VMs |
| 2.10 | Output 6 "in the M6 live-change kit or listed as new" | The M6 kit contents (Scentia `CHANGES.md`) aren't available in the workspace; I can't check what's in it | Marked all live changes "new for rehearsal" |
| 2.11 | Gate A "approved build pattern" | Process §6/§9.3 says Gate A only accepts catalogue patterns; no pattern catalogue file exists. W3's Gate A says "named module or pattern" | Used module IDs (M/B-M) as the "pattern". Process and workflow disagree on the bar |
| 2.12 | Buildability of AI document reading | Whether the agent can read real payslip PDFs on the platform isn't in any pack. If not, the scene shows something as real that isn't | Rated 🟠 with a named 🔴 risk, an SE check and a labelled fallback (pre-extracted fields). Left Gate A open on it |
| 2.13 | Personas: attendee names on screen | Rule 10 forbids real personal data in seed data; it's silent on using attendees' names (Megan, Lisa) as demo users | Used role titles + fictional staff names; attendees named only in the talk track |
| 2.14 | Lisa's 20-minute window | W2 promised Lisa the turnaround view in the first 20 min; the Great Demo! structure puts the hero scene at minutes 8–24 | Added a "Lisa checkpoint" summary at ~10:18 |
| 2.15 | Soft checks | Some As (stage split of the 9 days, "brokers hear only by email") can't be changed live and aren't worth a VM slot | Listed them as "soft checks" outside the 3–5 VMs. Not a concept the workflow has |
| 2.16 | Targets tagged A | Rule 6 says every A the story depends on becomes a VM. "To" values (5–10 min, 1 round, about half the calls) are As the summarise beat depends on | Said aloud as "our estimate", not VMs. The rule as written would push to 8+ VMs, over the 3–5 limit |

## 3. Missing inputs
- **Brief §8b (Great Demo! situation)** is referenced by Step 2 but absent from the W2 output (the W2 workflow now has it; this mock predates it). Derived CBI/Delta from §2/§4; **no Critical Date exists**, so I used the LOS renewal (~Jan 2028, inferred) as a working anchor and made it a close question.
- **No one-pager replies, no "one thing"** (broker call number). All four checks became validation moments or soft checks; scene 3's KPI has no number.
- **Peer reviewer name**: not in any input. Gate A can't close without it.
- **SC and AE names**: inferred from the one-pager signature (Daniel and Renzo); W3 doesn't ask for them.
- **Customer branding/logo**: fictional, so placeholder.
- **`creatio-demo-runbook`**: named as the consumer of Output 4, but no such skill is in the available toolkit list (there are `creatio-demo-build`, `creatio-demo-prep`, etc.). I couldn't check what format it expects.

## 4. Conflicts between workflow, process and packs

| # | Conflict | Effect |
|---|---|---|
| 4.1 | The 60% C+I gate is easy to pass by counting baselines and names. On rules/thresholds only (values 19–29, 34–38), C+I = 9 of 16 (56%) | Gate A passes on the letter; arguably not on the intent ("the demo runs on their rules") |
| 4.2 | Governance pack: the "in-country hosting" can-say line is unconfirmed for **AI Studio** (#2d, #10), and Core M5 says don't lean on AI Studio governance in regulated deals. W3 leaves "how to build" to the toolkit, but the honest answer to Raj's "where does the AI run?" depends on whether the agent is Creatio.ai or AI Studio | The close-sheet answer is only safe if the agent is built in Creatio.ai, or if Raj is told AI Studio specifics come in writing. W3 should make the SC decide this before Gate A |
| 4.3 | Governance #7/#8: no documented approval-before-action or AI logging. D3's proof moment needs "the audit trail is shown". B-M10 (AI evidence view) doesn't exist yet | We show a log we build into the demo process; must not be presented as a platform audit feature. Not stated anywhere in W3 |
| 4.4 | Process §4.1: Track A demos need Gate B with an agent test set (10–20 inputs). W3's Output 3 doesn't list it, so the budget omits it unless the SC remembers | Added 2 h for it |
| 4.5 | Rule 3 says each scene has "one differentiator", but W2's scene 1 is "D3 (+ D5)" and scene 2 "D4 / D1"; the core set (4 Ds for P+A) can't fit 3 scenes + scene 0 with one each unless D5 piggy-backs | Allowed a secondary D per scene, as Step 3 permits ("add it as a proof moment") |
| 4.6 | Process §5.3 says Amber A means "no AI pilot is proposed", while process §4.1 Stage 3 says A missing any of the four → **Red**, or Amber with an AI ideas workshop | Followed the W2 result (Amber) and W3 rule 1; flagging that §4.1 could make this Red |
| 4.7 | B-M2 (the hero module) "does not exist" (BFSI §8), so "reuse before building" mostly means building M-size new work under a 3–4-day budget | Budget fit (30 h) is optimistic |

## 5. Was Gate A passed honestly?
**No, and I reported it as not passed.** Six of eight items pass on content. Open: (1) peer reviewer not named, (2) the
SE check on document reading. Two "passes" are soft: the 60% share depends on what counts as a value (§4.1), and pain
3's KPI "to" is our estimate with the "from" number still pending. If the workflow is used as-is, an SC under time
pressure could tick all eight boxes truthfully on the wording while the demo still rests on assumed rules.

## 6. Size and effort
- Output: 5,711 words (9 outputs + Steps 1–2 preamble). Output 4 and Output 5 are the longest. A 15-minute peer check
  is not realistic at this length; a one-page "Gate A summary" at the top would help.
- The workflow itself is clear on *what* to produce; most friction was in *counting rules* (hours, config values) and
  in rules that collide with the agreed scenario (scene order, one-D-per-scene, live change per VM).
