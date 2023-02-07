from software import Software, betterdiscord
from utils import dprint, eprint
import utils
import os
import InfoManager

class firefox(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "firefox"

        self.run_cmd = "/usr/bin/firefox"
        self.generic_name = "firefox"
        self.icon = "firefox"
    
    def install(self):
        return self.install_package("firefox")

    
    def uninstall(self):
        return self.remove_package("firefox")
    
    def check_install(self):
        return self.query_package("firefox")

    def check_windows(self):
        if os.path.isdir(os.path.expandvars("C:\\Users\\$USERNAME\\AppData\\Local\\Discord")):
            return True
        return False
        
    def find_profile(self, path: str):
        """
        finds the firefox profile in a dir
        """

        for d in os.listdir(path):
            if len(os.listdir(os.path.join(path, d))) > 1:
                return os.path.join(path, d)
        
        return False
    
    def get_config_windows(self):
        profiles_path = os.path.expandvars("C:\\Users\\$USERNAME\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles")

        utils.copy_dir(self.find_profile(profiles_path), self.get_config_folder())