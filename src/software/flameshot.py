from software import Software
import os

class flameshot(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "flameshot"

        self.run_cmd = "flameshot gui"
        self.generic_name = "screenshot"
        self.icon = "screengrab"
    
    def install(self):
        output = self.install_package("flameshot")
        self.cmd(["flameshot", "-a true"]) # autostart

    
    def uninstall(self):
        return self.remove_package("flameshot")
    
    def check_install(self):
        return self.query_package("flameshot")

    def check_windows(self):
        # screenshot util installed by default in windows
        return True

    def get_config_windows(self):
        # screenshot util installed by default in windows
        pass