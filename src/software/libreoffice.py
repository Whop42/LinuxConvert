from software import Software
from utils import dprint, eprint, get_root_folder
import utils
import os
import InfoManager

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
        cfg_path = os.path.join(os.getcwd(), "src", "media", "light.xcu")
        if InfoManager.InfoManager.config["personalization"]["theme_mode"] == "dark":
            cfg_path = os.path.join(os.getcwd(), "src", "media", "dark.xcu")
        
        if not os.path.exists(os.path.expanduser("~/.config/libreoffice/4/user/")):
            os.makedirs(os.path.expanduser("~/.config/libreoffice/4/user/"))
        utils.copy_file(cfg_path, os.path.expanduser("~/.config/libreoffice/4/user/registrymodifications.xcu"))

    
    def uninstall(self):
        return self.remove_package("libreoffice-fresh")
    
    def check_install(self):
        return self.query_package("libreoffice-fresh")

    def check_windows(self):
        # installed by default
        return True
        
    def get_config_windows(self):
        # no config
        pass