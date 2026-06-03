"""05 - Extract a POST result table.

Many result tables share the real command /post/TABLE.  The difference is the
TABLE_TYPE value in the Argument body.
"""

from utils import MidasAPI, get_config, save_json, show


config = get_config()

element_weight_table = {
    "Argument": {
        "TABLE_NAME": "Element Weight",
        "TABLE_TYPE": "ELEMENTWEIGHT",
        "EXPORT_PATH": "",
        "NODE_ELEMS": {"TO": "1 to 35"},
    }
}
result = MidasAPI("POST", "/post/TABLE", element_weight_table, config)
show("Element weight table", result)

if result is not None:
    save_json("element_weight_result.json", result)
