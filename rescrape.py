"""
Re-scrape knowledge base using existing structure (no midas_main.html needed).
Uses the fixed scraper.parse_article_body() to capture all spec tables and method examples.
"""
import json
import time
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scraper import parse_article_body, fetch_article

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, "midas_api_knowledge_base.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "midas_api_knowledge_base.json")
BACKUP_FILE = os.path.join(BASE_DIR, "midas_api_knowledge_base_backup.json")
PROGRESS_FILE = os.path.join(BASE_DIR, "rescrape_progress.json")

# Load existing KB
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    kb = json.load(f)

# Backup original
if not os.path.exists(BACKUP_FILE):
    with open(BACKUP_FILE, 'w', encoding='utf-8') as f:
        json.dump(kb, f, ensure_ascii=False, indent=2)
    print(f"Backup saved to {BACKUP_FILE}")

# Load progress
processed = set()
if os.path.exists(PROGRESS_FILE):
    with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
        processed = set(json.load(f))
    print(f"Resuming: {len(processed)} already processed")

# Collect all endpoints
all_eps = []
for section_name, section_data in kb["structure"].items():
    for ep in section_data.get("endpoints", []):
        if ep.get("article_id"):
            all_eps.append((section_name, None, ep))
    for sub_name, sub_eps in section_data.get("subsections", {}).items():
        for ep in sub_eps:
            if ep.get("article_id"):
                all_eps.append((section_name, sub_name, ep))

total = len(all_eps)
print(f"Total endpoints: {total}")
print("=" * 60)

api_data = kb.get("api_data", {})

for idx, (section_name, sub_name, ep) in enumerate(all_eps):
    ep_key = str(ep["article_id"])
    if ep_key in processed:
        continue

    processed_count = len(processed) + 1
    label = f"[{section_name}]"
    if sub_name:
        label += f" [{sub_name}]"
    print(f"  [{processed_count}/{total}] {label} {ep['endpoint']} - {ep['name']}")

    article_data = fetch_article(ep["article_id"])
    parsed = parse_article_body(article_data)

    if parsed:
        parsed["section"] = section_name
        if sub_name:
            parsed["subsection"] = sub_name

        if section_name not in api_data:
            api_data[section_name] = {"endpoints": {}, "subsections": {}}

        if sub_name:
            if sub_name not in api_data[section_name]["subsections"]:
                api_data[section_name]["subsections"][sub_name] = {}
            api_data[section_name]["subsections"][sub_name][ep["endpoint"]] = parsed
        else:
            api_data[section_name]["endpoints"][ep["endpoint"]] = parsed

    processed.add(ep_key)

    if processed_count % 20 == 0:
        kb["api_data"] = api_data
        kb["meta"]["generated_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(kb, f, ensure_ascii=False, indent=2)
        with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
            json.dump(list(processed), f)
        print(f"  [Progress: {processed_count}/{total}]")

    time.sleep(0.15)

# Final save
kb["api_data"] = api_data
kb["meta"]["generated_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(kb, f, ensure_ascii=False, indent=2)
with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
    json.dump(list(processed), f)

print(f"\nDone! Processed {len(processed)} endpoints.")
print(f"Output: {OUTPUT_FILE}")
print(f"File size: {os.path.getsize(OUTPUT_FILE) / 1024:.1f} KB")
