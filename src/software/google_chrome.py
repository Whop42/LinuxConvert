from software import Software
from utils import dprint, eprint, get_root_folder
import os
import InfoManager

class google_chrome(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "chrome"

        self.run_cmd = "/usr/bin/google-chrome-stable"
        self.generic_name = "chrome"
        self.icon = "google-chrome"
    
    def install(self):
        install_chrome = True
        if "chromium" not in InfoManager.InfoManager.applications:
            if self.recommend(
                "installing chromium (an open-source version of google chrome that respects your privacy) instead",
                "collects your data"):
                install_chrome = False
                InfoManager.InfoManager.applications.append("chromium")
                

        if install_chrome:
            return self.install_package("google-chrome-stable")

    
    def uninstall(self):
        return self.remove_package("google-chrome-stable")
    
    def check_install(self):
        return self.query_package("google-chrome-stable")

    def check_windows(self):
        if os.path.isdir(os.path.expandvars(r"C:\Program Files\Google\Chrome")):
            return True
        return False
        
    def get_config_windows(self):
        # no config
        pass