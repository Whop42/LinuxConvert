from software import Software, betterdiscord
from utils import dprint, eprint, get_root_folder
import os
import InfoManager

class kdenlive(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "kdenlive"

        self.run_cmd = "/usr/bin/kdenlive"
        self.generic_name = "kdenlive"
        self.icon = "kdenlive"
    
    def install(self):
        print("=============================")
        print("adobe premiere does not run on linux.")
        print("LinuxConvert will install a similar alternative, Kdenlive")
        print("=============================")
        
        return self.install_package("kdenlive")

    
    def uninstall(self):
        return self.remove_package("kdenlive")
    
    def check_install(self):
        return self.query_package("kdenlive")

    def check_windows(self):
        for dirname in os.listdir(os.path.expandvars("C:\\Program Files\\Adobe")):
            if "premiere" in dirname.lower():
                return True
        if os.path.isdir(os.path.expandvars("C:\\Users\\$USERNAME\\AppData\\Roaming\\kdenlive")):
            return True
        return False
        
    def get_config_windows(self):
        # no config that can be transferred
        pass