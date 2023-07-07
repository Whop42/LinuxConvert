from linuxconvert.software import Software, betterdiscord
from linuxconvert.utils import dprint, eprint, get_root_folder
import os
import linuxconvert.storage.InfoManager as InfoManager

class zoom(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "zoom"

        self.run_cmd = "/usr/bin/zoom"
        self.generic_name = "zoom"
        self.icon = "application-x-zoom"
    
    def install(self):
        return self.install_package("zoom")

    
    def uninstall(self):
        return self.remove_package("zoom")
    
    def check_install(self):
        return self.query_package("zoom")

    def check_windows(self):
        if os.path.isdir(os.path.expandvars("C:\\Program Files\\Zoom")):
            return True
        return False
        
    def get_config_windows(self):
        # no config
        pass