# W0 Transcript intake v0.1 (12 Nov 2026)

AEs and BDRs drop call transcripts in the Teams channel **GTM Team → APAC Transcript Submission** (private; SCs +
AEs + BDRs). A Claude scheduled task (`sc-transcript-intake`, Renzo's PC) checks the channel's synced folder and turns
each new transcript into a first-meeting pack, so the SC starts from a draft and not from a late heads-up.

**Pilot:** Renzo's PC only. The task runs only while the Claude app is open. Willy and Ferdhi join after two real deals.

## Paths

| What | Path |
|---|---|
| Intake (channel files, AEs write here) | `C:\Users\r.huruiti\OneDrive - Creatio\GTM Team-APAC Transcript Submission - Documents` |
| Team root (SC only) | `C:\Users\r.huruiti\OneDrive - Creatio\APAC Solution Consulting - Documents` |
| Deals | `<team root>\Deals\<kebab-case-account>-<sc>\` (`sc` from `~/.apac-sc-motion.json`; the task runs on Renzo's PC, so `rh`. Deal folder rule: `sc-setup`) |
| Intake log + status | `<team root>\Deals\_intake\intake-log.json`, `<team root>\Deals\_intake\INTAKE-STATUS.md` |
| First-meeting skill | `C:\Projects\Workspaces\AI Sales Motion\apac-sc-motion\skills\sc-first-meeting\SKILL.md` |

## Each run

1. **Scan** the intake folder recursively (skip `desktop.ini`, hidden files and any folder starting with `_` or `.`).
   Candidates: `.docx`, `.vtt`, `.txt`, `.md`, `.pdf`. Ignore anything else (images, decks, videos) and log it once as
   `ignored`.
2. **Skip what's done or still arriving:** skip any file whose key (relative path + size + last-modified) is already in
   `intake-log.json`, and any file modified less than 5 minutes ago (it may still be syncing). Max **3** new files per
   run; the rest wait for the next run.
3. **Read it.** `.docx` with `python -I` + `python-docx` (fallback: unzip `word/document.xml`), `.vtt`/`.txt`/`.md` as
   text, `.pdf` with the Read tool. If it isn't a sales call transcript (a test file, a deck, minutes with no customer),
   log `not-a-transcript` and move on.
4. **Find the account**: customer company name from the transcript, the file name (Teams uses the meeting title) and
   who's on the call. Who uploaded it = the file's "Modified By" if you can read it, else "unknown AE".
   - Not sure which company → log `needs-sc` with the reason. Don't create a folder.
5. **Existing deal?** If `Deals\<account>\` already exists with no suffix or any suffix (`-rh`, `-wn`, `-fa`; also
   check close spellings), copy the transcript in as
   `00-<source>-transcript-<yyyy-mm-dd>.md` (source = bdr / ae / partner / customer), log `existing-deal`, and stop
   there for this file. The SC decides whether it changes the pack (often it's the second call).
6. **New deal:** create `Deals\<kebab-case-account>-<sc>\`, save the transcript as `00-<source>-transcript-<yyyy-mm-dd>.md`,
   then run `sc-first-meeting` **steps 1 to 6 only** (six answers + coverage, track and pack, research, `deck.json`,
   build and render the deck, `01-fm-prep.md`). No company website was given: find it, confirm it's the right company,
   and put "Confirm website: <url>" as SC question 1.
7. **Stop before anything is built.** Never run step 5b, 6b or 7, never touch a Creatio stand, never run clio.
   Put the three pre-build questions (competition with names · anything else from the customer · anything else to know)
   at the top of `01-fm-prep.md` under "Questions for the SC", unanswered.
8. **Log and report.** Add each file to `intake-log.json` (`key, file, uploaded_by, account, status, deal_folder,
   coverage, processed_at`) and add a line to the top of `INTAKE-STATUS.md`:
   `yyyy-mm-dd hh:mm · <account> · <status> · coverage n/6 · <deal folder> · uploaded by <name>`.
   If anything was processed and a push-notification tool is available, send one: "New transcript: <account>, pack
   ready" (or "needs SC"). A run with nothing new ends quietly with no files written.

## Rules

- **Never write, rename or delete anything in the intake folder.** It's the AEs' space; outputs go only to `Deals`.
- Everything in `sc-first-meeting` applies: evidence tags, catalogue-only claims, governance "can say" lines, and
  "SC check required before this is used with the customer." at the end of `01-fm-prep.md` and the deck's last notes.
- Transcripts are customer data: don't paste them into web searches; search with the company name and country only.
- If a step fails (sync, build, render), log `error` with one line on why, and leave the file for the SC.
