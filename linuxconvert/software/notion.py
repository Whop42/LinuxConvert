from software import Software, betterdiscord
from utils import dprint, eprint, get_root_folder
import os
import InfoManager

class notion(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "notion"

        self.run_cmd = "/usr/bin/notion-app"
        self.generic_name = "notion"
        self.icon = "notion-app"
    
    def install(self):
        return self.install_package("notion-app")

    
    def uninstall(self):
        return self.remove_package("notion-app")
    
    def check_install(self):
        return self.query_package("notion-app")

    def check_windows(self):
        if os.path.isdir(os.path.expandvars("C:\\Users\\$USERNAME\\AppData\\Local\\Programs\\Notion")):
            return True
        return False
        
    def get_config_windows(self):
        # no config
        pass