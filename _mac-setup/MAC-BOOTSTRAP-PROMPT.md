# Mac bootstrap prompt (16 Nov 2026)

## Before you paste (Renzo, about 15 min, needs your passwords)
1. **Claude desktop app**: install it and sign in with your Creatio seat. Open the Code tab on your home folder (`~`).
2. **OneDrive**: sign in with your Creatio account. In SharePoint, open *APAC Solution Consulting → Documents* → **Sync**.
   In Finder, right-click `Deals` and `Plugin` → **Always keep on this device**. Wait until they show the green tick.
3. **Homebrew** (it asks for your Mac password, so run it yourself in Terminal):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   Then run the two `echo ... >> ~/.zprofile` lines it prints at the end.
4. **Microsoft 365 apps** (PowerPoint, Word) from Company Portal or office.com: needed to render decks.

## The prompt (paste into Claude Code on the Mac)

```text
Set up this Mac for my Creatio "AI Sales Motion" work. I also work on a Windows PC; everything I work on lives in two private GitHub repos (account anzcreatio) plus a SharePoint library synced by OneDrive. Work through the steps in order, tell me after each phase what passed and what failed, and keep going unless a step needs me.

HARD RULES: never type or ask me to paste a password, token or MFA code into chat; I do every sign-in myself in the browser or terminal. Never open CREDENTIALS.md files. Never register clio environments. Never create scheduled tasks (they run on the PC only). Don't touch Creatio stands.

PHASE 1 - command-line tools (Homebrew is already installed)
1. brew install git gh python@3.12 node ffmpeg
2. brew install --cask dotnet-sdk google-chrome
3. dotnet tool install --global clio ; make sure ~/.dotnet/tools is on PATH in ~/.zprofile ; check `clio --version` (the PC has 8.1.0.149; any 8.1.x is fine).
4. Python packages for python3 (Homebrew's): python3 -m pip install --user --break-system-packages python-pptx python-docx openpyxl pymupdf Pillow lxml requests websockets playwright ; then python3 -m playwright install chromium.
5. Show me a table of versions: git, gh, python3, node, ffmpeg, dotnet, clio, and one python3 -c import check of pptx, docx, openpyxl, fitz, PIL, lxml, playwright.

PHASE 2 - GitHub and the repos
6. Run `gh auth login` (GitHub.com, HTTPS, login with a web browser) and let me finish it in the browser as anzcreatio. Then `gh auth setup-git`.
7. mkdir -p ~/Projects/Workspaces ; clone https://github.com/anzcreatio/ai-sales-motion.git into "~/Projects/Workspaces/AI Sales Motion" ; clone https://github.com/anzcreatio/apac-sc-motion.git into "~/Projects/Workspaces/AI Sales Motion/apac-sc-motion".
8. In both repos set user.name "Renzo Huruiti" and the same user.email the PC uses (read it from `git log -1 --format=%ae` in the workspace repo).

PHASE 3 - SharePoint library
9. Find the synced library folder. Try ~/Library/CloudStorage/OneDrive-SharedLibraries-Creatio/"APAC Solution Consulting - Documents" and ~/Library/CloudStorage/OneDrive-Creatio/"APAC Solution Consulting - Documents"; otherwise search ~/Library/CloudStorage for a folder containing both Deals/ and Plugin/apac-sc-motion/.claude-plugin/. Call it LIB. If it isn't there, stop and tell me.
10. ln -s "LIB/Deals" "~/Projects/Workspaces/AI Sales Motion/deals"
11. Write ~/.apac-sc-motion.json as {"sharepoint_root": "<LIB>", "sc": "rh"}.

PHASE 4 - Claude config
12. Copy "~/Projects/Workspaces/AI Sales Motion/_mac-setup/global-CLAUDE.md" to ~/.claude/CLAUDE.md (if one exists, show me the diff first).
13. Read _mac-setup/settings.json. Merge its "extraKnownMarketplaces" and "enabledPlugins" into ~/.claude/settings.json (keep anything already there). In the "apac-sc" marketplace replace "<MAC PATH>/APAC Solution Consulting - Documents" with LIB.

PHASE 5 - plugins (use the claude CLI: `claude plugin marketplace add ...` and `claude plugin install <plugin>@<marketplace>`)
14. Marketplaces: creatio = https://github.com/Creatio-Platform/creatio-ai-app-development-toolkit.git ; creatio-demo-lab = https://github.com/isavenkocreatio/creatio-demo-toolkit.git ; claude-plugins-official = https://github.com/anthropics/claude-plugins-official.git ; apac-sc = the LIB/Plugin/apac-sc-motion folder ; ai-driven-apps = https://tscore-git.creatio.com/global-customer-success/ai-driven-apps/ai-driven-apps-marketplace.git (this one needs my Creatio GitLab sign-in: when git asks, stop and let me sign in in the terminal; if it still fails, skip it and tell me).
15. Install and enable: creatio-ai-app-development-toolkit@creatio, creatio-demo-toolkit@creatio-demo-lab, apac-sc-motion@apac-sc, ai-driven-atlassian@ai-driven-apps, ai-driven-plugin-auditor@ai-driven-apps, ai-driven-project-estimation@ai-driven-apps, ai-driven-video-to-document@ai-driven-apps. Leave ai-driven-ai-studio, ai-driven-delivery-assurance-review and ai-driven-development-kit disabled (same as the PC).
16. creatio-demo-toolkit checks its own prerequisites on first session (scripts/check-prereqs.sh). Run that check now and install only what it says is missing.
17. Check the clio MCP server starts: `clio mcp-server` must launch without error (stop it after it starts). No environments will be registered yet: that's expected.

PHASE 6 - memory and handover
18. Tell me to start a NEW Claude Code session on "~/Projects/Workspaces/AI Sales Motion" (so the project memory folder exists). In that session: copy _mac-setup/memory/*.md into that project's memory folder under ~/.claude/projects/ (the folder whose name is the project path with / and spaces turned into -), and fix any Windows paths inside them for the Mac.
19. In that new session, read CLAUDE.md and CONTEXT-HANDOVER.md, run the apac-sc-motion `sc-setup` checks, and give me one table: component | status | what I must do. Things only I can do: Creatio stand sign-ins and clio environment registration, Microsoft 365 connectors, the tscore-git sign-in if it was skipped.

Finish with the two-machine rule from CLAUDE.md in one line, so I remember it: git pull both repos at the start; commit and push both before switching; one machine per deal at a time; publish the plugin and run scheduled tasks on the PC only.
```

## After it finishes
- Run `/plugin` in the new session to check all 7 plugins are listed.
- Register your demo stands in clio yourself in a Terminal, not inside Claude (memory `clio-register-outside-claude-app`; the Windows MSIX copy issue shouldn't apply on a Mac, but check `clio show-settings-file` first).
