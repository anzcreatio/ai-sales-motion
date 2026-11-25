---
name: no-sc-check-lines
description: "Never add \"SC check required before this is used with the customer.\" (or similar) to anything generated"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 74c4de5f-bd9e-4ef3-8c19-b09d6beb4f06
  modified: 2026-11-17T05:26:51.778Z
---

Never end or stamp any generated content (docs, emails, decks, speaker notes, HTML, scripts) with "SC check required before this is used with the customer." or any similar warning line. Rule since 17 Nov 2026; replaces the old CLAUDE.md convention.

**Why:** Renzo had to delete it by hand before sending, and it could leak to a customer. The SC reviews everything anyway.

**How to apply:** no warning line; keep real approval gates (DRAFT banner until the SC approves) without "SC check" wording. Related: [[customer-slides-labels-not-explanations]].
