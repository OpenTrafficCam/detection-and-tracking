# OTVision: Python module to read and write configuration dict

# Copyright (C) 2020 OpenTrafficCam Contributors
# <https://github.com/OpenTrafficCam
# <team@opentrafficcam.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pathlib import Path
import json
from helpers.files import _get_testdatafolder


TESTDATAFOLDER = _get_testdatafolder()


CONFIG = {}

# FILETYPES
CONFIG["FILETYPES"] = {}
CONFIG["FILETYPES"]["VID"] = [
    ".mov",
    ".avi",
    ".mp4",
    ".mpg",
    ".mpeg",
    ".m4v",
    ".wmv",
    ".mkv",
]
CONFIG["FILETYPES"]["IMG"] = [".jpg", ".jpeg", ".png"]

# LAST PATHS
CONFIG["LAST PATHS"] = {}
CONFIG["LAST PATHS"]["FOLDERS"] = [TESTDATAFOLDER]
CONFIG["LAST PATHS"]["VIDEOS"] = []
CONFIG["LAST PATHS"]["DETECTIONS"] = []
CONFIG["LAST PATHS"]["TRACKS"] = []
CONFIG["LAST PATHS"]["CALIBRATIONS"] = []
CONFIG["LAST PATHS"]["REFPTS"] = []

# CONVERT
CONFIG["CONVERT"] = {}
CONFIG["CONVERT"]["OUTPUT_FILETYPE"] = ".avi"
CONFIG["CONVERT"]["FPS"] = 25.0
CONFIG["CONVERT"]["OVERWRITE"] = True

# DETECT
CONFIG["DETECT"] = {}
CONFIG["DETECT"]["YOLO"] = {}
CONFIG["DETECT"]["YOLO"]["WEIGHTS"] = "yolov5s"
CONFIG["DETECT"]["YOLO"]["CONF"] = 0.25
CONFIG["DETECT"]["YOLO"]["IOU"] = 0.45
CONFIG["DETECT"]["YOLO"]["SIZE"] = 640
CONFIG["DETECT"]["YOLO"]["CHUNKSIZE"] = 0
CONFIG["DETECT"]["YOLO"]["NORMALIZED"] = False
CONFIG["DETECT"]["YOLO"]["OVERWRTIE"] = True

# UNDISTORT
CONFIG["UNDISTORT"] = {}
CONFIG["UNDISTORT"]["OVERWRTIE"] = False

# TRANSFORM
CONFIG["TRANSFORM"] = {}
CONFIG["TRANSFORM"]["OVERWRTIE"] = False

# GUI
CONFIG["GUI"] = {}
CONFIG["GUI"]["FONT"] = "Open Sans"
CONFIG["GUI"]["FONTSIZE"] = 12
CONFIG["GUI"]["WINDOW"] = {}
CONFIG["GUI"]["WINDOW"]["LOCATION_X"] = 0
CONFIG["GUI"]["WINDOW"]["LOCATION_Y"] = 0


# TODO: #72 Overwrite default config with user config from user.conf (json file)
def _read(config_name: str = "user"):
    config_path = get_path(config_name=config_name)
    if config_path.suffix == ".otconf":
        if not config_path.is_file():
            print(f"{config_name}.otconf doesnt exist, load default.otconf instead")
            config_path = get_path(config_name="default")
            if not config_path.is_file():
                raise FileNotFoundError()
        with open(str(config_path)) as f:
            config = json.load(f)
        return config
    else:
        raise ValueError("Filetype for configuratuin has to be .otconf")


def _write(config: dict, config_name: str = "user"):
    config_path = get_path(config_name=config_name)
    if config_name == "default":
        answer = input("Sure you wanna overwrite default.otconf? [y/n]")
        if answer != "y":
            print("Configuration not saved, default.otconf not overwritten")
            return None
        print("default.otconf overwritten")
    with open(str(config_path), "w") as f:
        json.dump(config, f, indent=4)


def get_path(config_name="default"):
    config_path = Path(__file__).parents[0] / f"{config_name}.otconf"
    return config_path


if __name__ == "__main__":
    # config_dict = _read()
    # print(f"Config dict: {config_dict}")
    # _write(config_dict, config_name="user")
    pass