import subprocess
import install_software
import os

config = install_software.load_files(os.getcwd())
print(config)

if config["original_os"] == "win10":
    win10(config)
elif config["original_os"] == "win11":
    win11(config)
elif config["original_os"] == "win7":
    print("no windows 7 support yet :(")
elif config["original_os"] == "macOS":
    print("no macOS support yet :( (soon)")

def win10(conf):
    #install win10 lookalike theme

    #set taskbar location

    #add applications to taskbar

    #set background image

    #set lockscreen image
    pass