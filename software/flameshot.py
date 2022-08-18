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
        return self.install_package("flameshot")

    
    def uninstall(self):
        return self.remove_package("flameshot")
    
    def check_install(self):
        return self.query_package("flameshot")