# Context handover: Renzo × Claude (Creatio APAC Solution Consulting)

**Read this first, every session (short on purpose, ~4k tokens). Last restructured 12 Nov 2026.**

> Source of truth: **this folder**. `CLAUDE.md` (auto-loaded) points here. This file is enough to start; the history
> is in **`CONTEXT-HANDOVER-LOG.md`** (toolchain gotchas §2, past builds §3, every motion decision §4, deal history
> §5a). Read the log only when a task needs it, for example "why did we decide X", a clio/Creatio build, or a deal's
> history. Each deal's current detail lives in its own folder (`Deals/<account>/`, notes such as `01-fm-prep.md`,
> `04-build-notes.md`, `PROJECT-NOTE.md`). No passwords or tokens are in these files; never ask for them. Renzo
> registers environments himself.
>
> Account-bound, not in this folder: the published sign-off page (https://claude.ai/artifact/9r67D1pjyW9UaCyVE5eT5y,
> owned by Renzo's original account; another account can view it if shared but can't edit it), claude.ai connectors,
> org-provided plugins (`ai-driven-apps`). Claude's memory files on Renzo's PC
> (`C:\Users\r.huruiti\.claude\projects\*\memory\`) add background; they belong to the Windows user, not the account.

---

## 1. Who you are working with

- **Renzo Huruiti**: Solution Consultant (SC), Creatio APAC. Based in Australia (Sydney time). Recent deals span
  AU, Indonesia, Vietnam and Malaysia.
- He builds Creatio demos and POCs himself with Claude Code (desktop app, Windows) plus the Creatio toolkits
  (clio MCP, creatio-demo-toolkit, creatio-ai-app-development-toolkit). He has also used Codex for some builds and
  hands work between the two with written briefs.
- Style: moves fast and thinks out loud. Typos are normal. He wants a recommendation, not a menu. He likes plain
  English, tables and short steps, and he dislikes long prose.

### Working preferences (confirmed by him)
| Preference | Detail |
|---|---|
| **OOTB / no-code first** | Use business rules, page config, placeholders and tooltips before any code. He declined even a 10-line page handler on Pertamina. Mention code only as an optional extra. Exception: custom Angular components when Freedom UI cannot give the UX (Scentia portal). |
| **Beyond the minimum** | "Mature, competition-beating, clean, intuitive UI/UX" in every scenario: hub views, where-used lists, KPI strips, chips, dashboards, tooltips, and seed data so that no view is empty. |
| **Business sense over feature dumps** | Demos must map to real business pains, not "configure what they said". |
| **Verification in browser** | Latest choice (Oct 2026): **automatic**. After a clio change, open the page in the built-in browser and check it yourself. If sign-in is needed, he signs in. (An older Aug 2026 preference said manual, but the later one supersedes it.) |
| **Safety gates** | Read before write (`get-page`, `describe-business-process`, `get-entity-schema-properties`). Dry run before deletes. Ask before deletes, compiles, installing packages (e.g. CrtProcessBuilder), security/permission settings or user creation. **Don't run compile-creatio unless asked**: a compile once broke an env for hours. |
| **Never** | Type passwords, register clio envs, create accounts, or open/quote `CREDENTIALS.md` files. |
| **Log everything** | Dated PROJECT-NOTE / build-decisions files, a prompt log, a demo script that stays true, and a reset script. |
| **Hand-over mindset** | Every build should be explainable to the customer's devs or a partner, and rebuildable from builder scripts. |

---

---

## 2. Where things stand (12 Nov 2026)

| Area | Status | Detail |
|---|---|---|
| Motion design | Done: process v0.5 + workflows, packs, catalogue, templates. Sign-off with the Sales Director pending (`SIGN-OFF-PACK-v0.5.md`) | `SC-MOTION-PROCESS-v0.5.md` (§8 = current versions, §15 = changes) |
| Plugin `apac-sc-motion` | **v0.18.0 published 13 Nov 2026 15:17** (0d84925, tag v0.18.0; log §4 item 81). Next: 0.19.0 (BOM, release notes, inbox routing; items 74-77). Published to SharePoint `Plugin/`. Every release needs a CHANGELOG entry (`publish.ps1` enforces it and tags `v<version>`); Claude tells each SC about updates at session start | `apac-sc-motion/CHANGELOG.md`; log §4 items 58–61 |
| Bank.AI log + deal dates (13 Nov) | `sc-bank-ai-log` → SharePoint `Bank-AI-Requirements/` (320 lines from Pegadaian, Mandiri, Adira; share the folder with Bank.AI; run on Navalo and EWB next). Build rules: ask before compile/restart, token check first. `deal-dates.json` on every deal (none backfilled yet). Committed, **not yet released**: waits on the East West build-plan changes (log §4 66b–67) | `CONTEXT-HANDOVER-LOG.md` §4 66b–67 |
| Team | Renzo (rh), Willy (wn), Ferdhi (fa). New deal folders `<account>-<initials>` | `sc-setup` deal folder rule |
| Scheduled tasks (Renzo's PC) | Fri 3 pm weekly lessons digest; Mon 8 am release message (backup until the update notice is proven for Willy and Ferdhi). Transcript intake task (W0) is **not** in the task list as of 12 Nov: ask Renzo before relying on it | `workflows/W0-Transcript-Intake-v0.1.md` |

**Live deals** (one line each; open the deal folder for detail, the log §5a for history before 12 Nov):

| Deal | Folder | Where it is |
|---|---|---|
| Navalo / Metrics Credit Partners | `metrics-credit-partners` | **Meeting 2 held Mon 16 Nov: informal RFP briefing, no demo** (review `18-meeting-review-2026-11-16.md`, log §4 item 96). Lending platform Aryza via middleware; CIO Sal; group CEO endorses; POC sprint offer accepted. **Next: RFP criteria ~Wed 18 Nov → `sc-rfp`, then `sc-demo-plan` for the sprint. Hold BWP4+ broker build until then.** Stand `11014108` clean. Build history: `build/build-report.md` |
| East West Bank (PH) | `east-west-bank-rh` | Plan v5 (47 h) **approved 12 Nov; Phase 1 build in progress on `11014930-demo` (clio `ewb-pain`)**. Done 13 Nov: prefix `lab`, cliogate, CrtProcessBuilder; packages `labPainDiscovery` / `labUiKit` / `labPainDiscoveryEwb`; full `labPd*` object model; live score view `labPdCardTotal`; stage bar (DCM via import-schema); guard process; module + EastWest seed (6 cards, 25 steps); roles + record rights; UI kit 0.2.0 (5 components, branch `ewb-components` in `C:\Projects\builds\ui-kit-ewb`) installed; card page, board, cards list, scoring rules, units' home, leads workplace, configurable "How this works" help panels on every page — all re-checked on screen 13 Nov after the restart (board fix: unscored cards off the plot, kit `c66150e`). **Reusable module (13 Nov, Renzo "Start now")**: module exports cleanly with no SQL view and no East West wording (customer wording via replacing pages + instruction "Replaces"); scale, board axes, stage rule, all kit text configurable; kit 0.3.0 `d9fcbf8`. Unit rights on new cards automated (script task, compiled 13 Nov). Clean-install test passed on `pd-clean` (11014933-demo); one manual step (record permissions on cards). Install guide `09-module-install-guide.md`. Tested on 3 other use cases (bank AI portfolio, RFP fit-gap at 300, manufacturing quality): all work; board now merges bubbles at volume (kit 0.3.1). **Programmes (14 Nov, kit 0.4.0):** several use cases on one stand, default programme from a system setting. Limits: axis names and stages shared across programmes, scales ≤5. Log rows 60–87. **UI polish (14 Nov, kit 0.5.1):** short card titles + quotes, slim help, visual system, card tiles home; brand step waits for EWB's logo. Plan `10-polish-plan.html`, rows 89–94. **Resume: `Deals/east-west-bank-rh/08-build-log.md` "Resume here"**. Logins 24 Nov, session 27 Nov or early week of 30 Nov |
| Abbe (packaging, AU) | `abbe-rh` | AE intro 11 Nov (Ayush ↔ Will Purcell, data and AI). **Detailed first demo Tue 1 Dec**: voice visit recap → right Kiwi account and fields → Monday (simulated). Deck 02 built; build plan 03 v2 (10 steps, 27.5 h, four value additions) **approved 16 Nov**; AE brief 05. Waiting on: clean stand (Renzo requesting), then approval pack + day-1 voice test on iPhone via Mac (log §4 item 97) |
| IQumulate (premium funder, Steadfast Group) | `iqumulate-rh` | Discovery + generic demo 22 Oct (AE Aaron + Koncept). **Biggest risk: Koncept did Steadfast Life (went badly); Wai-Lum spoke to its CEO and now fears implementation cost.** Plan: guided workshop 1 in Melbourne (broker quote follow-up) → journey built for workshop 2 → phased roadmap + fixed phase 1. **Decided 16 Nov: customer-led backed by Delivery Assurance** (maybe a different partner for bounded pieces); five delivery controls answer the Steadfast Life failures (log item 114); budget cycle Apr 2027. Next: Aaron gets Steadfast Life facts + Delivery Assurance scope + 12 Nov call notes, handles Koncept, calls Wai-Lum, sends `workshop/w1-00-invite-email.md` (log §4 item 107) |
| MartinJenkins (NZ consulting) | `martinjenkins-rh` | Advisor recommends separate ERP + CRM: now CRM vs CRM (log §4 items 112, 118). Next: Aaron calls Hannah (`07-aaron-call-brief.md`), then email 04 v0.2 + one-pager 06 (PDF) asking for a 2-h session on 3 adoption tests. Drafts await Renzo's SC check + 4 [TBC] |
| Scentia | `scentia` | Phase 1 + client separation built on `11014147-2-demo`; not yet tested as real users |
| Telkomsel | `telkomsel` | Meeting 12 Nov (Deloitte-led). Next: re-run FM on the meeting transcript, then the light config they pick |
| Suntory Oceania | `suntory-oceania` | Demo held 11 Nov; Andrew re-engages late Jan; send slides PDF + FMCG stories |
| Hardware & General | `hardware-and-general` | Built on `11011710-demo`; deck 07 and click path await SC check; waiting on Geoffrey's document |
| SAHE | `southern-academy-of-higher-education` | First meeting moved (TBC); keep-warm email approved, needs dates + AE name |

## 3. Resume here

- **16 Nov: `sc-bom` published in plugin 0.25.0** (§4 item 116; tag v0.25.0 = d0976d7, merged to `main`): which licences a deal needs (SKUs, candidate tier, extras, gotchas, sizing questions; no prices, no users). Catalogue `knowledge/BOM-CATALOGUE-v0.1.json` (that's the "untracked" file in item 115). To do: Renzo pushes `apac-sc-motion` with tags; first real run on Navalo once the RFP criteria land; Deal Desk to close OPEN-1 to OPEN-4.

- **16 Nov: EDB + plugin 0.24.0 published** (§4 item 115): `deals/edb-rh/` (existing customer, session Tue 17 Nov, deck `02-session-deck-2026-11-17.pptx`). Plugin 0.24.0 published (also ships 0.22.0 Delivery Assurance and 0.23.0 master stands): confidential terms, existing-customer path (`sc-guide` mode D), roadmap owners. Open: EDB's five archetype names for `confidential.json` (ask Renzo); the untracked `apac-sc-motion/knowledge/BOM-CATALOGUE-v0.1.json` belongs to another chat.

- **16 Nov: build on top of master stands** (§4 item 109): demo bar v0.3 §6c, build rules v0.5, register `apac-sc-motion/library/stands.json` (first master `11011710-demo`, H&G layer off first; `11013904-demo` off limits). Plugin 0.23.0 committed, not published. Next: register Renzo's new clean sandboxes as masters (names + industries), then publish.

- **16 Nov: Delivery Assurance knowledge** (§4 items 108, 110): `apac-sc-motion/knowledge/DELIVERY-ASSURANCE-v0.2.md` (internal; owner Alex Klochkov; no prices in any output, chat only with a warning). Hooked into first meeting, deck, workshop, meeting review, RFP, W5. Plugin 0.22.0 (not published). Open: currency; consider DA in the IQumulate delivery model.

- **16 Nov: IQumulate** (§4 items 107, 111, 114): `deals/iqumulate-rh/`. Decided: customer-led backed by Delivery Assurance (package #2 recommended, confirm with Alex Klochkov); strong PM raised internally only; five delivery controls answer the Steadfast Life failures. Drafted for Renzo to send: `04-aaron-brief.md` (Koncept, Alex/DA incl. PM cover, call plan + qualifying questions) and `05-technical-questions.md` (Velvetech Zoom Contact Center; Creatio tech Snowflake ≤5 min). Next: Aaron's call → workshop 1 early Dec.

- **16 Nov: plugin 0.21.0 published** (tag v0.21.0 = 386ae3f): chat section rule, UI kit standard v0.4, **DECK-STANDARD v0.5** (no title kickers, card agenda, owners and minutes in the notes; log §4 item 98). Navalo meeting 2 reviewed (item 96): next = RFP criteria ~Wed 18 Nov.

- **16 Nov: Abbe first-meeting pack** (§4 item 97): `deals/abbe-rh/`. Build plan v2 approved, stand `11014981-demo` (clio `abbe`) registered, approval pack confirmed 16 Nov; deck rebuilt on DECK-STANDARD v0.5. Next: start the build session "Abbe 02 · Build" (pre-flight, restore point, day-1 voice test on the iPhone mirrored to the Mac); Ayush sends the success-criteria email (`01-fm-prep.md` Output 5) with `05-ae-brief.html`; meeting time, format and attendees TBC. Voice: browser call from the phone, voice captures and a text step drafts; runbook + 29-failure research + proof gates G1–G6 in `06-voice-agent-runbook.md` (go/stop Fri 20 Nov).

- **16 Nov: customer chats grouped and numbered** (§4 item 95): rule in `CLAUDE.md` ("Customer chats"); `00-chats.md` in 11 deal folders, 17 chats renamed into 9 new + 2 existing sections. Sections rule **published in plugin 0.21.0** (16 Nov, tag v0.21.0, commit 386ae3f; also carries deck standard v0.5 + UI kit v0.4). To do: Renzo pushes `apac-sc-motion` with tags; trial the numbering on 2–3 deals this week, then add numbering to the plugin.

- **16 Nov: second machine (Mac)** (§4 item 94): workspace + plugin are git repos for GitHub `anzcreatio`. Workspace pushed to `anzcreatio/ai-sales-motion` 16 Nov. To do: Renzo pushes `apac-sc-motion` himself (`git push -u origin main --tags`; Claude's push was blocked by auto mode), then Mac setup per `_mac-setup/MAC-SETUP.md`.

- **15 Nov: Navalo performance page + labUiKit 0.5.0 (no-code pickers) live on 11014108** (§4 item 89). To do: open the pickers in the designer; Renzo pushes the kit; page into the menu after Monday.

- **17 Nov: East West go-live tested with real logins** (§4 items 103–104, 120): 6 logins live; unit and Dodong tests pass; gaps fixed on 11014930 (units see only Pain Point Discovery, rules read-only for units, stage bar for leads only). Cards checked by Renzo and fixed 17 Nov. Ready to open; optional full Send dry run. Report `deals/east-west-bank-rh/12-go-live-test-report.md`.

- **14 Nov: `sc-desk` built** (log §4 item 101): commitments ledger, stall checks, daily brief (8 am task on Renzo's PC), weekly desk view, load check; plugin commit 3ccc007 for 0.20.0, unpublished. Privacy (log items 102, 105): desk briefs, coaching and training results stay on each SC's PC; skill feedback global; no per-person scores. **0.20.0 published 15 Nov 2026** (3be2868, tag v0.20.0). Open: Renzo picks commitments to capture, connects Microsoft 365 if wanted, approves the Friday task prompt update (steps 0b, 1b, learn stats); parked ideas: win/loss debriefs, missed-review nudge, day-before readiness, stand clashes, AE weekly note, claims check, where we win.

- **14 Nov late: Navalo full rehearsal passed, stand reset** (§4 item 87). Portal pages built (not in Monday demo). Pre-Monday fixes a–c done (meeting after 8:30 am; Daniel in the reset, 23 rows). Stand ready.

- **14 Nov: `sc-customer-academy` built** (log §4 item 100): customer enablement on Creatio's public toolkit, 2 tracks, 11 modules pending Renzo's approval; same release.
- **14 Nov: `sc-academy` built** (log §4 item 99), committed for 0.19.0 with sc-coach, unpublished. Open: Renzo reads
  and approves the 9 modules (stamped pending), then releases. Each SC trains on their own stand (Renzo).

- **14 Nov: Navalo broker components BWP1-3 done locally** (labUiKit 0.2.0, `dc6206f`, on GitHub, installed on 11014108 14 Nov but not placed on a page; §4 item 86). Next: BWP4 after the Mon 16 Nov meeting; runbook `Deals/metrics-credit-partners/12-broker-runbook.md`.

- **13 Nov: plugin 0.17.0 and 0.18.0 published** (§4 items 80-81). Requirements seed awaits Renzo's Friday approval. Next build: 0.19.0.

- **13 Nov: FM v0.5 (demo depth first, §4 item 68)** released in 0.17.0.

- **13 Nov: SC click path that teaches the demo (§4 item 71): DONE.** Approved by Renzo; commit d6dcf78 on branch
  `sc-clickpath-descriptive` (worktree `C:\Projects\builds\apac-sc-motion-clickpath`), merged into `release-0.18` by
  the release session. Logins from SharePoint `Stand-logins/stand-logins.json`. Navalo pages in the deal's `clickpath/`.

- **Navalo / Metrics Credit Partners (12 Nov):** new deal `deals/metrics-credit-partners/`. FM v0.3 run on Ayush's BDR intro call
  (~10 Nov, Claudio and Chris, unsecured lending): `00-bdr-transcript-2026-11-10.md`, `01-fm-prep.md`, `deck.json` →
  `02-first-meeting-deck.pptx` (17 slides, rendered, no warnings). Navalo = ex-Payright + BC Invest + Taurus, being merged
  under one brand. Pre-RFP demo: preferred vendor before Christmas. Coverage 3/6, Platform track, BFSI pack. Top pain:
  single view of customer. Light config 4.0 h (customer + Loans 360, application stage bar + product rules table, Creatio.ai
  summary skill, AI missing-docs step). **Update 12 Nov (later):** meeting confirmed Mon 16 Nov; competition assumed
  Salesforce, Microsoft, Zoho, HubSpot; Navalo's overview email saved (`00-customer-email-2026-11-12.md`: CRM + workflow
  + integration/middleware, 9 weighted criteria, 10-business-day RFP response). Deck reworked to it: hypothesis = one view
  of every customer · straight through by the rules (approval limits as data) · every decision on the record; campaigns
  to notes only. Light config still 4.0 h, live change now a T1 limit change. Biggest risk: no AU lending reference
  (their top criterion). Next: build the light config Fri 13 Nov on a stand Renzo names; Renzo's SC check of the deck.
  Process: FM v0.4 / plugin 0.14.1 (website + customer documents as inputs), committed and published 12 Nov.
  **Build stopped 12 Nov (Renzo): new rule, visual build plan approved by the SC before any stand write.** Only the empty
  app shell `Navalo Lending` (package `UsrNavaloApplication`) exists on 11014108. Build plan `03-build-plan.html` from
  `build-plan.json`, rendered by the new `sc-demo-plan/scripts/build_build_plan.py` + `templates/build-plan.html`
  (wireframes from JSON, cheap per deal). v2 same day (Renzo): per scene the customer's verbatim quote, checked by the
  builder against the transcript/email, or a sourced "our idea" blind spot (max 2, after their scenes; Navalo step 8 =
  hardship visible across the three businesses); minutes vs demo slot; differentiator + competitor angle; reuse chip;
  their criteria vs our demo. Plugin 0.15.0 committed (b75db1b) and published 12 Nov; Renzo approved the Navalo plan
  with all 6 recommended decisions.
  **Build on 11014108 (12 Nov, in progress):** package `UsrNavaloApplication`; lookups, objects, example data and 4
  processes built and proven on data (checklist, straight-through/approval with the native Approval element, hardship
  across the group, Lodge). Ids, traps and the reset file are in the deal's `04-build-notes.md` / `04-reset-demo.json`.
  Pages, dashboard, Lodge button and workplace "Navalo lending" (home page `UsrNavaloLendingHomePage`) built by
  the demo-builder agent by ~17:02 12 Nov (confirmed by clio read; not yet seen on screen). DCM case "Application"
  (`UsrCase_7c5a45a`) finished by Renzo; the stage bar shows on applications (checked on screen). The "Navalo
  lending" workplace, application page, Documents tab, home page and policy list were also checked on screen.
  **Done 12 Nov evening:** Navalo customer page `UsrNavaloCustomer_FormPage` opened by a typed Contact page binding
  (contact type "Navalo customer"), so the hospital demo's Contact page is untouched; Account page is clean. All 8
  demo steps rehearsed live and passed; hero records reset (`04-reset-demo.json`); Tom's test approvals deleted.
  **RESUME HERE → `Deals/metrics-credit-partners/05-ux-runbook.md`:** UX pass "from forms to a lending desk",
  WP1–WP10 (plan `05-ux-build-plan.html`, approved by Renzo 12 Nov). **13 Nov: WP1–WP6, WP8, WP9 done and checked in
  the browser** (quick filters, menu order, teal icons and charts; log §4 item 62). WP7 (Awaiting approval as an alternative
  stage) done by Renzo 13 Nov and checked on screen. **WP10 (13 Nov):** all 8 steps passed live, 12 frames in
  `clickpath/shots/`, data reset, new deck `06-demo-deck.pptx` (build slide + 6 screen slides; AI "next time"). Tom's
  rehearsal approval deleted (Renzo's yes); **WP1–WP10 all done**, stand clean. Lodge button now shows only at Ready to lodge (2 page
  business rules, checked on screen). "and campaigns" dropped from the agenda (Renzo, 13 Nov). Left: Renzo's SC check of deck 06.
  **Custom components (13 Nov, APPROVED as recommended; runbook `08-components-runbook.md`; CWP1–CWP4 built and
  tested LOCALLY in `C:\Projects\builds\ui-kit\` (26 tests pass, README there; git, pushed to private GitHub
  `anzcreatio/lab-ui-kit`; 0.1.2 (polished) installed on 11014108 and PLACED on the Navalo customer + application
  pages 13 Nov (Renzo's call, before Monday), verified live on Mia (incl. hardship) / Tom / Aisha; CWP5 done; CWP6
  done on Navalo only (clean-clone rebuild + pull to SharePoint `Library/ui-kit/`, L1; first install on a fresh
  stand still untested, next would be master stand 11011710 with Renzo's yes); CWP7 done 13 Nov (frames 04c/05e/08b,
  deck 06 slides 15/16/19 swapped to component frames, stand reset and read back incl. Tom's approval deleted); CWP8
  done (standard promoted to `apac-sc-motion/standards/UI-KIT-STANDARD-v0.2.md`, log §4 item 64); all CWPs done.
  Open: plugin commit + publish (Renzo; repo also holds EWB's uncommitted 0.16.2), Renzo's SC check of deck 06).
  **Next: application flow (13 Nov, APPROVED, log §4 item 65):** Flow timeline component + native next-step banners,
  ~14 h, runbook `10-flow-runbook.md` (FWP1–FWP7). FWP1 + FWP2 DONE 13 Nov (labUiKit 0.1.3 with Flow timeline, 40 tests,
  GitHub 6941b64); 0.1.5 INSTALLED and Flow timeline PLACED on the application page 13 Nov (Renzo's call); rollback zip 0.1.2 in
  Library/ui-kit; FWP3 DONE 13 Nov (demo morning Mon 16 Nov 8:35–9:51, reset now 19 rows); wording fix in 0.1.5 done;
  FWP5 DONE 13 Nov (4 native next-step banners + 8 page rules, tabs Documents-first); FWP6 DONE 13 Nov (rehearsed,
  deck 06 slides 16 + 18 updated, stand reset and read back); FWP7 DONE (library 0.1.5, standard v0.3, log §4 item 66). All FWPs done. Open: Renzo's SC check of
  deck 06 (slides 15, 16, 18, 19 changed), plugin publish, merging main into ewb-components before any EWB install. Deal dates set (call 10 Nov BDR, SC 12 Nov,
  demo 16 Nov planned; mark done after Monday); Bank.AI log started (10 lines, 0 gaps, `bank-ai.json`; update after
  the 16 Nov meeting with any new requirements):**
  **14 Nov:** PC now on Sydney time (UTC+11); demo morning re-seeded in Sydney time (consent 7:05) and reset
  updated; 16 other applications' dates spread and "Verified" docs → Received; approval banner text fixed. Australian date
  format set on the Supervisor profile (16/11/2026). Next plan:
  `11-broker-view-build-plan.html` (dealer/broker portal + Stage funnel and Request checklist components + AI, named
  approver, STP KPIs, field history; 36 h; after Monday), APPROVED 14 Nov (log §4 item 84),
  runbook `12-broker-runbook.md`; BWP1–BWP3 (checks, two components locally) can start before Monday, the rest after.
  14 Nov: next-step banners restyled as slim strips; routing incident fixed (log §4 item 85); the 20 stray
  approvals deleted with Renzo's yes. Stand ready for Monday. `07-components-build-plan.html/.json`: two
  reusable no-code components for the shared `labUiKit` (see EWB `06-ui-kit-standard.md`): Group holdings (customer
  across the 3 businesses) and Decision checks (why straight through / needs approval, limit bar). ~20.5 h, build after
  Monday, show at the shortlist demo. Risk raised: Navalo's "configuration over customisation" criterion; label as custom
  development in the RFP. Pre-build answers still open (recorded as assumptions in the runbook). AI parked (Support ticket on Creatio.ai invalid_client).

## 4. Likely next steps

  1. Run W2 v0.2 on the next real call (first live use after the blind-test fixes); run it on SAHE once its meeting happens.
  2. Sign-off with the Sales Director, then pilot readiness: shared Claude project (blockers in
     `CLAUDE-PROJECT-SETUP-v0.1.md` §0), pack owners, baseline metrics, governance asks sent.
  3. Build the harvested demo modules first (incl. M6 demo rules object), then the industry videos.
  4. Still open: official price book; proof points for D3/D4/D5; who answers AI security questions; AI Studio governance
     coverage; agent test-set template; video hosting/tracking tool.
  5. Done earlier (no longer to-do): differentiator catalogue, discovery card, leadership sign-off pack, partner pack.
     The master sandbox stays parked until the modules exist.

## 5. How to work in this folder

- First reply: confirm briefly that you've read this file, then get to the task. Questions go at the top (`CLAUDE.md`).
- Before you claim a fact about a past build, check the deal folder (PROJECT-NOTE.md, build notes) and, if needed,
  the log. This summary may lag behind the live instances.
- **Keep this file short and current.** When a decision is made: add a numbered item to the log §4 (next number) and,
  if it changes how we work, one line here. When a deal moves: update its row above and write the detail in the
  deal folder, not here. When work finishes or a session ends mid-task: update §2 and §3. Aim to keep this file
  under ~200 lines; move anything historical to the log.
