from software import Software
import os
import shutil

class vscode(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "vscode"

        self.run_cmd = "code"
        self.generic_name = "screenshot"
        self.icon = "screengrab"
    
    def install(self):
        # install "Code - OSS" w/ package manager
        output = [self.install_package("code"), self.install_package("code-marketplace")]
        # move configs
        self.move_configs("~/.config/Code - OSS")
        
        return output

    
    def uninstall(self):
        return self.remove_package("code")
    
    def check_install(self):
        return self.query_package("code")
    
    def check_windows(self):
        if shutil.which("code"):
            return True
        return False
    
    def get_config_windows(self):
        pass