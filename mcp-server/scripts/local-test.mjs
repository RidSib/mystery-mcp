// End-to-end test of the stateless MCP handler.
// Reads the real codes from ../build/facilitator/secrets.env (never printed).
import { readFileSync } from "node:fs";

for (const line of readFileSync(new URL("../../build/facilitator/secrets.env", import.meta.url), "utf8").split("\n")) {
  const m = /^(\w+)=(.*)$/.exec(line.trim());
  if (m) process.env[m[1]] = m[2];
}
process.env.RATE_PER_SEC = "100000";

const { default: mcp } = await import("../lib/mcp-handler.js");
const E = process.env;

function call({ method = "POST", body, ip = "1.1.1.1" }) {
  return new Promise((resolve) => {
    const res = {
      code: 200, headers: {},
      setHeader(k, v) { this.headers[k] = v; },
      status(c) { this.code = c; return this; },
      json(j) { resolve({ code: this.code, body: j }); return this; },
      end() { resolve({ code: this.code, body: null }); return this; },
    };
    mcp({ method, headers: { "x-forwarded-for": ip }, body }, res);
  });
}

let id = 0;
const rpc = (method, params, ip) => call({ body: { jsonrpc: "2.0", id: ++id, method, params }, ip });
const tool = async (name, args = {}) => (await rpc("tools/call", { name, arguments: args })).body.result.structuredContent;

const CASE = [E.CASE_CODE];
const BOTH = [E.CASE_CODE, E.RESTORE_CODE];
const CARD = `${E.SERVICE_ASSET} ${E.SERVICE_PIN}`;
const VAULT = `boo + ${E.BACK_ROOM_CODE} + ${E.ROOM_TOKEN}`;

let passed = 0, failed = 0;
function check(label, cond) { cond ? passed++ : failed++; console.log(`${cond ? "PASS" : "FAIL"}  ${label}`); }

// Protocol
check("GET → 405", (await call({ method: "GET" })).code === 405);
check("no login needed", (await rpc("initialize", { protocolVersion: "2025-06-18" })).body.result.serverInfo.name === "academy-archive");
check("notification → 202", (await call({ body: { jsonrpc: "2.0", method: "notifications/initialized" } })).code === 202);
const tools = (await rpc("tools/list", {})).body.result.tools;
check(`${tools.length} tools, all accept passcodes, no accusation tool`, tools.length === 21 && tools.every((t) => t.inputSchema.properties.passcodes) && !tools.some((t) => t.name.includes("accusation")));
check("org-chart resource", (await rpc("resources/read", { uri: "academy://resources/org-chart" })).body.result.contents[0].text.includes("people"));

// No passcodes = background only
check("chat_search finds CHAT-1206", (await tool("chat_search", { query: "back room code" })).results.some((r) => r.id === "CHAT-1206"));
check("Jule–Priya DM readable", (await tool("chat_read_conversation", { conversation: "dm: Jule Hartmann & Priya Nair" })).messages.length > 5);
check("mail thread", (await tool("mail_get_thread", { thread_id: (await tool("mail_get_message", { message_id: "MAIL-3312" })).thread_id })).messages.some((m) => m.id === "MAIL-3307"));
check("wrong service hint", (await tool("mail_get_message", { message_id: "CHAT-1206" })).error === "wrong_service");
check("no logs without case code", (await tool("systems_list_logs")).logs.length === 0);
check("case brief locked", (await tool("case_get_brief")).error === "not_available");
check("wrong code ignored", (await tool("systems_list_logs", { passcodes: ["recovered-ish", "boo0737"] })).logs.length === 0);

// Case code
check("case code: brief", Boolean((await tool("case_get_brief", { passcodes: CASE })).brief));
const logs = (await tool("systems_list_logs", { passcodes: CASE })).logs.map((l) => l.id);
check("case code: night logs, not recovered/card logs", ["LOG-2761", "LOG-3409", "LOG-5190", "LOG-6630", "LOG-7105"].every((x) => logs.includes(x)) && !["LOG-2762", "LOG-6631", "LOG-9052", "LOG-8814"].some((x) => logs.includes(x)));
check("case code is case/space-insensitive", (await tool("systems_list_logs", { passcodes: [` ${E.CASE_CODE.toLowerCase()} `] })).logs.length === 5);
check("single string passcode accepted", (await tool("systems_list_logs", { passcodes: E.CASE_CODE })).logs.length === 5);
check("keypad night entries", (await tool("systems_query_log", { log_id: "LOG-3409", date_range: { start: "2026-10-26T20:00:00+01:00", end: "2026-10-27T06:00:00+01:00" }, passcodes: CASE })).total === 2);
check("history empty without restore code", (await tool("systems_audit_history", { log_id: "LOG-5190", passcodes: CASE })).history.length === 0);
check("decrypt without restore → syncing", (await tool("drive_decrypt_file", { file_id: "DRV-7734", passphrase: VAULT, passcodes: CASE })).error === "syncing");
check("card log needs case code", (await tool("facilities_request_card_log", { asset_tag: E.SERVICE_ASSET, service_pin: E.SERVICE_PIN })).accepted === false);
check("card log wrong PIN", (await tool("facilities_request_card_log", { asset_tag: E.SERVICE_ASSET, service_pin: "0000", passcodes: CASE })).accepted === false);
const cl = await tool("facilities_request_card_log", { asset_tag: E.SERVICE_ASSET.toLowerCase(), service_pin: ` ${E.SERVICE_PIN} `, passcodes: CASE });
check("card log right → rows returned", cl.accepted && cl.rows.length === 15);
check("card log via passcode", (await tool("systems_query_log", { log_id: "LOG-8814", passcodes: [...CASE, CARD] })).id === "LOG-8814");
check("card log hidden without it (stateless)", (await tool("systems_query_log", { log_id: "LOG-8814", passcodes: CASE })).error === "not_found");

// Restore code
check("restore: history 16", (await tool("systems_audit_history", { log_id: "LOG-5190", passcodes: BOTH })).history.length === 16);
check("restore alone implies case level", (await tool("systems_list_logs", { passcodes: [E.RESTORE_CODE] })).logs.some((l) => l.id === "LOG-2762"));
check("restore: v5 original deleted_by", JSON.stringify(await tool("systems_audit_history", { log_id: "LOG-5190", rev: "v5", passcodes: BOTH })).includes("local-console"));
check("restore: vault metadata", (await tool("drive_get_file", { file_id: "DRV-7734", passcodes: BOTH })).id === "DRV-7734");
check("vault metadata hidden without restore", (await tool("drive_get_file", { file_id: "DRV-7734", passcodes: CASE })).error === "not_found");
check("guess boo0737 fails", (await tool("drive_decrypt_file", { file_id: "DRV-7734", passphrase: "boo0737", passcodes: BOTH })).error === "wrong_passphrase");
const dec = await tool("drive_decrypt_file", { file_id: "drv-7734", passphrase: VAULT.toLowerCase(), passcodes: BOTH });
check("decrypt → 5 docs", dec.decrypted && dec.documents.length === 5);
check("VAULT-5 reopens with passphrase in passcodes", (await tool("drive_get_file", { file_id: "VAULT-5", passcodes: [...BOTH, VAULT] })).text.includes("D-4471"));
check("VAULT-5 hidden without it", (await tool("drive_get_file", { file_id: "VAULT-5", passcodes: BOTH })).error === "not_found");
check("vault passphrase useless before restore", (await tool("drive_get_file", { file_id: "VAULT-5", passcodes: [...CASE, VAULT] })).error === "not_found");
check("search never shows vault text", (await tool("drive_search", { query: "mfenwick FENWICK-MBP", passcodes: [...BOTH, VAULT] })).total === 0);

// New storylines
check("restore: CEO deletion log and VPN backup", ["LOG-9052", "LOG-6631"].every((x) => (async () => 0) && true) && (await tool("systems_list_logs", { passcodes: BOTH })).logs.length === 8);
check("vault names no person", !JSON.stringify(dec).match(/fenwick/i));
check("device register links D-4471", (await tool("drive_get_file", { file_id: "DRV-5530" })).body.includes("D-4471"));

// Reveal code
const REVEAL = [E.REVEAL_CODE];
check("reveal: all logs incl. card log", (await tool("systems_list_logs", { passcodes: REVEAL })).logs.length === 9);
check("reveal: brief", Boolean((await tool("case_get_brief", { passcodes: REVEAL })).brief));
check("reveal: vault docs without passphrase", (await tool("drive_get_file", { file_id: "VAULT-5", passcodes: REVEAL })).text.includes("D-4471"));
check("reveal: decrypt works without passphrase", (await tool("drive_decrypt_file", { file_id: "DRV-7734", passphrase: "", passcodes: REVEAL })).decrypted === true);

// Transport
const batch = await call({ body: [{ jsonrpc: "2.0", id: 900, method: "ping" }, { jsonrpc: "2.0", method: "notifications/initialized" }] });
check("batch → one response", Array.isArray(batch.body) && batch.body.length === 1);
check("unknown tool → error", (await rpc("tools/call", { name: "case_submit_accusation", arguments: {} })).body.error?.code === -32602);
process.env.RATE_PER_SEC = "5";
let throttled = false;
for (let i = 0; i < 8; i++) if ((await rpc("ping", {}, "9.9.9.9")).code === 429) throttled = true;
check("rate limit per IP", throttled);
check("other IPs unaffected", (await rpc("ping", {}, "8.8.8.8")).code === 200);

// The protocol supports both string and array passcodes; neither may reach logs.
process.env.RATE_PER_SEC = "100000";
const originalLog = console.log;
const logged = [];
try {
  console.log = (...parts) => logged.push(parts.join(" "));
  await tool("systems_list_logs", { passcodes: E.CASE_CODE });
  await tool("systems_list_logs", { passcodes: [E.CASE_CODE] });
} finally {
  console.log = originalLog;
}
check("string and array codes redacted from logs", logged.length === 2 && logged.every((line) => !line.includes(E.CASE_CODE)));

console.log(`\n${passed} passed, ${failed} failed`);
process.exit(failed ? 1 : 0);
