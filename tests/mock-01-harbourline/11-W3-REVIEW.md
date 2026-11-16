# W3 test: review (3 Nov 2026)

Blind run of W3 v0.1 on the Harbourline mock (fictional). Input: [02-W2-output.md](02-W2-output.md) only; the agent did
not see the transcript or anything from after the demo. Outputs: [09-W3-design-pack.md](09-W3-design-pack.md) ·
[10-W3-run-notes.md](10-W3-run-notes.md).

## Verdict: the method works; the counting rules didn't (fixed → W3 v0.2)

### Against what "happened" in the mock demo ([04](04-input-demo-outcome-notes.md))
| What happened in the demo | Did W3 plan for it? |
|---|---|
| The approval limit is lower for investment loans ($800k, not $1.2m); changed live | ✔ **Predicted exactly**: validation moment 4, "Is the $1.2m limit the same for all home loan types?", with the live change ready |
| Self-employed applicants need 2 years of tax returns; added live | ✔ Validation moment 2 covered self-employed documents, with the checklist change ready |
| The COO joined for the first 20 minutes only | ✔ Planned a COO checkpoint inside her window |
| "Where does the AI run?" asked twice; wanted a paper for the CRO | ✔ In the close sheet and the action plan (governance answers in writing) |
| **Brokers won't log into "another portal"; want status pushed** | ✘ **Missed.** Scene 3 assumed a broker portal and treated the platform only as "peel back". Fixed by the **new-user test** (rule 8) |
| New pain: committee papers built by hand | ✘ Not foreseeable from the call; correctly left for W5 |

### Problems found and fixed
| # | Problem | Fix in v0.2 |
|---|---|---|
| 1 | The 60% test could be passed on wording: baselines and role names are easy "Confirmed" values. On rules only, the run was 56% | **Decision values** defined (rule 6); only they count. Below 60%: chase the one-pager checks or label pack defaults |
| 2 | Scene order by pain rank broke the journey agreed in the call | Ranking decides inclusion and time; order follows the agreed scenario (rule 3) |
| 3 | Budget unclear: day length, P+A, size → hours, test set and reset not included | SC-hours table; P colour sets the budget (rules 1–2) |
| 4 | "A live change for every validation moment" is impossible for architecture items; targets would push past 5 moments | Validation moments (3–5, live change) vs **logged checks**; targets said as "our estimate" (rule 7) |
| 5 | The AI answer depends on Creatio.ai vs AI Studio; a demo-built log could pass as a platform audit feature | Decide the build option before Gate A; audit-trail wording (rule 10) |
| 6 | 5,711 words: too long for a 15-minute peer check | One-page summary first; ≤ 4,000 words (rule 12, Output 0) |
| 7 | No peer reviewer named; missing §8b; attendees as demo users | Reviewer is a required input; §8b derivation; attendees not demo users |
| 8 | No pattern catalogue exists, but Gate A asks for one | Module IDs stand in until it exists (rule 5; process §6) |
| 9 | W2 and W3 used different pain IDs | Brief's ranks (P1–P3) everywhere; W2 Output 4 updated |

### Tester's claims checked
- "`creatio-demo-runbook` isn't in the toolkit": **wrong.** It exists (toolkit 4.0.12.0, `skills/creatio-demo-runbook`) and
  takes a raw SC script with the business voice, which is what Output 4 produces. The tester's skill list was incomplete.
- Process §4.1 vs §5.3 on Amber A: §4.1 is for AI Studio-only deals; P+A follows §5.3. Wording clarified in the process.

## Still open
- **Hours are estimates** until the pilot logs real SC hours per module (pilot metric).
- **The broker-portal miss shows the limit of a 20-minute call:** channel adoption questions belong in the one-pager's checks too.
- Gate B (reset, video, test set) and the build itself (W4) are the toolkit's; not tested here.
