import os
import sys
import json
from utils import dprint, eprint, get_softwares
import shutil

class Install_Software:
    def __init__(self):
        self.applications = []
        self.config = {}
        self.softwares = get_softwares()

    def load_files(self, directory):
        path = os.getcwd()
        for filename in os.listdir(os.getcwd()):
            if filename == directory:
                #get applications + info
                for application_folder in os.listdir(os.path.join(path, filename, "applications")):
                    for application_file in os.listdir(os.path.join(path, filename, "applications", application_folder)):
                        try:
                            f = open(os.path.join(path, filename, "applications", application_folder, application_file))
                            json_str = json.loads(f.read())
                            self.applications.append([application_folder, json_str["name"], json_str["original_path"]])
                            f.close()
                        except:
                            eprint(application_file + " is not a valid application configuration")
                dprint(str(self.applications))
                for f in os.listdir(os.path.join(path, filename)):
                    if "-config.json" in f:
                        config_file = open(os.path.join(path, filename, f))
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
                if name not in [applications[i][1] for i in applications]:
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