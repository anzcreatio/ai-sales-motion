# Creatio Confluence: what improves how Claude configures Creatio (read 19 Nov 2026)

Source: `creatio.atlassian.net/wiki`, read-only, via the REST API in the built-in browser. ~45 pages read in English,
Ukrainian and Russian (list in §5). **Internal Creatio content: not for customers.** Tags: C = stated on the page,
I = my inference.

## 1. The honest headline

| Finding | Evidence |
|---|---|
| **Most Confluence no-code best practice is already in our toolkit.** `creatio-demo-toolkit` 4.0.12 already covers idempotent processes, recursion guards, no hard-coded values, CrtProcessBuilder versions, gateways, Read Data columns, data-source dependencies | grep of the installed toolkit: "idempot" in 34 files, "recurs/retrigger" in 7, Read Data columns in 7 (I) |
| **The big lever is R&D's own AI setup, which we don't use.** R&D runs Claude Code with an official instruction server (`creatio-instructions` MCP), shared skills (`@creatio/dev-skills`, auto-updated every 6 h), `creatio-compass` (finds the platform module for a task) and `AI_GUIDES` shipped inside the `@creatio` npm packages | NCD "Setting up Claude Code for Creatio development" (18 Sep 2026); AKH "MCP Servers" (12 Jun 2026); RNDKS "Creatio Dev Skills" (20 May 2026); TER "How to Create Custom Creatio Components with AI Agents" (24 Jul 2026) (C) |
| A dozen specific rules are **not** in our build rules or the toolkit yet | §3 (I, after the grep) |

## 2. Recommended changes to how I work (ranked by impact)

| # | Change | Safer / faster / better | Effort | Needs |
|---|---|---|---|---|
| 1 | **Connect the Creatio Instructions MCP** (`https://ai-instructions-rnd.creatio.com/api/v1/mcp`), so I load R&D's current instructions before building instead of relying on what I remember | Better: same guidance R&D's agents use, updated centrally | 15 min | Your OK. It's internal R&D tooling, may need VPN or Nexus access. The full installer (`install.py`) also adds skills and MCP servers, so run it yourself, not me |
| 2 | **Custom components: tell the agent "Read AI_GUIDES from @creatio libraries"** and use two prompts: one for the component (behaviour, config panel, binding, validation, accessibility), one for registering it in the Designer | Better first build, fewer fix loops | Add to `UI-KIT-STANDARD` | Nothing. Check the guides exist in `node_modules/@creatio/*` on the next build |
| 3 | ~~Atlassian MCP so chats can search Confluence~~ | **Declined by Renzo (19 Nov 2026):** chats don't search Confluence | — | — |
| 4 | Add the §3 rules to `BUILD-RULES` v0.7 as a short "configuration quality" section | Safer + better | 1 h | Your OK |
| 5 | Send the toolkit owners (creatio-demo-lab) the rules from §3 that belong in their skills | Better for every SC | 30 min | — |

## 3. Rules not yet in our build rules or toolkit

### Safety
| Rule | Source |
|---|---|
| **Changes on a customer (or shared) site:** test on a copy first; agree a window in writing; leave a written instruction with the time window, the steps, **a test case that proves it worked**, and what to do if it fails; back up the database or binaries first; **do nothing that isn't in the instruction**; no ad-hoc transactions on prod | TS "Правила внесения изменений/правок на сайты клиентов" (Rules for making changes on customer sites, 3 Apr 2025) (C) |
| **Data bindings:** to ship new lookup records, create a **new** binding; don't edit the existing one. Updates only install new bindings (`installOnlyNewDataOrLocalization`), so edits to an old binding never reach existing sites. To change data on live sites, write an Install script. Columns that must overwrite need `ForceUpdate` | TER "[8.0.8+] Регламент поставки новых данных" (Rules for delivering new data on update, 15 Aug 2023); KB "Чек-лист по привязке данных" (Data binding checklist, 6 Jun 2023) (C) |
| **C# in a package: ship source only, not a DLL.** A DLL built against a newer core won't load, yet the install still "succeeds", so the failure shows up later at the first call. Compiled on the target, a mismatch fails loudly at install | TER "Package delivery — compiled assembly vs source-only" (6 Aug 2026) (C) |
| A handler without `scopes` runs on **every page**; a handler that doesn't `return this.next?.handle(request)` silently breaks the chain (e.g. save) | TER "Freedom UI Request Handlers" (11 Mar 2026) (C) |
| Bulk process runs: foreground runs one at a time in the user's session; background runs **10 at once** by default (`messageProcessingThreadsCount`). Big batches go in the background, overnight, split into chunks | "Best practices for mass launching business processes" (13 Mar 2026) (C) |
| AI Studio: an integration with shared credentials can be found and attached by any user (APD-8145, blocker). Use delegated credentials in demo agents | TER "Unguarded Integrations" (19 Aug 2026) (C) |

### Efficiency
| Rule | Source |
|---|---|
| **"Works at runtime, missing in the Designer"** = a missing package dependency, not a bug. Opened from a package, the Designer shows only what that package depends on. Fix: add the dependency to the highest common package, or edit from runtime | TER "Interface Designer: why elements from other packages may not appear" (1 Jul 2026) (C) |
| Process generation via clio: write the prompt as **trigger → records involved → steps in order → who's responsible → exact values and timings → target package and version**. Not supported yet: branching in generated flows, record sets, sub-processes, email templates. Plan around these limits | TER "Generate business processes using the Creatio AI app development toolkit" (3 Sep 2026) (C) |
| Business rules: several rules on one field with different conditions **don't add up**; only one fires. Use one rule with combined conditions | KB "Чек-лист бизнес-правил" (Business rules checklist, 8 Sep 2026) (C) |
| External calls blocked in the browser ("Refused to connect") = CSP. Check `CSPMode` and the trusted-sources lookup; add the source through a data binding | KB "Чек-лист по настройке CSP политик" (CSP policy setup checklist, 26 Feb 2024) (C) |
| Incoming integrations: basic auth needs `BPMCSRF` + cookies; OAuth needs Identity Service | KB incoming integrations checklist (17 Oct 2024) (C) |

### Quality
| Rule | Source |
|---|---|
| **Less metadata is better:** don't write properties that keep their default value (`color: default`, `disabled: false`, `iconPosition`) into page bodies | TER "Рекомендації по оптимізації метаданих" (Metadata optimisation recommendations, 31 Jan 2022) (C) |
| Data model: extend OOTB objects before new ones; lookups not text; details for repeating items; no stored derived values; external-Id fields for integrations; "if the process is complex, the data model is probably wrong" | TER "Best Practices for Data Model design" (27 Apr 2026) (C) |
| Processes: one job per process; must fit on one screen; gateway = one condition, true/false branches, default flow, closing gateway; always a failure path | TER BP best practice (27 Apr 2026); NCD gateway standard (12 Sep 2024) (C) |
| Naming: NCD table (`ContactInAccount`, `Contact_FormPage`, `AddButton`, business rule "Action: target", `<Title>Widget`, `<Domain>Agent`, lookup codes without `Id`) | NCD "No-Code Naming Standards" (25 Nov 2025) (C) |

## 4. Where I'd push back

| Idea | Why not (yet) |
|---|---|
| Copying the DEAI delivery model (Git for everything, own dev site per person) into demo builds | Right for a project, too heavy for a 2-day demo. Our restore point + rollback covers it (I) |
| Running R&D's `install.py` on your PC | It installs skills, plugins and MCP servers globally, and some (GHE, Jenkins, Nexus) are R&D-only. Connect the instructions MCP alone first and see what it gives us (I) |
| Rate limiting (`[RateLimit]`) and OData memory fixes | Platform and delivery topics; rarely matter for a demo (I) |

## 5. Pages read

**English:** Data model best practice 4557111302 · BP best practice 4556718093 · No-Code Naming Standards 3228139569 ·
gateways 3251306616 · Read Data 4050747394 · messages/event sub-processes 3252289538 · mass launching BPs 4400775170 ·
button → process 3770384511 · request handlers 4392845334 · data sources 4114939905 · components with AI 4640997417 ·
component playbook 5285445650 · client naming (Cdx) 4080599209 · rate limiting 5304418307 · webhooks 3259695376 ·
Unguarded Integrations 4988403713 · dedup 4414439437 · How to Deliver 5119574084 · OData memory 4490067972 ·
SQL optimisation 3848175906 · DEAI Standards 5269520388 · Setting up Claude Code 5041422343 · MCP Servers 3882680355 ·
Dev Skills 4455727206 · Toolkit developer skills 5014945807 · Designer package visibility 4809785450 · source-only
delivery 4938399778 · BP generation 5049155608.

**Ukrainian / Russian:** Rules for changes on customer sites 2353139052 · Metadata optimisation 2461630556 · Data binding
checklist 2360838360 · Package install checklist 2360837290 · New data delivery 8.0.8+ 2645786868 · Business rules
checklist 2385218501 · CSP checklist 2626125924 · Incoming integrations checklist 3314778214 · AI Builder v.0
instructions/skills/MCP 5314609183.

Skipped on purpose: ~140 Russian pages from 2012–2017 about Classic UI / bpm'online 7.x (outdated for 8.x), billing,
SCRUM, VM and phone rules.

URL: `https://creatio.atlassian.net/wiki/spaces/<SPACE>/pages/<id>`.

## 6. Mobile pages (second pass, 19 Nov 2026)

88 mobile pages changed since Jun 2025; 13 read. **Already covered well by the demo toolkit**
(`creatio-freedom-pages/references/mobile-golden-standard.md`: layout, crashers, refresh after a process, default
mobile sections via `SysWorkplace` + `SysModule.MobileSectionSchemaUId`) and by our `UI-KIT-STANDARD` (custom
components don't render on mobile). New from Confluence:

| # | Rule | Source (space, id, date) | Tag |
|---|---|---|---|
| 1 | **Web and mobile pages are separate.** A web page never appears in the app by itself; after conversion the two are independent, so a later web change must be copied by hand | TER 5137727548 "[Academy draft] Convert web pages to mobile pages", 29 Sep 2026 | C |
| 2 | **Use R&D's `creatio-mobile-page-conversion` skill** (installed with the AI app development toolkit) to build a mobile version: analysis → plan in plain words → your approval → build → publishing approval → report. Prompt: "Convert the Leads section to mobile." Beta; **phone layout only, no tablet**; Freedom UI pages only | same | C |
| 3 | **Publishing replaces what's there:** registering the section or the default mobile edit page makes the app open the new page instead of the current one. Check what users see today first. **Converting again overwrites Mobile Designer edits**: say "update the existing mobile page", or the agent may create a duplicate | same | C |
| 4 | Buttons that open a page with no mobile version open nothing (e.g. New on Products): convert the related object's form page too | same | C |
| 5 | **Mobile page schemas are JSON only: no code in the page.** Logic goes in request handlers through the mobile TS SDK (`@creatio/mobile-common`) | TER 2754380052 "Mobile 8.X. Page schema metadata", 28 Jan 2026; TER 5331058690, 16 Nov 2026 | C |
| 6 | **Custom view elements on mobile don't exist yet.** The app is compiled Flutter; an unknown component type renders a placeholder. R&D's design for `usr.*` mobile components is a DRAFT (16 Nov 2026). Plan native fields for every custom web component | TER 5331058690 "Architectural solution: Mobile custom components", 16 Nov 2026 | C |
| 7 | **Offline business rules are limited:** only model-level rules run on the device; page (view) rules, rules that need server code (e.g. case number generation) or unsynchronised data don't. If the demo is offline, test every rule with the network off | TER 2482537177 "Flutter. Low-code. Бізнес-правила" (business rules), 8 Feb 2023; TER 5137727548 | C |
| 8 | **Data freshness per list:** `cacheConfig.readMode` on the attribute: `auto` (0), `forceLocal` (1), `forceRemote` (2, always fresh: use for a live demo list), `remote` (3), plus `cacheMaxAge` in minutes | TER 2853241136 "Mobile 8.X. Load component data", 21 Jul 2026 | C |
| 9 | **Mobile workplaces (8.3.3+):** Workplace setup → Usage type = Mobile → sections → user groups. Existing stands need feature `Mobile.UseSysWorkplaceForModuleRegistration`, and users on a legacy workplace must switch to "Main workplace" in Settings to see all sections | TER 4195778627 "Workplaces in the Creatio Mobile App", 16 Jan 2026 | C |
| 10 | Mobile list page for an existing web section: Application Hub → Add page → "List page mobile", then set `SysModule.MobileSectionSchemaUId` (SQL) and, from 8.3.2, add the section to a mobile workplace | TER 4375085089, 23 Mar 2026 | C |
| 11 | Hide the floating action button (Copy/Delete): in the page's `viewConfigDiff`, `merge` `FloatingActionButton` with `visible: false` | TER 2848063544, 18 May 2026 | C |
| 12 | Mobile has its own components (`crt.FloatingActionButton`, `crt.Button` with `menuItems` and `buttonType: quick-add`, `crt.IndicatorWidget` with `useCompactFormat`, `crt.ChartWidget`) and a native DCM stage bar that works offline from cached stage data | TER 2853863987 "Mobile 8.X. Components", 24 Sep 2026; TER 4672553000, 6 Jul 2026; TER 4018896947, 28 Jan 2026 | C |
| 13 | Gaps seen in a real project (Apr 2026): buttons that create a record pre-filled from the page aren't fully no-code; no way to limit rows shown in a detail; custom-code features (e.g. "Set GPS coordinates") need a plan | TER 4503896109 "Mobile Freedom UI App Designer gap analysis", 14 Apr 2026 | C |

**For our builds (I):** rules 1–4, 6–9 belong in BUILD-RULES as a short mobile block (pending Renzo's OK); rules 8,
11, 12 are details for the toolkit owners.

Pages read: 5137727548, 4181721096, 4503896109, 4375085089, 5331058690, 2754380052, 2853863987, 2853241136,
2848063544, 4195778627, 4672553000, 5273026563, 2371551418, 2358904221, 2482537177 (Ukrainian), 4018896947.
