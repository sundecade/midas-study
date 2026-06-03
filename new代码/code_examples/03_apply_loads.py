"""03 - Add simple self-weight.

Use /db/BODF for self-weight.  Beam member loads use /db/BMLD and have a more
specific ITEMS structure; check the API search before changing that body.
"""

from utils import MidasAPI, get_config, show


config = get_config()

self_weight = {
    "Assign": {
        "1": {
            "LCNAME": "SelfWeight",
            "GROUP_NAME": "",
            "FV": [0, 0, -1],
        }
    }
}
show("Create self-weight load", MidasAPI("POST", "/db/BODF", self_weight, config))
