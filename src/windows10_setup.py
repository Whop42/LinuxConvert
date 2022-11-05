import os
import platform
import sys
import json
import shutil
from win32api import GetMonitorInfo, MonitorFromPoint
import darkdetect
from winreg import ConnectRegistry, OpenKey, QueryValueEx, HKEY_CURRENT_USER
from utils import dprint, get_softwares, debug
import software.Software as sw
import time

# TODO: features:
#   * create config folder + config
#   * get system info for config
#   * go through each software and grab configs
#   * compress config

debug = True

def create_config(path):
    try:
        if debug: shutil.rmtree(os.path.join(os.getcwd(), "windows10-linuxconvert"))
    except:
        pass
    # create config dir and json
    os.mkdir(path)
    conf_file = open(os.path.join(path, "windows-config.json"), "w")
    dprint("made conf folder and file")

    # get wallpaper. TODO: Test
    # registry = ConnectRegistry(None, HKEY_CURRENT_USER)
    # key = OpenKey(
    #     registry, r"\\Control Panel\\Desktop"
    # )
    # wallpaper_path = QueryValueEx(key, "WallPaper")
    # print(wallpaper_path)
    
    # get taskbar height + position
    monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
    monitor_area = monitor_info.get("Monitor")
    work_area = monitor_info.get("Work")
    panel_height = monitor_area[3] - work_area[3]
    dprint("panel height: " + str(panel_height))
    panel_position = (
        "bottom"  # TODO: find an actual way to determine where the taskbar is
    )

    # get theme color (dark/light)
    if darkdetect.isDark():
        theme_color = "dark"
    else:
        theme_color = "light"
    dprint("got color scheme: " + theme_color)

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
    dprint("got accent: #" + str(accent))

    config = {
        "original_os": "win10",
        "personalization": {
            "theme_mode": theme_color,
            "background_image": "background.jpg",
            "lockscreen_image": "https://betanews.com/wp-content/uploads/2015/09/Windows-10-lock-screen.jpg",
            "panel_position": panel_position,
            "panel_height": panel_height,
            "accent_color": "#" + str(accent),
        },
        # TODO: taskbar items
    }

    conf_file.write(json.dumps(config))
    conf_file.close()
    dprint("wrote config to conf_file")
    os.mkdir(os.path.join(path, "applications"))

def get_config_from_software(software):

    if software.check_windows():
        software.create_config()
        software.get_config_windows()
        dprint("Got config from " + software.name)
    else:
        dprint(software.name + " not installed.")

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



if __name__ == "__main__":
    main()
