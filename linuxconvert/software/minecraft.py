from software import Software
from utils import dprint, eprint, get_root_folder
import utils
import os
import InfoManager
import requests

class minecraft(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "minecraft"

        self.run_cmd = "/usr/bin/minecraft-launcher"
        self.generic_name = "minecraft"
        self.icon = "minecraft"

    def install(self):
        output = self.install_package("minecraft-launcher")

        self.move_configs(os.path.expanduser("~/.minecraft"))

        return output

    
    def uninstall(self):
        return self.remove_package("minecraft-launcher")
    
    def check_install(self):
        return self.query_package("minecraft-launcher")

    def check_windows(self):
        if os.path.isdir(os.path.expandvars(r"C:\Users\$USERNAME\AppData\Roaming\.minecraft")):
            return True
        return False
        
    def get_config_windows(self):
        utils.copy_dir(os.path.expandvars(r"C:\Users\$USERNAME\AppData\Roaming\.minecraft"), self.get_config_folder())