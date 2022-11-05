import subprocess
from Install_Software import Install_Software
import os
import shutil
import sys
from utils import eprint, dprint

install_software = Install_Software()

def unzip():
    zipfile = sys.argv[1]

    if zipfile:
        dprint("unzipping config folder...")
        conf_path = zipfile.removesuffix(".zip")
        final_conf_path = os.path.join(os.getcwd(), os.path.split(conf_path)[1])
        try:
            shutil.unpack_archive(zipfile, final_conf_path)
        except OSError as e:
            eprint(str(e))
            exit()
        dprint("unzipped config folder to " + conf_path)


def main():
    config = install_software.load_files(final_conf_path)
    dprint("loaded config")
    install_software.install_from_list()

    theme(config)

    print("LinuxConvert install completed!")

def theme(config):
    if(config["original_os"] == "win10"):
        win10(config)
    elif(config["original_os"] == "win11"):
        win11(config)
    else:
        eprint("config doesn't specify OS (may be corrupt)")
        default = input("which theme would you like? (win10/win11/none")
        if default.lower() in ["win10", "win11", "none"]:
            config["original_os"] = default.lower()
        else:
            print("invalid option...")

        theme(config)

def win10(conf):
    #install win10 lookalike theme

    #move/add launchers to taskbar/panel

    #set background image

    #set lockscreen image
    pass

