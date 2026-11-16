# Mock discovery call 01: Harbourline Mutual Bank (FICTIONAL)

> **Test data.** The company, people and numbers are invented to test the card and W2. Any resemblance to a real
> organisation is unintended. The call is written to be realistic: vague answers, an IT voice pulling elsewhere,
> half-commitments.

## Inputs W2 receives

### Part A pre-fill (from W1)
- **Account:** Harbourline Mutual Bank · customer-owned bank, Australia · ~180k members · home lending via brokers + branches
- **Industry pack:** BFSI · **Track:** P+A (BDR tagged "Both")
- **BDR trigger quote:** "Our broker channel is drowning, approvals are too slow, and the board wants an AI plan by Q2."
- **Hypotheses on the slide:**
  - H1 Slow time to decision on home loans (KPI: days to conditional approval)
  - H2 Brokers chase status by phone and email (KPI: status calls per week, broker NPS)
  - H3 Manual document checking: payslips, statements, ID (KPI: minutes per file, % incomplete applications)
  - H4 Hardship and complaints handling under regulatory pressure (KPI: response time vs obligation)
  - H5 No single view of the member across lending, deposits and service (KPI: cross-sell, handling time)
- **Picture on screen:** Lodge → Assess → Verify docs → Serviceability → Credit decision → Conditional approval → Valuation → Formal approval → Settlement
- **3 things to learn:** where the time actually goes · who owns the broker relationship problem · AI policy stance

### Card notes (AE, partial; the call was recorded so only ★ blocks were filled)
Consent ✔ · Pick: H1 ✔ rank 1, H3 ✔ rank 2, H2 ✔ rank 3, H4 ✘, H5 ? · Size: "8–10 days, sometimes 3 weeks", ~900 apps/month ·
Why now: brokers going to faster lenders; LOS renewal ~14 months · Sign-off: COO (Lisa Moretti) · Demo: Thu 13 Nov, 10am ·
COO "will try" · will forward ✔ · screen ✘ · Red flags: none ticked

### Attendees
- **Megan Holt**, Head of Lending Operations (business owner)
- **Raj Iyer**, Enterprise Architect (IT)
- **Daniel**, Account Executive (Creatio) · **Renzo**, Solution Consultant (Creatio)

---

## Transcript (recorded, 31 min, lightly condensed)

**[00:00] Daniel:** Thanks both for the time. Before we start, are you OK if we record this so we don't miss anything? It stays internal.
**[00:06] Megan:** Yep, that's fine.
**[00:08] Raj:** Fine with me.
**[00:12] Daniel:** Great. Renzo leads our solution team for banking. The goal today is to understand what's going on in lending, and if it makes sense, agree what we'd show you next time. Renzo?

**[01:40] Renzo:** I'll share one slide. This is what we usually see at customer-owned banks your size. Five things. Which of these are true for you, and which hurts most?
**[02:05] Megan:** The first one, honestly. Time to decision. That's the one the board keeps asking about.
**[02:12] Renzo:** OK. And the others?
**[02:15] Megan:** Documents, number three, that's a big one. Half the applications come in incomplete. And brokers chasing us, yes, that's real. It's kind of the same problem though, isn't it? If we were faster they wouldn't chase.
**[02:31] Renzo:** Fair. Hardship and complaints?
**[02:34] Megan:** No, that sits with the member service team, it's a separate thing. They're fine.
**[02:40] Raj:** The single view one, I'd say that's an IT priority more than lending. We've got a data platform project on that already.
**[02:48] Renzo:** Got it. So: time to decision first, documents second, brokers chasing third. Did I get that right?
**[02:53] Megan:** Yes. Although documents might actually be the cause of the first one.
**[02:58] Renzo:** That's a really useful point. Let's go there.

**[03:10] Renzo:** Here's a typical home loan journey. Walk me through where this goes wrong for you. Where does it get stuck?
**[03:20] Megan:** So, the broker lodges it, most come through the broker portal, maybe 70 percent, the rest from branch. It lands in the LOS and sits in a queue.
**[03:31] Renzo:** How long does it sit there?
**[03:33] Megan:** Depends on the week. A day or two. Then an assessor picks it up and the first thing they do is check the documents. Payslips, bank statements, ID, sometimes tax returns for self-employed.
**[03:45] Renzo:** And that's where the incomplete ones bounce?
**[03:47] Megan:** Exactly. They email the broker, "we need the last two payslips", and then it waits again. Could be two rounds of that. Sometimes three.
**[03:57] Renzo:** Who does the checking, is it the same assessor?
**[04:00] Megan:** Yes, our credit assessors. We call them assessors. They're expensive people doing admin, frankly.
**[04:07] Renzo:** Then serviceability?
**[04:09] Megan:** Serviceability is in the LOS but half of them still do a spreadsheet alongside because they don't trust it. Then the decision. Up to $1.2 million the assessor can approve under their DLA, above that it goes to credit committee, which meets twice a week.
**[04:25] Renzo:** DLA, delegated lending authority?
**[04:27] Megan:** Yes.
**[04:28] Renzo:** And then conditional approval goes back to the broker?
**[04:31] Megan:** Yes, by email from the LOS. Then valuation, which is outsourced, then formal approval and settlement. Settlement's mostly fine, it's the front half that kills us.
**[04:42] Renzo:** So the front half: queue, documents, back-and-forth, serviceability, decision.
**[04:47] Megan:** That's it.
**[04:50] Raj:** I'd add the LOS is old. It's a vendor product, heavily customised, nobody wants to touch it.
**[04:57] Renzo:** Is replacing it on the table?
**[04:59] Raj:** Not this year. The contract's up in about 14 months. Everything's on the table then. Right now we'd want something to sit around it.

**[05:40] Renzo:** Let me ask about the AI piece, because the BDR mentioned the board wants an AI plan. If an AI agent took one thing off the assessors' plate, what would it be?
**[05:50] Megan:** The document check. Easily. Look at the payslip, does it match the application, is the statement recent enough, what's missing. Then tell the broker what's missing straight away, not three days later.
**[06:05] Renzo:** What could it do on its own, and what needs a human?
**[06:08] Megan:** It can check and it can draft the request to the broker. I'd want an assessor to approve the request before it goes, at least at first. And obviously no credit decisions. That stays human.
**[06:20] Raj:** And it can't make anything up. If it's not sure it has to say so.
**[06:24] Renzo:** Agreed, that's how we'd design it. Where do the documents live today?
**[06:28] Megan:** They come in through the broker portal into the LOS document store. Some come by email when brokers send follow-ups.
**[06:35] Raj:** We'd need to look at how anything gets at the LOS documents. There's an API but it's limited. I'm not promising anything there.
**[06:43] Renzo:** Understood. Is there an AI policy, or someone who owns AI risk?
**[06:47] Raj:** We've rolled out Copilot internally. There's an AI policy in draft, and the risk committee has to approve anything that touches members or decisions. And data has to stay in Australia, that's non-negotiable.
**[07:00] Renzo:** Who chairs that risk committee?
**[07:02] Raj:** The CRO.
**[07:04] Renzo:** OK.

**[08:10] Daniel:** Can I ask about size? Roughly how long from lodgement to conditional approval today? Closer to 3 days, a week, or more?
**[08:18] Megan:** More. Eight to ten days on average. Some take three weeks.
**[08:22] Daniel:** And where would you want it?
**[08:24] Megan:** The big four are doing two to three days for clean deals. We need to be under five. I'd love three.
**[08:30] Daniel:** How many applications a month?
**[08:32] Megan:** Around 900. Bit more in spring.
**[08:35] Daniel:** And how much of the assessor's time goes on documents, roughly?
**[08:39] Megan:** I'd guess 30 to 40 minutes a file just on documents. More if it's self-employed.
**[08:45] Daniel:** And the broker chasing, any sense of volume?
**[08:48] Megan:** The lending support team says it's hundreds of calls a week. I can get the number.
**[08:53] Daniel:** That would help. What happens if nothing changes in the next 12 months?
**[08:58] Megan:** We keep losing broker share. Brokers send deals to whoever's fastest. We dropped from about 6 percent to 4 and a half percent of our main aggregator's volume this year. That's real money.

**[10:05] Daniel:** Why now, rather than last year?
**[10:08] Megan:** The broker share drop. And the new COO. She's made turnaround time her thing.
**[10:14] Daniel:** Is she the one who'd sign off something like this?
**[10:17] Megan:** Lisa, yes. Lisa Moretti. For anything over a certain amount it goes to the board but she'd sponsor it.
**[10:23] Daniel:** And who else wants this fixed as much as you do?
**[10:26] Megan:** The head of broker distribution. Probably more than me, actually. James.
**[10:31] Daniel:** How did the last decision like this get made?
**[10:34] Raj:** Badly. We did a CRM project about five years ago and it failed. Took two years and nobody used it. So there's scar tissue.
**[10:42] Megan:** Yeah. That's honestly a concern. People will hear "CRM" and roll their eyes.
**[10:47] Daniel:** That's helpful to know. Are you talking to anyone else about this?
**[10:50] Raj:** We're a Microsoft shop, so we'll look at what Microsoft has. And I think someone in digital had a Salesforce meeting. I don't know where that went.
**[10:58] Daniel:** Would something like this go to tender?
**[11:00] Raj:** Over a threshold, yes. Procurement would run it. I don't know the number off the top of my head.

**[12:30] Daniel:** So here's what I'd suggest. Next time we show you this working: a broker lodges an application, an AI agent checks the documents and drafts the request for what's missing, the assessor approves it, and you see time to decision on a dashboard. Who should be there, and when?
**[12:45] Megan:** I'd want James there. And Lisa, if she can. I'll try, I can't promise, her diary's brutal.
**[12:51] Daniel:** Would it help if we sent you a one-page summary of today that you could forward to her?
**[12:55] Megan:** Yes, that would help actually.
**[12:57] Renzo:** Could you show us the LOS screen an assessor uses, even for two minutes, at the demo?
**[13:01] Raj:** Probably not, there's member data all over it. I can describe it.
**[13:05] Daniel:** No problem. Dates: could we do next week?
**[13:08] Megan:** Next week's month-end. Thursday the 13th? 10am?
**[13:12] Daniel:** Works for us. I'll send the invite.
**[13:15] Megan:** Send me the summary first and I'll forward it to Lisa and James.

**[13:20–31:00]** Introductions to Creatio, the one-slide pitch, Q&A on the AU data centre (Raj), wrap-up. (Not relevant for W2.)
