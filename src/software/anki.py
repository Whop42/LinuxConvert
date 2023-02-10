from software import Software
from utils import dprint, eprint, get_root_folder
import utils
import os
import InfoManager

class anki(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "anki"

        self.run_cmd = "/usr/bin/anki"
        self.generic_name = "anki"
        self.icon = "anki"
    
    def install(self):
        output = self.install_package("anki-bin")
        self.move_configs(r"~/.local/share/Anki2")
        return output


    
    def uninstall(self):
        return self.remove_package("anki-bin")
    
    def check_install(self):
        return self.query_package("anki-bin")

    def check_windows(self):
        if os.path.isdir(os.path.expandvars(r"C:\Program Files\Anki")):
            return True
        return False
        
    def get_config_windows(self):
        utils.copy_dir(os.path.expandvars(r"C:\Users\$USERNAME\AppData\Roaming\Anki2"), self.get_config_folder())