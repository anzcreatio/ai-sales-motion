# Manufacturing pack: raw research findings

Researched 3 Nov 2026 for `packs/MANUFACTURING-PACK-v0.1.md`. About 22 web searches + 3 page fetches (1 succeeded, 2 failed: TGA news page timed out, ACCC productsafety page returned 403; those rows rely on search-result summaries of the same pages).

**Quality flags** (same as the Core research):
- **Strong:** regulator, statute, government, industry body, peer-reviewed or a trade publication with a stated, checkable method.
- **Medium:** analyst/trade press summary, a vendor survey with a stated sample, or a secondary restatement of a Strong source.
- **Weak:** vendor blog, stats aggregator, unsourced claim.
- "Secondary" = I could not open the primary document; the figure comes from a page or search summary that cites it.

---

## 1. APAC / AU manufacturing pains (context for §1–§2)

| # | Finding | Exact figure / wording | Source | Date | Quality |
|---|---|---|---|---|---|
| P1 | AU manufacturing is a large, export-heavy sector | Industry value added AUD 35,269m; 90,879 businesses; export earnings AUD 25,933m (54.7% of all export earnings in Ai Group's table); ~867,500 employees (data table) / 916,900 jobs (June qtr 2026) | Ai Group, *Manufacturing in Australia 2026: Performance and Outlook* (fetched) [1] | Oct 2026 | **Strong** (industry body, ABS-based). Page has typos and inconsistent employment figures; check the PDF |
| P2 | Productivity is falling | Output growth 0.9% vs 2.3% all industries; productivity growth **−2.9%**; multifactor productivity 4% below a decade ago; labour productivity 7% lower | [1] | Oct 2026 | **Strong** |
| P3 | Cost pressure | Input prices **+10.7%** in 2025-26; energy-related inputs +5% to +25%; employment on-costs 17.2% of wages | [1] | Oct 2026 | **Strong** |
| P4 | Skills shortage | **52%** of manufacturers report recruitment difficulty (45% all industries); technical/trade roles 58%, machinery operators 54%; vacancies 2.4% of jobs (~double normal); 36%+ of employees aged 50+ | [1] | Oct 2026 | **Strong** |
| P5 | Technology adoption (last year) | Cybersecurity 58%, digital management systems 50%, automation 46%, robotics 29%, standalone AI **53%**, embedded AI 29%. Manufacturing leads all industries on cyber, digital management systems, automation and robotics; AI slightly below other industries | [1] | Oct 2026 | **Strong** (but "digital management systems" is not ERP/CRM; no ERP/CRM figure published) |
| P6 | Sector in contraction through H1 2026 | Ai Group Industry Index (manufacturing) −27.9 in March 2026 (sharpest fall since Apr 2020); −16.8 in June 2026; capacity utilisation 73.7% (Mar). Causes cited: weak demand, input, energy, packaging and transport costs | Trading Economics summaries of Ai Group index [2]; Ai Group Australian Industry Index Mar 2026 PDF [3] | Mar–Jun 2026 | **Medium** (secondary restatement of an industry-body index; figures differ slightly between summaries) |
| P7 | Skills block digital adoption; legacy systems create silos | Mid-sized firms study: workforce skills 37% as a barrier to AI adoption (cyber/privacy 45%); firms with cloud ERP + integrated data more likely to report AI benefits. KPMG (via a reseller): SMBs struggle to connect legacy systems → data silos | MYOB/Oxford Economics via IT Brief [4]; DJC [5] | 2025 | **Medium** (trade-press restatement) / **Weak** (DJC) |
| P8 | No public, Australia-specific survey of CRM/ERP adoption in manufacturing found | — | Searches | — | Gap |

**Interpretation for the pack (A):** the public data supports "cost, productivity and skills pressure" strongly; it does **not** directly support process-level pains (quotes, warranty, complaints). Those stay "A (Assumed)" until deals confirm them.

---

## 2. KPI benchmarks (§4)

| # | KPI | Figure | Exact wording / note | Source | Date | Quality |
|---|---|---|---|---|---|---|
| K1 | Warranty claims as % of product sales (US manufacturers) | **1.30%** (2025); 1.329% (2024). Autos higher: Ford 3.4%, GM 3.2% (Q4 2025) | Warranty Week analysis of SEC filings, 1,400+ US warranty-issuing manufacturers; 23rd Annual Product Warranty Report | Warranty Week [6] | 2025–2026 | **Strong** for method (public filings); **US only**. Primary report page not opened; figures from search summary of warrantyweek.com pages |
| K2 | Warranty accrual rate (US) | **1.43%** of product sales (2025); 1.333% (2024) | As above | [6] | 2026 | **Strong**, US only (secondary for the 2025 number) |
| K3 | Cost to process one warranty claim | Vendor estimates USD 18–25, USD 38–65 "fully loaded", USD 45–65 (auto, "citing Warranty Week 2025", unverified) | APQC has a proper open-standards measure but the numbers are paywalled | Claimlane, Bruviti, StealthAgents (vendor) [7]; APQC measure [8] | 2025–2026 | **Weak** (vendors selling automation). APQC = get access |
| K4 | Warranty claim resolution time | 3–7 days, 5–7 days; analyst coding 8–12 min/claim | Vendor blogs | [7] | 2025–2026 | **Weak** |
| K5 | First-time fix rate (field service) | Best-in-class **88%** (some cite 89%); average 75–80%; laggards ~63% | Aberdeen "Fixing First-Time Fix", Mar 2013 (data Jan 2013); only secondary write-ups readable | Aberdeen via Asentria PDF / ServiceMax [9] | 2013 | **Medium**, old, secondary, numbers vary between summaries |
| K6 | CAPA time to closure (common internal targets) | Minor 30 d, major 45 d, critical 60 d; "under 60 days average" is a common target | Vendor guidance (AssurX); MDIC defines time to closure as initiation → closure after effectiveness check | AssurX [10] | 2022 | **Weak** (vendor, targets not actuals) |
| K7 | CAPA closure baseline (FDA CDRH pilot) | Pilot: 60% of CAPAs closed in 60 days vs an average of **>400 days** before | Unclear from the summary whether this is industry CAPAs or the FDA's own process. **Do not use** until the article is read | FDAnews [11] | ~2020 | Medium source, **unclear meaning → don't use** |
| K8 | OTIF | "Good" OTIF 95–99%; some sectors aim 80–90%. Transplace survey (mostly manufacturers): >⅓ ship OTIF 95–99%, 28% at 90–94%, 3% at 100% | McKinsey/Trading Partner Alliance: companies define OTIF differently; no consensus on the "on-time" window, so cross-company comparisons mislead | DHL glossary [12]; McKinsey [13]; Transplace (secondary, primary not located, date unknown) | various | **Weak** (DHL, Transplace secondary) / **Strong** for the definitional caveat (McKinsey) |
| K9 | Quote lead time with configurators (engineering-oriented firms) | Configurators reduced quotation lead time by **85.5% on average** (up to 99.9%) | Estimates in case companies; full text paywalled | Haug, Hvam & Mortensen, *AI EDAM* (Cambridge) [14] | ~2011–2012 | **Medium** (peer-reviewed, but small case sample, estimated, old) |
| K10 | ETO best practice | Top ETO performers >2× as likely to use technical product configurators; 53% more likely to automate quotes | Tech-Clarity survey | [15] | ~2016 | **Medium** (analyst survey, old) |
| K11 | Quote turnaround (B2B, absolute) | No credible absolute figure for configured products; Core's 24 h–4.5 days is CPQ-vendor data | — | Core research | — | **Weak** (inherit Core row) |
| K12 | Dealer/distributor portal availability vs demand | Only ~30% of distributors offer a customer portal; >70% of customers prefer online service | Industrial Distribution blog | [16] | date not shown | **Weak** |
| K13 | Aftersales portal use | 90% of B2B buyers aware of self-service portals; of those, **79%** use them; agriculture lags | Spryker-commissioned study (vendor) | [17] | ~2024 | **Medium** (vendor survey) |
| K14 | Portal order share after launch | "60–80% of orders shift to the portal within months"; 50–70% six-month target | Portal vendors, unsourced | Orderwerks, ChannelDock (search summary) | 2025–2026 | **Weak**: don't use |
| K15 | AI adoption in AU manufacturing | 53% standalone AI, 29% embedded AI | [1] | Oct 2026 | **Strong** |
| K16 | TGA recall reporting | Interim report at **6 weeks**, close-out at **12 weeks** (PRAC) | Regulatory timeframe, not a benchmark, but usable as an SLA in the demo | TGA / KWM [19] | 2025 | **Strong** (regulator), secondary read |

---

## 3. Regulation hooks (§6)

| # | Theme | What we found | Source | Date | Confidence |
|---|---|---|---|---|---|
| R1 | **TGA GMP for medicines (AU)** | TGA adopts the PIC/S Guide to GMP as the Manufacturing Principles, with Annexes 4, 5 and 14 excluded. PE009-16 is adopted; TGA consulted on PE009-17 (explanatory statement, Aug 2025). Complaints and recalls sit in PIC/S Part I **Chapter 8**; outsourced activities in **Chapter 7** (written contract between contract giver and acceptor). Annex 11 (computerised systems) is not in the excluded list → **applies** | TGA PE009 PDF [18]; Federal Register explanatory statement F2025L00990 [18]; Chapter 7 wording via secondary translation | 2020–2025 | **Medium-High**. Check which PE009 version is current on the day; read Ch 7/8 and Annex 11 text before quoting |
| R2 | **TGA recalls: PRAC replaces URPTG** | *Procedure for Recalls, Product Alerts and Product Corrections* (PRAC) commenced **5 Mar 2025**, replacing URPTG. Australian **sponsor** carries out and reports recall actions unless agreed otherwise; sponsor obtains a risk analysis from the manufacturer; interim report 6 weeks, close-out 12 weeks | TGA news page (timed out on fetch; search summary) + KWM [19] | 2025 | **Medium-High** (regulator page, read via summary) |
| R3 | TGA enforcement exists | Australian manufacturer fined ~AUD 160k for alleged breach of medicines manufacturing licence conditions | TGA media release [20] | date not checked | Medium (use only as colour) |
| R4 | **ACCC recall notification** | Supplier must notify a voluntary recall of consumer goods to the ACCC (on behalf of the Minister) within **2 days** of taking recall action. Division 3 (recalls) | productsafety.gov.au (403 on fetch; search summary) [21]; HWL Ebsworth [21] | 2026 | **Medium-High** |
| R5 | **ACCC mandatory reporting** | Report within **2 days** of becoming aware of a death, serious injury or serious illness associated with a consumer product supplied; no need to verify first; confidential, not an admission. Division 5. ACCC updated guidance **Jul 2026**; obligations unchanged | HWL Ebsworth [21] | Jul 2026 | **Medium-High** (law firm on regulator guidance) |
| R6 | **ACL consumer guarantees + manufacturer indemnity** | s274: manufacturer must indemnify a supplier who remedies a consumer-guarantee failure; s276: can't be contracted out of except to increase manufacturer liability; 3-year limit to claim (s274(4)). Warranties against defects require prescribed mandatory text (separate obligation) | HWL Ebsworth; JWS [22] | 2024 | **Medium-High** (law firms; read the ACL text before quoting) |
| R7 | **Food recall (AU/NZ)** | FSANZ Standard 3.2.2 cl 12: manufacturers, wholesale suppliers and importers must have a **written recall system**, show it to an authorised officer on request, and follow it. FSANZ Food Industry Recall Protocol; annual review + mock recall recommended | FSANZ [23]; WA Health | 2023–2026 | **Medium-High** (regulator FAQ; protocol edition to confirm) |
| R8 | **AU mandatory climate disclosure** | Group 1 from FY starting 1 Jan 2025; **Group 2 from FY starting 1 Jul 2026**; Group 3 from 1 Jul 2027 (only if threshold test met). Scope 3 from year 2 | CA ANZ (Aug 2026); KPMG; HLB [24] | 2024–2026 | **High** (consistent across sources). **Relevance to Creatio: low** (data lives in ERP/ESG tools). Use only as "supplier data requests" context |
| R9 | **Indonesia: BPOM** | New BPOM food recall regulation (Jul 2025) replaces 2017 rules: documented recall procedure + batch/lot traceability; recall report to BPOM head (and optionally provincial head). CPOB (GMP for drugs) covers complaints and recalls | Tilleke & Gibbins [25]; BPOM CPOB (Scribd copy) | 2025 | **Medium** (law firm) |
| R10 | **Indonesia: TKDN local content** | MOI Reg **35/2025** replaces MOI 16/2011; effective ~11/12 Dec 2025; certification 10 working days (was 22); weighted calculation; IKM self-declaration (May 2026). Government procurement thresholds (e.g. 40%) sector-specific | ABNR, SSEK, Makarim [26] | 2025–2026 | **Medium** (law firms). Process hook, not compliance claim |
| R11 | **Malaysia: NPRA** | Product quality reporting and recall guideline (DRGD Appendix 34); NPRA GMP inspections of local and foreign manufacturers; annual deficiency reports | NPRA [27] | 2023–2024 | **Medium-High** (regulator docs; not read in full) |
| R12 | **Malaysia: NSRF (IFRS S1/S2)** | ~130 large Main Market issuers report under IFRS S1/S2 from FY starting 1 Jan 2025; phased; climate-first | IFRS Foundation jurisdiction profile (Jun 2025); S&P [27] | 2024–2025 | **High** for Group 1; phases 2–3 not verified |
| R13 | **Singapore** | SGX: all listed issuers report Scope 1–2 from FY 2025; wider ISSB rollout deferred (Aug 2025) and tiered by market cap; Scope 3 voluntary for smaller non-STI issuers; large non-listed from FY 2027 delayed. HSA: ASEAN GMP MRA participant | Linklaters; Rajah & Tann [28] | 2024–2025 | **Medium-High** (law firms; timeline changed once, check again) |
| R14 | **Vietnam: EPR** | Decree **05/2025/ND-CP** (6 Jan 2025) amends Decree 08/2022 EPR: producers/importers recycle at mandatory rates or pay the Vietnam Environmental Protection Fund; scope widened. Later decrees 48/2026 and 110/2026 (eff. 1 Apr 2026) reported but not verified | Tilleke; KPMG Vietnam [29] | 2025–2026 | **Medium** (law firms); later decrees **unverified** |
| R15 | **Vietnam: product recall** | Not verified in this pass | — | — | **Unsure**: don't state |
| R16 | **NZ climate disclosure** | XRB Aotearoa NZ Climate Standards (Dec 2022) for large listed issuers, banks, insurers, etc. 2025–26 changes **not verified** | IAS Plus; XRB [30] | 2022–2023 | **Medium** (dated) |
| R17 | **ASEAN GMP baseline** | ASEAN GMP (traditional medicines/health supplements) Ch 9: written complaint procedures incl. considering a recall for a possible product defect | ASEAN [31] | 2021 | **Medium-High** |

---

## 4. Landscape (§7)

### ERP

| # | Finding | Source | Date | Quality |
|---|---|---|---|---|
| E1 | SAP = 59% of **global** manufacturing ERP case studies (3,745 of 6,333) in ERP Research's corpus; then Odoo, Oracle NetSuite, Microsoft Dynamics | ERP Research [32] | 2026 | **Weak** for share (vendor-published case-study corpus, global), Medium as "SAP is the most common in manufacturing" |
| E2 | Microsoft Dynamics 365 = 67.7% of ERP detected on **Australian websites** | wmtips [32] | 2026 | **Weak** (web-tech detection ≠ installed base) |
| E3 | AU mid-market manufacturing guides list Epicor (shop floor), Pronto Xi (local), MYOB Advanced/Acumatica, Dynamics 365 Business Central, NetSuite, SAP Business One | businesshub.com.au; Pronto (vendor) [33] | 2025–2026 | **Weak** (consultant/vendor content) |
| E4 | SYSPRO has an AU manufacturing customer base (2024 roadshow survey of 128 manufacturers) | Australian Manufacturing [34] | 2024 | Medium (presence only) |
| E5 | No independent AU/ASEAN manufacturing ERP market-share survey found | — | — | Gap: paid Frost/IDC report only |

### Competitors

| # | Finding | Source | Date | Quality |
|---|---|---|---|---|
| X1 | Salesforce Manufacturing Cloud: sales agreements (predicted vs actual volumes), account forecasts, Rebate Management (add-on), partner communities / Partner Visit Management; "Agentforce for Manufacturing" agent templates for sales planning, quotes and trade-ins, inventory, channel management incl. **warranty management** | Salesforce AU manufacturing AI page; Trailhead; partner blogs [35] | 2025–2026 | Official (vendor) for what they market. **Not a catalogue fact → not usable in counters**; use only to anticipate their pitch |
| X2 | Salesforce positions Manufacturing Cloud as "#1 Agentic CRM for manufacturing" | Already in differentiators research E1d | — | Vendor claim |
| X3 | Partner estimate: Manufacturing Cloud core 14–20 weeks, + 6–10 weeks for rebates | Partner blog (search summary) | — | **Weak**: don't use (not in catalogue) |
| X4 | Creatio: Leader, IDC MarketScape Worldwide B2B CRM Platform Software for Industrial Manufacturing **2024** (doc US52034425, Jun 2024, 12 vendors) | Creatio news [36] | Jun 2024 | Vendor announcement of an analyst report. **Resolves the "year not shown" gap in differentiators research C12** |
| X5 | Microsoft, SAP CX, ServiceNow FSM, Oracle: no new facts gathered; counters must stay on catalogue facts (D2/D7 Microsoft facts exist; none for SAP/Oracle/ServiceNow beyond Core's "D1, D7 at mid-market scale") | — | — | — |

---

## 5. Pact Group (public facts only)

| # | Finding | Source | Date | Quality |
|---|---|---|---|---|
| G1 | Pact's Contract Manufacturing division = Jalco, Pascoes, Australian Pharmaceutical Manufacturing (APM); health & wellness manufacturing covers **TGA and non-TGA** formulations; APM Keysborough site manufactures to TGA licensing requirements | Pact website [37] | current | Official |
| G2 | Pact tried to sell the Contract Manufacturing division (2020) and halted the sale | Australian Manufacturing [37] | 2020–2021 | Trade press |
| G3 | No public source links Pact to SAP or Microsoft Dynamics | Searches | — | The Dynamics / SAP / AI-agents landscape is **from our deal notes only**; keep it internal |

---

## 6. Gaps to close
1. APQC warranty-claim cost benchmark (paywalled): get access or drop the KPI to "ask open".
2. Read PIC/S PE009 Ch 7, Ch 8 and Annex 11 + TGA PRAC text; confirm current PE009 version.
3. Ask Creatio product: does any APAC customer run Creatio for a GxP process, and what validation package (Annex 11 / 21 CFR Part 11-style audit trail, e-signature) exists? Unknown today.
4. Vietnam recall rules; Decrees 48/2026 and 110/2026; NZ climate timeline changes.
5. A credible OTIF and CAPA-closure benchmark (not vendor targets).
6. Any AU/ASEAN manufacturing reference for Creatio (unchanged from catalogue §4).

---

## Sources
[1] Ai Group, Manufacturing in Australia 2026: Performance and Outlook (Oct 2026). https://www.australianindustrygroup.com.au/resourcecentre/research-economics/manufacturing-in-australia-2026/
[2] Trading Economics, Ai Group industry index – manufacturing (news summaries, 2026). https://tradingeconomics.com/australia/industry-index-manufacturing
[3] Ai Group Australian Industry Index, Mar 2026 (PDF mirror). https://mtsinsights-assets.s3.amazonaws.com/media/summaries/att/ai-group-australian-industry-index/2026/04/01/b634cdec-1474-495b-8614-dffcab4d686e.pdf
[4] IT Brief, "Australian mid-sized firms gain from AI but skills lag" (MYOB/Oxford Economics). https://itbrief.com.au/story/australian-mid-sized-firms-gain-from-ai-but-skills-lag
[5] DJC, IT challenges for Australian manufacturing SMBs 2025. https://www.djc.com.au/it-challenges-australian-manufacturing-smbs-2025/
[6] Warranty Week (homepage, statistics, 2025–26 archive). https://www.warrantyweek.com/ ; https://www.warrantyweek.com/statistics
[7] Claimlane, cost per warranty claim. https://www.claimlane.com/resources/blog/cost-per-warranty-claim ; Bruviti. https://bruviti.com/blogs/warranty-claims-automation-ai ; StealthAgents. https://stealthagents.com/research/ai-warranty-claims-automation-statistics-2026
[8] APQC, total cost to process warranty claims per claim. https://www.apqc.org/resources/benchmarking/open-standards-benchmarking/measures/total-cost-perform-process-process-18
[9] Aberdeen Group (via Asentria). https://www.asentria.com/wordpress/wp-content/uploads/2019/09/aberdeen-group-report-repairing-field-efficiency.pdf ; ServiceMax. https://fsd.servicemax.com/university/first-time-fix-rate-field-service-metrics-that-matter/
[10] AssurX, 8 CAPA KPIs. https://assurx.com/8-capa-kpis-you-should-be-measuring-now
[11] FDAnews, CAPA timelines reduced 50%. https://www.fdanews.com/articles/212852-timelines-reduced-by-50-percent-under-revamped-capa-process-fda-says
[12] DHL, OTIF glossary. https://lot.dhl.com/glossary/on-time-in-full-otif/
[13] McKinsey, Defining on-time, in-full in the consumer sector. https://www.mckinsey.com/capabilities/operations/our-insights/defining-on-time-in-full-in-the-consumer-sector
[14] Haug, Hvam, Mortensen, Impact of product configurators on lead times in engineering-oriented companies, AI EDAM. https://www.cambridge.org/core/journals/ai-edam/article/impact-of-product-configurators-on-lead-times-in-engineeringoriented-companies/107D0DB206626EE028613F59CB0DF203
[15] Tech-Clarity, ETO best practices. https://tech-clarity.com/documents/Tech-Clarity-Perspective-ETO-Best-Practices-Summary.pdf
[16] Industrial Distribution. https://www.inddist.com/operations/blog/13764355/distributors-claim-theyre-easy-to-do-business-with-but-lack-tools-to-prove-it
[17] Spryker, self-service portals study. https://spryker.com/press-releases/self-service-portals-study
[18] TGA, PIC/S Guide to GMP PE009. https://www.tga.gov.au/sites/default/files/pe009-pics-guide-gmp-medicinal-products.pdf ; Explanatory statement F2025L00990. https://www.legislation.gov.au/F2025L00990/asmade/2025-08-28/es/original/word
[19] TGA, Recall reforms update and new procedure. https://www.tga.gov.au/news/news-articles/recall-reforms-update-and-new-procedure ; KWM. https://www.mallesons.com/au/en/insights/latest-thinking/navigating-the-new-procedure-for-recalls-product-alerts-and-product-corrections.html
[20] TGA media release. https://www.tga.gov.au/news/media-releases/australian-manufacturer-fined-almost-160000-allegedly-breaching-conditions-its-medicines-manufacturing-licence
[21] ACCC Product Safety, tell the ACCC of the recall. https://www.productsafety.gov.au/business/recall-an-unsafe-product/tell-the-accc-of-the-recall ; HWL Ebsworth, updated mandatory reporting guidelines. https://hwlebsworth.com.au/accc-publishes-updated-mandatory-reporting-guidelines-what-businesses-need-to-know/
[22] HWL Ebsworth, ACL suppliers and manufacturers. https://hwlebsworth.com.au/the-australian-consumer-law-suppliers-and-manufacturers-who-is-ultimately-liable-to-consumers-for-defective-goods/ ; JWS. https://jws.com.au/what-we-think/enforcement-actions-for-consumer-guarantee-failures-and-supplier-indemnities/
[23] FSANZ, food recalls FAQ for business. https://www.foodstandards.gov.au/food-recalls/faqbusiness ; https://www.foodstandards.gov.au/business/food-recalls
[24] CA ANZ, Group 2 and 3 pathway (Aug 2026). https://www.charteredaccountantsanz.com/news-and-analysis/insights/research-and-insights/navigating-climate-related-financial-disclosures-a-pathway-for-group-2-and-group-3-entities ; KPMG guide. https://assets.kpmg.com/content/dam/kpmg/au/pdf/2024/australian-sustainability-reporting-legislation-standards-guide.pdf
[25] Tilleke & Gibbins, Food recall regulations in Indonesia, Thailand and Vietnam. https://www.tilleke.com/insights/food-recall-regulations-in-indonesia-thailand-and-vietnam
[26] ABNR, MOI Reg 35/2025. https://www.abnrlaw.com/news/new-local-content-rules-key-changes-under-moi-regulation-no-35-of-2025 ; SSEK. https://ssek.com/blog/revamping-indonesias-tkdn-rules-what-moi-reg-35-2025-means-for-industry/
[27] NPRA, DRGD Appendix 34. https://npra.gov.my/easyarticles/images/users/1153/drgd_appendices/APPENDIX-34-Guideline-for-Product-Quality-Reporting-and-Recall-Procedures.pdf ; IFRS Foundation, Malaysia profile. https://www.ifrs.org/content/dam/ifrs/publications/sustainability-jurisdictions/pdf-profiles/malaysia-ifrs-profile.pdf
[28] Linklaters, Singapore extended timelines. https://sustainablefutures.linklaters.com/post/102l487/singapore-extended-timelines-for-most-climate-reporting-requirements-for-listed ; Rajah & Tann. https://sg.rajahtannasia.com/viewpoints/mandatory-climate-reporting-for-listed-issuers-from-fy-2025-and-large-non-listed-companies-to-follow-from-fy-2027/
[29] Tilleke & Gibbins, Decree 05 EPR. https://www.tilleke.com/insights/decree-05-updates-extended-producer-responsibility-regulations-in-vietnam ; KPMG Vietnam. https://kpmg.com/vn/en/insights/2025/02/key-amendments-to-vietnam-environment-protection-regulations.html
[30] IAS Plus, NZ climate standards. https://www.iasplus.com/en/news/2022/12/nz-climate-standard
[31] ASEAN GMP training, Ch 9 Complaints and Recalls. https://asean.org/wp-content/uploads/2021/01/ASEAN-TMHS-GMP-Training-%E2%80%93-Chapter-9-Complaints-and-Recalls-FD.pdf
[32] ERP Research, ERP market share. https://erpresearch.com/erp-market-share ; wmtips, ERP in Australia. https://www.wmtips.com/technologies/erp/country/au
[33] BusinessHub, best cloud ERP for AU mid-sized manufacturers. https://businesshub.com.au/erp/best-cloud-erp-for-australian-mid-sized-manufacturers ; Pronto. https://www.pronto.net/pronto-xi-epicor-alternative/
[34] Australian Manufacturing, SYSPRO smart-tech survey. https://www.australianmanufacturing.com.au/manufacturers-eye-smart-tech-adoption-amid-ongoing-labour-and-integration-hurdles-syspro-finds/
[35] Salesforce AU, manufacturing AI. https://www.salesforce.com/au/manufacturing/artificial-intelligence/ ; partner channel. https://www.salesforce.com/au/manufacturing/partner-channel-engagement-software/
[36] Creatio, IDC MarketScape industrial manufacturing CRM 2024. https://www.creatio.com/company/news/23238
[37] Pact Group, health and wellness contract manufacturing. https://pactgroup.com/products-services/contract-manufacturing/health-and-wellness/ ; Australian Manufacturing, Pact halts sale. https://www.australianmanufacturing.com.au/?p=144530
