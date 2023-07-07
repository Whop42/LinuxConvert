from linuxconvert.software import Software
import os
import linuxconvert.utils
import requests

class chromium(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "chromium"

        self.run_cmd = "chromium"
        self.generic_name = "chromium"
        self.icon = "chromium"
    
    def install(self):
        output = self.install_package("chromium")
        return output


    
    def uninstall(self):
        return self.remove_package("chromium")
    
    def check_install(self):
        return self.query_package("chromium")

    def check_windows(self):
        return False

    def get_config_windows(self):
        pass