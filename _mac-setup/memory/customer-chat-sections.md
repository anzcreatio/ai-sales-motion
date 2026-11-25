---
name: customer-chat-sections
description: "Every customer chat gets a row in <deal>/00-chats.md (desk.py chat-open/chat-set), a per-customer sidebar section and title \"<Customer> NN · <Stage> · <topic>\"; rules now in the plugin"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 80355baf-1d7a-44ee-ba73-d0b77af33197
  modified: 2026-11-18T03:24:59.438Z
---

Renzo (16 Nov 2026, extended 18 Nov): group all chats for a customer in their own sidebar section, number them, and track each chat's status, next step and due date so parallel work is visible.

**Why:** he and the other SCs run many chats per deal across a PC and a Mac and lose track. The sidebar is per machine, so the record lives in the deal folder (`00-chats.md`, SharePoint). No master chat: the desk shows open work.

**How to apply:** follow `apac-sc-motion/standards/CHAT-TRACKING-v0.1.md` (loaded by the plugin hook since 0.29.0): `desk.py chat-open` at start, sidebar section + title, `desk.py chat-set --status --next [--due]` at every wrap-up, `desk.py work` for "what's running?". Skip scheduled tasks and motion work. Related: [[questions-first]].
