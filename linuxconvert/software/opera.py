# C:\Program Files\Opera
from software import Software, betterdiscord
from utils import dprint, eprint
import utils
import os
import InfoManager

class opera(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "opera"

        self.run_cmd = "/usr/bin/opera"
        self.generic_name = "opera"
        self.icon = "opera"
    
    def install(self):
        return self.install_packages(["opera", "opera-ffmpeg-codecs"])
    
    def uninstall(self):
        return self.remove_package("opera")
    
    def check_install(self):
        return False

    def check_windows(self):
        if os.path.isdir(os.path.expandvars("C:\\Program Files\\Opera")):
            return True
        if os.path.isdir(os.path.expandvars("C:\\Users\\$USERNAME\\AppData\\Local\\Programs\\Opera GX")):
            return True
        return False
    
    def get_config_windows(self):
        # no useful config
        pass