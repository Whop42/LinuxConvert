from linuxconvert.software import Software
from linuxconvert.utils import dprint, eprint, get_root_folder
import linuxconvert.utils
import os

class pamac(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "pamac"

        self.run_cmd = "/usr/bin/pamac"
        self.generic_name = "Add/Remove Software"
        self.icon = "pamac"

    def install(self):
        return self.install_package("pamac-all")

    
    def uninstall(self):
        return self.remove_package("pamac-all")
    
    def check_install(self):
        return self.query_package("pamac-all")

    def check_windows(self):
        return True
        
    def get_config_windows(self):
        # no config
        pass