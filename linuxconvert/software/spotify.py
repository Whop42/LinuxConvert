from linuxconvert.software import Software, betterdiscord
from linuxconvert.utils import dprint, eprint, get_root_folder
import os
import linuxconvert.storage.InfoManager as InfoManager

class spotify(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "spotify"

        self.run_cmd = "/usr/bin/spotify-launcher"
        self.generic_name = "spotify"
        self.icon = "spotify-launcher"
    
    def install(self):
        return self.install_package("spotify-launcher")

    
    def uninstall(self):
        return self.remove_package("spotify-launcher")
    
    def check_install(self):
        return self.query_package("spotify-launcher")

    def check_windows(self):
        if os.path.isdir(os.path.expandvars("C:\\Users\\$USERNAME\\AppData\\Roaming\\Spotify")):
            return True
        if os.path.exists(os.path.expandvars(r"C:\Users\$USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Spotify.lnk")):
            return True
        return False
        
    def get_config_windows(self):
        # no config
        pass