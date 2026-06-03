"""Build the MIDAS API knowledge base from a saved article-id snapshot.

Use this when `midas_api_knowledge_base.json` is missing and you do not have
`midas_main.html`.  The snapshot contains the section/subsection/endpoint list
and Zendesk article ids; this script fetches each article and parses it with
the current scraper logic.

After this script finishes, run:

    python enhance_kb.py
    python tools/refresh_learning_assets.py
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path

from scraper import fetch_article, parse_article_body


BASE_DIR = Path(__file__).resolve().parent
SNAPSHOT_FILE = BASE_DIR / "midas_api_structure_snapshot.json"
OUTPUT_FILE = BASE_DIR / "midas_api_knowledge_base.json"
PROGRESS_FILE = BASE_DIR / "build_kb_progress.json"


def _load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _save_json(path: Path, data) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def _iter_endpoints(structure):
    for section_name, section_data in structure.items():
        for ep in section_data.get("endpoints", []):
            yield section_name, None, ep
        for sub_name, endpoints in section_data.get("subsections", {}).items():
            for ep in endpoints:
                yield section_name, sub_name, ep


def main() -> int:
    if not SNAPSHOT_FILE.exists():
        print(f"Missing snapshot file: {SNAPSHOT_FILE}")
        return 1

    snapshot = _load_json(SNAPSHOT_FILE)
    structure = snapshot["structure"]
    all_eps = list(_iter_endpoints(structure))
    total = len(all_eps)

    api_data = {}
    processed = set()
    if PROGRESS_FILE.exists():
        progress = _load_json(PROGRESS_FILE)
        api_data = progress.get("api_data", {})
        processed = set(progress.get("processed", []))
        print(f"Resume: {len(processed)}/{total} already processed")

    for index, (section_name, sub_name, ep) in enumerate(all_eps, start=1):
        article_id = ep.get("article_id")
        key = f"{section_name}:{sub_name or ''}:{ep.get('endpoint')}:{article_id}"
        if key in processed:
            continue

        label = f"[{section_name}]"
        if sub_name:
            label += f" [{sub_name}]"
        print(f"[{index}/{total}] {label} {ep.get('endpoint')} - {ep.get('name')}")

        parsed = None
        if article_id:
            parsed = parse_article_body(fetch_article(article_id))

        if parsed:
            parsed["section"] = section_name
            if sub_name:
                parsed["subsection"] = sub_name

            api_data.setdefault(section_name, {"endpoints": {}, "subsections": {}})
            if sub_name:
                api_data[section_name]["subsections"].setdefault(sub_name, {})
                api_data[section_name]["subsections"][sub_name][ep["endpoint"]] = parsed
            else:
                api_data[section_name]["endpoints"][ep["endpoint"]] = parsed

        processed.add(key)
        if len(processed) % 20 == 0:
            _save_json(PROGRESS_FILE, {"api_data": api_data, "processed": sorted(processed)})

        time.sleep(0.15)

    output = {
        "meta": {
            "source": snapshot.get("source", "structure snapshot"),
            "description": "MIDAS API Online Manual - Unified Knowledge Base for AI retrieval",
            "total_endpoints": total,
            "sections": list(structure.keys()),
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "schema_version": "1.0",
        },
        "structure": structure,
        "api_data": api_data,
    }
    _save_json(OUTPUT_FILE, output)

    if PROGRESS_FILE.exists():
        PROGRESS_FILE.unlink()

    print(f"Done: {OUTPUT_FILE}")
    print("Next: python enhance_kb.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
