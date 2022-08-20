import os
import platform
import sys
import json
from wallpaper import get_wallpaper
import shutil

# features:
#   - create config folder + config
#   - get system info for config
#   - give each software a windows_config(conf_folder) function
#   - go through each software and grab configs
#   - file backups
#   - compress config

def create_config(path):
    os.mkdir(path)
    conf_file = open(os.path.join(path, "windows-config.json"), "w")

    shutil.copyfile(get_wallpaper(), os.path.join(os.getcwd(), "background.jpg"))

    config = {
        "original_os": "win10",
        "personalization": {
            "background_image": "background.jpg"
        }
    }

def main():
    if not "Windows" in platform.system():
        print("Not running on windows. Stopping...")
        return
    
    create_config(os.path.join(os.getcwd(), "windows-linuxconvert"))



if __name__ == "__main__":
    main()