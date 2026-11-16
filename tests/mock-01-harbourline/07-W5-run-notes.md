# W5 run notes: Harbourline Mutual Bank (mock 01, FICTIONAL)

Run of `workflows/W5-Close.md` (blind test) on `02-W2-output.md`, `01-input-transcript.md`, `04-input-demo-outcome-notes.md`,
the differentiator catalogue, the AI governance pack lite, and the Core and BFSI packs.
Outputs: `05-W5-proposal.md` (step-1 change list as an internal block at the top) · `06-W5-partner-pack.md`.
No price book, partner effort band, demo runbook or build log.

## 1. Gate C result

| Check | Result | Notes |
|---|---|---|
| Every Proposal promise is in Partner Pack §3 "Commitments made in the sale" | **Pass** | C-01 to C-21. I read "promise" broadly: anything the Proposal says we, the solution or the partner will do, including roles, dated deliverables and later-phase items |
| Every Proposal assumption (§10) is in Partner Pack §6, with a validation route | **Pass** | Proposal §10 #1–14 = Pack A-01 to A-14, same wording, each with a validation route. A-15 to A-24 are extra internal items |
| Every Partner Pack item has an evidence tag; every built item has a demo status; simulated items are listed | **Pass with caveats** | Tagged wherever the template has a Tag column. The template has no tag column for commitments (§3), the discovery agenda (§7) or risks (§8). Demo status comes from the SC's notes, not a build log. §4 and §5 are marked TO COMPLETE. Simulated items listed in §5: LOS document store stand-in and seed data |
| No Proposal statement contradicts the Partner Pack | **Pass** | Checked: scope, phases, pilot length and gates, the AI's alone/approves split, push updates instead of a portal, LOS stays the record, DLA values |
| AI statements match the governance pack's "can say" list | **Pass, with one risk** | Used only: in-country hosting "including in Australia" (provider not named), no training on customer data, SOC 1/SOC 2/ISO 27001. Approval and recording are described as part of the proposed process design (the governance pack's "design around it"), not as platform features. None of the "don't say yet" lines appear. **Risk:** the demo answer to Raj ("in-country hosting is available in Australia") was given for an AI Studio agent, and governance #2(d) and #10 say AI Studio coverage is unconfirmed |
| Costs include licences, AI credits and the partner band; the headline value is risk-adjusted | **Open (can't be fixed with these inputs)** | Licence, AI credit and partner rows are present but hold placeholders, so NPV and payback can't be calculated. The headline is risk-adjusted: about AUD 396k present value of benefits over 3 years, before costs |
| No claim from the catalogue's "don't use" list; no competitor named negatively | **Pass** | The Proposal names no competitor. The Partner Pack names Microsoft and Salesforce only as competition in the deal |

**Overall:** consistent; one item stays open until prices and the partner band exist. W5 step 7 says "fix any failure before replying", which isn't possible for this item.

## 2. What the SC must fill in or check before sending

**Fill in**
1. Prices from the official price book: Business Studio plan, products, AI credit package (Proposal §7 costs, Pack §1). Confirm the 3-year term.
2. Partner effort band (Proposal §7, Pack §9, using the estimation skills once a partner is chosen), then NPV and payback (Proposal §7, 3-year table).
3. Harbourline internal effort estimate (Proposal §7).
4. AE and SC surnames; partner names (Proposal cover, Pack §0).
5. Three demo screenshots (Proposal §2 and §5 placeholders). The demo wasn't recorded, so take them from the stand.
6. Source link for the SOC/ISO certifications (Proposal Appendix A). The governance pack says "with the link" but gives none.
7. Dates in the mutual action plan (Proposal §9), including the exact ExCo date in February 2027.
8. Partner Pack §4 and §5 from the build log: pattern IDs, stand and packages, click path, reset steps, full list of demo-only items, and a check of each demo status I took from the notes.

**Check (assumptions I made)**
9. Loaded hourly costs of **AUD 70 (assessor)** and **AUD 50 (lending support)**. They aren't in any input; I chose them and tagged them as assumed. They drive the value headline.
10. Other value-case assumptions: 7.5 min/file with the assistant, 50% fewer status calls, 5 min per call, half the benefit in Year 1, risk adjustment by the least-certain input.
11. Plan numbers I proposed: **8-week AI pilot** and **about 12 weeks to Phase 1** (anchored on the D6 Howdens proof). Both are now commitments C-15 and C-16, so the partner must confirm them.
12. **In-country AI hosting for AI Studio:** get written confirmation (governance internal asks #1, #2, #10) **before the 21 Nov CRO paper**. The demo answer has already gone further than the pack confirms.
13. The Proposal says the demo showed "what was checked and who approved". The demo notes don't say this explicitly; I took it from the W2 scene plan ("audit trail shown"). Check it.
14. Proof points: the catalogue has none for D3 or D5, so two of the three "Why Creatio" rows rely on the demo alone. The broker-status section has no catalogue proof point.
15. I left out D2's analyst proof (Gartner MQ "**CRM** Sales Platforms", Forrester Wave "**CRM** Software for Financial Services") because the deal's positioning note says never say "CRM". Decide whether to put them back.
16. I added locations for OTP Bank (Hungary) and Ent Credit Union (United States) from general knowledge. The catalogue asks us to "say where they are" but doesn't give the locations. Verify both.
17. "Microsoft 365 stays for your teams' email" (Proposal §5): the Brief has M365 integration only as "Likely (I)". Confirm with Raj.
18. **Test-data dates:** the notes say "Thu 13 Nov" and "Monday 17 Nov", but in 2026, 13 Nov is a Friday, 17 Nov a Tuesday and 21 Nov a Saturday. Both documents use dates only, with no weekdays.

## 3. W5 or template instructions that were ambiguous, contradictory or impossible

1. **Partner Pack §4–5 "marked 'to complete'" (W5 inputs table):** it doesn't say whether the whole sections stay empty or only the build-log-dependent parts. I filled what the Brief and demo notes support and marked the gaps. Gate C still asks for a demo status on every built item, which needs the build log.
2. **Hot buttons (step 2): "strongest reaction" vs "customer's priority order".** Documents got the strongest reaction but were ranked #2. I chose by reaction and ordered by the customer's ranking. The new committee-paper pain had no reaction to judge.
3. **Three differentiators:** the template says "D1 + D3, plus D2 **or** D5", but for a P+A deal the catalogue says to show **both** D2 and D5. Step 3 says to pick by "what the hot buttons need", which points to D2 (dashboard, broker status), while the buying condition and Raj's silo objection point to D5. This was a judgement call; I chose D5.
4. **Proof points that don't exist:** template §5 needs a catalogue proof point under each hot button, and §6 needs one per differentiator. The catalogue has none for D3, D4 or D5, so this was impossible for 2 of the 3 rows.
5. **Catalogue vs deal positioning:** D2's analyst proof titles contain "CRM", which this deal forbids.
6. **Governance pack contradictions:** "Safe to say: the default model runs on Microsoft Azure…" vs "Never name the cloud model provider." The pack header says "Internal. Not for customers yet", yet the Proposal's Appendix A must be built from it. The certifications line says "(with the link)" but no link exists.
7. **Value case inputs:** step 4 says "benefits from the Brief's numbers", but the Brief has no value per unit (hourly cost, margin). The −10/−25/−50% rule doesn't say what to do when a benefit mixes confirmed and assumed inputs.
8. **NPV, payback and the headline (template §7) can't be computed** without prices or the partner band. The template's 4-box asks for a "conservative headline value", so I headlined the risk-adjusted PV of benefits before costs.
9. **Gate C cost check vs W5's own fallback:** the inputs table says to use placeholders when there's no price book or band, but Gate C then fails, and step 7 says to fix failures before replying.
10. **"Promise" is undefined** for the Gate C commitments check.
11. **"Every Partner Pack item has an evidence tag"** while three template tables (§3 commitments, §7, §8) have no Tag column.
12. **"Screens from the demo"** (template rule 7): impossible, because the demo wasn't recorded and no screens were supplied.
13. **Plan numbers (template §8):** the pilot needs a length in weeks and Phase 1 needs a time to its first live outcome, but no input gives either. I had to propose numbers, and they then become commitments.
14. **Timing:** "Proposal within 48 h of the demo" (W5 header) vs the date agreed with the customer (17 Nov, about 4 days later).
15. **Step 8 "Reply with… both documents":** the user's test brief asked for files instead, so I put the change list in the Proposal as an internal block.
16. **Rule 1 says "A → C"** but the Brief also had Inferred items that the demo confirmed (e.g. brokers hear only by email). I treated those as I → C.
17. **"Body ≤ 10 pages"** has no page definition for a Markdown output.

## 4. What took most effort

1. **The value case:** no value per unit, prices or band. I had to invent clearly tagged assumptions, choose a rule for mixed evidence tags, add a ramp, and still could only headline benefits before costs.
2. **AI and governance wording:** saying enough to answer Raj and the CRO without going past the "can say" list. The demo had already gone further than the pack confirms for AI Studio, and human approval and recording are design choices, not platform features.
3. **The promise-to-commitment mapping for Gate C:** I re-read the Proposal line by line to extract every promise. The Partner Pack also had to keep the Proposal's assumption wording exactly.
4. Picking the third differentiator, and finding proof points where the catalogue has none.

## 5. Word counts and length

| Document | Words |
|---|---|
| `05-W5-proposal.md`, whole file | 4,601 |
| of which internal change-list block | 685 |
| Proposal body (cover to §10) | 3,669 |
| Proposal appendices | ~250 |
| Proposal executive summary | 342 (fits one page) |
| `06-W5-partner-pack.md` | 5,292 (of which §4 is ~1,690) |
| `07-W5-run-notes.md` | ~1,800 |

**Is the Proposal body within 10 pages?** **Yes, probably about 8–9 pages** once laid out in A4 at 11 pt. Prose runs about 500 words a page, the tables and roadmap add space, and the three screenshots still to add will push it towards 10. The budget is tight: adding the screenshots plus a cost table with real figures could exceed 10 pages. If so, move §4 into §3 or shorten the §7 risks.

The Partner Pack is probably about 11–13 pages, above the template's 6–10 target. The extra length is mainly the wide §4 tables and the 24-row assumptions register.
