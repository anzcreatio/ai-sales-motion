---
name: kit-worktree-ownership
description: Never build or edit in a kit worktree another chat owns (C:\Projects\builds\ui-kit-ewb = EWB chat); use your own git worktree
metadata:
  node_type: memory
  type: feedback
  originSessionId: f1b78aec-98b2-4bd3-aeeb-1904b821822a
  modified: 2026-11-18T07:53:58.960Z
---

The EWB chat owns `C:\Projects\builds\ui-kit-ewb` (Renzo's call, 18 Nov 2026). Do kit work in `C:\Projects\builds\ui-kit`
(main) or a new `git worktree`, never in another chat's worktree.

**Why:** on 18 Nov my `ng build` in ui-kit-ewb (after merging main into ewb-components) ran while the EWB chat pushed the
package; its push caught the build mid-write and the live EWB stand (11014930) briefly had no kit JS.

**How to apply:** before building, merging or pushing in any `C:\Projects\builds\*` folder, check whether another live
chat works there (`ListAgents`, the deal's `00-chats.md`); if so, message it or use a separate worktree.
