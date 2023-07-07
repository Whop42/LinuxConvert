from linuxconvert.software import Software

class gimp(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "gimp"

        self.run_cmd = "/usr/bin/gimp"
        self.generic_name = "gimp"
        self.icon = "gimp"
    
    def install(self):
        return self.install_package("gimp")
    
    def uninstall(self):
        return self.remove_package("gimp")
    
    def check_install(self):
        return self.query_package("gimp")

    def check_windows(self):
        return True

    def get_config_windows(self):
        pass