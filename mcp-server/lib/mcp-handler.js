// MCP endpoint: Streamable HTTP transport, stateless, JSON responses only. No login:
// what a caller can see depends only on the passcodes sent with each tool call.
import { TOOLS, RESOURCE_LIST, callTool, readResource } from "./game.js";

const SUPPORTED = ["2025-06-18", "2025-03-26", "2024-11-05"];
const INSTRUCTIONS =
  "This server exposes the Academy's systems as separate services: mail_*, chat_*, calendar_*, drive_*, meetings_* (transcripts), " +
  "expenses_* and systems_* (facilities and IT logs). Each service has its own search and read tools; there is no search across all of them. " +
  "Record IDs show their service: MAIL, CHAT, CAL, DRV, TRN, EXP, LOG. " +
  "Every tool accepts optional passcodes. Codes your team is given or finds unlock more records; send all of them with every call.";

// Per-instance flood guard by client IP. Not game state: losing it changes nothing.
const rate = new Map();
function limited(ip) {
  const sec = Math.floor(Date.now() / 1000);
  const r = rate.get(ip);
  if (!r || r.sec !== sec) {
    if (rate.size > 5000) rate.clear();
    rate.set(ip, { sec, n: 1 });
    return false;
  }
  return ++r.n > Number(process.env.RATE_PER_SEC || 10);
}

const ok = (id, result) => ({ jsonrpc: "2.0", id, result });
const fail = (id, code, message) => ({ jsonrpc: "2.0", id, error: { code, message } });

function redact(args = {}) {
  const out = { ...args };
  for (const f of ["passphrase", "service_pin", "asset_tag"]) if (f in out) out[f] = "[redacted]";
  if ("passcodes" in out) out.passcodes = Array.isArray(out.passcodes) ? `[${out.passcodes.length} codes]` : "[redacted]";
  return out;
}

async function handle(msg) {
  const { id, method, params = {} } = msg || {};
  if (!method || msg.jsonrpc !== "2.0") return fail(id ?? null, -32600, "Invalid request");
  if (id === undefined) return null; // notification

  switch (method) {
    case "initialize":
      return ok(id, {
        protocolVersion: SUPPORTED.includes(params.protocolVersion) ? params.protocolVersion : SUPPORTED[0],
        capabilities: { tools: { listChanged: false }, resources: { listChanged: false } },
        serverInfo: { name: "academy-archive", version: "2.0.0" },
        instructions: INSTRUCTIONS,
      });
    case "ping":
      return ok(id, {});
    case "tools/list":
      return ok(id, { tools: TOOLS });
    case "tools/call": {
      const { name, arguments: args = {} } = params;
      console.log(JSON.stringify({ tool: name, args: redact(args) }));
      const result = callTool(name, args);
      if (result === null) return fail(id, -32602, `Unknown tool: ${name}`);
      return ok(id, { content: [{ type: "text", text: JSON.stringify(result, null, 2) }], structuredContent: result, isError: Boolean(result.error) });
    }
    case "resources/list":
      return ok(id, { resources: RESOURCE_LIST });
    case "resources/templates/list":
      return ok(id, { resourceTemplates: [] });
    case "resources/read": {
      const r = readResource(params.uri);
      return r ? ok(id, { contents: [r] }) : fail(id, -32002, "Resource not found");
    }
    case "prompts/list":
      return ok(id, { prompts: [] });
    default:
      return fail(id, -32601, `Method not found: ${method}`);
  }
}

export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Headers", "Authorization, Content-Type, Accept, Mcp-Protocol-Version, Mcp-Session-Id");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST, OPTIONS");
    return res.status(405).json(fail(null, -32000, "Use POST. This server does not offer an SSE stream."));
  }

  const ip = String(req.headers["x-forwarded-for"] || "local").split(",")[0].trim();
  if (limited(ip)) return res.status(429).json(fail(null, -32003, "Too many requests. Slow down to a few calls per second."));

  let body = req.body;
  if (typeof body === "string") {
    try { body = JSON.parse(body); } catch { return res.status(400).json(fail(null, -32700, "Parse error")); }
  }
  if (!body) return res.status(400).json(fail(null, -32700, "Parse error"));

  try {
    if (Array.isArray(body)) {
      const out = (await Promise.all(body.map(handle))).filter(Boolean);
      return out.length ? res.status(200).json(out) : res.status(202).end();
    }
    const out = await handle(body);
    return out ? res.status(200).json(out) : res.status(202).end();
  } catch (e) {
    console.error(JSON.stringify({ error: String(e) }));
    return res.status(500).json(fail(body?.id ?? null, -32603, "Internal error"));
  }
}
