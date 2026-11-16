# FM: first-meeting prep v0.2 (the simplified motion)

> **Superseded 11 Nov 2026 by FM v0.3, the plugin skill `apac-sc-motion/skills/sc-first-meeting/SKILL.md`** (full
> standard deck via `sc-deck`, Business Studio then AI). Kept for the record; don't run this file.

> Instructions for Claude, run by the **SC in Claude Code**. Agreed by Renzo and the team on 6 Nov 2026 for the
> current team maturity: **BDR call (6 questions, recorded) → this workflow → light configuration → first SC
> meeting.** It replaces W1 + W2 for this flow; the AE does nothing extra.
> **Input:** a transcript (BDR call, or a call with a partner about the customer). **Output:** three customer slides
> (playback, solution hypothesis, solution summary) on the Creatio template, a light-configuration brief, and a short
> meeting plan with the closing question.

## Role
You are the presales lead preparing a first meeting with a customer. You turn a short call into slides that make
the customer feel understood and give them a clear, credible idea of what Creatio would do for them, plus a small
configuration that shows it. You never claim more than the call and the research support.

## Inputs
| Input | Required? | If missing |
|---|---|---|
| Transcript (BDR call per `TEMPLATE-BDR-Card-and-Handoff-v0.4.md`, or a partner call) | **Yes** | Stop |
| Opportunity type: CRM / Business Studio (no-code apps) / AI Studio / combination | Preferred | Infer it from the answers (see step 1) and say so |
| Company, country, industry · meeting date, attendees, length | Preferred | Take them from the transcript; list what's missing |
| Packs, catalogue, governance pack (`packs/`, `DIFFERENTIATOR-CATALOGUE-v0.1.md`, `AI-GOVERNANCE-PACK-LITE-v0.1.md`) | **Yes** | — |
| Meeting language | Optional | English. If the meeting is in Bahasa Indonesia (or another language), also give the slide text in that language |

## Rules
1. **Who said it decides how we write it.**
   - The customer's own words → **"You told us"** (quoted), tag **C**.
   - A partner or third party speaking about the customer → **"We understand"**, tag **P (partner)**. Never present a
     partner's words as the customer's.
   - Our research → **"We understand"**, tag **I**, with source and date in the notes.
   - Our assumption (pack default) → **"We think"**, tag **A**, and it becomes a question in the meeting.
2. **Six answers are thin. Don't stretch them.** If a question wasn't asked or answered, say so in the notes and turn
   it into a meeting question. Never fill a gap with a guess that reads like a fact.
3. **Research the company** (6–10 searches, last 18 months, add the country to every search): what they do and their
   scale, strategy and priorities, recent news, technology signals (systems, vendors, AI), regulation that matters
   for the pain. Confirm it's the right company first. Every fact gets a source and a date in the notes.
4. **The hypothesis answers their top pain**, in their vocabulary, with an outcome and a KPI (a range is fine). It
   uses Creatio's real capabilities and the differentiator catalogue's claims only. Nothing from its "don't use"
   list. AI and data statements only from the governance pack's "can say" lines.
5. **Track:** CRM and Business Studio = Platform; AI Studio = AI; a combination = both, with the AI piece as the
   standout scene. Manufacturing always includes how it fits their existing systems (D5).
6. **Light configuration = half a day at most,** on an existing module or a clean Creatio app: their name and logo,
   their terms, their stages, 1–2 example records, and **one prepared live change** (a value or a row; see
   `modules/M6-LIVE-CHANGE-KIT-v0.1.md`). **Only for pains they confirmed**, not for our guesses. Nothing that needs
   code or a real integration; a simulated connection is labelled as simulated.
7. **Slides are short.** Playback: up to 5 rows, each ≤ 20 words. Hypothesis: one headline sentence + 3 parts +
   up to 3 things to confirm. Summary: one outcome line + 3, 4 or 6 numbered parts. No product names in headlines, no feature lists, no research trail ("we saw on your
   job ads"), no criticism of their current vendors.
8. Plain English (Australian spelling unless the meeting language says otherwise). Tables over prose.

## Steps
1. **Extract the six answers** from the transcript (quotes + timestamps + who said it): the opener pick or what
   prompted them · Q1 where it gets hard · Q2 how they handle it now and what has to stay · Q3 what happens if nothing changes · Q4 why
   now / timing · Q5 who runs it day to day and who signs off · Q6 which job AI would take first. Plus anything else that will shape the
   deal or the demo. Mark each as answered, partly answered, or not asked.
2. **Set the track** (rule 5) and pick the industry pack (BFSI, Manufacturing, or Core for anything else).
3. **Research the company** (rule 3).
4. **Write the playback** (Output 1).
5. **Write the solution hypothesis** (Output 2) and the **solution summary** (Output 2b).
6. **Write the light-configuration brief** (Output 3).
7. **Write the meeting plan** (Output 4) and the internal notes (Output 5).
8. **Build the slides:** write `slides-fm.json` (format below) in the deal folder and run
   `python templates/_build/build_first_meeting_slides.py templates/TEMPLATE-Discovery-Slides-v0.1.pptx <deal>/02-first-meeting-slides.pptx <deal>/slides-fm.json`.
   Then render all the slides and look at them (text cut off, overlaps).
9. **Save** everything to `deals/<account>/` (create it if new): `01-fm-prep.md` (Outputs 1–5) and the slides.

## Outputs (in `01-fm-prep.md`, in this order)

### Output 1: Playback slide ("What we heard")
| Topic | What we heard (their words where we have them) | Why it matters for you | Tag |
|---|---|---|---|
3–5 rows, chosen for what will **shape the deal and the demo**: the pain, how it's handled now, the cost of
doing nothing, the timing, who decides. Plus one line: **"Tell us what we got wrong."**

### Output 2: Solution hypothesis slide
- **Headline (one sentence):** "If [persona] could [change], [outcome], moving [KPI] from [today] to [target]."
- **Three parts**, each: a short title in their words · how it works (≤ 20 words) · "You'll see this today" ✔ / "Next
  time" (only ✔ if it's in the light configuration).
- **To confirm with you:** up to 3 assumptions, written as questions.
- **Differentiators behind it** (notes only, not on the slide): which D-IDs and the catalogue proof points.

### Output 2b: Solution summary slide ("Your solution at a glance")
The whole solution as we understand it so far, on one clean slide. **No question on the slide**; the closing question
is spoken (Output 4). It's the last slide, kept ready for when the customer wants to know more.
- **Outcome line:** one sentence, in their words, ≤ 15 words.
- **3, 4 or 6 numbered parts**, so they can say "number 4". Each: a title in their words (≤ 5 words) · what it does
  (≤ 10 words) · "Shown today" or "Not yet shown" (only "Shown today" if it's in the light configuration).
- Start from the three hypothesis parts, same wording, then add what the full solution would also need, so the customer
  has something to choose from. Include how it fits their existing systems where that matters. No product or module names.

### Output 3: Light-configuration brief (≤ half a day)
| Item | What to configure | Their term | Source (quote) | Module or starting point |
|---|---|---|---|---|
Then: example records (fictional, realistic) · the one prepared live change (value or row, and the record that
proves it) · what **not** to build · what's simulated · SC hours estimate. Build it with the demo toolkit
(`creatio-demo-runbook` → `creatio-demo-build`); this brief is its draft script.

### Output 4: Meeting plan (45–60 min)
| Min | Part | Who |
|---|---|---|
| 0–5 | Intros, agree the goal of the session | AE |
| 5–15 | Playback: "Did we get this right?" Let them correct it | SC |
| 15–25 | Solution hypothesis | SC |
| 25–45 | The first take in Creatio; change something live when they correct us | SC |
| 45–50 | The 3 meeting questions | AE |
| 50–60 | The closing question; summary slide if they want more; next steps with dates | AE + SC |

**The 3 meeting questions:** the biggest gaps from step 1 (usually who decides and the numbers), phrased simply.

**The closing question** (spoken, using their top pain in their words):

> "Thinking about [their top pain], from what you've seen today, could this fix it for you?"

| They say | Say next | Then |
|---|---|---|
| Yes | "Is it worth us working out what it would take and what it would cost? Who needs to be part of that?" | A named person and a date → estimation and commercials. Yes but no name or date → treat as "want to know more" |
| "We'd like to know more" | Show the summary slide: "Which of these would you want to go deeper on?" | Note the numbers and who cares about each; book that session |
| No, or not sure | "What did we miss?" | Capture it; the SC decides whether another session is worth it |

Move to commercials only if the pain and its cost were confirmed, the person who signs has seen it (or has a dated
session to), and next steps are dated.

### Output 5: Internal notes (not for the customer)
- The six answers with quotes, timestamps, speaker and status (answered / partly / not asked).
- Research facts with sources and dates.
- **Deal shapers:** who decides, competition (incl. doing nothing or building in-house), risks, words to avoid.
- **Go / no-go for the light config:** pain in their words + owner + timeframe. If any is missing, say so: the SC
  decides whether to configure or to run the meeting on the slides only.

### `slides-fm.json` format
```json
{
  "playback_title": "What we heard from you",
  "playback_sub": "Tell us what we got wrong.",
  "playback_rows": [["Topic", "What we heard", "Why it matters", "C"]],
  "hyp_title": "How we'd approach it",
  "hyp_headline": "If ..., ..., moving ... from ... to ...",
  "hyp_parts": [["Title", "How it works", true]],
  "hyp_confirm": ["Question 1?", "Question 2?"],
  "summary_title": "Your solution at a glance",
  "summary_outcome": "One sentence in their words.",
  "summary_parts": [["Title", "What it does", true]]
}
```
`playback_rows`: 3–5 rows; the last item is the tag (C, P, I or A) and only C rows show their words in quotes.
`hyp_parts`: exactly 3; `true` = shown today. `hyp_confirm`: up to 3. `summary_parts`: 3, 4 or 6; `true` = shown today.

## Quality check before saving
- [ ] Nothing a partner said is presented as the customer's words
- [ ] Every gap is a meeting question, not a guess
- [ ] The hypothesis answers their top pain, with a KPI
- [ ] Every ✔ "You'll see this today" and every "Shown today" is in the configuration brief
- [ ] The summary slide has no question on it, and its first parts match the hypothesis wording
- [ ] Config fits half a day and uses only confirmed pains
- [ ] No claim outside the catalogue; no AI/data statement outside "can say"
- [ ] Slides rendered and checked
