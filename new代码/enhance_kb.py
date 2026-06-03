"""
Enhance midas_api_knowledge_base.json with explicit request templates.
The JSON schema shows inner structure only; this adds the required wrapping layers
(Assign/Argument + numeric keys) so LLMs generate correct full JSON.
"""
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KB_PATH = os.path.join(BASE_DIR, "midas_api_knowledge_base.json")


def safe_json_parse(s):
    """Parse a JSON string, with fallback fixes for common issues like unescaped
    Windows path backslashes in the stored content."""
    if not isinstance(s, str) or not s.strip():
        return None
    try:
        return json.loads(s)
    except (json.JSONDecodeError, ValueError):
        pass
    # Fix unescaped backslashes (common in Windows paths embedded in JSON strings)
    try:
        fixed = s.replace("\\", "\\\\")
        return json.loads(fixed)
    except (json.JSONDecodeError, ValueError):
        pass
    return None


def get_wrapper_type_and_info(ep_data):
    """
    Determine the wrapper type from examples.
    Returns (wrapper_type, wrapper_info_string).

    wrapper_type is one of:
      "Assign+Numeric" — DB POST/PUT: {"Assign": {"1": {data}}}
      "Assign+ID"      — DB GET/PUT simple: {"Assign": {"ID": 1}}
      "Argument"        — DOC/OPE: {"Argument": {data}}
      "EndpointKey"     — Some OPE/VIEW: {"ENDPOINTKEY": {data}}
    """
    examples = ep_data.get("json_examples", [])
    section = ep_data.get("section", "")
    http_methods = ep_data.get("http_method", [])

    wrappers_seen = set()

    for ex in examples:
        content = ex.get("content", ex.get("data", {}))
        # Handle JSON string content
        if isinstance(content, str) and content.strip():
            try:
                content = safe_json_parse(content)
            except (json.JSONDecodeError, ValueError):
                continue
        if not isinstance(content, dict) or not content:
            continue

        outer_keys = list(content.keys())

        if "Assign" in outer_keys:
            av = content["Assign"]
            if isinstance(av, dict) and av:
                first_key = list(av.keys())[0]
                if first_key.isdigit() and isinstance(av[first_key], dict):
                    wrappers_seen.add("Assign+Numeric")
                elif first_key == "ID":
                    wrappers_seen.add("Assign+ID")
                else:
                    wrappers_seen.add("Assign+Numeric")
        elif "Argument" in outer_keys:
            wrappers_seen.add("Argument")
        else:
            wrappers_seen.add("EndpointKey")

    # For DB section without examples, default to Assign+Numeric
    if not wrappers_seen and section == "DB":
        wrappers_seen.add("Assign+Numeric")
    # For DOC/OPE/VIEW/POST without examples, default to Argument
    if not wrappers_seen and section in ("DOC", "OPE", "VIEW", "POST"):
        wrappers_seen.add("Argument")

    # Determine primary wrapper type
    if "Assign+Numeric" in wrappers_seen:
        wrapper_type = "Assign+Numeric"
        wrapper_info = (
            "MANDATORY JSON STRUCTURE: "
            "{\"Assign\": {\"N\": {data}}}. "
            "Three layers required: (1) Outer \"Assign\" key, "
            "(2) numeric string keys (\"1\",\"2\",...) as assignment indices, "
            "(3) each index holds the actual data object or ITEMS array. "
            "WRONG FORMAT: {\"FORCE\":\"kN\",\"DIST\":\"m\"} — missing Assign wrapper and numeric key! "
            "CORRECT FORMAT: {\"Assign\": {\"1\": {\"FORCE\":\"kN\",\"DIST\":\"m\"}}}. "
            "NEVER send raw data without the Assign wrapper and numeric index."
        )
    elif "Assign+ID" in wrappers_seen:
        wrapper_type = "Assign+ID"
        wrapper_info = (
            "MANDATORY JSON STRUCTURE: "
            "{\"Assign\": {\"ID\": <id>, ...fields}}. "
            "For PUT: specify ID of record to update plus new field values."
        )
    elif "Argument" in wrappers_seen:
        wrapper_type = "Argument"
        wrapper_info = (
            "MANDATORY JSON STRUCTURE: "
            "{\"Argument\": {data}}. "
            "All parameters go directly inside the \"Argument\" object."
        )
    elif "EndpointKey" in wrappers_seen:
        # Find the first non-Assign, non-Argument key used
        for ex in examples:
            content = ex.get("content", ex.get("data", {}))
            if isinstance(content, dict) and content:
                for k in content:
                    if k not in ("Assign", "Argument"):
                        wrapper_type = f"Key:{k}"
                        wrapper_info = (
                            f"MANDATORY JSON STRUCTURE: "
                            f"{{\"{k}\": {{data}}}}. "
                            f"Data goes directly inside the \"{k}\" object, no numeric index."
                        )
                        break
                break
        else:
            wrapper_type = "Unknown"
            wrapper_info = ""
    else:
        wrapper_type = "Unknown"
        wrapper_info = ""

    return wrapper_type, wrapper_info


def _apply_wrapper(inner_data, wrapper_type):
    """Apply the correct outer wrapper to inner data (shared by all template builders)."""
    if wrapper_type == "Assign+Numeric":
        return {"Assign": {"<1>": inner_data}}
    elif wrapper_type == "Assign+ID":
        return {"Assign": inner_data}
    elif wrapper_type.startswith("Key:"):
        key_name = wrapper_type.split(":", 1)[1]
        return {key_name: inner_data}
    else:
        return {"Argument": inner_data}


def _prop_to_placeholder(prop_info):
    """Convert a JSON schema property to a placeholder value (shared helper)."""
    ptype = prop_info.get("type", "string")
    if ptype == "integer":
        return "<integer>"
    elif ptype == "number":
        return "<number>"
    elif ptype == "boolean":
        return "<boolean>"
    elif ptype == "array":
        items = prop_info.get("items", {})
        if isinstance(items, dict) and items.get("type") == "object" and "properties" in items:
            return [{k: _prop_to_placeholder(v) for k, v in items["properties"].items()}]
        return ["<value>"]
    elif ptype == "object":
        sub_props = prop_info.get("properties", {})
        if sub_props:
            return {k: _prop_to_placeholder(v) for k, v in sub_props.items()}
        return {}
    return "<string>"


def build_template_from_example(example_content, method, wrapper_type):
    """Convert an example's content into a clean template with <type> placeholders."""
    if isinstance(example_content, str) and example_content.strip():
        parsed = safe_json_parse(example_content)
        if parsed is not None:
            example_content = parsed
    if not isinstance(example_content, dict):
        return example_content

    def make_template(obj):
        if isinstance(obj, dict):
            result = {}
            for k, v in obj.items():
                result[k] = make_template(v)
            return result
        elif isinstance(obj, list):
            if obj:
                return [make_template(obj[0])]
            return ["<value>"]
        elif isinstance(obj, str):
            return f"<string>"
        elif isinstance(obj, bool):
            return f"<boolean>"
        elif isinstance(obj, (int, float)):
            if isinstance(obj, int):
                return f"<integer>"
            return f"<number>"
        elif obj is None:
            return "<value>"
        return str(obj)

    template = make_template(example_content)

    # For DB PUT with Assign+ID (simplified example), fix to use numeric key structure
    if method == "PUT" and wrapper_type == "Assign+Numeric":
        if isinstance(template, dict) and "Assign" in template:
            av = template["Assign"]
            if isinstance(av, dict) and "ID" in av and not any(k.isdigit() for k in av):
                template["Assign"] = {"<1>": av}

    # Normalize all numeric keys to generic <1>, <2>, ... placeholders
    # (examples may have actual IDs like "6001" that confuse the LLM)
    if wrapper_type == "Assign+Numeric":
        if isinstance(template, dict) and "Assign" in template:
            av = template["Assign"]
            if isinstance(av, dict):
                numeric_keys = [k for k in av if k.strip("<>").isdigit()]
                if numeric_keys:
                    new_av = {}
                    for i, old_key in enumerate(numeric_keys, 1):
                        new_av[f"<{i}>"] = av[old_key]
                    template["Assign"] = new_av

    return template


def build_template_from_schema(ep_data, wrapper_type, section):
    """Build a POST template from schema properties."""
    schema = ep_data.get("json_schema", {})
    if not isinstance(schema, dict) or not schema:
        return None

    schema_name = list(schema.keys())[0]
    schema_obj = schema.get(schema_name, {})
    if not isinstance(schema_obj, dict):
        return None

    props = schema_obj.get("properties", {})
    if not props:
        return None

    inner_data = {key: _prop_to_placeholder(val) for key, val in props.items()}

    # Detect if schema properties embed a wrapper key to avoid double-wrapping
    wrapper_keys = {"Argument", "Assign"}
    if len(inner_data) == 1:
        only_key = list(inner_data.keys())[0]
        if only_key in wrapper_keys and isinstance(inner_data[only_key], dict):
            inner_data = inner_data[only_key]

    return _apply_wrapper(inner_data, wrapper_type)


def _build_template_from_params(ep_data, method, wrapper_type):
    """Build a minimal template from parameters when no examples or schema exist."""
    params = ep_data.get("parameters", [])
    if not params:
        return None

    inner_data = {}
    for p in params:
        key = p.get("key", "")
        if not key:
            continue
        ptype = p.get("value_type", "String")
        if "Array" in ptype:
            inner_data[key] = ["<value>"]
        elif "Integer" in ptype or "Number" in ptype:
            inner_data[key] = "<number>"
        elif "Boolean" in ptype:
            inner_data[key] = "<boolean>"
        elif "Object" in ptype:
            inner_data[key] = {}
        else:
            inner_data[key] = "<string>"

    return _apply_wrapper(inner_data, wrapper_type)


def build_field_guide(ep_data):
    """Build a concise field reference from parameters."""
    params = ep_data.get("parameters", [])
    if not params:
        return None

    guide = {}
    for p in params:
        key = p.get("key", "")
        if not key:
            continue
        guide[key] = {
            "required": bool(p.get("required")),
            "type": p.get("value_type", ""),
            "default": p.get("default"),
            "desc": (p.get("description") or "")[:300],
        }
    return guide


def _iter_all_endpoints(kb):
    """Yield (ep_path, ep_data) for every endpoint in the knowledge base."""
    for section_data in kb["api_data"].values():
        for ep_path, ep_data in section_data.get("endpoints", {}).items():
            yield ep_path, ep_data
        for sub_data in section_data.get("subsections", {}).values():
            for ep_path, ep_data in sub_data.items():
                yield ep_path, ep_data


def _inject_sect_vsize_guide(templates, http_methods):
    """为SECT端点注入vSIZE数组各索引的字段含义说明。
    vSIZE是一个数值数组，每个位置有固定的工程含义（如高度、宽度等），
    不同SHAPE类型的vSIZE含义和数量不同。MIDAS网页表格虽有9列，
    但每个截面类型只用其中一部分，**只用到的列写数据，不用的不要补0占位**。
    若无此说明，LLM会自行猜测数组顺序（通常猜反宽/高）或补多余0。"""
    vsize_guide = (
        "【vSIZE数组索引含义】\n"
        "vSIZE 是一个数值数组，不同截面类型使用的数组长度不同。\n"
        "⚠️ 核心规则：**只用截面类型实际需要的参数个数，不要补多余的 0！**\n"
        "MIDAS 数组顺序：**高度(H)在前，宽度(B)在后**。\n\n"
        "箱型截面(SHAPE=\"B\") — VALUE/DBUSER 均只用 4 个值:\n"
        "  [0] H  — 截面总高度 (m)\n"
        "  [1] B  — 截面总宽度 (m)\n"
        "  [2] tw — 腹板厚度 (m)\n"
        "  [3] tf — 翼缘厚度 (m)，顶板和底板同厚\n"
        "  ✅ 正确: vSIZE=[1.5, 3.0, 0.3, 0.3]  ← 4个值\n"
        "  ❌ 错误: vSIZE=[1.5, 3.0, 0.3, 0.3, 0, 0, 0, 0]  ← 不要补0!\n\n"
        "其他常用 SHAPE 类型:\n"
        "  实心矩形(SHAPE=\"SB\"): 2个值 [H, B]\n"
        "  实心圆形(SHAPE=\"SR\"): 1个值 [D]\n"
        "  H型钢(SHAPE=\"H\"): 参照 MIDAS UI 输入对话框的字段数\n\n"
        "通用规则：每个截面类型只填写它实际需要的参数个数，表格中空着的列不要补 0 占位。"
    )
    for method in http_methods:
        if method in templates:
            if f"{method}_note" not in templates:
                templates[f"{method}_note"] = ""
            templates[f"{method}_note"] = vsize_guide + "\n" + templates[f"{method}_note"]


def enhance_knowledge_base():
    with open(KB_PATH, "r", encoding="utf-8") as f:
        kb = json.load(f)

    count = 0
    for ep_path, ep_data in _iter_all_endpoints(kb):
        _enhance_one_endpoint(ep_data, ep_path)
        count += 1

    # Atomic write: temp file first, then rename to avoid corruption
    tmp_path = KB_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(kb, f, indent=2, ensure_ascii=False)
    os.replace(tmp_path, KB_PATH)

    print(f"Enhanced {count} endpoints → {KB_PATH}")


def _enhance_one_endpoint(ep_data, ep_path):
    """Enhance a single endpoint with request_template and field_guide."""
    wrapper_type, wrapper_info = get_wrapper_type_and_info(ep_data)
    http_methods = ep_data.get("http_method", [])
    examples = ep_data.get("json_examples", [])
    section = ep_data.get("section", "")

    templates = {}
    templates["_wrapper_type"] = wrapper_type
    templates["_wrapper_info"] = wrapper_info

    # Group examples by method
    method_examples = {m: [] for m in http_methods}
    for ex in examples:
        name = ex.get("name", "")
        for m in http_methods:
            if m in name:
                method_examples[m].append(ex)
                break
        else:
            # Try to infer method from content structure
            content = ex.get("content", ex.get("data", {}))
            # Handle JSON string content
            if isinstance(content, str) and content.strip():
                parsed = safe_json_parse(content)
                if parsed is not None:
                    content = parsed
                    ex["content"] = content  # store parsed version back
                else:
                    continue
            if isinstance(content, dict):
                if "Assign" in content:
                    av = content["Assign"]
                    if isinstance(av, dict) and av:
                        first_key = list(av.keys())[0]
                        if first_key.isdigit() and isinstance(av[first_key], dict):
                            inner = av[first_key]
                            if "ITEMS" in inner:
                                method_examples.setdefault("POST", []).append(ex)
                            elif "ID" in inner:
                                # Has ID + other fields → PUT; ID only → POST
                                non_id = [k for k in inner if k != "ID"]
                                if non_id:
                                    method_examples.setdefault("PUT", []).append(ex)
                                else:
                                    method_examples.setdefault("POST", []).append(ex)
                            else:
                                # Numeric key with data fields (no ID, no ITEMS) → POST
                                method_examples.setdefault("POST", []).append(ex)
                        elif first_key == "ID":
                            method_examples.setdefault("PUT", []).append(ex)
                        else:
                            # Non-numeric, non-ID key → treat as POST data
                            method_examples.setdefault("POST", []).append(ex)
                elif "Argument" in content:
                    av = content["Argument"]
                    if isinstance(av, dict):
                        arg_keys = list(av.keys())
                        if arg_keys == ["ID"]:
                            if "DELETE" in name:
                                method_examples.setdefault("DELETE", []).append(ex)
                            else:
                                method_examples.setdefault("GET", []).append(ex)
                        else:
                            # Argument with data fields → POST
                            method_examples.setdefault("POST", []).append(ex)

    # Build per-method templates
    for method in http_methods:
        mex = method_examples.get(method, [])
        if mex:
            best = mex[0]
            content = best.get("content", best.get("data", {}))
            if isinstance(content, dict) and content:
                templates[method] = build_template_from_example(content, method, wrapper_type)
            if best.get("note"):
                templates[f"{method}_note"] = best["note"]
        else:
            # No example for this method — try schema fallback
            if method in ("POST", "PUT"):
                t = build_template_from_schema(ep_data, wrapper_type, section)
                if t:
                    templates[method] = t

    # Final fallback: for methods still without templates, build from parameters
    for method in http_methods:
        if method not in templates:
            t = _build_template_from_params(ep_data, method, wrapper_type)
            if t:
                templates[method] = t

    # ── 后处理：修复模板质量 ──

    # 1. POST 模板如果包含 >2 个重复条目，截断为 2 个（避免 LLM 迷失）
    if "POST" in templates:
        post_t = templates["POST"]
        if isinstance(post_t, dict) and "Assign" in post_t:
            av = post_t["Assign"]
            if isinstance(av, dict):
                numeric_keys = [k for k in av if k.strip("<>").isdigit()]
                if len(numeric_keys) > 2:
                    # 只保留前2个不同的结构，删除重复
                    seen_structures = []
                    to_keep = {}
                    for key in numeric_keys:
                        struct = json.dumps(av[key], sort_keys=True, ensure_ascii=False)
                        if struct not in seen_structures:
                            seen_structures.append(struct)
                            to_keep[key] = av[key]
                        if len(to_keep) >= 2:
                            break
                    post_t["Assign"] = to_keep

    # 2. PUT 模板如果只有 ID 字段，用 field_guide 中的关键字段补充
    if "PUT" in templates:
        put_t = templates["PUT"]
        if isinstance(put_t, dict) and "Assign" in put_t:
            av = put_t["Assign"]
            if isinstance(av, dict):
                inner = None
                numeric_key = None
                for k in av:
                    if k.strip("<>").isdigit():
                        inner = av[k]
                        numeric_key = k
                        break
                if inner is None:
                    inner = av
                if isinstance(inner, dict):
                    inner_fields = [k for k in inner if not k.startswith("__")]
                    # 如果只有 ID 字段（1-2个字段），需要补充
                    if len(inner_fields) <= 2 and "ID" in inner_fields:
                        # 从 POST 模板提取顶层字段名作为补充参考
                        enrich_keys = set()
                        if "POST" in templates:
                            post_av = templates["POST"].get("Assign", {})
                            for pk in post_av:
                                if pk.strip("<>").isdigit() and isinstance(post_av[pk], dict):
                                    enrich_keys.update(k for k in post_av[pk] if not k.startswith("__"))
                        # 没有 POST 模板时，用 field_guide
                        if not enrich_keys:
                            guide = build_field_guide(ep_data) or {}
                            enrich_keys = set(guide.keys())
                        for key in enrich_keys:
                            if key in inner_fields or key == "ITEMS" or key.startswith("__"):
                                continue
                            inner[key] = "<string>"
                        if numeric_key:
                            av[numeric_key] = inner
                        templates["PUT"] = put_t

    # 3. ITEMS 模板：添加多节点说明
    for method in ["POST"]:
        if method in templates:
            tmpl_str = json.dumps(templates[method])
            if "ITEMS" in tmpl_str:
                if f"{method}_note" not in templates:
                    templates[f"{method}_note"] = ""
                templates[f"{method}_note"] += (
                    "如需定义多个对象（如多个节点/多个约束），每个对象应放在独立的数字键下。"
                    '例: {"Assign": {"1": {"ITEMS": [{...}]}, "2": {"ITEMS": [{...}]}}}'
                    " 而不是把所有对象都放在同一个键的 ITEMS 数组里。"
                )

    # 4. 多模板变体：添加区分说明（如 SECT 的等截面/变截面）
    for method in ["POST"]:
        if method in templates:
            tmpl = templates[method]
            if isinstance(tmpl, dict) and "Assign" in tmpl:
                av = tmpl["Assign"]
                if isinstance(av, dict):
                    num_keys = [k for k in av if k.strip("<>").isdigit()]
                    if len(num_keys) >= 2:
                        # 比较各变体的字段差异
                        def _leaf_keys(d, prefix=""):
                            keys = set()
                            if isinstance(d, dict):
                                for k, v in d.items():
                                    keys.update(_leaf_keys(v, f"{prefix}.{k}" if prefix else k))
                            else:
                                keys.add(prefix)
                            return keys

                        variants = {}
                        for k in num_keys:
                            if isinstance(av[k], dict):
                                variants[k] = _leaf_keys(av[k])
                        if len(variants) >= 2:
                            vk = list(variants.keys())
                            diff1 = variants[vk[0]] - variants[vk[1]]
                            diff2 = variants[vk[1]] - variants[vk[0]]
                            parts = [f"模板包含 {len(num_keys)} 种变体，请根据需求选择："]
                            if diff1:
                                parts.append(f"{vk[0]}特有: {', '.join(sorted(diff1)[:5])}")
                            if diff2:
                                parts.append(f"{vk[1]}特有: {', '.join(sorted(diff2)[:5])}")

                            # SECT 特殊说明：解释每个变体的 SECTTYPE
                            if ep_path == "/db/SECT":
                                if "SECT_BEFORE.DATATYPE" in str(diff1):
                                    parts.append(f"{vk[0]}=DBUSER类型(用户自定义尺寸输入)")
                                if "SECT_BEFORE.TYPE" in str(diff1):
                                    parts.append(f"{vk[0]}=VARIABLE类型(变截面)")
                                if "SECT_BEFORE.DATATYPE" in str(diff2):
                                    parts.append(f"{vk[1]}=DBUSER类型(用户自定义尺寸输入)")
                                if "SECT_BEFORE.TYPE" in str(diff2):
                                    parts.append(f"{vk[1]}=VARIABLE类型(变截面)")

                            note = "。 ".join(parts)
                            if f"{method}_note" not in templates:
                                templates[f"{method}_note"] = ""
                            templates[f"{method}_note"] = note + "\n" + templates[f"{method}_note"]

    # 5. M1端点警告：M1=Hyper-S求解器专用，与主端点结构完全不同
    if "-M1" in ep_path:
        for method in http_methods:
            if method in templates:
                if f"{method}_note" not in templates:
                    templates[f"{method}_note"] = ""
                templates[f"{method}_note"] = (
                    "⚠️ 此为Hyper-S求解器专用接口(M1)，字段结构与标准接口完全不同。"
                    f"标准建模请使用 {ep_path.replace('-M1', '')}。"
                    "此接口使用Assign+ID(非Assign+Numeric)，字段直接放在Assign下(无PARAM数组)。"
                    "\n" + templates[f"{method}_note"]
                )

    # 6. SECT截面vSIZE字段说明：注入截面尺寸数组的索引含义
    if ep_path == "/db/SECT":
        _inject_sect_vsize_guide(templates, http_methods)

    ep_data["request_templates"] = templates

    # Add field guide
    guide = build_field_guide(ep_data)
    if guide:
        ep_data["request_field_guide"] = guide


if __name__ == "__main__":
    enhance_knowledge_base()
