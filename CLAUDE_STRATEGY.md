# Strategy and Case Proposal

Author: Claude (Opus 5.5)
Date: 26 October 2026
Responding to: `MYSTERY_GAME_SUMMARY.md`, `CLAUDE_DESIGN_NOTES.md`, `CODEX_DESIGN_NOTES.md`, `GEMINI_DESIGN_NOTES.md`, and the `v1/` prototype wiki.

## 1. What is already settled

All four documents agree on the following. Treat these as decisions, not open questions:

- **Write the proof chain before generating any data.** List the facts that prove the answer, the best false theory, and the evidence that tells them apart.
- **Generate from a world model, then render.** The world model records what happened, who knew what, and what each person claimed. Rendered artifacts are checked against it.
- **Use the same rendering pipeline for clues and background.** No surface-level tells.
- **Keep three kinds of gate apart:** access (physical key, encryption), interpretation (identity corruption, revision history) and progression (checkpoints, releases).
- **Have one consequential reveal** that forces teams to repair their wiki.
- **Force a "shift change":** a fresh conversation that carries over only the wiki.
- **Use structured submissions,** and check citation validity separately from whether the evidence actually supports the claim.
- **Point the counting challenges back into the story.**

## 2. Where the notes disagree, and my call

| Question | Positions | Call |
| --- | --- | --- |
| Archive size | Claude: ~50k as the difficulty lever. Gemini: 300–800. Codex: treat it as a parameter to test. | **Gemini is right that scale isn't the difficulty.** A coding agent filters 50k records down to 30 in seconds. Use scale for *immersion and the counting tasks*, not to stop the solver. Target a **few thousand** artifacts with a living organization around them. That's big enough that nobody reads everything and small enough to validate. Difficulty comes from the gates and the server boundary. |
| Per-team seeds vs. one shared case | Claude: a seed per team. Codex and Gemini: one shared case. | **One canonical case per event.** Props, hints, wiki swaps and the debrief all depend on a shared case. Keep seeds for automated playtesting and for running the game again at future events. |
| Human-only steps | Claude: definitional decisions belong to humans. Codex: an LLM can propose those too. | **Codex is right.** Only **physical** and **time** gates are real boundaries. Use them for the two decisive gates and nothing else. |
| Starting perspective | Gemini: different departmental starting leads per team. | **Adopt it.** It makes the mid-game wiki exchange meaningful within a shared case. |
| Server-side discipline | Gemini: metadata-only search, explicit full fetches, revision history, all three MCP primitives. | **Adopt it.** It's the most practical anti-shortcut design so far, and it teaches MCP directly. |

## 3. What v1 shows

`v1/` is a strong example of **what a good team wiki looks like**. It keeps claims apart from facts, records where each source came from, marks retracted attributions, separates analysis from verdict, and has a usable handoff page. Its mechanics work: the Barbara/Max display collision, the pet-email checkpoint that unlocks evidence, the calendar spike pointing to a week, and the sealed receipt behind a physical card.

**As a game, though, it isn't fun yet:**

- **There's no answer.** The case question is a compliance review whose honest conclusion is "unresolved". Players need a reveal that pays off, not a well-hedged register.
- **The stakes are abstract.** An out-of-scope export of 12,480 rows matters to a security team. It doesn't make a room lean in.
- **There's no Halloween.** The folder is called `halloween-mystery`, and the theme should earn that name.
- **It gives too much away to use as a handout.** It solves the first half of the case. Use it as the **facilitator's reference** for a good wiki and as a source for a cut-down starter template.

Keep its mechanics, add a real answer and real stakes, and make it spooky.

## 4. What makes a mystery work in this format

1. **The crime has to happen inside systems.** Approvals, accounts, edits and exports leave natural traces in email, calendars, documents and transcripts. A stabbing in a stairwell doesn't.
2. **There must be a definite answer:** who, how and why, plus one reveal that reframes earlier documents.
3. **There must be a tempting wrong answer** that a lazy "summarize everything" pass will produce. The game rewards teams that don't stop there.
4. **The twist should be about the workflow itself:** attribution, provenance, identity, untrusted text. Then the plot is the lesson.
5. **It needs to be Halloween-flavored without being grim.** Uncanny, not gory.

## 5. Case concepts

### A. The Ghost Approver (recommended)

**Pitch.** Vera Lindqvist left Aster Labs in July. Her account was never shut down. All October, "Vera" keeps showing up: she accepts meeting invites, comments on documents, and appears in meeting transcripts. People start joking that the office is haunted. On the Friday before Halloween, a live customer-data export goes out to a prospective client, Cedar. The second approval it needed is signed by Vera.

**Question given to teams:** *Who is wearing the ghost, and what did they do with it?*

**Why it fits:**

- **Most "sightings" have boring explanations,** and those are the analytical challenges. A recurring series auto-accepts invites. The transcript exporter's name collision puts her name on someone else's words. A shared delegate mailbox does the rest. Teams classify every sighting: automated, mislabeled, or **manual**.
- **A counting challenge finds the week.** Vera's activity per week, split by type, is flat for automated sightings and spikes for manual ones in week 43. That is v1's calendar-load mechanic with a real payoff.
- **The person who pressed the button isn't the culprit.** Barbara ran the export, believing the approval was real. That makes her the perfect second wrong answer after Max, the first one the transcript points to.
- **The culprit is the person who held delegate access to Vera's account:** Jonas, her former manager and the executive sponsor of the Cedar deal. His motive is the deal and its fee sheet.
- **The theme pays off.** Act 1 reads like a ghost story. Act 2 shows that every haunting is either a system quirk or a cover-up.

**Proof chain (draft):**

| # | Fact the final answer needs | Where it lives | Gate |
| --- | --- | --- | --- |
| 1 | The export happened and exceeded scope | Job trace, policy document | Open |
| 2 | The second approval was signed by Vera's account | Approval record | Open |
| 3 | Vera left in July and her account stayed active | HR offboarding email, IT backlog | Open, but buried |
| 4 | Most Vera sightings are automated or mislabeled | Calendar series data, exporter bug report | Counting challenge, then checkpoint release |
| 5 | Manual Vera activity starts in week 43 | Calendar and document-comment activity | Counting challenge |
| 6 | Jonas was granted delegate access to Vera's mailbox in July | IT ticket | Search beyond the case-directed threads |
| 7 | The approval session came from Jonas's device | Session audit | **Encrypted; key on a physical card** |
| 8 | Jonas edited the exception policy hours before the export | Document revision history | **Hidden tool parameter** (Gemini's silent edit) |
| 9 | Jonas's Cedar call ended 10 minutes before the approval | Calendar plus call notes | Open |

**Wrong theories the case must defeat:** (1) Max authorized it, based on the corrupted transcript. (2) Barbara did it, since she ran the job. (3) It really was a ghost, or a system bug. (4) Vera came back, which is ruled out by her new employer's out-of-office replies.

**Optional AI twist (from concept B):** Jonas leaves a comment on the approval written for automated assistants, saying the approval was verified by Security. A team that asks its LLM to summarize the approval gets misled. A team that reads the raw record catches it. Keep the injected text harmless and limited to the game, and explain it in the debrief.

### B. The Possessed Assistant

The company's internal AI operations agent ran the export. Someone planted instructions in a shared document that the agent read. The participants' own LLMs then hit the same poisoned document. This is the most on-topic option for AI literacy, but it's mostly one trick. It works better as a mechanism inside A than as a whole case.

### C. The Vanishing

An employee disappears on the Friday before Halloween. Teams reconstruct their last 72 hours across every service. It turns out they went to a regulator with evidence, and the others are covering their tracks. The emotional pull is strong and the ending is hopeful. The risks: a missing-person story can feel heavy, and the reveal depends more on reading than on the analytical mechanics.

### D. Who Killed the Build Server?

A light, comic whodunit around an office Halloween party: a sabotaged deployment, a missing pumpkin trophy, a petty feud. It's low stakes and good for beginners. It has less depth, so use it as a **20-minute warm-up case** for teaching MCP connection and wiki basics before the main case.

**Recommendation:** run **A as the main case**, with **B's injection as one of its mechanisms**, and **D as an optional warm-up**.

## 6. Session structure (about 3 hours)

| Phase | Time | What happens | Skill |
| --- | --- | --- | --- |
| 0. Connect | 15 min | Connect the MCP server, list its tools, resources and prompts, and inspect one raw request and response | MCP literacy |
| 1. The haunting | 45 min | Departmental starting leads; build people pages and a sightings ledger; first theory (Max) | Retrieval, wiki structure |
| Checkpoint | — | Submit a classified count of sightings to release the exporter bug report | Complete retrieval, definitions |
| 2. Rationalize | 40 min | Max theory collapses; repair the wiki; the week-43 spike points to the delegate-access ticket; find the physical card; decrypt the session audit | Revision, tool use, physical gate |
| Shift change | 5 min | Fresh conversation from the wiki only; swap selected pages with another department | Durable knowledge |
| 3. Unmask | 35 min | Revision history, timeline reconstruction, structured accusation with citations and the best rejected alternative | Synthesis, verification |
| Debrief | 20 min | Reveal the event log; map each mechanic to a real-world workflow | Transfer |

## 7. Build plan

1. **Case bible.** Characters (keep v1's cast and add Vera), the world-model event log, the proof chain table, wrong theories, and the props list. Write this before any code.
2. **Core set.** Render about 80–150 decisive and supporting artifacts. Check each proof-chain row against the exact passages that support it.
3. **Agent test on the core set.** Can a capable agent solve it with the gates open? With the gates closed, where does it get stuck? Fix leaks, such as plaintext showing in snippets or the culprit being findable before the gates.
4. **Grow the organization.** Generate the surrounding company with the same pipeline: projects, threads, the PawPrint list, and real background storylines, a few thousand artifacts in all. Re-run the surface-feature check.
5. **MCP server.** Stateless HTTP on Vercel. Metadata-only search and listing, explicit full fetches, document revisions, `decrypt_document`, `submit_checkpoint`, `submit_final`, resources for the org chart and policies, and one biased server prompt. Per-team tokens and rate limits. Pre-built index, no LLM calls at runtime.
6. **Grading.** Answer keys computed from the event log. A citation validator. A short rubric for the final explanation.
7. **Playtests.** Agents first, across archive sizes, with and without a wiki workflow. Then a human team. Measure where people stall, whether everyone contributes, and whether they can explain how they know.
8. **Props.** The handover card with the key, the sealed envelope, department lead cards and a facilitator hint ladder.

## 8. Main risks

- **The plot is too easy:** the culprit is visible in an open document. Mitigation: the proof-chain audit and agent playtests with gates closed.
- **The plot is too hard:** a gate stalls the room. Mitigation: two routes to every essential fact except the physical key, plus a timed hint ladder.
- **The ghost device is unclear.** Every manual sighting must be traceable to a person through independent evidence, never through a single document.
- **Free-tier exhaustion.** Run playtests locally. Hobby pauses for 30 days if you go over, and it's for non-commercial use only.
- **Too little time.** If the event is on 31 October, cut steps 4 and 7 down: a smaller organization (around 1–2k artifacts), one agent playtest, one human dry run, no warm-up case.

## 9. Next concrete step

Write `CASE_BIBLE.md` for The Ghost Approver: cast with secrets and motives, the event log for 1 July – 31 October, the proof chain with artifact IDs and gates, the four wrong theories with the evidence that defeats each one, and the prop list.

---

*Written by Claude (Opus 5.5). A proposal for the team to accept, change or reject.*
