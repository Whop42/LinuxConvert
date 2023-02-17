from software import Software, betterdiscord
from utils import dprint, eprint
import utils
import os
import InfoManager

class vivaldi(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "vivaldi"

        self.run_cmd = "/usr/bin/vivaldi-stable"
        self.generic_name = "vivaldi"
        self.icon = "vivaldi"
    
    def install(self):
        out = self.install_packages(["vivaldi", "vivaldi-ffmpeg-codecs"])
        self.move_configs(os.path.expanduser("~/.config/vivaldi"))
        return out
    
    def uninstall(self):
        return self.remove_package("vivaldi")
    
    def check_install(self):
        return False

    def check_windows(self):
        if os.path.isdir(os.path.expandvars("C:\\Users\\$USERNAME\\AppData\\Local\\Vivaldi\\User Data")):
            return True
        return False
    
    def get_config_windows(self):
        # profiles_path = os.path.expandvars("C:\\Users\\$USERNAME\\AppData\\Local\\Vivaldi\\User Data")

        # utils.copy_dir(profiles_path, self.get_config_folder())
        pass