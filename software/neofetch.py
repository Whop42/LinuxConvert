from software import Software

class neofetch(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "neofetch"

        self.run_cmd = "neofetch"
        self.generic_name = "screenfetch"
        self.icon = "screengrab"
    
    def install(self):
        print(self.install_package("neofetch"))
    
    def uninstall(self):
        print(self.remove_package("neofetch"))
    
    def check_install(self):
        return self.query_package("neofetch")