from linuxconvert.software import Software
from linuxconvert.utils import dprint, eprint, get_root_folder
import linuxconvert.utils
import os
import linuxconvert.storage.InfoManager as InfoManager
import requests

class libreoffice(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "libreoffice"

        self.run_cmd = "/usr/bin/libreoffice"
        self.generic_name = "office"
        self.icon = "applications-office"
    
    """
    installs libreoffice by...
        - installing packages
        - moving the configs
        - downloading the spellcheck dictionary
        - installing the spellcheck dictionary
    """
    def install(self):
        self.install_packages(["libreoffice-fresh",
                                "ttf-ms-fonts", # default microsoft fonts
                                "ttf-carlito" # calibri
                                ])
        
        # find where default configs are stored
        cfg_path = os.path.join(os.getcwd(), "linuxconvert", "media", "light.xcu") # if light mode
        if InfoManager.InfoManager.config["personalization"]["theme_mode"] == "dark":
            cfg_path = os.path.join(os.getcwd(), "linuxconvert", "media", "dark.xcu") # if dark mode
        
        # make sure the config folder exists
        if not os.path.exists(os.path.expanduser("~/.config/libreoffice/4/user/")):
            os.makedirs(os.path.expanduser("~/.config/libreoffice/4/user/"))
        
        # copy config
        utils.copy_file(cfg_path, os.path.expanduser("~/.config/libreoffice/4/user/registrymodifications.xcu"))

        # download the dictionary
        dict_url = "https://extensions.libreoffice.org/assets/downloads/41/1675249081/dict-en-20230201_lo.oxt"
        with open("dict.oxt", "wb") as f:
            f.write(requests.get(dict_url).content)

        # install dictionary by running libreoffice w/ it as an arg
        os.system("libreoffice -o dict.oxt")
        
        # libreoffice opens a window from the above line, it must be closed to properly install
        dprint("close the libreoffice window to continue...")

        # remove the downloaded dict (it's already copied to libreoffice's files)
        os.remove("dict.oxt")

    
    def uninstall(self):
        return self.remove_package("libreoffice-fresh")
    
    def check_install(self):
        return self.query_package("libreoffice-fresh")

    def check_windows(self):
        # installed by default
        return True
        
    def get_config_windows(self):
        # no config in windows
        pass