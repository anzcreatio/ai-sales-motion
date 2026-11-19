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
| 3 | **Atlassian MCP** (`claude mcp add --scope user --transport http atlassian https://mcp.atlassian.com/v1/mcp`, or the `ai-driven-atlassian:atlassian-setup` skill) | Faster: I can search Confluence in any chat without driving a browser | 10 min | Your sign-in |
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
