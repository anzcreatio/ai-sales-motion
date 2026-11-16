# Mac setup: AI Sales Motion on a second machine (16 Nov 2026)

Renzo works on a Windows PC and a Mac, each with its own Creatio Claude seat. The **folder is the source of truth**:
Claude sessions, memory and artifacts never cross between the two accounts. Decision: `CONTEXT-HANDOVER-LOG.md` §4 item 94.

## Where things live

| What | Home | How the Mac gets it |
|---|---|---|
| Workspace (this repo: CLAUDE.md, handover, process, packs, workflows, tests, research) | GitHub `anzcreatio/ai-sales-motion` (private) | `git clone` |
| Plugin source `apac-sc-motion` | GitHub `anzcreatio/apac-sc-motion` (private) | `git clone` into `apac-sc-motion/` |
| Deals, published plugin, Lessons, Slide-library, Bank-AI-Requirements | SharePoint `APAC Solution Consulting` → Documents | OneDrive sync |
| Global CLAUDE.md, memory, settings | Each machine's `~/.claude` | One-time copy from this folder |

**First-time install from nothing (tools, toolkits, plugins): use `MAC-BOOTSTRAP-PROMPT.md`.** The short prompt below
is for when the repos are already cloned.

## Paste this into Claude on the Mac (after the two clones)

```text
Set this Mac up for my "AI Sales Motion" project. Read ~/Projects/Workspaces/AI Sales Motion/_mac-setup/MAC-SETUP.md and do the "Steps for Claude" section. Don't register clio environments, enter passwords, open CREDENTIALS.md or create scheduled tasks. I do sign-ins myself.
```

## Steps for Renzo (before you paste)
1. Install OneDrive and sign in with your Creatio account. Sync the SharePoint library **APAC Solution Consulting - Documents**
   (Teams/SharePoint → Sync, or "Add shortcut to My files"). Right-click `Deals` and `Plugin` → **Always keep on this device**.
2. Install the Claude desktop app, Git (`xcode-select --install`) and Python 3 (`brew install python` or python.org).
3. Sign in to GitHub as `anzcreatio` when git asks (use a personal access token or `brew install gh && gh auth login`).
4. Clone:
   ```bash
   mkdir -p ~/Projects/Workspaces && cd ~/Projects/Workspaces
   git clone https://github.com/anzcreatio/ai-sales-motion.git "AI Sales Motion"
   git clone https://github.com/anzcreatio/apac-sc-motion.git "AI Sales Motion/apac-sc-motion"
   ```
5. Open Claude Code on `~/Projects/Workspaces/AI Sales Motion` and paste the prompt above.

## Steps for Claude (on the Mac)
1. Find the synced library path. Try `~/Library/CloudStorage/OneDrive-SharedLibraries-Creatio/APAC Solution Consulting - Documents`
   and `~/Library/CloudStorage/OneDrive-Creatio/APAC Solution Consulting - Documents`. Confirm `Deals/` and
   `Plugin/apac-sc-motion/.claude-plugin/` exist. Call it `<LIB>` below. Stop and tell Renzo if it isn't there.
2. Link deals: `ln -s "<LIB>/Deals" "~/Projects/Workspaces/AI Sales Motion/deals"`.
3. Write `~/.apac-sc-motion.json`: `{"sharepoint_root": "<LIB>", "sc": "rh"}`.
4. Copy `_mac-setup/global-CLAUDE.md` → `~/.claude/CLAUDE.md` (merge if one exists; show Renzo the diff).
5. Copy `_mac-setup/memory/*.md` → `~/.claude/projects/<this project's folder slug>/memory/` (the slug is the project
   path with `/` and spaces as `-`; check `~/.claude/projects/` after the first session to get it exactly).
   Paths inside the memory files are Windows paths: fix them for the Mac.
6. Merge `_mac-setup/settings.json` into `~/.claude/settings.json` (marketplaces + enabledPlugins). Replace
   `<MAC PATH>` in the `apac-sc` marketplace with `<LIB>`. Then install the enabled plugins and check `/plugin` lists
   `apac-sc-motion@apac-sc`. `ai-driven-apps` needs Renzo's sign-in to `tscore-git.creatio.com`: tell him, don't try.
7. `pip3 install python-pptx`.
8. Run the `sc-setup` skill's checks and report: what works, what's missing, what Renzo must do.
9. Don't create scheduled tasks: the Friday digest, Monday release message and 8 am desk brief run on the PC only.

## Working on two machines (the rule)
- **Start:** `git pull` in both repos. **Stop or switch:** commit and `git push` both repos, and update
  `CONTEXT-HANDOVER.md` §3 (Resume here).
- **One machine per deal at a time.** Deal files are on OneDrive: two machines editing one file make conflict copies.
- **Publish the plugin from the PC only** (`publish.ps1` and `office_deck.ps1` are Windows-only). On the Mac you can edit
  and push plugin source; publish happens on the PC.
- Stand logins, clio environments and Microsoft 365 connectors are set up per machine, by Renzo.
- Lasting rules go in `CLAUDE.md` (it travels); memory is per machine and is only a convenience.

## Mac limits
| Thing | Mac |
|---|---|
| Deck build (`sc-deck`) | Works; PNG rendering needs PowerPoint for Mac (or LibreOffice) installed |
| Slide-library extract, `publish.ps1` | Windows only: do on the PC |
| clio / stands | Re-register per machine (Renzo) |
