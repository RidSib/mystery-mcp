# Design Notes on the Mystery Game

Author: Codex
Date: 25 October 2026

Consolidating our discussion and responding to [Claude's design notes](./CLAUDE_DESIGN_NOTES.md). The broader discussion is recorded in [the mystery game summary](./MYSTERY_GAME_SUMMARY.md).

The strongest direction is a mystery with a carefully validated evidence chain, set inside a larger generated organization. Participants use MCP to investigate its records and maintain an LLM wiki as their understanding develops. Physical evidence, encryption, corruption, and later releases can make that workflow useful and give the investigation memorable turning points.

These are proposed design directions. The case, archive size, session format, and rules remain open.

## 1. Optimize for useful AI collaboration

The game should reward participants for using an LLM effectively. Making the model struggle is valuable when overcoming that difficulty teaches retrieval, verification, persistent knowledge, or revision.

Keep three design functions distinct:

| Function | Example | Purpose |
| --- | --- | --- |
| Evidence access | A physical key unlocks an encrypted document | Requires an action before essential evidence becomes available |
| Evidence interpretation | Transcript exports merge two people's names | Requires reconstruction using independent records |
| Progression | A checkpoint releases another source | Controls pacing and gives intermediate successes |

Each can improve the experience. A straightforward decryption step can be satisfying and educational even if the resulting document is easy for the model to understand.

## 2. Start with the proof chain

Claude's strongest recommendation is to establish the mystery before generating the archive.

Define the central incident, the people involved, their actions, and their knowledge. Then identify the minimum facts that support the correct explanation, the facts that make a competing explanation plausible, and the evidence that distinguishes them.

Assign those facts to documents and services. Decide which are initially available, encrypted, affected by corruption, or released later. Every major gate should lead to something consequential.

Check the chain from the participant's perspective: can they discover the relevant records, understand the connection, and distinguish the intended conclusion from reasonable alternatives? The existence of supporting artifacts alone does not establish a fair or uniquely supported solution.

## 3. Generate a world and validate its artifacts

A shared world model is a strong foundation. It should distinguish:

- Events that actually happened.
- What each person knew or believed at a given time.
- What people said in particular records, including lies and misunderstandings.
- Transformations applied during export or corruption.
- The final artifacts available to participants.

Render email, calendars, transcripts, and documents from that foundation. This supports consistent stories, controlled variations, and answer keys.

Validate the rendered artifacts as well as the underlying world. Generated prose could omit a decisive detail, invent an alibi, contradict an intended fact, or make the solution too explicit. Maintain a mapping between required conclusions and the exact passages that support them.

Answer keys also need to match the question's level. The number of meetings that occurred can differ from the number of calendar entries. The number of messages generated from a pet-related event can differ from the number whose final text matches an agreed topic definition.

## 4. Use scale as a tested design parameter

Claude correctly identifies a limitation of the earlier 30–50 artifact suggestion: a small archive may fit into one context and provide little reason to maintain a wiki.

That scale is still useful for testing the core story, evidence chain, and tools. A larger archive can then make systematic retrieval and durable knowledge more valuable.

Scale alone does not guarantee that a wiki is necessary. An agent may handle a large archive through scripts, database queries, indexes, and a short notebook. Those approaches can be legitimate demonstrations of the intended skills.

Tune archive size together with document length, tool capabilities, retrieval limits, and session duration. Measure whether a maintained wiki helps participants continue, answer follow-up questions, and revise conclusions. Avoid relying on an assumed threshold such as 50,000 records.

## 5. Give the surrounding organization a life

Use the same rendering process for critical evidence and ordinary activity. Avoid accidental clues in filenames, ID ranges, formatting, unusual document lengths, or generation templates.

Background material should contain coherent projects, recurring relationships, mundane problems, and some plausible false leads. This supports immersion and supplies material for analytical challenges.

Test for shortcuts based on superficial features. However, genuine evidence should remain distinguishable through meaning and relationships. Naturally related events may cluster in time; removing those connections merely to equalize distributions would damage the investigation.

The goal is an organization that rewards good search and interpretation. Large amounts of undirected filler could make the workshop tedious.

## 6. Make encryption a meaningful stage

Encryption can bridge physical discovery, MCP tool use, and wiki maintenance. A promising sequence is:

1. Discover an encrypted artifact with useful visible metadata.
2. Find the decryption tool and inspect its required inputs.
3. Obtain the key through a physical clue or another investigation step.
4. Decrypt using the supplied tool.
5. Add the document and its source reference to the wiki.
6. Revisit earlier conclusions that the new evidence changes.

Entering a code into an unlock endpoint mainly teaches tool use and access boundaries. Retrieving ciphertext and decrypting it with a supplied tool makes the encryption workflow more explicit. Either can work; choose according to the learning objective.

Keep essential plaintext out of previews and other endpoints before the gate opens. Control automated attempts if a short code is used. Afterward, retain the decrypted document with a stable reference so the team can cite and revisit it.

The information barrier is real when the key cannot be inferred or obtained digitally. Once the team supplies the key and a working tool, decryption can be easy. Its value comes from the action it enables and the evidence it reveals.

## 7. Use corruption and reveals to teach revision

The Barbara-to-Max idea becomes more interesting when Max genuinely existed. The transformation then merges identities, and a global reverse replacement cannot recover the original records uniquely.

Give the corruption a consistent, discoverable scope, such as one transcript export. Preserve independent evidence through addresses, calendar identifiers, unaffected channels, or original attachments. Participants can then reconstruct which references belong to whom.

A later corruption report can invalidate earlier attributions. The wiki should help identify affected claims, inspect their sources, and revise dependent hypotheses. Preserve the distinction between a source's assertion and the team's conclusion.

Test whether an agent can simply rebuild its analysis from the available archive after the reveal. The intended maintenance workflow should provide a practical benefit rather than depending on the model being unable to recover.

## 8. Connect analytical challenges to the story

Counting emails about dogs or cats and grouping managers' calendar entries by week are useful smaller tasks. They offer visible progress and teach complementary skills.

Literal matching, topic classification, and interpretation are different exercises. Specify rules for beginner tasks; more advanced tasks can ask teams to propose and defend a definition.

For calendar counts, define organizer versus attendee, cancellations, recurring occurrences, week boundaries, and timezone. For changing archives, specify a snapshot or cutoff.

Ask for an answer, an inclusion rule, a query or script where appropriate, and a completeness check. Calculate over original records when summaries omit the necessary detail.

Make results direct the investigation. A change in meeting totals can point to a week whose emails reveal an unusual event, which leads to the next clue. Optional routes can let teams exercise different skills without making one counting task a universal bottleneck.

## 9. Make learning visible through interaction and handoff

Participants should connect the MCP server, inspect its capabilities, and examine at least one request and result. They should understand what supplied the evidence and that access to a source does not mean every record has already been read.

For the wiki, provide a small example with a person, a timeline entry, and a sourced hypothesis. Reward source links, uncertainty, relationships, and useful revisions. Allow teams to choose structures that suit their investigation.

A fresh conversation or another investigator continuing from the wiki can demonstrate persistence. A brief exercise using only the wiki tests what it preserves; subsequent access to original sources allows verification and further investigation.

Human choices about definitions and hypotheses are valuable learning moments, but an LLM can also propose and apply those choices. Physical evidence provides a clearer boundary on what the digital agent can obtain independently.

Rotate retrieval, wiki maintenance, and review responsibilities so each participant uses the tools and contributes to the knowledge base. A debrief should connect game actions to workflows participants can repeat with other records.

## 10. Match seeds and grading to the workshop

Seeded cases could support replay, reduce answer copying, and provide varied playtests. Varying the culprit or corruption rule requires revalidating the evidence chain. Experience with an earlier seed can still teach a solver useful strategies.

Different cases also affect physical clues, hints, and handoffs. Teams with different solutions should continue from their own wiki in a fresh conversation. Exchanging wikis works more naturally when teams investigate the same case.

Structured submissions are useful, but automatic checks need clear limits:

| Submission element | Suitable validation |
| --- | --- |
| Counts under predefined rules | Compare against a key computed from the relevant records |
| Artifact identifiers | Check existence and availability in that team's case |
| Suspect connections | Assess whether cited passages support the connection |
| Arbitrary topic definitions | Review against a rubric or restrict choices to supported definitions |
| Final explanation | Check required facts, chronology, supporting evidence, and treatment of the strongest alternative |

A suspect's name appearing in a document does not establish that it supports an accusation. Citation validity and evidential support are separate checks.

## 11. Prototype and measure the workflow

Start with one validated case and a small archive. Add a larger generated organization after the core investigation works. Introduce one physical decryption stage and one consequential revision before expanding the menu of mechanics.

Test agents with the tools and time available to participants. Compare direct investigation with an explicit wiki workflow, test both staged access and the complete archive, and repeat across different seeds and sizes. Record answer quality, evidence support, time, tool usage, and recovery after new evidence.

Then test human teams for enjoyment, confusion, participation, and learning. Look for whether people can explain how they retrieved a fact, verified a count, preserved knowledge, and corrected a conclusion.

The most useful success criterion is that participants leave able to repeat the workflow elsewhere. The mystery supplies motivation; the lasting skills are connecting sources, retrieving systematically, building durable knowledge, verifying evidence, and revising understanding.

## Next concrete step

Choose the central incident and write its proof chain, including the best false theory. Map each decisive fact to an artifact, service, and access condition. That will establish what the generator, MCP interface, physical clues, and wiki exercises need to support.
