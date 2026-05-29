"""
Midas API Documentation Scraper
Parses the MIDAS API Online Manual into a unified JSON knowledge base.
"""
import json
import re
import time
import os
import requests
from bs4 import BeautifulSoup

# Encoding handled via PYTHONUTF8=1 environment variable

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_PAGE = os.path.join(BASE_DIR, "midas_main.html")
OUTPUT_FILE = os.path.join(BASE_DIR, "midas_api_knowledge_base.json")
PROGRESS_FILE = os.path.join(BASE_DIR, "scraper_progress.json")
ZENDESK_API = "https://support.midasuser.com/api/v2/help_center/en-us/articles/{}"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def parse_main_page():
    """Extract section -> subsection -> endpoint -> {name, article_id} mapping."""
    with open(MAIN_PAGE, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    article_body = soup.find('section', class_='article-body')
    if not article_body:
        print("ERROR: Could not find article-body")
        return {}

    structure = {}
    current_section = None
    current_subsection = None

    for elem in article_body.find_all(['h2', 'h3', 'table']):
        if elem.name == 'h2':
            section_name = elem.get_text(strip=True)
            if section_name not in ('INTRODUCTION',):
                current_section = section_name
                current_subsection = None
                if current_section not in structure:
                    structure[current_section] = {"subsections": {}, "endpoints": []}

        elif elem.name == 'h3':
            subsection_name = elem.get_text(strip=True)
            current_subsection = subsection_name
            if current_section and current_section in structure:
                if subsection_name not in structure[current_section]["subsections"]:
                    structure[current_section]["subsections"][subsection_name] = []

        elif elem.name == 'table':
            if current_section is None:
                continue
            endpoints = _parse_endpoint_table(elem)
            if endpoints:
                if current_subsection:
                    if current_section in structure:
                        structure[current_section]["subsections"][current_subsection].extend(endpoints)
                else:
                    if current_section in structure:
                        structure[current_section]["endpoints"].extend(endpoints)

    return structure


def _parse_endpoint_table(table):
    """Parse a table into a list of {name, endpoint, article_id} dicts."""
    endpoints = []
    rows = table.find_all('tr')[1:]  # Skip header row

    for row in rows:
        cells = row.find_all('td')
        if len(cells) < 3:
            continue

        endpoint_cell = cells[1]
        endpoint_text = endpoint_cell.get_text(strip=True)

        detail_cell = cells[2]
        link = detail_cell.find('a', href=True)
        if not link:
            continue

        name = link.get_text(strip=True).replace('↗', '').strip()
        href = link['href']

        match = re.search(r'/articles/(\d+)', href)
        article_id = int(match.group(1)) if match else None

        endpoints.append({
            "name": name,
            "endpoint": endpoint_text,
            "article_id": article_id
        })

    return endpoints


def fetch_article(article_id):
    """Fetch article content via Zendesk API."""
    url = ZENDESK_API.format(article_id)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f"  HTTP {resp.status_code} for article {article_id}")
            return None
    except Exception as e:
        print(f"  Error fetching article {article_id}: {e}")
        return None


def extract_key_name(raw_key):
    """Clean up key name from spec table - strip quotes and whitespace."""
    if not raw_key or raw_key == '-':
        return None
    key = raw_key.strip().strip('"').strip("'").strip()
    return key if key and key != '-' else None


def parse_required(raw_required):
    """Parse the Required field value into a boolean."""
    if not raw_required:
        return None
    text = raw_required.strip().upper()
    if text in ('O', 'REQUIRED', 'YES', 'TRUE', 'MANDATORY'):
        return True
    elif text in ('X', 'OPTIONAL', 'NO', 'FALSE', '-'):
        return False
    return False


def _extract_json_from_div(div_elem):
    """Extract and parse JSON from a div containing formatted JSON text."""
    if not div_elem:
        return None

    # Walk through children to extract the JSON text
    def walk(elem):
        parts = []
        for child in elem.children:
            if isinstance(child, str):
                parts.append(child)
            elif child.name == 'br':
                parts.append('\n')
            elif child.name in ('span', 'div', 'p'):
                parts.append(walk(child))
            else:
                parts.append(child.get_text() if hasattr(child, 'get_text') else str(child))
        return ''.join(parts)

    raw_text = walk(div_elem)
    raw_text = raw_text.replace('\xa0', ' ')
    raw_text = raw_text.replace(' ', ' ')
    # Remove "Copy" button text
    raw_text = re.sub(r'\bCopy\b\s*', '', raw_text)

    # Try to parse as JSON
    try:
        return json.loads(raw_text)
    except (json.JSONDecodeError, ValueError):
        pass

    # Fallback: use get_text() directly (handles &nbsp; better in some cases)
    try:
        fallback = div_elem.get_text()
        fallback = fallback.replace('\xa0', ' ').replace(' ', ' ')
        fallback = re.sub(r'\bCopy\b\s*', '', fallback)
        result = json.loads(fallback)
        return result
    except (json.JSONDecodeError, ValueError):
        pass

    # Try to find JSON object
    for pattern in [r'\{[\s\S]*\}', r'\[[\s\S]*\]']:
        match = re.search(pattern, raw_text)
        if match:
            try:
                return json.loads(match.group())
            except (json.JSONDecodeError, ValueError):
                pass

    text = raw_text.strip()
    return text if text else None


def extract_parameters_from_schema(schema, prefix=''):
    """Recursively extract parameters from a JSON schema."""
    params = []
    if not isinstance(schema, dict):
        return params

    # Skip $schema, title, type at root level of schema
    props = schema.get('properties', {})
    if not props and isinstance(schema, dict):
        # Check if any value is a dict with 'properties' (nested schema)
        for k, v in schema.items():
            if isinstance(v, dict) and 'properties' in v:
                props = v.get('properties', {})
                prefix = k + '.' if not prefix else prefix + k + '.'
                break

    for key, value in props.items():
        if isinstance(value, dict):
            desc = value.get('description', '')
            vtype = value.get('type', '')
            param = {
                "key": key,
                "description": desc,
                "value_type": vtype,
                "default": value.get('default', None),
                "required": False,  # Schema doesn't specify required status reliably
                "optional": True,
                "json_path": prefix + key if prefix else key,
                "json_level": prefix.rstrip('.') if prefix else 'root',
                "source": "schema"
            }
            params.append(param)

            # Check for nested properties
            nested = value.get('properties', {})
            if nested:
                for nk, nv in nested.items():
                    if isinstance(nv, dict):
                        params.append({
                            "key": nk,
                            "description": nv.get('description', ''),
                            "value_type": nv.get('type', ''),
                            "default": nv.get('default', None),
                            "required": False,
                            "optional": True,
                            "json_path": f"{prefix}{key}.{nk}" if prefix else f"{key}.{nk}",
                            "json_level": f"{prefix}{key}" if prefix else key,
                            "source": "schema"
                        })

    return params


def _find_section(soup, keyword):
    """Find an h3 section by keyword text, handling whitespace in nested tags."""
    return soup.find(lambda tag: tag.name == 'h3' and keyword.lower() in tag.get_text().lower())


def _find_all_tables_between(soup, start_elem):
    """Find all <table> elements between start_elem and the next h3 heading."""
    tables = []
    next_boundary = start_elem.find_next('h3')
    current = start_elem.find_next('table')
    while current:
        if next_boundary and getattr(current, 'sourceline', 0) and getattr(next_boundary, 'sourceline', 0):
            if current.sourceline > next_boundary.sourceline:
                break
        elif next_boundary:
            # sourceline not available, compare by tree position
            if current.find_previous('h3') != start_elem:
                break
        tables.append(current)
        current = current.find_next('table')
    return tables


def _parse_spec_table(table):
    """Parse a specification table. Returns (params, is_main_table)."""
    rows = table.find_all('tr')
    if not rows:
        return [], False

    header_cells = rows[0].find_all(['th', 'td'])
    header_texts = [c.get_text(strip=True) for c in header_cells]

    # Detect table type by header pattern
    # Main spec table: No. | Description | Key | Value Type | Default | Required
    is_main = any('Key' in h for h in header_texts) and any('Required' in h for h in header_texts)
    # Enum reference table: has "Value" column and fewer columns
    is_enum = any('Value' in h for h in header_texts) and len(header_texts) <= 4

    params = []
    for row in rows[1:]:
        cells = row.find_all('td')
        if not cells:
            continue

        if is_main and len(cells) >= 6:
            key = extract_key_name(cells[2].get_text(strip=True))
            if key:
                params.append({
                    "number": cells[0].get_text(strip=True),
                    "description": cells[1].get_text(strip=True),
                    "key": key,
                    "value_type": cells[3].get_text(strip=True),
                    "default": cells[4].get_text(strip=True) if cells[4].get_text(strip=True) != '-' else None,
                    "required": parse_required(cells[5].get_text(strip=True)),
                    "optional": not parse_required(cells[5].get_text(strip=True)),
                    "source": "spec_table"
                })
        elif is_main and len(cells) == 1:
            # Section header row like "Offset Setting" or "Additional Option"
            colspan = cells[0].get('colspan')
            if colspan:
                params.append({
                    "number": "",
                    "description": cells[0].get_text(strip=True),
                    "key": None,
                    "value_type": "",
                    "default": None,
                    "required": False,
                    "optional": True,
                    "source": "spec_section_header"
                })
        elif is_enum or (not is_main and len(cells) >= 2):
            # Enum/reference table row
            entry = {"values": [c.get_text(strip=True) for c in cells]}
            params.append(entry)

    return params, is_main


def _parse_all_spec_tables(tables):
    """Parse all specification tables. Returns (main_params, reference_tables)."""
    main_params = []
    reference_tables = []

    for i, table in enumerate(tables):
        params, is_main = _parse_spec_table(table)
        if is_main and i == 0:
            main_params = [p for p in params if p.get("key")]  # Filter out section headers
        elif params:
            # Determine the table name from context
            rows = table.find_all('tr')
            header_text = rows[0].get_text(strip=True) if rows else f"Table {i}"
            ref_entry = {
                "table_index": i,
                "table_header": header_text,
                "rows": [p for p in params if isinstance(p, dict)]
            }
            reference_tables.append(ref_entry)

    return main_params, reference_tables


def _generate_method_examples(http_methods, existing_examples, api_name, json_schema):
    """Generate basic examples for methods that lack documentation examples."""
    generated = []

    # Determine if we need to generate for specific methods
    has_post = any(ex for ex in existing_examples)
    if not has_post and 'POST' in http_methods:
        pass  # No POST example and POST method exists — schema-based generation too complex

    if 'GET' in http_methods:
        # Check if there's already a GET example
        has_get = any('GET' in ex.get('name', '').upper() for ex in existing_examples)
        if not has_get:
            generated.append({
                "name": "GET (Query by ID)",
                "content": {"Argument": {"ID": 1}},
                "note": "GET 请求不带 JSON body，直接通过 URL 路径指定 ID 查询，例如: GET /db/NODE/1"
            })

    if 'PUT' in http_methods:
        has_put = any('PUT' in ex.get('name', '').upper() for ex in existing_examples)
        if not has_put:
            generated.append({
                "name": "PUT (Update by ID)",
                "content": {"Assign": {"ID": 1}},
                "note": "PUT 请求格式与 POST 类似，在 Assign 中指定要修改对象的 ID 及新值。如: {\"Assign\": {\"1\": {\"ID\": 1, ...新参数值...}}}"
            })

    if 'DELETE' in http_methods:
        has_delete = any('DELETE' in ex.get('name', '').upper() for ex in existing_examples)
        if not has_delete:
            generated.append({
                "name": "DELETE (Remove by ID)",
                "content": {"Argument": {"ID": 1}},
                "note": "DELETE 请求通过 Argument 指定要删除的对象 ID。如: {\"Argument\": {\"ID\": 1}}"
            })

    return generated


def parse_article_body(article_data):
    """Parse the HTML body of an article to extract API details."""
    if not article_data:
        return None

    body_html = article_data.get('article', {}).get('body', '')
    soup = BeautifulSoup(body_html, 'html.parser')

    result = {
        "api_name": article_data.get('article', {}).get('title', ''),
        "http_method": [],
        "url": "",
        "parameters": [],
        "json_schema": None,
        "json_examples": [],
        "reference_tables": [],
        "labels": article_data.get('article', {}).get('label_names', []),
        "source_article_id": article_data.get('article', {}).get('id'),
    }

    # --- Extract Input URI ---
    uri_section = _find_section(soup, 'Input URI')
    if uri_section:
        uri_table = uri_section.find_next('table')
        if uri_table:
            result["url"] = uri_table.get_text(strip=True)

    # --- Extract Active Methods ---
    method_section = _find_section(soup, 'Active Methods')
    if method_section:
        method_table = method_section.find_next('table')
        if method_table:
            method_text = method_table.get_text(strip=True)
            methods = re.findall(r'(GET|POST|PUT|DELETE|PATCH)', method_text)
            result["http_method"] = methods if methods else [method_text.strip()]

    # --- Extract JSON Schema ---
    schema_section = _find_section(soup, 'JSON Schema')
    if schema_section:
        schema_div = schema_section.find_next('div', id=re.compile(r'copyTarget'))
        if schema_div:
            schema_json = _extract_json_from_div(schema_div)
            if schema_json:
                result["json_schema"] = schema_json

    # --- Extract Examples ---
    examples_section = _find_section(soup, 'Example')
    if examples_section:
        current = examples_section
        seen_examples = set()
        while True:
            current = current.find_next('div', id=re.compile(r'copyTarget'))
            if not current:
                break
            ex_json = _extract_json_from_div(current)
            if ex_json:
                name_elem = current.find_previous('p', class_='btn_dropdown')
                ex_name = name_elem.get_text(strip=True) if name_elem else "Example"
                if ex_name not in seen_examples:
                    seen_examples.add(ex_name)
                    result["json_examples"].append({"name": ex_name, "content": ex_json})

    # --- Generate method-specific examples for GET/PUT/DELETE ---
    method_examples = _generate_method_examples(
        result["http_method"], result["json_examples"],
        result["api_name"], result["json_schema"]
    )
    result["json_examples"].extend(method_examples)

    # --- Extract ALL Specification tables ---
    spec_section = _find_section(soup, 'Specifications')
    spec_params = []
    if spec_section:
        spec_tables = _find_all_tables_between(soup, spec_section)
        if spec_tables:
            spec_params, reference_tables = _parse_all_spec_tables(spec_tables)
            result["reference_tables"] = reference_tables

    # --- Merge parameters from schema and spec table ---
    schema_params = []
    if result["json_schema"]:
        schema_params = extract_parameters_from_schema(result["json_schema"])

    # Merge: spec table params take priority for required/default/description
    merged = {}
    for p in schema_params:
        k = p["key"]
        merged[k] = p

    for p in spec_params:
        k = p.get("key")
        if not k:
            continue
        if k in merged:
            # Merge: spec table overrides schema for these fields
            merged[k]["number"] = p.get("number", merged[k].get("number"))
            merged[k]["description"] = p.get("description") or merged[k].get("description")
            merged[k]["value_type"] = p.get("value_type") or merged[k].get("value_type")
            merged[k]["default"] = p.get("default") if p.get("default") is not None else merged[k].get("default")
            merged[k]["required"] = p.get("required", merged[k].get("required"))
            merged[k]["optional"] = p.get("optional", merged[k].get("optional"))
            merged[k]["source"] = "merged"
        else:
            # Param only in spec table, not in schema
            json_path = _determine_json_path(k, result["json_schema"])
            merged[k] = {
                "key": k,
                "description": p.get("description", ""),
                "value_type": p.get("value_type", ""),
                "default": p.get("default"),
                "required": p.get("required", False),
                "optional": p.get("optional", True),
                "number": p.get("number", ""),
                "json_path": json_path,
                "json_level": _get_parent_path(json_path),
                "source": "spec_table"
            }

    # Also capture params in schema but NOT in spec table
    schema_only = []
    spec_keys = {p.get("key") for p in spec_params if p.get("key")}
    for p in schema_params:
        if p["key"] not in spec_keys:
            p["in_schema_only"] = True
            schema_only.append(p["key"])

    result["parameters"] = list(merged.values())
    result["schema_only_params"] = schema_only

    return result


def _determine_json_path(key, json_schema):
    """Search for a key in the schema and return its JSON path."""
    if not key or not json_schema or not isinstance(json_schema, dict):
        return key

    def search(schema, target, path=''):
        if not isinstance(schema, dict):
            return None
        if target in schema:
            return path + '.' + target if path else target
        for k, v in schema.items():
            if isinstance(v, dict):
                result = search(v, target, path + '.' + k if path else k)
                if result:
                    return result
            if k == 'properties' and isinstance(v, dict):
                result = search(v, target, path)
                if result:
                    return result
        return None

    found = search(json_schema, key)
    return found if found else key


def _get_parent_path(full_path):
    """Get the parent path from a full JSON path."""
    if not full_path or '.' not in full_path:
        return 'root'
    return '.'.join(full_path.split('.')[:-1])


def load_progress():
    """Load saved progress for resuming."""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_progress(results, processed_endpoints):
    """Save progress for resuming."""
    progress = {
        "results": results,
        "processed_endpoints": processed_endpoints,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
    }
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def process_all_endpoints(structure, resume=True):
    """Fetch and parse all endpoints."""
    results = {}
    processed_set = set()
    total = 0

    if resume:
        saved = load_progress()
        if saved:
            results = saved.get("results", {})
            processed_set = set(saved.get("processed_endpoints", []))
            print(f"Resuming from previous run: {len(processed_set)} endpoints already processed")

    # Count total
    all_endpoints = []
    for section_name, section_data in structure.items():
        for ep in section_data.get("endpoints", []):
            all_endpoints.append((section_name, None, ep))
        for sub_name, sub_endpoints in section_data.get("subsections", {}).items():
            for ep in sub_endpoints:
                all_endpoints.append((section_name, sub_name, ep))

    total = len(all_endpoints)
    print(f"Total endpoints to process: {total}")
    print(f"Already processed: {len(processed_set)}")
    print("=" * 60)

    for idx, (section_name, sub_name, ep) in enumerate(all_endpoints):
        ep_key = f"{section_name}:{sub_name or ''}:{ep['endpoint']}"
        if ep_key in processed_set:
            continue

        processed = len(processed_set) + 1
        label = f"[{section_name}]"
        if sub_name:
            label += f" [{sub_name}]"
        print(f"  [{processed}/{total}] {label} {ep['endpoint']} - {ep['name']}")

        article_data = fetch_article(ep['article_id'])
        parsed = parse_article_body(article_data)

        if parsed:
            parsed["section"] = section_name
            if sub_name:
                parsed["subsection"] = sub_name

            # Store in results structure
            if section_name not in results:
                results[section_name] = {"endpoints": {}, "subsections": {}}

            if sub_name:
                if sub_name not in results[section_name]["subsections"]:
                    results[section_name]["subsections"][sub_name] = {}
                results[section_name]["subsections"][sub_name][ep['endpoint']] = parsed
            else:
                results[section_name]["endpoints"][ep['endpoint']] = parsed

        processed_set.add(ep_key)

        # Save progress every 20 endpoints
        if processed % 20 == 0:
            save_progress(results, list(processed_set))
            print(f"  [Progress saved: {processed}/{total}]")

        time.sleep(0.15)

    save_progress(results, list(processed_set))
    return results, total


def main():
    print("=" * 60)
    print("Midas API Documentation Scraper")
    print("=" * 60)

    # Step 1: Parse main page
    print("\n[1/3] Parsing main page structure...")
    structure = parse_main_page()
    if not structure:
        print("ERROR: Failed to parse main page")
        return

    total = 0
    for section_name, section_data in structure.items():
        n = len(section_data.get("endpoints", []))
        sub_n = sum(len(v) for v in section_data.get("subsections", {}).values())
        total += n + sub_n
        print(f"  {section_name}: {n} + {sub_n} sub = {n+sub_n} endpoints")

    print(f"  Total: {total} endpoints")

    # Step 2: Fetch and parse
    print(f"\n[2/3] Fetching and parsing articles...")
    results, actual_total = process_all_endpoints(structure)

    # Step 3: Build output
    print(f"\n[3/3] Building final output...")
    output = {
        "meta": {
            "source": "https://support.midasuser.com/hc/en-us/articles/33016922742937-MIDAS-API-Online-Manual",
            "description": "MIDAS API Online Manual - Unified Knowledge Base for AI retrieval",
            "total_endpoints": actual_total,
            "sections": list(structure.keys()),
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "schema_version": "1.0"
        },
        "structure": structure,
        "api_data": results
    }

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nDone! Output: {OUTPUT_FILE}")
    print(f"File size: {os.path.getsize(OUTPUT_FILE) / 1024:.1f} KB")

    # Clean up progress file on success
    if os.path.exists(PROGRESS_FILE):
        os.remove(PROGRESS_FILE)


if __name__ == "__main__":
    main()
