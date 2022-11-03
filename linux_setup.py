import subprocess
from Install_Software import Install_Software
import os
import shutil
import sys
from utils import eprint, dprint

install_software = Install_Software()

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

    try:
        shutil.move(conf_path, final_conf_path)
    except OSError as e:
        eprint(str(e))
        exit()
    dprint("moved config folder to " + final_conf_path)


    config = install_software.load_files(final_conf_path)
    dprint("loaded config")
    install_software.install_from_list()
    print("LinuxConvert install completed!")


# print(config)

# if config["original_os"] == "win10":
#     win10(config)
# elif config["original_os"] == "win11":
#     win11(config)
# elif config["original_os"] == "win7":
#     print("no windows 7 support yet :(")

def win10(conf):
    #install win10 lookalike theme

    #move/add launchers to taskbar/panel

    #set background image

    #set lockscreen image
    pass

