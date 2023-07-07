from linuxconvert.software import Software
from linuxconvert.utils import dprint, eprint, get_root_folder
import os
import linuxconvert.storage.InfoManager as InfoManager

class edge(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "edge"

        self.run_cmd = "/usr/bin/microsoft-edge-stable"
        self.generic_name = "edge"
        self.icon = "microsoft-edge"
    
    def install(self):
        install_edge = True
        if "firefox" not in InfoManager.InfoManager.applications:
            if self.recommend(
                "installing firefox (a browser that respects your privacy) instead",
                "collects your data"):
                install_edge = False
                InfoManager.InfoManager.applications.append("firefox")     

        if install_edge:
            return self.install_package("microsoft-edge-stable-bin")

    
    def uninstall(self):
        return self.remove_package("microsoft-edge-stable-bin")
    
    def check_install(self):
        return self.query_package("microsoft-edge-stable-bin")

    def check_windows(self):
        # installed by default
        return True
        
    def get_config_windows(self):
        # no config
        pass