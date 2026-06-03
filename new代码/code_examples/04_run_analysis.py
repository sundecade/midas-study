"""04 - Run analysis.

Some MIDAS versions accept an empty Argument for normal analysis.  If your
product asks for a type, use {"Argument": {"TYPE": "Pushover"}} only for
pushover analysis.
"""

from utils import MidasAPI, get_config, show


config = get_config()
show("Run analysis", MidasAPI("POST", "/doc/ANAL", {"Argument": {}}, config))
