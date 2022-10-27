import os
import sys
import json
from utils import dprint, eprint, get_softwares, get_root_folder
import shutil

class Install_Software:
    def __init__(self):
        self.applications = []
        self.config = {}
        self.softwares = get_softwares()

    def load_files(self, dir) -> dict:
        dprint("loading files from " + str(dir))
        for filename in os.listdir(dir):
            for application_folder in os.listdir(os.path.join(dir, "applications")):
                for application_file in os.listdir(os.path.join(dir, "applications", application_folder)):
                    try:
                        f = open(os.path.join(dir, "applications", application_folder, application_file))
                        json_str = json.loads(f.read())
                        self.applications.append([application_folder, json_str["name"]])
                        f.close()
                    except:
                        eprint(application_file + " is not a valid application configuration")
            dprint(str(self.applications))
            for f in os.listdir(dir):
                if "-config.json" in f:
                    config_file = open(os.path.join(dir, f))
                    self.config = json.loads(config_file.read())
                    config_file.close()
                    dprint("created config file")
            return self.config

        eprint("filename not in directory")
        exit()

    def install(self, name):
        for software in self.softwares:
            if software.name == name:
                if software.check_install():
                    dprint(software.name + " is already installed. Skipping...")
                    return
                print("Installing " + software.name + "...")
                output = software.install()
                software.create_desktop(os.getcwd() + str(software.name) + ".desktop")
                dprint(output)
                print(name + " installed.")
            else:
                if name not in [self.applications[i][1] for i in self.applications]:
                    dprint(name  +  " isn't in applications...")
            
    def install_from_list(self):
        for application in self.applications:
            self.install(application[1])

    # def install_basics():
    #     print("Installing basic applications...")

    #     basics = [
    #         "neofetch", # because you can't show off linux without neofetch
    #         "flameshot" # screenshot utility
    #     ]

    #     for software in basics:
    #         install(software)