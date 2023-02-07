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

    def backup_copy(self, src, dest):
        self.cmd(["copy", src, dest])
        # if not os.access(src, os.W_OK):
        #     os.chmod(src, stat.S_IWUSR)
        # try:
        #     shutil.copy2(src, dest, )
        # except shutil.Error as e:
        #     utils.eprint(f"could not copy {src} to {dest}")

    def get_config_windows(self):
        utils.dprint("copying backups...")

        # TODO: make it not include AppData

        src_folder = os.path.expanduser("~")
        dst_folder = self.get_config_folder()

        subprocess.call(f"robocopy {src_folder} {dst_folder} /xd \"AppData\" /s /COPY:D")

        # for item in os.listdir(src_folder):
        #     s = os.path.join(src_folder, item)
        #     d = os.path.join(dst_folder, item)
        #     if os.path.isdir(s) and "AppData" not in s:
        #         try:
        #             shutil.copytree(s, d, False, None)
        #         except PermissionError:
        #             utils.eprint(f"PermissionError: Skipping {s}")
        #         except OSError:
        #             utils.eprint(f"OSError: Skipping {s}")
        #     else:
        #         try:
        #             shutil.copy2(s, d)
        #         except PermissionError:
        #             utils.eprint(f"PermissionError: Skipping {s}")
        #         except OSError:
        #             utils.eprint(f"OSError: Skipping {s}")

        # for d in os.listdir(os.path.expanduser("~")):
        #     if not "AppData" in d:
        #         self.cmd(["cp", "\"" + os.path.join(os.path.expanduser("~"), d) + "\"", "\"" + os.path.join(self.get_config_folder(), d) + "\""])

        # if utils.copy_dir(os.path.expanduser("~")):
        #     utils.dprint("copied backups")
        # else:
        #     utils.eprint("failed to copy backups") 