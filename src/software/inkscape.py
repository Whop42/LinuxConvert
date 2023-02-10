from software import Software, betterdiscord
from utils import dprint, eprint, get_root_folder
import os
import InfoManager

class inkscape(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "inkscape"

        self.run_cmd = "/usr/bin/inkscape"
        self.generic_name = "inkscape"
        self.icon = "inkscape"
    
    def install(self):
        print("=============================")
        print("adobe illustrator does not run on linux.")
        print("LinuxConvert will install a similar alternative, InkScape")
        print("=============================")
        
        return self.install_package("inkscape")

    
    def uninstall(self):
        return self.remove_package("inkscape")
    
    def check_install(self):
        return self.query_package("inkscape")

    def check_windows(self):
        if os.path.isdir(os.path.expandvars("C:\\Users\\$USERNAME\\AppData\\Roaming\\Adobe\\Illustrator")): #TODO: illustrator path!
            return True
        return False
        
    def get_config_windows(self):
        # no config
        pass