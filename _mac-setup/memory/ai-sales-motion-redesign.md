---
name: ai-sales-motion-redesign
description: "Renzo's APAC SC demo-motion redesign — team shape, decisions, process-first rule, working files"
metadata:
  node_type: memory
  type: project
  originSessionId: a5e31f55-5bed-4b24-9e7c-b2d5b5361e1b
  modified: 2026-11-03T12:11:00.605Z
---

Started 2 Nov 2026 in C:\Projects\Workspaces\AI Sales Motion. Goal: streamline SC motion so every interaction shows differentiators, standardise, master sandbox, partner-ready design doc.

- Team: 3 SCs, 8 AEs; SEs are a shared pool, not allocated → SC + Claude build by default, SE = escalation only.
- Differentiators: defined by us. Industries (updated 3 Nov 2026): **BFSI, Manufacturing, General industry**. The motion must be ready for all three (this replaces "Banking first").
- Discovery reality: 30-min calls (max 45), ≤20 min of real discovery; AEs weak at qualifying. The full list of answers is kept current in CONTEXT-HANDOVER.md §4.
- Two presales documents, both pre-contract: customer Solution Proposal (sales, best-practice based) + Partner Handover Pack (enough for the partner to run its own discovery; never a full spec — partners are weak at delivery).
- Pilot locally. **Process first: build nothing until the process is agreed.**
- Working files: CONTEXT-HANDOVER.md (context for another Claude account), SC-MOTION-PROCESS-v0.5.md (draft process; filename tracks the version), TEMPLATE-*.md (BDR card, discovery notes).

- v0.3 (3 Nov 2026) adds two tracks in one motion: P = Platform (CRM / no-code) and A = AI Studio (bundled with Business Studio since 1 May 2026; standalone if necessary), plus P+A. Track A has a stricter go/no-go, an agent test set, a measured pilot, an agent spec and an AI governance pack. The Sales Director sponsors go/no-go.
- The core flow (since v0.2) is hypothesis-led: a BDR forked card (CRM / AI Studio) → AI pre-call pack → one 30-min discovery (≤20 min) → AI-scored go/no-go signed by the SC → "What we heard" one-pager → build from Core + Industry Packs → value demo (L2–L3, validation moments, live change) → Proposal + Partner Pack. Evidence tags: Confirmed / Inferred / Assumed. Each SC owns one pack.
- v0.4 (3 Nov): after mock call 01 (tests/), a tiered go/no-go (Green L3 / Amber 1-day L2 / Red video), a 4+1 hypothesis slide, "send us one thing" as a commitment, and governance pack lite in Phase 1. Built: the 20-min card v0.2, workflows/W1-Pre-Call.md (v0.2, blind-tested on a real bank, tests/w1-test-01), workflows/W2-Post-Call.md, AI-GOVERNANCE-PACK-LITE-v0.1.md. Also: packs/ (INDUSTRY-PACK-TEMPLATE-v0.1, CORE-PACK-v0.1 with 14 hypotheses, 3 journeys, KPI ranges, 8 AI tasks, 7 demo modules; BFSI-PACK-v0.1 and MANUFACTURING-PACK-v0.1 overlays drafted 3 Nov via research agents; manufacturing = use case + coexistence, D5 in every demo (approved by Renzo 3 Nov), CRM assumed to stay; only real deals count as hypothesis hits), DIFFERENTIATOR-CATALOGUE-v0.1.md (D1–D7, core = D1 + D3 + D2 (P) or D5 (A); research in research/). Also: templates/ (Solution Proposal + Partner Handover Pack v0.1) + workflows/W5-Close.md v0.2, blind-tested on the mock; frameworks verified (research/proposal-handover-frameworks). Still open: a real recording test; official price book; proof points for D3/D4/D5; (AI Studio is bundled with Business Studio since 1 May 2026, confirmed by Renzo; track = buyer interest, not licence); who answers the AI security questions; AI Studio governance coverage.

**Why:** today's 7-step SC→SE flow loses context at each handoff and doesn't guarantee differentiators.
**How to apply:** iterate on the process doc; don't touch Creatio stands for this work unless asked.
- 3 Nov 2026: **sign-off candidate**. Process v0.5 + SIGN-OFF-PACK-v0.5.md (8 decisions: pilot baseline, tiered gate, BDR books joint discovery, recording + tool, pack owners, shared Claude project, build only harvested modules first, artefact home) + PILOT-GUIDE.md. Next: Renzo + Sales Director sign-off → pilot readiness → 6-week pilot → v1.0.
- Later 3 Nov: CLAUDE-PROJECT-SETUP-v0.1.md (shared project kit; blockers: Team/Enterprise plan, security OK for transcripts), templates/TEMPLATE-Discovery-Slides-v0.1.pptx (Creatio template; build script in templates/_build/), and workflows/W3-Demo-Design.md v0.2 (blind-tested, tests/mock-01-harbourline/09–11). W3's demo script feeds the demo toolkit's creatio-demo-runbook → creatio-demo-build; W3 must not duplicate the runbook. modules/M6-LIVE-CHANGE-KIT-v0.1.md (design): validation moments answered by T1 value / T2 row changes in one demo rules object per stand; process changes are set pieces only (Scentia timed them at 3–8 min). modules/VIDEO-LIBRARY-PLAN-v0.1.md + templates/TEMPLATE-Red-Followup-Email-v0.1.md: Red deals get a W2-drafted email + 4–6 min industry video; videos need built modules (interim: public Creatio videos); hosting/tracking tool undecided. Sign-off page published: https://claude.ai/artifact/9r67D1pjyW9UaCyVE5eT5y
- 5 Nov 2026: project `CLAUDE.md` added (auto-loads; read order, rules, folder map, tools) and CONTEXT-HANDOVER.md refreshed (§4 items 26–27: W1 v0.3 outbound branch, first real deals SAHE + Perth Radiological in deals/; §5 current status + next steps). Renzo may switch Claude accounts: keep the handover current so the folder alone is enough.
