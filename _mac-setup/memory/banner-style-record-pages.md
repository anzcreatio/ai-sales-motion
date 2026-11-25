---
name: banner-style-record-pages
description: "Renzo prefers demo record pages built as a native banner (key number, route/status, main action) plus live tiles, not plain field forms"
metadata:
  node_type: memory
  type: feedback
  originSessionId: e7b4f015-64c2-4fb6-b864-51725b21add5
  modified: 2026-11-23T03:04:55.139Z
---

For Creatio demo record pages, lead with a native **banner**: navy band with the page's key live number (metric widget), the record name and context, the one main action button, and the business route or status as coloured steps (names read from the record). Follow with a row of live tiles, then the detail cards. Avoid pages that read as "a simple form" (fields in two columns).

**Why:** Renzo, 23 Nov 2026 (Yokogawa limit page): "I do like the look and feel of this because it makes the page more engaging than the simple look we usually have", after several rounds where pages were judged "still a simple form".

**How to apply:** In any demo build plan, design each record page from its purpose and give it a banner-first layout. Build it native (containers, labels, metric widgets, process buttons) so it stays no-code. Keep margins aligned with the page title, no nested bordered containers. A reusable "Approval route" kit component is logged for later in `lab-ui-kit/APPROVAL-ROUTE-IDEA.md`. Related: [[mockups-look-like-creatio]], [[build-plan-before-build]].
