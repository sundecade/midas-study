"""01 - Project setup.

Normal order starts with a new project, then units.  /db/UNIT supports GET and
PUT only, so do not send POST to /db/UNIT.
"""

from utils import MidasAPI, get_config, show


config = get_config()

show("New project", MidasAPI("POST", "/doc/NEW", {"Argument": {}}, config))

unit_body = {
    "Assign": {
        "1": {
            "ID": 1,
            "FORCE": "N",
            "DIST": "m",
            "HEAT": "C",
            "TEMPER": "C",
        }
    }
}
show("Set units", MidasAPI("PUT", "/db/UNIT", unit_body, config))
