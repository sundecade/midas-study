"""02 - Build a 20+30+20 m continuous beam.

Correct order:
1. Material
2. Section
3. Nodes
4. Elements
5. Supports
"""

from utils import MidasAPI, get_config, show


config = get_config()

material = {
    "Assign": {
        "1": {
            "TYPE": "CONC",
            "NAME": "C50",
            "HE_SPEC": 0,
            "HE_COND": 0,
            "PLMT": 0,
            "P_NAME": "",
            "bMASS_DENS": False,
            "DAMP_RAT": 0,
            "PARAM": [
                {
                    "P_TYPE": 1,
                    "STANDARD": "JTG3362-18(RC)",
                    "CODE": "",
                    "DB": "C50",
                    "bELAST": False,
                    "ELAST": 0,
                }
            ],
        }
    }
}
show("Create C50 material", MidasAPI("POST", "/db/MATL", material, config))

section = {
    "Assign": {
        "1": {
            "SECTTYPE": "DBUSER",
            "SECT_NAME": "Box_1.5m",
            "SECT_BEFORE": {
                "OFFSET_PT": "CC",
                "HORZ_OFFSET_OPT": 0,
                "VERT_OFFSET_OPT": 0,
                "USE_SHEAR_DEFORM": False,
                "USE_WARPING_EFFECT": False,
                "SHAPE": "B",
                "DATATYPE": 2,
                "SECT_I": {"vSIZE": [1.5, 1.0, 0.2, 0.2, 0.2, 0.2]},
            },
        }
    }
}
show("Create box section", MidasAPI("POST", "/db/SECT", section, config))

nodes = {}
for index in range(36):
    node_id = index + 1
    nodes[str(node_id)] = {"X": index * 2.0, "Y": 0, "Z": 0}
show("Create nodes", MidasAPI("POST", "/db/NODE", {"Assign": nodes}, config))

elements = {}
for index in range(35):
    elem_id = index + 1
    elements[str(elem_id)] = {
        "TYPE": "BEAM",
        "MATL": 1,
        "SECT": 1,
        "NODE": [index + 1, index + 2],
        "ANGLE": 0,
    }
show("Create beam elements", MidasAPI("POST", "/db/ELEM", {"Assign": elements}, config))

supports = {
    "Assign": {
        "1": {"ITEMS": [{"ID": 1, "GROUP_NAME": "", "CONSTRAINT": "1111110"}]},
        "11": {"ITEMS": [{"ID": 11, "GROUP_NAME": "", "CONSTRAINT": "0110000"}]},
        "26": {"ITEMS": [{"ID": 26, "GROUP_NAME": "", "CONSTRAINT": "0110000"}]},
        "36": {"ITEMS": [{"ID": 36, "GROUP_NAME": "", "CONSTRAINT": "0110000"}]},
    }
}
show("Create supports", MidasAPI("POST", "/db/CONS", supports, config))
