from software import Software
from utils import dprint, eprint, get_root_folder
import utils
import os
import InfoManager
import requests

class libreoffice(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "libreoffice"

        self.run_cmd = "/usr/bin/libreoffice"
        self.generic_name = "office"
        self.icon = "applications-office"
    
    def install(self):
        self.install_packages(["libreoffice-fresh",
                                "ttf-ms-fonts",
                                "ttf-carlito"
                                ])
        
        # move config to config folder
        cfg_path = os.path.join(os.getcwd(), "linuxconvert", "media", "light.xcu")
        if InfoManager.InfoManager.config["personalization"]["theme_mode"] == "dark":
            cfg_path = os.path.join(os.getcwd(), "linuxconvert", "media", "dark.xcu")
        
        if not os.path.exists(os.path.expanduser("~/.config/libreoffice/4/user/")):
            os.makedirs(os.path.expanduser("~/.config/libreoffice/4/user/"))
        utils.copy_file(cfg_path, os.path.expanduser("~/.config/libreoffice/4/user/registrymodifications.xcu"))

        dict_url = "https://extensions.libreoffice.org/assets/downloads/41/1675249081/dict-en-20230201_lo.oxt"
        f = open("dict.oxt", "wb")
        f.write(requests.get(dict_url).content)
        f.close()
        os.system("libreoffice -o dict.oxt")
        print("============================")
        print("NOTE: close the libreoffice window after installing the dictionary")
        print("============================")
        os.remove("dict.oxt")

    
    def uninstall(self):
        return self.remove_package("libreoffice-fresh")
    
    def check_install(self):
        return self.query_package("libreoffice-fresh")

    def check_windows(self):
        # installed by default
        return True
        
    def get_config_windows(self):
        # no configlibreoff
        pass