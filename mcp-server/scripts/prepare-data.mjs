// Copies only the served archive and the server-held vault records from ../build
// into data/. Nothing else from build/facilitator is bundled.
import { readFileSync, writeFileSync, readdirSync, mkdirSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const build = join(root, "..", "build");
const out = join(root, "data");
mkdirSync(out, { recursive: true });

const records = [];
const recordsDir = join(build, "archive", "records");
for (const channel of readdirSync(recordsDir, { withFileTypes: true }).filter((d) => d.isDirectory()).map((d) => d.name)) {
  for (const file of readdirSync(join(recordsDir, channel))) {
    if (file.endsWith(".json")) records.push(JSON.parse(readFileSync(join(recordsDir, channel, file), "utf8")));
  }
}

const revisions = JSON.parse(readFileSync(join(build, "archive", "revisions", "LOG-5190.json"), "utf8"));
const resources = {
  "org-chart": readFileSync(join(build, "archive", "resources", "org-chart.json"), "utf8"),
  "case-brief": readFileSync(join(build, "archive", "resources", "case-brief.md"), "utf8"),
};

const vault = [];
const vaultDir = join(build, "facilitator", "vault");
for (const file of readdirSync(vaultDir).sort()) {
  if (!file.endsWith(".md")) continue;
  const text = readFileSync(join(vaultDir, file), "utf8");
  vault.push({ id: file.replace(/\.md$/, ""), text: text.replace(/^---[\s\S]*?---\s*/, "") });
}

writeFileSync(join(out, "records.json"), JSON.stringify(records));
writeFileSync(join(out, "revisions.json"), JSON.stringify(revisions));
writeFileSync(join(out, "resources.json"), JSON.stringify(resources));
writeFileSync(join(out, "vault.json"), JSON.stringify(vault));
console.log(`records ${records.length}, revisions ${revisions.revisions.length}, vault ${vault.length}`);
