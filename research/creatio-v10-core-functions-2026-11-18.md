# Creatio v10 core functions: Sales, Marketing, Service, AI (research 18 Nov 2026)

Source: Creatio Academy, version 10 (the default; unversioned URLs `academy.creatio.com/guides/creatio-apps/...`;
selector offers 10, 8.3–8.0; no 9.x). Release notes: 10X Unlimited (15 Jul 2026), 10.1 Unlimited (8 Oct 2026).
Gathered by four research agents on 18 Nov 2026 for the first-meeting standard demo spine. Tag: **C** (documented)
unless marked. Base: `https://academy.creatio.com/guides/creatio-apps/` (B), AI tools `https://academy.creatio.com/guides/no-code-customization/ai-tools/` (G).

## Cross-product (Customer 360, Productivity)
| Function | What it does | URL |
|---|---|---|
| Account/contact pages | Company + person records, contacts, structure, channels, files, feed | B`products/crm-tools/accounts-and-contacts/customer-360-overview` |
| Timeline | All interactions on account, contact, lead, opportunity | same |
| Relationship chart | Links between accounts and contacts | same |
| Duplicate search/merge | Scheduled or on demand; leads too | same |
| AI news and insights | News on up to 50 owned accounts; **needs a Gemini API key** | B`products/crm-tools/accounts-and-contacts/ai-news-and-insights-for-accounts` |
| Productivity | Tasks, calendar; AI schedules meetings, replies to and summarises email | B`products/crm-tools/activities/productivity-ai` |
| AI meeting summaries | **MS Teams only**, Office 365 cloud | B`products/crm-tools/activities/view-ai-meeting-summaries` |
| Mobile | iOS/Android, offline, custom home page and offline charts (10.x) | B`overview/sales-creatio-overview` |

## Sales
| Function | What it does | URL |
|---|---|---|
| Leads + lead process | Manual, Excel import, auto from ML score ≥ 80; qualify, nurture, hand off, convert | B`products/sales-tools/lead-and-opportunity-management/leads/lead-management-process` |
| Predictive lead scoring | ML score so only sales-ready leads move on | `.../leads/predictive-scoring-of-leads` |
| Opportunities | Stages, needs, competitors, stakeholders, products; editable stage process | `.../opportunities/corporate-sale-process` |
| Sales pipeline | Funnel by stage with conversion; on Sales home pages | `.../opportunities/sales-pipeline` |
| MEDDPICC (new in 10) | Deal-health tab scored 1–5 per element | `.../opportunities/assess-opportunities-with-meddpicc` |
| Forecasting | By rep, account, industry vs actuals; hierarchy (10.1) | B`products/sales-tools/forecasting/set-up-a-forecast` |
| Revenue intelligence | Waterfall/Sankey, deal-slip signals; **needs Sales Forecasts (Marketplace)** | B`products/sales-tools/revenue-intelligence/revenue-intelligence-overview` |
| Products, orders, invoices, contracts | Catalogue, price lists, orders, approvals, templates | B`products/sales-tools/orders-and-invoices/create-an-order` |
| Channel sales | Partner programmes, conditions, funds | B`category/channel-sales` |
| Sales Engagement | Email/call/task sequences; **on request** | B`products/sales-tools/sales-engagement-overview` |
| Creatio.ai for sales | Summarise lead/opportunity, prepare meeting, agenda, call script, lead probability insights, enrich, recommend products | B`products/sales-tools/sales-ai` |
| Field Sales | Visits, GPS check-in, offline; separate app | B`products/more-apps/field-sales/...` |

## Marketing
| Function | What it does | URL |
|---|---|---|
| Campaign designer | No-code flow: triggers, audiences, timers, conditions, emails, A/B split, ads, exits | B`products/marketing-tools/marketing-campaings/set-up-campaign-diagram` |
| Campaign generation agent | Prompt → proposed flow as "Planned"; triggers, emails, delays still set by hand | `.../create-a-campaign-using-creatio-ai` |
| Campaign monitoring | Participant counts per element, log, each contact's step | `.../monitor-campaigns` |
| Email designer | Drag and drop, dynamic content, multilingual; one designer for bulk + transactional (10.1) | B`products/marketing-tools/email-marketing/freedom-ui/email-designer-elements` |
| Email generation agent | Whole email from a prompt, brand colours, unsubscribe; placeholder images | `.../create-an-email-using-creatio-ai` |
| Email analytics, deliverability, subscriptions | Opens, clicks, delivery; domain verification; subscription page | B`category/email-analytics` |
| Segments | Reusable groups with entry/exit rules; scheduled refresh **10.1+** | B`products/marketing-tools/segments/segments-overview` |
| Landing pages + forms | No-code pages and forms; AI-generated pages; external form capture | B`category/landing-page-designer` |
| Web tracking, digital ads, events | Matomo/GA, Facebook/Google Ads audiences, events | B`category/website-tracking` |
| SMS | Twilio; **docs say Europe-only contacts, conflicting Marketplace note: check before APAC use** | B`products/marketing-tools/omnichannel-marketing/omnichannel-marketing-overview` |
| Lead conversion score | ML MQL likelihood; auto-lead at 80 | B`overview/marketing-creatio-overview` |

## Service
| Function | What it does | URL |
|---|---|---|
| Case management | Lifecycle, stages, escalate, conversation tab, reopen on reply | B`products/service-tools/service-cases/case-management-overview` |
| Email-to-case | Shared mailbox → case; follow-ups link; auto-categorise | `.../case-settings/set-up-a-shared-email-account` |
| Predictive routing | ML predicts service + assignee group (best with 20k+ records) | `.../service-case-processing/predictive-case-routing` |
| SLA / agreements / catalogue | Response and resolution deadlines from service, agreement, calendar | `.../manage-service-agreements` |
| CSAT | Survey on resolve; 1–2 reopens the case | `.../case-settings/set-up-case-customer-feedback` |
| Agent Inbox (Comm Hub) | Chats, calls, emails in one workspace; supervisor view | B`products/crm-tools/inbound-communications/overview` |
| Chat channels | Web chat, WhatsApp (native Meta API 10.1), Telegram, Messenger, SMS | `.../communication-workflows/chat-workflow` |
| AI-handled chats | Bot answers from KB, says it is AI, hands off with history | `.../work-with-ai-handled-chats` |
| AI email replies | Draft for review or auto-reply above a threshold | `.../review-and-send-ai-email-replies` |
| Creatio.ai for service | Case summary, resolution suggestion, case performance | B`products/service-tools/service-ai` |
| Knowledge base | Articles; AI creates an article from a case | B`category/knowledge-management` |
| Portal | Raise and track cases, KB search | B`products/more-apps/portal/portal-overview` |
| Not in v10 core | ITSM problems/changes/CIs (Marketplace Classic add-on); field service (custom/Marketplace) | — |

## AI layer
| Capability | What it does | Status | URL |
|---|---|---|---|
| Creatio.ai panel | Chat that acts on data, Freedom UI; AI Credits | GA | G`creatio-ai/creatio-ai-overview` |
| 12 built-in agents, 63 skills | Sales, Email Gen, Case Resolution, Knowledge, Analytics, Segmentation, Campaign Gen… | GA | G`creatio-ai/ai-agent-list`, G`creatio-ai/ai-skill-list` |
| Custom sub-agents | No-code: prompt + actions + parameters | GA | G`creatio-ai/develop-ai-skill/introduction-to-ai-skill-development` |
| Sub-agent process element | AI step inside a business process | GA | G`creatio-ai/develop-ai-agent/develop-ai-agent-example` |
| AI Command Center | Monitor and configure sub-agents | GA | overview |
| Predictive ML | Lookup/numeric prediction, scoring, recommendation | GA | G`predictive-models/predictive-data-analysis` |
| Governance | No training on customer data, same-region Azure LLM, encryption, RBAC, LLM registry, own LLM | GA | G`creatio-ai/data-privacy` |
| AI Studio | Agents (AI Twin, Prompt Agent Designer), skills, tools (HTTP, MCP), knowledge, channels (web chat, voice, email), governance (PII masking, HITL, audit, evals) | GA; Workflow/Code Agent Designers and Teams **coming soon** | `https://academy.creatio.com/guides/ai-studio/creatio-ai-studio-overview` |
| AI app development toolkit | Coding agents build apps from prompts; parts **Beta** (processes, Classic→Freedom) | Mixed | `https://academy.creatio.com/guides/ai-development/creatio-ai-toolkit-overview` |

Beta in 10.1: AI-generated filters (needs AI Studio + AI Twin), personal WhatsApp, metric comparison/trend.
