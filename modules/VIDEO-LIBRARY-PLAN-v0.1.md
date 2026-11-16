# Demo video library: plan v0.1 (design; nothing recorded before sign-off)

> **Why:** the tiered gate only holds if Red deals still get something good. A Red deal gets a short recorded demo
> and 2–3 questions instead of SC build time ([process §5.3](../SC-MOTION-PROCESS-v0.5.md)). The same library gives
> every live demo its backup video (Gate B) and gives Amber deals and Proposals short clips to link to.
> **How they're made:** the demo toolkit records from a working stand: `creatio-demo-video-browser` (a timed take in
> Chrome, a voice-over script timed to the real scenes, then the presenter's own recorded voice laid over it), and
> `creatio-demo-video-phone` for mobile scenes. So **a video can only exist once its module is built and green.**
> **Owner:** each pack owner for their industry's videos; Renzo approves before first use.

## 1. What the library holds

| Type | Length | Who it's for | Made from |
|---|---|---|---|
| **Industry demo** (Red follow-up) | **4–6 min**, in chapters | Red deals; nurture; anyone who missed the demo | A standard industry stand (Core + overlay modules), fictional data |
| **Scene clip** | 60–90 s, one proof moment | Amber follow-up, Proposals ("see it in 90 seconds"), AE emails | Cut from the industry demo or a module take |
| **Deal backup video** | Full planned demo | The live demo, if the stand fails (Gate B) | That deal's stand, after the build; **never sent outside the deal** |
| **Personal intro** | 30–60 s | The Red email | Recorded by the AE on their laptop or phone, per deal |

**Why short:** a Red buyer gave us no commitment, so we are asking for five minutes, not an hour. Chapters let them
jump to their pain. The full value demo is the reward for re-engaging.

## 2. The first videos (in build order)

| # | Video | Chapters (each = pain → proof moment) | Core set shown | Depends on modules | Owner |
|---|---|---|---|---|---|
| V1 | **General: "From enquiry to resolved, on one platform"** | Outcome view · case + SLA with a live rule change · AI triage that a person confirms · fits your systems | D1, D2, D3, D5 | M1, M4, M6, M5 (triage), M7 | Core pack owner |
| V2 | **BFSI: "Home loan decisions in days, not weeks"** | Turnaround view · AI document check, assessor approves · approval limit changed live · broker status | D1, D2, D3, D5 | B-M1, B-M2, B-M3, B-M9, M6 | BFSI pack owner |
| V3 | **Manufacturing: "Warranty and complaints beside your ERP"** | Record arrives from "SAP" · claim triage, a person confirms · a rule changed live · status back to the ERP | D1, D3, D5 (D2) | MM1, MM2 or MM3, MM6 | Manufacturing pack owner |
| V4 | **AI Studio: "An agent that acts, with your people in control"** | The task · agent does it alone · flags and hands off with a summary · a rule it reads changed live | D1, D3, D5 | M5 / B-M6, M6 | Core pack owner + SE |

Then scene clips cut from V1–V4 (one per chapter). Add an industry video only when a second deal in that industry
needs it.

## 3. Standards for every video

**Story (Great Demo!):** open on the outcome in the first 20 seconds. One chapter per pain: the situation in one line
→ the result → do it → the value in one line. No login screens, no menu tours, no feature lists.

**Content rules**
- **Fictional company and data only.** Never a real customer's stand, name, logo or data, even with permission.
  Scentia, Pertamina and other customer demos can't be reused as videos; their modules can.
- **Claims only from the [differentiator catalogue](../DIFFERENTIATOR-CATALOGUE-v0.1.md)**; nothing from its "don't use"
  list. AI and data statements only from the governance pack's "can say" lines. No prices.
- **Simulated integrations are labelled** on screen ("simulated ERP"), as in live demos.
- Show the live change as a change (M6 T1/T2), with the "trained configurator close to the business" line.
- Plain Australian English voice-over at ~140 words a minute. **Captions on** (many people watch muted, and captions
  help non-native English speakers across APAC).
- End card: "Want to see this on your process? Reply to the email, or book here: [AE booking link]."

**Production (toolkit)**
1. Module(s) green in readiness on the standard industry stand.
2. Write the voice-over lines from the chapter table and the catalogue's claim wording.
3. Record the take (`creatio-demo-video-browser`); the toolkit times the voice-over table to the recorded file.
4. The presenter (pack owner or a strong presenter) records the lines; the toolkit lays them in.
5. Add captions and chapter markers; export 1080p.
6. **Review:** a peer SC checks the claims and the "don't use" list; Renzo approves. Log the version and date.

**Effort:** about **1–1.5 SC days per industry video** once the stand is green (take, voice, review), plus scene clips
~1 hour each. Measured in the pilot.

**Refresh:** when Creatio changes the UI noticeably, when a claim or proof point changes in the catalogue, or every
6 months, whichever comes first. A video with an outdated UI does more harm than none.

## 4. Hosting and tracking (decision needed)

A Red video only helps qualification if we know who watched it. Needs a host that gives a **link per recipient and
view data** (who watched, how much, which chapter).

| Option | Notes |
|---|---|
| Creatio's own sales video or enablement tool, if there is one | Preferred: ask sales ops / marketing first |
| A video host with viewer tracking (e.g. Vidyard, Loom Business) | Needs budget approval |
| SharePoint/Stream link | No per-viewer tracking outside Creatio's tenant; only a fallback |

**Open question for Renzo / sales ops:** which tool, and who pays. Until decided, send a SharePoint link and ask the
2–3 questions in the email; replies are the only signal.

## 5. How a Red video re-qualifies a deal

| Signal | AE action |
|---|---|
| Replied to any question with a real answer | Re-run W2 on the reply; it may score Amber or Green |
| Watched most of it, or one chapter twice (if tracked) | Day-3 email or call on that chapter's pain |
| No open, no reply after the day-7 nudge | Nurture (marketing); no more SC time |

The email and the follow-up are in [TEMPLATE-Red-Followup-Email-v0.1.md](../templates/TEMPLATE-Red-Followup-Email-v0.1.md).

## 5b. Until the videos exist (the pilot will hit this)

The pilot starts before V1–V4 can be recorded, because their modules aren't built yet.
- **Red deals in the pilot:** send the Red email with Creatio's **public** product videos for that area (creatio.com,
  Academy), plus the personal intro and the 2–3 questions. Pick a video that matches their pain; check its claims
  against the "don't use" list first.
- **Record V1 first**, as soon as M4 + M6 are built (they are the first modules after sign-off).
- Count Red deals in the pilot log, so the week-6 review can see whether the videos are worth the effort.

## 6. Open items
| # | Item | Owner |
|---|---|---|
| 1 | Hosting and tracking tool (§4) | Renzo → sales ops |
| 2 | The standard industry stands (one per industry, fictional company) that V1–V4 are recorded on | Pack owners, after sign-off |
| 3 | Pick 2–3 public Creatio videos per industry as the interim set (§5b) | Each pack owner, before day 1 |
| 4 | Who presents the voice-over (one voice per video series is best) | Renzo |
