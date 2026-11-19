# Set up Claude to build in Creatio (Windows)

Time: about 20 minutes.

> **SC note (remove this and the last line before sending):** nothing to fill in. Claude asks the customer for their
> sandbox address and names the connection `sandbox`.

## Before you start (5 minutes, by hand)

1. A Claude plan that includes Claude Code: **Pro, Max, Team or Enterprise** (the free plan doesn't).
2. Install the **Claude desktop app** from claude.ai/download and sign in with your own account.
3. Your own **Creatio login** for your **sandbox** (test) site, not the one your business runs on.
   **Find your site address:** open the sandbox in your browser and copy the address up to and including
   `.creatio.com` (for example `https://yourcompany-dev.creatio.com`). Leave off anything after it, such as `/0/Shell/`.
4. You need permission to install software. If your company locks that down, ask IT to run this with you.
5. In the Claude app, open the **Code** tab, choose an empty folder (for example `Documents\creatio-build`), and paste
   the prompt below as your first message. Approve the commands Claude asks to run.

## The prompt

```text
Set up this Windows computer for building in Creatio with Creatio's AI App Development Toolkit. Work one step at a
time, tell me in one line what each step does before you run it, and check each step worked before moving on.
If a download fails (connection reset, timeout), run the same command again before trying anything else.
Never ask for any password in chat, and never run a command that needs one: give it to me to run myself.

1. .NET SDK 10. Check with `dotnet --list-sdks`, and if `dotnet` isn't found, try
   "C:\Program Files\dotnet\dotnet.exe" --list-sdks. If there's no 10.x SDK, run
   `winget install --id Microsoft.DotNet.SDK.10 -e --accept-source-agreements --accept-package-agreements`.
   If winget is missing or blocked, stop and tell me to install the .NET 10 SDK (Windows x64 installer) from
   https://dotnet.microsoft.com/en-us/download/dotnet/10.0, then wait.
   Your shell may not see PATH changes until the app restarts, so use full paths where needed.
2. clio: `dotnet tool install clio -g` (or `dotnet tool update clio -g` if it's already there). Make sure
   %USERPROFILE%\.dotnet\tools is on my user PATH permanently. Check it starts with
   "%USERPROFILE%\.dotnet\tools\clio.exe" --version.
   If it won't start and the error names a missing framework (Microsoft.NETCore.App 8.0.0 or 10.0.0), set
   "runtimeOptions": { "rollForward": "LatestMajor" } in every clio.runtimeconfig.json under
   %USERPROFILE%\.dotnet\tools\.store\clio\, keeping everything else, and check again.
   Don't run any other clio command yet (registering comes later, and I do it myself).
3. The toolkit plugin. If the `claude` command works, run:
   claude plugin marketplace add https://github.com/Creatio-Platform/creatio-ai-app-development-toolkit.git
   claude plugin install creatio-ai-app-development-toolkit@creatio
   If `claude` isn't available, add this to %USERPROFILE%\.claude\settings.json instead (create the file if
   missing; keep anything already in it, back it up first):
   "extraKnownMarketplaces": { "creatio": { "source": { "source": "git", "url":
   "https://github.com/Creatio-Platform/creatio-ai-app-development-toolkit.git" }, "autoUpdate": true } },
   "enabledPlugins": { "creatio-ai-app-development-toolkit@creatio": true }
4. Ask me for my sandbox site address (ending in .creatio.com, nothing after it). Check with me that it's a sandbox
   or test site, never the live one my business runs on.
   Connecting to Creatio needs my Creatio password, so I do it myself. Give me these two commands to run in my own
   PowerShell window (Start menu → PowerShell, not this chat), with my site address filled in and my login and password left for me to fill in.
   Tell me to keep the single quotes around the password:
   clio reg-web-app sandbox -u <my-site-address> -l <my-login> -p '<my-password>' -a
   clio ping-app -e sandbox
   Then wait until I tell you what ping-app said.
5. Give me a short table: what was installed, the version of each, and anything that didn't work. Then tell me to
   quit the Claude app completely (also from the system tray, by the clock), open it again, open this same folder
   and paste the check prompt.
```

## After the restart: the check prompt

```text
Which Creatio sites can you see through the clio tools? List the apps on sandbox. Don't change anything.
If you can't see sandbox but `clio ping-app -e sandbox` worked in my PowerShell: the Claude app may be reading its
own private copy of clio's settings. Using PowerShell, compare
%LOCALAPPDATA%\creatio\clio\appsettings.json with
%LOCALAPPDATA%\Packages\Claude_*\LocalCache\Local\creatio\clio\appsettings.json (size, date and the environment
names only; never show any password). If the private copy exists and lacks sandbox, back it up as
appsettings.json.bak, copy the real file over it, and tell me to restart the app again.
If the toolkit asks whether it may send usage data to Creatio, ask me; it's my choice.
```

You should see **sandbox** and a list of apps. If not, send a screenshot to your Creatio contact.

## What this covers (and what it doesn't)

- **Covers Business Studio:** Claude builds and changes apps, pages, objects and branding in your Creatio site,
  through Creatio's AI App Development Toolkit.
- **Doesn't cover AI Studio:** AI Studio agents are set up in AI Studio itself. This toolkit doesn't build them.

## House rules for building

1. **Sandbox only.** Never connect Claude to your live Creatio site for building.
2. **Build in your own package**, not in Creatio's own packages.
3. If colleagues build on the same site, don't edit the same page or object at the same time. The last save wins.
4. Claude asks before it changes things. Read its plan, and say no when you're not sure.
5. Start by describing the app in plain words, for example "Create an app to track partner onboarding requests".
   The toolkit writes a Business Plan first and builds only after you approve it.

---