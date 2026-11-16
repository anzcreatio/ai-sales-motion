# Shared Claude project: setup kit v0.1

**For:** Renzo (sets it up once) · **Used by:** AEs, SCs and BDR leads in the pilot · **Sign-off decision:** 6
**What it does:** runs W1 (pre-call pack) and W2 (post-call Brief, go/no-go, one-pager) for any booked deal, from the
same instructions and knowledge for everyone. W5 (Proposal + Partner Pack) stays with SCs in Claude Code.

## 0. Check before you build it (blockers)

| # | Check | Why | Owner |
|---|---|---|---|
| 1 | **Creatio's Claude plan is Team or Enterprise**, and every pilot AE/SC has a seat | Only those plans can share a project with colleagues. On Pro, each person would need their own copy and they'd drift | Renzo → IT |
| 2 | **Creatio allows customer call transcripts and notes in Claude** (security/legal) | W2 needs the transcript. Team/Enterprise doesn't train on your data by default, but company policy decides. Without approval, W2 runs on the card notes only | Renzo → Creatio security (add to the governance asks) |
| 3 | **Web search is allowed** for the org | W1 depends on it. Without it, W1 must stop rather than guess | IT |

If 2 is a "no" for now: run W2 from the filled-in discovery card only, and drop the transcript input.

## 1. Create the project

1. In claude.ai: **Projects → Create project**.
2. **Name:** `APAC Presales: Discovery (W1 + W2)`
3. **Description:** `Pre-call packs and post-call Briefs for booked discoveries. One chat per deal. SC checks every output.`
4. Paste section 2 below into **Project instructions** (Set custom instructions).
5. Upload the files in section 3 to **Project knowledge**.
6. **Share** the project with the pilot AEs and SCs (Can use). Give edit rights to Renzo and the pack owners only.

## 2. Project instructions (paste exactly)

```text
You support the Creatio APAC presales team. Your instructions are in the project knowledge files. Follow them exactly.

WHICH WORKFLOW
- The user pastes a BDR handoff form (company, trigger quote, attendees), or the same form for a meeting we generated ourselves (no trigger) → run W1-Pre-Call.md (its Outbound branch when there's no trigger) and return the pre-call pack.
- The user pastes a filled-in discovery card and/or a call transcript → run W2-Post-Call.md and return the SC summary, the Brief, the qualification score, the "What we heard" one-pager and the gaps.
- Anything else → ask which of the two they need. Do not draft proposals here: say "Proposals are done by the SC in W5."

FILES
- Knowledge files may appear without their folder names. "packs/CORE-PACK-v0.1.md" is the file CORE-PACK-v0.1.md, and so on.
- Use the industry pack the handoff names: BFSI-PACK, MANUFACTURING-PACK, or CORE-PACK only for General.
- Claims and proof points come only from DIFFERENTIATOR-CATALOGUE-v0.1.md. Never use anything on its "don't use" list.
- Anything about AI, data, hosting or security comes only from the "can say" lines in AI-GOVERNANCE-PACK-LITE-v0.1.md. If a question isn't covered, say "we'll confirm in writing".

ALWAYS
- W1 needs web search. If you can't search, say "Web search is off: turn it on and resend" and stop. Never fill gaps from memory.
- Every research fact has a source and a date. Evidence tags as the workflows define them (C / I / A).
- Plain Australian English. Tables over prose. The pack must be readable in 10 minutes.
- End every output with: "SC check required before this is used with the customer."
- Slide text (W1 Outputs 4 and 8) is written to paste straight into TEMPLATE-Discovery-Slides-v0.1.pptx.

NEVER
- Personal data about people beyond their public professional role.
- Credentials, prices not in the price book, or promises the catalogue doesn't support.
- Competitor criticism by name in anything customer-facing.
```

## 3. Project knowledge (upload these 11 files)

| File | Used by | Words |
|---|---|---|
| `workflows/W1-Pre-Call.md` | W1 | 1,590 |
| `workflows/W2-Post-Call.md` | W2 (v0.2) | 2,090 |
| `TEMPLATE-BDR-Card-and-Handoff-v0.4.md` | W1 (what the BDR asked) | 610 |
| `TEMPLATE-Discovery-Card-v0.2.md` | W1 Part A, W2 input | 850 |
| `packs/CORE-PACK-v0.1.md` | both | 3,580 |
| `packs/BFSI-PACK-v0.1.md` | both | 6,140 |
| `packs/MANUFACTURING-PACK-v0.1.md` | both | 6,750 |
| `DIFFERENTIATOR-CATALOGUE-v0.1.md` | both | 2,110 |
| `AI-GOVERNANCE-PACK-LITE-v0.1.md` | both | 960 |
| `templates/TEMPLATE-Red-Followup-Email-v0.1.md` | W2 (Red deals) | 620 |
| `modules/VIDEO-LIBRARY-PLAN-v0.1.md` | W2 (video choice for Red) | 1,280 |

About 25,500 words (~35k tokens), well within project limits. **Don't upload:** W5 and the Proposal/Partner templates
(SC-only), the research files (too long; the packs already summarise them), the tests, or anything internal-only
such as the sign-off pack.

## 4. How people use it (one chat per deal)

| When | Who | What to do |
|---|---|---|
| Discovery booked | AE or SC | New chat named `[Account]: W1 [date]`. **Turn web search on.** Paste the BDR handoff form (+ BDR notes). Wait 3–5 minutes |
| Same day | SC | Check the pack (10 min): company, numbers in exact units, sources, hypotheses an owner could say no to. Fix in the chat ("H4 is a truism, rewrite it") |
| Before the call | AE | Paste Output 8 into slide 1 and Output 4 into slide 2 of `templates/TEMPLATE-Discovery-Slides-v0.1.pptx`. Paste Output 9 into Part A of the card |
| After the call | SC | **Same chat.** Paste the filled card + the transcript (if allowed). W2 returns the Brief, score and one-pager |
| Within 24 h | AE | Send the "What we heard" one-pager after the SC's go/no-go |

Keep W1 and W2 in the same chat so W2 sees the hypotheses. Save each output to the deal's Teams/SharePoint folder
(decision 8); the chat isn't the record.

## 5. Keeping it current

- **One owner per file:** Renzo for the workflows and cards; the pack owners for their packs (decision 5).
- When a file changes: bump its version in the file name, **replace** it in project knowledge (delete the old one,
  don't keep both), and post a one-line note in the pilot channel.
- The process doc (§8) is the master list of current versions. If the project and §8 disagree, §8 wins.

## 6. Test it once before day 1

Re-run the Great Southern Bank test: new chat, paste `tests/w1-test-01-great-southern-bank/00-input-handoff.md`, then
compare with `01-W1-output.md` and the review in `03-REVIEW.md`. **Pass:** 10 outputs, sources dated, ~100 agents and
280 licences kept apart, H4 written as a pain, ends with the SC-check line. A fail means the instructions or files
didn't load; fix that before anyone uses it.

## 7. Known limits

- Output varies run to run; the SC check is what makes it safe.
- Web results can be stale or wrong company (shared names). W1 step 2 checks the ABN/country; the SC confirms.
- Each AE's chats are private to them unless they share them. The deal folder is the shared record.
