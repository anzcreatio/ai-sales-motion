---
name: build-rules-and-bank-ai
description: "Ask before compile/restart (try a browser refresh first), check the OData token when calls fail; BFSI deals feed the Bank.AI log"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 64514312-2bbb-43be-a904-304f714b7d9d
  modified: 2026-11-13T03:38:04.038Z
---

Standing rules from Renzo (13 Nov 2026):

0. **Approve upfront, build non-stop (14 Nov):** with the build plan get one approval pack (`build/approval-pack.json`), then build without asking in chat; only the six hard stops pause it (out of scope, shared-stand restart, sign-in he must do, deleting non-demo data, same failure twice, anything to a customer). Restarts pre-approved on our own clean stand only. Log small decisions with defaults. Keep-awake, notify, build report. v0.4: pre-flight with him before he leaves, restore point first, two tries per item then skip and carry on, irreversible choices stop; caps enforced by `approval_pack.py` + autoMode rules.
1. **Compile and restart need his OK** (or the approval pack's). First check whether a browser refresh (or cache clear + refresh) is enough: pages, captions, rules, data, processes and AI prompts usually are. Compile only for schema, C# or script-task changes; restart only if required. Ask with the reason and the downtime.
2. **Calls suddenly failing (401/403, login page instead of JSON)?** Check and refresh the OData token or session first, retry once, then debug.
3. **Rollback plan before custom components or code** (or standard-object / shared-setting changes): back up first, write the undo steps, how to check, and the demo's plan B in the build log. Custom work in its own package.
4. **BFSI deals** (banks, lenders, multi-finance, pawn, securities, insurers): run `sc-bank-ai-log` after each requirement-capturing step. The log (SharePoint `Bank-AI-Requirements`) holds customer requirements in their words + our proposed configuration + fit/gaps only. Never demo quality, meeting reviews, commercials, competitor or people names. The bank's name is fine.

**Why:** unnecessary restarts cost stand time; expired tokens look like real bugs; the Bank.AI team needs clean APAC requirements and gaps to build banking features.

**How to apply:** full text in `apac-sc-motion/standards/BUILD-RULES-v0.4.md` and `skills/sc-bank-ai-log/SKILL.md`. Related: [[build-plan-before-build]], [[ai-sales-motion-redesign]].
