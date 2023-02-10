from software import Software, betterdiscord
from utils import dprint, eprint, get_root_folder
import os
import InfoManager

class steam(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "steam"

        self.run_cmd = "/usr/bin/steam"
        self.generic_name = "steam"
        self.icon = "steam"
    
    def install(self):
        return self.install_package("steam")

    
    def uninstall(self):
        return self.remove_package("steam")
    
    def check_install(self):
        return self.query_package("steam")

    def check_windows(self):
        if os.path.isdir(os.path.expandvars("C:\\Program Files (x86)\\Steam")):
            return True
        return False
        
    def get_config_windows(self):
        # no config
        pass