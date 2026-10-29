# Publication audit

Date: 29 October 2026.

This repository intentionally includes the complete fictional mystery, facilitator notes, answer keys, physical-clue designs and vault solution. Those are reusable game content. They are not meant to be hidden from repository readers.

## Removed or replaced

- All seven active event-code values were replaced with public examples throughout the story, records, props, configuration, tests and documentation. Phase-code variants with spaces or punctuation were also checked. Ordinary timestamps are preserved.
- Production environment files, hosting-project links and account identifiers were excluded.
- The original deployment hostname was replaced with a placeholder. The landing page uses its own `/mcp` path.
- Personal home-directory paths were generalized.
- Generated server bundles, validation reports, caches, operating-system files and operator-only audit notes are ignored by Git.
- The initial Git history starts from the sanitized files. No earlier unsanitized commit was imported.

The generic hosting-function configuration remains so others can deploy their own instance; it contains no production-account linkage.

## Checks performed

The staged Git contents were compared with the seven active values and two hosting identifiers outside this checkout. No matches remained. The credential-pattern scan also checked for private keys, common API-token formats, credential-bearing URLs, personal home paths, linked-hosting IDs and production deployment hostnames.

Email addresses found in the published files use a reserved `.example` domain for fictional correspondence. No real customer or organization account was imported.

The export preserves all 406 record IDs, release levels, people, record timestamps, transcript transport timestamps and existing log-row timestamps. The metadata comparison checked 1,121 timestamp values. Example access-code substitutions and equivalent wording changes do not change the story's actors or event sequence.

The local server suite passes **47 checks** with the public example environment. It verifies protocol behavior, service routing, release gates, checkpoint and vault access, filtering, request limits and log redaction. String and array passcodes are both redacted from logs in this distribution. No model acceptance tests or live-deployment tests were run.

## Repeat the staged-file check

From the repository root after staging a change:

```sh
python3 scripts/check_publication.py
```

An operator can additionally pass `--private-env` and `--private-project` paths to compare against local values without printing them. Those files must stay outside the public commit. Purely numeric values are compared literally so legitimate timestamps do not become false credential matches.

## Limits

This is a content and known-secret audit, not a penetration test or a guarantee that arbitrary future contributions are safe. New secrets and event-specific customizations require a fresh review before publishing. The historical fixture generator/verifier describes an earlier snapshot; the current JSON records and runtime suite are the starting point for adaptations.

Public example codes are visible by design and must not be used to protect confidential information or treated as private credentials for an event.
