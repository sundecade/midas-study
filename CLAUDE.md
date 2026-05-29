# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Extracting the MIDAS API Online Manual (engineering structural analysis software) into a structured JSON knowledge base for AI-assisted learning. The target audience is engineers with domain knowledge but no programming experience.

Two subsystems:
- **Knowledge base pipeline**: scraper → enhance → JSON (static data)
- **Tutor app** (`midas_tutor/`): Streamlit web app with RAG search + LLM chat

## Task Phases (from .ini files)

- **part1.ini** — Scrape MIDAS API docs into unified JSON (done)
- **part2.ini** — Generate beginner-friendly API teaching content
- **part3.ini** — Generate annotated Python API-calling code

## Data Pipeline (order matters)

```
scraper.py → midas_api_knowledge_base.json → enhance_kb.py → same file (enriched)
                                                                    │
                                              ┌─────────────────────┘
                                              ▼
                              midas_tutor/retriever.py (search + format for LLM)
                                              │
                                              ▼
                              midas_tutor/llm.py (RAG context → LLM)
                                              │
                                              ▼
                              midas_tutor/app.py (Streamlit UI)
```

**After every re-scrape you MUST run enhance_kb.py** — it adds `request_templates` and `request_field_guide` to every endpoint. Without it, the retriever won't send wrapping rules to the LLM, and the LLM will generate structurally invalid JSON (missing `Assign`/numeric-key layers for DB endpoints).

## Commands

```bash
# Scrape from scratch (needs midas_main.html cached)
PYTHONUTF8=1 python scraper.py

# Re-scrape using existing KB structure (no midas_main.html needed)
PYTHONUTF8=1 python rescrape.py

# Post-process: add request templates (MUST run after scraper/rescrape)
PYTHONUTF8=1 python enhance_kb.py

# Generate teaching markdown files
PYTHONUTF8=1 python generate_teaching.py

# Generate code examples
PYTHONUTF8=1 python generate_code_examples.py

# Test an endpoint's correct JSON format
PYTHONUTF8=1 python test_endpoint.py /db/CONS
PYTHONUTF8=1 python test_endpoint.py --list DB

# CLI search (no Streamlit needed)
cd midas_tutor && PYTHONUTF8=1 python search_cli.py "创建节点"

# Launch tutor web app
cd midas_tutor && streamlit run app.py
# Or double-click: midas_tutor/启动助手.bat
```

## midas_tutor Architecture

Three key modules:

**retriever.py** — `APIRetriever` class. Loads the KB JSON, builds a flat search index with Chinese-English keyword mapping. `format_endpoint_detail()` is the critical function that assembles the text context sent to the LLM — it MUST include `request_templates` (wrapping rules + per-method JSON templates) and `request_field_guide`. If the LLM generates wrong JSON, check this function first.

**llm.py** — `LLMClient` class. Multi-backend (DeepSeek, Ollama, custom OpenAI-compatible). `chat_with_context()` does RAG: calls retriever → formats results → sends to LLM with a system prompt that includes the complete MAPI workflow doc (auth, base_url, request patterns). The system prompt contains hardcoded JSON format rules that supplement the KB data.

**app.py** — Streamlit UI with 4 tabs: search, AI chat, teaching materials, code examples. Session state manages chat history and LLM client. Code extracted from AI responses can be saved, run in a subprocess, or downloaded as HTML.

## KB JSON Structure

```
{
  "meta": { ... },
  "structure": { section → { subsections, endpoints[] } },
  "api_data": { section → { endpoints: { path → api_object }, subsections: { name → { path → api_object } } } }
}
```

Each API object key fields:
| Field | Purpose |
|---|---|
| `api_name`, `http_method`, `url` | Basic identification |
| `parameters[]` | Merged from JSON schema + spec table (key, description, value_type, required, optional, default, json_path, json_level, source) |
| `json_schema` | Raw JSON Schema (inner structure only, NO wrapping layers) |
| `json_examples[]` | Named examples from docs (may be incomplete for PUT/DELETE) |
| `request_templates` | **Authoritative source** for complete JSON structure. Contains `_wrapper_info` (rules), per-method templates (POST/GET/PUT/DELETE) with full wrapping |
| `request_field_guide` | Per-field: required/optional, type, default, description |

## Critical: JSON Wrapping for DB Endpoints

DB section endpoints require a two-level wrapper that the raw schema DOES NOT show:

```json
{"Assign": {"1": {data}, "2": {data}, ...}}
```

The schema only shows the `data` portion (e.g., `ITEMS`, `X`, `Y`, `Z`). LLMs reading schema alone will generate unwrapped JSON. The fix chain:
1. `enhance_kb.py` adds `request_templates` with complete structure to KB
2. `retriever.format_endpoint_detail()` includes `request_templates` in LLM context
3. `llm.py` system prompt also hardcodes the Assign/Argument wrapping rules as a safety net

DOC/OPE sections use `{"Argument": {data}}` instead — simpler, no numeric index layer.

## Technical Notes

- **Python 3.12** — uses `PYTHONUTF8=1` on Windows to avoid GBK encoding crashes
- **BeautifulSoup matching**: `soup.find('h3', string=...)` fails when h3 contains nested `<strong>` elements (tag.string becomes None). Use `_find_section(soup, keyword)` which matches via `tag.get_text()`
- **Zendesk API**: articles fetched via `https://support.midasuser.com/api/v2/help_center/en-us/articles/{id}` (public, no auth). JS-rendered main page must be cached as `midas_main.html`
- **scraper_progress.json**: saves every 20 endpoints, enables resume
- **rescrape_progress.json**: same pattern for incremental re-scraping
- **midas_api_knowledge_base_backup.json**: created by rescrape.py before overwriting KB
- `/db/POSL` (article 49511153905177) returns HTTP 401 — permanently unscrapable
- M1-suffixed endpoints (e.g., `/db/STYP-M1`) are Hyper-S solver variants, structurally identical to base endpoints
- `generate_teaching.py` and `generate_code_examples.py` also read the KB and output to `teaching/` and `code_examples/` directories
- `test_endpoint.py` — quick lookup tool: `PYTHONUTF8=1 python test_endpoint.py /db/CONS` shows correct JSON format and field guide for any endpoint
- `search_cli.py` — terminal search (no browser needed): `cd midas_tutor && PYTHONUTF8=1 python search_cli.py "创建节点"`
- `LEARNING_GUIDE.md` — comprehensive learning guide covering all 41 files, 6-day study plan, and design rationale (intended for human developers learning the codebase)
