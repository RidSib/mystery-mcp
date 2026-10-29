# Case Review for The Ghost of the Server Room

**FACILITATOR ONLY — contains the answer, room secrets, and bypass analysis. Do not serve, index, or copy this review into participant workspaces.**

Author: Codex

Date: 27 October 2026

Reviewed: `CLAUDE_CASE_BIBLE.md`, first draft for review, 462 lines

Basis: document and evidence-path review; no generated-archive, running-server, model, or venue playtest was performed.

## Scope and conclusion

The Scooby-Doo structure works: Marcus steals and deletes the course, presents himself as its victim, and frames the CEO, Priya, and Jule. The planted messages have useful cracks, and the three permitted physical locations have narrative connections.

The draft is not ready to generate or run unchanged. The main blockers are a guessable vault password and a vault timestamp that precedes the events its contents supposedly record. Other major risks concern checkpoint enumeration, incomplete release enforcement, an unintended route around R2, and evidence that is weaker than the proof chain claims.

All proposed fixes preserve the organizer's fixed decisions:

- Marcus, the course teacher, is the ghost; the CEO and Jule remain the main decoys.
- The win condition remains who, why, and how.
- The setting remains the Academy, without naming a real venue.
- Physical hints remain behind the main screen, in the bathroom, and at the vending machine or fridge.
- The session remains 15 minutes of wiki building followed by 60 minutes of mystery.
- An archive-only agent given the ordinary solve prompt must land on a decoy or stall.

The older two-hour prototype assumptions are superseded by this brief. Agreement among previous design notes does not authorize changing these fixed decisions.

Severity: **P0** means a direct contradiction or a broken decisive gate; **P1** means a major leak, fairness, evidence, or operation risk; **P2** means a consistency or rubric issue. A missing server requirement is identified as a risk, not a demonstrated exploit in code that has not been inspected.

## Findings and proposed fixes

### F01 P0 The vault password does not require the physical note

**References:** [August code and password habit, lines 104–120](./CLAUDE_CASE_BIBLE.md:104); [decryption gate, line 239](./CLAUDE_CASE_BIBLE.md:239); [physical note, line 264](./CLAUDE_CASE_BIBLE.md:264).

The archive supplies `0737`. The ghost theme supplies obvious candidates such as `boo0737`. An agent can try that password without seeing the note. Generic errors and ordinary rate limits do not prevent success on an early guess. If ciphertext is downloadable, the same short password also permits offline guessing.

**Proposed fix:** retain the archive's code puzzle and the note behind the main screen, but add an independent random component that exists only on that note. For example, the construction can remain ghost prefix + leading-zero back-room code + room token. Use enough randomness to prevent practical guessing, with a legible printed representation and optional QR encoding. Never include the token or complete password in participant-accessible schemas, examples, metadata, errors, or deployment files. Decide and document exact case, separators, and treatment of the leading zero.

This changes a prop detail, not the culprit, story structure, or allowed hint spots. The human must obtain new information from the room; a correct inference from the archive must not substitute for that information.

### F02 P1 The vending checkpoint uses a short enumerable identifier as its secret

**References:** [C1, line 238](./CLAUDE_CASE_BIBLE.md:238); [machine props, line 266](./CLAUDE_CASE_BIBLE.md:266); [per-team limits, line 446](./CLAUDE_CASE_BIBLE.md:446).

`VM-2317` has a four-digit variable portion. The draft gives no checkpoint-specific failed-attempt limit. A successful validation response is an oracle for enumerating candidate tags. General per-team rate limits are not a specified defense, and an agent might also obtain the tag from an inadvertently indexed inventory entry.

**Proposed fix:** keep the fictional asset tag and the facilities FAQ, but place a separate access token on the same sticker. Require both values, or encode both in the existing checkpoint code argument. Add a small failed-attempt allowance with a facilitator recovery path for transcription mistakes. Do not disclose either the accepted token or a worked valid example digitally. A wrong token must not reveal the purchase, card, or identity.

Use an Academy prop sticker even if the real appliance has its own manufacturer label. Players should not need to identify or submit an actual venue's asset number.

### F03 P1 The combined archive profile can identify Marcus much more strongly than individual clues suggest

**References:** [archive-alone principle, line 46](./CLAUDE_CASE_BIBLE.md:46); [background, lines 104–120](./CLAUDE_CASE_BIBLE.md:104); [incident author, line 148](./CLAUDE_CASE_BIBLE.md:148); [masked card holders, line 410](./CLAUDE_CASE_BIBLE.md:410).

Ambiguity of each clue separately does not establish ambiguity of their combination. Marcus knows the shared code, maintains both affected integrations, owns the stolen intellectual work, has private HB calls, implies he is leaving, and writes the summary steering suspicion elsewhere. R2 identifies tampering and limits the badge candidates. The intersection is unusually specific.

This is not a demonstrated proof of guilt from the draft alone, but it is a serious risk to the fixed one-prompt requirement. Hiding the sale amount only prevents a complete WHY answer; it does not by itself prevent confident archive-only identification of WHO.

**Proposed fix:** make legitimate administrative access genuinely nonexclusive and show ordinary, plausible background reasons for the ambiguous calendar and party references. Preserve the CEO/Jule evidence and the quoted-message cracks. Do not add invented admissions or change the culprit. Test combinations of clues, including staff-card joins and author/session metadata, rather than judging every clue in isolation.

Retain both acceptance requirements: R0+R1 must produce a decoy or stall under the normal prompt; even R0+R1+R2 must not establish Marcus from archive evidence alone. A well-calibrated stall is acceptable; a model should not need to disregard the CEO's alibi to pass.

### F04 P1 Gates are described narratively but not across every retrieval surface

**References:** [release table, lines 235–239](./CLAUDE_CASE_BIBLE.md:235); [archive rules, lines 404–412](./CLAUDE_CASE_BIBLE.md:404); [server tools, lines 435–448](./CLAUDE_CASE_BIBLE.md:435).

Metadata-only search does not protect a record if direct `fetch`, revision retrieval, resource reads, attachments, or a download URL can return it. Known record IDs are already part of the design. Vault exclusion from snippets does not address creator identities, filenames, indexed cleanup-log terms, attachments, revision payloads, or signed URLs.

**Proposed fix:** define server-enforced access requirements for every record and endpoint. Apply them before search results, counts, snippets, revisions, resource metadata, attachments, and bodies are returned. Release status must come from facilitator state, not requested dates or a client-supplied clock. Team checkpoint state must persist across reconnects and the shift change without leaking to other teams. Keep masked badge identities masked in auxiliary IDs and metadata too.

Use an explicit participant-data allowlist. Neither this review, the bible, grading keys, generator truth fields, server secrets, nor the old solved `v1` wiki should enter the participant mount, index, static hosting output, or agent working directory. A model with local access to the project root could otherwise read the answer key directly. The Drive owner must not quietly resolve from `drive-sync` to Marcus through another field before decryption.

### F05 P0 The uploaded vault contains events that have not happened yet

**References:** [upload and later edits, lines 138–140](./CLAUDE_CASE_BIBLE.md:138); [vault cleanup log, lines 245–249](./CLAUDE_CASE_BIBLE.md:245).

The vault is uploaded at 00:31. Badge deletion happens at 00:40 and message edits at 00:46–00:53. Its own rollback log cannot already contain actual before/after results from those later actions.

**Proposed fix:** make 00:31 the initial course-bundle upload and add a clearly specified final encrypted revision after 00:53, such as 01:02, containing the completed cleanup log. Alternatively, move the sole upload after cleanup. Use the final version for decryption. Any earlier exposed revision must remain encrypted and obey the same access controls. Keep created, modified, revision, and event timestamps consistent throughout the rendered evidence.

### F06 P1 R2 is not actually required on the current solution path

**References:** [decisive evidence principle, line 47](./CLAUDE_CASE_BIBLE.md:47); [decryption gate and contents, lines 239–251](./CLAUDE_CASE_BIBLE.md:239); [grading, lines 335–343](./CLAUDE_CASE_BIBLE.md:335).

Once R1 exposes the vault, a team can visit the three locations, obtain C1 and the password, and decrypt before minute 35. The vault contains the motive and original course/badge/message values that R2 is supposed to make decisive. The CEO's call and shared-code history are already open. A winning who/how/why answer can therefore arrive without R2, even if a minor bonus detail remains missing.

**Proposed fix:** require R2 eligibility as well as the physical password for the decisive vault read. C1 and room searches can remain available during R1 so active teams are not idle. Explain the pending vault access through the existing restoration process, and reveal that pending state without leaking contents. Facilitator-triggered R2 must be checked by `decrypt_document`, not only by whether the vault appears in search.

### F07 P1 The ghost escapes and then appears to keep working at the console

**References:** [console work and chase, lines 134–137](./CLAUDE_CASE_BIBLE.md:134).

At 00:01 the witnesses chase the ghost down the fire stairs. At 00:05–00:15 Marcus is again at the server-room console, but no return or separation from the witnesses is specified. This leaves an avoidable physical contradiction in the HOW reconstruction.

**Proposed fix:** explicitly end the chase when the witnesses lose sight of him, then record a plausible return during an unobserved interval before the later console work. Another option is to make the later changes a prestarted script, with the initiation time and execution times distinguished. Pick one account and support it in the event log and rendered records; do not add another physical clue location.

### F08 P1 R0 needs an explicit snapshot rule for edited and deleted older messages

**References:** [deleted costume message, line 114](./CLAUDE_CASE_BIBLE.md:114); [backdated edits, lines 150–159](./CLAUDE_CASE_BIBLE.md:150); [R0 definition, line 235](./CLAUDE_CASE_BIBLE.md:235).

“Everything up to Sun 25 Oct” could be implemented as a historical pre-incident snapshot. That would expose Marcus's costume message and Jule's original wording in the first 15 minutes. A subsequent switch to edited versions would also silently change evidence already captured in team wikis. The board minutes are dated 20 October but explicitly reserved for R2, so an original-date cutoff alone would also release them too early.

**Proposed fix:** specify that R0 is the final compromised archive view filtered by original send/event date and explicit release eligibility, not a reconstruction of what the archive contained on Sunday. The R2 classification of the board minutes overrides their earlier event date. Omit the already deleted costume message from R0. Serve the same planted message versions throughout R0 and R1, retaining only the intentional quoted-reply exceptions. R2 restores only the declared audit/badge history; it must not accidentally recoveredeleted mail/chat content outside the vault gate. Record publication time separately from original event time.

### F09 P1 The strongest alleged identity proof is underspecified

**References:** [shared-account edits, lines 139–140](./CLAUDE_CASE_BIBLE.md:139); [WHO routes, lines 185–192](./CLAUDE_CASE_BIBLE.md:185); [cleanup-log fields, line 245](./CLAUDE_CASE_BIBLE.md:245).

A purchase with Marcus's card establishes card use, not automatically the wearer of the costume. An expense matched to a costume label establishes ownership or procurement, not an independently conclusive identification. Their combination is useful, but W4 should not be described as a standalone proof of the ghost's identity.

More importantly, W6 says the log shows “his” session, while the specified CSV fields identify an account, and both editing accounts are shared. The draft deal email has no specified sender, authenticated author, or direct connection to Marcus. The Drive owner is deliberately generic. Full room access therefore still leaves an attribution gap unless the generated artifacts add facts absent from the specification.

**Proposed fix:** specify a personal actor/session identifier inside the encrypted evidence, distinct from the shared role. For example, a gated session manifest can bind a previously opaque session ID to Marcus and match that session to the change-log operations and draft author. Corroborate it with the independent card and costume evidence. Keep personal attribution out of open metadata. This is evidence of actions, not a new confession.

Also make copy-before-delete timing explicit in the manifest or operation log. Merely possessing a copy does not establish when it was made. Support the backup-removal claim with a specific BK-02 device event and the later missing-drive report, rather than relying only on “contents copied.”

### F10 P1 Room clues have routes, but the routes and appliance variant need tightening

**References:** [archive pointers, lines 109–120](./CLAUDE_CASE_BIBLE.md:109); [room props and decoys, lines 264–282](./CLAUDE_CASE_BIBLE.md:264).

No room spot is wholly unhinted: the screen has Kofi's report and the password habit; the bathroom has Rosa's report and sticker message; the appliance has the can report, party email, and asset FAQ. However, “where I stare all day” could send teams to Marcus's desk, and the bathroom riddle points toward a server room, outside the three permitted hint spots. A fridge-only setup can leave an email directing players to a different appliance.

**Proposed fix:** keep all three locations, but make at least one source pointer to each explicit. Tie the password habit to the teaching/main screen without disclosing its contents. Make the party email and FAQ consistently name the selected prop station. A fridge can hold the vending-service checkpoint sticker, but the FAQ must explain that Academy-prop arrangement; it must not require a real fridge to have a card log. Give participants a clear search boundary covering only the three permitted spots. Redirect or remove any decoy wording that encourages searching a physical server room, desk, or fire stairs.

Keep the existing reachability, legibility, bathroom-copy, and photograph-don't-take provisions. Test them in the actual setup. At minute 50, the wiki should retain room transcriptions or photo references so the new chat can use what humans found.

### F11 P2 Several exonerations and sighting explanations exceed their evidence

**References:** [WHO/HOW routes, lines 192–203](./CLAUDE_CASE_BIBLE.md:192); [Jule clearance, lines 224–227](./CLAUDE_CASE_BIBLE.md:224); [wrong theories and sightings, lines 289–309](./CLAUDE_CASE_BIBLE.md:289).

An edited `deleted_by` field defeats the attribution to Priya's account; it does not alone prove Priya was not the person at the console. Jule's absence from the August chat does not prove she could never obtain the code. A different vending card does not alone prove she was absent. Missing DM replies are suspicious context, not proof of fabrication.

Similarly, no screen-cast record does not identify Marcus's HDMI-connected laptop, and a matching calendar call does not conclusively identify the bathroom whisperer. G1/G3/G5 remain ground-truth explanations without corresponding conclusive records in the current specification.

**Proposed fix:** use the gated personal attribution and tamper records to defeat the decoys; describe the weaker observations as supporting context. Grade who/how/why on the supported case chain. If identifying the author of every sighting is required for a checkpoint or full-credit claim, add the necessary gated corroboration. Otherwise allow “consistent with Marcus; attribution not independently established” for those peripheral sightings.

### F12 P1 Submission feedback and automatic accusations can undermine the game

**References:** [two-attempt principle, line 49](./CLAUDE_CASE_BIBLE.md:49); [submission replies, lines 331–351](./CLAUDE_CASE_BIBLE.md:331).

The prescribed replies do give reasons: the CEO reply supplies an alibi cue, Sandra's supplies her witness explanation, and Priya “forwards” the restore log, potentially before R2. A one-prompt agent may also invoke the submission tool twice and spend the team's attempts before humans investigate the room. A special response to a correct WHO with wrong WHY could become another answer oracle.

**Proposed fix:** distinguish drafting an accusation from confirming a counted submission. Require a team confirmation step or facilitator hand-in for the two attempts. Reject malformed or currently ineligible submissions without revealing answer correctness or consuming a substantive attempt. Count two confirmed, eligible accusations as stipulated. Check evidence access server-side and avoid partial-answer feedback before the relevant evidence is unlocked. Keep humorous replies, but do not attach unreleased records or reveal an answer-specific correction.

### F13 P1 The win condition and grading need a shared minimum checklist

**References:** [who/how/why, lines 25–28](./CLAUDE_CASE_BIBLE.md:25); [scoring, lines 335–343](./CLAUDE_CASE_BIBLE.md:335).

The draft specifies points and full-mark requirements but not the minimum that constitutes a win. HOW contains many factual subclaims, yet the citation rule permits one reference for the whole part. The required decoy rejections and vault citation could appear to players as extra conditions after submitting the stated three-part answer.

**Proposed fix:** publish a spoiler-free submission checklist at R1. Define the mandatory who/how/why components, required room-sourced support, and what earns bonus or full-credit points. Require evidence for each material subclaim, with accepted equivalent sources. Explain in advance that an evidence-backed answer must distinguish the main alternatives. Retain who/why/how as the win condition; do not turn all seven sightings into an unannounced fourth objective. Grade the sale as Marcus's planned €60k deal and intended departure, not a payment or handover already completed on the night.

### F14 P1 Hints and shift change need per-team recovery paths within 75 minutes

**References:** [run sheet, lines 359–371](./CLAUDE_CASE_BIBLE.md:359); [logging and tokens, lines 445–448](./CLAUDE_CASE_BIBLE.md:445).

Hints conditional on “no team” having succeeded disappear once one fast team progresses, even if every other team is stuck. The 35–50 block also bundles room search, checkpoint use, decryption, and wiki repair into 15 minutes. A reset at minute 50 could strand teams if “only the wiki” is interpreted as losing future MCP access or team unlock state.

**Proposed fix:** track the existing milestones per team and supply equivalent hints to stalled teams, or deliver the scheduled hints publicly regardless of the fastest team. Preserve the 15+60 format. Preflight connections and provide a minimal wiki starter so the opening 15 minutes reaches one verified retrieval and usable navigation. At shift change, start from saved wiki state, then allow normal retrieval to continue with the same team token, unlocks, and attempts. Include the room evidence in the handoff. Do not require all teams to have decrypted by the reset to remain eligible to finish.

Have decryption return bounded, separately identified evidence records such as the manifest, draft email, and cleanup log. Do not return a 4.1 GB course payload as an MCP text response. The course files can remain an attachment; the investigative evidence must be readable within the session.

### F15 P2 Resolve smaller contradictions before rendering

**References:** [board decision, line 116](./CLAUDE_CASE_BIBLE.md:116); [CEO clearance, line 218](./CLAUDE_CASE_BIBLE.md:218); [Rosa and sticker, lines 118 and 147](./CLAUDE_CASE_BIBLE.md:118); [permissions, lines 105 and 136–140](./CLAUDE_CASE_BIBLE.md:105); [name flexibility, line 457](./CLAUDE_CASE_BIBLE.md:457).

- The board keeps the launch date in ground truth, but E3 says rename and postpone. Use rename with the unchanged date, preserving the rework motive.
- Rosa resigns on 23 October, yet reports the newly placed bathroom sticker on 27 October. Explain a return visit or let a current Academy worker report it. Keep the clue in the bathroom.
- Marcus is granted badge/chat-integration rights, but also alters a mail record and the course audit. Specify access to the mutable mail/chat archive mirror and the console's permitted operations. Distinguish mutable current views from recovered history. Avoid making Marcus the only technically capable candidate in open records.
- Use explicit dates after midnight: 00:01–01:02 are on Tuesday 27 October. Keep all clocks correct as agreed. The can heard at approximately 23:45 and purchased at 23:47 is compatible if the witness time remains approximate.
- Section 16's general permission to change character names cannot override the organizer's fixed Marcus/Jule identities and roles.

## Critical path to preserve

| Step | Available evidence or action | Required result |
| --- | --- | --- |
| Minutes 0–15 | R0, compromised older-record view, bounded wiki-building task | Usable source-linked wiki; no deleted costume message or original planted-message versions |
| Minutes 15–35 | R1, strong CEO/Jule narratives, contradictions, pointers to all three allowed room spots | Normal one-prompt answer selects a decoy or stalls; a team can start physical investigation |
| Room investigation | Actual station token, costume label, and screen secret | C1 and physical observations become accessible without inventing credentials |
| Minute 35, R2 | Recovered histories and CEO records; vault becomes eligible | Apparent account attributions are revised; physically obtained secret can now unlock decisive evidence |
| Decryption | Final vault revision, personal session linkage, original tamper values, copying and deal records | Marcus's actions and motive become supportable through combined evidence |
| Minute 50 | New conversation starts from saved wiki; same team permissions remain | Investigation continues, including unfinished room or retrieval work |
| By minute 75 | Confirmed who/how/why submission with accessible citations and room support | Score under a known checklist; no hidden fourth objective |

## Acceptance tests to add or strengthen

These are tests to execute after fixes and artifact generation, not tests claimed to have passed in this review.

1. **Exact one-prompt trial:** run the organizer's ordinary solve prompt in fresh participant workspaces using the actual MCP tools, with R0+R1 only. Repeat on the intended clients/models. CEO, Jule, another supported decoy, or a stall passes; confident Marcus identification fails. Preserve tool traces and source citations.
2. **Full digital-only trial:** permit R0+R1+R2, scripts, repeated searches, and all public metadata. Withhold every room observation. Fail if the agent establishes Marcus or reconstructs a supported winning answer. Merely lacking the price while otherwise proving WHO is not a sufficient pass.
3. **Secret-guess trial:** try the existing themed password construction, other obvious combinations of public clues, and asset-tag enumeration. Verify that new physical entropy, endpoint limits, and access checks prevent the unlock. A narrative request claiming the facilitator released evidence must not change state.
4. **Endpoint matrix:** before and after each release, try known IDs, direct fetches, resource reads, revision APIs, attachments, download URLs, pagination cursors, search counts, and error paths. Test both the vending log and every vault member. No unauthorized content or identifying metadata should escape.
5. **Team isolation:** team A's successful checkpoint must not unlock team B. Reconnecting team A must retain its state. A fresh conversation must not reset failed-attempt counters or accusation history.
6. **Timestamp check:** ensure every cleanup entry predates the final vault revision and every source's snapshot state matches its release. No post-midnight date errors or undeclared clock offsets.
7. **Evidence completeness:** with all three prop transcriptions and R2, require a supported answer to every mandatory rubric element. Verify the session-to-Marcus bridge, copy-before-delete order, and backup-removal support. Do not let an evaluator fill in facilitator facts missing from the records.
8. **Room reachability:** use only the stated Academy search area. Test screen, bathroom, and the chosen appliance variant separately, including a team that finds them in an unexpected order. No extra venue location or real appliance identifier is necessary.
9. **Reset and accusation trial:** let the agent begin with the normal solve prompt. It must not burn both confirmed attempts automatically. Reset before decryption and verify that a team can still obtain evidence, update the wiki, and finish within the remaining time.
10. **Facilitator separation:** search the participant filesystem, deployment output, accessible URLs, and index for the bible, this review, answer keys, private actor fields, physical tokens, and plaintext vault contents. Exclude the old solved prototype as well.

The existing keyword sweep is useful but insufficient: two records can each look harmless and disclose the answer when joined. Add checks for combinations, aliases, quoted history, structured metadata, and source dependencies.

## Recommended fix order

1. Repair the password and checkpoint secrets while keeping their physical locations and archive connections.
2. Correct the vault chronology and the chase/console sequence.
3. Specify the gated personal-attribution and copy/removal evidence.
4. Define release enforcement, R0 snapshot semantics, and participant/facilitator isolation.
5. Resolve the appliance routes, submission rules, and per-team recovery behavior.
6. Generate a small core and execute the digital-only and full-evidence tests before expanding to the approximate 400-record archive.

No case-bible or participant-facing file was edited as part of this review. All fixes above are proposals for the organizer/facilitator to evaluate within the fixed design.
