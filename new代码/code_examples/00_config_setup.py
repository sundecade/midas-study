"""00 - Check the MIDAS API connection.

Run this first.  It does not modify the model.
"""

from utils import MidasAPI, get_config, show


config = get_config()
print("base_url:", config["base_url"])
print("mapi_key:", config["mapi_key"][:8] + "..." if config["mapi_key"] else "<empty>")

status = MidasAPI("GET", "/ope/PROJECTSTATUS", config=config)
show("Project status", status)
