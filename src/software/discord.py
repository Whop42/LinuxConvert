from software import Software, betterdiscord
from utils import dprint, eprint, get_root_folder
import os
import InfoManager

class discord(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "discord"

        self.run_cmd = "/usr/bin/discord"
        self.generic_name = "discord"
        self.icon = "discord"
    
    def install(self):
        if "betterdiscord" not in InfoManager.InfoManager.applications:
            if self.recommend(
                "installing betterdiscord (a utility to customize discord with plugins and themes)",
                "isn't very customizable"):
                # TODO: install betterdiscord
                InfoManager.InfoManager.applications.append("betterdiscord")
                os.mkdir(os.path.join(get_root_folder(), "betterdiscord"))
                pass

        return self.install_package("discord")

    
    def uninstall(self):
        return self.remove_package("discord")
    
    def check_install(self):
        return self.query_package("discord")

    def check_windows(self):
        if os.path.isdir(os.path.expandvars("C:\\Users\\$USERNAME\\AppData\\Local\\Discord")):
            return True
        return False
        
    def get_config_windows(self):
        # no config
        pass