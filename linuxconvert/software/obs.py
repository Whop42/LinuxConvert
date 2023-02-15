from software import Software, betterdiscord
from utils import dprint, eprint, get_root_folder
import os
import InfoManager

class obs(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "obs"

        self.run_cmd = "/usr/bin/obs"
        self.generic_name = "obs"
        self.icon = "com.obsproject.Studio"
    
    def install(self):
        return self.install_package("obs-studio")

    
    def uninstall(self):
        return self.remove_package("obs-studio")
    
    def check_install(self):
        return self.query_package("obs-studio")

    def check_windows(self):
        if os.path.isdir(os.path.expandvars("C:\\Program Files\\obs-studio")):
            return True
        return False
        
    def get_config_windows(self):
        # no config
        pass