import os
import sys
import json
from software import neofetch

applications = []
config = {}
softwares = []

#initialize software
softwares.append(neofetch.neofetch())

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

def install(name):
    for software in softwares:
        if software.name == applications[0]:
            software.install()
        

load_files(os.getcwd())