import stat
from software import Software
import shutil
import utils
import os
import subprocess

class backups(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "backups"
    
    def install(self):
        self.move_configs(os.path.expanduser("~/"))
        return "moved configs..."
    
    def uninstall(self):
        return
    
    def check_install(self):
        return False

    def check_windows(self):
        return True

    def backup_copy(self, src, dest):
        self.cmd(["copy", src, dest])

    def get_config_windows(self):
        utils.dprint("copying backups...")

        src_folder = os.path.expanduser("~")
        dst_folder = self.get_config_folder()

        subprocess.call(f"robocopy {src_folder} {dst_folder} /xd \"AppData\" /xd \"Local Settings\" /xd \"Application Data\" /s /COPY:D")