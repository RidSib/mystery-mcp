# Content revision report — facilitator only

Date: 27 October 2026. Source: `CLAUDE_CASE_BIBLE.md`, v3. Do not serve this report, the authoring code or the integrity baseline to participants.

## What changed

- Replaced every background body: 153 emails, 81 chats, 19 Drive documents, nine transcripts, 52 calendar descriptions and 18 expense descriptions. Threads now develop through actual requests, corrections, disagreements and handoffs. Voices follow roles: Finance tracks units and receipts, facilities distinguishes faults from bookings, students ask concrete questions, and marketing argues over wording.
- The background includes the milk-steamer fault, confusing welcome-pack versions, Maja's staff induction, demo descriptions and equipment, page-versus-sheet purchasing, duplicate budget entries, late planning drafts, the Halloween Bash committee, Leo's caption and staged-video discussions, separate spreadsheet-workshop refunds, IT overload and NordByte's two integration queues. Suspicious-looking disputes concern ordinary work; they introduce no new crime evidence.
- Rewrote the case prose in the same style, retaining required quotations and evidence. The four planted texts stay verbatim. Jule's six genuine notes now have the same short, plain, single-paragraph shape. Sandra's quoted reply and Hanna's title reaction remain intact.
- Replaced 393 record bodies overall. All 397 records remain, with 65 critical records identified only in the private key. IDs, metadata, releases, existing timestamped evidence movements, transcript speakers and line timestamps remain unchanged. The approved badge annotation/untimed-marker replacements are documented below. Purchase rows retain their existing times/items; the fourteen ordinary card assignments were deliberately replaced as requested.
- Badge traffic after the organizer's follow-up correction: 47 in / 45 out on Monday; 52 in / 19 out on Tuesday. Every row has the same time/name/direction fields. Marcus arrives Monday 08:50, leaves 18:30, and returns Tuesday 08:45. Sandra leaves Tuesday 00:35 and returns 08:40 for the all-hands. Kofi's timed overnight coverage is Monday 21:30–Tuesday 09:30. The unique departure note and untimed coverage marker are removed. The deleted overnight rows remain absent. Tuesday traffic ends before the existing noon collection timestamp.
- Keypad: 78 rows across August–October, covering slots 1–3. Course audit: 100 rows with seven routine activity types alongside the retained deletion. Drinks: fifteen purchases, using a shuffled selection of real allocations in the holder register rather than sequential card numbers; the required late purchase is untouched. Routine purchases avoid the resigned cleaner and the travelling CEO.
- Revision history: eight earlier routine revisions plus all eight original R2 revisions, retaining their IDs, actions and times. The one explicitly requested repair fills `scheduled — launch 9 Nov` in both the status revision and VAULT-4.
- Added private `polish_content.py` and wired it into regeneration. Complete coverage is asserted before writing, so no record silently falls back to the old template. `content_baseline.json` contains the original fixtures only for immutable-field comparisons; none of that old prose is served.

## Static results

`python3 build/facilitator/verify.py` — **PASS**, zero errors.

- Distinct first paragraphs: **234 / 234 (100%)** background email/chat records; threshold 90%. A record qualifies only if its first paragraph occurs once.
- Repeated sentences: **zero violations** among 1193 distinct qualifying sentences. Sentences with six or more words may occur in at most three records; explicitly required quotations are exempt. Comparison normalizes case, Unicode and quotation marks, strips transcript transport prefixes, and segments punctuation/newlines. This is a deterministic text check, not a semantic similarity judge.
- Jule: genuine range **6–18 words**; planted notes **6–16 words**. All ten are single paragraphs, with no format marker identifying a planted record.
- Length results below use Unicode word tokens, including transport text already present in a body. Each comparable channel and the overall corpus pass the documented median-ratio and range-overlap check. Structured registers account for the large critical Drive maximum.

| Channel | Critical median (range), words | Background median (range), words |
|---|---:|---:|
| all | 33 (2–456) | 36 (2–226) |
| mail | 48 (7–69) | 40 (10–81) |
| chat | 18 (5–39) | 20 (4–40) |
| drive | 110 (57–456) | 101 (51–165) |
| transcript | 186 (180–215) | 164 (153–226) |
| calendar | 6 (2–24) | 5 (2–21) |
| expense | 23 (23–23) | 17 (12–28) |
| log | 36 (25–41) | — |

- Required-quotation assertions: 26 records. Original metadata, transcript timing/speakers, required evidence rows, original revision history and restricted-string occurrence locations match the pre-edit baseline, with only the requested prior-status correction, ordinary purchase-card substitutions and follow-up badge annotation/coverage-marker replacements permitted.
- Restricted-string and separation sweep: **419 files**, no violations. Real room secrets remain confined to their approved prop masters and the private environment file.
- Timestamp checks: **1035 values**, no invalid dates, missing offsets or Berlin-offset errors. Release/catalog, schema, masking, roster, cleanup consistency and export/delete/unmount/backup ordering all pass.
- The case bible is unchanged: SHA-256 `7885c4267b795b4af99b53ef0ed54eb8da1334cb105549dfee3f2483965ae8a2`.

## Spec gaps and interpretations

1. **“Similar” has no numerical definition.** The verifier requires each critical/background median to be within a factor of 1.5 and their observed ranges to overlap, overall and per comparable channel. It reports full medians/ranges rather than treating this as proof of indistinguishable writing. There are no background logs to compare against.
2. **Routine history and traffic density are unspecified.** Added ordinary daytime rows and earlier routine revisions, without adding named nighttime actors or personal session attribution. The existing logged period and all original times were preserved. Maja's induction and other incidental work details are background, not added case evidence.
3. **Pre-existing log collection-time ambiguity.** LOG-8814's existing event_time is noon although its required late purchase occurs later that day. The instruction prohibits changing that time, so it remains unchanged. The spec needs to distinguish a daily collection label from an export-as-of cutoff if a future server uses event_time for filtering; release levels currently control availability.
4. **The earlier missing status is resolved.** No remaining before-value is blank in that status edit. Other previously documented implementation gaps, including real signing/runtime behavior, remain as described in BUILD_NOTES; no server was implemented here.
5. **Organizer's badge correction supersedes the old blanket cutoff.** The section 17.3 wording forbidding Marcus rows after Monday 18:30 is now interpreted as the overnight absence, followed by his explicitly requested Tuesday morning return. The bible is unchanged. The verifier retains the original baseline, permits precisely the approved note/coverage-marker replacements, and checks all 36 visible people's movement sequences, ordinary workday spans, morning arrival windows and all-hands presence.

Model acceptance tests, runtime/server tests and human playtests were **not run**. These checks establish fixture integrity and prose statistics, not the intended one-prompt decoy/stall outcome.
