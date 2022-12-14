import os
import sys
import json
from utils import dprint, eprint, get_root_folder
from software import Software
import shutil
import InfoManager

class Install_Software:
    def __init__(self):
        self.applications = []
        self.config = {}
        self.im = InfoManager.InfoManager()

    def load_files(self, dir) -> dict:
        dprint("loading files from " + str(dir))
        for filename in os.listdir(dir):
            for application_folder in os.listdir(os.path.join(dir, "applications")): # for each application folder
                for application_file in os.listdir(os.path.join(dir, "applications", application_folder)): # for each file in the application folder
                    if ".json" not in application_file:
                        continue # ignore if not .json file

                    try:
                        f = open(os.path.join(dir, "applications", application_folder, application_file))
                        json_str = json.loads(f.read())

                        # applications list format: folder name, real name
                        self.applications.append([application_folder, json_str["name"]])

                        f.close()
                    except:
                        eprint(application_file + " is not a valid application configuration")
            dprint("applications list: " + str(self.applications))

            for f in os.listdir(dir):
                # find the config file and dump it into self.config
                if "-config.json" in f: 
                    config_file = open(os.path.join(dir, f))
                    self.config = json.loads(config_file.read())
                    config_file.close()
                    dprint("dumped -config.json file")
                    self.im.config = self.config
                    return
            eprint("couldn't find -config.json file")
            exit()

    def install(self, name):
        for software in self.im.softwares:
            if software.name == name:
                if software.check_install():
                    dprint(software.name + " is already installed. Skipping...")
                    return
                
                print("Installing " + software.name + "...")
                output = software.install()

                software.create_desktop(os.path.expanduser(os.path.join("~/Desktop", str(software.name) + ".desktop")))

                self.im.installed_softwares.append(software.name)
                print(name + " installed.")

            
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