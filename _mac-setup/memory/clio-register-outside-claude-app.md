---
name: clio-register-outside-claude-app
description: clio MCP can read a private MSIX copy of appsettings.json that keeps coming back; check both files BEFORE telling Renzo where to register a stand. Never suggest show-web-app-list
metadata:
  node_type: memory
  type: reference
  originSessionId: 544fdbca-593e-44ea-9983-4cd0614dcb56
  modified: 2026-11-18T07:20:58.435Z
---

On Renzo's PC the Claude desktop app is an MSIX package. Once any process inside it (the clio MCP, Claude's Bash) writes
clio's settings, Windows keeps a private copy at
`AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Local\creatio\clio\appsettings.json`, and the clio MCP and
Bash then read **that copy**, even though they report the real path. Terminals (Start menu or the app's Terminal
panel) write the **real** `AppData\Local\creatio\clio\appsettings.json`. Result: a newly registered stand is invisible
to the MCP (12 Nov 2026 `ewb-pain`; again 13 Nov 2026 `pd-clean`).

**The copy comes back.** It was moved aside on 12 Nov and the app recreated it on 13 Nov (13:03). On 13 Nov a fresh
`reg-web-app` in Windows Terminal also left the real file holding ONLY the new stand (the other 11 lived only in the
copy). Fixed by: back up the real file, copy the app's copy over it, move the copy aside (`.stale-<date>`), then Renzo
re-runs `reg-web-app` in Windows Terminal.

**18 Nov 2026 (stand clean82 = 11014982):** same again: the real file held only clean82, the copy the other 13. Auto mode
blocked Claude's merge twice (even with Renzo's yes in chat), so hand Renzo the merge script to run in Windows Terminal
instead of trying it yourself. The one-line script (backup real → add the real file's Environments into the copy's →
write to real → move copy to `.stale-<date>`) worked: MCP saw all 14 stands straight away, no restart.

**How to apply:** BEFORE telling Renzo where to register, compare both files with Claude's **PowerShell tool**
(it sees the two paths separately; Bash sees the copy for both): size, date, stand names (never print values). If the
copy exists, merge as above first. If `list-environments` misses a stand, same check. Never type the password or run
reg-web-app myself. Never suggest `clio show-web-app-list`: it prints every stand's password in clear text
(`list-environments` masks them).

**20 Nov 2026 (yokogawa-demo = 11015210):** the merge script I gave first used `$r/$R` and `$c/$C`: PowerShell
variables are case-insensitive, so nothing was written. The fixed script worked, but Renzo ran it twice: the second
run found no copy (already moved aside) and wrote a **0-byte** real file. Recovered from the newest `.bak-<stamp>`
(the merged one, 19 stands). Rules: distinct variable names; make the script stop if the copy is missing
(`if(!(Test-Path $copyPath)){"already merged";return}`); after it runs, check sizes and `list-environments` yourself.
