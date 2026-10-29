// The single Vercel function: the MCP endpoint.
import mcp from "../lib/mcp-handler.js";

export default function handler(req, res) {
  return mcp(req, res);
}
