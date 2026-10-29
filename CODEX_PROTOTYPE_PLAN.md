# Prototype Plan for the MCP Mystery Game

Author: Codex
Date: 26 October 2026

## Proposed direction

Build one complete playable prototype around a single evidence chain. Use it to test the story, learning goals, and tool workflow before expanding the archive.

For the first pilot, use these provisional assumptions:

- Approximately two hours.
- Teams of three or four participants.
- One shared case and consistent physical props.
- One pretested MCP-capable agent configuration, a Markdown wiki, and Obsidian.
- Two major mechanics: physical decryption and revision of earlier conclusions.

These are planning assumptions, not settled requirements. The audience, duration, final story, and difficulty still need to be established.

## 1. Define observable learning outcomes

Participants should leave able to:

1. Connect an MCP source and inspect a tool call and its result.
2. Retrieve relevant evidence and verify what it supports.
3. Preserve useful findings, source references, uncertainty, and hypotheses in a wiki.
4. Revise affected wiki claims when new evidence changes their interpretation.

Choose challenges according to these outcomes. Effective use of the LLM should help participants progress. The wiki should preserve a useful, correctable understanding of the case across conversations and investigators.

## 2. Write the case bible and proof chain

Establish the incident before building the generator or server:

- What actually happened and in what sequence.
- Who acted, who knew what, and what each person reported or concealed.
- The strongest misleading explanation.
- The evidence that distinguishes the true sequence from that explanation.
- The facts participants must establish to support a final answer.

Map each required deduction to specific artifact IDs, service channels, and access conditions. Specify whether each artifact is initially available, in revision history, encrypted, affected by corruption, or released through a checkpoint.

Check that the participant-visible evidence supports the intended conclusion and addresses reasonable alternatives. An underlying event log alone does not establish that the rendered mystery is solvable.

Keep the case bible and answer key separate from participant files. The existing `v1` wiki illustrates the outcome of a partly completed investigation. Participants should begin with a mostly empty wiki and a few maintenance conventions.

Aster can supply prototype material without becoming the final story by default. The case still needs a compelling opening question, understandable stakes, and a satisfying reveal.

## 3. Build the smallest complete technical version

Use one MCP server to simulate email, calendars, documents, and meeting transcripts. Provide a coherent initial interface for:

- Searching and listing records.
- Fetching full records by stable source identifier.
- Inspecting document revisions.
- Submitting an evidence checkpoint.
- Decrypting an artifact using an externally obtained key.

Preserve original records separately from wiki interpretations. Make the scope of search results and any pagination clear enough to support complete analytical queries.

Implement one actual encrypted document whose key is obtained physically. Its contents should materially change the investigation. Preserve access to the decrypted evidence afterward so teams can cite and revisit it.

Use a pretested agent setup, Markdown files, and Obsidian. Leave NemoClaw out of the first pilot; operating an agent platform is outside the initial learning objectives.

The first technical version needs enough records to test the complete investigation. Final archive size should follow playtesting rather than serve as an assumed guarantee of difficulty.

## 4. Build the session progression

| Stage | Participant activity | Intended result |
| --- | --- | --- |
| Opening | Connect the server, inspect a request and result, and solve an easy retrieval task | Understand where the agent obtains evidence |
| Investigation | Identify plausible suspects and build initial wiki pages | Preserve a sourced working model of the case |
| Turning point | Complete an analytical task that leads to a physical key, then decrypt an artifact | Discover evidence that changes the interpretation of earlier records |
| Revision | Repair affected claims and continue in a fresh conversation using the wiki | Experience the value of persistent, maintained knowledge |
| Resolution | Submit an explanation with supporting evidence and discuss the method | Demonstrate both deduction and transferable skills |

Use physical decryption and evidence revision as the two major mechanics. A document revision puzzle can connect them: an earlier quote disagrees with a current document, prompting investigation of its history and the evidence behind the alteration.

The turning point could reveal the Barbara/Max identity collision or a consequential document change. Choose its exact form after the proof chain is written.

Keep prompt injection as an optional later extension. The first pilot already covers retrieval, analysis, persistence, verification, and revision.

## 5. Test the complete case before expanding it

First, let a capable agent investigate using the participant-visible tools and evidence. Look for unintended shortcuts, missing support for deductions, ambiguous grading, and immediate solutions that bypass the intended progression. Compare staged access with access to the complete archive.

Then run a small human playtest. Observe:

- Whether participants know what to do next.
- Whether each participant uses the tools and contributes to the investigation.
- Whether the wiki helps with continuation and correction.
- Whether the discoveries and turning point are enjoyable.
- Whether the final explanation is supported by evidence.
- Whether participants can explain how they retrieved, checked, stored, and revised their findings.

Completion time alone is insufficient. A technically sound case may still be tedious, and a fast team may have learned the intended skills well.

## 6. Tune scale and team differences from the results

Add coherent background activity where the investigation needs greater retrieval depth. Increase analytical complexity where teams need more challenge. Preserve the central evidence chain while adjusting optional tasks.

Teams can receive different starting leads within the same case. If they exchange wiki pages, ensure recipients can inspect the cited source records or receive an accompanying source bundle.

Introduce fetch budgets or other access restrictions only if playtests demonstrate a useful role. Avoid making an arbitrary record count or retrieval limit the foundation of difficulty.

## Next concrete deliverable

Draft `CASE_BIBLE.md` with the incident, characters, misleading theory, true sequence, and proof-chain table. Use that document to define the required artifacts, MCP capabilities, physical props, checkpoint rules, and wiki exercises.

The immediate aim is one complete, reviewable case that can be played and tested from opening question through final explanation.
