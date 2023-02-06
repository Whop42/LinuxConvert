from software import Software
import os
import utils
import requests

class betterdiscord(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "betterdiscord"

        self.run_cmd = "betterdiscordctl install"
        self.generic_name = "betterdiscord"
        self.icon = "betterdiscord"
    
    def install(self):
        output = self.install_package("betterdiscordctl")
        plugins_folder = os.path.join(self.get_config_folder(), "plugins")

        # if configs don't exist, make a basic install (repos)
        if not os.path.exists(plugins_folder):
            os.makedirs(plugins_folder)
            # PluginRepo.plugin.js -> repo of plugins
            pr: requests.Response = requests.get("https://betterdiscord.app/Download?id=200")
            open(os.path.join(self.get_config_folder(), "Plugins", "PluginRepo.plugin.js")).write(pr.content)

            # ThemeRepo.plugin.js -> repo of themes
            tr: requests.Response = requests.get("https://betterdiscord.app/Download?id=201")
            open(os.path.join(self.get_config_folder(), "Plugins", "ThemeRepo.plugin.js")).write(tr.content)

        # move configs
        self.move_configs("~/.config/BetterDiscord")
        return output


    
    def uninstall(self):
        return self.remove_package("betterdiscordctl")
    
    def check_install(self):
        return self.query_package("betterdiscordctl")

    def check_windows(self):
        return os.path.isdir(os.path.expandvars("C:\\Users\\$USERNAME\\AppData\\Roaming\\BetterDiscord"))

    def get_config_windows(self):
        utils.copy_dir(os.path.expandvars("C:\\Users\\$USERNAME\\AppData\\Roaming\\BetterDiscord"), self.get_config_folder())