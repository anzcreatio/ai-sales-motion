---
name: ai-twin-password-session
description: "AI Twin on a demo stand needs a username/password session (not Creatio ID), matching user email, and a one-time consent click by the SC"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 7f79a5f5-5b22-4217-91a3-65280bda4c05
  modified: 2026-11-24T21:13:00.588Z
---

The AI Twin panel on a Creatio stand only connects when:
- the browser session uses username/password, not Creatio ID (with Creatio ID, EnsureUser returns 400);
- the user's SysAdminUnit email and contact email equal the SC's AI Studio login;
- the SC clicks the one-time "Connect your Creatio access" consent (OAuth consent, so it's theirs to click).

**Why:** this cost about an hour on the Strata Plan build (25 Nov 2026) before the 1 pm demo.
**How to apply:** for any Twin-led demo, set the emails first, tell the SC to sign in with a password, and fire one test question during the build so consent happens then. Related: [[build-rules-and-bank-ai]].
