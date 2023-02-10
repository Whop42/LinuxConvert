from software import Software

class okular(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "okular"

        self.run_cmd = "/usr/bin/okular"
        self.generic_name = "pdf reader"
        self.icon = "okular"
    
    def install(self):
        return self.install_package("okular")
    
    def uninstall(self):
        return self.remove_package("okular")
    
    def check_install(self):
        return self.query_package("okular")

    def check_windows(self):
        return True

    def get_config_windows(self):
        pass