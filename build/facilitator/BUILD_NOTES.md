# Build notes — facilitator only

Generated from the v3 case bible, sections 1–17. No case-bible changes were made. This file and the rest of the private operator directory must not enter a participant workspace, public index, or server deployment bundle.

## Contents

- 397 schema-shaped archive records: 170 mail, 100 chat, 60 calendar, 30 Drive, 12 transcripts, 20 expenses, and 5 logs.
- All 65 case-critical archive record IDs from section 17.3, with their stated releases. Importance flags are false in every served record; true flags exist only in the answer key.
- One separate R2 revision history, two resources, and an ID-to-release manifest including the five private evidence members.
- Five private vault text records. The encrypted course is represented by metadata only; no blob, ciphertext, course payload, or download URL was generated.
- The grading sheet, run sheet, diagnostic hint ladder, debrief, nine print masters, empty wiki starter and seven templates, handouts, server tool/resource schemas, access checklist, environment example, and acceptance procedures.

The additional generator, authored prose module, document renderer, verifier, integrity baseline, these notes, content revision report, and validation report are private operator helpers. They are not served records. `content_baseline.json` preserves the original pre-rewrite fixture solely for integrity comparisons; its old prose is never emitted.

## Regeneration and checks

Edit the prescribed root configuration for names or the selected station word, then run from the build directory:

```sh
python3 facilitator/generate.py
python3 facilitator/verify.py
```

Regeneration replaces records previously emitted by the manifest. It does not change the case bible. The verifier uses local files only. Its results are in `validation_report.json`; it runs no model, runtime endpoint, or human playtest.

The root configuration is private build control: it contains role mappings and restricted values explicitly required by section 17.2. It is not participant data or a server file. Give participants only their participant folder and a gated MCP connection. Do not hand over the whole build directory. The archive is private runtime data, not a static public directory; the separately held vault records require authorized server-side delivery.

## Spec gaps and conservative resolutions

1. **Restricted-sweep scope versus root configuration.** Section 17.2 requires the root config to contain the back-room code, order, card, session, competitor, and role mappings, while 17.6 restricts occurrences in game records. Following section 14's archive-sweep scope, those rules are enforced on the archive; participant/server files receive an additional strict sweep. Private control/test files are not treated as served records. Real room/service secrets remain confined to the approved prop masters and private environment file.
2. **Generic identifier prohibition versus mandatory audit values.** The required current audit names the tech administrator account, and the required admin list names a shared service account. Those explicit section 17.3 fields take precedence over the generic display-name-only sentence. No email addresses or teacher-identifying usernames are placed in served records. Private receipt/operator identifiers remain in the vault only.
3. **Original course-status value resolved.** The updated bible and organizer instruction supply `scheduled — launch 9 Nov`. That exact before-value now appears in both the R2 status revision and VAULT-4; the earlier null/blank is removed.
4. **Six genuine Marketing records, five supplied phrases.** One existing title objection is repeated on another date. No sixth threat or new case fact was invented.
5. **Unspecified incidental metadata.** Ordinary dates/times within stated ranges, thread IDs, support conversations, reporting lines, and routine expenses are fixture background. Precise crime, call, entry, edit, storage, and publication times follow the bible. Unknown calendar end times, the hotel amount/approver, and undated vault drafts are null rather than new evidential claims.
6. **Roster versus external buyer.** Thirty ordinary staff and twenty ordinary students are added. All internal named people and the added roster appear in the org chart. The buyer is omitted from all public directory material, following the explicit prohibition. The contractor is listed as external support. The card list has forty holders, including two daytime-access students; only the four specified cards use the protected prefix.
7. **Approximate critical counts.** Section 17.3 enumerates three critical transcripts and eleven critical Drive records, rather than section 13's approximate four and twelve. The explicit catalog wins; total channel volumes are preserved. Background fills the remaining slots.
8. **Late-record timing.** Twenty ordinary background records are R1 and dated Monday/Tuesday. The specified future calendar entries remain R0. Release levels, not date cutoffs, control access. The board minutes remain R2 despite their earlier date.
9. **Dates in configuration.** The tree comment mentions dates, but the prescribed config object supplies no date fields. That object was retained; canonical dates live in the private generation recipe. No invented date settings were added.
10. **Receipt is a fictional evidence fixture.** The platform receipt is rendered exactly with its stated valid-signature assertion. No signing protocol, certificate, or cryptographic verifier was specified, so no real signature infrastructure was fabricated.
11. **Runtime deployment is not specified by this tree.** The deliverable contains schemas and an access checklist, not executable MCP endpoints or a facilitator console. Actual connection URLs and team credentials remain placeholders. Private-vault provisioning, room-photo references, runtime persistence, and endpoint authorization still need implementation and testing.
12. **No media asset provided.** The student post represents the admitted staged bedsheet clip in text. No external video URL or fabricated media file was added.

## Test status

Run the verifier after generation. It checks restricted strings and their preserved placements, timestamps, the requested tree, critical catalog, release coverage, schema shape, roster, masking, current-versus-cleanup consistency, and copy/delete/unmount/backup ordering. It also checks distinct first paragraphs, repeated sentences, channel length distributions, Jule's message lengths and shape, required quotations, legacy filler, original metadata/evidence-row integrity, log traffic, earlier revisions and the confirmed prior status. See `CONTENT_REVISION_REPORT.md` for the content rewrite and exact results.

Model acceptance tests, endpoint/runtime tests, and the human rehearsal are **not run**. Passing static checks does not establish the intended one-prompt decoy/stall behavior.
