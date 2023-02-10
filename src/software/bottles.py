from software import Software
from utils import dprint, eprint, get_root_folder
import utils
import os
import InfoManager
import requests

class bottles(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "bottles"

        self.run_cmd = "/usr/bin/bottles"
        self.generic_name = "bottles"
        self.icon = "bottles"

    def install(self):
        return self.install_package("bottles")

    
    def uninstall(self):
        return self.remove_package("bottles")
    
    def check_install(self):
        return self.query_package("bottles")

    def check_windows(self):
        return True
        
    def get_config_windows(self):
        # no config
        pass