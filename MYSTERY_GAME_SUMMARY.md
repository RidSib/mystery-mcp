# Mystery Game with MCP and LLM Wikis

Discussion summary — 25 October 2026

## Concept and purpose

Participants investigate a mystery hidden across a fictional organization's digital records. An MCP server exposes information that mimics several services: email, calendars, shared documents such as Google Drive files, and meeting transcripts. The reference point is *Her Story*, with the investigation unfolding mainly through documents and records.

Participants build a second brain, or LLM wiki, to organize discoveries and help solve the case. The wiki becomes their detective notebook: people, relationships, timelines, claims, hypotheses, contradictions, and links to original evidence.

The experience has three goals: enjoyment, learning, and challenge. Escape room mechanics, physical clues, staged document releases, and smaller analytical tasks can be adjusted to balance those goals. The mechanics below are options discussed for development; the story, workshop format, and final rules remain open.

## What makes the format promising

The mystery can live in the connections between sources. An email records an intention, a calendar records a plan, and a transcript records what someone said or understood. Their differences can reveal a contradiction that no single document explains.

Different services should contribute different kinds of evidence. Official documents may present an agreed narrative, while emails expose private concerns and transcripts capture misunderstandings or accidental disclosures. Each artifact should remain plausible on its own.

A strong investigation would give participants a concrete starting question, several plausible explanations, and reasons to revise their early theory. The final explanation should depend on multiple sources. A single hidden confession would reduce the value of the surrounding archive.

Teams could organize their wikis differently. A timeline, a network of people and relationships, or a ledger of claims and contradictions might each reveal useful connections. The game can support that freedom while providing beginners with a small starting template.

## Novelty and positioning

Investigating digital records is an established game format. Delivering a mystery through MCP also has precedents. The strongest distinction in this concept is that participants build and maintain their own LLM wiki while investigating a simulated workplace across multiple services.

Relevant precedents discussed were:

- [The Roottrees Are Dead](https://play.google.com/store/apps/details?id=com.theroottrees.android), which involves cross-referencing fictional records to reconstruct family relationships.
- [Murder.Ai](https://huggingface.co/spaces/MCP-1st-Birthday/Murder.Ai/blob/main/README.md), whose project documentation describes an MCP-based mystery with evidence tools and suspect interrogation.
- [Mastra's detective game](https://mastra.ai/blog/the-detective-game), which uses AI agents as suspects in an investigation centered on conversation.

These establish adjacent approaches. The search did not establish that the complete proposed combination is unique, so a claim of being the first would be premature.

A possible description is: **A detective game where you build an AI second brain to uncover a mystery hidden across a fictional company's digital life.**

## Difficulty for LLMs and for players

The central design risk is an agent retrieving the archive and producing a supported solution immediately. Difficulty should be tested against an LLM with search, scripts, persistent notes, and repeated attempts.

Three kinds of difficulty need separate treatment:

| Type | Example | Effect |
| --- | --- | --- |
| Access to evidence | A physical key is needed to decrypt a document | Essential information remains unavailable until the team acts |
| Interpretation of evidence | Some transcript references to Max actually refer to Barbara | The team must reconstruct meaning from independent sources |
| Progression and pacing | A new document appears after a checkpoint or time interval | Controls when the investigation can advance |

An access barrier can guarantee a required step without making the eventual reasoning difficult. Likewise, a timed release can extend the session even if the new evidence is quickly understood. Both can still serve the game well.

Contradictions and scattered clues alone do not reliably prevent a capable agent from solving the case. Research on [implicit evidence detection](https://aclanthology.org/2024.findings-emnlp.11/) and [contradictions in detective narratives](https://arxiv.org/abs/2505.15712) identifies challenging tasks for the evaluated models, but does not establish the difficulty of this particular game.

## Mechanics discussed

### Physical clues and encrypted documents

Physical clues can connect activity in the room to evidence in the digital archive. A key in an envelope or locked box can make human observation and physical participation necessary.

Encryption deserves a substantial role because it can support access control, tool use, and a meaningful expansion of the wiki. Two implementations teach different things:

| Implementation | Main learning opportunity |
| --- | --- |
| Enter a code into an unlock tool | Discovering and using a tool, and understanding access boundaries |
| Retrieve ciphertext and use a supplied decryption tool with a key | Following an encryption and decryption workflow, inspecting the output, and ingesting new evidence |

Participants need not implement cryptography. The visible workflow could be: retrieve the encrypted artifact, discover the tool, inspect its inputs, obtain the key, decrypt, read, and update the wiki.

The encrypted content must remain unavailable through search snippets, previews, or other endpoints. If a short code can be submitted automatically, attempts need to be controlled to preserve the intended puzzle.

The key-finding activity determines much of the investigative difficulty. Once a valid key and working tool are available, decryption can be straightforward and still provide a valuable learning moment. A photographed cipher or word puzzle may also become easy for a model once uploaded.

Decrypted material should remain available afterward with a stable source reference, so teams can cite and revisit it. The strongest payoff would be evidence that changes their understanding of earlier records.

### Corrupted names and identity reconstruction

The proposed example was that occurrences of Barbara had been replaced with Max, changing the apparent meaning of many documents.

If the replacement rule is known and there was no genuine Max in the affected material, reversing it is straightforward with a script. If Max already existed, the transformation merges two identities: some references genuinely mean Max, and others mean Barbara. Replacing every Max with Barbara would introduce new errors.

A stronger version would affect a discoverable subset of sources, such as exported meeting transcripts. Intact email addresses, calendar identifiers, original attachments, or unaffected records would let teams infer which references belong to whom.

The corruption should follow a consistent rule and leave enough independent evidence for a supported reconstruction. Arbitrary changes could produce several equally valid answers.

### New evidence over time

Documents could appear at scheduled times or after teams complete challenges. Withholding essential evidence can prevent a fully supported early solution.

Adding another fact may be easy for an LLM to handle. A stronger learning mechanic introduces evidence that changes an established conclusion and requires the wiki to be repaired. For example, a later export report could reveal the name corruption, undermining several claims derived from transcripts.

This creates a reason to preserve sources and distinguish facts from hypotheses. Research on [belief revision](https://aclanthology.org/2024.emnlp-main.586/) found difficulties in the evaluated models, but rebuilding the analysis from the complete archive may still let an agent recover quickly.

### Ambiguous questions

An opening such as “Something illegal happened here. What was it?” broadens the investigation. It also gives an LLM room to generate many hypotheses, so ambiguity alone offers limited resistance.

A fairer challenge would include several suspicious activities but enough evidence to distinguish the central incident. A final submission could identify the act, participants, timeline, supporting sources, and why the strongest alternative explanation fails.

For beginners, a concrete incident offers an easier entry point. Its deeper meaning can emerge later.

### Suspect checkpoints and clue rewards

Teams could unlock evidence by identifying three suspects. Naming plausible suspects may be easy, and unlimited submissions could turn the checkpoint into a guessing exercise.

A more useful checkpoint would require each suspect's connection to the incident, source citations, and an unresolved contradiction. The reward then follows demonstrated investigation.

Feedback also conveys information. The design should specify whether a checkpoint confirms that particular people are correct suspects or simply accepts a well-supported theory as sufficient progress.

## Smaller analytical challenges

Additional tasks can provide verifiable progress before teams understand the whole mystery. Examples proposed were counting emails about dogs or cats and counting each manager's calendar entries per week. Completing these could reveal further clues.

| Challenge | Learning opportunity |
| --- | --- |
| Count emails mentioning dog or cat | Complete retrieval, pagination, deduplication, and literal matching |
| Count emails about dogs or cats | Defining a topic, classifying messages, and reviewing ambiguous cases |
| Count calendar entries per manager per week | Dates, grouping, structured data, and reproducible calculations |
| Investigate an unusual change in meeting totals | Connecting quantitative patterns to narrative evidence |

“Mentions” and “is about” are different questions. A topic challenge needs rules for overlapping categories, names such as Cat, and messages about pets that omit the target words. Introductory challenges can specify those rules; later challenges can ask teams to justify their own definition.

Calendar tasks should define whether meetings count by organizer or attendee, how canceled and recurring meetings are treated, and the relevant week boundaries and timezone. A changing archive also needs a defined snapshot or cutoff for graded answers.

LLMs can help construct and explain calculations, while scripts or structured queries calculate over the underlying records. Wiki summaries may omit individual messages or events, so these tasks can teach when to return to source data.

A submission could contain the answer, the method and inclusion rules, and a check against example records or retrieval completeness.

Analytical tasks work best when the result directs the investigation. A sudden change in one manager's schedule could identify the week to examine. Emails from that week could explain the change and lead to the next clue. Optional tasks and several routes to essential evidence could prevent one counting exercise from stalling the room.

## Learning goals

### Understanding MCP

Participants should connect the server, inspect its available capabilities, and examine at least one actual request and result. The aim is to understand how the application obtains information and what the connection enables.

MCP servers can expose tools, resources, and prompts. Tools execute operations and can retrieve information; resources expose contextual data; prompts provide reusable interaction templates. [Official MCP server concepts](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/docs/2026-07-28/learn/server-concepts.mdx)

The game can demonstrate that connecting a source gives access without implying that the model has already read every record. If all interaction stays hidden behind a chat interface, participants may finish without understanding MCP's role.

Using MCP and building MCP servers are separate learning goals. The proposed format fits learning to use connected sources. Teaching server development would need an additional exercise, such as exposing a new fictional evidence source.

### Building and maintaining an LLM wiki

Participants should practice organizing people and events, linking related information, preserving source references, recording uncertainty, separating reported claims from established facts, and revising conclusions.

For example, “Lea claimed Jonas canceled the meeting” should retain its attribution. Turning it into “Jonas canceled the meeting” would erase a distinction the mystery may depend on.

A small starter example could include a person page, a timeline entry, and a hypothesis with evidence links. Teams could extend it in their preferred structure.

A handoff to another investigator or a fresh conversation can demonstrate the value of persistent knowledge. Continuing from the saved wiki reveals whether earlier discoveries were captured clearly enough to reuse.

### Participation and transferable skills

One confident operator could otherwise perform all the technical work. Rotating responsibility for retrieval, wiki maintenance, and challenging the current theory would give more participants practical experience.

Success includes participants being able to repeat the workflow on another collection of records: connect a source, retrieve evidence, build durable knowledge, verify it, and revise it. A short debrief can connect each game mechanic to that workflow.

## Possible combined investigation

One illustrative sequence brings several mechanics together:

1. Teams connect the MCP server, find an email and calendar event, and inspect how they were retrieved.
2. They build an initial wiki and identify several plausible suspects.
3. Calendar analysis reveals an unexplained meeting involving three managers.
4. That discovery points to a physical envelope containing a decryption key.
5. Teams use a supplied tool through MCP to decrypt meeting minutes.
6. The minutes reveal a corruption rule affecting transcript identities.
7. Teams revisit the affected wiki claims and revise their theory.
8. They submit an explanation with citations and discuss their method.

This is a proposed example, not an agreed plot. Its purpose is to make retrieval, analysis, physical discovery, decryption, and wiki maintenance contribute to the same investigation.

## Prototype and playtesting

A suggested starting scope was five characters, one central incident, four simulated services, and approximately 30–50 artifacts. This is a provisional scale for testing the investigation before expanding the archive.

Playtesting should distinguish the difficulty of the complete case from progression created by withheld evidence. Give a capable agent all currently accessible tools and records, then test it again with the complete archive. Also test whether rebuilding its analysis after a reveal bypasses the intended revision challenge.

Observe where human teams stall, whether all participants contribute, which tasks feel rewarding, whether the wiki helps them continue, and whether they can explain how they obtained their answers. Completion time alone will not measure learning or enjoyment.

The number and complexity of optional challenges can then be adjusted while preserving the central story. Effective LLM use should help participants advance, and the challenges should reward skills that remain useful outside the game.

## Open design choices

- Audience experience, team size, session length, and supported LLM applications.
- Whether participants only use MCP or also build or extend a server.
- How much wiki structure and tooling to provide at the start.
- The story, central incident, suspects, and required final explanation.
- Which evidence is initially available, physically unlocked, released by time, or earned through checkpoints.
- Whether the encryption stage demonstrates unlocking access or actual decryption of ciphertext.
- Rules and validation for analytical tasks, suspect submissions, and clue rewards.
- How optional routes, facilitator hints, and shared physical clues work across teams.
- How to assess learning as well as the quality of the final solution.
