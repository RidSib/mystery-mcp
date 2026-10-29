# Academy MCP Mystery

A Halloween mystery played through an MCP-connected AI agent, a Markdown wiki and clues hidden around a room. The server presents a fictional Academy's email, chat, calendar, shared documents, meeting transcripts, expenses and system logs as separate services.

**The complete story and its solution are included. Spoilers are intentional. Fork it, change the characters, rewrite the mystery or use the server for a different workshop.**

## The game

A flagship course disappears shortly before launch. Staff report a ghost, the records disagree, and several people have plausible motives. Teams investigate who did it, how and why.

The session lasts 75 minutes:

1. **15 minutes:** connect to MCP, inspect source records and build a small wiki.
2. **60 minutes:** investigate the mystery, discover room clues, incorporate later evidence and cite a final answer.

Participants switch to a fresh AI conversation during the investigation and continue from their wiki. The exercise teaches source checking, durable notes and revising an earlier conclusion when new evidence arrives.

The dataset contains 406 fictional records. No real email, calendar or company account is connected. Runtime responses use the bundled files; the server makes no LLM calls.

## Contents

| Path | Contents |
| --- | --- |
| [CLAUDE_CASE_BIBLE.md](CLAUDE_CASE_BIBLE.md) | Full story, solution, clue dependencies and facilitator rules |
| [build/archive/](build/archive/) | Current fictional records, revisions and resources |
| [build/facilitator/](build/facilitator/) | Answer key, vault documents, run sheet, hints and design helpers |
| [build/props/](build/props/) | Printable physical clues and decoys, using public example codes |
| [build/participant/](build/participant/) | Handouts and empty wiki templates |
| [mcp-server/](mcp-server/) | Server implementation and local protocol tests |
| Root design notes and reviews | Earlier design choices and case-review history |

“Facilitator only” inside these documents means they should not be handed to players or exposed through the game's tools during a session. They are deliberately available to readers of this repository.

## Run the local checks

Requirements: Node.js 20 or newer. The server uses built-in libraries and has no third-party runtime packages.

From the repository root:

```sh
cp build/facilitator/secrets.env.example build/facilitator/secrets.env
cd mcp-server
npm run prepare-data
npm test
```

The first command creates an ignored local environment file containing **public demo values**. Data preparation bundles the current archive and vault in the ignored `mcp-server/data/` directory. The tests exercise the handler locally; they do not contact a deployed endpoint or run an AI model.

## Deploy your own server

The included `mcp-server/vercel.json` is an account-neutral deployment recipe. No production project link, account ID or live endpoint is included.

1. Prepare the data as above.
2. From `mcp-server/`, link the project to your own hosting account.
3. Configure the environment variables below on that project.
4. Deploy from `mcp-server/`. With the Vercel CLI, use `vercel deploy --prod`.
5. Connect an MCP client to `https://YOUR-HOST/mcp` using Streamable HTTP.

| Variable | Purpose |
| --- | --- |
| `CASE_CODE` | Opens the first investigation batch |
| `RESTORE_CODE` | Opens the second batch and enables the vault gate |
| `REVEAL_CODE` | Opens all evidence for the final reveal |
| `SERVICE_ASSET`, `SERVICE_PIN` | The drinks-station checkpoint |
| `BACK_ROOM_CODE`, `ROOM_TOKEN` | The archive/room components of the vault passphrase |
| `RATE_PER_SEC` | Optional per-instance, per-IP request limit; default 10 |

Choose your own event values. When changing a room code or token, update the matching archive clue, printed prop and facilitator instructions as well as the environment. Keep your event-specific changes private if you want those values to stay undisclosed.

The supplied codes are examples, not access credentials for an existing event. Passcode gates organize gameplay; this application is intended for fictional game data, not confidential business records. The flood guard is per process and is not a durable attempt counter.

## MCP interface

The server offers 21 tools across separate services:

- `mail_*` and `chat_*` search messages and read threads or conversations.
- `calendar_*`, `drive_*` and `meetings_*` retrieve events, documents and transcripts.
- `expenses_*` searches and reads claims.
- `systems_*` lists and filters logs and reads available audit history.
- `facilities_request_card_log` opens the physical checkpoint.
- `case_get_brief` returns the investigation question after its release.

Search results contain metadata and snippets. Read tools return full records. Every call can carry a `passcodes` array; the server does not retain a team's unlock state. There is also an always-available organization-chart resource.

The vault operation is a server-side passphrase gate over bundled text records. It does not provide cryptographic encryption of a downloadable file. Final accusations are handled by the facilitator rather than a server-side scoring tool.

## Adapt the story

Start with the case bible and the current JSON records. Follow a clue through its source documents, room prop and answer-key references before changing it. Record IDs connect those pieces.

The historical Python generation and verification helpers target earlier case snapshots and contain assumptions about record counts and releases. Do not run the generator over the current dataset without reconciling those assumptions first. The current checked-in records are the starting point for this edition.

For participants, share the handouts, wiki starter and your MCP endpoint. Avoid handing them an entire repository clone unless reading the answer key is part of the activity.

## Publication and reuse

This is a sanitized source distribution. Active event codes were replaced throughout the files, local personal paths were generalized, and production environment files, generated runtime bundles, logs and hosting-account metadata were excluded. See [PUBLICATION_AUDIT.md](PUBLICATION_AUDIT.md) for the audit scope and limitations.

Code, original fictional game content and documentation are provided under the [MIT License](LICENSE). Adaptations and contributions are welcome. Characters, organizations and correspondence in the game are fictional; references to third-party products do not imply endorsement.
