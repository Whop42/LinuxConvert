from software import Software

class flameshot(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "flameshot"

        self.run_cmd = "flameshot gui"
        self.generic_name = "screenshot"
        self.icon = "screengrab"
    
    def install(self):
        print(self.install_package("flameshot"))
    
    def uninstall(self):
        print(self.remove_package("flameshot"))
    
    def check_install(self):
        return self.query_package("flameshot")