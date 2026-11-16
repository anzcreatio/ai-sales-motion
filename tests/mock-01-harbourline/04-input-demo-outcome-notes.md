# Mock demo outcome notes: Harbourline Mutual Bank (FICTIONAL)

> **Test data**, written by Claude to exercise W5. SC notes taken straight after the demo (not recorded).

- **Demo:** Thu 13 Nov 2026, 10:00–11:05. Built at L3 + simulated L4 (LOS document store stand-in). Scenes 0–3 as planned in the W2 output.
- **Attendees:** Megan Holt (Head of Lending Ops), Raj Iyer (Enterprise Architect), **James Wu (Head of Broker Distribution)**, and **Lisa Moretti (COO) joined for the first 20 minutes**.
- **Reactions:**
  - Lisa, on the opening turnaround dashboard: "If I could see this every Monday, that alone would change our conversation with the board."
  - The document-check agent got the strongest reaction. Megan: "That's the bit. That's three days gone." James: "Brokers would love the instant missing-docs request."
  - Raj asked twice where the AI runs. We answered: in-country hosting is available in Australia; we'd confirm the routing details in writing. He asked for "something on paper for the CRO".
  - The broker status view: James wants it, but said brokers won't log into "another portal". They live in their aggregator software. He wants status **pushed** to brokers (email/SMS or via the aggregator).
- **Corrections → live changes made in the demo:**
  1. The DLA is $1.2m for owner-occupied loans but **$800k for investment loans**. We changed the rule live (business rule value) and re-ran the routing. Megan: "OK, that's actually impressive."
  2. Self-employed applicants need **2 years of tax returns**, not 1. Added to the document checklist live.
- **One-pager checks answered:** Q1 (same limit for all loan types) = **No** (see above) · Q2 (self-employed in Phase 1) = **Yes** · Q3 (brokers only hear by email) = **Yes** · Q4 (PDFs/photos, no paper) = **Mostly; some branches still scan paper**.
- **New pain:** Credit committee packs are assembled by hand: "an assessor spends half a day building the committee paper."
- **Objections:**
  - Raj: "How does this not become another silo next to the LOS?"
  - Lisa: "We've been burnt before. I need to see value in months, not years."
- **Numbers updated:** broker status calls ≈ **400 a week** (Megan's team counted). Assessors: **14 FTE**.
- **Decision process (asked at close):** COO sponsors → business case to the Executive Committee in **February 2027** → board approval needed above **$1m total contract value** → procurement runs an RFQ (not a full tender) under that threshold.
- **Next steps agreed:** Proposal by Monday 17 Nov · Raj gets the AI/data paper for the CRO by 21 Nov · a working session on the LOS integration with Raj and the LOS vendor in early December.
- **Partner:** not chosen yet; two Creatio partners in AU are likely. Prepare the Partner Pack anyway.
- **Price book:** not available to the test. Use placeholders.
