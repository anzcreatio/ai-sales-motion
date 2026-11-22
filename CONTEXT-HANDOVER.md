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
| Navalo / Metrics Credit Partners | `metrics-credit-partners` | **RFP received 18 Nov, fit-gapped** (`rfp/`, log §4 item 147): must-have fit 95%, **Bid with conditions**; 28 clarification questions in `rfp/06` ready to send (due ~Wed 25 Nov, A; intent ~Mon 23 Nov; response ~Wed 2 Dec). Next: Renzo confirms dates and sends questions; AE: AU lending references, partner, Creatio legal; then `sc-demo-plan` (proof mode) from `rfp/05-poc-brief.md` once journeys arrive. Sprint = no-code only. Stand `11014108` |
| East West Bank (PH) | `east-west-bank-rh` | Plan v5 (47 h) **approved 12 Nov; Phase 1 build in progress on `11014930-demo` (clio `ewb-pain`)**. Done 13 Nov: prefix `lab`, cliogate, CrtProcessBuilder; packages `labPainDiscovery` / `labUiKit` / `labPainDiscoveryEwb`; full `labPd*` object model; live score view `labPdCardTotal`; stage bar (DCM via import-schema); guard process; module + EastWest seed (6 cards, 25 steps); roles + record rights; UI kit 0.2.0 (5 components, branch `ewb-components` in `C:\Projects\builds\ui-kit-ewb`) installed; card page, board, cards list, scoring rules, units' home, leads workplace, configurable "How this works" help panels on every page — all re-checked on screen 13 Nov after the restart (board fix: unscored cards off the plot, kit `c66150e`). **Reusable module (13 Nov, Renzo "Start now")**: module exports cleanly with no SQL view and no East West wording (customer wording via replacing pages + instruction "Replaces"); scale, board axes, stage rule, all kit text configurable; kit 0.3.0 `d9fcbf8`. Unit rights on new cards automated (script task, compiled 13 Nov). Clean-install test passed on `pd-clean` (11014933-demo); one manual step (record permissions on cards). Install guide `09-module-install-guide.md`. Tested on 3 other use cases (bank AI portfolio, RFP fit-gap at 300, manufacturing quality): all work; board now merges bubbles at volume (kit 0.3.1). **Programmes (14 Nov, kit 0.4.0):** several use cases on one stand, default programme from a system setting. Limits: axis names and stages shared across programmes, scales ≤5. Log rows 60–87. **UI polish (14 Nov, kit 0.5.1):** short card titles + quotes, slim help, visual system, card tiles home; brand step waits for EWB's logo. Plan `10-polish-plan.html`, rows 89–94. **Resume: `Deals/east-west-bank-rh/08-build-log.md` "Resume here"**. Logins 24 Nov, session 27 Nov or early week of 30 Nov |
| Abbe (packaging, AU) | `abbe-rh` | AE intro 11 Nov (Ayush ↔ Will Purcell, data and AI). **Detailed first demo Tue 1 Dec**: voice visit recap → right Kiwi account and fields → Monday (simulated). Deck 02 built; build plan 03 v3 (11 steps, 30.5 h; Will ranked the pains by email 17 Nov: new-customer step added) **approved 16–17 Nov**; AE brief 05. Waiting on: clean stand (Renzo requesting), then approval pack + day-1 voice test on iPhone via Mac (log §4 item 97) |
| IQumulate (premium funder, Steadfast Group) | `iqumulate-rh` | Discovery + generic demo 22 Oct (AE Aaron + Koncept). **Biggest risk: Koncept did Steadfast Life (went badly); Wai-Lum spoke to its CEO and now fears implementation cost.** Plan: guided workshop 1 in Melbourne (broker quote follow-up) → journey built for workshop 2 → phased roadmap + fixed phase 1. **Decided 16 Nov: customer-led backed by Delivery Assurance** (maybe a different partner for bounded pieces); five delivery controls answer the Steadfast Life failures (log item 114); budget cycle Apr 2027. Next: Aaron gets Steadfast Life facts + Delivery Assurance scope + 12 Nov call notes, handles Koncept, calls Wai-Lum, sends `workshop/w1-00-invite-email.md` (log §4 item 107) |
| MartinJenkins (NZ consulting) | `martinjenkins-rh` | Advisor recommends separate ERP + CRM: now CRM vs CRM (log §4 items 112, 118). Next: Aaron calls Hannah (`07-aaron-call-brief.md`), then email 04 v0.2 + one-pager 06 (PDF) asking for a 2-h session on 3 adoption tests. Drafts await Renzo's SC check + 4 [TBC] |
| FirstCape (NZ wealth) | `firstcape-rh` | AE intro 18 Nov (Ayush ↔ Dawie Olivier, transformation; Microsoft + FNZ + InvestCloud). Asked for a written comparison, no further work. Sent to Ayush 18 Nov: Renzo's `Creatio Comparison Analysis v2` (PDF, "both can build it, the difference is how") + email `03-ae-email-sent-to-ayush-2026-11-18.md`. Next: Ayush sends; Deal Desk break-even + tenancy options (may need FirstCape inputs); qualify on what JBWere advisers use. Build nothing until Dawie names a gap. **Hard-sell lesson** `apac-sc-motion/lessons/2026-11-18-firstcape.md`: no reply by Wed 2 Dec 2026 = record "didn't work" (Renzo) |
| Scentia | `scentia` | Phase 1 + client separation built on `11014147-2-demo`; not yet tested as real users |
| Telkomsel | `telkomsel` | Meeting 12 Nov (Deloitte-led). Next: re-run FM on the meeting transcript, then the light config they pick |
| Suntory Oceania | `suntory-oceania` | Demo held 11 Nov; Andrew re-engages late Jan; send slides PDF + FMCG stories |
| Hardware & General | `hardware-and-general` | Built on `11011710-demo`; deck 07 and click path await SC check; waiting on Geoffrey's document |
| SAHE | `southern-academy-of-higher-education` | First meeting moved (TBC); keep-warm email approved, needs dates + AE name |

## 3. Resume here
- **20 Nov: build chats (§4 item 162), PAUSED.** Done + committed, not published. **Next:** Renzo runs `sc-academy` A3 from the repo copy (starter message in the motion chat 'creatio-instructions-mcp Confluence VPN'; training stand: decide, default `test-stand` 11015172; his set-up folder = `AI Sales Motion`), then fix the module, stamp A3 `--by "Renzo Huruiti"`, publish (blocked until the morning-brief chat commits its `sc-desk` work), re-check A3 Part 3 (wrong-folder hook) on the installed plugin, share the team page with Willy and Ferdhi. Willy: change the BPD sandbox password, close the debug Chrome.
- **20 Nov: toolkit notes auto-refresh + AI app dev toolkit check in `sc-setup`** (§4 item 161): committed under `## Unreleased`, **not published**. To do: "publish the plugin"; Willy/Ferdhi run `sc-setup` to install the R&D toolkit.
- **19 Nov: GenLife proof build done on 11015170** (§4 item 160; `deals/genlife-rh/09-proof-pack/`, build report `build/build-report.md`): all 8 steps proven (dup on save, name + DOB, adviser code, rules on every channel no code, export history, live change, listener block). Stand left clean for the live call with Tim (rules inactive). To do: Renzo reviews the pack and sends it; Claude never sends.
- **19 Nov: release flow** (§4 item 159): plugin changes go under `## Unreleased`; "publish the plugin" runs `publish.ps1` (picks the version). Queue: `apac-sc-motion/RELEASE-QUEUE.md`. Mac: add `plugin_repo` to `~/.apac-sc-motion.json`. Kit side: Scentia chat.
- **19 Nov: tool routing v0.1, plugin 0.36.1** (§4 items 157, 158; **published 19 Nov, tag v0.36.1**, with `UI-KIT-STANDARD-v0.7` rename). Release owners: plugin = motion chat, UI kit = Scentia chat (CLAUDE.md). Open: auto-refresh of toolkit notes + AI app dev toolkit check in `sc-setup` (awaiting Renzo's yes); kit 0.8.4 version integrity (Scentia chat).
- **19 Nov: build rules v0.8 §7 mobile pages, plugin 0.36.0** (§4 item 156; **published 19 Nov, tag v0.36.0**, includes 0.35.1). Renzo's PC updated; toolkit notes block refreshed (rules 1–10).
- **19 Nov: build rules v0.7 from Creatio Confluence, plugin 0.35.0** (§4 item 153; **published 19 Nov, tag v0.35.0**): `BUILD-RULES-v0.7` §6 configuration quality + toolkit notes rule 9; research `research/CONFLUENCE-BEST-PRACTICE-2026-11-19.md`. `creatio-instructions-mcp` ships in the plugin's `.mcp.json` (VPN only); Renzo's PC updated, hand-added copy removed, plugin copy connected; plugin repo's own `.mcp.json` disabled in its `.claude/settings.local.json`. No Atlassian MCP (Renzo). To do: Renzo sends `research/TOOLKIT-FEEDBACK-confluence-2026-11-19.md` to the toolkit owners.
- **18 Nov: UI kit 0.6.4 + plugin 0.32.5 published** (§4 item 148; tag v0.32.5): kit zip in SharePoint `Library/ui-kit/packages/`, `main` = `ewb-components` = 0.6.4. Both pushed with tags 18 Nov.
- **19 Nov: channels showcase phase 1 built + install test PASSED** (§4 items 143, 145, 146, 152): build 11014983, clean install 11014993 OK. `Library/channels-showcase/` (plan, build-report, shots), source `C:\Projectsuilds\channels-showcase`. 19 Nov later: relay LIVE (channels-relay.apac-sc-demos.workers.dev, core-system check succeeds), Telegram LIVE (AI answers from indexed KB, hands over on the first request). 19-20 Nov: social comments LIVE via relay (OAuth + DataService; app runs as Supervisor on the demo stand) with AI triage (labSocialTriage) -> rule -> case; support ticket sent (webhook key + technical-user rights). Next: Meta set-up (Page + dev app -> relay), click path, publish plugin; Twilio parked; then B4 live comments, B7 AI triage, B8 channels, phase 2 campaign WhatsApp, phase 3 custom campaign element. In library catalogue as L2 (19 Nov, plugin a4a43b6, not yet published); L3 after live channels + AI triage.

- **19 Nov: UI kit standard v0.6, plugin 0.32.4** (§4 items 139–140; **published 19 Nov, tag v0.32.4**): §2d = rules from all 37 Freedom UI Academy front-end pages, §2e = lessons from 40 Community forum threads, both checked against the kit. EWB kit 0.6.1 live on 11014930 (19 Nov). **Kit `main` = 0.6.2** (`c92cebc`, not pushed): `ewb-components` fast-forwarded in, then the §2d/§2e to-dos done (choice-picker default + clear with null, panel errors visible, versions pinned, canSave/canDelete before writes, Stage funnel server-side counts); 116 tests; installed and rehearsed on clean82 only (counts match 104; test page deleted). Left: i18n (before a non-English customer); EWB stand gets 0.6.2 only with Renzo's yes and a heads-up to the EWB chat; zoneless test on a 10.2 stand before any customer stand goes to 10.2.1.

- **18 Nov: DOC-STANDARD v0.1** (§4 item 136; plugin 0.32.3 `a7bd1b2`, not published): every Word document uses the Creatio look via `standards/doc-kit/creatio_doc.py`; PDF through Word. To do: Renzo runs `publish.ps1`.

- **18 Nov: native Freedom UI patterns → UI kit standard v0.5, plugin 0.32.2** (§4 item 135; not committed or published): §2c tokens, component looks and schema conventions from clean stand 11014982; kit `_kit-tokens.scss` now chains to Creatio's `--crt-*` tokens Committed (plugin `80995ab` + rehearsal note; kit 0.5.5 `6ab9ace` + track/focus fix). clio sees 11014982 as `clean82`. Kit 0.5.5 installed and rehearsed on clean82 (Stage funnel matches native; test page deleted). To do: publish 0.32.2; merge kit `main` into `ewb-components` before the next EWB install; check status colours in real dark mode before a customer uses it.

- **18 Nov: learning loop pilot, plugin 0.32.0** (§4 item 133; **published 18 Nov, tag v0.32.0**): `sc-ready` readiness check (quiz first), call it first in FM v0.7 + demo plan, 💡 Learn points (CHAT-FORMAT v0.2). On for Renzo only (`pilot` in `~/.apac-sc-motion.json`). To do: run `claude plugin update apac-sc-motion@apac-sc`, new session; first real run: `am I ready for insignia-financial-rh?` (demo Thu 19 Nov); review 2 Dec with `ready.py stats`.

- **18 Nov: Agrobank on-prem sizing** (§4 item 132; `deals/agrobank-fa/03-sizing*`): merged with Ferdhi's sizing + TCS answers (per-year hardware, portal inferred 2,000); drafts in `03-sizing-notes.md`; Ferdhi takes over via `04-handover-ferdhi.md`. **After Sergey replies (Renzo, 18 Nov): sc-sizing 0.33.0**: per-year hardware, Inputs sheet with I/A highlighted, storage from customer volumes + backup policy/audit log, bill of quantities + thresholds sheets, general RFI template filler (from `agrobank-fa/sizing/build_template.py`); `SIZING-RULES-v0.2` (MS SQL for HA, OpenShift wording, existing services, portal inference, named=online, mailboxes 50%, DR kind, squeeze only if Sergey confirms); checks (FT+PG, 'likely', missing RabbitMQ/MongoDB, unexplained I/A); SKILL.md notes. Full list: `Lessons/feedback/2026-11-18-renzo-huruiti-sizing-methods-to-adopt.md` (16 methods) + `…-sizing-partner-doc-checks.md` + `…-sizing-infer-and-highlight.md` + `…-sizing-no-openshift-mssql-ha.md` + `…-sizing-branded-customer-doc.md` (branded customer doc + PDF from `agrobank-fa/sizing/build_doc.py`). Test: rerun Agrobank, match the merged figures. Tender due Thu 19 Nov. To do: Ferdhi sends the Sergey note today (MS SQL Always On, Kubernetes on Debian 12, no OpenShift), apply his review, then reply to TCS; commit + publish the `sizing.py` decimal-disk fix (uncommitted in `apac-sc-motion`).

- **18 Nov: BPD Bali POC Day 1 reviewed (Willy's deal, `deals/bpd-bali-wn/`)**: review `02-meeting-review-2026-11-18.md` (16 asked-not-seen items G1–G16), overnight plan `03-overnight-build-plan.html` (Tier 1 B1–B8, 15 h; Tier 2 parked), Bank.AI 18 lines. Handed to Willy (he has the stand and clio): `04-handover-to-willy.md`; his Claude approves, builds and runs Day 2 (19 Nov 09:15 WITA).

- **18 Nov: sizing-only deal entry, plugin 0.31.0** (§4 item 131; **published 18 Nov, tag v0.31.0**): `sizing.py start` creates/reuses the deal folder for partner-led deals that only need a sizing; chat stage `Sizing`.

- **18 Nov: on-prem sizing skill `sc-sizing`, plugin 0.30.0** (§4 item 130; **published 18 Nov, tag v0.30.0**): calculator live + rules R1–R31 from Academy and Sergey; customer `.docx`/`.xlsx` worded as pending infra review. To do: Sergey reviews `SIZING-RULES-v0.1.json` once; recover the POC app/DB image from his 15 Jul email; settle the AI licence conflict (Freedom vs Accelerate).

- **18 Nov: chat format + open-work tracking, plugin 0.29.0** (§4 item 129; `79b9c93` + `0cf54c8`, not published): `CHAT-FORMAT-v0.1` (❓ first, six marks) and `CHAT-TRACKING-v0.1` (`00-chats.md` Status/Next/Due, `desk.py chat-open | chat-set | work`, Desk sidebar section, no master chat) load into every session via the plugin hook. **Release bundled 18 Nov** (`265395f`): 0.27.0 + 0.28.0 (slide types, cover) + 0.29.0 → one changelog entry, plugin.json 0.29.0, tree clean. Older chats' statuses set (9 open). To do: Renzo runs `publish.ps1`; in a fresh session check the format applies.

- **18 Nov: new visual slide types proposed** (§4 item 128): 9 types in the creatio.com style, mock-ups on https://claude.ai/artifact/Fv5a9SYA5PYBqDqh1RA4Hi. Built: 8 types (not the values tiles), DECK-STANDARD v0.6, **published in plugin 0.29.0 (18 Nov, tag v0.29.0)**. To do: brand photos for `photo_cards`.

- **18 Nov: Scentia install guide** (`deals/scentia/12-customer-toolkit-install.md`): one prompt for Windows and Mac, site `11014147-demo`, connection `scentia`; `13-…-windows.md` superseded. To do: Renzo sends it to the builders.

- **18 Nov: FirstCape intro reviewed** (§4 item 127): no FM pack, by the customer's "no further work". Deck `05-comparison-deck.pptx` + email `03` await Renzo, then Ayush sends. No build until Dawie names a gap.

- **17 Nov: no "SC check required" lines** (§4 item 126; plugin 0.27.0, unpublished): rule in CLAUDE.md; stripped from plugin, templates, Slide-library and Renzo's deals. All deal folders clean (incl. `-wn` / `-fa`, 18 Nov). To do: Renzo commits `CLAUDE.md` + publishes 0.27.0 (until then the installed builder still adds the line).

- **17 Nov: customer self-install guides in plugin 0.26.0** (§4 item 125; `ff1f76f`, unpublished): `sc-customer-academy` F0 → `F0-install-windows.md` / `F0-install-mac.md`. To do: test each on a clean machine; Renzo publishes.

- **17 Nov: AI coding agent explainer in the Slide-library** (§4 item 124): `Slide-library/ai-coding-agent-explainer-2026-11.pptx` (5 slides, generic), source `Deals/_examples/ai-coding-toolkit-explainer/`. Announced in plugin 0.26.0 (published 17 Nov). To do: Renzo posts the Teams draft and pushes the plugin repo with tags; optional fictional public-toolkit build for request → plan → page screens; needs a clean stand.

- **17 Nov: BAF AI architecture v0.2** (§4 item 122): `deals/baf/` slide + page. On-prem Business Studio → secure gateway → AI Studio (governance) → LLM; on-prem microservice dropped. To do: confirm gateway date, AI Studio region for Indonesia, sources for cost caps + redaction; ask BAF IT about the gateway.

- **16 Nov: `sc-bom` published in plugin 0.25.0** (§4 item 116; tag v0.25.0 = d0976d7, merged to `main`): which licences a deal needs (SKUs, candidate tier, extras, gotchas, sizing questions; no prices, no users). Catalogue `knowledge/BOM-CATALOGUE-v0.1.json` (that's the "untracked" file in item 115). To do: Renzo pushes `apac-sc-motion` with tags; first real run on Navalo once the RFP criteria land; Deal Desk to close OPEN-1 to OPEN-4.

- **16 Nov: EDB + plugin 0.24.0 published** (§4 item 115): `deals/edb-rh/` (existing customer, session Tue 17 Nov, deck `02-session-deck-2026-11-17.pptx`). Plugin 0.24.0 published (also ships 0.22.0 Delivery Assurance and 0.23.0 master stands): confidential terms, existing-customer path (`sc-guide` mode D), roadmap owners. Open: EDB's five archetype names for `confidential.json` (ask Renzo); the untracked `apac-sc-motion/knowledge/BOM-CATALOGUE-v0.1.json` belongs to another chat.

- **16 Nov: build on top of master stands** (§4 item 109): demo bar v0.3 §6c, build rules v0.5, register `apac-sc-motion/library/stands.json` (first master `11011710-demo`, H&G layer off first; `11013904-demo` off limits). Plugin 0.23.0 committed, not published. Next: register Renzo's new clean sandboxes as masters (names + industries), then publish.

- **16 Nov: Delivery Assurance knowledge** (§4 items 108, 110): `apac-sc-motion/knowledge/DELIVERY-ASSURANCE-v0.2.md` (internal; owner Alex Klochkov; no prices in any output, chat only with a warning). Hooked into first meeting, deck, workshop, meeting review, RFP, W5. Plugin 0.22.0 (not published). Open: currency; consider DA in the IQumulate delivery model.

- **16 Nov: IQumulate** (§4 items 107, 111, 114): `deals/iqumulate-rh/`. Decided: customer-led backed by Delivery Assurance (package #2 recommended, confirm with Alex Klochkov); strong PM raised internally only; five delivery controls answer the Steadfast Life failures. Drafted for Renzo to send: `04-aaron-brief.md` (Koncept, Alex/DA incl. PM cover, call plan + qualifying questions) and `05-technical-questions.md` (Velvetech Zoom Contact Center; Creatio tech Snowflake ≤5 min). **17 Nov (item 123):** NDA not signed; next = 90-min implementation options session (`06-options-session-plan.md`), journey workshop only after he picks an option. Renzo to send `05` today; then Claude drafts the options one-pager with effort ranges.

- **16 Nov: plugin 0.21.0 published** (tag v0.21.0 = 386ae3f): chat section rule, UI kit standard v0.4, **DECK-STANDARD v0.5** (no title kickers, card agenda, owners and minutes in the notes; log §4 item 98). Navalo meeting 2 reviewed (item 96): next = RFP criteria ~Wed 18 Nov.

- **16 Nov: Abbe first-meeting pack** (§4 item 97): `deals/abbe-rh/`. Build plan v2 approved, stand `11014981-demo` (clio `abbe`) registered, approval pack confirmed 16 Nov; deck rebuilt on DECK-STANDARD v0.5. Next: start the build session "Abbe 02 · Build" (pre-flight, restore point, day-1 voice test on the iPhone mirrored to the Mac); Ayush sends the success-criteria email (`01-fm-prep.md` Output 5) with `05-ae-brief.html`; meeting time, format and attendees TBC. Voice: browser call from the phone, voice captures and a text step drafts; runbook + 29-failure research + proof gates G1–G6 in `06-voice-agent-runbook.md` (go/stop Fri 20 Nov).

- **16 Nov: customer chats grouped and numbered** (§4 item 95): rule in `CLAUDE.md` ("Customer chats"); `00-chats.md` in 11 deal folders, 17 chats renamed into 9 new + 2 existing sections. Sections rule **published in plugin 0.21.0** (16 Nov, tag v0.21.0, commit 386ae3f; also carries deck standard v0.5 + UI kit v0.4). To do: Renzo pushes `apac-sc-motion` with tags; trial the numbering on 2–3 deals this week, then add numbering to the plugin.

- **16 Nov: second machine (Mac)** (§4 item 94): workspace + plugin are git repos for GitHub `anzcreatio`. Workspace pushed to `anzcreatio/ai-sales-motion` 16 Nov. To do: Renzo pushes `apac-sc-motion` himself (`git push -u origin main --tags`; Claude's push was blocked by auto mode), then Mac setup per `_mac-setup/MAC-SETUP.md`.

- **15 Nov: Navalo performance page + labUiKit 0.5.0 (no-code pickers) live on 11014108** (§4 item 89). To do: open the pickers in the designer; Renzo pushes the kit; page into the menu after Monday.

- **17 Nov: East West go-live tested with real logins** (§4 items 103–104, 120): 6 logins live; unit and Dodong tests pass; gaps fixed on 11014930 (units see only Pain Point Discovery, rules read-only for units, stage bar for leads only). Cards checked by Renzo and fixed 17 Nov. Full re-run 17 Nov (§4 item 121): home tile fixed in kit 0.5.3 (counts sent cards, own unit only); EWB logins land on a new Pain Point Discovery desktop; all 6 logins checked 18 Nov. E2E browser run 18 Nov: H6 fixed (card title + auto unit), H7 accepted. Kit 0.5.6 installed 18 Nov after a push race broke the stand for 11 min (build log rows 114–115). Kit 0.6.1 live 18 Nov: EWB components aligned to UI kit standard v0.5/v0.6 (native tokens, pickers, skeletons, row caps); regression passed as Marketing, board as Dodong, designer panel as Supervisor (build log rows 116–117). E2E misuse run 18 Nov: H10, H9, E1, H8, F2 found and fixed (kit 0.6.4, board override, card page; build log rows 118–119, `14-e2e-misuse-test.md`). Smoke test on 0.6.4 passed 18 Nov (build log row 121). Ready to send the logins with `13-user-guide.pdf`. This EWB chat owns `ui-kit-ewb`. Then send the logins (G4 accepted 18 Nov) with the user guide `13-user-guide.pdf`; the guide is also linked inside the stand (kit 0.5.4, §4 item 134). Report `deals/east-west-bank-rh/12-go-live-test-report.md`.

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
- **GeoMap (`usr.GeoMap`) released in kit 0.7.0, now in 0.8.x; form page checked on clean82 20 Nov, all pass (log §4 item 144).** Open: release owner reinstalls 0.8.4 on clean82 (my branch push overwrote it); then session timeout back to 60, delete the test page. Handover `C:/Projects/builds/geomap/HANDOVER.md`.
- *(was)* **Parked (Renzo, 18 Nov 2026): generalise the BPD map into a reusable `labUiKit` component after BPD Bali Day 2.** Generic layers (object, lat/long, label, colour-by, owner, date) with BPD values as defaults, picker panel, swap the vendored kit files for the kit's own, move into `lab-ui-kit` in a worktree of its own. Steps: `Deals/bpd-bali-wn/map-sandbox/BPD-MAP-COMPONENT-README.md`.

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
