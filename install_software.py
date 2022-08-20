import os
import sys
import json
from software import neofetch, flameshot
import utils
import shutil

debug = True

applications = []
config = {}
softwares = []

#initialize software
softwares.append(neofetch.neofetch())
softwares.append(flameshot.flameshot())

def load_files(path):
    for filename in os.listdir(path):
        #check if it's a linuxconvert folder
        if "-linuxconvert" in filename:
            #get applications + info
            for application_folder in os.listdir(os.path.join(path, filename, "applications")):
                for application_file in os.listdir(os.path.join(path, filename, "applications", application_folder)):
                    try:
                        f = open(os.path.join(path, filename, "applications", application_folder, application_file))
                        json_str = json.loads(f.read())
                        applications.append([application_folder, json_str["name"], json_str["original_path"]])
                        f.close()
                    except:
                        print(application_file + " is not a valid application configuration...")
            
            for f in os.listdir(os.path.join(path, filename)):
                if "-config.json" in f:
                    config_file = open(os.path.join(path, filename, f))
                    config = json.loads(config_file.read())
                    config_file.close()
    # print(applications)
    # print(config)
    return config

def copy_backups():
    """
    copies *all* files in *-linuxconvert/file_backups to ~

    WARNING: not tested
    """

    for f in utils.locate_backup_folder():
        shutil.copy(f, os.path.join("~", f))


def install(name):
    for software in softwares:
        if software.name == name:
            if software.check_install():
                print(software.name + " is already installed. Skipping...")
                return
            print("Installing " + software.name + "...")
            output = software.install()
            software.create_desktop(os.getcwd() + str(software.name) + ".desktop")
            if debug:
                print(output)
            print(name + " installed.")
        
def install_from_list():
    for application in applications:
        install(application[1])

def install_basics():
    print("Installing basic applications...")

    basics = [
        "neofetch", # because you can't show off linux without neofetch
        "flameshot" # screenshot utility
    ]

    for software in basics:
        install(software)