# Suggestions for the creatio-demo-toolkit owners (from Creatio Confluence, 19 Nov 2026)

To: creatio-demo-lab (owners of `creatio-demo-toolkit`, checked against 4.0.12). From: APAC SC (Renzo Huruiti).
These are rules from internal Confluence pages that we couldn't find in the toolkit's skills. We've added them to our
own build rules (`apac-sc-motion` BUILD-RULES v0.7 §6) and think they belong in the toolkit for everyone.

| # | Suggested rule | Toolkit skill | Confluence source |
|---|---|---|---|
| 1 | Before building, load R&D's instructions from `creatio-instructions-mcp` (`https://ai-instructions-rnd.creatio.com/api/v1/mcp`, VPN) when it's connected | `creatio-demo-build` | AKH "MCP Servers" 3882680355; NCD "Setting up Claude Code for Creatio development" 5041422343 |
| 2 | Custom components: one prompt for the component, a separate one for Designer registration; "Read AI_GUIDES from @creatio libraries" | component / UI skills | TER "How to Create Custom Creatio Components with AI Agents" 4640997417 |
| 3 | Bulk process runs: background, batched; 10 run at once by default (`messageProcessingThreadsCount`) | `creatio-business-processes`, `creatio-demo-data-population` | "Best practices for mass launching business processes" 4400775170 |
| 4 | Business rules: several rules on one field don't add up; only one fires. Combine conditions | `creatio-freedom-pages` | KB "Чек-лист бизнес-правил" 2385218501 |
| 5 | Don't write default-valued properties into page bodies | `creatio-freedom-pages` | TER "Рекомендації по оптимізації метаданих" 2461630556 |
| 6 | New lookup data ships in a **new** data binding; edits to an existing binding don't install on update | `creatio-object-model`, package/clone skills | TER "[8.0.8+] Регламент поставки новых данных" 2645786868 |
| 7 | C# in a package as source only, never a compiled DLL | any skill that ships C# | TER "Package delivery — compiled assembly vs source-only" 4938399778 |
| 8 | "Works at runtime, missing in the Designer" = package dependency gap | `creatio-freedom-pages` | TER "Interface Designer: why elements from other packages may not appear" 4809785450 |
| 9 | AI Studio demo agents: delegated credentials, not shared integration credentials, until APD-8145 is fixed | `ai-studio-*` | TER "Unguarded Integrations" 4988403713 (internal) |

Pages: `https://creatio.atlassian.net/wiki/spaces/<SPACE>/pages/<id>`. Full research:
`research/CONFLUENCE-BEST-PRACTICE-2026-11-19.md` (AI Sales Motion folder).
