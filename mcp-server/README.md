# Academy MCP server

The stateless server for the fictional Academy mystery. The repository includes the full game and solution for adaptation; do not give the source checkout to players who want to investigate without spoilers.

See the [root README](../README.md) for the game, setup and adaptation instructions.

| Path | Purpose |
| --- | --- |
| `api/server.js` | Hosting-function entry point, routed to `/mcp` |
| `lib/mcp-handler.js` | MCP/JSON-RPC transport, argument redaction and per-IP flood guard |
| `lib/game.js` | Search, service tools and passcode gates |
| `scripts/prepare-data.mjs` | Bundles the current archive and vault from `../build` |
| `scripts/local-test.mjs` | Local protocol and access-gate tests; no AI calls |
| `data/` | Generated runtime files, ignored by Git |
| `public/` | Landing page; no game source or vault files |
| `vercel.json` | Reusable routing/function configuration; no account linkage |

First copy `../build/facilitator/secrets.env.example` to `../build/facilitator/secrets.env` from a fresh checkout. Then, in this directory:

```sh
npm run prepare-data
npm test
```

The tests use the ignored local environment file. Example values are public and must be replaced consistently in the configuration and physical props for your own event.

For deployment, prepare the data, configure the environment on your own hosting project and run `vercel deploy --prod`. The function uses environment variables supplied by the host; it does not read the facilitator environment file at runtime. Only `public/` is statically served. The JSON bundle is included inside the server function.

Do not deploy the entire repository as a static site. The facilitator documents and vault contents are public source material, but the game endpoint should disclose them only through its intended tools and passcode gates.
