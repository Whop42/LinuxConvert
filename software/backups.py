from software import Software
import shutil
import utils
import os

class backups(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "backups"
    
    def install(self):
        self.move_configs("~/")
    
    def uninstall(self):
        return
    
    def check_install(self):
        if "Documents" in os.listdir("~/"):
            return True
        return False

    def check_windows(self):
        return True

    def get_config_windows(self):
        if utils.move_dirs_to_dir(["Documents", "Pictures", "Downloads"], "~/"):
            utils.dprint("moved backups")
        else:
            utils.eprint("failed to move backups")