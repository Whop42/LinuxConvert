import os
import platform
import sys
import json
import shutil
from typing import Tuple
from win32api import GetMonitorInfo, MonitorFromPoint
import darkdetect
from winreg import ConnectRegistry, OpenKey, QueryValueEx, HKEY_CURRENT_USER
from utils import dprint, get_softwares, debug
import software.Software
import time
import logging
import utils

logger: logging.Logger = logging.getLogger(__name__ + "::" + __file__)

def main():
    if not "Windows" in platform.system():
        print("Not running on windows. Stopping...")
        return

    conf_path = os.path.join(os.getcwd(), "windows10-linuxconvert")

    create_config(conf_path)

    for s in get_softwares():
        get_config_from_software(s)
    
    dprint("zipping...")
    zipfile = "windows10-linuxconvert-" + time.strftime("%m-%d-%H-%M-%S")
    shutil.make_archive(zipfile, "zip", conf_path, conf_path)

    shutil.rmtree(conf_path)
        
    dprint(conf_path + " removed.")
    print(f"File created: {os.getcwd() + zipfile}")
    print("Complete!")

def create_config(path: str):
    # tries to remove the windows10-linuxconvert folder (if debug)
    # it doesn't matter if it isn't there
    try:
        if utils.debug:
            shutil.rmtree(os.path.join(os.getcwd(), "windows10-linuxconvert"))
    except:
        pass

    # create config dir and json
    os.mkdir(path)
    conf_file = open(os.path.join(path, "windows-config.json"), "w")
    dprint("made conf folder and file")

    panel_position, panel_height = get_panel_info()

    config = {
        "original_os": "win10",
        "personalization": {
            "theme_mode": get_theme_mode(),
            "background_image": get_background_image(),
            "lockscreen_image": get_lockscreen_image(),
            "panel_position": panel_position,
            "panel_height": panel_height,
            "accent_color": get_accent_color(),
        },
        # TODO: taskbar items
    }

    conf_file.write(json.dumps(config))
    conf_file.close()
    dprint("wrote config to conf_file")
    os.mkdir(os.path.join(path, "applications"))

def get_theme_mode() -> str:
    # get theme color (dark/light)
    if darkdetect.isDark():
        return "dark"
    else:
        return "light"

def get_accent_color() -> str:
    """
    returns accent color as a hex string starting with #
    ex. #2e2e4f
    """
    # get accent color
    registry = ConnectRegistry(None, HKEY_CURRENT_USER)
    key = OpenKey(
        registry, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Accent"
    )
    key_value = QueryValueEx(key, "AccentColorMenu")
    accent_int = key_value[0]
    accent = accent_int - 4278190080
    accent = str(hex(accent)).split("x")[1]
    accent = accent[4:6] + accent[2:4] + accent[0:2]
    return f"#{accent}"

def get_background_image() -> str:
    # get wallpaper. TODO: Doesn't actually work yet
    # registry = ConnectRegistry(None, HKEY_CURRENT_USER)
    # key = OpenKey(
    #     registry, r"\\Control Panel\\Desktop"
    # )
    # return QueryValueEx(key, "WallPaper")
    return "background.jpg"

def get_panel_info() -> Tuple[str, int]:
    # get taskbar height + position
    monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
    monitor_area = monitor_info.get("Monitor")
    work_area = monitor_info.get("Work")
    panel_height: int = monitor_area[3] - work_area[3]
    dprint("panel height: " + str(panel_height))

    panel_position: str = "bottom" # TODO: find a way to get this

    return (panel_position, panel_height)

def get_lockscreen_image() -> str:
    # TODO: find how to do this (is it possible??)
    return "lockscreen.jpg"

def get_config_from_software(software: software.Software.Software):
    if software.check_windows():
        software.create_config()
        software.get_config_windows()
        dprint("Got config from " + software.name)
    else:
        dprint(software.name + " not installed.")

if __name__ == "__main__":
    main()