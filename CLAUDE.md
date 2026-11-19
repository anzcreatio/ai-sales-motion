# AI Sales Motion: project instructions for Claude

Renzo Huruiti (SC, Creatio APAC) is redesigning the APAC solution-consulting demo motion with Claude. This folder
holds the whole motion: process, workflows, packs, templates, tests and live deals. The design is done and was put
up for sign-off on 3 Nov 2026. It is now being tried on real deals.

## Read first, in this order
1. `CONTEXT-HANDOVER.md` (short, ~3k tokens): who Renzo is, how he works, where things stand, resume point.
   **Don't read `CONTEXT-HANDOVER-LOG.md` up front** (~26k tokens: toolchain gotchas, past builds, the §4 decision
   log, deal history). Open the section you need when a task calls for it ("§4 item N" elsewhere points there).
2. `SC-MOTION-PROCESS-v0.5.md` (~12k tokens): **only when the task changes the motion or you need a document's current
   version** (§8; if another file disagrees with §8, §8 wins; §15 = changelog). Not needed for deal work through the
   plugin skills.
3. The workflow for the task. **Default since 11 Nov 2026: the plugin repo `apac-sc-motion/`** (team rollout).
   First meeting = skill `apac-sc-motion/skills/sc-first-meeting/SKILL.md` (FM v0.7); decks = `sc-deck` +
   `apac-sc-motion/standards/DECK-STANDARD-v0.6.md` (one `deck.json` per deal). Packs, catalogue and governance pack:
   the copies in `apac-sc-motion/knowledge/` are the ones SCs use, so change them there. The full motion stays for later
   stages: `W1-Pre-Call.md`, `W2-Post-Call.md`, `W3-Demo-Design.md` (deeper demo), `W5-Close.md` (Proposal + Partner Pack).

## How to work with Renzo
- **Challenge him.** Say so when there's a better option or he's heading the wrong way, give the reason, then
  recommend. Agree when he's right. Once he decides, execute without re-arguing.
- **Questions go at the top of every message**, numbered, before any summary or detail ("No questions" if none).
  Renzo may read only the top of a long reply before clicking accept (11 Nov 2026).
- **Before any demo configuration starts** (after the script or plan, before building), ask the three pre-build
  questions at the top of the message, even if you think you know. **Then give the SC a visual build plan**
  (`NN-build-plan.html`: storyboard with screen wireframes, what we'll build and hours, example data, what's not
  built) and **don't touch a stand until the SC approves it** (12 Nov 2026). The three questions: (1) Who is our competition, with names if known?
  (2) Has the customer given us anything else (RFP, requirements, an email, documents)? (3) Anything else we should
  know before we start configuring? Record the answers in the deal's plan.
- **While building** (13–14 Nov 2026, `apac-sc-motion/standards/BUILD-RULES-v0.6.md`): **approve upfront, build
  non-stop.** With the build plan, get one approval pack (`<deal>/build/approval-pack.json`: scope, stand, compiles,
  restarts on our own clean stand, custom code with rollback, auto-rollback, data, decisions log); then build without
  asking in chat, stopping only for the six hard stops (out of scope, shared-stand restart, a sign-in Renzo must do,
  deleting non-demo data, the same failure twice, anything to a customer). Before leaving: pre-flight with Renzo, then a restore
  point; check each item, two tries then skip and carry on; irreversible choices stop. Caps are enforced by
  `sc-demo-plan/scripts/approval_pack.py` and auto-mode rules. Keep the laptop awake, notify at the end, write a build report. Permission allowlist: `.claude/settings.local.json` (loads in a new session). Otherwise: refresh the browser before any
  compile or restart, and **ask Renzo before a compile or restart**, saying why a refresh isn't enough. When calls
  suddenly fail (401/403, a login page instead of JSON), check and refresh the OData token first, then debug.
  **Before any custom component or code** (or a standard-object or shared-setting change): back up first and write a
  rollback plan in the build log (how to undo, how to check, the demo's plan B).
- **Demo depth first** (13 Nov 2026): at the start of every new deal, ask the SC at the top: "introduction to
  Creatio, or a detailed demo on their pains?" Introduction → the plan as it is (light config). Detailed → best-practice
  pains from the pack (tag I), a success-criteria email so the customer ranks them, and a Full demo plan through
  `sc-demo-plan`; guide the SC through it. Rule: `sc-first-meeting` step 0b and rule 7b.
- **Log SC feedback as you go** (13 Nov 2026): when the SC corrects, overrides or rejects an output, or adds a rule,
  write a feedback file in SharePoint `Lessons/feedback/` (about the skills and Claude: shared with everyone; never about how the SC performed. Coaching, meeting self-ratings and training results stay on the SC's own PC and are shared only by their choice; never show one SC another's) (format: `sc-guide` mode C, plus `Source: chat` and the
  skill + step) without asking. At the end of each skill run, ask one short "how did that go?" question. Not for
  practice folders. Full loop: `apac-sc-motion/standards/FEEDBACK-LOOP-v0.2.md` (plugin 0.20.0, §4 items 71b, 102, 105); lessons in a chat of their own: `/sc-lessons`.
- **BFSI deals** (bank, lender, multi-finance, pawn, securities, insurer): after first-meeting prep, RFP fit-gap,
  workshop, demo plan or a meeting with new requirements, run `sc-bank-ai-log`. It writes the customer's requirements
  and our proposed configuration to SharePoint `Bank-AI-Requirements` for the Bank.AI team. Requirements only: no
  demo, meeting, commercial or competitor content.
- **Deal dates on every deal** (13 Nov 2026): `<deal>/deal-dates.json` holds when the first call happened (BDR, AE or
  discovery), when the SC got the transcript, and when the demo is (planned, then done). Use
  `apac-sc-motion/skills/sc-guide/scripts/deal_dates.py` (`show`, `set`, `stats`). Take dates from the handoff or the
  transcript; ask at the top only for the missing ones; never guess.
- **Customer chats and reply format: in the plugin since 0.29.0** (18 Nov 2026, log §4). `apac-sc-motion/standards/
  CHAT-TRACKING-v0.2.md` (number + row via `desk.py chat-open`, sidebar section per customer, title
  `🟢 <Customer> NN · <Stage> · <topic>`; since 0.33.0 every open chat's title carries 🟢/🟡/🔵, removed on "end chat", log §4 item 149, status/next/due via `desk.py chat-set` at every wrap-up; "what's running?" =
  `desk.py work`; no master chat) and `CHAT-FORMAT-v0.1.md` (❓ questions first with defaults, ⚠️ only for real risk,
  ✅ done, 💡 learn; seven fixed marks). The plugin's SessionStart hook loads both into every session. Not for scheduled tasks
  or motion/plugin work.
- He wants a recommendation, not a menu. Plain Australian English, tables, short steps, no long prose. He types
  fast, so typos are normal.
- **Process first:** don't build Creatio modules or touch Creatio stands for this work unless he asks.
- Never type passwords, register clio environments, create accounts, or open `CREDENTIALS.md` files.
- **Two machines** (16 Nov 2026): Renzo works on a Windows PC and a Mac (separate Claude seats; nothing but this folder
  crosses). This folder and `apac-sc-motion/` are private git repos on GitHub `anzcreatio`. At the start of a session
  `git pull` both; before stopping, update the handover §3. A **SessionEnd hook** (`.claude/hooks/session_end_sync.py`,
  in `settings.local.json`) then commits only the two handover files and pushes committed work in both repos; it skips
  demo-build chats. Claude itself still may not `git push` (deny rule); commit other files yourself or leave them to Renzo. One machine per deal at a time
  (deals are on OneDrive). Publish the plugin and run scheduled tasks on the PC only. Setup: `_mac-setup/MAC-SETUP.md`.

## Folder map
| Path | What |
|---|---|
| `SC-MOTION-PROCESS-v0.5.md`, `SIGN-OFF-PACK-v0.5.md`, `PILOT-GUIDE.md` | Process, sign-off decisions, one-page guide |
| `workflows/` | W1, W2, W3, W5: instructions Claude follows |
| `packs/` | Core + BFSI + Manufacturing industry packs (hypotheses, journeys, KPIs) |
| `DIFFERENTIATOR-CATALOGUE-v0.1.md` | D1–D7. All claims and proof points come only from here |
| `AI-GOVERNANCE-PACK-LITE-v0.1.md` | All AI, data, hosting and security answers come only from its "can say" lines |
| `TEMPLATE-*.md`, `templates/` | BDR card, discovery card, slides, proposal, partner pack, Red follow-up email |
| `templates/_build/build_first_meeting_slides.py` | Builds the FM playback + hypothesis slides from a deal's `slides-fm.json` |
| `templates/_build/build_hypothesis_slides.py` | Builds the discovery slides from a deal's `slides-data.json` (needs Python + `python-pptx`) |
| `modules/` | M6 live-change kit, video library plan (designs; nothing built yet) |
| `deals/<account>/` | Real deals. Numbered outputs: `01-W1-pre-call-pack.md`, `02-discovery-slides.pptx`, `03-discovery-card.md`, … **Since 11 Nov 2026 the deals live on the shared SharePoint site** (`APAC Solution Consulting`, library Documents → `Deals`), synced on Renzo's PC to `C:\Users\r.huruiti\OneDrive - Creatio\APAC Solution Consulting - Documents\Deals`. `deals` in this folder is a link to that path (on the Mac: the `~/Library/CloudStorage/...` path in `~/.apac-sc-motion.json`; not in git). Old local copy: `_deals-local-backup-2026-11-11` (don't use; delete after a week) |
| SharePoint `_inbox`, `Slide-library`, `Lessons` | New corporate templates/content dropped by anyone · approved reusable slides · weekly lessons digests |
| `apac-sc-motion/` | **Plugin repo for the SC team (git; published to SharePoint `Plugin/apac-sc-motion` with `publish.ps1`; installed as `apac-sc-motion@apac-sc`):** skills, standards, templates, knowledge, demo library, lessons. Rollout plan: Phase 0 done 11 Nov (repo + deck builder); 1 `sc-demo-plan`; 2 library + `sc-harvest`; 3 click path + `sc-meeting-review` + weekly lessons; 4 onboard SCs. Test any change with `tests/deck/sample-fictional` |
| `tests/` | Blind tests with inputs, outputs and reviews. Use them to check a workflow after you change it |
| `research/` | Source research behind the packs and catalogue (dated 3 Nov 2026) |
| `CLAUDE-PROJECT-SETUP-v0.1.md` | Kit for the claude.ai shared project that AEs use for W1 + W2 |
| `_archive/` | Superseded files. Don't use |

## Conventions
- **The file name carries the version.** When you change a file materially, bump `vX.Y` in the name, update every
  reference to it (process §8 above all), and add a line to the process §15 changelog.
- Evidence tags in every output: **C** Confirmed · **I** Inferred · **A** Assumed. Every research fact gets a source
  and a date. Keep numbers in their exact unit.
- **Word documents use the Creatio look** (18 Nov 2026, Renzo): every Word document in the motion, customer or
  internal, is built with the doc kit per `apac-sc-motion/standards/DOC-STANDARD-v0.1.md` (logo, orange cover band,
  Montserrat headings, navy tables, estimates shaded, status in the footer), exported to PDF through Word, every page checked.
- **No "SC check" warning lines** (17 Nov 2026, Renzo): never add "SC check required before this is used with the
  customer." or any similar line to anything you generate (docs, emails, decks, notes, HTML, scripts). The SC still
  reviews everything before it reaches a customer and Claude never sends; the line itself is gone.
- New deal: create `deals/<kebab-case-account>-<initials>/` (`rh` Renzo, `wn` Willy, `fa` Ferdhi; from `"sc"` in
  `~/.apac-sc-motion.json`) and number the files in workflow order. Suffix on the deal folder only; one folder per
  account (reuse it whatever its suffix); never rename. Folders made before 12 Nov 2026 have no suffix. Rule: `sc-setup`.
- **Never put `node_modules`, build caches (`.angular`, `dist`) or videos in a deal folder**: it is synced to every SC.
  Custom-component workspaces live in `C:\Projects\builds\<account>\`; only their source and a README go in the deal folder.
- When a decision is made or work is finished, add the decision to `CONTEXT-HANDOVER-LOG.md` §4 (next number: re-read
  the last item number right before you write, in the same step, because parallel chats write here too; items 99–106
  were renumbered on 16 Nov after three chats reused 87–93) and
  **Adding to an existing log item later:** edit that item's own line in place (re-read the file right before writing); never append text at the end of the file, because parallel chats rewrite the end (18 Nov 2026: additions to item 144 were lost that way). update `CONTEXT-HANDOVER.md` §2–§3 (status, resume point; keep it short, deal detail goes in the deal folder), so any
  Claude account, on any machine, can continue from this folder alone.

## Tools this project needs
- Web search (W1 stops without it).
- Python 3 + `python-pptx` for the slide build script.
- For W3/W4 only: the `creatio-demo-toolkit` plugin (`creatio-demo-runbook` → `creatio-demo-build`) and clio.
  These are installed per user. Check they're present before running W3.
