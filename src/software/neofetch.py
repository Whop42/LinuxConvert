from software import Software

class neofetch(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "neofetch"

        self.run_cmd = "neofetch"
        self.generic_name = "neofetch"
        self.icon = "screengrab"
    
    def install(self):
        return self.install_package("neofetch")
    
    def uninstall(self):
        return self.remove_package("neofetch")
    
    def check_install(self):
        return self.query_package("neofetch")

    def check_windows(self):
        # welcome to the rice fields, moth******er
        return True

    def get_config_windows(self):
        # welcome to the rice fields, moth******er
        pass