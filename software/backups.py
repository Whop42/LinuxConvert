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
        return "moved configs..."
    
    def uninstall(self):
        return
    
    def check_install(self):
        if "Documents" in os.listdir(os.path.expanduser("~")):
            return True
        return False

    def check_windows(self):
        return True

    def get_config_windows(self):

        dirs = ["~/Pictures", "~/Downloads", "~/Videos", "~/Documents"]

        utils.dprint("copying backups...")
        if utils.copy_dirs(dirs, self.get_config_folder()):
            utils.dprint("copied backups")
        else:
            utils.eprint("failed to copy backups")