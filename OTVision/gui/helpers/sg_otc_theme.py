# OTVision: Python module to calculate homography matrix from reference
# points and transform trajectory points from pixel into world coordinates.

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


import PySimpleGUI as sg
from pathlib import Path

# Add your new theme colors and settings
sg.LOOK_AND_FEEL_TABLE["OTC"] = {
    "BACKGROUND": "#ffffff",
    "TEXT": "#000000",
    "INPUT": "#ebebeb",
    "TEXT_INPUT": "#000000",
    "SCROLL": "#ebebeb",
    "BUTTON": ("#ffffff", "#37483e"),
    "PROGRESS": ("#ffffff", "#37483e"),
    "BORDER": 1,
    "SLIDER_DEPTH": 0,
    "PROGRESS_DEPTH": 0,
}


# Switch to use your newly created theme
OTC_THEME = sg.theme("OTC")


# Official OTC font
OTC_FONT = "Open Sans"
OTC_FONTSIZE = 12
# OTC_FONTTYPE = "bold"


# More elements in OTC style
OTC_ICON = b"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"
# OTC_ICON = str(Path(__file__).parents[1] / "helpers" / r"OTC.ico")


if __name__ == "__main__":
    # Call a popup to show what the theme looks like
    print(OTC_ICON)
    sg.SetOptions(font=(OTC_FONT, OTC_FONTSIZE))
    layout = [[sg.T("Test text")], [sg.B("Test button")]]
    window = sg.Window(
        "This is how OTC themed window looks like", layout=layout, icon=OTC_ICON
    )
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break

    window.close()