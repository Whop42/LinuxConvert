from linuxconvert.software import Software, betterdiscord
from linuxconvert.utils import dprint, eprint, get_root_folder
import os
import linuxconvert.storage.InfoManager as InfoManager

class teams(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "teams"

        self.run_cmd = "/usr/bin/teams"
        self.generic_name = "teams"
        self.icon = "teams"
    
    def install(self):
        return self.install_package("teams")

    
    def uninstall(self):
        return self.remove_package("teams")
    
    def check_install(self):
        return self.query_package("teams")

    def check_windows(self):
        if os.path.isdir(os.path.expandvars("C:\\Users\\$USERNAME\\AppData\\Local\\Microsoft\\Teams")):
            return True
        return False
        
    def get_config_windows(self):
        # no config
        pass