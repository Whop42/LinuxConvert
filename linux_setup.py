import subprocess
import install_software
import os

config = install_software.load_files(os.getcwd())
# print(config)

# if config["original_os"] == "win10":
#     win10(config)
# elif config["original_os"] == "win11":
#     win11(config)
# elif config["original_os"] == "win7":
#     print("no windows 7 support yet :(")
# elif config["original_os"] == "macOS":
#     print("no macOS support yet :( (soon)")

def win10(conf):
    #install win10 lookalike theme

    #move/add launchers to taskbar/panel

    #set background image

    #set lockscreen image
    pass

install_software.install_basics()
install_software.copy_backups()
install_software.install_from_list()