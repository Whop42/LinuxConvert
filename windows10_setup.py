import os
import platform
import sys
import json
from wallpaper import get_wallpaper
import shutil
from win32api import GetMonitorInfo, MonitorFromPoint
from ctypes import windll
import darkdetect
from winreg import ConnectRegistry, OpenKey, QueryValueEx

# TODO: features:
#   * create config folder + config
#   * get system info for config
#   - give each software a windows_config(conf_folder) function
#   - go through each software and grab configs
#   - file backups
#   - compress config


def create_config(path):
    # create config dir and json
    os.mkdir(path)
    conf_file = open(os.path.join(path, "windows-config.json"), "w")

    # get wallpaper. TODO: Test
    shutil.copyfile(get_wallpaper(), os.path.join(os.getcwd(), "background.jpg"))

    # get taskbar height + position
    monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
    monitor_area = monitor_info.get("Monitor")
    work_area = monitor_info.get("Work")
    panel_height = monitor_area[3] - work_area[3]  # TODO: test this!
    panel_position = (
        "bottom"  # TODO: find an actual way to determine where the taskbar is
    )

    # get theme color (dark/light.) TODO: Test
    if darkdetect.isDark():
        theme_color = "dark"
    else:
        theme_color = "light"

    # get accent color. TODO: Test
    registry = ConnectRegistry(None, HKEY_CURRENT_USER)
    key = OpenKey(
        registry, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Accent"
    )
    key_value = QueryValueEx(key, "AccentColorMenu")
    accent_int = key_value[0]
    accent = accent_int - 4278190080
    accent = str(hex(accent)).split("x")[1]
    accent = accent[4:6] + accent[2:4] + accent[0:2]

    config = {
        "original_os": "win10",
        "personalization": {
            "theme_mode": theme_color,
            "background_image": "background.jpg",
            "lockscreen_image": "https://betanews.com/wp-content/uploads/2015/09/Windows-10-lock-screen.jpg",  # TODO: find lockscreen image
            "panel_position": panel_position,
            "panel_height": panel_height,
            "accent_color": "#" + str(accent),
        },
    }

def get_application_list(conf_path):
    apps = []

    for application in os.listdir(conf_path)

def main():
    if not "Windows" in platform.system():
        print("Not running on windows. Stopping...")
        return

    conf_path = os.path.join(os.getcwd(), "windows10-linuxconvert")

    create_config(os.path.join(os.getcwd(), "windows10-linuxconvert"))
    get_application_list(os.path)

if __name__ == "__main__":
    main()
