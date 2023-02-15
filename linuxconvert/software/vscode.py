from software import Software
import os
import shutil
import utils

class vscode(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "vscode"

        self.run_cmd = "code"
        self.generic_name = "vscode"
        self.icon = "code"

        self.pkg_names = ["code", "code-marketplace"]
    
    def install(self):
        output = ""
        # install "Code - OSS" w/ package manager
        for pkg in self.pkg_names:
            output += self.install_package(pkg)
        # move configs
        self.move_configs("~/.config/Code - OSS/User")
        
        return output

    
    def uninstall(self):
        output = ""
        for pkg in self.pkg_names:
            output += str(self.remove_package(pkg))
        return output

    
    def check_install(self):
        return self.query_package(self.pkg_names[0])
    
    def check_windows(self):
        if shutil.which("code"):
            return True
        return False
    
    def get_config_windows(self):
        """
        copies windows config,
        """
        utils.copy_dir(os.path.expandvars("%APPDATA%\\Code\\User"), self.get_config_folder())
        # for dir in ["Cache", "Network", "GPUCache"]:
        #     shutil.rmtree(os.path.join(self.get_config_folder(), dir))