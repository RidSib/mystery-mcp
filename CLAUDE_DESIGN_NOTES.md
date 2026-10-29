# Design Notes on the Mystery Game

Author: Claude (Opus 5.5), responding to `MYSTERY_GAME_SUMMARY.md`
Date: 25 October 2026

These notes assume data is effectively unlimited. The archive can be as large as the design needs, and it is generated on purpose rather than written by hand. Many of the summary's open questions look different once that's true.

## 1. Scale is the difficulty lever

The summary treats an LLM reading the whole archive and solving the case as the central risk. That risk comes from a small archive. At 30–50 artifacts, everything fits in one context window. At 50,000 it doesn't, and the game changes:

- **No agent can read everything.** Players have to search, sample, filter and index. Retrieval strategy becomes the skill being tested.
- **The wiki becomes necessary.** With a small archive, the wiki is optional bookkeeping. With a huge one, it's the only way a team or an agent keeps track of what it has found across sessions and context resets. The game's second goal then follows from its structure without any extra rule.
- **Counting has to be done properly.** Nobody can eyeball "how many emails are about cats" across 40,000 messages. Teams have to write a query or script, define their rules and check that retrieval was complete. Answers based on search snippets will be visibly wrong.
- **Difficulty is a dial.** Archive size, noise ratio and how spread out the clues are become tunable parameters. You no longer have to hand-craft obstacles.

This resolves the tension in the summary. The game shouldn't try to beat the model at reasoning. It should be too large to solve without the workflow it's meant to teach: connect, retrieve systematically, build durable knowledge, verify, revise.

## 2. Generate from a world model, then render

Don't generate documents directly. Generate a **ground-truth event log** first: who did what, when, with whom, who knew what, and who lied about what. Then turn that log into emails, calendar entries, transcripts, documents and board updates.

This gives you:

- **Consistency.** Every artifact comes from the same facts, so contradictions occur only where you intend them, such as lies, misunderstandings and corruption.
- **Automatic answer keys.** Counts, timelines and identity mappings can be computed from the log. Grading becomes a lookup.
- **Fairness checks.** You can prove the case can be solved: for each required conclusion, list the artifacts that support it and confirm they exist and can be found.
- **Planted corruption with a known inverse.** The Barbara/Max swap becomes a transformation applied to one rendering channel, such as transcript exports. Its scope is exact and its reversal can be checked.

## 3. The main generation risk: noise and signal must look the same

If clue documents are written carefully and filler is mass-generated, an agent will tell them apart. It can use style, length, vocabulary, timestamps or metadata. Then it ignores the noise and the archive shrinks back to 40 documents.

To prevent that:

- Render clues and filler through **the same pipeline, prompts and model**. The difference should be only in the event log they come from, never in how they're written.
- Give the filler **its own storylines**: office politics, a product launch, a dog that keeps getting mentioned. Make some of them suspicious enough to be real red herrings.
- Check the distributions. Run a classifier over the archive to see whether "clue vs. filler" can be predicted from surface features. If it can, regenerate.
- Mix the ordering of IDs, timestamps and authors so that clue artifacts don't cluster in time or ID ranges.

## 4. A different case for every team

Since generation is cheap, give each team, or each session, **its own seed**: the same story structure with different names, dates, culprit or corruption rule.

- Teams can't copy each other's answers.
- The game can be replayed and run again at future workshops.
- You can playtest against agents many times without memorization. A model that solved seed 17 gets nothing from it on seed 18.
- Facilitators still run one story structure, so hints and the debrief stay consistent.

## 5. Make the LLM necessary but not sufficient

At scale, the LLM is needed: no human team can work through the archive without it. Keep it insufficient by putting a few decisive steps outside its reach:

- **Physical keys** for the decryption stage. The key never exists in the digital archive.
- **Definitional decisions** made by people: what counts as "about cats", which week boundaries apply. The team must state and defend its rule. The model can propose a rule but can't settle it.
- **Belief revision by reveal.** A later release, such as the corruption report, invalidates claims across thousands of transcripts. A team with a wiki that tracks sources can repair it in a targeted way. A team without one has to start over. At small scale that's cheap. At large scale it costs real time, which is exactly the lesson.

## 6. A forced wiki handoff

Make the handoff compulsory. Halfway through, each team:

- swaps wikis with another team, or
- starts a fresh LLM conversation that can read only its own wiki.

At this archive size, starting again from the raw data is too slow, so the wiki's quality decides how fast a team recovers. It's the clearest way to make the value of persistent knowledge felt rather than explained.

## 7. Structured, machine-gradable submissions

The answer key comes from the event log, so the final answer and the checkpoints should be structured:

- **Final answer:** act, participants, timeline, at least three cited artifact IDs, and the strongest alternative with the artifact that rules it out.
- **Counting challenges:** the number, the inclusion rule, and the query or script used. Grade the number against the key computed for the team's stated rule, so a defensible definition isn't marked wrong.
- **Suspect checkpoints:** each suspect with one cited link to the incident. Validate citations automatically: the artifact exists and actually mentions the suspect.

This keeps grading quick during a live session and grades the method as well as the answer.

## 8. Write the proof chain before building anything

The summary is still mostly a list of mechanics. The next concrete step:

1. Choose the central incident.
2. Write the **proof chain**: the minimum set of facts that together prove it, and the facts that support the best false theory.
3. Assign each fact to a channel and a gate: openly available, hidden by scale, behind corruption, behind encryption, or released by time.
4. Only then build the event-log generator and the renderers.

Every mechanic should protect a link in that chain. Any mechanic that doesn't can be cut.

## 9. Playtest with agents at scale

Because cases are seeded and keys are automatic, playtesting can be automated:

- Run a capable agent over many seeds and several archive sizes. Record where it fails, how far it gets, and how long it takes.
- Find the archive size at which an unaided agent stops solving the case but an agent using a good wiki workflow still does. That gap is the game.
- Then playtest with humans to tune enjoyment, which the automated runs can't measure.

---

*Written by Claude (Opus 5.5). These are design suggestions, not decisions; the story, format and rules remain the team's call.*
