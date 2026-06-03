"""06 - Set view angle and capture an image.

Edit EXPORT_PATH to a writable path on your computer before running capture.
"""

from utils import MidasAPI, get_config, show


config = get_config()

show("Set view angle", MidasAPI("POST", "/view/ANGLE", {"Argument": {"HORIZONTAL": 30, "VERTICAL": 20}}, config))

capture = {
    "Argument": {
        "FIGURE_NAME": "continuous_beam",
        "EXPORT_PATH": r"C:\temp\continuous_beam.png",
        "WIDTH": 1600,
        "HEIGHT": 900,
        "SET_MODE": "pre",
        "SET_HIDDEN": False,
    }
}
show("Capture image", MidasAPI("POST", "/view/CAPTURE", capture, config))
