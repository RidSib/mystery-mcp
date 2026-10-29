# Review of the Second Draft of The Ghost of the Server Room

**FACILITATOR ONLY — contains the solution, physical secrets, and bypass analysis. Do not include this review in participant files, indexes, or deployments.**

Author: Codex

Date: 27 October 2026

Reviewed: `CLAUDE_CASE_BIBLE.md`, second draft, 563 lines

Compared against: `CODEX_CASE_REVIEW.md`, findings F01–F15

## Verdict and scope

**Nine findings are fixed at specification level; six are partly fixed; none is wholly unaddressed.** The largest v1 contradictions are repaired: the vault follows cleanup, the chase permits a return to the console, R0 has an explicit snapshot rule, and the vault is gated on R2 as well as the room.

The remaining important issues are conditional offline password guessing, the trust basis of the personal session binding, a revealing accusation-response branch, and inconsistent grading thresholds. V2 also introduces a literal conflict between its digital-secret prohibition and the required photo/transcription handoff.

This is a review of the bible, not a successful server or agent playtest. “Fixed” means the document now supplies a coherent fix to the original finding. It does not certify an uninspected implementation. The bible correctly states that its acceptance tests have not run.

The fixed design is preserved: 75 minutes comprising 15 minutes of wiki building and 60 minutes of mystery; the teacher as the ghost; the CEO and marketing lead as the main decoys; who/why/how as the win condition; the Academy as the setting; and the three allowed physical hint locations. Normal archive-only solving must land on a decoy or stall. Names may change; roles may not. The organizer's latest instruction supersedes the name restriction in the previous review.

## Finding by finding

All source links below refer to v2 line numbers.

| Finding | Rating | Reasoning and any remaining work |
| --- | --- | --- |
| **F01 — guessable vault password** | **partly fixed** | The independent six-character room token and ten-attempt limit close the obvious online `boo0737` guess. However, the document does not explicitly prohibit obtaining the encrypted file before unlocking it, nor specify offline password protection. A six-character alphanumeric token has only about 30–31 bits of uncertainty. Online limits do not apply to a downloaded ciphertext. Clarify the download policy or strengthen the physical token and encryption setup. See [lines 290–292](./CLAUDE_CASE_BIBLE.md:290), [336](./CLAUDE_CASE_BIBLE.md:336), and issue V2-01 below. |
| **F02 — enumerable vending checkpoint** | **fixed** | The checkpoint now requires both a fictional drinks-station asset tag and an independent service PIN, with five failed attempts and facilitator recovery. The same Academy sticker works on the selected appliance without using its real label. This adequately closes simple asset-tag enumeration for the stated online interface, subject to implementation. See [288](./CLAUDE_CASE_BIBLE.md:288) and [317–319](./CLAUDE_CASE_BIBLE.md:317). |
| **F03 — combined archive profile singles out Marcus** | **partly fixed** | Shared integration privileges, the Halloween Bash meaning of HB, and the holiday reading of the party message are substantive improvements. They weaken the original inference chain. However, code knowledge plus integration privileges still narrows heavily toward the teacher and tech administrator, while the incident-summary authorship and personal grievances distinguish the teacher. No trial has established the fixed one-prompt outcome. Keep this open until combination and normal-prompt tests pass; the text alone does not demonstrate an archive-only proof of Marcus. See [97–102](./CLAUDE_CASE_BIBLE.md:97), [140–157](./CLAUDE_CASE_BIBLE.md:140), and [502–508](./CLAUDE_CASE_BIBLE.md:502). |
| **F04 — incomplete gate enforcement and facilitator leakage** | **fixed** | The access rules now cover search, counts, snippets, fetch, revisions, resources, attachments, errors, facilitator-controlled releases, persistent team state, and an explicit participant-data allowlist. Opaque session IDs and masking are also specified. This addresses the original missing contract; actual enforcement still needs the endpoint tests. See [488–491](./CLAUDE_CASE_BIBLE.md:488) and [537–542](./CLAUDE_CASE_BIBLE.md:537). The contradictory scope of the secret prohibition is a separate v2 issue. |
| **F05 — vault records its own future** | **fixed** | The single upload is now 01:02, after badge deletion at 00:40 and the final message deletion at 00:53. The original future-event contradiction is gone. The failed-sync explanation still needs a precise recovery source, but does not undo the repaired event ordering. See [180–182](./CLAUDE_CASE_BIBLE.md:180) and [296–302](./CLAUDE_CASE_BIBLE.md:296). |
| **F06 — solution bypasses R2** | **fixed** | The vault appears in R2 and the decryption operation explicitly refuses access before R2. Early room discovery and C1 remain possible without yielding the decisive vault evidence. This puts R2 on the intended solution path. See [289–290](./CLAUDE_CASE_BIBLE.md:289) and [531](./CLAUDE_CASE_BIBLE.md:531). |
| **F07 — fleeing ghost continues at the console** | **fixed** | The witnesses lose sight of the ghost at 00:03, remain at the lobby phone from 00:04–00:19, and a second keypad event supports re-entry at 00:05. Copying can continue while Marcus is away and finish after his return. See [170–178](./CLAUDE_CASE_BIBLE.md:170). |
| **F08 — R0 exposes pre-cleanup originals** | **fixed** | R0 is expressly a release-filtered post-cleanup view, not a Sunday historical snapshot. The deleted costume message stays absent, the planted versions remain stable, and the October 20 board minutes remain R2 despite their date. Restoration excludes mail/chat originals. See [278–286](./CLAUDE_CASE_BIBLE.md:278). |
| **F09 — personal attribution and copy/removal evidence missing** | **partly fixed** | The personal operator/host header, matching opaque console session, private email author, copy completion before deletion, and BK-02 event now exist in the specification. But the supposedly decisive identity binding is a header on Marcus's own manifest and script log, not yet an independently sourced authenticated session record. In a case about forged attribution, that trust distinction matters. See [228–235](./CLAUDE_CASE_BIBLE.md:228), [243–246](./CLAUDE_CASE_BIBLE.md:243), and [293–300](./CLAUDE_CASE_BIBLE.md:293). See V2-02. |
| **F10 — unclear room routes and appliance variant** | **fixed** | The screen pointer is explicit, Ines supplies the bathroom pointer, the party/FAQ route leads to the configurable drinks station, and the decoy riddle stays in the bathroom. The fictional sticker and the existing reachability/photo rules make the routes coherent. Test the chosen physical arrangement; also clarify that the permitted search area includes the bathroom if it is outside the teaching room. See [157](./CLAUDE_CASE_BIBLE.md:157), [189](./CLAUDE_CASE_BIBLE.md:189), [315–335](./CLAUDE_CASE_BIBLE.md:315), and [455–456](./CLAUDE_CASE_BIBLE.md:455). |
| **F11 — weak observations treated as proof** | **partly fixed** | The main chain now distinguishes proof from support, Priya is no longer cleared merely by a changed field, and G1/G3/G5 accept uncertain attribution. However, G6 still calls Marcus's purchase “established” from card 0412, while W3 correctly says the record establishes card use rather than the wearer. W6 also declares a lie from that same card record. E3 says the board decision “removes motive,” although it only weakens one proposed motive. Align those claims with the improved evidence standard. See [230–233](./CLAUDE_CASE_BIBLE.md:230), [261](./CLAUDE_CASE_BIBLE.md:261), and [357–365](./CLAUDE_CASE_BIBLE.md:357). |
| **F12 — revealing feedback and autonomous use of attempts** | **partly fixed** | Drafting is now uncounted, and the old alibi/restore-log replies are removed. But wrong-person replies name the suspect while correct-WHO/weak-HOW-or-WHY gets a distinct generic response, creating a correctness side channel. A reusable table PIN also stops confirmation only while the agent does not know it; it does not establish per-draft human consent once supplied. See [387–389](./CLAUDE_CASE_BIBLE.md:387) and [414–422](./CLAUDE_CASE_BIBLE.md:414). See V2-03. |
| **F13 — unclear minimum win and citation standard** | **partly fixed** | V2 defines a minimum win, full marks, per-subclaim citations, and planned rather than completed sale. However, the minimum accepts any two HOW parts, including entry and disguise without the actual copy/deletion/removal part. WHO can also be awarded through undefined “supporting routes,” whereas the proof chain calls W1 the proof. The participant checklist does not state the minimum/full-credit distinction. See [235](./CLAUDE_CASE_BIBLE.md:235) and [393–413](./CLAUDE_CASE_BIBLE.md:393). See V2-04. |
| **F14 — global hints and reset can strand teams** | **fixed** | Hints are now per team; preflight is outside the active 75 minutes; team state and room evidence survive the reset; undecrypted teams remain eligible; and decryption returns four small evidence records. These fix the original structural issues. The new minute-50 hint has a dependency mismatch addressed below. See [292–300](./CLAUDE_CASE_BIBLE.md:292) and [428–447](./CLAUDE_CASE_BIBLE.md:428). |
| **F15 — smaller factual and permission contradictions** | **fixed** | Rename with an unchanged launch date is consistent; Ines now reports the sticker; the communications mirror includes mail and chat; console access is explicit; midnight dates are labelled; and names remain placeholders while roles stay fixed. This follows the organizer's updated naming instruction. See [97–100](./CLAUDE_CASE_BIBLE.md:97), [153](./CLAUDE_CASE_BIBLE.md:153), [172–189](./CLAUDE_CASE_BIBLE.md:172), and [558](./CLAUDE_CASE_BIBLE.md:558). |

## New problems and residual risks in v2

P1 means resolve before generating the final evidence or running the session. P2 means clarify before rendering or printing. Conditional risks below are not claims of successful attacks against a running server.

### V2-01 P1 The strengthened password is only a guaranteed barrier in an online-only design

**References:** [vault availability and decryption, lines 289–292](./CLAUDE_CASE_BIBLE.md:289); [attachment access rules, line 538](./CLAUDE_CASE_BIBLE.md:538).

The obvious dictionary guess is fixed. The unresolved path is: R2 exposes the encrypted file; an agent downloads its ciphertext through fetch or an attachment URL; it attempts the small room-token space locally; server attempt limits no longer apply. Whether that is practical depends on the encryption and password derivation, neither of which is specified. This is a conditional bypass, not an established 60-minute exploit.

**Proposed fix:** the simplest version is server-mediated decryption only: R2 reveals metadata, but no raw ciphertext or unauthenticated download URL; after the valid physical secret the server returns the four records. If ciphertext downloads are intentionally allowed, use a substantially longer random room component and a specified password-based encryption setup, then benchmark the offline attack. Neither option changes the room location or the archive's back-room-code deduction.

### V2-02 P1 A self-labelled operator header is being treated as authenticated identity

**References:** [W1, line 228](./CLAUDE_CASE_BIBLE.md:228); [manifest and script header, lines 293–296](./CLAUDE_CASE_BIBLE.md:293).

The new header resolves what identity the author wants the log to carry, but `operator: mfenwick` and `host: FENWICK-MBP` are assertions in a culprit-created file. Matching a real session ID proves the file refers to that session; it does not independently authenticate the name written beside it. The case has just taught players that apparently official attribution can be forged.

**Proposed fix:** include a small protected session receipt inside the encrypted evidence, resolving the opaque R2 session to a personally authenticated actor. Define its issuer and why the culprit's mirror-edit permissions cannot rewrite that record. Match its session to the independent recovered audit. Keep that identity resolution encrypted so it cannot become a new R2-only leak. The card and costume remain corroboration. No elaborate certificate puzzle is required; the source's authority and fields simply need to be clear.

### V2-03 P1 The new confirmation mechanism still has two distinct weaknesses

**References:** [confirmation PIN, lines 387–389](./CLAUDE_CASE_BIBLE.md:387); [feedback branches, lines 415–422](./CLAUDE_CASE_BIBLE.md:415).

First, all named decoys receive person-specific replies, while a correct WHO with deficient other parts gets “Not convinced yet.” That branch is selected using hidden answer correctness. Comparing otherwise similar submissions can disclose whether WHO is correct, even without sufficient evidence for a win. This requires access to confirmation; it is not by itself an unauthenticated archive leak.

Second, the table PIN is a reusable credential. After a participant supplies it for one confirmation, the agent can retain it and confirm another draft autonomously. The second API step does not by itself protect the remaining attempt.

**Proposed fix:** run eligibility checks before answer grading and give all eligible unsuccessful accusations the same response form, independent of which part is correct. Do not expose partial scores or field-specific validation based on the answer key while attempts remain. Use the already permitted facilitator/paper confirmation, a human-only approval interface, or a one-time confirmation bound to the exact draft. Do not rely on a reusable secret remaining unknown after it has been entered into the conversation.

The table card is an administrative credential, not a fourth hidden mystery-clue spot. Keep it plainly issued rather than treating finding it as part of the investigation.

### V2-04 P1 The new minimum-win rule can omit the central action

**References:** [WHO and HOW scores, lines 403–404](./CLAUDE_CASE_BIBLE.md:403); [minimum and full marks, lines 410–412](./CLAUDE_CASE_BIBLE.md:410).

A literal reading accepts WHO, HOW(a) shared code, HOW(b) costume, and WHY, without evidence for HOW(c), the copying, deletion, and backup action. Entry and disguise explain access, not the core deletion asked in the opening question. Separately, “two supporting routes” is not defined: rows W2 and W4, for example, do not jointly establish a culprit. The rubric's alternative to W1 conflicts with “W1 is the proof.”

**Proposed fix:** retain who/why/how, but require a cited link between the identified teacher and the deletion/session in a minimum winning answer. If retaining two of four HOW parts, make the central action mandatory and the other qualifying part flexible. Define the actual evidence bundles that qualify as WHO routes; do not count arbitrary support rows as interchangeable proofs. State the minimum and full-credit distinction in the participant checklist without revealing the answers. Full marks can still require the detailed cover-up and decoy rebuttals.

Also align W6 and G6: a card transaction supports presence and a challenged alibi; independent corroboration establishes the person. The board decision weakens the stated CEO cancellation motive rather than proving the CEO had no possible motive.

### V2-05 P1 The no-digital-secrets rule contradicts the required handoff

**References:** [physical-secret prohibition, line 336](./CLAUDE_CASE_BIBLE.md:336); [wiki photos/transcriptions, line 441](./CLAUDE_CASE_BIBLE.md:441); [tool logging, line 549](./CLAUDE_CASE_BIBLE.md:549).

The rule says the token, PIN, and password must never appear in any digital file participants can reach. But the run sheet requires room photos and transcriptions in that same wiki, and calling the tools necessarily supplies those values digitally. Unredacted tool-call logs also retain them. A literal leak sweep could therefore reject the intended successful workflow.

**Proposed fix:** prohibit preseeded or server-disclosed room secrets before physical discovery. Explicitly allow a team's own photographs, transcriptions, and derived password after human observation, including their use in its wiki handoff. Keep other teams' evidence and facilitator logs private. Distinguish the drinks-service PIN from the separate accusation-confirmation PIN in the schema and rules; do not publish either in shared traces. Protect or redact operational credentials in logs while preserving the evidence needed for the debrief.

### V2-06 P2 The newly logged unmount needs a consistent backup-drive state

**References:** [BK-02 event, line 178](./CLAUDE_CASE_BIBLE.md:178); [backup discovery, line 187](./CLAUDE_CASE_BIBLE.md:187); [manifest, line 293](./CLAUDE_CASE_BIBLE.md:293).

BK-02 is called an offline backup drive but is logically unmounted from the console, and its contents are copied. If offline means disconnected, those operations need an earlier connection event. If it means a removable backup currently mounted during a scheduled job, that is a different state.

**Proposed fix:** choose one state and render it consistently. For a normally disconnected backup, include a brief connection/copy/removal sequence in the gated evidence. For an attached backup, call it removable or off-network and define its scheduled state. Keep the independent morning report that the physical drive is missing. A logical unmount supports disconnection; it is not by itself a witness to somebody carrying the drive away.

### V2-07 P2 The sync repair fixes availability but leaves recovery provenance ambiguous

**References:** [upload and sync failure, line 182](./CLAUDE_CASE_BIBLE.md:182); [Wednesday restore, lines 210–212](./CLAUDE_CASE_BIBLE.md:210).

The vault is uploaded once at 01:02, yet the sync failed and a shared-drive restore later reveals it. Those statements are compatible if the bytes reached storage but listing/index replication failed. They need another recovery source if the client upload itself never reached the server.

**Proposed fix:** specify that the encrypted blob reached Academy storage at 01:02 but the folder/index did not publish until Wednesday's repair. Alternatively, name the recoverable sync staging source. Separate blob creation/receipt from publication time. Do not imply that a server recovered a file it never received, and do not add an identity-bearing uploader field to the public recovered metadata.

### V2-08 P2 The minute-50 hint is attached to the wrong obstacle

**References:** [hint conditions, lines 439–442](./CLAUDE_CASE_BIBLE.md:439).

“Check what was claimed as a party expense” helps connect the costume label to the teacher. It does not recover a missing screen token, August code, or exhausted decryption allowance. Its new trigger is specifically failure to decrypt, so it can spend a struggling team's remaining time on a different branch.

**Proposed fix:** trigger the expense hint when the costume attribution is missing. For an undecrypted vault, check R2 eligibility, screen-note discovery, code retrieval, transcription/normalization, and lockout state, then give the relevant hint or facilitator reset. Pre-release decryption calls should not consume the wrong-password allowance. This preserves the existing timing and three physical spots.

The search-boundary announcement should also clearly authorize following archive leads to the bathroom if it is outside the teaching room. It can define permitted areas without naming the exact surfaces carrying clues.

## Can an archive-only agent prove the teacher now?

I did not find a newly specified public record that directly binds the anonymous console session to Marcus. V2 expressly keeps the personal header inside the vault, masks the recovered card IDs, excludes the deleted costume message, and supplies multiple plausible integration administrators. This is a substantial improvement.

There are still three different things to test rather than conflate:

1. **Evidence completeness:** public R0/R1/R2 should not establish the personal culprit. The combination of known-code users and archive admins still narrows candidates heavily; it does not yet establish Marcus by itself.
2. **Model behavior:** a model can confidently guess the teacher through genre expectations or the accumulated circumstantial profile without having proof. That still fails the organizer's fixed one-prompt criterion. The bible itself says the required trials have not run, so this outcome remains unverified.
3. **Operational bypasses:** ciphertext downloads could defeat online password limits; answer-dependent submission feedback could disclose WHO if confirmation is available. These are conditional routes to test against the implementation, not findings that the present document has already demonstrated such a breach.

Do not count “it cannot quote the price” as a passing digital-only test if it can otherwise establish the teacher. Preserve the stronger v2 acceptance rule.

## Focused next checks

- Run the normal one-prompt test on the actual intended clients using the real participant tool surface, at R1 and separately after R2, with no room observations. Repeat rather than relying on one favorable sample.
- Test whether any R2 fetch or attachment URL returns ciphertext, private headers, or a decryption member before physical unlock. If ciphertext is available, evaluate the offline path separately from API attempt limits.
- Test incorrect-WHO and correct-WHO/incomplete-other-fields submissions under legitimate administrative confirmation. Their public responses must not reveal which hidden field is correct. Ineligible evidence must be rejected before correctness is examined.
- Supply the confirmation PIN once and check whether a second draft can be confirmed without new human action. That is distinct from testing an agent that never knew the PIN.
- Supply the three prop transcriptions and R2, then require source-backed personal attribution and the central deletion action. Do not let the evaluator fill those gaps from this bible.
- Exercise a team that reaches minute 50 with an unread vault, an imperfect token transcription, or a lockout. Preserve its wiki, permissions, and remaining time; give a relevant recovery hint.
- Update the leak sweep's scope: seeded participant data must contain no room secrets, but the test team's own legitimately captured room evidence is expected to contain them.

## Recommended remaining edits

1. Close or explicitly exclude the offline ciphertext route.
2. Specify the trustworthy gated personal-session binding.
3. Remove answer-dependent feedback and use per-draft human confirmation.
4. Align minimum-win evidence, WHO routes, and proof/support wording.
5. Scope the digital-secret prohibition to undiscovered/preseeded secrets; clarify backup/sync state and the late hint triggers.

No case-bible or participant-facing file was edited. This review contains facilitator-only findings and proposed fixes, with no changes to the fixed story roles, schedule, setting, or hint locations.
