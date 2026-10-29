// Game rules: data, release gates, and the participant tools.
// The archive is presented as separate Academy services (mail, chat, calendar,
// drive, meetings, expenses, systems), each with its own tools and query style.
// Stateless: every call carries the passcodes it knows, and the answer depends
// only on those passcodes and the deployed data.
import { readFileSync } from "node:fs";
import { join } from "node:path";

const dataDir = join(process.cwd(), "data");
const load = (f) => JSON.parse(readFileSync(join(dataDir, f), "utf8"));

const RAW = load("records.json");
const REVISIONS = load("revisions.json");
const RESOURCES = load("resources.json");
const VAULT = load("vault.json");

const LEVEL = { R0: 0, R1: 1, R2: 2 };
const PAGE_SIZE = 20;
const LOG_PAGE_SIZE = 50;
const VAULT_DOC = "DRV-7734";
const C1_RECORD = "LOG-8814";

// Each service owns one record prefix.
const SERVICES = {
  mail: { prefix: "MAIL", channel: "mail", label: "mail", getTool: "mail_get_message" },
  chat: { prefix: "CHAT", channel: "chat", label: "chat", getTool: "chat_get_message" },
  calendar: { prefix: "CAL", channel: "calendar", label: "calendar", getTool: "calendar_get_event" },
  drive: { prefix: "DRV", channel: "drive", label: "drive", getTool: "drive_get_file" },
  meetings: { prefix: "TRN", channel: "transcript", label: "meeting recorder", getTool: "meetings_get_transcript" },
  expenses: { prefix: "EXP", channel: "expense", label: "expenses", getTool: "expenses_get" },
  systems: { prefix: "LOG", channel: "log", label: "systems", getTool: "systems_query_log" },
};
const BY_PREFIX = Object.fromEntries(Object.values(SERVICES).map((s) => [s.prefix, s]));

// Served copies never carry the release level or importance flag.
const RELEASE = new Map();
const RECORDS = new Map();
for (const r of RAW) {
  RELEASE.set(r.id, r.release);
  const { release, case_critical, ...served } = r;
  RECORDS.set(r.id, served);
}

// ---------- search index ----------

const tokenize = (s) => (String(s).toLowerCase().match(/[\p{L}\p{N}*#@.-]+/gu) || []).map((t) => t.replace(/^[.\-]+|[.\-]+$/g, "")).filter(Boolean);

function headText(r) {
  return [r.subject, r.title, r.from, ...(r.to || []), ...(r.cc || []), ...(r.attendees || []), r.author_credit].filter(Boolean).join("\n");
}

function contentText(r) {
  const parts = [r.body];
  for (const l of r.lines || []) parts.push(`${l.speaker}: ${l.text}`);
  for (const row of r.rows || []) parts.push(Object.values(row).filter((v) => v != null).join(" "));
  for (const h of r.holders || []) parts.push(Object.values(h).join(" "));
  if (r.directory) parts.push(JSON.stringify(r.directory));
  return parts.filter(Boolean).join("\n");
}

// Snippets come from the content; matching also covers subject and people.
const INDEX = new Map();
for (const [id, r] of RECORDS) {
  const text = contentText(r);
  const tf = new Map();
  for (const t of tokenize(`${headText(r)}\n${text}`)) tf.set(t, (tf.get(t) || 0) + 1);
  INDEX.set(id, { text, tf, time: Date.parse(r.start || r.event_time || 0) || 0 });
}

function snippet(text, terms) {
  const lower = text.toLowerCase();
  let at = -1;
  for (const t of terms) {
    const i = lower.indexOf(t);
    if (i >= 0 && (at < 0 || i < at)) at = i;
  }
  const start = Math.max(0, at < 0 ? 0 : at - 70);
  const s = text.slice(start, start + 200).replace(/\s+/g, " ").trim();
  return (start > 0 ? "…" : "") + s + (start + 200 < text.length ? "…" : "");
}

// Chat conversations: a channel (#marketing, Student channel), a named group, or a DM pair.
function conversationOf(r) {
  const to = r.to || [];
  if (to.length === 1 && (to[0].startsWith("#") || /channel/i.test(to[0]))) return to[0];
  if (to.length > 1) return `group: ${r.subject}`;
  return `dm: ${[r.from, to[0]].sort().join(" & ")}`;
}
for (const [id, r] of RECORDS) if (r.channel === "chat") INDEX.get(id).conversation = conversationOf(r);

// ---------- passcodes ----------

const norm = (s) => String(s || "").toLowerCase().replace(/[^a-z0-9]/g, "");
const env = (name) => norm(process.env[name]);
const cardLogCode = () => env("SERVICE_ASSET") + env("SERVICE_PIN");
const vaultCode = () => norm(`boo${process.env.BACK_ROOM_CODE || ""}${process.env.ROOM_TOKEN || ""}`);

// What a set of passcodes unlocks. Unknown codes are simply ignored.
export function context(passcodes) {
  const list = Array.isArray(passcodes) ? passcodes : passcodes ? [passcodes] : [];
  const codes = new Set(list.map(norm).filter(Boolean));
  const has = (code) => Boolean(code) && codes.has(code);
  let level = 0;
  if (has(env("CASE_CODE"))) level = 1;
  if (has(env("RESTORE_CODE"))) level = 2;
  // The reveal code (announced at the end) opens everything, room clues included.
  const reveal = has(env("REVEAL_CODE"));
  if (reveal) level = 2;
  const c1 = reveal || (level >= 1 && Boolean(env("SERVICE_PIN")) && (has(cardLogCode()) || has(env("SERVICE_PIN") + env("SERVICE_ASSET"))));
  const vault = reveal || (level >= 2 && Boolean(process.env.ROOM_TOKEN) && has(vaultCode()));
  return { level, c1, vault, reveal };
}

function visible(id, ctx) {
  const rel = RELEASE.get(id);
  if (!rel) return false;
  if (rel === "C1") return ctx.c1 && ctx.level >= 1;
  if (rel in LEVEL) return ctx.level >= LEVEL[rel];
  return false;
}

const cleanId = (id) => String(id || "").trim().toUpperCase();
const notFound = (id) => ({ error: "not_found", message: `No record ${id} is available.` });
const hasPerson = (list, name) => list.some((p) => String(p).toLowerCase().includes(name.toLowerCase()));

// Look up an ID in one service. Points to the right tool when the ID belongs elsewhere.
function getIn(service, ctx, rawId) {
  const id = cleanId(rawId);
  const owner = BY_PREFIX[id.split("-")[0]];
  if (owner && owner !== service && RECORDS.has(id) && visible(id, ctx)) {
    return { error: "wrong_service", message: `${id} is a ${owner.label} record. Use ${owner.getTool}.` };
  }
  if (!id.startsWith(`${service.prefix}-`) || !visible(id, ctx)) return notFound(id);
  return RECORDS.get(id);
}

function parseRange(range) {
  const from = range?.start ? Date.parse(range.start) : NaN;
  const end = range?.end ? Date.parse(String(range.end).length <= 10 ? `${range.end}T23:59:59+01:00` : range.end) : NaN;
  return { from: Number.isNaN(from) ? null : from, to: Number.isNaN(end) ? null : end };
}

// Ranked search inside one channel, with an optional extra filter.
function searchChannel(ctx, channel, { query = "", date_range, page = 1 }, filter = () => true) {
  const terms = [...new Set(tokenize(query))];
  const { from, to } = parseRange(date_range);
  const hits = [];
  for (const [id, entry] of INDEX) {
    const r = RECORDS.get(id);
    if (r.channel !== channel || !visible(id, ctx) || !filter(r, entry)) continue;
    if (from != null && entry.time < from) continue;
    if (to != null && entry.time > to) continue;
    let matched = 0, score = 0;
    for (const t of terms) {
      const n = entry.tf.get(t) || 0;
      if (n) { matched++; score += Math.min(n, 5); }
    }
    if (terms.length && !matched) continue;
    hits.push({ id, matched, score, time: entry.time, terms });
  }
  hits.sort((a, b) => b.matched - a.matched || b.score - a.score || b.time - a.time);
  return paginate(hits, page, PAGE_SIZE);
}

function paginate(items, page, size) {
  const p = Math.max(1, Math.floor(Number(page) || 1));
  return { page: p, page_size: size, total: items.length, total_pages: Math.max(1, Math.ceil(items.length / size)), items: items.slice((p - 1) * size, p * size) };
}

const listing = ({ items, ...meta }, shape) => ({ ...meta, results: items.map(shape) });
const snip = (h) => snippet(INDEX.get(h.id).text, h.terms);

// ---------- tool definitions ----------

const str = (description) => ({ type: "string", ...(description ? { description } : {}) });
const RANGE = {
  type: "object",
  description: "ISO dates or datetimes, e.g. {\"start\":\"2026-10-26\",\"end\":\"2026-10-27\"}",
  properties: { start: str(), end: str() },
  required: ["start", "end"],
  additionalProperties: false,
};
const PAGE = { type: "integer", minimum: 1 };
const PASSCODES = {
  type: "array",
  items: { type: "string" },
  description: "Optional unlock codes your team has been given or has found. Send all of them with every call; without them, unlocked records are hidden again.",
};
const obj = (properties, required = []) => ({ type: "object", properties: { ...properties, passcodes: PASSCODES }, required, additionalProperties: false });

export const TOOLS = [
  // Mail
  { name: "mail_search", description: "Academy Mail: search messages. Returns sender, recipients, subject, thread and a snippet, 20 per page. Leave query empty to list newest first.",
    inputSchema: obj({ query: str("Words to look for"), from: str("Sender name"), to: str("Recipient name"), date_range: RANGE, page: PAGE }) },
  { name: "mail_get_message", description: "Academy Mail: read one message in full by ID (MAIL-…).", inputSchema: obj({ message_id: str() }, ["message_id"]) },
  { name: "mail_get_thread", description: "Academy Mail: read every message in a thread, oldest first.", inputSchema: obj({ thread_id: str("THR-… from a message") }, ["thread_id"]) },

  // Chat
  { name: "chat_list_conversations", description: "Academy Chat: list channels, group chats and direct-message pairs, with message counts and last activity.",
    inputSchema: obj({ person: str("Only conversations this person is in"), page: PAGE }) },
  { name: "chat_read_conversation", description: "Academy Chat: read a conversation in order, 20 messages per page. Use a name exactly as chat_list_conversations shows it.",
    inputSchema: obj({ conversation: str(), date_range: RANGE, page: PAGE }, ["conversation"]) },
  { name: "chat_search", description: "Academy Chat: search messages across conversations. Returns the conversation, sender and a snippet.",
    inputSchema: obj({ query: str(), from: str("Sender name"), date_range: RANGE, page: PAGE }, ["query"]) },
  { name: "chat_get_message", description: "Academy Chat: read one message by ID (CHAT-…).", inputSchema: obj({ message_id: str() }, ["message_id"]) },

  // Calendar
  { name: "calendar_search_events", description: "Academy Calendar: find events by text, attendee and date range. Returns title, time, attendees.",
    inputSchema: obj({ query: str("Words in the title or description"), attendee: str("Person on the event"), date_range: RANGE, page: PAGE }) },
  { name: "calendar_get_event", description: "Academy Calendar: read one event in full by ID (CAL-…).", inputSchema: obj({ event_id: str() }, ["event_id"]) },

  // Drive
  { name: "drive_search", description: "Academy Drive: search shared files by title and content. Returns title, author, dates and a snippet.",
    inputSchema: obj({ query: str(), author: str("Author or credited team"), page: PAGE }) },
  { name: "drive_get_file", description: "Academy Drive: open one file by ID (DRV-…). Decrypted documents can be reopened here by their ID.", inputSchema: obj({ file_id: str() }, ["file_id"]) },
  { name: "drive_decrypt_file", description: "Academy Drive: open an encrypted file with its passphrase.",
    inputSchema: obj({ file_id: str(), passphrase: str() }, ["file_id", "passphrase"]) },

  // Meetings
  { name: "meetings_list", description: "Meeting recorder: list recorded meetings by text, participant and date range.",
    inputSchema: obj({ query: str("Words in the title or transcript"), participant: str(), date_range: RANGE, page: PAGE }) },
  { name: "meetings_get_transcript", description: "Meeting recorder: read a transcript (TRN-…), optionally only one speaker's lines.",
    inputSchema: obj({ meeting_id: str(), speaker: str() }, ["meeting_id"]) },

  // Expenses
  { name: "expenses_search", description: "Expenses: search claims by text, submitter and status. Returns amount, status and approver.",
    inputSchema: obj({ query: str(), submitter: str(), status: str("e.g. submitted, approved"), page: PAGE }) },
  { name: "expenses_get", description: "Expenses: read one claim in full by ID (EXP-…).", inputSchema: obj({ expense_id: str() }, ["expense_id"]) },

  // Systems
  { name: "systems_list_logs", description: "Facilities & IT: list the system logs you can access (door, keypad, platform, machines), with row counts and columns.", inputSchema: obj({}) },
  { name: "systems_query_log", description: "Facilities & IT: read rows from a log (LOG-…), 50 per page, filtered by time and by column values (substring match).",
    inputSchema: obj({ log_id: str(), date_range: RANGE, where: { type: "object", description: "Column filters, e.g. {\"name\":\"Sandra\"}", additionalProperties: { type: ["string", "number"] } }, page: PAGE }, ["log_id"]) },
  { name: "systems_audit_history", description: "Facilities & IT: the retained change history of a system log, if any. Without rev it lists entries; with rev it returns one entry in full.",
    inputSchema: obj({ log_id: str(), rev: str() }, ["log_id"]) },
  { name: "facilities_request_card_log", description: "Facilities: request a machine's card-purchase log by quoting the asset tag and service PIN printed on the machine.",
    inputSchema: obj({ asset_tag: str(), service_pin: str() }, ["asset_tag", "service_pin"]) },

  // Case
  { name: "case_get_brief", description: "The investigation brief and submission checklist, once the case has been announced.", inputSchema: obj({}) },
];

// ---------- tool implementations ----------

const brief = (r, h) => ({ id: r.id, time: r.event_time, from: r.from, to: r.to, subject: r.subject, thread_id: r.thread_id, snippet: snip(h) });

const mail = {
  search: (ctx, a) => listing(
    searchChannel(ctx, "mail", a, (r) => (!a.from || hasPerson([r.from], a.from)) && (!a.to || hasPerson([...(r.to || []), ...(r.cc || [])], a.to))),
    (h) => brief(RECORDS.get(h.id), h)),
  get: (ctx, { message_id }) => getIn(SERVICES.mail, ctx, message_id),
  thread: (ctx, { thread_id }) => {
    const t = cleanId(thread_id);
    const msgs = [...RECORDS.values()].filter((r) => r.channel === "mail" && r.thread_id === t && visible(r.id, ctx)).sort((a, b) => Date.parse(a.event_time) - Date.parse(b.event_time));
    return msgs.length ? { thread_id: t, messages: msgs } : { error: "not_found", message: `No mail thread ${t} is available.` };
  },
};

function conversations(ctx) {
  const map = new Map();
  for (const [id, entry] of INDEX) {
    const r = RECORDS.get(id);
    if (r.channel !== "chat" || !visible(id, ctx)) continue;
    const c = map.get(entry.conversation) || { conversation: entry.conversation, members: new Set(), messages: 0, last: 0 };
    c.members.add(r.from); (r.to || []).forEach((p) => c.members.add(p));
    c.messages++; c.last = Math.max(c.last, entry.time);
    map.set(entry.conversation, c);
  }
  return [...map.values()];
}

const chat = {
  list: (ctx, { person, page }) => {
    const all = conversations(ctx).filter((c) => !person || hasPerson([...c.members], person)).sort((a, b) => b.last - a.last);
    const { items, ...meta } = paginate(all, page, 50);
    return { ...meta, conversations: items.map((c) => ({ conversation: c.conversation, messages: c.messages, last_activity: new Date(c.last).toISOString() })) };
  },
  read: (ctx, { conversation, date_range, page }) => {
    const name = String(conversation || "").trim().toLowerCase();
    const { from, to } = parseRange(date_range);
    const msgs = [...INDEX].filter(([id, e]) => e.conversation && e.conversation.toLowerCase() === name && visible(id, ctx) && (from == null || e.time >= from) && (to == null || e.time <= to))
      .sort((a, b) => a[1].time - b[1].time).map(([id]) => RECORDS.get(id));
    if (!msgs.length) return { error: "not_found", message: `No conversation "${conversation}" with messages available. Use chat_list_conversations for exact names.` };
    const { items, ...meta } = paginate(msgs, page, PAGE_SIZE);
    return { conversation: INDEX.get(msgs[0].id).conversation, ...meta, messages: items.map((r) => ({ id: r.id, time: r.event_time, from: r.from, text: r.body })) };
  },
  search: (ctx, a) => listing(searchChannel(ctx, "chat", a, (r) => !a.from || hasPerson([r.from], a.from)),
    (h) => { const r = RECORDS.get(h.id); return { id: r.id, time: r.event_time, conversation: INDEX.get(h.id).conversation, from: r.from, snippet: snip(h) }; }),
  get: (ctx, { message_id }) => {
    const r = getIn(SERVICES.chat, ctx, message_id);
    return r.error ? r : { ...r, conversation: INDEX.get(r.id).conversation };
  },
};

const calendar = {
  search: (ctx, a) => listing(searchChannel(ctx, "calendar", a, (r) => !a.attendee || hasPerson([r.from, ...(r.attendees || [])], a.attendee)),
    (h) => { const r = RECORDS.get(h.id); return { id: r.id, title: r.subject, start: r.start, end: r.end, organizer: r.from, attendees: r.attendees, private: r.private }; }),
  get: (ctx, { event_id }) => getIn(SERVICES.calendar, ctx, event_id),
};

const drive = {
  search: (ctx, a) => listing(searchChannel(ctx, "drive", a, (r) => !a.author || hasPerson([r.from, r.author_credit].filter(Boolean), a.author)),
    (h) => { const r = RECORDS.get(h.id); return { id: r.id, title: r.title || r.subject, author: r.author_credit || r.from, modified: r.event_time, snippet: snip(h) }; }),
  get: (ctx, { file_id }) => {
    const id = cleanId(file_id);
    const v = VAULT.find((x) => x.id === id);
    if (v) return ctx.vault && ctx.level >= 2 ? { id: v.id, source: VAULT_DOC, text: v.text } : notFound(id);
    return getIn(SERVICES.drive, ctx, id);
  },
  decrypt: (ctx, { file_id, passphrase }) => {
    const id = cleanId(file_id);
    if (id !== VAULT_DOC) {
      const r = getIn(SERVICES.drive, ctx, id);
      return r.error ? r : { error: "not_encrypted", message: `${id} is not encrypted.` };
    }
    if (ctx.level < 2) return { error: "syncing", message: "This file is still syncing. Try again later." };
    if (!ctx.reveal && (!process.env.ROOM_TOKEN || norm(passphrase) !== vaultCode())) return { error: "wrong_passphrase", message: "Passphrase not accepted." };
    return {
      decrypted: true,
      file_id: id,
      documents: VAULT.map((v) => ({ id: v.id, text: v.text })),
      note: "To reopen these with drive_get_file (e.g. VAULT-1), add this passphrase to your passcodes.",
    };
  },
};

const meetings = {
  list: (ctx, a) => listing(searchChannel(ctx, "transcript", a, (r) => !a.participant || hasPerson(r.speakers || r.to || [], a.participant)),
    (h) => { const r = RECORDS.get(h.id); return { id: r.id, title: r.subject, time: r.event_time, participants: r.speakers || r.to, snippet: snip(h) }; }),
  transcript: (ctx, { meeting_id, speaker }) => {
    const r = getIn(SERVICES.meetings, ctx, meeting_id);
    if (r.error || !speaker) return r;
    return { ...r, lines: (r.lines || []).filter((l) => hasPerson([l.speaker], speaker)) };
  },
};

const expenses = {
  search: (ctx, a) => listing(
    searchChannel(ctx, "expense", a, (r) => (!a.submitter || hasPerson([r.from], a.submitter)) && (!a.status || String(r.status || "").toLowerCase().includes(String(a.status).toLowerCase()))),
    (h) => { const r = RECORDS.get(h.id); return { id: r.id, submitted: r.event_time, submitter: r.from, title: r.subject, amount: r.amount, status: r.status, approver: r.approver }; }),
  get: (ctx, { expense_id }) => getIn(SERVICES.expenses, ctx, expense_id),
};

const systems = {
  list: (ctx) => ({
    logs: [...RECORDS.values()].filter((r) => r.channel === "log" && visible(r.id, ctx))
      .map((r) => ({ id: r.id, name: r.subject, rows: (r.rows || []).length, columns: Object.keys((r.rows || [])[0] || {}), has_history: revisionsVisible(r.id, ctx) })),
  }),
  query: (ctx, { log_id, date_range, where = {}, page }) => {
    const r = getIn(SERVICES.systems, ctx, log_id);
    if (r.error) return r;
    const { from, to } = parseRange(date_range);
    const rows = (r.rows || []).filter((row) => {
      const t = Date.parse(row.time);
      if (from != null && !(t >= from)) return false;
      if (to != null && !(t <= to)) return false;
      return Object.entries(where).every(([col, val]) => String(row[col] ?? "").toLowerCase().includes(String(val).toLowerCase()));
    });
    const { items, ...meta } = paginate(rows, page, LOG_PAGE_SIZE);
    return { id: r.id, name: r.subject, description: r.body || undefined, ...meta, rows: items };
  },
  history: (ctx, { log_id, rev }) => {
    const r = getIn(SERVICES.systems, ctx, log_id);
    if (r.error) return r;
    if (!revisionsVisible(r.id, ctx)) return { id: r.id, history: [], message: "No retained change history for this log." };
    if (!rev) return { id: r.id, history: REVISIONS.revisions.map((x) => ({ rev: x.revision, time: x.event_time, action: x.action })) };
    const x = REVISIONS.revisions.find((y) => y.revision.toLowerCase() === String(rev).trim().toLowerCase());
    return x ? { id: r.id, ...x } : { error: "not_found", message: `No entry ${rev} in ${r.id}'s history.` };
  },
  cardLog: (ctx, { asset_tag, service_pin }) => {
    if (ctx.level < 1) return { accepted: false, message: "Card logs can't be requested right now." };
    const ok = env("SERVICE_PIN") && norm(asset_tag) === env("SERVICE_ASSET") && norm(service_pin) === env("SERVICE_PIN");
    if (!ok) return { accepted: false, message: "Asset tag and PIN not accepted." };
    const log = RECORDS.get(C1_RECORD);
    return {
      accepted: true,
      message: `Released: ${C1_RECORD}. To query it again with systems_query_log, add "<asset tag> <service PIN>" to your passcodes.`,
      id: log.id, name: log.subject, rows: log.rows,
    };
  },
};

function revisionsVisible(id, ctx) {
  return id === REVISIONS.record_id && ctx.level >= LEVEL[REVISIONS.release];
}

const HANDLERS = {
  mail_search: mail.search, mail_get_message: mail.get, mail_get_thread: mail.thread,
  chat_list_conversations: chat.list, chat_read_conversation: chat.read, chat_search: chat.search, chat_get_message: chat.get,
  calendar_search_events: calendar.search, calendar_get_event: calendar.get,
  drive_search: drive.search, drive_get_file: drive.get, drive_decrypt_file: drive.decrypt,
  meetings_list: meetings.list, meetings_get_transcript: meetings.transcript,
  expenses_search: expenses.search, expenses_get: expenses.get,
  systems_list_logs: systems.list, systems_query_log: systems.query, systems_audit_history: systems.history,
  facilities_request_card_log: systems.cardLog,
  case_get_brief: (ctx) => (ctx.level >= 1 ? { brief: RESOURCES["case-brief"] } : { error: "not_available", message: "No case has been announced yet." }),
};

export function callTool(name, args = {}) {
  const fn = HANDLERS[name];
  if (!fn) return null;
  const { passcodes, ...rest } = args || {};
  return fn(context(passcodes), rest);
}

// ---------- resources ----------

// Resources can't carry passcodes, so only the always-public org chart is one.
export const RESOURCE_LIST = [
  { uri: "academy://resources/org-chart", name: "org-chart", description: "The Academy directory and reporting lines.", mimeType: "application/json" },
];

export function readResource(uri) {
  if (uri !== RESOURCE_LIST[0].uri) return null;
  const { release, ...rest } = JSON.parse(RESOURCES["org-chart"]);
  return { uri, mimeType: "application/json", text: JSON.stringify(rest, null, 2) };
}
