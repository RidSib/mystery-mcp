# Runtime access checklist

This is an implementation specification, not a running server. Only approved rendered archive data is ordinary retrieval input. Private operator material, source design documents, old solved workspaces, build controls, test keys, and private generation tools must not be deployed as public files or mounted into agent workspaces.

## Releases and reads

- Authenticate each team and keep its state private.
- Check the release manifest on every search result, count, snippet, fetch, revision, resource, and error path. IDs and client dates never grant access.
- Operator controls alone advance R1 and R2. C1 and VAULT are independent per-team gates, not later numeric release levels.
- C1 requires R1 plus both values from the physical service sticker. Five wrong eligible attempts lock it until an operator checks and resets the team.
- The current course record is readable in R1; its separate history is R2. All other mail/chat records and the incident summary have no retained revisions.
- The directory resource is R0; the case brief is R1.
- Keep recovered badge values masked in bodies, row keys, identifiers, and metadata. Keep console session identifiers opaque outside unlocked evidence.

## Server-mediated decryption

- The released file is metadata only. There is no ciphertext, attachment payload, blob, or download URL to serve.
- Require R2 and the normalized physical passphrase before returning any private evidence member. Normalize case, spaces, hyphens, and plus signs; preserve leading zeros in the code component.
- Prerelease calls return the pending-sync response and do not count as wrong passwords. Ten incorrect eligible attempts lock this operation until operator reset.
- After success, return five small text records from the separately provisioned private evidence store. Never expose private storage paths through the API. Do not bundle the private operator directory into a participant/server artifact.

## Drafts and human confirmation

- Participant tools create drafts only. They never confirm or score a draft.
- The separate operator console checks complete fields and accessible citations before confirming an eligible draft in person.
- Keep two counted accusations per team. Ineligible drafts do not spend an attempt or reveal correctness.
- The only confirmed replies are “The mask comes off. Well done, meddling kids.” and “Not convinced. Attempts left: N.” No field-level or partial-score oracle while attempts remain.
- Operator-only controls advance releases, reset lockouts, confirm drafts, and view milestones. They are absent from the participant tool list.

## Persistence and secrets

- Persist checkpoint/decryption grants, failed attempts, drafts, and confirmations across reconnects and new conversations. Never share grants across teams.
- Load credentials from private runtime environment configuration; the example file supplies variable names only. Never include real values in schemas, examples, errors, or server files.
- Redact passphrases, checkpoint codes, and access credentials in tool-call logs. Teams may retain their own physically discovered evidence in their own wiki.
- Build the search index ahead of the event from authorized archive inputs; do not call an LLM at runtime.
- Use pagination and per-team request limits. Neither bulk export nor direct static access to the data directory is an approved endpoint.
