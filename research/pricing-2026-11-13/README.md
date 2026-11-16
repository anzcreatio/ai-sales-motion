# Pricing research for the BOM (13 Nov 2026), INTERNAL ONLY

Draft inputs for plugin 0.19.0 (`knowledge/BOM-GOTCHAS`, the BOM skill and `templates/BOM-TEMPLATE`). Decisions: handover log §4 item 74.

| File | What |
|---|---|
| `BOM-TEMPLATE-v0.2.xlsx` | Blank BOM. **First tab = one-page Summary for the AE** (filled in automatically: the deal, products needed, extras to quote, not decided yet, what to ask, what to do next). Then for the SC: Read me, Deal (candidate tier calculated), SKUs (34 lines), Gotchas (18), Sizing questions (13), Tiers |
| `BOM-EXAMPLE-navalo-v0.2.xlsx` | The same, filled in for Navalo (Metrics Credit Partners) as a worked example. Most of it is still TBC |

Rules: SKUs plus a candidate tier only. **No dollar amounts and no users per module.** The AE and Deal Desk own the price.

## Sources (all read 13 Nov 2026)

| Source | Use |
|---|---|
| FY27 Unlimited Pricing Model deck (internal, Downloads) | **Wins.** Unlimited is the default from 1 May 2026; tiers (highest of revenue/AUM and employees); what's included or not; dedicated blocks by tier; storage 2 GB DB + 2 GB files × tier max employees; 3-year minimum; 5% uplift; approval flow; AI Platform mandatory with Studio (same quantity and edition) |
| 10x AI Pricing Update deck (internal) | **Wins for AI.** AI Packages Start/Grow/Accelerate/Scale/Freedom; 500k credit blocks; no discounts; credits expire at end of term; BYO LLM and on-prem AI = Freedom only; bundled credits Growth 200/user, Enterprise 400/user, Unlimited 10,000/org |
| Studio Creatio Platform Plans PDF (creatio.com, v5) | Public plan limits: Growth cloud only, 2 environments, 50 roles, 50K process elements/month, 10K API calls/user/day, no SSO/LDAP/audit log; Enterprise 3 environments, dedicated instance and custom domain paid; Governance Application a paid add-on on Growth/Enterprise; standard term 3 years |
| creatio.com/products/pricing/compare-ai-packages, /services/support/options | AI packages (public); support plans Business / Premium; support is mandatory for the whole term and covers all products |
| Creatio Pricing Deep Dive (new-hire guide) | **Talk tracks only.** Its tier model and support details are older than FY27 |

## Open: Deal Desk to confirm

1. Unlimited AI allowance: "500 AI actions one-time" (FY27 deck) vs "10,000 AI credits per organisation" (10x deck and the public sheet).
2. Unlimited storage: "2 GB × tier max employees" (FY27 deck) vs "unlimited / extended storage included" (public sheet).
3. SKU names for the VPN tunnel and the hosting region; CRM app editions (the public configurator is JavaScript-only and couldn't be read).
4. Credit block price for Scale: $4,300 (10x deck) vs $4,400 (website). It isn't used in the BOM, but noted.
