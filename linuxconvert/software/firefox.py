from linuxconvert.software import Software, betterdiscord
from linuxconvert.utils import dprint, eprint
import linuxconvert.utils
import os
import linuxconvert.storage.InfoManager as InfoManager

class firefox(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "firefox"

        self.run_cmd = "/usr/bin/firefox"
        self.generic_name = "firefox"
        self.icon = "firefox"

    def find_profile(self, path: str):
        """
        finds the firefox profile in a dir
        """

        for d in os.listdir(path):
            if os.path.isdir(d):
                print(d)
                if len(os.listdir(os.path.join(path, d))) > 1:
                    dprint("found firefox profile dir: " + d)
                    return os.path.join(path, d)
        
        return False
    
    def install(self):
        if not self.query_package("firefox"):
            self.install_package("firefox")
        
        if os.path.exists(self.get_config_folder()):
            path = os.path.expanduser("~/.mozilla/firefox")

            dprint("installing firefox profile to " + path)

            self.move_configs(path)

    
    def uninstall(self):
        return self.remove_package("firefox")
    
    def check_install(self):
        return False

    def check_windows(self):
        if os.path.isdir(os.path.expandvars("C:\\Users\\$USERNAME\\AppData\\Local\\Discord")):
            return True
        return False
    
    def get_config_windows(self):
        profiles_path = os.path.expandvars("C:\\Users\\$USERNAME\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles")

        if self.find_profile(profiles_path):
            utils.copy_dir(self.find_profile(profiles_path), self.get_config_folder())